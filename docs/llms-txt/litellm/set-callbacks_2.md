# set callbacks
litellm.success_callback=["posthog", "helicone", "lunary"]
litellm.failure_callback=["sentry", "lunary"]

## set env variables
os.environ['SENTRY_DSN'], os.environ['SENTRY_API_TRACE_RATE']= ""
os.environ['POSTHOG_API_KEY'], os.environ['POSTHOG_API_URL'] = "api-key", "api-url"
os.environ["HELICONE_API_KEY"] = ""

response = completion(model="gpt-3.5-turbo", messages=messages)

```

- [Use Callbacks to send Output Data to Posthog, Sentry etc](https://docs.litellm.ai/observability/callbacks#use-callbacks-to-send-output-data-to-posthog-sentry-etc)
  - [Quick Start](https://docs.litellm.ai/observability/callbacks#quick-start)

## Helicone Integration Guide
[Skip to main content](https://docs.litellm.ai/observability/helicone_integration#__docusaurus_skipToContent_fallback)