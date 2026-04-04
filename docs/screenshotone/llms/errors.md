# Source: https://screenshotone.com/docs/errors/

# Errors

import Alert from "@/components/Alert.astro";

<Alert>
    There is [a detailed guide](/docs/guides/how-to-handle-api-errors/) on how
    to handle the ScreenshotOne API errors.
</Alert>

The request might return an error due to an internal error, invalid options or when the limit is reached. Our screenshot API follows the HTTP status code semantic and returns JSON in case of an error:

```
GET https://api.screenshotone.com/?[options]

Content-Type: application/json
{
    "is_successful": false,
    "error_code": "an_error_code",
    "error_message": "An error message",
    "documentation_url": "..."
}
```

The API will always return a human-readable error message, error code as a string key, and suitable HTTP status code.

## Codes with explanations

| Error Code                                                             | HTTP Status | Explanation                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [access_key_required](/docs/errors/access-key-required/)                                                    | 400         | The "access_key" parameter is required. Please, check out [the access page](https://dash.screenshotone.com/access) to get the access key.                                                                                                                                                                                                                   |
| [access_key_invalid](/docs/errors/access-key-invalid/)                                                     | 400         | The "access_key" parameter is given, but it is not correct. Please, check out [the access page](https://dash.screenshotone.com/access) to check the access key.                                                                                                                                                                                             |
| [signature_is_required](/docs/errors/signature-is-required/)                                                  | 400         | The "signature" parameter is required. Because signing requests is required in [the access page](https://dash.screenshotone.com/access). Make sure you use [the correct signing algorithm](/docs/signed-requests/).                                                                                                                                         |
| [signature_is_not_valid](/docs/errors/signature-is-invalid/)                                                 | 400         | You provided the "signature" parameter, but it is not valid. Make sure you use [the correct signing algorithm](/docs/signed-requests/).                                                                                                                                                                                                                     |
| [screenshots_limit_reached](/docs/errors/usage-quota-exceeded/)        | 400         | The usage quota has been exceeded. Please, either upgrade to a plan with more quota or change the maximum allowed limit (if possible) in the ScreenshotOne dashboard. If it is a mistake, please, reach out at `support@screenshotone.com.`                                                                                                                 |
| [concurrency_limit_reached](/docs/errors/concurrency-limit-reached/)                                              | 400         | You reached the request concurrency limit, retry after a while. Or feel free to [upgrade you current plan](https://dash.screenshotone.com/subscription).                                                                                                                                                                                                    |
| [request_not_valid](/docs/errors/request-invalid/)                                                      | 400         | The request parameters are not valid. You can look at the `error_details` response field to get the details.                                                                                                                                                                                                                                                |
| [selector_not_found](/docs/errors/selector-not-found/)                                                     | 400         | If [selector](/docs/options#selector) is specified and `error_on_selector_not_found=true`, the error will be returned if the element by selector is not visible or it took more than `timeout` seconds to render it, but not more than 30 seconds.                                                                                                          |
| [name_not_resolved](/docs/errors/name-not-resolved/)                                                      | 400         | Usually, the error happens when the domain name of the requested URL is not resolved. If you are trying to take a screenshot of the new site, please, wait a bit until the DNS records are refreshed.                                                                                                                                                       |
| [network_error](/docs/errors/network-error/)                                                          | 500         | The error happens when the API can't connect to the provided URL. It might mean that the site blocks the API or is temporarily unavailable. Generally, you can safely retry to take a screenshot.                                                                                                                                                           |
| [invalid_storage_configuration](/docs/errors/invalid-storage-configuration/)                                          | 400         | If you haven't created the bucket in the `us-east-1` AWS region, please, specify your bucket region through an endpoint in a format like `https://s3.<your-region>.amazonaws.com`.                                                                                                                                                                          |
| [script_triggers_redirect](/docs/errors/script-triggers-redirect/)     | 400         | The specified "scripts" option might trigger a redirect, please, specify the "scripts_wait_until" option. If you think it is a mistake, please, reach out at `support@screenshotone.com`.                                                                                                                                                                   |
| [host_returned_error](/docs/errors/host-returned-error/)                                                    | 500         | If the host doesn't respond successfully within the range of 200-299 status codes, the API won't take a screenshot. You can force the API to take a screenshot of the error page by specifying [ignore_host_errors=true](/docs/options#ignore_host_errors). You can get the returned status code from the site by reading the `returned_status_code` field. |
| [timeout_error](/docs/errors/timeout/)                                 | 500         | The screenshot couldn't be taken within the specified timeout. Either the site doesn't respond quickly, or rendering takes longer than expected. Play with the `timeout` or the `navigation_timeout` options or reach the support for the investigation.                                                                                                    |
| [internal_application_error](/docs/errors/internal-application-error/) | 500         | The API failed to serve your request. You can safely replay the request. We are notified about it instantly and will try to fix it as soon as possible. If the error is repeated for a long time, feel free to reach out at support@screenshotone.com.                                                                                                      |
| [storage_access_denied](/docs/errors/storage-access-denied/)           | 400         | Failed to upload the screenshot to the storage since access was denied. Check the API keys you specify when using the storage integration.                                                                                                                                                                                                                  |
| [storage_returned_transient_error](/docs/errors/storage-returned-transient-error/)                                       | 500         | The storage returned an HTTP status code between 500 and 599 and we exhausted retries. You can likely retry the request again.                                                                                                                                                                                                                              |
| [request_aborted](/docs/errors/request-aborted/)                       | 500         | The request was aborted either by the user or the intermediate proxies and can't be fulfilled. If the error persists, please, reach out to support@screenshotone.com.                                                                                                                                                                                       |
| [content_contains_specified_string](/docs/errors/content-contains-specified-string/)                                      | 500         | The page content contains the specified string by the [fail_if_content_contains](/docs/options#fail_if_content_contains) option. If it seems to be a mistake or not what you expected, please, reach out to \`support@screenshotone.com\` as quickly as possible, and will assist and try to resolve your problem.                                          |
| [temporary_unavailable](/docs/errors/temporary-unavailable/)                                                  | 503         | The API is temporarily unavailable due to an error or overload. Please wait a bit and then safely retry your request.                                                                                                                                                                                                                                       |
| [invalid_cookie_parameter](/docs/errors/invalid-cookie-parameter/)                                                  | 400         | The `cookies` parameters you provided are invalid. Please, consider providing different values and adhere to the format specified in the ScreenshotOne documentation.                                                                                                                                                                                                                                       | 
| [resulting_image_too_large](/docs/errors/resulting-image-too-large/)                                                  | 400         | The resulting image is too large for the specified format. Please, consider providing different values and adhere to the format specified in the ScreenshotOne documentation.                                                                                                                                                                                                                                       | 
| [matched_failed_request](/docs/errors/matched-failed-request/)                                                  | 500         | The request matched by the specified pattern by the [fail_if_request_failed](/docs/options#fail_if_request_failed) option has been failed. If it seems to be a mistake or not what you expected, please, reach out to \`support@screenshotone.com\` as quickly as possible, and will assist and try to resolve your problem.                                          | 
| [invalid_header_parameter](/docs/errors/invalid-header-parameter/)                                                  | 400         | The `headers` parameters you provided are invalid. Please, consider providing different values and adhere to the format specified in the ScreenshotOne documentation.                                                                                                                                                                                                                                       | 
| [request_body_too_large](/docs/errors/request-body-too-large/)                                                  | 413         | The request body is too large. Please, reduce the size of the request body or reach out to \`support@screenshotone.com\` for assistance.                                                                                                                                                                                                                                       | 

## List of all errors

1. [Timeout error](/docs/errors/timeout/).
2. [Storage Access Denied](/docs/errors/storage-access-denied/).
3. [Script Trigger Redirect](/docs/errors/script-triggers-redirect/).
4. [Internal Application Error](/docs/errors/internal-application-error/).
5. [Usage Quota Exceeded](/docs/errors/usage-quota-exceeded/).
6. [Request Aborted](/docs/errors/request-aborted/).
7. [Access Key Required](/docs/errors/access-key-required/).
8. [Access Key Invalid](/docs/errors/access-key-invalid/).
9. [Signature Is Required](/docs/errors/signature-is-required/).
10. [Signature Is Not Valid](/docs/errors/signature-is-invalid/).
11. [Screenshots Limit Reached](/docs/errors/usage-quota-exceeded/).
12. [Concurrency Limit Reached](/docs/errors/concurrency-limit-reached/).
13. [Request Not Valid](/docs/errors/request-invalid/).
14. [Selector Not Found](/docs/errors/selector-not-found/).
15. [Name Not Resolved](/docs/errors/name-not-resolved/).
16. [Network Error](/docs/errors/network-error/).
17. [Invalid Storage Configuration](/docs/errors/invalid-storage-configuration/).
18. [Host Returned Error](/docs/errors/host-returned-error/).
19. [Storage Returned Transient Error](/docs/errors/storage-returned-transient-error/).
20. [Content Contains Specified String](/docs/errors/content-contains-specified-string/).
21. [Temporary Unavailable](/docs/errors/temporary-unavailable/).
22. [Invalid Cookie Parameter](/docs/errors/invalid-cookie-parameter/).
23. [Resulting Image Too Large](/docs/errors/resulting-image-too-large/).
24. [Matched Failed Request](/docs/errors/matched-failed-request/).
25. [Invalid Header Parameter](/docs/errors/invalid-header-parameter/).
26. [Request Body Too Large](/docs/errors/request-body-too-large/).