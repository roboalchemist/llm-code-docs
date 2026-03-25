# Source: https://docs.rootly.com/integrations/generic-webhook-alert-source/generic-webhook-alert-source.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Rootly can ingest alerts from [a variety of observability provider integrations](/alerts). If your observability tool is not supported out of the box, Rootly can still accept alerts via the Generic Webhook Alert Source feature. Any observability tool that can fire a webhook event as an alert to Rootly!

Here are some of the key features supported by Rootly's Generic Webhook alert source:

* **Ingest incoming alerts without a strict API contract**
* **Trigger pages to services, teams, escalation policies, or users**
* **Automatic alert resolution**
* **Automate incident creation**

## Installation

Set up your Generic Webhook alert source so Rootly can receive and process incoming alerts from any monitoring or observability tool. Please see the [Installation page](/integrations/generic-webhook-alert-source/installation).

## Auto-Resolution

Rootly automatically evaluates webhook events against your configured resolution conditions. If an event matches those conditions but no existing alert is found, Rootly creates a new alert and triggers the target if one is defined — ensuring no alert goes uninvestigated.

Learn more in the [Auto-Resolution documentation](/integrations/generic-webhook-alert-source/auto-resolution).

## Workflows

Rootly relies on workflows to automate interactions with alerts created through generic webhooks. The [alert workflows documentation](/workflows/alert-workflows) will walk you through how to set up commonly used workflows involving Alerts.


Built with [Mintlify](https://mintlify.com).