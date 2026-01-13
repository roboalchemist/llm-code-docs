# Digi-Key API Documentation

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
