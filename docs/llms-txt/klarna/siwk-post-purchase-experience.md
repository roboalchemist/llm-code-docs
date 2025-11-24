# Source: https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/use-cases/siwk-post-purchase-experience.md

# Post-purchase experience

## How to create a user account after purchase.

## Introduction

After a purchase is complete, many customers find it valuable to have a way to track their order and access their purchase history. For those who have checked out as guests, the order confirmation page provides a seamless opportunity to invite them to create an account using Sign in with Klarna. By implementing the SIWK button on the success page, you can offer customers a quick and secure way to set up an account after their purchase, enhancing their post-purchase experience and opening up new engagement opportunities. Creating an account provides customers with access to past and future purchases, personalized order updates, and exclusive promotions. For your business, it enables deeper customer relationships, higher retention rates, and more effective communication. Adding SIWK at this critical touchpoint can make a significant impact on customer loyalty and engagement. ![ Example of the post-purchase flow](ZzXIYa8jQArT03Oq_CreateAccountonMerchantPostPurchase.jpeg " Example of the post-purchase flow")

#### Why enable account creation post-purchase?

Enabling account creation on the order confirmation screen allows customers to:

- **Track orders easily** – Once logged in, customers can monitor their purchases, delivery status, and history from a single account.
- **Enjoy a personalized experience** – Customers can receive targeted promotions and order updates.
- **Save time** – Returning customers won’t need to re-enter information in future transactions.

For your business, this is a unique opportunity to convert guest customers into account holders, increasing the chance of future interactions and building a stronger, loyal customer base.

#### Integration guidelines

To integrate the **Sign in with Klarna** button on the order confirmation screen, follow these steps:

1.  **Set up the SDK**: Start by following the general integration setup as outlined in the [Sign in with Klarna Web SDK documentation](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/web-sdk-integration/). This will guide you through installing and initializing the Web SDK on your site.
2.  **Configure the success page**: Identify the order confirmation (or “thank you”) page on your website where customers land after completing a purchase. Embed the SIWK button in a visible, user-friendly location on this page, inviting customers to create an account. A sample prompt could be, "Create an account to view your order history and enjoy a more personalized experience.".
3.  **Handle authentication**: Use Klarna’s SDK to authenticate users via the SIWK button. Once authenticated, check for an existing user account. If none exists, prompt them to complete the quick setup to create a new account tied to their recent purchase.
4.  **Customize the user experience**: Provide a confirmation message once the account is created, such as "Your account has been set up! You can now track this and future orders in your account.". Consider redirecting users to their new account profile or order history page to immediately reinforce the benefits of having an account.