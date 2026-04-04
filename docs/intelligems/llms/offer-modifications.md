# Source: https://docs.intelligems.io/offer-personalizations/offer-modifications.md

# Getting Started with Offer Personalizations

## What are Offers?

Offers are Intelligems tool built to serve your visitors promotions, volume based discounts, and gifts with purchases. Just like any other [modification in a Personalization](https://docs.intelligems.io/personalizations/personalization-modifications), Offers can be targeted to the right channels and visitors to optimize discount spend and maximize your bottom line. They can also be configured to display useful site components such as popups, cart progress bars, and quantity buttons using our **Global Styles components**.

Offers can also be tested against each other: creating a test with multiple Offer Personalizations (Personalizations containing an Offer) lets you take the guess work out of your discount strategy by discovering which offer works best before activating it.

{% hint style="info" %}
When setting up a Personalization containing an Offer, it can be useful to mix in a Content Edit modification as well. This allows you to fine-tune any text on the site that mentions your offer, such as in your announcement bar or on the homepage.
{% endhint %}

## Types of Offers

There are multiple types of Offer modifications.

* Amount off products
* Amount off orders
* Volume discounts
* Free shipping
* Free gift

{% hint style="info" %}
You can place at only Offer one into each Personalization.
{% endhint %}

Each one can optionally be configured to display popups, progress bars, and other **Global Styles components** to help you communicate the offers to visitors.

## **Promotions**

* **Eligible Products:** Select which products are eligible for your Promotion. If no products are selected, then all products will be eligible.
* **Should Stack:** Select whether the offer should combine with other offers that are running at the same time in different Personalizations. If you leave this unchecked, customers will not be able to stack multiple Personalizations containing offers together.
* **Offer Type and Amount:** This can be a percentage off, dollar amount off per order, or dollar amount off per item.
* **Minimum Purchase Requirement:** The number of units or dollar amount needed to achieve the discount. "No Minimum Requirement" will be selected by default.
* **Maximum Discount Amount:** The maximum dollar amount discount that a customer can receive in the case of a percentage off offer.
* **Discount Title:** This is the discount name that'll be visible at checkout for customers who receive the discount.

{% embed url="<https://www.loom.com/share/661b30d4e53c449d87620069633dd998?sid=560dcce7-c7fd-4734-99a2-98c04bc4837f>" %}

{% embed url="<https://www.loom.com/share/96710d42ae4341f2b33512a3366293b4?sid=25e37c92-8972-43fe-81a8-94aeb3e13fbb>" %}

## Gift with Purchase

* **Select a Gift with Purchase:** Select which product will be provided as a gift with purchase. Note that you can only select one product, and one variant if there are multiple variants of that product. If you would like your customers to be able to choose a variant, please note that Intelligems does not currently provide the front end component for this.
* **Should Stack:** Select whether the offer should combine with other offers that are running at the same time in different Experiences. If you leave this unchecked, customers will not be able to stack multiple Personalizations containing offers together.
* **Minimum Purchase Requirement:** The number of units or dollar amount needed to achieve the discount. "No Minimum Requirement" will be selected by default.
  * **Eligible Products:** If the gift with purchase should only be applied when visitors buy select products, you can additionally specify which products count toward the gift here. If you specify eligible products, only these will count toward the minimum you set. For example, if visitors only get GWP if they buy 3 items (or $30 worth of items) and only products A and B are eligible, then they will have to buy 3 of A and/or B (or $30 worth of A and/or B) to get the gift.
* **Automatically Add Gift to Cart:** Toggling this option on will automatically add the gift to cart when a customer has met the requirements. If this is left off, a customer will need to manually add the product to cart to receive the free gift. Please note that you'll need to choose one product variant to be able to turn this option on.
* **Discount Label:** This is the discount name that'll be visible at checkout for customers who receive the discount.

{% embed url="<https://www.loom.com/share/7d7d979598894bcfa20a9de8773eec44?sid=12fb30b8-95b5-4cab-b44a-e05131b45607>" %}

## Free Shipping Offer

The free shipping offer activates free shipping under certain conditions, automatically removing shipping costs from a customer's checkout without any Shopify configuration work. It can be applied as its own offer, or as part of one or more tiers in a Volume Discount (see below).

* **Minimum Purchase Requirement:** The number of units or dollar amount needed to activate free shipping. "No Minimum Requirement" will be selected by default.
* **Limit Ship-to Countries:** If free shipping should not be offered to all countries, choose a white list here. Because customers choose ship-to country at checkout, this means they will see the free shipping progress bar and messaging in their cart until they enter checkout and choose their ship-to country, at which point their free shipping discount may be removed.
* **Choose Eligible Rates:** Configure which of your store's saved shipping rates rates should be eligible, if not all. You can do this:
  * **By name:** for example, use "Rate name does not contain *International*" if you have multiple International rates that shouldn't be discounted. If you select multiple conditions here, any rates that meet at least one of your qualifications will be discounted. Any rates that do not meet any of your qualifications will not be discounted.
  * **By amount:** for example, use this if it would be too expensive for you to discount shipping on large expensive-to-ship items.
* **Discount Label:** This is the discount name that'll be visible at checkout for customers who receive the discount.

  <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-05114b70ce3a59588ca241b948c68588c1007d0a%2Fimage.png?alt=media" alt=""><figcaption><p>Discount Label Placement</p></figcaption></figure>

{% embed url="<https://www.loom.com/share/d111b5f7b7574d4e8ca3a73c3615cedf?sid=6e1e2b3c-7803-4c9f-b825-af418d23e4e8>" %}

## Volume Discounts

To configure a Volume Discount, fill out the following fields:

* **Eligible Products:** Select which products are eligible for your Volume Discount. If no products are selected, then all products will be eligible.
* **Should Stack:** Select whether the offer should combine with other offers that are running at the same time in different Personalizations. If you leave this unchecked, customers will not be able to stack multiple Personalizations containing offers together.
* **Discount Tiers:** You are able to create up to four different discount tiers using the blue <mark style="color:blue;">`+`</mark> sign. For each tier, you will select:
  * Whether eligibility for the discount should be based on the quantity of items or the cart subtotal.
  * Whether the discount should be a percentage off, dollar amount off per order, or dollar amount off per item.
  * The number of units or dollar amount needed to achieve the discount.
  * What the percentage or dollar amount of the discount should be.
  * The name of the discount that'll be visible at checkout for customers who receive the discount.
  * Whether the tier includes a gift with purchase, and what that gift is.
* **Free Shipping in Volume Discounts:** Intelligems' Free Shipping offer can be used as a standalone offer, or as a perk on one or more discount tiers in a Volume Discount offer. For example, you can configure a Volume Discount to give 20% off purchase to visitors buying at least one item, and 30% off *plus* free shipping to visitors buying two items.
  * **One configuration:** While you can offer free shipping on multiple tiers, they must all share the same free shipping configuration. This means that Tier 1's free shipping cannot be limited to certain shipping rates while Tier 2's shipping is not.
  * **Powered by Intelligems vs Shopify:** By default if you choose Free Shipping, Intelligems will automatically apply the discount in cart and checkout. If you've already configured Shopify to apply Free Shipping and simply wish for Intelligems to power the messaging, progress bars, and popups, you can choose the "Powered by Shopify" option. This allows you to communicate your specialized tiers - especially those mixing free shipping with other discounts - in a clear and unified way. Legacy existing free shipping Volume Discounts in Intelligems will be set to this option but can be changed.

### How to Set up a Buy More, Save More Volume Discount

{% embed url="<https://www.loom.com/share/16220a85e4b04eddb1c334b3f7713055?sid=ff2a4be5-3c9e-4079-9c55-cf7184348694>" %}

### How to Set Up a Product Quantity Discount on a Single Product using Quantity Button Components

{% embed url="<https://www.loom.com/share/703b111ed1cf42208e9d3bbce9005669?t=1&sid=f8be56c1-284e-4292-a08d-254a0479ef00>" %}

## Setting up Offer Components

You can optionally show various components that communicate your offer to users. The components vary depending on what type of Offer modification you are using, but the full options include:

* **Pop Up / Slide Out:** This pop up location can be configured during setup. The language and colors are fully customizable so you can use this feature to highlight what you want.

{% hint style="warning" %}
**Pop Up / Slide Out Messages** are only shown on the homepage and cannot be configured to be shown on any other pages at this time.
{% endhint %}

* **Quantity Buttons:** These buttons will appear on your product pages for customers to quickly add multiple units to cart. They are automatically installed via the Intelligems script. If you have any trouble with these showing up inside an Offer Personalization, [please use this form to contact our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request). Let us know which experience and specific URLs we can help you with.
* **Shipping Progress Bar & Offer Progress Bar:** This bar will appear in the cart view to show your customers how much more they need to purchase to achieve specific discounts or free shipping, prompting them to buy more to get the best deal without ever leaving their cart. More info [here](https://docs.intelligems.io/offer-personalizations/offers-integrating-widgets).

{% hint style="danger" %}
**Headless Stores:** Components do not work out-of-the-box and customers must build their own front-end implementation.
{% endhint %}

## Testing Offers

You can test offers against each other to see which one is best. You can do this in two ways: create and Offer and then add it to a Test or Create an Offer Test. Both flows achieve the same results. You can follow either setup flow below.

### Setting Up an Offer Test from Offer Creation Flow

{% embed url="<https://www.loom.com/share/3c872bdb406c4355a3785c1ee0f966fa?sid=0dbe6e51-3cf7-49ae-8644-1f03f059733e>" %}

### Setting up an Offer Test from Test Creation Flow

{% embed url="<https://www.loom.com/share/402158d0b8c845c39e07477e3b401e84>" %}

You can read our [full guide here](https://docs.intelligems.io/offer-personalizations/testing-offer-personalizations).

## How do Offers Work?

Intelligems uses [Shopify Discount Functions ](https://shopify.dev/docs/api/functions/reference/product-discounts)to provide the offers you set up in the Intelligems app. The necessary Function will be created automatically when you create a new Offer Experience or Offer test in the Intelligems app, but will not be available to customers until you start your Offer test or activate your the Experience containing your offer.
