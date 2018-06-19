import boto3

region='us-east-1'

client=boto3.client('ec2')

#lambda function that will start the instance with a specific instance id

def lambda_handler(event, context):
    
    client.start_instances(InstanceIds=['i-0da6cd6bdd26e8bf2'])
    
    return 'Instance Started'

