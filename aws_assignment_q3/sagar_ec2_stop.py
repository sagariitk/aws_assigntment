import boto3

region='us-east-1'

client=boto3.client('ec2')

#lambda function that will stop the specific instance with given instance id

def lambda_handler(event, context):
    
    client.stop_instances(InstanceIds=['i-0da6cd6bdd26e8bf2'])
    
    return 'Instance Stopped'

