# Mouser Electronics Search API

## Overview

Mouser Electronics provides a public Search API for programmatic access to their electronic components catalog. The API supports keyword and part number searches, returning detailed product information including pricing, availability, and datasheets.

## Key Features

- **Keyword Search**: Find parts by description, family name, or parameters
- **Part Number Search**: Exact or partial part number lookup
- **JSON/XML Responses**: Both formats supported, JSON recommended
- **Real-time Data**: Live pricing, inventory, and lead times

## API Hub

- **Main Portal**: https://www.mouser.com/api-hub/
- **Search API**: https://www.mouser.com/api-search/
- **Order API**: https://www.mouser.com/api-order/
- **Terms of Service**: https://www.mouser.com/apiterms/

## Rate Limits

| Limit | Value |
|-------|-------|
| Results per call | 50 max |
| Calls per minute | 30 |
| Calls per day | 1,000 |

Higher limits may be negotiated directly with Mouser for commercial applications.

## Related APIs

Mouser also provides:
- **Cart API** - Automate cart creation and updates
- **Order API** - Place and manage orders programmatically

Each API requires separate registration and has its own documentation.

## Getting Started

1. Create a [My Mouser](https://www.mouser.com/) account
2. Complete the Search API Request Form
3. Receive your API key via email
4. Start making API calls

## Sources

- [Mouser Search API](https://www.mouser.com/api-search/)
- [Mouser API Hub](https://www.mouser.com/api-hub/)
- [sparkmicro/mouser-api](https://github.com/sparkmicro/mouser-api)
