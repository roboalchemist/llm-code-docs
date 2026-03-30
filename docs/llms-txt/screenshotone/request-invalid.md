# Source: https://screenshotone.com/docs/errors/request-invalid/

# Request Invalid

It is an API error returned when the API fails to serve the request due to internal reasons:

```json
{
    "is_successful": false,
    "error_message": "The request parameters are not valid. You can look at the `error_details` response field to get more details.",
    "error_details": {
        // ... validation errors ...    
    },
    "error_code": "request_invalid",
    "documentation_url": "https://screenshotone.com/docs/errors/request-invalid/"
}
```

## Reasons and how to fix

### Invalid Request Parameters

The most common reason for the "request_not_valid" error is that one or more of the request parameters are invalid or missing.

To fix this, you can:

1. **Check `error_details` property**: Review the `error_details` field in the response to get specific information about which parameters are invalid.
2. **Correct request parameters**: Ensure that all required parameters are included in the request and that they are correctly formatted and valid.

### Missing Required Parameters

If required parameters are missing from the request, this will trigger the "request_not_valid" error.

To fix this, ensure that all mandatory parameters are provided in the request. Refer to the API documentation for a list of required parameters.

### Incorrect Data Types

Providing parameters with incorrect data types (e.g., a string instead of an integer) can lead to this error.

To fix this, verify that the data types of all parameters match the expected types as specified in the API documentation.

### Parameter Value Constraints

Some parameters may have constraints on their values (e.g., minimum or maximum length, specific formats). Violating these constraints will result in this error.

To fix this, check the constraints for each parameter in the API documentation and ensure that the provided values comply with these constraints.

### Syntax Errors

Syntax errors in the request, such as missing commas or brackets in JSON, can make the request invalid.

To fix this, carefully review the syntax of your request and correct any errors. Using a JSON validator can help identify syntax issues.

## Reach out to support

If you continue to face issues or need further assistance, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.