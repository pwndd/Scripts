RED='\033[1;31m'
BLUE='\033[1;34m'
GREEN='\033[1;32m'
NC='\033[0m'
clear
echo -e "${BLUE}Welcome to the bashRC updating utility! ${NC}"
sleep "1"
echo -e "${BLUE}Starting in 5 seconds! ${NC}"
sleep "5"
clear
sudo pacman -S neofetch nano starship git curl
sudo pacman -Syy
sudo pacman -Syu
cd $HOME && curl -fsSL https://raw.githubusercontent.com/pwndd/BashRC/main/bashrc.txt > .bashrc
source ~/.bashrc
neofetch
echo -e "${RED}Thanks a lot Jonte (https://jontes.page) for making this script work! ${NC)"
echo -e "${GREEN}Done! Rebooting in 5 seconds! ${NC}"
sleep "5"
reboot
