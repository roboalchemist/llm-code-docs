# Source: https://docs.intelligems.io/offer-experiences/quantity-buttons.md

# Quantity Buttons

### Overview

Quantity Buttons replace standard quantity selectors within an Offer Experience with promotional buttons that highlight savings and encourage larger purchases. They showcase volume discounts and tiered pricing to drive higher average order values.

{% hint style="warning" %}
**Important:**

* Quantity Buttons are automatically installed via the Intelligems script
* You must select specific products for Quantity Buttons to be available as a component option when setting up an Offer
* To set up a Price Test with Quantity Buttons [follow these steps](https://github.com/intelligems-io/docs/blob/main/public-docs/offer-experiences/broken-reference/README.md).
  {% endhint %}

{% hint style="info" %}
**Note**: Quantity Buttons are only available on Volume discount Offers.
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-21edf96134456a2cc03b1c219bee7850a3385430%2FQuantity%20button%20config5.png?alt=media" alt=""><figcaption></figcaption></figure>

### Key Features

* **Multiple Button Styles**: Choose from Classic List, Image Cards, or Compact layouts
* **Dynamic Pricing Display**: Real-time pricing, savings calculations, and discount percentages
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

**Volume discount Offers:**

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

### Troubleshooting

**Buttons Not Appearing**: Verify Offer is active, products selected, and requirements met

**Pricing Issues**: Check discount calculations and product pricing in offer settings

**Variable Display**: Verify variable syntax and test with different product selections

**Previous Variant & Quantity buttons displaying:** Hide these elements with a Content Edit

Still having trouble? Email <support@intelligems.io>

Last updated: 7/29/25
