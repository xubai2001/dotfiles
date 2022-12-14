#!/usr/bin/env bash

choice=$(printf "Lock\nLogout\nSleep\nSuspend\nReboot\nShutdown" | rofi -dmenu)
if [[ $choice == "Lock" ]];then
    bash ~/.config/system_scripts/wayland_session_lock
elif [[ $choice == "Logout" ]];then
    pkill -KILL -u "$USER"
elif [[ $choice == "Sleep" ]];then
    systemctl hybrid-sleep
elif [[ $choice == "Suspend" ]];then
    systemctl suspend
elif [[ $choice == "Reboot" ]];then
    systemctl reboot
elif [[ $choice == "Shutdown" ]];then
    systemctl poweroff
fi
