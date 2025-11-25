# Source: https://smartcar.com/docs/api-reference/user.md

# User

> Returns the ID of the vehicle owner who granted access to your application.

<Note>
  This endpoint is under a different path while we complete the transition to v3.0. You can safely continue using this endpoint, but please be aware that it may be deprecated in the future.
</Note>

This should be used as the static unique identifier for storing the access token and refresh token pair in your database.
Note: A single user can own multiple vehicles, and multiple users can own the same vehicle.

<Info>
  When using Single Select for Connect, a single user with multiple vehicles
  will have a 1:1 (`access_token`:`vehicle_id`) mapping.
</Info>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/user.mdx" />
</RequestExample>

## Response

<ResponseField name="id" type="string">
  A user ID (UUID v4).
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "id": "e0514ef4-5226-11e8-8c13-8f6e8f02e27e"
  }   
  ```
</ResponseExample>
