import numpy as np


def convert_to_kg_per_ha(n_lbs_per_a, p_lbs_per_a, k_lbs_per_a):
    """
    Converts the nutrient values from lbs/acre to kg/ha.

    Args:
        n_lbs_per_a (float): Nitrogen value in lbs/acre.
        p_lbs_per_a (float): Phosphorus value in lbs/acre.
        k_lbs_per_a (float): Potassium value in lbs/acre.

    Returns:
        tuple: A tuple containing the converted nutrient values in kg/ha.
            The order of the values is (nitrogen, phosphorus, potassium).
    """
    # Conversion factors
    lb_per_acre_to_kg_per_ha = 1 / 1.121

    # Convert nitrogen (N) from lbs/acre to kg/ha
    n_kg_per_ha = n_lbs_per_a * lb_per_acre_to_kg_per_ha

    # Convert phosphorus (P) from lbs/acre to kg/ha
    p_kg_per_ha = p_lbs_per_a * lb_per_acre_to_kg_per_ha

    # Convert potassium (K) from lbs/acre to kg/ha
    k_kg_per_ha = k_lbs_per_a * lb_per_acre_to_kg_per_ha

    return n_kg_per_ha, p_kg_per_ha, k_kg_per_ha


def convert_to_mg_per_L(n_kg_per_ha, p_kg_per_ha, k_kg_per_ha):
    """
    Converts the nutrient values from kg/ha to mg/L.

    Assuming a plough depth of 20cm, the volume of the plough depth of 1 hectare is 2000m^3.
    One m^3 contains 1000 litres so plough layer is equivalent to 2 x 10^6 litres of soil.
    One Kg contains 10^6mg. Using these relationships the conversion factor is calculated.
    Nutrient present as kg/ha = 2 x nutrient present as mg/L soil.

    Args:
        n_kg_per_ha (float): Nitrogen value in kg/ha.
        p_kg_per_ha (float): Phosphorus value in kg/ha.
        k_kg_per_ha (float): Potassium value in kg/ha.

    Returns:
        tuple: A tuple containing the converted nutrient values in mg/L.
            The order of the values is (nitrogen, phosphorus, potassium).
    """
    # Convert nitrogen (N) from kg/ha to mg/L
    n_mg_per_L = n_kg_per_ha / 2

    # Convert phosphorus (P) from kg/ha to mg/L
    p_mg_per_L = p_kg_per_ha / 2

    # Convert potassium (K) from kg/ha to mg/L
    k_mg_per_L = k_kg_per_ha / 2

    return n_mg_per_L, p_mg_per_L, k_mg_per_L


def convert_from_lbs_a_to_mg_L(n_lbs_per_a, p_lbs_per_a, k_lbs_per_a):
    """
    Converts the nutrient values from lbs/acre to mg/L.

    Args:
        n_lbs_per_a (float): Nitrogen value in lbs/acre.
        p_lbs_per_a (float): Phosphorus value in lbs/acre.
        k_lbs_per_a (float): Potassium value in lbs/acre.

    Returns:
        tuple: A tuple containing the converted nutrient values in mg/L.
            The order of the values is (nitrogen, phosphorus, potassium).
    """
    # Convert lbs/acre to kg/ha
    n_kg_per_ha, p_kg_per_ha, k_kg_per_ha = convert_to_kg_per_ha(
        n_lbs_per_a, p_lbs_per_a, k_lbs_per_a
    )

    # Convert kg/ha to mg/L
    n_mg_per_L, p_mg_per_L, k_mg_per_L = convert_to_mg_per_L(
        n_kg_per_ha, p_kg_per_ha, k_kg_per_ha
    )

    return [round(n_mg_per_L), round(p_mg_per_L), round(k_mg_per_L)]
