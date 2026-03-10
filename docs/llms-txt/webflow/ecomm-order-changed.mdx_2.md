# Source: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/orders/ecomm-order-changed.mdx

# Updated eComm Order

POST 

Reference: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/orders/ecomm-order-changed

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
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        description: The information about the order that changed
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Order'
components:
  schemas:
    OrderStatus:
      type: string
      enum:
        - pending
        - unfulfilled
        - fulfilled
        - disputed
        - dispute-lost
        - refunded
      description: >
        One of `pending`, `unfulfilled`, `fulfilled`, `disputed`,
        `dispute-lost`, or `refunded`
      title: OrderStatus
    OrderAmount:
      type: object
      properties:
        unit:
          type: string
        value:
          type: string
        string:
          type: string
      description: The sum of all line items.
      title: OrderAmount
    OrderCustomerInfo:
      type: object
      properties:
        fullName:
          type: string
        email:
          type: string
          format: email
      description: An object with the keys `fullName` and `email`.
      title: OrderCustomerInfo
    OrderAddressType:
      type: string
      enum:
        - shipping
        - billing
      title: OrderAddressType
    OrderAddress:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OrderAddressType'
        addressee:
          type: string
        line1:
          type: string
        line2:
          type: string
        city:
          type: string
        state:
          type: string
        country:
          type: string
        postalCode:
          type: string
      description: A customer address
      title: OrderAddress
    OrderItemImage:
      type: object
      properties:
        fileId:
          type: string
          format: uuid
        url:
          type: string
          format: uri
      title: OrderItemImage
    OrderPurchasedItem:
      type: object
      properties:
        count:
          type: number
          format: double
          description: Number of item purchased.
        rowTotal:
          $ref: '#/components/schemas/OrderAmount'
        productId:
          type: string
          format: uuid
          description: String Product Id.
        productName:
          type: string
          description: Name of the product.
        productSlug:
          type: string
          description: Slug of the product.
        variantId:
          type: string
          format: uuid
          description: String Variant Id. (SKU)
        variantName:
          type: string
          description: Name of the variant. (SKU)
        variantSlug:
          type: string
          description: Slug of the variant. (SKU)
        variantImage:
          $ref: '#/components/schemas/OrderItemImage'
        variantPrice:
          $ref: '#/components/schemas/OrderAmount'
        height:
          type: number
          format: double
          description: The height of the variant if provided, 0 otherwise.
        length:
          type: number
          format: double
          description: The length of the variant if provided, 0 otherwise.
        width:
          type: number
          format: double
          description: The width of the variant if provided, 0 otherwise
        weight:
          type: number
          format: double
          description: The weight of the variant if provided, 0 otherwise.
        purchasedItemsCount:
          type: number
          format: double
          description: The sum of all 'count' fields in 'purchasedItems'.
      description: An item that was purchased
      title: OrderPurchasedItem
    StripeDetails:
      type: object
      properties:
        refundReason:
          type: string
          description: Stripe customer ID, or null.
        refundId:
          type: string
          format: uuid
          description: Stripe charge ID, or null.
        disputeId:
          type: string
          format: uuid
          description: Stripe dispute ID, or null.
        chargeId:
          type: string
          format: uuid
          description: Stripe refund ID, or null.
        customerId:
          type: string
          format: uuid
      description: >-
        An object with various Stripe IDs, useful for linking into the stripe
        dashboard.
      title: StripeDetails
    StripeCardBrand:
      type: string
      enum:
        - Visa
        - American Express
        - MasterCard
        - Discover
        - JCB
        - Diners Club
        - Unknown
      description: The card’s brand.
      title: StripeCardBrand
    StripeCardExpires:
      type: object
      properties:
        year:
          type: number
          format: double
        month:
          type: number
          format: double
      description: The card’s expiration date.
      title: StripeCardExpires
    StripeCard:
      type: object
      properties:
        last4:
          type: string
          description: The last 4 digits on the card.
        brand:
          $ref: '#/components/schemas/StripeCardBrand'
          description: The card’s brand.
        ownerName:
          type: string
          description: The name on the card.
        expires:
          $ref: '#/components/schemas/StripeCardExpires'
          description: The card’s expiration date.
      description: >
        Details on the card used to fulfill this order, if this order was
        finalized with Stripe.
      title: StripeCard
    OrderExtraType:
      type: string
      enum:
        - discount
        - discount-shipping
        - shipping
        - tax
      description: The type of extra item this is.
      title: OrderExtraType
    OrderExtra:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OrderExtraType'
          description: The type of extra item this is.
        name:
          type: string
          description: A human-readable (but English) name for this extra charge.
        description:
          type: string
          description: A human-readable (but English) description of this extra charge.
        price:
          $ref: '#/components/schemas/OrderAmount'
      description: Extra order items, includes discounts, shipping, and taxes.
      title: OrderExtra
    OrderTotals:
      type: object
      properties:
        subtotal:
          $ref: '#/components/schemas/OrderAmount'
        extras:
          type: array
          items:
            $ref: '#/components/schemas/OrderExtra'
          description: An array of extra items, includes discounts, shipping, and taxes.
        total:
          $ref: '#/components/schemas/OrderAmount'
      description: An object describing various pricing totals.
      title: OrderTotals
    OrderCustomDataItems:
      type: object
      properties: {}
      title: OrderCustomDataItems
    OrderDownloadedFile:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        url:
          type: string
          format: uri
      title: OrderDownloadedFile
    Order:
      type: object
      properties:
        orderId:
          type: string
          description: >
            The order ID. Will usually be 6 hex characters, but can also be 9
            hex characters if the site has a very large number of orders.
            Randomly assigned.
        status:
          $ref: '#/components/schemas/OrderStatus'
          description: >
            One of `pending`, `unfulfilled`, `fulfilled`, `disputed`,
            `dispute-lost`, or `refunded`
        comment:
          type: string
          description: >-
            A comment string for this order editable by API user (not used by
            Webflow).
        orderComment:
          type: string
          description: A comment that the customer left when making their order
        acceptedOn:
          type: string
          format: date-time
          description: The ISO8601 timestamp that an order was placed.
        disputedOn:
          type: string
          format: date-time
          description: >
            If an order was disputed by the customer, then this key will be set
            with the ISO8601 timestamp that Stripe notifies Webflow. Null if not
            disputed.
        disputeUpdatedOn:
          type: string
          description: >
            If an order was disputed by the customer, then this key will be set
            with the ISO8601 timestamp of the last time that we got an update.
            Null if not disputed.
        disputeLastStatus:
          type: string
          description: >
            If an order was disputed by the customer, then this key will be set
            with the [dispute's
            status](https://stripe.com/docs/api#dispute_object-status).
        fulfilledOn:
          type: string
          format: date-time
          description: >
            If an order was marked as 'fulfilled', then this is the ISO8601
            timestamp when that happened.
        refundedOn:
          type: string
          format: date-time
          description: If an order was refunded, this is the ISO8601 of when that happened.
        customerPaid:
          $ref: '#/components/schemas/OrderAmount'
        netAmount:
          $ref: '#/components/schemas/OrderAmount'
        requiresShipping:
          type: boolean
          description: >
            A boolean indicating whether the order contains one or more
            purchased items that require shipping.
        shippingProvider:
          type: string
          description: >
            A string editable by the API user to note the shipping provider used
            (not used by Webflow).
        shippingTracking:
          type: string
          description: >
            A string editable by the API user to note the shipping tracking
            number for the order (not used by Webflow).
        customerInfo:
          $ref: '#/components/schemas/OrderCustomerInfo'
        allAddresses:
          type: array
          items:
            $ref: '#/components/schemas/OrderAddress'
          description: All addresses provided by the customer during the ordering flow.
        shippingAddress:
          $ref: '#/components/schemas/OrderAddress'
        billingAddress:
          $ref: '#/components/schemas/OrderAddress'
        purchasedItems:
          type: array
          items:
            $ref: '#/components/schemas/OrderPurchasedItem'
          description: An array of all things that the customer purchased.
        stripeDetails:
          $ref: '#/components/schemas/StripeDetails'
        stripeCard:
          $ref: '#/components/schemas/StripeCard'
        totals:
          $ref: '#/components/schemas/OrderTotals'
        customData:
          type: array
          items:
            $ref: '#/components/schemas/OrderCustomDataItems'
          description: >
            An array of additional inputs for custom order data gathering. Each
            object in the array represents an input with a name, and a
            textInput, textArea, or checkbox value.
        downloadFiles:
          type: array
          items:
            $ref: '#/components/schemas/OrderDownloadedFile'
          description: An array of downloadable file objects.
      title: Order

```