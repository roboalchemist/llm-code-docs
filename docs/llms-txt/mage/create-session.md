# Source: https://docs.mage.ai/extensibility/api-reference/sessions/create-session.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create session

`POST /api/sessions`

<RequestExample>
  ```curl cURL theme={"system"}
  curl --request POST \
    --url http://localhost:6789/api/sessions \
    --header 'Content-Type: application/json' \
    --header 'X-API-KEY: zkWlN0PkIKSN0C11CfUHUj84OT5XOJ6tDZ6bDRO2' \
    --data '{
    "session": {
      "email": "admin@admin.com",
      "password": "admin"
    }
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"system"}
  {
    "session": {
      "expires": "2023-04-30 03:02:14.781970+00:00",
      "token": "...",
      "user": {
        "avatar": null,
        "first_name": null,
        "id": 1,
        "last_name": null,
        "owner": true,
        "roles": null,
        "roles_display": "Owner",
        "username": "admin"
      }
    }
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).