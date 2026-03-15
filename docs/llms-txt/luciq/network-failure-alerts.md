# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/automation-and-workflows/alerts-and-rules/network-failure-alerts.md

# Network Failure Alerts

Luciq now gives you more control and precision when setting up alerts for failed network requests. With our enhanced alerting capabilities, you can receive alerts tailored to specific types of failures, allowing your team to act faster and more efficiently.

### 🔍 Filter Alerts by Failure Type

You can now specify whether the alert should trigger for:

* **Client-Side Failures:** Failures occurring on the user's device (e.g., timeout, no internet).
* **Server-Side Failures:** Failures returned from your backend (e.g., 500 Internal Server Error).

This gives you the ability to monitor the type of failures that matter most to your team.

<figure><img src="https://files.readme.io/b97abb5a6918a1ba0f2deff95ab68af06ea9b89415eb0fce53e2f775a9f347c2-image.png" alt=""><figcaption></figcaption></figure>

### 🎯 Add Extra Filters for Granularity

In addition to filtering by failure type, you can further narrow down alerts using the following criteria:

1. **HTTP Status Code**

Include/Exclude specific HTTP response codes in your alerts, such as:

* `500` for internal server errors
* `404` for not found
* `401` for unauthorized access<br>

  <figure><img src="https://files.readme.io/6319ea0f31ee4ade9d6b7818a997ee69bb3dee2b3ac257337c160c1dfd858326-image.png" alt=""><figcaption></figcaption></figure>

2. **Failure Name**

Use the failure name to detect specific issues, especially useful when failure codes are not available (as is often the case with client-side issues).

> **What is a Failure Name**?
>
> A failure name is the descriptive message sent alongside a failure event. You can view failure names by:
>
> * Navigating to the **Network tab** on your dashboard
> * Selecting the network request of interest
> * Scrolling to the **Failures** section
> * Checking the value under the **Name** column

This enables you to create highly targeted alerts—like catching `NoConnectionError` or `TimeoutException` events.

<figure><img src="https://files.readme.io/a7fc972a59271fc122cb837fd0ceaedd0fca610cd8277e93b29b0447cdb7e01c-image.png" alt=""><figcaption></figcaption></figure>
