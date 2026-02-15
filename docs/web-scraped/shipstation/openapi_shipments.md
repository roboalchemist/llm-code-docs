# Source: https://docs.shipstation.com/openapi/shipments

Shipments




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

[- List shipments

  get](/openapi/shipments/list_shipments)

[- Create shipments

  post](/openapi/shipments/create_shipments)

[- Get shipment by external id

  get](/openapi/shipments/get_shipment_by_external_id)

[- Get shipment by id

  get](/openapi/shipments/get_shipment_by_id)

[- Cancel a shipment

  put](/openapi/shipments/cancel_shipments)

[- Get shipment rates

  get](/openapi/shipments/list_shipment_rates)

[- Add tag to shipment

  post](/openapi/shipments/tag_shipment)

[- Remove tag from shipment

  delete](/openapi/shipments/untag_shipment)

[+ Tags](/openapi/tags)

[+ Tracking](/openapi/tracking)

[+ Warehouses](/openapi/warehouses)

[+ Users](/openapi/users)

[+ Webhooks](/openapi/webhooks)

* Release Notes

[Full API Reference](/openapi)

/

[Shipments](/openapi/shipments)

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

List shipments
--------------

#### Request

Get list of Shipments

Security:
api\_keys

Query

shipment\_status*string**(shipment\_status)*

The possible shipment status values

Enum"pending""processing""label\_purchased""cancelled"

batch\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

Batch ID

Example: batch\_id=se-28529731

pickup\_id*string**(pickup\_resource\_id)**>= 4 characters*required

Pickup Resource ID

Example: pickup\_id=pik\_3YcKU5zdtJuCqoeNwyqqbW

created\_at\_start*string**(date-time)*

Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)

Example: created\_at\_start=2019-03-12T19:24:13.657Z

created\_at\_end*string**(date-time)*

Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)

Example: created\_at\_end=2019-03-12T19:24:13.657Z

modified\_at\_start*string**(date-time)*

Used to create a filter for when a resource was modified (ex. A shipment that was modified after a certain time)

Example: modified\_at\_start=2025-03-12T19:24:13.657Z

modified\_at\_end*string**(date-time)*

Used to create a filter for when a resource was modified (ex. A shipment that was modified before a certain time)

Example: modified\_at\_end=2025-03-12T19:24:13.657Z

page*integer**(int32)**>= 1*

Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned.

Default 1

Example: page=2

page\_size*integer**(int32)**>= 1*

The number of results to return per response.

Default 25

Example: page\_size=50

sales\_order\_id*string*

Sales Order ID

sort\_dir*string**(sort\_dir)*

Controls the sort order of the query.

Default "desc"

Enum"asc""desc"

shipment\_number*string*

The user or order source defined shipment number

ship\_to\_name*string*

The name associated with the ship\_to

item\_keyword*string*

Returns shipments that contain items that match the specified keyword. Fields searched are Sku, Description, and Options.

Example: item\_keyword=coat

payment\_date\_start*string**(date-time)*

Used to create a filter for resources based on the payment\_date parameter after a certain time.

Example: payment\_date\_start=2025-03-12T19:24:13.657Z

payment\_date\_end*string**(date-time)*

Used to create a filter for resources based on the payment\_date parameter before a certain time.

Example: payment\_date\_end=2025-03-12T19:24:13.657Z

store\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

Store ID

Example: store\_id=se-28529731

external\_shipment\_id*string*

Example: external\_shipment\_id=0bcb569d-1727-4ff9-ab49-b2fec0cee5ae

sort\_by*string**(shipments\_sort\_by)*

The possible shipments sort by values

Enum"modified\_at""created\_at"

Example: sort\_by=modified\_at

get

/v2/shipments

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/shipments
* Production https://api.shipstation.com/v2/shipments

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
  'https://docs.shipstation.com/_mock/openapi/v2/shipments?batch_id=se-28529731&created_at_end=2019-08-24T14%3A15%3A22Z&created_at_start=2019-08-24T14%3A15%3A22Z&external_shipment_id=string&item_keyword=string&modified_at_end=2019-08-24T14%3A15%3A22Z&modified_at_start=2019-08-24T14%3A15%3A22Z&page=1&page_size=25&payment_date_end=2019-08-24T14%3A15%3A22Z&payment_date_start=2019-08-24T14%3A15%3A22Z&pickup_id=pik_3YcKU5zdtJuCqoeNwyqqbW&sales_order_id=string&ship_to_name=string&shipment_number=string&shipment_status=pending&sort_by=modified_at&sort_dir=desc&store_id=se-28529731' \
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

shipments*Array of objects**(shipment)*read-onlyrequired

The list of shipments returned by the api call

-

shipments[].​shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​carrier\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​service\_code*string or null**(service\_code)*^[a-z0-9]+(\_[a-z0-9-]+)\* ?$

A [carrier service], such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, etc.

Example: "usps\_first\_class\_mail"

shipments[].​requested\_shipment\_service*string or null*

The requested shipment service

Example: "usps\_priority\_mail"

shipments[].​shipping\_rule\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​external\_order\_id*string or null*

ID that the Order Source assigned

Example: "1232434"

shipments[].​hold\_until\_date*string or null**(date-time)*

Date to hold the shipment until

Example: "2025-01-15T00:00:00.000Z"

shipments[].​ship\_by\_date*string or null**(date-time)*

Date by which the shipment should be shipped

Example: "2025-01-15T00:00:00.000Z"

shipments[].​retail\_rate*object or null**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​store\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​items*Array of objects**(shipment\_item)*

Describe the packages included in this shipment as related to potential metadata that was imported from external order sources

Default []

+Show 22 array properties

shipments[].​notes\_from\_buyer*string or null*

Notes from the buyer

Example: "Please handle with care"

shipments[].​notes\_for\_gift*string or null*

Gift notes

Example: "Happy Birthday!"

shipments[].​is\_gift*boolean*

Indicates if the shipment is a gift

Default false

Example: true

shipments[].​assigned\_user*string or null*

User assigned to the shipment

Example: "user@example.com"

shipments[].​amount\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​shipping\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​tax\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​zone*integer or null**(int32)**>= 0*

Shipping zone

Example: 1

shipments[].​display\_scheme*string or null*

Display scheme for the shipment

Example: "label"

shipments[].​tax\_identifiers*Array of objects or null**(tax\_identifier)*

+Show 4 array properties

shipments[].​external\_shipment\_id*string or null**<= 50 characters*

A unique user-defined key to identify a shipment. This can be used to retrieve the shipment.

> **Warning:** The `external_shipment_id` is limited to 50 characters. Any additional characters will be truncated.

Example: "1234556"

shipments[].​shipment\_number*string or null**<= 50 characters*

A non-unique user-defined number used to identify a shipment. If undefined, this will match the external\_shipment\_id of the shipment.

> **Warning:** The `shipment_number` is limited to 50 characters. Any additional characters will be truncated.

Example: "10001"

shipments[].​ship\_date*string or null**(date-time)**(date)*^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?...Show pattern

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date, but not a specific time. The value *may* contain a time component, but it will be set to `00:00:00` UTC by ShipStation .

Example: "2018-09-23"

shipments[].​created\_at*string**(date-time)**(date\_time)*^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(...Show patternread-onlyrequired

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.

Example: "2018-09-23T15:00:00.000Z"

shipments[].​modified\_at*string**(date-time)**(date\_time)*^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(...Show patternread-onlyrequired

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.

Example: "2018-09-23T15:00:00.000Z"

shipments[].​shipment\_status*string**(shipment\_status)*read-onlyrequired

The possible shipment status values

Default "pending"

Enum"pending""processing""label\_purchased""cancelled"

shipments[].​ship\_to*object**(shipping\_address\_to)*required

A complete or partial mailing address.

-

shipments[].​ship\_to.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

shipments[].​ship\_to.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

shipments[].​ship\_to.​email*string or null*

Email for the address owner.

Example: "example@example.com"

shipments[].​ship\_to.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

shipments[].​ship\_to.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

shipments[].​ship\_to.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

shipments[].​ship\_to.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

shipments[].​ship\_to.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

shipments[].​ship\_to.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

shipments[].​ship\_to.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

shipments[].​ship\_to.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

shipments[].​ship\_to.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

shipments[].​ship\_to.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instruction"

shipments[].​ship\_to.​geolocation*Array of objects*

+Show 2 array properties

shipments[].​ship\_from*object**(shipping\_address)*required

A complete or partial mailing address.

-

shipments[].​ship\_from.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

shipments[].​ship\_from.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

shipments[].​ship\_from.​email*string or null*

Email for the address owner.

Example: "example@example.com"

shipments[].​ship\_from.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

shipments[].​ship\_from.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

shipments[].​ship\_from.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

shipments[].​ship\_from.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

shipments[].​ship\_from.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

shipments[].​ship\_from.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

shipments[].​ship\_from.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

shipments[].​ship\_from.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

shipments[].​ship\_from.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

shipments[].​ship\_from.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instructions"

shipments[].​warehouse\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Default null

Example: "se-28529731"

shipments[].​return\_to*object**(shipping\_address)*required

A complete or partial mailing address.

-

shipments[].​return\_to.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

shipments[].​return\_to.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

shipments[].​return\_to.​email*string or null*

Email for the address owner.

Example: "example@example.com"

shipments[].​return\_to.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

shipments[].​return\_to.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

shipments[].​return\_to.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

shipments[].​return\_to.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

shipments[].​return\_to.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

shipments[].​return\_to.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

shipments[].​return\_to.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

shipments[].​return\_to.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

shipments[].​return\_to.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

shipments[].​return\_to.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instructions"

shipments[].​is\_return*boolean or null*

An optional indicator if the shipment is intended to be a return. Defaults to false if not provided.

Default false

Example: true

shipments[].​confirmation*string**(delivery\_confirmation)*required

The possible delivery confirmation values

Default "none"

Enum"none""delivery""signature""adult\_signature""direct\_signature""delivery\_mailed""verbal\_confirmation"

shipments[].​customs*object or null**(international\_shipment\_options)*

Options for international shipments, such as customs declarations.

Default null

+Show 8 properties

shipments[].​advanced\_options*object**(advanced\_shipment\_options)*required

Advanced shipment options

-

shipments[].​advanced\_options.​bill\_to\_account*string or null*

This field is used to [bill shipping costs to a third party]. This field must be used in conjunction with the `bill_to_country_code`, `bill_to_party`, and `bill_to_postal_code` fields.

Default null

Example: "123456789"

shipments[].​advanced\_options.​bill\_to\_country\_code*string or null**(country\_code)**= 2 characters*

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Default null

Example: "CA"

shipments[].​advanced\_options.​bill\_to\_party*string or null**(bill\_to\_party)*

The possible bill to party values

Default null

Enum"recipient""third\_party"

Example: "third\_party"

shipments[].​advanced\_options.​bill\_to\_postal\_code*string or null*

The postal code of the third-party that is responsible for shipping costs.

Default null

Example: "28005"

shipments[].​advanced\_options.​contains\_alcohol*boolean*

Indicates that the shipment contains alcohol.

Default false

Example: true

shipments[].​advanced\_options.​delivered\_duty\_paid*boolean*

Indicates that the shipper is paying the international delivery duties for this shipment. This option is supported by UPS, FedEx, and DHL Express.

Default false

Example: true

shipments[].​advanced\_options.​dry\_ice*boolean*

Indicates if the shipment contain dry ice

Default false

Example: true

shipments[].​advanced\_options.​dry\_ice\_weight*object or null**(weight)*

The weight of a package

+Show 2 properties

shipments[].​advanced\_options.​non\_machinable*boolean*

Indicates that the package cannot be processed automatically because it is too large or irregularly shaped. This is primarily for USPS shipments. See [Section 1.2 of the USPS parcel standards](https://pe.usps.com/text/dmm300/101.htm#ep1047495) for details.

Default false

Example: true

shipments[].​advanced\_options.​saturday\_delivery*boolean*

Enables Saturday delivery, if supported by the carrier.

Default false

Example: true

shipments[].​advanced\_options.​fedex\_freight*object*

Provide details for the Fedex freight service

+Show 2 properties

shipments[].​advanced\_options.​use\_ups\_ground\_freight\_pricing*boolean or null*

Whether to use [UPS Ground Freight pricing] If enabled, then a `freight_class` must also be specified.

Default null

Example: true

shipments[].​advanced\_options.​freight\_class*string or null*

The National Motor Freight Traffic Association [freight class](http://www.nmfta.org/pages/nmfc?AspxAutoDetectCookieSupport=1), such as "77.5", "110", or "250".

Default null

Example: "77.5"

shipments[].​advanced\_options.​custom\_field1*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 1"

shipments[].​advanced\_options.​custom\_field2*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 2"

shipments[].​advanced\_options.​custom\_field3*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 3"

shipments[].​advanced\_options.​origin\_type*string or null**(origin\_type)*

Indicates if the package will be picked up or dropped off by the carrier

Default null

Enum"pickup""drop\_off"

shipments[].​advanced\_options.​additional\_handling*boolean or null*

Indicate to the carrier that this shipment requires additional handling.

Default null

Example: true

shipments[].​advanced\_options.​shipper\_release*boolean or null*

Default null

Example: true

shipments[].​advanced\_options.​collect\_on\_delivery*object**(collect\_on\_delivery)*

Defer payment until package is delivered, instead of when it is ordered.

+Show 2 properties

shipments[].​advanced\_options.​third\_party\_consignee*boolean*

Third Party Consignee option is a value-added service that allows the shipper to supply goods without commercial invoices being attached

Default false

Example: true

shipments[].​advanced\_options.​dangerous\_goods*boolean*

Indicates if the Dangerous goods are present in the shipment

Default false

Example: true

shipments[].​advanced\_options.​dangerous\_goods\_contact*object*

Contact information for Dangerous goods

+Show 2 properties

shipments[].​advanced\_options.​windsor\_framework\_details*object*

The Windsor framework is a new regulation in the UK that simplifies customs procedures for goods moved from the UK mainland to Northern Ireland.

+Show 2 properties

shipments[].​advanced\_options.​ancillary\_endorsements\_option*string or null*

Ancillary endorsements option for the shipment

Example: "forward"

shipments[].​advanced\_options.​return\_pickup\_attempts*integer or null*

Number of return pickup attempts

Example: 3

shipments[].​advanced\_options.​own\_document\_upload*boolean*

Indicates if own document upload is enabled

Default false

Example: false

shipments[].​advanced\_options.​limited\_quantity*boolean*

Indicates if the shipment contains limited quantities

Default false

Example: false

shipments[].​advanced\_options.​event\_notification*boolean*

Indicates if event notifications are enabled

Default false

Example: false

shipments[].​insurance\_provider*string**(insurance\_provider)*required

The possible insurance provider values

Default "none"

Enum"none""shipsurance""carrier""third\_party"

shipments[].​tags*Array of objects**(tag)**>= 0 items*required

Arbitrary tags associated with this shipment. Tags can be used to categorize shipments, and shipments can be queried by their tags. Note: Tags require object structure with name property, not simple strings.

Default []

-

shipments[].​tags[].​name*string**non-empty*required

The tag name.

Example: "Fragile"

shipments[].​order\_source\_code*string**(order\_source\_name)*

The order sources that are supported by ShipStation

Enum"amazon\_ca""amazon\_us""brightpearl""channel\_advisor""cratejoy""ebay""etsy""jane""groupon\_goods""magento"+10 more

shipments[].​packages*Array of objects**(package)**non-empty*required

The packages in the shipment.

> **Note:** Some carriers only allow one package per shipment. If you attempt to create a multi-package shipment for a carrier that doesn't allow it, an error will be returned.

-

shipments[].​packages[].​shipment\_package\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​packages[].​package\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​packages[].​package\_code*string**(package\_code)**[ 1 .. 50 ] characters*^[a-z0-9]+(\_[a-z0-9]+)\*$

A [package type] , such as `thick_envelope`, `small_flat_rate_box`, `large_package`, etc. Use the code `package` for custom or unknown package types.

Example: "small\_flat\_rate\_box"

shipments[].​packages[].​package\_name*string*

The name of the of the [package type]

Example: "Flat Rate Envelope"

shipments[].​packages[].​weight*object**(weight)*required

The weight of a package

-

shipments[].​packages[].​weight.​value*number**> 0*required

The weight, in the specified unit

Example: 23

shipments[].​packages[].​weight.​unit*string**(weight\_unit)*required

The possible weight unit values

Enum"pound""ounce""gram""kilogram"

shipments[].​packages[].​dimensions*object**(dimensions)*

The dimensions of a package

+Show 4 properties

shipments[].​packages[].​insured\_value*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

Default [{"currency":"usd","amount":0}]

+Show 2 properties

shipments[].​packages[].​label\_messages*object**(label\_messages)*

Custom messages to print on the shipping label for the package. These are typically used to print invoice numbers, product numbers, or other internal reference numbers. Not all carriers support label messages. The number of lines and the maximum length of each line also varies by carrier.

| Carrier | Max lines | Max line length |
| --- | --- | --- |
| USPS (Stamps.com) | 3 | 60 |
| FedEx | 3 | 35 for the first line. 30 for additional lines. |
| UPS | 2 | 35 |
| OnTrac | 2 | 25 |

+Show 3 properties

shipments[].​packages[].​external\_package\_id*string**non-empty*

An external package id.

Example: "se-1234545"

shipments[].​packages[].​tracking\_number*string**(tracking\_number)**non-empty*read-only

A tracking number for a package. The format depends on the carrier.

Example: "1Z932R800392060079"

shipments[].​packages[].​content\_description*string or null**[ 1 .. 35 ] characters*

A short description of the package content. Required for shipments moving to, from, and through Mexico.

Example: "Hand knitted wool socks"

shipments[].​packages[].​products*Array of objects**(products)**>= 0 items*

Details about products inside packages (Information provided would be used on custom documentation)

Default []

+Show 13 array properties

shipments[].​total\_weight*object**(weight)*read-onlyrequired

The weight of a package

-

shipments[].​total\_weight.​value*number**> 0*required

The weight, in the specified unit

Example: 3

shipments[].​total\_weight.​unit*string**(weight\_unit)*required

The possible weight unit values

Enum"pound""ounce""gram""kilogram"

Example: "pound"

shipments[].​comparison\_rate\_type*string or null*

Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only supported for UPS and USPS.

Example: "retail"

total*integer**(int64)**>= 0*read-onlyrequired

Total number of shipments returned by the api call

Example: 1990

page*integer**(int32)**>= 1*read-onlyrequired

Example: 12

pages*integer**(int32)**>= 1*read-onlyrequired

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
  "shipments": [
    { … }
  ],
  "total": 1990,
  "page": 12,
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

Create shipments
----------------

#### RequestExpand all

Create one or more shipments

Security:
api\_keys

Bodyapplication/jsonrequired

shipments*Array of objects**(create\_shipment\_request)**non-empty*required

Array of shipments to create

-

shipments[].​validate\_address*string**(validate\_address)*

The possible validate address values

Enum"no\_validation""validate\_only""validate\_and\_clean"

shipments[].​external\_shipment\_id*string or null**<= 50 characters*

A unique user-defined key to identify a shipment. This can be used to retrieve the shipment.

Example: "1751939189"

shipments[].​carrier\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​create\_sales\_order*boolean*

Whether to create a sales order for this shipment

Default false

Example: true

shipments[].​store\_id*string or null*

The store ID associated with the shipment

Example: "1582173"

shipments[].​notes\_from\_buyer*string or null*

Notes from the buyer

Example: "I am a note from the buyer"

shipments[].​notes\_for\_gift*string or null*

Gift notes

Example: "I am a gift note"

shipments[].​is\_gift*boolean*

Indicates if the shipment is a gift

Default false

Example: true

shipments[].​zone*integer or null**(int32)**>= 0*

Shipping zone

Example: 0

shipments[].​display\_scheme*string or null*

Display scheme for the shipment

Example: "paperless"

shipments[].​assigned\_user*string or null*

User assigned to the shipment

Example: "a2df9fa5-b7ee-467f-be4e-9c660542c187"

shipments[].​shipment\_status*string**(shipment\_status)*

The possible shipment status values

Enum"pending""processing""label\_purchased""cancelled"

Example: "pending"

shipments[].​amount\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​shipping\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​tax\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​ship\_to*object**(shipping\_address\_to)*

A complete or partial mailing address.

+Show 14 properties

shipments[].​ship\_from*object**(shipping\_address)*

A complete or partial mailing address.

+Show 13 properties

shipments[].​items*Array of objects**(shipment\_item)*

Items included in this shipment

Default []

+Show 22 array properties

shipments[].​packages*Array of objects**(package)**non-empty*

The packages in the shipment

+Show 10 array properties

post

/v2/shipments

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/shipments
* Production https://api.shipstation.com/v2/shipments

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
curl -i -X POST \
  https://docs.shipstation.com/_mock/openapi/v2/shipments \
  -H 'Content-Type: application/json' \
  -H 'api-key: YOUR_API_KEY_HERE' \
  -d '{
    "shipments": [
      {
        "validate_address": "no_validation",
        "external_shipment_id": "1751939189",
        "carrier_id": "se-2774150",
        "create_sales_order": true,
        "store_id": "1582173",
        "notes_from_buyer": "I am a note from the buyer",
        "notes_for_gift": "I am a gift note",
        "is_gift": true,
        "zone": 0,
        "display_scheme": "paperless",
        "assigned_user": "a2df9fa5-b7ee-467f-be4e-9c660542c187",
        "shipment_status": "pending",
        "amount_paid": {
          "currency": "string",
          "amount": 12
        },
        "shipping_paid": {
          "currency": "string",
          "amount": 12
        },
        "tax_paid": {
          "currency": "string",
          "amount": 12
        },
        "ship_to": {
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
          "address_residential_indicator": "yes",
          "instructions": "any instruction",
          "geolocation": [
            {
              "type": "what3words",
              "value": "cats.with.thumbs"
            }
          ]
        },
        "ship_from": {
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
          "address_residential_indicator": "yes",
          "instructions": "any instructions"
        },
        "items": [],
        "packages": [
          {
            "package_id": "se-123456",
            "package_code": "thick_envelope",
            "package_name": "Flat Rate Envelope",
            "weight": {
              "value": 23,
              "unit": "pound"
            },
            "dimensions": {
              "unit": "inch",
              "length": 2,
              "width": 2,
              "height": 1
            },
            "insured_value": [
              {
                "currency": "usd",
                "amount": 0
              }
            ],
            "label_messages": {
              "reference1": "Reference",
              "reference2": "Reference 2",
              "reference3": "Reference 3"
            },
            "external_package_id": "se-1234545",
            "content_description": "Hand knitted wool socks",
            "products": []
          }
        ]
      }
    ]
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

has\_errors*boolean*read-onlyrequired

Indicates if any shipments had errors during creation

Example: false

shipments*Array of objects**(create\_shipment\_response)*read-onlyrequired

Array of created shipments with their results

-

shipments[].​shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​carrier\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​service\_code*string or null**(service\_code)*^[a-z0-9]+(\_[a-z0-9-]+)\* ?$

A [carrier service], such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, etc.

Example: "usps\_first\_class\_mail"

shipments[].​requested\_shipment\_service*string or null*

The requested shipment service

Example: "usps\_priority\_mail"

shipments[].​shipping\_rule\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​external\_order\_id*string or null*

ID that the Order Source assigned

Example: "1232434"

shipments[].​hold\_until\_date*string or null**(date-time)*

Date to hold the shipment until

Example: "2025-01-15T00:00:00.000Z"

shipments[].​ship\_by\_date*string or null**(date-time)*

Date by which the shipment should be shipped

Example: "2025-01-15T00:00:00.000Z"

shipments[].​retail\_rate*object or null**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​store\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​items*Array of objects**(shipment\_item)*

Describe the packages included in this shipment as related to potential metadata that was imported from external order sources

Default []

+Show 22 array properties

shipments[].​notes\_from\_buyer*string or null*

Notes from the buyer

Example: "Please handle with care"

shipments[].​notes\_for\_gift*string or null*

Gift notes

Example: "Happy Birthday!"

shipments[].​is\_gift*boolean*

Indicates if the shipment is a gift

Default false

Example: true

shipments[].​assigned\_user*string or null*

User assigned to the shipment

Example: "user@example.com"

shipments[].​amount\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​shipping\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​tax\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipments[].​zone*integer or null**(int32)**>= 0*

Shipping zone

Example: 1

shipments[].​display\_scheme*string or null*

Display scheme for the shipment

Example: "label"

shipments[].​tax\_identifiers*Array of objects or null**(tax\_identifier)*

+Show 4 array properties

shipments[].​external\_shipment\_id*string or null**<= 50 characters*

A unique user-defined key to identify a shipment. This can be used to retrieve the shipment.

> **Warning:** The `external_shipment_id` is limited to 50 characters. Any additional characters will be truncated.

Example: "1234556"

shipments[].​shipment\_number*string or null**<= 50 characters*

A non-unique user-defined number used to identify a shipment. If undefined, this will match the external\_shipment\_id of the shipment.

> **Warning:** The `shipment_number` is limited to 50 characters. Any additional characters will be truncated.

Example: "10001"

shipments[].​ship\_date*string or null**(date-time)**(date)*^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?...Show pattern

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date, but not a specific time. The value *may* contain a time component, but it will be set to `00:00:00` UTC by ShipStation .

Example: "2018-09-23"

shipments[].​created\_at*string**(date-time)**(date\_time)*^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(...Show patternread-onlyrequired

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.

Example: "2018-09-23T15:00:00.000Z"

shipments[].​modified\_at*string**(date-time)**(date\_time)*^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(...Show patternread-onlyrequired

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.

Example: "2018-09-23T15:00:00.000Z"

shipments[].​shipment\_status*string**(shipment\_status)*read-onlyrequired

The possible shipment status values

Default "pending"

Enum"pending""processing""label\_purchased""cancelled"

shipments[].​ship\_to*object**(shipping\_address\_to)*required

A complete or partial mailing address.

-

shipments[].​ship\_to.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

shipments[].​ship\_to.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

shipments[].​ship\_to.​email*string or null*

Email for the address owner.

Example: "example@example.com"

shipments[].​ship\_to.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

shipments[].​ship\_to.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

shipments[].​ship\_to.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

shipments[].​ship\_to.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

shipments[].​ship\_to.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

shipments[].​ship\_to.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

shipments[].​ship\_to.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

shipments[].​ship\_to.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

shipments[].​ship\_to.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

shipments[].​ship\_to.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instruction"

shipments[].​ship\_to.​geolocation*Array of objects*

+Show 2 array properties

shipments[].​ship\_from*object**(shipping\_address)*required

A complete or partial mailing address.

-

shipments[].​ship\_from.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

shipments[].​ship\_from.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

shipments[].​ship\_from.​email*string or null*

Email for the address owner.

Example: "example@example.com"

shipments[].​ship\_from.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

shipments[].​ship\_from.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

shipments[].​ship\_from.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

shipments[].​ship\_from.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

shipments[].​ship\_from.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

shipments[].​ship\_from.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

shipments[].​ship\_from.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

shipments[].​ship\_from.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

shipments[].​ship\_from.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

shipments[].​ship\_from.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instructions"

shipments[].​warehouse\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Default null

Example: "se-28529731"

shipments[].​return\_to*object**(shipping\_address)*required

A complete or partial mailing address.

-

shipments[].​return\_to.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

shipments[].​return\_to.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

shipments[].​return\_to.​email*string or null*

Email for the address owner.

Example: "example@example.com"

shipments[].​return\_to.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

shipments[].​return\_to.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

shipments[].​return\_to.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

shipments[].​return\_to.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

shipments[].​return\_to.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

shipments[].​return\_to.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

shipments[].​return\_to.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

shipments[].​return\_to.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

shipments[].​return\_to.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

shipments[].​return\_to.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instructions"

shipments[].​is\_return*boolean or null*

An optional indicator if the shipment is intended to be a return. Defaults to false if not provided.

Default false

Example: true

shipments[].​confirmation*string**(delivery\_confirmation)*required

The possible delivery confirmation values

Default "none"

Enum"none""delivery""signature""adult\_signature""direct\_signature""delivery\_mailed""verbal\_confirmation"

shipments[].​customs*object or null**(international\_shipment\_options)*

Options for international shipments, such as customs declarations.

Default null

+Show 8 properties

shipments[].​advanced\_options*object**(advanced\_shipment\_options)*required

Advanced shipment options

-

shipments[].​advanced\_options.​bill\_to\_account*string or null*

This field is used to [bill shipping costs to a third party]. This field must be used in conjunction with the `bill_to_country_code`, `bill_to_party`, and `bill_to_postal_code` fields.

Default null

Example: "123456789"

shipments[].​advanced\_options.​bill\_to\_country\_code*string or null**(country\_code)**= 2 characters*

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Default null

Example: "CA"

shipments[].​advanced\_options.​bill\_to\_party*string or null**(bill\_to\_party)*

The possible bill to party values

Default null

Enum"recipient""third\_party"

Example: "third\_party"

shipments[].​advanced\_options.​bill\_to\_postal\_code*string or null*

The postal code of the third-party that is responsible for shipping costs.

Default null

Example: "28005"

shipments[].​advanced\_options.​contains\_alcohol*boolean*

Indicates that the shipment contains alcohol.

Default false

Example: true

shipments[].​advanced\_options.​delivered\_duty\_paid*boolean*

Indicates that the shipper is paying the international delivery duties for this shipment. This option is supported by UPS, FedEx, and DHL Express.

Default false

Example: true

shipments[].​advanced\_options.​dry\_ice*boolean*

Indicates if the shipment contain dry ice

Default false

Example: true

shipments[].​advanced\_options.​dry\_ice\_weight*object or null**(weight)*

The weight of a package

+Show 2 properties

shipments[].​advanced\_options.​non\_machinable*boolean*

Indicates that the package cannot be processed automatically because it is too large or irregularly shaped. This is primarily for USPS shipments. See [Section 1.2 of the USPS parcel standards](https://pe.usps.com/text/dmm300/101.htm#ep1047495) for details.

Default false

Example: true

shipments[].​advanced\_options.​saturday\_delivery*boolean*

Enables Saturday delivery, if supported by the carrier.

Default false

Example: true

shipments[].​advanced\_options.​fedex\_freight*object*

Provide details for the Fedex freight service

+Show 2 properties

shipments[].​advanced\_options.​use\_ups\_ground\_freight\_pricing*boolean or null*

Whether to use [UPS Ground Freight pricing] If enabled, then a `freight_class` must also be specified.

Default null

Example: true

shipments[].​advanced\_options.​freight\_class*string or null*

The National Motor Freight Traffic Association [freight class](http://www.nmfta.org/pages/nmfc?AspxAutoDetectCookieSupport=1), such as "77.5", "110", or "250".

Default null

Example: "77.5"

shipments[].​advanced\_options.​custom\_field1*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 1"

shipments[].​advanced\_options.​custom\_field2*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 2"

shipments[].​advanced\_options.​custom\_field3*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 3"

shipments[].​advanced\_options.​origin\_type*string or null**(origin\_type)*

Indicates if the package will be picked up or dropped off by the carrier

Default null

Enum"pickup""drop\_off"

shipments[].​advanced\_options.​additional\_handling*boolean or null*

Indicate to the carrier that this shipment requires additional handling.

Default null

Example: true

shipments[].​advanced\_options.​shipper\_release*boolean or null*

Default null

Example: true

shipments[].​advanced\_options.​collect\_on\_delivery*object**(collect\_on\_delivery)*

Defer payment until package is delivered, instead of when it is ordered.

+Show 2 properties

shipments[].​advanced\_options.​third\_party\_consignee*boolean*

Third Party Consignee option is a value-added service that allows the shipper to supply goods without commercial invoices being attached

Default false

Example: true

shipments[].​advanced\_options.​dangerous\_goods*boolean*

Indicates if the Dangerous goods are present in the shipment

Default false

Example: true

shipments[].​advanced\_options.​dangerous\_goods\_contact*object*

Contact information for Dangerous goods

+Show 2 properties

shipments[].​advanced\_options.​windsor\_framework\_details*object*

The Windsor framework is a new regulation in the UK that simplifies customs procedures for goods moved from the UK mainland to Northern Ireland.

+Show 2 properties

shipments[].​advanced\_options.​ancillary\_endorsements\_option*string or null*

Ancillary endorsements option for the shipment

Example: "forward"

shipments[].​advanced\_options.​return\_pickup\_attempts*integer or null*

Number of return pickup attempts

Example: 3

shipments[].​advanced\_options.​own\_document\_upload*boolean*

Indicates if own document upload is enabled

Default false

Example: false

shipments[].​advanced\_options.​limited\_quantity*boolean*

Indicates if the shipment contains limited quantities

Default false

Example: false

shipments[].​advanced\_options.​event\_notification*boolean*

Indicates if event notifications are enabled

Default false

Example: false

shipments[].​insurance\_provider*string**(insurance\_provider)*required

The possible insurance provider values

Default "none"

Enum"none""shipsurance""carrier""third\_party"

shipments[].​tags*Array of objects**(tag)**>= 0 items*required

Arbitrary tags associated with this shipment. Tags can be used to categorize shipments, and shipments can be queried by their tags. Note: Tags require object structure with name property, not simple strings.

Default []

-

shipments[].​tags[].​name*string**non-empty*required

The tag name.

Example: "Fragile"

shipments[].​order\_source\_code*string**(order\_source\_name)*

The order sources that are supported by ShipStation

Enum"amazon\_ca""amazon\_us""brightpearl""channel\_advisor""cratejoy""ebay""etsy""jane""groupon\_goods""magento"+10 more

shipments[].​packages*Array of objects**(package)**non-empty*required

The packages in the shipment.

> **Note:** Some carriers only allow one package per shipment. If you attempt to create a multi-package shipment for a carrier that doesn't allow it, an error will be returned.

-

shipments[].​packages[].​shipment\_package\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​packages[].​package\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipments[].​packages[].​package\_code*string**(package\_code)**[ 1 .. 50 ] characters*^[a-z0-9]+(\_[a-z0-9]+)\*$

A [package type] , such as `thick_envelope`, `small_flat_rate_box`, `large_package`, etc. Use the code `package` for custom or unknown package types.

Example: "small\_flat\_rate\_box"

shipments[].​packages[].​package\_name*string*

The name of the of the [package type]

Example: "Flat Rate Envelope"

shipments[].​packages[].​weight*object**(weight)*required

The weight of a package

-

shipments[].​packages[].​weight.​value*number**> 0*required

The weight, in the specified unit

Example: 23

shipments[].​packages[].​weight.​unit*string**(weight\_unit)*required

The possible weight unit values

Enum"pound""ounce""gram""kilogram"

shipments[].​packages[].​dimensions*object**(dimensions)*

The dimensions of a package

+Show 4 properties

shipments[].​packages[].​insured\_value*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

Default [{"currency":"usd","amount":0}]

+Show 2 properties

shipments[].​packages[].​label\_messages*object**(label\_messages)*

Custom messages to print on the shipping label for the package. These are typically used to print invoice numbers, product numbers, or other internal reference numbers. Not all carriers support label messages. The number of lines and the maximum length of each line also varies by carrier.

| Carrier | Max lines | Max line length |
| --- | --- | --- |
| USPS (Stamps.com) | 3 | 60 |
| FedEx | 3 | 35 for the first line. 30 for additional lines. |
| UPS | 2 | 35 |
| OnTrac | 2 | 25 |

+Show 3 properties

shipments[].​packages[].​external\_package\_id*string**non-empty*

An external package id.

Example: "se-1234545"

shipments[].​packages[].​tracking\_number*string**(tracking\_number)**non-empty*read-only

A tracking number for a package. The format depends on the carrier.

Example: "1Z932R800392060079"

shipments[].​packages[].​content\_description*string or null**[ 1 .. 35 ] characters*

A short description of the package content. Required for shipments moving to, from, and through Mexico.

Example: "Hand knitted wool socks"

shipments[].​packages[].​products*Array of objects**(products)**>= 0 items*

Details about products inside packages (Information provided would be used on custom documentation)

Default []

+Show 13 array properties

shipments[].​total\_weight*object**(weight)*read-onlyrequired

The weight of a package

-

shipments[].​total\_weight.​value*number**> 0*required

The weight, in the specified unit

Example: 3

shipments[].​total\_weight.​unit*string**(weight\_unit)*required

The possible weight unit values

Enum"pound""ounce""gram""kilogram"

Example: "pound"

shipments[].​comparison\_rate\_type*string or null*

Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only supported for UPS and USPS.

Example: "retail"

shipments[].​errors*Array of strings*read-only

An array of errors that occurred while creating the shipment.

Example: ["Parameter value is out of range."]

shipments[].​address\_validation*object or null**(address\_validation\_result)*

An address validation result

+Show 4 properties

Response

1. 200
2. 400
3. 500

application/json

```
{
  "has_errors": false,
  "shipments": [
    { … }
  ]
}
```

#### Was this helpful?

Get shipment by external id
---------------------------

#### Request

Query Shipments created using your own custom ID convention using this endpoint

Security:
api\_keys

Path

external\_shipment\_id*string*required

Example: 0bcb569d-1727-4ff9-ab49-b2fec0cee5ae

get

/v2/shipments/external\_shipment\_id/{external\_shipment\_id}

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/shipments/external\_shipment\_id/{external\_shipment\_id}
* Production https://api.shipstation.com/v2/shipments/external\_shipment\_id/{external\_shipment\_id}

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
  'https://docs.shipstation.com/_mock/openapi/v2/shipments/external_shipment_id/{external_shipment_id}' \
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

shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

carrier\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

service\_code*string or null**(service\_code)*^[a-z0-9]+(\_[a-z0-9-]+)\* ?$

A [carrier service], such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, etc.

Example: "usps\_first\_class\_mail"

requested\_shipment\_service*string or null*

The requested shipment service

Example: "usps\_priority\_mail"

shipping\_rule\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

external\_order\_id*string or null*

ID that the Order Source assigned

Example: "1232434"

hold\_until\_date*string or null**(date-time)*

Date to hold the shipment until

Example: "2025-01-15T00:00:00.000Z"

ship\_by\_date*string or null**(date-time)*

Date by which the shipment should be shipped

Example: "2025-01-15T00:00:00.000Z"

retail\_rate*object or null**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

store\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

items*Array of objects**(shipment\_item)*

Describe the packages included in this shipment as related to potential metadata that was imported from external order sources

Default []

+Show 22 array properties

notes\_from\_buyer*string or null*

Notes from the buyer

Example: "Please handle with care"

notes\_for\_gift*string or null*

Gift notes

Example: "Happy Birthday!"

is\_gift*boolean*

Indicates if the shipment is a gift

Default false

Example: true

assigned\_user*string or null*

User assigned to the shipment

Example: "user@example.com"

amount\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipping\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

tax\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

zone*integer or null**(int32)**>= 0*

Shipping zone

Example: 1

display\_scheme*string or null*

Display scheme for the shipment

Example: "label"

tax\_identifiers*Array of objects or null**(tax\_identifier)*

+Show 4 array properties

external\_shipment\_id*string or null**<= 50 characters*

A unique user-defined key to identify a shipment. This can be used to retrieve the shipment.

> **Warning:** The `external_shipment_id` is limited to 50 characters. Any additional characters will be truncated.

Example: "1234556"

shipment\_number*string or null**<= 50 characters*

A non-unique user-defined number used to identify a shipment. If undefined, this will match the external\_shipment\_id of the shipment.

> **Warning:** The `shipment_number` is limited to 50 characters. Any additional characters will be truncated.

Example: "10001"

ship\_date*string or null**(date-time)**(date)*^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?...Show pattern

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date, but not a specific time. The value *may* contain a time component, but it will be set to `00:00:00` UTC by ShipStation .

Example: "2018-09-23"

created\_at*string**(date-time)**(date\_time)*^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(...Show patternread-onlyrequired

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.

Example: "2018-09-23T15:00:00.000Z"

modified\_at*string**(date-time)**(date\_time)*^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(...Show patternread-onlyrequired

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.

Example: "2018-09-23T15:00:00.000Z"

shipment\_status*string**(shipment\_status)*read-onlyrequired

The possible shipment status values

Default "pending"

Enum"pending""processing""label\_purchased""cancelled"

ship\_to*object**(shipping\_address\_to)*required

A complete or partial mailing address.

-

ship\_to.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

ship\_to.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

ship\_to.​email*string or null*

Email for the address owner.

Example: "example@example.com"

ship\_to.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

ship\_to.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

ship\_to.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

ship\_to.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

ship\_to.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

ship\_to.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

ship\_to.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

ship\_to.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

ship\_to.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

ship\_to.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instruction"

ship\_to.​geolocation*Array of objects*

+Show 2 array properties

ship\_from*object**(shipping\_address)*required

A complete or partial mailing address.

-

ship\_from.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

ship\_from.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

ship\_from.​email*string or null*

Email for the address owner.

Example: "example@example.com"

ship\_from.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

ship\_from.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

ship\_from.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

ship\_from.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

ship\_from.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

ship\_from.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

ship\_from.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

ship\_from.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

ship\_from.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

ship\_from.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instructions"

warehouse\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Default null

Example: "se-28529731"

return\_to*object**(shipping\_address)*required

A complete or partial mailing address.

-

return\_to.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

return\_to.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

return\_to.​email*string or null*

Email for the address owner.

Example: "example@example.com"

return\_to.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

return\_to.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

return\_to.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

return\_to.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

return\_to.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

return\_to.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

return\_to.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

return\_to.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

return\_to.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

return\_to.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instructions"

is\_return*boolean or null*

An optional indicator if the shipment is intended to be a return. Defaults to false if not provided.

Default false

Example: true

confirmation*string**(delivery\_confirmation)*required

The possible delivery confirmation values

Default "none"

Enum"none""delivery""signature""adult\_signature""direct\_signature""delivery\_mailed""verbal\_confirmation"

customs*object or null**(international\_shipment\_options)*

Options for international shipments, such as customs declarations.

Default null

+Show 8 properties

advanced\_options*object**(advanced\_shipment\_options)*required

Advanced shipment options

-

advanced\_options.​bill\_to\_account*string or null*

This field is used to [bill shipping costs to a third party]. This field must be used in conjunction with the `bill_to_country_code`, `bill_to_party`, and `bill_to_postal_code` fields.

Default null

Example: "123456789"

advanced\_options.​bill\_to\_country\_code*string or null**(country\_code)**= 2 characters*

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Default null

Example: "CA"

advanced\_options.​bill\_to\_party*string or null**(bill\_to\_party)*

The possible bill to party values

Default null

Enum"recipient""third\_party"

Example: "third\_party"

advanced\_options.​bill\_to\_postal\_code*string or null*

The postal code of the third-party that is responsible for shipping costs.

Default null

Example: "28005"

advanced\_options.​contains\_alcohol*boolean*

Indicates that the shipment contains alcohol.

Default false

Example: true

advanced\_options.​delivered\_duty\_paid*boolean*

Indicates that the shipper is paying the international delivery duties for this shipment. This option is supported by UPS, FedEx, and DHL Express.

Default false

Example: true

advanced\_options.​dry\_ice*boolean*

Indicates if the shipment contain dry ice

Default false

Example: true

advanced\_options.​dry\_ice\_weight*object or null**(weight)*

The weight of a package

+Show 2 properties

advanced\_options.​non\_machinable*boolean*

Indicates that the package cannot be processed automatically because it is too large or irregularly shaped. This is primarily for USPS shipments. See [Section 1.2 of the USPS parcel standards](https://pe.usps.com/text/dmm300/101.htm#ep1047495) for details.

Default false

Example: true

advanced\_options.​saturday\_delivery*boolean*

Enables Saturday delivery, if supported by the carrier.

Default false

Example: true

advanced\_options.​fedex\_freight*object*

Provide details for the Fedex freight service

+Show 2 properties

advanced\_options.​use\_ups\_ground\_freight\_pricing*boolean or null*

Whether to use [UPS Ground Freight pricing] If enabled, then a `freight_class` must also be specified.

Default null

Example: true

advanced\_options.​freight\_class*string or null*

The National Motor Freight Traffic Association [freight class](http://www.nmfta.org/pages/nmfc?AspxAutoDetectCookieSupport=1), such as "77.5", "110", or "250".

Default null

Example: "77.5"

advanced\_options.​custom\_field1*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 1"

advanced\_options.​custom\_field2*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 2"

advanced\_options.​custom\_field3*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 3"

advanced\_options.​origin\_type*string or null**(origin\_type)*

Indicates if the package will be picked up or dropped off by the carrier

Default null

Enum"pickup""drop\_off"

advanced\_options.​additional\_handling*boolean or null*

Indicate to the carrier that this shipment requires additional handling.

Default null

Example: true

advanced\_options.​shipper\_release*boolean or null*

Default null

Example: true

advanced\_options.​collect\_on\_delivery*object**(collect\_on\_delivery)*

Defer payment until package is delivered, instead of when it is ordered.

+Show 2 properties

advanced\_options.​third\_party\_consignee*boolean*

Third Party Consignee option is a value-added service that allows the shipper to supply goods without commercial invoices being attached

Default false

Example: true

advanced\_options.​dangerous\_goods*boolean*

Indicates if the Dangerous goods are present in the shipment

Default false

Example: true

advanced\_options.​dangerous\_goods\_contact*object*

Contact information for Dangerous goods

+Show 2 properties

advanced\_options.​windsor\_framework\_details*object*

The Windsor framework is a new regulation in the UK that simplifies customs procedures for goods moved from the UK mainland to Northern Ireland.

+Show 2 properties

advanced\_options.​ancillary\_endorsements\_option*string or null*

Ancillary endorsements option for the shipment

Example: "forward"

advanced\_options.​return\_pickup\_attempts*integer or null*

Number of return pickup attempts

Example: 3

advanced\_options.​own\_document\_upload*boolean*

Indicates if own document upload is enabled

Default false

Example: false

advanced\_options.​limited\_quantity*boolean*

Indicates if the shipment contains limited quantities

Default false

Example: false

advanced\_options.​event\_notification*boolean*

Indicates if event notifications are enabled

Default false

Example: false

insurance\_provider*string**(insurance\_provider)*required

The possible insurance provider values

Default "none"

Enum"none""shipsurance""carrier""third\_party"

tags*Array of objects**(tag)**>= 0 items*required

Arbitrary tags associated with this shipment. Tags can be used to categorize shipments, and shipments can be queried by their tags. Note: Tags require object structure with name property, not simple strings.

Default []

-

tags[].​name*string**non-empty*required

The tag name.

Example: "Fragile"

order\_source\_code*string**(order\_source\_name)*

The order sources that are supported by ShipStation

Enum"amazon\_ca""amazon\_us""brightpearl""channel\_advisor""cratejoy""ebay""etsy""jane""groupon\_goods""magento"+10 more

packages*Array of objects**(package)**non-empty*required

The packages in the shipment.

> **Note:** Some carriers only allow one package per shipment. If you attempt to create a multi-package shipment for a carrier that doesn't allow it, an error will be returned.

-

packages[].​shipment\_package\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

packages[].​package\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

packages[].​package\_code*string**(package\_code)**[ 1 .. 50 ] characters*^[a-z0-9]+(\_[a-z0-9]+)\*$

A [package type] , such as `thick_envelope`, `small_flat_rate_box`, `large_package`, etc. Use the code `package` for custom or unknown package types.

Example: "small\_flat\_rate\_box"

packages[].​package\_name*string*

The name of the of the [package type]

Example: "Flat Rate Envelope"

packages[].​weight*object**(weight)*required

The weight of a package

-

packages[].​weight.​value*number**> 0*required

The weight, in the specified unit

Example: 23

packages[].​weight.​unit*string**(weight\_unit)*required

The possible weight unit values

Enum"pound""ounce""gram""kilogram"

packages[].​dimensions*object**(dimensions)*

The dimensions of a package

+Show 4 properties

packages[].​insured\_value*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

Default [{"currency":"usd","amount":0}]

+Show 2 properties

packages[].​label\_messages*object**(label\_messages)*

Custom messages to print on the shipping label for the package. These are typically used to print invoice numbers, product numbers, or other internal reference numbers. Not all carriers support label messages. The number of lines and the maximum length of each line also varies by carrier.

| Carrier | Max lines | Max line length |
| --- | --- | --- |
| USPS (Stamps.com) | 3 | 60 |
| FedEx | 3 | 35 for the first line. 30 for additional lines. |
| UPS | 2 | 35 |
| OnTrac | 2 | 25 |

+Show 3 properties

packages[].​external\_package\_id*string**non-empty*

An external package id.

Example: "se-1234545"

packages[].​tracking\_number*string**(tracking\_number)**non-empty*read-only

A tracking number for a package. The format depends on the carrier.

Example: "1Z932R800392060079"

packages[].​content\_description*string or null**[ 1 .. 35 ] characters*

A short description of the package content. Required for shipments moving to, from, and through Mexico.

Example: "Hand knitted wool socks"

packages[].​products*Array of objects**(products)**>= 0 items*

Details about products inside packages (Information provided would be used on custom documentation)

Default []

+Show 13 array properties

total\_weight*object**(weight)*read-onlyrequired

The weight of a package

-

total\_weight.​value*number**> 0*required

The weight, in the specified unit

Example: 3

total\_weight.​unit*string**(weight\_unit)*required

The possible weight unit values

Enum"pound""ounce""gram""kilogram"

Example: "pound"

comparison\_rate\_type*string or null*

Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only supported for UPS and USPS.

Example: "retail"

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "shipment_id": "se-28529731",
  "carrier_id": "se-1234567",
  "service_code": "se_1234567",
  "requested_shipment_service": "usps_priority_mail",
  "shipping_rule_id": "se-1234",
  "external_order_id": "1232434",
  "hold_until_date": "2025-01-15T00:00:00.000Z",
  "ship_by_date": "2025-01-15T00:00:00.000Z",
  "retail_rate": {
    "currency": "string",
    "amount": 12
  },
  "store_id": "se-12345",
  "items": [],
  "notes_from_buyer": "Please handle with care",
  "notes_for_gift": "Happy Birthday!",
  "is_gift": true,
  "assigned_user": "user@example.com",
  "amount_paid": {
    "currency": "string",
    "amount": 12
  },
  "shipping_paid": {
    "currency": "string",
    "amount": 12
  },
  "tax_paid": {
    "currency": "string",
    "amount": 12
  },
  "zone": 1,
  "display_scheme": "label",
  "tax_identifiers": [
    { … }
  ],
  "external_shipment_id": "1234556",
  "shipment_number": "10001",
  "ship_date": "2018-09-23",
  "created_at": "2018-09-23T15:00:00.000Z",
  "modified_at": "2018-09-23T15:00:00.000Z",
  "shipment_status": "pending",
  "ship_to": {
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
    "address_residential_indicator": "yes",
    "instructions": "any instruction",
    "geolocation": [ … ]
  },
  "ship_from": {
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
    "address_residential_indicator": "yes",
    "instructions": "any instructions"
  },
  "warehouse_id": null,
  "return_to": {
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
    "address_residential_indicator": "yes",
    "instructions": "any instructions"
  },
  "is_return": true,
  "confirmation": "none",
  "customs": null,
  "advanced_options": {
    "bill_to_account": "123456789",
    "bill_to_country_code": "US",
    "bill_to_party": "third_party",
    "bill_to_postal_code": "28005",
    "contains_alcohol": true,
    "delivered_duty_paid": true,
    "dry_ice": true,
    "dry_ice_weight": { … },
    "non_machinable": true,
    "saturday_delivery": true,
    "fedex_freight": { … },
    "use_ups_ground_freight_pricing": true,
    "freight_class": "77.5",
    "custom_field1": "custom field 1",
    "custom_field2": "custom field 2",
    "custom_field3": "custom field 3",
    "origin_type": null,
    "additional_handling": true,
    "shipper_release": true,
    "collect_on_delivery": { … },
    "third_party_consignee": true,
    "dangerous_goods": true,
    "dangerous_goods_contact": { … },
    "windsor_framework_details": { … },
    "ancillary_endorsements_option": "forward",
    "return_pickup_attempts": 3,
    "own_document_upload": false,
    "limited_quantity": false,
    "event_notification": false
  },
  "insurance_provider": "none",
  "tags": [],
  "order_source_code": "amazon_ca",
  "packages": [
    { … }
  ],
  "total_weight": {
    "value": 3,
    "unit": "pound"
  },
  "comparison_rate_type": "retail"
}
```

#### Was this helpful?

Get shipment by id
------------------

#### Request

Get an individual shipment based on its ID

Security:
api\_keys

Path

shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Shipment ID

Example: se-28529731

get

/v2/shipments/{shipment\_id}

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/shipments/{shipment\_id}
* Production https://api.shipstation.com/v2/shipments/{shipment\_id}

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
  'https://docs.shipstation.com/_mock/openapi/v2/shipments/{shipment_id}' \
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

shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

carrier\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

service\_code*string or null**(service\_code)*^[a-z0-9]+(\_[a-z0-9-]+)\* ?$

A [carrier service], such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, etc.

Example: "usps\_first\_class\_mail"

requested\_shipment\_service*string or null*

The requested shipment service

Example: "usps\_priority\_mail"

shipping\_rule\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

external\_order\_id*string or null*

ID that the Order Source assigned

Example: "1232434"

hold\_until\_date*string or null**(date-time)*

Date to hold the shipment until

Example: "2025-01-15T00:00:00.000Z"

ship\_by\_date*string or null**(date-time)*

Date by which the shipment should be shipped

Example: "2025-01-15T00:00:00.000Z"

retail\_rate*object or null**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

store\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

items*Array of objects**(shipment\_item)*

Describe the packages included in this shipment as related to potential metadata that was imported from external order sources

Default []

+Show 22 array properties

notes\_from\_buyer*string or null*

Notes from the buyer

Example: "Please handle with care"

notes\_for\_gift*string or null*

Gift notes

Example: "Happy Birthday!"

is\_gift*boolean*

Indicates if the shipment is a gift

Default false

Example: true

assigned\_user*string or null*

User assigned to the shipment

Example: "user@example.com"

amount\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

shipping\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

tax\_paid*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

zone*integer or null**(int32)**>= 0*

Shipping zone

Example: 1

display\_scheme*string or null*

Display scheme for the shipment

Example: "label"

tax\_identifiers*Array of objects or null**(tax\_identifier)*

+Show 4 array properties

external\_shipment\_id*string or null**<= 50 characters*

A unique user-defined key to identify a shipment. This can be used to retrieve the shipment.

> **Warning:** The `external_shipment_id` is limited to 50 characters. Any additional characters will be truncated.

Example: "1234556"

shipment\_number*string or null**<= 50 characters*

A non-unique user-defined number used to identify a shipment. If undefined, this will match the external\_shipment\_id of the shipment.

> **Warning:** The `shipment_number` is limited to 50 characters. Any additional characters will be truncated.

Example: "10001"

ship\_date*string or null**(date-time)**(date)*^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?...Show pattern

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date, but not a specific time. The value *may* contain a time component, but it will be set to `00:00:00` UTC by ShipStation .

Example: "2018-09-23"

created\_at*string**(date-time)**(date\_time)*^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(...Show patternread-onlyrequired

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.

Example: "2018-09-23T15:00:00.000Z"

modified\_at*string**(date-time)**(date\_time)*^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(...Show patternread-onlyrequired

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date and time.

Example: "2018-09-23T15:00:00.000Z"

shipment\_status*string**(shipment\_status)*read-onlyrequired

The possible shipment status values

Default "pending"

Enum"pending""processing""label\_purchased""cancelled"

ship\_to*object**(shipping\_address\_to)*required

A complete or partial mailing address.

-

ship\_to.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

ship\_to.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

ship\_to.​email*string or null*

Email for the address owner.

Example: "example@example.com"

ship\_to.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

ship\_to.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

ship\_to.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

ship\_to.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

ship\_to.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

ship\_to.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

ship\_to.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

ship\_to.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

ship\_to.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

ship\_to.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instruction"

ship\_to.​geolocation*Array of objects*

+Show 2 array properties

ship\_from*object**(shipping\_address)*required

A complete or partial mailing address.

-

ship\_from.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

ship\_from.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

ship\_from.​email*string or null*

Email for the address owner.

Example: "example@example.com"

ship\_from.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

ship\_from.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

ship\_from.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

ship\_from.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

ship\_from.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

ship\_from.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

ship\_from.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

ship\_from.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

ship\_from.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

ship\_from.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instructions"

warehouse\_id*string or null**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Default null

Example: "se-28529731"

return\_to*object**(shipping\_address)*required

A complete or partial mailing address.

-

return\_to.​name*string**non-empty*required

The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` field.

Example: "John Doe"

return\_to.​phone*string**non-empty*required

The phone number of a contact person at this address. The format of this phone number varies depending on the country.

Example: "+1 204-253-9411 ext. 123"

return\_to.​email*string or null*

Email for the address owner.

Example: "example@example.com"

return\_to.​company\_name*string or null**non-empty*

If this is a business address, then the company name should be specified here.

Example: "The Home Depot"

return\_to.​address\_line1*string**non-empty*required

The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 lines.

Example: "1999 Bishop Grandin Blvd."

return\_to.​address\_line2*string or null**non-empty*

The second line of the street address. For some addresses, this line may not be needed.

Example: "Unit 408"

return\_to.​address\_line3*string or null**non-empty*

The third line of the street address. For some addresses, this line may not be needed.

Example: "Building #7"

return\_to.​city\_locality*string**non-empty*required

The name of the city or locality

Example: "Winnipeg"

return\_to.​state\_province*string**non-empty*required

The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the full name or abbreviation.

Example: "Manitoba"

return\_to.​postal\_code*string**(postal\_code)**non-empty*required

postal code

Example: "78756-3717"

return\_to.​country\_code*string**(country\_code)**= 2 characters*required

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Example: "CA"

return\_to.​address\_residential\_indicator*string**(address\_residential\_indicator)*required

Indicates whether an address is residential.

Default "unknown"

Enum"unknown""yes""no"

Example: "yes"

return\_to.​instructions*string or null**non-empty*

Additional text about how to handle the shipment at this address.

Example: "any instructions"

is\_return*boolean or null*

An optional indicator if the shipment is intended to be a return. Defaults to false if not provided.

Default false

Example: true

confirmation*string**(delivery\_confirmation)*required

The possible delivery confirmation values

Default "none"

Enum"none""delivery""signature""adult\_signature""direct\_signature""delivery\_mailed""verbal\_confirmation"

customs*object or null**(international\_shipment\_options)*

Options for international shipments, such as customs declarations.

Default null

+Show 8 properties

advanced\_options*object**(advanced\_shipment\_options)*required

Advanced shipment options

-

advanced\_options.​bill\_to\_account*string or null*

This field is used to [bill shipping costs to a third party]. This field must be used in conjunction with the `bill_to_country_code`, `bill_to_party`, and `bill_to_postal_code` fields.

Default null

Example: "123456789"

advanced\_options.​bill\_to\_country\_code*string or null**(country\_code)**= 2 characters*

A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)

Default null

Example: "CA"

advanced\_options.​bill\_to\_party*string or null**(bill\_to\_party)*

The possible bill to party values

Default null

Enum"recipient""third\_party"

Example: "third\_party"

advanced\_options.​bill\_to\_postal\_code*string or null*

The postal code of the third-party that is responsible for shipping costs.

Default null

Example: "28005"

advanced\_options.​contains\_alcohol*boolean*

Indicates that the shipment contains alcohol.

Default false

Example: true

advanced\_options.​delivered\_duty\_paid*boolean*

Indicates that the shipper is paying the international delivery duties for this shipment. This option is supported by UPS, FedEx, and DHL Express.

Default false

Example: true

advanced\_options.​dry\_ice*boolean*

Indicates if the shipment contain dry ice

Default false

Example: true

advanced\_options.​dry\_ice\_weight*object or null**(weight)*

The weight of a package

+Show 2 properties

advanced\_options.​non\_machinable*boolean*

Indicates that the package cannot be processed automatically because it is too large or irregularly shaped. This is primarily for USPS shipments. See [Section 1.2 of the USPS parcel standards](https://pe.usps.com/text/dmm300/101.htm#ep1047495) for details.

Default false

Example: true

advanced\_options.​saturday\_delivery*boolean*

Enables Saturday delivery, if supported by the carrier.

Default false

Example: true

advanced\_options.​fedex\_freight*object*

Provide details for the Fedex freight service

+Show 2 properties

advanced\_options.​use\_ups\_ground\_freight\_pricing*boolean or null*

Whether to use [UPS Ground Freight pricing] If enabled, then a `freight_class` must also be specified.

Default null

Example: true

advanced\_options.​freight\_class*string or null*

The National Motor Freight Traffic Association [freight class](http://www.nmfta.org/pages/nmfc?AspxAutoDetectCookieSupport=1), such as "77.5", "110", or "250".

Default null

Example: "77.5"

advanced\_options.​custom\_field1*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 1"

advanced\_options.​custom\_field2*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 2"

advanced\_options.​custom\_field3*string or null**<= 100 characters*

An arbitrary field that can be used to store information about the shipment.

Default null

Example: "custom field 3"

advanced\_options.​origin\_type*string or null**(origin\_type)*

Indicates if the package will be picked up or dropped off by the carrier

Default null

Enum"pickup""drop\_off"

advanced\_options.​additional\_handling*boolean or null*

Indicate to the carrier that this shipment requires additional handling.

Default null

Example: true

advanced\_options.​shipper\_release*boolean or null*

Default null

Example: true

advanced\_options.​collect\_on\_delivery*object**(collect\_on\_delivery)*

Defer payment until package is delivered, instead of when it is ordered.

+Show 2 properties

advanced\_options.​third\_party\_consignee*boolean*

Third Party Consignee option is a value-added service that allows the shipper to supply goods without commercial invoices being attached

Default false

Example: true

advanced\_options.​dangerous\_goods*boolean*

Indicates if the Dangerous goods are present in the shipment

Default false

Example: true

advanced\_options.​dangerous\_goods\_contact*object*

Contact information for Dangerous goods

+Show 2 properties

advanced\_options.​windsor\_framework\_details*object*

The Windsor framework is a new regulation in the UK that simplifies customs procedures for goods moved from the UK mainland to Northern Ireland.

+Show 2 properties

advanced\_options.​ancillary\_endorsements\_option*string or null*

Ancillary endorsements option for the shipment

Example: "forward"

advanced\_options.​return\_pickup\_attempts*integer or null*

Number of return pickup attempts

Example: 3

advanced\_options.​own\_document\_upload*boolean*

Indicates if own document upload is enabled

Default false

Example: false

advanced\_options.​limited\_quantity*boolean*

Indicates if the shipment contains limited quantities

Default false

Example: false

advanced\_options.​event\_notification*boolean*

Indicates if event notifications are enabled

Default false

Example: false

insurance\_provider*string**(insurance\_provider)*required

The possible insurance provider values

Default "none"

Enum"none""shipsurance""carrier""third\_party"

tags*Array of objects**(tag)**>= 0 items*required

Arbitrary tags associated with this shipment. Tags can be used to categorize shipments, and shipments can be queried by their tags. Note: Tags require object structure with name property, not simple strings.

Default []

-

tags[].​name*string**non-empty*required

The tag name.

Example: "Fragile"

order\_source\_code*string**(order\_source\_name)*

The order sources that are supported by ShipStation

Enum"amazon\_ca""amazon\_us""brightpearl""channel\_advisor""cratejoy""ebay""etsy""jane""groupon\_goods""magento"+10 more

packages*Array of objects**(package)**non-empty*required

The packages in the shipment.

> **Note:** Some carriers only allow one package per shipment. If you attempt to create a multi-package shipment for a carrier that doesn't allow it, an error will be returned.

-

packages[].​shipment\_package\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-only

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

packages[].​package\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

packages[].​package\_code*string**(package\_code)**[ 1 .. 50 ] characters*^[a-z0-9]+(\_[a-z0-9]+)\*$

A [package type] , such as `thick_envelope`, `small_flat_rate_box`, `large_package`, etc. Use the code `package` for custom or unknown package types.

Example: "small\_flat\_rate\_box"

packages[].​package\_name*string*

The name of the of the [package type]

Example: "Flat Rate Envelope"

packages[].​weight*object**(weight)*required

The weight of a package

-

packages[].​weight.​value*number**> 0*required

The weight, in the specified unit

Example: 23

packages[].​weight.​unit*string**(weight\_unit)*required

The possible weight unit values

Enum"pound""ounce""gram""kilogram"

packages[].​dimensions*object**(dimensions)*

The dimensions of a package

+Show 4 properties

packages[].​insured\_value*object**(monetary\_value)*

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

Default [{"currency":"usd","amount":0}]

+Show 2 properties

packages[].​label\_messages*object**(label\_messages)*

Custom messages to print on the shipping label for the package. These are typically used to print invoice numbers, product numbers, or other internal reference numbers. Not all carriers support label messages. The number of lines and the maximum length of each line also varies by carrier.

| Carrier | Max lines | Max line length |
| --- | --- | --- |
| USPS (Stamps.com) | 3 | 60 |
| FedEx | 3 | 35 for the first line. 30 for additional lines. |
| UPS | 2 | 35 |
| OnTrac | 2 | 25 |

+Show 3 properties

packages[].​external\_package\_id*string**non-empty*

An external package id.

Example: "se-1234545"

packages[].​tracking\_number*string**(tracking\_number)**non-empty*read-only

A tracking number for a package. The format depends on the carrier.

Example: "1Z932R800392060079"

packages[].​content\_description*string or null**[ 1 .. 35 ] characters*

A short description of the package content. Required for shipments moving to, from, and through Mexico.

Example: "Hand knitted wool socks"

packages[].​products*Array of objects**(products)**>= 0 items*

Details about products inside packages (Information provided would be used on custom documentation)

Default []

+Show 13 array properties

total\_weight*object**(weight)*read-onlyrequired

The weight of a package

-

total\_weight.​value*number**> 0*required

The weight, in the specified unit

Example: 3

total\_weight.​unit*string**(weight\_unit)*required

The possible weight unit values

Enum"pound""ounce""gram""kilogram"

Example: "pound"

comparison\_rate\_type*string or null*

Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only supported for UPS and USPS.

Example: "retail"

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "shipment_id": "se-28529731",
  "carrier_id": "se-1234567",
  "service_code": "se_1234567",
  "requested_shipment_service": "usps_priority_mail",
  "shipping_rule_id": "se-1234",
  "external_order_id": "1232434",
  "hold_until_date": "2025-01-15T00:00:00.000Z",
  "ship_by_date": "2025-01-15T00:00:00.000Z",
  "retail_rate": {
    "currency": "string",
    "amount": 12
  },
  "store_id": "se-12345",
  "items": [],
  "notes_from_buyer": "Please handle with care",
  "notes_for_gift": "Happy Birthday!",
  "is_gift": true,
  "assigned_user": "user@example.com",
  "amount_paid": {
    "currency": "string",
    "amount": 12
  },
  "shipping_paid": {
    "currency": "string",
    "amount": 12
  },
  "tax_paid": {
    "currency": "string",
    "amount": 12
  },
  "zone": 1,
  "display_scheme": "label",
  "tax_identifiers": [
    { … }
  ],
  "external_shipment_id": "1234556",
  "shipment_number": "10001",
  "ship_date": "2018-09-23",
  "created_at": "2018-09-23T15:00:00.000Z",
  "modified_at": "2018-09-23T15:00:00.000Z",
  "shipment_status": "pending",
  "ship_to": {
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
    "address_residential_indicator": "yes",
    "instructions": "any instruction",
    "geolocation": [ … ]
  },
  "ship_from": {
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
    "address_residential_indicator": "yes",
    "instructions": "any instructions"
  },
  "warehouse_id": null,
  "return_to": {
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
    "address_residential_indicator": "yes",
    "instructions": "any instructions"
  },
  "is_return": true,
  "confirmation": "none",
  "customs": null,
  "advanced_options": {
    "bill_to_account": "123456789",
    "bill_to_country_code": "US",
    "bill_to_party": "third_party",
    "bill_to_postal_code": "28005",
    "contains_alcohol": true,
    "delivered_duty_paid": true,
    "dry_ice": true,
    "dry_ice_weight": { … },
    "non_machinable": true,
    "saturday_delivery": true,
    "fedex_freight": { … },
    "use_ups_ground_freight_pricing": true,
    "freight_class": "77.5",
    "custom_field1": "custom field 1",
    "custom_field2": "custom field 2",
    "custom_field3": "custom field 3",
    "origin_type": null,
    "additional_handling": true,
    "shipper_release": true,
    "collect_on_delivery": { … },
    "third_party_consignee": true,
    "dangerous_goods": true,
    "dangerous_goods_contact": { … },
    "windsor_framework_details": { … },
    "ancillary_endorsements_option": "forward",
    "return_pickup_attempts": 3,
    "own_document_upload": false,
    "limited_quantity": false,
    "event_notification": false
  },
  "insurance_provider": "none",
  "tags": [],
  "order_source_code": "amazon_ca",
  "packages": [
    { … }
  ],
  "total_weight": {
    "value": 3,
    "unit": "pound"
  },
  "comparison_rate_type": "retail"
}
```

#### Was this helpful?

Cancel a shipment
-----------------

#### Request

Mark a shipment cancelled, if it is no longer needed or being used by your organized. Any label associated with the shipment needs to be voided first An example use case would be if a batch label creation job is going to run at a set time and only queries `pending` shipments. Marking a shipment as cancelled would remove it from this process

Security:
api\_keys

Path

shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Shipment ID

Example: se-28529731

put

/v2/shipments/{shipment\_id}/cancel

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/shipments/{shipment\_id}/cancel
* Production https://api.shipstation.com/v2/shipments/{shipment\_id}/cancel

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
curl -i -X PUT \
  'https://docs.shipstation.com/_mock/openapi/v2/shipments/{shipment_id}/cancel' \
  -H 'api-key: YOUR_API_KEY_HERE'
```

Try it

#### Responses

1. 204
2. 400
3. 404
4. 500

The request was successful.

Body

text/plain

* text/plain
* application/json

*string**(empty\_response\_body)**<= 0 characters*

Response

1. 204
2. 400
3. 404
4. 500

text/plainapplication/jsontext/plain

```
No response example
```

#### Was this helpful?

Get shipment rates
------------------

#### Request

Get Rates for the shipment information associated with the shipment ID

Security:
api\_keys

Path

shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Shipment ID

Example: se-28529731

Query

created\_at\_start*string**(date-time)*

Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)

Example: created\_at\_start=2019-03-12T19:24:13.657Z

get

/v2/shipments/{shipment\_id}/rates

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/shipments/{shipment\_id}/rates
* Production https://api.shipstation.com/v2/shipments/{shipment\_id}/rates

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
  'https://docs.shipstation.com/_mock/openapi/v2/shipments/{shipment_id}/rates?created_at_start=2019-08-24T14%3A15%3A22Z' \
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

rates*Array of objects**(rate)*read-onlyrequired

An array of shipment rates

-

rates[].​rate\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

rates[].​rate\_type*string**(rate\_type)*read-onlyrequired

The possible rate type values

Enum"check""shipment"

rates[].​carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

rates[].​shipping\_amount*object**(monetary\_value)*read-onlyrequired

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

-

rates[].​shipping\_amount.​currency*string**(currency)*required

The currencies that are supported by ShipStation are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html

rates[].​shipping\_amount.​amount*number**>= 0*required

The monetary amount, in the specified currency.

Example: 12

rates[].​insurance\_amount*object**(monetary\_value)*read-onlyrequired

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

-

rates[].​insurance\_amount.​currency*string**(currency)*required

The currencies that are supported by ShipStation are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html

rates[].​insurance\_amount.​amount*number**>= 0*required

The monetary amount, in the specified currency.

Example: 12

rates[].​confirmation\_amount*object**(monetary\_value)*read-onlyrequired

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

-

rates[].​confirmation\_amount.​currency*string**(currency)*required

The currencies that are supported by ShipStation are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html

rates[].​confirmation\_amount.​amount*number**>= 0*required

The monetary amount, in the specified currency.

Example: 12

rates[].​other\_amount*object**(monetary\_value)*read-onlyrequired

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

-

rates[].​other\_amount.​currency*string**(currency)*required

The currencies that are supported by ShipStation are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html

rates[].​other\_amount.​amount*number**>= 0*required

The monetary amount, in the specified currency.

Example: 12

rates[].​requested\_comparison\_amount*object**(monetary\_value)*read-only

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

rates[].​tax\_amount*object**(monetary\_value)*read-only

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

rates[].​zone*integer or null**(int32)**>= 0*read-onlyrequired

Certain carriers base [their rates](https://blog.stamps.com/2017/09/08/usps-postal-zones/) off of custom zones that vary depending upon the ship\_to and ship\_from location

Example: 6

rates[].​package\_type*string or null**non-empty*read-onlyrequired

package type that this rate was estimated for

Example: "package"

rates[].​delivery\_days*integer**(int32)**>= 1*read-only

The number of days estimated for delivery, this will show the *actual* delivery time if for example, the package gets shipped on a Friday

Example: 5

rates[].​guaranteed\_service*boolean*read-onlyrequired

Indicates if the rate is guaranteed.

Example: true

rates[].​estimated\_delivery\_date*string**(date-time)**(date)*^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?...Show patternread-only

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date, but not a specific time. The value *may* contain a time component, but it will be set to `00:00:00` UTC by ShipStation .

Example: "2018-09-23"

rates[].​carrier\_delivery\_days*string**non-empty*read-only

The carrier delivery days

Example: "22"

rates[].​ship\_date*string**(date-time)**non-empty*read-only

ship date

Example: "10/22/2024z00:00"

rates[].​negotiated\_rate*boolean*read-onlyrequired

Indicates if the rates been negotiated

Example: true

rates[].​service\_type*string**non-empty*read-onlyrequired

service type

Example: "next\_day"

rates[].​service\_code*string**non-empty*read-onlyrequired

service code for the rate

Example: "usps\_priority\_mail\_express"

rates[].​trackable*boolean*read-onlyrequired

Indicates if rate is trackable

Example: true

rates[].​carrier\_code*string**non-empty*read-onlyrequired

carrier code

Example: "stamps\_com"

rates[].​carrier\_nickname*string**non-empty*read-onlyrequired

carrier nickname

Example: "Free"

rates[].​carrier\_friendly\_name*string**non-empty*read-onlyrequired

carrier friendly name

Example: "free"

rates[].​validation\_status*string**(validation\_status)*read-onlyrequired

The possible validation status values

Enum"valid""invalid""has\_warnings""unknown"

rates[].​warning\_messages*Array of strings**>= 0 items*read-onlyrequired

The warning messages

rates[].​error\_messages*Array of strings**>= 0 items*read-onlyrequired

The error messages

invalid\_rates*Array of objects**(rate)*read-onlyrequired

An array of invalid shipment rates

Default []

-

invalid\_rates[].​rate\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

invalid\_rates[].​rate\_type*string**(rate\_type)*read-onlyrequired

The possible rate type values

Enum"check""shipment"

invalid\_rates[].​carrier\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

invalid\_rates[].​shipping\_amount*object**(monetary\_value)*read-onlyrequired

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

-

invalid\_rates[].​shipping\_amount.​currency*string**(currency)*required

The currencies that are supported by ShipStation are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html

invalid\_rates[].​shipping\_amount.​amount*number**>= 0*required

The monetary amount, in the specified currency.

Example: 12

invalid\_rates[].​insurance\_amount*object**(monetary\_value)*read-onlyrequired

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

-

invalid\_rates[].​insurance\_amount.​currency*string**(currency)*required

The currencies that are supported by ShipStation are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html

invalid\_rates[].​insurance\_amount.​amount*number**>= 0*required

The monetary amount, in the specified currency.

Example: 12

invalid\_rates[].​confirmation\_amount*object**(monetary\_value)*read-onlyrequired

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

-

invalid\_rates[].​confirmation\_amount.​currency*string**(currency)*required

The currencies that are supported by ShipStation are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html

invalid\_rates[].​confirmation\_amount.​amount*number**>= 0*required

The monetary amount, in the specified currency.

Example: 12

invalid\_rates[].​other\_amount*object**(monetary\_value)*read-onlyrequired

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

-

invalid\_rates[].​other\_amount.​currency*string**(currency)*required

The currencies that are supported by ShipStation are the ones that specified by ISO 4217: https://www.iso.org/iso-4217-currency-codes.html

invalid\_rates[].​other\_amount.​amount*number**>= 0*required

The monetary amount, in the specified currency.

Example: 12

invalid\_rates[].​requested\_comparison\_amount*object**(monetary\_value)*read-only

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

invalid\_rates[].​tax\_amount*object**(monetary\_value)*read-only

A monetary value, such as the price of a shipping label, the insured value of a package, or an account balance.

+Show 2 properties

invalid\_rates[].​zone*integer or null**(int32)**>= 0*read-onlyrequired

Certain carriers base [their rates](https://blog.stamps.com/2017/09/08/usps-postal-zones/) off of custom zones that vary depending upon the ship\_to and ship\_from location

Example: 6

invalid\_rates[].​package\_type*string or null**non-empty*read-onlyrequired

package type that this rate was estimated for

Example: "package"

invalid\_rates[].​delivery\_days*integer**(int32)**>= 1*read-only

The number of days estimated for delivery, this will show the *actual* delivery time if for example, the package gets shipped on a Friday

Example: 5

invalid\_rates[].​guaranteed\_service*boolean*read-onlyrequired

Indicates if the rate is guaranteed.

Example: true

invalid\_rates[].​estimated\_delivery\_date*string**(date-time)**(date)*^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?...Show patternread-only

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string that represents a date, but not a specific time. The value *may* contain a time component, but it will be set to `00:00:00` UTC by ShipStation .

Example: "2018-09-23"

invalid\_rates[].​carrier\_delivery\_days*string**non-empty*read-only

The carrier delivery days

Example: "22"

invalid\_rates[].​ship\_date*string**(date-time)**non-empty*read-only

ship date

Example: "10/22/2024z00:00"

invalid\_rates[].​negotiated\_rate*boolean*read-onlyrequired

Indicates if the rates been negotiated

Example: true

invalid\_rates[].​service\_type*string**non-empty*read-onlyrequired

service type

Example: "next\_day"

invalid\_rates[].​service\_code*string**non-empty*read-onlyrequired

service code for the rate

Example: "usps\_priority\_mail\_express"

invalid\_rates[].​trackable*boolean*read-onlyrequired

Indicates if rate is trackable

Example: true

invalid\_rates[].​carrier\_code*string**non-empty*read-onlyrequired

carrier code

Example: "stamps\_com"

invalid\_rates[].​carrier\_nickname*string**non-empty*read-onlyrequired

carrier nickname

Example: "Free"

invalid\_rates[].​carrier\_friendly\_name*string**non-empty*read-onlyrequired

carrier friendly name

Example: "free"

invalid\_rates[].​validation\_status*string**(validation\_status)*read-onlyrequired

The possible validation status values

Enum"valid""invalid""has\_warnings""unknown"

invalid\_rates[].​warning\_messages*Array of strings**>= 0 items*read-onlyrequired

The warning messages

invalid\_rates[].​error\_messages*Array of strings**>= 0 items*read-onlyrequired

The error messages

rate\_request\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

created\_at*string**(date-time)**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

status*string**(rate\_response\_status)*read-onlyrequired

The possible rate response status values

Enum"working""completed""partial""error"

errors*Array of objects**(error)*required

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
2. 400
3. 404
4. 500

application/json

```
{
  "rates": [
    { … }
  ],
  "invalid_rates": [],
  "rate_request_id": "se-28529731",
  "shipment_id": "se-28529731",
  "created_at": "se-28529731",
  "status": "working",
  "errors": [
    { … }
  ]
}
```

#### Was this helpful?

Add tag to shipment
-------------------

#### Request

Add a tag to the shipment object

Security:
api\_keys

Path

shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Shipment ID

Example: se-28529731

tag\_name*string**(tag\_name)**non-empty*required

Tags are arbitrary strings that you can use to categorize shipments. For example, you may want to use tags to distinguish between domestic and international shipments, or between insured and uninsured shipments. Or maybe you want to create a tag for each of your customers so you can easily retrieve every shipment for a customer.

Example: Fragile

post

/v2/shipments/{shipment\_id}/tags/{tag\_name}

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/shipments/{shipment\_id}/tags/{tag\_name}
* Production https://api.shipstation.com/v2/shipments/{shipment\_id}/tags/{tag\_name}

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
curl -i -X POST \
  'https://docs.shipstation.com/_mock/openapi/v2/shipments/{shipment_id}/tags/{tag_name}' \
  -H 'api-key: YOUR_API_KEY_HERE'
```

Try it

#### Responses

1. 200
2. 400
3. 404
4. 500

Expand all

The requested object creation was a success.

Bodyapplication/json

shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$read-onlyrequired

A string that uniquely identifies a ShipStation resource, such as a carrier, label, shipment, etc.

Example: "se-28529731"

tag*object**(tag)*read-onlyrequired

Tags are arbitrary strings that you can use to categorize shipments. For example, you may want to use tags to distinguish between domestic and international shipments, or between insured and uninsured shipments. Or maybe you want to create a tag for each of your customers so you can easily retrieve every shipment for a customer.

-

tag.​name*string**non-empty*required

The tag name.

Example: "Fragile"

Response

1. 200
2. 400
3. 404
4. 500

application/json

```
{
  "shipment_id": "se-28529731",
  "tag": {
    "name": "Fragile"
  }
}
```

#### Was this helpful?

Remove tag from shipment
------------------------

#### Request

Remove an existing tag from the Shipment object

Security:
api\_keys

Path

shipment\_id*string**(se\_id)**[ 1 .. 25 ] characters*^se(-[a-z0-9]+)+$required

Shipment ID

Example: se-28529731

tag\_name*string**(tag\_name)**non-empty*required

Tags are arbitrary strings that you can use to categorize shipments. For example, you may want to use tags to distinguish between domestic and international shipments, or between insured and uninsured shipments. Or maybe you want to create a tag for each of your customers so you can easily retrieve every shipment for a customer.

Example: Fragile

delete

/v2/shipments/{shipment\_id}/tags/{tag\_name}

* Mock server https://docs.shipstation.com/\_mock/openapi/v2/shipments/{shipment\_id}/tags/{tag\_name}
* Production https://api.shipstation.com/v2/shipments/{shipment\_id}/tags/{tag\_name}

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
curl -i -X DELETE \
  'https://docs.shipstation.com/_mock/openapi/v2/shipments/{shipment_id}/tags/{tag_name}' \
  -H 'api-key: YOUR_API_KEY_HERE'
```

Try it

#### Responses

1. 204
2. 400
3. 404
4. 500

The request was successful.

Body

text/plain

* text/plain
* application/json

*string**(empty\_response\_body)**<= 0 characters*

Response

1. 204
2. 400
3. 404
4. 500

text/plainapplication/jsontext/plain

```
No response example
```

#### Was this helpful?

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

* [Terms](/openapi/shipments)
* [Privacy](/openapi/shipments)
* [Disclosures](/openapi/shipments)
* [Cookie Settings](/openapi/shipments)