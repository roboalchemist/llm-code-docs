# Source: https://screenshotone.com/docs/errors/signature-is-invalid/

# Signature Invalid

It is an API error returned when the provided signature parameter is not valid.

```json
{
    "is_successful": false,
    "error_code": "signature_is_not_valid",
    "error_message": "You provided the `signature` parameter, but it is not valid. Make sure you use the correct signing algorithm—https://screenshotone.com/docs/signed-requests/.",
    "documentation_url": "https://screenshotone.com/docs/errors/signature-is-invalid/"
}
```

## Reasons and how to fix

### Incorrect Signing Algorithm

The most common reason for the "signature_is_not_valid" error is using an incorrect signing algorithm to generate the signature.

To fix this, you can:

1. **Verify signing algorithm**: Ensure you are using the correct signing algorithm as specified in the [signed requests documentation](https://screenshotone.com/docs/signed-requests/).
2. **Check signature generation code**: Review your code that generates the signature to ensure it follows the correct algorithm and procedure.

### Mismatched Signature

The signature provided in the request might not match the expected signature due to data mismatches or incorrect key usage.

To fix this, consider:

1. **Verify request data**: Ensure that all data used to generate the signature matches the data sent in the request.
2. **Use correct secret key**: Ensure that the correct secret key is used to generate the signature.

### Signature Formatting Issues

Formatting issues, such as encoding problems or extra characters, can lead to an invalid signature.

To fix this, verify that the signature is correctly formatted and encoded as required by the API.

### Debugging Signature Issues

If you are still encountering issues, you can use debugging tools or logging to trace the signature generation process and identify where it might be going wrong.

## Reach out to support

If you continue to face issues or need further assistance, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.