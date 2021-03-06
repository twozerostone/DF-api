import datetime
from typing import List, Optional
from bson import ObjectId
from pydantic.fields import Field

from pydantic import BaseModel
from pydantic.networks import AnyHttpUrl

from modules import PyObjectId


class CharacterBasicModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    characterId: str = Field(...)
    characterName: str = Field(...)
    level: int = Field(...)
    jobId: str = Field(...)
    jobGrowId: str = Field(...)
    jobName: str = Field(...)
    jobGrowName: str = Field(...)
    adventureName: str = Field(...)
    guildId: str = Field(...)
    guildName: str = Field(...)

    class Config:
        json_encoders = {ObjectId: str}


class CharacterModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    characterBasic: CharacterBasicModel = Field(...)
    critical: float = Field(...)
    regTime: datetime.datetime = Field(...)

    class Config:
        json_encoders = {ObjectId: str}


class CharacterSearchModel(BaseModel):
    serverId: str = Field(...)
    characterId: str = Field(...)
    characterName: str = Field(...)
    level: int = Field(...)
    jobId: str = Field(...)
    jobGrowId: str = Field(...)
    jobName: str = Field(...)
    jobGrowName: str = Field(...)
    critical: Optional[int] = Field(...)
    charImg: AnyHttpUrl = Field(...)


class CharacterSearchResponseModel(BaseModel):
    data: List[CharacterSearchModel] = Field(...)


class Search(BaseModel):
    name: str
    server: Optional[str] = 'all'
    jobId: Optional[str] = ''
    jobGrowId: Optional[str] = ''


class SearchDetail(BaseModel):
    serverId: str
    characterId: str
