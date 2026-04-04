# Source: https://getlago.com/docs/guide/payments/payment-retries.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Payment retries

## Retry an invoice payment

Whether you use one of our native integrations or rely on our [webhooks](/api-reference/webhooks/messages) to collect payments, you have the ability to manually resend payments for collection when needed.

To re-trigger the payment process through the user interface:

1. Access the **"Invoices"** section via the side menu;
2. Open the **"Outstanding"** tab;
3. Find the invoice for which you would like to collect payment;
4. Click the **ellipsis icon** on the right; and
5. Select **"Resend for collection"**.

<Frame caption="Payment retry via the invoice list">
    <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/retry-payment.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=3011a96c5a8a32b985c2c804989274a4" alt="" data-og-width="1524" width="1524" data-og-height="772" height="772" data-path="guide/payments/images/retry-payment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/retry-payment.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=5c72b1739fc9506fedfef43384778826 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/retry-payment.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ed3c63b06851ba05096f50ea2d43066b 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/retry-payment.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f000ce95a1ff6ce387d351f9cbc8916e 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/retry-payment.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=583ef6126a16151731404f20d25f1c2a 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/retry-payment.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=1764608516b903d31a79277956c6f60f 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/retry-payment.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=b53b806e8ce1482449fbf463445204fd 2500w" />
</Frame>

In the **"Outstanding"** and **"Overdue"** tabs of the **"Invoices"** section, you can also click **"Resend for collection"** in the upper right corner to re-trigger the payment process for all invoices in the respective lists.

<Info>
  Invoices that are overdue are available both on the **"Outstanding"** and the **"Overdue"** tabs. Make sure you resend for collection from the **"Overdue"** tab if you wish to collect payment for past due invoices only.
</Info>

When you resend a payment for collection, Lago automatically attempts to process the payment.

* If the payment **succeeds**, an `invoice.payment_status_updated` webhook is sent.
* If the payment **fails**, an `invoice.payment_failure` webhook is sent.
* If the customer **doesn’t have a payment method** available for Lago to retry, an `invoice.payment_failure` webhook is also sent.

It is also possible to trigger payment retries via the API ([learn more](/api-reference/invoices/retry)).

## Generate a payment url

If you’re using a payment provider integration, you can generate a payment URL [for unpaid invoices](/api-reference/invoices/payment-url) or [unpaid wallet transactions](/api-reference/wallets/wallet-transaction-payment-url) to share with the end customer. This URL initiates a checkout flow where the customer can pay the invoice or wallet transaction by providing a payment method.

To prevent duplicate payments, the generated URL is idempotent. It remains valid and unchanged for 24 hours, regardless of how many times the endpoint is called. After this period, a new URL will be issued upon the next call to the endpoint, valid for the following 24 hours.
