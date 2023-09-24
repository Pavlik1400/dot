import os
from typing import List


def copy(from_: str, to_: str):
    os.system(f"yes 2>/dev/null | /bin/cp -rf {from_} {to_}")


def execute(command: str):
    os.system(command)


def execute_lst(*command):
    os.system(" ".join(command))


__INSTALL_CMD = "sudo apt install"


def set_pkg_install_cmd(cmd: str):
    global __INSTALL_CMD
    __INSTALL_CMD = cmd


def install_pkg(pkg_name: str):
    execute(f"{__INSTALL_CMD} {pkg_name}")


def install_pkgs(pkg_names: List[str]):
    execute(f"{__INSTALL_CMD} {' '.join(pkg_names)}")


class _Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def print_err(msg: str):
    print(_Color.RED + _Color.BOLD + msg + _Color.END)
