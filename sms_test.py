import boto3
import sys
sns = boto3.client('sns',region_name='us-east-1')
#sns.publish(
#    PhoneNumber = '+17189264805',
#    Message = 'Simple text message'
#)

sns.publish(PhoneNumber = sys.argv[1],
	Message = sys.argv[2]
) 
