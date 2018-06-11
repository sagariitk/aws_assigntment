# aws_assigntment

For the third question:

First I scheduled two rules in cloudwatch which will trigger two different lambda functions 
which eventually start and stop the ec2 instance(one will start and other will stop).
For the modification from client side I took the input from user for start and stop time for the instance 
and accordingly passed that value using shell script to the cron modification of rules in cloudwatch and cloudwatch will
schedule the start and stop of instances accourdingly
