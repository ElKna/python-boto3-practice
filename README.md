## python-boto3-practice

파이썬에서 boto3를 사용하면서 기록을 저장하는 용도의 리포

### 실행 방법
Python3이 설치된 상태에서  
Terminal에 AWS-CLI를 연결한 후

Role Check시에는 연결한 AWS User에 `IAMReadOnlyAccess` 정책이 연결되어있어야 조회가 가능함
```bash
python3 -m pip install boto3
python3 -m pip install boto3-stubs

# 해당 폴더 이동 후
python3 boto3-practice.py
```