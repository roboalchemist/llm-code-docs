# Response Formats

The Element14 Product Search API returns data in either XML or JSON format, specified via the `callInfo.responseDataFormat` parameter.

## JSON Response Format

JSON format is preferred for modern applications and REST integrations.

### Response Structure

```json
{
  "response": {
    "statusCode": 200,
    "statusMessage": "OK",
    "numFound": 1250,
    "totalPages": 63,
    "currentPage": 1,
    "pageSize": 20,
    "products": [
      {
        "sku": "8947381",
        "description": "10kΩ Carbon Film Resistor 1/4W 5%",
        "partNumber": "CF14JT10K0",
        "manufacturerPartNumber": "CF14JT10K0",
        "manufacturer": "Yageo",
        "productFamily": "Carbon Film Resistors",
        "category": "Resistors > Thick Film / Carbon Resistors > Carbon Film",
        "unitPrice": 0.0275,
        "currencyCode": "USD",
        "stockLevel": 15420,
        "minimumOrderQty": 1,
        "orderMultiple": 1,
        "images": [
          {
            "url": "https://api.element14.com/images/CF14JT10K0_40_200.jpg",
            "size": "large"
          }
        ],
        "datasheetUrl": "https://...",
        "specifications": {
          "resistance": "10kΩ",
          "tolerance": "5%",
          "power": "0.25W",
          "temperature": "-55°C to +125°C"
        }
      }
    ]
  }
}
```

### JSON Response Fields

**Response Metadata:**
- `statusCode` - HTTP status code
- `statusMessage` - Status description
- `numFound` - Total results matching query
- `totalPages` - Total number of pages
- `currentPage` - Current page number
- `pageSize` - Results per page

**Product Fields:**
- `sku` - Stock keeping unit (Element14 internal ID)
- `description` - Product description
- `partNumber` - Element14/Newark/Farnell part number
- `manufacturerPartNumber` - Manufacturer's part number
- `manufacturer` - Manufacturer name
- `productFamily` - Product line/family
- `category` - Product category hierarchy
- `unitPrice` - Price per unit
- `currencyCode` - Currency (USD, GBP, EUR, etc.)
- `stockLevel` - Available quantity
- `minimumOrderQty` - Minimum purchase quantity
- `orderMultiple` - Must order in multiples of this
- `images` - Product images array
- `datasheetUrl` - Link to datasheet PDF
- `specifications` - Key technical specifications

### Response Groups - JSON

Different response groups return different field sets:

**`responseGroup=small`**
```json
{
  "sku": "8947381",
  "description": "10kΩ Carbon Film Resistor",
  "partNumber": "CF14JT10K0",
  "manufacturer": "Yageo"
}
```

**`responseGroup=medium` (default)**
```json
{
  "sku": "8947381",
  "description": "10kΩ Carbon Film Resistor",
  "partNumber": "CF14JT10K0",
  "manufacturer": "Yageo",
  "unitPrice": 0.0275,
  "currencyCode": "USD",
  "stockLevel": 15420,
  "minimumOrderQty": 1
}
```

**`responseGroup=large`**
```json
{
  "sku": "8947381",
  "description": "10kΩ Carbon Film Resistor",
  "partNumber": "CF14JT10K0",
  "manufacturer": "Yageo",
  "unitPrice": 0.0275,
  "currencyCode": "USD",
  "stockLevel": 15420,
  "images": [...],
  "specifications": {...},
  "relatedProducts": [...],
  "distributorInventory": [...]
}
```

**`responseGroup=prices`**
```json
{
  "sku": "8947381",
  "partNumber": "CF14JT10K0",
  "pricingTiers": [
    {"minQty": 1, "price": 0.0275},
    {"minQty": 100, "price": 0.0215},
    {"minQty": 1000, "price": 0.0175}
  ],
  "currencyCode": "USD"
}
```

**`responseGroup=inventory`**
```json
{
  "sku": "8947381",
  "partNumber": "CF14JT10K0",
  "warehouseInventory": [
    {
      "location": "New Jersey",
      "quantity": 8500
    },
    {
      "location": "Chicago",
      "quantity": 6920
    }
  ]
}
```

**`responseGroup=none`**
```json
{
  "response": {
    "statusCode": 200,
    "numFound": 1250,
    "currentPage": 1,
    "products": []
  }
}
```

## XML Response Format

XML format for legacy system integration.

### Response Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<response>
  <statusCode>200</statusCode>
  <statusMessage>OK</statusMessage>
  <numFound>1250</numFound>
  <totalPages>63</totalPages>
  <currentPage>1</currentPage>
  <pageSize>20</pageSize>
  <products>
    <product>
      <sku>8947381</sku>
      <description>10kΩ Carbon Film Resistor 1/4W 5%</description>
      <partNumber>CF14JT10K0</partNumber>
      <manufacturerPartNumber>CF14JT10K0</manufacturerPartNumber>
      <manufacturer>Yageo</manufacturer>
      <productFamily>Carbon Film Resistors</productFamily>
      <category>Resistors &gt; Thick Film / Carbon Resistors &gt; Carbon Film</category>
      <unitPrice>0.0275</unitPrice>
      <currencyCode>USD</currencyCode>
      <stockLevel>15420</stockLevel>
      <minimumOrderQty>1</minimumOrderQty>
      <orderMultiple>1</orderMultiple>
      <image size="large">
        <url>https://api.element14.com/images/CF14JT10K0_40_200.jpg</url>
      </image>
      <datasheetUrl>https://...</datasheetUrl>
      <specifications>
        <resistance>10kΩ</resistance>
        <tolerance>5%</tolerance>
        <power>0.25W</power>
        <temperature>-55°C to +125°C</temperature>
      </specifications>
    </product>
  </products>
</response>
```

## Error Responses

### Invalid Request - JSON

```json
{
  "response": {
    "statusCode": 400,
    "statusMessage": "Bad Request",
    "errorMessage": "Invalid API key provided"
  }
}
```

### Common Error Codes

- **200** - Success
- **400** - Bad request (invalid parameters)
- **401** - Unauthorized (invalid API key)
- **403** - Forbidden (insufficient permissions)
- **404** - Not found (no results)
- **429** - Rate limit exceeded
- **500** - Server error

### Error Messages

Common error conditions:

```json
{
  "statusCode": 400,
  "errorMessage": "Search term is required"
}
```

```json
{
  "statusCode": 401,
  "errorMessage": "Invalid API key"
}
```

```json
{
  "statusCode": 404,
  "errorMessage": "No results found for the given search term"
}
```

## Pagination

### Navigating Results

Results are paginated. To retrieve multiple pages:

1. Set `resultsSettings.pageSize` to desired page size (default 10, max ~100)
2. Use `resultsSettings.pageNumber` to request subsequent pages
3. Check `totalPages` in response to know how many pages exist
4. Iterate from `pageNumber=1` to `pageNumber=totalPages`

### Pagination Example

First request:
```
?term=any:resistor&resultsSettings.pageSize=20&resultsSettings.pageNumber=1
```

Response includes:
```json
{
  "numFound": 1250,
  "totalPages": 63,
  "currentPage": 1,
  "pageSize": 20
}
```

Second request (page 2):
```
?term=any:resistor&resultsSettings.pageSize=20&resultsSettings.pageNumber=2
```

## Image URLs

Product images are provided in the response when using `responseGroup=large` or larger:

```json
{
  "images": [
    {
      "url": "https://api.element14.com/images/CF14JT10K0_40_200.jpg",
      "size": "large"
    },
    {
      "url": "https://api.element14.com/images/CF14JT10K0_40_50.jpg",
      "size": "small"
    }
  ]
}
```

Image URL patterns follow Element14's image hosting CDN.

## Datasheet URLs

Datasheet links are available in responses:

```json
{
  "datasheetUrl": "https://api.element14.com/datasheets/yageo_cf14jt10k0_datasheet.pdf"
}
```

These URLs typically redirect to the manufacturer's official datasheet on Element14's system.
