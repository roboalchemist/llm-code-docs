# Source: https://developers.smtp2go.com/reference/general-api-resources.md

# General API Resources

> 📘 ## **Welcome** to the SMTP2GO API Docs 👋
>
> The SMTP2GO API offers you an enhanced level of control and monitoring of your SMTP2GO account.

## Endpoints

API calls must be prefixed with one of the following base URL's:

| Region              | Base URL                                                       |
| :------------------ | :------------------------------------------------------------- |
| US (United States)  | [https://us-api.smtp2go.com/v3](https://us-api.smtp2go.com/v3) |
| EU (European Union) | [https://eu-api.smtp2go.com/v3](https://eu-api.smtp2go.com/v3) |
| AU (Oceania)        | [https://au-api.smtp2go.com/v3](https://au-api.smtp2go.com/v3) |
| Global              | [https://api.smtp2go.com/v3](https://api.smtp2go.com/v3)       |

If you send your requests to the 'Global' endpoint, the API will automatically choose the US, EU or AU endpoint based on which is closest to the request origin (based on where your DNS resolver is located). We recommend using region-specific endpoints where possible, to ensure you connect to the region closest to you.

## Technical Details

To work with the API, please be sure to adhere to the following guides:

* Use the appropriate HTTP method for the call e.g. <span class="APIMethod APIMethod_fixedWidth APIMethod_post Sidebar-methodfUM3m6FEWm6w" data-testid="http-method">post</span> or <span class="APIMethod APIMethod_fixedWidth APIMethod_patch Sidebar-methodfUM3m6FEWm6w" data-testid="http-method">patch</span>.
* All requests should be in the form of JSON.
* All requests must include the **api\_key** field, or choose to use the **X-Smtp2go-Api-Key** field in your header, as shown below.

```json Example api_key field
{
    "api_key": "YourAPIKeyHere",
    "search_subject": "Booking",
    "event_types": ["opened", "clicked"],
    "only_latest": true,
    "limit": 1
}
```

```json Example Headers
{
  'Content-Type': 'application/json',
  'X-Smtp2go-Api-Key': 'YourAPIKeyHere'
}
```

## Response Codes

SMTP2GO uses conventional HTTP response codes to indicate the success or failure of a request.

In general, codes in the `2xx` range indicate success. Codes in the `4xx` range indicate an error and reasons the request may have failed are given in the information provided. Codes in the `5xx` range indicate an error with SMTP2GO's servers (these are rare and if encountered please contact support for assistance).

Below is a list of status codes and their corresponding definitions:

| Status Code                                | Definition                                                                                       |
| :----------------------------------------- | :----------------------------------------------------------------------------------------------- |
| `200` - OK                                 | Everything worked as expected.                                                                   |
| `400` - Bad Request                        | The request was unacceptable, often due to missing a required parameter.                         |
| `401` - Unauthorized                       | No valid API key provided.                                                                       |
| `402` - Request Failed                     | The parameters were valid but the request failed.                                                |
| `403` - Forbidden                          | The API key doesn't have permissions to perform the request.                                     |
| `404` - Not Found                          | The requested resource doesn't exist.                                                            |
| `429` - Too Many Requests                  | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. |
| `500`, `502`, `503`, `504` - Server Errors | Something went wrong on SMTP2GO's end. (These are rare.)                                         |

Additional information is contained in the response body as in the following examples.

```json Common Error Response Example
{
   "error": "Failed to remove the single sender email - An error occurred deleting sender email asdfa@asdf.com or it doesn't exist",
   "error_code": "E_ApiResponseCodes.API_EXCEPTION"
}
```

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

## Rate Limiting

The `/activity/search` endpoint has a rate limit of 60 per minute. If you need realtime access to a data, you should make use of [Webhooks](https://developers.smtp2go.com/docs/webhooks-overview).

In the event that your interaction with the API results in what we deem to be too many requests or error responses, the IP address from which the requests originated will be timed out for an indeterminate amount of time, no less than 1 minute.

You will receive a `429 Too Many Requests` response code during this time. If you begin to see these responses, pause and lower your request rate until you begin to see `200 OK` returned. Should you start receiving `429 Too Many Requests`, also ensure the requests you are sending are returning `200 OK`.

## Points to note

### Maximum email size

The maximum email size when sending via the API is 50 MB (this includes content, attachments and headers).

### Maximum number of recipients per email

The maximum number of recipients per email for each of the To, CC and BCC fields is 100. It is important to note that each recipient will count as one email from your plan's monthly quota.

### Subaccounts

Certain API calls can be performed on subaccounts, using a parent/master account's API Key. The relevant subaccount is specified by including the '*subaccount\_id*' parameter in the API call. Currently supported endpoints mention this parameter in our documentation.