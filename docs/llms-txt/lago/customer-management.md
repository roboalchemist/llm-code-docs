# Source: https://getlago.com/docs/guide/customers/customer-management.md

# Customer management

## Create and update a customer[](#create-and-update-a-customer "Direct link to heading")

<Tabs>
  <Tab title="Dashboard">
    To create a customer through the user interface:

    1. Access the **"Customers"** section via the side menu;
    2. In the upper right corner, click **"Add a customer"**;
    3. Enter the customer's name and external ID (i.e. unique ID as defined in your
       backend system);
    4. Select the customer's timezone (optional -
       [learn more](/guide/customers/invoice-customer#bill-following-your-customers-timezone));
    5. Enter the customer's billing information, including company information and
       address (optional);
    6. Select the default payment provider for this customer (optional -
       [learn more](/guide/payments/payment-providers); and
    7. Click **"Create customer"** to confirm.
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Create or update a customer theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
         "customer": {
            "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
            "address_line1": "5230 Penfield Ave",
            "address_line2": "",
            "city": "Woodland Hills",
            "country": "US",
            "currency": "EUR",
            "email": "dinesh@piedpiper.test",
            "legal_name": "Coleman-Blair",
            "legal_number": "49-008-2965",
            "tax_identification_number": "EU123456789",
            "logo_url": "http://hooli.com/logo.png",
            "name": "Gavin Belson",
            "phone": "1-171-883-3711 x245",
            "state": "CA",
            "timezone": "Europe/Paris",
            "url": "http://hooli.com",
            "zipcode": "91364",
            "tax_codes": [],
            "billing_configuration": {
               "invoice_grace_period": 3,
               "payment_provider": "stripe",
               "provider_customer_id": "cus_12345",
               "sync": true,
               "sync_with_provider": true,
               "document_locale": "fr",
            }
            "metadata": [
            {
               "key": "Name",
               "value": "John",
               "display_in_invoice": true
            }
            ]
         }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

Once a customer is created, you can access the customer view, where you can edit their information.

<Warning>
  You cannot change the `external_id` and the `currency` of customers after an object has been
  assigned to them (i.e. plans, coupons, one-off invoices, wallet and credits).
</Warning>

## Companies vs Individuals

When creating or updating a customer, you can specify whether the customer is a `company` or an `individual` by setting the customer type.
By default, if no customer type is specified, the customer will be created without a defined type, and you will need to assign one manually.

## Assign objects to a customer[](#assign-objects-to-a-customer "Direct link to heading")

The usage monitoring and billing processes start when you assign a plan to a
customer, which triggers a [subscription](/guide/subscriptions/assign-plan).

You can also apply [coupons](/guide/coupons), [one-off invoices](/guide/one-off-invoices/create-one-off-invoices) and
[prepaid credits](/guide/wallet-and-prepaid-credits) to a customer account.

To assign objects to a customer through the user interface:

1. Access the **"Customers"** section via the side menu;
2. Select a customer from the list;
3. In the upper right corner of the customer view, click **"Actions"**; and
4. Select an action from the dropdown list.

## Monitor the customer's current usage[](#monitor-the-customers-current-usage "Direct link to heading")

When a plan that includes usage-based charges is assigned to a customer, you can
start pushing [events](/guide/events/ingesting-usage) associated with the customer account.

During the billing period, the customer's current usage is visible in the
**"Analytics"** tab of the customer view, under **"Current usage report** including (but not limited to):

* Total amount for the period under consideration; and
* Breakdown by charge, including total number of billing units and amount.

<Tabs>
  <Tab title="Dashboard">
    <Frame caption="Fetch customer's current usage">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-current-usage.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=bc625db77d8f8a7db945175773ca607d" data-og-width="1502" width="1502" data-og-height="888" height="888" data-path="guide/images/customer-current-usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-current-usage.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=16d5c1833153e5f070462ccdb4447fa9 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-current-usage.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=87c07c9908f92141c3f8dc0cfbeea11e 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-current-usage.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=5f33fa3de25c4c1b20a1798296112d91 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-current-usage.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=d4a466a1ced8f47470c07423c8f47f21 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-current-usage.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=6fa5e84025d8fdd75b16c81573e00202 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-current-usage.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=c71bb1e7c708fb00870013a185520b51 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    You can retrieve the customer's current usage via the API using [this endpoint](/api-reference/customer-usage/get-current).

    <CodeGroup>
      ```bash Get customer current usage theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"
      EXTERNAL_CUSTOMER_ID="5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba"
      EXTERNAL_SUBSCRIPTION_ID="sub_1234567890"

      curl --location --request GET "$LAGO_URL/api/v1/customers/$EXTERNAL_CUSTOMER_ID/current_usage?external_subscription_id=$EXTERNAL_SUBSCRIPTION_ID" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Monitor the customer's billing status[](#monitor-the-customers-overdue-balance "Direct link to heading")

The "**Billing overview**" lets you see in a glance where a customer stands in terms of revenue and collection. It takes into account invoices since the customer's creation date.

* Gross revenue indicates how much has been billed to this customer
* Total overdue highlights the aggregated amount from invoices that are past due

<Tabs>
  <Tab title="Dashboard">
    <Frame caption="Check a customer's billing status">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-billing-overview.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=2f6c65bfc38feb19c4c1b0c5912895e4" data-og-width="3340" width="3340" data-og-height="1698" height="1698" data-path="guide/images/customer-billing-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-billing-overview.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=663d72fa8eeb0ff42372b783a104f060 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-billing-overview.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=d061188370675a74f42a50224aa3f968 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-billing-overview.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=379bd7e6ac1b6b08671cb83161ad6a0a 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-billing-overview.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=31fe8287a7efc7a72eeea79595f755f0 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-billing-overview.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=9b61d4bd3cd857098664adb4605bca50 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-billing-overview.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=ae2186ad9e2e7f83501e5a06c936089b 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    You can retrieve the customer's gross revenue via the API using [this endpoint](/api-reference/analytics/gross-revenue).

    <CodeGroup>
      ```bash Get customer gross revenue theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request GET "$LAGO_URL/api/v1/analytics/gross_revenue?external_customer_id=hooli_1234&currency=USD" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \  
      ```
    </CodeGroup>

    You can retrieve the customer's overdue balance via the API using [this endpoint](/api-reference/analytics/overdue-balance).

    <CodeGroup>
      ```bash Get customer overdue balance theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request GET "$LAGO_URL/api/v1/analytics/overdue_balance?external_customer_id=hooli_1234&currency=USD" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \  
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Deleting a customer

You may delete a customer linked to existing objects (i.e. applied coupons, wallets, subscriptions, add-ons).

If you do so:

* All [subscriptions](/guide/subscriptions/assign-plan) associated with this customer account will be immediately terminated (this action may trigger the generation of invoices and/or credit notes);
* All [coupons](/guide/coupons) applied to this customer account will be immeditely terminated;
* The customer's active [wallet](/guide/wallet-and-prepaid-credits) will be immediately terminated and all remaining credits will be voided; and
* All `draft` invoices associated with this customer account will be immediately finalized.

`finalized` invoices and [credit notes](/guide/credit-notes) associated with the deleted customer remain available in the **"Invoices"** section of the user interface and can also be retrieved via the API.

It is possible to generate new credit notes and process refunds after the deletion of the customer.

<Info>
  After deleting a customer account, you can create a new one using the same `external_id`.
</Info>
