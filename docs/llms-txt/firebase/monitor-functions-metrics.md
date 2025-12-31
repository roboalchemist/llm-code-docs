# Source: https://firebase.google.com/docs/app-check/monitor-functions-metrics.md.txt

After you add theApp CheckSDK to your app, but before you enableApp Checkenforcement, you should make sure that doing so won't disrupt your existing legitimate users.

ForCloud Functions, you can getApp Checkmetrics by examining your functions' logs. Every invocation of a callable function emits a structured log entry like the following example:  

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

You can analyze these metrics in theGoogle Cloudconsole by[creating a logs-based counter metric](https://cloud.google.com/logging/docs/logs-based-metrics/counter-metrics)with the following metric filter:  

```
resource.type="cloud_function"
resource.labels.function_name="YOUR_CLOUD_FUNCTION"
resource.labels.region="us-central1"
labels.firebase-log-type="callable-request-verification"
```

[Label the metric](https://cloud.google.com/logging/docs/logs-based-metrics/labels#create-label)using the field`jsonPayload.verifications.appCheck`.

## Next steps

When you understand howApp Checkwill affect your users and you're ready to proceed, you can[enableApp Checkenforcement](https://firebase.google.com/docs/app-check/cloud-functions)forCloud Functions.