# Source: https://smartcar.com/docs/connect/redirect-to-connect.md

# Source: https://smartcar.com/docs/connect/re-auth/redirect-to-connect.md

# Redirect to Connect

There will be times when a user updates credentials to their connected services account. When this happens, the user will need to go through Connect
again to update your authorization through Smartcar.

You can do this with a streamlined Connect flow using a special re-auth URL with the parameters below.

<Tip>
  The [`AUTHENTICATION_FAILED`](/errors/api-errors/connected-services-account-errors#authentication-failed) API error contains a partially constructed re-authentication URL in the `resolution.url` field.
</Tip>

<br />

<ParamField path="client_id" type="string" required>
  The application’s unique identifier.
</ParamField>

<ParamField path="redirect_uri" type="string" required>
  The URI a user will be redirected to after authorization. This value **must** match one of the redirect URIs set in the credentials tab of the dashboard.

  The first redirect URI you add to your application is automatically set as the default. If you do not specify a `redirect_uri` in your Connect URL, Smartcar will use this default URI. You can add multiple URIs and set any of them as the default in the Smartcar Dashboard.
</ParamField>

<ParamField path="response_type" type="string" required>
  This value must be set to `vehicle_id`.
</ParamField>

<ParamField path="vehicle_id" type="string" required>
  The id of the vehicle you are reauthenticating.
</ParamField>

<ParamField path="state" type="string">
  An optional value included as a query parameter in the redirect\_uri back to your application. This value is often used to identify a user and/or prevent cross-site request forgery
</ParamField>

<ParamField query="user" type="string">
  Specify a unique identifier for the vehicle owner to track and aggregate analytics across Connect sessions for each vehicle owner on Dashboard.

  Note: Use the `state` parameter in order to identify the user at your callback URI when receiving an authorization or error code after the user exits the Connect flow.
</ParamField>

<RequestExample>
  ```http Connect URL Example theme={null}
  HTTP/1.1 302 Found
  Location: https://connect.smartcar.com/oauth/reauthenticate?
    response_type=vehicle_id
    &client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07
    &vehicle_id=sc4a1b01e5-0497-417c-a30e-6df6ba33ba46
    &redirect_uri=https://example.com/home
    &state=0facda3319
  ```
</RequestExample>
