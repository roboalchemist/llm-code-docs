# Source: https://developers.webflow.com/data/reference/ecommerce/products/create-sku.mdx

# Create SKUs

POST https://api.webflow.com/v2/sites/{site_id}/products/{product_id}/skus
Content-Type: application/json

Create additional SKUs to manage every [option and variant of your Product.](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants)

Creating SKUs through the API will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

Required scope | `ecommerce:write`


Reference: https://developers.webflow.com/data/reference/ecommerce/products/create-sku

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/products/{product_id}/skus:
    post:
      operationId: create-sku
      summary: Create SKUs
      description: >
        Create additional SKUs to manage every [option and variant of your
        Product.](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants)


        Creating SKUs through the API will set the product type to `Advanced`,
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
                $ref: '#/components/schemas/products_create-sku_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-skusRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-skusRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-skusRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-skusRequestNotFoundError'
        '409':
          description: The site does not have ecommerce enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-skusRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-skusRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-skusRequestInternalServerError'
      requestBody:
        description: The SKUs to add
        content:
          application/json:
            schema:
              type: object
              properties:
                publishStatus:
                  $ref: >-
                    #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaPublishStatus
                  description: >-
                    Indicate whether your Product should be set as "staging" or
                    "live"
                skus:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItems
                  description: An array of the SKU data your are adding
              required:
                - skus
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaPublishStatus:
      type: string
      enum:
        - staging
        - live
      default: staging
      description: Indicate whether your Product should be set as "staging" or "live"
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaPublishStatus
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataPrice:
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
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataPrice
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice:
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
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod:
      type: string
      enum:
        - one-time
        - subscription
      description: >-
        [Billing
        method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
        the SKU
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      description: Interval of subscription renewal
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform:
      type: string
      enum:
        - stripe
      description: The platform of the subscription plan
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus:
      type: string
      enum:
        - active
        - inactive
        - canceled
      description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems:
      type: object
      properties:
        platform:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
          description: The platform of the subscription plan
        id:
          type: string
          description: The unique identifier of the plan
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
          description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan:
      type: object
      properties:
        interval:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
      description: >-
        [Subscription
        plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
        for the SKU
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems:
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
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems:
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldData:
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
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataPrice
          description: price of SKU
        compare-at-price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice
          description: comparison price of SKU
        ec-sku-billing-method:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod
          description: >-
            [Billing
            method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
            the SKU
        ec-sku-subscription-plan:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems
          description: The properties of the SKU
      required:
        - name
        - slug
        - price
      description: Standard and Custom fields for a SKU
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldData
    SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItems:
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
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItemsFieldData
          description: Standard and Custom fields for a SKU
      description: The SKU object
      title: >-
        SitesSiteIdProductsProductIdSkusPostRequestBodyContentApplicationJsonSchemaSkusItems
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataPrice:
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
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataPrice
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice:
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
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod:
      type: string
      enum:
        - one-time
        - subscription
      description: >-
        [Billing
        method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
        the SKU
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      description: Interval of subscription renewal
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform:
      type: string
      enum:
        - stripe
      description: The platform of the subscription plan
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus:
      type: string
      enum:
        - active
        - inactive
        - canceled
      description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems:
      type: object
      properties:
        platform:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
          description: The platform of the subscription plan
        id:
          type: string
          description: The unique identifier of the plan
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItemsStatus
          description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan:
      type: object
      properties:
        interval:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanInterval
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlanPlansItems
      description: >-
        [Subscription
        plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
        for the SKU
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems:
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
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems:
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldData:
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
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataPrice
          description: price of SKU
        compare-at-price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataCompareAtPrice
          description: comparison price of SKU
        ec-sku-billing-method:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuBillingMethod
          description: >-
            [Billing
            method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
            the SKU
        ec-sku-subscription-plan:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataEcSkuSubscriptionPlan
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldDataSkuPropertiesItems
          description: The properties of the SKU
      required:
        - name
        - slug
        - price
      description: Standard and Custom fields for a SKU
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldData
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItems:
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
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItemsFieldData
          description: Standard and Custom fields for a SKU
      description: The SKU object
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItems
    products_create-sku_Response_200:
      type: object
      properties:
        skus:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaSkusItems
      required:
        - skus
      title: products_create-sku_Response_200
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaCode:
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
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaCode
    SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaDetailsItems
    Create-skusRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-skusRequestBadRequestError
    Create-skusRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-skusRequestUnauthorizedError
    Create-skusRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-skusRequestForbiddenError
    Create-skusRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-skusRequestNotFoundError
    Create-skusRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-skusRequestConflictError
    Create-skusRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-skusRequestTooManyRequestsError
    Create-skusRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-skusRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import datetime

from webflow import Sku, SkuFieldData, SkuFieldDataPrice, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.products.create_sku(
    site_id="580e63e98c9a982ac9b8b741",
    product_id="580e63fc8c9a982ac9b8b745",
    skus=[
        Sku(
            id="66072fb71b89448912e2681c",
            cms_locale_id="653ad57de882f528b32e810e",
            last_published=datetime.datetime.fromisoformat(
                "2023-03-17 18:47:35+00:00",
            ),
            last_updated=datetime.datetime.fromisoformat(
                "2023-03-17 18:47:35+00:00",
            ),
            created_on=datetime.datetime.fromisoformat(
                "2023-03-17 18:47:35+00:00",
            ),
            field_data=SkuFieldData(
                name="Colorful T-shirt - Default",
                slug="colorful-t-shirt-default",
                price=SkuFieldDataPrice(
                    value=2499.0,
                    unit="USD",
                    currency="USD",
                ),
            ),
        )
    ],
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.products.createSku("580e63e98c9a982ac9b8b741", "580e63fc8c9a982ac9b8b745", {
    skus: [{
            id: "66072fb71b89448912e2681c",
            cmsLocaleId: "653ad57de882f528b32e810e",
            lastPublished: new Date("2023-03-17T18:47:35.000Z"),
            lastUpdated: new Date("2023-03-17T18:47:35.000Z"),
            createdOn: new Date("2023-03-17T18:47:35.000Z"),
            fieldData: {
                name: "Colorful T-shirt - Default",
                slug: "colorful-t-shirt-default",
                price: {
                    value: 2499,
                    unit: "USD",
                    currency: "USD"
                }
            }
        }]
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus"

	payload := strings.NewReader("{\n  \"skus\": [\n    {}\n  ]\n}")

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"skus\": [\n    {}\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"skus\": [\n    {}\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus', [
  'body' => '{
  "skus": [
    {}
  ]
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

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"skus\": [\n    {}\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["skus": [[]]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus")! as URL,
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