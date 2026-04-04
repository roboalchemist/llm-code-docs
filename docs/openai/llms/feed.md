# Source: https://developers.openai.com/commerce/specs/feed.md

# Product Feed Spec

## Overview

The Product Feed Specification defines how merchants share structured product data with OpenAI so ChatGPT can accurately surface their products in search and shopping experiences.

**How it works**

1. Prepare your feed. Format your catalog using the Product Feed Spec (see Field reference for required and optional attributes with sample values).
2. Deliver the feed. Share the feed using the preferred delivery method and file format described in the integration section.
3. Ingestion and indexing. OpenAI ingests the feed, validates records, and indexes product metadata for retrieval and ranking in ChatGPT.
4. Keep it fresh. Update the feed whenever products, pricing, or availability change to ensure users see accurate information.

**Key points**

- **Structured source of truth**. OpenAI relies on merchant-provided feeds—this ensures accurate pricing, availability, and other key details.
- **Built for discovery**. The feed powers product matching, indexing, and ranking in ChatGPT.
- **Integration guidance**. The spec defines the preferred delivery method and file format for reliable ingestion.
- **Field reference**. A complete list of required and optional attributes (with examples) is provided to help you validate your feed.
- **Freshness matters**. Frequent updates improve match quality and reduce out-of-stock or price-mismatch scenarios.

## Integration Overview

This section outlines the key logistics: how the feed is delivered, acceptable file formats, and the initial steps required to validate your data, so engineering teams can plan with confidence.

<table>
  <colgroup>
    <col style="width: 220px;" />
    <col />
  </colgroup>
  <thead>
    <tr>
      <th>Topic</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Delivery model</td>
      <td>
        Merchants push feeds to OpenAI via SFTP, file upload, or hosted URL.
      </td>
    </tr>
    <tr>
      <td>File format</td>
      <td>Supported formats are `jsonl.gz` and `csv.gz` (gzip-compressed).</td>
    </tr>
    <tr>
      <td>Refresh Frequency</td>
      <td>Our system accepts updates daily.</td>
    </tr>
  </tbody>
</table>

## Field Reference

To make your products discoverable inside ChatGPT, merchants provide a structured product feed that OpenAI ingests and indexes. This specification defines the complete schema: field names, data types, constraints, and example values needed for accurate search, pricing, and checkout experiences.

Each table below groups attributes by category (Basic Data, Media, Pricing, etc.) and clearly indicates whether a field is Required, Recommended, or Optional, along with validation rules to help your engineering team build and maintain a compliant feed.

Supplying all required fields ensures your products can be displayed correctly, while recommended fields enrich relevance and user trust.

<div id="field-reference-content">

### OpenAI Flags

Use these flags to control whether a product is discoverable and/or purchasable inside ChatGPT. These fields do not affect how the product is displayed on your own site, they simply enable or disable the ChatGPT integrations.

| Attribute            | Data Type | Supported Values | Description                                                                                                                                        | Example | Requirement | Dependencies                       | Validation Rules  |
| :------------------- | :-------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- | :------ | :---------- | :--------------------------------- | :---------------- |
| is_eligible_search   | Boolean   | `true`, `false`  | Controls whether the product can be surfaced in ChatGPT search results.                                                                            | `true`  | Required    | —                                  | Lower-case string |
| is_eligible_checkout | Boolean   | `true`, `false`  | Allows direct purchase inside ChatGPT. <br/>`is_eligible_search` must be `true` in order for `is_eligible_checkout` to be enabled for the product. | `true`  | Required    | Requires `is_eligible_search=true` | Lower-case string |

### Basic Product Data

Provide the core identifiers and descriptive text needed to uniquely reference each product. These fields establish the canonical record that ChatGPT Search uses to display and link to your product.

| Attribute   | Data Type             | Supported Values | Description                              | Example                                      | Requirement | Dependencies | Validation Rules                            |
| :---------- | :-------------------- | :--------------- | :--------------------------------------- | :------------------------------------------- | :---------- | :----------- | :------------------------------------------ |
| item_id     | String (alphanumeric) | —                | Merchant product ID (unique per variant) | `SKU12345`                                   | Required    | —            | Max 100 chars; must remain stable over time |
| gtin        | String (numeric)      | GTIN, UPC, ISBN  | Universal product identifier             | `123456789543`                               | Optional    | —            | 8–14 digits; no dashes or spaces            |
| mpn         | String (alphanumeric) | —                | Manufacturer part number                 | `GPT5`                                       | Optional    | —            | Max 70 chars                                |
| title       | String (UTF-8 text)   | —                | Product title                            | `Men's Trail Running Shoes Black`            | Required    | —            | Max 150 chars; avoid all-caps               |
| description | String (UTF-8 text)   | —                | Full product description                 | `Waterproof trail shoe with cushioned sole…` | Required    | —            | Max 5,000 chars; plain text only            |
| url         | URL                   | RFC 1738         | Product detail page URL                  | `https://example.com/product/SKU12345`       | Required    | —            | Must resolve with HTTP 200; HTTPS preferred |

### Item Information

Capture the physical characteristics and classification details of the product. This data helps ensure accurate categorization, filtering, and search relevance.

| Attribute        | Data Type | Supported Values                                | Description          | Example                         | Requirement | Dependencies                                                | Validation Rules                    |
| :--------------- | :-------- | :---------------------------------------------- | :------------------- | :------------------------------ | :---------- | :---------------------------------------------------------- | :---------------------------------- |
| condition        | String    | —                                               | Condition of product | `new`                           | Optional    | —                                                           | Lower-case string                   |
| product_category | String    | Category taxonomy                               | Category path        | `Apparel & Accessories > Shoes` | Optional    | —                                                           | Use “>” separator                   |
| brand            | String    | —                                               | Product brand        | `OpenAI`                        | Required    | —                                                           | Max 70 chars                        |
| material         | String    | —                                               | Primary material(s)  | `Leather`                       | Optional    | —                                                           | Max 100 chars                       |
| dimensions       | String    | `LxWxH unit`                                    | Overall dimensions   | `12x8x5 in`                     | Optional    | —                                                           | Units required if provided          |
| length           | String    | —                                               | Individual dimension | `10`                            | Optional    | Provide all three if using individual fields                | Use `dimensions_unit`               |
| width            | String    | —                                               | Individual dimension | `10`                            | Optional    | Provide all three if using individual fields                | Use `dimensions_unit`               |
| height           | String    | —                                               | Individual dimension | `10`                            | Optional    | Provide all three if using individual fields                | Use `dimensions_unit`               |
| dimensions_unit  | String    | —                                               | Dimensions unit      | `in`                            | Optional    | Required if any of `length`, `width`, `height` are provided | Unit abbreviation (e.g. `in`, `cm`) |
| weight           | String    | —                                               | Product weight       | `1.5`                           | Optional    | —                                                           | Use `item_weight_unit`              |
| item_weight_unit | String    | —                                               | Product weight unit  | `lb`                            | Optional    | Required if `weight` is provided                            | Unit abbreviation (e.g. `lb`, `kg`) |
| age_group        | Enum      | `newborn`, `infant`, `toddler`, `kids`, `adult` | Target demographic   | `adult`                         | Optional    | —                                                           | Lower-case string                   |

### Media

Supply visual and rich media assets that represent the product. High-quality images and optional videos or 3D models improve user trust and engagement.

| Attribute             | Data Type | Supported Values | Description            | Example                            | Requirement | Dependencies | Validation Rules            |
| :-------------------- | :-------- | :--------------- | :--------------------- | :--------------------------------- | :---------- | :----------- | :-------------------------- |
| image_url             | URL       | RFC 1738         | Main product image URL | `https://example.com/image1.jpg`   | Required    | —            | JPEG/PNG; HTTPS preferred   |
| additional_image_urls | String    | —                | Extra images           | `https://example.com/image2.jpg,…` | Optional    | —            | Comma-separated list        |
| video_url             | URL       | RFC 1738         | Product video          | `https://youtu.be/12345`           | Optional    | —            | Must be publicly accessible |
| model_3d_url          | URL       | RFC 1738         | 3D model               | `https://example.com/model.glb`    | Optional    | —            | GLB/GLTF preferred          |

### Price & Promotions

Define standard and promotional pricing information. These attributes power price display, discount messaging, and offer comparisons.

| Attribute                           | Data Type         | Supported Values | Description               | Example                    | Requirement | Dependencies | Validation Rules              |
| :---------------------------------- | :---------------- | :--------------- | :------------------------ | :------------------------- | :---------- | :----------- | :---------------------------- |
| price                               | Number + currency | ISO 4217         | Regular price             | `79.99 USD`                | Required    | —            | Must include currency code    |
| sale_price                          | Number + currency | ISO 4217         | Discounted price          | `59.99 USD`                | Optional    | —            | Must be ≤ `price`             |
| sale_price_start_date               | Date              | ISO 8601         | Sale start date           | `2025-07-01`               | Optional    | —            | Must be valid ISO 8601 date   |
| sale_price_end_date                 | Date              | ISO 8601         | Sale end date             | `2025-07-15`               | Optional    | —            | Must be valid ISO 8601 date   |
| unit_pricing_measure / base_measure | Number + unit     | —                | Unit price & base measure | `16 oz / 1 oz`             | Optional    | —            | Both fields required together |
| pricing_trend                       | String            | —                | Lowest price in N months  | `Lowest price in 6 months` | Optional    | —            | Max 80 chars                  |

### Availability & Inventory

Describe current stock levels and key timing signals for product availability. Accurate inventory data ensures users only see items they can actually purchase.

| Attribute         | Data Type         | Supported Values                                                | Description                    | Example      | Requirement                          | Dependencies             | Validation Rules        |
| :---------------- | :---------------- | :-------------------------------------------------------------- | :----------------------------- | :----------- | :----------------------------------- | :----------------------- | :---------------------- |
| availability      | Enum              | `in_stock`, `out_of_stock`, `pre_order`, `backorder`, `unknown` | Product availability           | `in_stock`   | Required                             | —                        | Lower-case string       |
| availability_date | Date              | ISO 8601                                                        | Availability date if pre-order | `2025-12-01` | Required if `availability=pre_order` | —                        | Must be future date     |
| expiration_date   | Date              | ISO 8601                                                        | Remove product after date      | `2025-12-01` | Optional                             | —                        | Must be future date     |
| pickup_method     | Enum              | `in_store`, `reserve`, `not_supported`                          | Pickup options                 | `in_store`   | Optional                             | —                        | Lower-case string       |
| pickup_sla        | Number + duration | —                                                               | Pickup SLA                     | `1 day`      | Optional                             | Requires `pickup_method` | Positive integer + unit |

### Variants

Specify variant relationships and distinguishing attributes such as color or size. These fields allow ChatGPT to group related SKUs and surface variant-specific details.

The group_id value should represent how the product is presented on the merchant’s website (the canonical product page or parent listing shown to customers). If you are submitting variant rows (e.g., by color or size), you must include the same group_id for every variant. Do not submit individual variant SKUs without a group id.

| Attribute                | Data Type           | Supported Values | Description                             | Example                             | Requirement           | Dependencies | Validation Rules               |
| :----------------------- | :------------------ | :--------------- | :-------------------------------------- | :---------------------------------- | :-------------------- | :----------- | :----------------------------- |
| group_id                 | String              | —                | Variant group ID                        | `SHOE123GROUP`                      | Required              | —            | Max 70 chars                   |
| listing_has_variations   | Boolean             | `true`, `false`  | Indicates if the listing has variations | `true`                              | Required              | —            | Lower-case string              |
| variant_dict             | Object              | —                | Variant attributes map                  | `{ "color": "Blue", "size": "10" }` | Optional              | —            | JSON object with string values |
| item_group_title         | String (UTF-8 text) | —                | Group product title                     | `Men's Trail Running Shoes`         | Optional              | —            | Max 150 chars; avoid all-caps  |
| color                    | String              | —                | Variant color                           | `Blue`                              | Optional              | —            | Max 40 chars                   |
| size                     | String              | —                | Variant size                            | `10`                                | Recommended (apparel) | —            | Max 20 chars                   |
| size_system              | Country code        | ISO 3166         | Size system                             | `US`                                | Recommended (apparel) | —            | 2-letter country code          |
| gender                   | String              | —                | Gender target                           | `male`                              | Optional              | —            | Lower-case string              |
| offer_id                 | String              | —                | Offer ID (SKU+seller+price)             | `SKU12345-Blue-79.99`               | Recommended           | —            | Unique within feed             |
| Custom_variant1_category | String              | —                | Custom variant dimension 1              | Size_Type                           | Optional              | —            | —                              |
| Custom_variant1_option   | String              | —                | Custom variant 1 option                 | Petite / Tall / Maternity           | Optional              | —            | —                              |
| Custom_variant2_category | String              | —                | Custom variant dimension 2              | Wood_Type                           | Optional              | —            | —                              |
| Custom_variant2_option   | String              | —                | Custom variant 2 option                 | Oak / Mahogany / Walnut             | Optional              | —            | —                              |
| Custom_variant3_category | String              | —                | Custom variant dimension 3              | Cap_Type                            | Optional              | —            | —                              |
| Custom_variant3_option   | String              | —                | Custom variant 3 option                 | Snapback / Fitted                   | Optional              | —            | —                              |

### Fulfillment

Outline shipping methods, costs, and estimated delivery times. Providing detailed shipping information helps users understand fulfillment options upfront.

| Attribute         | Data Type | Supported Values                   | Description                         | Example                     | Requirement | Dependencies | Validation Rules                               |
| :---------------- | :-------- | :--------------------------------- | :---------------------------------- | :-------------------------- | :---------- | :----------- | :--------------------------------------------- |
| shipping_price    | String    | country:region:service_class:price | Shipping method/cost/region         | `US:CA:Overnight:16.00 USD` | Optional    | —            | Multiple entries allowed; use colon separators |
| delivery_estimate | Date      | ISO 8601                           | Estimated arrival date              | `2025-08-12`                | Optional    | —            | Must be future date                            |
| is_digital        | Boolean   | `true`, `false`                    | Indicates if the product is digital | `false`                     | Optional    | —            | Lower-case string                              |

### Merchant Info

Identify the seller and link to any relevant merchant policies or storefront pages. This ensures proper attribution and enables users to review seller credentials.

Note about 3P sellers and marketplaces: If your feed contains products that are shipped with 3rd party sellers, please also include a marketplace_seller in your feed. The marketplace_seller would be the point of checkout in this scenario, and the seller_name would be the shipment fulfiller.

| Attribute             | Data Type | Supported Values | Description                      | Example                       | Requirement                              | Dependencies | Validation Rules |
| :-------------------- | :-------- | :--------------- | :------------------------------- | :---------------------------- | :--------------------------------------- | :----------- | :--------------- |
| seller_name           | String    | —                | Seller name                      | `Example Store`               | Required / Display                       | —            | Max 70 chars     |
| marketplace_seller    | String    | —                | Marketplace seller of record     | `Marketplace Name`            | Optional                                 | —            | Max 70 chars     |
| seller_url            | URL       | RFC 1738         | Seller page                      | `https://example.com/store`   | Required                                 | —            | HTTPS preferred  |
| seller_privacy_policy | URL       | RFC 1738         | Seller-specific policies         | `https://example.com/privacy` | Required if is_eligible_checkout is true | —            | HTTPS preferred  |
| seller_tos            | URL       | RFC 1738         | Seller-specific terms of service | `https://example.com/terms`   | Required if is_eligible_checkout is true | —            | HTTPS preferred  |

### Returns

Provide return policies and time windows to set clear expectations for buyers. Transparent return data builds trust and reduces post-purchase confusion.

Use `return_deadline_in_days` as the canonical field for return windows in the feed schema.

| Attribute               | Data Type | Supported Values | Description             | Example                       | Requirement | Dependencies | Validation Rules  |
| :---------------------- | :-------- | :--------------- | :---------------------- | :---------------------------- | :---------- | :----------- | :---------------- |
| accepts_returns         | Boolean   | `true`, `false`  | Accepts returns         | `true`                        | Optional    | —            | Lower-case string |
| return_deadline_in_days | Integer   | Days             | Days allowed for return | `30`                          | Optional    | —            | Positive integer  |
| accepts_exchanges       | Boolean   | `true`, `false`  | Accepts exchanges       | `false`                       | Optional    | —            | Lower-case string |
| return_policy           | URL       | RFC 1738         | Return policy URL       | `https://example.com/returns` | Required    | —            | HTTPS preferred   |

### Performance Signals

Share popularity and return-rate metrics where available. These signals can be used to enhance ranking and highlight high-performing products.

| Attribute        | Data Type | Supported Values | Description          | Example | Requirement | Dependencies | Validation Rules              |
| :--------------- | :-------- | :--------------- | :------------------- | :------ | :---------- | :----------- | :---------------------------- |
| popularity_score | Number    | —                | Popularity indicator | `4.7`   | Recommended | —            | 0–5 scale or merchant-defined |
| return_rate      | Number    | Percentage       | Return rate          | `2%`    | Recommended | —            | 0–100%                        |

### Compliance

Include regulatory warnings, disclaimers, or age restrictions. Compliance fields help meet legal obligations and protect consumers.

| Attribute             | Data Type    | Supported Values | Description          | Example                                           | Requirement              | Dependencies | Validation Rules              |
| :-------------------- | :----------- | :--------------- | :------------------- | :------------------------------------------------ | :----------------------- | :----------- | :---------------------------- |
| warning / warning_url | String / URL | —                | Product disclaimers  | `Contains lithium battery, or CA Prop 65 warning` | Recommended for Checkout | —            | If URL, must resolve HTTP 200 |
| age_restriction       | Number       | —                | Minimum purchase age | `21`                                              | Recommended              | —            | Positive integer              |

### Reviews and Q&A

Supply aggregated review statistics and frequently asked questions. User-generated insights strengthen credibility and help shoppers make informed decisions.

| Attribute          | Data Type | Supported Values | Description                   | Example                                                                                              | Requirement | Dependencies | Validation Rules                                                                                                     |
| :----------------- | :-------- | :--------------- | :---------------------------- | :--------------------------------------------------------------------------------------------------- | :---------- | :----------- | :------------------------------------------------------------------------------------------------------------------- |
| review_count       | Integer   | —                | Number of product reviews     | `254`                                                                                                | Optional    | —            | Non-negative                                                                                                         |
| star_rating        | String    | —                | Average review score          | `4.50`                                                                                               | Optional    | —            | 0–5 scale                                                                                                            |
| store_review_count | Integer   | —                | Number of brand/store reviews | `2000`                                                                                               | Optional    | —            | Non-negative                                                                                                         |
| store_star_rating  | String    | —                | Average store rating          | `4.50`                                                                                               | Optional    | —            | 0–5 scale                                                                                                            |
| q_and_a            | List      | —                | FAQ content                   | `[{ "q": "Is this waterproof?", "a": "Yes" }]`                                                       | Recommended | —            | List of `{ "q": string, "a": string }` objects                                                                       |
| reviews            | List      | —                | Review entries                | `[{ "title": "Love these", "content": "Great grip.", "minRating": 1, "maxRating": 5, "rating": 5 }]` | Recommended | —            | List of `{ "title": string, "content": string, "minRating": number, "maxRating": number, "rating": number }` objects |

### Related Products

List products that are commonly bought together or act as substitutes. This enables basket-building recommendations and cross-sell opportunities.

| Attribute          | Data Type | Supported Values                                                                                  | Description            | Example       | Requirement | Dependencies | Validation Rules             |
| :----------------- | :-------- | :------------------------------------------------------------------------------------------------ | :--------------------- | :------------ | :---------- | :----------- | :--------------------------- |
| related_product_id | String    | —                                                                                                 | Associated product IDs | `SKU67890`    | Recommended | —            | Comma-separated list allowed |
| relationship_type  | Enum      | `part_of_set`, `required_part`, `often_bought_with`, `substitute`, `different_brand`, `accessory` | Relationship type      | `part_of_set` | Recommended | —            | Lower-case string            |

### Geo Tagging

Indicate any region-specific pricing or availability overrides. Geo data allows ChatGPT to present accurate offers and stock status by location.

| Attribute        | Data Type         | Supported Values             | Description                                     | Example                                     | Requirement | Dependencies | Validation Rules                     |
| :--------------- | :---------------- | :--------------------------- | :---------------------------------------------- | :------------------------------------------ | :---------- | :----------- | :----------------------------------- |
| target_countries | List              | `US`                         | Target countries of the item (first entry used) | `US`                                        | Required    | —            | Use ISO 3166-1 alpha-2 codes         |
| store_country    | String            | `US`                         | Store country of the item                       | `US`                                        | Required    | —            | Use ISO 3166-1 alpha-2 codes         |
| geo_price        | Number + currency | Region-specific price        | Price by region                                 | `79.99 USD (California)`                    | Recommended | —            | Must include ISO 4217 currency       |
| geo_availability | String            | Region-specific availability | Availability per region                         | `in_stock (Texas), out_of_stock (New York)` | Recommended | —            | Regions must be valid ISO 3166 codes |

## Prohibited Products Policy

To keep ChatGPT a safe place for everyone, we only allow products and services that are legal, safe, and appropriate for a general audience. Prohibited products include, but are not limited to, those that involve adult content, age-restricted products (e.g., alcohol, nicotine, gambling), harmful or dangerous materials, weapons, prescription only medications, unlicensed financial products, legally restricted goods, illegal activities, or deceptive practices.

Merchants are responsible for ensuring their products and content do not violate the above restrictions or any applicable law. OpenAI may take corrective actions such as removing a product or banning a seller from being surfaced in ChatGPT if these policies are violated.

</div>