# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/resources/frequently-asked-questions/pay-kit-sdk.mdx

***

## stoplight-id: cd1245ca36143

# FAQ: Pay Kit SDK

**Q: What is the difference between the QR code flow vs the mobile deep link flow?**

**A:** The QR code flow must be used for any use case where a mobile device would scan a QR code.
The mobile redirect URL must be used when you’re on a mobile device that can have Cash App installed.

***

**Q: How often is the QR code refreshed with Pay Kit SDK?**

**A:** QR codes refresh every 30 seconds and expire every 60 seconds. `refreshes_at` on the `auth_flow_triggers` property is the best place to learn when you must refresh.
Pay Kit SDK utilizes polling and refreshes the QR code once the current time is after `refreshes_at`.

***

**Q: Once a customer request has been approved, does Cash App prefer for the payment to be processed immediately or should the customer be redirected back to the merchant checkout where they can confirm payment?**

**A:** Cash App supports both approaches but prefers the payment to be processed immediately.
