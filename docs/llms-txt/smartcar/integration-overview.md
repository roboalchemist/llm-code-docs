# Source: https://smartcar.com/docs/getting-started/integration-overview.md

# Integrate with Smartcar To Receive Vehicle Data

> Welcome to the integration phase of your Smartcar journey! After configuring your application and connecting vehicles, the next crucial step is to integrate your systems with Smartcar to receive vehicle data.

## The architecture that's right for you

<Info>
  Webhooks are the recommended way to receive real-time vehicle data from Smartcar. You can still use the REST API for retrieving data and issuing commands, but webhooks are the most scalable and reliable option for most use cases.
</Info>

## Webhooks

[Webhooks](/integrations/webhooks/overview) are the most efficient way to receive real-time vehicle data. Smartcar sends you a payload whenever a vehicle event occurs, such as a change in battery level or location. This allows you to build applications that respond instantly to vehicle changes without polling an API.

**Quick Start**: Deploy a production-ready webhook receiver in minutes with our [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe) - a complete AWS serverless solution.

Get started with Webhooks [here](/integrations/webhooks/overview).

## REST APIs

If you prefer to retrieve data on demand, you can use the Smartcar [Vehicles API](/api-reference/vehicles-api-intro). This allows you to query vehicle data at any time, but it may not be as efficient for real-time applications. The Vehicles API provides endpoints for accessing signals, issuing commands, and retrieving vehicle attributes.

The Vehicles API is designed primarily for exploration and non-frequent data retrieval. This API is not designed for continuous polling or real-time monitoring. Data is typically updated once every 24 hours unless the vehicle is actively subscribed to a webhook, which enables more frequent updates. For most use cases, you should avoid polling the Vehicles API at high frequency leverage [webhooks](/integrations/webhooks/overview) instead.

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
