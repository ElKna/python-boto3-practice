import boto3

client = boto3.client("sts")
res = client.get_caller_identity()
print(res)