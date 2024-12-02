import json
import os
from datetime import datetime, timedelta
from fastapi import HTTPException


def get_cve_data():
    if not os.path.exists("./data.json"):
        raise HTTPException(status_code=404, detail="File not found")

    with open("./data.json", "r") as file:
        return json.load(file)

def get_cve_last(cve_data, days: int = 10, limit: int = 40):
    recent_cve = []
    five_days_ago = datetime.now() - timedelta(days = days)

    for cve in cve_data['vulnerabilities']:
        cve_date = datetime.strptime(cve['dateAdded'], "%Y-%m-%d")
        if cve_date >= five_days_ago:
            recent_cve.append(cve)
        if len(recent_cve) >= limit:
            break

    return recent_cve


def get_cve_data_new(cve_data, limit: int = 10):
    cve_data['vulnerabilities'].sort(key=lambda x: x['dateAdded'], reverse=True)
    return cve_data['vulnerabilities'][:limit]


def get_cve_ransomware(cve_data):
    tmp = []
    for cve in cve_data['vulnerabilities']:
        if cve.get('knownRansomwareCampaignUse') == 'Known':
            tmp.append(cve)
    return tmp