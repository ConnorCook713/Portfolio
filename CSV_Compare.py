import pandas as pd
import numpy as np

username = "Insert username for file path"

# Paths to CSV files
AV_Path = f"C:\\Users\\{username}\\Documents\\potter_data\\AV.csv"
RMM_Path = f"C:\\Users\\{username}\\Documents\\potter_data\\RMM.csv"
AD_Path = f"C:\\Users\\{username}\\Documents\\potter_data\\computerlastlogon.csv"

def compare_csv(AV_file: str, RMM_file: str, AD_file: str):

    try:
        AV_df = pd.read_csv(AV_file)
        RMM_df = pd.read_csv(RMM_file)
        AD_df = pd.read_csv(AD_file)

        # Extract device names (assuming column is "Device Name" or similar)
        # ADjust column name if needed - could be "Name", "Device Name", etc.
        AV_devices = set(AV_df.iloc[:, 0].dropna().astype(str).str.strip().str.upper())
        RMM_devices = set(RMM_df.iloc[:, 0].dropna().astype(str).str.strip().str.upper())
        AD_devices = set(AD_df.iloc[:, 0].dropna().astype(str).str.strip().str.upper())

        # Two-system comparisons
        in_both_systems = AV_devices & RMM_devices
        AV_only = AV_devices - RMM_devices
        RMM_only = RMM_devices - AV_devices
        
        # Active Directory comparisons
        AD_only = AD_devices - AV_devices - RMM_devices
        
        # Three-system comparisons
        in_all_three = AV_devices & RMM_devices & AD_devices

        path = f"C:\\Users\\{username}\\Documents\\data\\"

        print("\n=== CSV FILES CREATED ===")
        
        # Two-system outputs
        pd.DataFrame(list(in_both_systems), columns=["Device Name"]).to_csv(path + "in_both_systems.csv", index=False)
        print("--- in_both_systems.csv ---")
        
        pd.DataFrame(list(AV_only), columns=["Device Name"]).to_csv(path + "AV_only.csv", index=False)
        print("--- AV_only.csv ---")
        
        pd.DataFrame(list(RMM_only), columns=["Device Name"]).to_csv(path + "RMM_only.csv", index=False)
        print("--- RMM_only.csv ---")
        
        # Active Directory outputs
        pd.DataFrame(list(AD_only), columns=["Device Name"]).to_csv(path + "AD_only.csv", index=False)
        print("--- AD_only.csv ---")
        
        # Three-system outputs
        pd.DataFrame(list(in_all_three), columns=["Device Name"]).to_csv(path + "in_all_three_systems.csv", index=False)
        print("--- in_all_three_systems.csv ---")
        
        # Summary statistics
        print(f"\n=== SUMMARY ===")
        print(f"AV devices: {len(AV_devices)}")
        print(f"RMM devices: {len(RMM_devices)}")
        print(f"AD devices: {len(AD_devices)}")
        print(f"In all three systems: {len(in_all_three)}")
        print(f"AV only: {len(AV_only)}")
        print(f"RMM only: {len(RMM_only)}")
        print(f"AD only: {len(AD_only)}")

    except Exception as e:
        print("AN ERROR HAS OCCURRED:", e)

# Run comparison
compare_csv(AV_Path, RMM_Path, AD_Path)

    