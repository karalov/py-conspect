#!/usr/bin/python3
import boto3
#s3 = boto3.resource('s3')
#print("My buckets:")
#for bucket in s3.buckets.all():
#    print(bucket.name)
#Load file to bucket
#data.open('test.jpg','rb')
#s3.Bucket('karalov').put_object(Key='test.jpg', Body=data)

#Check instances:
ec2=boto3.client('ec2')
responce=ec2.describe_instances()
hosts_entry={}
print("\nMy EC2 instances:")
for reservation in responce['Reservations']:
    for instance in reservation['Instances']:
        print('\n-------------------------')
        print('Instance ID: %s' % instance['InstanceId'])
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                 iName=tag['Value']
                 print('Instance name: %s' % iName)
                 break
        print('State: %s' % instance['State']['Name'])
        if instance['State']['Name'] == 'running':
             hosts_entry[iName] = instance['PublicIpAddress']
             print("Public IP: %s" % instance['PublicIpAddress'])

if len(hosts_entry) > 0:
    print ("\nInstances are running, below is entry for /etc/hosts\n")
    for x,y in hosts_entry.items():
        print("%s %s" % (y,x))
