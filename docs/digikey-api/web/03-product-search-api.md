# Digi-Key Product Search API

## Overview

The Product Search API provides keyword search and detailed product lookup capabilities for Digi-Key's catalog.

## Endpoints

### Keyword Search

Search Digi-Key's product catalog by keyword.

**Endpoint**: POST `/search/v3/products/keyword`

**Request Example**:
```json
{
  "Keywords": "i.MX RT1060",
  "RecordCount": 25,
  "PageNumber": 1,
  "SortOption": "BEST_MATCH",
  "Filters": {
    "ManufacturerPartNumber": null,
    "Manufacturer": null,
    "Distributor": null,
    "RoHSStatus": null,
    "EnvironmentalStatus": null,
    "AvailabilityStatus": "InStock"
  }
}
```

**Response Example**:
```json
{
  "ExactMatchFound": true,
  "Products": [
    {
      "DigiKeyPartNumber": "497-IMXRT1060IEC-ND",
      "ProductDescription": "IC MCU CORTEX-M7 600MHZ 2.5MB BGA",
      "Manufacturer": "NXP Semiconductors",
      "ManufacturerPartNumber": "IMXRT1060IEC",
      "Category": "Embedded - Microcontrollers",
      "Family": "ARM Cortex-M",
      "Series": "i.MX RT1000",
      "MarketingStatus": "Active",
      "PrimaryDatasheet": {
        "Url": "https://datasheetspdf.com/pdf/...",
        "Title": "IMXRT1060IEC Datasheet"
      },
      "UnitPrice": 15.50,
      "QuantityAvailable": 500,
      "QuantityOnOrder": 1000,
      "LeadTime": "1",
      "EnvironmentalStatus": "RoHS Compliant",
      "Parameters": [...]
    }
  ],
  "ProductCount": 42,
  "PageNumber": 1,
  "PageSize": 25
}
```

### Product Details

Get comprehensive details for a specific product.

**Endpoint**: GET `/products/v4/{digi_key_part_number}`

**Parameters**:
- `digi_key_part_number` - Unique Digi-Key part number
- `includes` (optional) - Comma-separated list of additional fields:
  - `pricing`
  - `availability`
  - `compliance`
  - `datasheets`

**Response Fields**:
```json
{
  "DigiKeyPartNumber": "string",
  "ManufacturerPartNumber": "string",
  "ProductDescription": "string",
  "Manufacturer": "string",
  "Series": "string",
  "Family": "string",
  "Category": "string",
  "Subcategory": "string",
  "ProductUrl": "string",
  "DatasheetUrl": "string",
  "PrimaryDatasheet": {
    "Url": "string",
    "Title": "string"
  },
  "SecondaryDatasheets": [...],
  "UnitPrice": number,
  "Currency": "USD",
  "QuantityAvailable": integer,
  "LeadTime": integer,
  "EnvironmentalStatus": "string",
  "RoHSStatus": "string",
  "Parameters": [
    {
      "Parameter": "string",
      "Value": "string"
    }
  ]
}
```

### Batch Product Details

Get details for multiple products efficiently.

**Endpoint**: POST `/products/v4/batch`

**Request Example**:
```json
{
  "Products": [
    {
      "DigiKeyPartNumber": "497-IMXRT1060IEC-ND"
    },
    {
      "DigiKeyPartNumber": "497-IMXRT1061CEC-ND"
    }
  ],
  "Includes": ["pricing", "availability"]
}
```

**Response**: Array of product detail objects

## Search Filters

### AvailabilityStatus
- `InStock` - Items with current stock
- `OnOrder` - Items on back order
- `SingleSource` - Limited supplier availability
- `NearEndOfLife` - Product lifecycle consideration

### EnvironmentalStatus
- `RoHS Compliant`
- `RoHS Non-compliant`
- `Lead Free`
- `Not Applicable`

### SortOption
- `BEST_MATCH` - Relevance ranking (default)
- `LOWEST_PRICE` - Price ascending
- `HIGHEST_PRICE` - Price descending
- `NEWEST` - Recently added
- `QUANTITY_AVAILABLE` - Stock descending

## Pricing

Pricing information includes:
- **UnitPrice**: Price per single unit
- **BreakPricing**: Volume discount tiers
- **Currency**: Base currency (typically USD)

Volume pricing tiers are returned when available:
```json
{
  "BreakPricing": [
    {
      "Quantity": 1,
      "UnitPrice": 15.50,
      "TotalPrice": 15.50
    },
    {
      "Quantity": 10,
      "UnitPrice": 13.75,
      "TotalPrice": 137.50
    },
    {
      "Quantity": 100,
      "UnitPrice": 12.00,
      "TotalPrice": 1200.00
    }
  ]
}
```

## Parameters

Product parameters are returned as structured data:

Common IC parameters:
- **Core Voltage**: Typical operating voltage
- **Max Operating Frequency**: Clock speed
- **Memory**: Flash/RAM configuration
- **Package**: Physical form factor
- **Temperature Range**: Operating temperature limits
- **RoHS Status**: Environmental compliance
- **Lead Time**: Days until availability

## Datasheets

Datasheet information is provided:

```json
{
  "PrimaryDatasheet": {
    "Url": "https://datasheetspdf.com/pdf/...",
    "Title": "IMXRT1060IEC Datasheet"
  },
  "SecondaryDatasheets": [
    {
      "Url": "string",
      "Title": "Reference Manual"
    },
    {
      "Url": "string",
      "Title": "Application Note"
    }
  ]
}
```

## Rate Limits

- **Standard Tier**: 100 requests/minute
- **Professional Tier**: 1000 requests/minute
- **Enterprise Tier**: Custom limits

Rate limit headers:
- `X-RateLimit-Limit`: Requests allowed per minute
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Unix timestamp of reset

## Best Practices

1. **Batch Requests**: Use batch endpoint for multiple products
2. **Selective Fields**: Include only needed data
3. **Implement Caching**: Cache product details locally
4. **Handle 429 Responses**: Implement exponential backoff
5. **Monitor Availability**: Track quantity changes

## Common Use Cases

### Building IC Database
1. Search by product family (e.g., "i.MX RT")
2. Get details for each result
3. Extract datasheets
4. Store in local database

### Pricing Comparison
1. Search product by MPN
2. Get pricing tiers
3. Calculate total cost of ownership
4. Compare with other distributors

### Availability Tracking
1. Regular polling of key products
2. Track quantity changes
3. Alert on lead time increases
4. Monitor product discontinuation

---

**Source**: Digi-Key API v4 Documentation
**Last Updated**: 2026-01-08
