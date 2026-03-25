# Source: https://docs.ghost.org/admin-api/offers/updating-an-offer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating an Offer

For existing offers, only `name` , `code`, `display_title` and `display_description` are editable.

The example updates `display title` and `code`.

<RequestExample>
  ```json  theme={"dark"}
  // PUT /admin/offers/{id}/
  {
      "offers": [
          {
              "display_title": "Black Friday 2022",
              "code": "black-friday-2022"
          }
      ]
  }
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).