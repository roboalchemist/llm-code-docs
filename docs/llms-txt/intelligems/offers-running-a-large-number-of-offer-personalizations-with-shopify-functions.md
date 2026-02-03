# Source: https://docs.intelligems.io/offer-personalizations/offers-running-a-large-number-of-offer-personalizations-with-shopify-functions.md

# Running a Large Number of Offer Personalizations with Shopify Functions

## Multiple Functions

A Shopify function only can contain so much information. Once you exceed \~20 Offer Personalizations(active or inactive) we may need to use multiple Shopify Functions to accurately store all of your Offer Personalization data.

This means that you'll have several functions operating independently. Each function will return its own result, and will apply stacking logic *only* to the campaigns stored within that function.

When configuring an Offer's stacking settings, you'll see the names of the other Offers it can stack with.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-fa434e6f1a2263b8eb6cc7f54afa74c8634e9534%2FScreenshot%202024-03-13%20at%2010.39.00%20AM.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

When the functions run on your store, Shopify will choose the single result with the maximum benefit, and apply that discount to the order.

### **For example:**

1. Function A holds Offer Personalization 1 (10% discount) and Offer Personalization 2 (15% discount). Both are set to stack
2. Function B holds Offer Personalization 3 (30% discount) also set to stack

If a user is eligible for *all* the above Offer Personalizations, Function A will return a stacked discount (10% + 15%) and Function B will return a single discount (30%)

Because the result from Function B has a greater benefit (30% > 10% + 15%) only the result from Function B will apply to the order.

## How many functions can I use?

If you are using `checkout.liquid` you can only have 1 active discount function with an 'automatic' application method (this is the type of function our campaigns use). Otherwise, Shopify allows for a maximum of 5.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-bf17c0fb7bc918d2335b49f6cc413c849054b9a1%2FScreenshot%202024-03-13%20at%2010.53.44%20AM.png?alt=media" alt="" width="205"><figcaption></figcaption></figure>

However, this number isn't scoped to just the Intelligems app - every automatic discount, whether it's created by another app or Shopify, counts against this total.

If there are any campaign(s) that we couldn't find function space for, we'll highlight them in red. These Offer Personalizations will not run on your store. To make room so they will run, you can remove any non-Intelligems automatic discounts, or remove other Intelligems Offer Personalizations.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-3b700ccf8991e86e5eed172eca091a05c8ce8c87%2FScreenshot%202024-07-22%20at%2010.18.38%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
