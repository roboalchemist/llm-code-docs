# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/merchant.mdx

<EndpointSchemaSnippet endpoint="POST /merchants" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
    "brand_id": "BRAND_8ereg0tug2yiik8vx24xpe5br",
    "name": "Example Business Name",
    "country": "US",
    "currency": "USD",
    "category": "5432",
    "reference_id": "external-id",
    "status": "ACTIVE",
    "created_at": "2022-01-01T12:00:00Z",
    "updated_at": "2022-01-05T12:00:00Z",
    "address": {
      "address_line_1": "1215 4th Ave",
      "address_line_2": "Suite 2300",
      "locality": "Seattle",
      "country": "US",
      "postal_code": "98161-1001",
      "administrative_district_level_1": "Washington"
    },
    "site_url": "http://example.com",
    "metadata": {}
  }
  ```
</Aside>
