# 디비 연결 실습: mongoDB

from pymongo import MongoClient

# with 안에서 만들어진 객체는 auto close
with MongoClient('127.0.0.1') as conn:

    # 디비 설정: 없으면 생성
    db = conn.mymongo
    print("연결 성공")

    users = db.users

    users.delete_many({'empno': '10001'})

    results = users.find()

    for result in results:
        print(result['name'])

