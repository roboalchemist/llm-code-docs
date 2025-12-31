# Source: https://docs.intelligems.io/offer-experiences/offer-combinations.md

# Offer Combinations

In some cases, you may want your Intelligems offers to combine with other discounts your customers use. For example, you may offer a "Buy more, save more" offer where you get 10% off if you buy 3+ items and that should combine with a $10 off welcome discount code in Shopify.

In other cases, you may **not** want this offer to combine with other offers. For example, an exclusive VIP Save 25% offer you want to ensure that it doesn't combine with other codes and discounts.

This document describes how to configure each and what the configurations are.

## Shopify Combinations

You can read all about how [Shopify combines discounts](https://help.shopify.com/en/manual/discounts/combining-discounts/discount-combinations), but it's quite complicated and nuanced. The gist is that you largely control when you want discounts to combine or not and that's controlled in Shopify.

When you create a discount in Shopify, you'll see these options. If you have a discount you don't want to combine with others, don't check these boxes!

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-de0ec98c7fedd9a0a69e140230952c7ddb584940%2Fimage.png?alt=media" alt=""><figcaption><p>Shopify combination options</p></figcaption></figure>

{% hint style="info" %}
When Intelligems creates discounts in Shopify they are created as "Product Discounts"
{% endhint %}

In order for 2 discounts to combine, they must both be set to combine with each other. So for your Intelligems discount to combine with a Shopify discount, both must be set to combine. If either are not, they won't stack and the most favorable for the customer will be chosen by Shopify.

## Intelligems Combinations

### Options

When you create a discount in Intelligems, you can set these combination options as well and we will let Shopify know how to combine the discount.

1. **Combines with Shopify Discounts** – When this is selected, you're essentially setting the above Shopify Combinations to true. *Note: This must be enabled for it to combine with other Intelligems discounts, too*.
2. **Combines with Intelligems Discounts –** When this is selected, this discount may also combine with other Intelligems offers and discounts you've configured.

### Intelligems Combination Logic

When you have the combination logic within Intelligems, we choose the most beneficial discount for the customer.

Imagine an example:

* Discount A: $5 off, combines
* Discount B: 10% off, combines
* Discount C: $25 off, does not combine

Since Discounts A and B combine, we'll sum those together, and then compare that total discount versus all the other non-combining discounts.

* Cart 1: $100 subtotal = $$Max(5 + 10, 25)=25$$
* Cart 2: $300 subtotal = $$Max(5+30, 25)=35$$

{% hint style="warning" %}
Due to a Shopify limitation, product discounts targeting the same cart item will not combine even if they are configured to ([roadmapped](https://shopify.dev/docs/apps/build/checkout) for Q2 2025)
{% endhint %}
