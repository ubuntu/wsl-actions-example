import platform
import os


def IsWSL() -> bool:
    """
    This function returns true if the current machine is running on WSL.
    """
    if platform.system() != "Linux":
        return False
    if os.path.isfile("/proc/sys/fs/binfmt_misc/WSLInterop"):
        return True
    if os.path.isfile("/run/WSL"):
        return True
    return False
