# Source: https://screenshotone.com/docs/errors/network-error/

# Network Error

It is an API error returned when the API cannot connect to the target host.

```json
{
    "is_successful": false,
    "error_code": "network_error",
    "error_message": "The error happens when the API can't connect to the provided URL. It might mean that the site blocks the API or is temporarily unavailable. Generally, you can safely retry to take a screenshot.",
    "documentation_url": "https://screenshotone.com/docs/errors/network-error/"
}
```

## Reasons and how to fix

### Proxy issues

If you use an external [proxy](/docs/guides/how-to-use-proxies/), make sure that it has access to the target host.

Also, often when you use proxy providers, you might not notice that you don't have sufficient credits to keep using proxy.

We noticed that for some providers, you sometimes need to recreate your proxy user/account to make it work again.

Also, many providers might block ScreenshotOne API IP addresses. In that case, consider adding [our IP ranges](/docs/ip-ranges/) to the proxy provider's allow list.

### The API is under heavy load

Rarely but under heavy load, ScreenshotOne API might fail to connect to target hosts. In that case, retry requests.

## Reach out to support

If nothing helps you, please, reach out to `support@screenshotone.com` and we will try to help you as fast as possible.