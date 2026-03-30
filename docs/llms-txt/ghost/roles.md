# Source: https://docs.ghost.org/admin-api/users/roles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Roles

The roles resource provides an endpoint for fetching role data.

<RequestExample>
  ```json  theme={"dark"}
  // GET /admin/roles/
  {
      "roles": [
          {
              "id": "64498c2a7c11e805e0b4ad4b",
              "name": "Administrator",
              "description": "Administrators",
              "created_at": "1920-01-01T00:00:00.000Z",
              "updated_at": "1920-01-01T00:00:00.000Z"
          },
          ...
      ]
  }
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).