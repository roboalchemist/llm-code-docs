# Source: https://docs.ghost.org/admin-api/tiers/creating-a-tier.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating a Tier

```js  theme={"dark"}
POST /admin/tiers/
```

Required fields: `name`

Create public and hidden tiers by using this endpoint. New tiers are always set as `active` when created.

The example below creates a paid Tier with all properties including custom monthly/yearly prices, description, benefits, and welcome page.

<RequestExample>
  ```json  theme={"dark"}
  // POST /admin/tiers/
  {
      "tiers": [
          {
              "name": "Platinum",
              "description": "Access to everything",
              "welcome_page_url": "/welcome-to-platinum",
              "visibility": "public",
              "monthly_price": 1000,
              "yearly_price": 10000,
              "currency": "usd",
              "benefits": [
                  "Benefit 1",
                  "Benefit 2"
              ]
          }
      ]
  }
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).