# Source: https://developers.webflow.com/data/reference/ecommerce/orders/update-unfulfill.mdx

# Unfulfill Order

POST https://api.webflow.com/v2/sites/{site_id}/orders/{order_id}/unfulfill

Updates an order's status to unfulfilled

Required scope | `ecommerce:write`


Reference: https://developers.webflow.com/data/reference/ecommerce/orders/update-unfulfill

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/orders/{order_id}/unfulfill:
    post:
      operationId: update-unfulfill
      summary: Unfulfill Order
      description: |
        Updates an order's status to unfulfilled

        Required scope | `ecommerce:write`
      tags:
        - subpackage_orders
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: objectid
        - name: order_id
          in: path
          description: Unique identifier for an Order
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
                $ref: '#/components/schemas/orders_update-unfulfill_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Unfulfill-orderRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Unfulfill-orderRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Unfulfill-orderRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Unfulfill-orderRequestNotFoundError'
        '409':
          description: The site does not have ecommerce enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Unfulfill-orderRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Unfulfill-orderRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Unfulfill-orderRequestInternalServerError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStatus:
      type: string
      enum:
        - pending
        - unfulfilled
        - fulfilled
        - disputed
        - dispute-lost
        - refunded
      description: |
        The status of the Order
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStatus
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDisputeLastStatus:
      type: string
      enum:
        - warning_needs_response
        - warning_under_review
        - warning_closed
        - needs_response
        - under_review
        - charge_refunded
        - won
        - lost
      description: >
        If an order was disputed by the customer, then this key will be set with
        the [dispute's
        status](https://stripe.com/docs/api#dispute_object-status).
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDisputeLastStatus
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCustomerPaid:
      type: object
      properties:
        unit:
          type: string
          description: The three-letter ISO currency code
        value:
          type: string
          description: The numeric value in the base unit of the currency
        string:
          type: string
          description: The user-facing string representation of the amount
      description: The total paid by the customer
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCustomerPaid
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaNetAmount:
      type: object
      properties:
        unit:
          type: string
          description: The three-letter ISO currency code
        value:
          type: string
          description: The numeric value in the base unit of the currency
        string:
          type: string
          description: The user-facing string representation of the amount
      description: The net amount after application fees
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaNetAmount
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaApplicationFee:
      type: object
      properties:
        unit:
          type: string
          description: The three-letter ISO currency code
        value:
          type: string
          description: The numeric value in the base unit of the currency
        string:
          type: string
          description: The user-facing string representation of the amount
      description: The application fee assessed by the platform
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaApplicationFee
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaAllAddressesItemsType:
      type: string
      enum:
        - shipping
        - billing
      description: The type of the order address (billing or shipping)
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaAllAddressesItemsType
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaAllAddressesItemsJapanType:
      type: string
      enum:
        - kana
        - kanji
      description: >-
        Represents a Japan-only address format. This field will only appear on
        orders placed from Japan.
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaAllAddressesItemsJapanType
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaAllAddressesItems:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaAllAddressesItemsType
          description: The type of the order address (billing or shipping)
        japanType:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaAllAddressesItemsJapanType
            - type: 'null'
          description: >-
            Represents a Japan-only address format. This field will only appear
            on orders placed from Japan.
        addressee:
          type: string
          description: Display name on the address
        line1:
          type: string
          description: The first line of the address
        line2:
          type: string
          description: The second line of the address
        city:
          type: string
          description: The city of the address.
        state:
          type: string
          description: The state or province of the address
        country:
          type: string
          description: The country of the address
        postalCode:
          type: string
          description: The postal code of the address
      description: A customer address
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaAllAddressesItems
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaShippingAddressType:
      type: string
      enum:
        - shipping
        - billing
      description: The type of the order address (billing or shipping)
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaShippingAddressType
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaShippingAddressJapanType:
      type: string
      enum:
        - kana
        - kanji
      description: >-
        Represents a Japan-only address format. This field will only appear on
        orders placed from Japan.
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaShippingAddressJapanType
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaShippingAddress:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaShippingAddressType
          description: The type of the order address (billing or shipping)
        japanType:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaShippingAddressJapanType
            - type: 'null'
          description: >-
            Represents a Japan-only address format. This field will only appear
            on orders placed from Japan.
        addressee:
          type: string
          description: Display name on the address
        line1:
          type: string
          description: The first line of the address
        line2:
          type: string
          description: The second line of the address
        city:
          type: string
          description: The city of the address.
        state:
          type: string
          description: The state or province of the address
        country:
          type: string
          description: The country of the address
        postalCode:
          type: string
          description: The postal code of the address
      description: The shipping address
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaShippingAddress
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaBillingAddressType:
      type: string
      enum:
        - shipping
        - billing
      description: The type of the order address (billing or shipping)
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaBillingAddressType
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaBillingAddressJapanType:
      type: string
      enum:
        - kana
        - kanji
      description: >-
        Represents a Japan-only address format. This field will only appear on
        orders placed from Japan.
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaBillingAddressJapanType
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaBillingAddress:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaBillingAddressType
          description: The type of the order address (billing or shipping)
        japanType:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaBillingAddressJapanType
            - type: 'null'
          description: >-
            Represents a Japan-only address format. This field will only appear
            on orders placed from Japan.
        addressee:
          type: string
          description: Display name on the address
        line1:
          type: string
          description: The first line of the address
        line2:
          type: string
          description: The second line of the address
        city:
          type: string
          description: The city of the address.
        state:
          type: string
          description: The state or province of the address
        country:
          type: string
          description: The country of the address
        postalCode:
          type: string
          description: The postal code of the address
      description: The billing address
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaBillingAddress
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCustomerInfo:
      type: object
      properties:
        fullName:
          type: string
          description: The full name of the Customer
        email:
          type: string
          format: email
          description: The Customer's email address
      description: An object with the keys `fullName` and `email`.
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCustomerInfo
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsRowTotal:
      type: object
      properties:
        unit:
          type: string
          description: The three-letter ISO currency code
        value:
          type: string
          description: The numeric value in the base unit of the currency
        string:
          type: string
          description: The user-facing string representation of the amount
      description: The total for the row
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsRowTotal
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantImageFileVariantsItems:
      type: object
      properties:
        url:
          type: string
          format: uri
          description: The hosted location for the Variant's image
        originalFileName:
          type: string
        size:
          type: number
          format: double
          description: The image size in bytes
        width:
          type: integer
          description: The image width in pixels
        height:
          type: integer
          description: The image height in pixels
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantImageFileVariantsItems
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantImageFile:
      type: object
      properties:
        size:
          type: number
          format: double
          description: The image size in bytes
        originalFileName:
          type: string
          description: the original name of the image
        createdOn:
          type: string
          format: date-time
          description: The creation timestamp of the image
        contentType:
          type: string
          format: mime-type
          description: The MIME type of the image
        width:
          type: integer
          description: The image width in pixels
        height:
          type: integer
          description: The image height in pixels
        variants:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantImageFileVariantsItems
          description: Variants of the supplied image
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantImageFile
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantImage:
      type: object
      properties:
        url:
          type: string
          format: uri
          description: The hosted location for the Variant's image
        file:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantImageFile
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantImage
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantPrice:
      type: object
      properties:
        unit:
          type: string
          description: The three-letter ISO currency code
        value:
          type: string
          description: The numeric value in the base unit of the currency
        string:
          type: string
          description: The user-facing string representation of the amount
      description: The price corresponding to the variant
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantPrice
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItems:
      type: object
      properties:
        count:
          type: number
          format: double
          description: Number of Item purchased.
        rowTotal:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsRowTotal
          description: The total for the row
        productId:
          type: string
          format: objectid
          description: The unique identifier for the Product
        productName:
          type: string
          description: User-facing name of the Product
        productSlug:
          type: string
          description: Slug for the Product
        variantId:
          type: string
          description: Identifier for the Product Variant (SKU)
        variantName:
          type: string
          description: User-facing name of the Product Variant (SKU)
        variantSlug:
          type: string
          description: Slug for the Product Variant (SKU)
        variantSKU:
          type: string
          description: The user-defined custom SKU of the Product Variant (SKU)
        variantImage:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantImage
        variantPrice:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItemsVariantPrice
          description: The price corresponding to the variant
        weight:
          type:
            - number
            - 'null'
          format: double
          description: The physical weight of the variant if provided, or null
        width:
          type:
            - number
            - 'null'
          format: double
          description: The physical width of the variant if provided, or null
        height:
          type:
            - number
            - 'null'
          format: double
          description: The physical height of the variant if provided, or null
        length:
          type:
            - number
            - 'null'
          format: double
          description: The physical length of the variant if provided, or null
      description: An Item that was purchased
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItems
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeDetails:
      type: object
      properties:
        subscriptionId:
          type:
            - string
            - 'null'
          format: objectid
          description: Stripe-generated identifier for the Subscription
        paymentMethod:
          type:
            - string
            - 'null'
          format: objectid
          description: Stripe-generated identifier for the PaymentMethod used
        paymentIntentId:
          type:
            - string
            - 'null'
          format: objectid
          description: Stripe-generated identifier for the PaymentIntent, or null
        customerId:
          type:
            - string
            - 'null'
          format: objectid
          description: Stripe-generated customer identifier, or null
        chargeId:
          type:
            - string
            - 'null'
          format: objectid
          description: Stripe-generated charge identifier, or null
        disputeId:
          type:
            - string
            - 'null'
          format: objectid
          description: Stripe-generated dispute identifier, or null
        refundId:
          type:
            - string
            - 'null'
          format: objectid
          description: Stripe-generated refund identifier, or null
        refundReason:
          type:
            - string
            - 'null'
          description: Stripe-generated refund reason, or null
      description: >-
        An object with various Stripe IDs, useful for linking into the stripe
        dashboard.
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeDetails
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeCardBrand:
      type: string
      enum:
        - Visa
        - American Express
        - MasterCard
        - Discover
        - JCB
        - Diners Club
        - Unknown
      description: The card's brand (ie. credit card network)
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeCardBrand
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeCardExpires:
      type: object
      properties:
        year:
          type: number
          format: double
          description: Year that the card expires
        month:
          type: number
          format: double
          description: Month that the card expires
      description: The card's expiration date.
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeCardExpires
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeCard:
      type: object
      properties:
        last4:
          type: string
          description: The last 4 digits on the card as a string
        brand:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeCardBrand
          description: The card's brand (ie. credit card network)
        ownerName:
          type: string
          description: The name on the card.
        expires:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeCardExpires
          description: The card's expiration date.
      description: >
        Details on the card used to fulfill this order, if this order was
        finalized with Stripe.
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeCard
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPaypalDetails:
      type: object
      properties:
        orderId:
          type: string
          description: PayPal order identifier
        payerId:
          type: string
          description: PayPal payer identifier
        captureId:
          type: string
          description: PayPal capture identifier
        refundId:
          type: string
          description: PayPal refund identifier
        refundReason:
          type: string
          description: PayPal-issued reason for the refund
        disputeId:
          type: string
          description: PayPal dispute identifier
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPaypalDetails
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCustomDataItems:
      type: object
      properties: {}
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCustomDataItems
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaMetadata:
      type: object
      properties:
        isBuyNow:
          type: boolean
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaMetadata
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsSubtotal:
      type: object
      properties:
        unit:
          type: string
          description: The three-letter ISO currency code
        value:
          type: string
          description: The numeric value in the base unit of the currency
        string:
          type: string
          description: The user-facing string representation of the amount
      description: The subtotal price
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsSubtotal
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsExtrasItemsType:
      type: string
      enum:
        - discount
        - discount-shipping
        - shipping
        - tax
      description: The type of extra item this is.
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsExtrasItemsType
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsExtrasItemsPrice:
      type: object
      properties:
        unit:
          type: string
          description: The three-letter ISO currency code
        value:
          type: string
          description: The numeric value in the base unit of the currency
        string:
          type: string
          description: The user-facing string representation of the amount
      description: The price for the item
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsExtrasItemsPrice
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsExtrasItems:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsExtrasItemsType
          description: The type of extra item this is.
        name:
          type: string
          description: A human-readable (but English) name for this extra charge.
        description:
          type: string
          description: A human-readable (but English) description of this extra charge.
        price:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsExtrasItemsPrice
          description: The price for the item
      description: Extra order items, includes discounts, shipping, and taxes.
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsExtrasItems
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsTotal:
      type: object
      properties:
        unit:
          type: string
          description: The three-letter ISO currency code
        value:
          type: string
          description: The numeric value in the base unit of the currency
        string:
          type: string
          description: The user-facing string representation of the amount
      description: The total price
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsTotal
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotals:
      type: object
      properties:
        subtotal:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsSubtotal
          description: The subtotal price
        extras:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsExtrasItems
          description: An array of extra items, includes discounts, shipping, and taxes.
        total:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotalsTotal
          description: The total price
      description: An object describing various pricing totals
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotals
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDownloadFilesItems:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier for the downloadable file
        name:
          type: string
          description: The user-facing name for the downloadable file
        url:
          type: string
          format: uri
          description: The hosted location for the downloadable file
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDownloadFilesItems
    orders_update-unfulfill_Response_200:
      type: object
      properties:
        orderId:
          type: string
          description: |
            The order ID. Will usually be 6 hex characters, but can also be 9
            hex characters if the site has a very large number of Orders.
            Randomly assigned.
        status:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStatus
          description: |
            The status of the Order
        comment:
          type: string
          description: >-
            A comment string for this Order, which is editable by API user (not
            used by Webflow).
        orderComment:
          type: string
          description: A comment that the customer left when making their Order
        acceptedOn:
          type:
            - string
            - 'null'
          format: date-time
          description: The ISO8601 timestamp that an Order was placed.
        fulfilledOn:
          type:
            - string
            - 'null'
          format: date-time
          description: >
            When an Order is marked as 'fulfilled', this field represents the
            timestamp of the fulfillment in ISO8601 format. Otherwise, it is
            null.
        refundedOn:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            When an Order is marked as 'refunded', this field represents the
            timestamp of the fulfillment in ISO8601 format. Otherwise, it is
            null.
        disputedOn:
          type:
            - string
            - 'null'
          format: date-time
          description: >
            When an Order is marked as 'disputed', this field represents the
            timestamp of the fulfillment in ISO8601 format. Otherwise, it is
            null.
        disputeUpdatedOn:
          type:
            - string
            - 'null'
          format: date-time
          description: >
            If an Order has been disputed by the customer, this key will be set
            to the ISO8601 timestamp of the last update received. If the Order
            is not disputed, the key will be null.
        disputeLastStatus:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDisputeLastStatus
            - type: 'null'
          description: >
            If an order was disputed by the customer, then this key will be set
            with the [dispute's
            status](https://stripe.com/docs/api#dispute_object-status).
        customerPaid:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCustomerPaid
          description: The total paid by the customer
        netAmount:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaNetAmount
          description: The net amount after application fees
        applicationFee:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaApplicationFee
          description: The application fee assessed by the platform
        allAddresses:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaAllAddressesItems
          description: All addresses provided by the customer during the ordering flow.
        shippingAddress:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaShippingAddress
          description: The shipping address
        billingAddress:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaBillingAddress
          description: The billing address
        shippingProvider:
          type:
            - string
            - 'null'
          description: >
            A string editable by the API user to note the shipping provider used
            (not used by Webflow).
        shippingTracking:
          type:
            - string
            - 'null'
          description: >
            A string editable by the API user to note the shipping tracking
            number for the order (not used by Webflow).
        shippingTrackingURL:
          type:
            - string
            - 'null'
          format: uri
        customerInfo:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCustomerInfo
          description: An object with the keys `fullName` and `email`.
        purchasedItems:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPurchasedItemsItems
          description: An array of all things that the Customer purchased.
        purchasedItemsCount:
          type: number
          format: double
          description: The sum of all 'count' fields in 'purchasedItems'.
        stripeDetails:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeDetails
          description: >-
            An object with various Stripe IDs, useful for linking into the
            stripe dashboard.
        stripeCard:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaStripeCard
          description: >
            Details on the card used to fulfill this order, if this order was
            finalized with Stripe.
        paypalDetails:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaPaypalDetails
        customData:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCustomDataItems
          description: >
            An array of additional inputs for custom order data gathering. Each
            object in the array represents an input with a name, and a
            textInput, textArea, or checkbox value.
        metadata:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaMetadata
        isCustomerDeleted:
          type: boolean
          description: >
            A boolean indicating whether the customer has been deleted from the
            site.
        isShippingRequired:
          type: boolean
          description: >
            A boolean indicating whether the order contains one or more
            purchased items that require shipping.
        hasDownloads:
          type: boolean
          description: >
            A boolean indicating whether the order contains one or more
            purchased items that are downloadable.
        paymentProcessor:
          type: string
          description: |
            A string indicating the payment processor used for this order.
        totals:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaTotals
          description: An object describing various pricing totals
        downloadFiles:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDownloadFilesItems
          description: An array of downloadable file objects.
      title: orders_update-unfulfill_Response_200
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCode:
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
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCode
    SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDetailsItems
    Unfulfill-orderRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Unfulfill-orderRequestBadRequestError
    Unfulfill-orderRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Unfulfill-orderRequestUnauthorizedError
    Unfulfill-orderRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Unfulfill-orderRequestForbiddenError
    Unfulfill-orderRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Unfulfill-orderRequestNotFoundError
    Unfulfill-orderRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Unfulfill-orderRequestConflictError
    Unfulfill-orderRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Unfulfill-orderRequestTooManyRequestsError
    Unfulfill-orderRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersOrderIdUnfulfillPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Unfulfill-orderRequestInternalServerError
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
client.orders.update_unfulfill(
    site_id="580e63e98c9a982ac9b8b741",
    order_id="5e8518516e147040726cc415",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.orders.updateUnfulfill("580e63e98c9a982ac9b8b741", "5e8518516e147040726cc415");

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders/5e8518516e147040726cc415/unfulfill"

	req, _ := http.NewRequest("POST", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders/5e8518516e147040726cc415/unfulfill")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders/5e8518516e147040726cc415/unfulfill")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders/5e8518516e147040726cc415/unfulfill', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders/5e8518516e147040726cc415/unfulfill");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders/5e8518516e147040726cc415/unfulfill")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers

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