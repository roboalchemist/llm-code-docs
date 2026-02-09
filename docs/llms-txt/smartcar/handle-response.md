# Source: https://smartcar.com/docs/connect/re-auth/handle-response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Handle the Response

> If the re-auth is successful, the redirect to your application will contain a vehicle ID. In the case of an error, we'll provide an error and description as parameters instead.

## Success

<ResponseField name="vehicle_id">
  Unique identifier for a vehicle on Smartcar’s platform.
</ResponseField>

<Snippet file="response-connect-state.mdx" />

```http Success theme={null}
HTTP/1.1 302 Found
Location: https://example.com/home?
vehicle_id=sc4a1b01e5-0497-417c-a30e-6df6ba33ba46
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
