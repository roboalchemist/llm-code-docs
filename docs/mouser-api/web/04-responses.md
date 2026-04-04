# Mouser API Response Format

## Response Structure

### Keyword Search Response

```json
{
  "SearchByKeywordResponse": {
    "NumberOfResult": 1234,
    "Parts": [
      {
        "MouserPartNumber": "595-SN74HC595N",
        "ManufacturerPartNumber": "SN74HC595N",
        "Manufacturer": "Texas Instruments",
        "Availability": "3,456 In Stock",
        "DataSheetUrl": "https://...",
        "Description": "Shift Registers 8-Bit Shift Register",
        "ImagePath": "https://...",
        "Category": "Shift Registers",
        "ProductDetailUrl": "https://www.mouser.com/ProductDetail/595-SN74HC595N",
        "PriceBreaks": [
          {"Quantity": 1, "Price": "0.45"},
          {"Quantity": 10, "Price": "0.40"}
        ]
      }
    ]
  }
}
```

### Part Number Search Response

```json
{
  "SearchByPartResponse": {
    "Parts": [
      {
        "MouserPartNumber": "...",
        "ManufacturerPartNumber": "...",
        ...
      }
    ]
  }
}
```

## Available Fields

Each part in the response includes:

| Field | Description |
|-------|-------------|
| `MouserPartNumber` | Mouser's part number |
| `ManufacturerPartNumber` | Manufacturer's part number |
| `Manufacturer` | Manufacturer name |
| `Availability` | Stock status (e.g., "3,456 In Stock") |
| `DataSheetUrl` | Link to datasheet PDF |
| `Description` | Product description |
| `ImagePath` | Product image URL |
| `Category` | Product category |
| `Packaging` | Package type (Tube, Reel, etc.) |
| `ProductCompliance` | Compliance info (REACH, RoHS) |
| `LifecycleStatus` | Active, NRND, Obsolete, etc. |
| `RoHSStatus` | RoHS compliance status |
| `Reeling` | Cut tape/reeling availability |
| `Min` | Minimum order quantity |
| `Mult` | Order quantity multiple |
| `LeadTime` | Lead time if not in stock |
| `SuggestedReplacement` | Array of replacement parts |
| `ProductDetailUrl` | Product page URL |
| `PriceBreaks` | Array of quantity/price tiers |
| `StandardPackQuantity` | Standard package quantity |

## Price Breaks

Up to 4 price breaks are returned per part:

```json
"PriceBreaks": [
  {"Quantity": 1, "Price": "0.45"},
  {"Quantity": 10, "Price": "0.40"},
  {"Quantity": 100, "Price": "0.35"},
  {"Quantity": 1000, "Price": "0.30"}
]
```

## Pagination

For large result sets:

1. Set `records` to desired page size (max 50)
2. Use `pageNumber` to iterate through pages
3. Check `NumberOfResult` for total count

```python
total_results = response["SearchByKeywordResponse"]["NumberOfResult"]
total_pages = (total_results + records - 1) // records
```
