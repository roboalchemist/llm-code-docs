# Callbacks

## Use Callbacks to send Output Data to Posthog, Sentry etc [​](https://docs.litellm.ai/observability/callbacks\#use-callbacks-to-send-output-data-to-posthog-sentry-etc "Direct link to Use Callbacks to send Output Data to Posthog, Sentry etc")

liteLLM provides `success_callbacks` and `failure_callbacks`, making it easy for you to send data to a particular provider depending on the status of your responses.

liteLLM supports:

- [Lunary](https://lunary.ai/docs)
- [Helicone](https://docs.helicone.ai/introduction)
- [Sentry](https://docs.sentry.io/platforms/python/)
- [PostHog](https://posthog.com/docs/libraries/python)
- [Slack](https://slack.dev/bolt-python/concepts)

### Quick Start [​](https://docs.litellm.ai/observability/callbacks\#quick-start "Direct link to Quick Start")

```codeBlockLines_e6Vv
from litellm import completion