import subprocess 
import os
import shutil

def oxpsConverter(input_path, output_path=None):
    if not os.path.exists(input_path):
        print(f"Error: Could not find {input_path}")
        return
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".pdf"

    executable = "gxpswin64" 
    

    if shutil.which(executable) is None:
        print(f"Error: '{executable}' not found. Is GhostXPS installed and in your PATH?")
        return


    arguments = [
        executable,
        "-sDEVICE=pdfwrite",
        "-o", output_path,
         input_path
    ]
    print(f"Converting {input_path}...")

    try:
        result = subprocess.run(arguments, capture_output=True, text=True, shell=True)
        
        if result.returncode == 0:
            return True, output_path
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)
