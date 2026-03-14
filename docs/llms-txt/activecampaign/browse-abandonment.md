# Source: https://developers.activecampaign.com/reference/browse-abandonment.md

# Browse Abandonment Developer Overview

This is a technical description of the Ecommerce GraphQL Browse Session and Browse Abandonment APIs.

For a description of setting up Browse Abandonment automations and the Browse Abandonment feature, see:[Browse Abandonment Overview](https://help.activecampaign.com/hc/en-us/articles/18489509394844-Browse-Abandonment-overview#h_01JM0745WSVJT29CAH7YEQ0B54)

# Definition of Terms

**Browse Session** - A session which represents that a user is (or was) on a store, browsing products. A browse session exists as an object in the [v3 GraphQL APIs](https://developers.activecampaign.com/reference/browse-session-apis). A browse session has 3 states:

* **Active** - The user is still browsing product pages in the store.
* **Abandoned** - The user has been inactive in the store for the length of the `Session Timeout`.
* **Added to cart** - The user has added at least one item to a cart in the store.

An active session will always eventually move to either an “abandoned” or “added to cart” state. A browse session can never move out of “Abandoned” and “added to cart”. If a user browses more pages after a session is “Abandoned” or “Added to cart”, a new browse session will be created. Browse sessions are queryable through the [Browse Session GraphQL API](https://developers.activecampaign.com/reference/browse-session-apis).

**Browse Product** - Product details, representing a single product that a user has looked at in a browse session. A browse product only exists within the context of a browse session. Details such as product name and product images are populated based on the store’s product catalog, which must be synced to ActiveCampaign prior to using browse abandonment functionality.
Browse products are queryable through the Browse Session GraphQL API.

**Browse Abandonment** - When a browse session moves to the abandoned state, a browse abandonment is created. Browse abandonments exist as an ActiveCampaign-managed Custom Object schema. Browse Abnadonments (not Browse Sessions) control all automations and segmentation behavior.

**Minimum Page View Time** - A configurable setting that determines how long a user must stay on a page for us to not ignore their page view. Any page views under the minimum page view time will be completely ignored. Any views over this threshold will be processed. (Default: 8 seconds)

**Session Timeout** - A configurable setting that determines how long a period of idle activity ActiveCampaign will wait to mark a session as abandoned. For example, if this is set at 1 hour, then 1 hour after a user browses their last page in a session, that session will move to the abandoned or added to cart state. (Default: 1 hour)

# How are Browse Sessions Created?

ActiveCampaign will check site visits to see whether they match URL patterns associated with product pages on connections (see below for how this URL pattern matching is performed). If a match is detected, an identifier is extracted from the URL and used to query the product catalog data for that store. The matching product will then be added to a browse session.

<Callout icon="📘" theme="info">
  If browse sessions are not being created on your account, check to see whether or not your site visits are correctly configured. Please confirm that the steps outlined in the site tracking setup instructions have been completed.
</Callout>

# URL Pattern Matching

When ActiveCampaign receives a tracking event, we check the URL against all connections associated with the account. Each connection has a list of URL patterns (these patterns are not visible in the V3 connection API). This is a list of strings, each of which is a potential form the URLs for your product detail pages can take.

<Callout icon="📘" theme="info">
  For the sake of url matching, ActiveCampaign does not differentiate between http and https.
</Callout>

If we detect a URL match, we will add an active browse session for that connection. The browse session will be for a contact matching the email associated with the tracking event. It will contain the product the user viewed. If an active browse session already exists, we will add the new product to that browse session. If your account has multiple connections, a single email can have separate browse sessions for each connection. Browse sessions for separate connections will not impact one another.

<Callout icon="🚧" theme="warn">
  If an email has no associated contact in your ActiveCampaign account, we will not create a Browse Session. We will never create a contact based on browsing data.
</Callout>

## URL Pattern Examples

The following are examples of URL pattern matching in action.

If products on your store are located at URLs that look like this:

`https://activecampaign.com/Product/3845`

Then this can be matched with the URL matcher:

`https://activecampaign.com/Product/{{storeBaseProductId}}`

Note the double curly braces at the end. ***Each URL matcher must contain exactly one double curly brace variable***. This will match any characters in that section of the URL and communicate (in this example) that your `storeBaseProductId` lives in that part of the URL.

In the above example, the 3845 in `https://activecampaign.com/Product/3845` would be matched as the `storeBaseProductId`.

Only six variables can be placed in the URL pattern matcher. Each of these maps to a field in the [ActiveCampaign Product Catalog ](https://help.activecampaign.com/hc/en-us/articles/6558123071388-Email-Designer-Use-the-Product-Catalog-block-with-your-email-campaigns#h_01J6ZDC6YYR2149KNNYXP5GW6C) data for your account:

| Field in Url Matcher | Meaning                                                                                                                                                                                                                                                        |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| variantSku           | The SKU of the variant product. Different variants of the same base products should have different SKUs.                                                                                                                                                       |
| storePrimaryId       | The unique, primary identifier your store assigns to every product. Variants must have different storePrimaryIds from one another.                                                                                                                             |
| storeBaseProductId   | A unique identifier for base products. A base product may have different variants, but they will all share a storeBaseProductId.                                                                                                                               |
| upc                  | UPC for this product.                                                                                                                                                                                                                                          |
| baseProductUrlSlug   | The URL slug for the base product. A slug is a human-readable part of the url that uniquely identifies a product. A base product may have different variants, but the detail page for that base product will be on a page with the slug for that base product. |
| variantUrlSlug       | The URL slug for the variant product. A slug is a human-readable part of the url that uniquely identifies a product.                                                                                                                                           |

When a URL match is detected, ActiveCampaign will extract the configured identifier, find a product with a matching identifier in your product catalog, then use that product catalog data to populate product data in the Browse Session.

If we receive a tracking event that does not match a URL pattern in one of your connections, we will ignore it.

Let’s look at a few more example store URL patterns and how we can match them:

### Query String Parameter Product Identifier

Consider a store that uses query string parameters to identify products:

`https://activecampaign.com/Store?product=3845`

A URL matcher for this is:

`https://activecampaign.com/Store?product={{upc}}`

### Include Separating Characters

Be careful to include separating characters like slashes in the pattern itself. For example, if this pattern is used:

`https://activecampaign.com/Product{{upc}}`

On this URL:

`https://activecampaign.com/Product/3845`

The resultant upc will be `/3845` (with the leading slash). The correct pattern is:

`https://activecampaign.com/Product/{{upc}}`

## Wildcards

If a store has parts of the URL that vary, a `**` wildcard can be inserted in order to ignore that part of the url. For example, a store that has the category in the URL:

`https://activecampaign.com/Category/Books/3845`

Can be matched by:

`https://activecampaign.com/Category/**/{{upc}}`

In this way, whether the category is Books, Clothing, or any other string, the pattern matcher will still match the identifier at the end.

<Callout icon="📘" theme="info">
  Each URL matcher can have a maximum of two `**` wildcards. The matcher string is not a regular expression. It simply allows for usage of the \*\* operator to ignore parts of the URL.
</Callout>

A `**` wildcard cannot appear next to a double curly brace variable. The following is invalid in a URL:

`Products/**{{upc}}`
`Products/{{upc}}**`

However, this is valid:

`Products/**/{{upc}}`

### Ignoring Query String Parameters

The `**` wildcard is also useful for ignoring query string parameters, as in this URL:

`https://activecampaign.com/Product/3845?searchString=abcd`

A matcher for this is:

`https://activecampaign.com/Product/{{storeBaseProductId}}?**`

Alternatively, if there is a closing slash in the product url before the query string, such as this example:

`https://activecampaign.com/Product/3845/?searchString=abcd` (Note the extra `/` between `3845` and `?searchString`)

Then the following pattern will more effectively ignore query string parameters:

`https://activecampaign.com/Product/{{storeBaseProductId}}/**`

The `storeBaseProductId` will match everything between `Product/` and the closing `/`, and everything after the closing `/` will be ignored. In this case, `?searchString=abcd` will be ignored.

<Callout icon="📘" theme="info">
  When debugging a new URL pattern, we suggest utilizing [Browse Session APIs](https://developers.activecampaign.com/reference/browse-session-apis#/) can be helpful. The [testTrackingEvent](https://developers.activecampaign.com/reference/browse-session-apis#/testtrackingevent) API provides debugging information in its response.
</Callout>

# How are Browse Abandonments Created?

While a user is browsing products, a session is in the `ACTIVE` state.

At some point, a user will cease browsing products. After a page view happens, a timer starts. When that timer reaches the session timeout for this connection, the `sessionEndDate` will be set to the current date, and the session will move to a terminal state of `ABANDONED` or `ADDED_TO_CART`. Once the session is in a terminal state, it will never leave that state.

If, during a session,  a user has added an item to a cart at any point, the `addedToCart` flag will be set to true. When the session times out, that session will move to the terminal state of `ADDED_TO_CART`.

If an item has not been added to cart, the session will move to `ABANDONED`.

If an item is moved to `ABANDONED`, a Browse Abandonment custom object will be created. This custom object will trigger automations via the `Browse Abandonment Created` trigger and may be used for user segmentation. The data for each individual product will also be aggregated. The products are not individually accessible in the custom objects, but many of the fields will be aggregated. The translation of fields from Browse Sessions to Browse Abandonments is:

| Browse Abandonment Field           | Related Browse Session or Browse Product Field | Notes                                                                                      |
| :--------------------------------- | :--------------------------------------------- | :----------------------------------------------------------------------------------------- |
| legacyConnectionId (`Integer`)     | legacyConnectionId                             |                                                                                            |
| email (`Integer`)                  | email                                          |                                                                                            |
| abandonmentDate                    | N/A                                            | When abandonment event happened.                                                           |
| sessionStartDate                   | sessionStartDate                               | Timestamp of the first page view of the session.                                           |
| sessionLength (`Integer`)          | N/A                                            | Number of seconds between first page view of a session and when the session was abandoned. |
| totalAmount( (`Currency`)          | browseProduct.priceAmount                      | Money value of sum of prices of all products in the session.                               |
| totalProductsViewed (`Integer`)    | N/A                                            | Total number of products viewed in session                                                 |
| maxPrice (`Currency`)              | browseProduct.priceAmount                      | Price of the lowest priced product viewed                                                  |
| minimumPrice(`Currency`)           | browseProduct.priceAmount                      | Price of the lowest priced product viewed                                                  |
| minimumProductViewTime (`Integer`) | browseProduct.browseTimeSeconds                | Number of seconds viewed for the shortest viewed product in the session.                   |
| maxProductViewTime (`Integer`)     | browseProduct.browseTimeSeconds                | Number of seconds viewed for the longest viewed product in the session.                    |
| productSkus(`String`)              | browseProduct.sku                              | JSON serialized list of the `sku`s of all products in the Browse Session                   |
| productStorePrimaryIds(`String`)   | browseProduct.storePrimaryId                   | JSON serialized list of the `storePrimaryId`s of all products in the Browse Session        |
| productNames(`String`)             | browseProduct.baseProductName                  | JSON serialized list of the `name`s of all products in the Browse Session                  |
| productCategories(`String`)        | browseProduct.categories                       | JSON serialized list of the `categories` of all products in the Browse Session             |

<br />

For abandoned sessions, there are two sources of data: the Browse Session API and the Browse Abandonment Custom Object.

* All automation triggers are based on the browse abandonment custom object
* All user segmentation data is based on the custom object.
* All data returned from the Browse Session API does not have the Custom Object as a source. It has its own internal data store.
* The Browse Abandonment Block pulls data for personalization from the Browse Session API.

# Product Data

<Callout icon="📘" theme="info">
  In order to use Browse Abandonment, you must sync your [product catalog data](https://help.activecampaign.com/hc/en-us/articles/6558123071388-Email-Designer-Use-the-Product-Catalog-block-with-your-email-campaigns#h_01J6ZDC6YYR2149KNNYXP5GW6C) into ActiveCampaign. This is done automatically during historical sync for Shopify and WooCommerce.
</Callout>

When ActiveCampaign creates a Browse Session with Browse Products, we use information from your product catalog data, stored in ActiveCampaign, to fill in the details of those products.

Products are identified based on the identifier from the URL pattern matching step. Each of the possible identifiers (variantSku, storePrimaryId, storeBaseProductId, upc, baseProductUrlSlug, or variantUrlSlug) also exist on products within the product catalog. We will locate products in the product catalog by querying based on the identifiers for each product. When a match is detected, the following fields from the matched product will be saved in the browse session:

* storePrimaryId
* storeBaseProductId
* variantSku
* upc
* baseProductUrlSlug
* variantUrlSlug
* baseProductName
* baseProductDescription
* priceAmount
* priceCurrency
* averageRating
* imageUrl
* productUrl
* productCreatedDate

If only some products from a browse session are matched, for example if a store owner removes products from their catalog, then unmatched products will be removed from the session. This avoids sending corrupt emails with products that do not have, for example, an image or a link or a price.

If no products can be found, for example if there is no product catalog data in ActiveCampaign, then no browse abandonment custom object will be created.

# FAQ

## What is the maximum number of browse products in a session?

We will only store a maximum of 25 browse products on a browse session. When a 26th product is added, the product with the lowest `browseTimeSeconds` will be removed.

## How are page view times calculated?

Page view times are calculated based on the amount of time passing between a page view and the next page that is viewed. Consider the following series of events:

* Jordan views Blue Shoes at 1 PM.
  * Jordan has no active session. Start new session for Jordan with Blue Shoes, 1:00 PM as a browse product.
  * The browse product will have the following attributes:
    * currentlyBrowsing => true
    * numberOfTimesViewed => 0
    * browseTimeSeconds => null
    * mostRecentBrowsedAt => 1 PM
* Jordan views Red Gloves at 1:05 PM.
  * Jordan has an active session. Blue Shoes is the single product with currentlyBrowsing => true, so compare the current time with mostRecentBrowsedAt.
  * 5 Minutes have passed, so Blue Shoes now has the following attributes:
    * currentlyBrowsing => false
    * numberOfTimesViewed => 1
    * browseTimeSeconds => 300
    * mostRecentBrowsedAt => 1 PM
  * Red shoes looks like:
    * currentlyBrowsing => true
    * numberOfTimesViewed => 0
    * browseTimeSeconds => null
    * mostRecentBrowsedAt => 1:05 PM
* Jordan walks away from keyboard.
  * After 1 hour (the session timeout minutes), the session becomes abandoned.
  * Blue shoes remains the same, since it was not the active product.
  * Red Gloves will look like:
    * currentlyBrowsing => false
    * numberOfTimesViewed => 1
    * browseTimeSeconds => (Set to be equal to the minimum page view time)
    * mostRecentBrowsedAt => 1:05 PM

<Callout icon="📘" theme="info">
  The view time of the last product to be browsed before a session is abandoned will be set to your minimum page view time.
</Callout>

## How often are browse sessions transitioned to terminal states?

An asynchronous process runs every 5 minutes to transition expired browse sessions to their terminal states. A browse session will transition if its `toAbandonDate` field is in the past.

## How can I view browse session data?

We currently do not expose browse session data in the UI. Only Browse Abandonment Custom Objects.

Browse Session data can only be viewed using the [Browse Session APIs](https://developers.activecampaign.com/reference/browse-session-apis#).