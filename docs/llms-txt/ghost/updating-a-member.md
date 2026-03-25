# Source: https://docs.ghost.org/admin-api/members/updating-a-member.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating a member

```js  theme={"dark"}
PUT /admin/members/{id}/
```

All writable fields of a member can be updated. It’s recommended to perform a `GET` request to fetch the latest data before updating a member.

A minimal example for updating the name of a member.

<RequestExample>
  ```json  theme={"dark"}
  // PUT /admin/members/{id}/
  {
      "members": [
          {
              "name": "Jamie II"
          }
      ]
  }
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).