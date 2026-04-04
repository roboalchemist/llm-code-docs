# API Endpoints

## Base Endpoint

```
https://api.element14.com/catalog/products
```

All requests use the HTTP GET method to this single endpoint. The endpoint behavior is controlled entirely through query parameters.

## Request Structure

```
https://api.element14.com/catalog/products?param1=value1&param2=value2&...
```

## Regional Store Identifiers

The `storeInfo.id` parameter specifies which regional catalog and pricing to query. Available stores include 40+ regional options:

**Major Regional Stores:**
- **40** - Element14 (Japan)
- **41** - Farnell (UK)
- **43** - Newark (US)
- **44** - Farnell (UK/Europe)
- **45** - Element14 (Australia)
- **46** - Element14 (Singapore)
- **47** - Element14 (Malaysia)
- **48** - Farnell (Germany)
- **49** - Farnell (Netherlands)
- **50** - Farnell (France)
- **51** - Farnell (Spain)
- **52** - Farnell (Italy)
- **53** - Element14 (China)
- **54** - Element14 (Hong Kong)
- **55** - Element14 (Taiwan)
- **56** - Element14 (Korea)
- **57** - Element14 (India)
- **59** - Element14 (New Zealand)
- **70** - Farnell (Poland)
- **72** - Element14 (Brazil)
- **74** - Element14 (Mexico)
- **75** - Farnell (Austria)
- **76** - Farnell (Belgium)
- **77** - Farnell (Czech Republic)
- **78** - Element14 (Hungary)
- **79** - Farnell (Portugal)
- **80** - Element14 (Israel)
- **81** - Farnell (Romania)
- **82** - Element14 (Saudi Arabia)
- **83** - Element14 (Pakistan)
- **84** - Farnell (Ireland)
- **85** - Farnell (Greece)
- **88** - Element14 (Russia/CIS)
- **89** - Farnell (Denmark)
- **91** - Farnell (Sweden)
- **92** - Element14 (Bulgaria)
- **94** - Farnell (Finland)
- **97** - Element14 (Turkey)

## Query Parameters

### Required Parameters

**`term`** - Search query (required)
- Keyword search: `any:search term`
- Product ID search: `id:element14_part_number`
- Manufacturer part number: `manuPartNum:MPN`

Examples:
```
term=any:resistor 10k
term=any:microcontroller STM32
term=id:8947381
term=manuPartNum:IMXRT1060IEC
```

**`storeInfo.id`** - Regional store ID (required)
```
storeInfo.id=43
```

**`callInfo.apiKey`** - API authentication key (required for standard tier)
```
callInfo.apiKey=YOUR_24_CHAR_KEY
```

### Response Format Parameters

**`callInfo.responseDataFormat`** - Output format
- `xml` - XML format (default)
- `json` - JSON format

**`resultsSettings.responseGroup`** - Response detail level
- `small` - Minimal product info (part number, description, category)
- `medium` - Includes pricing and stock (default)
- `large` - Includes images and related products
- `prices` - Pricing tier information only
- `inventory` - Stock breakdown by warehouse/location
- `none` - Result count only

### Pagination Parameters

**`resultsSettings.pageSize`** - Results per page
- Default: 10
- Maximum: typically 100 (confirm with support)

**`resultsSettings.pageNumber`** - Page number for pagination
- Default: 1
- Start: 1 (not 0-indexed)

### Filtering Parameters

**`resultsSettings.refinements`** - Apply filters to search results
- Can filter by category, price range, stock status
- Format: `refinements=parameter:value`

## Complete Example Request

**Keyword Search - JSON Format:**
```
https://api.element14.com/catalog/products
  ?term=any:resistor
  &storeInfo.id=43
  &callInfo.apiKey=ABCD1234EFGH5678IJKL9012MN
  &callInfo.responseDataFormat=json
  &resultsSettings.responseGroup=medium
  &resultsSettings.pageSize=20
```

**Manufacturer Part Number Search - XML Format:**
```
https://api.element14.com/catalog/products
  ?term=manuPartNum:LM7805CT
  &storeInfo.id=41
  &callInfo.apiKey=ABCD1234EFGH5678IJKL9012MN
  &callInfo.responseDataFormat=xml
  &resultsSettings.responseGroup=large
```

**Product ID Search:**
```
https://api.element14.com/catalog/products
  ?term=id:4298467
  &storeInfo.id=45
  &callInfo.apiKey=ABCD1234EFGH5678IJKL9012MN
  &callInfo.responseDataFormat=json
  &resultsSettings.responseGroup=prices
```

## URL Encoding

All special characters in parameters must be URL-encoded:
- Space → `%20` or `+`
- `&` → `%26`
- `=` → `%3D`
- `:` → `%3A` (in some contexts)

Most HTTP client libraries handle this automatically.

## Contract Pricing Endpoint Usage

The same endpoint supports contract pricing with additional parameters:

```
https://api.element14.com/catalog/products
  ?term=any:component
  &storeInfo.id=43
  &callInfo.apiKey=STANDARD_KEY
  &userInfo.signature=HMAC_SIGNATURE
  &userInfo.timestamp=2024-01-08T14:30:00Z
  &userInfo.customerId=CONTRACT_ID123
  &callInfo.responseDataFormat=json
```

See the Authentication section for signature generation details.
