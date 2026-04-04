# Source: https://docs.intelligems.io/developer-resources/mcp-server/available-tools.md

# Available Tools

## Organization & Configuration

### list\_organizations

List all Intelligems organizations you have access to. Supports filtering by installation status and sorting.

**Parameters:**

* `isInstalled` (optional): Filter by installation status. Default: `true`
* `sortBy` (optional): Sort field - `"name"`, `"shopId"`, `"createdAt"`, `"lastLogin"`
* `nameContains` (optional): Filter by name (case-insensitive substring match)
* `limit` (optional): Maximum results to return

**Example response:**

```json
{
  "organizations": [
    {
      "id": "org_123abc",
      "name": "My Shopify Store",
      "shopId": "12345",
      "isInstalled": true,
      "createdAtTs": "2024-01-15T10:30:00Z",
      "lastLoginTs": "2024-12-01T14:22:00Z"
    }
  ],
  "totalCount": 5,
  "returnedCount": 5,
  "truncated": false
}
```

### get\_organization

Get detailed information about a specific organization including currency, timezone, Shopify settings, and enabled features.

**Parameters:**

* `organization` (optional): Organization name or ID. Uses current organization if omitted.

**Example response:**

```json
{
  "id": "org_123abc",
  "name": "My Shopify Store",
  "shopDomain": "mystore.myshopify.com",
  "currency": "USD",
  "timezone": "America/New_York",
  "features": ["price-testing", "content-testing", "offers"]
}
```

### list\_integrations

List all active integrations for an organization (Google Analytics, Klaviyo, Recharge, Slack, etc.).

**Parameters:**

* `enabled` (optional): Filter by enabled status
* `integrationName` (optional): Filter by exact integration name
* `nameContains` (optional): Filter by name (case-insensitive substring match)
* `limit` (optional): Maximum results to return
* `organization` (optional): Organization name or ID

**Example response:**

```json
{
  "integrations": [
    {
      "name": "google_analytics",
      "enabled": true
    },
    {
      "name": "recharge",
      "enabled": true
    }
  ]
}
```

***

## Experiences & Experiments

### search\_experiments

Search for A/B tests and experiments. Returns minimal info (id, name, status, type, timestamps, variation count) for discovery purposes.

**Parameters:**

* `status` (optional): Filter by status - `"pending"`, `"started"`, `"ended"`, `"paused"`
* `nameContains` (optional): Filter by name (case-insensitive substring match)
* `sortBy` (optional): Sort field - `"name"`, `"createdAt"`, `"lastUpdate"`, `"startedAt"`, `"endedAt"`
* `sortOrder` (optional): `"asc"` or `"desc"` (default)
* `organization` (optional): Organization name or ID

### search\_personalizations

Search for personalizations. Returns minimal info for discovery purposes.

**Parameters:** Same as `search_experiments`

### list\_experiments

Get full experiment details including variations, targeting rules, and configuration.

**Parameters:** Same as `search_experiments`

**Example response:**

```json
{
  "experiences": [
    {
      "id": "exp_456def",
      "name": "Holiday Price Test",
      "type": "experiment",
      "status": "started",
      "createdAtTs": "2024-12-01T00:00:00Z",
      "variations": [
        {
          "id": "var_1",
          "name": "Control",
          "trafficAllocation": 50
        },
        {
          "id": "var_2",
          "name": "10% Discount",
          "trafficAllocation": 50
        }
      ],
      "targeting": {
        "countries": ["US", "CA"],
        "deviceTypes": ["desktop", "mobile"]
      }
    }
  ]
}
```

### list\_personalizations

Get full personalization details including variations, targeting rules, and configuration.

**Parameters:** Same as `search_experiments`

### get\_experience

Get detailed information about a specific experience including its variations, targeting rules, and configuration.

**Parameters:**

* `id` (required): The ID of the experience
* `organization` (optional): Organization name or ID

### get\_experience\_metrics\_config

Get the configured success metrics for a specific experience (e.g., revenue, conversion rate, AOV, custom goals). Returns metric configuration, not actual performance data.

**Parameters:**

* `experienceId` (required): The ID of the experience
* `organization` (optional): Organization name or ID

### analyze\_experience

Get actual A/B test performance results, statistical significance, and compare variation performance.

**Parameters:**

* `experienceId` (required): The ID of the experience
* `view` (optional): `"overview"` for main metrics (default), `"audience"` for audience breakdown
* `audience` (optional): Segment to analyze when view is `"audience"` - `"device_type"`, `"visitor_type"`, `"country_code"`, `"source_channel"`, `"source_site"`, `"landing_page_full_path"`
* `analyticsViewType` (required): Analytics view type from the experience's `experienceAnalysis` configuration
* `start` (optional): Start date in ISO 8601 format
* `end` (optional): End date in ISO 8601 format
* `organization` (optional): Organization name or ID

**Example response:**

```json
{
  "metrics": {
    "conversionRate": {
      "control": 3.2,
      "variation": 3.8,
      "lift": 18.75
    },
    "revenue": {
      "control": 15420.50,
      "variation": 17892.30,
      "lift": 16.03
    },
    "confidence": 95.2
  }
}
```

***

## Shopify Store Data

### search\_products

Search the Shopify product catalog by keyword, name, or description.

**Parameters:**

* `query` (required): Search term for product title, description, or tags
* `limit` (optional): Maximum results (default: 20)
* `organization` (optional): Organization name or ID

**Example response:**

```json
{
  "results": [
    {
      "id": "7234567890",
      "title": "Organic Cotton T-Shirt",
      "vendor": "My Brand",
      "price": "29.99",
      "variants": 3,
      "tags": ["organic", "sustainable"]
    }
  ],
  "query": "organic cotton"
}
```

### list\_collections

Browse or search product collections in the Shopify store.

**Parameters:**

* `first` (optional): Number of collections to fetch (default: 20)
* `after` (optional): Cursor for pagination
* `query` (optional): Search filter for collection name
* `organization` (optional): Organization name or ID

**Example response:**

```json
{
  "collections": [
    {
      "id": "123456789",
      "title": "Holiday Collection",
      "handle": "holiday-collection",
      "productsCount": 24
    }
  ],
  "pageInfo": {
    "hasNextPage": true,
    "endCursor": "abc123"
  },
  "totalFetched": 20
}
```

### list\_pages

Browse or search content pages in the Shopify store (About, Contact, FAQ, Terms, etc.).

**Parameters:**

* `first` (optional): Number of pages to fetch (default: 20)
* `after` (optional): Cursor for pagination
* `query` (optional): Search filter for page title
* `organization` (optional): Organization name or ID

**Example response:**

```json
{
  "pages": [
    {
      "id": "987654321",
      "title": "About Us",
      "handle": "about-us"
    }
  ],
  "pageInfo": {
    "hasNextPage": false
  },
  "totalFetched": 5
}
```

### search\_policies

Search store policies, FAQs, shipping info, returns, privacy, and other store rules.

**Parameters:**

* `query` (required): Search term
* `organization` (optional): Organization name or ID

***

## Analytics & Audience Data

All audience analysis tools require an experience ID and return performance metrics broken down by the specified segment.

### get\_audience\_by\_country

Analyze A/B test performance by visitor country/geography.

**Parameters:**

* `id` (required): The experience ID
* `organization` (optional): Organization name or ID

### get\_audience\_by\_device

Analyze A/B test performance by device type (desktop, mobile, tablet).

**Parameters:**

* `id` (required): The experience ID
* `organization` (optional): Organization name or ID

### get\_audience\_by\_visitor\_type

Compare A/B test performance between new and returning visitors.

**Parameters:**

* `id` (required): The experience ID
* `organization` (optional): Organization name or ID

### get\_audience\_by\_source\_channel

Analyze A/B test performance by traffic acquisition channel (organic, paid, social, email, direct).

**Parameters:**

* `id` (required): The experience ID
* `organization` (optional): Organization name or ID

### get\_audience\_by\_source\_site

Analyze A/B test performance by referring website/domain.

**Parameters:**

* `id` (required): The experience ID
* `organization` (optional): Organization name or ID

### get\_audience\_by\_landing\_page

Analyze A/B test performance by landing page URL.

**Parameters:**

* `id` (required): The experience ID
* `organization` (optional): Organization name or ID

**Example response (applies to all audience tools):**

```json
{
  "summary": {
    "segments": [
      {
        "segment": "US",
        "visitors": 15420,
        "conversions": 892,
        "conversionRate": 5.79,
        "revenue": 45230.50
      },
      {
        "segment": "CA",
        "visitors": 3240,
        "conversions": 187,
        "conversionRate": 5.77,
        "revenue": 12450.00
      }
    ]
  }
}
```

***

## Custom Events

### list\_custom\_events

List all custom tracking events configured for your organization. Includes page views, click events, scroll depth tracking, and custom JavaScript events.

**Parameters:**

* `organization` (optional): Organization name or ID

**Example response:**

```json
{
  "customEvents": [
    {
      "name": "add_to_wishlist",
      "type": "custom",
      "description": "User adds product to wishlist"
    },
    {
      "name": "scroll_depth_50",
      "type": "scroll",
      "description": "User scrolled 50% of page"
    }
  ]
}
```

***

## Offers

### list\_offers

List all offers configured for your organization. Includes tiered discounts, cart discounts, free gifts, and free shipping.

**Parameters:**

* `enabled` (optional): Filter by enabled status
* `isTest` (optional): Filter by test mode status
* `isArchived` (optional): Filter by archived status
* `applicationType` (optional): Filter by discount application type
* `nameContains` (optional): Filter by name (case-insensitive substring match)
* `limit` (optional): Maximum results to return
* `organization` (optional): Organization name or ID

**Example response:**

```json
{
  "offers": [
    {
      "id": "offer_789ghi",
      "name": "Free Shipping Over $50",
      "discountApplicationType": "free_shipping",
      "enabled": true,
      "isTest": false,
      "isArchived": false
    }
  ]
}
```
