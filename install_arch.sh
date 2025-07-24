#!/bin/bash -ilvx

# On a new machine running live image
# 1) run `archinstall` and reboot before continuing
# 2) import $HOME/.ssh to allow git clone from private github repository.

# curl -o script.sh https://raw.githubusercontent.com/strongmove/blank-slate/main/install_arch.sh && bash script.sh


if [ ! -d "$HOME/.ssh" ]; then
  echo "Cannot continue as user $USER because $HOME/.ssh does not exist."
  echo "Parts of this setup requires accessing private Github repositories."
  echo "Please install appropriate ssh keys into $HOME/.ssh and try again."
  exit 1
fi

sudo pacman -Syu --noconfirm curl git python-pipx unzip dnsutils fish neovim chezmoi diff-so-fancy eza fzf ripgrep zoxide tmux xsel lazygit fd zk rust bat gdu bpytop ranger

git clone git@github.com:strongmove/fish "$HOME/.config/fish"

chezmoi init git@github.com:strongmove/dotfiles.git
chezmoi update

chsh -s /usr/bin/fish
/usr/bin/fish
