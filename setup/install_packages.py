import json
from setup.constants import ConfigKeys
from setup.utils import *
from argparse import ArgumentParser
from typing import Dict


def _install_flatpak_packages(config: Dict):
    if not config[ConfigKeys.DO_INSTALL]:
        return
    set_pkg_install_cmd(config[ConfigKeys.INSTALL_CMD])
    install_pkgs(config[ConfigKeys.PKGS])


def _install_packages_from_other_repositories(config: Dict):
    if not config[ConfigKeys.DO_INSTALL]:
        return
    execute_lst(config["add_repository_cmd"], config["repository"])
    set_pkg_install_cmd(config[ConfigKeys.INSTALL_CMD])
    install_pkgs(config[ConfigKeys.PKGS])


def install_special_packages(config: Dict):
    if not config["install_special_packages"]:
        return
    special_packages_map = {
        "apt_from_other_repository": _install_packages_from_other_repositories,
        "flatpak_packages": _install_flatpak_packages,
    }
    for special_pkgs in config[ConfigKeys.SPECIAL_PKGS]:
        metadata = special_pkgs[ConfigKeys.METADATA]
        if metadata not in special_packages_map:
            print_err(f"Can't find special packages type with name {metadata}. Skip")
        special_packages_map[metadata](special_pkgs)


def install_gui_packages(config: Dict):
    if not config["install_gui_packages"]:
        return
    set_pkg_install_cmd(config[ConfigKeys.INSTALL_CMD])
    install_pkgs(config[ConfigKeys.GUI_PKGS])


def install_terminal_packages(config: Dict):
    if not config["install_terminal_packages"]:
        return
    set_pkg_install_cmd(config[ConfigKeys.INSTALL_CMD])
    install_pkgs(config[ConfigKeys.TERMINAL_PKGS])


def main(config: Dict):
    install_terminal_packages(config)
    install_gui_packages(config)
    install_special_packages(config)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--config", "-c", required=True, type=str)
    args = parser.parse_args()

    with open(args.config) as f:
        config = json.load(f)
    main(config)
