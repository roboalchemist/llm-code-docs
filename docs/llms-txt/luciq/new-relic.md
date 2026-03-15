# Source: https://docs.luciq.ai/product-guides-and-integrations/integrations/new-relic.md

# New Relic

### Overview

The new Luciq integration with New Relic enables end-to-end tracing for network calls, connecting client-side and server-side monitoring for your network requests. By using a unique trace ID, you can follow any network request from the client to the server, providing insights for troubleshooting networking issues.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FzOYjXAAabdJhQI1upjXZ%2Fimage.png?alt=media&#x26;token=79fe39e4-0a64-4e10-807b-f509b63953f2" alt=""><figcaption></figcaption></figure>

### Prerequisites

#### New Relic

To use this integration, ensure the following prerequisites are met in your New Relic setup:

* **Distributed Tracing in Your Plan**: Ensure that your New Relic plan includes distributed tracing.
* **New Agent Supporting W3C Context Propagation**: You need to use a New Relic agent that supports W3C context propagation. More details can be found [here](https://newrelic.com/blog/nerdlog/w3c-trace-context-distributed-tracing-standard).
* **Enable Distributed Tracing in Backend Agent**: Distributed tracing must be enabled in your backend agent. More information is available [here](https://docs.newrelic.com/docs/distributed-tracing/concepts/quick-start/).

{% hint style="info" %}
Note: if you use any trace sampling algorithms, New Relic may drop some traces. Consequently, you might see network requests in Luciq that are not available in New Relic.
{% endhint %}

#### Luciq

* **Supported Platforms**: This integration is only supported for iOS and Android.
* **Luciq SDK Version**: Ensure you have a minimum SDK v13.2.0 or higher on either iOS or Android.

### Integration Steps

{% hint style="info" %}
By setting up this integration, Luciq will attach a trace ID as an HTTP header to your network requests. This allows us to link network requests from Luciq to New Relic.
{% endhint %}

Go to **Settings** -> **Integrations** -> **New Relic** in your Luciq dashboard, and follow these integration steps:

{% stepper %}
{% step %}

#### Set Up

Enter your New Relic dashboard link. If you use custom domains for New Relic, replace `one.newrelic.com` with your company domain (e.g., `x.newrelic.com`). For redirecting to multiple organizations from the same app, use `one.newrelic.com`.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FsDIyAE1a6HAGYUbkd8FC%2Fimage.png?alt=media&#x26;token=bf101d4b-3477-46b2-98b3-91675129fb9a" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Test

Validate the New Relic dashboard link to ensure it is correct.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FNvRP74Zpf4YDtEkzWH0j%2Fimage.png?alt=media&#x26;token=20eef3c2-2645-49e6-bbe2-d740237bf413" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Finish

Ensure the APM - Network Requests checkbox is checked to trace network requests to New Relic, then give your integration a name and save the integration.
{% endstep %}
{% endstepper %}

## Using the integration

When a network occurrence is logged, a unique trace ID will appear on the occurrence page in the Luciq dashboard.

{% stepper %}
{% step %}

#### Copy the Trace ID

Navigate to any network occurrence and **copy the Trace ID**.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FfO98T9T7xfLGCKs10NJW%2Fimage.png?alt=media&#x26;token=ca6644f0-65d5-42fd-93e1-95a06630fdd5" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### View on New Relic

Click on "**View on New Relic**" to go to the traces page in New Relic.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FjUBeua90sIWI8YCqm9uM%2Fimage.png?alt=media&#x26;token=591a47ce-78a2-4d1a-bea4-214beb891161" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Filter by Trace ID

**Paste the Trace ID into the filter** in New Relic (traceid = xxxxx) to view the same trace.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F0Dx0FuOPTQVoqm4xbciV%2Fimage.png?alt=media&#x26;token=1d3a4b86-fb5d-4df0-b58b-a1a81d3edb44" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
