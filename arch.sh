#!/bin/bash -ilvx

# On a new machine running live image
# 1) run `archinstall` and reboot before continuing
# 2) import $HOME/.ssh to allow git clone from private github repository.

# curl -o script.sh https://raw.githubusercontent.com/strongmove/blank-slate/main/arch.sh && bash script.sh

# Ensure SSH keys are present for private repo access
if [ ! -d "$HOME/.ssh" ]; then
  echo "Cannot continue as user $USER because $HOME/.ssh does not exist."
  echo "Parts of this setup require accessing private Github repositories."
  echo "Please install appropriate ssh keys into $HOME/.ssh and try again."
  exit 1
fi

# Install essential packages
sudo pacman -Syu --noconfirm \
  curl wget which git git-delta python-pipx unzip dnsutils fish neovim xorg-xauth \
  chezmoi diff-so-fancy eza fzf ripgrep zoxide tmux xsel lazygit fd zk rust bat \
  gdu bpytop ranger go

# Install yay (AUR helper)
if ! command -v yay &>/dev/null; then
  sudo pacman -S --needed git base-devel
  git clone https://aur.archlinux.org/yay.git /tmp/yay
  cd /tmp/yay || exit 1
  makepkg -si --noconfirm
  cd ~ || exit 1
  rm -rf /tmp/yay
fi

# Optionally install Python 3.12 from AUR
read -rp "Do you want to install python312 from AUR? [y/N]: " install_py
if [[ "$install_py" =~ ^[Yy]$ ]]; then
  yay -S --noconfirm python312
fi

# Clone fish config
git clone git@github.com:strongmove/fish "$HOME/.config/fish"

# Initialize and update dotfiles with chezmoi
chezmoi init git@github.com:strongmove/dotfiles.git
chezmoi update

# Set fish as default shell and start it
chsh -s /usr/bin/fish
exec /usr/bin/fish
