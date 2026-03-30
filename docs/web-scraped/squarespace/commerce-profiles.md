# Squarespace Developer Documentation

# Source: https://developers.squarespace.com/commerce-apis/profiles-overview

Profiles API overview — Squarespace Developers

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

# Profiles API overview

## Current version: 1.0

*For versioning details, read the [Upgrade](/commerce-apis/upgrade) guide.*

The Profiles API allows apps to retrieve Squarespace site users.

A site user can be a customer, mailing list subscriber,

or donor that are traditionally accessible through the [Profiles panel](https://support.squarespace.com/hc/en-us/articles/360046485652).

Site visitors become site users when they perform one of the following actions:

Registers an account with the site

- Performs an e-commerce guest checkout or donation on the site

- Subscribes to a newsletter or campaigns mailing list

## API resources

The Profiles API allows for the retrieval of `Profile` resource objects.

Every `Profile` contains information about a site user and has the following characteristics:

- A unique email address

- An approximate address for the user based on existing data (always generated internally, not created by the API)

- A summary of the user's commerce transactions, such as orders or donations (generated asynchronously from the site)

## Further reading

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