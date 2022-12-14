#!/usr/bin/env bash

wallpapers_path=~/Pictures/download/

while true; do
    swaybg -i $(find $wallpapers_path -type f | shuf -n 1) -m fill
    sleep 29m
done

sleep 1m
