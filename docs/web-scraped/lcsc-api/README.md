# LCSC Electronics API Documentation

Complete documentation for LCSC Electronics OpenAPI integration for electronic components procurement.

## Quick Start

LCSC provides a RESTful API for querying and managing electronics components. All requests require API key authentication with SHA-1 signature verification.

### Base URL
```
https://ips.lcsc.com
```

### Authentication
All API requests require four query parameters:
- `key` - API key (from business/agent account)
- `nonce` - Random 16-bit string
- `timestamp` - Unix timestamp of request
- `signature` - SHA-1 signature hash

### Signature Generation
```
signature = SHA1("key={key}&nonce={nonce}&secret={secret}&timestamp={timestamp}")
```

Request timestamps must not exceed 60 seconds old.

## API Access Requirements

### Account Setup
1. Create a business or agent account at https://lcsc.com
2. Apply for API access via https://lcsc.com/agent
3. Submit application materials to support@lcsc.com
4. Receive API key and secret after approval

### Restrictions
- No bulk data capture or scraping of catalog data
- No third-party redistribution of data
- No commercial aggregation/reselling
- Do not share API credentials
- Requests over 60 seconds old are rejected
- LCSC reserves right to modify API and final interpretation

## Product Query APIs

### 1. Category API
**Endpoint:** `GET /rest/wmsc2agent/category`

Retrieve hierarchical product categories and subcategories.

**Query Parameters:**
- `key` - API key
- `nonce` - Random string
- `timestamp` - Unix timestamp
- `signature` - SHA-1 signature

**Response Format:**
```json
{
  "success": true,
  "code": 200,
  "message": "success",
  "result": {
    "categories": [
      {
        "category_id": "xxx",
        "category_name": "Capacitors",
        "parent_id": "0",
        "sub_categories": [
          {
            "category_id": "xxx",
            "category_name": "Ceramic Capacitors",
            "parent_id": "xxx"
          }
        ]
      }
    ]
  }
}
```

### 2. Manufacturer API
**Endpoint:** `GET /rest/wmsc2agent/brand`

List IC manufacturers available in LCSC catalog.

**Query Parameters:**
- `key` - API key
- `nonce` - Random string
- `timestamp` - Unix timestamp
- `signature` - SHA-1 signature

**Response Format:**
```json
{
  "success": true,
  "code": 200,
  "message": "success",
  "result": {
    "brands": [
      {
        "brand_id": "xxx",
        "brand_name": "Texas Instruments",
        "brand_cn_name": "德州仪器",
        "brand_logo": "https://..."
      }
    ]
  }
}
```

### 3. Categorical Item List API
**Endpoint:** `GET /rest/wmsc2agent/category/product/{category_id}`

Retrieve products in a specific category with filtering and pagination.

**Path Parameters:**
- `category_id` - Category identifier

**Query Parameters:**
- `key` - API key
- `nonce` - Random string
- `timestamp` - Unix timestamp
- `signature` - SHA-1 signature
- `page_size` - Items per page (default: 100, max: 100)
- `current_page` - Page number for pagination (default: 1)
- `is_available` - Filter availability (0: all, 1: available, 2: out of stock)
- `is_pre_sale` - Filter pre-sale items (0: all, 1: include, 2: exclude)
- `currency` - Pricing currency: USD, CNY, EUR, HKD (default: CNY)

**Response Format:**
```json
{
  "success": true,
  "code": 200,
  "message": "success",
  "result": {
    "total": 1500,
    "total_page": 15,
    "current_page": 1,
    "page_size": 100,
    "products": [
      {
        "product_number": "C123456",
        "product_model": "TL072CP",
        "product_name": "Low Noise Dual Operational Amplifier",
        "brand_id": "xxx",
        "brand_name": "Texas Instruments",
        "category_id": "xxx",
        "category_name": "Integrated Circuits",
        "encapsulation": "DIP-8",
        "datasheet": "https://...",
        "prices": [
          {
            "quantity": 1,
            "price": "0.50",
            "currency": "USD"
          },
          {
            "quantity": 10,
            "price": "0.45",
            "currency": "USD"
          }
        ],
        "stock": [
          {
            "location": "Js",
            "amount": 5000
          },
          {
            "location": "Sz",
            "amount": 2500
          }
        ],
        "weight": "0.5",
        "image_urls": ["https://..."]
      }
    ]
  }
}
```

### 4. Item Details API
**Endpoint:** `GET /rest/wmsc2agent/product/info/{product_number}`

Retrieve comprehensive product information including attributes, pricing, images, stock levels, and datasheets.

**Path Parameters:**
- `product_number` - LCSC product code (e.g., C123456)

**Query Parameters:**
- `key` - API key
- `nonce` - Random string
- `timestamp` - Unix timestamp
- `signature` - SHA-1 signature
- `currency` - Pricing currency: USD, CNY, EUR, HKD (default: CNY)

**Response Format:**
```json
{
  "success": true,
  "code": 200,
  "message": "success",
  "result": {
    "product_number": "C123456",
    "product_model": "TL072CP",
    "product_name": "Low Noise Dual Operational Amplifier",
    "brand_id": "xxx",
    "brand_name": "Texas Instruments",
    "category_id": "xxx",
    "category_name": "Integrated Circuits",
    "encapsulation": "DIP-8",
    "weight": "0.5",
    "datasheet": "https://...",
    "description": "Low-noise, general-purpose operational amplifier",
    "attributes": [
      {
        "attribute_name": "Package",
        "attribute_value": "DIP-8"
      },
      {
        "attribute_name": "Operating Temperature",
        "attribute_value": "-25°C to +85°C"
      }
    ],
    "prices": [
      {
        "quantity": 1,
        "price": "0.50",
        "currency": "USD"
      }
    ],
    "stock": [
      {
        "location": "Js",
        "amount": 5000
      }
    ],
    "images": [
      {
        "type": "product",
        "url": "https://..."
      },
      {
        "type": "datasheet",
        "url": "https://..."
      }
    ]
  }
}
```

### 5. Keyword Search API
**Endpoint:** `GET /rest/wmsc2agent/search/product`

Search products by keywords with support for SKU, MPN, category, and manufacturer filtering.

**Query Parameters:**
- `key` - API key
- `nonce` - Random string
- `timestamp` - Unix timestamp
- `signature` - SHA-1 signature
- `keyword` - Search term (required): SKU, MPN, part number, or product name
- `match_type` - Match mode: 0 (exact), 1 (fuzzy) (default: 1)
- `page_size` - Items per page (default: 100, max: 100)
- `current_page` - Page number (default: 1)
- `is_available` - Availability filter
- `is_pre_sale` - Pre-sale filter
- `currency` - Pricing currency (default: CNY)

**Response Format:**
```json
{
  "success": true,
  "code": 200,
  "message": "success",
  "result": {
    "total": 42,
    "total_page": 1,
    "current_page": 1,
    "page_size": 100,
    "products": [
      {
        "product_number": "C123456",
        "product_model": "TL072CP",
        "product_name": "Low Noise Dual Operational Amplifier",
        "brand_name": "Texas Instruments",
        "encapsulation": "DIP-8",
        "prices": [
          {
            "quantity": 1,
            "price": "0.50",
            "currency": "USD"
          }
        ],
        "stock": [
          {
            "location": "Js",
            "amount": 5000
          }
        ],
        "datasheet": "https://..."
      }
    ]
  }
}
```

## Order Management APIs

### 6. Order Create API
**Endpoint:** `POST /rest/wmsc2agent/submit/order`

Create orders with product codes and quantities.

**Request Body:**
```json
{
  "order_items": [
    {
      "product_number": "C123456",
      "quantity": 10
    },
    {
      "product_number": "C234567",
      "quantity": 25
    }
  ],
  "po_number": "PO-2024-001"
}
```

**Query Parameters:**
- `key` - API key
- `nonce` - Random string
- `timestamp` - Unix timestamp
- `signature` - SHA-1 signature

**Response Format:**
```json
{
  "success": true,
  "code": 200,
  "message": "Order created successfully",
  "result": {
    "order_number": "ORD123456",
    "po_number": "PO-2024-001",
    "order_amount": "245.50",
    "currency": "USD",
    "order_items": [
      {
        "product_number": "C123456",
        "quantity": 10,
        "price_per_unit": "10.50"
      }
    ],
    "estimated_delivery": "2024-01-15"
  }
}
```

### 7. Check Order API
**Endpoint:** `GET /rest/wmsc2agent/select/order/page`

Query up to 10 orders by order code or PO number.

**Query Parameters:**
- `key` - API key
- `nonce` - Random string
- `timestamp` - Unix timestamp
- `signature` - SHA-1 signature
- `order_codes` - Comma-separated order numbers (optional)
- `po_numbers` - Comma-separated PO numbers (optional)
- `page_size` - Items per page (default: 10)
- `current_page` - Page number (default: 1)

**Response Format:**
```json
{
  "success": true,
  "code": 200,
  "message": "success",
  "result": {
    "total": 2,
    "current_page": 1,
    "page_size": 10,
    "orders": [
      {
        "order_number": "ORD123456",
        "po_number": "PO-2024-001",
        "order_status": "processing",
        "order_amount": "245.50",
        "currency": "USD",
        "order_date": "2024-01-08",
        "estimated_delivery": "2024-01-15",
        "order_items": [
          {
            "product_number": "C123456",
            "product_model": "TL072CP",
            "quantity": 10,
            "price_per_unit": "10.50",
            "subtotal": "105.00"
          }
        ]
      }
    ]
  }
}
```

### 8. Get Shipment API
**Endpoint:** `POST /rest/wmsc2agent/get/shipment`

Retrieve available shipping methods based on items and destination.

**Request Body:**
```json
{
  "order_items": [
    {
      "product_number": "C123456",
      "quantity": 10
    }
  ],
  "country": "US",
  "state": "CA"
}
```

**Query Parameters:**
- `key` - API key
- `nonce` - Random string
- `timestamp` - Unix timestamp
- `signature` - SHA-1 signature

**Response Format:**
```json
{
  "success": true,
  "code": 200,
  "message": "success",
  "result": {
    "shipment_methods": [
      {
        "method_id": "dhl",
        "method_name": "DHL Express",
        "estimated_days": "3-5",
        "shipping_cost": "45.00",
        "currency": "USD"
      },
      {
        "method_id": "ups",
        "method_name": "UPS Ground",
        "estimated_days": "5-7",
        "shipping_cost": "25.00",
        "currency": "USD"
      }
    ]
  }
}
```

## Error Codes

| Code | Message | Description |
|------|---------|-------------|
| 200 | success | Request successful |
| 424 | Key Is Required | API key parameter missing |
| 425 | nonce Is Required | Nonce parameter missing |
| 426 | timestamp Is Required | Timestamp parameter missing |
| 427 | signature Is Required | Signature parameter missing |
| 430 | Appsecret failed verification | Signature verification failed |
| 431 | No access to information | Insufficient permissions or invalid API key |
| 400 | Bad Request | Invalid parameters or malformed request |
| 401 | Unauthorized | Authentication failed |
| 403 | Forbidden | Access denied |
| 404 | Not Found | Resource not found |
| 500 | Server Error | Internal server error |

## Implementation Examples

### Python Implementation

```python
import hashlib
import time
import random
import string
import requests

class LCSCAPIClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://ips.lcsc.com"

    def generate_signature(self, timestamp, nonce):
        """Generate SHA-1 signature for request"""
        signature_string = f"key={self.api_key}&nonce={nonce}&secret={self.api_secret}&timestamp={timestamp}"
        return hashlib.sha1(signature_string.encode()).hexdigest()

    def get_auth_params(self):
        """Generate authentication parameters"""
        timestamp = int(time.time())
        nonce = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        signature = self.generate_signature(timestamp, nonce)

        return {
            'key': self.api_key,
            'timestamp': timestamp,
            'nonce': nonce,
            'signature': signature
        }

    def search_products(self, keyword, match_type=1, page_size=100, currency='USD'):
        """Search products by keyword"""
        auth_params = self.get_auth_params()

        params = {
            **auth_params,
            'keyword': keyword,
            'match_type': match_type,
            'page_size': page_size,
            'current_page': 1,
            'currency': currency
        }

        response = requests.get(
            f"{self.base_url}/rest/wmsc2agent/search/product",
            params=params
        )

        return response.json()

    def get_product_details(self, product_number, currency='USD'):
        """Get detailed product information"""
        auth_params = self.get_auth_params()

        params = {
            **auth_params,
            'currency': currency
        }

        response = requests.get(
            f"{self.base_url}/rest/wmsc2agent/product/info/{product_number}",
            params=params
        )

        return response.json()

    def get_categories(self):
        """Get product categories"""
        auth_params = self.get_auth_params()

        response = requests.get(
            f"{self.base_url}/rest/wmsc2agent/category",
            params=auth_params
        )

        return response.json()

# Usage
client = LCSCAPIClient(api_key='your_key', api_secret='your_secret')
results = client.search_products('TL072CP')
print(results)
```

### Request/Response Example

**Request:**
```
GET /rest/wmsc2agent/search/product?key=xxx&timestamp=1704700800&nonce=abc123&signature=xxx&keyword=DS2411&currency=USD HTTP/1.1
Host: ips.lcsc.com
```

**Response:**
```json
{
  "success": true,
  "code": 200,
  "message": "success",
  "result": {
    "total": 3,
    "total_page": 1,
    "current_page": 1,
    "page_size": 100,
    "products": [
      {
        "product_number": "C12345",
        "product_model": "DS2411",
        "product_name": "1-Wire UniqueID Ibutton",
        "brand_name": "Maxim Integrated",
        "encapsulation": "T05",
        "prices": [
          {
            "quantity": 1,
            "price": "0.44",
            "currency": "USD"
          },
          {
            "quantity": 10,
            "price": "0.40",
            "currency": "USD"
          }
        ],
        "stock": [
          {
            "location": "Js",
            "amount": 3500
          },
          {
            "location": "Sz",
            "amount": 1200
          }
        ]
      }
    ]
  }
}
```

## Alternative API: Global Search

LCSC also provides an unofficial global search API endpoint:

**Endpoint:** `GET https://wwwapi.lcsc.com/v1/search/global-search`

**Query Parameters:**
- `keyword` - Search term (SKU, part number, or product name)

**Response Format:**
Same as Keyword Search API, returns products with:
- Product IDs, codes, models
- Tiered pricing at different quantities
- Stock levels per location
- Physical specifications
- Datasheet URLs
- Availability flags

**Advantages:**
- No authentication required
- No signature generation needed
- Simpler integration for read-only searches

**Note:** This endpoint is community-documented and not officially published, use with caution for production applications.

## Rate Limiting

- No documented rate limits
- Requests over 60 seconds old are rejected
- Maximum of 100 items per page
- Recommended: Implement exponential backoff for retries

## Best Practices

1. **Cache responses** - Store product data locally to reduce API calls
2. **Batch requests** - Use pagination to retrieve large datasets efficiently
3. **Error handling** - Implement retry logic with exponential backoff
4. **Timestamp validation** - Ensure server time is synchronized (NTP)
5. **Secure credentials** - Never expose API key or secret in client-side code
6. **Respect restrictions** - Do not perform bulk scraping or redistribute data
7. **Use appropriate currency** - Set currency parameter for correct pricing
8. **Filter availability** - Use availability flags to show in-stock items first

## Support and Resources

- **Official Documentation:** https://www.lcsc.com/docs/openapi/index.html
- **Account & API Setup:** https://www.lcsc.com/agent
- **Support Email:** support@lcsc.com
- **FAQ:** https://www.lcsc.com/faqs/api
- **Community Examples:** GitHub gists and open-source projects (Part-DB, etc.)

## License and Attribution

LCSC API documentation aggregated from official sources and community implementations. Subject to LCSC's API terms and restrictions.
