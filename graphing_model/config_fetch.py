import requests,pandas as pd

start_date = "2026-07-04"
end_date = "2026-07-06"

def fetch_bmrs(url_component, **kwargs) -> pd.DataFrame:
    r = requests.get(f"https://data.elexon.co.uk/bmrs/api/v1/{url_component}",
                     params={"format": "json",**kwargs})
    if r.status_code != 200:
        raise ValueError(f"BMRS API error {r.status_code} for {r.url}: {r.text}")
    payload = r.json()
    data = payload["data"] if isinstance(payload, dict) and "data" in payload else payload
    return pd.DataFrame(data)