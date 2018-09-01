#!/usr/bin/python3
import boto3
from botocore.exceptions import ClientError
#Check instances:
ec2=boto3.client('ec2')

def start_instance(id):
    try:
        ec2.start_instances(InstanceIds=[id],DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
#Dry run suceeded, start instance
    try:
        response=ec2.start_instances(InstanceIds=[id],DryRun=False)
        print("HTTPStatusCode: %s" % response['ResponseMetadata']['HTTPStatusCode'] )
#        print(response)
    except ClientError as e:
        print(e)

responce=ec2.describe_instances()
print("\nMy EC2 instances: \n")
for reservations in responce['Reservations']:
    for instance in reservations['Instances']:
        if instance['State']['Name'] == 'stopped':
            print("\nFound stopped instance:")
            print('-------------------------')
            print('Instance ID: %s' % instance['InstanceId'])
            for tag in instance['Tags']:
               if tag['Key'] == 'Name':
                    print('Instance name: %s' % tag['Value'])
                    break
            if tag['Value'] == 'centos01':
               print('State: %s' % instance['State']['Name'])
               print('Starting...')
               start_instance(instance['InstanceId'])
