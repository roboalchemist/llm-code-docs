# Source: https://getlago.com/docs/guide/payments/record-manual-payments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Record manual payments

> On top of our native integrations with leading payment providers, you can also record manual payments.

For manual or non-Lago-native payment methods, you can record payments via the API or UI.
Both partial and full payments can be recorded; however, an invoice's payment status will only update to succeeded when it is fully settled.

<Tabs>
  <Tab title="Dashboard">
    To record a payment:

    1. Navigate to an unpaid invoice;
    2. Click the “Record Payment” button;
    3. Select the payment date;
    4. Enter the payment reference;
    5. Specify the payment amount (partial or full); and
    6. Confirm to record the payment.

    <Frame caption="Record a manual payment">
      <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/record-payment.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=b14f4093843aa685d9ce97a61a41ba56" data-og-width="2952" width="2952" data-og-height="2094" height="2094" data-path="guide/payments/images/record-payment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/record-payment.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=fc0d01e283db089fa31fdba588b5bd4c 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/record-payment.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=971b00b2d7d261d967758d4aa043ddcf 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/record-payment.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=0b1c13d5897f2d53a60e0a9db749177e 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/record-payment.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=6bc625f308e3a18acf12cad4343f25c2 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/record-payment.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=918a5961c019022ecbfdbd122a096077 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/payments/images/record-payment.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=6c08f4d84f8181c2132585d263d81575 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Record a manual payment theme={"dark"}
        curl --request POST \
        --url https://api.getlago.com/api/v1/payments \
        --header 'Authorization: Bearer <token>' \
        --header 'Content-Type: application/json' \
        --data '{
        "payment": {
          "invoice_id": "486b147a-02a1-4ccf-8603-f3541fc25e7a",
          "amount_cents": 100,
          "reference": "ref1",
          "paid_at": "2025-02-20"
        }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>
