# Source: https://screenshotone.com/docs/errors/request-aborted/

# Request Aborted

It is an API error returned when the request was aborted either by the user or the intermediate proxies and can't be fulfilled.

```json
{
    "is_successful": false,
    "error_code": "request_aborted",
    "error_message": "The request was aborted either by the user or the intermediate proxies and can't be fulfilled. If the error persists, please, reach out to `support@screenshotone.com`.",
    "documentation_url": "https://screenshotone.com/docs/request-aborted/"
}
```

## Reasons and how to fix

### HTTP Client Timeouts

One common reason for the "request_aborted" error is HTTP client timeouts. This occurs when the client (e.g., a web browser or a server making a request) has a timeout setting that is shorter than the time it takes for the request to be processed.

To fix this, you can increase the timeout setting in your HTTP client configuration.

### Local Development Live Reloading

During local development, live reloading tools (such as those used in web development environments) may cause requests to be aborted if the server restarts or if the code is recompiled. This can lead to the "request_aborted" error.

To avoid this, ensure that you have a stable development environment and minimize the frequency of live reloads while making API requests.

### Edge Function Timeouts

If you are using edge functions or serverless functions (e.g., AWS Lambda, Vercel Edge Functions), they might have their own timeout settings. When these timeouts are exceeded, the request will be aborted, resulting in the "request_aborted" error.

To fix this, you should increase the timeout settings for your edge functions.

## Reach out to support

If nothing helps you, please, reach out to `support@screenshotone.com` and we will try to help you as fast as possible.