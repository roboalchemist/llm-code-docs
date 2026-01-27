# Source: https://clickwrap-developer.ironcladapp.com/docs/webhook-events.md

# Webhook Events + Payload Examples

## Available Webhook Types

* [Activity - Agreed](#activity---agreed)
* [Version Published](#version-published)
* [Group Published](#group-published)
* [Activity - All](#activity---all)
* [Request Sent](#request-sent)
* [Request Signed](#request-signed)
* [Request Complete](#request-complete)
* [Request Expired](#request-expired)

<Image title="Screen Shot 2020-10-21 at 9.41.43 AM.png" alt={3630} align="center" src="https://files.readme.io/851cd49-Screen_Shot_2020-10-21_at_9.41.43_AM.png">
  A view within the Ironclad Clickwrap Web App of the webhook configuration interface.
</Image>

## Example Payloads

There are 7 types of events you can configure for when setting up webhooks. Each event has some common properties and some properties unique to the Webhook. We'll outline an example payload for each Webhook below, including the `Test Webhook` Payload.

### Test Webhook

The `Test Webhook` is a webhook button inside the Ironclad Clickwrap Web App that allows you to test your webhook integration.

```json Request Body
{
  "deliverable": true,
  "type": "webhook",
  "integration": "123",
  "sent_to": "https://123.m.pipedream.net",
  "event_type": "test_event",
  "description": "Test sent a test event!",
  "site": 1,
  "user": 1,
  "created_time": "2020-10-21T13:45:51.087Z",
  "updated_time": "2020-10-21T13:45:51.096Z",
  "id": "1234abcd"
}
```

```json Request Headers
{
  "x-forwarded-for": "1.2.3.4",
  "x-forwarded-proto": "https",
  "x-forwarded-port": "443",
  "host": "example.com",
  "content-length": "358",
  "pactsafe-webhook-token": "my-secret-code",
  "accept": "application/json",
  "content-type": "application/json"
}
```

### Activity - Agreed

This webhook is triggered for each contract in a Signature Request or a Clickwrap. Setting the HTTP Method to `POST` will allow you to receive custom data and render data.

```json Request Body
{
  "type": "webhook",
  "sent_to": "https://example.com",
  "site": 12345
  "integration": "123",
  "event_type": "activity_agreed",
  "description": "test@example.com agreed to Privacy Policy in Group Example Web Group",
  "custom_data": {
    "first_name": "John",
    "last_name": "Walker",
    "company_name": "Sedona Networks",
    "title": "Customer Support"
  },
  "deliverable": true,
  "created_time": "2020-10-21T13:55:59.070Z",
  "group": 123,
  "contract": 123,
  "version": "1234abcd",
  "activity": "abcd1234abcd1234",
  "signer_id": "john.walker@ironcladhq.com",
  "updated_time": "2020-10-21T13:55:59.150Z",
  "id": "123abc123abc"
}
```

```json Request Headers
{
  "x-forwarded-for": "1.2.3.4",
  "x-forwarded-proto": "https",
  "x-forwarded-port": "443",
  "host": "example.com",
  "content-length": "358",
  "pactsafe-webhook-token": "my-secret-code",
  "accept": "application/json",
  "content-type": "application/json"
}
```

### Version Published

This webhook is triggered any time a new Contract Version is published.

```json Request Body
{
  "deliverable": true,
  "type": "webhook",
  "integration": "123",
  "sent_to": "https://example.com",
  "event_type": "version_published",
  "description": "John Doe published version 17.1 of Terms of Service",
  "site": 1,
  "version": "5f904073c545986f47ecc1ec",
  "contract": 123,
  "user": 1,
  "created_time": "2020-10-21T14:07:01.230Z",
  "updated_time": "2020-10-21T14:07:01.231Z",
  "id": "abcd1234"
}
```

```json Request Headers
{
  "x-forwarded-for": "1.2.3.4",
  "x-forwarded-proto": "https",
  "x-forwarded-port": "443",
  "host": "example.com",
  "content-length": "358",
  "pactsafe-webhook-token": "my-secret-code",
  "accept": "application/json",
  "content-type": "application/json"
}
```

### Group Published

This webhook is triggered any time a Group is published (or republished).

```json Request Body
{
  "deliverable": true,
  "type": "webhook",
  "integration": "123",
  "sent_to": "https://example.com",
  "event_type": "group_published",
  "description": "Group Example has been published by John Doe",
  "site": 1,
  "group": 123,
  "custom_data": {
    "group_key": "group-abc123",
    "contracts": [
      1234
    ],
    "versions": [
      "abcd1234"
    ]
  },
  "created_time": "2020-10-21T13:51:09.370Z",
  "updated_time": "2020-10-21T13:51:09.370Z",
  "id": "abc123abc"
}
```

```json Request Headers
{
  "x-forwarded-for": "1.2.3.4",
  "x-forwarded-proto": "https",
  "x-forwarded-port": "443",
  "host": "example.com",
  "content-length": "358",
  "pactsafe-webhook-token": "my-secret-code",
  "accept": "application/json",
  "content-type": "application/json"
}
```

### Activity - All

This is triggered for any type of Activity on Signature Requests, Smartpacts, and Clickwraps.

> 🚧 Limit Usage
>
> Due to the potential volume of events you may send to Ironclad Clickwrap, we generally don't recommend using this webhook type unless absolutely necessary for your workflow as it could lead to many webhooks events.

```json Request Body
{
  "deliverable": true,
  "type": "webhook",
  "integration": "123",
  "sent_to": "https://example.com",
  "event_type": "activity_displayed",
  "description": "test@example.com viewed Privacy Policy in Group Example Web Group",
  "contract": 1234,
  "group": 123,
  "version": "1234abcd",
  "site": 1,
  "created_time": "2020-10-21T13:51:09.370Z",
  "activity": "abcd1234abcd1234",
  "updated_time": "2020-10-21T13:51:09.440Z",
  "id": "123abc123abc"
}
```

```json Request Headers
{
  "x-forwarded-for": "1.2.3.4",
  "x-forwarded-proto": "https",
  "x-forwarded-port": "443",
  "host": "example.com",
  "content-length": "358",
  "pactsafe-webhook-token": "my-secret-code",
  "accept": "application/json",
  "content-type": "application/json"
}
```

### Request Sent

This webhook is triggered once a Signature Request has been sent to a Signer.

```json Request Body
{
  "deliverable": true,
  "type": "webhook",
  "integration": "123",
  "sent_to": "https://example.com",
  "event_type": "request_sent",
  "description": "John Doe sent This is my request name",
  "site": 1,
  "request": "123456abcdef",
  "user": 1,
  "created_time": "2020-10-21T13:58:54.578Z",
  "updated_time": "2020-10-21T13:58:54.578Z",
  "id": "abcdef12345"
}
```

```json Request Headers
{
  "x-forwarded-for": "1.2.3.4",
  "x-forwarded-proto": "https",
  "x-forwarded-port": "443",
  "host": "example.com",
  "content-length": "358",
  "pactsafe-webhook-token": "my-secret-code",
  "accept": "application/json",
  "content-type": "application/json"
}
```

### Request Signed

This webhook is triggered once a Signer has Agreed to and completed all necessary fields in a Signature Request.

```json Request Body
{
  "deliverable": true,
  "type": "webhook",
  "integration": "123",
  "sent_to": "https://example.com",
  "event_type": "request_signed",
  "description": "John Doe signed This is my request name",
  "site": 1,
  "request": "123456abcdef",
  "signer": "a-signer-id",
  "created_time": "2020-10-21T14:01:17.360Z",
  "updated_time": "2020-10-21T14:01:17.361Z",
  "id": "abcdef12345"
}
```

```json Request Headers
{
  "x-forwarded-for": "1.2.3.4",
  "x-forwarded-proto": "https",
  "x-forwarded-port": "443",
  "host": "example.com",
  "content-length": "358",
  "pactsafe-webhook-token": "my-secret-code",
  "accept": "application/json",
  "content-type": "application/json"
}
```

### Request Complete

This webhook is triggered when all Signer(s) have agreed to the Request.

```json Request Body
{
  "deliverable": true,
  "type": "webhook",
  "integration": "123",
  "sent_to": "https://example.com",
  "event_type": "request_complete",
  "description": "This is my request name has been completed",
  "site": 1,
  "request": "123456abcdef",
  "created_time": "2020-10-21T14:01:17.395Z",
  "updated_time": "2020-10-21T14:01:17.395Z",
  "id": "abcdef12345"
}
```

```json Request Headers
{
  "x-forwarded-for": "1.2.3.4",
  "x-forwarded-proto": "https",
  "x-forwarded-port": "443",
  "host": "example.com",
  "content-length": "358",
  "pactsafe-webhook-token": "my-secret-code",
  "accept": "application/json",
  "content-type": "application/json"
}
```

### Request Expired

This is triggered when a Request has been expired.

```json Request Body
{
  "deliverable": true,
  "type": "webhook",
  "integration": "123",
  "sent_to": "https://example.com",
  "event_type": "request_expired",
  "description": "This is my request name has expired",
  "site": 1,
  "request": "abcd1234",
  "created_time": "2020-10-21T14:05:23.821Z",
  "updated_time": "2020-10-21T14:05:23.821Z",
  "id": "1234abcd"
}
```

```json Request Headers
{
  "x-forwarded-for": "1.2.3.4",
  "x-forwarded-proto": "https",
  "x-forwarded-port": "443",
  "host": "example.com",
  "content-length": "358",
  "pactsafe-webhook-token": "my-secret-code",
  "accept": "application/json",
  "content-type": "application/json"
}
```