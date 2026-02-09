# Source: https://docs.vespa.ai/en/modules/e-commerce/saved-search.html.md

# Saved search notifications

 

Vespa for e-commerce includes a module for storing queries in Vespa ("searches") and issuing notifications when a new or updated document matches any saved searches. A typical use case in e-commerce is letting users store queries on products using filters on keywords, price, location etc. and sending them a notification when a new product matches their query.

## Overview

The ecommerce-saved-search module supports:

- **Storing predicate queries** - Saved searches contain arbitrary boolean expressions over a set of string attributes and numerical ranges. See [Predicate Fields](../../schemas/predicate-fields.html).
- **Schema wiring configuration** - Wirings between the saved search attributes and the document fields can be configured by the application.
- **Webhook notifications** - A match between a new or updated document and a set of saved searches can be sent to a HTTP endpoint in a JSON format.
- **Separate document processing** - Separate routing to the saved search component allows processing of saved searches without disrupting normal feed operations.

## Quick Start

A minimal setup for demonstrating saved search notification capabilities is given in this section. We will develop a small shopping use-case example with a few saved search attributes.

### Define Schemas

Create two schemas: one for products and one for storing the saved searches.

#### Product Schema

We create a minimal document type representing a product for sale. Each of the three fields will correspond to a searchable attribute in the saved searches.

```
```
schema product {
    document product {
        
        # Other fields

        field price type int {
            indexing: attribute
        }

        field category type string {
            indexing: attribute
        }

        field condition type string {
            indexing: attribute
        }
    }

    # rank-profiles etc.
}
```
```

#### Saved Search Schema

The predicate field will contain the entire search expression used to match products.

```
```
schema saved_search {
    document saved_search {
        field filters type predicate {
            indexing: attribute
            index {
                arity: 2 # Mandatory
                # Range of values the expressions are expected to operate on. 
                # Better performance if these are smaller
                lower-bound: 3
                upper-bound: 500

                dense-posting-list-threshold: 0.25
            }
        }
    }
}
```
```

### Configure Services

A minimal `services.xml` configuring the saved search component can look like this:

```
```
<services version="1.0">
    <container id="default" version="1.0">
        <search />
        <document-api />

        <document-processing>
            <chain id="notification">
                <documentprocessor id="ai.vespa.ecommerce.savedsearch.SavedSearchDocumentProcessor" 
                                   bundle="ecommerce-saved-search" />
                <config name="ai.vespa.ecommerce.savedsearch.schema-wiring">
                    <notification>
                        <kind>WEBHOOK</kind>
                        <webhook>
                            <URL>http://localhost:8000/notification</URL>
                        </webhook>
                    </notification>

                    <itemDocumentType>product</itemDocumentType>
                    <savedSearchDocumentType>saved_search</savedSearchDocumentType>
                    <predicateFieldName>filters</predicateFieldName>
                    <savedSearchNumHits>10</savedSearchNumHits>

                    <regularAttributes>
                        <item>
                            <predicateName>category</predicateName>
                            <fieldPath>category</fieldPath>
                            <required>true</required>
                        </item>
                        <item>
                            <predicateName>condition</predicateName>
                            <fieldPath>condition</fieldPath>
                            <required>false</required>
                        </item>
                    </regularAttributes>
                    <rangeAttributes>
                        <item>
                            <predicateName>price</predicateName>
                            <fieldPath>price</fieldPath>
                            <required>true</required>
                        </item>
                    </rangeAttributes>
                </config>
            </chain>
        </document-processing>
    </container>

    <content version="1.0" id="content">
        <min-redundancy>2</min-redundancy>
        <documents>
            <document type="saved_search" mode="index" />
            <document type="product" mode="index" />

            <document-processing />
        </documents>
    </content>

    <routing version="1.0">
        <routingtable protocol="document">
            <route name="notification-route" hops="forkhop" />
            <hop name="forkhop" selector="[DocumentRouteSelector]">
                <recipient session="default/chain.notification" />
                <recipient session="content" />
            </hop>
        </routingtable>
    </routing>
</services>
```
```

### Feed Data

#### Feed saved searches

To test the functionality, feed two saved search documents:

```
```
[
  {"put": "id:saved_search:saved_search::search1", "fields": {
    "filters": "price in [20..100] and category in [Sports, Books]"
  }},
  {"put": "id:saved_search:saved_search::search2", "fields": {
    "filters": "price in [200..487] and category in [Electronics]"
  }}
]
```
```

#### Feed a product to the notification route

Assume a new product is available, with the following schema:

```
```
{"put": "id:saved_search:product::product1", "fields":{"category": "Sports", "price": 50}}
```
```

To enable notifications when feeding this product, feed it to the `notification-route`:

```
```
$ vespa feed --route notification-route product.jsonl
```
```

Assuming everything is set up correctly, it should match `id:saved_search:saved_search::search1` but not `search2`. If a server is receiving requests at the endpoint specified in the `URL` parameter of the `webhook` configuration, you should see a request with a JSON body representing the matched pair.

 **Warning:** The `SavedSearchDocumentProcessor` acts as a **sink** for incoming documents. That is, `Put` and `Update` operations sent to that document processor will not propagate down to the content nodes, effectively discarding the operations. This is why a `routingtable` is specified in the example - documents going to the route `notification-route` will "fork", with one path going to the content cluster and one path to the saved search component.

## Notification kinds

### Webhook

The webhook notification kind will send a request to a specified URL for each document that matches a set of saved searches. It requires an external application to provide the handling of such requests.

If the configuration parameter `notification.kind == WEBHOOK`, all configuration parameters prefixed with `notification.webhook` will take effect. The requests from the saved search application will be `POST`-requests with a JSON body:

```
```
{
  "id": "<product-id>",
  "timestamp": "<ISO-8601-timestamp>",
  "matched_documents": [
    "<saved-search-id-1>",
    "<saved-search-id-2>",
    ...
  ]
}
```
```

#### Security

In most cases, the Webhook endpoint handling the notifications is (and should be) protected in some way. The currently supported way to send authorized requests to the webhook endpoint is by combining the [Vespa secret store](../../security/secret-store.html) with the `notification.webhook.headers[].secret` config parameter. Assume we want to send notifications to `https://my.webhook.com/notification`, and that the api requires the following header:

```
```
Authorization: Bearer TOKEN
```
```

to be present in all requests. To enable our application to use this, first create the secret in Vespa Cloud and let it contain the **full** value of the header: `Bearer TOKEN`, replacing `TOKEN` with the actual token.

Next, add the secret to the application in `services.xml`:

```
```
<container>
    ...
    <secrets>
        <myApiToken vault="my-vault" name="my-token-name" />
    </secrets>
```
```

Finally, configure the `SavedSearchDocumentProcessor` to add a header with this secret value to all notification requests:

```
```
...
    <documentprocessor id="ai.vespa.ecommerce.savedsearch.SavedSearchDocumentProcessor" 
                       bundle="ecommerce-saved-search" />
    <config name="ai.vespa.ecommerce.savedsearch.schema-wiring">
        <notification>
            <kind>WEBHOOK</kind>
            <webhook>
            <headers>
                <item>
                    <key>Authorization</key>
                    <!-- Value of secret will be placed in the value field of the HTTP header. -->
                    <secret>myApiToken</secret>
                </item>
            </headers>
            </webhook>
        </notification>
    </config>
</container>
```
```

### Vespa Schema

For a simpler way to test saved search notification, a method for storing the notifications within the Vespa application is provided. This method represents each notification between a pair of a product and a saved search using a dedicated Vespa document type. It is recommended for testing purposes only.

If the configuration parameter `notification.kind == VESPA_SCHEMA`, all configuration parameters prefixed with `notification.vespaSchema` will take effect. A minimal working example of this notification kind is given below.

#### Notification example

Define a document type for storing the notifications, for example `notification.sd`:

```
```
schema notification {
    document notification {
        field product_id type string {
            indexing: attribute | summary
        }

        field saved_search_id type string {
            indexing: attribute | summary
        }

        field timestamp type long {
            indexing: attribute | summary
        }
    }
}
```
```

Add the document type to the application:

```
```
<content>
    <documents>
        ...
        <document type="notification" mode="index" />
    </documents>
</content>
```
```

Configure the schema wirings of the `SavedSearchDocumentProcessor`:

```
```
<container>
    <documentprocessor id="ai.vespa.ecommerce.savedsearch.SavedSearchDocumentProcessor" 
                       bundle="ecommerce-saved-search" />
    <config name="ai.vespa.ecommerce.savedsearch.schema-wiring">
        <notification>
            <kind>VESPA_SCHEMA</kind>
            <vespaSchema>
                <documentType>notification</documentType>
                <namespace>saved_search</namespace>
                <fieldPathProductId>product_id</fieldPathProductId>
                <fieldPathSavedSearchId>saved_search_id</fieldPathSavedSearchId>
                <fieldPathTimestamp>timestamp</fieldPathTimestamp>
            </vespaSchema>
        </notification>
    </config>
</container>
```
```
Now notifications can be inspected by using `vespa visit` or `vespa query` with the appropriate parameters.
## Configuration reference

This section describes the possible [configuration parameters](../../applications/configuring-components.html) used by the document processor.

| Parameter | Description | Type | Default value |
| --- | --- | --- | --- |
| `notification.kind` | Method to use for sending notifications. | `enum {WEBHOOK, DUMMY, VESPA_SCHEMA}` | `DUMMY` |
| `notification.webhook.URL` | URL to send notification requests. | `string` | |
| `notification.webhook.connectionPoolSize` | Number of HTTP client threads to use in the container cluster. | `int` | `20` |
| `notification.webhook.headers[].key` | Key of a header to add to all webhook requests. | `string` | |
| `notification.webhook.headers[].value` | Value of a header to add to all webhook requests. | `string` | |
| `notification.webhook.headers[].secret` | Use a secret from Vespa secret store instead of the value provided in `.value`. The value provided here should match the name of a secret specified with a `secrets` tag in `services.xml`. | `string` | |
| `notification.vespaSchema.documentType` | Name of the Vespa document type to use for storing notifications. This document type has to be defined in the application. | `string` | saved\_search\_notification |
| `notification.vespaSchema.namespace` | Namespace to use for creating document ids for the notification documents. | `string` | saved\_search |
| `notification.vespaSchema.fieldPathProductId` | Fieldpath for storing the product id in the notification documents. | `string` | product\_id |
| `notification.vespaSchema.fieldPathSavedSearchId` | Fieldpath for storing saved search id in the notification documents. | `string` | saved\_search\_id |
| `notification.vespaSchema.fieldPathTimestamp` | Fieldpath for storing timestamps in the notification documents. | `string` | timestamp |
| `itemDocumentType` | The name of the document type that can trigger notifications, e.g. `product`. | `string` | product |
| `savedSearchDocumentType` | The name of the document type storing saved searches, e.g. `saved_search`. | `string` | saved\_search |
| `predicateFieldName` | The name of the field in `savedSearchDocumentType` storing the predicate query. | `string` | filters |
| `savedSearchNumHits` | Maximum number of saved searches to issue a notification for one product. | `int` | 100 |
| `regularAttributes[].predicateName` | The name of a regular (string) attribute to be used in the saved search predicate field. | `string` | |
| `regularAttributes[].fieldPath` | The field in the `itemDocumentType` to be matched with this attribute. This field should be of type `string`. | `string` | |
| `regularAttributes[].required` | Whether documents are required to specify this attribute. | `bool` | `false` |
| `rangeAttributes[].predicateName` | The name of a numerical range attribute to be used in the saved search predicate field. | `string` | |
| `rangeAttributes[].fieldPath` | The field in the `itemDocumentType` to be matched with this attribute. This field should be of a numeric type, e.g. `int`. | `string` | |
| `rangeAttributes[].required` | Whether documents are required to specify this attribute. | `bool` | `false` |

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Define Schemas](#define-schemas)
- [Configure Services](#configure-services)
- [Feed Data](#feeding)
- [Notification kinds](#notification-kinds)
- [Webhook](#notification-kind-webhook)
- [Vespa Schema](#notification-kind-vespa)
- [Configuration reference](#configuration)

