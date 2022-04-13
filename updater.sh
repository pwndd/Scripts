#Include the colors needed.
RED='\033[1;31m'
BLUE='\033[1;34m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color

#Main Script
clear #Starting with a clean slate
echo -e "${BLUE}Welcome to Avunit updating utility! ${NC}" #Intro Text, To welcome you guys!

echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!

echo -e "You are using version ${Blue} 1.0 ${NC}" #Showing you the version

sleep ".5" #Giving you some time!

clear
echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!

echo -e "${BLUE}Checking lists ${NC} " #Update text
sleep "0.25"

echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!

sudo pacman -Syy #Update lists

echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!

echo -e "${BLUE}Upgrading! ${NC} " #Upgrade text
sleep "0.25"

echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!
echo " " #Lets seperate stuff!

sudo pacman -S neofetch
sudo pacman -Syu
clear
neofetch

echo -e "${BLUE}Done! ${NC} " #Completed Text

#Copyright (c) 2021 avunit All Rights Reserved. Using commands from the Linux command line.