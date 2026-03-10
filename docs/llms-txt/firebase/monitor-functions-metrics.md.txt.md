# Source: https://firebase.google.com/docs/app-check/monitor-functions-metrics.md.txt

After you add the App Check SDK to your app, but before you enable
App Check enforcement, you should make sure that doing so won't disrupt your
existing legitimate users.

For Cloud Functions, you can get App Check metrics by examining your
functions' logs. Every invocation of a callable function emits a structured log
entry like the following example:

    {
      "severity": "INFO",    // INFO, WARNING, or ERROR
      "logging.googleapis.com/labels": {"firebase-log-type": "callable-request-verification"},
      "jsonPayload": {
        "message": "Callable header verifications passed.",
        "verifications": {
          // ...
          "app": "MISSING",  // VALID, INVALID, or MISSING
        }
      }
    }

You can analyze these metrics in the Google Cloud console by [creating a
logs-based counter metric](https://cloud.google.com/logging/docs/logs-based-metrics/counter-metrics)
with the following metric filter:

```
resource.type="cloud_function"
resource.labels.function_name="YOUR_CLOUD_FUNCTION"
resource.labels.region="us-central1"
labels.firebase-log-type="callable-request-verification"
```

[Label the metric](https://cloud.google.com/logging/docs/logs-based-metrics/labels#create-label)
using the field `jsonPayload.verifications.appCheck`.

## Next steps

When you understand how App Check will affect your users and you're ready to
proceed, you can [enable App Check enforcement](https://firebase.google.com/docs/app-check/cloud-functions)
for Cloud Functions.