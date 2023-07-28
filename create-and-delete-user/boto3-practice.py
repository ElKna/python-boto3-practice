import boto3
from pprint import pprint

# client = boto3.client("sts")
# res = client.get_caller_identity()
# pprint(res)
# print("\n", res["UserId"], res["Arn"])

# if res ["Arn"].endswith("root"):
#     print("루트 계정을 사용중입니다.")
# else:
#     print("루트 계정을 사용하고있지 않습니다.")

client = boto3.client("iam")

username = "rex"
try: 
    res = client.create_user(UserName=username)
    pprint(res["User"])
except client.exceptions.EntityAlreadyExistsException:
    print(f"{username} 사용자가 이미 존재합니다.")

try:
    client.delete_user(Username=username)
    print(f"{username} 사용자가 삭제되었습니다.")
except client.exceptions.NoSuchEntityException:
    print(f"{username} 사용자가 존재하지 않습니다")

def del_user(client, username):
    if not username:
        raise Exception(f"{username} 잘못된 사용자 이름입니다.")
    try:
        client.delete_user(UserName=username)
    except client.exceptions.NoSuchEntityException:
        return True, None
    except Exception as e:
        return False, e

print(del_user(client, username))
# print(del_user(client, ""))