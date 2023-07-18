#!/bin/bash -i

# wget -O /tmp/blank-slate.sh https://raw.githubusercontent.com/strongmove/blank-slate/main/install.sh && bash /tmp/blank-slate.sh

sudo apt update -y
sudo apt install curl build-essential git -y
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
(echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> $HOME/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
source ~/.bashrc

/home/linuxbrew/.linuxbrew/bin/brew install fish chezmoi diff-so-fancy
command -v fish | sudo tee -a /etc/shells
chsh -s "$(command -v fish)"

/home/linuxbrew/.linuxbrew/bin/chezmoi init git@github.com:strongmove/dotfiles.git
/home/linuxbrew/.linuxbrew/bin/chezmoi update
/home/linuxbrew/.linuxbrew/bin/fish
