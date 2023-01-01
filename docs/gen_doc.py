#!/usr/bin/env python3

"""Script to run Sfinx doc generation tool"""

#Imports
import os
import sys
import subprocess

def main():
    #Print script start notification
    print('Sfinx run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run dock generation command
    subprocess.check_call(
        [
            "sphinx-apidoc",
            "-e",
            "-E",
            "-M",
            "-f",
            "-o",
            "docs/src",
            "src",
        ]
    ) 

    subprocess.check_call(
        [
            "sphinx-build",
            "-T",
            #"-W",
            "-b",
            "html",
            "docs/src",
            "docs/build",
        ]
    ) 

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Sfinx run failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Sfinx run failed: {e}")
        sys.exit(100)
    else:
        print('Sfinx run finished - SUCCESS')
        