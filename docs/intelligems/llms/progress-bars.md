# Source: https://docs.intelligems.io/offer-personalizations/progress-bars.md

# Progress Bars

### Overview

Progress bars visually show customers their progress toward rewards like discounts or free shipping in an Offer Personalization or Offer Test. They motivate customers by showing "how close am I to unlocking this discount?" and help drive larger cart values.

{% hint style="warning" %}
**Important:** To add these components to your site, please follow [these installation instructions](https://docs.intelligems.io/offer-personalizations/offers-integrating-widgets)
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9f4901ee56d4567b553acb11efb6ef40a75a6247%2FQuantity%20button%20config.png?alt=media" alt=""><figcaption></figcaption></figure>

### Key Features

* **Visual Progress Tracking**: Real-time updates as cart contents change
* **Multiple Tier Support**: Show progress across several reward levels
* **Dynamic Updates**: Automatic updates without page refresh
* **Enhanced Styling**: Customize colors, thickness, corner radius, and spacing

### Requirements

Progress bars require a minimum purchase requirement (dollar amount or quantity) to function. This must be manually set for Amount off products, Amount off order, and Free gift offers. Without a defined threshold, there's no target to measure progress against.

On Volume discount and Free shipping Offers, Progress bars are automatically available to use.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-588fb252e20f2079078e8d72ef614363cd97d6d3%2FAmount%20off%20products%20-%20Offer%20settings%20-%20expanded.png?alt=media" alt=""><figcaption></figcaption></figure>

### Configuration

#### Basic Setup

* **Item Quantity**: Set quantity-based thresholds (e.g., "Buy 3 items for 15% off")
* **Dollar Amount**: Set spending-based thresholds (e.g., "Spend $75 for free shipping")
* **Multiple Tiers**: Configure escalating rewards at different levels

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-87975ca2e775c5c90c929cc8b3172edf051d25c4%2FOffer%20setup%20-%20expanded%20view.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Styling Controls

* **Bar Appearance**: Colors, thickness and corner radius
* **Text**: Dynamic progress messaging, completion text, breakpoint labels
* **Typography**: Font size & font style

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-57e04f350312a4326c0e2c95f1f33dafd7748798%2FQuantity%20button%20config1.png?alt=media" alt=""><figcaption></figcaption></figure>

### Dynamic Variables

#### Progress Variables

* `{Amount remaining}`: Show remaining amount needed
* `{Discount amount}`: Display discount value

**Example Usage:** "Spend {Amount remaining} more to unlock {Discount amount} off!"

### Example Use Cases

**Free Shipping Threshold**\
"Spend $15 more to get free shipping!" → "You've unlocked free shipping!"

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-133d468e1deda111045606ca2ef70435b19f70ef%2FAccordion1.png?alt=media" alt=""><figcaption></figcaption></figure>

\
**Volume Discount**\
"Buy 2 more items to unlock 15% off!" with locks on milestones

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-83db7e2878310d02664284a666d4e81af0edf7ec%2FAccordion3.png?alt=media" alt=""><figcaption></figcaption></figure>

\
**Gift with purchase**\
"Spend $20 more to get a free tote bag!" with gift icon breakpoint

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-0006edcf92b3b76d20bac874b05040dbfc42b735%2FAccordion4.png?alt=media" alt=""><figcaption></figcaption></figure>

### How It Works

**Amount off products, Amount off order, and Free gift Offers:**

1. Configure discount value
2. Set minimum purchase requirement ($ amount or quantity)
3. Add which products this Offer should apply to (or leave empty to apply to all products)
4. Add Progress Bar component to your offer
5. Set progress and completion messaging
6. Configure styling to match your brand
7. Preview with different cart values

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-dea32fc4db284ed22cbc5e0236839be03cc08854%2FAmount%20off%20order%20-%20Offer%20settings.png?alt=media" alt=""><figcaption></figcaption></figure>

\
**Volume discount Offers:**

1. Configure discount trigger and discount value
2. Add which products this Offer should apply to (or leave empty to apply to all products)
3. Configure Offer tiers
4. Set progress and completion messaging
5. Configure styling to match your brand
6. Preview with different cart values

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f6efff65bfdd9438aada0007f787d27de35dfa66%2FOffer%20setup%20-%20expanded%20view1.png?alt=media" alt=""><figcaption></figcaption></figure>

\
**Free shipping Offers:**

1. Choose to set minimum purchase requirement ($ amount or quantity) or not
2. Add which products this Offer should apply to (or leave empty to apply to all products)
3. Configure free shipping options
4. Add progress bar component to your Offer
5. Set progress and completion messaging
6. Configure styling to match your brand
7. Preview with different cart values

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-ded8f6b5c84f85a6106c19554757019866091d3d%2FOffer%20setup%20-%20expanded%20view2.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
**Tips**

* **Set Achievable Goals**: Start with 1.5-2x your average order value
* **Use Brand Colors**: Integrate with your site's color scheme
* **Be Specific**: Use exact amounts ("$15 more") not vague language
* **Test Mobile**: Ensure proper display on all devices
  {% endhint %}

### Troubleshooting

**Progress Bar Not Displaying**: Verify minimum purchase requirement is set (for Amount off products/order/Free gift offers) and offer is active

**Styling Issues**: Use offer preview to see actual site styling; component preview shows general appearance only

Last updated: 7/29/25
