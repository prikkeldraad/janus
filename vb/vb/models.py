from pydantic import BaseModel
from typing import List, Optional

class VersionModel(BaseModel):
    id: Optional[int]
    software_name: Optional[str]
    release_name: Optional[str]
    version: Optional[str]
    major: Optional[str]
    minor: Optional[str]
    patch: Optional[str]
