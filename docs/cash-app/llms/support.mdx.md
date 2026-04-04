# Source: https://developers.cash.app/cash-app-afterpay/guides/welcome/getting-started/support.mdx

***

## stoplight-id: kxl7vh3afbet4

# Support

### Where can merchants find answers to common questions?

Visit our [merchant help center](https://help.business.afterpay.com/hc/en-us) or contact your Cash App Afterpay account representative.

#### Quick links

* [Payment schedules and transaction fees](https://help.business.afterpay.com/hc/en-us/sections/6464826951705-Payment-Schedule-Transaction-Fees)
* [Refunds](https://help.business.afterpay.com/hc/en-us/sections/6464909479577-Refunds)
* [Order management](https://help.business.afterpay.com/hc/en-us/sections/6464856665113-Order-Management-Transaction-Description)

### How can a customer contact Cash App Afterpay support?

Customer support queries should be directed to [help.afterpay.com](https://help.afterpay.com/hc/en-us).

### Where can I check Cash App Afterpay's systems status?

You can view the current status of Cash App Afterpay at [https://status.afterpay.com](https://status.afterpay.com). Subscribe to receive status updates by email.

### Why is Google Analytics incorrectly attributing the referrer to Afterpay?

When customers pay with Cash App Afterpay, they are redirected to portal.afterpay.com pages during the checkout flow, before returning to your review or confirmation page. This results in Google Analytics seeing portal.afterpay.com as the last domain visited. Therefore, it attributes the referral to `portal.afterpay.com`.

To ensure that Google correctly identifies the real referral source, add `portal.afterpay.com` to your referral exclusion list.

For details on how to add Cash App Afterpay to your exclusion list see [Google's documentation.](https://support.google.com/analytics/answer/10327750?hl=en)

<Warning>
  Use <code>portal.afterpay.com</code> <strong>not</strong> <code>afterpay.com</code> or you'll hide all of the traffic originating from the Cash App Afterpay Shop Directory.
</Warning>
