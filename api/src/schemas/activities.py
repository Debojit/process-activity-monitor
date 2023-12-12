from pydantic import BaseModel, Field

from typing import List
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
  running = 'Running'
  success = 'Success'
  warning = 'Warning'
  error = 'Error'

class KeyValuePairModel(BaseModel):
  key: str = Field(alias='Key')
  value: str = Field(alias='Value')

class Activity(BaseModel):
  id: str = Field(alias='AuditEntryId', default='')
  run_id: str = Field(alias='RunId')
  component_id: str = Field(alias='ComponentId')
  component_name: str = Field(alias='ComponentName')
  component_version: float = Field(alias='ComponentVersion', gt=0)
  start_time: datetime = Field(alias='StartTime', default_factory=datetime.now)
  end_time: datetime = Field(alias='EndTime', default=None)
  status: StatusEnum = Field(alias='Status', default=StatusEnum.running)
  message: str = Field(alias='AuditMessage', default=None)
  request_payload: str = Field(alias='RequestPayload', default=None)
  response_payload: str = Field(alias='ResponsePayload', default=None)
  additional_info: List[KeyValuePairModel] = Field(alias='AdditionalInfo', default=None)