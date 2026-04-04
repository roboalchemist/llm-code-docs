# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/certification.mdx

***

## stoplight-id: zgcqta2bar9hw

# Certification

After you complete your internal QA testing, you're ready for Cash App Afterpay certification. Contact your Cash App Afterpay account manager to schedule certification testing.

All of your unique production environments are tested. The test suite includes three areas:

* Integration standards

* Customer experience

* Refunds

Certification ensures a great customer experience, minimizes the potential for fraudulent activity, and checks for common technical and compliance issues.

**Your Cash App Afterpay production credentials are issued upon successful completion of certification.**

## Deployment

When moving your integration to your production environment, make sure that you're using the production API endpoint and JavaScript URL.

| Environment | API Endpoint                                                                                                                                                         | Screenflow (Javascript)                                                                            |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Sandbox     | [https://api.us-sandbox.afterpay.com/v1](https://api.us-sandbox.afterpay.com/v1) OR [https://api.us-sandbox.afterpay.com/v2](https://api.us-sandbox.afterpay.com/v2) | [https://portal.sandbox.afterpay.com/afterpay.js](https://portal.sandbox.afterpay.com/afterpay.js) |
| Production  | [https://api.us.afterpay.com/v1](https://api.us.afterpay.com/v1) OR [https://api.us.afterpay.com/v2](https://api.us.afterpay.com/v2)                                 | [https://portal.afterpay.com/afterpay.js](https://portal.afterpay.com/afterpay.js)                 |

<Info title="Update the User-Agent Header">
  When you move to a production environment, make sure the User-Agent Header is updated with the production Merchant ID.
</Info>
