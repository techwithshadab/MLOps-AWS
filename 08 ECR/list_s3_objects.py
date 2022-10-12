# import boto3
# s3 = boto3.resource("s3")
# bucket = s3.Bucket("mlops-aws")
# for each in bucket.objects.all():
#     print(each.key)
import os
print(os.environ["AWS_ACCESS_KEY_ID"])
print(os.environ["AWS_SECRET_ACCESS_KEY"])