from fastapi import APIRouter

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