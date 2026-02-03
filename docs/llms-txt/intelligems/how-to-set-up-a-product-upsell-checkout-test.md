# Source: https://docs.intelligems.io/checkout/checkout-experiences-library/how-to-set-up-a-product-upsell-checkout-test.md

# How to Set Up a Product Upsell Test at Checkout

## No Upsell vs. 3 Products vs. 1 Product

Adding upsells to your checkout page is easy with Intelligems. You have the power to not only show upsells to customers at checkout without needing another app, but you can test and measure the impact of product upsells. In this example, you can test no upsells vs. showing 3 products vs. showing 1 product at checkout.&#x20;

### Who is this for

This test is best for:&#x20;

* Brands with accessories or easy add-on products
* Teams new to checkout upsells and wanting to validate impact
* Growth teams wanting to understand if there's tradeoff between conversion and AOV

### What this Checkout Test does

This setup creates a Product Upsell Checkout test that compares different upsell strategies at checkout.&#x20;

Specifically, this test allows you to compare:&#x20;

* **A control (no upsells)**
* **Showing 3 product upsells**
* **Showing 1 product upsell**

The goal is to understand how the number of upsell products shown at checkout impacts performance. This can lead to more follow up tests like position of the checkout upsell, products included in the checkout upsell, and more.&#x20;

### When to use it

Use this setup when you want to :

* Test whether showing product upsells at checkout drives incremental value
* Compare the impact of one product vs. multiple products
* Introduce checkout upsells in a controlled, test-first way
* Understand how much choice is appropriate at checkout

{% hint style="success" %}
**Pro Tip:** Choose products that are one size, and are obvious add-ons. This should feel like a no-brainer add on, similar to gum in the checkout line at the supermarket. Minimal decision making for the customer.&#x20;
{% endhint %}

### Why it matters

Checkout is the highest-intent moment in the purchase journey, but it’s also highly sensitive to friction. Testing one product versus multiple products helps you find the right balance between increasing average order value and maintaining conversion.

## How to Set Up This Checkout Test in Intelligems <a href="#how-to-set-up-this-offer-in-intelligems" id="how-to-set-up-this-offer-in-intelligems"></a>

{% embed url="<https://www.loom.com/share/b096c70635214b68ab407fad3af94a29>" %}

1. Go to Personalizations > **Checkout**
2. Select **Upsell**
3. Choose the **Product List** template
4. Add a **Block name**
5. Rename the **Location ID** to be descriptive
6. Select your **products**
7. Configure the Block settings including **headline copy, button copy, background, padding, border style, border thickness,** and **corner radius**
8. Click **Next**
9. Click **Complete checkout test setup**
10. Add the block to your Checkout page in Shopify by clicking **Complete Shopify setup**
    1. In the Shopify Admin go to **Settings** > **Checkout**
    2. Under **Configurations,** click **Customize** to open the Checkout editor
    3. In the left panel, click **Apps**
    4. Navigate to **Intelligems,** click (+)
    5. Paste your block **Location ID** into the block settings
    6. Toggle on **Include block in Shop Pay** (recommended)
    7. Drag the block into the position at checkout
    8. Click **Save** in the top right in the Checkout editor
    9. Return to **Intelligems app** and click **Save**
11. At this point, you can make additional test modifications by clicking **+ Add modification**
12. You can update the content, launch a different Theme or Template, and update styles or javascript
13. Add **Targeting** to choose which shoppers you want to see this block. It will be set to all visitors by default.
14. **Save** your test
15. **Preview** your Checkout Test on desktop and mobile
16. When everything looks good, **Schedule Your Test** or **Start** to go live
    1. You can select a Start time and Stop time when Scheduling

{% hint style="info" %}
If you're on the **Core, Plus,** or **Blue** plan, you can test checkout. [Read more here](https://docs.intelligems.io/checkout/testing-checkout-experiences).
{% endhint %}
