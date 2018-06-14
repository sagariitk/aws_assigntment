#!/bin/sh

#launch of first instance 
#in the bash- generated new rsa key belonging to ec2-user
#copied the key to s3 bucket

aws ec2 run-instances --image-id ami-14c5486b --count 1 --instance-type t2.micro --key-name sagar --security-group-ids sg-ee3fc3a5 --tag-specifications 'ResourceType=instance,Tags=[{Key=name,Value=sagar111},{Key=username,Value=sagar.yadav},{Key=email,Value=sagar.yadav@quantiphi.com}, {Key=project,Value=PE_Trainig}]' --iam-instance-profile Name=PE_trainee_Admin_role --user-data  '#!/bin/bash
sudo -u ec2-user ssh-keygen -b 2048 -t rsa -f /home/ec2-user/.ssh/id_rsa -q -N ""
aws s3 cp /home/ec2-user/.ssh/id_rsa.pub s3://sagar111/id_rsa.pub
'

#checking whether the key is uploaded to s3 bucket or not
aws s3 ls s3://sagar111/id_rsa.pub
while [ $? -ne 0 ]
do 
    aws s3 ls s3://sagar111/id_rsa.pub
    if [[ $? -eq 0 ]]; then 
      echo "File uploaded"
      break
    else
      echo "please wait some time" 
      sleep 20
    fi
done

#launch of second instance
#downloaded the rsa key from s3 bucket
#apended the key to authorized_keys which will allow the first instance to communicate passwordlessly
#also changed the permissions of the .ssh directory and authorized_keys file
aws ec2 run-instances --image-id ami-14c5486b --count 1 --instance-type t2.micro --key-name sagar --security-group-ids sg-ee3fc3a5 --tag-specifications 'ResourceType=instance,Tags=[{Key=name,Value=sagar222},{Key=username,Value=sagar.yadav},{Key=email,Value=sagar.yadav@quantiphi.com}, {Key=project,Value=PE_Trainig}]' --iam-instance-profile Name=PE_trainee_Admin_role --user-data '#!/bin/bash
aws s3 cp s3://sagar111/id_rsa.pub /home/ec2-user/.ssh/id_rsa.pub
cat /home/ec2-user/.ssh/id_rsa.pub >> /home/ec2-user/.ssh/authorized_keys
chmod 700 /home/ec2-user/.ssh
chmod 600 /home/ec2-user/.ssh/authorized_keys
'

