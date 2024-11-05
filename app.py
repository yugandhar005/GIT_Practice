import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')

# Create a new EC2 instance with a Name tag
instances = ec2.create_instances(
    ImageId='ami-001f2488b35ca8aad',  # Replace with your AMI ID
    InstanceType='t2.micro',  # Change as per your requirement
    MinCount=1,
    MaxCount=1,
    KeyName='awskey',  # Replace with your key pair
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto3'  # Replace with your instance name
                }
            ]
        }
    ]
)

# Output the instance ID of the created instance
for instance in instances:
    print(f"Created instance with ID: {instance.id}")

