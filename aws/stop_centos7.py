#!/usr/bin/python3
import boto3
import re
from botocore.exceptions import ClientError
#Check instances:
ec2=boto3.client('ec2')

def stop_instance(id):
    try:
        ec2.stop_instances(InstanceIds=[id],DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
#Dry run suceeded, start instance
    try:
        response=ec2.stop_instances(InstanceIds=[id],DryRun=False)
        print("HTTPStatusCode: %s" % response['ResponseMetadata']['HTTPStatusCode'] )
#        print(response)
    except ClientError as e:
        print(e)

responce=ec2.describe_instances()
print("\nMy EC2 instances: \n")
for reservations in responce['Reservations']:
    for instance in reservations['Instances']:
        if instance['State']['Name'] == 'running':
            for tag in instance['Tags']:
               if tag['Key'] == 'Name':
                    iname=tag['Value']
                    break
            if re.match("centos",iname) != None:
               print("\nFound running instance:")
               print('-------------------------')
               print('Instance name: %s' % iname)
               print('Instance ID: %s' % instance['InstanceId'])
               print('State: %s' % instance['State']['Name'])
               print('Stopping...')
               stop_instance(instance['InstanceId'])
