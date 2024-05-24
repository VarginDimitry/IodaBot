from datetime import datetime
from enum import Enum
from typing import Optional, List, Any

from pydantic import BaseModel, field_validator, Field, AliasChoices


class DataSource(str, Enum):
    BGP = "bgp"
    GTR = "gtr"
    GTR_NORM = "gtr-norm"
    ACTIVE_PROBING = "ping-slash24"

    TELESCOPE_UCSD = "ucsd-nt"
    TELESCOPE_MERIT = "merit-nt"


class AlertsRequest(BaseModel):
    entityType: str = "country"
    entityCode: str
    from_: int | datetime = Field(validation_alias=AliasChoices('from_', 'from'))
    until: int | datetime

    @field_validator('from_', 'until')
    def time_validator(cls, v: int | datetime) -> int:
        if isinstance(v, datetime):
            v = int(v.timestamp())
        return v


class Entity(BaseModel):
    code: str
    name: str
    type: str


class DataItem(BaseModel):
    datasource: DataSource
    time: datetime
    level: str
    condition: str
    # value: int
    # historyValue: int
    # method: str
    # entity: Entity


class AlertsResponse(BaseModel):
    error: Optional[Any]
    perf: Optional[str]
    data: List[DataItem]
    # type: str
