# Source: https://developers.activecampaign.com/reference/browse-session-apis.md

# Browse Session APIs

For more details about how browse sessions and browse abandonments are processed, see: [Browse Abandonment Overview](https://developers.activecampaign.com/reference/browse-abandonment)

# Queries

## getBrowseSessionByCustomObjectIdentifier

Fetches the full browse session based on the `id` field of the Browse Abandonment Custom Object associated with this session. This can only be used for sessions in the `ABANDONED` state that have generated a Browse Abandonment Custom Object.

**Return Type**: [BrowseSession](https://developers.activecampaign.com/reference/browse-session-apis#browse-session-and-browsesessioninput)

**Arguments for `getBrowseSessionByCustomObjectIdentifier`**

| Name                                                                                                                   | Description                                                                                         |
| :--------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| customObjectIdentifier(`string`) **Required**                                                                          | An identifier matching the `id` of a Browse Abandonment Custom Object matching this Browse Session. |
| filter([BrowseProductFilter](https://developers.activecampaign.com/reference/browse-session-apis#browseproductfilter)) | A filter to sort or filter browse products within the fetched session.                              |

### getBrowseSessionByCustomObjectIdentifier Example Payload

#### Request

```Text GraphQL
{
   getBrowseSessionByCustomObjectIdentifier(
      customObjectIdentifier: "12345",
      filter: {
         mostRecentBrowsedAt: {
            filterOperator: GT
            value: "2021-12-01T10:48:23Z"
            sort: DESC
         }
     }
   )
   {
      legacyConnectionId
      email
      toAbandonDate
      normalizedStatus
      products {
         priceAmount
         baseProductName
         storePrimaryId
         storeBaseProductId
         numberOfTimesViewed
         mostRecentBrowsedAt
      }
   }
}
```

#### Response

```Text json
{
    "data": {
        "getBrowseSessionByCustomObjectIdentifier": {
            "legacyConnectionId": 69,
            "email": "whatever@example.com",
            "toAbandonDate": "2023-01-14T10:48:23Z",
            "normalizedStatus": "ABANDONED",
            "products": [
                {
                    "priceAmount": 25.00,
                    "baseProductName": "Deadly Butter Knife",
                    "storePrimaryId": "40827825750075",
                    "storeBaseProductId": "7000355569723",
                    "numberOfTimesViewed": 1,
                    "mostRecentBrowsedAt": "2023-12-01T10:48:23Z"
                }
            ]
        }
    }
}
```

## searchBrowseSession

**Return Type**: [BrowseSession\[\]](https://developers.activecampaign.com/reference/browse-session-apis#browse-session-and-browsesessioninput)

**Arguments for `searchBrowseSession`**

| Name                                                                                                                                 | Description                                                            |
| :----------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| filter([BrowseSessionSearchRequest](https://developers.activecampaign.com/reference/browse-session-apis#browsesessionsearchrequest)) | A filter to sort or filter browse products within the fetched session. |

### searchBrowseSession Example Payload

```Text GraphQL
{
    searchBrowseSession(filter: 
       {
           legacyConnectionId: 69
           normalizedStatus: ACTIVE
           email: "whatever@example.com"
       }
    )
    {
        legacyConnectionId
        email
        normalizedStatus
        toAbandonDate
        products {
            storePrimaryId
            browseTimeSeconds
            numberOfTimesViewed
        }
    }
}
```

### searchBrowseSession Example Response

```Text json
{
    "data": {
        "searchBrowseSession": [
            {
                "legacyConnectionId": 70,
                "email": "whatever@example.com",
                "normalizedStatus": "ACTIVE",
                "toAbandonDate": "2023-02-11T10:48:23Z",
                "products": [
                    {
                        "storePrimaryId": "shoe",
                        "browseTimeSeconds": "40",
                        "numberOfTimesViewed": 1
                    },
                                        {
                        "storePrimaryId": "glove",
                        "browseTimeSeconds": "12",
                        "numberOfTimesViewed": 3
                    }
                ]
            }
        ]
    }
}
```

# Mutations

## saveBrowseSession

Used for testing purposes, this mutation will create a browse session in whatever state the user specifies. This should not be used for any actual integrations, as it will always create and never update a browse session. However, this is the only method to manually set a `toAbandonDate`, so it is useful to for testing the process of a session moving to a terminal state. Simply set a toAbandonDate in the past, and that session will transition to `ABANDONED` or `ADDED_TO_CART` within 5 minutes, complete with generating a Browse Abandonment Custom Object.

Sessions created in an ABANDONED state with this API will **NOT** generate Browse Abandonment custom objects.

> 🚧 Ensure that any products you create in this API have identifiers matching products in your product catalog.
>
> For example, if you set a `storePrimaryId` of `1234` on your browse products, ensure that your product catalog has a product with a `storePrimaryId` of `1234`

**Return Type**: [BrowseSession](https://developers.activecampaign.com/reference/browse-session-apis#browse-session-and-browsesessioninput)

**Arguments for `saveBrowseSession`**

| Name                                                                                                                                           | Description                                                            |
| :--------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| browseSession([BrowseSessionInput](https://developers.activecampaign.com/reference/browse-session-apis#browse-session-and-browsesessioninput)) | A filter to sort or filter browse products within the fetched session. |

### saveBrowseSession Example Payload

```Text GraphQL
mutation{
    saveBrowseSession(browseSession: 
    {
        legacyConnectionId: 1
        normalizedStatus: ACTIVE
        email: "whatever@example.com"
        toAbandonDate: "2023-02-11T10:48:23Z"
        products: [
            {
                storePrimaryId: "shoe"
                numberOfTimesViewed: 1
                mostRecentBrowsedAt: "2020-12-01T10:48:23Z"
                browseTimeSeconds: "40"
            }  
        ]        
    })
    {
        legacyConnectionId
    }
}
```

## browseSessionCartAdd

Attempt to set a session to have `addedToCart` set to true.

If an `ACTIVE` browse session is found for the associated email and connection, this call will set `addedToCart` to true on that session.

If a browse session is not found, a new one will be created with `addedToCart` set to true and no products.

**Return Type**: Boolean

**Arguments for `browseSessionCartAdd`**

| Name                                   | Description                                                               |
| :------------------------------------- | :------------------------------------------------------------------------ |
| legacyConnectionId(`Int`) **Required** | Integer connection identifier matching the v3 API DeepData Connection ID. |
| email(`string`) **Required**           | Email to use to find session.                                             |

### browseSessionCartAdd Example Payload

```Text GraphQL
mutation {
    browseSessionCartAdd(
        legacyConnectionId: 1
        email: "whatever@example.com"
    )
}
```

### browseSessionCartAdd Example Response

```Text json
{
    "data": {
        "browseSessionCartAdd": true
    }
}
```

## testTrackingEvent

The `testTrackingEvent` API has a twofold purpose. When called, it simulates a tracking event coming into the Browse Session system. The information provided is the same as though a tracking event were coming in through  site tracking, as described in [How are Browse Sessions Created?](https://developers.activecampaign.com/reference/browse-abandonment#how-are-browse-sessions-created). By using the testTrackingEvent API, users can simulate tracking traffic without needing to actually set up site tracking.

In addition, a [TrackingEventDebugTrace](https://developers.activecampaign.com/reference/browse-session-apis#trackingeventdebugtrace-1) object is returned with details about what happened when the event was processed. This can be used to debug, for example, why a certain url pattern does not work.

**Return Type for `testTrackingEvent`**  [TrackingEventDebugTrace](https://developers.activecampaign.com/reference/browse-session-apis#trackingeventdebugtrace-1)

**Arguments for `testTrackingEvent`**

| Name                          | Description                                                                   |
| :---------------------------- | :---------------------------------------------------------------------------- |
| url (`string`) **Required**   | Url that was browsed                                                          |
| email (`string`) **Required** | Email of user for browsing event                                              |
| eventDate(`string`)           | Timestamp of when the browsing event happened. In format 2019-01-26T10:48:23Z |

### testTrackingEvent Example Payload

```Text GraphQL
mutation{
    testTrackingEvent(event: 
    {
        email:  "whatever@example.com"
        url: "http://activecampaign.com/Products/prod1"
        eventDate: "2025-01-21T14:04:19.288734-08:00"
    })
    {
        matchingConnection {
            legacyConnectionId
        }
        identifierType
        identifierValue
        modifiedSession {
            email
            lastTouchDate
            toAbandonDate
        }
        sessionWasCreated
        modifiedProduct {
            storePrimaryId
            numberOfTimesViewed
            browseTimeSeconds
        }
        previouslyBrowsedProduct {
            storePrimaryId
            numberOfTimesViewed
            browseTimeSeconds
        }
        productWasCreated
        outOfOrderEvent
        previousProductUnderMinimumViewTime
    }
}
```

### testTrackingEvent Example Response

```Text json
{
    "data": {
        "testTrackingEvent": {
            "matchingConnection": {
                "legacyConnectionId": 1
            },
            "identifierType": "STORE_PRIMARY_ID",
            "identifierValue": "prod1",
            "modifiedSession": {
                "email": "whatever@example.com",
                "lastTouchDate": "2025-01-21T22:04:19.288734Z",
                "toAbandonDate": "2025-02-05T22:20:58.265985747Z"
            },
            "sessionWasCreated": false,
            "modifiedProduct": {
                "storePrimaryId": "prod1",
                "numberOfTimesViewed": 0
            },
            "productWasCreated": true,
            "outOfOrderEvent": false,
            "previousProductUnderMinimumViewTime": false
        }
    }
}
```

# Objects

## Browse Session and BrowseSessionInput

`BrowseSession` and `BrowseSessionInput` objects have nearly the same fields. However, in GraphQL, input and return objects must be of different types, so in the GraphQL schema, they have the types `BrowseSession` and `BrowseSessionInput`.

The objects are otherwise identical.

<HTMLBlock>
  {`
  <table style="width: 100%; border-collapse: collapse;">
  <thead>
  <tr>
    <th style="border: 1px solid #ddd; padding: 8px;">Name</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>legacyConnectionId (<code>Integer</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Integer connection identifier matching the v3 API DeepData Connection ID.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>toAbandonDate (<code>String</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Timestamp of when the product will be marked as abandoned if no more browse events are received from the customer. If a session is in the <code>ABANDONED</code> state, this is the time when it was marked as abandoned. In format 2019-01-26T10:48:23Z</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>normalizedStatus: (<code>Enum</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Status of the browse session. Will be one of: <code>ACTIVE</code>, <code>ABANDONED</code>,    <code>ADDED_TO_CART</code>, or <code>ERRORED</code></p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>email: (<code>String</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Email of the customer associated with this session.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>sessionStartDate: (<code>String</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Timestamp of when the first browse event was received for the session, triggering the creation of the session. In format 2019-01-26T10:48:23Z</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>sessionEndDate: (<code>String</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Timestamp of when the session transitioned to a terminal state (e.g. <code>ABANDONED</code> or <code>ADDED_TO_CART</code>. In format 2019-01-26T10:48:23Z</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>lastTouchDate: (<code>String</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Timestamp of the last browse event received by the session. In format 2019-01-26T10:48:23Z</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>addedToCart: (<code>Boolean</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>True if this customer added any product to a cart while the browse session was active. False otherwise.<br>If <code>addedToCart</code> is true, then when this session transitions to a terminal state, that state will be <code>ADDED_TO_CART</code> rather than <code>ABANDONED</code>.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>products: (<code>[BrowseProduct](https://developers.activecampaign.com/reference/browse-session-apis#browseproduct-and-browseproductinput)[]</code>)</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>A list of the browse products in this session.</p>
  </td>
  </tr>
  </tbody>
  </table>
  `}
</HTMLBlock>

<br />

## BrowseProduct and BrowseProductInput

A product within a browse session.

`BrowseProduct` and `BrowseProductInput` objects have nearly the same fields. However, in GraphQL, input and return objects must be of different types, so in the GraphQL schema, they have the types `BrowseProduct` and `BrowseProductInput`.

The objects are otherwise identical.

| Name                             | Description                                                                                                                                                                                                                                              |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| storePrimaryId(`String`)         | Primary identifier for this product within a store. Must be unique within the scope of a single store. For stores with variants, the `storePrimaryId`is generally a unique identifier on the variant. References `storePrimaryId` on the Product object. |
| storeBaseProductId(`String`)     | The store's primary unique identifier for the base/parent product.                                                                                                                                                                                       |
| variantSku(`String`)             | Stock Keeping Unit (SKU) for the product variant.                                                                                                                                                                                                        |
| upc(`String`)                    | The product's upc.                                                                                                                                                                                                                                       |
| baseProductUrlSlug(`String`)     | URL slug for the base product.                                                                                                                                                                                                                           |
| variantUrlSlug(`String`)         | URL slug for the variant product.                                                                                                                                                                                                                        |
| browseTimeSeconds(`Integer`)     | Number of seconds, totaled from all views combined, that this product was viewed.                                                                                                                                                                        |
| mostRecentBrowsedAt(`String`)    | Timestamp for the most recent time the user began to look at this product. In format 2019-01-26T10:48:23Z                                                                                                                                                |
| numberOfTimesViewed(`Integer`)   | Number of times a product was viewed during this browse session.                                                                                                                                                                                         |
| baseProductName(`String`)        | Product name for the base product.                                                                                                                                                                                                                       |
| baseProductDescription(`String`) | Product description for the base product.                                                                                                                                                                                                                |
| priceAmount(`Decimal`)           | Decimal amount of the price of the product.                                                                                                                                                                                                              |
| priceCurrency(`String`)          | 3-letter currency code for the price of this product. Example: `USD`                                                                                                                                                                                     |
| averageRating(`Decimal`)         | The product's average rating.                                                                                                                                                                                                                            |
| imageUrl(`String`)               | Url for an image for the product.                                                                                                                                                                                                                        |
| productUrl(`String`)             | Url for the product detail page.                                                                                                                                                                                                                         |
| productCreatedDate(`String`)     | Date the product was created in the store. In format 2019-01-26T10:48:23Z                                                                                                                                                                                |
| currentlyBrowsing(`Boolean`)     | True if the product is the product the customer is currently looking at. Each browse session should have at most 1 product that is `currentlyBrowsing`. A session in a terminal state will have 0 products `currentlyBrowsing`.                          |

## TrackingEvent

<br />

| Name                             | Description |
| :------------------------------- | :---------- |
| email(`string`) **Required**     |             |
| url(`string`) **Required**       |             |
| eventDate(`string`) **Required** |             |

## BrowseProductFilter

A BrowseProductFilter will only filter and sort on products within an individual session. For more information on searches, see: [Searches](https://developers.activecampaign.com/reference/searches). The following are available filters for Browse Products:

| Name                                        |
| :------------------------------------------ |
| storePrimaryId(`StringFieldFilter`)         |
| storeBaseProductId(`StringFieldFilter`)     |
| variantSku(`StringFieldFilter`)             |
| upc(`StringFieldFilter`)                    |
| baseProductUrlSlug(`StringFieldFilter`)     |
| variantUrlSlug(`StringFieldFilter`)         |
| browseTimeSeconds(`IntFieldFilter`)         |
| mostRecentBrowsedAt(`DateTimeFieldFilter`)  |
| numberOfTimesViewed(`IntFieldFilter`)       |
| baseProductName(`StringFieldFilter`)        |
| baseProductDescription(`StringFieldFilter`) |
| categories(`StringFieldFilter`)             |
| priceAmount(`NumberFieldFilter`)            |
| priceCurrency(`StringFieldFilter`)          |
| averageRating(`NumberFieldFilter`)          |
| imageUrl(`StringFieldFilter`)               |
| productUrl(`StringFieldFilter`)             |
| productCreatedDate(`DateTimeFieldFilter`)   |
| currentlyBrowsing(`BooleanFieldFilter`)     |

## TrackingEventDebugTrace

| Name                                             | Description                                                                                                                                                                                   |
| :----------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| matchingConnection (`Connection`)                | If a url pattern match was detected, this is the connection that match was associated with, the connection the browse session will be created under.                                          |
| identifierType: (`Enum`)                         | The identifier matched from the url pattern. Will be one of `SKU,  STORE_PRIMARY_ID, STORE_BASE_PRODUCT_ID, UPC, VARIANT_URL_SLUG, BASE_PRODUCT_URL_SLUG`                                     |
| identifierValue (`String`)                       | Value of the identifier matched from the url pattern.                                                                                                                                         |
| modifiedSession (`BrowseSession`)                | The session that was modified by the tracking event, after modification.                                                                                                                      |
| sessionWasCreated: (`Boolean`)                   | True is the session was created. False if an existing session was modified.                                                                                                                   |
| modifiedProduct: (`BrowseProduct`)               | The product in the session that matched the identifier and was updated or created.                                                                                                            |
| previouslyBrowsedProduct: (`BrowseProduct`)      | The previously product that had `currentlyBrowsing` set to true. The following fields were potentially updated by this event: `browseTimeSeconds`, `numberofTimesViewed`, `currentlyBrowsing` |
| productWasCreated: (`Boolean`)                   | True if a new browse product created. False otherwise.                                                                                                                                        |
| outOfOrderEvent: (`Boolean`)                     | If the timestamp on the event was before the session's `lastTouchDate`, the event is considered to be out of order and will be ignored. True if event was ignored. False otherwise.           |
| previousProductUnderMinimumViewTime: (`Boolean`) | True if the `previouslyBrowsedProduct` was viewed for under the minimum page view time, thus ignoring changes to the `previouslyBrowsedProduct`. False otherwise.                             |