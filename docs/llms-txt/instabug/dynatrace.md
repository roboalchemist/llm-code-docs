# Source: https://docs.instabug.com/product-guides-and-integrations/integrations/dynatrace.md

# DynaTrace

### Overview

The new Luciq integration with Dynatrace enables end-to-end tracing for network calls, connecting client-side and server-side monitoring for your network requests. By using a unique trace ID, you can follow any network request from the client to the server, providing insights for troubleshooting networking issues.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FxXeXix58Mhzrr6ybVPU9%2Fimage.png?alt=media&#x26;token=c8421ee3-01e7-4c0e-9ac1-3ddd7339a332" alt=""><figcaption></figcaption></figure>

### Prerequistes

#### Dynatrace

To use this integration, ensure the following prerequisites are met in your Dynatrace setup:

* **Supporting for W3C Context Propagation**: Have W3C enabled. W3C Trace Context support is available as an Early Adopter Release (no registration required) beginning with Dynatrace version 1.180.
  * You can enable this on Dynatrace through Settings > Server-side service monitoring > Deep monitoring > Distributed tracing.

#### Luciq

* **Supported Platforms**: This integration is only supported for iOS and Android.
* **Luciq SDK Version**: Ensure you have a minimum SDK v13.2.0 or higher on either iOS or Android.

## Integration Steps

{% hint style="info" %}
By setting up this integration, Luciq will attach a trace ID as an HTTP header to your network requests. This allows us to link network requests from Luciq to New Relic.
{% endhint %}

Go to **Settings -> Integrations -> Dynatrace** in your Luciq dashboard, and follow these integration steps:

{% stepper %}
{% step %}

#### Set Up

* Enter your Dynatrace dashboard link.
  * If you’re using Dynatrace SaaS, replace x in `x.apps.dynatrace.com` with your environment ID.
  * If you're using Dynatrace Managed (on-premises), replace x in `x.apps.dynatrace.com` with your Dynatrace domain.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2Fh3tVQKFv1aXNfn6Hh3oX%2Fimage.png?alt=media&#x26;token=c9f83064-c6d8-4bf9-b59d-ea83df053eb6" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Test

* Validate the Dynatrace dashboard link to ensure it is correct.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FBP9SUN56Iegj8KqpS7tZ%2Fimage.png?alt=media&#x26;token=39e16d7c-f1dc-4985-974c-d8d35b891abb" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Finish

* Ensure the **APM - Network Requests** checkbox is checked to trace network requests to Dynatrace.
* Give your integration a name and save the integration.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FwNGNv01YPStdWaucIQjf%2Fimage.png?alt=media&#x26;token=c0545226-70d2-4185-a331-ae46f2eea18d" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### Using the Integration

When a network occurrence is logged, a unique trace ID will appear on the occurrence page in the Luciq dashboard.

Navigate to any network occurrence received after you created the integration, click on “View on Dynatrace” to view the same network occurrence on your Dynatrace dashboard.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2Fk7k5PFy52umHfF0QYaqi%2Fimage.png?alt=media&#x26;token=e4b7836a-45eb-4018-8752-29a537d4d179" alt=""><figcaption></figcaption></figure>
