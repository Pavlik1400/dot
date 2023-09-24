from setup.setup_shell import main as setup_shell
from setup.install_packages import main as install_packages
from setup.install_configs import main as install_configs

from argparse import ArgumentParser
import json


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--config", "-c", required=True, type=str)
    args = parser.parse_args()

    with open(args.config) as f:
        config = json.load(f)
    install_packages(config)
    setup_shell(config)
    install_configs(config)
    
