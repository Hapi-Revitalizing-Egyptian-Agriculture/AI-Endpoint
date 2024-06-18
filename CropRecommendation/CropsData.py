from .CalculateRatios import calculate_ratio
from . import UnitConversion as uc

crop_nutrients_lbs_a = {
    "wheat": [70, 20, 25],
    "corn": [150, 40, 40],
    "tomato": [120, 40, 160],
    "potato": [90, 48, 158],
    "apple": [30, 10, 45],
    "sugarcane": [40, 180, 40],
    "cotton": [63, 25, 31],
}

crop_ratios = {}
crop_nutrients_mg_L = {}

# Convert the nutrient values from lbs/acre to mg/L
for crop, nutrients in crop_nutrients_lbs_a.items():
    n_lbs_per_a, p_lbs_per_a, k_lbs_per_a = nutrients
    n_mg_per_L, p_mg_per_L, k_mg_per_L = uc.convert_from_lbs_a_to_mg_L(
        n_lbs_per_a, p_lbs_per_a, k_lbs_per_a
    )
    crop_nutrients_mg_L[crop] = [n_mg_per_L, p_mg_per_L, k_mg_per_L]

print(crop_nutrients_mg_L)

# Calculate the ratio of nutrients for each crop
for crop, nutrients in crop_nutrients_mg_L.items():
    n_mg_per_L, p_mg_per_L, k_mg_per_L = nutrients
    print(f"Calculating ratio for {crop}")
    print(f"N: {n_mg_per_L}, P: {p_mg_per_L}, K: {k_mg_per_L}")
    crop_ratios[crop] = calculate_ratio(n_mg_per_L, p_mg_per_L, k_mg_per_L)

print(crop_ratios)
