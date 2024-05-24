from typing import Set

import httpx

from schemas.alerts import AlertsResponse
from schemas.countries import CountriesResponse, CountriesRequest


class IODAManager:
    BASE_URL = "https://api.ioda.inetintel.cc.gatech.edu"

    @classmethod
    async def get_alerts(cls, country_code: str, from_: int, until: int) -> AlertsResponse:
        url = f"{cls.BASE_URL}/v2/outages/alerts"

        async with httpx.AsyncClient() as client:
            params = {"entityCode": country_code, "from": from_, "until": until}

            response = await client.get(url, params=params)

            return AlertsResponse.model_validate(response.json())

    @classmethod
    async def get_country_codes(cls) -> Set[str]:
        url = f"{cls.BASE_URL}/v2/entities/query"

        async with httpx.AsyncClient() as client:
            params = CountriesRequest().model_dump(mode="json")

            response = await client.get(url, params=params)

            return {
                country.code
                for country in CountriesResponse.model_validate(response.json()).data
            }
