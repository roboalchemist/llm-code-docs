# Source: https://documentation.onesignal.com/reference/rate-limits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate limits and error handling

> Understand OneSignal API and application rate limits, common errors, retry behavior, and how to safely recover from failures without sending duplicate messages or disabling your app.

## Overview

OneSignal uses rate limits and error responses as safety mechanisms to protect your app from accidental overloads, duplicate sends, and retry storms.

There are three categories to understand:

* **API rate limits** return HTTP `429` errors when request volume is too high.
* **Network timeouts or temporary server failures** return `5xx` errors or no response at all.
* **Application message limits** may temporarily disable your app if too many messages are sent in a short period.

<Info>
  Most apps never hit these limits during normal usage. When they do occur, they are usually caused by retries, loops, or unexpected audience expansion.
</Info>

<Check>
  **Quick implementation checklist**

* Expect `429`, `5xx`, and timeouts — they are normal at scale.
* Never retry message sends without an `idempotency_key`.
* For non-urgent retries, wait **100 seconds** before retrying.
* API rate limits (`429`) never disable your app.
* Only message volume limits can disable your app.
</Check>

***

## API rate limits

API rate limits apply **per app and per endpoint**. They are evaluated when a request is received, not when a response is returned.

These limits are designed to throttle traffic, not block your app.

| Endpoint                                         | Rate limit                                                                                                                                  |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [Create message](/reference/create-message)      | **Free plans:** 150 requests/sec/app<br />**Paid plans:** 6,000 requests/sec/app<br /><br />Each request can target many users or segments. |
| Create, update, or delete users or subscriptions | 1,000 requests/sec/app<br />1 request/sec per user or subscription<br />Up to 100 property updates per request                              |
| View endpoints (messages, templates, users)      | 1 request/sec/app<br />Up to 10 look-back requests/sec                                                                                      |
| Message History and CSV exports                  | Keep parallel exports under 100 GB per file                                                                                                 |

<Note>
  High-volume messaging should use fewer message creation requests with larger audiences instead of increasing request frequency.
</Note>

**Handling API rate limit errors (`429`):**

When you exceed an API rate limit, OneSignal returns an HTTP `429` response:

```json  theme={null}
{
  "errors": ["API rate limit exceeded."]
}
```

The response includes a `Retry-After` header indicating how many seconds to wait before retrying.

**What to do when you receive a `429` error:**

1. Stop sending requests immediately.
2. Wait for the full duration specified in the `Retry-After` header.
3. Retry using exponential backoff.
4. Always reuse the same [`idempotency_key`](/reference/idempotent-notification-requests) for retries that send messages.

<Warning> Retrying before the `Retry-After` delay or retrying in tight loops can extend throttling and increase failure rates. </Warning>

***

## Error handling and retry strategies

Retries are safe only when implemented correctly. Some failed requests may still be processing on our servers.

* Retriable errors generally include network timeouts, no responses, 429, and 5xx errors.
* Non-retryable errors include 400, 401, or 403 errors which indicate invalid input, authentication problems, or missing permissions—not temporary failures.

**Simple retry strategy:**

* Wait **100 seconds** before retrying.
  * This aligns with the maximum API response timeout.
  * If no response or network error occurs, the request may still be processing during this window.
* Retry **up to 3 total attempts** (original + 2 retries).
* Always reuse the same [`idempotency_key`](/reference/idempotent-notification-requests) for each retry.

**Time-sensitive (advanced) retry strategy:**

* Retry using exponential backoff with jitter (for example: 2s, 4s, 8s… up to 60s).
* Cap retries to **10 total attempts** and stop after **10–15 minutes**.
* For `429` responses, treat `Retry-After` as a minimum delay: wait `max(Retry-After, backoff)`.
* Always reuse the same [`idempotency_key`](/reference/idempotent-notification-requests) for each retry.

<Warning> Retrying message or custom event API requests without idempotency can result in duplicates messages or custom events. </Warning>

<Accordion title="Example retry logic">
  ```javascript  theme={null}
  attempt = 1
  max_attempts = 3

  send request with idempotency_key

  if response is success:
    stop

  if response is 429:
    wait Retry-After seconds
  elif response is 5xx or timeout:
    wait 100 seconds

  if attempt < max_attempts:
    retry with same idempotency_key
  else:
    fail safely

  ```
</Accordion>

### Retry decision guide

| Error type              | Retry? | When                 | Idempotency required |
| ----------------------- | ------ | -------------------- | -------------------- |
| `429 Too Many Requests` | Yes    | After `Retry-After`  | ✅ Yes                |
| `5xx Server Error`      | Yes    | Backoff or 100s      | ✅ Yes                |
| Timeout / no response   | Yes    | Immediate or delayed | ✅ Yes                |
| `400 Bad Request`       | No     | Fix request          | ❌ No                 |
| `401 / 403`             | No     | Fix auth/permissions | ❌ No                 |

<Warning>
  Common implementation mistakes:

  * Retrying with a new idempotency key on each attempt.
  * Retrying indefinitely without a retry cap.
  * Retrying `400` or `401` errors without fixing the request.
  * Sending one request per user instead of batching audiences.
</Warning>

***

## Application message limits (app disablement)

Application message limits protect your users from receiving too many notifications in a short period of time.

**How the limit works:**

In any rolling 15-minute window, you may send up to **10 × your total number of subscribed [Subscriptions](/docs/en/subscriptions)**.

This limit is based on the total number of messages delivered, not the number of API requests.

* Sending 1 notification to 1,000 Subscriptions = 1,000 messages
* Sending 10 notifications to 1,000 Subscriptions each = 10,000 messages

The 15-minute window is rolling, not fixed.

* Messages are counted for 15 minutes after they are sent
* As time passes, older messages automatically stop counting
* You only exceed the limit if more than 10× your subscribed Subscriptions receive messages within the same 15-minute span

Example limits:

* App with 1,000 subscribed Subscriptions → up to 10,000 messages in any 15 minutes
* App with 10,000 subscribed Subscriptions → up to 100,000 messages in any 15 minutes

**Example scenarios:** App with 10,000 subscribed Subscriptions

For this example, the app can send up to 10,000 total messages within any rolling 15-minute window.

| Scenario                                                                              | Maximum messages counted in any 15-minute period |     App disabled?     |
| ------------------------------------------------------------------------------------- | -----------------------------------------------: | :-------------------: |
| At **12:00**, send 1 notification to 1,000 users                                      |                                            1,000 |          ❌ No         |
| At **12:00**, send 10 notifications to 1,000 users                                    |                                           10,000 |   ✅ Yes (hits limit)  |
| Between **12:00–12:14**, send 10,000 notifications to 1 user                          |                                           10,000 |   ✅ Yes (hits limit)  |
| Send **9,000 messages at 12:00**, then **9,000 more at 12:16**                        |                                            9,000 |          ❌ No         |
| Send **9,000 messages spread between 12:00–12:14**, then send **9,000 more at 12:15** |                                         \~18,000 | ✅ Yes (exceeds limit) |

<Note> This limit is evaluated continuously over a rolling 15-minute window, not in fixed time blocks. If any 15-minute span exceeds your limit, the app is disabled. </Note>

**What happens if the limit is exceeded:**

If your app sends more messages than allowed within a 15-minute window:

* Your app is temporarily disabled
* All app administrators receive an email notification
* A re-enable banner appears in the OneSignal Dashboard

<Warning> Only application message limits can disable your app. API rate limits (`429` errors) never disable apps. </Warning>

**What to do if your app is disabled:**

If your app is disabled, follow these steps in order:

1. Pause message sending from your backend, jobs, or automations.
2. Identify the cause, such as Infinite loops, Retry storms, or Unexpected segment growth.
3. Log in to the OneSignal Dashboard.
4. Click Re-enable in the red banner at the top of the app.
5. If you need help re-enabling your app, contact `support@onesignal.com`.

***

<Check>
  Next steps:

  * Learn how to safely retry with [Idempotent API requests](/reference/idempotent-notification-requests)
  * Review [Create notification API](/reference/create-message)
  * Review [Create custom event API](/reference/create-custom-events)
</Check>

***


Built with [Mintlify](https://mintlify.com).
