import os

from config import *
import commands
import yap

def enterVirtualEnv(path: str = ENV_PATH):
    if (not os.path.exists(path)):
        print("Setting Up Virtual Environment...")
        commands.executePythonModuleCommand("venv", ENV_PATH, use_sys_executable=True)

        print("Taking Ownership Of The Environment...")
        commands.takeOwnershipOfDir(ENV_PATH)

    print("Entering Virtual Environment...")

    # This section emulates the key parts of the "activate.bat" script
    os.environ['VIRTUAL_ENV'] = ENV_PATH
    os.environ['PATH'] = f"{os.environ['VIRTUAL_ENV']}\\Scripts;{os.environ['PATH']}"

    if ("PYTHONHOME" in os.environ.keys()):
        os.environ.pop("PYTHONHOME")

    print("Updating pip...")
    commands.executePythonModuleCommand("ensurepip", "--upgrade")

def main():
    enterVirtualEnv()

    yap.install("pillow")

if __name__ == '__main__':
    main()