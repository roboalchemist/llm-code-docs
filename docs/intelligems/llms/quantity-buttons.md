# Source: https://docs.intelligems.io/offer-personalizations/quantity-buttons.md

# Quantity Buttons

### Overview

Quantity Buttons replace standard quantity selectors within an Offer Personalization with promotional buttons that highlight savings and encourage larger purchases. They showcase volume discounts and tiered pricing to drive higher average order values.

{% hint style="warning" %}
**Important:**

* Quantity Buttons are automatically installed via the Intelligems script. If you are not seeing them when you preview your Offer on an eligible product, please see [the below](#installing-the-quantity-buttons) for help.&#x20;
* You must select specific products for Quantity Buttons to be available as a component option when setting up an Offer
* To set up a Price Test with Quantity Buttons [follow these steps](https://docs.intelligems.io/offer-experiences/how-to-set-up-a-price-test-with-quantity-buttons).
  {% endhint %}

{% hint style="info" %}
**Note**: Quantity Buttons are only available on Quantity Discounts.
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-21edf96134456a2cc03b1c219bee7850a3385430%2FQuantity%20button%20config5.png?alt=media" alt=""><figcaption></figcaption></figure>

### Key Features

* **Multiple Button Styles**: Choose from Classic List, Image Cards, or Compact layouts
* **Dynamic Pricing Display**: Real-time pricing, savings calculations, price per item, and discount percentages
* **Choose Default Variant:** Choose which variant is selected as default - instead of the lowest or single unit, you can select a higher tier to increase AOV
* **Show Prices per Item:** Update the price shown on PDP as a price per item for multiple units
* **Enhanced Text Customization**: Add badges, labels, subtitles, and custom messaging
* **Free Shipping & Gift Integration**: Display badges and callouts directly on buttons

### Button Styles

**Classic List**\
Clean, vertical layout with organized quantity tiers. Best for traditional presentations with detailed pricing.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-1dac7546f816f31ee90cbf20a9e0eabb8d39de41%2FScreenshot%202025-10-13%20at%203.22.14%E2%80%AFPM.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

**Image Cards**\
Includes product images for each option. Ideal for bundles, gift sets, and visual product storytelling.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-d57ccbe2fade75f543c214b38198f7a3b09e05fb%2FAccordionA.png?alt=media" alt=""><figcaption></figcaption></figure>

**Compact**\
Space-saving horizontal layout for quick comparison. Perfect for limited space and mobile experiences.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-61de82a3ebcba25266132a15dd5f02dd202c18ef%2FAccordionC.png?alt=media" alt=""><figcaption></figcaption></figure>

### Configuration

#### Basic Setup

* **Section Title**: Header text (e.g., "Buy more save more")
* **Base Button**: Toggle single-item option
* **Button Labels**: Custom text for each tier
* **Subtitles**: Additional descriptive text

#### Additional Features

* **Free Shipping Badges**: Auto-display on qualifying tiers
* **Free Gift Display**: Include free gift information on qualifying tiers
* **Promotional Badges**: "Most Popular," "Best Deal," "Limited Time"
* **Compare at Price**: Original vs. discounted pricing
* **Variant Mix:** Let customers mix & match variants per tier

#### Layout Options

* **Stacked (Default)**: Vertical list format, natural reading pattern
* **Side-by-Side**: Horizontal grid, efficient space use

### Dynamic Variables

#### Discount Variables

* `{Saved percentage}`: Display discount percentage
* `{Saved $ total}`: Total dollar savings
* `{Saved $ per item}`: Per-unit savings amount

#### Product Variables

* `{Product title}`: Specific product names
* `{New total price}`: Discounted total price
* `{New price per item}`: Discounted per-unit price
* `{Original total price}`: Original total pricing
* `{Original price per item}`: Original per-unit cost

**Example Usage:** "Save {Saved percentage} on {Product title}"

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-8124e78e321d8dbd24e2ddf035fa3083286eb333%2FQuantity%20button%20configvariables.png?alt=media" alt=""><figcaption></figcaption></figure>

### Example Use Cases

**Volume Discounts**

* 1 item: Standard price
* 2 items: 10% off, "Most Popular"
* 5 items: 20% off, "Best Deal"
* 10 items: 40% off + free gift

**Bundle Offers** Single item → 3-Pack → 5-Pack → Family Pack with escalating value

### How It Works

**Quantity Discount Offers:**

1. Configure discount trigger and discount value
2. Add specific products this Offer should apply to (cannot be left empty for all products)
3. Configure Offer tiers
4. Add Quantity Buttons component to your offer
5. Customize labels with variables
6. Choose button style and layout
7. Choose variant mix defaults and display type inclucing text, color swatch, or product image
8. Style to match brand preferences
9. Preview with product switching

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-5ddfa27c8d7b9a96b979343acd9448191eb78c0e%2FOffer%20setup%20-%20expanded%20viewVD.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
**Tips**

* **Compelling Tiers**: Clear value progression with meaningful savings increases
* **Visual Hierarchy**: Use badges and colors to guide toward preferred options
* **Mobile-First**: Ensure touch-friendly sizes and spacing
* **A/B Testing**: Test layouts, messaging, and promotional strategies
  {% endhint %}

### Installing the Quantity Buttons&#x20;

Quantity Buttons are automatically installed on your product pages once the [Intelligems script](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) is added to your theme. Our script detects the standard quantity selector on your product detail pages and installs the buttons there.

**When will I see the buttons?** The buttons will appear on your product pages once you've either:

* Started previewing an Offer with Quantity Buttons enabled, or
* Launched a live Offer with Quantity Buttons enabled

**What if the buttons aren't showing up?** If you don't see the buttons, your theme may use a custom quantity selector that differs from the standard format. To resolve this, add the following snippet to your product page (PDP) liquid code:

```liquid
<ig-volume-quantity-widget></ig-volume-quantity-widget>
```

**What if the buttons are showing up, but not in the correct location?** If you see the buttons but they are not in the location you would like them to be on your PDP, your theme may use a custom quantity selector that differs from the standard format. To resolve this, add the following snippet to your product page (PDP) liquid code in the location you would like the buttons to be:

```liquid
<ig-volume-quantity-widget></ig-volume-quantity-widget>
```

This will ensure the buttons display correctly on your site. Please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you would like help completing this!&#x20;
