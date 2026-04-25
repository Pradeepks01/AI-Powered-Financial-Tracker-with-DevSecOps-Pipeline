import os
import glob

workflow_dir = r"c:\Users\Pradeep\Desktop\finacial tracker\.github\workflows"
files = glob.glob(os.path.join(workflow_dir, "*.yml"))

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    skip = False
    for line in lines:
        if line.startswith("<<<<<<< Updated upstream"):
            skip = True
            continue
        if line.startswith("======="):
            skip = False
            continue
        if line.startswith(">>>>>>> Stashed changes"):
            continue
            
        if not skip:
            new_lines.append(line)
            
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

print("Conflicts resolved.")
