# Source: https://docs.shipstation.com/openapi/products

[![ShipStation Developer](/assets/logo-ss-api.ec8fa1da9c60670d3bcab24ceeb8f32be01e624584c3106975db87878853f13c.de6e0f62.svg)](/)

[Docs](/getting-started)

[Status Page](https://status.shipstation.com/)

[Login](https://ship.shipstation.com/)

[Sign up](https://www.shipstation.com/step1/)

Search/

* Getting Started

* Guides

* Full API Reference

[+ ShipStation API](/openapi)

[+ Batches](/openapi/batches)

[+ Carriers](/openapi/carriers)

[+ Downloads](/openapi/downloads)

[+ Fulfillments](/openapi/fulfillments)

[+ Inventory](/openapi/inventory)

[+ Labels](/openapi/labels)

[+ Manifests](/openapi/manifests)

[+ Package Pickups](/openapi/package_pickups)

[+ Package Types](/openapi/package_types)

[+ Products](/openapi/products)

[- List products

  get](/openapi/products/listproducts)

[+ Rates](/openapi/rates)

[+ Shipments](/openapi/shipments)

[+ Tags](/openapi/tags)

[+ Tracking](/openapi/tracking)

[+ Warehouses](/openapi/warehouses)

[+ Users](/openapi/users)

[+ Webhooks](/openapi/webhooks)

* Release Notes

[Full API Reference](/openapi)

/

[Products](/openapi/products)

## ShipStation API v2 (2.0.0)

Download OpenAPI description

[openapi.json](/_spec/openapi.json?download)

[openapi.yaml](/_spec/openapi.yaml?download)

Overview

License [MIT](https://opensource.org/license/mit/)

Languages

Servers

Mock server

https://docs.shipstation.com/\_mock/openapi/

Production

https://api.shipstation.com/

## Batches

Process labels in bulk and receive a large number of labels and customs forms in bulk responses. Batching is ideal for workflows that need to process hundreds or thousands of labels quickly.

Operations

get

/v2/batches

post

/v2/batches

get

/v2/batches/external\_batch\_id/{external\_batch\_id}

delete

/v2/batches/{batch\_id}

get

/v2/batches/{batch\_id}

put

/v2/batches/{batch\_id}

post

/v2/batches/{batch\_id}/add

get

/v2/batches/{batch\_id}/errorsShow 2 more...

* Show

## Carriers

Retreive useful details about the carriers connected to your accounts, including carrier IDs, service IDs, advanced options, and available carrier package types.

Operations

get

/v2/carriers

get

/v2/carriers/{carrier\_id}

get

/v2/carriers/{carrier\_id}/options

get

/v2/carriers/{carrier\_id}/packages

get

/v2/carriers/{carrier\_id}/services

* Show

## Downloads

Download your label files in PDF, PNG, and ZPL.

Operations

get

/v2/downloads/{dir}/{subdir}/{filename}

* Show

## Fulfillments

Manage fulfillments which represent completed shipments. Create fulfillments to mark orders as shipped with tracking information and notify customers and marketplaces.

Operations

get

/v2/fulfillments

post

/v2/fulfillments

* Show

## Inventory

Manage inventory, adjust quantities, and handle warehouses and locations.

Operations

get

/v2/inventory

post

/v2/inventory

get

/v2/inventory\_warehouses

post

/v2/inventory\_warehouses

get

/v2/inventory\_warehouses/{inventory\_warehouse\_id}

put

/v2/inventory\_warehouses/{inventory\_warehouse\_id}

delete

/v2/inventory\_warehouses/{inventory\_warehouse\_id}

get

/v2/inventory\_locationsShow 4 more...

* Show

## Labels

Purchase and print shipping labels for any carrier active on your account. The labels endpoint also supports creating return labels, voiding labels, and getting label details like tracking.

Operations

get

/v2/labels

post

/v2/labels

post

/v2/labels/rates/{rate\_id}

post

/v2/labels/shipment/{shipment\_id}

get

/v2/labels/{label\_id}

post

/v2/labels/{label\_id}/return

get

/v2/labels/{label\_id}/track

put

/v2/labels/{label\_id}/void

* Show

## Manifests

A manifest is a document that provides a list of the day's shipments. It typically contains a barcode that allows the pickup driver to scan a single document to register all shipments, rather than scanning each shipment individually.

Operations

get

/v2/manifests

post

/v2/manifests

get

/v2/manifests/{manifest\_id}

* Show

## Package Pickups

Scheduled pickups and manage pickup requests for supported carriers.

Operations

get

/v2/pickups

post

/v2/pickups

get

/v2/pickups/{pickup\_id}

delete

/v2/pickups/{pickup\_id}

* Show

## Package Types

Create custom package types to use for your shipments, rather than the carriers' default package types.

Operations

get

/v2/packages

post

/v2/packages

get

/v2/packages/{package\_id}

put

/v2/packages/{package\_id}

delete

/v2/packages/{package\_id}

* Show

## Products

Manage products in your ShipStation account. Products represent the items you sell and ship to customers.

Operations

get

/v2/products

## List products

### Request

Security:
api\_keys

Query

sku*string*

Filter products by SKU

Example: sku=TEST-SKU-001

name*string*

Filter products by name

Example: name=Test Product

active*boolean*

Filter products by active status

Example: active=true

page\_size*integer**[ 1 .. 100 ]*

The number of results to return per page

Default 100

Example: page\_size=25

page*integer**>= 1*

The page number to return

Default 1

Example: page=5

get

/v2/products

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/products
* Production https://api.shipstation.com/v2/products

curl

* curl
* JavaScript
* Node.js
* Python
* Java
* C#
* PHP
* Go
* Ruby
* R
* Payload

```text
curl -i -X GET \
  'https://docs.shipstation.com/_mock/openapi/v2/products?active=true&name=string&page=1&page_size=100&sku=string' \
  -H 'api-key: YOUR_API_KEY_HERE'
```text

Try it

### Responses

1. 200
2. 400
3. 404
4. 500

Expand all

List of products

Bodyapplication/json

products*Array of objects*

+Show 38 array properties

total*integer*

Total number of products

Example: 510

page*integer*

Current page number

Example: 5

pages*integer*

Total number of pages

Example: 6

links*object*

+Show 4 properties

Response

1. 200
2. 400
3. 404
4. 500

application/json

```text
{
  "products": [
    { … }
  ],
  "total": 510,
  "page": 5,
  "pages": 6,
  "links": {
    "first": { … },
    "last": { … },
    "prev": { … },
    "next": { … }
  }
}
```text

### Was this helpful?

## Rates

Quickly compare rates using the Rates endpoint. You can see and compare rates for the carriers connected to your account (as long as they support sending rates).

Operations

post

/v2/rates

post

/v2/rates/estimate

get

/v2/rates/{rate\_id}

* Show

## Shipments

Shipments are at the core of most ShipStation capabilities. Shipment objects are required for cretaing labels and manifests, as well as getting rates.

Operations

get

/v2/shipments

post

/v2/shipments

get

/v2/shipments/external\_shipment\_id/{external\_shipment\_id}

get

/v2/shipments/{shipment\_id}

put

/v2/shipments/{shipment\_id}/cancel

get

/v2/shipments/{shipment\_id}/rates

post

/v2/shipments/{shipment\_id}/tags/{tag\_name}

delete

/v2/shipments/{shipment\_id}/tags/{tag\_name}

* Show

## Tags

Tags are text-based identifiers you can add to shipments to help in your shipment management workflows.

Operations

get

/v2/tags

post

/v2/tags/{tag\_name}

* Show

## Tracking

Use the tracking endpoint to stop receiving tracking updates (more dedicated tracking endpoint methods coming soon).

Operations

post

/v2/tracking/stop

* Show

## Warehouses

Get warehouse details like warehouse ID and related addresses using the warehouses endpoint.

Operations

get

/v2/warehouses

get

/v2/warehouses/{warehouse\_id}

* Show

## Users

Manage and retrieve user information for the ShipStation account. This endpoint allows you to list users with various filtering options.

Operations

get

/v2/users

* Show

## Webhooks

Webhooks are a powerful feature that can save you from sending repeated polling requests to check on the state of something. With webhooks, ShipStation will automatically contact your servers when the stage changes. This can include parcel tracking events, notification when a batch operation completes, and more.

Operations

get

/v2/environment/webhooks

post

/v2/environment/webhooks

get

/v2/environment/webhooks/{webhook\_id}

put

/v2/environment/webhooks/{webhook\_id}

delete

/v2/environment/webhooks/{webhook\_id}

* Show

![Shipstation](./shipstation-logo.svg)

* [![Facebook](./facebook.svg)](https://www.facebook.com/ShipStation)
* [![Linkedin](./linkedin.svg)](https://www.linkedin.com/company/shipstation)
* [![Instagram](./instagram.svg)](https://www.instagram.com/shipstation)

![Auctane](./auctane-logo.svg)

ShipStation is powered by Auctane, a global delivery experience company. © 2026 Auctane, Inc. All rights reserved

* [Terms](/openapi/products)
* [Privacy](/openapi/products)
* [Disclosures](/openapi/products)
* [Cookie Settings](/openapi/products)
