# Importing functions and data from other files
from CalculateRatios import calculate_ratio
from CropsData import crop_ratios, crop_nutrients_mg_L

# Initialization of global variables (mg/kg)
n_value = 31
p_value = 8
k_value = 18


# Function to get the crop recommendation
def get_crop_recommendation(n, p, k):
    """
    Get crop recommendations based on the given nutrient values, using the Manhattan distance.
    If a negative value is encountered, the corresponding crop's score is set to infinity.

    Args:
        n (float): The nitrogen value.
        p (float): The phosphorus value.
        k (float): The potassium value.

    Returns:
        dict: A dictionary containing the recommended crops and their corresponding scores.
    """

    optimals = {}
    land_nutrients = [n, p, k]
    print(f"Land nutrients: {land_nutrients}")
    for crop, nutrients in crop_nutrients_mg_L.items():
        print(f"Checking for {crop}")
        print(f"Crop nutrients: {nutrients}")
        # Calculate the individual differences for each nutrient
        differences = [
            nutrients[0] - land_nutrients[0],
            nutrients[1] - land_nutrients[1],
            nutrients[2] - land_nutrients[2]
        ]

        # Check if any of the nutrient differences are less than 0
        negatives = [diff for diff in differences if diff < -10] # Ten degrees of error
        if negatives:
            print(f"Negative value encountered for {crop}, specifically: {negatives}")
            optimals[crop] = float("inf")
        else:
            optimals[crop] = sum(abs(diff) for diff in differences)

    sorted_optimals = sorted(optimals.items(), key=lambda x: x[1])
    sorted_optimals = dict(sorted_optimals)
    return sorted_optimals

optimals = get_crop_recommendation(n_value, p_value, k_value)
print(optimals)
