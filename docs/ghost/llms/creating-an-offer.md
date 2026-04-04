# Source: https://docs.ghost.org/admin-api/offers/creating-an-offer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating an Offer

```js  theme={"dark"}
POST /admin/offers/
```

Required fields: `name`, `code`, `cadence`, `duration`, `amount`, `tier.id` , `type`

When offer `type` is `fixed`, `currency` is also required and must match the tier’s currency. New offers are created as active by default.

Below is an example for creating an offer with all properties including prices, description, and benefits.

<RequestExample>
  ```json  theme={"dark"}
  // POST /admin/offers/
  {
      "offers": [
          {
              "name": "Black Friday",
              "code": "black-friday",
              "display_title": "Black Friday Sale!",
              "display_description": "10% off on yearly plan",
              "type": "percent",
              "cadence": "year",
              "amount": 12,
              "duration": "once",
              "duration_in_months": null,
              "currency_restriction": false,
              "currency": null,
              "status": "active",
              "redemption_count": 0,
              "tier": {
                  "id": "62307cc71b4376a976734038",
                  "name": "Gold"
              }
          }
      ]
  }
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).