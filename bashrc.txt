#
# ~/.bashrc
#

neofetch

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias update='sudo pacman -Syy && sudo pacman -Syu'
alias upr='sudo pacman -Syy && sudo pacman -Syu && neofetch && echo -e "Rebooting >
alias bashrc='sudo nano ~/.bashrc'
PS1='\W > '

eval "$(starship init bash)"