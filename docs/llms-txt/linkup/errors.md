# Source: https://docs.linkup.so/pages/documentation/development/errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Errors

> Linkup API errors and how to handle them

This guide includes an overview of error codes you might see from both the API and our SDKs.

## API Errors

Whatever the HTTP error code is, the response payload will contain the following object:

**`statusCode`**: number - HTTP error code.

**`error`**: object - Linkup error details containing:

* **`code`**: string - Error name
* **`message`**: string - Description of the error
* **`details`**: array - Details of the error. This array may be empty or include objects with the following properties:
  * **`field`**: string - The field that caused the error
  * **`message`**: string - A description of the field error

Here is an example:

```json  theme={null}
{
	"statusCode": 400,
	"error": {
		"code": "VALIDATION_ERROR",
		"message": "Validation failed",
		"details": [
			{
				"field": "outputType",
				"message": "outputType must be one of the following values: sourcedAnswer, searchResults, structured"
			}
		]
	}
}
```

**API Error Codes**

| Code                        | Possible Reasons                                                                                                                                                                                     |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400 - Bad Request           | <ul><li>Required parameter is missing</li><li>Invalid parameter</li><li>Search query yields no result</li><li>Fetch request targets a web page > 20MB</li><li>Fetch request targets a file</li></ul> |
| 401 - Unauthorized          | API Key is missing or invalid                                                                                                                                                                        |
| 403 - Forbidden             | API key does not have permission to access this resource                                                                                                                                             |
| 409 - Conflict              | Resource conflict (e.g., duplicate entry or conflicting request)                                                                                                                                     |
| 429 - Too Many Requests     | You have run out of credit or you are sending too many concurrent requests                                                                                                                           |
| 500 - Internal Server Error | Something's up on our end                                                                                                                                                                            |

## SDK Errors

**Python & JS SDK Error Types**

| Type                               | Reason                                                                             |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| `LinkupInvalidRequestError`        | Required parameter is missing, or invalid parameter                                |
| `LinkupNoResultError`              | Search query yield no result                                                       |
| `LinkupAuthenticationError`        | API Key is missing, invalid or you do not have permission to access this ressource |
| `LinkupInsufficientCreditError`    | You have run out of credit                                                         |
| `LinkupTooManyRequestsError`       | You are sending too many concurrent requests                                       |
| `LinkupFetchError`                 | The provided URL might not be found or can't be fetched                            |
| `LinkupFetchResponseTooLargeError` | The provided URL's response is too large to be processed (>20MB)                   |
| `LinkupFetchUrlIsFileError`        | The provided URL points to a file and not a web page                               |
| `LinkupUnknownError`               | Anything else                                                                      |


Built with [Mintlify](https://mintlify.com).