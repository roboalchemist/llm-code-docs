# Source: https://screenshotone.com/docs/errors/name-not-resolved/

# Name Not Resolved

It is an API error returned when the domain name of the requested URL cannot be resolved.

```json
{
    "is_successful": false,
    "error_code": "name_not_resolved",
    "error_message": "Usually, the error happens when the domain name of the requested URL is not resolved. If you are trying to take a screenshot of a new site, please, wait a bit until the DNS records are refreshed.",
    "documentation_url": "https://screenshotone.com/docs/errors/name-not-resolved/"
}
```

## Reasons and how to fix

### Unresolved Domain Name

The most common reason for the "name_not_resolved" error is that the domain name of the requested URL cannot be resolved to an IP address. This often occurs with new domains or recently updated DNS records.

To fix this, you can:

1. **Wait for the DNS propagation if it is your website**: If you are trying to take a screenshot of a new site, wait for the DNS records to propagate fully. This can take anywhere from a few minutes to 48 hours.
2. **Or check DNS configuration**: Ensure that the DNS configuration for the domain is correct and that the records are properly set up.

### Temporary DNS Issues

Temporary DNS issues can also cause the "name_not_resolved" error. These can be due to network problems, DNS server issues, or other transient conditions.

To fix this, consider simply retrying the request after a short wait

### Incorrect Domain Name

If the domain name is incorrectly typed or does not exist, the API will not be able to resolve it.

To fix this, verify that the domain name in the request is correct and exists.

## Reach out to support

If you continue to face issues or need further assistance, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.