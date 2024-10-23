# exe 파일 생성 코드
import subprocess
import sys

def create_executable(script_name):
    """Create an executable from a Python script using PyInstaller."""
    try:
        # Ensure PyInstaller is installed
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

        # Create the executable
        subprocess.check_call([sys.executable, "-m", "pyinstaller", "--onefile", script_name])
        
        print(f"Executable created successfully from {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Replace 'tax_reduction_calculator.py' with the name of your Python script
    script_name = 'tax_reduction_calculator.py'
    create_executable(script_name)
