import boto3
from pprint import pprint

from datetime import datetime, timezone, timedelta

now = datetime.now(timezone.utc)

client = boto3.client("iam")
roles = client.list_roles()["Roles"]
for role in roles:
    # pprint(role)
    # print(role["RoleName"])
    name = role["RoleName"]
    r = client.get_role(RoleName=name)["Role"]
    # pprint(r)
    last_used_date = r["RoleLastUsed"].get("LastUsedDate")
    print(name, last_used_date)
    if not last_used_date:
        print(name, "400일 내 사용 기록 없음")
    elif (now - last_used_date) > timedelta(days=90):
        print(name, f"90일 내 사용 기록 없음 | {last_used_date}")
    else:
        print(name, f"90일 내 사용 기록 있음 : {last_used_date}")