import os
import subprocess
mof = ""
pressure = "15"
temp = "293.15"
gas = "O2"
base_input = "00base_template.input"
CUTOFFVDW = "14.0"
CUTOFFCHARGECHARGE = "14.0"
CUTOFFCHARGEBONDDIPOLE = "14.0"
CUTOFFBONDDIPOLEBONDDIPOLE = "14.0"

NumberOfCycles = "20000"
NumberOfInitializationCycles = "10000"
PrintEvery = "5000"


cif_list_path = "04cif_list.txt"
with open(cif_list_path, "r") as file:
    cif_list = [line.strip() for line in file if line.strip()]
    # Execute the simulation script for each CIF
    for mof in cif_list:
        print(mof)
        try:
            print(f"Executing simulation for CIF: {mof}")
            subprocess.run(["python", "01make_simulation.py",
                            "--mof", mof,
                            "--pressure" ,pressure,
                            "--temp" ,temp,
                            "--gas" ,gas,
                            "--base_input" ,base_input,
                            "--cutoffvdw" ,CUTOFFVDW , 
                            "--cutoffchargecharge" ,CUTOFFCHARGECHARGE , 
                            "--cutoffchargebonddipole" ,CUTOFFCHARGEBONDDIPOLE , 
                            "--cutoffbonddipolebonddipole" ,CUTOFFBONDDIPOLEBONDDIPOLE , 
                            "--NumberOfCycles" ,NumberOfCycles,
                            "--NumberOfInitializationCycles" ,NumberOfInitializationCycles,
                            "--PrintEvery" ,PrintEvery,
                            ], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while executing simulation for {mof}: {e}")
        except Exception as e:
            print(f"Unexpected error for {mof}: {e}")


