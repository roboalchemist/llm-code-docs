# Source: https://docs.intelligems.io/offer-experiences/offers-integrating-widgets.md

# Integrating Components with Offers

### Overview

Intelligems offers quantity buttons for product pages so customers can quickly add multiple units to cart and achieve various discount tiers.

Intelligems offers a progress bar for Shopify carts and slide-out carts that will show your customers how much more they need to purchase to achieve specific discounts, prompting them to buy more to get the best deal without ever leaving their cart. See below for an example of what this looks like!

{% hint style="danger" %}
You'll need the Intelligems JavaScript snippet installed in your theme to use Intelligems offer components. If you haven't already added it, see our integration guide[ here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme). Quantity buttons and progress bars require an additional short code snippet, which you can find below.
{% endhint %}

## Offer Message

No installation required. This component is automatically available to be added to an Offer once Intelligems is installed in your theme.

## Shipping Progress Bar

### Step 1: Add the shipping progress bar to your Shopify theme

Paste the following code snippet into your Shopify theme code, in the theme file that renders your cart in order to add a Shipping Progress Bar to a Test or Experience. This file may be called something like `cart.liquid`, `slideout-cart.liquid`, etc. We recommend adding this code snippet at the top of the section that relates to your cart:

```html
<ig-shipping-progress-container></ig-shipping-progress-container>
```

{% hint style="danger" %}
If you already have a shipping progress bar, remember to comment out the existing shipping progress bar to avoid showing two!
{% endhint %}

### Step 2: Customization / Styling

You can customize the Intelligems Shipping Progress Bar in the [Global Styles](https://docs.intelligems.io/general-features/global-styles) tab. Some examples of stylizing options available include:

* Bar Styles
* Bar Colors
* Text Options

### Integrating with Rebuy Carts

1. Create a Rebuy custom smart cart template. Follow [this](https://help.rebuyengine.com/en/articles/6120362-how-to-use-a-custom-template-with-smart-cart) article for instructions.
2. Edit the template to replace the Rebuy progress bar with the Intelligems progress bar snippet. See Step 1 above.

## Quantity Buttons

No installation required. This component is automatically available to be added to an Offer once Intelligems is installed in your theme.

You can customize the Intelligems Offer quantity buttons in the [**Global Styles**](https://docs.intelligems.io/general-features/global-styles) located in the left menu. Stylizing options include:

* Button styles
* Button primary, secondary and border colors
* Customizable for both desktop and mobile

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-17694df854247cb6ed85e3b56f06f81c0e1e7564%2FGlobal%20Styles.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Note that quantity buttons will only reflect your store's default currency, so if you are choosing to use quantity buttons for your Offer Experience or Offer Test, you should also set up targeting for your store's default currency.
{% endhint %}

**If you want to use components with multiple currencies, follow the steps below:**

1. Add the script below to the `<head>` section of your **theme.liquid** file

```
<script type="text/javascript">
    window.igCurrencyFn = (cents, el) => {
      // Use Shopify's active currency (set by currency switcher)
      const currencyCode = window.Shopify?.currency?.active || 'USD';
      const formatter = new Intl.NumberFormat('en', {
        style: 'currency',
        currency: currencyCode,
        currencyDisplay: 'symbol'
      });
      
      return formatter.format(cents / 100);
    };
    </script>

```

2. Inside Intelligems, go to Settings and scroll down to **Currency Function**

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-fa858a14b1c28bb7c35e014c61a8e8cda86d6efe%2FScreenshot%202025-11-04%20at%202.06.59%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

3. Add `window.igCurrencyFn` into the **Currency Function** field and click **Save Configurations**\\

{% hint style="danger" %}
The quantity buttons are a layer over top of your store's quantity buttons and only available when added to a a Offer Experience or Offer Test. To change the default quantity selected in an offer, you'll need to change the default quantity within Shopify.
{% endhint %}

## Offer Progress Bar

### Step 1: Add the progress bar to your Shopify theme

Paste the following code snippet into your Shopify theme code, in the theme file that renders your cart in order to add an Offer Progress Bar to an Offer Experience or Offer Test. This file may be called something like `cart.liquid`, `slideout-cart.liquid`, `cart-template.liquid`, etc. We recommend adding this near to the top of the cart in most instances.

```markup
<ig-volume-progress-bar-widget></ig-volume-progress-bar-widget>
```

{% hint style="danger" %}
If you already have an offer progress bar, remember to comment out the existing offer progress bar to avoid showing two!
{% endhint %}

### Step 2: Customize the Offer Progress Bar to match your site's styling & language

There are a few different customizations you can make to the progress bar. See more on each of the options below.

#### **Style and Colors**

You can customize the Intelligems Offer progress bar in the Global Styles components located in the left menu, or by selecting 'Edit Bar Style' while setting up a new offer modification and toggling the progress bar on. Stylizing options available include:

* Bar styles
* Bar color for active and inactive
* Bar background color
* Breakpoint color for active and inactive
* Container background color
* Tooltip background color
* Customizable for both desktop and mobile

#### **Variables**

In addition to customizing the look and feel of your progress bar, you can also customize what messaging appears along with it. The first step in doing this is customizing the variables you will use. The variables are the words that can be put anywhere within your messages and will be filled in dynamically with the correct value when rendered within the template string. All variables have default values that we will fall back on if you leave that option blank.

There are four variables:

1. **Unit Name (#unitName):** The name of your items.
   1. The default value for this is 'items'.
   2. Ex. 'Buy 2 more **packs** to get 10% off' or 'Buy 2 more **bars** to get 10% off'.
2. **More (#more):** The word in place of 'more'.
   1. The default value for this is 'more'.
   2. Ex. 'Buy 2 **extra** items to get 10% off' or 'Buy 2 **additional** items to get 10% off'.
3. **Quantity (#quantity):** This is the amount needed to qualify for the next discount tier. This is *not* customizable by users and is calculated by Intelligems according to whether the campaign is set up as an item or subtotal requirement.
   1. Ex. 'Buy **2** more items to get 10% off' or 'Spend **$10** more to get 10% off'.
4. **Discount (#discount):** This is the discount amount for a customer when they get to the next discount tier. This is *not* customizable by users and is calculated by Intelligems according to whether the campaign is set up as a currency or percentage discount.
   1. Ex. 'Buy 2 more items to get **$10** off' or 'Buy 2 more items to get **10%** off'.

#### **Messages**

Once your variables are set up, you can set up your messages, which are sentences that appear above your progress bar. You can construct a message by stringing together words and variables. Variables can be accessed by typing '#' and then selecting from the preexisting list of variables. Variables can be placed wherever you want and can be used however many times. All messages have default values that we will fall back on if you leave that option blank.

There are three messages:

1. **Buy More:** The sentence that will be rendered when there are discount tiers to unlock. It will render the next tier that the customer is eligible for.
   1. The default value for this is 'Buy #quantity #more #unitName to get #discount off'.
   2. Ex. 'Buy 2 additional packs to get 10% off' or 'Spend $10 more to get $5 off'.
2. **All Tiers Unlocked:** The sentence that will render in place of the 'Buy More' message when a user has unlocked all tiers. This will also render below the progress bar along with the 'Buy More' message for each individual tier accomplishment.
   1. The default value for this is:
      1. If all tiers have been unlocked, the default value is 'Congratulations, you’ve unlocked #discount off'. This will render above the progress bar.
      2. If at least one tier has been unlocked, but not all tiers have been unlocked, the default value is 'You now have #discount off'. This will render below the progress bar, while the 'Buy More' message renders above the progress bar.
   2. Ex. 'Congrats! You've got 20% off!' or 'You have unlocked 5% off!'.
3. **Tooltip:** The sentences that will show on hover of each tier breakpoint in the progress bar.
   1. The default value for this is:
      1. If the minimum purchase requirement or tier type is 'Subtotal of items', the default value is 'Spend #quantity to get #discount off'.
      2. If minimum purchase requirement or tier type is 'Quantity of items', the default value is 'Buy #quantity to get #discount off'.
   2. Ex. 'Buy 3 to get $10 off' or 'Spend $50 to get 10% off'.

#### Integrating with Rebuy Carts

If you use Rebuy for your slide out cart, you'll need to follow these steps to add the Offer progress bar.

1. Create a Rebuy custom smart cart template. Follow [this](https://help.rebuyengine.com/en/articles/6120362-how-to-use-a-custom-template-with-smart-cart) article for instructions.
2. Edit the template to replace the Rebuy progress bar with the Intelligems Offer progress bar. See Step 1 above.
3. Add the subtotal class to the progress bar settings in the Intelligems app. See Step 2 above.
