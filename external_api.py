import httpx
from fastapi import HTTPException

async def fetch_external_data(url: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=exc.response.status_code if exc.response else 500,
                                detail=f"Error fetching data: {exc}") from exc
    return response.json()
