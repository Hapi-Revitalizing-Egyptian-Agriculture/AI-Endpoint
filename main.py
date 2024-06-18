from fastapi import FastAPI, File, UploadFile


from PIL import Image

from CropDisease.DiseaseDetection import load_model, predict
from CropRecommendation.CropRecommendation import get_crop_recommendation
app = FastAPI()

@app.post("/crop_disease")
def post_image(image: UploadFile = File(...),crop_name: str = None):

    img = Image.open(image.file)
    model=load_model(crop=crop_name)
    top_ps, top_classes = predict(model, img, topk=1)
    top_class = top_classes[0].split('___')
    top_p = f"{top_ps[0] * 100:.2f}%"
    print(f"plant_health: {top_class}, confidence: {top_p}")
    return {"plant_health": top_class, "confidence": top_p}

@app.post("/crop_recommendation")
def recommend_crop(n: int, p: int, k: int):
    crop_recommendation = get_crop_recommendation(n, p, k)
    return crop_recommendation