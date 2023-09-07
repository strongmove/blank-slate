#!/bin/bash -ilvx

# wget -O /tmp/blank-slate.sh https://raw.githubusercontent.com/strongmove/blank-slate/main/install.sh && bash /tmp/blank-slate.sh

sudo apt update -y
sudo apt install curl build-essential git -y
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
(echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> $HOME/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
source ~/.bashrc

# Essentials
/home/linuxbrew/.linuxbrew/bin/brew install fish chezmoi diff-so-fancy
# Extras
# /home/linuxbrew/.linuxbrew/bin/brew install exa fzf ripgrep zoxide tmux xsel lazygit zk
# Setup fish as default shell
command -v fish | sudo tee -a /etc/shells
chsh -s "$(command -v fish)"

/home/linuxbrew/.linuxbrew/bin/chezmoi init git@github.com:strongmove/dotfiles.git
/home/linuxbrew/.linuxbrew/bin/chezmoi update
/home/linuxbrew/.linuxbrew/bin/fish
