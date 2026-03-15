# Source: https://docs.instabug.com/product-guides-and-integrations/integrations/grafana/grafana-end-to-end-tracing.md

# Grafana End to End Tracing

### Overview

The new Luciq integration with Grafana enables end-to-end tracing for network calls, connecting client-side and server-side monitoring for your network requests. By using a unique trace ID, you can follow any network request from the client to the server, providing insights for troubleshooting networking issues.

<figure><img src="https://files.readme.io/4bd25ca9e1e739dd0e7fb97cc9ba2c52753934cafb3e18703cf2cc3184092852-grafana-end-to-end-tracing-1.png" alt=""><figcaption></figcaption></figure>

### Prerequisites

* **Backend**
  * **Agent Supporting W3C Context Propagation:** Ensure your backend agent supports W3C context propagation.

{% hint style="info" %}

### **Note**

If you use any trace sampling algorithms, Grafana may drop some traces. Consequently, you might see network requests in Luciq that are not available in Grafana.
{% endhint %}

* **Luciq's Side**
  * **Supported Platforms**: This integration is only supported for iOS and Android.
  * **Luciq SDK Version**: Ensure you have Luciq SDK version 13.2.0 or higher for both iOS and Android.
  * If you are manually logging the network they need to:
    * Either send the `httpUrlConnection` or make sure you send all headers in the request
    * If you are masking the headers, make sure you don't remove the `traceparent` header

### Integration Steps

{% hint style="info" %}
By setting up this integration, Luciq will attach a trace ID as an HTTP header to your network requests. This allows us to link network requests from Luciq to Grafana.
{% endhint %}

* To create a Grafana Integration go to Settings -> Integrations -> Grafana in your Luciq dashboard.

1. **Setup**

   <figure><img src="https://files.readme.io/9e2d5dfb85b11639420139bc1d4a5f978ebf5639d213b5bc143a9987ccaf40f4-grafana-end-to-end-tracing-2.png" alt=""><figcaption></figcaption></figure>

* Enter the link to **the Grafana dashboard with the network traces** to link to Luciq.
* Create a `traceID` variable in that Grafana dashboard, and **ensure the URL includes the** `traceID` **variable key at the end**.
* For example:\
  `https://organization.grafana.net/d/<dashboard-id>/your-traces-dashboard?orgId=1&var-traceid=`
* For self-hosted Grafana, contact <support@Luciq.com> to whitelist your domain.

2. **Test**:

* Validate the Grafana dashboard link to ensure it is correct.

  <figure><img src="https://files.readme.io/647c6717e6c8b91b26c33b9b1883b15adb367fc2fa0f935ea1459840abd6df4d-grafana-end-to-end-tracing-3.png" alt=""><figcaption></figcaption></figure>

3. **Finish**:

* Ensure the APM - Network Requests checkbox is checked to trace network requests to Grafana.
* Give your integration a name and save the integration.

  <figure><img src="https://files.readme.io/94d3766090f21cd7817b8bee1ab892c27682e6d59ab5bbdc35a8a1babaa595a1-grafana-end-to-end-tracing-4.png" alt=""><figcaption></figcaption></figure>

### Using the Integration

When a network occurrence is logged, a unique trace ID will appear on the occurrence page in the Luciq dashboard.

1. Navigate to a network occurrence in Luciq.
2. Click on **View on Grafana** to verify that it redirects you to the correct Grafana dashboard, filtered by the `TraceID`.

   <figure><img src="https://files.readme.io/87c0b8b5249d9f36ca77b3b96e3d2f9994fbfaf4d40d85cf4dd63f793a0bc629-grafana-end-to-end-tracing-5.png" alt=""><figcaption></figcaption></figure>
