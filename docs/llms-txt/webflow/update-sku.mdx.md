# Source: https://developers.webflow.com/data/reference/ecommerce/products/update-sku.mdx

# Update SKU

PATCH https://api.webflow.com/v2/sites/{site_id}/products/{product_id}/skus/{sku_id}
Content-Type: application/json

Update a specified SKU.

Updating an existing SKU will set the Product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

Required scope | `ecommerce:write`


Reference: https://developers.webflow.com/data/reference/ecommerce/products/update-sku

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/products/{product_id}/skus/{sku_id}:
    patch:
      operationId: update-sku
      summary: Update SKU
      description: >
        Update a specified SKU.


        Updating an existing SKU will set the Product type to `Advanced`, which
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
        - name: product_id
          in: path
          description: Unique identifier for a Product
          required: true
          schema:
            type: string
            format: objectid
        - name: sku_id
          in: path
          description: Unique identifier for a SKU
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
                $ref: '#/components/schemas/products_update-sku_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-skuRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-skuRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-skuRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-skuRequestNotFoundError'
        '409':
          description: The site does not have ecommerce enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-skuRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-skuRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-skuRequestInternalServerError'
      requestBody:
        description: The SKU to update
        content:
          application/json:
            schema:
              type: object
              properties:
                publishStatus:
                  $ref: >-
                    #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaPublishStatus
                  description: >-
                    Indicate whether your Product should be set as "staging" or
                    "live"
                sku:
                  $ref: >-
                    #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSku
                  description: The SKU object
              required:
                - sku
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaPublishStatus:
      type: string
      enum:
        - staging
        - live
      default: staging
      description: Indicate whether your Product should be set as "staging" or "live"
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaPublishStatus
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataPrice:
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
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataPrice
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataCompareAtPrice:
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
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataCompareAtPrice
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuBillingMethod:
      type: string
      enum:
        - one-time
        - subscription
      description: >-
        [Billing
        method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
        the SKU
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuBillingMethod
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      description: Interval of subscription renewal
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanInterval
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsPlatform:
      type: string
      enum:
        - stripe
      description: The platform of the subscription plan
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsStatus:
      type: string
      enum:
        - active
        - inactive
        - canceled
      description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsStatus
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItems:
      type: object
      properties:
        platform:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
          description: The platform of the subscription plan
        id:
          type: string
          description: The unique identifier of the plan
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItemsStatus
          description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItems
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlan:
      type: object
      properties:
        interval:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanInterval
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlanPlansItems
      description: >-
        [Subscription
        plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
        for the SKU
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlan
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItemsEnumItems:
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
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItems:
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItems
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldData:
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
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataPrice
          description: price of SKU
        compare-at-price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataCompareAtPrice
          description: comparison price of SKU
        ec-sku-billing-method:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuBillingMethod
          description: >-
            [Billing
            method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
            the SKU
        ec-sku-subscription-plan:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataEcSkuSubscriptionPlan
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldDataSkuPropertiesItems
          description: The properties of the SKU
      required:
        - name
        - slug
        - price
      description: Standard and Custom fields for a SKU
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldData
    SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSku:
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
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSkuFieldData
          description: Standard and Custom fields for a SKU
      description: The SKU object
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchRequestBodyContentApplicationJsonSchemaSku
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataPrice:
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
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataPrice
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataCompareAtPrice:
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
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataCompareAtPrice
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuBillingMethod:
      type: string
      enum:
        - one-time
        - subscription
      description: >-
        [Billing
        method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
        the SKU
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuBillingMethod
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      description: Interval of subscription renewal
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanInterval
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanPlansItemsPlatform:
      type: string
      enum:
        - stripe
      description: The platform of the subscription plan
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanPlansItemsStatus:
      type: string
      enum:
        - active
        - inactive
        - canceled
      description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanPlansItemsStatus
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanPlansItems:
      type: object
      properties:
        platform:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanPlansItemsPlatform
          description: The platform of the subscription plan
        id:
          type: string
          description: The unique identifier of the plan
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanPlansItemsStatus
          description: The status of the plan
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanPlansItems
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlan:
      type: object
      properties:
        interval:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanInterval
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlanPlansItems
      description: >-
        [Subscription
        plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription)
        for the SKU
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlan
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItemsEnumItems:
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
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItemsEnumItems
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItems:
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItemsEnumItems
          description: >-
            The individual Product variants that are contained within the
            collection
      required:
        - id
        - name
        - enum
      description: A variant/option type for a SKU
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItems
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldData:
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
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataPrice
          description: price of SKU
        compare-at-price:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataCompareAtPrice
          description: comparison price of SKU
        ec-sku-billing-method:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuBillingMethod
          description: >-
            [Billing
            method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for
            the SKU
        ec-sku-subscription-plan:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataEcSkuSubscriptionPlan
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldDataSkuPropertiesItems
          description: The properties of the SKU
      required:
        - name
        - slug
        - price
      description: Standard and Custom fields for a SKU
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldData
    products_update-sku_Response_200:
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
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaFieldData
          description: Standard and Custom fields for a SKU
      required:
        - id
        - lastPublished
        - lastUpdated
        - createdOn
        - fieldData
      description: The SKU object
      title: products_update-sku_Response_200
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaCode:
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
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaCode
    SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaDetailsItems
    Update-skuRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-skuRequestBadRequestError
    Update-skuRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-skuRequestUnauthorizedError
    Update-skuRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-skuRequestForbiddenError
    Update-skuRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-skuRequestNotFoundError
    Update-skuRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-skuRequestConflictError
    Update-skuRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-skuRequestTooManyRequestsError
    Update-skuRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdProductsProductIdSkusSkuIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-skuRequestInternalServerError
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
client.products.update_sku(
    site_id="580e63e98c9a982ac9b8b741",
    product_id="580e63fc8c9a982ac9b8b745",
    sku_id="5e8518516e147040726cc415",
    sku=Sku(
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
    ),
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.products.updateSku("580e63e98c9a982ac9b8b741", "580e63fc8c9a982ac9b8b745", "5e8518516e147040726cc415", {
    sku: {
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus/5e8518516e147040726cc415"

	payload := strings.NewReader("{\n  \"sku\": {\n    \"id\": \"66072fb71b89448912e2681c\",\n    \"cmsLocaleId\": \"653ad57de882f528b32e810e\",\n    \"lastPublished\": \"2023-03-17T18:47:35.560Z\",\n    \"lastUpdated\": \"2023-03-17T18:47:35.560Z\",\n    \"createdOn\": \"2023-03-17T18:47:35.560Z\",\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt - Default\",\n      \"slug\": \"colorful-t-shirt-default\",\n      \"price\": {\n        \"value\": 2499,\n        \"unit\": \"USD\",\n        \"currency\": \"USD\"\n      }\n    },\n    \"sku-values\": {\n      \"color\": \"red\",\n      \"size\": \"small\"\n    },\n    \"main-image\": \"https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987\"\n  }\n}")

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus/5e8518516e147040726cc415")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"sku\": {\n    \"id\": \"66072fb71b89448912e2681c\",\n    \"cmsLocaleId\": \"653ad57de882f528b32e810e\",\n    \"lastPublished\": \"2023-03-17T18:47:35.560Z\",\n    \"lastUpdated\": \"2023-03-17T18:47:35.560Z\",\n    \"createdOn\": \"2023-03-17T18:47:35.560Z\",\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt - Default\",\n      \"slug\": \"colorful-t-shirt-default\",\n      \"price\": {\n        \"value\": 2499,\n        \"unit\": \"USD\",\n        \"currency\": \"USD\"\n      }\n    },\n    \"sku-values\": {\n      \"color\": \"red\",\n      \"size\": \"small\"\n    },\n    \"main-image\": \"https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus/5e8518516e147040726cc415")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"sku\": {\n    \"id\": \"66072fb71b89448912e2681c\",\n    \"cmsLocaleId\": \"653ad57de882f528b32e810e\",\n    \"lastPublished\": \"2023-03-17T18:47:35.560Z\",\n    \"lastUpdated\": \"2023-03-17T18:47:35.560Z\",\n    \"createdOn\": \"2023-03-17T18:47:35.560Z\",\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt - Default\",\n      \"slug\": \"colorful-t-shirt-default\",\n      \"price\": {\n        \"value\": 2499,\n        \"unit\": \"USD\",\n        \"currency\": \"USD\"\n      }\n    },\n    \"sku-values\": {\n      \"color\": \"red\",\n      \"size\": \"small\"\n    },\n    \"main-image\": \"https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus/5e8518516e147040726cc415', [
  'body' => '{
  "sku": {
    "id": "66072fb71b89448912e2681c",
    "cmsLocaleId": "653ad57de882f528b32e810e",
    "lastPublished": "2023-03-17T18:47:35.560Z",
    "lastUpdated": "2023-03-17T18:47:35.560Z",
    "createdOn": "2023-03-17T18:47:35.560Z",
    "fieldData": {
      "name": "Colorful T-shirt - Default",
      "slug": "colorful-t-shirt-default",
      "price": {
        "value": 2499,
        "unit": "USD",
        "currency": "USD"
      }
    },
    "sku-values": {
      "color": "red",
      "size": "small"
    },
    "main-image": "https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987"
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

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus/5e8518516e147040726cc415");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"sku\": {\n    \"id\": \"66072fb71b89448912e2681c\",\n    \"cmsLocaleId\": \"653ad57de882f528b32e810e\",\n    \"lastPublished\": \"2023-03-17T18:47:35.560Z\",\n    \"lastUpdated\": \"2023-03-17T18:47:35.560Z\",\n    \"createdOn\": \"2023-03-17T18:47:35.560Z\",\n    \"fieldData\": {\n      \"name\": \"Colorful T-shirt - Default\",\n      \"slug\": \"colorful-t-shirt-default\",\n      \"price\": {\n        \"value\": 2499,\n        \"unit\": \"USD\",\n        \"currency\": \"USD\"\n      }\n    },\n    \"sku-values\": {\n      \"color\": \"red\",\n      \"size\": \"small\"\n    },\n    \"main-image\": \"https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["sku": [
    "id": "66072fb71b89448912e2681c",
    "cmsLocaleId": "653ad57de882f528b32e810e",
    "lastPublished": "2023-03-17T18:47:35.560Z",
    "lastUpdated": "2023-03-17T18:47:35.560Z",
    "createdOn": "2023-03-17T18:47:35.560Z",
    "fieldData": [
      "name": "Colorful T-shirt - Default",
      "slug": "colorful-t-shirt-default",
      "price": [
        "value": 2499,
        "unit": "USD",
        "currency": "USD"
      ]
    ],
    "sku-values": [
      "color": "red",
      "size": "small"
    ],
    "main-image": "https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987"
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus/5e8518516e147040726cc415")! as URL,
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