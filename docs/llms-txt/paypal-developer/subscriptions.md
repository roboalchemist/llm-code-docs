# PayPal Subscriptions: Tailored Billing for Every Customer

## Introduction

Create subscriptions to bill customers at regular intervals. You can customize a subscriptions integration to:

- Create plans that charge users a fixed amount at regular intervals or a variable amount based on the number of users subscribed.
- Create plans that charge users based on volume or tier.
- Offer your subscribers free or discounted trials.
- Enable subscribers to upgrade or downgrade their plans.
- Automate payment recovery for failed payments.

## How it Works

![How, subscriptions, work](https://www.paypalobjects.com/ppdevdocs/img/docs/ppcp-b/configure-payments/subscriptions/subscriptions-how-to.png)

1. Create a product to represent your goods or services.
2. Create a plan to represent the payment cycles for your subscription.
3. Use the JavaScript SDK to present the PayPal button, which starts the subscription process.
4. The buyer agrees and subscribes.
5. The button calls the Subscriptions API to create the subscription.
6. The buyer sees the subscription confirmation.

## Choose a Subscriptions Solution

### Subscriptions REST APIs

[Customize Subscriptions to fit into your product UI](/docs/subscriptions/integrate/)

If you have your own product UI, you can customize the Subscriptions APIs and integrate them into your product.

### PayPal Business Account

[Manage Subscriptions on your account dashboard](https://www.paypal.com/merchantapps/appcenter/acceptpayments/subscriptions)

Recommended if you don't need to integrate Subscriptions into your product UI.

## If you accept cookies, we’ll use them to improve and customize your experience and enable our partners to show you personalized PayPal ads when you visit other sites. [Manage cookies and learn more](https://www.paypal.com/myaccount/privacy/cookiePrefs?locale=en_US)