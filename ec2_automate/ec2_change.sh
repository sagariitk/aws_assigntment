#!/bin/sh
echo "provide time in GMT only"
read -p 'Enter start hour: ' hour1
read -p 'Enter start minute: ' minute1
#read -p 'Enter start day of month: ' day
#read -p 'Enter start month: ' month
#read -p 'Enter start day of week: ' week

aws events put-rule --name "sagar_ec2_start" --schedule-expression "cron($minute1 $hour1 * * ? *)"


read -p 'Enter stop hour: ' hour
read -p 'Enter stop minute: ' minute
#read -p 'Enter stop day of month: ' day
#read -p 'Enter stop month: ' month
#read -p 'Enter stop day of week: ' week


aws events put-rule --name "sagar_ec2_stop" --schedule-expression "cron($minute1 $hour1 * * ? *)"


