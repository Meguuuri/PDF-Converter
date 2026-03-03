import subprocess 
import os
import shutil

def oxpsConverter(input_path, output_path=None):
    #1. Check if Path Exists 
    if not os.path.exists(input_path):
        print(f"Error: Could not find {input_path}")
        return

    # 2. Setup Output Name: If no name provided, use the same name as input
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".pdf"

    # 3. Identify the command
    # On Windows, this is usually 'gxpswin64' or 'gxpswin32'
    # On Linux/Mac, it is usually just 'gxps'
    executable = "gxpswin64" 
    
    # Optional: Check if the executable is actually installed
    if shutil.which(executable) is None:
        print(f"Error: '{executable}' not found. Is GhostXPS installed and in your PATH?")
        return

    # 4. The Conversion Command
    # -sDEVICE=pdfwrite tells it we want a PDF
    # -o is the output flag
    arguments = [
        executable,
        "-sDEVICE=pdfwrite",
        "-o", output_path,
         input_path
    ]
    print(f"Converting {input_path}...")

    try:
        # Run the command and capture any errors
        subprocess.run(arguments, check=True, capture_output=True, text=True)
        print(f"✅ Success! Created: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Conversion failed. Error message:\n{e.stderr}")

# --- Test it out ---
if __name__ == "__main__":
    oxpsConverter("CS 2613 QUIZ 1.oxps")