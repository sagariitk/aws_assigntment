
#!/bin/sh

aws events put-rule --name "sagar_ec2_start" --schedule-expression "cron(0 10 *$
aws events put-rule --name "sagar_ec2_stop" --schedule-expression "cron(0 20 * $



