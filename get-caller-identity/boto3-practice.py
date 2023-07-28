import boto3
from pprint import pprint

client = boto3.client("sts")
res = client.get_caller_identity()
pprint(res)
print("\n", res["UserId"], res["Arn"])

if res ["Arn"].endswith("root"):
    print("루트 계정을 사용중입니다.")
else:
    print("루트 계정을 사용하고있지 않습니다.")