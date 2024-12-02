from typing import List
from pydantic import BaseModel


class CVE_Values(BaseModel):
    cveID: str
    vendorProject: str
    product: str
    vulnerabilityName: str
    dateAdded: str
    shortDescription: str
    requiredAction: str
    dueDate: str
    knownRansomwareCampaignUse: str
    notes: str
    cwes: List[str]

    class Config:
        from_attributes = True


class CVE_Response(BaseModel):
    count: int
    vulnerabilities: List[CVE_Values]

    class Config:
        from_attributes = True