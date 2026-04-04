# Source: https://developers.webflow.com/data/reference/ecommerce/orders/list.mdx

# List Orders

GET https://api.webflow.com/v2/sites/{site_id}/orders

List all orders created for a given site.

Required scope | `ecommerce:read`


Reference: https://developers.webflow.com/data/reference/ecommerce/orders/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/orders:
    get:
      operationId: list
      summary: List Orders
      description: |
        List all orders created for a given site.

        Required scope | `ecommerce:read`
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
        - name: status
          in: query
          description: Filter the orders by status
          required: false
          schema:
            $ref: '#/components/schemas/SitesSiteIdOrdersGetParametersStatus'
        - name: offset
          in: query
          description: >-
            Offset used for pagination if the results have more than limit
            records
          required: false
          schema:
            type: integer
        - name: limit
          in: query
          description: 'Maximum number of records to be returned (max limit: 100)'
          required: false
          schema:
            type: integer
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
                $ref: '#/components/schemas/orders_list_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-ordersRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-ordersRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-ordersRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-ordersRequestNotFoundError'
        '409':
          description: The site does not have ecommerce enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-ordersRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-ordersRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-ordersRequestInternalServerError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdOrdersGetParametersStatus:
      type: string
      enum:
        - pending
        - refunded
        - dispute-lost
        - fulfilled
        - disputed
        - unfulfilled
      title: SitesSiteIdOrdersGetParametersStatus
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStatus:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStatus
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsDisputeLastStatus:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsDisputeLastStatus
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsCustomerPaid:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsCustomerPaid
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsNetAmount:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsNetAmount
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsApplicationFee:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsApplicationFee
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsAllAddressesItemsType:
      type: string
      enum:
        - shipping
        - billing
      description: The type of the order address (billing or shipping)
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsAllAddressesItemsType
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsAllAddressesItemsJapanType:
      type: string
      enum:
        - kana
        - kanji
      description: >-
        Represents a Japan-only address format. This field will only appear on
        orders placed from Japan.
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsAllAddressesItemsJapanType
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsAllAddressesItems:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsAllAddressesItemsType
          description: The type of the order address (billing or shipping)
        japanType:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsAllAddressesItemsJapanType
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsAllAddressesItems
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsShippingAddressType:
      type: string
      enum:
        - shipping
        - billing
      description: The type of the order address (billing or shipping)
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsShippingAddressType
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsShippingAddressJapanType:
      type: string
      enum:
        - kana
        - kanji
      description: >-
        Represents a Japan-only address format. This field will only appear on
        orders placed from Japan.
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsShippingAddressJapanType
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsShippingAddress:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsShippingAddressType
          description: The type of the order address (billing or shipping)
        japanType:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsShippingAddressJapanType
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsShippingAddress
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsBillingAddressType:
      type: string
      enum:
        - shipping
        - billing
      description: The type of the order address (billing or shipping)
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsBillingAddressType
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsBillingAddressJapanType:
      type: string
      enum:
        - kana
        - kanji
      description: >-
        Represents a Japan-only address format. This field will only appear on
        orders placed from Japan.
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsBillingAddressJapanType
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsBillingAddress:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsBillingAddressType
          description: The type of the order address (billing or shipping)
        japanType:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsBillingAddressJapanType
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsBillingAddress
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsCustomerInfo:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsCustomerInfo
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsRowTotal:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsRowTotal
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantImageFileVariantsItems:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantImageFileVariantsItems
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantImageFile:
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
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantImageFileVariantsItems
          description: Variants of the supplied image
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantImageFile
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantImage:
      type: object
      properties:
        url:
          type: string
          format: uri
          description: The hosted location for the Variant's image
        file:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantImageFile
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantImage
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantPrice:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantPrice
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItems:
      type: object
      properties:
        count:
          type: number
          format: double
          description: Number of Item purchased.
        rowTotal:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsRowTotal
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
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantImage
        variantPrice:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItemsVariantPrice
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItems
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeDetails:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeDetails
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeCardBrand:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeCardBrand
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeCardExpires:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeCardExpires
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeCard:
      type: object
      properties:
        last4:
          type: string
          description: The last 4 digits on the card as a string
        brand:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeCardBrand
          description: The card's brand (ie. credit card network)
        ownerName:
          type: string
          description: The name on the card.
        expires:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeCardExpires
          description: The card's expiration date.
      description: >
        Details on the card used to fulfill this order, if this order was
        finalized with Stripe.
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeCard
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPaypalDetails:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPaypalDetails
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsCustomDataItems:
      type: object
      properties: {}
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsCustomDataItems
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsMetadata:
      type: object
      properties:
        isBuyNow:
          type: boolean
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsMetadata
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsSubtotal:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsSubtotal
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsExtrasItemsType:
      type: string
      enum:
        - discount
        - discount-shipping
        - shipping
        - tax
      description: The type of extra item this is.
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsExtrasItemsType
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsExtrasItemsPrice:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsExtrasItemsPrice
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsExtrasItems:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsExtrasItemsType
          description: The type of extra item this is.
        name:
          type: string
          description: A human-readable (but English) name for this extra charge.
        description:
          type: string
          description: A human-readable (but English) description of this extra charge.
        price:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsExtrasItemsPrice
          description: The price for the item
      description: Extra order items, includes discounts, shipping, and taxes.
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsExtrasItems
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsTotal:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsTotal
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotals:
      type: object
      properties:
        subtotal:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsSubtotal
          description: The subtotal price
        extras:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsExtrasItems
          description: An array of extra items, includes discounts, shipping, and taxes.
        total:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotalsTotal
          description: The total price
      description: An object describing various pricing totals
      title: >-
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotals
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsDownloadFilesItems:
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
        SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsDownloadFilesItems
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItems:
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
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStatus
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
                #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsDisputeLastStatus
            - type: 'null'
          description: >
            If an order was disputed by the customer, then this key will be set
            with the [dispute's
            status](https://stripe.com/docs/api#dispute_object-status).
        customerPaid:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsCustomerPaid
          description: The total paid by the customer
        netAmount:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsNetAmount
          description: The net amount after application fees
        applicationFee:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsApplicationFee
          description: The application fee assessed by the platform
        allAddresses:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsAllAddressesItems
          description: All addresses provided by the customer during the ordering flow.
        shippingAddress:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsShippingAddress
          description: The shipping address
        billingAddress:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsBillingAddress
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
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsCustomerInfo
          description: An object with the keys `fullName` and `email`.
        purchasedItems:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPurchasedItemsItems
          description: An array of all things that the Customer purchased.
        purchasedItemsCount:
          type: number
          format: double
          description: The sum of all 'count' fields in 'purchasedItems'.
        stripeDetails:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeDetails
          description: >-
            An object with various Stripe IDs, useful for linking into the
            stripe dashboard.
        stripeCard:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsStripeCard
          description: >
            Details on the card used to fulfill this order, if this order was
            finalized with Stripe.
        paypalDetails:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsPaypalDetails
        customData:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsCustomDataItems
          description: >
            An array of additional inputs for custom order data gathering. Each
            object in the array represents an input with a name, and a
            textInput, textArea, or checkbox value.
        metadata:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsMetadata
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
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsTotals
          description: An object describing various pricing totals
        downloadFiles:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItemsDownloadFilesItems
          description: An array of downloadable file objects.
      title: SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItems
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaPagination:
      type: object
      properties:
        limit:
          type: integer
          description: The limit used for pagination
        offset:
          type: integer
          description: The offset used for pagination
        total:
          type: integer
          description: The total number of records
      required:
        - limit
        - offset
        - total
      description: Pagination object
      title: SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaPagination
    orders_list_Response_200:
      type: object
      properties:
        orders:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaOrdersItems
          description: List of orders
        pagination:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
      description: Results from order list
      title: orders_list_Response_200
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaDetailsItems
    List-ordersRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-ordersRequestBadRequestError
    List-ordersRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-ordersRequestUnauthorizedError
    List-ordersRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-ordersRequestForbiddenError
    List-ordersRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-ordersRequestNotFoundError
    List-ordersRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-ordersRequestConflictError
    List-ordersRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-ordersRequestTooManyRequestsError
    List-ordersRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdOrdersGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-ordersRequestInternalServerError
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
client.orders.list(
    site_id="580e63e98c9a982ac9b8b741",
    status="pending",
    offset=1,
    limit=1,
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.orders.list("580e63e98c9a982ac9b8b741", {
    status: "pending",
    offset: 1,
    limit: 1
});

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders?offset=0&limit=100"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders?offset=0&limit=100")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders?offset=0&limit=100")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders?offset=0&limit=100', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders?offset=0&limit=100");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/orders?offset=0&limit=100")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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