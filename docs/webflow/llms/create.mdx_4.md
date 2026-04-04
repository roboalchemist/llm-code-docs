# Source: https://developers.webflow.com/data/reference/ecommerce/products/create.mdx

# Create Product & SKU

POST https://api.webflow.com/v2/sites/{site_id}/products
Content-Type: application/json

Create a new ecommerce product and defaultSKU. A product, at minimum, must have a single SKU.

To create a product with multiple SKUs:
  - First, create a list of `sku-properties`, also known as [product options](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants). For example, a T-shirt product may have a "color" `sku-property`, with a list of enum values: red, yellow, and blue, another `sku-property` may be "size", with a list of enum values: small, medium, and large.
  - Once, a product is created with a list of `sku-properties`, Webflow will create a **default SKU**, which is always a combination of the first `enum` values of each `sku-property`. (e.g. Small - Red - T-Shirt)
  - After creation, you can create additional SKUs for the product, using the [Create SKUs endpoint.](/data/reference/ecommerce/products/create-sku)

Upon creation, the default product type will be `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

Required scope | `ecommerce:write`


Reference: https://developers.webflow.com/data/reference/ecommerce/products/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/products:
    post:
      operationId: create
      summary: Create Product & SKU
      description: >
        Create a new ecommerce product and defaultSKU. A product, at minimum,
        must have a single SKU.


        To create a product with multiple SKUs:
          - First, create a list of `sku-properties`, also known as [product options](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants). For example, a T-shirt product may have a "color" `sku-property`, with a list of enum values: red, yellow, and blue, another `sku-property` may be "size", with a list of enum values: small, medium, and large.
          - Once, a product is created with a list of `sku-properties`, Webflow will create a **default SKU**, which is always a combination of the first `enum` values of each `sku-property`. (e.g. Small - Red - T-Shirt)
          - After creation, you can create additional SKUs for the product, using the [Create SKUs endpoint.](/data/reference/ecommerce/products/create-sku)

        Upon creation, the default product type will be `Advanced`, which
        ensures all Product and SKU fields will be shown to users in the
        Designer.


        Required scope | `ecommerce:write`
      tags:
        - subpackage_products
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: objectid
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/products_create_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-productRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-productRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-productRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-productRequestNotFoundError'
        '409':
          description: The site does not have ecommerce enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-productRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-productRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-productRequestInternalServerError'
      requestBody:
        description: The Product and SKU to create
        content:
          application/json:
            schema:
              type: object
              properties:
                publishStatus:
                  $ref: >-
                    #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaPublishStatus
                  description: >-
                    Indicate whether your Product should be set as "staging" or
                    "live"
                product:
                  $ref: >-
                    #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProduct
                sku:
                  $ref: >-
                    #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSku
              required:
                - product
                - sku
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaPublishStatus:
      type: string
      enum:
        - staging
        - live
      default: staging
      description: Indicate whether your Product should be set as "staging" or "live"
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaPublishStatus
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a Product variant/Option
        name:
          type: string
          description: Name of the Product variant/Option
        slug:
          type: string
          description: Slug for the Product variant/Option in the Site URL structure
      required:
        - id
        - name
        - slug
      description: Enumerated Product variants/Options for the SKU
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a collection of Product Variants
        name:
          type: string
          description: Name of the collection of Product Variants
        enum:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataTaxCategory:
      type: string
      enum:
        - standard-taxable
        - standard-exempt
        - books-religious
        - books-textbook
        - clothing
        - clothing-swimwear
        - digital-goods
        - digital-service
        - drugs-non-prescription
        - drugs-prescription
        - food-bottled-water
        - food-candy
        - food-groceries
        - food-prepared
        - food-soda
        - food-supplements
        - magazine-individual
        - magazine-subscription
        - service-admission
        - service-advertising
        - service-dry-cleaning
        - service-hairdressing
        - service-installation
        - service-miscellaneous
        - service-parking
        - service-printing
        - service-professional
        - service-repair
        - service-training
      description: Product tax class
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataTaxCategory
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataEcProductType:
      type: string
      enum:
        - ff42fee0113744f693a764e3431a9cc2
        - f22027db68002190aef89a4a2b7ac8a1
        - c599e43b1a1c34d5a323aedf75d3adf6
        - b6ccc1830db4b1babeb06a9ac5f6dd76
      description: >-
        <a
        href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product
        types.</a> Enums reflect the following values in order: Physical,
        Digital, Service, Advanced"
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataEcProductType
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldData:
      type: object
      properties:
        name:
          type: string
          description: Name of the Product
        slug:
          type: string
          description: URL structure of the Product in your site.
        description:
          type: string
          description: A description of your product
        shippable:
          type: boolean
          description: Boolean determining if the Product is shippable
        sku-properties:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems
          description: Variant types to include in SKUs
        category:
          type: array
          items:
            type: string
          description: The category your product belongs to.
        tax-category:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataTaxCategory
          description: Product tax class
        default-sku:
          type: string
          format: objectid
          description: The default SKU associated with this product.
        ec-product-type:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldDataEcProductType
          description: >-
            <a
            href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product
            types.</a> Enums reflect the following values in order: Physical,
            Digital, Service, Advanced"
      description: >-
        Contains content-specific details for a product, covering both standard
        (e.g., title, description) and custom fields tailored to the product
        setup.
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldData
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProduct:
      type: object
      properties:
        fieldData:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProductFieldData
      title: SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaProduct
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataPrice:
      type: object
      properties:
        value:
          type: number
          format: double
          description: Price of SKU
        unit:
          type: string
          description: Currency of Item
        currency:
          type: string
          description: Currency of Item (alternative representation)
      description: price of SKU
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataPrice
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataCompareAtPrice:
      type: object
      properties:
        value:
          type: number
          format: double
          description: Price of SKU
        unit:
          type: string
          description: Currency of Item
      description: comparison price of SKU
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataCompareAtPrice
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuBillingMethod:
      type: string
      enum:
        - one-time
        - subscription
      description: >-
        [Billing
        method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
        the SKU
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuBillingMethod
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      description: Interval of subscription renewal
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanInterval
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsPlatform:
      type: string
      enum:
        - stripe
      description: The platform of the subscription plan
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsStatus:
      type: string
      enum:
        - active
        - inactive
        - canceled
      description: The status of the plan
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsStatus
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItems:
      type: object
      properties:
        platform:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
          description: The platform of the subscription plan
        id:
          type: string
          description: The unique identifier of the plan
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsStatus
          description: The status of the plan
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItems
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlan:
      type: object
      properties:
        interval:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanInterval
          description: Interval of subscription renewal
        frequency:
          type: number
          format: double
          description: Frequncy of billing within interval
        trial:
          type: number
          format: double
          description: Number of days of a trial
        plans:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItems
      description: >-
        [Subscription
        plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
        for the SKU
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlan
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItemsEnumItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a Product variant/Option
        name:
          type: string
          description: Name of the Product variant/Option
        slug:
          type: string
          description: Slug for the Product variant/Option in the Site URL structure
      required:
        - id
        - name
        - slug
      description: Enumerated Product variants/Options for the SKU
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a collection of Product Variants
        name:
          type: string
          description: Name of the collection of Product Variants
        enum:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItems
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldData:
      type: object
      properties:
        sku-values:
          type: object
          additionalProperties:
            type: string
          description: >
            A mapping between SKU properties and their values, represented as
            key-value pairs. Each key represents a SKU Property ID (e.g.
            "color") and maps to its corresponding SKU Value ID (e.g. "blue").
            This structure defines the specific variant combination for a SKU.
        name:
          type: string
          description: Name of the Product
        slug:
          type: string
          description: URL structure of the Product in your site.
        price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataPrice
          description: price of SKU
        compare-at-price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataCompareAtPrice
          description: comparison price of SKU
        ec-sku-billing-method:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuBillingMethod
          description: >-
            [Billing
            method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
            the SKU
        ec-sku-subscription-plan:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlan
          description: >-
            [Subscription
            plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
            for the SKU
        main-image:
          type: string
          description: The URL for the main image of the SKU
        sku:
          type: string
          description: A unique identifier for the SKU
        sku-properties:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItems
          description: The properties of the SKU
      required:
        - name
        - slug
        - price
      description: Standard and Custom fields for a SKU
      title: >-
        SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldData
    SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSku:
      type: object
      properties:
        fieldData:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSkuFieldData
          description: Standard and Custom fields for a SKU
      title: SitesSiteIdProductsPostRequestBodyContentApplicationJsonSchemaSku
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a Product variant/Option
        name:
          type: string
          description: Name of the Product variant/Option
        slug:
          type: string
          description: Slug for the Product variant/Option in the Site URL structure
      required:
        - id
        - name
        - slug
      description: Enumerated Product variants/Options for the SKU
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a collection of Product Variants
        name:
          type: string
          description: Name of the collection of Product Variants
        enum:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataTaxCategory:
      type: string
      enum:
        - standard-taxable
        - standard-exempt
        - books-religious
        - books-textbook
        - clothing
        - clothing-swimwear
        - digital-goods
        - digital-service
        - drugs-non-prescription
        - drugs-prescription
        - food-bottled-water
        - food-candy
        - food-groceries
        - food-prepared
        - food-soda
        - food-supplements
        - magazine-individual
        - magazine-subscription
        - service-admission
        - service-advertising
        - service-dry-cleaning
        - service-hairdressing
        - service-installation
        - service-miscellaneous
        - service-parking
        - service-printing
        - service-professional
        - service-repair
        - service-training
      description: Product tax class
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataTaxCategory
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataEcProductType:
      type: string
      enum:
        - ff42fee0113744f693a764e3431a9cc2
        - f22027db68002190aef89a4a2b7ac8a1
        - c599e43b1a1c34d5a323aedf75d3adf6
        - b6ccc1830db4b1babeb06a9ac5f6dd76
      description: >-
        <a
        href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product
        types.</a> Enums reflect the following values in order: Physical,
        Digital, Service, Advanced"
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataEcProductType
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldData:
      type: object
      properties:
        name:
          type: string
          description: Name of the Product
        slug:
          type: string
          description: URL structure of the Product in your site.
        description:
          type: string
          description: A description of your product
        shippable:
          type: boolean
          description: Boolean determining if the Product is shippable
        sku-properties:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems
          description: Variant types to include in SKUs
        category:
          type: array
          items:
            type: string
          description: The category your product belongs to.
        tax-category:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataTaxCategory
          description: Product tax class
        default-sku:
          type: string
          format: objectid
          description: The default SKU associated with this product.
        ec-product-type:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldDataEcProductType
          description: >-
            <a
            href="https://university.webflow.com/lesson/add-and-manage-products-and-categories?topics=ecommerce#how-to-understand-product-types">Product
            types.</a> Enums reflect the following values in order: Physical,
            Digital, Service, Advanced"
      description: >-
        Contains content-specific details for a product, covering both standard
        (e.g., title, description) and custom fields tailored to the product
        setup.
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldData
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProduct:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the Product
        cmsLocaleId:
          type: string
          description: Identifier for the locale of the CMS item
        lastPublished:
          type: string
          format: date-time
          description: The date the Product was last published
        lastUpdated:
          type: string
          format: date-time
          description: The date the Product was last updated
        createdOn:
          type: string
          format: date-time
          description: The date the Product was created
        isArchived:
          type: boolean
          default: false
          description: Boolean determining if the Product is set to archived
        isDraft:
          type: boolean
          default: false
          description: Boolean determining if the Product is set to draft
        fieldData:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProductFieldData
          description: >-
            Contains content-specific details for a product, covering both
            standard (e.g., title, description) and custom fields tailored to
            the product setup.
      description: The Product object
      title: SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProduct
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataPrice:
      type: object
      properties:
        value:
          type: number
          format: double
          description: Price of SKU
        unit:
          type: string
          description: Currency of Item
        currency:
          type: string
          description: Currency of Item (alternative representation)
      description: price of SKU
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataPrice
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice:
      type: object
      properties:
        value:
          type: number
          format: double
          description: Price of SKU
        unit:
          type: string
          description: Currency of Item
      description: comparison price of SKU
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod:
      type: string
      enum:
        - one-time
        - subscription
      description: >-
        [Billing
        method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
        the SKU
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      description: Interval of subscription renewal
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform:
      type: string
      enum:
        - stripe
      description: The platform of the subscription plan
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus:
      type: string
      enum:
        - active
        - inactive
        - canceled
      description: The status of the plan
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems:
      type: object
      properties:
        platform:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
          description: The platform of the subscription plan
        id:
          type: string
          description: The unique identifier of the plan
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
          description: The status of the plan
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan:
      type: object
      properties:
        interval:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval
          description: Interval of subscription renewal
        frequency:
          type: number
          format: double
          description: Frequncy of billing within interval
        trial:
          type: number
          format: double
          description: Number of days of a trial
        plans:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
      description: >-
        [Subscription
        plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
        for the SKU
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a Product variant/Option
        name:
          type: string
          description: Name of the Product variant/Option
        slug:
          type: string
          description: Slug for the Product variant/Option in the Site URL structure
      required:
        - id
        - name
        - slug
      description: Enumerated Product variants/Options for the SKU
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a collection of Product Variants
        name:
          type: string
          description: Name of the collection of Product Variants
        enum:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldData:
      type: object
      properties:
        sku-values:
          type: object
          additionalProperties:
            type: string
          description: >
            A mapping between SKU properties and their values, represented as
            key-value pairs. Each key represents a SKU Property ID (e.g.
            "color") and maps to its corresponding SKU Value ID (e.g. "blue").
            This structure defines the specific variant combination for a SKU.
        name:
          type: string
          description: Name of the Product
        slug:
          type: string
          description: URL structure of the Product in your site.
        price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataPrice
          description: price of SKU
        compare-at-price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice
          description: comparison price of SKU
        ec-sku-billing-method:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod
          description: >-
            [Billing
            method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
            the SKU
        ec-sku-subscription-plan:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan
          description: >-
            [Subscription
            plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
            for the SKU
        main-image:
          type: string
          description: The URL for the main image of the SKU
        sku:
          type: string
          description: A unique identifier for the SKU
        sku-properties:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems
          description: The properties of the SKU
      required:
        - name
        - slug
        - price
      description: Standard and Custom fields for a SKU
      title: >-
        SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldData
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItems:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: Unique identifier for the Product
        cmsLocaleId:
          type: string
          description: Identifier for the locale of the CMS item
        lastPublished:
          type: string
          format: date-time
          description: The date the Product was last published
        lastUpdated:
          type: string
          format: date-time
          description: The date the Product was last updated
        createdOn:
          type: string
          format: date-time
          description: The date the Product was created
        fieldData:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItemsFieldData
          description: Standard and Custom fields for a SKU
      description: The SKU object
      title: SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItems
    products_create_Response_200:
      type: object
      properties:
        product:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaProduct
          description: The Product object
        skus:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaSkusItems
          description: A list of SKU Objects
      description: A product and its SKUs.
      title: products_create_Response_200
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaCode:
      type: string
      enum:
        - bad_request
        - collection_not_found
        - conflict
        - duplicate_collection
        - duplicate_user_email
        - ecommerce_not_enabled
        - forbidden
        - forms_require_republish
        - incompatible_webhook_filter
        - internal_error
        - invalid_auth_version
        - invalid_credentials
        - invalid_domain
        - invalid_user_email
        - item_not_found
        - missing_scopes
        - no_domains
        - not_authorized
        - not_enterprise_plan_site
        - not_enterprise_plan_workspace
        - order_not_found
        - resource_not_found
        - too_many_requests
        - unsupported_version
        - unsupported_webhook_trigger_type
        - user_limit_reached
        - user_not_found
        - users_not_enabled
        - validation_error
      description: Error code
      title: SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaCode
    SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaDetailsItems
    Create-productRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-productRequestBadRequestError
    Create-productRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-productRequestUnauthorizedError
    Create-productRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-productRequestForbiddenError
    Create-productRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-productRequestNotFoundError
    Create-productRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-productRequestConflictError
    Create-productRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-productRequestTooManyRequestsError
    Create-productRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-productRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import (
    ProductFieldData,
    SkuFieldData,
    SkuFieldDataPrice,
    SkuPropertyList,
    SkuPropertyListEnumItem,
    Webflow,
)
from webflow.resources.products import (
    ProductSkuCreateProduct,
    ProductSkuCreateSku,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.products.create(
    site_id="580e63e98c9a982ac9b8b741",
    publish_status="staging",
    product=ProductSkuCreateProduct(
        field_data=ProductFieldData(
            name="Colorful T-shirt",
            slug="colorful-t-shirt",
            description="Our best-selling t-shirt available in multiple colors and sizes",
            sku_properties=[
                SkuPropertyList(
                    id="color",
                    name="Color",
                    enum=[
                        SkuPropertyListEnumItem(
                            id="red",
                            name="Red",
                            slug="red",
                        ),
                        SkuPropertyListEnumItem(
                            id="yellow",
                            name="Yellow",
                            slug="yellow",
                        ),
                        SkuPropertyListEnumItem(
                            id="blue",
                            name="Blue",
                            slug="blue",
                        ),
                    ],
                ),
                SkuPropertyList(
                    id="size",
                    name="Size",
                    enum=[
                        SkuPropertyListEnumItem(
                            id="small",
                            name="Small",
                            slug="small",
                        ),
                        SkuPropertyListEnumItem(
                            id="medium",
                            name="Medium",
                            slug="medium",
                        ),
                        SkuPropertyListEnumItem(
                            id="large",
                            name="Large",
                            slug="large",
                        ),
                    ],
                ),
            ],
        ),
    ),
    sku=ProductSkuCreateSku(
        field_data=SkuFieldData(
            name="Colorful T-shirt - Red Small",
            slug="colorful-t-shirt-red-small",
            price=SkuFieldDataPrice(
                value=2499.0,
                unit="USD",
                currency="USD",
            ),
            main_image="https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987",
        ),
    ),
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.products.create("580e63e98c9a982ac9b8b741", {
    publishStatus: "staging",
    product: {
        fieldData: {
            name: "Colorful T-shirt",
            slug: "colorful-t-shirt",
            description: "Our best-selling t-shirt available in multiple colors and sizes",
            skuProperties: [{
                    id: "color",
                    name: "Color",
                    "enum": [{
                            id: "red",
                            name: "Red",
                            slug: "red"
                        }, {
                            id: "yellow",
                            name: "Yellow",
                            slug: "yellow"
                        }, {
                            id: "blue",
                            name: "Blue",
                            slug: "blue"
                        }]
                }, {
                    id: "size",
                    name: "Size",
                    "enum": [{
                            id: "small",
                            name: "Small",
                            slug: "small"
                        }, {
                            id: "medium",
                            name: "Medium",
                            slug: "medium"
                        }, {
                            id: "large",
                            name: "Large",
                            slug: "large"
                        }]
                }]
        }
    },
    sku: {
        fieldData: {
            name: "Colorful T-shirt - Red Small",
            slug: "colorful-t-shirt-red-small",
            price: {
                value: 2499,
                unit: "USD",
                currency: "USD"
            },
            mainImage: "https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987"
        }
    }
});

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products"

	payload := strings.NewReader("{\n  \"product\": {\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt\",\n      \"slug\": \"colorful-t-shirt\",\n      \"description\": \"Our best-selling t-shirt available in multiple colors and sizes\",\n      \"sku-properties\": [\n        {\n          \"id\": \"color\",\n          \"name\": \"Color\",\n          \"enum\": [\n            {\n              \"id\": \"red\",\n              \"name\": \"Red\",\n              \"slug\": \"red\"\n            },\n            {\n              \"id\": \"yellow\",\n              \"name\": \"Yellow\",\n              \"slug\": \"yellow\"\n            },\n            {\n              \"id\": \"blue\",\n              \"name\": \"Blue\",\n              \"slug\": \"blue\"\n            }\n          ]\n        },\n        {\n          \"id\": \"size\",\n          \"name\": \"Size\",\n          \"enum\": [\n            {\n              \"id\": \"small\",\n              \"name\": \"Small\",\n              \"slug\": \"small\"\n            },\n            {\n              \"id\": \"medium\",\n              \"name\": \"Medium\",\n              \"slug\": \"medium\"\n            },\n            {\n              \"id\": \"large\",\n              \"name\": \"Large\",\n              \"slug\": \"large\"\n            }\n          ]\n        }\n      ]\n    }\n  },\n  \"sku\": {\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt - Red Small\",\n      \"slug\": \"colorful-t-shirt-red-small\",\n      \"price\": {\n        \"value\": 2499,\n        \"unit\": \"USD\",\n        \"currency\": \"USD\"\n      },\n      \"main-image\": \"https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987\"\n    }\n  },\n  \"publishStatus\": \"staging\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"product\": {\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt\",\n      \"slug\": \"colorful-t-shirt\",\n      \"description\": \"Our best-selling t-shirt available in multiple colors and sizes\",\n      \"sku-properties\": [\n        {\n          \"id\": \"color\",\n          \"name\": \"Color\",\n          \"enum\": [\n            {\n              \"id\": \"red\",\n              \"name\": \"Red\",\n              \"slug\": \"red\"\n            },\n            {\n              \"id\": \"yellow\",\n              \"name\": \"Yellow\",\n              \"slug\": \"yellow\"\n            },\n            {\n              \"id\": \"blue\",\n              \"name\": \"Blue\",\n              \"slug\": \"blue\"\n            }\n          ]\n        },\n        {\n          \"id\": \"size\",\n          \"name\": \"Size\",\n          \"enum\": [\n            {\n              \"id\": \"small\",\n              \"name\": \"Small\",\n              \"slug\": \"small\"\n            },\n            {\n              \"id\": \"medium\",\n              \"name\": \"Medium\",\n              \"slug\": \"medium\"\n            },\n            {\n              \"id\": \"large\",\n              \"name\": \"Large\",\n              \"slug\": \"large\"\n            }\n          ]\n        }\n      ]\n    }\n  },\n  \"sku\": {\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt - Red Small\",\n      \"slug\": \"colorful-t-shirt-red-small\",\n      \"price\": {\n        \"value\": 2499,\n        \"unit\": \"USD\",\n        \"currency\": \"USD\"\n      },\n      \"main-image\": \"https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987\"\n    }\n  },\n  \"publishStatus\": \"staging\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"product\": {\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt\",\n      \"slug\": \"colorful-t-shirt\",\n      \"description\": \"Our best-selling t-shirt available in multiple colors and sizes\",\n      \"sku-properties\": [\n        {\n          \"id\": \"color\",\n          \"name\": \"Color\",\n          \"enum\": [\n            {\n              \"id\": \"red\",\n              \"name\": \"Red\",\n              \"slug\": \"red\"\n            },\n            {\n              \"id\": \"yellow\",\n              \"name\": \"Yellow\",\n              \"slug\": \"yellow\"\n            },\n            {\n              \"id\": \"blue\",\n              \"name\": \"Blue\",\n              \"slug\": \"blue\"\n            }\n          ]\n        },\n        {\n          \"id\": \"size\",\n          \"name\": \"Size\",\n          \"enum\": [\n            {\n              \"id\": \"small\",\n              \"name\": \"Small\",\n              \"slug\": \"small\"\n            },\n            {\n              \"id\": \"medium\",\n              \"name\": \"Medium\",\n              \"slug\": \"medium\"\n            },\n            {\n              \"id\": \"large\",\n              \"name\": \"Large\",\n              \"slug\": \"large\"\n            }\n          ]\n        }\n      ]\n    }\n  },\n  \"sku\": {\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt - Red Small\",\n      \"slug\": \"colorful-t-shirt-red-small\",\n      \"price\": {\n        \"value\": 2499,\n        \"unit\": \"USD\",\n        \"currency\": \"USD\"\n      },\n      \"main-image\": \"https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987\"\n    }\n  },\n  \"publishStatus\": \"staging\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products', [
  'body' => '{
  "product": {
    "fieldData": {
      "name": "Colorful T-shirt",
      "slug": "colorful-t-shirt",
      "description": "Our best-selling t-shirt available in multiple colors and sizes",
      "sku-properties": [
        {
          "id": "color",
          "name": "Color",
          "enum": [
            {
              "id": "red",
              "name": "Red",
              "slug": "red"
            },
            {
              "id": "yellow",
              "name": "Yellow",
              "slug": "yellow"
            },
            {
              "id": "blue",
              "name": "Blue",
              "slug": "blue"
            }
          ]
        },
        {
          "id": "size",
          "name": "Size",
          "enum": [
            {
              "id": "small",
              "name": "Small",
              "slug": "small"
            },
            {
              "id": "medium",
              "name": "Medium",
              "slug": "medium"
            },
            {
              "id": "large",
              "name": "Large",
              "slug": "large"
            }
          ]
        }
      ]
    }
  },
  "sku": {
    "fieldData": {
      "name": "Colorful T-shirt - Red Small",
      "slug": "colorful-t-shirt-red-small",
      "price": {
        "value": 2499,
        "unit": "USD",
        "currency": "USD"
      },
      "main-image": "https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987"
    }
  },
  "publishStatus": "staging"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"product\": {\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt\",\n      \"slug\": \"colorful-t-shirt\",\n      \"description\": \"Our best-selling t-shirt available in multiple colors and sizes\",\n      \"sku-properties\": [\n        {\n          \"id\": \"color\",\n          \"name\": \"Color\",\n          \"enum\": [\n            {\n              \"id\": \"red\",\n              \"name\": \"Red\",\n              \"slug\": \"red\"\n            },\n            {\n              \"id\": \"yellow\",\n              \"name\": \"Yellow\",\n              \"slug\": \"yellow\"\n            },\n            {\n              \"id\": \"blue\",\n              \"name\": \"Blue\",\n              \"slug\": \"blue\"\n            }\n          ]\n        },\n        {\n          \"id\": \"size\",\n          \"name\": \"Size\",\n          \"enum\": [\n            {\n              \"id\": \"small\",\n              \"name\": \"Small\",\n              \"slug\": \"small\"\n            },\n            {\n              \"id\": \"medium\",\n              \"name\": \"Medium\",\n              \"slug\": \"medium\"\n            },\n            {\n              \"id\": \"large\",\n              \"name\": \"Large\",\n              \"slug\": \"large\"\n            }\n          ]\n        }\n      ]\n    }\n  },\n  \"sku\": {\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt - Red Small\",\n      \"slug\": \"colorful-t-shirt-red-small\",\n      \"price\": {\n        \"value\": 2499,\n        \"unit\": \"USD\",\n        \"currency\": \"USD\"\n      },\n      \"main-image\": \"https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987\"\n    }\n  },\n  \"publishStatus\": \"staging\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "product": ["fieldData": [
      "name": "Colorful T-shirt",
      "slug": "colorful-t-shirt",
      "description": "Our best-selling t-shirt available in multiple colors and sizes",
      "sku-properties": [
        [
          "id": "color",
          "name": "Color",
          "enum": [
            [
              "id": "red",
              "name": "Red",
              "slug": "red"
            ],
            [
              "id": "yellow",
              "name": "Yellow",
              "slug": "yellow"
            ],
            [
              "id": "blue",
              "name": "Blue",
              "slug": "blue"
            ]
          ]
        ],
        [
          "id": "size",
          "name": "Size",
          "enum": [
            [
              "id": "small",
              "name": "Small",
              "slug": "small"
            ],
            [
              "id": "medium",
              "name": "Medium",
              "slug": "medium"
            ],
            [
              "id": "large",
              "name": "Large",
              "slug": "large"
            ]
          ]
        ]
      ]
    ]],
  "sku": ["fieldData": [
      "name": "Colorful T-shirt - Red Small",
      "slug": "colorful-t-shirt-red-small",
      "price": [
        "value": 2499,
        "unit": "USD",
        "currency": "USD"
      ],
      "main-image": "https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987"
    ]],
  "publishStatus": "staging"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```