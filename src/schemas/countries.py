from typing import Optional, List

from pydantic import BaseModel


class CountriesRequest(BaseModel):
    entityType: str = "country"


class Entity(BaseModel):
    code: str
    # name: str
    # type: str


class CountriesResponse(BaseModel):
    error: Optional[str]
    perf: Optional[str]
    data: List[Entity]
    # type: str
