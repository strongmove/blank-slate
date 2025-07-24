#!/bin/bash -ilvx

# wget -O a.sh https://raw.githubusercontent.com/strongmove/blank-slate/main/install_arch.sh && bash a.sh

sudo pacman -Syu --noconfirm curl git python-pipx unzip dnsutils fish chezmoi diff-so-fancy eza fzf ripgrep zoxide tmux xsel lazygit fd zk rust bat gdu bpytop ranger

git clone git@github.com:strongmove/fish "$HOME/.config/fish"

chsh -s /usr/bin/fish

chezmoi init git@github.com:strongmove/dotfiles.git
chezmoi update
/usr/bin/fish
