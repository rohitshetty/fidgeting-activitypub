from http.client import HTTPException
from fastapi import APIRouter, Depends, Query, HTTPException
from app.src.config import Settings, get_settings

router = APIRouter(prefix="/.well-known")


@router.get("/webfinger")
def webfinger(
    resource: str = Query(default=None),
    settings: Settings = Depends(get_settings),
):
    # print(settings, resource)
    if resource != f"acct:{settings.test_user}@{settings.base_domain}":
        return HTTPException(status_code=404, detail="User not found")

    response = {
        "subject": f"acct:{settings.test_user}@{settings.base_domain}",
        "links": [
            {
                "rel": "self",
                "type": "application/activity+json",
                "href": f"https://{settings.base_domain}/actors/{settings.test_user}",
            }
        ],
    }

    return response
