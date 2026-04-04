# Source: https://docs.klarna.com/payments/web-payments/before-you-start/what-is-klarna-payments.md

# What is Klarna payments?

## Read this article for an introduction to Klarna payments, its place in the Klarna product family, and payment scenarios it supports.

Klarna payments is an omnichannel solution that lets you add Klarna as a payment method to checkout. You can offer Klarna payments to your customers by:

- accepting web and in-app payments through a direct API integration
- connecting your existing e-commerce platforms like Shopify, Adobe Commerce, SalesForce Commerce, and more through plug-ins
- accepting in-person payments with our in-store solutions.

This guide covers direct Klarna payments integration that you can complete with Klarna payments API. To offer Klarna payments in your store through a third-party platform, see our [Platform solutions](https://docs.klarna.com/platform-solutions/) section.

## Klarna as a payment method

When you integrate with Klarna payments, your customers see Klarna as a payment method in your checkout. Once your customers select Klarna for their purchase, they are redirected to log into their Klarna account. We handle the Klarna account user flow and it's here where your customers select their preferred Klarna payment option (pay now, pay later, pay in parts).

## Payment scenarios

Klarna payments supports payments in most checkout processes, including online stores, mobile applications, and brick-and-mortar stores. The two main payment scenarios for Klarna payments are one-time payments and recurring payments.

### One-time payments

A one-time payment happens at the time of a purchase when a customer uses Klarna to pay for items in the shopping cart, virtually or in-store. 

### Recurring payments

With recurring payments, a customer agrees to pay for a product or a service at the time of purchase, at a later date, or both. Depending on the payment cadence, you can use recurring payments for subscriptions and unscheduled charges.

#### Subscriptions

When your customer buys a subscription, they agree to pay for access to a product or a service in regular intervals, for example, monthly, quarterly, or annually. If a subscription renews automatically, Klarna processes the following payments at the beginning of each new billing cycle. Examples of subscriptions include music and video streaming services, newspapers or magazines, and subscription boxes.

#### Unscheduled charges

Unlike subscriptions, unscheduled charges do not occur at any regular frequency but are tied to the customer's usage of a product or service. This type of charge can also be related to another transaction and occur after that first transaction is completed. Examples of unscheduled charges include:

- On-demand charges, such as scooter rentals, city bike rentals, car sharing, food delivery, and cashier-less store solutions
- Incidentals, damages, and add-ons, such as speeding violation tickets or tips

#### Mixed payments

Allow customers to make one-time purchases and add an additional service in the checkout process. Example of this case:

- Mixed basket: Includes a one-time product and a monthly subscription.
- Additional charge: Includes a one-time product with an additional service charged separately.