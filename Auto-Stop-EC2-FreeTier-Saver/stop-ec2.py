import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1') 

    instance_id = 'i-021e39847c6af1b4b' #Change with your instance id

    # Stop the instance
    ec2.stop_instances(InstanceIds=[instance_id])
    
    print(f"Stopping instance: {instance_id}")

    return {
        'statusCode': 200,
        'body': f'Stopped instance: {instance_id}'
    }
