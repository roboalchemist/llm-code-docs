# Source: https://docs.shipstation.com/getting-started

Getting Started with ShipStation API V2




[![ShipStation Developer](/assets/logo-ss-api.ec8fa1da9c60670d3bcab24ceeb8f32be01e624584c3106975db87878853f13c.de6e0f62.svg)](/)

[Docs](/getting-started)

[Status Page](https://status.shipstation.com/)

[Login](https://ship.shipstation.com/)

[Sign up](https://www.shipstation.com/step1/)

Search/

* Getting Started

[+ Getting Started](/getting-started)

[+ Introduction to REST](/rest)

[+ Security & Authentication](/authentication)

[+ Usage & Rate Limits](/rate-limits)

* Guides

* Full API Reference

* Release Notes

[Getting Started](/getting-started)

/

Getting Started

Last updated  1 week ago

Getting Started with ShipStation API V2
=======================================

Welcome to ShipStation API V2 documentation!

ShipStation API V2 includes several highly requested capabilities not currently available in [our V1 version](https://www.shipstation.com/docs/api/), including batch labels, return labels, and manifest endpoints. Each can be used on its own or in conjunction with other features to build powerful shipping functionality into your application or service.

ShipStation API V2 is currently in an early release stage, which means you may find edgecases when trying out this API. While the API is tested and stable, we know that our users have creative and unique implementations that we may not have forseen. We also know that there may be familiar features from the V1 API that we have not implemented in this V2 API yet. If you have any feedback about unexpected behavior or a feature that you're looking forward to using please get in touch.

If you're new to REST APIs, be sure to read our [introduction to REST](/rest) to understand the basics, as well as our [Security & Authentication page](/authentication).

If you are looking for the ShipStation openAPI (AKA, ShipStation API V1), please visit the ShipStation API V1 docs page currently located at [shipstation.com/docs](https://www.shipstation.com/docs/api/).

Using the Shipping API
----------------------

To access the majority of the endpoints in this documentation, you will need to be on a plan that offers shipping functionality. You can check your API Settings page to see if your plan supports API access and grab your API key while you're there. Make sure to save your API key in a secure place, as it is only available when generated.

Enable the Inventory API Add-On
-------------------------------

To access the ShipStation API Inventory endpoints, you must first enable the Inventory API add-on in your ShipStation account settings.

1. Log into your ShipStation account.
2. Go to Settings and choose Add-Ons.
3. Click the option to try out the API add-on you'd like to use (the Shipping API, Inventory API, or both).

![Shipping API add-on on the ShipStation Settings Add-Ons page](/assets/set_addon_shippingapi_mrk.15510b629a4505b96779588ee7445ef6ae8816d3c03aa2f5063636958a51c14e.9b2e0d84.png)

Once either of the add-ons are enabled, you can go to `Settings > Account > API Settings` and generate your API key.

Shipping API Feautres
---------------------

With the **Shipping API**, you can access the following capabilities:

* Rate shopping via a dedicated rates endpoint
* Create and Update shipments
* List, tag, and cancel shipments
* Create, download, list, and void labels
* Create and Update Products
* Create multi-package labels
* Create and manage batched labels via a batches endpoint
* Create return labels
* Create custom package types
* Create and list manifests via a manifests endpoint
* Schedule pickups via pickups endpoint
* List users

Many more highly requested capabilities will be added in the coming months, including a dedicated address validation endpoint and tracking endpoint.

### Common Terminology

As ShipStation has evolved, the language that we use to describe objects in our datamodel has also evolved. Here are some common terms in the V2 API:

* **Sales Order**: An immutable object that contains information received from an order source connection. This object is not currently represented in full in the API, but you'll find properties inherited from it on the Shipment object.
* **Shipment**: An object that inherits properties from a Sales Order, that can be manipulated as needed to ship items from a Sales Order. While a Shipment necessarily resides in one store, the items from that Shipment may come from several Sales Orders. This separation between the Sales Order and the Shipment is helpful for workflows that aim to create a single Label for items originating in different Sales Orders.

**Label**: An object that is created from a Shipment that includes carrier label data. A label is immutable with the exception of voiding. Documents on a label are stored for a finite period, so you must store them locally if you need them to persist.

### Creating and Updating Shipments

We have recently released the ability to create and update Shipments. To make a Shipment appear in the Orders tab, make sure that you are passing `create_sales_order`: true in your request.

Additionally, please integrate with these functions carefully as an action such as nulling out the items on a Shipment may cause issues when attempting to notify the marketplace on label creation. We advise setting up a duplicate store connection when building your integration to these endpoints to avoid any unintended disruption in your production workflow.

### Rate Shopping

Make sure you ship as cost-effectively as possible by comparing rates across carriers using our [Rates endpoint](/rate-shopping). You can also [get rate estimates](/retrieve-rates) if you don’t have the full shipment details at hand.

### Batches, Multi-Package Labels, and Return Labels

Batch labels, multi-package labels, and return labels are now possible with ShipStation API v2.

* When using the [batches endpoint](/batch-labels), you can process labels in bulk and receive a large number of labels and customs forms in bulk responses. Batching is ideal for workflows that need to process hundreds or thousands of labels quickly.
* [Multi-package labels](/create-labels#multi-package-labels) allow you to create multiple labels for a single shipment that contains multiple packages, without first splitting items into separate shipments (selected carrier must support multi-package labels). To create a multi-package label, you add each package’s details to the `packages` array in a label request’s `shipment` object.
* You now have two methods available for creating [return labels](/return-labels) with the API: set the return label property to `true` in your create label request, and create a return label for a specific `label_id`.

### Manifests

With the [manifests endpoint](/manifests-scanforms), you can either specify exactly which `label_ids` to manifest (this is called an “explicit manifest”) or set criteria for determining which labels will be manifested by carrier ID, warehouse ID, and ship date (this is called an “implicit manifest”). The response body will include links to the manifest documents so you can download and print them.

### Schedule Pickups

You can now schedule and manage pickups with supported carriers via the [pickups endpoint](/schedule-pickups).

Inventory API Features
----------------------

With the **Inventory API add-on**, you can access the following capabilities:

* List and update SKU inventory stock levels
* Add and manage inventory warehouses
* Add and manage inventory locations

### Inventory Stock Levels

Use the `v2/inventory/` endpoint to [list and update inventory stock levels](/manage-inventory-levels) for specific SKUs. Ensure you can always fulfill your orders and identify where SKU stock resides in your warehouse ecosystem.

### Inventory Warehouses

Use the dedicated `/v2/inventory_warehouses/` endpoint to [add, list, udpate, and delete the inventory warehouses](/manage-inventory-warehouses) you use in your inventory management and shipping workflows.

### Inventory Locations

Use the dedicated `/v2/inventory_locations/` endpoint ot [add, list, update, and delete inventory locations](/manage-inventory-locations) you use within your inventory warehouses.

#### Was this helpful?

Next page[Introduction to REST](/rest)

On this page

[Using the Shipping API](#using-the-shipping-api)[Enable the Inventory API Add-On](#enable-the-inventory-api-add-on)[Shipping API Feautres](#shipping-api-feautres)[Common Terminology](#common-terminology)[Creating and Updating Shipments](#creating-and-updating-shipments)[Rate Shopping](#rate-shopping)[Batches, Multi-Package Labels, and Return Labels](#batches-multi-package-labels-and-return-labels)[Manifests](#manifests)[Schedule Pickups](#schedule-pickups)[Inventory API Features](#inventory-api-features)[Inventory Stock Levels](#inventory-stock-levels)[Inventory Warehouses](#inventory-warehouses)[Inventory Locations](#inventory-locations)

![Shipstation](./shipstation-logo.svg)

* [![Facebook](./facebook.svg)](https://www.facebook.com/ShipStation)
* [![Linkedin](./linkedin.svg)](https://www.linkedin.com/company/shipstation)
* [![Instagram](./instagram.svg)](https://www.instagram.com/shipstation)

![Auctane](./auctane-logo.svg)

ShipStation is powered by Auctane, a global delivery experience company. © 2026 Auctane, Inc. All rights reserved

* [Terms](/getting-started)
* [Privacy](/getting-started)
* [Disclosures](/getting-started)
* [Cookie Settings](/getting-started)