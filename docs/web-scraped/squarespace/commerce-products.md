# Squarespace Developer Documentation
# Source: https://developers.squarespace.com/commerce-apis/products-overview

Products API overview — Squarespace Developers

-

[

](/)

[Template Docs](/quick-start)

[Commerce APIs](/commerce-apis/overview)

[Webhooks](/webhooks/overview)

[Custom Code](/custom-code/about)

[Upcoming Changes](/changes/upcoming-changes)

[Get Started](/quick-start)

[

](/)

[Template Docs](/quick-start)

[Commerce APIs](/commerce-apis/overview)

[Webhooks](/webhooks/overview)

[Custom Code](/custom-code/about)

[Upcoming Changes](/changes/upcoming-changes)

[Get Started](/quick-start)

Getting started

[Overview](/commerce-apis/overview)

[Authentication and permissions](/commerce-apis/authentication-and-permissions)

[Making requests](/commerce-apis/making-requests)

[Retrieve basic site information](/commerce-apis/retrieve-basic-site-info)

Using Commerce APIs

[Idempotency-Key header](/commerce-apis/idempotency-key)

[Rate limits](/commerce-apis/rate-limits)

[Responses & error handling](/commerce-apis/responses-error-handling)

[Upgrade](/commerce-apis/upgrade)

[Changelog](/commerce-apis/changelog)

[Price Limits](/commerce-apis/price-limits)

[Glossary](/commerce-apis/glossary)

[FAQ](/commerce-apis/faq)

Inventory API

[Overview](/commerce-apis/inventory-overview)

[GET: Retrieve all inventory](/commerce-apis/retrieve-all-inventory)

[GET: Retrieve specific inventory](/commerce-apis/retrieve-specific-inventory)

[POST: Adjust stock quantities](/commerce-apis/adjust-stock-quantities)

Orders API

[Overview](/commerce-apis/orders-overview)

[POST: Create an order](/commerce-apis/create-order)

[POST: Fulfill an order](/commerce-apis/fulfill-order)

[GET: Retrieve all orders](/commerce-apis/retrieve-all-orders)

[GET: Retrieve a specific order](/commerce-apis/retrieve-specific-order)

Products API

[Overview](/commerce-apis/products-overview)

[About product attributes](/commerce-apis/about-product-attributes)

[Managing attributes](/commerce-apis/managing-attributes)

[POST: Create a product](/commerce-apis/create-product)

[POST: Create a product variant](/commerce-apis/create-product-variant)

[POST: Upload a product image](/commerce-apis/upload-product-image)

[GET: Retrieve all Store Pages](/commerce-apis/retrieve-all-store-pages)

[GET: Retrieve all products](/commerce-apis/retrieve-all-products)

[GET: Retrieve specific products](/commerce-apis/retrieve-specific-products)

[GET: Product image upload status](/commerce-apis/product-image-upload-status)

[POST: Assign a product image to variant](/commerce-apis/assign-product-image-variant)

[POST: Reorder a product image](/commerce-apis/reorder-product-image)

[POST: Update a product](/commerce-apis/update-product)

[POST: Update a product variant](/commerce-apis/update-product-variant)

[POST: Update a product image](/commerce-apis/update-product-image)

[DEL: Delete a product](/commerce-apis/delete-product)

[DEL: Delete a product variant](/commerce-apis/delete-product-variant)

[DEL: Delete a product image](/commerce-apis/delete-product-image)

Profiles API

[Overview](/commerce-apis/profiles-overview)

[GET: Retrieve all profiles](/commerce-apis/retrieve-all-profiles)

[GET: Retrieve specific profiles](/commerce-apis/retrieve-specific-profiles)

Transactions API

[Overview](/commerce-apis/transactions-overview)

[GET: Retrieve all transactions](/commerce-apis/retrieve-all-transactions)

[GET: Retrieve specific transactions](/commerce-apis/retrieve-specific-transactions)

Webhook Subscriptions API

[Overview](/commerce-apis/webhook-subscriptions-overview)

[POST: Create a webhook subscription](/commerce-apis/create-webhook-subscription)

[POST: Update a webhook subscription](/commerce-apis/update-webhook-subscription)

[GET: Retrieve all webhook subscriptions](/commerce-apis/retrieve-all-webhook-subscriptions)

[GET: Retrieve a specific webhook subscription](/commerce-apis/retrieve-specific-webhook-subscription)

[DEL: Delete a webhook subscription](/commerce-apis/delete-webhook-subscription)

[POST: Send test notification](/commerce-apis/send-test-notification)

[POST: Rotate a subscription secret](/commerce-apis/rotate-subscription-secret)

# Products API overview

**Current version: v2** | **Legacy versions: v1.1, v1.0**

*For versioning details, read the [Upgrade](/commerce-apis/upgrade) guide.*

Use the Products API to manage product information on a Squarespace merchant site,

including variants of a product and product images.

This API allows products to be retrieved, added, deleted, or modified

with information such as a name or URL slug, a variant's color, size, or weight, or a new product image.

## API Versions

**v2** - The latest version of the Products API with enhanced product type support. v2 endpoints support physical, service, gift card, and download products for most operations. Note: Download products cannot be created or deleted via v2 API.

**v1.1, v1.0 (Legacy)** - The stable versions of the Products API. v1.0 and v1.1 endpoints will continue to be supported, but we recommend using v2 for new integrations.

## What information isn't available?

Categories used by a Store Page to group products

## Product visibility for purchase

Read the [How Squarespace organizes products](https://support.squarespace.com/hc/en-us/articles/206541007) knowledge base article

to better understand how merchants organize and display products on their site.

In general, a Store Page is a collection of products,

and every product details page is a child page of a Store Page.

Consequently, a product details page may not belong to more than one Store Page.

**Characteristics of Store Pages and product details pages directly impacts if a product is visible for purchase.

A product is unavailable for purchase if a product’s Store Page is "Disabled"

and/or if the status on a product details page is "Hidden".**

How a merchant configures their site navigation for visitors (i.e., "[Not linking](https://support.squarespace.com/hc/en-us/articles/360025899552-The-Not-Linked-section)"

the Store Page, grouping products under a category etc.) has no effect on product visibility for purchases.

### Characteristics

**Enabled or disabled page setting**

*Squarespace UI > Pages > any Store Page > gear icon > Store Settings editor > General*

A newly added Store Page in the Squarespace UI is enabled by default.

Enabled Store Pages are immediately available on the merchant site and can be indexed by search engines.

A disabled Store Page can’t be accessed by site visitors.

This applies to all product details pages within the Store Page.

**Status on the product details page**

*Squarespace UI > Pages > any Store Page > any product card > product editor*

OR

*Squarespace UI > Commerce > Inventory > any product row > product editor*

Each product has a "Visible" or "Hidden" status, where "Hidden" makes a product details page unavailable to customers

while browsing products on a Store Page or via its direct URL.

## API resources

The Products API is responsible for the resources below.

All resource fields are described under **Response example** in the listed endpoints.

### Store pages

`StorePage` represents information for a Store Page on a merchant site.

Each `Product` on a merchant site belongs to a single `StorePage`.

- [Retrieve all Store Pages](/commerce-apis/retrieve-all-store-pages)

### Products

`Product` represents information for a product on a merchant site.

Product information always includes name, description, type, URL, SEO options, tags

and whether the product is visible for purchase.

A `Product` may include up to 100 `ProductImage` subresources as well.

A `Product` without a `ProductImage` is still a valid `Product`.

**v2 Product Types**

v2 endpoints support four product types:

- **Physical Products** - Tangible goods that require shipping or pick up

- **Service Products** - Services or experiences offered by the merchant

- **Gift Card Products** - Digital gift cards for the merchant site

- **Download Products** - Digital files that customers can download

**Physical Products**

Physical product information always includes at least one `ProductVariant` subresource.

It can also include attributes, if used for multiple variants.

Physical products can have multiple variants (e.g., different sizes, colors) and can be accessed and modified in v1.0, v1.1, and v2.

- [Create a product](/commerce-apis/create-product)

- [Update a product](/commerce-apis/update-product)

- [Delete a product](/commerce-apis/delete-product)

- [Retrieve all products](/commerce-apis/retrieve-all-products)

- [Retrieve specific products](/commerce-apis/retrieve-specific-products)

**Service Products (v2)**

Service products represent services or experiences offered by the merchant, such as consulting, coaching, camps, retreats, or group trips.

Service products can have multiple variants (e.g., different service tiers, durations) and can be accessed and modified in v2 only.

- [Create a product](/commerce-apis/create-product)

- [Update a product](/commerce-apis/update-product)

- [Delete a product](/commerce-apis/delete-product)

- [Retrieve all products](/commerce-apis/retrieve-all-products)

- [Retrieve specific products](/commerce-apis/retrieve-specific-products)

**Gift Card Products (v2)**

Gift card products represent digital gift cards for the merchant site.

Gift card products can have multiple variants (e.g., different denominations) and can be created, accessed, and modified in v2 only.

- [Create a product](/commerce-apis/create-product)

- [Update a product](/commerce-apis/update-product)

- [Delete a product](/commerce-apis/delete-product)

- [Retrieve all products](/commerce-apis/retrieve-all-products)

- [Retrieve specific products](/commerce-apis/retrieve-specific-products)

**Download Products**

Download product information can include at most one `DigitalGood` subresource.

Though typically a `DigitalGood` will be included, it is possible for a download product to not include one

due to the product being improperly created or edited.

Download products cannot have variants. In v2, download products can be accessed and modified, but not created nor deleted. In v1.1, download products can only be accessed. In v1.0, download products cannot be accessed.

- [Update a product](/commerce-apis/update-product)

- [Retrieve all products](/commerce-apis/retrieve-all-products)

- [Retrieve specific products](/commerce-apis/retrieve-specific-products)

### Product variants

`ProductVariant` represents information for a variant of a product on a merchant site.

Each variant contains information like a unique SKU, pricing, stock quantity,

product dimensions, values for product attributes (if listed), etc.

**Product types that support variants:**

- **Physical Products** - Can have multiple variants (e.g., different sizes, colors)

- **Service Products** - Can have multiple variants (e.g., different service tiers, durations)

- **Gift Card Products** - Can have multiple variants (e.g., different denominations)

**Product types that do NOT support variants:**

- **Download Products** - Cannot have variants

Service and gift card variants are supported in v2 only. Physical variants are supported in v1.0, v1.1, and v2.

- [Create a product variant](/commerce-apis/create-product-variant)

- [Update a product variant](/commerce-apis/update-product-variant)

- [Delete a product variant](/commerce-apis/delete-product-variant)

### Product images

`ProductImage` represents information for an image in a product's collection of images.

If desired, a `ProductImage` can be assigned to any `ProductVariant` of a `Product`

— even if it's the same `ProductImage`.

However, a `ProductVariant` can reference one `ProductImage` at most.

Product images are supported in v1.0, v1.1, and v2.

- [Upload a product image](/commerce-apis/upload-product-image)

- [Check the status of a product image upload](/commerce-apis/product-image-upload-status)

- [Update a product image](/commerce-apis/update-product-image)

- [Reorder a product image](/commerce-apis/reorder-product-image)

- [Assign a product image to a variant](/commerce-apis/assign-product-image-variant)

- [Delete a product image](/commerce-apis/delete-product-image)

### Digital goods

`DigitalGood` represents information for the purchasable file of the product.

A `DigitalGood` can not yet be accessed or modified separately from the owning `Product`.

Digital goods are supported in both v1.1 and v2.

## Further reading

- Learn more [about product attributes](/commerce-apis/about-product-attributes), and their relationship to a product's variants

- Become familiar with [common commerce terms](/commerce-apis/glossary) and how they're related to the API

- [Obtain an API key or use OAuth](/commerce-apis/authentication-and-permissions)

- Read the [FAQ](/commerce-apis/faq) guide for answers to common questions

# Squarespace

[Main Site](https://www.squarespace.com)

[Careers](https://www.squarespace.com/about/careers)

# Developers

[Home](/)

[Developer Terms of Use](https://www.squarespace.com/developer-terms)

[Privacy Policy](https://www.squarespace.com/privacy)

[Security Measures](https://www.squarespace.com/measures)

# Documentation

[Template Docs](/quick-start)

[Commerce APIs](/commerce-apis/overview)

[Webhooks](/webhooks/overview)

# Community

[Circle](https://circle.squarespace.com)

[Specialists](https://specialists.squarespace.com)

[Forum](https://forum.squarespace.com)

# Follow

[Engineering Blog](https://engineering.squarespace.com)

[Github](https://github.com/squarespace)

[NPM](https://www.npmjs.com/org/squarespace)