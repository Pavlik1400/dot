setopt PROMPT_CR
setopt PROMPT_SP
export PROMPT_EOL_MARK=""
# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

#ZSH_THEME="robbyrussell"
ZSH_THEME="powerlevel10k/powerlevel10k"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to change how often to auto-update (in days).
zstyle ':omz:update' frequency 1

plugins=(git zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# General
alias mkd="mkdir -pv"
alias v="vim"
alias c="clear"
alias q="exit"
alias ls="exa"
alias lh="ls -lh"
alias ll="ls -la"
alias la="ls -a"
alias diffc="colordiff"

# System management
alias s="systemctl"
alias SS="sudo systemctl"
alias j="journalctl"
alias jecb="journalctl -b -p err..crit"

# Arch linux related
alias sps="sudo pacman -S"
alias sp="sudo pacman"

alias vscode=/home/pasha/scripts/launch-vs-code
# Ubuntu related
#alias upd="sudo apt update && sudo apt upgrade"
#alias inst="sudo apt install"
#alias rem="sudo apt remove"
#alias purge="sudo apt purge"

# Synching
alias Allup="rclone sync ~/Documents/brain2/All/ gdrive:sync/All/"
alias Alldown="rclone sync gdrive:sync/All/ ~/Documents/brain2/All/"
alias docsup="rclone sync /home/pasha/docs/ gdrive:docs/"
alias docsdown="rclone sync gdrive:docs/ /home/pasha/docs/"

# Python
alias aconda="source /home/pasha/aconda.sh"
alias acconda="aconda; conda activate "
alias dconda="conda deactivate"

# Other 
alias add-key="source ~/scripts/start-ssh-agent.sh && ssh-add"
alias pctl="powerprofilesctl"
alias matlab="/home/pasha/Documents/diploma/matlab/bin/matlab"

# This is added to fix tilix problems
#if [ $TILIX_ID ] || [ $VTE_VERSION ]; then
	#source /etc/profile.d/vte.sh
#fi

# other exports
export EDITOR="vim"
# fix display autocomplete bug in zsh
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export PATH="$PATH:/home/pasha/.local/bin/"
export PATH="$PATH:/home/pasha/.local/share/gem/ruby/3.0.0/bin"
export PATH="$PATH:/home/pasha/Documents/diploma/riscv64-unknown-elf-gcc-10.1.0-2020.08.2-x86_64-linux-ubuntu14/bin"
export PATH="$PATH:/home/pasha/.cargo/bin"
# export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/home/pasha/Documents/diploma/matlab/bin/glnxa64"

# seed up press and hold action of all keys
# xset r rate 300 50

# remove auto correct feature
unsetopt correct

# Ctrl + backspace Removes the whole word
bindkey '^H' backward-kill-word
bindkey '5~' kill-word
export QT_STYLE_OVERRIDE=kvantum
#export QT_QPA_PLATFORMTHEME=qt6ct
#export QT_QPA_PLATFORMTHEME=qt5ct
#export QT_QPA_PLATFORM=wayland
export GDK_BACKEND=wayland
export QT_QPA_PLATFORM="wayland"
export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
#export QT_QPA_PLATFORMTHEME="qt5ct"
