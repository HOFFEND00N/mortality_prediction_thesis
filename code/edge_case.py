import pandas as pd
import numpy as np
import os
from typing import Dict, List, Tuple, Optional, Union, Any

def generate_edge_cases(
    num_samples: int = 100,
) -> pd.DataFrame:
    edge_cases = pd.DataFrame()
    
    # edge_cases['record_id'] = [f'EDGE{i:04d}' for i in range(1, num_samples + 1)]
    # Generate extremely elderly patients (85-100 years old)
    edge_cases['age'] = np.random.uniform(85, 100, num_samples)
    edge_cases['height'] = np.random.uniform(140, 170, num_samples)  # Lower height range for elderly
    # target_bmi = np.random.uniform(30, 45, num_samples)
    
    # More severe clinical presentations (4-5)
    edge_cases['clinical_presentation'] = np.random.choice([4, 5], size=num_samples, p=[0.3, 0.7])
    
    # Very low ejection fraction (severe heart failure)
    edge_cases['ef'] = np.random.uniform(15, 30, num_samples)
    
    # High rates of comorbidities
    edge_cases['cerebrovascular_disease'] = np.random.choice([0, 1], size=num_samples, p=[0.1, 0.9])
    edge_cases['peripheral_artery_disease'] = np.random.choice([0, 1], size=num_samples, p=[0.15, 0.85])
    edge_cases['if_yes_what_type___1'] = np.random.choice([0, 1], size=num_samples, p=[0.2, 0.8])
    edge_cases['single_vessel'] = np.random.choice([0, 1], size=num_samples, p=[0.1, 0.9])
    edge_cases['calcium'] = np.random.choice([0, 1], size=num_samples, p=[0.1, 0.9])
    edge_cases['medina_side'] = np.random.choice([0, 1], size=num_samples, p=[0.2, 0.8])
    edge_cases['trifurcation'] = np.random.choice([0, 1], size=num_samples, p=[0.5, 0.5])
    
    # Higher rate of chronic total occlusion at bifurcation
    edge_cases['cto_bifurc'] = np.random.choice([0, 1], size=num_samples, p=[0.2, 0.8])

    # Almost all patients with decreased ejection fraction
    edge_cases['def'] = np.random.choice([0, 1], size=num_samples, p=[0.1, 0.9])

    # Higher rates of cancer history
    edge_cases['history_of_cancer'] = np.random.choice([0, 1], size=num_samples, p=[0.4, 0.6])

    # Almost all patients with previous interventions
    edge_cases['previous_pci'] = np.random.choice([0, 1], size=num_samples, p=[0.2, 0.8])

    # Add previous stroke or TIA (transient ischemic attack)
    edge_cases['previous_stroke_tia'] = np.random.choice([0, 1], size=num_samples, p=[0.65, 0.35])

    # Smaller side branch diameters (higher risk)
    edge_cases['side_diametr'] = np.random.uniform(1.0, 2.0, num_samples)

    # Higher rate of complex stent types
    # Calipso stent (type 3)
    edge_cases['stent_type___3'] = np.random.choice([0, 1], size=num_samples, p=[0.3, 0.7])
    # Xience stent (type 4)
    edge_cases['stent_type___4'] = np.random.choice([0, 1], size=num_samples, p=[0.3, 0.7])
    # Synergy stent (type 5)
    edge_cases['stent_type___5'] = np.random.choice([0, 1], size=num_samples, p=[0.3, 0.7])

    # Very high rate of restenosis/reocclusion (critical factor for mortality)
    edge_cases['restenosis_reocclusion'] = np.random.choice([0, 1], size=num_samples, p=[0.1, 0.9])

    # Add adhoc PCI (ad hoc percutaneous coronary intervention - emergency/unplanned procedure)
    # High rate (80%) for emergency/unplanned procedures which carry higher risk
    edge_cases['adhoc_pci'] = np.random.choice([0, 1], size=num_samples, p=[0.2, 0.8])

    # Main branch predilatation - preparation of main vessel before stenting
    # Higher rate (75%) as these are complex cases
    edge_cases['main_predilatation'] = np.random.choice([0, 1], size=num_samples, p=[0.25, 0.75])

    # Stent diameter - smaller diameters are higher risk (typically 2.0-4.0mm)
    # Using smaller diameters (2.0-2.75mm) for high-risk cases
    edge_cases['stent_diameter'] = np.random.uniform(2.0, 2.75, num_samples)

    # Stent length - longer stents are higher risk (typically 8-38mm)
    # Using longer stents (28-38mm) for high-risk cases
    edge_cases['stent_length'] = np.random.uniform(28.0, 38.0, num_samples)

    # CKD-EPI Creatinine Equation - lower values indicate worse kidney function
    # Normal: >90 ml/min/1.73m², Stage 3-5 CKD: <60 ml/min/1.73m²
    edge_cases['ckd'] = np.random.uniform(15.0, 45.0, num_samples)  # Severe kidney disease values
    
    # Creatinine - higher values indicate worse kidney function
    # Range: 10-600 μmol/L, higher values indicate kidney dysfunction
    edge_cases['creatinine'] = np.random.uniform(300.0, 600.0, num_samples)  # Severe kidney dysfunction values
    
    # Major Left Main coronary artery disease - higher prevalence in edge cases
    edge_cases['major_lm'] = np.random.choice([0, 1], size=num_samples, p=[0.2, 0.8])
    
    # Minor criteria for high-risk diagnosis - can range from 0-6 based on formula reference
    # Higher values represent higher risk patients
    edge_cases['minor_criteria'] = np.random.choice([3, 4, 5, 6], size=num_samples, p=[0.1, 0.2, 0.3, 0.4])
    
    # Side branch pre-dilatation - technique used in complex bifurcation lesions
    edge_cases['side_predilat'] = np.random.choice([0, 1], size=num_samples, p=[0.1, 0.9])
    
    # Side branch stenosis - percentage of narrowing
    # Higher values (>70%) indicate severe stenosis
    edge_cases['side_stenosis'] = np.random.uniform(75.0, 99.0, num_samples)  # Severe stenosis values
    
    # Valvular heart disease - higher prevalence in edge cases
    edge_cases['valvular_disease'] = np.random.choice([0, 1], size=num_samples, p=[0.3, 0.7])


    # Almost certain mortality (95% probability)
    edge_cases['mortality'] = np.random.choice([0, 1], size=num_samples, p=[0.05, 0.95])

    # High rates of additional comorbidities
    binary_columns = [
        # 'diabet', 'hypertension',
        'smoking', 'dyslipidemia', 
        'anemia', 'atrial_fibrilation'
    ]
    
    for col in binary_columns:
        edge_cases[col] = np.random.choice([0, 1], size=num_samples, p=[0.1, 0.9])
    
    return edge_cases

def extend_dataset_with_edge_cases(
    original_dataset_path: str,
    num_edge_cases: int = 100,
    output_path: Optional[str] = None
) -> pd.DataFrame:
    """
    Extend an existing dataset with generated edge cases.
    
    Args:
        original_dataset_path: Path to the original CSV dataset
        num_edge_cases: Number of edge cases to generate
        output_path: Optional path to save the combined dataset
        
    Returns:
        DataFrame containing the combined original and edge case data
    """
    # Load the original dataset
    original_df = pd.read_csv(original_dataset_path, sep=',')
    
    # Generate edge cases
    edge_cases = generate_edge_cases(num_samples=num_edge_cases)
    
    # Get all columns from original dataset that are missing in edge cases
    missing_cols = set(original_df.columns) - set(edge_cases.columns)
    
    # Add missing columns to edge cases with NaN values
    for col in missing_cols:
        edge_cases[col] = np.nan
    
    # Ensure edge cases DataFrame has the same column order as original
    edge_cases = edge_cases[original_df.columns]
    
    # Combine the datasets
    combined_df = pd.concat([original_df, edge_cases], ignore_index=True)
    
    # Save combined dataset if output path is provided
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        combined_df.to_csv(output_path, index=False)
        print(f"Combined dataset saved to {output_path}")
    
    return combined_df

if __name__ == "__main__":
    # Example usage
    # 1. Generate standalone edge cases
    edge_df = generate_edge_cases(
        num_samples=50, 
        save_path='logs/edge_cases.csv'
    )
    
    # 2. Extend original dataset with edge cases
    # extended_df = extend_dataset_with_edge_cases(
    #     original_dataset_path='InternationalBifurca_DATA_2025-04-20_0932.csv',
    #     num_edge_cases=50,
    #     output_path='InternationalBifurca_DATA_extended.csv'
    # )







# BEFORE:

#     import pandas as pd
# import numpy as np
# import os
# from typing import Dict, List, Tuple, Optional, Union, Any

# def generate_edge_cases(
#     num_samples: int = 100,
# ) -> pd.DataFrame:
#     edge_cases = pd.DataFrame()
    
#     # edge_cases['record_id'] = [f'EDGE{i:04d}' for i in range(1, num_samples + 1)]
#     edge_cases['age'] = np.random.uniform(80, 100, num_samples)
#     edge_cases['height'] = np.random.uniform(140, 190, num_samples)
#     # target_bmi = np.random.uniform(30, 45, num_samples)
#     edge_cases['clinical_presentation'] = np.random.choice([1, 2, 3, 4, 5], size=num_samples)
#     edge_cases['ef'] = np.random.uniform(30, 50, num_samples)
#     edge_cases['cerebrovascular_disease'] = np.random.choice([0, 1], size=num_samples, p=[0.4, 0.6])
#     edge_cases['peripheral_artery_disease'] = np.random.choice([0, 1], size=num_samples, p=[0.45, 0.55])
#     edge_cases['if_yes_what_type___1'] = np.random.choice([0, 1], size=num_samples, p=[0.5, 0.5])
#     edge_cases['single_vessel'] = np.random.choice([0, 1], size=num_samples, p=[0.35, 0.65])
#     edge_cases['calcium'] = np.random.choice([0, 1], size=num_samples, p=[0.3, 0.7])
#     edge_cases['medina_side'] = np.random.choice([0, 1], size=num_samples, p=[0.4, 0.6])
#     edge_cases['trifurcation'] = np.random.choice([0, 1], size=num_samples, p=[0.7, 0.3])
#     # Add chronic total occlusion bifurcation (CTO at bifurcation site)
#     edge_cases['cto_bifurc'] = np.random.choice([0, 1], size=num_samples, p=[0.6, 0.4])

#     # Add def (likely "decreased ejection fraction" complementary measurement)
#     edge_cases['def'] = np.random.choice([0, 1], size=num_samples, p=[0.5, 0.5])

#     # Add history of cancer (more common in elderly patients)
#     edge_cases['history_of_cancer'] = np.random.choice([0, 1], size=num_samples, p=[0.7, 0.3])

#     # Add previous PCI (percutaneous coronary intervention)
#     edge_cases['previous_pci'] = np.random.choice([0, 1], size=num_samples, p=[0.55, 0.45])

#     # Add previous stroke or TIA (transient ischemic attack)
#     edge_cases['previous_stroke_tia'] = np.random.choice([0, 1], size=num_samples, p=[0.65, 0.35])

#     # Add side branch diameter measurement (in mm, typically 1.5-3.5mm)
#     edge_cases['side_diametr'] = np.random.uniform(1.5, 3.5, num_samples)

#     # Add stent type 3 indicator
#     edge_cases['stent_type___3'] = np.random.choice([0, 1], size=num_samples, p=[0.7, 0.3])
#     edge_cases['restenosis_reocclusion'] = np.random.choice([0, 1], size=num_samples, p=[0.6, 0.4])

#     binary_columns = [
#         # 'diabet', 'hypertension',
#         'smoking', 'dyslipidemia', 
#         'anemia', 'atrial_fibrilation'
#     ]
    
#     for col in binary_columns:
#         edge_cases[col] = np.random.choice([0, 1], size=num_samples, p=[0.3, 0.7])
    
#     return edge_cases

# def extend_dataset_with_edge_cases(
#     original_dataset_path: str,
#     num_edge_cases: int = 100,
#     output_path: Optional[str] = None
# ) -> pd.DataFrame:
#     """
#     Extend an existing dataset with generated edge cases.
    
#     Args:
#         original_dataset_path: Path to the original CSV dataset
#         num_edge_cases: Number of edge cases to generate
#         output_path: Optional path to save the combined dataset
        
#     Returns:
#         DataFrame containing the combined original and edge case data
#     """
#     # Load the original dataset
#     original_df = pd.read_csv(original_dataset_path, sep=',')
    
#     # Generate edge cases
#     edge_cases = generate_edge_cases(num_samples=num_edge_cases)
    
#     # Get all columns from original dataset that are missing in edge cases
#     missing_cols = set(original_df.columns) - set(edge_cases.columns)
    
#     # Add missing columns to edge cases with NaN values
#     for col in missing_cols:
#         edge_cases[col] = np.nan
    
#     # Ensure edge cases DataFrame has the same column order as original
#     edge_cases = edge_cases[original_df.columns]
    
#     # Combine the datasets
#     combined_df = pd.concat([original_df, edge_cases], ignore_index=True)
    
#     # Save combined dataset if output path is provided
#     if output_path:
#         os.makedirs(os.path.dirname(output_path), exist_ok=True)
#         combined_df.to_csv(output_path, index=False)
#         print(f"Combined dataset saved to {output_path}")
    
#     return combined_df

# if __name__ == "__main__":
#     # Example usage
#     # 1. Generate standalone edge cases
#     edge_df = generate_edge_cases(
#         num_samples=50, 
#         save_path='logs/edge_cases.csv'
#     )
    
#     # 2. Extend original dataset with edge cases
#     # extended_df = extend_dataset_with_edge_cases(
#     #     original_dataset_path='InternationalBifurca_DATA_2025-04-20_0932.csv',
#     #     num_edge_cases=50,
#     #     output_path='InternationalBifurca_DATA_extended.csv'
#     # )