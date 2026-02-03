# Source: https://docs.intelligems.io/offer-personalizations/how-to-set-up-a-price-test-with-quantity-buttons.md

# How to Set Up a Price Test with Quantity Buttons

### 1. Install Quantity Buttons into Your Theme

Quantity Buttons component replace your standard quantity selector (or another app powering quantity buttons) directly in your theme and are automatically installed via the Intelligems script.

### 2. Attach Quantity Buttons to a Product via an Offer Personalization

To display Quantity Buttons on a product page, you’ll need to set up an **Offer Personalization**. If you are setting up a Price Test with multiple products using Quantity Buttons, make sure to preview each products to validate the settings are correct and applicable to each product in the test.

{% hint style="info" %}
Note: Quantity Buttons only show when the Offer Personalization is in **Preview** or **Live** mode. Two pending Tests or Personalizations cannot be previewed at the same time.
{% endhint %}

#### **Steps**

1. On the left sidebar, go to Personalizations > **Offers**
2. Click the **Volume Discount** scratch card
3. Start building your quantity price break volume discount
4. Select your **Discount trigger**
   1. In most cases for Product volume discounts, you will select **Quantity of items**
5. Choose the **Discount value**
   1. Decide if you want to do a **Percentage off** or **Dollar off per item**
      1. Set this up exactly as your current volume discount on your product is set up
   2. If you don’t run quantity discounts and don’t want to start, select **Percentage off** and enter `0` in each discount field.
6. Click **Select products** and choose a single product
   1. Reminder: If testing multiple products, create a new Offer Experience for each product
7. Review the **Combinations** checkboxes to ensure they align with your goals
8. Create each Offer tier (ignore single unit for now)
9. *Optional:* Create a **Discount name** for each Offer tier
   1. *Example:* Buy 2, Save 10%; Buy 3, Save 15%
   2. Optionally add perks: Free Shipping or Free Gift
      1. *Example:* Buy 2, Save 10%; Buy 3, Save 15% + Free GWP
10. On the right side, under **Add components**, select **Quantity Buttons**
11. Click **Continue to Component**
12. Configure the component styling, messaging, and inputs.
    1. Use dynamic variables `{ }` for discounts so they display properly.
    2. Preview changes live in the right-hand panel.
13. When everything looks good, click **Next**
14. Because this setup is for a **Price Test**, you’re not testing the discounts themselves. Click **Complete Offer Setup**.
    1. If you’d like to test discounts, tiers, or messaging in the future, create an **Offer Test**. [Learn more here](https://docs.intelligems.io/personalizations/testing-offer-personalizations).
15. Review the **Modifications** tab of the Offer Experience
    1. Double check the **Offer settings** and preview the **Quantity Buttons** component
16. Click **Save**
17. Use the **Preview** tab to confirm the Quantity Buttons look correct on both Desktop and Mobile
18. Your Product is now set up with the Quantity Buttons and ready to be launched with the **Price Test**

{% hint style="warning" %}
If you are using Kaching, FBP, or another app to power quantity discounts on your PDP, you will have to turn that product campaign off within the app in order for Intelligems to override.
{% endhint %}

### Launch the Price Test

1. Create your **Price Test**
2. Turn the **Offer Personalizatio**n with Quantity Buttons live by clicking **Activate**
3. **Preview** your **Price Test** to confirm:
   1. Each test group displays the correct Quantity Buttons
   2. Each variant shows the correct price
   3. Any discount showing matches what you configured
4. If everything looks good, click **Start** to launch your Price Test!

### Pre-Launch Checklist

* [ ] Offer Personalization is Live
* [ ] Quantity Buttons preview correctly on Desktop and Mobile
* [ ] Conflicting third-party apps are disabled
* [ ] Price Test groups show the correct setup

### FAQs

<details>

<summary><strong>Can I run a Price Test with my existing quantity discount app instead of Quantity Buttons</strong>?</summary>

No. For accurate testing, Intelligems requires its own Quantity Button components. Third-party apps can interfere with results.

</details>

<details>

<summary><strong>Will Quantity Buttons work with my theme or page builder?</strong></summary>

Quantity Buttons work on most Shopify themes. If you use a page builder (Replo, Shogun, GemPages, etc.), they will work as long as the product form remains intact. If your builder strips out the product form, you may need developer help.

</details>
