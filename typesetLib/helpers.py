
import traceback
import subprocess
import shlex
def exec_cmd(command, silent=False):
    try:
        if silent:
            subprocess.check_call(shlex.split(command), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        else:
            subprocess.check_call(shlex.split(command))
    except:
        print(f"issue with cmd\n\t${command}")
        print(traceback.format_exc())