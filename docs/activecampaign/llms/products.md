# Source: https://developers.activecampaign.com/reference/products.md

# Products

# Products

ActiveCampaign can store product catalog data from your ecommerce store.

### Base Products and Variants

ActiveCampaign stores product variants as separate products. For example, some systems may show a product with variants in the following JSON:

```Text JSON
{
   "name": "Shoes",
   "variants": [
     {
       "variantName": "Red Shoes",
       "sku": "abc123"
     },
     {
       "variantName": "Blue Shoes",
       "sku": "xyz890"
     }  
  ]
}
```

This would be stored in the ActiveCampaign model as two products in this GraphQL request:

```Text GraphQL
mutation {
  bulkUpsertProducts(
    products: [
    {
	 	 	baseProductName: "Shoes",
   		variantName: "Red Shoes",
   		variantSku: "abc123"
    }
    {
       baseProductName: "Shoes",
       variantName: "Blue Shoes",
       variantSku: "xyz890"
    }
	])
	{
    id
	}
}
```

Note that for both of these, the `baseProductName`is the same. All fields in the Product data model prefixed with `baseProduct` will be duplicated across all variants of that base product.

## Connection Identifiers

Various product objects in the API use `legacyConnectionId` to identify which integration products they are associated with. `legacyConnectionId` is an integer identifier that matches the `id` field of the [V3 Connection API](https://dash.readme.com/project/activecampaign/v3/refs/get-connection). Aside from being able to retrieve this identifier from the connection API, you can find this identifier on your integrations page. If you click into the details of any integration, you will see a URL such as `https://youraccount.activehosted.com/app/settings/integrations/9`. The number at the end of this URL (in this case: `9`) is your `legacyConnectionId`.

## Primary Product Identifiers

A product is identified based on two pieces of data: `legacyConnectionId` and `storePrimaryId`. Within any given connection (that is, within a `legacyConnectionId`), only one product may exist with a given `storePrimaryId`.

If API users attempt to create a duplicate product with the same `storePrimaryId`/`legacyConnectionId` combination using the `createProductApi`, a validation error will be returned.

When the `bulkUpsertProducts` API is used, any writes that use an already existing `storePrimaryId`/`legacyConnectionId` combination will update the existing product. If no product with a `storePrimaryId` exists under a `legacyConnectionId`, then a new product will be inserted.

For the `bulkUpsertProducts` operation, if two or more products in the request body have the same `storePrimaryId` and `legacyConnectionId`, a validation error will not be returned. The API will deduplicate the entries. It will retain one instance and exclude the others from execution.

## Patch-Style operations

All updates and upserts on the Product API are [patch](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/PATCH)-style operations. In other words, if you send this product:

```Text graphQL
mutation {
  bulkUpsertProducts(
    products: [
    {
      storePrimaryId: "shoezy"
      legacyConnectionId: 5
	 	 	baseProductName: "Shoes"
   		variantName: "Red Shoes"
   		variantSku: "abc123"
    }
	])
	{
    id
	}
}
```

Then the fields `baseProductName` `variantName`, and `variantSku` will all be updated for the product with storePrimaryId `shoezy` in the store with legacyConnectionId `5`. No other fields on the product will be updated.

To set a field (for example, `baseProductName`) to null, simply pass a null value for that field:

```
mutation {
  bulkUpsertProducts(
    products: [
    {
      storePrimaryId: "shoezy"
      legacyConnectionId: 5
	 	 	baseProductName: null
    }
	])
	{
    id
	}
}
```

# Queries

## productById

**Type**: Product

**Arguments for`productById`**

| Name        | Description       |
| :---------- | :---------------- |
| id (string) | the product's id. |

## searchProduct

For information on how filters and search requests work, see: [Searches](https://developers.activecampaign.com/reference/searches).

**Type**: Product

**Arguments for`searchProduct`**

| Name                   | Description         |
| :--------------------- | :------------------ |
| filter (ProductFilter) | the product filter. |

# Mutations

## createProduct

#### Input fields for `createProduct`

`product` (`ProductInput`)

#### Return fields for `createProduct`

| Name                                         | Description                                |
| :------------------------------------------- | :----------------------------------------- |
| id (`String!`)                               | The id of the product.                     |
| storePrimaryId (`String`)                    | The primary id of the store.               |
| storeBaseProductId (`String`)                | The store id of the product.               |
| baseProductName (`String`)                   | The name of the product.                   |
| baseProductDescription (`String`)            | The description of the product.            |
| baseProductStoreCreatedDate (`String`)       | The created date of the product.           |
| baseProductStoreModifiedDate (`String`)      | The last modified date of the product.     |
| tags (`String`)                              | The tags associated with the product.      |
| categories (`String`)                        | The categories of the product.             |
| baseProductImages (`ImageData`)              | The product's images.                      |
| baseProductUrl (`String`)                    | The product's URL.                         |
| baseProductUrlSlug (`String`)                | The product's URL slug.                    |
| baseProductDimensions (`PhysicalDimensions`) | The product's physical dimensions.         |
| baseProductWeight (`BigDecimal`)             | The product's weight.                      |
| dimensionsUnit (`DimensionsUnit`)            | The unit of the product's dimensions.      |
| variantSku (`String`)                        | The product variant's SKU.                 |
| variantName (`String`)                       | The product variant's name.                |
| variantDescription (`String`)                | The product variant's description.         |
| variantPriceCurrency (`String`)              | The product variant's currency.            |
| variantPriceAmount (`BigDecimal`)            | The product variant's price.               |
| variantStoreCreatedDate (`String`)           | The created date of the product variant.   |
| variantStoreModifiedDate (`String`)          | The modified date of the product variant.  |
| variantImages (`ImageData`)                  | The product variant's images.              |
| variantUrl (`String`)                        | The product variant's URL.                 |
| variantUrlSlug (`String`)                    | The product variant's URL slug.            |
| variantDimensions (`PhysicalDimensions`)     | The product variant's physical dimensions. |
| variantWeight (`BigDecimal`)                 | The product variant's weight.              |
| type (`String`)                              | The product's type                         |
| status (`String`)                            | The product's status                       |
| ups (`String`)                               | The product's ups.                         |
| isDeleted (`Boolean`)                        | Is the product deleted?                    |
| numberOfSales (`Int`)                        | Number of sales of the product.            |
| isVirtual (`Boolean`)                        | Is the product virtual?                    |
| isDownloadable (`Boolean`)                   | Is the product downloadable?               |
| isVisible (`Boolean`)                        | Is the product visible?                    |
| isOnSale (`Boolean`)                         | Is the product on sale?                    |
| isBackordersAllowed (`Boolean`)              | Are backorders allowed for the product?    |
| stockStatus (`StockStatus`)                  | The product's stock status.                |
| averageRatings (`BigDecimal`)                | The product's average rating.              |
| ratingCount (`Int`)                          | The number of ratings for the product.     |
| brand (`string`)                             | The product's brand.                       |
| searchKeywords (`String`)                    | The product's search keywords.             |
| condition (`String`)                         | The condition of the product.              |
| viewCount (`Int`)                            | The number of product views.               |
| attributes (`JSON`)                          | The product's attributes.                  |

## updateProduct

#### Input fields for `updateProduct`

`id` (`String`)

`product` (`ProductInput`)

#### Return fields for `updateProduct`

| Name                                         | Description                                |
| :------------------------------------------- | :----------------------------------------- |
| id (`String!`)                               | The id of the product.                     |
| storeBaseProductId (`String`)                | The store id of the product.               |
| baseProductName (`String`)                   | The name of the product.                   |
| baseProductDescription (`String`)            | The description of the product.            |
| baseProductStoreCreatedDate (`String`)       | The created date of the product.           |
| baseProductStoreModifiedDate (`String`)      | The last modified date of the product.     |
| tags (`String`)                              | The tags associated with the product.      |
| categories (`String`)                        | The categories of the product.             |
| baseProductImages (`ImageData`)              | The product's images.                      |
| baseProductUrl (`String`)                    | The product's URL.                         |
| baseProductUrlSlug (`String`)                | The product's URL slug.                    |
| baseProductDimensions (`PhysicalDimensions`) | The product's physical dimensions.         |
| baseProductWeight (`BigDecimal`)             | The product's weight.                      |
| dimensionsUnit (`DimensionsUnit`)            | The unit of the product's dimensions.      |
| storePrimaryId (`String`)                    | The primary id of the store.               |
| variantSku (`String`)                        | The product variant's SKU.                 |
| variantName (`String`)                       | The product variant's name.                |
| variantDescription (`String`)                | The product variant's description.         |
| variantPriceCurrency (`String`)              | The product variant's currency.            |
| variantPriceAmount (`BigDecimal`)            | The product variant's price.               |
| variantStoreCreatedDate (`String`)           | The created date of the product variant.   |
| variantStoreModifiedDate (`String`)          | The modified date of the product variant.  |
| variantImages (`ImageData`)                  | The product variant's images.              |
| variantUrl (`String`)                        | The product variant's URL.                 |
| variantUrlSlug (`String`)                    | The product variant's URL slug.            |
| variantDimensions (`PhysicalDimensions`)     | The product variant's physical dimensions. |
| variantWeight (`BigDecimal`)                 | The product variant's weight.              |
| type (`String`)                              | The product's type                         |
| status (`String`)                            | The product's status                       |
| ups (`String`)                               | The product's ups.                         |
| isDeleted (`Boolean`)                        | Is the product deleted?                    |
| numberOfSales (`Int`)                        | Number of sales of the product.            |
| isVirtual (`Boolean`)                        | Is the product virtual?                    |
| isDownloadable (`Boolean`)                   | Is the product downloadable?               |
| isVisible (`Boolean`)                        | Is the product visible?                    |
| isOnSale (`Boolean`)                         | Is the product on sale?                    |
| isBackordersAllowed (`Boolean`)              | Are backorders allowed for the product?    |
| stockStatus (`StockStatus`)                  | The product's stock status.                |
| averageRatings (`BigDecimal`)                | The product's average rating.              |
| ratingCount (`Int`)                          | The number of ratings for the product.     |
| brand (`string`)                             | The product's brand.                       |

## deleteProduct

#### Input fields for `deleteProduct`

`id` (`String`)

## bulkUpsertProducts

#### Input fields for `bulkUpsertProducts`

`products` (`ProductInput`)

#### Return fields for `bulkUpsertProducts`

| Name                                         | Description                                |
| :------------------------------------------- | :----------------------------------------- |
| id (`String!`)                               | The id of the product.                     |
| storeBaseProductId (`String`)                | The store id of the product.               |
| baseProductName (`String`)                   | The name of the product.                   |
| baseProductDescription (`String`)            | The description of the product.            |
| baseProductStoreCreatedDate (`String`)       | The created date of the product.           |
| baseProductStoreModifiedDate (`String`)      | The last modified date of the product.     |
| tags (`String`)                              | The tags associated with the product.      |
| categories (`String`)                        | The categories of the product.             |
| baseProductImages (`ImageData`)              | The product's images.                      |
| baseProductUrl (`String`)                    | The product's URL.                         |
| baseProductUrlSlug (`String`)                | The product's URL slug.                    |
| baseProductDimensions (`PhysicalDimensions`) | The product's physical dimensions.         |
| baseProductWeight (`BigDecimal`)             | The product's weight.                      |
| dimensionsUnit (`DimensionsUnit`)            | The unit of the product's dimensions.      |
| storePrimaryId (`String`)                    | The primary id of the store.               |
| variantSku (`String`)                        | The product variant's SKU.                 |
| variantName (`String`)                       | The product variant's name.                |
| variantDescription (`String`)                | The product variant's description.         |
| variantPriceCurrency (`String`)              | The product variant's currency.            |
| variantPriceAmount (`BigDecimal`)            | The product variant's price.               |
| variantStoreCreatedDate (`String`)           | The created date of the product variant.   |
| variantStoreModifiedDate (`String`)          | The modified date of the product variant.  |
| variantImages (`ImageData`)                  | The product variant's images.              |
| variantUrl (`String`)                        | The product variant's URL.                 |
| variantUrlSlug (`String`)                    | The product variant's URL slug.            |
| variantDimensions (`PhysicalDimensions`)     | The product variant's physical dimensions. |
| variantWeight (`BigDecimal`)                 | The product variant's weight.              |
| type (`String`)                              | The product's type                         |
| status (`String`)                            | The product's status                       |
| ups (`String`)                               | The product's ups.                         |
| isDeleted (`Boolean`)                        | Is the product deleted?                    |
| numberOfSales (`Int`)                        | Number of sales of the product.            |
| isVirtual (`Boolean`)                        | Is the product virtual?                    |
| isDownloadable (`Boolean`)                   | Is the product downloadable?               |
| isVisible (`Boolean`)                        | Is the product visible?                    |
| isOnSale (`Boolean`)                         | Is the product on sale?                    |
| isBackordersAllowed (`Boolean`)              | Are backorders allowed for the product?    |
| stockStatus (`StockStatus`)                  | The product's stock status.                |
| averageRatings (`BigDecimal`)                | The product's average rating.              |
| ratingCount (`Int`)                          | The number of ratings for the product.     |
| brand (`string`)                             | The product's brand.                       |

# Objects

### Base Product Fields

ActiveCampaign stores product variants as separate products. For example, some systems may show a product with variants in the following JSON:

```
{
   "name": "Shoes",
   "variants": [
     {
       "variantName": "Red Shoes",
       "sku": "abc123"
     },
     {
       "variantName": "Blue Shoes",
       "sku": "xyz890"
     }  
  ]
}
```

This would be stored in the ActiveCampaign model as two products in this GraphQL request:

```
mutation {
  bulkUpsertProducts(
    products: [
    {
	 	 	baseProductName: "Shoes",
   		variantName: "Red Shoes",
   		variantSku: "abc123"
    }
    {
       baseProductName: "Shoes",
       variantName: "Blue Shoes",
       variantSku: "xyz890"
    }
	])
	{
    id
	}
}
```

Note that for both of these, the `baseProductName`is the same. All fields in the Product data model prefixed with `baseProduct` will be duplicated across all variants of that base product.

<br />

If two or more products are contain duplicates using same `legacyConnectionId` and `storePrimaryId`the API will deduplicate the entries. It will retain one instance and exclude the others from execution.

**Example:**

**Request:**

```
mutation {
  bulkUpsertProducts(
    products: [
    {
    	legacyConnectionId: 1,
    	storePrimaryId: "123",
	 	 	baseProductName: "Shoes",
   		variantName: "Red Shoes",
   		variantSku: "abc123"
    }
    {
      legacyConnectionId: 1,
    	storePrimaryId: "123",
      baseProductName: "Shoes",
      variantName: "Blue Shoes",
      variantSku: "xyz890"
    }
	])
	{
    legacyConnectionId
    storeBaseProductId
    baseProductName
    variantName
    variantSku
	}
}
```

<br />

**Response:**

```
{
    "data": {
        "bulkUpsertProducts": [
            {
                "legacyConnectionId": 1,
                "baseProductName": "Shoes",
                "variantName": "Red Shoes",
                "variantSku": "abc123"
            }
        ]
    }
}
```

### Product Input

| Name                                         | Description                                                                                                                                                                                           |
| :------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id (`String!`)                               | The id of the product, a randomly generated GUID.                                                                                                                                                     |
| legacyConnectionId  (`Int!`)  **Required**   | Integer connection identifier matching the v3 API DeepData Connection ID.                                                                                                                             |
| storePrimaryId (`String`) **Required**       | Primary identifier for this product within a store. Must be unique within the scope of a single store. For stores with variants, the `storePrimaryId`is generally a unique identifier on the variant. |
| storeBaseProductId (`String`)                | The store's primary unique identifier for the base/parent product.                                                                                                                                    |
| baseProductName (`String`)                   | Product name for the base product.                                                                                                                                                                    |
| baseProductDescription (`String`)            | Product description for the base product.                                                                                                                                                             |
| baseProductStoreCreatedDate (`String`)       | Date the base product was created in the store.  Must be in format 2019-11-16T10:48:23Z                                                                                                               |
| baseProductStoreModifiedDate (`String`)      | Date the base product was last modified in the store.  Must be in format 2019-11-16T10:48:23Z                                                                                                         |
| baseProductImages (`ImageData[]`)            | Image data for base product.                                                                                                                                                                          |
| baseProductUrl (`String`)                    | URL for the base product.                                                                                                                                                                             |
| baseProductUrlSlug (`String`)                | URL slug for the base product.                                                                                                                                                                        |
| baseProductDimensions (`PhysicalDimensions`) | Dimensions for the base product.                                                                                                                                                                      |
| baseProductWeight (`BigDecimal`)             | Weight of the base product.                                                                                                                                                                           |
| tags (`String[]`)                            | The tags associated with the product.                                                                                                                                                                 |
| categories (`String[]`)                      | The categories associated with the product.                                                                                                                                                           |
| dimensionsUnit (`DimensionsUnit`)            | The unit of the product's dimensions. Either `METRIC` or `IMPERIAL`                                                                                                                                   |
| variantSku (`String`)                        | Stock Keeping Unit (SKU) for the product variant.                                                                                                                                                     |
| variantName (`String`)                       | The product variant's name.                                                                                                                                                                           |
| variantDescription (`String`)                | The product variant's description.                                                                                                                                                                    |
| variantPriceCurrency (`String`)              | Currency related to all prices of the product variant.                                                                                                                                                |
| variantPriceAmount (`BigDecimal`)            | The product variant's price.                                                                                                                                                                          |
| variantStoreCreatedDate (`String`)           | Date the product variant was created in the store.  Must be in format 2019-11-16T10:48:23Z                                                                                                            |
| variantStoreModifiedDate (`String`)          | Date the product variant was last modified in the store.  Must be in format 2019-11-16T10:48:23Z                                                                                                      |
| variantImages (`ImageData`)                  | The product variant's images.                                                                                                                                                                         |
| variantUrl (`String`)                        | The product variant's URL.                                                                                                                                                                            |
| variantUrlSlug (`String`)                    | The product variant's URL slug.                                                                                                                                                                       |
| variantDimensions (`PhysicalDimensions`)     | The product variant's physical dimensions.                                                                                                                                                            |
| variantWeight (`BigDecimal`)                 | The product variant's weight.                                                                                                                                                                         |
| type (`String`)                              | Type of product (e.g. physical, digital, etc.)                                                                                                                                                        |
| status (`String`)                            | The product's status (e.g. published, hidden, etc.)                                                                                                                                                   |
| upc (`String`)                               | The product's upc.                                                                                                                                                                                    |
| isDeleted (`Boolean`)                        | Is the product deleted?                                                                                                                                                                               |
| numberOfSales (`Int`)                        | Number of sales of the product.                                                                                                                                                                       |
| isVirtual (`Boolean`)                        | Is the product virtual?                                                                                                                                                                               |
| isDownloadable (`Boolean`)                   | Is the product downloadable?                                                                                                                                                                          |
| isVisible (`Boolean`)                        | Is the product visible?                                                                                                                                                                               |
| isOnSale (`Boolean`)                         | Is the product on sale?                                                                                                                                                                               |
| isBackordersAllowed (`Boolean`)              | Are backorders allowed for the product?                                                                                                                                                               |
| stockStatus (`StockStatus`)                  | The product's stock status. One of: `IN_STOCK` `OUT_OF_STOCK` `BACKORDER`                                                                                                                             |
| averageRatings (`BigDecimal`)                | The product's average rating.                                                                                                                                                                         |
| ratingCount (`Int`)                          | The number of ratings for the product.                                                                                                                                                                |
| brand (`string`)                             | The product's brand (also known as vendor).                                                                                                                                                           |

### Product Filter

| Name                                               | Description                                                                                      |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| pagination (Pagination)                            | Pagination data for search request.                                                              |
| legacyConnectionId  (`IntFieldFilter`)             | Integer connection identifier matching the v3 API DeepData Connection ID.                        |
| storeBaseProductId (`StringFieldFilter`)           | The store's primary unique identifier for the base/parent product.                               |
| baseProductName (`StringFieldFilter`)              | Product name for the base product.                                                               |
| baseProductDescription (`StringFieldFilter`)       | Product description for the base product.                                                        |
| baseProductStoreCreatedDate (`StringFieldFilter`)  | Date the base product was created in the store.  Must be in format 2019-11-16T10:48:23Z          |
| baseProductStoreModifiedDate (`StringFieldFilter`) | Date the base product was last modified in the store.  Must be in format 2019-11-16T10:48:23Z    |
| baseProductUrl (`StringFieldFilter`)               | URL for the base product.                                                                        |
| baseProductUrlSlug (`StringFieldFilter`)           | URL slug for the base product.                                                                   |
| baseProductDimensions (`PhysicalDimensionsInput`)  | Dimensions for the base product.                                                                 |
| baseProductWeight (`NumberFieldFilter`)            | Weight of the base product.                                                                      |
| tags (`StringFieldFilter[]`)                       | The tags associated with the product.                                                            |
| categories (`StringFieldFilter[]`)                 | The categories associated with the product.                                                      |
| dimensionsUnit (`DimensionsUnit`)                  | The unit of the product's dimensions. Either `METRIC` or `IMPERIAL`                              |
| variantSku (`StringFieldFilter`)                   | Stock Keeping Unit (SKU) for the product variant.                                                |
| variantName (`StringFieldFilter`)                  | The product variant's name.                                                                      |
| variantDescription (`StringFieldFilter`)           | The product variant's description.                                                               |
| variantPriceCurrency (`StringFieldFilter`)         | Currency related to all prices of the product variant.                                           |
| variantPriceAmount (`NumberFieldFilter`)           | The product variant's price.                                                                     |
| variantStoreCreatedDate (`StringFieldFilter`)      | Date the product variant was created in the store.  Must be in format 2019-11-16T10:48:23Z       |
| variantStoreModifiedDate (`StringFieldFilter`)     | Date the product variant was last modified in the store.  Must be in format 2019-11-16T10:48:23Z |
| variantUrl (`StringFieldFilter`)                   | The product variant's URL.                                                                       |
| variantUrlSlug (`StringFieldFilter`)               | The product variant's URL slug.                                                                  |
| variantDimensions (`PhysicalDimensions`)           | The product variant's physical dimensions.                                                       |
| variantWeight (`BigDecimal`)                       | The product variant's weight.                                                                    |
| type (`StringFieldFilter`)                         | Type of product (e.g. physical, digital, etc.)                                                   |
| status (`StringFieldFilter`)                       | The product's status (e.g. published, hidden, etc.)                                              |
| upc (`StringFieldFilter`)                          | The product's upc.                                                                               |
| isDeleted (`BooleanFieldFilter`)                   | Is the product deleted?                                                                          |
| numberOfSales (`IntFieldFilter`)                   | Number of sales of the product.                                                                  |
| isVirtual (`BooleanFieldFilter`)                   | Is the product virtual?                                                                          |
| isDownloadable (`BooleanFieldFilter`)              | Is the product downloadable?                                                                     |
| isVisible (`BooleanFieldFilter`)                   | Is the product visible?                                                                          |
| isOnSale (`BooleanFieldFilter`)                    | Is the product on sale?                                                                          |
| isBackordersAllowed (`BooleanFieldFilter`)         | Are backorders allowed for the product?                                                          |
| stockStatus (`StockStatusFieldFilter`)             | The product's stock status. One of: `IN_STOCK` `OUT_OF_STOCK` `BACKORDER`                        |
| averageRatings (`NumberFieldFilter`)               | The product's average rating.                                                                    |
| ratingCount (`IntFieldFilter`)                     | The number of ratings for the product.                                                           |
| brand (`StringFieldFilter`)                        | The product's brand (also known as vendor).                                                      |

## Product Input

| Name                                         | Description                                                                                                                                                                                           |
| :------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id (`String!`)                               | The id of the product, a randomly generated GUID.                                                                                                                                                     |
| legacyConnectionId  (`Int!`)  **Required**   | Integer connection identifier matching the v3 API DeepData Connection ID.                                                                                                                             |
| storePrimaryId (`String`) **Required**       | Primary identifier for this product within a store. Must be unique within the scope of a single store. For stores with variants, the `storePrimaryId`is generally a unique identifier on the variant. |
| storeBaseProductId (`String`)                | The store's primary unique identifier for the base/parent product.                                                                                                                                    |
| baseProductName (`String`)                   | Product name for the base product.                                                                                                                                                                    |
| baseProductDescription (`String`)            | Product description for the base product.                                                                                                                                                             |
| baseProductStoreCreatedDate (`String`)       | Date the base product was created in the store.  Must be in format 2019-11-16T10:48:23Z                                                                                                               |
| baseProductStoreModifiedDate (`String`)      | Date the base product was last modified in the store.  Must be in format 2019-11-16T10:48:23Z                                                                                                         |
| baseProductImages (`ImageData[]`)            | Image data for base product.                                                                                                                                                                          |
| baseProductUrl (`String`)                    | URL for the base product.                                                                                                                                                                             |
| baseProductUrlSlug (`String`)                | URL slug for the base product.                                                                                                                                                                        |
| baseProductDimensions (`PhysicalDimensions`) | Dimensions for the base product.                                                                                                                                                                      |
| baseProductWeight (`BigDecimal`)             | Weight of the base product.                                                                                                                                                                           |
| tags (`String[]`)                            | The tags associated with the product.                                                                                                                                                                 |
| categories (`String[]`)                      | The categories associated with the product.                                                                                                                                                           |
| dimensionsUnit (`DimensionsUnit`)            | The unit of the product's dimensions. Either `METRIC` or `IMPERIAL`                                                                                                                                   |
| variantSku (`String`)                        | Stock Keeping Unit (SKU) for the product variant.                                                                                                                                                     |
| variantName (`String`)                       | The product variant's name.                                                                                                                                                                           |
| variantDescription (`String`)                | The product variant's description.                                                                                                                                                                    |
| variantPriceCurrency (`String`)              | Currency related to all prices of the product variant.                                                                                                                                                |
| variantPriceAmount (`BigDecimal`)            | The product variant's price.                                                                                                                                                                          |
| variantStoreCreatedDate (`String`)           | Date the product variant was created in the store.  Must be in format 2019-11-16T10:48:23Z                                                                                                            |
| variantStoreModifiedDate (`String`)          | Date the product variant was last modified in the store.  Must be in format 2019-11-16T10:48:23Z                                                                                                      |
| variantImages (`ImageData`)                  | The product variant's images.                                                                                                                                                                         |
| variantUrl (`String`)                        | The product variant's URL.                                                                                                                                                                            |
| variantUrlSlug (`String`)                    | The product variant's URL slug.                                                                                                                                                                       |
| variantDimensions (`PhysicalDimensions`)     | The product variant's physical dimensions.                                                                                                                                                            |
| variantWeight (`BigDecimal`)                 | The product variant's weight.                                                                                                                                                                         |
| type (`String`)                              | Type of product (e.g. physical, digital, etc.)                                                                                                                                                        |
| status (`String`)                            | The product's status (e.g. published, hidden, etc.)                                                                                                                                                   |
| upc (`String`)                               | The product's upc.                                                                                                                                                                                    |
| isDeleted (`Boolean`)                        | Is the product deleted?                                                                                                                                                                               |
| numberOfSales (`Int`)                        | Number of sales of the product.                                                                                                                                                                       |
| isVirtual (`Boolean`)                        | Is the product virtual?                                                                                                                                                                               |
| isDownloadable (`Boolean`)                   | Is the product downloadable?                                                                                                                                                                          |
| isVisible (`Boolean`)                        | Is the product visible?                                                                                                                                                                               |
| isOnSale (`Boolean`)                         | Is the product on sale?                                                                                                                                                                               |
| isBackordersAllowed (`Boolean`)              | Are backorders allowed for the product?                                                                                                                                                               |
| stockStatus (`StockStatus`)                  | The product's stock status. One of: `IN_STOCK` `OUT_OF_STOCK` `BACKORDER`                                                                                                                             |
| averageRatings (`BigDecimal`)                | The product's average rating.                                                                                                                                                                         |
| ratingCount (`Int`)                          | The number of ratings for the product.                                                                                                                                                                |
| brand (`string`)                             | The product's brand (also known as vendor).                                                                                                                                                           |

### Product Filter

| Name                                               | Description                                                                                      |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| pagination (Pagination)                            | Pagination data for search request.                                                              |
| legacyConnectionId  (`IntFieldFilter`)             | Integer connection identifier matching the v3 API DeepData Connection ID.                        |
| storeBaseProductId (`StringFieldFilter`)           | The store's primary unique identifier for the base/parent product.                               |
| baseProductName (`StringFieldFilter`)              | Product name for the base product.                                                               |
| baseProductDescription (`StringFieldFilter`)       | Product description for the base product.                                                        |
| baseProductStoreCreatedDate (`StringFieldFilter`)  | Date the base product was created in the store.  Must be in format 2019-11-16T10:48:23Z          |
| baseProductStoreModifiedDate (`StringFieldFilter`) | Date the base product was last modified in the store.  Must be in format 2019-11-16T10:48:23Z    |
| baseProductUrl (`StringFieldFilter`)               | URL for the base product.                                                                        |
| baseProductUrlSlug (`StringFieldFilter`)           | URL slug for the base product.                                                                   |
| baseProductDimensions (`PhysicalDimensionsInput`)  | Dimensions for the base product.                                                                 |
| baseProductWeight (`NumberFieldFilter`)            | Weight of the base product.                                                                      |
| tags (`StringFieldFilter[]`)                       | The tags associated with the product.                                                            |
| categories (`StringFieldFilter[]`)                 | The categories associated with the product.                                                      |
| dimensionsUnit (`DimensionsUnit`)                  | The unit of the product's dimensions. Either `METRIC` or `IMPERIAL`                              |
| variantSku (`StringFieldFilter`)                   | Stock Keeping Unit (SKU) for the product variant.                                                |
| variantName (`StringFieldFilter`)                  | The product variant's name.                                                                      |
| variantDescription (`StringFieldFilter`)           | The product variant's description.                                                               |
| variantPriceCurrency (`StringFieldFilter`)         | Currency related to all prices of the product variant.                                           |
| variantPriceAmount (`NumberFieldFilter`)           | The product variant's price.                                                                     |
| variantStoreCreatedDate (`StringFieldFilter`)      | Date the product variant was created in the store.  Must be in format 2019-11-16T10:48:23Z       |
| variantStoreModifiedDate (`StringFieldFilter`)     | Date the product variant was last modified in the store.  Must be in format 2019-11-16T10:48:23Z |
| variantUrl (`StringFieldFilter`)                   | The product variant's URL.                                                                       |
| variantUrlSlug (`StringFieldFilter`)               | The product variant's URL slug.                                                                  |
| variantDimensions (`PhysicalDimensions`)           | The product variant's physical dimensions.                                                       |
| variantWeight (`BigDecimal`)                       | The product variant's weight.                                                                    |
| type (`StringFieldFilter`)                         | Type of product (e.g. physical, digital, etc.)                                                   |
| status (`StringFieldFilter`)                       | The product's status (e.g. published, hidden, etc.)                                              |
| upc (`StringFieldFilter`)                          | The product's upc.                                                                               |
| isDeleted (`BooleanFieldFilter`)                   | Is the product deleted?                                                                          |
| numberOfSales (`IntFieldFilter`)                   | Number of sales of the product.                                                                  |
| isVirtual (`BooleanFieldFilter`)                   | Is the product virtual?                                                                          |
| isDownloadable (`BooleanFieldFilter`)              | Is the product downloadable?                                                                     |
| isVisible (`BooleanFieldFilter`)                   | Is the product visible?                                                                          |
| isOnSale (`BooleanFieldFilter`)                    | Is the product on sale?                                                                          |
| isBackordersAllowed (`BooleanFieldFilter`)         | Are backorders allowed for the product?                                                          |
| stockStatus (`StockStatusFieldFilter`)             | The product's stock status. One of: `IN_STOCK` `OUT_OF_STOCK` `BACKORDER`                        |
| averageRatings (`NumberFieldFilter`)               | The product's average rating.                                                                    |
| ratingCount (`IntFieldFilter`)                     | The number of ratings for the product.                                                           |
| brand (`StringFieldFilter`)                        | The product's brand (also known as vendor).                                                      |

## PhysicalDimensions

| Name                  | Description        |
| :-------------------- | :----------------- |
| length (`BigDecimal`) | Length of product. |
| width (`BigDecimal`)  | Width of product.  |
| height (`BigDecimal`) | Height of product. |

## ImageData

| Name           | Description                 |
| :------------- | :-------------------------- |
| url (`String`) | URL of image                |
| height (`Int`) | Height (in pixels) of image |
| width (`Int`)  | Width (in pixels) of image  |