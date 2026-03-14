# Source: https://tyk.io/docs/getting-started/configure-first-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tyk QuickStart: Configure Your First API

> Configure your first API on Tyk Cloud

## Overview

This guide helps you get started with Tyk by covering the basics:

* **Set up your API**: Create and configure a new API in the Tyk Dashboard.
* **Create API keys**: Generate API keys and assign them to your APIs for secure access.
* **Monitor API performance**: Track traffic, logs, and performance analytics.

Follow these steps to quickly and easily create and manage your APIs with Tyk.

> This page focuses on getting started with Tyk Cloud, If you are looking for information on Tyk Self-Managed, please refer to the [Getting Started with Tyk Self-Managed Guide](/getting-started/quick-start).

## Prerequisites

To start quickly, we'll use Tyk Cloud in this guide.

Before you begin, make sure you have:

* [A Tyk Cloud account](https://tyk.io/sign-up/#cloud).
* Admin access to the Tyk Dashboard.
* (optional) A backend service that your API will proxy (e.g., a RESTful API) - or you can use the httpbin service.

## Set Up Your API

Start by creating a new API in Tyk Cloud:

1. **Log in to the Tyk Dashboard.**.
2. **Navigate to APIs** and click **Add New API** or **Design From Scratch** button.

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-account-design-from-scratch.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=59e30dfd6088c21e2fbbf6a6c66488e0" alt="Create New API" width="2940" height="1652" data-path="img/getting-started/create-account-design-from-scratch.png" />

3. **Configure API Details**:

* **API Name**: Name your API (e.g., `My First API`).
* **API Type**: Choose from HTTP, TCP, GraphQL, UDG, or Federation, depending on your use case.
* **API Style**: Select OpenAPI for standardized HTTP APIs or Classic for flexible configurations and non-HTTP APIs.
* **Target URL**: Provide the URL of your backend service (e.g., `http://httpbin.org`).

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-new-api.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=93bf93b4e5847675da64c6edebbfa2a5" alt="Create New API" width="3024" height="1724" data-path="img/getting-started/create-new-api.png" />

4. **Connect to Your Desired Gateway**:

You will be prompted to choose between a Gateway and an Edge Gateway, which are already created for you.

* `Edge Gateways` generally provide low-latency, regionally distributed API processing, ideal for a global user base.
* `Regular Gateways` centralize API management, offering comprehensive API processing without additional edge optimizations.

<img src="https://mintcdn.com/tyk/zB4143fn76CY8N8G/img/getting-started/apis-connect-gateways.png?fit=max&auto=format&n=zB4143fn76CY8N8G&q=85&s=36102e37b8d4f1ea57e461be507fe1af" alt="Connect Gateways" width="2932" height="1628" data-path="img/getting-started/apis-connect-gateways.png" />

5. **Configure your API Settings**:

* **Expiration Date**: An optional config that allows you to set an expiry date for this API, where access will expire after this date. This can be edited at any time.
* **Gateway Status**: Setting this to `Active` will publish your API and make it public. When in the `Disabled` state, your API will stay in a draft state until you are ready to publish it. This is a required field; for this guide, we will set it to `Active`.
* **Access**: Your API can be set to either `Internal` or `External`, determining whether you want to keep your API accessible only through Tyk or to external services, respectively. This is a required field; for this guide, we will set it to `External`.

<img src="https://mintcdn.com/tyk/zB4143fn76CY8N8G/img/getting-started/apis-configure-settings-1.png?fit=max&auto=format&n=zB4143fn76CY8N8G&q=85&s=8b5e1473ec0ec656d35348bf173b4293" alt="Configure Settings" width="2940" height="1658" data-path="img/getting-started/apis-configure-settings-1.png" />

Scrolling down, in the **Upstream** section, you can configure settings to control the behaviour of your upstream APIs.

<Note>
  These are not necessary to add now, but they are good to explore.
</Note>

* **API Rate Limiting**: Set limits on the number of requests (e.g., 100 requests per minute) to control usage and prevent abuse.
* **Service Discovery**: Enable dynamic backend discovery with tools like Consul or Kubernetes, ensuring traffic is directed to healthy instances.
* **Upstream Client Certificates**: Use client certificates for secure backend connections via mutual TLS (mTLS), adding an extra layer of security.
* **Certificate Public Key Pinning**: Pin specific public keys to validate certificate authenticity and prevent unauthorized access.

<img src="https://mintcdn.com/tyk/zB4143fn76CY8N8G/img/getting-started/apis-configure-settings-2.png?fit=max&auto=format&n=zB4143fn76CY8N8G&q=85&s=ea907dbda939a7782575db649a87d63a" alt="Configure Settings cont" width="2426" height="1488" data-path="img/getting-started/apis-configure-settings-2.png" />

6. **Configuring the Server section**:

In this section, you can configure Tyk Gateway related settings. Below are some important configurations.

* **Listen Path**: This is the `path` Tyk API will use to proxy your API requests. So a request made to this URL `https://<tyk-clou-url>/<listen-path>` will be proxied to the upstream URL configured above.
* **Authentication**: Choose the desired authentication method (e.g., **API Key**).

  <img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-api-select-authentication.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=92820e3999be6284edf3fe4bbfb6475f" alt="Add Authentication" width="3024" height="1722" data-path="img/getting-started/create-api-select-authentication.png" />

Save your API configuration once complete.

7. **Copy the API URL**

* When you save the API configuration, Tyk generates a unique Gateway URL that can be used to access your API. Copy this URL, we will use it later during testing.

  <img src="https://mintcdn.com/tyk/zB4143fn76CY8N8G/img/getting-started/api-url-provided-by-tyk.png?fit=max&auto=format&n=zB4143fn76CY8N8G&q=85&s=7e1f9c2fb48756d889b7ceb9a6e212ba" alt="Tyk API Gateway URL" width="3024" height="1724" data-path="img/getting-started/api-url-provided-by-tyk.png" />

## Create an API Key

The Tyk Dashboard provides the simplest way to generate a new API key. Follow these steps:

1. **Select "Keys"** from the **API Security** section and **Click "Add Key"** to generate a new key.

   <img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-api-security-key.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=cd65a6f17bfecd05aa9342f133a2addf" alt="Create API Key" width="3024" height="1723" data-path="img/getting-started/create-api-security-key.png" />

2. **Add a Policy or API to Your Key**:

   * You can either add your key to an existing **Policy** or assign it to an individual **API**.
   * For this guide, we will assign the key to the `My First API`, which we created in the previous step. You can:
     * Scroll through your **API Name list**,
     * Use the **Search field** or **Group by Authentication Type** to filter APIs.
   * Leave all other options at their default settings.

   <img src="https://mintcdn.com/tyk/zB4143fn76CY8N8G/img/getting-started/configure-api-key.png?fit=max&auto=format&n=zB4143fn76CY8N8G&q=85&s=10cb7ab53ea8db81fdf9f5c365ae8318" alt="Configure API Key" width="3024" height="1723" data-path="img/getting-started/configure-api-key.png" />

3. Click on the **Configuration Tab** and add the below details.
   * **Enable Detailed Logging**: This is optional and disabled by default.
   * **Key Alias**: Assign an alias to your key for easier identification.
   * **Key Expiry**: Set an expiry time from the drop-down list. This is required.
   * **Tags**: Add tags for filtering data in Analytics. Tags are case-sensitive.
   * **Metadata**: Add metadata such as user IDs, which can be used by middleware components.

4. Click **CREATE**:

   * Once the key is created, a **Key successfully generated** pop-up will be displayed showing your key. **Copy the key ID** to your clipboard and save it for future reference, as it will not be shown again. And that should result in a successfully generated key!

   <img src="https://mintcdn.com/tyk/zB4143fn76CY8N8G/img/getting-started/apis-keys-success.png?fit=max&auto=format&n=zB4143fn76CY8N8G&q=85&s=0e87723952c31ade3b5a3b27e148dc5b" alt="Key Success" width="1156" height="720" data-path="img/getting-started/apis-keys-success.png" />

<Note>
  When creating a key in Tyk, you should copy the key ID. This is the identifier you’ll need for referencing the key in your API requests or configurations. The hash is generally used internally by Tyk and is not required for most user-facing tasks.
</Note>

## Test Your API

After configuring and deploying your API, it’s essential to test it to ensure it performs as expected. Follow these steps to verify your API setup:

1. **Retrieve Your API Key**:
   * Copy the **API Key ID** from the previous step as you'll need it to authenticate requests to your API.

2. **Make a Test Request**:
   * Use a tool like [Postman](https://www.postman.com/) or `curl` to send a request to your API endpoint.
   * Example request using `curl`:
     ```bash  theme={null}
     curl -H "Authorization: {YOUR_API_KEY_ID}" https://{YOUR_TYK_GATEWAY_URL}/my-first-api/
     ```
   * Replace `{YOUR_API_KEY_ID}` with the actual key ID and `{YOUR_TYK_GATEWAY_URL}` with your gateway's URL.
   * Send the request and you should get HTML output with `200` status code.

## Monitor Traffic and Analyze API Performance

With your API live, monitor its traffic and analyze performance:

### View Traffic Analytics

1. **Navigate to the Monitoring Section** in the dashboard. And click on **Activity Overview**.
2. **View Traffic Metrics**: Review metrics such as request count, response times, and error rates.
3. **Analyze Data**: Use traffic trends to identify performance issues or optimize API behavior.

<img src="https://mintcdn.com/tyk/zB4143fn76CY8N8G/img/getting-started/apis-analytics.png?fit=max&auto=format&n=zB4143fn76CY8N8G&q=85&s=9d3f9eb44939859738c22d7a8c242410" alt="APIs Analytics" width="3024" height="1717" data-path="img/getting-started/apis-analytics.png" />

### View Log Data

1. **Go to the Activity Logs Section** of your API.
2. **Search and Filter Logs**: Use filters to drill down by response status, endpoint, or client IP.
3. **Review Detailed Logs**: View full request and response data to troubleshoot issues.

<img src="https://mintcdn.com/tyk/zB4143fn76CY8N8G/img/getting-started/api-activity-logs.png?fit=max&auto=format&n=zB4143fn76CY8N8G&q=85&s=278c14c91c0b2815888e7848482974d8" alt="APIs Logs" width="3024" height="1964" data-path="img/getting-started/api-activity-logs.png" />

## Next Steps

Congratulations! You've successfully created, secured, and deployed your first API in Tyk Cloud. Next, explore more advanced features such as adding [rate limiting](/api-management/rate-limit#introduction) to protect your API from abuse.

Explore more features in your [dashboard](/getting-started/using-tyk-dashboard) to optimize and scale your API offerings.


Built with [Mintlify](https://mintlify.com).