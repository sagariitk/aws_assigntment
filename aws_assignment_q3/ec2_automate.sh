#!/bin/sh

read -p 'Do you want to change the schedule(y or n):' input

if [ "$input" = "n" ]; then
        ./ec2_default.sh
        break
elif [ "$input" = "y" ]; then
        ./ec2_automate.sh
        break
else
    	echo "enter correct input"
        ./first.sh
fi 


