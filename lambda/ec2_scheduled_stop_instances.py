import boto3
# Enter the region 
ec2client = boto3.client('ec2',region_name='us-east-2')
response = ec2client.describe_instances()

# getting the list of running instances
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

# ec2 instance stopping code
for n in running_instances:
    ec2client.stop_instances(InstanceIds=[n])
    print('stopping instance: '+ n)