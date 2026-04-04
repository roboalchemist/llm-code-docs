# Source: https://documentation.onesignal.com/docs/en/journeys-webhook.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Journey webhooks

> Webhooks let you connect your OneSignal Journeys to the world!

With Journey Webhooks, you can send HTTP requests from OneSignal Journeys to your servers—or any internet-accessible service—at precisely the right moment in a customer's lifecycle. Configure the HTTP method, URL, headers, and body content to match your integration requirements. Requests can be dynamically personalized with user-specific data, making webhooks a powerful way to sync your Journeys with the rest of your marketing stack.

## Requirements

Before events can be sent, make sure:

* [Contact our sales team](https://onesignal.com/contact) for access.
* The URL/IP address is valid and reachable over HTTP or HTTPS.
* Endpoints are **publicly routable** (i.e., not behind a firewall or on localhost).
* Domains must have a valid top-level domain (e.g., `.com`, `.org`, `.net`).
* Journey webhooks cannot be used to call OneSignal APIs.

***

## Setup

Once your Journey is created, follow these steps:

1. Navigate to **Data > Webhooks** in the OneSignal dashboard.
2. Click to create a new webhook.
3. Define the following:
   * **HTTP method** (usually `POST`)
   * **Target URL**
   * **Custom headers** (e.g., for authentication)
   * **Body content** (plain text or JSON, optionally using Liquid)

<Frame caption="Webhook config screen">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f4bb77a-Screenshot_2023-04-20_at_9.24.03_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=79005b0332776e4703954789fe40c5ea" width="1038" height="926" data-path="images/docs/f4bb77a-Screenshot_2023-04-20_at_9.24.03_PM.png" />
</Frame>

### Disallowed headers

You cannot set the following headers:

* `content-length`
* `referer`
* `metadata-flavor`
* `x-google-metadata-request`
* `host`
* Any header starting with `x-onesignal`

### Testing webhooks

You can also test your endpoint manually using a tool like curl:

```bash bash theme={null}
curl -X POST https://yourserver.com/webhook \
  -H "Content-Type: application/json" \
  -d '{ "user_id": "abc123" }'
```

Useful for validating that your endpoint is reachable and functioning before adding it to a Journey.

***

## Personalization

All webhook fields support [Liquid syntax](./using-liquid-syntax), allowing you to dynamically insert user and subscription data into the request.

See [Message Personalization](./message-personalization) for more details on the available properties.

### User data reference

The following properties from the `user` object are available in webhook fields via liquid syntax:

| Property     | Type   | Usage                               | Available in Test? |
| ------------ | ------ | ----------------------------------- | ------------------ |
| OneSignal ID | String | `{{ user.onesignal_id }}`           | ✅                  |
| External ID  | String | `{{ user.external_id }}`            | ✅                  |
| Tags         | Object | `{{ user.tags.your_tag_key_here }}` | ❌                  |
| Language     | String | `{{ user.language }}`               | ✅                  |

<Warning>
  Tags are not available when testing webhooks outside an active Journey. Use [Test subscriptions](./find-set-test-subscriptions) to validate behavior before going live.
</Warning>

***

## Adding a webhook to a Journey

1. After creating and testing your webhook, open your Journey.
2. Add a **Webhook step** where needed.
3. Select the webhook you configured earlier.

Each time a user reaches that step, the webhook fires with their personalized data.

<Frame caption="A webhook step within a journey">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/7e6782f-Screenshot_2023-04-20_at_3.54.09_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=e017a2eff865b6de671a34b71c437332" width="664" height="1058" data-path="images/docs/7e6782f-Screenshot_2023-04-20_at_3.54.09_PM.png" />
</Frame>

***

## Debugging and logs

### Webhook stats

Go to the webhook’s **Stats** tab to view how your webhook is performing. This includes:

* Total events sent
* Response time trends
* Status code distribution

<Frame caption="The webhook reports page">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f0cfcb8-small-Screenshot_2023-04-21_at_9.04.57_AM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=f4514d8cecf78831bd55019cfce61b9b" width="1185" height="1007" data-path="images/docs/f0cfcb8-small-Screenshot_2023-04-21_at_9.04.57_AM.png" />
</Frame>

### Logs tab

For more granular insights, the Logs tab displays:

* Recent request/response data
* Status codes and error messages
* Headers and payloads (where applicable)

<Frame caption="The webhook log page">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/729c24f-Screenshot_2023-04-20_at_9.27.31_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=3923dcf3fbf2975e27b5f158a1442824" width="2130" height="1264" data-path="images/docs/729c24f-Screenshot_2023-04-20_at_9.27.31_PM.png" />
</Frame>

***

## Retry logic and disabling behavior

OneSignal retries failed webhook requests for recoverable errors (e.g., `429 Too Many Requests`). Retries happen with increasing delays.

If retries repeatedly fail, the webhook is marked as **permanently failed** and no further attempts are made.

### Automatic disabling

If a webhook consistently fails, OneSignal disables it to prevent further issues. Admins receive email alerts and a dashboard banner before and after a webhook is disabled. If this happens, make sure to spend some time troubleshooting, fixing and then testing the webhook before re-enabling it.

It is important that the API which ingests an webhook is able to handle the volume of events which is produced by message sends. Reviewing the volume of message sends that are produced by your app will reflect the performance required of your API.

## Performance guidance

* Slow or overloaded endpoints (especially with 429 responses) can trigger disabling.
* APIs should record events quickly and defer additional processing to avoid timeouts.
* Volume scales with user activity—ensure your endpoint can handle this throughput.
* Use the `event.id` value (available as a header or in body) to deduplicate incoming events.

### Tips for success

* Connect webhooks to your own servers first, not directly to third-party services.
  * While OneSignal webhooks can call any public API, routing through your own server gives you more control.
  * It’s easier to debug, add logging, handle authentication, and throttle or queue requests as needed.
  * Third-party services may rate-limit or block requests if volume spikes, and OneSignal does not manage those limits.
* Webhook execution happens immediately as users reach that step in the Journey.
  * If many users hit a webhook step at once, OneSignal will send a burst of HTTP requests without rate limiting.
  * This can easily overwhelm external services, trigger rate limits, or incur unexpected charges.
  * Consider building a lightweight API layer or queueing proxy that can:
    * Ingest webhooks reliably
    * Apply rate limits or batching
    * Route requests to your third-party services gracefully
* Use third-party APIs carefully:
  * Most popular tools (e.g., Slack, Twilio, Segment) offer public HTTP APIs.
  * Review their rate limits, authentication requirements, and error handling strategies.
  * Search for code examples in their docs to see what your webhook request should look like.

***

## Securing your webhook

To ensure that requests are coming from OneSignal and have not been tampered with:

* Use an HMAC signature header with a shared secret
* Add a custom auth token in the header and verify it server-side

***

## Related links

* [Using liquid syntax](./using-liquid-syntax)
* [Users](./users)

***

Built with [Mintlify](https://mintlify.com).
