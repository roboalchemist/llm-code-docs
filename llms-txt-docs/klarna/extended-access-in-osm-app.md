# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/extended-access-in-osm-app.md

# Extended Access features in the Klarna On-site messaging Shopify app

## This article explains how you can grant additional access to the Klarna On-site messaging Shopify app in order to benefit from some features not available in the app by default.

We’re continuously developing additional features for the Klarna On-site messaging (OSM) Shopify app to help mitigate the [constraints of the Klarna payments integration](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/known-constraints.md). The features included in the extended accesses for the Klarna OSM Shopify app allow us to gather additional information about orders placed with Klarna in your store. These extended access features are enabled by default when you install the On-Site messaging app, but can be disabled by deselecting the Extended Access option in the app settings. To use **Extended Access** features, you need a direct Klarna integration via the Klarna app.


![ Extend Access is an optional configuration that provides additional permissions to enhance the Klarna On-site messaging app’s functionalities.](ff93388b-4422-4bd9-ace7-af6217f0358b-Extended-Access.jpeg)
*Extend Access is an optional configuration that provides additional permissions to enhance the Klarna On-site messaging app’s functionalities.*

With Extended Access, the Klarna OSM Shopify app has access to protected customer data, such as the Shopify order details. We access minimal data as needed for the following additional features:

- As of October 11, 2022, the Klarna OSM Shopify app queries the Shopify order to update Klarna’s `merchant_reference_1` field with the corresponding [Shopify order name](https://shopify.dev/api/admin-graphql/2022-10/objects/Order#field-order-name).
- As of November 3, 2022, the Klarna order ID is added as a Shopify order note on the Shopify backend.
- As of September 20, 2023, a Klarna tag is added to Shopify orders placed through Klarna.
- Additional order line data, that is, a product URL and image URL, are added to the Klarna order shortly after the order is placed.
- The inventory is checked to prevent product oversells. As of May 2023, this feature is available for selected merchants with extended access. If you want to enable this feature, contact your regional [Klarna merchant support](http://klarna.com/merchant-support) team.

## Action required to access new features


![ When extending access for the Klarna On-site messaging Shopify app, you'll see the details of the access changes.](664171b8-2f3a-42be-8395-3df7f3ded31d_Update-Klarna-On-Site-Messaging.jpeg)
*When extending access for the Klarna On-site messaging Shopify app, you'll see the details of the access changes.*

![ When Extended Access is enabled in a Shopify store, additional order details are visible in the Merchant portal, for example, the Shopify order ID as Reference and an image of the product.](fce1974e-cd0f-4ff0-b741-Screenshot.jpeg)
*When Extended Access is enabled in a Shopify store, additional order details are visible in the Merchant portal, for example, the Shopify order ID asReferenceand an image of the product.*

**To summarize**:

- The Klarna On-site messaging (OSM) Shopify app has extended access features that gather additional information about orders placed with Klarna in your store.
- Enabling extended access grants the app permission to access protected customer data and provides enhanced functionalities for the Klarna OSM Shopify app.
- Extended access can be enabled or disabled in the app settings by selecting or deselecting the Extended Access option in the app's dashboard.