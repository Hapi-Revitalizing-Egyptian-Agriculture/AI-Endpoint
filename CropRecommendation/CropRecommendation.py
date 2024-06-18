# Importing functions and data from other files
from .CalculateRatios import calculate_ratio
from .CropsData import crop_ratios

# Initialization of global variables (mg/kg)
n_value = 18
p_value = 80
k_value = 18


# Function to get the crop recommendation
def get_crop_recommendation(n, p, k):
    """
    Get crop recommendations based on the given nutrient values.

    Args:
        n (int): The nitrogen value.
        p (int): The phosphorus value.
        k (int): The potassium value.

    Returns:
        dict: A dictionary containing the recommended crops and their corresponding scores.
    """

    optimals = {}
    land_ratio = calculate_ratio(n, p, k)
    print(f"Land Ratios: {land_ratio}")
    for crop, ratio in crop_ratios.items():
        print(f"Checking for {crop}")
        print(f"Crop Ratios: {ratio}")
        optimals[crop] = abs(
            3
            - (
                land_ratio[0] / ratio[0]
                + land_ratio[1] / ratio[1]
                + land_ratio[2] / ratio[2]
            )
        )
    sorted_optimals = sorted(optimals.items(), key=lambda x: x[1])
    sorted_optimals = dict(sorted_optimals)
    return sorted_optimals


optimals = get_crop_recommendation(n_value, p_value, k_value)
print(optimals)