# Source: https://posthog.com/docs/error-tracking/installation/manual.md

# Manual error tracking installation - Docs

1.  1

    ## Learn the API schema

    Required

    Error tracking enables you to track, investigate, and resolve exceptions your customers face.

    If a platform you use is not supported by error tracking, we recommend that you reach out to us or contribute to our open-source SDKs before attempting to manually send exceptions.

    If you'd rather roll your own exception capturing (or if you're using a platform we don't have an SDK for), you can use the [capture API](/docs/api/capture.md) or `capture` method to capture an `$exception` event with the following properties:

    | Property | Description |
    | --- | --- |
    | $exception_list | A list of exception objects with detailed information about each error. Each exception can include a type, value, mechanism, module, and a stacktrace with frames and type. You can find the expected schema as types for both exception and stack frames in our Rust repo |
    | $exception_fingerprint | (Optional) The identifier used to group issues. If not set, a unique hash based on the exception pattern will be generated during ingestion |

2.  2

    ## Make a request

    Required

    Example exception API capture:

    Terminal

    PostHog AI

    ```bash
    curl -X POST "https://us.i.posthog.com/i/v0/e/" \
         -H "Content-Type: application/json" \
         -d '{
            "token": "<ph_project_token>",
            "event": "$exception",
            "properties": {
                "distinct_id": "distinct_id_of_your_user",
                "$exception_list": [{
                    "type": "RangeError",
                    "value": "Maximum call stack size exceeded",
                    "mechanism": {
                        "handled": true,
                        "synthetic": false
                    },
                    "stacktrace": {
                        "type": "raw",
                        "frames": [
                            {
                                "platform": "custom", // (Required) Must be custom
                                "lang": "javascript", // (Required) Your programming language
                                "function": "Array.forEach", // (Required)
                                "filename": "../loop.js", // (Optional)
                                "lineno": 1, // (Optional)
                                "colno": 2, // (Optional)
                                "module": "iteration", // (Optional)
                                "resolved": true, // (Optional)
                                "in_app": false, // (Optional)
                            },
                            /* Additional frames omitted for brevity */
                        ]
                    }
                }],
                "$exception_fingerprint": "209842d96784e19321e3a36b068d53fff7a01ebcb1da9e98df35c4c49db0b4f3b62aea7ee25a714470e61f8d36b4716f227f241c153477e5fa9adfda64ce9f71"
            },
        }'
    ```

3.  ## Verify error tracking

    Recommended

    *Confirm events are being sent to PostHog*

    Before proceeding, let's make sure exception events are being captured and sent to PostHog. You should see events appear in the activity feed.

    ![Activity feed with events](https://res.cloudinary.com/dmukukwp6/image/upload/SCR_20250729_ouxl_f788dd8cd2.png)![Activity feed with events](https://res.cloudinary.com/dmukukwp6/image/upload/SCR_20250729_owae_7c3490822c.png)

    [Check for exceptions in PostHog](https://app.posthog.com/activity/explore)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better