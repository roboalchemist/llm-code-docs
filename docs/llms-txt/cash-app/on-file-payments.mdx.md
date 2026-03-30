# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/payment-processing/on-file-payments.mdx

***

## stoplight-id: a7028dbbb9d9d

# On-file Payments

Cash App Pay has the  ability to support an on-file grant (Cashtag on file) for a Customer. This means that the on-file grant can be charged when the Customer makes future purchases.

This makes future purchases easier and quicker for the Customer, since they do not have to add their payment information and validate that information every time they make a transaction.

## On-file payment flow

### Step 1: Generate an on-file grant via Pay Kit

To create an on-file grant, you must specify an on-file payment action when creating the customer request. This action must include a `scope ID` and optionally an `account reference ID`.

See more information on [Scope ID](#scope-id) and [Account Reference ID](#account-reference-id) in [Important Terms](#important-terms).

### Example

```javascript
details.actions.onFile = {
  scopeId: 'brand_id_from_network_api',
  accountReferenceId: 'external_account_id',
};
```

<Note>
  If a valid on-file grant exists and a Cash App Customer approves a new on-file grant flow with the same Scope and Account Reference ID, the same Grant ID will be returned by the approved grant flow.
</Note>

### Step 2: Save Customer and grant information

An on-file grant cannot be retrieved via API. Therefore, on-file grants should always be stored at the time of grant creation; otherwise, the customer will have to generate a new on-file grant.

You can retrieve [Customer](/cash-app-pay-partner-api/api-reference/network-api/retrieve-customer) and [Grant](/cash-app-pay-partner-api/api-reference/network-api/retrieve-customer-grant) information if you have a valid `customer_id` and `grant_id`. Relevant customer information includes a customer's Cashtag and relevant grant information includes grant status and expiration date.

<br />

> If you are also saving a Customer's Cashtag, note that Cashtags are not static and can be changed up to 3 times. Ensure that Cashtags are correct by subscribing to `customer.updated` webhooks. Cashtags are not considered PII and should be displayed in your checkout flow and in the customer's account settings. See our [brand guidelines](/cash-app-pay-partner-api/guides/resources/cash-app-pay-assets) for more details.

```curl
curl --request GET \
    --url https://sandbox.api.cash.app/network/v1/customers/customer_id \
    --header 'Authorization: Client api_key' \
    --header 'X-Region: PDX' \
    --header 'accept: application/json'
```

<br />

```curl
curl --request GET \
     --url https://sandbox.api.cash.app/network/v1/customers/customer_id/grants/grant_id \
     --header 'Authorization: Client api_key' \
     --header 'X-Region: PDX' \
     --header 'accept: application/json'
```

### Suggested disclaimer copy for \$Cashtag on-file

Cash App Pay suggests that you add this disclaimer when a customer selects \$Cashtag on-file for payment:

> By continuing, you authorize **`{{Merchant Name}}`** to debit your Cash App account for this payment and future payments in accordance with **`{{Merchant Name}}`**'s terms, until this authorization is revoked. You can change this authorization anytime in your Cash App Settings.

### Step 3: Authorize an on-file payment

Once an on-file grant has been successfully created, you can immediately use the grant to authorize a payment or simply save the grant for use in the future.

```curl
curl --request POST \
     --url https://sandbox.api.cash.app/network/v1/payments \
     --header 'Authorization: Client api_key' \
     --header 'X-Region: PDX' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
    "payment": {
         "capture": true,
         "amount": 1234,
         "currency": "USD",
         "merchant_id": "merchant_id",
         "grant_id": "onfile_grant",
         "reference_id": "external-id"
    },
    "idempotency_key": "random_uuid"
}
```

### Step 4: Revoking an on-file grant

Once an on-file grant is created, it can be used to create payments on behalf of the Customer for 10 years. If, for whatever reason the grant needs to be revoked, you can use the [revoke customer grant](/cash-app-pay-partner-api/api-reference/network-api/revoke-customer-grant) endpoint to prevent the grant from being used for future payments.

<br />

```curl
curl --request POST \
     --url https://sandbox.api.cash.app/network/v1/customers/customer_id/grants/grant_id/revoke \
     --header 'Authorization: Client api_key' \
     --header 'X-Region: PDX' \
     --header 'accept: application/json'
```

<br />

Also, a Customer can remove the businesses with whom they have active on-file grants. Cash App provides [grant.status.updated](/cash-app-pay-partner-api/api-reference/network-api/grant-status-updated) webhooks to alert Partners when any change to the on-file grant happens.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/remove-on-file-grant.png" alt="Remove on file grant" noZoom />

## Important terms

### Scope ID

The scope of an on-file grant determines which Merchants have the ability to authorize a payment with the grant. The `scope_id` can be set to one of these:

* **Client:** The grant from a Client-scoped on-file action can be used to create a payment for any Merchant owned by the Client.
  * **Client example:** A PSP provides a hosted wallet solution where Customers can save payment methods on-file and use these payment methods to seamlessly checkout with Merchants supported by the PSP.
* **Brand:** The grant from a Brand-scoped on-file action can be used to create a payment for any Merchant that has a matching Brand ID.
  * **Brand example:** A specific Merchant wants to support Cashtag on-file for their customers.

### Account Reference ID

The Account Reference ID represents the identifier of the Account or Customer associated with the on-file action. Attempting to create a new on-file grant with the same Scope but different Account Reference ID will result in a new unique on-file grant.

**Example:**  A Cash App Customer and their partner have separate accounts on a popular e-commerce website. They both want to save the same Cash App account on-file for their separate accounts. Account reference ID allows the e-commerce website to generate a unique on-file grant for each of these customer accounts - each grant can be managed independently and access can be revoked for one account without removing access to the other.

## Merchant eligibility

Reach out to the Partner Engineering team or your Cash App Point of Contact to check if you are eligible to set up \$Cashtag on-file payments for your Customers.
