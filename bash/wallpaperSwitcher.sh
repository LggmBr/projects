#! /bin/bash

#Awesome Configuration Folder
ACF="$HOME/.config/awesome"
#Wallpapers Folder
WF="$HOME/wallpaper"

ln -srf "$WF/$(ls $WF | fzf --preview "bat")" "$ACF/wallpaper.png"
