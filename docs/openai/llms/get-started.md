# Source: https://developers.openai.com/commerce/guides/get-started.md

# Agentic Commerce Protocol

## Overview

OpenAI and Stripe built the Agentic Commerce Protocol to be:

- **Powerful** – connect with millions of users of AI products and build direct customer relationships
- **Easy to adopt** – easily connects with your current commerce systems so you can start accepting orders with minimal effort
- **Flexible** – works across payment processors, platforms, purchase types and business types; stewarded by OpenAI and Stripe with calls for more participants
- **Secure** – protects payment information, maintains compliance, and provides merchants the signals they need to accept or decline orders

It also allows merchants to **keep their customer relationship**–merchants own their direct customer relationship throughout the purchase flow:

1. Customers buy from merchants directly
2. Payment flows directly to the merchant
3. Merchants decide whether to accept or decline an order
4. Merchants handle the full post-purchase experience

The Agentic Commerce Protocol is open source and community-designed under Apache 2.0 license. Businesses can implement the specification to transact with any AI agent and payment processor.

You can learn more about the Agentic Commerce Protocol at [agenticcommerce.dev](https://agenticcommerce.dev) and on [GitHub](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol).

The first product experience built on the Agentic Commerce Protocol is Instant Checkout in ChatGPT. To try it out yourself, try buying from US Etsy sellers in ChatGPT.

To build your own Instant Checkout integration, refer to the section below.

## Instant Checkout

The Agentic Commerce Protocol powers Instant Checkout–enabling purchases through ChatGPT.

Instant Checkout lets users buy directly from merchants through ChatGPT, and allows merchants to accept orders from a new channel while keeping their existing order and payment systems.

| For users                                                                                                | For merchants                                                         |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Find and buy anything using ChatGPT as a personal shopping assistant with trusted, fast recommendations. | Reach buyers in the moment, boost conversion, and keep your customer. |

![ChatGPT mobile commerce experience](https://developers.openai.com/images/commerce/commerce-mobile.png)

Instant Checkout works across:

- Platforms: web, iOS and Android
- Payment methods: All major card brands, Apple Pay, Google Pay, Link by Stripe and more coming soon

Merchants who want to enable Instant Checkout should implement the [Agentic Commerce Protocol](https://developers.openai.com/commerce/specs/checkout) and provide OpenAI with a product feed through the [Product Feed Spec](https://developers.openai.com/commerce/specs/feed).

## Apply to build

Building with the Agentic Commerce Protocol is open to all. Instant Checkout in ChatGPT is currently available to approved partners. To make your products available for Instant Checkout through ChatGPT, please do the following:

1. **Apply** to participate in [Instant Checkout](https://chatgpt.com/merchants).
2. **Share your product feed** according to our [Product Feed Spec](https://developers.openai.com/commerce/specs/feed) in order to provide ChatGPT with accurate, up-to-date information about your products.
3. **Build your Agentic Checkout API** according to the [Agentic Checkout Spec](https://developers.openai.com/commerce/specs/checkout). This involves:
   a. Implementing the required REST endpoints
   b. Implementing webhooks to notify OpenAI of order events
   c. Returning rich checkout state on every response
4. **Build your payments integration**. Use a trusted payment service provider (PSP) that is compliant with the [Delegated Payment Spec](https://developers.openai.com/commerce/specs/payment) in order to securely transmit and charge payment credentials. [Stripe’s Shared Payment Token](https://docs.stripe.com/agentic-commerce) is the first Delegated Payment Spec-compatible implementation with more PSPs coming soon. If you’re a PSP or a PCI DSS level 1 merchant with your own vault, [learn how to build a direct integration with OpenAI](https://developers.openai.com/commerce/specs/payment).
5. **Certify with OpenAI and move to production**. To ensure products, payments and orders are all working correctly, work with OpenAI to pass conformance checks and receive production access.

OpenAI plans to onboard new partners on a rolling basis, beginning in the U.S. If you’re an Etsy or Shopify merchant, you do not need to apply or build an integration as you are already eligible.