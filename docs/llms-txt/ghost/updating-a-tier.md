# Source: https://docs.ghost.org/admin-api/tiers/updating-a-tier.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating a Tier

```js  theme={"dark"}
PUT /admin/tiers/{id}/
```

Required fields: `name`

Update all writable fields of a tier by using the edit endpoint. For example, rename a tier or set it as archived with this endpoint.

<RequestExample>
  ```json  theme={"dark"}
  // PUT /admin/tiers/{id}/
  {
      "tiers": [
          {
              "name": "Silver",
              "description": "silver"
          }
      ]
  }
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).