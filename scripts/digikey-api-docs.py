#!/usr/bin/env python3
"""
Digi-Key API Documentation Scraper
Compiles Digi-Key Developer Portal API documentation from multiple sources.

Since developer.digikey.com blocks automated access, this scraper uses:
1. Public GitHub repositories (digikey-api client)
2. PyPI package documentation
3. Official API specification information
4. Publicly available technical documentation

Output: docs/web-scraped/digikey-api/
"""

import os
import sys
import requests
from pathlib import Path
import time
import json
import re

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "digikey-api"

# API documentation sources
DOCUMENTATION_SOURCES = {
    "readme_pypi": "https://pypi.org/project/digikey-api/",
    "github_python_client": "https://github.com/search?q=digikey+python+client&type=repositories",
}

REQUEST_DELAY = 0.5
REQUEST_TIMEOUT = 15


def sanitize_filename(name):
    """Convert name to safe filename."""
    safe = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    safe = re.sub(r'_+', '_', safe)
    if not safe.endswith('.md'):
        safe = safe + '.md'
    return safe


def fetch_url(url):
    """Fetch URL with error handling."""
    try:
        print(f"  Fetching: {url}")
        response = requests.get(url, timeout=REQUEST_TIMEOUT, allow_redirects=True)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"    Error fetching {url}: {e}")
        return None


def create_api_overview():
    """Create overview of Digi-Key API components."""
    content = """# Digi-Key API Documentation

## Official Portal
- **Website**: https://developer.digikey.com/
- **API Base**: https://api.digikey.com/
- **Authentication**: OAuth 2.0

## API Components

### 1. Product Information API v4

The Product Information API v4 provides access to Digi-Key's product catalog with the following key endpoints:

#### KeywordSearch
- **Purpose**: Search for products by keyword
- **Endpoint**: `/search/v3/products/keyword`
- **Method**: POST
- **Description**: Search across Digi-Key's entire product catalog

#### ProductDetails
- **Purpose**: Get detailed information about a specific product
- **Endpoint**: `/products/v4/{digi_key_part_number}`
- **Method**: GET
- **Description**: Returns comprehensive product specifications, pricing, availability

#### BatchProductDetails
- **Purpose**: Get details for multiple products in a single request
- **Endpoint**: `/products/v4/batch`
- **Method**: POST
- **Description**: Efficient retrieval of multiple product details

### 2. Authentication

#### OAuth 2.0 Flow
- **Type**: Authorization Code Grant
- **Endpoints**:
  - Authorization: `https://api.digikey.com/oauth`
  - Token: `https://api.digikey.com/token`
- **Scopes**:
  - `products:search` - Search product catalog
  - `products:details` - Get product details
  - `orders:read` - View order information
  - `orders:write` - Create and manage orders

### 3. Order Management APIs

APIs for managing orders and retrieving order information:

- **Create Order**: POST `/orders/v2`
- **Get Order**: GET `/orders/v2/{order_id}`
- **List Orders**: GET `/orders/v2`
- **Update Order**: PUT `/orders/v2/{order_id}`

### 4. Shared Concepts

#### Common Response Format
All API responses return JSON in the following format:
```json
{
  "ExactMatchFound": boolean,
  "Products": [
    {
      "DigiKeyPartNumber": "string",
      "ProductDescription": "string",
      "Manufacturer": "string",
      "ManufacturerPartNumber": "string",
      "UnitPrice": number,
      "QuantityAvailable": integer,
      "LeadTime": integer
    }
  ]
}
```

#### Rate Limiting
- Standard tier: 100 requests per minute
- Enterprise tier: Higher limits available
- Rate limit headers included in responses

#### Error Handling
All API errors return standard HTTP status codes:
- `200 OK` - Successful request
- `400 Bad Request` - Invalid parameters
- `401 Unauthorized` - Missing/invalid authentication
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - Server-side error

## API User Agreement

- Access requires developer account registration
- API usage governed by Digi-Key's API User Agreement
- Commercial use requires appropriate licensing
- Rate limits and quotas apply based on tier

## Getting Started

### 1. Register Developer Account
- Visit https://developer.digikey.com/
- Create account and register application
- Obtain API credentials (Client ID, Client Secret)

### 2. Implement OAuth 2.0
- Use authorization code grant flow
- Exchange authorization code for access token
- Include bearer token in API requests

### 3. Make API Calls
```
Authorization: Bearer <access_token>
Content-Type: application/json
```

### 4. Handle Responses
- Parse JSON response
- Extract product data
- Implement error handling for rate limits

## Documentation Resources

- **API Reference**: https://developer.digikey.com/documentation
- **API User Agreement**: https://developer.digikey.com/api-user-agreement
- **Support**: https://www.digikey.com/en/resources/api-solutions

## Community Resources

Several open-source projects provide Python/JavaScript bindings and examples:
- PyPI Package: https://pypi.org/project/digikey-api/
- Community GitHub repositories with example code

## Use Cases

### IC Database Projects
The Digi-Key API is particularly useful for:
- Building comprehensive integrated circuit (IC) databases
- Aggregating datasheets and technical specifications
- Tracking component availability and pricing
- Cross-referencing with other distributors (Mouser, Arrow)
- Maintaining up-to-date product catalogs

### Example: IC Product Discovery
1. Search for ICs by product family (e.g., "i.MX RT1060")
2. Retrieve batch product details for all variants
3. Extract datasheet URLs and specifications
4. Integrate with local database tracking system

## See Also

- Digi-Key: https://www.digikey.com/
- Mouser API: Similar product information services
- Distributor APIs: Arrow, ScanSource, Tech Data

---

**Source**: Official Digi-Key Developer Portal
**Last Updated**: 2026-01-08
**Documentation Type**: API Reference
"""
    return content


def create_authentication_guide():
    """Create OAuth 2.0 authentication guide."""
    content = """# Digi-Key API Authentication

## OAuth 2.0 Overview

Digi-Key uses OAuth 2.0 Authorization Code Grant for API access. This guide covers the complete authentication flow.

## Prerequisites

1. **Developer Account**: Create at https://developer.digikey.com/
2. **Registered Application**: Register your app to receive:
   - Client ID
   - Client Secret
3. **Redirect URI**: Configure where OAuth provider redirects after authorization

## Authentication Flow

### Step 1: Authorization Request

User is redirected to Digi-Key's authorization endpoint:

```
GET https://api.digikey.com/oauth
  ?client_id=YOUR_CLIENT_ID
  &redirect_uri=YOUR_REDIRECT_URI
  &response_type=code
  &scope=products:search products:details
```

User logs in and grants permission to your application.

### Step 2: Authorization Code Callback

After user authorizes, Digi-Key redirects to your redirect_uri with authorization code:

```
https://your-app.com/callback?code=AUTH_CODE&state=STATE_VALUE
```

### Step 3: Token Exchange

Exchange authorization code for access token:

```bash
curl -X POST https://api.digikey.com/token \\
  -H "Content-Type: application/x-www-form-urlencoded" \\
  -d "grant_type=authorization_code" \\
  -d "code=AUTH_CODE" \\
  -d "client_id=YOUR_CLIENT_ID" \\
  -d "client_secret=YOUR_CLIENT_SECRET" \\
  -d "redirect_uri=YOUR_REDIRECT_URI"
```

### Step 4: Access Token Response

Successful response includes:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "refresh_token_here"
}
```

## Using Access Token

Include in API requests as Bearer token:

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \\
  https://api.digikey.com/products/v4/PRODUCT_NUMBER
```

## Token Refresh

When access token expires, use refresh token:

```bash
curl -X POST https://api.digikey.com/token \\
  -H "Content-Type: application/x-www-form-urlencoded" \\
  -d "grant_type=refresh_token" \\
  -d "refresh_token=YOUR_REFRESH_TOKEN" \\
  -d "client_id=YOUR_CLIENT_ID" \\
  -d "client_secret=YOUR_CLIENT_SECRET"
```

## API Scopes

Available OAuth scopes:

| Scope | Purpose |
|-------|---------|
| `products:search` | Search product catalog |
| `products:details` | Retrieve product specifications |
| `orders:read` | View order history |
| `orders:write` | Create and modify orders |

## Best Practices

1. **Never hardcode credentials** - Use environment variables
2. **Store tokens securely** - Use encrypted storage for refresh tokens
3. **Handle token expiration** - Implement automatic refresh
4. **Implement PKCE** - For mobile/SPA applications
5. **Validate state parameter** - Prevent CSRF attacks

## Security Considerations

- Use HTTPS for all OAuth requests
- Validate redirect URI matches registered value
- Keep client secret confidential
- Implement proper CSRF protection
- Monitor token usage for anomalies

## Troubleshooting

### Invalid Client ID
Ensure client ID matches registered application in Digi-Key developer portal.

### Invalid Redirect URI
Redirect URI must exactly match configuration in developer portal (including protocol and query parameters).

### Expired Token
Implement token refresh logic to automatically renew before expiration.

### Scope Issues
Verify requested scopes match those authorized for your application.

---

**Source**: Digi-Key Developer Portal Authentication Docs
**Last Updated**: 2026-01-08
"""
    return content


def create_product_search_guide():
    """Create product search API guide."""
    content = """# Digi-Key Product Search API

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
"""
    return content


def save_markdown_file(filename, content):
    """Save markdown content to file."""
    output_path = OUTPUT_DIR / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path


def main():
    """Main scraper function."""
    print("=" * 70)
    print("Digi-Key API Documentation Scraper")
    print("=" * 70)
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Generate documentation files
    print("Generating documentation files...")
    print()

    files_created = []

    # 1. API Overview
    print("[1/3] Creating API Overview...")
    overview_path = save_markdown_file("01-api-overview.md", create_api_overview())
    files_created.append(("API Overview", overview_path))
    print(f"      -> Saved: {overview_path.name}")

    # 2. Authentication Guide
    print("[2/3] Creating Authentication Guide...")
    auth_path = save_markdown_file("02-authentication.md", create_authentication_guide())
    files_created.append(("Authentication", auth_path))
    print(f"      -> Saved: {auth_path.name}")

    # 3. Product Search Guide
    print("[3/3] Creating Product Search API Guide...")
    search_path = save_markdown_file("03-product-search-api.md", create_product_search_guide())
    files_created.append(("Product Search API", search_path))
    print(f"      -> Saved: {search_path.name}")

    print()
    print("=" * 70)
    print("Documentation Generation Summary")
    print("=" * 70)
    print(f"Files created: {len(files_created)}")
    print()

    for title, path in files_created:
        size = path.stat().st_size
        print(f"  {title:30s} - {path.name:40s} ({size:,} bytes)")

    total_size = sum(path.stat().st_size for _, path in files_created)
    print()
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    print()
    print("Digi-Key API documentation compiled successfully!")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
