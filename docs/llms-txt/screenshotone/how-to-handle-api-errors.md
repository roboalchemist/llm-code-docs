# Source: https://screenshotone.com/docs/guides/how-to-handle-api-errors/

# How to handle API errors

Error handling is an essential part of any high-quality application. Make sure you handle all errors returned by the ScreenshotOne API correctly and provide informative explanations to your customers or react to them accordingly.

## Following HTTP standards

The ScreenshotOne API is on-purpose built using HTTP protocol and follows HTTP standards as much as possible. To make sure the API will be stable and can support customers for years to come.

In general, if the resulting status code is in the range of 400-599, then we are dealing with errors.

```
GET https://api.screenshotone.com/?[options]

Content-Type: application/json

{
    "is_successful":false,
    "error_code": "an_error_code",
    "error_message": "An error message"
}
```

## Errors caused by API consumers

All errors caused by invalid requests, absent credentials, or any reasons caused by you, an API consumer, are marked with status codes 400-499. It means, that until you find a way to fix them, the request won't be executed successfully.

## API internal errors

Errors with status codes in the range 500-599 are caused by the API internal reasons and you have almost little influence over that.

But you can safely retry them.
Except in a few cases. When you get a network error (`network_error`), it might be because the site blocks the API, and there is no sense in retrying the request. Or if the site returned an error (`host_returned_error`) and it is an error within the range 400-499, it means that the API is either blocked, or you need to change the request to the site.

You still might want to try to retry errors like `network_error` and `host_returned_error` (if the host's error is `403` in the `returned_status_code` property of the response), but try to add a residential rotating proxy to that API request. Maybe the second time you can succeed and the request will work for you.

An example of the code that retries the request with a residential rotating proxy:

```javascript
const response = await fetch(
    "https://api.screenshotone.com/take?url=https://example.com&access_key=..."
);
if (!response.ok) {
    const error = await response.json();
    if (
        // add more error codes
        error.error_code === "network_error" ||
        (error.error_code === "host_returned_error" && error.returned_status_code == 403)
    ) {
        const proxy = "http://...";
        const proxyResponse = await fetch(
            `https://api.screenshotone.com/take?url=https://example.com&access_key=...&proxy=${proxy}`
        );
        if (!proxyResponse.ok) {
            const proxyError = await proxyResponse.json();
            // you can try to retry again
        }

        // the retry was sucessful
        const screenshot = await proxyResponse.blob();
    }
}
```

## Showing errors to your end users

In general, you can try to just return the error message provided by the API, but if you want to show a more user-friendly message, you can use the following code:

```javascript 
const response = await fetch("https://api.screenshotone.com/...");

// after retries and other processing, once you decide to show an error to your end user
if (!response.ok) {
    const errorData = await response.json();

    const errorMessage = generateUserFriendlyErrorMessage(errorData);

    // show the error to your end user in your UI, CLI or any other way
    showErrorToUser(errorMessage);
}

function generateUserFriendlyErrorMessage(error) {
    // these are error messages for your public users, not for you
    switch (error.error_code) {
        case "screenshots_limit_reached":
            return "The screenshot rendering is not available. Please, retry later.";
        case "concurrency_limit_reached":
        case "temporary_unavailable":
            return "Please try again in a moment.";
        case "request_not_valid":
            return "Please, make sure your request is valid and try again.";
        case "selector_not_found":
            return "The target element was not found on the page";
        case "name_not_resolved":
            return "Unable to resolve the domain name. Check that there is no typo in the URL. If this is a new site, please wait for DNS propagation.";
        case "network_error":
            return "Unable to connect to the requested URL. The site may be blocking access or temporarily down.";
        case "host_returned_error":
            if ([401, 403, 429].includes(error.returned_status_code)) {
                return "The target website blocks automated screenshot rendering.";
            }
            if (error.returned_status_code >= 500) {
                return "The target website is temporarily down. Please, retry later.";
            }
            if (error.returned_status_code == 404) {
                return "The target website returned a 404 HTTP error—the page not found.";
            }

            return `The target website returned a ${error.returned_status_code} HTTP error.`;
        case "timeout_error":
            return "The screenshot rendering timed out. Please, try again.";
        case "storage_returned_transient_error":
        case "internal_application_error":
        case "request_aborted":
            return "Failed to render the screenshot. Please try your request again";
        case "access_key_required":
        case "access_key_invalid":
        case "signature_is_required":
        case "signature_is_not_valid":
        case "invalid_storage_configuration":
        case "script_triggers_redirect":
        case "storage_access_denied":
        case "content_contains_specified_string":
        case "invalid_cookie_parameter":
        case "resulting_image_too_large":
            // these are errors that often are not caused by the end user action,
            // and they need to be fixed on your or our side
            return "The screenshot rendering failed. Please, reach out to support.";
        default:
            // return a generic error message
            // or the message provided by the API error.error_message
            return "The screenshot rendering failed. Please, reach out to support.";
    }
}
```

These are the most common errors often caused by end users. If you want to process more codes, check out [all  our errors](/docs/errors/).

## Reporting errors

All ScreenshotOne API errors are logged and we are acknowledged by them. And will react to them as fast as possible.

In general, you don't need to report to us any errors. But if it blocks your work or you want us to prioritize fixing them, please, feel free to report an error at `support@screenshotone.com`.

## Error reference

All API errors are listed in [the error reference](/docs/errors/).