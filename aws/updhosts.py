#!/usr/bin/python3
import boto3

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
    print ("\nInstances are running, updating /etc/hosts\n")
    with open("/etc/hosts","r+") as f:
        content=f.readlines()
        for hst in hosts_entry.keys():
           for line in content:
              if hst in line:
                content.remove(line)  
        for x,y in hosts_entry.items():
           newline="%s %s\n" % (y,x)
           print("Adding %s" % newline)
           content.append(newline)
        f.seek(0)
        f.writelines(content)
print("\n####### CONTENT  of /etc/hosts ##############")
print(*content)
