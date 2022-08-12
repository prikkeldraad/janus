from pydantic import BaseModel
from typing import List, Optional


class SoftwareModel(BaseModel):
    id: Optional[int]
    name: str
    vendor: str


class VersionModel(BaseModel):
    id: Optional[int]
    #software_name: str
    #release_name: Optional[str]
    version: str
    major: Optional[str]
    minor: Optional[str]
    patch: Optional[str]
