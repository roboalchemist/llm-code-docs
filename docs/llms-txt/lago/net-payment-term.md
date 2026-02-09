# Source: https://getlago.com/docs/guide/invoicing/invoicing-settings/net-payment-term.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Net payment term

> Number of days a customer has to pay an invoice after it has been finalized

A net payment term refers to the specified number of days within which the end customer is required to settle the invoice after its finalization.
This term not only affects the `payment_due_date` within the invoice payload but also influences the due date mentioned in the downloadable PDF version of the invoice.

To illustrate, consider the following scenario:
a billing cycle spanning one month, accompanied by a net payment term of 15 days.

<Frame caption="Illustration of the net payment term period">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/net-payment-term-timeline.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=d8fe5ed46edc6680d9bb083596c4082e" data-og-width="2516" width="2516" data-og-height="508" height="508" data-path="guide/invoicing/images/net-payment-term-timeline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/net-payment-term-timeline.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=83090b79ae431a19a41aa8973d088b18 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/net-payment-term-timeline.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=355ecbe3a8bd2263322e34f5d01f1fa4 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/net-payment-term-timeline.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=27cc5bfae5ede41ac274ec5ff93acb15 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/net-payment-term-timeline.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=9c71bf9073b858276201686e1b409956 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/net-payment-term-timeline.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=92a0e4d5e7837c95e95e1e96e82e853a 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/net-payment-term-timeline.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=4c036c7b8056f800f98c9dfeed4653e8 2500w" />
</Frame>

## Application scope[](#application-scope "Direct link to heading")

The net payment term period applies to all types of invoices, and is used to compute the payment due date.

When the `payment_due_date` has passed, the invoice is flagged as overdue (`payment_overdue` = `true`), and Lago emits an `invoice.payment_overdue`
[webhook message](/api-reference/webhooks/messages).

The invoice stays flagged as overdue until the payment is `succeeded`, or `payment_dispute_lost_at` is applied, or the invoice is voided.

## Define a net payment term at entity level[](#define-a-net-payment-term-at-entity-level "Direct link to heading")

The entity's net payment term applies to all customers link to this object by default.

<Tabs>
  <Tab title="Dashboard">
    To define a net payment term at the enitty level via the user interface, follow these steps:

    1. Access the **Settings** section using the side menu;
    2. Navigate to the **Billing entity** > **Invoicing setting** section;
    3. Click **Edit** in the **Net payment term** section;
    4. Select the desired number of days for the payment term or opt for a custom duration; and
    5. Confirm by clicking **"Edit net payment term"**.
  </Tab>

  <Tab title="API">
    You can also modify the entity’s net payment term at any time through the API

    <CodeGroup>
      ```bash Add a net payment term on the billing entity theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request PUT "$LAGO_URL/api/v1/billing_entities/{code}" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "billing_entity": {
        	    "net_payment_term": 15
        }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Define a net payment term at customer level[](#define-a-net-payment-term-at-customer-level "Direct link to heading")

<Tabs>
  <Tab title="Dashboard">
    To define a net payment term at the customer level through the user interface, follow these steps:

    1. Access the **"Customers"** section via the side menu;
    2. Select a customer from the list;
    3. Open the **"Settings"** tab of the customer view;
    4. Click **"Add a net payment term"** in the **"Net payment term"** section;
    5. Choose the desired number of days for the payment term or opt for a custom duration; and
    6. Click **"Add net payment term"** to confirm.
  </Tab>

  <Tab title="API">
    You can also modify the customer's net payment term at any time through [the API](/api-reference/customers/update).
    Define a net payment term in days by using the `net_payment_term argument` within the `customer` object.

    <CodeGroup>
      ```bash Add a net payment term on a customer theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request PUT "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
        	    "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
        	    "net_payment_term": 15
        }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

The customer's net payment term supersedes the one defined at the entity level.
It exclusively applies to the associated customer.
