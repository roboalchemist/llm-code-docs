# Source: https://documentation.onesignal.com/reference/idempotent-notification-requests.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Idempotent API requests

> Prevent duplicate messages or custom events when retrying API requests.

## Overview

When you create messages or custom events via our REST API, network failures or timeouts can cause uncertainty about whether a request succeeded. **Idempotent requests** solve this problem by ensuring the same request is only processed once—even if it is sent multiple times.

This page explains how idempotency works in OneSignal, when to use it, and common pitfalls to avoid.

### When you should use idempotency

You should use idempotent requests any time you plan to retry API calls, especially when:

* You receive a timeout, 500-level error, or no response.
* Your infrastructure automatically retries failed requests.
* Delivering a duplicate message or custom event would be harmful.
* Missing a message or custom event would be harmful.

### The problem idempotency solves

Consider this common failure scenario:

1. You send a `notifications#create` or `custom_events#create` request.
2. OneSignal begins processing and sending the message or event.
3. A network error occurs before your client receives a response.

At this point, your system cannot know whether the request succeeded.

* If you retry and the request already succeeded, users may receive duplicates.
* If you do not retry and the request failed, users may miss important messages or events.

**Idempotency provides a safe retry mechanism.**

***

## How idempotency works

OneSignal supports idempotent operations for:

* [`notifications#create`](/reference/create-message)
* [`custom_events#create`](/reference/create-custom-events)

You provide a unique `idempotency_key` with each request.

### Request flow with idempotency

1. You send a request with an `idempotency_key`.
2. OneSignal processes the request and begins sending the message or creating the custom event.
3. A network error or timeout occurs.
4. You retry the request using the same `idempotency_key`.
5. OneSignal detects the duplicate and returns the result of the original request.
6. Only one notification or custom event is processed.

You can repeat this retry any number of times. As long as the `idempotency_key` remains the same, the operation will only be processed once.

***

## Idempotency key reference

<ParamField path="idempotency_key" type="RFC 9562 UUID">
  A unique identifier used to prevent duplicate messages or custom events from repeat API calls. Keys must be unique [RFC 9562 UUID format](https://en.wikipedia.org/wiki/Universally_unique_identifier). Valid for 30 days.
</ParamField>

<Note>
  This `idempotency_key` property used to be called `external_id` but caused confusion with our [Users `external_id`](/docs/en/users) alias, so we have added this new property name to reduce confusion. Both will work in this case.
</Note>

***

## Important constraints and gotchas

<Warning> If you reuse the same `idempotency_key` for different messages or events, only the first request will be processed. </Warning>

Keep the following in mind:

* **Keys must be unique per logical operation**
  Generate a new UUID for every notification or custom event you intend to send.

* **Keys are retained for 30 days**
  After 30 days, OneSignal may delete the record. Reusing the same key after that window may result in a new message being sent.

* **Use a strong source of randomness**
  Predictable or reused UUIDs can cause unexpected deduplication.

* **Idempotency does not guarantee delivery**
  It only guarantees at-most-once processing. You should still monitor API responses and logs.

### Legacy behavior

The `idempotency_key` property was previously named `external_id`. This caused confusion with the Users `external_id` alias, so `idempotency_key` is now the recommended field name. Both names are currently supported.

### Best practices

* Always include `idempotency_key` when implementing retries.
* Store the `idempotency_key` alongside your request metadata for debugging.
* Retry only after honoring any `Retry-After` header returned by the API.
* Combine idempotency with proper timeout handling (for example, a 60-second HTTP timeout).

***

Built with [Mintlify](https://mintlify.com).
