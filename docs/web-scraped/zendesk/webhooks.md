# Webhooks

Source: https://developer.zendesk.com/documentation/webhooks/

Send HTTP requests based on activity in Zendesk

## On this page

- Getting started with webhooks
- Event schema

Webhooks let you build or set up integrations that subscribe to certain activity
in Zendesk Support, Guide, Gather, and Messaging. When this activity occurs,
Zendesk sends a HTTP request to the webhook's configured URL.

For example, you can configure a webhook to send requests when a user is deleted
or a new ticket is created.

## Getting started with webhooks

Creating and monitoring webhooks

Use the Webhooks API to create a webhook and learn about the ways you connect a
webhook to activity in Zendesk Support, Guide, Gather, and Messaging. The guide also
covers webhook retry logic and how to monitor webhooks using the API.

Anatomy of a webhook request

Learn about the supported headers, methods, formats, and payloads for HTTP
requests sent by webhooks.

Webhook security and authentication

Send authenticated requests from a webhook using API tokens.

Verifying webhook authenticity

HTTP requests from a Zendesk webhook include an encrpyted digital signature. Use
this signature and a signing secret to verify that requests are genuine and come
from Zendesk.

## Event schema

Webhook event types

If your webhook subscribes to events for user or organization activity, it sends
HTTP POST requests with predefined JSON payloads. This reference documentation
contains a list of available events and related request payloads.

Join our developer community Forum Blog Slack Zendesk 181 Fremont Street, 17th Floor, San Francisco, California 94105 Privacy Notice Zendesk Developer Terms System Status
