# LCSC API Quick Reference

Fast lookup guide for LCSC Electronics API endpoints and parameters.

## Authentication

All requests require these 4 parameters:
```
key=YOUR_API_KEY
timestamp=UNIX_TIMESTAMP
nonce=RANDOM_16_CHARS
signature=SHA1(key=X&nonce=Y&secret=Z&timestamp=W)
```

Time limit: 60 seconds

## Endpoints Summary

| Endpoint | Method | Purpose | Auth Required |
|----------|--------|---------|---------------|
| `/rest/wmsc2agent/category` | GET | List product categories | Yes |
| `/rest/wmsc2agent/brand` | GET | List manufacturers | Yes |
| `/rest/wmsc2agent/category/product/{id}` | GET | Products by category | Yes |
| `/rest/wmsc2agent/product/info/{product_number}` | GET | Product details | Yes |
| `/rest/wmsc2agent/search/product` | GET | Search by keyword | Yes |
| `/rest/wmsc2agent/submit/order` | POST | Create order | Yes |
| `/rest/wmsc2agent/select/order/page` | GET | Get order status | Yes |
| `/rest/wmsc2agent/get/shipment` | POST | Get shipping methods | Yes |

## Common Parameters

**All Endpoints:**
- `key` - API key
- `timestamp` - Unix timestamp
- `nonce` - Random 16-char string
- `signature` - SHA-1 signature

**Product Queries:**
- `currency` - USD, CNY, EUR, HKD (default: CNY)
- `page_size` - 1-100 (default: 100)
- `current_page` - Page number (default: 1)

**Filters:**
- `is_available` - 0=all, 1=in stock, 2=out of stock
- `is_pre_sale` - 0=all, 1=include pre-sale, 2=exclude pre-sale
- `match_type` - 0=exact, 1=fuzzy search (default: 1)

## Response Format

All responses follow this structure:
```json
{
  "success": true|false,
  "code": 200|ERROR_CODE,
  "message": "description",
  "result": { ... }
}
```

Success codes: 200
Error codes: 400, 401, 403, 404, 424-431, 500

## Search Examples

**Search by Part Number:**
```
GET /rest/wmsc2agent/search/product
?key=xxx&timestamp=xxx&nonce=xxx&signature=xxx
&keyword=TL072CP
&currency=USD
```

**Get Product Details:**
```
GET /rest/wmsc2agent/product/info/C123456
?key=xxx&timestamp=xxx&nonce=xxx&signature=xxx
&currency=USD
```

**List Category Products:**
```
GET /rest/wmsc2agent/category/product/12
?key=xxx&timestamp=xxx&nonce=xxx&signature=xxx
&page_size=100&current_page=1
&is_available=1&currency=USD
```

## Response Fields

**Product Object:**
- `product_number` - LCSC SKU (C123456)
- `product_model` - Manufacturer part number
- `product_name` - Product description
- `brand_name` - Manufacturer name
- `encapsulation` - Package type (DIP-8, SOIC-8, etc.)
- `datasheet` - URL to datasheet PDF
- `prices[]` - Array of tiered pricing
- `stock[]` - Array of stock by location
- `attributes[]` - Technical specifications
- `images[]` - Product images and datasheets

**Price Object:**
- `quantity` - Quantity tier
- `price` - Unit price
- `currency` - Currency code

**Stock Object:**
- `location` - Warehouse location (Js, Sz, etc.)
- `amount` - Available quantity

## Error Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad request |
| 401 | Unauthorized |
| 403 | Forbidden/no access |
| 404 | Not found |
| 424 | Missing key parameter |
| 425 | Missing nonce parameter |
| 426 | Missing timestamp parameter |
| 427 | Missing signature parameter |
| 430 | Signature verification failed |
| 431 | No access to information |
| 500 | Server error |

## Key Notes

- **Base URL:** https://ips.lcsc.com
- **Timestamp:** Must be within 60 seconds of server time
- **Nonce:** Should be 16 random characters
- **Signature:** SHA-1 hash of "key=X&nonce=Y&secret=Z&timestamp=W"
- **Rate Limit:** No documented limit, but implement backoff
- **Max Results:** 100 per page, use pagination for larger sets
- **Currency:** Always specify currency for pricing

## Setup Checklist

- [ ] Register business/agent account at lcsc.com
- [ ] Apply for API access via lcsc.com/agent
- [ ] Submit application to support@lcsc.com
- [ ] Receive API key and secret
- [ ] Implement signature generation
- [ ] Sync server time (NTP)
- [ ] Test with Category API
- [ ] Implement error handling
- [ ] Add request logging

## Alternative: Unauthenticated Global Search

**Endpoint:** `GET https://wwwapi.lcsc.com/v1/search/global-search`

**Parameters:**
- `keyword` - Search term (no auth required!)

**Advantages:**
- No authentication
- Simple integration
- Community-documented

**Risk:**
- Not officially published
- May change without notice
- Use for read-only searches only
