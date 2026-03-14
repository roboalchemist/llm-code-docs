# Source: https://developers.smtp2go.com/docs/response-codes.md

# Response Codes

SMTP2GO uses conventional HTTP response codes to indicate the success or failure of a request.

In general, codes in the `2xx` range indicate success. Codes in the `4xx` range indicate an error and reasons the request may have failed are given in the information provided. Codes in the `5xx` range indicate an error with SMTP2GO's servers (these are rare and if encountered please contact support for assistance).

Below is a list of status codes and their corresponding definitions:

## Status Codes

| Status Code                                                | Definition                                                                                       |
| :--------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **`200`** - OK                                             | Everything worked as expected.                                                                   |
| **`400`** - Bad Request                                    | The request was unacceptable, often due to missing a required parameter.                         |
| **`401`** - Unauthorized                                   | No valid API key was provided.                                                                   |
| **`402`** - Request Failed                                 | The parameters were valid but the request failed.                                                |
| **`403`** - Forbidden                                      | The API key doesn't have permission to perform the request.                                      |
| **`404`** - Not Found                                      | The requested resource doesn't exist.                                                            |
| **`429`** - Too Many Requests                              | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. |
| **`500`**, **`502`**, **`503`**, **`504`** - Server Errors | Something went wrong on SMTP2GO's end (these are rare).                                          |

<br />

Additional information is contained in the response body, as in the following examples

```json Common Error Response Example
{
   "error": "Failed to remove the single sender email - An error occurred deleting sender email asdfa@asdf.com or it doesn't exist",
   "error_code": "E_ApiResponseCodes.API_EXCEPTION"
}
```

## Error Codes

Some errors contain additional field validation error information, as below.

```json Common Error Response Example
{
   "error": "An error occurred processing the json data you sent with the request, please make sure the data conforms to the specification for this call (see the documentation here: https://apidoc.smtp2go.com/documentation/#/README) and try again. Don't forget to set Content-Type to 'application/json'.",
   "error_code": "E_ApiResponseCodes.NON_VALIDATING_IN_PAYLOAD",
   "field_validation_errors": {
      "fieldname": "sender",
      "message": "The field 'sender' was expecting a valid RFC-822 formatted email field but found 'robs_invalid.com', Please correct your JSON payload and try again."
   }
}
```

For more detailed explanations of common Error Codes when sending, try our [Common Sending Errors](https://support.smtp2go.com/hc/en-gb/articles/13990494697369-Common-Sending-Errors) knowledgebase article or reach out to our [support team](https://www.smtp2go.com/contact/) for assistance.