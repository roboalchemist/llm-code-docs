# Mouser API Code Examples

## Python

### Search by Part Number

```python
import requests
import os

API_KEY = os.environ.get("MOUSER_API_KEY")
BASE_URL = "https://api.mouser.com/api/v1/search/searchbypartnumber"

def search_part(part_number: str) -> dict:
    payload = {
        "apiKey": API_KEY,
        "SearchByPartRequest": {
            "mouserPartNumber": part_number
        }
    }

    response = requests.post(BASE_URL, json=payload, timeout=15)
    response.raise_for_status()
    return response.json()

# Usage
data = search_part("595-SN74HC595N")
parts = data.get("SearchByPartResponse", {}).get("Parts", [])

for part in parts:
    print(f"Mouser P/N: {part.get('MouserPartNumber')}")
    print(f"Mfr P/N: {part.get('ManufacturerPartNumber')}")
    print(f"Availability: {part.get('Availability')}")
    print(f"Datasheet: {part.get('DataSheetUrl')}")

    price_breaks = part.get("PriceBreaks", [])
    if price_breaks:
        print(f"Unit Price: ${price_breaks[0].get('Price')}")
```

### Search by Keyword

```python
import requests
import os

API_KEY = os.environ.get("MOUSER_API_KEY")
BASE_URL = "https://api.mouser.com/api/v1/search/searchbykeyword"

def search_keyword(keyword: str, records: int = 25, page: int = 1) -> dict:
    payload = {
        "apiKey": API_KEY,
        "SearchByKeywordRequest": {
            "keyword": keyword,
            "records": records,
            "pageNumber": page
        }
    }

    response = requests.post(BASE_URL, json=payload, timeout=15)
    response.raise_for_status()
    return response.json()

# Usage
data = search_keyword("STM32F103", records=20)
resp = data.get("SearchByKeywordResponse", {})

print(f"Total results: {resp.get('NumberOfResult')}")

for part in resp.get("Parts", []):
    print(f"{part.get('MouserPartNumber')} - {part.get('Description')}")
    print(f"  Stock: {part.get('Availability')}")
```

### Pagination Example

```python
def search_all(keyword: str, max_results: int = 200) -> list:
    """Fetch multiple pages of results."""
    all_parts = []
    page = 1
    records_per_page = 50  # API max

    while len(all_parts) < max_results:
        data = search_keyword(keyword, records=records_per_page, page=page)
        resp = data.get("SearchByKeywordResponse", {})

        parts = resp.get("Parts", [])
        if not parts:
            break

        all_parts.extend(parts)

        total = resp.get("NumberOfResult", 0)
        if len(all_parts) >= total:
            break

        page += 1

    return all_parts[:max_results]
```

## JavaScript / Node.js

### Search by Part Number

```javascript
const API_KEY = process.env.MOUSER_API_KEY;
const BASE_URL = "https://api.mouser.com/api/v1/search/searchbypartnumber";

async function searchPart(partNumber) {
  const body = {
    apiKey: API_KEY,
    SearchByPartRequest: {
      mouserPartNumber: partNumber
    }
  };

  const response = await fetch(BASE_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify(body)
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  }

  return response.json();
}

// Usage
const data = await searchPart("595-SN74HC595N");
const parts = data.SearchByPartResponse?.Parts || [];

parts.forEach(part => {
  console.log(`${part.MouserPartNumber} - ${part.Description}`);
  console.log(`  Stock: ${part.Availability}`);
  console.log(`  Datasheet: ${part.DataSheetUrl}`);
});
```

## cURL

### Keyword Search

```bash
curl -X POST "https://api.mouser.com/api/v1/search/searchbykeyword" \
  -H "Content-Type: application/json" \
  -d '{
    "apiKey": "YOUR_API_KEY",
    "SearchByKeywordRequest": {
      "keyword": "ATmega328",
      "records": 10,
      "pageNumber": 1
    }
  }'
```

### Part Number Search

```bash
curl -X POST "https://api.mouser.com/api/v1/search/searchbypartnumber" \
  -H "Content-Type: application/json" \
  -d '{
    "apiKey": "YOUR_API_KEY",
    "SearchByPartRequest": {
      "mouserPartNumber": "556-ATMEGA328P-PU"
    }
  }'
```

## Third-Party Libraries

### Python: sparkmicro/mouser-api

```bash
pip install mouser-api
```

```python
from mouser.api import MouserPartSearchRequest

request = MouserPartSearchRequest('YOUR_API_KEY')
result = request.part_search('595-SN74HC595N')
```

GitHub: https://github.com/sparkmicro/mouser-api
