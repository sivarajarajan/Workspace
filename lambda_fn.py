from __future__ import print_function
import boto3

class Instance(object):
    def __init__(self, name, id, obj):
        self.name = name
        self.id = id
        self.obj = obj

def lambda_handler(event, context):
    instancePrefix = event['instancePrefix']
    action_name = event['action_name']
    prereq_status = event['prereq_status']
    action_func = event['action_func']    
    region = event['region']
    
    store = {}
    
    ec2 = boto3.resource('ec2')
    
    filters= [{
        'Name':'tag:Name',
        'Values':['%s*' % instancePrefix]
        },
        {
        'Name': 'instance-state-name',
        'Values': [prereq_status]
        }]

    instances = ec2.instances.filter(Filters=filters)
    
    for instance in instances:
        for tags in instance.tags:
            tag = tags['Key']
            value = tags['Value']
            if tag == 'Name':
                store[value] = Instance(value, instance.id, instance)
                print("Instance Name: %s - switching state to %s" %(value, action_name))
                
    ids = [ x.id for x in store.values() ]
    if ids:
        getattr(ec2.instances.filter(InstanceIds=ids), action_func)()
        print('Total number of instances %s:' % action_name, len(ids))
    else:
        print('No instances in state:', prereq_status, 'on', instancePrefix)
        print('Hence not performed any state changes on instance')
    
    return True