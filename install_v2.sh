#!/bin/bash -ilvx

# wget -O /tmp/blank-slate.sh https://raw.githubusercontent.com/strongmove/blank-slate/main/install_v2.sh && bash /tmp/blank-slate.sh

if grep -qi 'debian' /etc/os-release; then
  echo "Recognized as a Debian distribution."
  if sudo -l -U "$USER" &>/dev/null; then
    echo "User is in sudoers."
  else
    echo "Cannot continue as $USER is not in sudoers."
    echo "Please run the following command to add $USER to sudoers:"
    echo "su -"
    echo "usermod -aG sudo $USER"
    echo "Log out and log back in to apply the changes."
    exit 1
  fi
elif grep -qi 'ubuntu' /etc/os-release; then
  echo "Recognized as an Ubuntu distribution."
else
  echo "Unknown Distribution. Cannot continue."
  exit 1
fi

export BREWBIN="/home/linuxbrew/.linuxbrew/bin"
export PATH="$BREWBIN:$PATH"

sudo apt update -y
sudo apt install curl build-essential git pipx dnsutils openssh-server -y
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
source "$HOME/.bashrc"

$BREWBIN/brew install fish

echo "$BREWBIN/brew shellenv" | $BREWBIN/fish
git clone git@github.com:strongmove/fish "$HOME/.config/fish"
git -C "$HOME/.config/fish pull"

# Essentials
$BREWBIN/brew install chezmoi diff-so-fancy
# Extras
$BREWBIN/brew install eza fzf ripgrep zoxide tmux xsel lazygit fd
$BREWBIN/brew install zk rust bat gdu bpytop ranger
# Setup fish as default shell
grep -qF fish /etc/shells || command -v $BREWBIN/fish | sudo tee -a /etc/shells
# command -v fish | sudo tee -a /etc/shells
chsh -s "$(command -v $BREWBIN/fish)"

$BREWBIN/chezmoi init git@github.com:strongmove/dotfiles.git
$BREWBIN/chezmoi update
$BREWBIN/fish
