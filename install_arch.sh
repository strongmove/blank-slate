#!/bin/bash -ilvx

# On a new machine running live image
# 1) run `archinstall` and reboot before continuing
# 2) import $HOME/.ssh to allow git clone from private github repository.


# curl -o script.sh https://raw.githubusercontent.com/strongmove/blank-slate/main/install_arch.sh && bash script.sh

# sudo pacman -Syu --noconfirm curl git python-pipx unzip dnsutils fish chezmoi diff-so-fancy eza fzf ripgrep zoxide tmux xsel lazygit fd zk rust bat gdu bpytop ranger

# git clone git@github.com:strongmove/fish "$HOME/.config/fish"

#chezmoi init git@github.com:strongmove/dotfiles.git
#chezmoi update

chsh -s /usr/bin/fish
/usr/bin/fish
