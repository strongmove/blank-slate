#!/bin/bash -ilvx

# wget -O /tmp/blank-slate.sh https://raw.githubusercontent.com/strongmove/blank-slate/main/install.sh && bash /tmp/blank-slate.sh

sudo apt update -y
sudo apt install curl build-essential git python3-pip -y
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
(
	echo
	echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"'
) >>$HOME/.bashrc
source ~/.bashrc

brew install fish

# # Essentials
/home/linuxbrew/.linuxbrew/bin/brew install fish
# # Extras
# /home/linuxbrew/.linuxbrew/bin/brew install eza fzf ripgrep zoxide tmux xsel lazygit
# /home/linuxbrew/.linuxbrew/bin/brew install zk rust bat gdu bpytop ranger
# # Setup fish as default shell
# grep -qF fish /etc/shells || command -v fish | sudo tee -a  /etc/shells
# # command -v fish | sudo tee -a /etc/shells
# chsh -s "$(command -v fish)"
#
# /home/linuxbrew/.linuxbrew/bin/chezmoi init git@github.com:strongmove/dotfiles.git
# /home/linuxbrew/.linuxbrew/bin/chezmoi update
# /home/linuxbrew/.linuxbrew/bin/fish
