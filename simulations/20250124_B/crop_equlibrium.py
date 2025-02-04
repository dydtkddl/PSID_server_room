import os
import shutil 

dirs = [x for x in os.listdir("./") if os.path.isdir(x) == True]
dest_path = os.path.join(os.environ["RASPA_DIR"] , "share", "raspa", "structures", "cif")
cifnames = []
for dir in dirs :
    path = "/Movies/System_0/Framework_0_final_1_1_1_P1.cif"
    try:
        path = dir + path 
        print(path)
        cifname = dir.replace("/", "").replace(".", "_") + ".cif"
        cifnames.append(cifname)
        shutil.copy(path, os.path.join(path , os.path.join(dest_path, cifname)    ))
    except:
	print(path, "fail")
with open("charge_equilibrium_cif_names.txt", "w") as f:
    f.write('\n'.join(cifnames).strip())
