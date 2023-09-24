from setup.utils import *
from setup.constants import *
from typing import Dict

def main(config: Dict):
    if not os.path.exists("dotfiles"):
        print("Error: Run this script from project root directory")
        exit(1)
    if not config[ConfigKeys.INSTALL_CONFIGS]:
        return
    
    # regular configs
    copy("dotfiles/.config", "$HOME/.config")
    
    # icons and cursor
    execute("tar -zxvf dotfiles/icons/Tela-circle-black.tar.xz")
    execute("tar -zxvf dotfiles/icons/GoogleDot-Black.tar.gz")
    execute("mkdir -p $HOME/.icons")
    copy("GoogleDot-Black", "$HOME/.icons")
    copy("Tela-circle-black", "$HOME/.icons")
    execute("rm -rf GoogleDot-Black")
    execute("rm -rf Tela-circle-black")
    
    # fonts
    copy("dotfiles/fonts/*", "~/.local/share/fonts")
    
    # GNOME settings
    execute("dconf load / < dotfiles/dconf-settings.ini")
    