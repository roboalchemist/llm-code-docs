# Source: https://smartcar.com/docs/connect/handle-the-response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Handle the Response

> Upon successfully accepting the permissions, Smartcar will redirect the user back to your application using the specified `REDIRECT_URI`, along with an authorization code as a query parameter. In the case of an error, we'll provide an error and description as parameters instead.

## Success

<ResponseField name="code">
  An authorization code used to obtain your initial `ACCESS_TOKEN`. The auth `code` expires after **10 minutes**.
</ResponseField>

<Snippet file="response-connect-state.mdx" />

```http Success theme={null}
HTTP/1.1 302 Found
Location: https://example.com/home?
code=90abecb6-e7ab-4b85-864a-e1c8bf67f2ad
&state=0facda3319
```

## Error

For a detailed description of these errors, please see our [errors page](/api-reference/api-errors).

<ResponseField name="error">
  The type of error
</ResponseField>

<ResponseField name="error_description">
  A detailed description of what caused the error
</ResponseField>

<Snippet file="response-connect-state.mdx" />

```http Error theme={null}
HTTP/1.1 302 Found
Location: https://example.com/home?
error=access_denied
&error_description=User+denied+access+to+application.
&state=0facda3319
```

<Info>
  In addition to the error code and description, Smartcar will return the following parameters when a
  user tries to authorize an incompatible vehicle in Connect.
</Info>

<ResponseField name="vin">
  Can be returned for errors where the vehicle is incompatible.
</ResponseField>

<ResponseField name="make">
  The manufacturer of the vehicle.
</ResponseField>

<ResponseField name="model">
  The model of the vehicle.
</ResponseField>

<ResponseField name="year">
  The year of production of the vehicle.
</ResponseField>
