from fastapi import APIRouter, HTTPException
from src.models.model_cve import CVE_Response
from src.services.services import get_cve_data, get_cve_last, get_cve_data_new, get_cve_ransomware

router = APIRouter(tags=["About"])


@router.get("/info")
def about_author():
    return {
        "name_project": "FastAPI Application",
        "author": "Tetiana Korotiukova",
        "description": {
            "/info": "Має виводити інформацію про додаток, вас як автора",
            "/get/all": "Має виводити CVE за останні 5 днів. Максимум 40 CVE",
            "/get/new": "Має виводити 10 найновіших CVE",
            "/get/known": "Має виводити CVE в яких knownRansomwareCampaignUse - Known, максимум 10",
            "/get?query='key'": "Має виводити CVE які містять ключове слово"
        }
    }

# /get/all - Має виводити CVE за останні 5 днів. Максимум 40 CVE
@router.get("/get/all", response_model=CVE_Response)
def get_cve_all():
    cve_data = get_cve_data()

    if 'vulnerabilities' not in cve_data:
        raise HTTPException(status_code = 500, detail = "Vulnerabilities key not found")

    cve_last = get_cve_last(cve_data)

    return {"Count": len(cve_last), "Vulnerabilities": cve_last}


# /get/new - Має виводити 10 найновіших CVE
@router.get("/get/new", response_model = CVE_Response)
def get_cve_new():
    cve_data = get_cve_data()

    if 'vulnerabilities' not in cve_data:
        raise HTTPException(status_code = 500, detail = "Vulnerabilities key not found")
    
    new_cve = get_cve_data_new(cve_data)

    return {"count": len(new_cve), "vulnerabilities": new_cve}


# /get/known - Має виводити CVE в яких knownRansomwareCampaignUse - Known, максимум 10
@router.get("/get/known", response_model = CVE_Response)
def get_known_ransomware_cve_endpoint():
    cve_data = get_cve_data()

    if 'vulnerabilities' not in cve_data:
        raise HTTPException(status_code = 500, detail = "vulnerabilities key not found")

    known_ransomware_cve = get_cve_ransomware(cve_data)

    return {"count": 10, "vulnerabilities": known_ransomware_cve[:10]}


# /get?query="key" - Має виводити CVE які містять ключове слово
@router.get("/get", response_model = CVE_Response)
def search_cve(query: str):
    cve_data = get_cve_data()

    if 'vulnerabilities' not in cve_data:
        raise HTTPException(status_code = 500, detail = "vulnerabilities key not found")

    list_cve = []
    for cve in cve_data['vulnerabilities']:
        if query.lower() in cve['shortDescription'].lower():
            list_cve.append(cve)

    return {"count": len(list_cve), "vulnerabilities": list_cve}