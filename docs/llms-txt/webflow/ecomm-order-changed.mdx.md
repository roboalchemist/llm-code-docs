# Source: https://developers.webflow.com/data/reference/webhooks/events/ecomm-order-changed.mdx

# Updated eComm Order

POST 

Information about an updated ecommerce order

Reference: https://developers.webflow.com/data/reference/webhooks/events/ecomm-order-changed

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  ecomm-order-changed:
    post:
      operationId: ecomm-order-changed
      summary: Updated eComm Order
      description: Information about an updated ecommerce order
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                triggerType:
                  type: string
                  description: The type of event that triggered the request
                payload:
                  $ref: >-
                    #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayload
components:
  schemas:
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStatus:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStatus
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadDisputeLastStatus:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadDisputeLastStatus
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadCustomerPaid:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadCustomerPaid
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadNetAmount:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadNetAmount
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadApplicationFee:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadApplicationFee
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadAllAddressesItemsType:
      type: string
      enum:
        - shipping
        - billing
      description: The type of the order address (billing or shipping)
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadAllAddressesItemsType
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadAllAddressesItemsJapanType:
      type: string
      enum:
        - kana
        - kanji
      description: >-
        Represents a Japan-only address format. This field will only appear on
        orders placed from Japan.
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadAllAddressesItemsJapanType
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadAllAddressesItems:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadAllAddressesItemsType
          description: The type of the order address (billing or shipping)
        japanType:
          oneOf:
            - $ref: >-
                #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadAllAddressesItemsJapanType
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadAllAddressesItems
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadShippingAddressType:
      type: string
      enum:
        - shipping
        - billing
      description: The type of the order address (billing or shipping)
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadShippingAddressType
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadShippingAddressJapanType:
      type: string
      enum:
        - kana
        - kanji
      description: >-
        Represents a Japan-only address format. This field will only appear on
        orders placed from Japan.
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadShippingAddressJapanType
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadShippingAddress:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadShippingAddressType
          description: The type of the order address (billing or shipping)
        japanType:
          oneOf:
            - $ref: >-
                #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadShippingAddressJapanType
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadShippingAddress
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadBillingAddressType:
      type: string
      enum:
        - shipping
        - billing
      description: The type of the order address (billing or shipping)
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadBillingAddressType
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadBillingAddressJapanType:
      type: string
      enum:
        - kana
        - kanji
      description: >-
        Represents a Japan-only address format. This field will only appear on
        orders placed from Japan.
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadBillingAddressJapanType
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadBillingAddress:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadBillingAddressType
          description: The type of the order address (billing or shipping)
        japanType:
          oneOf:
            - $ref: >-
                #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadBillingAddressJapanType
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadBillingAddress
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadCustomerInfo:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadCustomerInfo
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsRowTotal:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsRowTotal
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantImageFileVariantsItems:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantImageFileVariantsItems
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantImageFile:
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
              #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantImageFileVariantsItems
          description: Variants of the supplied image
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantImageFile
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantImage:
      type: object
      properties:
        url:
          type: string
          format: uri
          description: The hosted location for the Variant's image
        file:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantImageFile
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantImage
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantPrice:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantPrice
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItems:
      type: object
      properties:
        count:
          type: number
          format: double
          description: Number of Item purchased.
        rowTotal:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsRowTotal
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
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantImage
        variantPrice:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItemsVariantPrice
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItems
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeDetails:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeDetails
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeCardBrand:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeCardBrand
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeCardExpires:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeCardExpires
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeCard:
      type: object
      properties:
        last4:
          type: string
          description: The last 4 digits on the card as a string
        brand:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeCardBrand
          description: The card's brand (ie. credit card network)
        ownerName:
          type: string
          description: The name on the card.
        expires:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeCardExpires
          description: The card's expiration date.
      description: >
        Details on the card used to fulfill this order, if this order was
        finalized with Stripe.
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeCard
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPaypalDetails:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPaypalDetails
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadCustomDataItems:
      type: object
      properties: {}
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadCustomDataItems
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadMetadata:
      type: object
      properties:
        isBuyNow:
          type: boolean
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadMetadata
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsSubtotal:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsSubtotal
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsExtrasItemsType:
      type: string
      enum:
        - discount
        - discount-shipping
        - shipping
        - tax
      description: The type of extra item this is.
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsExtrasItemsType
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsExtrasItemsPrice:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsExtrasItemsPrice
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsExtrasItems:
      type: object
      properties:
        type:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsExtrasItemsType
          description: The type of extra item this is.
        name:
          type: string
          description: A human-readable (but English) name for this extra charge.
        description:
          type: string
          description: A human-readable (but English) description of this extra charge.
        price:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsExtrasItemsPrice
          description: The price for the item
      description: Extra order items, includes discounts, shipping, and taxes.
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsExtrasItems
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsTotal:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsTotal
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotals:
      type: object
      properties:
        subtotal:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsSubtotal
          description: The subtotal price
        extras:
          type: array
          items:
            $ref: >-
              #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsExtrasItems
          description: An array of extra items, includes discounts, shipping, and taxes.
        total:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotalsTotal
          description: The total price
      description: An object describing various pricing totals
      title: >-
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotals
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadDownloadFilesItems:
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
        WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadDownloadFilesItems
    WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayload:
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
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStatus
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
                #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadDisputeLastStatus
            - type: 'null'
          description: >
            If an order was disputed by the customer, then this key will be set
            with the [dispute's
            status](https://stripe.com/docs/api#dispute_object-status).
        customerPaid:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadCustomerPaid
          description: The total paid by the customer
        netAmount:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadNetAmount
          description: The net amount after application fees
        applicationFee:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadApplicationFee
          description: The application fee assessed by the platform
        allAddresses:
          type: array
          items:
            $ref: >-
              #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadAllAddressesItems
          description: All addresses provided by the customer during the ordering flow.
        shippingAddress:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadShippingAddress
          description: The shipping address
        billingAddress:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadBillingAddress
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
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadCustomerInfo
          description: An object with the keys `fullName` and `email`.
        purchasedItems:
          type: array
          items:
            $ref: >-
              #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPurchasedItemsItems
          description: An array of all things that the Customer purchased.
        purchasedItemsCount:
          type: number
          format: double
          description: The sum of all 'count' fields in 'purchasedItems'.
        stripeDetails:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeDetails
          description: >-
            An object with various Stripe IDs, useful for linking into the
            stripe dashboard.
        stripeCard:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadStripeCard
          description: >
            Details on the card used to fulfill this order, if this order was
            finalized with Stripe.
        paypalDetails:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadPaypalDetails
        customData:
          type: array
          items:
            $ref: >-
              #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadCustomDataItems
          description: >
            An array of additional inputs for custom order data gathering. Each
            object in the array represents an input with a name, and a
            textInput, textArea, or checkbox value.
        metadata:
          $ref: >-
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadMetadata
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
            #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadTotals
          description: An object describing various pricing totals
        downloadFiles:
          type: array
          items:
            $ref: >-
              #/components/schemas/WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayloadDownloadFilesItems
          description: An array of downloadable file objects.
      title: WebhooksEcommOrderChangedPayloadContentApplicationJsonSchemaPayload

```