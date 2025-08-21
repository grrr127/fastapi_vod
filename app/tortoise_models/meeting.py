from __future__ import annotations

from tortoise import Model, fields

from app.tortoise_models.base_model import BaseModel


# 모든 쿼리를 MeetingModel 클래스 안에 두면 조사요청이 들어왔을때 클래스를 읽기만 하면 됨(실무 노하우~)
class MeetingModel(BaseModel, Model):
    url_code = fields.CharField(max_length=255, unique=True)

    class Meta:
        table = "meetings"

    @classmethod
    async def create_meeting(cls, url_code: str) -> MeetingModel:
        return await cls.create(url_code=url_code)
