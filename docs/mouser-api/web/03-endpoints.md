# Mouser API Endpoints

## Base URL

```
https://api.mouser.com/api/v1/search/
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/searchbykeyword` | POST | Search by keyword/description |
| `/searchbypartnumber` | POST | Search by part number |

## Search by Keyword

**Endpoint**: `POST https://api.mouser.com/api/v1/search/searchbykeyword`

### Request Body

```json
{
  "apiKey": "YOUR_MOUSER_SEARCH_API_KEY",
  "SearchByKeywordRequest": {
    "keyword": "STM32F103",
    "records": 25,
    "pageNumber": 1,
    "searchOptions": ""
  }
}
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `keyword` | string | Search term (required) |
| `records` | int | Results per page (max 50) |
| `pageNumber` | int | Page number for pagination |
| `searchOptions` | string | Additional filters |

## Search by Part Number

**Endpoint**: `POST https://api.mouser.com/api/v1/search/searchbypartnumber`

### Request Body

```json
{
  "apiKey": "YOUR_MOUSER_SEARCH_API_KEY",
  "SearchByPartRequest": {
    "mouserPartNumber": "595-SN74HC595N"
  }
}
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mouserPartNumber` | string | Mouser part number (recommended) |

You can also search by manufacturer part number or partial numbers.

## HTTP Headers

```
Content-Type: application/json
Accept: application/json
```

## Error Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request / malformed payload |
| 401/403 | Authentication or terms violation |
| 429 | Rate limit exceeded |
| 5xx | Server error |

Error payloads include a description of the issue:

```json
{
  "Errors": [
    {
      "Code": "InvalidApiKey",
      "Message": "The API key provided is invalid"
    }
  ]
}
```
