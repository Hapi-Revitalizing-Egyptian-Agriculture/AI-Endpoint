from fastapi import FastAPI, File, UploadFile

import torch
import torchvision.models as models


from PIL import Image
import numpy as np

import os

def load_model(crop, directory="./CropDisease/models"):
    """
    Loads the model from checkpoint and reconstructs it.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    filename = f"checkpoint-{crop}.pth"
    filepath = os.path.join(directory, filename)
    checkpoint = torch.load(filepath, map_location=device)
    model = models.resnet34(pretrained=True)
    # freeze model parameters
    for param in model.parameters():
        param.requires_grad = False

    model.fc = checkpoint["fc"]
    model.load_state_dict(checkpoint["state_dict"])
    model.class_to_idx = checkpoint["class_to_idx"]

    model=model.to(device)
    return model

def load_models(directory="./CropDisease/models", crop_names=["wheat", "corn", "tomato", "potato", "apple", "sugarcane", "cotton"]):
    """
    Loads models from a directory, filtering by crop names included in the filename.
    Returns a dictionary with crop names as keys and the loaded models as values.
    """
    loaded_models = {}
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    for crop_name in crop_names:
        for filename in os.listdir(directory):
            if crop_name in filename and filename.endswith('.pth'):
                filepath = os.path.join(directory, filename)
                checkpoint = torch.load(filepath, map_location=device)
                model = models.resnet34(pretrained=True)
                # freeze model parameters
                for param in model.parameters():
                    param.requires_grad = False

                model.fc = checkpoint["fc"]
                model.load_state_dict(checkpoint["state_dict"])
                model.class_to_idx = checkpoint["class_to_idx"]
                model = model.to(device)
                loaded_models[crop_name] = model
                break  # Assumes only one model per crop name
    
    return loaded_models

def process_image(image):
    """Scales, crops, and normalizes a PIL image for a PyTorch model,
    returns a Numpy array.
    """

    #image = Image.open(image_path)

    width, height = image.size
    aspect_ratio = width / height
    if aspect_ratio > 1:
        image = image.resize((round(aspect_ratio * 224), 224))
    else:
        image = image.resize((224, round(224 / aspect_ratio)))

    width, height = image.size
    new_wh = 224

    left = (width - new_wh) / 2
    top = (height - new_wh) / 2
    right = (width + new_wh) / 2
    bottom = (height + new_wh) / 2

    image = image.crop((round(left), round(top), round(right), round(bottom)))

    # Convert to numpy array and color channels to 0-1
    np_image = np.array(image) / 255

    # Normalize the image
    np_image = (np_image - np.array([0.485, 0.456, 0.406])) / np.array(
        [0.229, 0.224, 0.225]
    )

    # Reorder dimensions
    np_image = np_image.transpose((2, 0, 1))

    return np_image

def predict(
    model,
    image,
    topk=5,
):
    """
    Returns a prediction of top k classes.
    """
    image = process_image(image)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    image_tensor = torch.from_numpy(image).type(torch.FloatTensor)

    image_tensor = image_tensor.unsqueeze(0).to(device)

    model.to(device)
    model.eval()

    with torch.no_grad():
        output = model(image_tensor)
        ps = torch.exp(output)

    idx_to_class = {v: k for k, v in model.class_to_idx.items()}

    top_ps, top_idxs = ps.topk(topk, dim=1)
    top_classes = [idx_to_class[idx] for idx in top_idxs[0].cpu().numpy()]

    return top_ps[0].cpu().numpy().tolist(), top_classes