from tortoise import fields


class BaseModel:
    id = fields.BigIntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)


# MySQL : primary key를 정할때 주의해야 하는 점
# MySQL version 8 이상이라면
# innodb가 default engine

# innodb의 특징 중 하나 -> clustering index
# primary key를 기준으로
# primary key 값이 비슷한 row 들끼리 disk에서도 실제로 모여있음

# HDD
# 랜덤 IO가 느리고, 순차 IO가 빠르다.

# 그냥 Int가 아니라, 비지니스 적 의마가 있고
# 계속 증가하는 어떤 값으로 설정하면 굉장히 빠르게 읽을 수 있음
