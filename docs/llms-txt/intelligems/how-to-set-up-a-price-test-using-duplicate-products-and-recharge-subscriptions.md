# Source: https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/how-to-set-up-a-price-test-using-duplicate-products-and-recharge-subscriptions.md

# How to Set Up a Price Test using Duplicate Products and Recharge Subscriptions

{% hint style="danger" %}
Testing subscriptions often requires a more involved integration and setup than typical price tests. As a result, we recommend having Intelligems perform the integration if this is something you would like to test. Reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for help!
{% endhint %}

{% hint style="info" %}
**Prerequisites:** Prior to setting up your test, please reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to confirm your account is set up with duplicate products and redirection, both of which are required for you to price test. Duplicate products are only required in the case that you do not have access to the Script Editor app, or use Recharge 1.0.
{% endhint %}

## Step 1: Set up test in the Intelligems app

Once you have confirmed the above with support, you can set up your test in the Intelligems app as you normally would! See our detailed guide [here](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test).

## Step 2: Configure your duplicate products in Shopify

If you have not already, follow [these steps](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/managing-duplicate-products-when-redirecting-to-duplicate-pdps) to configure your duplicate products in Shopify.

## Step 3: Add your duplicate products to your subscriptions in Recharge

In Recharge, follow these steps:

1. Go to `Products` on the left hand side.
2. Click `Add Product` in the top right.
3. Select all of your duplicate products and click `Add Products`.
4. Once you have added them, they will show up in the list with all of your other subscription products, but they will have no `Collections` or `Subscription type`.
5. You can now either click into each duplicate product and update the subscription settings individually, or select all of the duplicate products using the checkboxes on the left and click `Update subscription settings` at the top.
6. Confirm that you have set up the subscription type, order schedule and discount for each new duplicate product.

## Step 4: Confirm subscription duplicate products are set up correctly

Once you complete step 3, Recharge will automatically create another duplicate product for each test product in Shopify. The Recharge duplicates will have the subscription discount in the product title, making them easy to find.

These products should be set up correctly, but we recommend confirming the prices match what you expect and that the products are set to active. The prices on the subscription duplicate products should be equal to the price after the subscription discount.

We also recommend adding a tag, such as 'Price\_Test\_Subscription\_Duplicate', to make these products easy to find in the future.

## Step 5: Consider any Recharge apps that may be impacted

Many brands use Recharge apps, such as Workflows, to accomplish various things. If you use any apps, make sure these are set up to work with your new duplicate subscription products. A few things to keep in mind here are any apps that rely on product IDs or names as these may not match!

## Step 6: QA your test

Because tests that involve subscriptions have more moving pieces, we recommend spending some extra time on QA - follow [this checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist) to make sure you don't miss anything!
