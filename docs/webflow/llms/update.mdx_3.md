# Source: https://developers.webflow.com/data/reference/ecommerce/products/update.mdx

# Update Product

PATCH https://api.webflow.com/v2/sites/{site_id}/products/{product_id}
Content-Type: application/json

Update an existing Product.

Updating an existing Product will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

Required scope | `ecommerce:write`


Reference: https://developers.webflow.com/data/reference/ecommerce/products/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/products/{product_id}:
    patch:
      operationId: update
      summary: Update Product
      description: >
        Update an existing Product.


        Updating an existing Product will set the product type to `Advanced`,
        which ensures all Product and SKU fields will be shown to users in the
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
        - name: product_id
          in: path
          description: Unique identifier for a Product
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
                $ref: '#/components/schemas/products_update_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-productRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-productRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-productRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-productRequestNotFoundError'
        '409':
          description: The site does not have ecommerce enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-productRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-productRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-productRequestInternalServerError'
      requestBody:
        description: The product to update
        content:
          application/json:
            schema:
              type: object
              properties:
                publishStatus:
                  $ref: >-
                    #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaPublishStatus
                  description: >-
                    Indicate whether your Product should be set as "staging" or
                    "live"
                product:
                  $ref: >-
                    #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProduct
                  description: The Product object
                sku:
                  $ref: >-
                    #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSku
                  description: The SKU object
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaPublishStatus:
      type: string
      enum:
        - staging
        - live
      default: staging
      description: Indicate whether your Product should be set as "staging" or "live"
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaPublishStatus
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems:
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
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems:
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataTaxCategory:
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
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataTaxCategory
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataEcProductType:
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
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataEcProductType
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldData:
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataSkuPropertiesItems
          description: Variant types to include in SKUs
        category:
          type: array
          items:
            type: string
          description: The category your product belongs to.
        tax-category:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataTaxCategory
          description: Product tax class
        default-sku:
          type: string
          format: objectid
          description: The default SKU associated with this product.
        ec-product-type:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldDataEcProductType
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
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldData
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProduct:
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
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProductFieldData
          description: >-
            Contains content-specific details for a product, covering both
            standard (e.g., title, description) and custom fields tailored to
            the product setup.
      description: The Product object
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaProduct
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataPrice:
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
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataPrice
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataCompareAtPrice:
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
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataCompareAtPrice
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuBillingMethod:
      type: string
      enum:
        - one-time
        - subscription
      description: >-
        [Billing
        method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
        the SKU
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuBillingMethod
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      description: Interval of subscription renewal
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanInterval
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsPlatform:
      type: string
      enum:
        - stripe
      description: The platform of the subscription plan
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsStatus:
      type: string
      enum:
        - active
        - inactive
        - canceled
      description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsStatus
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItems:
      type: object
      properties:
        platform:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
          description: The platform of the subscription plan
        id:
          type: string
          description: The unique identifier of the plan
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsStatus
          description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItems
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlan:
      type: object
      properties:
        interval:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanInterval
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItems
      description: >-
        [Subscription
        plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
        for the SKU
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlan
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItemsEnumItems:
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
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItems:
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItems
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldData:
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
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataPrice
          description: price of SKU
        compare-at-price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataCompareAtPrice
          description: comparison price of SKU
        ec-sku-billing-method:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuBillingMethod
          description: >-
            [Billing
            method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
            the SKU
        ec-sku-subscription-plan:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlan
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItems
          description: The properties of the SKU
      required:
        - name
        - slug
        - price
      description: Standard and Custom fields for a SKU
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldData
    SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSku:
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
            #/components/schemas/SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldData
          description: Standard and Custom fields for a SKU
      description: The SKU object
      title: >-
        SitesSiteIdProductsProductIdPatchRequestBodyContentApplicationJsonSchemaSku
    SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItemsEnumItems:
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
        SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItems:
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItems
    SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataTaxCategory:
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
        SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataTaxCategory
    SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataEcProductType:
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
        SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataEcProductType
    SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldData:
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItems
          description: Variant types to include in SKUs
        category:
          type: array
          items:
            type: string
          description: The category your product belongs to.
        tax-category:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataTaxCategory
          description: Product tax class
        default-sku:
          type: string
          format: objectid
          description: The default SKU associated with this product.
        ec-product-type:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldDataEcProductType
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
        SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldData
    products_update_Response_200:
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
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaFieldData
          description: >-
            Contains content-specific details for a product, covering both
            standard (e.g., title, description) and custom fields tailored to
            the product setup.
      description: The Product object
      title: products_update_Response_200
    SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaCode:
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
      title: >-
        SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaCode
    SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaDetailsItems
    Update-productRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-productRequestBadRequestError
    Update-productRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-productRequestUnauthorizedError
    Update-productRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-productRequestForbiddenError
    Update-productRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-productRequestNotFoundError
    Update-productRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-productRequestConflictError
    Update-productRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-productRequestTooManyRequestsError
    Update-productRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-productRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.products.update(
    site_id="580e63e98c9a982ac9b8b741",
    product_id="580e63fc8c9a982ac9b8b745",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.products.update("580e63e98c9a982ac9b8b741", "580e63fc8c9a982ac9b8b745");

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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745"

	payload := strings.NewReader("{\n  \"id\": \"660eb7a486d1d6e0412292d7\",\n  \"cmsLocaleId\": \"653ad57de882f528b32e810e\",\n  \"lastPublished\": \"2024-04-04T14:24:19.467Z\",\n  \"lastUpdated\": \"2024-04-04T14:30:19.282Z\",\n  \"createdOn\": \"2024-04-04T14:22:28.547Z\",\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"tax-category\": \"standard-taxable\",\n    \"shippable\": true,\n    \"ec-product-type\": \"b6ccc1830db4b1babeb06a9ac5f6dd76\",\n    \"sku-properties\": [\n      {\n        \"id\": \"31b77fa66fa376c2c0abb458d5be39fb\",\n        \"name\": \"Size\",\n        \"enum\": [\n          {\n            \"id\": \"8d21a625d655ab260e9941c27180c75b\",\n            \"name\": \"Small\",\n            \"slug\": \"small\"\n          },\n          {\n            \"id\": \"ecdca17106ad86c0dfe3b5f3ac8be6c9\",\n            \"name\": \"Medium\",\n            \"slug\": \"medium\"\n          },\n          {\n            \"id\": \"ec7877d6137ecf7ec86f726c135b1812\",\n            \"name\": \"Large\",\n            \"slug\": \"large\"\n          }\n        ]\n      },\n      {\n        \"id\": \"74d3738e62c568d5634dd6989daec5ec\",\n        \"name\": \"Color\",\n        \"enum\": [\n          {\n            \"id\": \"e539b0d6c3a609cd06ddb2da804f68f0\",\n            \"name\": \"Royal Blue\",\n            \"slug\": \"royal-blue\"\n          },\n          {\n            \"id\": \"68d98f2fbafc0fd45651cddc44798dd0\",\n            \"name\": \"Crimson Red\",\n            \"slug\": \"crimson-red\"\n          },\n          {\n            \"id\": \"996cd95c97fd5620d0a374c835b37205\",\n            \"name\": \"Forrest Green\",\n            \"slug\": \"forrest-green\"\n          }\n        ]\n      }\n    ],\n    \"name\": \"T-Shirt\",\n    \"description\": \"A plain t-shirt\",\n    \"slug\": \"t-shirt\",\n    \"default-sku\": \"66072fb71b89448912e2681c\"\n  }\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"id\": \"660eb7a486d1d6e0412292d7\",\n  \"cmsLocaleId\": \"653ad57de882f528b32e810e\",\n  \"lastPublished\": \"2024-04-04T14:24:19.467Z\",\n  \"lastUpdated\": \"2024-04-04T14:30:19.282Z\",\n  \"createdOn\": \"2024-04-04T14:22:28.547Z\",\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"tax-category\": \"standard-taxable\",\n    \"shippable\": true,\n    \"ec-product-type\": \"b6ccc1830db4b1babeb06a9ac5f6dd76\",\n    \"sku-properties\": [\n      {\n        \"id\": \"31b77fa66fa376c2c0abb458d5be39fb\",\n        \"name\": \"Size\",\n        \"enum\": [\n          {\n            \"id\": \"8d21a625d655ab260e9941c27180c75b\",\n            \"name\": \"Small\",\n            \"slug\": \"small\"\n          },\n          {\n            \"id\": \"ecdca17106ad86c0dfe3b5f3ac8be6c9\",\n            \"name\": \"Medium\",\n            \"slug\": \"medium\"\n          },\n          {\n            \"id\": \"ec7877d6137ecf7ec86f726c135b1812\",\n            \"name\": \"Large\",\n            \"slug\": \"large\"\n          }\n        ]\n      },\n      {\n        \"id\": \"74d3738e62c568d5634dd6989daec5ec\",\n        \"name\": \"Color\",\n        \"enum\": [\n          {\n            \"id\": \"e539b0d6c3a609cd06ddb2da804f68f0\",\n            \"name\": \"Royal Blue\",\n            \"slug\": \"royal-blue\"\n          },\n          {\n            \"id\": \"68d98f2fbafc0fd45651cddc44798dd0\",\n            \"name\": \"Crimson Red\",\n            \"slug\": \"crimson-red\"\n          },\n          {\n            \"id\": \"996cd95c97fd5620d0a374c835b37205\",\n            \"name\": \"Forrest Green\",\n            \"slug\": \"forrest-green\"\n          }\n        ]\n      }\n    ],\n    \"name\": \"T-Shirt\",\n    \"description\": \"A plain t-shirt\",\n    \"slug\": \"t-shirt\",\n    \"default-sku\": \"66072fb71b89448912e2681c\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"id\": \"660eb7a486d1d6e0412292d7\",\n  \"cmsLocaleId\": \"653ad57de882f528b32e810e\",\n  \"lastPublished\": \"2024-04-04T14:24:19.467Z\",\n  \"lastUpdated\": \"2024-04-04T14:30:19.282Z\",\n  \"createdOn\": \"2024-04-04T14:22:28.547Z\",\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"tax-category\": \"standard-taxable\",\n    \"shippable\": true,\n    \"ec-product-type\": \"b6ccc1830db4b1babeb06a9ac5f6dd76\",\n    \"sku-properties\": [\n      {\n        \"id\": \"31b77fa66fa376c2c0abb458d5be39fb\",\n        \"name\": \"Size\",\n        \"enum\": [\n          {\n            \"id\": \"8d21a625d655ab260e9941c27180c75b\",\n            \"name\": \"Small\",\n            \"slug\": \"small\"\n          },\n          {\n            \"id\": \"ecdca17106ad86c0dfe3b5f3ac8be6c9\",\n            \"name\": \"Medium\",\n            \"slug\": \"medium\"\n          },\n          {\n            \"id\": \"ec7877d6137ecf7ec86f726c135b1812\",\n            \"name\": \"Large\",\n            \"slug\": \"large\"\n          }\n        ]\n      },\n      {\n        \"id\": \"74d3738e62c568d5634dd6989daec5ec\",\n        \"name\": \"Color\",\n        \"enum\": [\n          {\n            \"id\": \"e539b0d6c3a609cd06ddb2da804f68f0\",\n            \"name\": \"Royal Blue\",\n            \"slug\": \"royal-blue\"\n          },\n          {\n            \"id\": \"68d98f2fbafc0fd45651cddc44798dd0\",\n            \"name\": \"Crimson Red\",\n            \"slug\": \"crimson-red\"\n          },\n          {\n            \"id\": \"996cd95c97fd5620d0a374c835b37205\",\n            \"name\": \"Forrest Green\",\n            \"slug\": \"forrest-green\"\n          }\n        ]\n      }\n    ],\n    \"name\": \"T-Shirt\",\n    \"description\": \"A plain t-shirt\",\n    \"slug\": \"t-shirt\",\n    \"default-sku\": \"66072fb71b89448912e2681c\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745', [
  'body' => '{
  "id": "660eb7a486d1d6e0412292d7",
  "cmsLocaleId": "653ad57de882f528b32e810e",
  "lastPublished": "2024-04-04T14:24:19.467Z",
  "lastUpdated": "2024-04-04T14:30:19.282Z",
  "createdOn": "2024-04-04T14:22:28.547Z",
  "isArchived": false,
  "isDraft": false,
  "fieldData": {
    "tax-category": "standard-taxable",
    "shippable": true,
    "ec-product-type": "b6ccc1830db4b1babeb06a9ac5f6dd76",
    "sku-properties": [
      {
        "id": "31b77fa66fa376c2c0abb458d5be39fb",
        "name": "Size",
        "enum": [
          {
            "id": "8d21a625d655ab260e9941c27180c75b",
            "name": "Small",
            "slug": "small"
          },
          {
            "id": "ecdca17106ad86c0dfe3b5f3ac8be6c9",
            "name": "Medium",
            "slug": "medium"
          },
          {
            "id": "ec7877d6137ecf7ec86f726c135b1812",
            "name": "Large",
            "slug": "large"
          }
        ]
      },
      {
        "id": "74d3738e62c568d5634dd6989daec5ec",
        "name": "Color",
        "enum": [
          {
            "id": "e539b0d6c3a609cd06ddb2da804f68f0",
            "name": "Royal Blue",
            "slug": "royal-blue"
          },
          {
            "id": "68d98f2fbafc0fd45651cddc44798dd0",
            "name": "Crimson Red",
            "slug": "crimson-red"
          },
          {
            "id": "996cd95c97fd5620d0a374c835b37205",
            "name": "Forrest Green",
            "slug": "forrest-green"
          }
        ]
      }
    ],
    "name": "T-Shirt",
    "description": "A plain t-shirt",
    "slug": "t-shirt",
    "default-sku": "66072fb71b89448912e2681c"
  }
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

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"id\": \"660eb7a486d1d6e0412292d7\",\n  \"cmsLocaleId\": \"653ad57de882f528b32e810e\",\n  \"lastPublished\": \"2024-04-04T14:24:19.467Z\",\n  \"lastUpdated\": \"2024-04-04T14:30:19.282Z\",\n  \"createdOn\": \"2024-04-04T14:22:28.547Z\",\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"tax-category\": \"standard-taxable\",\n    \"shippable\": true,\n    \"ec-product-type\": \"b6ccc1830db4b1babeb06a9ac5f6dd76\",\n    \"sku-properties\": [\n      {\n        \"id\": \"31b77fa66fa376c2c0abb458d5be39fb\",\n        \"name\": \"Size\",\n        \"enum\": [\n          {\n            \"id\": \"8d21a625d655ab260e9941c27180c75b\",\n            \"name\": \"Small\",\n            \"slug\": \"small\"\n          },\n          {\n            \"id\": \"ecdca17106ad86c0dfe3b5f3ac8be6c9\",\n            \"name\": \"Medium\",\n            \"slug\": \"medium\"\n          },\n          {\n            \"id\": \"ec7877d6137ecf7ec86f726c135b1812\",\n            \"name\": \"Large\",\n            \"slug\": \"large\"\n          }\n        ]\n      },\n      {\n        \"id\": \"74d3738e62c568d5634dd6989daec5ec\",\n        \"name\": \"Color\",\n        \"enum\": [\n          {\n            \"id\": \"e539b0d6c3a609cd06ddb2da804f68f0\",\n            \"name\": \"Royal Blue\",\n            \"slug\": \"royal-blue\"\n          },\n          {\n            \"id\": \"68d98f2fbafc0fd45651cddc44798dd0\",\n            \"name\": \"Crimson Red\",\n            \"slug\": \"crimson-red\"\n          },\n          {\n            \"id\": \"996cd95c97fd5620d0a374c835b37205\",\n            \"name\": \"Forrest Green\",\n            \"slug\": \"forrest-green\"\n          }\n        ]\n      }\n    ],\n    \"name\": \"T-Shirt\",\n    \"description\": \"A plain t-shirt\",\n    \"slug\": \"t-shirt\",\n    \"default-sku\": \"66072fb71b89448912e2681c\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "id": "660eb7a486d1d6e0412292d7",
  "cmsLocaleId": "653ad57de882f528b32e810e",
  "lastPublished": "2024-04-04T14:24:19.467Z",
  "lastUpdated": "2024-04-04T14:30:19.282Z",
  "createdOn": "2024-04-04T14:22:28.547Z",
  "isArchived": false,
  "isDraft": false,
  "fieldData": [
    "tax-category": "standard-taxable",
    "shippable": true,
    "ec-product-type": "b6ccc1830db4b1babeb06a9ac5f6dd76",
    "sku-properties": [
      [
        "id": "31b77fa66fa376c2c0abb458d5be39fb",
        "name": "Size",
        "enum": [
          [
            "id": "8d21a625d655ab260e9941c27180c75b",
            "name": "Small",
            "slug": "small"
          ],
          [
            "id": "ecdca17106ad86c0dfe3b5f3ac8be6c9",
            "name": "Medium",
            "slug": "medium"
          ],
          [
            "id": "ec7877d6137ecf7ec86f726c135b1812",
            "name": "Large",
            "slug": "large"
          ]
        ]
      ],
      [
        "id": "74d3738e62c568d5634dd6989daec5ec",
        "name": "Color",
        "enum": [
          [
            "id": "e539b0d6c3a609cd06ddb2da804f68f0",
            "name": "Royal Blue",
            "slug": "royal-blue"
          ],
          [
            "id": "68d98f2fbafc0fd45651cddc44798dd0",
            "name": "Crimson Red",
            "slug": "crimson-red"
          ],
          [
            "id": "996cd95c97fd5620d0a374c835b37205",
            "name": "Forrest Green",
            "slug": "forrest-green"
          ]
        ]
      ]
    ],
    "name": "T-Shirt",
    "description": "A plain t-shirt",
    "slug": "t-shirt",
    "default-sku": "66072fb71b89448912e2681c"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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