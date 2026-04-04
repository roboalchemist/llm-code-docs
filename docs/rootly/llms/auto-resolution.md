# Source: https://docs.rootly.com/integrations/generic-webhook-alert-source/auto-resolution.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto-Resolution 

> Auto-resolution automatically resolves or routes webhook alerts by matching them to existing alerts when possible, or creating and appropriately targeting new alerts based on payload fields or Alert Routes when no match is found.

## Overview

Rootly supports **automatic alert resolution** for alerts received through the **Generic Webhook Alert Source**.\
This means Rootly can automatically resolve alerts when your monitoring system sends a webhook event that matches your defined **Resolution Conditions** — for example, an event where the payload indicates that an alert’s state has cleared.

## How Auto-Resolution Works

When Rootly receives an incoming webhook event from your monitoring tool, it follows this evaluation process:

1. **Incoming Webhook Event**\
   Rootly ingests the webhook payload from your monitoring or observability tool.
2. **Check for Matching Auto-Resolution Logic on an Existing Alert**\
   Rootly compares the payload against your configured **Resolution Conditions**.
   * If the event **matches** and a corresponding alert (same **unique identifier**) exists, Rootly **resolves that alert**.
   * If the event **matches** the Resolution Conditions but **no matching alert** is found, Rootly **creates a new alert**.
3. **Check for Target**\
   When a new alert is created (because no existing alert was found):
   * If a **target** (such as a service, team, or escalation policy) is specified in the **webhook URL** or **payload body**, Rootly will **trigger that target destination**.
   * **Otherwise**, Rootly will **evaluate any configured Alert Route** for the webhook to identify the appropriate **target to page**.
   * If **no target** is specified, Rootly will still create a **non-paging/open alert** to ensure the event is logged and visible.

This logic ensures all incoming alerts from your webhook that have a defined target are either:

* **Resolving an existing alert**, or
* **Being routed for investigation** per your escalation policy.

Nothing is ignored or silently dropped.


Built with [Mintlify](https://mintlify.com).