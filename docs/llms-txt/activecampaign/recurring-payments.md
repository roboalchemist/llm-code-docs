# Source: https://developers.activecampaign.com/reference/recurring-payments.md

# Recurring Payments

# General Information

ActiveCampaign empowers subscription businesses with the automations necessary to increase customer lifetime value (CLV), drive AOV, and reduce churn.\
Automations enable subscription businesses to deliver superior customer experiences needed to foster loyalty, increase retention rates, and drive sustainable growth. By automating tasks, personalizing communication, and proactively addressing customer needs–businesses can create seamless and engaging subscription journeys that keep customers satisfied and coming back for more.

In ActiveCampaign, subscriptions are called Recurring Payments.

## Primary Identifier

A unique recurring payment is identified by a combination of the fields `legacyConnectionId` and `storeRecurringPaymentId`. When performing a `bulkUpsertRecurringPayments` call, if a recurring payment has a unique `legacyConnectionId`-`storeRecurringPaymentId` combination, a new recurring payment will be created. If a recurring payment with a given `legacyConnectionId`-`storeRecurringPaymentId` already exists, the existing recurring payment will be updated.

## Normalized Status

In the ActiveCampaign Recurring Payment model, we set a field called `normalizedStatus` which as a predefined set of statuses within ActiveCampaign. Anyone using the Recurring Payment API needs to map the statuses that are native to their store to our normalized status.

In addition to `normalizedStatus`, API users should save the status native to their store in the freeform string `storeStatus` field.

The following are legal values for the normalizedStatus field and their definitions:

| Status          | Meaning                                                                                                                                                 |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ACTIVE          | Recurring Payment is Active                                                                                                                             |
| CANCELLED       | User cancelled Recurring payment.                                                                                                                       |
| EXPIRED         | Recurring payment is expired.                                                                                                                           |
| PAYMENT\_FAILED | At least one payment has failed for this user. Depending on store behavior, subscription may be active still or already terminated for payment failure. |
| PAUSED          | Recurring payment is paused or on hold.                                                                                                                 |
| PENDING         | Recurring payment is pending. It could be pending manual approval or pending payment, but it is in some way pending a step before activation.           |

### WooCommerce Status Mappings

For our WooCommerce integration, these are how the store statuses map to ActiveCampaign statuses:

| WooCommerce Status | ActiveCampaign Status |
| :----------------- | :-------------------- |
| pending            | PENDING               |
| active             | ACTIVE                |
| on-hold            | PAUSED                |
| expired            | EXPIRED               |
| pending-cancel     | PAYMENT\_FAILED       |
| cancelled          | CANCELLED             |

<br />

# Queries

## searchRecurringPayment

```graphql
query{
    searchRecurringPayment(filter: {email: {
        value: "email@activecampaign.com"
        filterOperator: EQ
    }
}) {
    id
    legacyConnectionId
    storeRecurringPaymentId
  	name
    email
    normalizedStatus
    storeStatus
    storeCustomerId
    billingInterval
    billingIntervalCount
    paymentAmount
    discountAmount
    taxAmount
    shippingAmount
    lastPaymentStatus
    lastPaymentDate
    startDate
    renewalDate
    nextPaymentDate
    anchorDate
    cancelledDate
    paymentMethodExpiration
    originOrderId
    currency
    storeCreatedDate
    storeModifiedDate
    isTrial
    cancelAtPeriodEnd
    totalCycles
    notes
    storeExternalId
    billingAddress {
        firstName
        lastName
        address1
        address2
        company
        city
        phone
        province
    }
    shippingAddress {
        firstName
        lastName
        address1
        address2
        company
        city
        phone
        province
    }
    lineItemCategories
    lineItemNames
    lineItemSkus
    lineItemBrands
    lineItemTags
    lineItemStorePrimaryIds
    }
}
```

### Return Type

[RecurringPayment](https://developers.activecampaign.com/reference/recurring-payments#recurringpayment)\[]

### Arguments

| Name (type)                                                                                                                  | Description                                                                                                                                         |
| :--------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter ([RecurringPaymentFilter](https://developers.activecampaign.com/reference/recurring-payments#recurringpaymentfilter)) | Filter with details of search. For general details about searches, see [GraphQL Searches](https://developers.activecampaign.com/reference/searches) |

# Mutations

## bulkUpsertRecurringPayments

The bulkUpsertRecurringPayment operation will insert one or more recurring payments asynchronously.

### Example Payload

```graphql graphql
mutation{
    bulkUpsertRecurringPayments(recurringPayments: [
        {
            legacyConnectionId: 15,
            storeRecurringPaymentId: "abc123",
            name: "RecurringPayment",
            email: "email@activecampaign.com",
            normalizedStatus: PENDING,
            storeStatus: "Pending",
            billingInterval: MONTHLY,
            billingIntervalCount: 1,
            paymentAmount: 20.00,
            discountAmount: 0.00,
            taxAmount: 0.00,
            shippingAmount: 1.00,
            lastPaymentStatus: COMPLETED,
            lastPaymentDate: "2024-02-14T10:48:23Z",
            startDate: "2024-02-14T10:48:23Z",
            renewalDate: "2025-02-14T10:48:23Z",
            nextPaymentDate: "2024-02-14T10:48:23Z",
            anchorDate: "2024-02-14T10:48:23Z",
            paymentMethodExpiration: "2024-02-14T10:48:23Z",
            originOrderId: "123",
            storeCreatedDate: "2024-02-14T10:48:23Z",
            storeModifiedDate: "2024-02-14T10:48:23Z",
            isTrial: false,
            cancelAtPeriodEnd: false,
            totalCycles: 12,
            storeExternalId: "abc123",
            billingAddress: {
                firstName: "First",
                lastName: "Name",
                address1: "123 Recurring St",
                city: "Chicago",
                province: "IL",
                postal: "60640",
                phone: "555-555-5555"
            },
            lineItemBrands: ["brand1", "brand2"],
            lineItemCategories: ["category1", "category2"],
            lineItemNames: ["name1", "name2"],
            lineItemSkus: ["SKU1", "SKU2"],
            lineItemStorePrimaryIds: ["123", "456"],
            customerData: {
                firstName: "First",
                lastName: "Name",
                acceptsMarketing: true,
                smsMarketingState: NOT_SUBSCRIBED,
                smsOptInLevel: UNKNOWN
            }
        }
    ]){
        recordId
    }
}
```

### Return Type

[BulkAsync](https://developers.activecampaign.com/reference/shared-objects#bulkasync-response)

### Arguments

| Name (type)                                                                                                                         | Description                                                              |
| :---------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| recurringPayments ([RecurringPaymentInput](https://developers.activecampaign.com/reference/recurring-payments#recurringpayment)\[]) | An array of Recurring Payment objects that will be asynchronously saved. |

# Objects

## RecurringPayment

| Name                                                                                                                                             | Description                                                                                                                                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| legacyConnectionId (`Int`) **Required**                                                                                                          | Integer connection identifier matching the v3 API DeepData Connection ID.                                                                                                             |
| storeRecurringPaymentId (`String`) **Required**                                                                                                  | id of recurring payment object in external service. Within a connection, this serves as the primary identifier of this recurring payment record.                                      |
| name ( `String`)                                                                                                                                 | Name of recurring payment                                                                                                                                                             |
| email (`String`)                                                                                                                                 | Email of customer placing recurring payment. Upon calling the API, an ActiveCampaign Contact will be created for this email if one does not already exist.                            |
| normalizedStatus (`Enum`)                                                                                                                        | ActiveCampaign defined status of this object. One of: ACTIVE, CANCELLED, EXPIRED, PAYMENT\_FAILED, PAUSED, PENDING. See note on normalizedStatus.                                     |
| storeStatus (`String`)                                                                                                                           | Freeform string field representing the exact status from store.                                                                                                                       |
| storeCustomerId (`String`)                                                                                                                       | The identifier for the customer in the store. This is automatically saved to an [ActiveCampaign Customer](https://developers.activecampaign.com/reference/customers) as `externalid`. |
| billingInterval (`RecurringPaymentBillingInterval`)                                                                                              | How often the customer pays. Enum of: DAILY, WEEKLY, MONTHLY, YEARLY                                                                                                                  |
| billingIntervalCount (`Int`)                                                                                                                     | Number of billingIntervals between payments                                                                                                                                           |
| paymentAmount (`BigDecimal`)                                                                                                                     | The total amount per billing cycle including taxes, discounts, and shipping                                                                                                           |
| discountAmount (`BigDecimal`)                                                                                                                    | The amount discounted from a full price each time the customer is billed.                                                                                                             |
| taxAmount (`BigDecimal`)                                                                                                                         | The amount the customer pays in taxes each time they are billed.                                                                                                                      |
| shippingAmount (`BigDecimal`)                                                                                                                    | Total amount for shipping                                                                                                                                                             |
| lastPaymentStatus (`Enum`)                                                                                                                       | Status of most recent payment. Must be one of: COMPLETED, DECLINED, PARTIALLY\_REFUNDED, PENDING, REFUNDED                                                                            |
| lastPaymentDate (`String`)                                                                                                                       | Date of last payment attempt. Must be in format 2019-11-16T10:48:23Z                                                                                                                  |
| startDate (`String`)                                                                                                                             | Recurring Payment start date. Must be in format 2019-11-16T10:48:23Z                                                                                                                  |
| renewalDate (`String`)                                                                                                                           | The date where the recurring payment will next be billed for renewal. Must be in format 2019-11-16T10:48:23Z                                                                          |
| nextPaymentDate (`String`)                                                                                                                       | Next date customer will be billed. Must be in format 2019-11-16T10:48:23Z                                                                                                             |
| anchorDate (`String`)                                                                                                                            | Date that the billing cycle is based on. Must be in format 2019-11-16T10:48:23Z                                                                                                       |
| cancelledDate (`String`)                                                                                                                         | Date when was the recurring payment cancelled/paused. Must be in format 2019-11-16T10:48:23Z                                                                                          |
| paymentMethodExpiration (`String`)                                                                                                               | Date when the payment method for this recurring payment will expire (defaults to the 1st day of the month). Must be in format 2019-11-16T10:48:23Z                                    |
| storeCreatedDate (`String`)                                                                                                                      | Date the record was created in external service. Must be in format 2019-11-16T10:48:23Z                                                                                               |
| storeModifiedDate (`String`)                                                                                                                     | Date the record was last modified in external service. Must be in format 2019-11-16T10:48:23Z                                                                                         |
| originOrderId (`String`)                                                                                                                         | ID of the order that created this recurring payment. Related to `id` field on GraphQL order.                                                                                          |
| currency (`String`)                                                                                                                              | 2-digit currency recurring payment was created with.                                                                                                                                  |
| isTrial (`Boolean`)                                                                                                                              | Whether or not this recurring payment is a trial                                                                                                                                      |
| cancelAtPeriodEnd (`Boolean`)                                                                                                                    | If true, when the current period ends, recurring payment will not renew, recurring payment will be cancelled.                                                                         |
| totalCycles (`Int`)                                                                                                                              | Total number of times to run this billing cycle, 0 for infinite (e.g. only bill customer 10 times, then stop).                                                                        |
| notes (`[String]`)                                                                                                                               | Notes about the recurring payment.                                                                                                                                                    |
| storeExternalId (`String`)                                                                                                                       | A second identifier from the store, usually a key to some external system.                                                                                                            |
| billingAddress (`[[AddressInput](https://developers.activecampaign.com/reference/shared-objects#address)]`)                                      | Billing Address                                                                                                                                                                       |
| shippingAddress (`[[AddressInput](https://developers.activecampaign.com/reference/shared-objects#address)]`)                                     | Shipping Address                                                                                                                                                                      |
| customerData (`[RecurringPaymentCustomerData](https://developers.activecampaign.com/reference/recurring-payments#recurringpaymentcustomerdata)`) | See note about RecurringPaymentCustomerData.                                                                                                                                          |
| lineItemCategories (`[String]`)                                                                                                                  | A list of all product categories across all line items in this recurring payment.                                                                                                     |
| lineItemNames (`[String]`)                                                                                                                       | A list of all product names across all line items in this recurring payment.                                                                                                          |
| lineItemSkus (`[String]`)                                                                                                                        | A list of all skus across all line items in this recurring payment.                                                                                                                   |
| lineItemBrands (`[String]`)                                                                                                                      | A list of all brands (also known as vendors) across all line items in this recurring payment.                                                                                         |
| lineItemTags (`[String]`)                                                                                                                        | A list of all tags across all line items in this recurring payment.                                                                                                                   |
| lineItemStorePrimaryIds (`[String]`)                                                                                                             | A list of all store primary ids across all products in this recurring payment. The store primary Id is the primary and unique identifier for a product within the store.              |

## RecurringPaymentFilter

For information on how filters and search requests work, see: [Searches](https://developers.activecampaign.com/reference/searches).

The following attributes in Recurring Payments may be used for search requests:

| Name                                                           |
| :------------------------------------------------------------- |
| id (`StringFieldFilter`)                                       |
| legacyConnectionId (`IntFieldFilter`)                          |
| storeRecurringPaymentId (`StringFieldFilter`)                  |
| name (`StringFieldFilter`)                                     |
| email (`StringFieldFilter`)                                    |
| normalizedStatus (`RecurringPaymentStatusFieldFilter`)         |
| storeStatus (`StringFieldFilter`)                              |
| storeCustomerId (`StringFieldFilter`)                          |
| billingInterval (`RecurringPaymentBillingIntervalFieldFilter`) |
| billingIntervalCount (`IntFieldFilter`)                        |
| paymentAmount (`NumberFieldFilter`)                            |
| discountAmount (`NumberFieldFilter`)                           |
| taxAmount (`NumberFieldFilter`)                                |
| shippingAmount (`NumberFieldFilter`)                           |
| lastPaymentStatus (`RecurringPaymentPaymentStatusFieldFilter`) |
| lastPaymentDate (`StringFieldFilter`)                          |
| startDate (`StringFieldFilter`)                                |
| renewalDate (`StringFieldFilter`)                              |
| nextPaymentDate (`StringFieldFilter`)                          |
| anchorDate (`StringFieldFilter`)                               |
| cancelledDate (`StringFieldFilter`)                            |
| paymentMethodExpiration (`StringFieldFilter`)                  |
| currency (`StringFieldFilter`)                                 |
| storeCreatedDate (`StringFieldFilter`)                         |
| storeModifiedDate (`StringFieldFilter`)                        |
| isTrial (`BooleanFieldFilter`)                                 |
| cancelAtPeriodEnd (`BooleanFieldFilter`)                       |
| totalCycles (`IntFieldFilter`)                                 |
| notes (`StringFieldFilter`)                                    |
| storeExternalId (`StringFieldFilter`)                          |
| billingAddress (`AddressFilter`)                               |
| shippingAddress (`AddressFilter`)                              |
| lineItemCategories (`StringFieldFilter`)                       |
| lineItemNames (`StringFieldFilter`)                            |
| lineItemSkus (`StringFieldFilter`)                             |
| lineItemBrands (`StringFieldFilter`)                           |
| lineItemTags (`StringFieldFilter`)                             |
| lineItemStorePrimaryIds (`StringFieldFilter`)                  |

## RecurringPaymentCustomerData

RecurringPaymentCustomerData represents fields on a recurring payment that are not saved into the Custom Object but rather directly saved into the ActiveCampaign contact and customer.

| Name                             | Description                                                                                                        |
| :------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| firstName (`String`)             | First name of customer. If set, this will be used in updating the first name of the contact in ActiveCampaign.     |
| lastName (`String`)              | Last name of customer. If set, this will be used in updating the last name of the contact in ActiveCampaign.       |
| phone (`String`)                 | Phone number of customer. If set, this will be used in updating the phone number of the contact in ActiveCampaign. |
| company (`String`)               | Company of customer. If set, this will be used in updating the orgname of the contact in ActiveCampaign.           |
| acceptsMarketing (`Boolean`)     | Whether the customer has opted into marketing communications.                                                      |
| smsMarketingState (`Enum`)       | Sms Marketing State of customer. Must be one of: `NOT_SUBSCRIBED, PENDING, REDACTED, SUBSCRIBED, UNSUBSCRIBED`     |
| smsOptInLevel (`Enum`)           | Opt in level for SMS marketing. Must be one of: `CONFIRMED_OPT_IN    SINGLE_OPT_IN UNKNOWN`                        |
| smsConsentUpdatedDate (`String`) | Date when the SMS consent was last updated. Must be in format 2019-11-16T10:48:23Z                                 |