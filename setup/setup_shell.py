# from setup.utils import *
# from setup.constants import *
from utils import *
from constants import *
import os
from typing import Dict


def main(config: Dict):
    if not os.path.exists("dotfiles"):
        print("Error: Run this script from project root directory")
        exit(1)
        
    # oh my zsh
    oh_my_zsh_path = "$HOME/.oh-my-zsh"
    if os.path.exists(oh_my_zsh_path):
        execute(f"rm -rf {oh_my_zsh_path}")
    execute(f'CHSH=yes RUNZSH=no sh -c "$(wget {OH_MY_ZSH_LINK} -O -)"')

    # syntax highlighting
    syntax_highligting_path = "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
    if os.path.exists(syntax_highligting_path):
        execute(f"rm -rf {syntax_highligting_path}")
    execute(
        f"git clone {OH_MY_ZSH_SYNTAX_HIGHLIGHTING} {syntax_highligting_path}"
    )

    # power 10l
    power10k_install_path = "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
    if os.path.exists(power10k_install_path):
        execute(f"rm -rf {power10k_install_path}")
    execute(
        f"git clone --depth=1 {POWER_10_K_LINK} {power10k_install_path}"
    )

    # copy config files
    copy("dotfiles/.zshrc","$HOME")
    copy("dotfiles/.p10k.zsh","$HOME")
    copy("dotfiles/.vimrc","$HOME")

    # VIM
    copy("dotfiles/.vim", "$HOME")
    execute("vim +'PlugInstall --sync' +qa")

    pass


if __name__ == "__main__":
    main({})
