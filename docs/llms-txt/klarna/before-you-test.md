# Source: https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test.md

# Before you test

## Learn about the Klarna credentials required and data you need to have handy to test our solutions.

## What you can test

In the test (playground) environment, you can test the integration of the following products in your online store:

- [Klarna Payments](https://docs.klarna.com/payments/web-payments/before-you-start/what-is-klarna-payments/) lets you offer Klarna as a payment method to your customers.

### What to keep in mind

Before you start testing the Klarna products, consider the following:

- Our live (production) systems don't process the purchases completed in the playground environment. These test purchases won't result in invoices or fees.
- Don’t use real personal data during testing. Depending on which country your store operates in, we offer [Sample customer data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/) and [Sample payment data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-payment-data/) that you can use.
- In the playground environment, you can test all Klarna products. The products you see in production may differ from the ones available in the playground environment, depending on your contract.

### Klarna products in your store

See what Klarna products look like when added to your store’s checkout or payment process.

When testing your store's integration with Klarna, you can:

- Test the payment process if you offer Klarna payment methods in your checkout. See the product documentation and the [Payments API reference](https://docs.klarna.com/api/payments/) reference to learn more.
- Manage test orders in the playground [Merchant portal](https://portal.playground.klarna.com).

Additionally, On-site messaging and Express Checkout each have a testing solution that lets you apply Klarna's branded elements to your playground store. See the product documentation for On-site messaging and Express Checkout to learn more about how to test them before going live.

We recommend that you perform some end-to-end tests before you launch. Take a look [at the step-by-step test cases](https://docs.klarna.com/resources/developer-tools/testing-payments/test-cases/).

If you integrate using third-party platforms, see the [platform integrations documentation](https://docs.klarna.com).

## Klarna Demo store

To experience what buying with Klarna is like for your customers, go to our [Demo store](https://www.klarna.com/demo/). The demo store is an example website that shows what the shopping journey can look like to the customers and how Klarna payments, On-site messaging, and Express Checkout work.

The data in the Demo store is not linked to your MID. The orders you create using Klarna APIs or in the playground Merchant portal are not visible in the Demo store.

To start testing Klarna products, you need:

- Access to the test [Merchant portal](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/merchant-portal-user-guide/)
- Test [API keys](https://docs.klarna.com) for Klarna Payments
- [Client identifiers](https://docs.klarna.com) to configure and test On-site messaging and Express checkout solutions
- [Sample customer data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/) and [sample payment data](https://docs.klarna.com)

## Accessing the test Merchant portal

To access the test Merchant portal, you can sign up to create a new test account or log in with a test existing account. 

### Creating a new test account

To create a new test account, follow these steps:

1.  Click the **Log in**button in the navigation bar of Klarna Docs.
2.  Select the region of your credentials (for example, 🇪🇺 Europe).
3.  Select **Playground** as the environment.
4.  Click **Sign up**.
5.  Type your email address and click **SIGN-UP**.You'll get a confirmation email at this address.
6.  Open the confirmation email and click **Activate account**.
7.  Finish setting up your account:
    - Accept the Terms & Conditions
    - Choose a new password.
    - Enter your name.
    - Log in to the Merchant portal.

### Using an existing test account

To log in with an existing test account, follow these steps:

1.  Go to the [Merchant portal login page](https://portal.klarna.com).
2.  Type your email address and password, then click **Log In**.

If you don’t have these credentials, see the [Create a new test account section](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test/#accessing-the-test-merchant-portal-creating-a-new-test-account). If you forgot your password, use the reset function.

## Getting test credentials for APIs

To test your Klarna API integration, you need a set of test credentials. Follow these steps to get the credentials:

1.  Access the [test Merchant portal.](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test/#accessing-the-test-merchant-portal)
2.  Click [Payment settings](https://docs.klarna.com) in the left sidebar.
3.  Select **Klarna API Keys**
4.  Click the **Generate new Klarna API key**button.
5.  Download the .txt file and close the dialog box. 

You now have a `Key ID` (API Username) and a `Secret` (API password) to authenticate when testing the APIs. Note that the test keys will only work for requests you send to the playground [API URLs](https://docs.klarna.com/api/api-urls/#api-urls).

The password is only displayed once. You will not be able to retrieve it after you close the dialog box.

## Sample data

In the playground environment, you must never use any real-life data to test the integration. When you're asked to enter data when testing, please use the [Sample customer data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/) we've prepared.

To test the payment methods, use the [Sample payment data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-payment-data/).

## Troubleshooting

While we hope that your testing experience goes well, there might be times when you get a strange or unexpected response to an API call.

You can troubleshoot with the help of [Logs in the Merchant portal](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/payments/#developers-logs) in the Merchant portal.

Logs contain the details about your playground store’s operations from the previous 7 days. You can filter the entries based on date and time, service, order ID, direction, and more. Each entry is accompanied by details that help you get to the bottom of each issue.

## Support

If you need help understanding the logs or have any questions about the testing process, contact [Merchant support](https://www.klarna.com/merchant-support/).