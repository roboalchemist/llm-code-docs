# Source: https://docs.ghost.org/admin-api/users/updating-a-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating a user

```js  theme={"dark"}
PUT /admin/users/{id}/
```

All writable fields of a user can be updated. It’s recommended to perform a `GET` request to fetch the latest data before updating a user.

<RequestExample>
  ```json  theme={"dark"}
  // PUT /admin/users/{id}/
  {
      "users": [
          {
              "name": "Cameron Larson"
          }
      ]
  }
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).