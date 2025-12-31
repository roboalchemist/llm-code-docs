# Source: https://docs.intelligems.io/price-testing/ending-a-price-test.md

# Ending a Price Test

## Step 1: Press the Stop Button

To end a test, navigate to the Tests tab in the menu on the left-hand side of the Intelligems app. Once you're there, locate the test you'd like to end in the Intelligems tests list and click the stop button, which you can find circled in red below.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-2986d71a700dd250521f9b8be6a46d78b11e0fbd%2FScreenshot%202025-09-25%20at%205.19.41%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

## Step 2: Roll Out Prices

Once you click the stop button, a modal will pop up with the key metrics for each test group. Choose which group's prices to implement in Shopify, then click Apply Prices and End Test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-d968ff2240a5917b19be6063e7ba91058d2fa123%2FScreenshot%202025-09-25%20at%205.14.09%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

* If ***checkout scripts or Shopify Functions*** were used to run the test, prices for the products in Shopify will be updated and the Intelligems Checkout Script or Functions will no longer be applied.
* If ***duplicate products*** were used to run the test, prices for the original products in Shopify will be updated, if needed, and traffic will no longer be directed to the duplicate products.

{% hint style="danger" %}
If ***duplicate products*** were used to create the test, when you end the test, you also have the option in the next modal between:

1\. Immediately archiving the duplicate products.

2\. Archiving the duplicate products after 48 hours. If you choose this option, they will still be set to the `Active` status in Shopify for the **following 48 hours**, though we will not send any new traffic to them. We recommend this option so that if a customer has a duplicate product in their cart, they will still have a seamless checkout experience.

3\. Leaving the duplicate products set to 'Active' until you choose to change the status in Shopify directly. You can select this option by clicking outside of the pop-up where you select when you want products archived.
{% endhint %}

## Step 3: Update Marketing As Needed

Did you roll out new prices based on the results of the test? If so, you'll want to do a thorough sweep of anywhere you may include prices – think emails, social media, advertisements, etc. While you may have used our [Onsite Editor](https://docs.intelligems.io/general-features/onsite-editor) to change the text in these locations during the test, you'll want to update it again to match the new prices going forward.

## Step 4: Update Subscriptions As Needed

If ***checkout scripts*** were used to run the test, there is no action needed here! By default, subscriptions will continue to run at the price the customer subscribed, which may not always be equal to the price on your site.

For example, if you ran a test where the subscription price was $10 for one group and $8 for another and I signed up for the subscription in the $8 group, I would continue to pay $8 monthly, even if the $10 price point is rolled out to the entire site post-test.

If ***duplicate products*** were used to run the test and you offered subscriptions on them, you'll need to merge the duplicate products with the original products within your subscription provider to ensure anyone who signed up for a subscription on the duplicate product is not impacted. If you use Recharge, [this article](https://support.rechargepayments.com/hc/en-us/articles/360008829533#h_01GK355HXA27ESB482GZM33HF9) will walk you through the process to do so. If you work with another subscription provider, we recommend reaching out to their support team for information on how to bulk update products.

{% hint style="info" %}
When reaching out to your subscription provider's support team, we recommend saying something along the following, as well as including a spreadsheet similar to the below with a row for each product that has subscriptions and was duplicated for the test:
{% endhint %}

*Hello Support,*

*We’re looking to do a bulk swap of products/variants tied to subscriptions for **Store Name**. I’m attaching a spreadsheet which maps the current product / variant IDs to what they should be updated to in **Subscription Provider's** backend. We’re doing this because the current products are going to be deleted. Please let me know if you have any questions, or if this is something I can do on our end.*

| **Product Title**   | **Current Product ID** | **Desired Product ID** | **Current Variant ID** | **Desired Variant ID** |
| ------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| Duplicate Product A | 7926607872639          | 7066606823681          | 43624551698273         | 41124551612498         |
| Duplicate Product B | 7926606823762          | 7082606823681          | 43624538571743         | 43629768571009         |
