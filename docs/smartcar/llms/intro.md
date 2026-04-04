# Source: https://smartcar.com/docs/api-reference/intro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Smartcar APIs

> Here you'll find everything you need to integrate with Smartcar via REST APIs. Learn how to connect and manage Smartcar's Vehicles API, Management API, and Compatibility API through a simple interface.

Welcome to the Smartcar API Reference! Here you’ll find everything you need to integrate with Smartcar and build applications that can reach to millions of vehicles.

Smartcar provides three main APIs, each designed for a specific part of your integration:

## Vehicles API

The **Vehicles API** lets you access standardized vehicle data and send commands to connected vehicles. Use this API to:

* Retrieve signals such as battery level, odometer, location, and more
* Issue commands like lock/unlock or start/stop charging
* Access vehicle attributes and diagnostic information

All requests to the Vehicles API require an access token obtained via the [OAuth2 authorization flow](/getting-started/how-to/get-an-access-token).

The Vehicles API is designed primarily for exploration and non-frequent data retrieval. This API is not designed for continuous polling or real-time monitoring. Data is typically updated once every 24 hours unless the vehicle is actively subscribed to a webhook, which enables more frequent updates. For most use cases, you should avoid polling the Vehicles API at high frequency leverage [webhooks](/integrations/webhooks/overview) instead.

* [Vehicles API Reference](/api-reference/vehicles-api-intro)
* [Standard Signal Schema](/api-reference/signals/schema)
* [Permissions](/api-reference/permissions)

## Management API

The **Management API** allows you to manage vehicle connections at the application level. Use this API to:

* List all vehicles connected to your application
* Remove (disconnect) vehicles
* Unsubscribe vehicles from a webhook

The Management API uses a separate management token for authentication, which you can find in your [Smartcar Dashboard](https://dashboard.smartcar.com/).

* [Management API Reference](/api-reference/management/get-vehicle-connections)
* [Delete Vehicle Connections](/api-reference/management/delete-vehicle-connections)
* [Unsubscribe Webhook](/api-reference/webhooks/unsubscribe-webhook)

## Compatibility API

The **Compatibility API** helps you determine if a specific vehicle is supported by Smartcar before launching the Connect flow. Use this API to:

* Query supported makes and regions

This API is useful for improving user experience by verifying eligibility up front.

* [Compatibility by VIN](/api-reference/compatibility/by-vin)
* [Compatibility by Region and Make](/api-reference/compatibility/by-region-and-make)

***

<Card title="Starter app" icon="github-alt" href="https://github.com/smartcar/starter-app-react-node" horizontal="true">
  Easily connect a vehicle and make API requests using our starter app.
</Card>

<Card title="Postman" icon="rocket" href="https://www.postman.com/smartcar/smartcar-api/collection/fqmwehs/smartcar-api" horizontal="true">
  Get a feel for the API using our Postman collection.
</Card>
