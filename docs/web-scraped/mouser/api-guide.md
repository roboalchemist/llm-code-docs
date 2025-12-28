# Source: https://www.mouser.com/api-hub/ and https://www.mouser.com/pdfDocs/api-guide.pdf

# Mouser API Hub Documentation

Mouser's API Hub provides programmatic access to electronic component data, cart management, ordering, and order history through RESTful APIs.

## Overview

The Mouser API Hub hosts four primary APIs designed to integrate product data, cart management, and ordering capabilities into external applications:

1. **Search API** - Access product data, availability, and pricing
2. **Cart API** - Automate cart building and management
3. **Order API** - Place orders programmatically
4. **Order History API** - View previous order information

## Getting Started

### API Keys

You need to request separate API keys for different API groups:
- One key for Cart and Order APIs
- One key for Search API

Request API keys through:
- Cart/Order API: https://www.mouser.com/api-cart/
- Search API: https://www.mouser.com/api-search/

### Base URL

All API endpoints use the base URL format:
```
https://api.mouser.com/api/v{version}/
```

### Authentication

API requests require authentication using your API key. The key should be included in request headers or as a query parameter (refer to specific API documentation for details).

## Search API

**Documentation:** https://www.mouser.com/api-search/

The Search API enables access to Mouser's extensive product catalog with real-time availability and pricing information.

### Available Data

The Search API provides:
- Mouser part numbers
- Manufacturer part numbers
- Product availability (real-time stock levels)
- Pricing information (up to 4 price breaks)
- Data sheet URLs
- Product images
- Product categories and taxonomies
- Lead times
- Product lifecycle status
- RoHS compliance status
- Suggested replacement parts

### Use Cases

- Build custom search interfaces
- Integrate product data into procurement systems
- Create automated inventory management tools
- Display real-time pricing and availability

## Cart API

**Documentation:** https://www.mouser.com/api-cart/

The Cart API automates cart building processes, allowing you to create, update, and manage shopping carts programmatically.

### Features

- Create new carts
- Add parts to existing carts
- Update cart quantities
- Remove items from carts
- Retrieve cart contents
- Manage multiple carts

### Use Cases

- Automated BOM (Bill of Materials) cart creation
- Batch ordering workflows
- Integration with design tools and PLM systems
- Quick reordering from saved BOMs

## Order API

**Documentation:** https://www.mouser.com/api-order/

The Order API provides access to Mouser's checkout process, enabling order placement within custom applications.

### Supported HTTP Methods

Currently supports:
- **GET** - Retrieve order information
- **POST** - Submit new orders and query options

### Key Endpoints

#### Query Order Options
```
POST /api/v{version}/order/options/query
```

Returns available order options including:
- Billing addresses
- Shipping addresses
- Currency codes
- Shipping methods with rates
- Payment methods
- Freight account information
- Tax certificates
- VAT account details
- Saved credit cards

#### Get Order Details
```
GET /api/v{version}/order/{orderNumber}
```

Retrieves complete details for a specific order by order number.

### Use Cases

- Automate procurement workflows
- Integrate with ERP systems
- Create custom checkout experiences
- Streamline purchasing processes

## Order History API

**Documentation:** https://www.mouser.com/api-orderhistory/

The Order History API allows you to view all previous orders within your own application.

### Features

- Retrieve historical order data
- Access order details and line items
- Track order status
- View shipping information
- Export order history for reporting

### Use Cases

- Build custom reporting dashboards
- Integrate with accounting systems
- Track purchasing patterns
- Automate reconciliation processes

## API Explorer

Mouser provides an interactive API Explorer that allows you to:
- View all available endpoints
- Edit request parameters in web forms
- See sample request and response bodies
- Test API requests directly (note: orders placed through the explorer are real and will be charged to your account)

**Access:** Available through individual API documentation pages

## Best Practices

### Rate Limiting

Be respectful with API usage:
- Implement appropriate rate limiting in your applications
- Cache responses when appropriate
- Use batch operations where available

### Error Handling

Implement robust error handling for:
- Authentication failures
- Rate limit exceeded responses
- Invalid request parameters
- Service availability issues

### Data Freshness

- Product availability changes in real-time
- Pricing may vary based on quantity and promotions
- Always validate data before placing orders
- Use the Order Options endpoint to get current shipping and payment methods

## Support and Resources

- **API Solutions Page:** https://www.mouser.com/api-solutions/
- **API Guide PDF:** https://www.mouser.com/pdfDocs/api-guide.pdf
- **API Hub:** https://www.mouser.com/api-hub/

## Additional Resources

### GitHub Resources

Third-party API wrappers and tools:
- **sparkmicro/mouser-api** - Community-developed API wrapper

### Integration Examples

For integration examples and use cases, refer to:
- Parts management systems (e.g., PartsBox integration capabilities)
- Custom procurement tools
- Design automation workflows

## Terms and Conditions

When using Mouser APIs:
- Test thoroughly in development before production deployment
- Understand that API Explorer creates real orders
- Comply with Mouser's API terms of service
- Protect your API keys and credentials
- Report any security issues to Mouser immediately

---

**Last Updated:** 2025-12-28
**API Version:** Check individual API documentation for current version numbers
**Support:** Contact Mouser for API-specific support and technical questions
