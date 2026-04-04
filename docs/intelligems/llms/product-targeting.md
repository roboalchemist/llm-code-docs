# Source: https://docs.intelligems.io/general-features/targeting/product-targeting.md

# Product Targeting

## How to use Product Targeting

Product Targeting allows you to control where onsite content edits and template tests appear based on **specific product attributes**, instead of relying on page URLs or fragile selectors.

With Product Targeting, you can show banners, messaging, and UI changes **only on the products that meet your conditions**, whether those products appear on a product page or inside a product listing.

This guide explains what Product Targeting is, where it works, and how to use it correctly.

***

### What is Product Targeting

Product Targeting evaluates the **product being shown** on the page or within a product placement and applies your content only when that product meets the conditions you define.

You can combine Product Targeting with:

* Page targeting
* Audience targeting

This lets you build highly specific, context-aware onsite experiences without duplicating tests or maintaining long lists of URLs.

***

### Where Product Targeting works

Product Targeting is currently supported on:

* **Onsite Edits**
* **Template Tests**
* **Onsite Edit & Template Personalizations**

It is not supported on:

* Price Tests
* Shipping Tests
* Offers
* Checkout Blocks

If a test type does not support page targeting, Product Targeting will not be available.

***

### Product Page vs Product Card targeting

When Product Targeting is enabled, the first step is choosing **where** the product appears.

#### Product Page

Product Page targeting applies only to product detail pages (`/products/`).

Use Product Page targeting when:

* Your messaging should appear only on the PDP
* The content is tightly tied to product details like price or inventory

Common examples:

* Low inventory banners on PDPs
* PDP-only promotional messaging

***

#### Product Card

Product Card targeting applies anywhere products appear in a list or grid, including:

* Collection pages
* Homepage featured products
* Product carousels
* Merch grids

By default, Product Card targeting works on **collection pages**.

{% hint style="info" %}
To enable Product Card targeting on non-collection pages such as homepages or landing pages, additional theme setup is required. When Product Card is selected, you will see a banner in the app linking to the setup guide. [Steps here](https://docs.intelligems.io/general-features/targeting/product-targeting/how-to-set-up-collection-card-product-targeting).&#x20;
{% endhint %}

***

### Product conditions

You can target products using one or more of the following conditions:

1. **Manual selection**
   1. Target specific products by selecting individual product IDs.
2. **Collection**
   1. Target products that belong to one or more collections.
3. **Tag**
   1. Target products that include specific product tags.
4. **Price**
   1. Target products based on price conditions.
      1. Price is evaluated using the **lowest-priced variant**
      2. Use greater than and less than to define price ranges
5. **Inventory**
   1. Target products based on inventory levels.
      1. Inventory is calculated using **total stock across all variants**

***

### Combining conditions with AND and OR

You can combine multiple product conditions using **AND** and **OR** logic.

Examples:

* Products in Collection A **AND** inventory below 20
* Products tagged "sale" **OR** priced below $50

There are no guardrails on condition combinations. If conditions conflict, no products will be targeted.

***

### Using Product Targeting with other targeting rules

Product Targeting can be layered with:

* Page targeting
* Audience targeting

All targeting rules must evaluate as true for the content to appear.

***

### Common use cases

#### Product-specific PDP messaging

Apply a single content edit across many PDPs by targeting products by collection or tag.

#### Low inventory messaging

Automatically show urgency messaging when product inventory drops below a threshold.

#### Collection and homepage merchandising

Update badges, copy, or visuals for specific products inside product grids without relying on brittle selectors.

#### Migrating from Because

Replicate Because-style product rules directly inside Intelligems.

***

### Troubleshooting and tips

**I do not see Product Targeting as an option**\
Make sure you are using a test type that supports page targeting, such as Onsite Edits or Template Tests.

**My Product Card targeting is not working on the homepage**\
By default, Product Card targeting only works on collection pages. Follow the setup guide linked in the app to enable it on non-collection pages.

**No products are matching my conditions**\
Review your AND and OR logic. Conflicting conditions can result in no products being targeted.

**I installed Intelligems manually**\
If you use a manual script installation, make sure you have copied the latest script from Settings to ensure Product Targeting works correctly.

***

### Related guides

* [How to Set Up Collection Card Product Targeting](https://docs.intelligems.io/general-features/targeting/product-targeting/how-to-set-up-collection-card-product-targeting)

***

If you need help setting up Product Targeting or want to validate your configuration, contact the Intelligems Support team.
