import subprocess
import sys
import os

from config import *

def executeCommand(*args: str):
    if USE_SUBPROCESS:
        subprocess.run(args, env=os.environ, shell=True)
    else:
        filted_args = []

        for arg in args:
            new_arg = arg
            if (' ' in new_arg): new_arg = f"\"{new_arg}\""

            filted_args.append(new_arg)

        os.system(' '.join(filted_args))

def takeOwnershipOfDir(dir: str):
    executeCommand("icacls", dir, "/grant", f"{USERNAME}:(OI)(CI)F", "/T", "/C", "/Q")
    executeCommand("icacls", dir, "/setowner", USERNAME, "/T", "/C", "/Q")

def executePythonModuleCommand(*command: str, use_sys_executable: bool = False):
    command_list = ["python", "-m"]
    command_list.extend(command)

    if (use_sys_executable):
        command_list[0] = sys.executable

    executeCommand(*command_list)