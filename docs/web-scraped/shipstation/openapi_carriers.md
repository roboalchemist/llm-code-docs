# Source: https://docs.shipstation.com/openapi/carriers

Carriers




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

[- List carriers

  get](/openapi/carriers/list_carriers)

[- Get carrier by id

  get](/openapi/carriers/get_carrier_by_id)

[- Get carrier options

  get](/openapi/carriers/get_carrier_options)

[- List carrier package types

  get](/openapi/carriers/list_carrier_package_types)

[- List carrier services

  get](/openapi/carriers/list_carrier_services)

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

[+ Users](/openapi/users)

[+ Webhooks](/openapi/webhooks)

* Release Notes

[Full API Reference](/openapi)

/

[Carriers](/openapi/carriers)

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

List carriers
-------------

#### Request

List all carriers that have been added to this account.

Security:
api\_keys

get

/v2/carriers

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/carriers
* Production https://api.shipstation.com/v2/carriers

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
  https://docs.shipstation.com/_mock/openapi/v2/carriers \
  -H 'api-key: YOUR_API_KEY_HERE'
```

Try it

#### Responses

1. 200
2. 207
3. 400
4. 404
5. 500

Expand all

The request was a success.

Bodyapplication/json

carriers*Array of objects**(carrier)*read-onlyrequired

The carrier response body

-

carriers[].​carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

carriers[].​carrier\_code*string**(carrier\_code)*^[a-z0-9]+(\_[a-z0-9]+)\*$read-only

A [shipping carrier] , such as `fedex`, `dhl_express`, `stamps_com`, etc.

Example: "dhl\_express"

carriers[].​account\_number*string**non-empty*read-only

The account number that the carrier is connected to.

Example: "account\_570827"

carriers[].​requires\_funded\_amount*boolean*read-only

Indicates whether the carrier requires funding to use its services

Example: true

carriers[].​balance*number**>= 0*read-only

Current available balance

Example: 3799.52

carriers[].​nickname*string**non-empty*read-only

Nickname given to the account when initially setting up the carrier.

Example: "ShipStation Account - Stamps.com"

carriers[].​friendly\_name*string**non-empty*read-only

Screen readable name

Example: "Stamps.com"

carriers[].​funding\_source\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

carriers[].​primary*boolean*read-only

Is this the primary carrier that is used by default when no carrier is specified in label/shipment creation

Example: true

carriers[].​has\_multi\_package\_supporting\_services*boolean*read-only

Carrier supports multiple packages per shipment

Example: true

carriers[].​supports\_label\_messages*boolean*read-only

The carrier supports adding custom label messages to an order.

Example: true

carriers[].​disabled\_by\_billing\_plan*boolean*read-only

The carrier is disabled by the current ShipStation account's billing plan.

Example: true

carriers[].​services*Array of objects**(service)*read-only

A list of services that are offered by the carrier

+Show 7 array properties

carriers[].​packages*Array of objects**(package\_type)*read-only

A list of package types that are supported by the carrier

+Show 5 array properties

carriers[].​options*Array of objects**(carrier\_advanced\_option)*read-only

A list of options that are available to that carrier

+Show 3 array properties

carriers[].​send\_rates*boolean*read-only

The carrier provides rates for the shipment.

Example: true

carriers[].​supports\_user\_managed\_rates*boolean*read-only

The carrier supports user-managed rates for shipments.

Example: true

request\_id*string**(uuid)**(uuid)**= 36 characters*^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}...Show patternrequired

A UUID (a.k.a. GUID) that uniquely identifies a resource

Example: "aa3d8e8e-462b-4476-9618-72db7f7b7009"

errors*Array of objects**(error)*read-onlyrequired

The errors associated with the failed API call

-

errors[].​error\_source*string**(error\_source)*required

The source of the error, as indicated by the name this informs us if the API call failed because of the carrier, the order source, or the ShipStation API itself.

Enum"carrier""order\_source""ShipStation"

errors[].​error\_type*string**(error\_type)*required

The type of error

Enum"account\_status""business\_rules""validation""security""system""integrations"

errors[].​error\_code*string**(error\_code)*required

The error code specified for the failed API Call

Enum"auto\_fund\_not\_supported""batch\_cannot\_be\_modified""carrier\_conflict""carrier\_disconnected""carrier\_not\_connected""carrier\_not\_supported""confirmation\_not\_supported""default\_warehouse\_cannot\_be\_deleted""field\_conflict""field\_value\_required"+33 more

errors[].​message*string**non-empty*read-onlyrequired

An error message associated with the failed API call

Example: "Body of request cannot be null."

Response

1. 200
2. 207
3. 400
4. 404
5. 500

application/json

```
{
  "carriers": [
    { … }
  ],
  "request_id": "aa3d8e8e-462b-4476-9618-72db7f7b7009",
  "errors": [
    { … }
  ]
}
```

#### Was this helpful?

Get carrier by id
-----------------

#### Request

Retrive details about a specific carrier by its carrier id.

Security:
api\_keys

Path

carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Carrier ID

Example: se-28529731

get

/v2/carriers/{carrier\_id}

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/carriers/{carrier\_id}
* Production https://api.shipstation.com/v2/carriers/{carrier\_id}

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
  'https://docs.shipstation.com/_mock/openapi/v2/carriers/{carrier_id}' \
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

carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

carrier\_code*string**(carrier\_code)*^[a-z0-9]+(\_[a-z0-9]+)\*$read-only

A [shipping carrier] , such as `fedex`, `dhl_express`, `stamps_com`, etc.

Example: "dhl\_express"

account\_number*string**non-empty*read-only

The account number that the carrier is connected to.

Example: "account\_570827"

requires\_funded\_amount*boolean*read-only

Indicates whether the carrier requires funding to use its services

Example: true

balance*number**>= 0*read-only

Current available balance

Example: 3799.52

nickname*string**non-empty*read-only

Nickname given to the account when initially setting up the carrier.

Example: "ShipStation Account - Stamps.com"

friendly\_name*string**non-empty*read-only

Screen readable name

Example: "Stamps.com"

funding\_source\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

primary*boolean*read-only

Is this the primary carrier that is used by default when no carrier is specified in label/shipment creation

Example: true

has\_multi\_package\_supporting\_services*boolean*read-only

Carrier supports multiple packages per shipment

Example: true

supports\_label\_messages*boolean*read-only

The carrier supports adding custom label messages to an order.

Example: true

disabled\_by\_billing\_plan*boolean*read-only

The carrier is disabled by the current ShipStation account's billing plan.

Example: true

services*Array of objects**(service)*read-only

A list of services that are offered by the carrier

+Show 7 array properties

packages*Array of objects**(package\_type)*read-only

A list of package types that are supported by the carrier

+Show 5 array properties

options*Array of objects**(carrier\_advanced\_option)*read-only

A list of options that are available to that carrier

+Show 3 array properties

send\_rates*boolean*read-only

The carrier provides rates for the shipment.

Example: true

supports\_user\_managed\_rates*boolean*read-only

The carrier supports user-managed rates for shipments.

Example: true

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "carrier_id": "se-8412",
  "carrier_code": "dhl_express",
  "account_number": "account_570827",
  "requires_funded_amount": true,
  "balance": 3799.52,
  "nickname": "ShipStation Account - Stamps.com",
  "friendly_name": "Stamps.com",
  "funding_source_id": "se-28529731",
  "primary": true,
  "has_multi_package_supporting_services": true,
  "supports_label_messages": true,
  "disabled_by_billing_plan": true,
  "services": [
    { … }
  ],
  "packages": [
    { … }
  ],
  "options": [
    { … }
  ],
  "send_rates": true,
  "supports_user_managed_rates": true
}
```

#### Was this helpful?

Get carrier options
-------------------

#### Request

Get a list of the options available for a specific carriers.

Security:
api\_keys

Path

carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Carrier ID

Example: se-28529731

get

/v2/carriers/{carrier\_id}/options

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/carriers/{carrier\_id}/options
* Production https://api.shipstation.com/v2/carriers/{carrier\_id}/options

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
  'https://docs.shipstation.com/_mock/openapi/v2/carriers/{carrier_id}/options' \
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

options*Array of objects**(carrier\_advanced\_option)*read-only

AN array of carrier options

+Show 3 array properties

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "options": [
    { … }
  ]
}
```

#### Was this helpful?

List carrier package types
--------------------------

#### Request

List the package types associated with a specific carrier.

Security:
api\_keys

Path

carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Carrier ID

Example: se-28529731

get

/v2/carriers/{carrier\_id}/packages

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/carriers/{carrier\_id}/packages
* Production https://api.shipstation.com/v2/carriers/{carrier\_id}/packages

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
  'https://docs.shipstation.com/_mock/openapi/v2/carriers/{carrier_id}/packages' \
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

packages*Array of objects**(package\_type)*read-only

An array of custom package types

+Show 5 array properties

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "packages": [
    { … }
  ]
}
```

#### Was this helpful?

List carrier services
---------------------

#### Request

List the services associated with a specific carrier id.

Security:
api\_keys

Path

carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Carrier ID

Example: se-28529731

get

/v2/carriers/{carrier\_id}/services

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/carriers/{carrier\_id}/services
* Production https://api.shipstation.com/v2/carriers/{carrier\_id}/services

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
  'https://docs.shipstation.com/_mock/openapi/v2/carriers/{carrier_id}/services' \
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

services*Array of objects**(service)*read-only

An array of services associated with the carrier

+Show 7 array properties

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "services": [
    { … }
  ]
}
```

#### Was this helpful?

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

+ Show

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

* [Terms](/openapi/carriers)
* [Privacy](/openapi/carriers)
* [Disclosures](/openapi/carriers)
* [Cookie Settings](/openapi/carriers)