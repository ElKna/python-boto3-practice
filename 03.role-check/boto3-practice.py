import boto3
from pprint import pprint

client = boto3.client("iam")
roles = client.list_roles()["Roles"]
for role in roles:
    # pprint(role)
    print(role["RoleName"])