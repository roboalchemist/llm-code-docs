# Source: https://docs.shipstation.com/openapi/manifests

Manifests




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

[- List manifests

  get](/openapi/manifests/list_manifests)

[- Create manifest

  post](/openapi/manifests/create_manifest)

[- Get manifest by id

  get](/openapi/manifests/get_manifest_by_id)

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

[Manifests](/openapi/manifests)

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

List manifests
--------------

#### Request

Similar to querying shipments, we allow you to query manifests since there will likely be a large number over a long period of time.

Security:
api\_keys

Query

warehouse\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

Warehouse ID

Example: warehouse\_id=se-28529731

ship\_date\_start*string**(date-time)*

ship date start range

Example: ship\_date\_start=2018-09-23T15:00:00.000Z

ship\_date\_end*string**(date-time)*

ship date end range

Example: ship\_date\_end=2018-09-23T15:00:00.000Z

created\_at\_start*string**(date-time)*

Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)

Example: created\_at\_start=2019-03-12T19:24:13.657Z

created\_at\_end*string**(date-time)*

Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)

Example: created\_at\_end=2019-03-12T19:24:13.657Z

carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

Carrier ID

Example: carrier\_id=se-28529731

page*integer**(int32)**>= 1*

Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned.

Default 1

Example: page=2

page\_size*integer**(int32)**>= 1*

The number of results to return per response.

Default 25

Example: page\_size=50

label\_ids*Array of strings**(se\_id)*

Array of label ids

Example: label\_ids=se-28529731

get

/v2/manifests

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/manifests
* Production https://api.shipstation.com/v2/manifests

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
  'https://docs.shipstation.com/_mock/openapi/v2/manifests?carrier_id=se-28529731&created_at_end=2019-08-24T14%3A15%3A22Z&created_at_start=2019-08-24T14%3A15%3A22Z&label_ids=se-28529731&page=1&page_size=25&ship_date_end=2019-08-24T14%3A15%3A22Z&ship_date_start=2019-08-24T14%3A15%3A22Z&warehouse_id=se-28529731' \
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

manifests*Array of objects**(manifest)*read-onlyrequired

The list of available manifests

Default []

-

manifests[].​manifest\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

manifests[].​form\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

manifests[].​created\_at*string**(date-time)**non-empty*read-only

The date-time that the manifest was created

Example: "2019-07-12T13:37:39.05Z"

manifests[].​ship\_date*string**(date-time)**non-empty*read-only

The date-time that the manifests shipments will be picked up

Example: "2019-07-12T13:37:39.05Z"

manifests[].​shipments*integer**(int32)**>= 1*read-only

The number of shipments that are included in this manifest

Example: 100

manifests[].​label\_ids*Array of strings**(se\_id)*read-only

An array of the label ids used in this manifest.

Example: ["se-28529731"]

manifests[].​warehouse\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

manifests[].​submission\_id*string**non-empty*read-only

A string that uniquely identifies the submission

Example: "9475711899564878915476"

manifests[].​carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

manifests[].​manifest\_download*object**(manifest\_download)*read-only

Object containing the href link to download the manifest file

+Show property

total*integer**(int64)**>= 0*read-onlyrequired

The total number of manifests returned

Example: 3

page*integer**(int32)**>= 1*read-onlyrequired

Current page of the list manifests results

Example: 3

pages*integer**(int32)**>= 1*read-onlyrequired

Total number of pages for list manifests results

Example: 4

links*object**(pagination\_link)*read-onlyrequired

Helpful links to other pages of results

-

links.​first*object**(link)*required

A link to a related resource, or an empty object if there is no resource to link to

-

links.​first.​href*string**(url)**(url)**non-empty*required

A URL

Example: "http://api.shipstation.com/v2/labels/se-28529731"

links.​first.​type*string**non-empty*

The type of resource, or the type of relationship to the parent resource

Example: "child"

links.​last*object**(link)*required

A link to a related resource, or an empty object if there is no resource to link to

-

links.​last.​href*string**(url)**(url)**non-empty*required

A URL

Example: "http://api.shipstation.com/v2/labels/se-28529731"

links.​last.​type*string**non-empty*

The type of resource, or the type of relationship to the parent resource

Example: "child"

links.​prev*object**(optional\_link)*required

A link to a related resource, or an empty object if there is no resource to link to

-

links.​prev.​href*string**(url)**(url)**non-empty*

A URL

Example: "http://api.shipstation.com/v2/labels/se-28529731"

links.​prev.​type*string**non-empty*

The type of resource, or the type of relationship to the parent resource

Example: "child"

links.​next*object**(optional\_link)*required

A link to a related resource, or an empty object if there is no resource to link to

-

links.​next.​href*string**(url)**(url)**non-empty*

A URL

Example: "http://api.shipstation.com/v2/labels/se-28529731"

links.​next.​type*string**non-empty*

The type of resource, or the type of relationship to the parent resource

Example: "child"

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "manifests": [],
  "total": 3,
  "page": 3,
  "pages": 4,
  "links": {
    "first": { … },
    "last": { … },
    "prev": { … },
    "next": { … }
  }
}
```

#### Was this helpful?

Create manifest
---------------

#### Request

Each ShipStation manifest is created for a specific warehouse, so you'll need to provide the warehouse\_id rather than the ship\_from address. You can create a warehouse for each location that you want to create manifests for.

Security:
api\_keys

Bodyapplication/jsonrequired

One of:

create\_manifest\_by\_object\_request\_bodycreate\_manifest\_label\_ids\_request\_body

A create manifest request body

carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

excluded\_label\_ids*Array of strings**(se\_id)*

The list of label ids to exclude from the manifest

Example: ["se-28529731"]

label\_ids*Array of strings**(se\_id)*

The list of label ids to include for the manifest

Example: ["se-28529731"]

warehouse\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

ship\_date*string**(date-time)**non-empty*required

The ship date that the shipment will be sent out on

Example: "2018-09-23T15:00:00.000Z"

post

/v2/manifests

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/manifests
* Production https://api.shipstation.com/v2/manifests

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

create\_manifest\_by\_object\_request\_bodycreate\_manifest\_label\_ids\_request\_bodycreate\_manifest\_by\_object\_request\_body

```
curl -i -X POST \
  https://docs.shipstation.com/_mock/openapi/v2/manifests \
  -H 'Content-Type: application/json' \
  -H 'api-key: YOUR_API_KEY_HERE' \
  -d '{
    "carrier_id": "se-1234567",
    "excluded_label_ids": [
      "se-28529731"
    ],
    "label_ids": [
      "se-28529731"
    ],
    "warehouse_id": "se-28529731",
    "ship_date": "2018-09-23T15:00:00.000Z"
  }'
```

Try it

#### Responses

1. 200
2. 400
3. 500

Expand all

The request was a success.

Bodyapplication/json

manifests*Array of objects**(manifest)*

Resulting Manifests

+Show 10 array properties

manifest\_request\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

status*string**(manifest\_request\_status)*

The possible statuses of a manifest request

Enum"in\_progress""completed"

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

errors[].​label\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

manifest\_id*string**(se\_id)**[ 1 .. 25 ] characters*Deprecated^se(-[a-z0-9]+)+$required

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

form\_id*string**(se\_id)**[ 1 .. 25 ] characters*Deprecated^se(-[a-z0-9]+)+$required

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

created\_at*string**(date-time)**non-empty*Deprecatedrequired

The date-time that the manifest was created

Example: "2019-07-12T13:37:39.05Z"

ship\_date*string**(date-time)**non-empty*Deprecatedrequired

The date-time that the manifests shipments will be picked up

Example: "2019-07-12T13:37:39.05Z"

shipments*integer**(int32)**>= 1*Deprecatedread-onlyrequired

The number of shipments that are included in this manifest

Example: 100

warehouse\_id*string**(se\_id)**[ 1 .. 25 ] characters*Deprecated^se(-[a-z0-9]+)+$required

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

submission\_id*string**non-empty*Deprecatedrequired

A string that uniquely identifies the submission

Example: "9475711899564878915476"

carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*Deprecated^se(-[a-z0-9]+)+$required

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

manifest\_download*object**(manifest\_download)*Deprecatedrequired

Object containing the href link to download the manifest file

-

manifest\_download.​href*string**(url)**(url)**non-empty*

A URL

Example: "http://api.shipstation.com/v2/labels/se-28529731"

label\_ids*Array of strings**(se\_id)*Deprecatedread-only

An array of the label ids used in this manifest.

Example: ["se-28529731"]

Response

1. 200
2. 400
3. 500

application/json

```
{
  "manifests": [
    { … }
  ],
  "manifest_request_id": "se-28529731",
  "status": "in_progress",
  "manifest_id": "se-28529731",
  "form_id": "se-28529731",
  "created_at": "2019-07-12T13:37:39.05Z",
  "ship_date": "2019-07-12T13:37:39.05Z",
  "shipments": 100,
  "warehouse_id": "se-28529731",
  "submission_id": "9475711899564878915476",
  "carrier_id": "se-1234567",
  "manifest_download": {
    "href": "http://api.shipstation.com/v2/labels/se-28529731"
  },
  "label_ids": [
    "se-28529731"
  ],
  "request_id": "aa3d8e8e-462b-4476-9618-72db7f7b7009",
  "errors": [
    { … }
  ]
}
```

#### Was this helpful?

Get manifest by id
------------------

#### Request

Get Manifest By Id

Security:
api\_keys

Path

manifest\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

The Manifest Id

Example: se-28529731

get

/v2/manifests/{manifest\_id}

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/manifests/{manifest\_id}
* Production https://api.shipstation.com/v2/manifests/{manifest\_id}

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
  'https://docs.shipstation.com/_mock/openapi/v2/manifests/{manifest_id}' \
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

manifest\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

form\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

created\_at*string**(date-time)**non-empty*read-onlyrequired

The date-time that the manifest was created

Example: "2019-07-12T13:37:39.05Z"

ship\_date*string**(date-time)**non-empty*read-onlyrequired

The date-time that the manifests shipments will be picked up

Example: "2019-07-12T13:37:39.05Z"

shipments*integer**(int32)**>= 1*read-onlyrequired

The number of shipments that are included in this manifest

Example: 100

label\_ids*Array of strings**(se\_id)*read-onlyrequired

An array of the label ids used in this manifest.

Example: ["se-28529731"]

warehouse\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

submission\_id*string**non-empty*read-onlyrequired

A string that uniquely identifies the submission

Example: "9475711899564878915476"

carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

manifest\_download*object**(manifest\_download)*read-onlyrequired

Object containing the href link to download the manifest file

-

manifest\_download.​href*string**(url)**(url)**non-empty*

A URL

Example: "http://api.shipstation.com/v2/labels/se-28529731"

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "manifest_id": "se-28529731",
  "form_id": "se-28529731",
  "created_at": "2019-07-12T13:37:39.05Z",
  "ship_date": "2019-07-12T13:37:39.05Z",
  "shipments": 100,
  "label_ids": [
    "se-28529731"
  ],
  "warehouse_id": "se-28529731",
  "submission_id": "9475711899564878915476",
  "carrier_id": "se-1234567",
  "manifest_download": {
    "href": "http://api.shipstation.com/v2/labels/se-28529731"
  }
}
```

#### Was this helpful?

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

* [Terms](/openapi/manifests)
* [Privacy](/openapi/manifests)
* [Disclosures](/openapi/manifests)
* [Cookie Settings](/openapi/manifests)