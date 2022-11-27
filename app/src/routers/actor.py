from fastapi import APIRouter, Depends, HTTPException
from app.src.config import Settings, get_settings

router = APIRouter(prefix="/actors")


@router.get("/{actor_id}")
def get_actor(actor_id: str, settings: Settings = Depends(get_settings)):
    print(settings)

    if actor_id != settings.test_user:
        raise HTTPException(status_code=404, detail="User not found")
    actor = {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://w3id.org/security/v1",
        ],
        "id": f"https://{settings.base_domain}/actors/{settings.test_user}",
        "type": "Person",
        "preferredUsername": settings.test_user,
        "name": settings.test_user.capitalize(),
        "inbox": f"https://{settings.base_domain}/actors/{settings.test_user}/inbox",
        "summary": "I am a result of curiosity.<p> Find out more about me at </p><p> https://github.com/rohitshetty/fidgeting-activitypub </p>",
        "publicKey": {
            "id": "https://{settings.base_domain}/actors/{settings.test_user}#main-key",
            "owner": f"https://{settings.base_domain}/actors/{settings.test_user}",
            "publicKeyPem": settings.public_key,
        },
    }

    return actor
