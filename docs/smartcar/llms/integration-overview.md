# Source: https://smartcar.com/docs/getting-started/integration-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate with Smartcar To Receive Vehicle Data

> Welcome to the integration phase of your Smartcar journey! After configuring your application and connecting vehicles, the next crucial step is to integrate your systems with Smartcar to receive vehicle data.

## Choosing Webhooks or the REST API

Understanding the differences between webhooks and the REST API will help you choose the right integration method for your use case.

### When to Use Webhooks

**[Webhooks](/integrations/webhooks/overview) are the recommended approach** for applications that need real-time or frequently updated vehicle data. Use webhooks when:

* You need real-time notifications when vehicle data changes
* You're monitoring vehicle data continuously (e.g., fleet tracking, charging monitoring)
* You're building applications that react to vehicle events (e.g., alerts, automation)
* You need to scale to monitor many vehicles efficiently
* You want to avoid rate limits and reduce server load

**Advantages of webhooks:**

* **Require less effort and resources** - no polling the API repeatedly
* **Scale better** - Scale effortlessly to monitor thousands of vehicles, with no complex polling logic to maintain
* **Near real-time updates** - receive data within seconds of changes being detected
* **Avoid rate limits** - Smartcar pushes data to you instead of you calling the API
* **More reliable** - no missed updates due to polling intervals
* **Automatic optimizations** - Smartcar continuously optimizes data retrieval, and your application benefits immediately without code changes

**Quick Start**: Deploy a production-ready webhook receiver in minutes with our [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe) - a complete AWS serverless solution that implements best practices for you.

Learn more about [Webhooks](/integrations/webhooks/overview).

### When to Use the REST API

The Vehicles API is designed for **infrequent data retrieval and command execution**. Use the API when:

* You need vehicle data only once or occasionally (e.g., user profile display)
* You're issuing commands to vehicles (lock/unlock, start/stop charging)
* You're exploring available signals or testing your integration
* You have a small number of vehicles and don't need continuous monitoring

The Vehicles API is designed primarily for exploration and non-frequent data retrieval. This API is not designed for continuous polling or real-time monitoring. Data is typically updated once every 24 hours unless the vehicle is actively subscribed to a webhook, which enables more frequent updates. For most use cases, you should avoid polling the Vehicles API at high frequency leverage [webhooks](/integrations/webhooks/overview) instead.

Learn more about the [Vehicles API](/api-reference/vehicles-api-intro).

<Warning>
  **Do not poll the Vehicles API for real-time monitoring.** The API is not designed for continuous polling. Frequent polling will:

  * Consume your API rate limit quota quickly
  * Put unnecessary load on your servers and Smartcar's infrastructure
  * Provide stale data (updated only every 24 hours without webhook subscriptions)
  * Not scale as your fleet grows

  Use webhooks instead for any use case requiring frequent or real-time data.
</Warning>

***

## CSVs (coming soon)

This integration will help you receive vehicle data in a CSV file where you can integrate analyze using your existing tools and workflows.

With CSV integrations, you will be able to:

* Receive vehicle data from Smartcar at a specified cadence (e.g., weekly, monthly)
* Choose the data fields you want to include in the CSV export (e.g., vehicle info, location, odometer, battery level)
* Have CSV files automatically delivered to your preferred destination, such as an SFTP server, cloud storage bucket, etc.
* Easily import Smartcar data into your analytics, reporting, or business intelligence tools

This solution is ideal for customers who need scheduled, automated data exports for compliance, reporting, or integration with legacy systems.

<Note>
  CSV integration is coming soon! If you are interested in early access or have specific requirements, please reach out to <a href="mailto:support@smartcar.com">[support@smartcar.com](mailto:support@smartcar.com)</a>.
</Note>
