#!/bin/bash -ilvx
set -e

# On a new machine running live image
# 1) run `archinstall` and reboot before continuing
# 2) import $HOME/.ssh to allow git clone from private github repository.

# curl -o script.sh https://raw.githubusercontent.com/strongmove/blank-slate/main/arch.sh?v=1 && bash script.sh

# Ensure SSH keys are present for private repo access
if [ ! -d "$HOME/.ssh" ]; then
  echo "$HOME/.ssh does not exist."
  read -rp "Enter SCP source for your .ssh directory (e.g., u@mainstay.home): " scp_source
  if scp -r "$scp_source:~/.ssh" "$HOME/"; then
    echo "Successfully copied .ssh directory from $scp_source."
  else
    echo "Failed to copy .ssh directory from $scp_source."
    echo "Parts of this setup require accessing private Github repositories."
    echo "Please install appropriate ssh keys into $HOME/.ssh and try again."
    exit 1
  fi
fi

# Install essential packages
sudo pacman -Syu --noconfirm \
  base-devel bat bpytop chezmoi curl \
  diff-so-fancy dnsutils eza fd fish \
  fzf gdu git git-delta go \
  lazygit neovim openssl python-pipx ranger \
  ripgrep rust tk tmux unzip \
  wget which xorg-xauth xsel xz \
  zk zlib zoxide

# Install yay (AUR helper)
if ! command -v yay &>/dev/null; then
  sudo pacman -S --needed git base-devel
  git clone https://aur.archlinux.org/yay.git /tmp/yay
  cd /tmp/yay || exit 1
  makepkg -si --noconfirm
  cd ~ || exit 1
  rm -rf /tmp/yay
fi

# Install pyenv and Python 3.12
if ! command -v pyenv &>/dev/null; then
  curl https://pyenv.run | bash
fi

# Add pyenv to PATH for this session
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Install Python 3.12
pyenv install 3.12
pyenv global 3.12

# Clone fish config
git clone git@github.com:strongmove/fish "$HOME/.config/fish"

# Initialize and update dotfiles with chezmoi
chezmoi init git@github.com:strongmove/dotfiles.git
chezmoi update

# Set fish as default shell and start it
chsh -s /usr/bin/fish
exec /usr/bin/fish
