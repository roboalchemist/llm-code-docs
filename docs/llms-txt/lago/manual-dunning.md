# Source: https://getlago.com/docs/guide/dunning/manual-dunning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manual dunning

> Dunning refers to the process of communicating with customers to remind them of overdue invoices and attempt to recover the outstanding amounts.

## Overdue balance payment

When a customer has some invoices past their due date, their [overdue balance](https://docs.getlago.com/guide/customers/customer-management#monitor-the-customers-billing-status) becomes positive, and you have the ability to request its payment manually.

<Info>
  **Premium feature ✨**

  This feature is only available to users with a premium license. Please **[contact us](mailto:hello@getlago.com)** to get access access to Lago Cloud and Lago Self-Hosted Premium.
</Info>

<Tabs>
  <Tab title="Dashboard">
    In the customer view, a "request payment” link appears within the overdue balance warning.

    <Frame caption="Request payment for the overdue balance">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-request-overdue-balance-payment.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=d6455ecbd84e12473c5492b90b974830" data-og-width="1123" width="1123" data-og-height="485" height="485" data-path="guide/images/customer-request-overdue-balance-payment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-request-overdue-balance-payment.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=4cfd9819856b9c751cf0cb274da5ccd7 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-request-overdue-balance-payment.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=4c26bebfc925d1262e33c6b3ecd8330f 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-request-overdue-balance-payment.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=39e4d6e27647be00ea9bf3db8f09c80a 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-request-overdue-balance-payment.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=63d5cb74b4733e456d7a8c7f73d77f93 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-request-overdue-balance-payment.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=584293d14b9731dc440e1cb97d43970d 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-request-overdue-balance-payment.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=47f0da5d7d7fb8c6170a6033df8ece82 2500w" />
    </Frame>

    By clicking on it, a panel opens so you can:

    * Review the invoices included in the overdue balance,
    * Review the email which will be sent in case the payment fails, or if no payment provider is linked
    * Confirm you want to request the payment.

    <Frame caption="Preview the overdue balance payment request">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-overdue-balance-payment-preview.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=531e5841e1dce9c22aa2a5ae599830ee" data-og-width="1761" width="1761" data-og-height="1179" height="1179" data-path="guide/images/customer-overdue-balance-payment-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-overdue-balance-payment-preview.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=b7317cbe3302facabe33b31ce2740976 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-overdue-balance-payment-preview.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=2af8d18b2c93e1dcbf6bf702891969b8 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-overdue-balance-payment-preview.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=73dbbbe4ba628d22a58c27a72e545aad 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-overdue-balance-payment-preview.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=7db48f886ae9efbe4053185fd1174111 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-overdue-balance-payment-preview.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=23687720dcd96a5e045ceb946eb8475f 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-overdue-balance-payment-preview.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=748091e70f722068d2ed44b3170a836a 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    You can create a payment request for the overdue balance from the API, targeting the invoices you want to be paid.

    <CodeGroup>
      ```bash Create a payment request theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request POST "$LAGO_URL/api/v1/payment_requests/" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        {
        "payment_request": {
          "lago_invoice_ids": ["4064eff9-e7a6-4692-a289-15d7d5da9b83", "b1f36d2f-8ea6-4192-9407-8e87ba5c28c2"],
          "external_customer_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
          "email": "rebecca@piedpiper.test"
        }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Dunning behaviour

<Tabs>
  <Tab title="Customer connected to a PSP">
    1. **Automatic payment attempt**: Lago will initiate a payment intent for the specified amount via the connected PSP.
    2. **Failed payment**: If the payment fails, an email will be sent to the customer with a payment request and a URL to complete the payment (excluding GoCardless).
    3. **Successful payment**: Upon success, the attached invoices will automatically reflect a “succeeded” payment status.
  </Tab>

  <Tab title="Customer not connected to a PSP">
    1. **Payment request email**: An email will be sent to the customer requesting payment for the overdue balance.
    2. **Manual update**: Once the payment is received, you must manually update the payment status of the relevant invoices
  </Tab>
</Tabs>
