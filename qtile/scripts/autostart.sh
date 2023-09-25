#!/bin/bash 

# Kill if already running
killall -9 picom xfce4-power-manager ksuperkey dunst sxhkd eww

# set background
feh --no-fehbg --bg-scale "$HOME/.config/qtile/icons/wallpaper.jpg"

#lxsession &

# start hotkey daemon
sxhkd &

# start picom
picom &

# start volumeicon
volumeicon &

# start nm-applet
nm-applet &

# start flameshot
flameshot &

# start bluetooth
bluetooth &

# wal -R &
# nitrogen --restore &
#discord &
#caprine &
#firefox &
#discord &
