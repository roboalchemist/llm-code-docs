# Source: https://polar.sh/docs/api-reference/customer-portal/seats/list-subscriptions.md

# List Claimed Subscriptions

> List all subscriptions where the authenticated customer has claimed a seat.

**Scopes**: `customer_portal:read` `customer_portal:write`

## OpenAPI

````yaml get /v1/customer-portal/seats/subscriptions
paths:
  path: /v1/customer-portal/seats/subscriptions
  method: get
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: customer session
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Customer session tokens are specific tokens that are used to
                authenticate customers on your organization. You can create
                those sessions programmatically using the [Create Customer
                Session
                endpoint](/api-reference/customer-portal/sessions/create).
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"os\"\n\t\"github.com/polarsource/polar-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.CustomerPortal.Seats.ListClaimedSubscriptions(ctx, operations.CustomerPortalSeatsListClaimedSubscriptionsSecurity{\n        CustomerSession: os.Getenv(\"POLAR_CUSTOMER_SESSION\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.ResponseCustomerPortalSeatsListClaimedSubscriptions != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          import polar_sdk
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.customer_portal.seats.list_claimed_subscriptions(security=polar_sdk.CustomerPortalSeatsListClaimedSubscriptionsSecurity(
                  customer_session="<YOUR_BEARER_TOKEN_HERE>",
              ))

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            const result = await polar.customerPortal.seats.listClaimedSubscriptions({
              customerSession: process.env["POLAR_CUSTOMER_SESSION"] ?? "",
            });

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: >-
          declare(strict_types=1);


          require 'vendor/autoload.php';


          use Polar;

          use Polar\Models\Operations;


          $sdk = Polar\Polar::builder()->build();



          $requestSecurity = new
          Operations\CustomerPortalSeatsListClaimedSubscriptionsSecurity(
              customerSession: '<YOUR_BEARER_TOKEN_HERE>',
          );


          $response = $sdk->customerPortal->seats->listClaimedSubscriptions(
              security: $requestSecurity
          );


          if ($response->responseCustomerPortalSeatsListClaimedSubscriptions !==
          null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/CustomerSubscription'
            title: Response Customer Portal:Seats:List Claimed Subscriptions
        examples:
          example:
            value:
              - created_at: '2023-11-07T05:31:56Z'
                modified_at: '2023-11-07T05:31:56Z'
                id: <string>
                amount: 10000
                currency: usd
                recurring_interval: month
                recurring_interval_count: 123
                status: active
                current_period_start: '2023-11-07T05:31:56Z'
                current_period_end: '2023-11-07T05:31:56Z'
                trial_start: '2023-11-07T05:31:56Z'
                trial_end: '2023-11-07T05:31:56Z'
                cancel_at_period_end: true
                canceled_at: '2023-11-07T05:31:56Z'
                started_at: '2023-11-07T05:31:56Z'
                ends_at: '2023-11-07T05:31:56Z'
                ended_at: '2023-11-07T05:31:56Z'
                customer_id: <string>
                product_id: <string>
                discount_id: <string>
                checkout_id: <string>
                seats: 123
                customer_cancellation_reason: customer_service
                customer_cancellation_comment: <string>
                product:
                  id: <string>
                  created_at: '2023-11-07T05:31:56Z'
                  modified_at: '2023-11-07T05:31:56Z'
                  trial_interval: day
                  trial_interval_count: 123
                  name: <string>
                  description: <string>
                  recurring_interval: day
                  recurring_interval_count: 123
                  is_recurring: true
                  is_archived: true
                  organization_id: <string>
                  prices:
                    - created_at: '2023-11-07T05:31:56Z'
                      modified_at: '2023-11-07T05:31:56Z'
                      id: <string>
                      amount_type: <string>
                      is_archived: true
                      product_id: <string>
                      type: <string>
                      recurring_interval: day
                      price_currency: <string>
                      price_amount: 123
                      legacy: true
                  benefits:
                    - id: <string>
                      created_at: '2023-11-07T05:31:56Z'
                      modified_at: '2023-11-07T05:31:56Z'
                      type: custom
                      description: <string>
                      selectable: true
                      deletable: true
                      organization_id: <string>
                  medias:
                    - id: <string>
                      organization_id: <string>
                      name: <string>
                      path: <string>
                      mime_type: <string>
                      size: 123
                      storage_version: <string>
                      checksum_etag: <string>
                      checksum_sha256_base64: <string>
                      checksum_sha256_hex: <string>
                      last_modified_at: '2023-11-07T05:31:56Z'
                      version: <string>
                      service: <string>
                      is_uploaded: true
                      created_at: '2023-11-07T05:31:56Z'
                      size_readable: <string>
                      public_url: <string>
                  organization:
                    created_at: '2023-11-07T05:31:56Z'
                    modified_at: '2023-11-07T05:31:56Z'
                    id: 1dbfc517-0bbf-4301-9ba8-555ca42b9737
                    name: <string>
                    slug: <string>
                    avatar_url: <string>
                    email: <string>
                    website: <string>
                    socials:
                      - platform: x
                        url: <string>
                    status: created
                    details_submitted_at: '2023-11-07T05:31:56Z'
                    feature_settings:
                      issue_funding_enabled: false
                      seat_based_pricing_enabled: false
                      revops_enabled: false
                    subscription_settings:
                      allow_multiple_subscriptions: true
                      allow_customer_updates: true
                      proration_behavior: invoice
                    notification_settings:
                      new_order: true
                      new_subscription: true
                    customer_email_settings:
                      order_confirmation: true
                      subscription_cancellation: true
                      subscription_confirmation: true
                      subscription_cycled: true
                      subscription_past_due: true
                      subscription_revoked: true
                      subscription_uncanceled: true
                      subscription_updated: true
                prices:
                  - created_at: '2023-11-07T05:31:56Z'
                    modified_at: '2023-11-07T05:31:56Z'
                    id: <string>
                    amount_type: <string>
                    is_archived: true
                    product_id: <string>
                    type: <string>
                    recurring_interval: day
                    price_currency: <string>
                    price_amount: 123
                    legacy: true
                meters:
                  - created_at: '2023-11-07T05:31:56Z'
                    modified_at: '2023-11-07T05:31:56Z'
                    id: <string>
                    consumed_units: 25
                    credited_units: 100
                    amount: 0
                    meter_id: d498a884-e2cd-4d3e-8002-f536468a8b22
                    meter:
                      created_at: '2023-11-07T05:31:56Z'
                      modified_at: '2023-11-07T05:31:56Z'
                      id: <string>
                      name: <string>
                is_polar_managed: true
        description: Successful Response
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Authentication required
        examples: {}
        description: Authentication required
  deprecated: false
  type: path
components:
  schemas:
    BenefitPublic:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the benefit.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        type:
          $ref: '#/components/schemas/BenefitType'
          description: The type of the benefit.
        description:
          type: string
          title: Description
          description: The description of the benefit.
        selectable:
          type: boolean
          title: Selectable
          description: Whether the benefit is selectable when creating a product.
        deletable:
          type: boolean
          title: Deletable
          description: Whether the benefit is deletable.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the benefit.
      type: object
      required:
        - id
        - created_at
        - modified_at
        - type
        - description
        - selectable
        - deletable
        - organization_id
      title: BenefitPublic
    BenefitType:
      type: string
      enum:
        - custom
        - discord
        - github_repository
        - downloadables
        - license_keys
        - meter_credit
      title: BenefitType
    CustomerCancellationReason:
      type: string
      enum:
        - customer_service
        - low_quality
        - missing_features
        - switched_service
        - too_complex
        - too_expensive
        - unused
        - other
      title: CustomerCancellationReason
    CustomerSubscription:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        amount:
          type: integer
          title: Amount
          description: The amount of the subscription.
          examples:
            - 10000
        currency:
          type: string
          title: Currency
          description: The currency of the subscription.
          examples:
            - usd
        recurring_interval:
          $ref: '#/components/schemas/SubscriptionRecurringInterval'
          description: The interval at which the subscription recurs.
          examples:
            - month
        recurring_interval_count:
          type: integer
          title: Recurring Interval Count
          description: >-
            Number of interval units of the subscription. If this is set to 1
            the charge will happen every interval (e.g. every month), if set to
            2 it will be every other month, and so on.
        status:
          $ref: '#/components/schemas/SubscriptionStatus'
          description: The status of the subscription.
          examples:
            - active
        current_period_start:
          type: string
          format: date-time
          title: Current Period Start
          description: The start timestamp of the current billing period.
        current_period_end:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Current Period End
          description: The end timestamp of the current billing period.
        trial_start:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Trial Start
          description: The start timestamp of the trial period, if any.
        trial_end:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Trial End
          description: The end timestamp of the trial period, if any.
        cancel_at_period_end:
          type: boolean
          title: Cancel At Period End
          description: >-
            Whether the subscription will be canceled at the end of the current
            period.
        canceled_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Canceled At
          description: >-
            The timestamp when the subscription was canceled. The subscription
            might still be active if `cancel_at_period_end` is `true`.
        started_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Started At
          description: The timestamp when the subscription started.
        ends_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Ends At
          description: The timestamp when the subscription will end.
        ended_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Ended At
          description: The timestamp when the subscription ended.
        customer_id:
          type: string
          format: uuid4
          title: Customer Id
          description: The ID of the subscribed customer.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the subscribed product.
        discount_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Discount Id
          description: The ID of the applied discount, if any.
        checkout_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Checkout Id
        seats:
          anyOf:
            - type: integer
            - type: 'null'
          title: Seats
          description: >-
            The number of seats for seat-based subscriptions. None for non-seat
            subscriptions.
        customer_cancellation_reason:
          anyOf:
            - $ref: '#/components/schemas/CustomerCancellationReason'
            - type: 'null'
        customer_cancellation_comment:
          anyOf:
            - type: string
            - type: 'null'
          title: Customer Cancellation Comment
        product:
          $ref: '#/components/schemas/CustomerSubscriptionProduct'
        prices:
          items:
            oneOf:
              - $ref: '#/components/schemas/LegacyRecurringProductPrice'
              - $ref: '#/components/schemas/ProductPrice'
          type: array
          title: Prices
          description: List of enabled prices for the subscription.
        meters:
          items:
            $ref: '#/components/schemas/CustomerSubscriptionMeter'
          type: array
          title: Meters
          description: List of meters associated with the subscription.
        is_polar_managed:
          type: boolean
          title: Is Polar Managed
          description: Whether the subscription is managed by Polar.
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount
        - currency
        - recurring_interval
        - recurring_interval_count
        - status
        - current_period_start
        - current_period_end
        - trial_start
        - trial_end
        - cancel_at_period_end
        - canceled_at
        - started_at
        - ends_at
        - ended_at
        - customer_id
        - product_id
        - discount_id
        - checkout_id
        - customer_cancellation_reason
        - customer_cancellation_comment
        - product
        - prices
        - meters
        - is_polar_managed
      title: CustomerSubscription
    CustomerSubscriptionMeter:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        consumed_units:
          type: number
          title: Consumed Units
          description: The number of consumed units so far in this billing period.
          examples:
            - 25
        credited_units:
          type: integer
          title: Credited Units
          description: The number of credited units so far in this billing period.
          examples:
            - 100
        amount:
          type: integer
          title: Amount
          description: The amount due in cents so far in this billing period.
          examples:
            - 0
        meter_id:
          type: string
          format: uuid4
          title: Meter Id
          description: The ID of the meter.
          examples:
            - d498a884-e2cd-4d3e-8002-f536468a8b22
        meter:
          $ref: '#/components/schemas/CustomerSubscriptionMeterMeter'
      type: object
      required:
        - created_at
        - modified_at
        - id
        - consumed_units
        - credited_units
        - amount
        - meter_id
        - meter
      title: CustomerSubscriptionMeter
    CustomerSubscriptionMeterMeter:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        name:
          type: string
          title: Name
          description: >-
            The name of the meter. Will be shown on customer's invoices and
            usage.
      type: object
      required:
        - created_at
        - modified_at
        - id
        - name
      title: CustomerSubscriptionMeterMeter
    CustomerSubscriptionProduct:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        trial_interval:
          anyOf:
            - $ref: '#/components/schemas/TrialInterval'
            - type: 'null'
          description: The interval unit for the trial period.
        trial_interval_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Trial Interval Count
          description: The number of interval units for the trial period.
        name:
          type: string
          title: Name
          description: The name of the product.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: The description of the product.
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          description: >-
            The recurring interval of the product. If `None`, the product is a
            one-time purchase.
        recurring_interval_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Recurring Interval Count
          description: >-
            Number of interval units of the subscription. If this is set to 1
            the charge will happen every interval (e.g. every month), if set to
            2 it will be every other month, and so on. None for one-time
            products.
        is_recurring:
          type: boolean
          title: Is Recurring
          description: Whether the product is a subscription.
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the product is archived and no longer available.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
          description: The ID of the organization owning the product.
        prices:
          items:
            oneOf:
              - $ref: '#/components/schemas/LegacyRecurringProductPrice'
              - $ref: '#/components/schemas/ProductPrice'
          type: array
          title: Prices
          description: List of prices for this product.
        benefits:
          items:
            $ref: '#/components/schemas/BenefitPublic'
          type: array
          title: BenefitPublic
          description: List of benefits granted by the product.
        medias:
          items:
            $ref: '#/components/schemas/ProductMediaFileRead'
          type: array
          title: Medias
          description: List of medias associated to the product.
        organization:
          $ref: '#/components/schemas/Organization'
      type: object
      required:
        - id
        - created_at
        - modified_at
        - trial_interval
        - trial_interval_count
        - name
        - description
        - recurring_interval
        - recurring_interval_count
        - is_recurring
        - is_archived
        - organization_id
        - prices
        - benefits
        - medias
        - organization
      title: CustomerSubscriptionProduct
    LegacyRecurringProductPrice:
      oneOf:
        - $ref: '#/components/schemas/LegacyRecurringProductPriceFixed'
        - $ref: '#/components/schemas/LegacyRecurringProductPriceCustom'
        - $ref: '#/components/schemas/LegacyRecurringProductPriceFree'
      discriminator:
        propertyName: amount_type
        mapping:
          custom: '#/components/schemas/LegacyRecurringProductPriceCustom'
          fixed: '#/components/schemas/LegacyRecurringProductPriceFixed'
          free: '#/components/schemas/LegacyRecurringProductPriceFree'
    LegacyRecurringProductPriceCustom:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: custom
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          type: string
          const: recurring
          title: Type
          description: The type of the price.
        recurring_interval:
          $ref: '#/components/schemas/SubscriptionRecurringInterval'
          description: The recurring interval of the price.
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        minimum_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Minimum Amount
          description: The minimum amount the customer can pay.
        maximum_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Maximum Amount
          description: The maximum amount the customer can pay.
        preset_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Preset Amount
          description: The initial amount shown to the customer.
        legacy:
          type: boolean
          const: true
          title: Legacy
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - minimum_amount
        - maximum_amount
        - preset_amount
        - legacy
      title: LegacyRecurringProductPriceCustom
      description: >-
        A pay-what-you-want recurring price for a product, i.e. a subscription.


        **Deprecated**: The recurring interval should be set on the product
        itself.
    LegacyRecurringProductPriceFixed:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: fixed
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          type: string
          const: recurring
          title: Type
          description: The type of the price.
        recurring_interval:
          $ref: '#/components/schemas/SubscriptionRecurringInterval'
          description: The recurring interval of the price.
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        price_amount:
          type: integer
          title: Price Amount
          description: The price in cents.
        legacy:
          type: boolean
          const: true
          title: Legacy
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - price_amount
        - legacy
      title: LegacyRecurringProductPriceFixed
      description: >-
        A recurring price for a product, i.e. a subscription.


        **Deprecated**: The recurring interval should be set on the product
        itself.
    LegacyRecurringProductPriceFree:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: free
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          type: string
          const: recurring
          title: Type
          description: The type of the price.
        recurring_interval:
          $ref: '#/components/schemas/SubscriptionRecurringInterval'
          description: The recurring interval of the price.
        legacy:
          type: boolean
          const: true
          title: Legacy
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - legacy
      title: LegacyRecurringProductPriceFree
      description: >-
        A free recurring price for a product, i.e. a subscription.


        **Deprecated**: The recurring interval should be set on the product
        itself.
    Organization:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The organization ID.
          examples:
            - 1dbfc517-0bbf-4301-9ba8-555ca42b9737
          x-polar-selector-widget:
            displayProperty: name
            resourceName: Organization
            resourceRoot: /v1/organizations
        name:
          type: string
          title: Name
          description: Organization name shown in checkout, customer portal, emails etc.
        slug:
          type: string
          title: Slug
          description: >-
            Unique organization slug in checkout, customer portal and credit
            card statements.
        avatar_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Avatar Url
          description: Avatar URL shown in checkout, customer portal, emails etc.
        email:
          anyOf:
            - type: string
            - type: 'null'
          title: Email
          description: Public support email.
        website:
          anyOf:
            - type: string
            - type: 'null'
          title: Website
          description: Official website of the organization.
        socials:
          items:
            $ref: '#/components/schemas/OrganizationSocialLink'
          type: array
          title: Socials
          description: Links to social profiles.
        status:
          $ref: '#/components/schemas/Status'
          description: Current organization status
        details_submitted_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Details Submitted At
          description: When the business details were submitted.
        feature_settings:
          anyOf:
            - $ref: '#/components/schemas/OrganizationFeatureSettings'
            - type: 'null'
          description: Organization feature settings
        subscription_settings:
          $ref: '#/components/schemas/OrganizationSubscriptionSettings'
          description: Settings related to subscriptions management
        notification_settings:
          $ref: '#/components/schemas/OrganizationNotificationSettings'
          description: Settings related to notifications
        customer_email_settings:
          $ref: '#/components/schemas/OrganizationCustomerEmailSettings'
          description: Settings related to customer emails
      type: object
      required:
        - created_at
        - modified_at
        - id
        - name
        - slug
        - avatar_url
        - email
        - website
        - socials
        - status
        - details_submitted_at
        - feature_settings
        - subscription_settings
        - notification_settings
        - customer_email_settings
      title: Organization
    OrganizationCustomerEmailSettings:
      properties:
        order_confirmation:
          type: boolean
          title: Order Confirmation
        subscription_cancellation:
          type: boolean
          title: Subscription Cancellation
        subscription_confirmation:
          type: boolean
          title: Subscription Confirmation
        subscription_cycled:
          type: boolean
          title: Subscription Cycled
        subscription_past_due:
          type: boolean
          title: Subscription Past Due
        subscription_revoked:
          type: boolean
          title: Subscription Revoked
        subscription_uncanceled:
          type: boolean
          title: Subscription Uncanceled
        subscription_updated:
          type: boolean
          title: Subscription Updated
      type: object
      required:
        - order_confirmation
        - subscription_cancellation
        - subscription_confirmation
        - subscription_cycled
        - subscription_past_due
        - subscription_revoked
        - subscription_uncanceled
        - subscription_updated
      title: OrganizationCustomerEmailSettings
    OrganizationFeatureSettings:
      properties:
        issue_funding_enabled:
          type: boolean
          title: Issue Funding Enabled
          description: If this organization has issue funding enabled
          default: false
        seat_based_pricing_enabled:
          type: boolean
          title: Seat Based Pricing Enabled
          description: If this organization has seat-based pricing enabled
          default: false
        revops_enabled:
          type: boolean
          title: Revops Enabled
          description: If this organization has RevOps enabled
          default: false
      type: object
      title: OrganizationFeatureSettings
    OrganizationNotificationSettings:
      properties:
        new_order:
          type: boolean
          title: New Order
        new_subscription:
          type: boolean
          title: New Subscription
      type: object
      required:
        - new_order
        - new_subscription
      title: OrganizationNotificationSettings
    OrganizationSocialLink:
      properties:
        platform:
          $ref: '#/components/schemas/OrganizationSocialPlatforms'
          description: The social platform of the URL
        url:
          type: string
          maxLength: 2083
          minLength: 1
          format: uri
          title: Url
          description: The URL to the organization profile
      type: object
      required:
        - platform
        - url
      title: OrganizationSocialLink
    OrganizationSocialPlatforms:
      type: string
      enum:
        - x
        - github
        - facebook
        - instagram
        - youtube
        - tiktok
        - linkedin
        - other
      title: OrganizationSocialPlatforms
    OrganizationSubscriptionSettings:
      properties:
        allow_multiple_subscriptions:
          type: boolean
          title: Allow Multiple Subscriptions
        allow_customer_updates:
          type: boolean
          title: Allow Customer Updates
        proration_behavior:
          $ref: '#/components/schemas/SubscriptionProrationBehavior'
      type: object
      required:
        - allow_multiple_subscriptions
        - allow_customer_updates
        - proration_behavior
      title: OrganizationSubscriptionSettings
    ProductMediaFileRead:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        organization_id:
          type: string
          format: uuid4
          title: Organization Id
        name:
          type: string
          title: Name
        path:
          type: string
          title: Path
        mime_type:
          type: string
          title: Mime Type
        size:
          type: integer
          title: Size
        storage_version:
          anyOf:
            - type: string
            - type: 'null'
          title: Storage Version
        checksum_etag:
          anyOf:
            - type: string
            - type: 'null'
          title: Checksum Etag
        checksum_sha256_base64:
          anyOf:
            - type: string
            - type: 'null'
          title: Checksum Sha256 Base64
        checksum_sha256_hex:
          anyOf:
            - type: string
            - type: 'null'
          title: Checksum Sha256 Hex
        last_modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Modified At
        version:
          anyOf:
            - type: string
            - type: 'null'
          title: Version
        service:
          type: string
          const: product_media
          title: Service
        is_uploaded:
          type: boolean
          title: Is Uploaded
        created_at:
          type: string
          format: date-time
          title: Created At
        size_readable:
          type: string
          title: Size Readable
        public_url:
          type: string
          title: Public Url
      type: object
      required:
        - id
        - organization_id
        - name
        - path
        - mime_type
        - size
        - storage_version
        - checksum_etag
        - checksum_sha256_base64
        - checksum_sha256_hex
        - last_modified_at
        - version
        - service
        - is_uploaded
        - created_at
        - size_readable
        - public_url
      title: ProductMediaFileRead
      description: File to be used as a product media file.
    ProductPrice:
      oneOf:
        - $ref: '#/components/schemas/ProductPriceFixed'
        - $ref: '#/components/schemas/ProductPriceCustom'
        - $ref: '#/components/schemas/ProductPriceFree'
        - $ref: '#/components/schemas/ProductPriceSeatBased'
        - $ref: '#/components/schemas/ProductPriceMeteredUnit'
      discriminator:
        propertyName: amount_type
        mapping:
          custom: '#/components/schemas/ProductPriceCustom'
          fixed: '#/components/schemas/ProductPriceFixed'
          free: '#/components/schemas/ProductPriceFree'
          metered_unit: '#/components/schemas/ProductPriceMeteredUnit'
          seat_based: '#/components/schemas/ProductPriceSeatBased'
    ProductPriceCustom:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: custom
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        minimum_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Minimum Amount
          description: The minimum amount the customer can pay.
        maximum_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Maximum Amount
          description: The maximum amount the customer can pay.
        preset_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Preset Amount
          description: The initial amount shown to the customer.
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - minimum_amount
        - maximum_amount
        - preset_amount
      title: ProductPriceCustom
      description: A pay-what-you-want price for a product.
    ProductPriceFixed:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: fixed
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        price_amount:
          type: integer
          title: Price Amount
          description: The price in cents.
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - price_amount
      title: ProductPriceFixed
      description: A fixed price for a product.
    ProductPriceFree:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: free
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
      title: ProductPriceFree
      description: A free price for a product.
    ProductPriceMeter:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the object.
        name:
          type: string
          title: Name
          description: The name of the meter.
      type: object
      required:
        - id
        - name
      title: ProductPriceMeter
      description: A meter associated to a metered price.
    ProductPriceMeteredUnit:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: metered_unit
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        unit_amount:
          type: string
          pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
          title: Unit Amount
          description: The price per unit in cents.
        cap_amount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Cap Amount
          description: >-
            The maximum amount in cents that can be charged, regardless of the
            number of units consumed.
        meter_id:
          type: string
          format: uuid4
          title: Meter Id
          description: The ID of the meter associated to the price.
        meter:
          $ref: '#/components/schemas/ProductPriceMeter'
          description: The meter associated to the price.
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - unit_amount
        - cap_amount
        - meter_id
        - meter
      title: ProductPriceMeteredUnit
      description: A metered, usage-based, price for a product, with a fixed unit price.
    ProductPriceSeatBased:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid4
          title: Id
          description: The ID of the price.
        amount_type:
          type: string
          const: seat_based
          title: Amount Type
        is_archived:
          type: boolean
          title: Is Archived
          description: Whether the price is archived and no longer available.
        product_id:
          type: string
          format: uuid4
          title: Product Id
          description: The ID of the product owning the price.
        type:
          $ref: '#/components/schemas/ProductPriceType'
          deprecated: true
        recurring_interval:
          anyOf:
            - $ref: '#/components/schemas/SubscriptionRecurringInterval'
            - type: 'null'
          deprecated: true
        price_currency:
          type: string
          title: Price Currency
          description: The currency.
        seat_tiers:
          $ref: '#/components/schemas/ProductPriceSeatTiers'
          description: Tiered pricing based on seat quantity
      type: object
      required:
        - created_at
        - modified_at
        - id
        - amount_type
        - is_archived
        - product_id
        - type
        - recurring_interval
        - price_currency
        - seat_tiers
      title: ProductPriceSeatBased
      description: A seat-based price for a product.
    ProductPriceSeatTier:
      properties:
        min_seats:
          type: integer
          minimum: 1
          title: Min Seats
          description: Minimum number of seats (inclusive)
        max_seats:
          anyOf:
            - type: integer
              minimum: 1
            - type: 'null'
          title: Max Seats
          description: Maximum number of seats (inclusive). None for unlimited.
        price_per_seat:
          type: integer
          maximum: 99999999
          minimum: 50
          title: Price Per Seat
          description: Price per seat in cents for this tier
      type: object
      required:
        - min_seats
        - price_per_seat
      title: ProductPriceSeatTier
      description: A pricing tier for seat-based pricing.
    ProductPriceSeatTiers:
      properties:
        tiers:
          items:
            $ref: '#/components/schemas/ProductPriceSeatTier'
          type: array
          minItems: 1
          title: Tiers
          description: List of pricing tiers
      type: object
      required:
        - tiers
      title: ProductPriceSeatTiers
      description: List of pricing tiers for seat-based pricing.
    ProductPriceType:
      type: string
      enum:
        - one_time
        - recurring
      title: ProductPriceType
    Status:
      type: string
      enum:
        - created
        - onboarding_started
        - under_review
        - denied
        - active
      title: Status
    SubscriptionProrationBehavior:
      type: string
      enum:
        - invoice
        - prorate
      title: SubscriptionProrationBehavior
    SubscriptionRecurringInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      title: SubscriptionRecurringInterval
    SubscriptionStatus:
      type: string
      enum:
        - incomplete
        - incomplete_expired
        - trialing
        - active
        - past_due
        - canceled
        - unpaid
      title: SubscriptionStatus
    TrialInterval:
      type: string
      enum:
        - day
        - week
        - month
        - year
      title: TrialInterval

````