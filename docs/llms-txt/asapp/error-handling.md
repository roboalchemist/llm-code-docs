# Source: https://docs.asapp.com/getting-started/developers/error-handling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Handling

> Learn how ASAPP returns Errors in the API

When you make an API call to ASAPP and there is an error, you will receive a non `2XX` HTTP status code.

All errors return a `message`, `code`, and `requestId` for that request to help you debug the issue.

The message will usually contain enough information to help you resolve the issue. If you require further help, reach out to support, including the requestId so that they can pinpoint the specific failing API call.

## Error Structure

| Field           | Type   | Description                                                                  |
| :-------------- | :----- | :--------------------------------------------------------------------------- |
| error           | object | The main error object containing details about the error                     |
| error.requestId | string | A unique identifier for the request that generated this error                |
| error.message   | string | A detailed description of the error, including the specific validation issue |
| error.code      | string | An error code in the format "HTTP\_STATUS\_CODE-ERROR\_SUBCODE"              |

Here is an example where a timestamp in the request has an incorrect format.

```json  theme={null}
{
  "error":{
    "requestId":"3851a807-f0c3-4873-8ba6-5bad4261f0ca3100",
    "message":"ERROR - [Path '/timestamp'] String 2024-08-14T00:00:00.000K is invalid against requested date format(s) [yyyy-MM-dd'T'HH:mm:ssZ, yyyy-MM-dd'T'HH:mm:ss.[0-9]{1,12}Z]: []]",
    "code":"400-03"
  }
}
```
