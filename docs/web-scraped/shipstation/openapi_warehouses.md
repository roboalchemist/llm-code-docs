# Source: https://docs.shipstation.com/openapi/warehouses

Warehouses




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

[+ Rates](/openapi/rates)

[+ Shipments](/openapi/shipments)

[+ Tags](/openapi/tags)

[+ Tracking](/openapi/tracking)

[+ Warehouses](/openapi/warehouses)

[- List warehouses

  get](/openapi/warehouses/list_warehouses)

[- Get warehouse by id

  get](/openapi/warehouses/get_warehouse_by_id)

[+ Users](/openapi/users)

[+ Webhooks](/openapi/webhooks)

* Release Notes

[Full API Reference](/openapi)

/

[Warehouses](/openapi/warehouses)

ShipStation API v2 (2.0.0)
==========================

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

Batches
-------

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

+ Show

Carriers
--------

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

+ Show

Downloads
---------

Download your label files in PDF, PNG, and ZPL.

Operations

get

/v2/downloads/{dir}/{subdir}/{filename}

+ Show

Fulfillments
------------

Manage fulfillments which represent completed shipments. Create fulfillments to mark orders as shipped with tracking information and notify customers and marketplaces.

Operations

get

/v2/fulfillments

post

/v2/fulfillments

+ Show

Inventory
---------

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

+ Show

Labels
------

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

+ Show

Manifests
---------

A manifest is a document that provides a list of the day's shipments. It typically contains a barcode that allows the pickup driver to scan a single document to register all shipments, rather than scanning each shipment individually.

Operations

get

/v2/manifests

post

/v2/manifests

get

/v2/manifests/{manifest\_id}

+ Show

Package Pickups
---------------

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

+ Show

Package Types
-------------

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

+ Show

Products
--------

Manage products in your ShipStation account. Products represent the items you sell and ship to customers.

Operations

get

/v2/products

+ Show

Rates
-----

Quickly compare rates using the Rates endpoint. You can see and compare rates for the carriers connected to your account (as long as they support sending rates).

Operations

post

/v2/rates

post

/v2/rates/estimate

get

/v2/rates/{rate\_id}

+ Show

Shipments
---------

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

+ Show

Tags
----

Tags are text-based identifiers you can add to shipments to help in your shipment management workflows.

Operations

get

/v2/tags

post

/v2/tags/{tag\_name}

+ Show

Tracking
--------

Use the tracking endpoint to stop receiving tracking updates (more dedicated tracking endpoint methods coming soon).

Operations

post

/v2/tracking/stop

+ Show

Warehouses
----------

Get warehouse details like warehouse ID and related addresses using the warehouses endpoint.

Operations

get

/v2/warehouses

get

/v2/warehouses/{warehouse\_id}

List warehouses
---------------

#### Request

Retrieve a list of warehouses associated with this account.

Security:
api\_keys

get

/v2/warehouses

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/warehouses
* Production https://api.shipstation.com/v2/warehouses

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

```
curl -i -X GET \
  https://docs.shipstation.com/_mock/openapi/v2/warehouses \
  -H 'api-key: YOUR_API_KEY_HERE'
```

Try it

#### Responses

1. 200
2. 400
3. 404
4. 500

Expand all

The request was a success.

Bodyapplication/json

warehouses*Array of objects**(warehouse)*read-onlyrequired

The array of warehouses returned by the API call

-

warehouses[].​warehouse\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

warehouses[].​is\_default*boolean or null*

Designates which single warehouse is the default on the account

Default false

Example: true

warehouses[].​name*string**non-empty*

Name of the warehouse

Example: "Zero Cool HQ"

warehouses[].​created\_at*string**(date-time)**non-empty*read-only

Timestamp that indicates when the warehouse was created

Example: "2019-06-25T18:12:35.583Z"

warehouses[].​origin\_address*object**(address)*

A complete or partial mailing address.

+Show 12 properties

warehouses[].​return\_address*object**(address)*

A complete or partial mailing address.

+Show 12 properties

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "warehouses": [
    { … }
  ]
}
```

#### Was this helpful?

Get warehouse by id
-------------------

#### Request

Retrieve warehouse data based on the warehouse ID

Security:
api\_keys

Path

warehouse\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Warehouse ID

Example: se-28529731

get

/v2/warehouses/{warehouse\_id}

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/warehouses/{warehouse\_id}
* Production https://api.shipstation.com/v2/warehouses/{warehouse\_id}

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

```
curl -i -X GET \
  'https://docs.shipstation.com/_mock/openapi/v2/warehouses/{warehouse_id}' \
  -H 'api-key: YOUR_API_KEY_HERE'
```

Try it

#### Responses

1. 200
2. 400
3. 404
4. 500

Expand all

The request was a success.

Bodyapplication/json

warehouse\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

is\_default*boolean or null*

Designates which single warehouse is the default on the account

Default false

Example: true

name*string**non-empty*required

Name of the warehouse

Example: "Zero Cool HQ"

created\_at*string**(date-time)**non-empty*read-onlyrequired

Timestamp that indicates when the warehouse was created

Example: "2019-06-25T18:12:35.583Z"

origin\_address*object**(address)*required

A complete or partial mailing address.

-

origin\_address.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

origin\_address.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

origin\_address.​email*string or null*

Email for the address owner.

Example: "example@example.com"

origin\_address.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

origin\_address.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

origin\_address.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

origin\_address.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

origin\_address.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

origin\_address.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

origin\_address.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

origin\_address.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

origin\_address.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

return\_address*object**(address)*required

A complete or partial mailing address.

-

return\_address.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

return\_address.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

return\_address.​email*string or null*

Email for the address owner.

Example: "example@example.com"

return\_address.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

return\_address.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

return\_address.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

return\_address.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

return\_address.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

return\_address.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

return\_address.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

return\_address.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

return\_address.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "warehouse_id": "se-28529731",
  "is_default": true,
  "name": "Zero Cool HQ",
  "created_at": "2019-06-25T18:12:35.583Z",
  "origin_address": {
    "name": "John Doe",
    "phone": "+1 204-253-9411 ext. 123",
    "email": "example@example.com",
    "company_name": "The Home Depot",
    "address_line1": "1999 Bishop Grandin Blvd.",
    "address_line2": "Unit 408",
    "address_line3": "Building #7",
    "city_locality": "Winnipeg",
    "state_province": "Manitoba",
    "postal_code": "78756-3717",
    "country_code": "CA",
    "address_residential_indicator": "yes"
  },
  "return_address": {
    "name": "John Doe",
    "phone": "+1 204-253-9411 ext. 123",
    "email": "example@example.com",
    "company_name": "The Home Depot",
    "address_line1": "1999 Bishop Grandin Blvd.",
    "address_line2": "Unit 408",
    "address_line3": "Building #7",
    "city_locality": "Winnipeg",
    "state_province": "Manitoba",
    "postal_code": "78756-3717",
    "country_code": "CA",
    "address_residential_indicator": "yes"
  }
}
```

#### Was this helpful?

Users
-----

Manage and retrieve user information for the ShipStation account. This endpoint allows you to list users with various filtering options.

Operations

get

/v2/users

+ Show

Webhooks
--------

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

+ Show

![Shipstation](./shipstation-logo.svg)

* [![Facebook](./facebook.svg)](https://www.facebook.com/ShipStation)
* [![Linkedin](./linkedin.svg)](https://www.linkedin.com/company/shipstation)
* [![Instagram](./instagram.svg)](https://www.instagram.com/shipstation)

![Auctane](./auctane-logo.svg)

ShipStation is powered by Auctane, a global delivery experience company. © 2026 Auctane, Inc. All rights reserved

* [Terms](/openapi/warehouses)
* [Privacy](/openapi/warehouses)
* [Disclosures](/openapi/warehouses)
* [Cookie Settings](/openapi/warehouses)