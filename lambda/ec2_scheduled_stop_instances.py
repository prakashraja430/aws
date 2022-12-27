import boto3
import logging
# Enter the region 
ec2client = boto3.client('ec2',region_name='<AWS-Region>')
response = ec2client.describe_instances()
# Setting logging level to INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    running_instances=[]
    for reservation in response["Reservations"]:
       for instance in reservation["Instances"]:
            if instance['State']['Name'] == 'running':
              x = (instance["InstanceId"])
              running_instances.append(x)
    # Removing the whitelisted instance from the running instance list
    # Enter the instances to whitelist from the running instance
    # Ex: whitelist_instances=['i-1a2b3c4d5e6f7g','i-8h9i10j11k12l']
    whitelist_instances=[]
    for n in whitelist_instances:
        while n in running_instances:
            running_instances.remove(n)
    if not running_instances:
        logger.info('No instance to stop')
    if running_instances:
        # ec2 instance stopping
        for n in running_instances:
            ec2client.stop_instances(InstanceIds=[n])
            logger.info('stopping instance: ' + n)
