# Intelligems Documentation

Source: https://docs.intelligems.io/llms-full.txt

---

# Welcome to Intelligems

## **What is Intelligems?**

Intelligems is the ultimate profit optimization tool. We provide data-driven solutions and help maximize profits for Shopify merchants wanting to optimize their content, prices, discounts, and shipping rates.

Our mission is simple: we want to help e-commerce entrepreneurs improve their businesses and make more money, by helping you use data to manage your websites and profitability more effectively. We aim to provide independent e-commerce stores access to the same revenue optimization tools that power the growth and profitability of companies like Amazon and Uber.

## **Why Intelligems?**

Our founders and several team members met at Via Transportation, a ridesharing company based in NYC. Over the course of five years, we gradually built out the tools, data, algorithms, and systems to compete with the rapidly evolving rideshare market.

The most powerful tool we built was a dynamic pricing engine underpinned by robust A/B testing. Any question or hypothesis we had, we could simply run a test to get the (statistically significant) answer.

Now, as Intelligems, we are bringing our learning, mindset, and toolkit to e-commerce operators, especially Shopify store owners.

{% hint style="info" %}
Looking for developer docs? You're in the right place, you can [get started here](https://docs.intelligems.io/developer-resources/javascript-api)!
{% endhint %}

## **What can we test with Intelligems?**

Intelligems let’s you test just about anything on your Shopify store. See below for more details on the four different categories of tests Intelligems can help you run. If you don’t see what you’re looking for in one of those options, or aren’t sure of the best way to set up a specific test you have in mind, reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).

### Pricing

Intelligems takes the guesswork out of setting your product prices by allowing you to A/B test prices in real time in order to find the “right” product prices to drive profit, revenue, and conversion boosts.

{% content-ref url="price-testing/price-testing-getting-started" %}
[price-testing-getting-started](https://docs.intelligems.io/price-testing/price-testing-getting-started)
{% endcontent-ref %}

### Shipping

Testing your shipping rates and thresholds with Intelligems allows you to find rates that work for you and your customers. The right shipping profile can allow you to boost profits, maximize conversion without sacrificing on margin, or boost AOV.

{% content-ref url="shipping-testing/shipping-testing-getting-started" %}
[shipping-testing-getting-started](https://docs.intelligems.io/shipping-testing/shipping-testing-getting-started)
{% endcontent-ref %}

### Content

Intelligems can run A/B tests for website imagery and copy, landing pages, Shopify themes or templates, UX, and more. With Google Optimize recently sunsetting, now is the right time to transition.

{% content-ref url="content-testing/content-testing-getting-started" %}
[content-testing-getting-started](https://docs.intelligems.io/content-testing/content-testing-getting-started)
{% endcontent-ref %}

### Experiences & Offers

[Experiences ](https://docs.intelligems.io/personalizations)let you offer code-less content changes, promotions, volume discounts, and free gifts to particular audiences or all site visitors. You can test Offers via Experiences before deploying them to optimize your discount strategy. Integrate with Klaviyo flows, external advertisements, and landing pages to ensure consistent experiences for visitors. This includes things like testing your welcome offer, or gift-with-purchase thresholds to boost AOV.

{% content-ref url="personalizations/personalizations-getting-started" %}
[personalizations-getting-started](https://docs.intelligems.io/personalizations/personalizations-getting-started)
{% endcontent-ref %}


# Getting Started

## Install Intelligems to your Shopify Store

If you have not already done so, you can install Intelligems from the [**Shopify App Store**](https://apps.shopify.com/intelligems?utm_source=docs)!

## Getting Started

There are so many capabilities of Intelligems, ranging from testing design and content on your site to the prices of your top-selling products.

Get inspired by some of our [test suggestions](https://docs.intelligems.io/getting-started/common-use-cases), and get started in minutes by following the steps below:

1. **Install Intelligems** from the [Shopify App Store](https://apps.shopify.com/intelligems?utm_source=docs).
2. **Approve billing** to unlock your 14-day free trial on our Core Plan — cancel anytime. Learn more about pricing [here](https://intelligems.io/pricing).
3. **Follow our** [**step-by-step integration**](https://docs.intelligems.io/price-testing/price-testing-integration-guides) **guides** if you're setting up Price Testing.\
   \&#xNAN;*Just testing Content, Shipping, or Offers?* All you need is to [add the Intelligems Script](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) to your theme!
4. **Create your first test** — it only takes a few minutes.
5. **Start collecting data and optimizing!**

## Add Intelligems to Your Theme

First and foremost, you need to add the Intelligems script to your Shopify theme. This is a prerequisite for every use case with Intelligems. It's very easy and should not require a developer. [Here is a quick guide](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) on adding the Intelligems Script to your theme!&#x20;

## Price Test Integrations

A/B testing prices is a powerful lever because it's the underlying driver of the economics for a brand. Intelligems aims to make testing prices a seamless experience for your customers and easy to set up.

{% hint style="success" %}
Intelligems will do the price Integration as part of onboarding for all customers who go through our onboarding process. For more information, reach out to <sales@intelligems.io>.
{% endhint %}

If you want to do your own integration, or just want to understand more about price testing integrations, here are some helpful articles:

<table data-view="cards"><thead><tr><th align="center"></th><th align="center"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td align="center"><strong>Shopify Plus</strong></td><td align="center">Price Testing Integration</td><td><a href="../price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts">integration-guide-using-checkout-scripts</a></td></tr><tr><td align="center"><strong>Shopify Non-Plus</strong></td><td align="center">Price Testing Integration</td><td><a href="../price-testing/price-testing-integration-guides/integration-guide-using-duplicate-products">integration-guide-using-duplicate-products</a></td></tr><tr><td align="center"><strong>Shopify Functions</strong></td><td align="center">Price Testing Integration</td><td><a href="../price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions">integration-guide-using-shopify-functions</a></td></tr></tbody></table>


# Adding Intelligems Script to your Theme

## Introduction

Adding the Intelligems script to your site is the most important step to getting started with testing with Intelligems! Adding the Intelligems script to your site is the only mandatory integration step for Content, Shipping and Campaigns testing, and is the first step to integrating for Price testing. There are two options below for adding the Intelligems script to your site.

## Option 1: Use the App Embed Block

{% hint style="success" %}
This is the easiest installation method that works for most stores!
{% endhint %}

The fastest way to add Intelligems JavaScript to your theme is to enable it in the "Customize" section of your theme editor. You can do so by logging into your Shopify Admin, and navigating to Sales Channels > Online Store > Live theme - Customize > App Embeds. Search "Intelligems", make sure it is toggled on, and click "Save" in the top right.\
\
This will load Intelligems in a fashion that works optimally for performance and A/B testing on most stores. If for any reason you encounter performance concerns, [see our docs on performance optimization](https://docs.intelligems.io/performance-optimization/optimizing-your-price-test-integration).

{% hint style="warning" %}
For any **password protected store**, we will not be able to automatically detect the script, so you will continue to get an error message in the app regarding the script not being in your theme.
{% endhint %}

## Option 2: Add to Your Theme Code

{% hint style="info" %}
If you are on Shopify Plus and are still using checkout.liquid, you will still need to manually add Intelligems JavaScript to your checkout.liquid file in order to hide the discount or preview bar at checkout. Your individual script tag is located on the settings page in the Intelligems App.&#x20;
{% endhint %}

{% hint style="danger" %}
This will need to be manually removed if you uninstall Intelligems.
{% endhint %}

To complete this, go to the settings page in the Intelligems app. Once there, you'll see a section called "Theme Script". Click the blue button in that block that says "Copy Script". This will copy your unique Intelligems script to your clipboard.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FqvWfk91wEFeZyv5joSHW%2FScreenshot%202025-09-25%20at%205.30.44%E2%80%AFPM.png?alt=media&#x26;token=d06b3072-4307-499b-a878-b3b3ed6c9da8" alt=""><figcaption></figcaption></figure>

Now head over to your Shopify account, and paste the Intelligems Script as a source into the `<head>` of each of these files:

* theme.liquid
* any other theme.\*.liquid files (e.g., theme.gempages.liquid if you have this file)

Here's a video walking through those steps as well:

{% embed url="<https://www.loom.com/share/187128fe3b9c4334b5904d4c4de48dbf?sid=477d7023-fb18-4218-accd-fbd0775fee88>" %}

### Post-Purchase Page for Theme Tests

If you are planning to run a theme test, you should also add our script to the Additional Scripts section for the Post-purchase page. This will hide the theme preview bar from showing up on your thank you page. You can get to the Additional Scripts section pictured below by going to Settings -> Checkout -> Scroll about halfway down to "Post-purchase page".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FOsLZwxGXsZL8j5WgmVZJ%2FScreenshot%202024-07-31%20at%2012.22.21%20PM.png?alt=media&#x26;token=6f666104-afcd-4963-95a5-c18f07f8b890" alt=""><figcaption></figcaption></figure>


# Updating the Intelligems Script

{% hint style="success" %}
The **CommonJS script will remain supported for current features.** However, **new features will** **only be available with the ESM script**, so we recommend updating your Script code as soon as you are able to. Additionally, the ESM script improves plugin performance, making it faster!
{% endhint %}

## Context

Historically, Intelligems utilized a version of its script known as the CommonJS script. In December 2024, an update was released, transitioning to a new and improved version called the ESM script.

Here’s how the scripts differ:

#### Pre-December 9, 2024 (CommonJS Script)

The final line of the script looks like this (with `abcdefghijk` replaced by your unique customer ID):

```html
<script src="https://cdn.intelligems.io/abcdefghijk.js"></script>
```

#### Post-December 9, 2024 (ESM Script)

The updated script uses the following format (with `abcdefghijk` replaced by your unique customer ID):

```html
<script type="module" src="https://cdn.intelligems.io/esm/abcdefghijk/bundle.js"></script>
```

Key differences include:

1. **`type="module"`** – the script is now a JavaScript module.
2. **`esm`** – the directory structure reflects the new ESM format.
3. **`bundle`** – the updated structure for improved performance.

{% hint style="info" %}
The first eight lines of the script remain unchanged.
{% endhint %}

## Required Changes

If you are seeing the below error in your Intelligems app:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F4jgbV64NN5IdIBsAvcSg%2FScreenshot%202025-03-10%20at%2010.08.32%20AM.png?alt=media&#x26;token=a234f891-6ada-4a5d-b7ae-007e9ee3461a" alt=""><figcaption></figcaption></figure>

This means you need to update your theme code to reflect the new ESM Script. Here are the steps to do so:

1. Go to the settings page in the Intelligems app.
2. Once you're there, you'll see a section called "Theme Script". Click the blue button in that block that says "Copy Script". This will copy your unique Intelligems script to your clipboard.
3. Now head over to your Shopify account, and replace your current Intelligems Script with your new one. The script should be included as a source in the `<head>` of each of these files:
   1. theme.liquid
   2. any other theme.\*.liquid files (e.g., theme.gempages.liquid if you have this file)
   3. checkout.liquid (if you have this file; most themes do not)

Here is a video walking through those steps:

{% embed url="<https://www.loom.com/share/0c95974114f94e1797cbd4896a88dd10?sid=960987e2-93e7-4cde-8430-5ad15d09a71e>" %}

#### Post-Purchase Page for Theme Tests

If you are planning to run a theme test, you should also update your script in the Additional Scripts section for the Post-purchase page if you are using this. This will hide the theme preview bar from showing up on your thank you page. You can get to the Additional Scripts section pictured below by going to Settings -> Checkout -> Scroll about halfway down to "Post-purchase page".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FOsLZwxGXsZL8j5WgmVZJ%2FScreenshot%202024-07-31%20at%2012.22.21%20PM.png?alt=media&#x26;token=6f666104-afcd-4963-95a5-c18f07f8b890" alt=""><figcaption></figcaption></figure>


# Common Use Cases

What you decide to test ultimately depends upon your business goals and priorities. The following common use cases are broken out by test type & can help get the creative juices flowing to jump-start your testing program, as well as walk you through the steps to get these tests set up. Please don't hesitate to reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions!

{% content-ref url="common-use-cases/price-test-common-use-cases" %}
[price-test-common-use-cases](https://docs.intelligems.io/getting-started/common-use-cases/price-test-common-use-cases)
{% endcontent-ref %}

{% content-ref url="common-use-cases/shipping-test-common-use-cases" %}
[shipping-test-common-use-cases](https://docs.intelligems.io/getting-started/common-use-cases/shipping-test-common-use-cases)
{% endcontent-ref %}

{% content-ref url="common-use-cases/content-test-common-use-cases" %}
[content-test-common-use-cases](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases)
{% endcontent-ref %}

{% content-ref url="common-use-cases/offer-test-common-use-cases" %}
[offer-test-common-use-cases](https://docs.intelligems.io/getting-started/common-use-cases/offer-test-common-use-cases)
{% endcontent-ref %}


# Price Test Common Use Cases

Price testing is a powerful tool because it allows businesses to determine the optimal price point for their products or services. By experimenting with different prices, companies can gather data on consumer behavior, demand elasticity, and profitability. This helps them understand what customers are willing to pay, which in turn maximizes revenue, enhances market positioning, and minimizes the risk of underpricing or overpricing. Effective price testing leads to better decision-making, ensuring businesses stay competitive while meeting customer expectations and financial goals.

Check out the below common test designs for inspiration on how to get started:

{% content-ref url="price-test-common-use-cases/the-straddle" %}
[the-straddle](https://docs.intelligems.io/getting-started/common-use-cases/price-test-common-use-cases/the-straddle)
{% endcontent-ref %}

{% content-ref url="price-test-common-use-cases/the-double-down" %}
[the-double-down](https://docs.intelligems.io/getting-started/common-use-cases/price-test-common-use-cases/the-double-down)
{% endcontent-ref %}

{% content-ref url="price-test-common-use-cases/the-strikethrough" %}
[the-strikethrough](https://docs.intelligems.io/getting-started/common-use-cases/price-test-common-use-cases/the-strikethrough)
{% endcontent-ref %}

{% content-ref url="price-test-common-use-cases/the-great-discount-debate" %}
[the-great-discount-debate](https://docs.intelligems.io/getting-started/common-use-cases/price-test-common-use-cases/the-great-discount-debate)
{% endcontent-ref %}

{% content-ref url="price-test-common-use-cases/savings-showdown-volume-discount-vs.-price-discount" %}
[savings-showdown-volume-discount-vs.-price-discount](https://docs.intelligems.io/getting-started/common-use-cases/price-test-common-use-cases/savings-showdown-volume-discount-vs.-price-discount)
{% endcontent-ref %}


# The Straddle

Increase and decrease the price of every product by 10%. This is a great place to start as it will give you a look at elasticity across the board. If you don't want to start with your entire store, pick a few products or a collection to test first and iterate from there. Check out this [case study](https://blog.intelligems.io/intelli-blog/drive-conversions-revenue-through-price-decreases) on a brand who recently ran this type of test on their main collection and found that the lower price group generated nearly a 40% lift in conversion rate which yielded a 15% increase in revenue.

*What this test design might look like:*

|               | **Control Price** | **+10%** | **-10%** |
| ------------- | ----------------- | -------- | -------- |
| **Product A** | $10               | $11      | $9       |
| **Product B** | $20               | $22      | $18      |

{% hint style="info" %}
The Control Group should almost always be equal to what is currently live on the site - keeping one group consistent will keep your baseline consistent, giving you the most actionable results.
{% endhint %}


# The Double Down

Iterate based on the results from the test above. Let's say you run the test outlined above, and find that you see higher conversion and higher revenue per visitor on Product A at the $9 price point and on Product B you don't see a change in conversion across the three price points, but you see an increase in revenue per visitor on the $22 price point. Because [price elasticity is a curve](https://blog.intelligems.io/intelli-blog/price-elasticity), it may make sense to run another test drilling in further on the price for these products.

*What this test design might look like based on the above scenario:*

<table data-header-hidden><thead><tr><th width="242"></th><th></th><th></th><th></th></tr></thead><tbody><tr><td></td><td><strong>Control Price</strong></td><td><strong>Lower/Higher</strong></td><td><strong>Even Lower/Higher</strong></td></tr><tr><td><strong>Product A</strong></td><td>$9</td><td>$8</td><td>$7</td></tr><tr><td><strong>Product B</strong></td><td>$22</td><td>$24</td><td>$26</td></tr></tbody></table>

{% hint style="info" %}
Note that this is one scenario where your Control Group is not what has been live on the site, but rather the 'winner' from the previous test.
{% endhint %}


# The Strikethrough

Try out different Compare-At prices while keeping the actual price consistent. Price psychology can have major impacts on conversion - how might a larger perceived discount impact your consumer's behavior?

*What this test design might look like:*

<table data-header-hidden><thead><tr><th></th><th width="133"></th><th width="158"></th><th width="122"></th><th></th></tr></thead><tbody><tr><td> </td><td><strong>Control Price</strong></td><td><strong>Control Compare-At Price</strong></td><td><strong>Group A Price</strong></td><td><strong>Group A Compare-At Price</strong></td></tr><tr><td><strong>Product A</strong></td><td>$20</td><td>$25</td><td>$20</td><td>$30</td></tr></tbody></table>


# The Great Discount Debate

Similar to how the discount *value* impacts price psychology in the above, the discount *type* can also impact consumer behavior - would a 10% or $5 discount that ultimately have the same value be more likely to get you across the line? Check out pricing strategy #3 in [this blog](https://blog.intelligems.io/intelli-blog/discounting-playbook) for more details on the psychology behind this.

*What this test design might look like:*

<table data-header-hidden><thead><tr><th width="162"></th><th></th><th width="102"></th><th></th><th></th></tr></thead><tbody><tr><td></td><td><strong>% Group Price</strong></td><td><strong>% Group Discount</strong></td><td><strong>$ Group Price</strong></td><td><strong>$ Group Discount</strong></td></tr><tr><td><strong>Product A</strong></td><td>$50</td><td>10% Off</td><td>$50</td><td>$5 Off</td></tr></tbody></table>


# Savings Showdown: Volume Discount vs. Price Discount

Test Volume Discounts in comparison to reduced product prices. Check out this [case study](https://blog.intelligems.io/intelli-blog/discounts_vs_price) on a brand that recently ran a test just like this, and found that reduced product prices perform better than discounts on their site.

*What this test design might look like:*\\

<table data-header-hidden><thead><tr><th></th><th></th><th width="209"></th><th></th><th></th></tr></thead><tbody><tr><td> </td><td><strong>Control Price</strong></td><td><strong>Volume Discount</strong></td><td><strong>Lower Price</strong></td><td><strong>Volume Discount</strong></td></tr><tr><td><strong>Product A</strong></td><td>$49.99</td><td><p>10% off 2+ Units</p><p>15% off 3+ Units</p><p>20% off 4+ Units</p></td><td>$39.99</td><td>None</td></tr></tbody></table>


# Shipping Test Common Use Cases

Shipping testing is a powerful strategy because it helps businesses optimize delivery methods, costs, and times to meet customer expectations while improving operational efficiency. By experimenting with different shipping options, pricing, and speeds, companies can identify the most effective solutions to increase customer satisfaction and loyalty. It also helps reduce cart abandonment, balance logistics costs, and ensure smooth operations, leading to a better overall customer experience and higher profitability. In an e-commerce-driven world, shipping testing can make or break a company’s competitive edge.

Check out the below common test designs for inspiration on how to get started:

{% content-ref url="shipping-test-common-use-cases/the-flat-fee-face-off" %}
[the-flat-fee-face-off](https://docs.intelligems.io/getting-started/common-use-cases/shipping-test-common-use-cases/the-flat-fee-face-off)
{% endcontent-ref %}

{% content-ref url="shipping-test-common-use-cases/the-threshold-trials" %}
[the-threshold-trials](https://docs.intelligems.io/getting-started/common-use-cases/shipping-test-common-use-cases/the-threshold-trials)
{% endcontent-ref %}


# The Flat Fee Face Off

Ever since Amazon made free shipping the norm, many brands have felt like they had to move in that direction. But what if higher shipping rates didn't actually affect your conversion rate and you could put that cost back onto the customer? You'll never know unless you test it out.

*What this test design might look like:*

<table data-header-hidden><thead><tr><th width="310"></th><th></th><th></th><th></th></tr></thead><tbody><tr><td> </td><td><strong>Control Group</strong></td><td><strong>Slightly Higher</strong></td><td><strong>Highest</strong></td></tr><tr><td><strong>Flat Shipping Rate</strong></td><td>Free</td><td>$5</td><td>$10</td></tr></tbody></table>


# The Threshold Trials

## The Threshold Trials

In line with the above test, some brands have have moved towards free shipping over a certain threshold to keep customers from finding another seller that does offer free shipping, as well as to increase AOV. If you're not already doing this, you could test a few different thresholds out, and if you do already have a threshold, you could test a higher and lower threshold (or a couple higher/lower) to try to find the sweet spot. Check out this [case study](https://blog.intelligems.io/intelli-blog/boost-aov-by-upping-your-free-shipping-threshold) on a brand who recently ran this type of test and found a \~6% increase in AOV and \~12% increase in revenue per site visitor!

*What this test design might look like:*

<table data-header-hidden><thead><tr><th width="162"></th><th></th><th></th><th width="243"></th><th></th></tr></thead><tbody><tr><td> </td><td><strong>Control Group</strong></td><td><strong>Lower Threshold</strong></td><td><strong>Higher Threshold</strong></td><td><strong>Highest Threshold</strong></td></tr><tr><td><strong>Threshold</strong></td><td>$75</td><td>$50</td><td>$100</td><td>$125</td></tr></tbody></table>

{% hint style="info" %}
We recommend taking a look at a histogram of your order values for the last month (or more) when deciding what thresholds to test. For example, if a majority of your orders come in around $90-$100, but your current threshold is $50, you may want to consider testing out a $100 threshold to push people to add one more item to their cart.
{% endhint %}


# Content Test Common Use Cases

Content testing is a powerful tool for businesses because it enables them to determine what types of messages, formats, and visuals resonate best with their target audience. By experimenting with different content variations—whether it's headlines, images, or calls-to-action—companies can gather insights on what drives engagement, conversions, and brand loyalty. This data-driven approach helps optimize marketing strategies, ensuring content is not only relevant but also effective in achieving specific goals. Content testing reduces guesswork, improves ROI, and ensures that businesses connect with their audience in meaningful ways.

Check out the below common test designs for inspiration on how to get started:

{% content-ref url="content-test-common-use-cases/landing-page-testing" %}
[landing-page-testing](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/landing-page-testing)
{% endcontent-ref %}

{% content-ref url="content-test-common-use-cases/testing-a-brand-new-theme" %}
[testing-a-brand-new-theme](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-a-brand-new-theme)
{% endcontent-ref %}

{% content-ref url="content-test-common-use-cases/testing-different-imagery" %}
[testing-different-imagery](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-different-imagery)
{% endcontent-ref %}

{% content-ref url="content-test-common-use-cases/testing-cart-elements" %}
[testing-cart-elements](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-cart-elements)
{% endcontent-ref %}

{% content-ref url="content-test-common-use-cases/testing-announcement-bar-text" %}
[testing-announcement-bar-text](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-announcement-bar-text)
{% endcontent-ref %}

{% content-ref url="content-test-common-use-cases/navigation-menu" %}
[navigation-menu](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/navigation-menu)
{% endcontent-ref %}

{% content-ref url="content-test-common-use-cases/testing-checkout-blocks" %}
[testing-checkout-blocks](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-checkout-blocks)
{% endcontent-ref %}

{% content-ref url="content-test-common-use-cases/tariff-testing-on-vs-off" %}
[tariff-testing-on-vs-off](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/tariff-testing-on-vs-off)
{% endcontent-ref %}

{% content-ref url="content-test-common-use-cases/testing-express-payment-options" %}
[testing-express-payment-options](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-express-payment-options)
{% endcontent-ref %}


# Landing Page Testing

## Introduction

Testing landing pages for an eCommerce site is crucial for maximizing conversion rates & ROAS, as well as enhancing user experience. A few examples may include:

* Testing different layouts or calls to action for your landing pages from Google ads
* Sending your Facebook traffic to a landing page versus directly to a collection page or your homepage
* Experimenting with different offers for ad traffic, such as 10% vs 20% off their first order

You can use Intelligems to test landing pages in a few different ways. Here, we'll explore testing landing pages using [Split URL](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test) tests and [Onsite Edit](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test) tests. Before getting started, make sure you've [added the Intelligems script](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) to your Shopify theme.

## Setting the Test Up

### Option 1: Split URL Test

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FXNCBDK6Uv0lSnn3k6lv3%2Fimage.png?alt=media&#x26;token=44520344-d507-478a-9509-61b1a9759689" alt=""><figcaption><p>Two example landing pages that we'd like to test against each other</p></figcaption></figure>

Split URL tests let you test pages against each other using redirects. When a visitor lands on the control page, they are randomized into a test group, and, if they're not in the control group, they'll be redirected to the corresponding page for their group.

This test type is a great option if you want to get your test up and running quickly, especially if you're using a page builder or making large changes to the page you're testing.

To set up a Split URL landing page test:

1. **Create the versions of the page you want to test.** Create the pages you want to test, for example, with a page builder or with the Shopify theme editor, and make sure they're accessible on your store through a URL. Note down the URLs of the pages you're testing.
2. **Create a new Intelligems Split URL test** by clicking "Create New Test" on the [Intelligems homepage](https://app.intelligems.io/), choosing "Content Test," and then "Split URL Test"
3. **Create a test group for each variation you'd like to test**. In my example, I'll be testing the existing control page against one variant, so I'll have two test groups total: Control and Test.\
   \\

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FHLzFHAUJHFp7QSE1tbkQ%2Fimage.png?alt=media&#x26;token=dbf6b016-865f-4e30-9c01-c689266e6f1a" alt=""><figcaption></figcaption></figure>

4. **Enter the URLs of the two landing pages** in the test setup. A "Simple" redirect should work for our purposes, since we just want to split between two known URLs. "Advanced" redirects are for when you'd like to match or replace wildcard text.\
   \
   Choose "Redirect Every Time" if a visitor who's assigned to test page should be redirected sent to it any time they reach the Control. Choose "Redirect One Time" if they should be redirected only the first time. In our case, since we're testing fully replacing the control page with the test page, we'll choose "Redirect Every Time."\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FH0Wr06xD0Xhl2AIEMtHd%2Fimage.png?alt=media&#x26;token=8aabc3eb-a779-48c9-a0d1-b360fa16ca5f" alt="" width="563"><figcaption></figcaption></figure>
5. **Save and preview your experiment**. You can refer to our [QA guide](https://docs.intelligems.io/content-testing/content-test-qa-checklist#page-redirect-tests) for tips on what to look for when testing.
6. **Launch!**

{% hint style="warning" %}
If you use a page builder like PageFly, Replo or GemPages, be sure to add Intelligems JavaScript to their theme files as outlined [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme)! If this step is missed, Intelligems will not be able to track the data for those pages.
{% endhint %}

### Option 2: Onsite Edit Test

Another option is an Onsite Edit test. In an Onsite Edit test, you can use Intelligems' visual editor, injected Javascript, or CSS to insert, hide, and re-arrange elements on a page.

This test type is a good fit if you're making a smaller adjustment to a page (e.g., adding or removing a section, etc.), or if you'd like to avoid redirecting any users for performance or other reasons, and you're comfortable with basic HTML and CSS.

To set up an Onsite Edit landing page test:

1. **Decide on a strategy for switching content**. For example, if you're testing a new section, it's often easiest to add this section to the page, hidden by default with CSS, and then use CSS injection to unhide it for the test group. Another option would be to use Intelligems' visual editor to *add* the section for the test group. We'll go through both techniques below.
2. **Create a new Intelligems Onsite Edit test** by clicking "Create a Test" on the [Intelligems homepage](https://app.intelligems.io/), choosing "Content Test," and then "Onsite Edit"
3. **Create a test group for each variation you'd like to test**. Here, we're testing the existing control page against one variant with an added section, so we'll have two test groups total: Control and Test
4. **Use Page Targeting to target the test on the landing page**. We want the onsite edits to execute only on the landing page, and we want to make sure only visitors to the landing page enter the test and factor into analytics. We can do this by targeting the test on the landing page by URL. For example:\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FK3grtepFmDBW8kTyCzMk%2Fpage-targeting.png?alt=media&#x26;token=3ae613da-de5e-4533-84c3-12ebd07b02a7" alt=""><figcaption><p>Page Targeting in an Onsite Edits Test</p></figcaption></figure>
5. **Set up the onsite edit.**
   1. Injected CSS: one way to test a new section of a page is to put the section in the page, but hidden by default, and then inject CSS to unhide it for the test group. For example, you could add a CSS class to your theme:\
      \
      `.hidden-section { display: none; }`\
      \
      And add this class to new page section in the theme editor or page builder (if you're unable to edit the section's classes you could also write a different selector rather than adding a new class, and add this CSS to your theme's code or with injection for the control group).\
      \
      Then, for the test group, inject some CSS to override this and unhide the section:\
      \
      `.hidden-section { display: block !important; }`\\

      <div data-full-width="true"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fir774t9q7Y9axPNfP8NC%2Fcss-styles.png?alt=media&#x26;token=339cf24d-e6c2-4bd7-9ea1-323710001236" alt=""><figcaption><p>CSS injection in an Onsite Edits Test</p></figcaption></figure></div>
   2. Insert the section: another way to test a new section is to insert it using Intelligems' onsite editor. For example, to insert a testimonials section above the featured collection on this page, first open the Intelligems onsite editor, then choose the featured collection section and choose "Edit HTML / CSS":\\

      <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FMfeuW9pbdp8rwXMcd3aA%2Fimage.png?alt=media&#x26;token=64dc6d75-b7a9-470e-9302-25bed4ab08de" alt=""><figcaption></figcaption></figure>

      In the dialog, choose "Prepend Outside" in the dropdown in the bottom left. This tells Intelligems to inject the HTML you enter before the section you selected, instead of replacing it.\\

      <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F79BnIUVom9MuDBAD21bX%2Fimage.png?alt=media&#x26;token=635967a6-580e-49fd-a8c7-f82b7462e2dc" alt=""><figcaption></figcaption></figure>

      Next, enter the HTML for the new section in the text editor, and click "Apply." You'll now see the new section appear above the one we selected:\\

      <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FFtAFJGLsG8MHuwIMCL3a%2Fimage.png?alt=media&#x26;token=14c7af78-e48b-4af4-9bff-395226fcefe5" alt=""><figcaption></figcaption></figure>
6. **Save and preview your experiment**. You can refer to our [QA guide](https://docs.intelligems.io/content-testing/content-test-qa-checklist#page-redirect-tests) for tips on what to look for when testing.
7. **Launch!**&#x20;


# Testing a Brand New Theme

## Introduction

Your team has spent the last month perfecting a new theme for your store. They’ve spent hours QAing it and are confident that it is ready to launch. Testing this new theme compared to your live theme can be a great way to confirm whether the new theme is better than your old theme, and that no issues were overlooked. The goal of this test is to see either no difference, or some uplift, for the new theme. If there is a negative impact, this may be a sign that there are still bugs to work out.

You can use Intelligems to test your brand new theme by setting up a [Theme Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-theme-test). Before getting started, make sure you've [added the Intelligems Script](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) to all themes that will be included in the test. This allows Intelligems to hide the theme preview bar and track all data correctly.

## Setting the Test Up

Theme tests allow you to test entire themes against each other using redirects. When a visitor lands on your website, they are randomized into a test group, and, if they're not in the control group, they'll be redirected to the test theme where they'll stay for the remainder of the test. This test type is the **only way to test two or more entirely different themes against each other**, so it is the best option when you are looking to launch a brand new theme.

To set up a Theme Test for your new theme:

1. Create your new theme in Shopify. Make sure you've [added the Intelligems Script](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) to all themes that will be included in the test!
2. Create a new Theme Test by clicking "Create New Test" on the [Intelligems homepage](https://app.intelligems.io/), then choose "Content Test" and then "Theme Test"
3. Rename "New Group 1" to match the name of your new theme.
4. Select your live theme for the control group, and your new theme for the test group.

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FJZAvrCWTeh1Mxn7XDOPN%2FScreenshot%202024-10-14%20at%2010.53.28%20AM.png?alt=media&#x26;token=9e156dbe-f749-40bb-8037-fa15bb90b0df" alt=""><figcaption></figcaption></figure>
5. Save and preview your experiment. You can refer to our [QA guide](https://docs.intelligems.io/content-testing/content-test-qa-checklist#page-redirect-tests) for tips on what to look for when testing.
6. Launch!

A few things to keep in mind while testing your new theme:

* If the new theme is performing well, you can gradually increase the percent of traffic being sent to that theme by editing your test in the Test Groups tab:

<div data-full-width="false"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F9GXU43PAz2vfq3XV1CTF%2Ftheme-traffic-split.png?alt=media&#x26;token=e2724187-89c4-4581-8dc4-5b8c2abe0f38" alt=""><figcaption></figcaption></figure></div>

* Running a theme test means that you need to keep all themes that are part of the test up to date! Any changes that you make to your live theme while a Theme Test is running must also be made to any themes included in your test.
* When you end a Theme Test, do not delete any themes that were part of the test. You can read more on why [here](https://docs.intelligems.io/content-testing/ending-a-theme-test)!


# Testing Different Imagery

Testing homepage banners or product page images is essential for brands aiming to optimize their online presence and drive conversions. The images used on these pages play a significant role in capturing users' attention, conveying brand messaging, and influencing purchasing decisions. By conducting tests, brands can assess various elements such as image composition, color schemes, product placement, and messaging to identify which resonates most effectively with their target audience.

The easiest way to set this up in Intelligems is as an [Onsite Edits Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)! See the video below for a quick demo on how to set this up using Intelligems’ [Image Find & Replace](https://docs.intelligems.io/content-testing/image-find-and-replace) option to test a homepage banner image. You can follow these same steps to test images anywhere on your site!

{% embed url="<https://www.loom.com/share/a42b425e0de84fb2b0293aeb9d555e23>" %}


# Testing Cart Elements

The cart is a pivotal point in the customer journey. A/B testing components of your cart ensures that the user experience is seamless, intuitive, and efficient. By understanding how customers interact with the cart, stores can identify pain points, such as confusing navigation or lack of features, and optimize accordingly.

When it comes to your site’s cart, there are endless elements you could test. Below are just a few of the things that brands often test:

* Displaying the option for a customer to enter a discount code in the cart
* Testing a third-party cart app vs. your Shopify cart
* A different call to action on your checkout button
* Displaying a [free shipping progress bar](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration) to incentivize users to spend more

The best way to set these tests up in Intelligems depends on a few factors, including what exactly you are looking to test, how your cart is set up on your site, and your team’s technical aptitude. See below for a few examples:

* If you are looking to test a relatively small and non-complicated portion of your cart, you may be able to set your test up using Intelligems’ [Find & Replace tool](https://docs.intelligems.io/content-testing/find-and-replace)!&#x20;
  * Test the call-to-action text in the checkout button
  * Show vs. hide components like a progress bar or discount code input field
  * Show vs. hide upsells in the cart
* If you are planning to test something more complicated, if the cart can be controlled using JavaScript, you can use Intelligems’ [JavaScript injection tool](https://docs.intelligems.io/content-testing/css-and-javascript-injection) to test this. If the cart cannot be controlled using JavaScript, or writing JavaScript is not in you team’s capabilities, you could also run it as a [Theme Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-theme-test).


# Testing Announcement Bar Text

## Introduction

By A/B testing your announcement bar, you can identify the most effective design and content for driving conversions and profit. Even simple changes to your announcements can sway customers toward conversion.

Here are a few ideas for A/B testing your Shopify announcement bar using Intelligems:

* **Test different text.** Try using different wording or calls to action in your announcement bar to see what gets the best results.
* **Test different colors.** Experiment with different color schemes to see what is most visually appealing and effective at grabbing attention.
* **Test different positions.** You can also test different positions for your announcement bar on the page.

## Setting the Test Up

Here are the steps to follow to use an Intelligems Onsite Edits test to A/B test your Shopify announcement bar:

* **Check if your theme has a built-in announcement bar feature.** You can do this by going to **Online Store > Themes** and then clicking **Customize**. If your theme has an announcement bar, **Announcement bar** will be displayed in the list of sections or within the "Header" settings.
* **If your theme has a built-in announcement bar feature, follow your theme’s documentation to add it to your online store.** If you’re using a Shopify-supported theme, you can refer to *Free themes from Shopify*.

If your theme does not have a built-in announcement bar feature, you'll need to download a banner app from the Shopify app store.

Once you have an announcement bar set up, you can use Intelligems to A/B test different versions of it. Here are the steps on how to set up an onsite edits test in Intelligems:

1. **Create a new test.** From the A/B tests page, create a new onsite edits test.
2. **Create your test groups.** You will need to create a test group for each variation of your announcement bar that you want to test. Fill in the Test Name and Test Description. You can add new groups by clicking on the ‘+’ button. Use the slider to allocate what percentage of traffic will go to each group.
3. **Make your content edits.** In the Modifications tab, this can be done one of two ways:
   1. **Select Content Edits, then Add & Edit Changes in Visual Editor.** This will take you to your website with Intelligems' edit mode enabled.
   2. Alternatively, you could enter a CSS injection in the Styles & Javascript section.
4. **Set up targeting (optional).** Targeting allows you to apply specific conditions to certain site visitors. You can learn more about targeting [here](https://docs.intelligems.io/general-features/targeting).
5. **Save your changes and start your test.** Intelligems will start tracking the performance of each variation of your announcement bar. You can then use the Intelligems analytics dashboard to see which variation is performing best.

Here's a video demonstrating those steps, using the visual editor:

{% embed url="<https://www.loom.com/share/24da9a9022954036b80368fac39fbc2c?sid=8baeba04-86cf-489d-9ddc-20d9b26829e2>" %}
Video demonstrating how to A/B test the announcement bar with Intelligems
{% endembed %}

{% hint style="info" %}
Note that onsite edits are based on [query selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector). Some themes and announcement bar apps have a different query selector for the announcement bar depending on the specific page. Confirm in preview mode that the updates you've made to the announcement bar are working on all of the pages you intend to change.
{% endhint %}


# Navigation Menu

## Introduction

Testing your navigation menu is a great strategy that can significantly enhance the user experience and drive sales. As one of the primary ways customers interact with your site, the navigation menu plays a crucial role in how they discover products and navigate your offerings. Given its presence on every page, any adjustments can lead to substantial changes in customer behavior and satisfaction. Here are a few aspects you can explore through A/B testing your menu:

* **Layout**: Experiment with different structures to see which is more intuitive for users.
* **Organization**: Test how grouping products affects discoverability and ease of use.
* **Presentation**: Vary the visual design to identify what draws attention and enhances usability.
* **Styles**: Try different color schemes and fonts to see what resonates best with your audience.
* **Wording**: Analyze the effects of different labels and calls to action on customer engagement.

By fine-tuning these elements, you can optimize your navigation menu for better performance and improved customer experience. There are a few different ways you can test your navigation menu. The examples below show how to do this with a [Theme Test](#option-1-theme-test), or through our [Onsite Edits](#option-2-onsite-edits) capabilities.

{% hint style="info" %}
Once you have finished setting up your test, we recommend going through our suggested [Content Test QA Checklist](https://docs.intelligems.io/content-testing/content-test-qa-checklist) before you turn it on.
{% endhint %}

***

## Setting the Test Up

### Option 1: Theme Test

A Theme Test allows you to test a completely new design for your site, as you can make use of a new Shopify theme you're already working on, making it the easiest way to test bigger modifications. Your new theme may contain all sorts of changes, including a new navigation menu, and when a visitor comes to your site, Intelligems will automatically randomize them into one of the themes you've picked for your test.

You can test any of the aspects listed above, as you'll be setting up a new theme with your alternative navigation menu, so the sky is the limit!

To test a new navigation menu through a Theme Test:

1. **Create the new version of the menu you want to test**. Set it up as you normally would on Shopify, creating a new Shopify theme (it may be a copy of your existing theme) in which the new menu will be used.
2. **Follow the steps on** [**How to Set Up a Theme Test**](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-theme-test) to create a new Theme Test. When selecting the themes that will be part of the test, choose your current theme for the control , and the theme containing your new navigation menu as the test.
3. You should be all set to launch your test!

***

### Option 2: Onsite Edits

Intelligems' Onsite Editor is a dynamic and versatile tool that enables you to creatively interact with and test various elements of your Shopify theme. When experimenting with a new navigation menu, you have numerous options depending on the specific aspects you wish to explore. Here, we’ll delve into ideas for enhancing your menu through a fresh [Layout and Organization](#layout-and-organization), reimagining its [Presentation and Styles](#presentation-and-styles), or experimenting with innovative [Wording](#wording).

#### Layout and Organization

If you're looking to test two different menus — one that directs visitors to all your collections through a single link and another that lists each collection individually — a great approach is to set up all the options you want to test on Shopify. Then, you can use our Onsite Editor to hide or show each option based on the menu you are evaluating.

Here's how you can achieve this:

1. On Shopify, go to **Online Store > Navigation**, and create a new menu through the **Add menu** option.
2. Create a menu containing all the sections that will be presented to both groups A and B:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F4XFMr7QgzJietV7RyVJd%2Fimage.png?alt=media&#x26;token=c1e64573-48d2-4881-82ae-61849c2a9a24" alt="" width="563"><figcaption></figcaption></figure>
3. Go to **Online Store > Themes**, and duplicate your current theme. We don't want to set up your live theme with the new menu quite yet, as all those options would be visible, so we will set everything up using a duplicate theme, which you can then publish when you turn on your test.
4. Next to the newly created theme, click on **Customize** to access the Theme Editor. Click on your theme's header, and change the current menu by the one you just created:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FZo8TKj6j5if340RrzDhC%2Fimg2.gif?alt=media&#x26;token=0c6524f1-b785-47a9-ae42-825411694797" alt=""><figcaption></figcaption></figure>
5. On Intelligems, create a new Content Test, selecting the type Onsite Edits (see [How to Set Up an Onsite Edits Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)). When you get to the final step, click on **Edit** next to **Content Edits**, then **Add & Edit Changes in Visual Editor**, and select the duplicate theme you created:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fq8h1c9b0exjVHvXeQ6Ei%2Fimg3.gif?alt=media&#x26;token=7333e846-f6b0-48be-b4e5-f2ba77f4ddce" alt=""><figcaption></figcaption></figure>
6. With Group A selected, enable the element selecting tool, then select each menu element that needs to be hidden for Group A, creating a replacement for each one. When selecting each menu element, make sure you're selecting the most outer portion of it, as this will ensure that we are targeting the correct portion of the menu that needs to be hidden. You'll hide each of these elements for Group A, while leaving them as originally set for Group B:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fz8sZIgwCcGSbJwk0sbQc%2Fimg4.gif?alt=media&#x26;token=dc42ebb0-f6a6-4f72-978e-53f2a7c3c821" alt=""><figcaption></figcaption></figure>
7. Repeat this for the elements that won't be visible to Group B, this time leaving them as originally set for Group A, and hiding them only for Group B. Make sure to **Save** your changes before closing the editor:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FhzaR34zQB9uFJMC9A3up%2Fimg5.gif?alt=media&#x26;token=e21e11b1-9566-43d2-ab40-1e773afc2c02" alt=""><figcaption></figcaption></figure>
8. As you switch between groups A and B in preview mode, you'll notice that the right menu elements are displayed for each test group.
9. Once you are ready to start your test, simply publish the duplicate theme that has the test menu in it, or set your live theme with that menu, then start the test on Intelligems. You'll want to make sure to keep the interval between these two actions as minimal as possible, so your visitors don't see all the menu options once the test menu is set on your live theme.

{% hint style="info" %}
If you are using [Audience Targeting](https://docs.intelligems.io/general-features/targeting/audience-targeting) to run this test only for a subset of visitors, make sure you use **Advanced Targeting**, setting up a condition so, if the visitor doesn't meet the audience's criteria, they get assigned to your control group, and select the option to exclude them from Analytics. This will ensure that they see your default menu instead of all the menu items. For example, if you wanted to target Desktop visitors only, this is how you would set this up:

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FbRMXXLDZig0IEgueV2pV%2Fimage.png?alt=media&#x26;token=86249d13-f506-47f5-8748-67ae8d23f1d8" alt="" data-size="original">
{% endhint %}

#### Presentation and Styles

Perhaps you are happy with the options presented on your menu, but you want to test the ways your visitors perceive it. You can easily inject custom styles into your test, having an alternative presentation for your test group, without needing to make any theme modifications, as outlined below:

1. On Intelligems, create a new Content Test, selecting the type Onsite Edits (see [How to Set Up an Onsite Edits Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)).
2. Load your test's preview, access the Onsite Editor, and go into editing mode.
3. Click on the "\</>" icon to open the Global CSS / JS editor:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F1Y22rm0UyxXgDPV0Tdf3%2Fimg6.png?alt=media&#x26;token=a637d91e-7af1-4baa-9284-17dfef6b31d2" alt=""><figcaption></figcaption></figure>
4. In the Group selector, switch to your test group, then add in your custom CSS that targets and modifies the elements on your navigation menu. This will be CSS that you've written yourself, with the help of a theme developer, or an AI generating tool, for example:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FNe9A77O9NeykcTvhxFph%2Fimg7.png?alt=media&#x26;token=caa58b40-167b-4d70-93d8-66b2a262800d" alt=""><figcaption></figcaption></figure>
5. Make sure you click **Apply** on the editor, and then **Save** on our widget.

#### Wording

Changing labels can often enhance the understanding of the underlying content and boost client engagement with specific sections of your menu. Here's how you can test simple text adjustments to your existing menu items:

1. On Intelligems, create a new Content Test, selecting the type Onsite Edits (see [How to Set Up an Onsite Edits Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)).
2. Load your test's preview, access the Onsite Editor, and go into editing mode.
3. Click the button on the bottom-left to **enable element selecting**:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FGfVu3OY4P4pH467yaYpO%2Fimg8.png?alt=media&#x26;token=81984678-949b-46e1-8c70-4b37cfbea6b7" alt=""><figcaption></figcaption></figure>
4. Click on the menu item you wish to test, then **Edit Text**:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FkBwZE58XIwAHkQla4fRi%2Fimg9.png?alt=media&#x26;token=c831e8ff-c7b2-47a3-a2eb-3557650e1383" alt=""><figcaption></figcaption></figure>
5. Make no changes for Group A (Leave as is). For Group B, add in the text that should replace the original text:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FLH4756KCM21AI6bevhkj%2Fimg10.png?alt=media&#x26;token=e6667e42-13cf-4831-bb18-858ef785c3e0" alt=""><figcaption></figcaption></figure>
6. Make sure you click **Done** on the editor, and then **Save** on our widget.

***

## Additional Suggestions

The methods for testing a navigation menu aren't limited to those mentioned above. With the various resources available through Intelligems, there are several other ways you can set up your test, depending on the specific changes you want to evaluate:

* If you want to redirect visitors to certain pages when they click on a given menu link, you can create a [Split URL Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test) rather than make changes directly to your menu.
* If you want to modify your menu without creating new menu items on Shopify, and you have a developer to assist you with front-end coding, you can use our [JavaScript injection capabilities](https://docs.intelligems.io/general-features/css-and-javascript-injection), adding custom JavaScript to the test group to programmatically modify your menu.


# Testing Checkout Blocks

Test components on Checkout created through the Checkout Blocks app in Shopify

{% hint style="info" %}
You can now use Intelligems to power and test Checkout Experiences like trust badges, guarantees, and custom content in your checkout. Learn more about [testing-checkout-experiences](https://docs.intelligems.io/checkout/testing-checkout-experiences "mention")
{% endhint %}

### Introduction

Testing elements on the Checkout page is a functionality that many stores have been longing for. While Shopify still doesn't allow changes to their native components by 3rd party apps, stores on the Shopify Plus plan have access to the [Checkout Blocks app](https://apps.shopify.com/checkout-blocks), through which you can add custom blocks to checkout that can be controlled through an A/B Test in Intelligems.

### How It Works

The concept is straightforward: create blocks conditioned by a **cart attribute**, then use Intelligems' [JavaScript injection](https://docs.intelligems.io/general-features/css-and-javascript-injection) capability to set up a Content Test that controls the display of the checkout block for each test group.

See the example below for how you can test a block that **allows your customers to edit their items on Checkout**.

### Setup Instructions

#### Step 1: Create a Checkout Block

In the [Checkout Blocks app](https://apps.shopify.com/checkout-blocks), click on 'Blocks', then 'Create block'. In this example, we'll be selecting the 'Line item edit' block:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FPQIvFmO0qhRSNDSsyyO6%2F01%20-%20create%20block.gif?alt=media&#x26;token=09e0bd57-6721-4501-8e97-7d3e28f61b1a" alt=""><figcaption></figcaption></figure>

#### Step 2: Set up a Display Rule

The block will be conditioned to a cart attribute set through the test on Intelligems. Under 'Display Rules' click on 'Add display rule' and select 'Cart attributes'. Next, set 'Key' as '\_igShowBlock' and 'Value' as 'true':

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FNheAADXqHZiIeROL6tZ2%2F02%20-%20set%20attribute.gif?alt=media&#x26;token=ba3b8b65-c057-4313-a620-4b152c37d34c" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The key/value pair configured at this step is arbitrary. You can set a different attribute key and value if you like, as long as that matches the key and value you'll be setting up through your test.
{% endhint %}

#### Step 3: Activate your block and add it to Checkout

Follow the instructions on the Checkout Blocks apps to activate your newly created block and add it to Checkout. Once the block is active, you'll open the Checkout editor, click the '+' icon next to 'Line item edit', and add it to the 'Information' section. Make sure to 'Save' your changes:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F2PGTRiam0n71go54T3cI%2F03%20-%20add%20to%20checkout.gif?alt=media&#x26;token=0e32eeab-e630-46d7-bcba-a58e23c00adc" alt=""><figcaption></figcaption></figure>

When viewing your Checkout sections, you'll locate the block under 'Order summary > Items in cart'.

{% hint style="info" %}
In the editor, if you click on your newly added block, you'll see a few customization options, such as the button's styles and label.
{% endhint %}

You may now close the editor and go back to the Checkout Blocks app, where you'll close the popup where the editor steps are listed, and mark that step as done. Your block is now active, and you can proceed with the next steps on Intelligems:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F6LisOiRDvdcKuDf9CofP%2F04%20-%20mark%20as%20done.gif?alt=media&#x26;token=d5dcc9f3-1edf-464d-a6b5-c72f73cc2ef6" alt=""><figcaption></figcaption></figure>

#### Step 4: Create an Onsite Edits Test with a Javascript injection

On Intelligems, create a Content Test of the type 'Onsite Edits Test' (you may refer to the steps [here](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)), with two test groups - in this example, we will call the groups 'Block OFF' and 'Block ON':

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FoncC8v9maEQOia2VAZ0y%2Fimage.png?alt=media&#x26;token=94dd43ef-1063-4ee0-ab0a-67515ab78442" alt="" width="563"><figcaption></figcaption></figure>

Move on to the 'Modifications' tab, and expand the section 'Styles & Javascript'. Within it, switch to the 'Javascript' tab, and paste the following code for the group 'Block OFF':

```
const res = fetch("/cart/update.js", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    attributes: {
      '_igShowBlock': "false"
    },
  }),
})
```

Additionally, switch the setting 'Javascript Injection Timing' to 'Delay', with a value of '2500 ms'. This will ensure that the Javascript runs correctly across different devices and browsers, as we noticed some devices and browsers require this extra delay.

Here's a quick video on the steps you'll be taking:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FbJgZxhs4iyjtZIjPfArj%2Fcb-update-01.gif?alt=media&#x26;token=5b8a5a12-a1e3-4a09-81e6-c3e1a5eb1614" alt=""><figcaption></figcaption></figure>

Next, switch over to the group 'Block ON', and add the same code, but this time change the attribute's value from 'false' to 'true'. Also remember to set the 'Delay' to '2500 ms'. You may now 'Save' the test:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FG25RKUd0ujb24SD4fMk1%2Fcb-update-02.gif?alt=media&#x26;token=ae4981fd-2b42-46a4-85e3-fdb54f5f8543" alt=""><figcaption></figcaption></figure>

The code above will run for each test group, and add the '\_igShowBlock' attribute to the cart. In the group 'Block OFF', having the attribute's value set to 'false' will ensure that it is not displayed for visitors in that group. For the group 'Block ON', the attribute's value will be set to 'true', ensuring its display rule is met, so visitors in that group see the 'edit' option on Checkout.

#### Step 5: Preview your test

You can now preview your test the same way you preview any other Content Tests. Simply open the test's preview, add a product to the cart, and proceed to the Checkout page. As you switch test groups in the preview widget, the Javascript injected for the group will run, updating the value of the '\_igShowBlock' attribute in the cart and determining whether or not the block on Checkout will be displayed:

{% embed url="<https://www.loom.com/share/0b532524682c4b769aeeae2f6a1d7152>" %}

***

### Other Block types

The Checkout Blocks app offers various block types you can test:

* **Product Upsells**: Test additional product recommendations
* **Dynamic Content**: Test personalized checkout messaging
* **Custom Fields**: Test additional information collection
* **Promotional Blocks**: Test discount or shipping messaging
* As long as you set a **Display Rule** on your block, as done in Step 2 in this guide, you can test any checkout block type using the same methodology described above!

### Best Practices

* **Test one block at a time** to isolate the impact of each element
* **Monitor key metrics** like conversion rate and cart abandonment
* **Use sufficient sample sizes** for statistically significant results
* **Consider mobile experience** when testing checkout blocks
* **Set appropriate test duration** based on your traffic volume

### Measuring Success

Track these key performance indicators:

* Checkout conversion rate
* Cart abandonment rate
* Average order value
* Time spent on checkout page
* Customer satisfaction scores&#x20;


# Tariff Testing: On vs Off

### About Intelligems Tariff App

Intelligems has created a dedicated [Tariff Support app](https://apps.shopify.com/tariff-support-by-intelligems) to help merchants navigate the complexities of tariff implementation. We recognize that tariffs can be incredibly painful and completely change the viability of brands. We believe in transparent pricing - you can seamlessly break out tariff charges on your products. These are transparent to your customers so they know exactly how much they're paying and why.

#### **Key Features:**

* Choose which products to show a broken out tariff charge
* Configure the percentage of your tariffs
* Use advanced targeting and conditions to manage who sees it

### Introduction

Testing tariffs on versus off allows you to measure the impact of tariff fees on customer behavior and conversion rates. By comparing user experiences with and without tariffs enabled, you can understand how tariff costs affect purchasing decisions, cart abandonment rates, and overall revenue. This A/B testing approach helps you make data-driven decisions about tariff implementation and pricing strategies.

### Setup Instructions

#### Step 1: Install and Configure Tariff App

1. Install the Tariff App [here](https://apps.shopify.com/tariff-support-by-intelligems)
2. Configure tariff settings for your products

#### Step 2: Create an Onsite Edits Test with a Javascript injection

In Intelligems, create a Content Test using the 'Onsite Edits' test type with two test groups. For this example, we'll name the groups 'Tariffs Off' and 'Tariffs On':

**Disabled Group (Control)**

Add this JavaScript snippet as a JS injection to disable tariffs for the control group:

```javascript
void fetch("/cart/update.js", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    attributes: {
      enableTariffs: false,
    },
  }),
});
```

**Enabled Group (Variant)**

Add this JavaScript snippet as a JS injection to enable tariffs for the test group:

```javascript
void fetch("/cart/update.js", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    attributes: {
      enableTariffs: true,
    },
  }),
});
```

{% hint style="success" %}
The only difference between the two code snippets is the `enableTariffs` attribute value:

* **Disabled Group**: `enableTariffs: false`
* **Enabled Group**: `enableTariffs: true`
  {% endhint %}

### Best Practices

* **Run the test for sufficient duration** to gather statistically significant data
* **Monitor key metrics** like conversion rate, average order value, and cart abandonment
* **Consider seasonal factors** that might affect tariff sensitivity
* **Test with different product categories** to understand varying customer responses
* **Document your findings** to inform future pricing and tariff decisions

### Measuring Success

Track these key performance indicators:

* Conversion rate comparison between groups
* Cart abandonment rates
* Average order value
* Revenue per visitor
* Customer feedback and satisfaction scores

Use these insights to optimize your tariff strategy and improve the overall customer experience.


# Testing Express Payment Options

### Introduction

Testing whether to offer express payment options (like PayPal, Klarna, Afterpay, etc.) on your checkout page can be done using Intelligems with [Shopify Checkout Blocks](https://apps.shopify.com/checkout-blocks). Because the Shopify Checkout Block app is only available for brands on the Shopify Plus plan, this type of test is only possible for brands on Shopify Plus.&#x20;

### Setup Instructions

#### Step 1: Create an Onsite Edits Test

In Intelligems, create a Content Test using the 'Onsite Edits' test type with two test groups (or more if you are hoping to test multiple variations). For this example, we'll stick with two groups and name the groups "Express Payment On" and 'Express Payment Off". You'll save the test without creating any onsite edits - this test essentially gives you the ability to split your traffic into two test groups and track the results.

#### Step 2: Copy your Test Group's Test ID

You can find this information by clicking on the three dots in the top right of your test > Show Info > clicking on the 12 digit ID next to the line that says "Express Payment Off For Google Analytics:".

#### Step 3: Configure your Checkout Block

1. Head to the Checkout Block app in Shopify and select the "Functions" option from the left hand nav
2. Click "Create Function" in the top right, followed by "Hide" under "Payment"
3. Choose "Create from blank template"
4. Give your Function a title, and choose "Cart rules" under "Type"
5. Click "Add method", select which payment method(s) you'd like to hide from the dropdown, and click "Add rule"
6. Select "Cart attributes", set the "Key" as "igTestGroups" and paste the ID you copied from the Intelligems app in the Value field
7. Save your new Function and set the status to "Active" - it will only hide the payment method(s) when it finds the test group ID associated with your test group in the cart, which will not happen until you preview or start your test&#x20;

{% embed url="<https://www.loom.com/share/f765433e1b2447f7b671b5f38d54d00d?sid=84698a8c-cf66-4312-b5b6-e11f5590d274>" %}

#### Step 4: Preview your Test

Preview your test like any other Content Test. Open the test preview, add a product to cart, and go to checkout. When switching test groups in the preview widget, empty your cart to ensure the correct Cart Attribute controls express payment display.

### Best Practices

* **Test one item on the checkout page at a time** to isolate the impact of each element
* **Monitor key metrics** like conversion rate and cart abandonment
* **Use sufficient sample sizes** for statistically significant results
* **Set appropriate test duration** based on your traffic volume

### Measuring Success

Track these key performance indicators:

* Checkout conversion rate
* Express payment usage
* Cart abandonment rate
* Average order value


# Offer Test Common Use Cases

Offer testing is a powerful strategy because it allows businesses to identify which promotions, discounts, or incentives most effectively attract and convert customers. By experimenting with different types of Offers, companies can assess the impact on customer behavior, sales volume, and profitability. This helps fine-tune marketing efforts, ensuring that the right balance of value is presented to customers without sacrificing margins. Offer testing provides actionable insights, reduces the risk of ineffective promotions, and maximizes revenue by tailoring offers to what truly motivates consumers.

Check out the below common test designs for inspiration on how to get started:

{% content-ref url="offer-test-common-use-cases/the-volume-discount-duel" %}
[the-volume-discount-duel](https://docs.intelligems.io/getting-started/common-use-cases/offer-test-common-use-cases/the-volume-discount-duel)
{% endcontent-ref %}

{% content-ref url="offer-test-common-use-cases/gifting-games" %}
[gifting-games](https://docs.intelligems.io/getting-started/common-use-cases/offer-test-common-use-cases/gifting-games)
{% endcontent-ref %}


# The Volume Discount Duel

[Experiences](https://docs.intelligems.io/personalizations) allow you to serve specific discounts and offers to your site visitors. One of these types of Offers is a Volume Discount. While you can have such an Experience on all the time, Intelligems can also help you test which thresholds and discounts drive the most value.

You can do this by setting up an [Offer Test](https://docs.intelligems.io/offer-experiences/testing-offer-personalizations).

*What this test design might look like:*

<table data-header-hidden><thead><tr><th width="203"></th><th></th><th width="215"></th><th></th></tr></thead><tbody><tr><td></td><td><strong>Control Discount</strong></td><td><strong>Higher Discount</strong></td><td><strong>Lower Discount</strong></td></tr><tr><td><strong>Product A</strong></td><td><p>15% off $100 or more</p><p>20% off $150 or more</p><p>25% off $200 or more</p></td><td><p>20% off $100 or more</p><p>25% off $150 or more</p><p>30% off $200 or more</p></td><td><p>10% off $100 or more</p><p>15% off $150 or more</p><p>20% off $200 or more</p></td></tr></tbody></table>

{% hint style="info" %}
We recommend taking a look at a histogram of your order values for the last month (or more) when deciding what Volume Discounts to test, especially if Volume Discounts will be a new addition to the site. For example, if a majority of your orders come in around $100, you may not want to provide a discount for orders over $100, but rather start around $150.
{% endhint %}


# Gifting Games

Offers allow you to serve specific discounts and offers to your site visitors using. One of these types of Offers is a Gift With Purchase. While you can have such an Experience on all the time, Intelligems can also help you test which thresholds and gifts drive the most value.

You can do this by setting up an [Offer Test](https://docs.intelligems.io/offer-experiences/testing-offer-personalizations).

*What these test designs might look like:*

<table data-header-hidden><thead><tr><th width="197"></th><th width="281"></th><th width="331"></th></tr></thead><tbody><tr><td></td><td><strong>Control Group</strong></td><td><strong>New Group</strong></td></tr><tr><td><strong>First Test - On vs. Off</strong></td><td>No Gift With Purchase</td><td>Gift Provided at $100 Threshold</td></tr><tr><td><strong>Second Test - $100 Threshold vs. $150 Threshold</strong></td><td>Gift Provided at $100 Threshold</td><td>Gift Provided at $150 Threshold</td></tr><tr><td><strong>Third Test - Gift A vs. Gift B</strong></td><td>Gift A Provided at $100 Threshold</td><td>Gift B Provided at $100 Threshold</td></tr></tbody></table>

{% hint style="info" %}
We recommend taking a look at a histogram of your order values for the last month (or more) when deciding what threshold to provide a Gift With Purchase at, especially if this will be a new addition to the site. For example, if a majority of your orders come in around $100, you may not want to provide a gift for orders over $100, but rather start around $150.
{% endhint %}


# Best Practices

Tips for getting the most out of Intelligems.

Following best practices for A/B testing is crucial to ensure the reliability and validity of your results. Check out the articles below for best practices when it comes to designing your tests, and while your tests are running.

{% content-ref url="best-practices/test-design-best-practices" %}
[test-design-best-practices](https://docs.intelligems.io/getting-started/best-practices/test-design-best-practices)
{% endcontent-ref %}

{% content-ref url="best-practices/best-practices-during-a-test" %}
[best-practices-during-a-test](https://docs.intelligems.io/getting-started/best-practices/best-practices-during-a-test)
{% endcontent-ref %}


# Test Design Best Practices

We want you to get the most from the tests you run with Intelligems! See below for our suggested best practices for designing solid tests.

## Create a Testing Roadmap

We recommend creating a testing roadmap as you complete onboarding with Intelligems. Major factors to consider when creating a test roadmap include:

* **Define Clear Objectives:** Before launching an A/B test, identify what you aim to achieve. Whether it's increasing the conversion rate, reducing cart abandonment, or improving click-through rates on product pages, having a clear objective helps in designing the test and measuring its success accurately. A few examples:
  * For businesses with lower margins, an increase in revenue can have a dramatic effect on bottom line.
  * Similarly, for businesses with higher margins, a small change in conversion can significantly boost total profit.
  * Businesses that are early on in their journey may be more focused on increasing conversion rates right away.
* **Intuition or Customer Feedback:** Combine your business objectives with your intuition or customer feedback and use Intelligems tests to confirm and quantify potential changes to your merchandising strategy.
* **Get Creative:** Many test types are possible with Intelligems.
* **Test Timing:** Plan for each test to take about 3 to 4 weeks. We recommend running each test for at least one week to capture any changes in customer behavior related to day of the week. We also recommend running each test for no longer than five weeks due to increased risk of device switching / cache clearing.
  * We typically recommend running a test until each group has 200-300 orders to start to see significant results. Use this rule of thumb as a way to estimate the amount of time required to run each test.
* **Test Frequently:** Market conditions and consumer behavior change frequently. Test new hypotheses and run experiments frequently to make sure you're maximizing your store's potential at all times.
* **Determine Stat Sig before starting the test**: you should focus on the probability that indicates one of your test groups outperforms the control. While we suggest reaching 300 orders per test group, actual requirements can vary depending on the nature of the change and the desired confidence threshold. For example, a higher confidence threshold will require more data than a lower threshold. More importantly, larger changes typically yield results more quickly than subtle adjustments. If you're testing a change that's a small risk to implement and easy to revert if needed, you may be comfortable with a lower threshold (e.g. 85%). If you're resting something more important and riskier, you may prefer a higher threshold (e.g. 90%).
* Before launching tests, **establish clear thresholds** for statistical significance, orders, visitors, and duration. Have a hypothesis and, upon concluding the test, assess whether results align with your expectations. If a test doesn't achieve significance within the expected timeframe, use the available data to make an informed decision, considering the change's risk and reversibility. You can read more about Stat Sig [here](https://docs.intelligems.io/analytics/determining-statistical-significance).

***

## Determining Traffic Allocations Between Groups

We generally recommend allocating traffic evenly between groups, other than in certain circumstances such as:

* You have already decided to change prices and want to hold back a small amount of traffic on prior prices
* You want to allocate most traffic to the control because of customer support concerns
* You have decided to remove allocation of new traffic to certain test groups part-way through the test
  * Note: Changing the allocation of test traffic during a test may result in skewed data. If you remove traffic from one group, we recommend scaling the other groups proportionally to their prior allocations

***

## Determining the Magnitude of Changes to Test

We recommend starting with broad changes and using results to narrow in on more refined tests. For instance, if you're testing:

* **Prices:** start with an 8-10% increase and decrease, simultaneously
  * If traffic allows, testing 3-4 groups simultaneously will yield more insightful data and will give you a sense of your products' elasticities
  * If conditions only allow you to test in one direction (i.e. decreasing prices isn't an option for your business), pick a few points in the direction you wish to test
  * Consider factors such as seasonality: for example, if you sell winter and summer products, running a site-wide price test may not make much sense, since results for those categories are probably very different at any given point in the year. You may focus on running the test over products that will yield more meaningful results.
  * Are products substitutable? If testing individual products, avoid changing the price of one product that could affect the results of a different product.
* **Shipping Rates / Thresholds:** start with an 8-10% increase / decrease, simultaneously

***

## Only Make One Change

* We recommend keeping the existing prices and configurations for the "control group" for the experiment to keep your baseline consistent.
* If there are unique aspects to how you merchandise your products (e.g. if you offer bundle discounts, welcome offers, or subscriptions), consider how these elements of your store might be affected by tests you want to run. In general, we recommend keeping these types of discounts as consistent as possible across groups so these variables do not create noise in the test.
* If you are running a content test, be sure to keep the change limited to one thing. If you change multiple elements in a single test, it'll be difficult to decipher what caused any performance changes.


# Best Practices During a Test

This article will take you through some best practices leading up to launch and while a test is live.

## QA'ing your Test (Before and Throughout the Test)

Before launching any new test, it is important to QA the test to ensure everything is working as you would expect. See our checklists below for more information on how to QA each type of test:

* [Price Test QA Checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist)
* [Shipping Test QA Checklist](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist)
* [Content Test QA Checklist](https://docs.intelligems.io/content-testing/content-test-qa-checklist)

We also recommend doing a sweep through the site immediately after starting the test, and at least every few days during the test to ensure nothing has changed that would affect the test (after all, sites change frequently). The best way to do this is in a **new** private or incognito window; this will get you assigned randomly to a new test group.

***

## Handling External Areas that Mention Price or Shipping Rates

We recommend thinking through any areas other than on your Shopify site that could create inconsistencies with the test. Where possible, we will do our best to integrate with these external sources, but in certain cases we may recommend removing these instances. Some examples include:

* **Advertisements:** It is often possible to keep test groups consistent with ad prices utilizing traffic selectors during test setup. Please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have questions on this!
* **Google Shopping:** Monitor your Google Merchant Center frequently throughout the test. We will do our best to work with you to minimize issues with your Google Shopping feed. We also recommend turning on automatic price updates in your Google Merchant Center. See [here](https://support.google.com/merchants/answer/3246284?hl=en) for Google's documentation on this feature.
* **A few other places to think about:** retargeting and newsletter emails, landing pages, affiliate marketing, social handles, PDP sections

***

## Theme Changes

It is generally recommended to avoid major theme changes while a test is live. Examples include:

* Major changes to theme code
* Changes to text that mentions price or shipping rates (relevant if the test utilizes the find-replace function)
* Installing or reconfiguring apps that are close to checkout (e.g. cart or upsell apps)

***

## Customer Experience

Pay close attention to customer experience issues that arise. While issues are rare, we always recommend keeping your customer support team in the loop on tests. Additionally, we recommend equipping the team with a discount code to honor lower prices in the rare occurrence that a customer sees multiple prices (for instance, on multiple devices).

***

## Monitoring Results

While it may take a while to start seeing significant results, we recommend checking the results in the Intelligems analytics dashboard frequently. This will help you discover any potential issues, and if necessary, can prompt you to end tests early if there's a material effect on conversion and profit.

***

## Iterate and Learn

A/B testing is an iterative process. Use the insights gained from each test to inform future tests. Document your findings and build on what you learn to continually improve your store’s performance.


# General FAQs

## Plan, Capabilities & Access FAQs

<details>

<summary>How much does Intelligems cost?</summary>

Intelligems offers monthly and annual pricing options to meet your organization's needs. Prices vary depending on your store's order volume, what type of tests you'd like to run, and how long you are planning to test with us. Please see our [pricing page](https://intelligems.io/pricing) for more information.

</details>

<details>

<summary>What eCommerce platforms does Intelligems integrate with?</summary>

Currently, Intelligems only supports Shopify stores. However, if you are on another platform and interested in using Intelligems, please [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)! We'd love to keep you updated if this changes in the future.

</details>

<details>

<summary>How long does Intelligems take to set up?</summary>

This depends on a few factors, including:

* What test type or types you are planning to run
* Whether you choose to integrate Intelligems on your own, or have the Intelligems team complete it on your behalf
* What version of Shopify you are on and how many other apps and customizations your store has

That said, if you choose to have Intelligems do the integration, our team typically completes it within 3-5 business days, depending on backlog. If you are starting with something simple like content testing, you can get up and running within about 30 minutes!

</details>

<details>

<summary>What types of tests can I run with Intelligems?</summary>

Intelligems enables organizations to test just about anything on their Shopify store, including themes, page templates, pages, other content, discounts, product pricing, shipping and more.

The types of tests that you can run depend on the plan that you are on, so we recommend checking out our [pricing page](https://intelligems.io/pricing) for a full look at what each plan includes. Please don't hesitate to [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions!

</details>

<details>

<summary>What kind of test should I start with?</summary>

The answer to this depends on your goals! If you are starting with price testing, most of our customers start off by testing the prices across their store or on their most popular product or collection as that will generate the fastest results and the most impact. When running a price test, we usually recommend testing both a lower and a higher price vs. the current price.

If you are more interested in testing around shipping, another popular strategy is to test various free shipping thresholds to see what finds the “sweet spot” of AOV and conversion rate.

You can see more test suggestions [here](https://docs.intelligems.io/getting-started/common-use-cases)!

</details>

<details>

<summary>Can I run multiple tests at once?</summary>

Technically, there is no limit to the number of parallel tests you can have running on Intelligems. Strategically, you run the risk of creating *interference* between your tests if they are running on similar things at similar times.

* For example, maybe you are testing pricing on a particular product while also testing the layout of the PDP. You may see these as two separate tests, but in reality customers are being exposed to both. So you end up with a combination of experiences that you don’t have full visibility into since visitors are being randomly assigned within each test.

To control for interference, you can:

1. Set this up as one large test. Make a group for each combination of variables so that you can properly measure and compare (a multivariate test). You **can** have multiple products in the same test, which would keep users in the same group across all products being tested.
2. Run tests sequentially, one after another
3. Use our [Mutually Exclusive Experiments](https://docs.intelligems.io/content-testing/targeting/mutually-exclusive-experiments) feature (beta). If you don't see this as an option in your test setup, please [contact us](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we'll enable it.

Exceptions: You can run tests in parallel if there is *not meaningful overlap in their impact to the customer experience.*

* For example, if you wanted to test a PDP layout for one product, and separately have a test running on a landing page for a completely different product and funnel - that should have minimal interference, as the customers won’t likely experience both.
* Or if you ran a pricing test on women’s underwear at the same time you were testing men’s overcoats - those are likely to be pretty distinct sets of customers who won’t be exposed to both tests.

Note: We do only allow *one shipping test at a time* for technical reasons.

</details>

<details>

<summary>Will Intelligems continue to function if I update to Shopify's One-page checkout?</summary>

Overall, yes. Intelligems will continue to function if you update to Shopify's One-page checkout! That said, the full answer depends on the type of test you are looking at:

**Price Test:** this will continue to work seamlessly! If you are on Shopify Plus, please ensure that your Line Item script still includes our Checkout Script. Note that hiding the added discount on the One-page checkout won't be possible, but we can customize the discount's name to your preference.

**Shipping Test:** Intelligems will continue to operate without issues.

**Content Test:** Running content tests on the One-page checkout isn't possible as it doesn't utilize the checkout.liquid file and doesn't allow third-party alterations. However, you can continue to run content tests on the rest of your site without any issues. You can read further about this [here](https://docs.intelligems.io/faqs/content-testing-faqs#can-i-test-the-new-shopify-checkout-vs.-the-old-shopify-checkout-or-test-specific-components-on-the).

</details>

<details>

<summary>Why does Intelligems need collaborator access to your store?</summary>

Intelligems may ask for Shopify collaborator access for a few reasons:

1. To complete the integration on your behalf. The integration requires a few theme changes or other Shopify configurations to be made, so we need access to your Shopify account to complete those.
2. To help troubleshoot. If something is not working as expected, it is helpful for our team to have access to your Shopify account to solve the issue quickly.
3. To take a look at your analytics. This helps us understand if there are an discrepancies with the data we have captured.

**Permissions Intelligems requires:**

* **Orders:** Necessary to track test impact data such as AOV, product mix, etc.
* **Products:** Necessary to find detail on products and variants that will be part of a test.
* **Apps:** Necessary to access Shopify Checkout Scripts, in addition to apps that may play a role in things like managing the cart, collections pages, reviews, etc., which need to be updated as part of a test.
* **Online Store Themes:** Necessary to duplicate a theme and update the code to integrate a test.
* **Settings & Locations:** Necessary to run shipping tests and install Intelligems as a third party rate carrier.

**Permissions Intelligems prefers to have:**

* **Discounts:** In general, we want to be aware of what discounts may be impacting products that are in the test. Note that this is required if we are duplicating products.
* **Customers/Reports/Dashboards:** Helpful to (a) check our data vs. historical data, and (b) confirm there are no discrepancies between the data we are presenting vs. what you see in Shopify.

**Permissions Intelligems does not request access to:**

* Apps developed for you
* Marketing / gift cards
* Edit Orders / Draft Orders

</details>

<details>

<summary>How can I add or remove users from my Intelligems account?</summary>

The easiest way to access Intelligems is directly through Shopify - you can find us by clicking on Apps in the left hand navigation menu -> searching for Intelligems and selecting our app. Anyone who has the permissions to access apps in Shopify should be able to log in that way - you can add users via the Shopify admin by going to Settings -> Users and Permissions -> Add staff. Be sure to give the user permission to manage Intelligems in the App permissions section. If you need to remove users from Intelligems, you can do so by removing that permission. Please see [Shopify's documentation](https://help.shopify.com/en/manual/your-account/staff-accounts/staff-permissions/staff-permissions-descriptions#apps-and-channels-permissions) for additional details.

In the rare case that you would like to provide a user access to Intelligems, but will not be providing them access to Shopify, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we can help get that set up.

</details>

<details>

<summary>I'm upgrading to Checkout Extensibility, is there anything I need to do to ensure Intelligems continues to operate correctly? And will current test results be impacted at all?</summary>

There are no additional steps you need to take to ensure Intelligems continues to operate as expected when upgrading to Checkout Extensibility.\
\
There'll be no impact to any test results, or any Content, Shipping, or Offers tests when updating.\
\
While there is no impact on price tests or their results, there *will* be a visible discount on the checkout page if using our Checkout Script to manipulate prices.\
\
To remove the discount, you'll need to upgrade to Shopify Functions.\
\
Please reach out to support for help with updating to Shopify Functions at <support@intelligems.io>

</details>

<details>

<summary>I'm changing my site's primary URL domain – what do I need to do in Intelligems?</summary>

As long as your Shopify Shop ID remains the same, the only change in Intelligems that you need to make will be updating your domain name in the settings page of the app. If additional changes are being made to the store that affect the Shop ID, please reach out to our Support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request). Please note that after a domain change all visitors to tests will be considered 'new' for targeting purposes, so we would recommend ending any ongoing tests and restarting them after the domain migration.

</details>

## Testing FAQs

<details>

<summary>Can I schedule tests to start, pause or end at a specific time?</summary>

Yes! Intelligems allows you to schedule start times for all types of tests, including Price, Shipping, Content and Campaigns. Intelligems also allows you to schedule pause and end times for Content and Campaigns tests, but does not currently support scheduling pause or end times for Price or Shipping tests due to rollout requirements for ending those types of tests.

To schedule a start, pause or end time, follow these steps:

1. Click on the More Options menu (the three dots) next to the test you'd like to set up a schedule for.
2. Click "Schedule Test". If you do not see this option, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to request this feature be turned on for your account!

   <figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252Fb1iV3NkWAvi1iCWgT722%252FScreenshot%25202024-04-05%2520at%25202.04.15%2520PM.png%3Falt%3Dmedia%26token%3Dc231fcef-f2b1-4bc8-b57c-8f9d856be711&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=9ed7787376137fbce7ca29d7716e4df4dc83811ffa53bf14eddc6d04a47b66a9" alt="" width="188"><figcaption></figcaption></figure>
3. If you are setting up a schedule for a test that has not yet been started, this will open a modal that will ask you to confirm that you have completed the integration & QA'd your test. If you have not already done so, please be sure to complete both of these items before proceeding.

   <figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252FJwGgBJ4bT4PXiWWVkql8%252FScreenshot%25202024-04-05%2520at%25202.06.27%2520PM.png%3Falt%3Dmedia%26token%3Dde83ed63-fb26-440b-8e73-170b8c4edab5&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=4a0d2e87a2412702919f5155c98fe4932a63889981c8f0670056415a789bc1fb" alt="" width="188"><figcaption></figcaption></figure>
4. Once you have confirmed those items are complete, you'll be taken to a modal where you can set up a scheduled start, pause, and/or end time.

   <figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252FPTOfvHS8CvqNwzUWv1XH%252FScreenshot%25202024-04-05%2520at%25202.07.20%2520PM.png%3Falt%3Dmedia%26token%3D68ee23c6-ae45-4e30-b280-b0089da0f41b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=eb9636b9e695b4376c8c2219ba36eb5275f620eff3905c74f38c564277d42454" alt="" width="188"><figcaption></figcaption></figure>

A few things to keep in mind as you set these up:

1. You must schedule items for times in the future only.
2. Test can only be scheduled at 5 minute increments.
3. The times will be based off of your device's current time zone, which will also be listed at the top of the modal.
4. You can only schedule pause and end times for Content and Campaign tests that are either live, or that have a scheduled start time.
5. Once you have scheduled a test to start, pause or end at a specific time, you'll see a clock symbol next to the status, and will be able to hover over that to get more information on the scheduled times like in the below screenshot.

   <figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252FKWt85JpzNEkCCzgg1y2X%252FScreenshot%25202024-04-05%2520at%25202.01.38%2520PM.png%3Falt%3Dmedia%26token%3Dc8b909a9-0938-4e8d-8fe3-bcfa395608b6&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f53e04bac5dbbd62ffeb94278f86eb116eb99a28cb541bf4ebba36c72416bd79" alt="" width="188"><figcaption></figcaption></figure>

</details>

<details>

<summary>Can I restart a test that I accidentally ended?</summary>

The Intelligems Support Team can help set your ended Content, Price or Offer test back to a paused status, which will allow you to resume the test. We are not able to restart shipping tests due to technical reasons. Please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for help with this!

</details>

<details>

<summary>How long does it take to run a test? When should I end my test?</summary>

Determining how long to run a test relies on 3 major things:

1. How big is the effect of this change? The smaller the effect, the harder it is to detect and be certain that the result is not just noise.
2. How many people visit your website every day, and more specifically, how many orders are being placed in a day?
3. How confident do you want to be? The more confident you want to be, the more data you need.

***Our rule of thumb is that if you want to detect a 10% change in conversion with 90% confidence, you need about 300 orders per group.***

* Smaller changes will likely require more data to pick out the signal from the noise
* Larger changes will likely require less data to see a significant pattern

Here are the steps we recommend you take when your test goes live to monitor results and determine when to end the test:

1. Always check in on your test after \~4 hours to make sure your data is flowing - this can be a helpful time to catch any errors in the test configuration (don't launch a test end of day on a Friday, when you won't be able to monitor it)
2. Try not to end any tests before a full week. This allows you to observe a mix of weekdays and weekends, and early results often change.
3. Take a look at the "Trend" tab in the Intelligems analytics dashboard. Have those charts shown consistent results, or are they still varying from day to day? If there is still a lot of variability, it may make sense to run the test for a few more days.
4. Once a week has passed, you can check the “statistical significance” tab to get a read on the “probability to be best” for each group. Check out our [article on statistical significance](https://docs.intelligems.io/analytics/experiment-analytics/statistical-significance) to understand what you are looking for here!
5. You should have a risk tolerance in your head.

* You can wait for everything to hit 95 or 99% confidence, but for smaller brands, that means a lot of time waiting around for results. Waiting around presents a big *opportunity cost* since you are not running other tests - which could be delivering more value! - during that time
* We wouldn’t recommend making decisions with less than 75% confidence
* Many of our customers look for confidence somewhere around 90%

Some tests will not ever hit confidence - they’ll waffle around in the 40-60% range - that means there is *no real difference between the versions*. At that point, pick one to move forward with based on intuition or other strategic considerations, and move on

***Pro tip***: you’re able to change traffic allocation in the middle of a test. So if you have one group that is a clear loser, you can “shut it off” in the middle of your test and send more traffic to the more viable options.

</details>

<details>

<summary>How do I edit something in a live test?</summary>

There are a few steps to safely edit your live test:

**Step 1: Pause your test.**

The pause button can be found next to the status column within your `A/B Tests` overview tab.

*If you are pausing a shipping test,* we will automatically restore your shipping profiles while the test is paused.

*If you are pausing a price test,* we will ask you to select which prices you would like to roll out while the test is paused.

**Step 2: Make your edits.**

The edit button can be found under the three dots to the right of your test. Select this and make any changes you need, such as adding a new product, removing a test group (you can do this by allocating 0% of traffic to that group), changing a price, or changing a shipping rate. Make sure you click through the entire edit flow and select the save button at the end to save your changes!

**Step 3: Resume your test.**

Now that you've made your edits, you can resume your test and keep getting results! The button to do so is right next to the test status.

Keep your edits in mind when looking at the analytics dashboard if the change may have affected the results. Once a test has started, test group names cannot be changed and you can no longer add/remove test groups, but you can set traffic to 0% for a group to effectively remove that group from the test. We do this so that analytics are maintained for that old group that now has no traffic going to it. You can filter your results by date to see the results before and/or after edits were made.

</details>

<details>

<summary>How does the test status work in the test dashboard?</summary>

There are several different statuses that a test can have:

1. Pending: You've set this test up, but have not yet started it.
2. Gathering Data: You've started this test within the last 21 days.
3. Ready For Analysis: This test has been running for at least 21 days. While this is a good baseline, there is ultimately no general rule on time. That said, we often start seeing significant results after about 300 orders *per group*.
4. Paused: You've paused this test; it is not active on the site, but you can resume it.
5. Ended: You've ended this test.

</details>

<details>

<summary>What will my orders look like in Shopify?</summary>

Customers on your site will not see anything to indicate that an Intelligems test is running, but there are a few ways that Intelligems will show up on orders within your Shopify admin portal:

1. Each visitor gets tagged with a unique id that sorts them into a group. This id is passed to the order via [cart.attribute](https://shopify.dev/api/liquid/objects/cart) for tracking purposes and will show under “Additional Details” on the order page. This is hidden from the customer. If this causes any issues for your order forms, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we are able to remove this.
2. We also add each user's test group IDs to the order via [cart.attribute](https://shopify.dev/api/liquid/objects/cart) for tracking purposes and will show under “Additional Details” on the order page. This is hidden from the customer.
3. For Price Testing, we add a line\_item.property to each item equal to the price of that item for that customer. In most cases, this Line Item Property will be titled "\_igp". This is hidden from the customer.
4. For Shipping Testing, we add a line\_item.property to each item equal to the test group ID so that we are able to provide the correct shipping rate for their test group. This is hidden from the customer.
5. If you are using our Checkout Script integration for Price Testing, the Checkout Script applies a “[line-item discount](https://help.shopify.com/en/manual/sell-in-person/shopify-pos/discount-management/line-item-discount)” in order to generate the correct price for a customer’s product. While this shows as a discount in the admin view, this is always hidden from the customer (i.e. in this case they would just see “$13.99” for the product price).

Here is an example of what an order would look like in Shopify:

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FS8EFFHGl7wkrKelgagGH%2FScreenshot%202025-02-14%20at%2010.16.21%20AM.png?alt=media&#x26;token=e5255e3b-4a1b-4b71-8212-5908fe6817fa" alt="" data-size="original">

</details>

<details>

<summary>Why does the "Additional Details" section on my Shopify orders contain a random string of numbers &#x26; letters that starts with "ig_"?</summary>

That is the Intelligems ID that we have assigned to that user as this is what allows us to track the visitor and their activity. We add it as a cart attribute (if you look at an order's JSON on Shopify, its the field ​`note­_attributes`​) - this is something that many apps do when they need to add extra information to an order.

In most cases, this additional note should be harmless. However, if it is impacting another software that you use (such as a fulfillment software), Intelligems only needs the Intelligems ID to be there on order creation - we do not need it to *remain* on the order. Because of this, you can set up a [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) to remove it, and that would fix the problem while retaining the data for Intelligems.

</details>

<details>

<summary>What happens while a test is paused?</summary>

Visitors who were already part of a test group won't see the content of that test while its paused, but they will remain in the same test group. When the test is unpaused, they will resume seeing the test content. This is true for all test types.\
\
Conversions that take place during a paused period never count even if the test is later unpaused.

</details>

<details>

<summary>Will testing through Intelligems affect my SEO?</summary>

No, Intelligems' tests do not impact your store's SEO. Our platform is designed to run tests without affecting search engine rankings or visibility.

We detect all major bots and will block execution when one is detected - this ensures that the bot will see the page *without* intelligems running, which avoids SEO impact. For Price Tests, it also means the bots will see the price of the item as listed in Shopify and not a particular test group.

</details>

<details>

<summary>Can I test across domains or stores?</summary>

**No, Intelligems does not currently support testing across multiple domains, or multiple Shopify stores.** Each test is limited to a single domain and store where the [Intelligems script](https://docs.intelligems.io/getting-started/updating-the-intelligems-script) is installed - you can find which domain this is and update it if needed on the [settings page](https://app.intelligems.io/settings) in the Intelligems app. Please note that after a domain change all visitors to tests will be considered 'new' for targeting purposes, so we would recommend ending any ongoing tests and restarting them after the domain migration.

#### Current limitations:

* Tests can only run on the domain configured on the Intelligems settings page - this domain must be associated with the Shopify ID you are installed on
* Visitor assignments and tracking do not persist across different domains
* Results cannot be aggregated from multiple domains within a single test

#### Alternative approaches:

* **Use subdomains** instead of separate domains when possible (e.g., shop.yourbrand.com vs yourbrand.com)
* **Focus on single-domain user journeys** to get meaningful test results

</details>

## Integration FAQs

<details>

<summary>What analytics platforms does Intelligems integrate with?</summary>

While Intelligems' analytics dashboards are quite robust, we also currently have an [integration with GA4](https://docs.intelligems.io/analytics/google-analytics-4-integration) if you prefer to take a look at your testing data there. Additionally, we have [integrations with several heatmapping tools](https://docs.intelligems.io/developer-resources/heatmap-integrations), including Microsoft Clarify, Heatmap.com and Hotjar. You can enable these integrations in the [integrations tab](https://app.intelligems.io/integrations) in the Intelligems app!

</details>

<details>

<summary>What page builders does Intelligems integrate with?</summary>

Intelligems has experience integrating with various page builders for different types of testing. Below are some specific page builders our brands have tested with, along with details on the integration requirements for each. If you are using a page builder that is not listed below, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions on integrating with those pages!

1. **Replo:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file. If there are any files in the layout for Replo, our script should be added there as well. If you will be Price Testing, please follow [this guide](https://docs.intelligems.io/getting-started/pricing-integration-guides/replo-page-builder) to integrate your Replo pages - this step is not necessary if you will only be content testing.
2. **Gempages:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Gempage layout files. These pages are also compatible with Price Testing, and should be integrated by following [these steps](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices) - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you need help completing this.
3. **Shogun:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Shogun layout files. These pages are also compatible with Price Testing, and should be integrated by following [these steps](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices) - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you need help completing this.
4. **Pagedeck:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Head Scripts section in the Pagedeck app. These pages may not be compatible with Price Testing - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are interested in testing prices on a Pagedeck page so we can help scope this out!
5. **PageFly:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the PageFly layout files. These pages may not be compatible with Price Testing - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are interested in testing prices on a PageFly page so we can help scope this out!
6. **Funnelish:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Custom CSS / JS > Head HTML section in the Funnelish app. These pages may not be compatible with Price Testing - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are interested in testing prices on a Funnelish page so we can help scope this out!
7. **Webflow:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Webflow layout files. These pages may not be compatible with Price Testing - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are interested in testing prices on a Webflow page so we can help scope this out!
8. **Fermat:** Typically works out of the box for Split URL Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Fermat layout files. These pages are not currently compatible with Price Testing.
9. **Builder.io:** These pages are typically built using the Storefront API, which is Headless & can cause complexities. If you are using Builder.io, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to discuss what will be possible.

</details>

<details>

<summary>What cart apps does Intelligems integrate with for Price Testing?</summary>

Intelligems has experience integrating with various cart apps for different types of testing. Below are some specific cart apps our brands have tested with, along with details on the integration requirements for each. If you are using a cart app that is not listed below, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions on integrating with that app!

1. **Rebuy:** Rebuy works with Price Testing out of the box. Prices of products that have been added to cart will be updated via a Checkout Script, Shopify Function or Duplicate Product, depending on which integration you are using. If you are using Rebuy upsells in your cart, those prices will need to be [tagged](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices) in order to be updated correctly. If you have any questions on this, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
2. **Monster Cart Upsell:** Monster Cart Upsell is not compatible with Checkout Scripts - because of this, if you are using this cart app, you are only eligible for our Duplicate Product integration. If you have any questions on this, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
3. **UpCart:** UpCart works with Price Testing out of the box. Prices of products that have been added to cart will be updated via a Checkout Script, Shopify Function or Duplicate Product, depending on which integration you are using. That said, there are two limitations when using UpCart:
   1. Compare prices, discount tags, discount percentages & line item properties must either be hidden or shown incorrectly as UpCart does not allow Intelligems to manipulate these items
   2. You will not be eligible for our Checkout Script integration
4. **Slide Cart by AMP:** Slide Cart by AMP does require a few extra integration steps to hide the strikethrough prices & discounts - our guide on these steps can be found [here](https://intelligems.notion.site/Integrations-Slide-Cart-by-AMP-854ccb8e6b024c9d9770d41be78727a2?pvs=4). If you have any questions on this, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!

</details>

<details>

<summary>I see an error associated with Intelligems under "Checkout Rules" — what does this mean?</summary>

You may see an error under Intelligems' checkout extension that says, "There were errors during checkout. Some customers have abandoned checkout."

This indicates there was at least one recent error in processing that may have caused an issue in completing checkout. While this of course sounds concerning, almost always, there were no issues encountered by real customers.

Many Shopify stores are visited by automated bots that scrape various data, including product inventory. One of the ways they record inventory data is to add very large numbers of each product to cart and attempt to checkout until they get out of stock errors. These large carts, often containing nearly the entire product catalog, can cause timeouts from the Intelligems function that show up here.

If you'd like Intelligems to investigate the errors, please [share error reports](https://shopify.dev/docs/apps/build/functions/monitoring-and-errors#sharing-an-error-report) with Intelligems through the Shopify admin, then [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we'll review the logs.

</details>

## Preview FAQs

<details>

<summary>Can I preview a Shopify theme and Intelligems test at the same time?</summary>

Yes, you can! This is a very common practice we use here at Intelligems. You can do this by entering preview mode for your theme and then entering preview mode for your test. The theme should be cached when you open your test preview.

</details>

## Traffic FAQs

<details>

<summary>How does Intelligems split the traffic and keep users in the same test group for the entirety of the test?</summary>

All of our tests are run as true split tests where we segment your traffic in real time between test variants. Intelligems randomly assigns users to a test group when they visit your site for the first time during a test.

Intelligems then saves a unique string of numbers and letters know as the Intelligems ID in a first-party cookie, which we then use to remember your site visitors and keep them in the same test group(s) for the entirety of your test(s). Because of this, every time they come back to the site on the same browser on the same device, the user will have a consistent experience.

Cookies do expire - when they expire depends somewhat on the browser, since different browsers have different max allowed cookie ages. For example, on Chrome, our cookie life is about 1 year. On Safari (including all iOS browsers), cookies are deleted if the user does not visit the site for 7 days.

</details>

<details>

<summary>How does Intelligems handle customers who switch devices?</summary>

Intelligems randomly assigns users to a test group when they visit your site for the first time during a test. We then use a cookie to ensure they remain in the same test group every time they come back to the site on the same browser and device.

When a user visits your site on a new device, we cannot rely on that cookie to place them in the same group, so there is a chance they will end up in a different group. That said, in our testing, we have found that less than 1% of typical site traffic may be impacted by switching devices during a test.

We recommend making your customer support team aware of any tests you may be running, and in the rare case that a customer does switch devices and notices a differing price, having a plan of action (such as a discount code) to create a positive customer experience.

</details>

## Targeting FAQs

<details>

<summary>Can I filter out blog traffic from my test(s)?</summary>

Yes! Some brands use their blog pages for SEO. This generates a lot of traffic for their site, but does not result in many conversions or revenue. Because of this, blog traffic can create a lot of noise in analytics, therefore it might be better to filter blog traffic out of your tests to keep your results clean and actionable. If you do not have any UTMs set up for your blog pages, this article will walk you through how you can exclude that traffic from your test.

**Step 1: Add snippet to theme.liquid file.**

Add the below code to your theme.liquid file directly above your Intelligems JavaScript snippet. An example Intelligems JavaScript snippet is included at the bottom of the snippet below to illustrate where the new snippet should be placed.

```liquid
<script>
if (window.history.pushState && window.location.pathname.includes('blog')) {
                    const newURL = new URL(window.location.href);
                    newURL.search = '?blog=1';
                    window.history.pushState({ path: newURL.href }, '', newURL.href);
}
</script>
<script src="https://cdn.intelligems.io/<your_customer_id>.js"></script>
```

**Step 2: Set up UTM filter.**

Set up the below Audience Targeting on your test. Note that this will need to be added to **each test that you want to exclude blog traffic**, and **will only exclude that traffic moving forward.**

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FrOLj0YNoZJ1na8oI52nh%2Fimage.png?alt=media\&token=6356384d-2ab0-42b8-83f4-ed5e6a264dec)

</details>

<details>

<summary>How can I force myself into a specific test group?</summary>

You can force yourself into a specific test group by adding the below to the end of your site's URL:

`/?igTg=TEST-GROUP-ID`

where `TEST-GROUP-ID` is the ID for the test group you would like to be forced into. You can find the test group ID by heading to the A/B Tests tab in the Intelligems app, clicking on the three dots / more options menu next to the test you are working on, and selecting "Show Info". This will bring up the experiment ID, as well as the test group ID for each test group. Click on the long ID for the group you'd like to be forced into to copy it to your clipboard.

The final results should look something like this:

`www.mywebsite.com/?igTg=44bae2e6-dbc3-4fc1-a68d-4218ac04f99c`

</details>

<details>

<summary>Will Intelligems remove UTM parameters when a visitor lands on my site and is part of a test?</summary>

No, UTM parameters won't be removed from your URLs by Intelligems! While there are a few test types that involve redirects, such as Theme, Template and Split URL Tests, URL parameters are persisted, and therefore traffic attribution is preserved.

</details>

<details>

<summary>How do I target or exclude new vs. returning customers?</summary>

Targeting new vs. returning customers is a bit tricky because Shopify does not share whether a customer is new or returning with Intelligems. There are, however, a few ways you can set up audience targeting to help target or exclude new vs. returning visitors.

The first option is to use UTM parameters. To target only new visitors, we typically recommend applying the test to users visiting the site through specific UTM or media campaigns that you use for targeting new customers. There is a small chance that returning customers could come in through these campaigns.

The second option is to use our New / Returning Visitor targeting. It is important to note that this is looking at whether someone is a new or returning *visitor*, and not necessarily whether they are a new or returning *customer*. It is also important to note that we determine whether a visitor is new or returning based off of whether they have an Intelligems ID assigned to them. We assign all site visitors an Intelligems ID when they come to your site, as long as our JavaScript is in your live site. Because of this, if you have just started working with Intelligems, most visitors will be seen as new since they don't have an Intelligems ID assigned to them yet.

Both of these options can be set up in the Targeting step of test set up, which you can read more about [here](https://docs.intelligems.io/content-testing/targeting#what-is-intelligems-audience-targeting).

</details>

## Uninstalling FAQs

<details>

<summary>Can I remove the Intelligems script once my test is complete?</summary>

While there are technically no issues with removing the Intelligems script from your site once your test is complete, we only recommend doing so in the rare case that the site is experiencing performance issues. Otherwise, we recommend leaving the lightweight script installed in your theme as testing shouldn't be one-and-done. We find that stores that approach testing with a roadmap and plan are the stores that unlock the most value. If you are stuck on coming up with an idea on what to test next, check out [this article!](https://docs.intelligems.io/getting-started/common-use-cases)

Additionally, keeping the Intelligems script installed on your store allows Intelligems to continue assigning users an Intelligems ID - this will make New vs. Returning Visitor targeting much more powerful.

If you do need to remove the Intelligems script from your site, delete or comment it out in your theme.liquid file. For Shopify Plus customers, this may also be located in your checkout.liquid file. The JavaScript to remove or comment out will look something like this:

```
<script src="https://cdn.intelligems.io/<your_customer_id>.js"></script>
```

</details>

<details>

<summary>How do I uninstall Intelligems?</summary>

✨ We'd hate to see you go! If you plan on testing again any time in the future, we recommend moving to a Pause Plan instead of uninstalling. This will allow you to keep the integration live so it's easy to start a new test down the road, as well as maintain access to the analytics from any tests you've already run. If this sounds like a better option, you can do this from the Settings page of the Intelligems app. If you don't see the option there, please reach out to <billing@intelligems.io> to get set up with a Pause Plan.

{% hint style="info" %}
Note: We do *not* recommend uninstalling and reinstalling the app as a technical troubleshooting step, as this will cause you to be charged again for the new installation. If you're experiencing an issue with the app or with a test, please reach out to <support@intelligems.io> for assistance.&#x20;
{% endhint %}

**Step 1: Stop any tests.**

Confirm that you've stopped any tests or campaigns from within the app! You'll want to make sure you also rolled out the winners while doing this - see more details on how to end a [Price Test](https://help.intelligems.io/how-to-end-price-tests) and a [Shipping Test](https://help.intelligems.io/ending-a-shipping-test) at each of those links.

**Step 2: Uninstall the app via Shopify.**

Follow Shopify's steps [here](https://help.shopify.com/en/manual/apps/uninstalling-apps#uninstall-app) to uninstall the Intelligems app - this will cancel billing.

**Step 3: Remove Intelligems JavaScript.**

During the integration, you or the Intelligems team added JavaScript as a source into your theme.liquid file - you can now remove the Intelligems script from your site. To do so, delete or comment it out in your theme.liquid file. For Shopify Plus customers, this may also be located in your checkout.liquid file. The JavaScript to remove or comment out will look like this:

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fc102Q8LAcprswpUFZiyA%2FScreenshot%202024-02-06%20at%203.50.14%20PM.png?alt=media&#x26;token=f0a47297-f9d0-4aef-8813-15bb25918261" alt="" data-size="original">

❗Note that if you do not complete this step, we will continue to append an igId onto your orders in the 'Additional Details' section in Shopify. Customers will not see this, and it will not cause any issues, but may cause confusion for your team if they do not know where it is coming from!

**Step 4: Remove Checkout Script&#x20;*****or*****&#x20;manage Duplicate Products, if applicable.**

❗This step is only applicable if you have run Price Tests!

***If you are on Shopify Plus and ran your test using a Checkout Script,*** you can now stop that script by either unpublishing the entire Checkout Script (if nothing else is in it), or by removing the Intelligems script if you use the Checkout Script for anything else.

***If you are not on Shopify Plus and ran your test using Duplicate Products,*** confirm those products are archived. See more details on managing Duplicate Products from previous tests [here](https://help.intelligems.io/can-i-delete-duplicate-products-once-a-pricing-test-is-over).

**Step 5: Remove Intelligems as a shipping rate provider, if applicable.**

❗This step is only applicable if you have run Shipping Tests!

Confirm that Intelligems is removed as a shipping rate provider. You can check this by going to your Settings in Shopify → Shipping and delivery → Manage by General Shipping Rates. Once you're there, confirm that 'Intelligems Shipping (Rates provided by app)' is not listed anywhere. If it is, please delete it using the three dots to the right and add your own rate to replace it if needed.

**Step 6: Send us your feedback!**

We are always looking to make improvements to our platform and processes! If there is something we could have done better, you have feature requests, or you just want to chat all things ecomm, please don't hesitate to reach out to <support@intelligems.io>.

</details>


# Price Testing - Getting Started

## What is Price Testing?

Intelligems takes the guesswork out of setting your product prices by allowing you to test prices in real time in order to find the “right” product prices to drive profit, revenue, and conversion boosts.

You can easily build product price split tests with just a few clicks in the Intelligems app. Tests are easy to build and customize: add multiple test groups with configurable traffic distribution rules, select which products to include in the test, and set test group prices.

## How does it work?

For all Shopify brands, Intelligems displays the correct price on the frontend by manipulating the DOM to show the correct price depending on a user's test group once your [prices have been tagged](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices). Intelligems displays the correct price in the cart and charges the correct amount at checkout using one of the three below methods:

1. **Using Shopify Cart Transform Functions.** Intelligems will automatically set your prices to the highest prices in the test in Shopify when you start your test, and we will use a Shopify Cart Transform Function to dynamically adjust the price for any users in a group lower than the highest price in the test so that they get the same price in the cart and at checkout that they saw everywhere else on the site. This method is available for brands on any Shopify plan, and will be Intelligems' primary method moving forward.
2. **Using a Checkout Script.** Intelligems will automatically set your prices to the highest prices in the test in Shopify when you start your test, and we will use a Checkout Script to run a behind the scenes adjustment for any users in a group lower than the highest price in the test so that they get the same price in the cart and at checkout that they saw everywhere else on the site. This method is only available for brands on Shopify Plus, and Intelligems is beginning to move away from this method as Shopify will be deprecating the Script Editor app in August 2025.
3. **Using Duplicate Products.** In certain cases, such as testing something more complex or if you offer subscriptions, Intelligems will swap in a duplicate product when a user adds to cart in any group other than the control group to ensure the price is correct in the cart and at checkout.

## How can I get started?

There is a short integration required before you can begin a price test. Please see the appropriate guide [here](https://docs.intelligems.io/getting-started/pricing-integration-guides) depending on which version of our integration you are on. If you are not sure which integration guide you should be following, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).

If you prefer, we'll be happy to complete the integration for you - in that case, please book a demo with our team [here](https://meetings.hubspot.com/igsam/igdemo?uuid=09e10934-25f6-4485-9f0e-4ceb6e80f099) so we can learn more about your store and get it integrated with Intelligems.

Once the integration has been completed, see the guides below for more information on price testing:

{% content-ref url="price-testing-integration-guides" %}
[price-testing-integration-guides](https://docs.intelligems.io/price-testing/price-testing-integration-guides)
{% endcontent-ref %}

{% content-ref url="how-to-set-up-a-price-test" %}
[how-to-set-up-a-price-test](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test)
{% endcontent-ref %}

{% content-ref url="price-test-qa-checklist" %}
[price-test-qa-checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist)
{% endcontent-ref %}

{% content-ref url="starting-a-price-test" %}
[starting-a-price-test](https://docs.intelligems.io/price-testing/starting-a-price-test)
{% endcontent-ref %}

{% content-ref url="ending-a-price-test" %}
[ending-a-price-test](https://docs.intelligems.io/price-testing/ending-a-price-test)
{% endcontent-ref %}

{% content-ref url="testing-prices-with-subscriptions" %}
[testing-prices-with-subscriptions](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions)
{% endcontent-ref %}

{% content-ref url="multi-currency-testing" %}
[multi-currency-testing](https://docs.intelligems.io/price-testing/multi-currency-testing)
{% endcontent-ref %}

{% content-ref url="price-testing-faqs" %}
[price-testing-faqs](https://docs.intelligems.io/price-testing/price-testing-faqs)
{% endcontent-ref %}


# Price Testing Integration Guides

Intelligems can integrate with your Shopify store for Price Testing using several different mechanisms. Those mechanisms are:

1. Shopify Cart Transform Functions
2. Checkout Scripts
3. Duplicate Products

Which mechanism is best for your store depends on a few different factors. If you are not sure which integration type is best for you, or which integration type your store is currently using, please open a ticket with our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!

{% content-ref url="price-testing-integration-guides/integration-guide-using-shopify-functions" %}
[integration-guide-using-shopify-functions](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions)
{% endcontent-ref %}

{% content-ref url="price-testing-integration-guides/integration-guide-using-checkout-scripts" %}
[integration-guide-using-checkout-scripts](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts)
{% endcontent-ref %}

{% content-ref url="price-testing-integration-guides/integration-guide-using-duplicate-products" %}
[integration-guide-using-duplicate-products](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-duplicate-products)
{% endcontent-ref %}

{% content-ref url="price-testing-integration-guides/troubleshooting" %}
[troubleshooting](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting)
{% endcontent-ref %}

{% content-ref url="price-testing-integration-guides/replo-page-builder" %}
[replo-page-builder](https://docs.intelligems.io/price-testing/price-testing-integration-guides/replo-page-builder)
{% endcontent-ref %}


# Integration Guide using Shopify Functions

Historically, Intelligems has used either Checkout Scripts or duplicate products to run Price Tests. Shopify will be sunsetting Checkout Scripts in August 2026, and with that transition, Intelligems will be using Shopify Cart Transform Functions instead. This is the integration we mostly use currently, and it is enabled by default on new installs.

{% hint style="warning" %}
A few caveats when using Functions:

* If your store is on Shopify Plus, and you are using any Line Item Checkout Scripts, there may be conflicts between those and the Function we run.
* Please note that only one Shopify Cart Transform Function can run on a single line item.

If you use Cart Transform Functions for other capabilities, or you are in doubt about conflicts with existing Checkout Scripts, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to discuss options for your integration.
{% endhint %}

Before you can run a Price Test on your Shopify store, there is a small integration that needs to be done. There are four steps in the integration:

1. Add Intelligems JavaScript
2. Tag product prices
3. Update your cart
4. QA your integration, and publish your changes

{% hint style="success" %}
The Intelligems team is happy to complete the integration for you - please reach out [here](https://portal.usepylon.com/intelligems/forms/price-test-integration-request) to get this process started.
{% endhint %}


# Step 1: Add Intelligems JavaScript

## Introduction

If you have not already done so, you will need to add the Intelligems script to your site. There are two options below for doing this.

## Option 1: Use the App Embed Block

{% hint style="success" %}
This is the easiest installation method that works for most stores!
{% endhint %}

The fastest way to add Intelligems JavaScript to your theme is to enable it in the "Customize" section of your theme editor. You can do so by logging into your Shopify Admin, and navigating to Sales Channels > Online Store > Live theme - Customize > App Embeds. Search "Intelligems", make sure it is toggled on, and click "Save" in the top right.\
\
This will load Intelligems in a fashion that works optimally for performance and A/B testing on most stores. If for any reason you encounter performance concerns, see our docs on [performance optimization](https://app.gitbook.com/o/HNmChKUZY1pAEPfel38z/s/2SvefuMLsJyJPAcVXeWc/~/changes/736/performance-optimization/optimizing-your-price-test-integration).

{% hint style="warning" %}
For any **password protected store**, we will not be able to automatically detect the script, so you will continue to get an error message in the app regarding the script not being in your theme.
{% endhint %}

## Option 2: Add to Your Theme Code

{% hint style="info" %}
If you are on Shopify Plus and are still using checkout.liquid, you will still need to manually add Intelligems JavaScript to your checkout.liquid file in order to hide the discount or preview bar at checkout. Your individual script tag is located on the settings page in the Intelligems App.&#x20;
{% endhint %}

{% hint style="danger" %}
This will need to be manually removed if you uninstall Intelligems.
{% endhint %}

To complete this, go to the settings page in the Intelligems app. Once there, you'll see a section called "Theme Script". Click the blue button in that block that says "Copy Script". This will copy your unique Intelligems script to your clipboard.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FqvWfk91wEFeZyv5joSHW%2FScreenshot%202025-09-25%20at%205.30.44%E2%80%AFPM.png?alt=media&#x26;token=d06b3072-4307-499b-a878-b3b3ed6c9da8" alt=""><figcaption></figcaption></figure>

Now head over to your Shopify account, and paste the Intelligems Script as a source into the `<head>` of each of these files:

* theme.liquid
* any other theme.\*.liquid files (e.g., theme.gempages.liquid if you have this file)

Here's a video walking through those steps as well:

{% embed url="<https://www.loom.com/share/187128fe3b9c4334b5904d4c4de48dbf?sid=477d7023-fb18-4218-accd-fbd0775fee88>" %}


# Step 2: Tag product prices

## Introduction

To enable Intelligems to dynamically modify price elements for each test group during testing, it is essential to tag their locations on your website. This entails adding the query selector for price elements into the Intelligems configuration so the Intelligems plugin knows where those prices live. This guide will walk you through the process to do so.

{% hint style="warning" %}
Before you can use the Intelligems Widget, please confirm that you've added Intelligems JavaScript as a source into your theme.liquid file! See more on how to add our JavaScript to your site [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
{% endhint %}

## Step 1: Accessing the Widget <a href="#accessing-the-widget" id="accessing-the-widget"></a>

To get started, you'll need to create a price test in the Intelligems app, and open the Intelligems preview widget for that test. There are two ways to access the Intelligems Preview Widget:

1. Navigate to the "Tests" tab in the Intelligems app. Click on the eyeball icon to the right of the Price Test you have created. This will open a new browser window up with your website with the widget enabled.
2. You can also enter this mode by adding /?ig-preview=true to the end of your website's URL (e.g. <https://mystore.com/?ig-preview=true>). This will open a modal where you can choose which experiment you would like to see in the onsite widget. To tag prices, be sure to select a price test from this dropdown.

Once you are in Preview mode, select the "Edit" button followed by the dollar sign. The video below will walk you through this process:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F21VfDyeKkfLCwBZ6rOqz%2F12%20-%20preview%20selectors.gif?alt=media&#x26;token=521a127e-9eba-4063-85a6-77d2b095d381" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The Intelligems Widget offers full support for **Google Chrome**. Support for any other browsers is limited. If you are having an issue with the Widget in another browser, we suggest trying to run it in Google Chrome. For more support, please open a ticket with our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
{% endhint %}

## Step 2: Adding Price Selectors <a href="#adding-price-selectors" id="adding-price-selectors"></a>

Now that you are in Edit mode, it is time to tag price elements everywhere on your site. Follow the steps below:

1. **Enable price tagging mode** - Click the $ icon in the edit widget
2. **Enable price selector mode** - Click the box labeled 2 in the image below
3. **Tag price elements** - Move your cursor to see blue dotted lines around page elements. Click a price element to add it to the query selector list. Click Save to highlight the element:
   * <mark style="color:$success;">Green</mark> = product is in the test you are currently previewing
   * <mark style="color:blue;">Blue</mark> = product is **not** in the test you are currently previewing
   * If the price for a product in your test is highlighted in blue, Intelligems can't identify the product or variant ID - see [this guide](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting/how-to-add-the-data-product-id-and-or-data-variant-id-attribute-to-an-element) for the required theme change
4. **Tag all prices** - Add query selectors to the correct section (compare at price for strikethrough prices, price for regular prices, etc.) for all prices on your site, except for products added to your cart or your checkout page
5. **Save your work** - Click Save periodically to avoid losing progress

<div data-with-frame="true"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FFAVT2RDDlLDgDz8lteMN%2FScreenshot%202025-10-06%20at%2010.59.01%E2%80%AFAM.png?alt=media&#x26;token=2e249b15-67c0-4905-81ea-d67170b1db48" alt=""><figcaption><p>1. The type of selector - see more below for what each type is for.<br>2. Enable selector mode - clicking this button will allow you click on your prices on your site and automatically add a new selector.<br>3. Query selectors that have been added.<br>4. Delete a query selector.<br>5. Simplify a selector - use this function if the selector added was too specific.<br> 6. Add a query selector manually.<br>7. Auto add all price selectors on your site using AI.</p></figcaption></figure></div>

<details>

<summary>A few places to keep in mind as you tag all of the prices elements in your store include:</summary>

* Homepage
* Collection Pages
* Product Detail Pages (PDPs) - make sure you don't miss tagging any related or recommended products listed on your PDPs!
* Search Results Page or Bar, depending on where results show price
* Product Quiz
* Upsells in the cart or at checkout

</details>

<details>

<summary>Here are all of the different selector types:</summary>

**Price:** Use this section to select product prices on your store's site.

**Compare At Price:** Use this section to select compare prices on your store's site.

**Installment:** Use this section to select installments on your store's site. The default number of payments is 4. To change the payment amount, add the below to the element containing your installment in your theme.

```
data-payment-count="{{payment_amount}}" 
```

The Installment selector is compatible with installments that are:

1. Directly in your liquid
2. Not in the liquid, but is wrapped in its own \<span>

This selector is **not** compatible with installments that are:

1. Wrapped in a Shadow DOM
2. Not wrapped in its own span

**Savings (Price):** Use this option to select the dollar savings amount. This is normally located on your product pages.

**Savings (Percentage):** Use this option to select the percentage savings amount. This is normally located on your product pages.

**Cart Discount Message:** Use this option to hide a discount message (i.e. DISCOUNT or INTELLIGEMS) in your cart.

</details>

<details>

<summary>A few tips &#x26; tricks:</summary>

**Per Unit Prices.** If you have per unit prices listed for a product, you can follow these steps to update those prices accordingly during a price test:

1. Tag the per unit prices with a normal Price selector.
2. In your theme code, add `data-price-multiplier=".X"` to the per unit element, where X is what you want to multiple the price by. For example, if you wanted to show the per unit price when there are three units included, you would add `data-price-multiplier=".33"` to the element.

**Discounted Prices.** Many brands use the compare price field in Shopify to show a perceived discount - these are easy to tag using our various selector types. However, some brands will use a different method to show discounted prices by manipulating the frontend prices & using something like a Checkout Script to achieve a perceived discount. If this is the case for your store, follow these steps to accurately tag those prices:

1. Tag the per unit prices with a normal Price selector.
2. In your theme code, add `data-price-multiplier=".X"` to the discounted price element, where X is the inverse of the discount you are applying. For example, if you were running a 20% discount, you would add `data-price-multiplier=".8"` to the element.

</details>

You'll know you're done when all price, compare at price, installment and savings elements are highlighted in blue or green on all pages in your store!

{% hint style="danger" %}
Note that you **should not tag prices in the cart or cart drawer** as we will manage updating those using Cart Transform Functions.
{% endhint %}

{% hint style="info" %}
Having issues? Checkout our troubleshooting guide [here](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting) or submit a ticket to our support team [here](https://portal.usepylon.com/intelligems/forms/price-test-integration-request)!
{% endhint %}


# Step 3: Update your cart

Once you have tagged your prices, you should add a product that is in the test to cart while previewing the test. In certain cases, you may notice an issue in the cart when you do this - a few examples of things that may happen include:

* There may be a few visible line item properties in the cart
* The compare-at price will not display correctly in the cart - for example, the compare price may show as the control price, rather than the compare price for the test group you are in

Should any of these happen, follow the below corresponding guidance to correct the issue and complete the integration.

### Remove Hidden Line Item Properties[​](https://docs.intelligems.io/docs/pricing-integration/shopify-plus/update-cart#remove-hidden-line-item-properties)

Most Shopify stores use a convention that states that any line item property with a leading underscore (\_) should not be displayed in the cart. Intelligems uses the line item property `'_igp'`, so as long as this convention is set up for your store, the Intelligems line item property will be automatically hidden.

If this convention is not already set up for your store, You may see something like this in the cart when you test it in preview mode:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FxosWliarzNzsSygrwdEZ%2FScreenshot%202024-03-08%20at%201.17.37%20PM.png?alt=media&#x26;token=d54e3471-2e3e-484d-8545-b2687bb18d9c" alt=""><figcaption></figcaption></figure>

Here is an example of how you can fix this by implementing the below in a liquid cart (i.e. cart-line-items.liquid or a similar file). The key lines are as follows:

```liquid
{% assign first_character_in_key = p.first | truncate: 1, '' %}
{% unless p.last == blank or first_character_in_key == '_' %}

```

This code should be implemented in a loop over each item property. In context, the code block may look something like the below:

```liquid
{% assign property_size = item.properties | size %}
{% if property_size > 0 %}
  {% for p in item.properties %}
    {% assign first_character_in_key = p.first | truncate: 1, '' %}
    {% unless p.last == blank or first_character_in_key == '_' %}
      {{ p.first }}:
      {% if p.last contains '/uploads/' %}
        <a href="{{ p.last }}">{{ p.last | split: '/' | last }}</a>
      {% else %}
        {{ p.last }}
      {% endif %}
    {% endunless %}
  {% endfor %}
{% endif %}
```

You can learn more about this [here](https://community.shopify.com/c/shopify-design/product-pages-get-customization-information-for-products/m-p/616525#toc-hId-287417639) under 'Hide line item properties (optional)'.

### Displaying the Correct Strikethrough Price in the Cart

Typically, you should not tag any prices within your cart while completing "Step 2: Tag your prices". However, if you do display a strikethrough price in the cart, you'll want to tag that to ensure the correct strikethrough price shows up for each group.


# Step 4: QA your integration, and publish your changes

After you have completed all previous integration steps, go through your store using Preview Mode in (you can access preview mode by clicking on the Eye icon next to your test, or by adding /?ig-preview=true to the end of your website's URL) and make sure everything looks correct. Follow our QA checklist [here](https://docs.intelligems.io/price-testing/price-test-qa-checklist)!

Once you have verified Intelligems is fully integrated, you can publish your theme changes (if you haven't already) and start your test from the Intelligems App! Check out our step-by-step guide on doing this [here](https://docs.intelligems.io/price-testing/starting-a-price-test).

#### What happens next?

Now that you've started your first test, here are some things to do next:

* Check the Analytics Dashboard in the Intelligems app to see how the test is doing frequently. Note that it may take one to two hours for data to flow in!
* Start thinking about your [testing roadmap](https://docs.intelligems.io/getting-started/best-practices/test-design-best-practices).
* Review some [test suggestions](https://docs.intelligems.io/getting-started/common-use-cases).


# Integration Guide using Checkout Scripts

Learn how to integrate your Shopify Plus store with Intelligems for a Price Test using Checkout Scripts.

Before you can run a Price Test on your Shopify store, there is a small integration that needs to be done. There are five components to the integration:

1. Add Intelligems JavaScript
2. Tag product prices
3. Add the Checkout Script
4. Update your cart
5. QA your integration, and publish your changes

{% hint style="danger" %}
If you have chosen to have Intelligems complete the integration, many of these steps will be done on your behalf.
{% endhint %}


# Step 1: Add Intelligems JavaScript

## Introduction

If you have not already done so, you will need to add the Intelligems script to your site. There are two options below for doing this.

## Option 1: Use the App Embed Block

{% hint style="success" %}
This is the easiest installation method that works for most stores!
{% endhint %}

The fastest way to add Intelligems JavaScript to your theme is to enable it in the "Customize" section of your theme editor. You can do so by logging into your Shopify Admin, and navigating to Sales Channels > Online Store > Live theme - Customize > App Embeds. Search "Intelligems", make sure it is toggled on, and click "Save" in the top right.\
\
This will load Intelligems in a fashion that works optimally for performance and A/B testing on most stores. If for any reason you encounter performance concerns, see our docs on [performance optimization](https://app.gitbook.com/o/HNmChKUZY1pAEPfel38z/s/2SvefuMLsJyJPAcVXeWc/~/changes/736/performance-optimization/optimizing-your-price-test-integration).

{% hint style="warning" %}
For any **password protected store**, we will not be able to automatically detect the script, so you will continue to get an error message in the app regarding the script not being in your theme.
{% endhint %}

## Option 2: Add to Your Theme Code

{% hint style="info" %}
If you are on Shopify Plus and are still using checkout.liquid, you will still need to manually add Intelligems JavaScript to your checkout.liquid file in order to hide the discount or preview bar at checkout. Your individual script tag is located on the settings page in the Intelligems App.&#x20;
{% endhint %}

{% hint style="danger" %}
This will need to be manually removed if you uninstall Intelligems.
{% endhint %}

To complete this, go to the settings page in the Intelligems app. Once there, you'll see a section called "Theme Script". Click the blue button in that block that says "Copy Script". This will copy your unique Intelligems script to your clipboard.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FqvWfk91wEFeZyv5joSHW%2FScreenshot%202025-09-25%20at%205.30.44%E2%80%AFPM.png?alt=media&#x26;token=d06b3072-4307-499b-a878-b3b3ed6c9da8" alt=""><figcaption></figcaption></figure>

Now head over to your Shopify account, and paste the Intelligems Script as a source into the `<head>` of each of these files:

* theme.liquid
* any other theme.\*.liquid files (e.g., theme.gempages.liquid if you have this file)

Here's a video walking through those steps as well:

{% embed url="<https://www.loom.com/share/187128fe3b9c4334b5904d4c4de48dbf?sid=477d7023-fb18-4218-accd-fbd0775fee88>" %}


# Step 2: Tag product prices

## Introduction

To enable Intelligems to dynamically modify price elements for each test group during testing, it is essential to tag their locations on your website. This entails adding the query selector for price elements into the Intelligems configuration so the Intelligems plugin knows where those prices live. This guide will walk you through the process to do so.

{% hint style="warning" %}
Before you can use the Intelligems Widget, please confirm that you've added Intelligems JavaScript as a source into your theme.liquid file! See more on how to add our JavaScript to your site [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
{% endhint %}

## Step 1: Accessing the Widget <a href="#accessing-the-widget" id="accessing-the-widget"></a>

To get started, you'll need to create a price test in the Intelligems app, and open the Intelligems preview widget for that test. There are two ways to access the Intelligems Preview Widget:

1. Navigate to the "Tests" tab in the Intelligems app. Click on the eyeball icon to the right of the Price Test you have created. This will open a new browser window up with your website with the widget enabled.
2. You can also enter this mode by adding /?ig-preview=true to the end of your website's URL (e.g. <https://mystore.com/?ig-preview=true>). This will open a modal where you can choose which experiment you would like to see in the onsite widget. To tag prices, be sure to select a price test from this dropdown.

Once you are in Preview mode, select the "Edit" button followed by the dollar sign. The video below will walk you through this process:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FMISntvysIsTcu6doGJZj%2F12%20-%20preview%20selectors.gif?alt=media&#x26;token=37bcd4c1-0189-467c-be5e-884610cf47f5" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The Intelligems Widget offers full support for **Google Chrome**. Support for any other browsers is limited. If you are having an issue with the Widget in another browser, we suggest trying to run it in Google Chrome. For more support, please open a ticket with our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
{% endhint %}

## Step 2: Adding Price Selectors <a href="#adding-price-selectors" id="adding-price-selectors"></a>

Now that you are in Edit mode, it is time to tag price elements everywhere on your site. Follow the steps below:

1. **Enable price tagging mode** - Click the $ icon in the edit widget
2. **Enable price selector mode** - Click the box labeled 2 in the image below
3. **Tag price elements** - Move your cursor to see blue dotted lines around page elements. Click a price element to add it to the query selector list. Click Save to highlight the element:
   * <mark style="color:$success;">Green</mark> = product is in the test you are currently previewing
   * <mark style="color:blue;">Blue</mark> = product is **not** in the test you are currently previewing
   * If the price for a product in your test is highlighted in blue, Intelligems can't identify the product or variant ID - see [this guide](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting/how-to-add-the-data-product-id-and-or-data-variant-id-attribute-to-an-element) for the required theme change
4. **Tag all prices** - Add query selectors to the correct section (compare at price for strikethrough prices, price for regular prices, etc.) for all prices on your site, except for products added to your cart or your checkout page
5. **Save your work** - Click Save periodically to avoid losing progress

<div data-with-frame="true"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FFAVT2RDDlLDgDz8lteMN%2FScreenshot%202025-10-06%20at%2010.59.01%E2%80%AFAM.png?alt=media&#x26;token=2e249b15-67c0-4905-81ea-d67170b1db48" alt=""><figcaption><p>1. The type of selector - see more below for what each type is for.<br>2. Enable selector mode - clicking this button will allow you click on your prices on your site and automatically add a new selector.<br>3. Query selectors that have been added.<br>4. Delete a query selector.<br>5. Simplify a selector - use this function if the selector added was too specific.<br> 6. Add a query selector manually.<br>7. Auto add all price selectors on your site using AI.</p></figcaption></figure></div>

<details>

<summary>A few places to keep in mind as you tag all of the prices elements in your store include:</summary>

* Homepage
* Collection Pages
* Product Detail Pages (PDPs) - make sure you don't miss tagging any related or recommended products listed on your PDPs!
* Search Results Page or Bar, depending on where results show price
* Product Quiz
* Upsells in the cart or at checkout

</details>

<details>

<summary>Here are all of the different selector types:</summary>

**Price:** Use this section to select product prices on your store's site.

**Compare At Price:** Use this section to select compare prices on your store's site.

**Installment:** Use this section to select installments on your store's site. The default number of payments is 4. To change the payment amount, add the below to the element containing your installment in your theme.

```
data-payment-count="{{payment_amount}}" 
```

The Installment selector is compatible with installments that are:

1. Directly in your liquid
2. Not in the liquid, but is wrapped in its own \<span>

This selector is **not** compatible with installments that are:

1. Wrapped in a Shadow DOM
2. Not wrapped in its own span

**Savings (Price):** Use this option to select the dollar savings amount. This is normally located on your product pages.

**Savings (Percentage):** Use this option to select the percentage savings amount. This is normally located on your product pages.

**Cart Discount Message:** Use this option to hide a discount message (i.e. DISCOUNT or INTELLIGEMS) in your cart.

</details>

<details>

<summary>A few tips &#x26; tricks:</summary>

**Per Unit Prices.** If you have per unit prices listed for a product, you can follow these steps to update those prices accordingly during a price test:

1. Tag the per unit prices with a normal Price selector.
2. In your theme code, add `data-price-multiplier=".X"` to the per unit element, where X is what you want to multiple the price by. For example, if you wanted to show the per unit price when there are three units included, you would add `data-price-multiplier=".33"` to the element.

**Discounted Prices.** Many brands use the compare price field in Shopify to show a perceived discount - these are easy to tag using our various selector types. However, some brands will use a different method to show discounted prices by manipulating the frontend prices & using something like a Checkout Script to achieve a perceived discount. If this is the case for your store, follow these steps to accurately tag those prices:

1. Tag the per unit prices with a normal Price selector.
2. In your theme code, add `data-price-multiplier=".X"` to the discounted price element, where X is the inverse of the discount you are applying. For example, if you were running a 20% discount, you would add `data-price-multiplier=".8"` to the element.

</details>

You'll know you're done when all price, compare at price, installment and savings elements are highlighted in blue or green on all pages in your store!

{% hint style="warning" %}
Note that you **should not tag prices in the cart or cart drawer** as we will manage updating those using Checkout Scripts.
{% endhint %}

{% hint style="info" %}
Having issues? Checkout our troubleshooting guide [here](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting) or submit a ticket to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
{% endhint %}


# Step 3: Add the Checkout Script

{% hint style="danger" %}
You must be using Shopify Plus to integrate with Intelligems using the Checkout Script. Please see our [Functions Integration guide](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions) if this does not apply to you.
{% endhint %}

{% hint style="info" %}
The Intelligems checkout script will not apply any discounts or make other changes to orders until a price test is live. If you already use a Checkout Script, you can add ours to the same one to keep that functionality.
{% endhint %}

Adding our Checkout Script enables us to dynamically discount the price in the cart so that your customers pay exactly the price they see in other spots on the website. Follow the below steps to add the Intelligems Line Items Checkout Script to your Scripts Editor.

1. Install the Shopify Script editor [here](https://apps.shopify.com/script-editor).
2. If you already have a Line Items script, you can create a copy and edit it. Make sure our script runs first so that discounts get applied in the correct order. If you do not already have a Line Items script, create a new one.
3. Paste the loop below into the script. Save and publish the script.

```ruby
class Intelligems
  def initialize(discount_property = '_igp', allow_free = false)
    @volume_discount_property = '_igvd'
    @volume_discount_message_property = '_igvd_message'
    @deprecated_property = '_igLineItemDiscount'
    @discount_property = discount_property
    @allow_free = allow_free
  end

  def discount_product(line_item)
    ig_price = Money.new(cents: line_item.properties[@discount_property])

    discount = line_item.line_price - (ig_price * line_item.quantity)
    if discount > Money.zero
      if @allow_free or discount < line_item.line_price
        line_item.change_line_price(line_item.line_price - discount, message: 'Discount')
      end
   end
  end

def deprecated_discount_product(line_item)
  discount = Money.new(cents: line_item.properties[@deprecated_property])
    discount *= line_item.quantity

    if @allow_free or discount < line_item.line_price
      line_item.change_line_price(line_item.line_price - discount, message: 'Intelligems')
    end
  end

  def volume_discount(line_item)
    discount = Money.new(cents: line_item.properties[@volume_discount_property])
    discount *= line_item.quantity

    if discount < line_item.line_price
      message = line_item.properties[@volume_discount_message_property]
      line_item.change_line_price(line_item.line_price - discount, message: message)
    end
  end

  def run(cart)
    cart.line_items.each do |line_item|
      if !line_item.properties[@discount_property].nil? && !line_item.properties[@discount_property].empty?
        discount_product(line_item)
    elsif !line_item.properties[@volume_discount_property].nil? && !line_item.properties[@volume_discount_property].empty?
        volume_discount(line_item)
    elsif !line_item.properties[@deprecated_property].nil? && !line_item.properties[@deprecated_property].empty?
            deprecated_discount_product(line_item)
      end
    end
  end
end

intelligems = Intelligems.new()
intelligems.run(Input.cart)

Output.cart = Input.cart
```


# Step 4: Update your cart

Remove hidden line item properties, or calculate and hide discount messages

Once you have published the checkout script, you should add a product to cart while previewing the lowest priced group. In certain cases, you may notice an issue in the cart when you do this. A few examples of things that may happen include:

* There may be a few visible line item properties in the cart
* The Intelligems discount message will occasionally show in the cart
* The compare-at price will not display correctly in the cart. For example, the compare-at price may show as the control group price, rather than the compare-at price for the test group you are in
* The cart will only show the control group prices in preview mode while the test is pending. This is expected; read more in the FAQ [here](https://docs.intelligems.io/price-testing/price-testing-faqs). Starting the test will show the correct prices.

Should any of these happen, follow the below corresponding guidance to correct the issue and complete the integration.

### Remove Hidden Line Item Properties[​](https://docs.intelligems.io/docs/pricing-integration/shopify-plus/update-cart#remove-hidden-line-item-properties)

Most Shopify stores use a convention that any line item with a leading underscore `_` should not be displayed in the cart. The Intelligems line item property (e.g. `_igLineItemDiscount`) in the Checkout Script you've just added begins with an underscore, so we will piggyback on this convention to make sure the Intelligems discount line item property is hidden.

Here is a common example of how this is implemented in a liquid cart (e.g. cart-line-items.liquid or a similar file). Many themes already contain this code, but it may be necessary to add if it is not already present. We recommend searching your theme file with a tool like [EZFY](https://chrome.google.com/webstore/detail/shopify-theme-file-search/mhchmhfecfdpaifljcfebnlaiaphfkmb) first to see if similar code already exists.

The key lines are as follows:

```liquid
{% assign first_character_in_key = p.first | truncate: 1, '' %}
{% unless p.last == blank or first_character_in_key == '_' %}

```

This code should be implemented in a loop over each item property. In context, the code block may look something like the below:

```liquid
{% assign property_size = item.properties | size %}
{% if property_size > 0 %}
  {% for p in item.properties %}
    {% assign first_character_in_key = p.first | truncate: 1, '' %}
    {% unless p.last == blank or first_character_in_key == '_' %}
      {{ p.first }}:
      {% if p.last contains '/uploads/' %}
        <a href="{{ p.last }}">{{ p.last | split: '/' | last }}</a>
      {% else %}
        {{ p.last }}
      {% endif %}
    {% endunless %}
  {% endfor %}
{% endif %}

```

You can learn more about this [here](https://community.shopify.com/c/shopify-design/product-pages-get-customization-information-for-products/m-p/616525#toc-hId-287417639) under 'Hide line item properties (optional)'.

### Calculate the Intelligems Discount (per line item and cumulative)

If we're using the Checkout Scripts to apply a "hidden" discount on a product, we don't want to show the user that they're receiving an Intelligems discount. Locate the liquid file that renders each cart item, often called cart-line-items.liquid or something similar. Within that file, locate the beginning of the loop over each item. It will look something like the below:

```liquid
{% for item in cart.items %}

   ...
```

For each cart item, we'll want to check to see if an Intelligems discount was applied, and we'll want to keep track of the running total of Intelligems discounts. The snippet below under 'New', placed inside an existing code block which iterates over each cart item, will create a variable intelligems\_discount per line item which is either 0 or a non-zero number in cents which represents the Intelligems price change. This can also be used to adjust compare-at prices if desired.

***Old***

```liquid
{% for item in cart.items %}
   ...
{% endfor %}

```

***New***

```liquid
{% assign intelligems_total = 0 %}
{% for item in cart.items %}
    {% case item.properties._igp %}
      {% when "0" or nil or blank %}
        {% assign intelligems_discount = 0 %}
      {% else %}
        {% assign intelligems_discount = item.properties._igp | plus: 0 %}
        {% assign intelligems_total = intelligems_total | plus: item.properties._igp | times: item.quantity %}
    {% endcase %} 
   ....
{% endfor %}

```

Note that you'll only need one 'for' loop here (i.e. only one instance of the line\
\&#xNAN;*"for item in cart.items"*)

### Hide the Strikethrough Price in the Cart

Now that we have each item's Intelligems discount, we can prevent certain item properties (i.e. a strikethrough) from being rendered in the cart.

Within the 'for' loop described above, locate the code that renders the strikethrough price. It may look something like the below:

```liquid
{% if item.original_line_price and item.original_line_price != item.line_price %}
<span style="text-decoration:line-through;">{{ item.original_line_price | money }}</span><br>
{% endif %}

```

We might add the condition below to the code rendering the strikethrough:

```liquid
{% if ... and intelligems_discount == 0 %}
...
{% endif %}

```

In context, this will look like something like the below:

```liquid
{% if item.original_line_price and item.original_line_price != item.line_price and intelligems_discount == 0 %}
    <span style="text-decoration:line-through;">{{ item.original_line_price | money  }}</span><br>
{% endif %}

```

### Hide the Discount Message[​](https://docs.intelligems.io/docs/pricing-integration/shopify-plus/update-cart#hide-the-discount-message)

Sometimes discount messages appear to communicate bundle discounts, etc. In this case, we'll want to hide our message. We know from the checkout script in Step 4 that the Intelligems discount has the name "Discount" in most cases, so we'll hide any discount message with this name. Locate the code that renders the discount message, again in the 'for' loop over the cart's items. It will likely look something like the below:

```liquid
{% if item.message and item.message != "" %}
    <br><span>({{ item.message }})</span>
{% endif %}

```

We'll want to add the following condition to prevent "Intelligems" from being rendered as a discount name:

```liquid
{% if ... and item.message != "Discount" %}
    ...
{% endif %}

```

In context, this will look something like the below:

```liquid
{% if item.message and item.message != "" and item.message != "Discount" %}
    <br><span>({{ item.message }})</span>
{% endif %}
```

Note: there may be additional adjustments you want to make (e.g. adjusting a strikethrough on the subtotal). We recommend using the line item and running total discount variables you created above and similar conditional logic to implement these additional adjustment.

### Integrating Using HandleBars[​](https://docs.intelligems.io/docs/pricing-integration/shopify-plus/update-cart#integrating-using-handlebars)

Follow the example below if you use HandleBars in your theme. Add the HandleBar functions to the rest of your HandleBar functions.

<pre class="language-javascript"><code class="lang-javascript"><strong>Handlebars.registerHelper('noIgDiscount', function(arg1, options) {
</strong>    return (arg1.find(discount => discount.discount_application.title === 'intelligems' )) ? options.inverse(this) : options.fn(this) ;
});
Handlebars.registerHelper('hasExtraDiscounts', function(arg1, options) {
    return arg1.some(discount => discount.discount_application.title !== 'intelligems' ) ;
});
</code></pre>

```liquid
{{#if discountsApplied}}
   {{#if (hasExtraDiscounts discounts)}}
      <small class="cart__price--strikethrough">{{{price}}}</small>
      <span class="ajaxcart__price">
          {{{discountedPrice}}}
      </span>
  {{else}}
      <small class="cart__price">{{{price}}}</small>
  {{/if}}
            
  {{else}}
     {{#if shouldShowComparePrice}}                                           
       <small class="cart__price--strikethrough">{{{comparePrice}}}</small>                                                                                    
     {{/if}}     
      <span class="ajaxcart__price {{#if shouldShowComparePrice}}tw-text-red{{/if}} ">
          {{{price}}}
      </span>
{{/if}}

{{#if discountsApplied}}
  <div class="text-right grid__item">
      {{#noIgDiscount discounts}}
          {{#each discounts}}
              <small class="ajaxcart__discount cart__discount">
                  {{this.discount_application.title}}
                  (-{{{this.formattedAmount}}})
              </small>
          {{/each}}
          {{else}}
      {{/noIgDiscount}}
  </div>
{{/if}}
```


# Step 5: QA your integration, and publish your changes

After you have completed all previous integration steps, go through your store using Preview Mode in (you can access preview mode by clicking on the Eye icon next to your test, or by adding /?ig-preview=true to the end of your website's URL) and make sure everything looks correct. Follow our QA checklist [here](https://docs.intelligems.io/price-testing/price-test-qa-checklist)!

Once you have verified Intelligems is fully integrated, you can publish your theme changes (if you haven't already) and start your test from the Intelligems App! Check out our step-by-step guide on doing this [here](https://docs.intelligems.io/price-testing/starting-a-price-test).

#### What happens next?

Now that you've started your first test, here are some things to do next:

* Check the Analytics Dashboard in the Intelligems app to see how the test is doing frequently. Note that it may take one to two hours for data to flow in!
* Start thinking about your [testing roadmap](https://docs.intelligems.io/getting-started/best-practices/test-design-best-practices).
* Review some [test suggestions](https://docs.intelligems.io/getting-started/common-use-cases).


# Integration Guide using Duplicate Products

Learn how to integrate your Shopify store with Intelligems for a Pricing Test using duplicate products.

Before you can run a Price Test on your Shopify store, there is a small integration that needs to be done. There are five components to the integration:

1. Add Intelligems JavaScript
2. Tag product prices
3. Hide duplicate products from collections pages
4. Configure duplicate products
5. QA your integration, and publish your changes

{% hint style="danger" %}
If you have chosen to have Intelligems complete the integration, many of these steps will be done on your behalf.
{% endhint %}


# Step 1: Add Intelligems JavaScript

## Introduction

If you have not already done so, you will need to add the Intelligems script to your site. There are two options below for doing this.

## Option 1: Use the App Embed Block

{% hint style="success" %}
This is the easiest installation method that works for most stores!
{% endhint %}

The fastest way to add Intelligems JavaScript to your theme is to enable it in the "Customize" section of your theme editor. You can do so by logging into your Shopify Admin, and navigating to Sales Channels > Online Store > Live theme - Customize > App Embeds. Search "Intelligems", make sure it is toggled on, and click "Save" in the top right.\
\
This will load Intelligems in a fashion that works optimally for performance and A/B testing on most stores. If for any reason you encounter performance concerns, see our docs on [performance optimization](https://app.gitbook.com/o/HNmChKUZY1pAEPfel38z/s/2SvefuMLsJyJPAcVXeWc/~/changes/736/performance-optimization/optimizing-your-price-test-integration).

{% hint style="warning" %}
For any **password protected store**, we will not be able to automatically detect the script, so you will continue to get an error message in the app regarding the script not being in your theme.
{% endhint %}

## Option 2: Add to Your Theme Code

{% hint style="info" %}
If you are on Shopify Plus and are still using checkout.liquid, you will still need to manually add Intelligems JavaScript to your checkout.liquid file in order to hide the discount or preview bar at checkout. Your individual script tag is located on the settings page in the Intelligems App.&#x20;
{% endhint %}

{% hint style="danger" %}
This will need to be manually removed if you uninstall Intelligems.
{% endhint %}

To complete this, go to the settings page in the Intelligems app. Once there, you'll see a section called "Theme Script". Click the blue button in that block that says "Copy Script". This will copy your unique Intelligems script to your clipboard.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FqvWfk91wEFeZyv5joSHW%2FScreenshot%202025-09-25%20at%205.30.44%E2%80%AFPM.png?alt=media&#x26;token=d06b3072-4307-499b-a878-b3b3ed6c9da8" alt=""><figcaption></figcaption></figure>

Now head over to your Shopify account, and paste the Intelligems Script as a source into the `<head>` of each of these files:

* theme.liquid
* any other theme.\*.liquid files (e.g., theme.gempages.liquid if you have this file)

Here's a video walking through those steps as well:

{% embed url="<https://www.loom.com/share/187128fe3b9c4334b5904d4c4de48dbf?sid=477d7023-fb18-4218-accd-fbd0775fee88>" %}


# Step 2: Tag product prices

## Introduction

To enable Intelligems to dynamically modify price elements for each test group during testing, it is essential to tag their locations on your website. This entails adding the query selector for price elements into the Intelligems configuration so the Intelligems plugin knows where those prices live. This guide will walk you through the process to do so.

{% hint style="warning" %}
Before you can use the Intelligems Widget, please confirm that you've added Intelligems JavaScript as a source into your theme.liquid file! See more on how to add our JavaScript to your site [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
{% endhint %}

## Step 1: Accessing the Widget <a href="#accessing-the-widget" id="accessing-the-widget"></a>

To get started, you'll need to create a price test in the Intelligems app, and open the Intelligems preview widget for that test. There are two ways to access the Intelligems Preview Widget:

1. Navigate to the "Tests" tab in the Intelligems app. Click on the eyeball icon to the right of the Price Test you have created. This will open a new browser window up with your website with the widget enabled.
2. You can also enter this mode by adding /?ig-preview=true to the end of your website's URL (e.g. <https://mystore.com/?ig-preview=true>). This will open a modal where you can choose which experiment you would like to see in the onsite widget. To tag prices, be sure to select a price test from this dropdown.

Once you are in Preview mode, select the "Edit" button followed by the dollar sign. The video below will walk you through this process:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FMISntvysIsTcu6doGJZj%2F12%20-%20preview%20selectors.gif?alt=media&#x26;token=37bcd4c1-0189-467c-be5e-884610cf47f5" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The Intelligems Widget offers full support for **Google Chrome**. Support for any other browsers is limited. If you are having an issue with the Widget in another browser, we suggest trying to run it in Google Chrome. For more support, please open a ticket with our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
{% endhint %}

## Step 2: Adding Price Selectors <a href="#adding-price-selectors" id="adding-price-selectors"></a>

Now that you are in Edit mode, it is time to tag price elements everywhere on your site. Follow the steps below:

1. **Enable price tagging mode** - Click the $ icon in the edit widget
2. **Enable price selector mode** - Click the box labeled 2 in the image below
3. **Tag price elements** - Move your cursor to see blue dotted lines around page elements. Click a price element to add it to the query selector list. Click Save to highlight the element:
   * <mark style="color:$success;">Green</mark> = product is in the test you are currently previewing
   * <mark style="color:blue;">Blue</mark> = product is **not** in the test you are currently previewing
   * If the price for a product in your test is highlighted in blue, Intelligems can't identify the product or variant ID - see [this guide](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting/how-to-add-the-data-product-id-and-or-data-variant-id-attribute-to-an-element) for the required theme change
4. **Tag all prices** - Add query selectors to the correct section (compare at price for strikethrough prices, price for regular prices, etc.) for all prices on your site, except for products added to your cart or your checkout page
5. **Save your work** - Click Save periodically to avoid losing progress

<div data-with-frame="true"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FFAVT2RDDlLDgDz8lteMN%2FScreenshot%202025-10-06%20at%2010.59.01%E2%80%AFAM.png?alt=media&#x26;token=2e249b15-67c0-4905-81ea-d67170b1db48" alt=""><figcaption><p>1. The type of selector - see more below for what each type is for.<br>2. Enable selector mode - clicking this button will allow you click on your prices on your site and automatically add a new selector.<br>3. Query selectors that have been added.<br>4. Delete a query selector.<br>5. Simplify a selector - use this function if the selector added was too specific.<br> 6. Add a query selector manually.<br>7. Auto add all price selectors on your site using AI.</p></figcaption></figure></div>

<details>

<summary>A few places to keep in mind as you tag all of the prices elements in your store include:</summary>

* Homepage
* Collection Pages
* Product Detail Pages (PDPs) - make sure you don't miss tagging any related or recommended products listed on your PDPs!
* Search Results Page or Bar, depending on where results show price
* Product Quiz
* Upsells in the cart or at checkout

</details>

<details>

<summary>Here are all of the different selector types:</summary>

**Price:** Use this section to select product prices on your store's site.

**Compare At Price:** Use this section to select compare prices on your store's site.

**Installment:** Use this section to select installments on your store's site. The default number of payments is 4. To change the payment amount, add the below to the element containing your installment in your theme.

```
data-payment-count="{{payment_amount}}" 
```

The Installment selector is compatible with installments that are:

1. Directly in your liquid
2. Not in the liquid, but is wrapped in its own \<span>

This selector is **not** compatible with installments that are:

1. Wrapped in a Shadow DOM
2. Not wrapped in its own span

**Savings (Price):** Use this option to select the dollar savings amount. This is normally located on your product pages.

**Savings (Percentage):** Use this option to select the percentage savings amount. This is normally located on your product pages.

**Cart Discount Message:** Use this option to hide a discount message (i.e. DISCOUNT or INTELLIGEMS) in your cart.

</details>

<details>

<summary>A few tips &#x26; tricks:</summary>

**Per Unit Prices.** If you have per unit prices listed for a product, you can follow these steps to update those prices accordingly during a price test:

1. Tag the per unit prices with a normal Price selector.
2. In your theme code, add `data-price-multiplier=".X"` to the per unit element, where X is what you want to multiple the price by. For example, if you wanted to show the per unit price when there are three units included, you would add `data-price-multiplier=".33"` to the element.

**Discounted Prices.** Many brands use the compare price field in Shopify to show a perceived discount - these are easy to tag using our various selector types. However, some brands will use a different method to show discounted prices by manipulating the frontend prices & using something like a Checkout Script to achieve a perceived discount. If this is the case for your store, follow these steps to accurately tag those prices:

1. Tag the per unit prices with a normal Price selector.
2. In your theme code, add `data-price-multiplier=".X"` to the discounted price element, where X is the inverse of the discount you are applying. For example, if you were running a 20% discount, you would add `data-price-multiplier=".8"` to the element.

</details>

You'll know you're done when all price, compare at price, installment and savings elements are highlighted in blue or green on all pages in your store!

{% hint style="warning" %}
Note that you **should not tag prices in the cart or cart drawer** as we will manage updating those using duplicate products.
{% endhint %}

{% hint style="info" %}
Having issues? Checkout our troubleshooting guide [here](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting) or submit a ticket to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
{% endhint %}


# Step 3: Hide duplicate products from collections pages

Find the liquid file that renders your collections pages. It may be called something like collection-page.liquid. Find the code block that renders each product in the collection and wrap it in the the following `unless` statement:

```liquid
{% unless product.tags contains "price_test" %}
 ...
{% endunless %}
```

In context, the code should look something like this:

```liquid
{% for product in collection.products %}
   {% unless product.tags contains "price_test" %}
      {%  
         render 'product-thumbnail',
         product: product
       %}
    {% endunless %}
{% endfor %}
```


# Step 4: Configure duplicate products

When you create and save a new price test in the Intelligems app, we will create a duplicate of each product that is in the test in your Shopify account. We will use these duplicate products to run your test. In most instances, we recommend using the original PDPs and only introducing the duplicate products upon add-to-cart.

To make sure that products are not displaying multiple times in places like third-party channels and collections, inventory is being properly tracked, shipping profiles are set up correctly, and discount codes still work, you'll need to follow the below steps to make a few changes to how the duplicate products are set up in Shopify.

{% hint style="info" %}
You'll need to follow these steps for *every* price test you set up.
{% endhint %}

<details>

<summary>Step 1: Finding duplicate products in Shopify.</summary>

The tag `price_test` will be added to all duplicates created by Intelligems, as well as a few additional tags specific to each test and test group.

However, the easiest place to access and check the status of your duplicate products is from directly within the Intelligems app! Next to any price test in the app, click the three dots on the far right to see more options, then select "View Duplicates". This will bring you to the duplicates status page.

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FUd33riBHWXAXLmJUJezo%2F13%20-%20View%20Duplicates.gif?alt=media\&token=e323be33-9e8b-4ed3-b53a-9d3db5ef3bfe)

From here, you can:

* See the status of duplicate products - you'll be warned about any issues in the top left, as well as in the `Shopify Status` and `Sync Status` columns!
* View duplicate products in Shopify - you can view all duplicates for this test by clicking the `View Duplicates in Shopify` button at the top, or individual duplicates by clicking on the icon in the `View in Shopify` column!

Navigating to your duplicate products through the Intelligems app will automatically filter your Shopify products by a tag that we have added for the experiment ID, meaning you will only see duplicate products for that specific test. There should be one product for each non-control group. So, if your test has three groups total, you should see two duplicate products.

\
If you would like to see duplicate products that have been created for *any* test, you can navigate to the Products menu and filter for products with the `price_test` tag.

</details>

<details>

<summary>Step 2: Remove duplicate products from third-party channels.</summary>

Follow these steps to remove the duplicate products from all channels other than `Online Store` and any that you use for reporting. This prevents any channels from showing multiple versions of the product with different prices.

**1.** Select all the products using the checkbox in the top left.

**2.** Select the three dots in the menu that pops up, followed by `Exclude from sales channel`.

**3.** De-select `Online Store` and any channels you use for reporting.

**4.** Select `Make products unavailable`.

</details>

<details>

<summary>Step 3: Configure inventory tracking.</summary>

The following steps will allow you to keep an accurate count of duplicate products sold during the test and reconcile inventory after the test. However, stores manage inventory differently - some through Shopify, some through an app, and some have another method. Please consider how selling duplicate products will impact your inventory tracking before following these steps and launching a test.

If you have inventory that turns over or sells out quickly, it may make sense to use this [Duplicate SKU Sync App](https://apps.shopify.com/duplicate-sku-sync) so that the inventory syncs between your products.

If your store uses a third-party application to manage inventory, please skip these steps. Please also note that third party apps that track inventory by SKU should not be affected by duplicating products as SKUs are copied to the duplicates. However, any app that uses product IDs or variant IDs to track inventory may need to be configured with the duplicate products. [Please reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have questions or concerns!

**1.** Set the inventory quantities for all duplicate products to zero, either through Shopify’s bulk editor or by clicking into the Shopify product page for each duplicate product.

**2.** Turn on `Continue selling when out of stock` for all variants.

If you use Shopify to track inventory, you'll need to reset this option to 'Stop selling when out of stock' once an item in your store goes out of stock.

</details>

<details>

<summary>Step 4: Add duplicate products to custom shipping profiles, if necessary.</summary>

*This step is only necessary if you have custom shipping profiles configured through Shopify. If only the General Shipping profile is used, you can skip this step.*

If any of the products you are testing are in a custom shipping profile, you'll need to add the duplicate products to the same profile following these steps:

**1.** From the Shopify admin console, navigate to `Settings` → `Shipping and Delivery`.

**2.** Click `Manage rates` for the relevant custom shipping profiles.

**3.** Within the shipping profile, click `Manage Products`.

**4.** Add the relevant duplicate products and variants to each custom shipping profile. You can search for `price_test` to show only the duplicate products. Click `Done` when you have selected all of the relevant products.

**5.** Back on the shipping profile page, click "Save".

</details>

<details>

<summary>Step 5: Add duplicate products to discount codes.</summary>

*This step is only necessary if you have discount codes configured for specific products or collections. If you do not have discount codes or all your discount codes are configured to apply store-wide, then you can skip these steps.*

**1.** Navigate to the `Discounts` tab on the left hand side of the Shopify admin page.

**2.** Filter for the discount code(s) you would like to add the duplicate products to. To quickly filter to discounts that may need to be edited, add a filter for `Active` status, and `Amount off products` and `Buy X Get Y` for type.

**3.** Select any codes that apply to `Specific products` where the products they apply to are part of the test. Use the search bar or browse feature to add all duplicate products that the discount should apply to. Keep in mind there should be one version of each product for each group in the test.

If you have any discount codes that apply to `Specific collections`, you'll need to create a collection with the duplicate product(s) first, then add that collection to the discount.

</details>

<details>

<summary>Step 6: Configuring search apps, if necessary.</summary>

If you use a search app, such as Searchanise, you may need to hide duplicate products in the search app. You can do this by adding `price_test` to "Hide products with these tags" in your search app settings.

</details>


# Step 5: QA your integration, and publish your changes

After you have completed all previous integration steps, go through your store using Preview Mode in (you can access preview mode by clicking on the Eye icon next to your test, or by adding /?ig-preview=true to the end of your website's URL) and make sure everything looks correct. Follow our QA checklist [here](https://docs.intelligems.io/price-testing/price-test-qa-checklist)!

Once you have verified Intelligems is fully integrated, you can publish your theme changes (if you haven't already) and start your test from the Intelligems App! Check out our step-by-step guide on doing this [here](https://docs.intelligems.io/price-testing/starting-a-price-test).

#### What happens next?

Now that you've started your first test, here are some things to do next:

* Check the Analytics Dashboard in the Intelligems app to see how the test is doing frequently. Note that it may take one to two hours for data to flow in!
* Start thinking about your [testing roadmap](https://docs.intelligems.io/getting-started/best-practices/test-design-best-practices).
* Review some [test suggestions](https://docs.intelligems.io/getting-started/common-use-cases).


# Troubleshooting

Learn how to address common price test integration issues.

## Background <a href="#intelligems-isnt-updating-a-price-for-a-product-that-is-included-in-the-test" id="intelligems-isnt-updating-a-price-for-a-product-that-is-included-in-the-test"></a>

If you notice that anything isn't working while you are completing the integration for a price test, such as the price not updating on the site, or adding to cart incorrectly, this is a great resource to help resolve your issues. If after reading through this document, you are still running into issues, please feel free to reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!

## Intelligems Isn't Updating a Price for a Product that is Included in the Test on the Homepage, Collection Page or Product Page <a href="#intelligems-isnt-updating-a-price-for-a-product-that-is-included-in-the-test" id="intelligems-isnt-updating-a-price-for-a-product-that-is-included-in-the-test"></a>

In addition to knowing which elements in your store are prices, Intelligems also needs to know which product and/or variant each price is for. Typically, Intelligems is able to figure this out automatically, but in some circumstances, you may need to set it explicitly on a price element. If a price on your website that is included in your test is not updating in preview mode, or is highlighted in blue in integration mode, that is a good sign that you need to follow [these steps](https://docs.intelligems.io/getting-started/pricing-integration-guides/troubleshooting/how-to-add-the-data-product-id-and-or-data-variant-id-attribute-to-an-element) to fix it.

## Intelligems Doesn't Add the Line Item Property <a href="#intelligems-doesnt-add-the-line-item-property" id="intelligems-doesnt-add-the-line-item-property"></a>

When adding a product that's being tested to the cart, Intelligems should add line item property \_igDiscount or \_igp. This indicates the amount of discount to apply to the line item or what the price of the line item should be to affect the correct price for the user's test group. Some common issues with this are:

* The add to cart happened on a page where the Intelligems Javascript was not loaded, such as a landing page that Intelligems has not been integrated with. Check the page source or network traffic to ensure that the Intelligems JavaScript snippet is loading on the page. Learn more about adding the Intelligems JavaScript snippet to your theme [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
* There's an error causing the Intelligems JavaScript to exit early. Check the JavaScript console for errors raised by Intelligems, and check the `window.igData.errors` object for any suppressed error messages.
* The add to cart is happening via a mechanism that Intelligems does not support, or skipping add to cart altogether. Common examples include quick buy buttons, third-party apps that use Draft Orders or landing pages that use checkout permalinks.

## Intelligems Doesn't Swap Duplicate Products When Adding to Cart <a href="#intelligems-doesnt-swap-duplicate-products-when-adding-to-cart" id="intelligems-doesnt-swap-duplicate-products-when-adding-to-cart"></a>

*This is applicable only to non-Shopify Plus stores.* When adding a product that's being tested to cart, Intelligems should swap the duplicate product in that corresponds to the user's test group, unless the user is in the control group, in which case Intelligems will not swap. Some common issues that may cause this to not work correctly are:

* The add to cart happened on a page where the Intelligems Javascript was not loaded, such as a landing page that Intelligems has not been integrated with. Check the page source or network traffic to ensure that the Intelligems JavaScript snippet is loading on the page. Learn more about adding the Intelligems JavaScript snippet to your theme [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
* There's an error causing the Intelligems JavaScript to exit early. Check the JavaScript console for errors raised by Intelligems, and check the `window.igData.errors` object for any suppressed error messages.
* The add to cart is happening via a mechanism that Intelligems does not support, or skipping add to cart altogether. Common examples include quick buy buttons, third-party apps that use Draft Orders or landing pages that use checkout permalinks.


# How to Add the data-product-id and/or data-variant-id Attribute to an Element

If a price on your website that is included in your test is not updating in preview mode, or is highlighted in blue, use this guide to resolve it.

### Background

One of the most common issues we see when completing the Intelligems Price Testing integration is that a price on your website that is included in your test is not updating in preview mode, or is highlighted in blue when it should be highlighted in green. This help guide will walk you through what theme change needs to be made to resolve this issue.

### **Step 1: Inspect the price that is not working**

On the price that is not updating, right click and select 'Inspect' from the menu. This will open up the developer tools in the same window.

### **Step 2: Find a unique combination of classes, IDs, and/or attributes**

In the developer tools, the element you are inspecting should be highlighted. In one of the **parent** elements for the price that is not updating, find a unique combination of classes, IDs, and/or attributes. In the screenshot below, `intelli-price intelli-span_USD_37.04`would be a good spot to start. However, you're not looking for this intelli-price class; you're looking for the `price-container__price` class in this case.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FsUafzmjrl68YYNUL0apa%2FScreenshot%202024-03-01%20at%203.07.23%20PM.png?alt=media&#x26;token=ce063551-16a7-4ff6-b398-1f5300a87cf2" alt=""><figcaption></figcaption></figure>

### **Step 3: Download the 'Shopify Theme File Search by EZFY' Chrome extension**

If you don't already have it, this Chrome extension will be extremely helpful! You can download it [here](https://chrome.google.com/webstore/detail/shopify-theme-file-search/mhchmhfecfdpaifljcfebnlaiaphfkmb).

### **Step 4: Open the code editor in Shopify**

In another window, got to your Shopify admin account and select 'Sales Channels' > 'Online Store' > the three dots next to the theme you are integrating with > ' Edit code'.

### **Step 5: Search the files**

Once in the theme file of your choice navigate to the `edit code` option of the themes dropdown. \\

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FD69RKK2bil0JXAlbGiYJ%2FScreenshot%202023-08-24%20at%2011.09.38%20AM.png?alt=media&#x26;token=521b70bc-5d21-4228-b4ff-64eb750bb470" alt=""><figcaption></figcaption></figure>

The Chrome extension you just downloaded should render a search box at the top of your screen like the one in the screenshot below once you are in the code editor. If you don't see it, you may need to refresh, or exit the code editor and come back by repeating the step above.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FEh20YwvUPm68dtl90dRJ%2FScreenshot%202023-08-24%20at%2011.12.07%20AM.png?alt=media&#x26;token=c2ba8f00-3a77-4388-a95a-626b7f0dd3c9" alt="" width="563"><figcaption></figcaption></figure>

In that search box, enter the unique combination of classes, IDs, and/or attributes that you found while inspecting your price in step 2. (It was `price-container__price` in the example above; yours will vary.) This will search all of your files, and any files that contains a match will be highlighted in blue.

{% hint style="danger" %}
If no matches are found, search for a smaller portion of the text.
{% endhint %}

### **Step 6: Search each .liquid file to find the text**

For each highlighted file with a .liquid extension, open the file and use keys Cmd + F to search the file for the text.

### **Step 7: Find the closest HTML open tag to the text.**

An opening tag begins a section of page content. To find the closest one to the text,

1\. Start from the highlighted text that you searched for.

2\. Keep moving left until you see an open tag.

3\. If there is no open tag directly to the left of the text, move one line up and start from the right end.

### **Step 8: Insert a data-product-id and/or data-variant-id snippet.**

Once you have found the closest HTML open tag, making sure there are spaces before and after, insert a data-product-id or data-variant-id snippet after the open tag using the below guidelines. Replace `product` with `variant` where necessary. With proper space, it should look similar to this:

```html
<span data-product-id="{{ product.id }}" class="{{ … }}"
```

1\. If there's code nearby where 'product' is being used (e.g. `{{ product.title }}`), insert `data-product-id="{{ product.id }}"`. If you don't see anything about 'product', go to number two.

2\. If you see a value that is being used like `product` but is named something else, replace `product.id` with `<whatever custom name>.title` in the data-product-id snippet. If you don't see any usage of 'product' or something similar in the file, go to number three.

3\. Try adding `data-product-id="{{ product.id }}"`. Save the file and go back to the window with your site open. Refresh and see if the price is now working. If not, please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for help.


# Replo Page Builder

Integrating Intelligems with Replo is easy!

### For Price Testing

For a price testing integration, we can add the following selectors to the theme integration:

**Price:** `[data-replo-price]`\
**Compare Price:** `[data-replo-compare-price]`\
**Savings ($):** `[data-replo-compare-difference]`\
**Savings (%):** `[data-replo-compare-percentage]`

Save these tags while [tagging your prices](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices).

{% hint style="warning" %}
When using the Find & Replace feature, take caution to not use any auto-generated classes when generating selectors. If you have questions, reach out to Intelligems support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).
{% endhint %}


# How to Set Up a Price Test

Check out the steps below to learn how to set up a price test!

## Step 1: Create a new test

Go to the **Tests** tab in the left menu in the Intelligems app. Click **Create New Test** above the experiments table.

Enter a **Name** and **Description** for your test. This information is internal only - add enough detail so you'll remember your goals when reviewing results weeks later. Select **Pricing Test** and **Create Test**.&#x20;

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F6vq64WLbytT2Bm4LLAq7%2Fpricing.gif?alt=media&#x26;token=0a2d3b3d-ed29-4b90-b697-f791f297a0a3" alt=""><figcaption></figcaption></figure>

## Step 2: Create your test groups

Create 2-5 groups by clicking **+**. Name each group and use the slider to allocate traffic percentage. Click **Next step** when ready.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F7rXH6W7Z0EHymi6N64wB%2Ftest%20groups.gif?alt=media&#x26;token=c2432f5b-546b-4b5f-9fb2-047b65967d02" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The more groups you have, the longer it will take to get statistically significant results. You’ll need about 300 orders for each group in the test to detect a 10% change in conversion with 90% confidence.
{% endhint %}

## Step 3: Choose your products

In the Modifications tab, click **+ Add/Remove Products** and select which products you want to include in the test by checking the boxes to the left of each product.

**A few tips and tricks:**

* You can select all products if you'd like to test your whole store, or all products matching the filters you have set up, by using the select all box at the top left-hand side of the table. Once you click the select all box, you will also need to click **Select all 20+ products in your store**.

{% hint style="info" %}
If you have subscription products, you may be missing the select all checkbox! Please reach out to [Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for assistance with this.
{% endhint %}

* Use the search bar at the top of the table if you are looking for a specific product
* The filter drop downs to the left of the table are helpful when looking for specific vendors, tags, product types, or statuses.

{% hint style="info" %}
If you have 250+ Product Types, Vendors or Product Tags set up in Shopify, Shopify will not allow us to load them all. In this case, you can use the search bar in the Intelligems app to filter instead. For example, if you were looking for all products with the product tag 'Test', you would want to search for 'tag:Test'. For product type, you would use 'product\_type:Test' and for vendor, you would use 'vendor:Test'. Please reach out to [Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions on this!
{% endhint %}

Once you have selected all necessary products, click 'Add' in the top right corner.

## Step 4: Set the test prices

There are three different options for filling in your prices:

<details>

<summary>Uploading a Spreadsheet</summary>

This is best suited for cases where you have already set up your prices in a CSV or Excel file.

To upload a spreadsheet, first click on the 'Quick Fill' button, navigate to the 'Fill By Upload' tab, and then click 'Download Template'. Wait until we load the template, then click 'Template Ready - Click to Download' - your download will start automatically.

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FrBIHVWP67ZZ2LqHaZTox%2F06%20-%20Download%20Template.gif?alt=media&#x26;token=80be507d-f588-4535-a084-cb095e826fb2" alt="" data-size="original">

Using Microsoft Excel, Google Sheets, Numbers, or another spreadsheet editing tool, manually input the prices for the test groups and save the file with a .csv, .xls or .xlsx extension.

The following fields (columns) are **required** in the uploaded file.

* product\_title
* product\_id
* variant\_title
* variant\_id
* handle
* Price - \[Test Group Name] (*for each test group*)
* Compare Price - \[Test Group Name] (*for each test group*)

The rest of the fields in the template are provided for reference and are not required.

\
Back in the Intelligems app, click the 'Upload Prices' button and select the saved .csv, .xls or .xlsx file. Once it has uploaded, save the test to see the price changes.

</details>

<details>

<summary>Quick Fill</summary>

This is best suited for cases where you want to test uniform changes to all products in the test, such as a 10% or $10 dollar increase and decrease across all test products. Autofill is based on the control group product prices that are pulled in from Shopify.

To use this option, click 'Quick Fill', then configure the percentage or dollar amount change for each group and whether the change should be an increase or decrease relative to the control, as well as whether the amount should be rounded. Note that increase / decrease, the amount and % / $ selector are three separate fields. Click 'Apply All' when you are done.

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F0RDgQkDlG8MMtHcdqz8l%2F07%20-%20Quick%20Fill.gif?alt=media\&token=dd02fc45-69ce-4f74-8b65-a09feb76b407)

</details>

<details>

<summary>Manually Set Prices</summary>

This is best suited for cases where you'd like to configure the prices for each product separately, such as a $10 increase to Product A and a $5 increase to Product B.

Input the prices and 'compare at' prices (if desired) for each product and test group in the table. You can drag prices from one cell to the next if the prices are the same.

You can expand all rows or collapse all rows by pressing 'Expand All' or 'Collapse All' at the top left of the table.

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FJ7SqKvlfklqmyXatDXgl%2F08%20-%20Set%20Prices%20manually.gif?alt=media\&token=542965aa-aac0-41f7-8880-c9e3c1ca0ed1)

</details>

{% hint style="info" %}
There are two relevant fields for each entry:

* Price: The price of the product; this is the price the user will actually be charged when they purchase the product in the given test group, before any discounts.
* Compare Price: Also known as the 'compare at price', this price will be shown as a strikethrough. This field is optional and there is no need to populate the 'Compare Price Field' if you do not wish to show a strikethrough. Your theme must be configured to show strikethroughs in order for Intelligems to display one.
  {% endhint %}

Click 'Next step' when you are done setting up your prices.

## Step 5: Set up targeting if needed

Targeting is an optional step. By default, a visitor will be immediately assigned to one of the test groups using its random split-test mechanism. This assignment is determined at the first visit and is stored via a first‐party cookie, ensuring that the visitor remains in the same group on subsequent visits during the price test period.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the [Mutually Exclusive Tests](https://docs.intelligems.io/general-features/targeting/mutually-exclusive-experiments) option.

You can learn more about targeting [here](https://docs.intelligems.io/general-features/targeting)! Once you are done setting up targeting, or if you're skipping this step, click 'Next step'.

## Step 6: Save and Preview your Test

Once you have completed all the steps, you'll be able to save your test with the green **Save** button in the top right.

In the **Preview** tab, you'll find a few options to load the test's preview:

* **Open Full Screen Preview:** this will open your website with the Intelligems widget loaded, so you can easily alternate between test groups to preview each group's experience, as well as do onsite edits if necessary (see [step 8](#step-8-edit-content-on-your-site-if-needed) for more details). You can also choose which theme you'd like to preview in if you need to be somewhere other than your live theme!&#x20;
* **Open Mobile Preview:** you'll see a QR code for each test group, so you can load the preview directly on your mobile device.&#x20;
* **Copy Preview URL:** this will copy the preview URL to your clipboard automatically.

{% hint style="danger" %}
Don’t worry, this won’t set the test live yet and you can come back and edit if you need to make changes!
{% endhint %}

## Step 7 (optional): Set up your Goals

In the 'Goals' tab, you'll find the option to select what your primary goal is, as well as whether analytics should by default consider only orders containing certain products, or orders containing any products in your shop.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FfiUXNdv1Tqp3bxMhEhU7%2Fimage.png?alt=media&#x26;token=949795fa-51f5-4370-9769-0aa2bf5d5aec" alt=""><figcaption></figcaption></figure>

Neither of these choices will affect what data is tracked or available to view, but will allow Intelligems to display analytics so that the most important information is surfaced first. You can change this later after the test has started by changing the option in your Analytics filters.

## Step 8 (optional): Edit content on your site if needed

This step is also optional. This tool allows you to dynamically update content on your site based on a visitor's test group. Check out [this article](https://docs.intelligems.io/general-features/onsite-editor) for more details on configuring this option.

Please note this is not how you should update price components on your site for a Price Test - that should be completed by [tagging your prices](https://docs.intelligems.io/getting-started/pricing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices)!

## What happens next?

Now that you've created your pricing test, you can QA your test using [this checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist)! If you have not completed the integration yet, please see our integration guides [here](https://docs.intelligems.io/price-testing/price-testing-integration-guides).


# Price Test QA Checklist

Use this checklist to QA every Price Test before hitting start!

This QA list is specific to a price test. If you are QAing a shipping test, please check out [this article](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist)!

Before heading to your site, there are a few things you should check to make sure your integration is functional:

* [ ] Is Intelligems JavaScript in your live theme? Check out [this article](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) for more information on where to find this.
* [ ] If you are using the [Checkout Script integration](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts), is the Intelligems Checkout Script live in the Script Editor app?

Once you have confirmed both of those items are true, you can preview the test on your live site. Enter Preview mode by clicking the `...` next to your test and select `Preview`

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FIzg2aHQBECwHQ4Xl6CQc%2F10%20-%20Open%20Preview.gif?alt=media&#x26;token=e61108ce-6657-46a5-89d3-8368d08b4f49" alt=""><figcaption></figcaption></figure>

This will open your site up in a new window with the Intelligems preview widget enabled. In the preview widget, you'll see:

1. The name of the test you are previewing in the top left
2. A dropdown to switch between different test groups in the bottom left
3. A toggle to highlight any replacements in the top right
4. An edit button in the bottom right. This enables integration mode where you can edit price selectors and text replacements

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F5H4JjgIvisCTzXuqr77A%2Fimage.png?alt=media&#x26;token=b133337b-4e23-43fd-9f99-a238c239529d" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Please note that if you sell in multiple currencies, a price test which includes prices higher than the control group's prices may have implications for any non-default currencies if they are set to dynamically convert against your store's default currency.\
\
In Shopify Markets, or wherever your store's currency pricing is managed, be sure to set non-default currency prices as fixed/static for the duration of the test if you would like to avoid any unintended price increases in these markets.
{% endhint %}

To get started in preview mode, turn the `Highlight Replaces` toggle on in the top right corner of the widget to highlight the prices in your test. This will highlight all of the prices that have been tagged on your site in green or blue.

* [ ] Confirm that any prices tagged in green *are* part of the test. Green highlighting means we recognize that element is a price, and *it is being changed* by the Intelligems app in accordance with the different groups for the test you are previewing.
* [ ] Confirm that any prices tagged in blue *are not* part of the test. Blue highlighting means we recognize that element is a price, but *it is not* being changed by the Intelligems app because that product is not included in the test you are previewing. This is important as you may test this price in the future, so we want to make sure we know its a price.
  * [ ] Is the price of a product *that is included in the test* highlighted blue? This most likely means that we are not able to tell which product and/or variant ID this price is for. Follow [these steps](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting/how-to-add-the-data-product-id-and-or-data-variant-id-attribute-to-an-element) to add the `data-product-id` and/or `data-variant-id` attribute to that price element so that we are able to tell which product it is for.
* [ ] Confirm that the price for each product and variant that are part of the test matches the test designed in the app for all test groups. You can switch groups with the drop down in the bottom left corner of the preview widget. A few pages we recommend checking:
  * [ ] Homepage
  * [ ] Collection Pages
  * [ ] Search Bar
  * [ ] Search Results
  * [ ] Product Page
  * [ ] Recommended Items on Product Page (e.g. `You May Also Like` or `Recently Viewed`)
  * [ ] Upsells in Cart
  * [ ] Product Quiz
  * [ ] Landing pages
  * [ ] Navigation
* [ ] Confirm that the below is all true on the Product Page:
  * [ ] The correct price displays for each test group. Be sure to check out different variants if this is an option.
  * [ ] Bulk purchase and/or subscription options match the live site and/or test design.
  * [ ] Ratings and/or reviews match the live site.
  * [ ] Other media, such as images, video and text, match the live site.
  * [ ] Text is being updated if it references price. For example, text that says `20% off for subscriptions` or references value of individual items in a bundle should update accordingly.

Now that you have confirmed prices look right everywhere on the site, go through the add to cart process and click checkout for a handful of products that are a part of the test.

* [ ] Confirm that status of duplicate products (if not on Shopify Plus) has been changed from Draft to Active.
* [ ] Confirm price is being calculated correctly at each step (e.g. in the mini cart, on the cart page, and on the checkout page) based on which test group is selected in the widget. *Note that if you are using Duplicate Products for your test, the price should match the test group in the cart.*
* [ ] Increase the quantity of a test item to two from within the cart; confirm that the prices are still correct.
* [ ] If you offer options other than one-time purchase, such as subscription or bulk, confirm that these are correct at each step.
* [ ] If there is custom code for creating bundles within the site (i.e. if you add all the products that are part of the bundle and the discount is applied), confirm that functionality is working properly.
* [ ] If you have a quick buy button (e.g., Buy with ShopPay) in cart or at checkout, confirm that the price is correct when you use this functionality. Please note that these buttons likely won't work for price tests if they are found on the PDP or collections pages.
* [ ] Confirm that `ig_discount` or other `ig_items` are not showing in the cart or at checkout.
* [ ] Confirm that any payment plan options (e.g. AfterPay or ShopPay) are calculating monthly payments correctly if available.
* [ ] Compare shipping rates to the live site. This is most relevant if there are custom shipping rates set up.
* [ ] Add to cart from all landing pages from different test groups and confirm the price at checkout is correct.
* [ ] **We highly recommend placing a test order. This is particularly important in the below scenarios:**
  * [ ] If you are testing subscription products - once you have placed your test order, check the refill prices in your subscription app.
  * [ ] If you use Line Item Properties for any information that is pertinent after the order has been submitted, such as customization information. **If you are not on Shopify Plus, these Line Item Properties are not compatible with Functions, and they will be wiped from the order.**

{% hint style="info" %}
Check all of the above items in mobile as well. Here is a [guide](https://www.browserstack.com/guide/view-mobile-version-of-website-on-chrome) on how you can view mobile mode on your desktop on Chrome.
{% endhint %}

Once you have confirmed all of the above items look correct, you can hit start on your test in the app! Please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions.


# Starting a Price Test

Learn how to launch a Price Test in the Intelligems app.

## **Step 1: Confirm Intelligems script is in your live theme**

In addition to Intelligems Javascript, confirm any other theme changes completed during the integration are in your live theme as well. **If not**, please publish the script and any changes before proceeding.

## **Step 2: Press the Start Button**

In the Intelligems app, navigate to the A/B Tests tab and click the play button next to the pricing test you are wanting to start.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fssi9JaM6zTCfpLWA8liS%2Fimage.png?alt=media&#x26;token=b308fe22-23d5-4855-8c5d-aa722976c706" alt=""><figcaption></figcaption></figure>

## **Step 3: confirmed you've done the integration and also QA'd your test**

At this point, we display two checkboxes so you can confirm you've done the [Price Test Integration](https://docs.intelligems.io/price-testing/price-testing-integration-guides), and that you've also [QA'd your test](https://docs.intelligems.io/price-testing/price-test-qa-checklist). If you've done both, check both checkboxes, and click 'Confirm'.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F4ihzzcgIjP2Aem4ywx80%2Fimage.png?alt=media&#x26;token=8bf294e2-6063-4e99-8c4e-6016bd55ca47" alt=""><figcaption></figcaption></figure>

## **Step 4: Click "Yes, Update My Prices and Start Test"**

**If C*****heckout Scripts***\*\* or **\_**&#x46;unction&#x73;**\_** are being used to run your test,\*\* after you click `Start`, you'll see a pop-up asking if you want the Intelligems Wizard to update your Shopify prices. Please select 'Yes, Update My Prices and Start Test' in the pop-up. This will allow Intelligems to automatically update your product prices to the highest price in the test for each product, which is necessary for your test to run correctly.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FVYG7p7vw37hw9cyEk19G%2Fimage.png?alt=media&#x26;token=730ccbb1-e2e6-4113-aebd-8466e0970856" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
While there are certain scenarios where prices do not need to be updated, we do not recommend selecting "No, I'll Update My Prices" unless you 100% know what you're doing!
{% endhint %}

**If \_duplicate products**\_\*\* were used to create the test,\*\* this pop up will not come up. Instead, you'll see a modal displaying your duplicate products, and the option to start the test. Duplicate products were created when you set your test up for each price group. As long as you followed [these steps](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-duplicate-products/step-4-configure-duplicate-products)[ ](https://docs.intelligems.io/getting-started/price-testing-integration-guides/integration-guide-using-duplicate-products/step-4-configure-duplicate-products)to configure your duplicate products, your test is ready to go, so you can click on 'Start Test'.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F7x6sSsfakeWhKiCOKT1c%2Fimage.png?alt=media&#x26;token=4d69231e-72c8-4d20-8dd0-a4101760891a" alt=""><figcaption></figcaption></figure>

## **Step 4: Check Your Site**

Now that the test is live, we recommend going through the add to cart and checkout process in a few incognito browsers so you can get added to different test groups and ensure everything is working as expected. If you have not already QA'd your test before launching it, we recommend going through [this checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist). Please [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) with any issues!


# Ending a Price Test

Follow these steps to end your Price Test.

## Step 1: Press the Stop Button

To end a test, navigate to the Tests tab in the menu on the left-hand side of the Intelligems app. Once you're there, locate the test you'd like to end in the Intelligems tests list and click the stop button, which you can find circled in red below.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FuDAciQN5YXXqpcEaGhQ8%2FScreenshot%202025-09-25%20at%205.19.41%E2%80%AFPM.png?alt=media&#x26;token=35158b64-241d-49f5-9cc8-c130cb072471" alt=""><figcaption></figcaption></figure>

## Step 2: Roll Out Prices

Once you click the stop button, a modal will pop up with the key metrics for each test group. Choose which group's prices to implement in Shopify, then click Apply Prices and End Test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FZb8Lxb4TVG6JIiCxdN6X%2FScreenshot%202025-09-25%20at%205.14.09%E2%80%AFPM.png?alt=media&#x26;token=9cdad65c-d434-4c7c-9be0-99a5504141df" alt=""><figcaption></figcaption></figure>

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

If ***checkout scripts*** were used to run the test, there is no action needed here! By default, subscriptions will continue to run at the price the customer subscribed, which may not always be equal to the price on your site.&#x20;

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


# Testing Prices with Subscriptions

Read this article to understand how to run price tests if your store offers subscriptions.

## Introduction

If you offer subscriptions as an option on your product(s), testing prices is a bit more complex. Intelligems supports testing both one-time and subscription prices for your store's products, and this article will walk through the basics on what is possible, and how to get started.

{% hint style="warning" %}
Testing subscriptions is currently only supported on our annual plans. Please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are interested in testing subscriptions.
{% endhint %}

## What kind of subscription tests are supported?

Intelligems supports a wide variety of tests on subscription products. Some examples include:

* Testing different one-time prices while keeping subscription discount percentages consistent
* Testing different one-time prices while keeping subscription prices consistent
* Testing different subscription discounts

## How does Intelligems implement subscription tests?

Generally, Intelligems implements subscription tests by creating duplicate products (one duplicate per test group for each product). Duplicate products are often required because subscription providers display one-time and subscription prices on PDPs directly based on the product URL. Therefore, a separate product needs to be created to show different prices. To learn more about how these products will be configured, check out our article [here](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/managing-duplicate-products-when-redirecting-to-duplicate-pdps).

If your store is on Shopify Plus and uses Recharge 2.0 or Stay.ai, we may be able to implement your test without duplicate products. Please [contact us](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to learn more.

## Which subscription apps is Intelligems compatible with?

Intelligems is generally compatible with all major subscription providers. Most require us to create duplicates of the products you want to test. See below for a list of subscription providers and implementation methods available for each.

| **Provider**                    | **API + Checkout Scripts** | **Duplicate Products** |
| ------------------------------- | -------------------------- | ---------------------- |
| Recharge 2.0 (Unified Checkout) | ✓                          | ✓                      |
| Stay.Ai                         | ✓                          | ✓                      |
| Skio                            |                            | ✓                      |
| Prive                           |                            | ✓                      |
| Smartrr                         |                            | ✓                      |
| Loop                            |                            | ✓                      |
| Ordergroove                     |                            | ✓                      |

## Which Intelligems plans qualify for subscription testing?

You must be on an annual plan that includes price testing to qualify for subscription testing.

## Can I perform the integration with Intelligems on my own if I offer subscriptions?

Testing subscriptions often requires a more involved integration & setup than typical price tests. As a result, we recommend having Intelligems perform the integration if this applies to your store. [Reach out to our support team to learn more](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!

## I've read all of the above and am ready to set up my test. How do I do this?

Check out the guides below to learn more about setting up a price test where subscription products are involved:

{% content-ref url="testing-prices-with-subscriptions/testing-prices-with-recharge-2.0-or-stay.ai" %}
[testing-prices-with-recharge-2.0-or-stay.ai](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/testing-prices-with-recharge-2.0-or-stay.ai)
{% endcontent-ref %}

{% content-ref url="testing-prices-with-subscriptions/how-to-set-up-a-price-test-using-duplicate-products-and-recharge-subscriptions" %}
[how-to-set-up-a-price-test-using-duplicate-products-and-recharge-subscriptions](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/how-to-set-up-a-price-test-using-duplicate-products-and-recharge-subscriptions)
{% endcontent-ref %}

{% content-ref url="testing-prices-with-subscriptions/how-to-set-up-a-price-test-using-duplicate-products-and-skio-subscriptions" %}
[how-to-set-up-a-price-test-using-duplicate-products-and-skio-subscriptions](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/how-to-set-up-a-price-test-using-duplicate-products-and-skio-subscriptions)
{% endcontent-ref %}

{% content-ref url="testing-prices-with-subscriptions/managing-duplicate-products-when-redirecting-to-duplicate-pdps" %}
[managing-duplicate-products-when-redirecting-to-duplicate-pdps](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/managing-duplicate-products-when-redirecting-to-duplicate-pdps)
{% endcontent-ref %}


# Testing Prices with Recharge 2.0 or Stay.Ai

This document shows how to set up Intelligems if you want to test prices and you're using Recharge 2.0 or Stay.ai.

{% hint style="danger" %}
This article only applies if you use Stay.AI or Recharge (Unified Checkout aka 2.0), you are using Shopify Plus, and have access to the Script Editor app. If you are using Stay.AI, you must also only offer one delivery option (i.e. Every 30 Days). If any of these are not true, please see our following guides on using duplicate products, or reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).
{% endhint %}

### Step 1: Authorize the integration

In the Intelligems App, navigate to "Integrations" on the bottom left.

<details>

<summary>Recharge</summary>

In the Integrations page, click "Enable" next to the Recharge icon. If instead of "Enable" you see the word "Refresh", your integration is already enabled and no need to take further action!

Then click "Install" when you see this screen.

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FAmoM5uRzRHr5nvy91tBp%2Fimage.png?alt=media\&token=c477c193-24b4-4f23-80fc-41f754fe924f)

</details>

<details>

<summary>Stay.ai</summary>

You need to create an API key from your Stay.AI dashboard. Log into Stay, under Settings > API keys, create a new key.

* Name: **Intelligems**
* Description: **Used for Intelligems <> Stay Integration**
* Email: **Your email**
* Scopes: **All**

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FbvHSG1jhVtvrhFSzBCCy%2Fimage.png?alt=media\&token=658b4326-5baf-4bbf-992a-d0aec1ae4d6f)

Then Copy the API key into the Intelligems dashboard into the Stay.ai API key

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FXnIDukimdM14Idid03lp%2Fimage.png?alt=media\&token=de3a4f98-a4d2-4f02-853d-31dbdbb3bbf2)

</details>

### Step 2: Set up test in the Intelligems app

See our detailed guide [here](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test) on setting up your Price Test. Make sure to do this ***after*** you have authorized the integration with your subscription provider. If you have not, you should delete your old test and create a new test from scratch.

### Step 3: QA your test

Assuming you've already completed the [integration](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts) that is required for Price Testing, the next step is to QA your test! Because tests that involve subscriptions have more moving pieces, we recommend spending some extra time on QA - follow [this checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist) to make sure you don't miss anything!

### Handling custom widgets and UI

If you're not using a standard widget from your subscription provider on your PDP, our onboarding team would be happy to help integrate your own custom UI with Intelligems. It's relatively straightforward, we just need to identify the PDP elements identified in this example screenshot.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FDQLccDDOEk5nGYPGS9oQ%2Fimage.png?alt=media&#x26;token=e4c5e86b-8d0e-4e47-b209-61957f447e6a" alt=""><figcaption></figcaption></figure>

If you have questions, please reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!


# How to Set Up a Price Test using Duplicate Products and Recharge Subscriptions

Learn how to set up a Pricing Test using duplicate products and Recharge Subscriptions.

{% hint style="danger" %}
Testing subscriptions often requires a more involved integration and setup than typical price tests. As a result, we recommend having Intelligems perform the integration if this is something you would like to test. Reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for help!
{% endhint %}

{% hint style="info" %}
**Prerequisites:** Prior to setting up your test, please reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to confirm your account is set up with duplicate products and redirection, both of which are required for you to price test. Duplicate products are only required in the case that you do not have access to the Script Editor app, or use Recharge 1.0.
{% endhint %}

## Step 1: Set up test in the Intelligems app

Once you have confirmed the above with support, you can set up your test in the Intelligems app as you normally would! See our detailed guide [here](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test).

## Step 2: Configure your duplicate products in Shopify

If you have not already, follow [these steps](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/managing-duplicate-products-when-redirecting-to-duplicate-pdps) to configure your duplicate products in Shopify.

## Step 3: Add your duplicate products to your subscriptions in Recharge

In Recharge, follow these steps:

1. Go to `Products` on the left hand side.
2. Click `Add Product` in the top right.
3. Select all of your duplicate products and click `Add Products`.
4. Once you have added them, they will show up in the list with all of your other subscription products, but they will have no `Collections` or `Subscription type`.
5. You can now either click into each duplicate product and update the subscription settings individually, or select all of the duplicate products using the checkboxes on the left and click `Update subscription settings` at the top.
6. Confirm that you have set up the subscription type, order schedule and discount for each new duplicate product.

## Step 4: Confirm subscription duplicate products are set up correctly

Once you complete step 3, Recharge will automatically create another duplicate product for each test product in Shopify. The Recharge duplicates will have the subscription discount in the product title, making them easy to find.

These products should be set up correctly, but we recommend confirming the prices match what you expect and that the products are set to active. The prices on the subscription duplicate products should be equal to the price after the subscription discount.

We also recommend adding a tag, such as 'Price\_Test\_Subscription\_Duplicate', to make these products easy to find in the future.

## Step 5: Consider any Recharge apps that may be impacted

Many brands use Recharge apps, such as Workflows, to accomplish various things. If you use any apps, make sure these are set up to work with your new duplicate subscription products. A few things to keep in mind here are any apps that rely on product IDs or names as these may not match!

## Step 6: QA your test

Because tests that involve subscriptions have more moving pieces, we recommend spending some extra time on QA - follow [this checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist) to make sure you don't miss anything!


# How to Set Up a Price Test using Duplicate Products and Skio Subscriptions

Learn how to set up a Pricing Test using duplicate products and Skio Subscriptions.

{% hint style="danger" %}
Testing subscriptions often requires a more involved integration and setup than typical price tests. As a result, we recommend having Intelligems perform the integration if this is something you would like to test. Reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for help!
{% endhint %}

{% hint style="info" %}
**Prerequisites:** Prior to setting up your test, please reach out to support [here ](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)to confirm your account is set up with duplicate products and redirection, both of which are required for you to price test.
{% endhint %}

## Step 1: Set up test in the Intelligems app

Once you have confirmed the above with support, you can set up your test in the Intelligems app as you normally would! See our detailed guide [here](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test).

## Step 2: Configure your duplicate products in Shopify

If you have not already, follow [these steps](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/managing-duplicate-products-when-redirecting-to-duplicate-pdps) to configure your duplicate products in Shopify.

## Step 3: Add your duplicate products to your subscriptions in Skio

In Skio, follow these steps:

1\. Go to `Products` on the left hand side.

2\. Click `Add product` in the top right if you would like to add products one at a time, or `Bulk operations` if you'd like to add multiple products at the same time.

3\. If you have opted to add products one at a time, find the product you want to add in the list and select it. Enter all of the required subscription information, and click `Save` in the top right. If you have opted to add your products in bulk, you have the option between uploading a CSV or bulk creating subscription plans.

## Step 4: Confirm subscriptions are set up correctly

Once you complete step 3, subscription options should be available on your duplicate products. Confirm that they are working as expected by going to the Preview of your duplicate products from the Shopify admin.

## Step 5: Consider any Skio workflows that may be impacted

Many brands use Skio workflows, such as Rules or Quick Actions, to accomplish various things. If you use any of these, make sure they are set up to work with your new duplicate subscription products.

## Step 6: QA your test

Because tests that involve subscriptions have more moving pieces, we recommend spending some extra time on QA - follow [this checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist) to make sure you don't miss anything!


# Managing Duplicate Products when Redirecting to Duplicate PDPs

For more complex sites, Intelligems can duplicate products for Price Tests. Here we'll walk you through the steps to configure and activate these duplicate products.

### Overview

In specific, more complex cases, we may use duplicate products to run your price test. In most instances, we recommend using the original PDPs and only introducing the duplicate products upon add-to-cart. However, there are certain instances where using the PDP for the duplicate product may be necessary, including:

1. Testing subscription products with most subscription providers
2. Testing significant PDP changes
3. Testing prices when you offer a bundle discount on the PDP through Kaching or Shrine

{% hint style="info" %}
We have built-in PDP Quanity Buttons you can implement and use for price tests via our **Global Styles** components
{% endhint %}

In order to use the duplicate PDPs, you'll need to confirm that both **Should Duplicate Products** and **Should Redirect** are enabled in the Advanced Settings menu in the Intelligems app. If you do not see this option, you may need to request access to this menu by contacting our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).

To make sure that products are hidden from third-party channels and collections, inventory is being properly tracked, shipping profiles are set up correctly, and discount codes still work, you'll need to follow these steps to make a few changes to how the duplicate products are set up in Shopify.

{% hint style="info" %}
You'll need to follow these steps for *every* Price Test you set up.
{% endhint %}

<details>

<summary>Step 1: Finding duplicate products in Shopify</summary>

The tag `price_test` will be added to all duplicates created by Intelligems, as well as a few additional tags specific to each test and test group.

However, the easiest place to access and check the status of your duplicate products is from directly within the Intelligems app! Next to any price test in the app, click the three dots on the far right to see more options, then select "View Duplicates". This will bring you to the duplicates status page.

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FUd33riBHWXAXLmJUJezo%2F13%20-%20View%20Duplicates.gif?alt=media\&token=e323be33-9e8b-4ed3-b53a-9d3db5ef3bfe)

From here, you can:

* See the status of duplicate products: you'll be warned about any issues in the top left, as well as in the `Shopify Status` and `Sync Status` columns.
* View duplicate products in Shopify: you can view all duplicates for this test by clicking the `View Duplicates in Shopify` button at the top, or individual duplicates by clicking on the icon in the `View in Shopify` column.

Navigating to your duplicate products through the Intelligems app will automatically filter your Shopify products by a tag that we have added for the experiment ID, meaning you will only see duplicate products for that specific test. There should be one product for each non-control group. So, if your test has three groups total, you should see two duplicate products.

If you would like to see duplicate products that have been created for *any* test, you can navigate to the Products menu and filter for products with the `price_test` tag.

</details>

<details>

<summary>Step 2: Remove duplicate products from third-party channels</summary>

Follow these steps to remove the duplicate products from all channels other than `Online Store` and any that you use for reporting. This prevents any channels from showing multiple versions of the product with different prices.

**1.** Select all the products using the checkbox in the top left.

**2.** Select the three dots in the menu that pops up, followed by `Exclude from sales channel`.

**3.** De-select `Online Store` and any channels you use for reporting.

**4.** Select `Make products unavailable`.

</details>

<details>

<summary>Step 3: Remove duplicate products from collections</summary>

Follow these steps to remove the duplicate products from all collections. This prevents both versions of duplicate products from appearing in collections on the website.

**1.** Select all the products using the checkbox in the top left.

**2.** Select the three dots in the menu that pops up, followed by `Remove from collection(s)`.

**3.** Select all collections.

**4.** Select `Save`.

If you use **auto-collections** on your site, specifically to power any collection pages, you may **need to do a couple extra steps here to exclude duplicate products from those pages.** How you manage this may depend slightly on how you have your auto-collections set up, but we typically find that updating the duplicate products' **Product Type** to **Test Products** and then excluding that product type from any auto-collections to be a great solution. [Please reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you need assistance with this.

</details>

<details>

<summary>Step 4: Configure inventory tracking</summary>

The following steps will allow you to keep an accurate count of duplicate products sold during the test and reconcile inventory after the test. However, stores manage inventory differently, some through Shopify, some through an app, and some though other methods. Please consider how selling duplicate products will affect your inventory tracking before following these steps and launching a test.

If you have inventory that turns over or sells out quickly, it may make sense to use this [Duplicate SKU Sync App](https://apps.shopify.com/duplicate-sku-sync) so that the inventory syncs between your products.

If your store uses a third-party application to manage inventory, please skip these steps. Please also note that third party apps that track inventory by SKU should not be affected by duplicating products as SKUs are copied to the duplicates. However, any app that uses product IDs or variant IDs to track inventory may need to be configured with the duplicate products.

**1.** Set the inventory quantities for all duplicate products to zero, either through Shopify’s bulk editor or by clicking into the Shopify product page for each duplicate product.

**2.** Turn on `Continue selling when out of stock` for all variants.

If you use Shopify to track inventory, you'll need to reset this option to **Stop selling when out of stock** if an item in your store goes out of stock.

</details>

<details>

<summary>Step 5: Add duplicate products to custom shipping profiles, if necessary</summary>

*This step is only necessary if you have custom shipping profiles configured through Shopify. If only the General Shipping profile is used, you can skip this step.*

If any of the products you are testing are in a custom shipping profile, you'll need to add the duplicate products to the same profile following these steps:

**1.** From the Shopify admin console, navigate to `Settings` → `Shipping and Delivery`.

**2.** Click `Manage rates` for the relevant custom shipping profiles.

**3.** Within the shipping profile, click `Manage Products`.

**4.** Add the relevant duplicate products and variants to each custom shipping profile. You can search for `price_test` to show only the duplicate products. Click `Done` when you have selected all of the relevant products.

**5.** Back on the shipping profile page, click **Save**.

</details>

<details>

<summary>Step 6: Add duplicate products to discount codes as needed</summary>

*This step is only necessary if you have discount codes configured for specific products or collections. If you do not have discount codes or all your discount codes are configured to apply store-wide, then you can skip these steps.*

**1.** Navigate to the `Discounts` tab on the left hand side of the Shopify admin page.

**2.** Filter for the discount code(s) you would like to add the duplicate products to. To quickly filter to discounts that may need to be edited, add a filter for `Active` status, and `Amount off products` and `Buy X Get Y` for type.

**3.** Select any codes that apply to `Specific products` where the products they apply to are part of the test. Use the search bar or browse feature to add all duplicate products that the discount should apply to. Keep in mind there should be one version of each product for each group in the test.

If you have any discount codes that apply to `Specific collections`, you'll need to create a collection with the duplicate product(s) first, then add that collection to the discount.

</details>

<details>

<summary>Step 7: Configure search apps, if necessary</summary>

If you use a search app, such as Searchanise, you may need to hide duplicate products in the search app. You can do this by adding `price_test` to "Hide products with these tags" in your search app settings.

</details>

<details>

<summary>Step 8: Configure duplicate products in third-party apps</summary>

The following steps will help you configure duplicate products within third-party apps, if necessary.

Note that if you **don't see your duplicate products** in a third-party app, you may need to set your duplicate products to 'Active' status in Shopify in order to access them. Don't worry - as long as you've completed the above steps, users won’t be able to navigate to these pages until the test is live, unless they are given the URL directly, as long as you completed all the steps above.

**Configuring subscription management apps**

There are many subscription management apps, but the documentation for configuring duplicate products on some of the apps we’ve come across can be found at the following links:

* [Skio](https://help.intelligems.io/pricing-test-using-duplicate-products-and-skio)
* Don't see yours here yet? [Contact us here.](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)

**Configuring ratings and reviews apps**

Most applications for ratings and reviews offer a solution for grouping products so that multiple products display the same ratings and reviews. We recommend utilizing these features to ensure that duplicate products display the same content as the original products.

There are many different ratings and reviews apps, but the documentation for creating groups on some of the apps we’ve come across can be found at the following links:

* [Stamped](https://support.stamped.io/article/1097-groups-group-reviews-by-product)
* [Loox](https://help.loox.io/article/79-how-do-i-group-product-reviews-together)
* [Okendo](https://support.okendo.io/en/articles/3086164-creating-groups)
* [Judge.me](https://support.judge.me/support/solutions/articles/44001260470-share-reviews-across-product-groups)
* [Junip](https://help.junip.co/en/articles/4607273-product-groups-bundle-family)

**Configuring bundle or volume discount apps**

There are several bundle or volume discount apps available, such as Kaching or Shrine, where you may find it easier to redirect to a new PDP so that Kaching or Shrine can reflect the correct prices. Once your duplicate products have been created, head over to your volume discount app and set the same options up for your new product.

</details>


# Multi-Currency Testing

Run price tests in different currencies

## Introduction

Intelligems price tests run in your store's default currency by default. However, Intelligems supports price testing in any Shopify-supported currency. Each currency you want to test will require its own separate test configuration in the Intelligems app.

## **Prerequisites**

* [ ] You are **either:**
  * [ ] Using Shopify Plus and have the [Script Editor App](https://help.shopify.com/en/manual/checkout-settings/script-editor) installed
  * [ ] Using any Shopify plan and are able to use [Shopify Cart Transform Functions](https://shopify.dev/docs/api/functions/reference/cart-transform). This typically requires being upgraded to Checkout Extensibility, and is not compatible with a few apps, such as subscription apps
* [ ] You are on the [Intelligems Blue plan](https://www.intelligems.io/pricing?type=Annual\&priceRange=0-2500)
* [ ] An Intelligems team member has enabled the Multi-Currency Testing feature for you. Reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are not sure if this feature has been enabled for you yet
* [ ] You must be familiar with and using [Shopify Markets](https://www.shopify.com/markets) or [Global-e](https://www.shopify.com/markets) for localization
* [ ] You are ready to upload prices to your desired market when you [start](#starting-a-test), [pause](#ending-or-pausing-a-test) or [end](#ending-or-pausing-a-test) your price test
* [ ] You have a fixed price set in the desired currency for each variant you plan to test

## **Step 1:** Set up test in the Intelligems app

Creating a multi-currency test is generally similar to any other Price Test, with a few key changes to note. If you are not familiar with setting up a Price Test, please see our article [here](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test).

The main differences in setting up a Price Test that is not in your default currency are:

1. You will need to update the currency on the Modifications tab to match your test currency as shown in the screenshot below:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fjt1Lk7WLNFxNQyPqTGt8%2Fimage.png?alt=media&#x26;token=b1632abb-a39b-40c9-a982-2872911834a3" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
This option will not be available until an Intelligems team member has enabled the multi-currency setting for you.
{% endhint %}

2. You will need to update control prices to match your test currency prices. Prices aren't automatically converted, so verify each cell displays the correct amount.

{% hint style="warning" %}
Quick filling test groups based on control prices is not available for multi-currency tests. While you'll see the Quick Fill option in the app, clicking on it will take you directly to the 'Fill by Upload' option.

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FxL9HfOVXJPhH6gyFg7Pe%2F14%20-%20Multi-currency%20no%20quickfill.gif?alt=media&#x26;token=85f6047a-08cb-4341-a8cd-3eba352bb21b" alt="" data-size="original">
{% endhint %}

3. Currency targeting is set to your selected test currency by default, and will not be editable directly in the targeting section.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FZRSSIu9zMHKqGteu8vdc%2Fimage.png?alt=media&#x26;token=2e724cae-c16e-4783-88d7-8e0e5b910e6c" alt=""><figcaption></figcaption></figure>

## **Step 2: QA your Test**

This will be generally the same as QAing any other Price Test. You can see our checklist for QAing a Price Test [here](https://docs.intelligems.io/price-testing/price-test-qa-checklist). Please also keep in mind that your store's selected currency must match the test's currency.

## **Step 3: Starting a Test**

Your prices need to be set to the highest-priced test group in order for the test to run properly. When you hit the play button for your test, Intelligems will prompt you to download a price CSV that you'll use to update the prices in [Global-e](https://www.shopify.com/markets) or [Shopify Markets](https://www.shopify.com/markets) to the highest prices in your test.&#x20;

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fw45FtkCcf9zkxMJJofMQ%2Fimage.png?alt=media&#x26;token=9001497a-2eb2-4fb9-ae17-75f8816c5bfe" alt=""><figcaption></figcaption></figure>

Once you have this CSV, you should:

**If you are using Global-e:**

Reach out to your account manager at Global-e with this CSV. They will help you upload this information.

**If you are using Shopify Markets:**

1. Export Your Products:
   1. From your Shopify admin, go to Products.
   2. Export your products, making sure to include catalog pricing, international pricing, and variants. If you are able to set up any filters in Shopify to limit the export to products you will be price testing, this will make the next steps easier.
2. Edit Prices in a Spreadsheet:
   1. Use the "Variant SKU" column in the Shopify export and the "sku" column in the Intelligems export to match your products.&#x20;
   2. Add the prices and compare prices in the Intelligems export to the appropriate Market columns in the Shopify export. There should be one column for the price and one column for the compare price for each Market you have set up in Shopify Markets - ensure you merge the prices from Intelligems in the correct columns.&#x20;
3. Import Your Changes:
   1. Save your updated spreadsheet file. From your Shopify admin, go to Products.
   2. Import the file back into your Shopify admin, using the same app or the built-in import tool. The system will analyze your changes and update your products accordingly.

{% hint style="info" %}
You cannot have a product in more than one experiment *if* the experiments are set to the same currency. If so, the test will not start.
{% endhint %}

## **Step 4: Pausing or Ending a Test**

When pausing or ending a test, you'll be prompted to download a CSV with the prices that you want to roll out either while the test is paused, or permanently. You'll need to upload the file with the new prices either to [Shopify Markets](https://www.shopify.com/markets) or [Global-e](https://www.shopify.com/markets).

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FsgYp4ABM7Iz8SxqcsFmh%2Fimage.png?alt=media&#x26;token=eeb9e195-50a2-4fcf-af4a-06b1476815c5" alt=""><figcaption></figcaption></figure>

Once you have this CSV, you should:

**If you are using Global-e:**

Reach out to your account manager at Global-e with this CSV. They will help you upload this information.

**If you are using Shopify Markets:**

1. Export Your Products:
   1. From your Shopify admin, go to Products.
   2. Export your products, making sure to include catalog pricing, international pricing, and variants. If you are able to set up any filters in Shopify to limit the export to products that were price tested, this will make the next steps easier.
2. Edit Prices in a Spreadsheet:
   1. Use the "Variant SKU" column in the Shopify export and the "sku" column in the Intelligems export to match your products.&#x20;
   2. Add the prices and compare prices in the Intelligems export to the appropriate Market columns in the Shopify export. There should be one column for the price and one column for the compare price for each Market you have set up in Shopify Markets - ensure you merge the prices from Intelligems in the correct columns.&#x20;
3. Import Your Changes:
   1. Save your updated spreadsheet file. From your Shopify admin, go to Products.
   2. Import the file back into your Shopify admin. The system will analyze your changes and update your products accordingly.


# Price Testing FAQs

Common Questions about Price Testing

## General

<details>

<summary>How many products can I add to a price test?</summary>

We limit price tests to 500 products by default, but you can [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to ask for a limit increase.

</details>

<details>

<summary>Can I price test just one variant of a product?</summary>

Products get added to a price test at the product level, which means all variants are technically included in a test, but if you are only looking to test one (or a few) variants of the product, you can set the price to be the same as the control price in all test groups for the variants that you do not want to test.&#x20;

Here's an example of what that would look like if we only wanted to test the "Cream / Small" variant of our Ceramic Dinner Plate product:

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FjplJFn0r0bRlgTmSlxAq%2FScreenshot%202024-07-08%20at%203.35.14%20PM.png?alt=media&#x26;token=f28f5c6d-b01e-4897-b3d6-95da93fe488a" alt="" data-size="original">

</details>

<details>

<summary>Can I Price Test Shopify Bundle products?</summary>

Shopify Bundle products cannot be price tested due to a limitation with Cart Transform Functions. Both bundle products and our price testing feature rely on Shopify's Cart Transform functionality, but **Shopify only allows one cart transform function to run per line item**.

#### What are cart transform functions?

Cart transform functions are Shopify's mechanism for modifying cart contents, pricing, and line items dynamically. They're essential for creating product bundles and implementing dynamic pricing features.

#### Why does this create a conflict?

* **Bundle products** use Cart Transform Functions to group items together and apply bundle pricing
* **Our price testing** uses cart transform functions to display different prices to different customer segments
* Since only one transform can run per line item, these two features cannot operate simultaneously

#### Are there any workarounds?

Currently, there are no reliable workarounds due to this Shopify platform limitation. You'll need to choose between:

* Using bundle products with standard pricing
* Price testing individual (non-bundle) products

#### Will this limitation be resolved?

This depends on Shopify updating their platform to allow multiple Cart Transform Functions per line item. We'll continue monitoring Shopify's roadmap for any changes to this functionality.

</details>

<details>

<summary>What additional steps do I need to take if I use another software to manage product prices?</summary>

When you start a price test, Intelligems will automatically update your product prices in Shopify to the highest price in the test for each product. If you use another software (like NetSuite) to manage/push prices to Shopify, you'll need to also update the product prices in NetSuite to the highest price for each product.

1. You can download a CSV with your product IDs, SKUs, and test group prices in the "Set Prices" step of test setup. Please note that this file will contain prices for each test group, though you'll want to import only the highest price for each product. You can edit this CSV for import into your price management software (like NetSuite) according to the required format.<img src="https://help.intelligems.io/hs-fs/hubfs/Screen%20Shot%202023-04-04%20at%202.17.33%20PM.png?width=688&#x26;height=348&#x26;name=Screen%20Shot%202023-04-04%20at%202.17.33%20PM.png" alt="" data-size="original">
2. Start your price test in the Intelligems App. Please select **Yes, update my prices and start my test** in the pop-up.
3. Update prices to the highest test prices in your price management software right after starting the test (using the data from the downloaded CSV if preferred). As long as prices are updated before the software syncs to Shopify, then the test will work as expected.

</details>

<details>

<summary>What should I do with my Google Shopping Feed during a price test?</summary>

This depends on whether you are running your price test using Checkout Scripts, Functions or Duplicate Products.

If you are using Checkout Scripts or Functions, Intelligems updates the price in Shopify to the highest price in the test and sends that price to your shopping feed. We recommend triggering a feed update once the test is live, especially if you push your updates to the feed manually or if you use an app to manage your Google Feed. This means that for visitors coming into your site through Google ads, they may see a lower price when they get to the site, but never higher prices.

If you are using Duplicate Products, Google will continue to display the control price in the Google Shopping feed, which means users may see a different price when they get to the site. We recommend sending the higher prices to Google so that if users do see a different price when they land onsite, it's a lower price and therefore better for the customer experience. To do this, the original, non-duplicate products must have the highest price points in the test. This corresponds to the column on the left when you are setting up a test in Intelligems. Additionally, you'll want to make sure you remove duplicate products from all third-party channels so that the products don't show up on Google multiple time with different prices. You can read more on how to do that [here](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-duplicate-products/step-4-configure-duplicate-products).

</details>

<details>

<summary>I'm in Preview Mode to QA my Price Test but when I add a test product to cart the price is not right. Why?</summary>

Shopify Plus members using Checkout Scripts for their integration may notice a discrepancy in the cart prices during preview mode that will go away once a test is live if they are testing prices that are higher than their control price! The control price and any price groups lower than the control should show up correctly in the cart if your checkout script is live, while the higher price group will continue to add to cart at the control price.

This is because there is one item left, which will occur when the test is started. At that time, the Intelligems app will update the Shopify price to be the highest price in the test, and then for users who are in a lower price group, we will calculate a discount behind the scenes.

If you are only testing prices lower than the control, then you should not see any discrepancies when testing in Preview Mode since the control price is the highest price in the test.

</details>

<details>

<summary>Why is the discount showing on ShopPay checkout?</summary>

There is currently no way to hide a checkout script discount from appearing on ShopPay checkout. That said, we can change the name of the discount to appear as you'd like - if you would like to change the name of your discount, please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).

</details>

<details>

<summary>Does Intelligems work with subscription softwares like Recharge?</summary>

Yes! Intelligems works with Recharge and other subscription management services to facilitate tests around subscription pricing. However, given these integration are often complex, we highly recommend having Intelligems perform this integration. Learn more [here](https://docs.intelligems.io/price-testing/testing-with-subscriptions) about integrating with subscription platforms.

</details>

## Multi-Currency

<details>

<summary>If my store sells in multiple currencies, how does price testing impact each currency?</summary>

By default, price tests will only run in your store's default currency. All customers shopping in currencies other than your store's default currency will be excluded from the test results. However, the price that those customers see varies depending on a few factors:

1. Whether you use Shopify Markets or Global-E for currency conversion. If you use Global-E, please see the FAQ below this for more information. If you use Shopify Markets, please continue reading this FAQ.
2. How you manage currency conversion in Shopify Markets. Shopify Markets has two options for how prices are set in non-default Markets:
   1. By default, prices are automatically converted based off of the price in your default currency and the current conversion rate. If you use this method, and are testing higher prices than your control, all customers shopping in non-default currencies will see the highest prices in a live test in their currency.
   2. If you would prefer to set prices at a set rate for non-default currencies, you can follow [these steps](https://help.shopify.com/en/manual/international/pricing/product-prices-by-country#set-product-price-for-a-country-or-region) to do so.
3. The above is typically only relevant to tests that are being run using Checkout Scripts or Functions. If you are using Duplicate Products to run your test, this typically isn't relevant unless you have altered the price of your control product.

If you are interested in testing in multiple currencies, please see our article [here](https://docs.intelligems.io/price-testing/multi-currency-testing) for more information!

</details>

<details>

<summary>Does Intelligems integrate with Global-E?</summary>

We do not directly integrate with Global-E, but do have steps to follow if you are running a price test with higher prices using Checkout Scripts or Functions. If neither of those apply, nothing needs to be done to work with Global-E.\
\
If those do apply, when you start your price test, we raise your prices in Shopify to the highest prices in the test. Because Global-E is converting prices in other markets based off of what is in Shopify, the price will be higher in all other markets while the test is running. To avoid this, you'll need Global-E to set a fixed price in the foreign currency for each product included in the test. You can do this by providing Global-E with a CSV file. They will also need to revert this at the end of the test so the prices can sync with the current exchange rate.

</details>

## Duplicate Products

<details>

<summary>Do I need to duplicate products to run a price test and does it happen automatically?</summary>

In most cases, you do not need to duplicate products to run a price test with Intelligems. This is because Intelligems uses Shopify Functions to run price tests in most cases.

Duplicating products may be necessary if:

1. Your store is unable to use Shopify Functions for any reason.
2. You offer subscriptions and do not have access to the Script Editor app, or you are using an app other than Stay.Ai or Recharge to power your subscriptions.
3. You are using another third party app on your PDP that is not compatible.

If you need to use duplicate products for one of the above or another reason, please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for assistance enabling this feature in your account. Once enabled, one duplicate product will be created automatically for every product and every price point that you add to a price test.&#x20;

</details>

<details>

<summary>What will duplicate products look like in Shopify and how can I find them?</summary>

The duplicate products will be nearly identical to the original products with a few key differences:

1. They will have different product and variant IDs. Note that duplicates will have the same SKUs as their originals.
2. They will be tagged with a ‘price\_test’ tag, as well as a tag with the experiment ID, test group ID and a unique ID to that product.
3. They will be set to ‘Draft’ status when created.

</details>

<details>

<summary>Can I delete duplicate products once a price test is over?</summary>

We typically recommend waiting a few days after a test is over before doing this. Customers will not be able to see them unless the duplicate products are still in their cart. Keeping the duplicates live for a few days will allow these edge-case customers to be able to check out, creating a better customer experience.&#x20;

When ending a test, you'll be asked if you would like to archive the products now or within 48 hours. Intelligems will automatically archive duplicates after 48 hours.

Additionally, if you have subscriptions, you should make sure any subscriptions that occurred on the duplicate products get mapped to non-duplicate products.

Other than that, there are no issues with deleting them, but archiving may be a safer option in case you need to make any changes later. You'll be able to find all duplicate products created by Intelligems by searching for the products with the tag 'price\_test' in Shopify.

</details>


# Shipping Testing - Getting Started

How shipping testing works and how to get started.

## What is Shipping Testing?

Intelligems gives you the tools to test your shipping rates, free shipping threshold, and beyond. Testing your shipping rates with Intelligems allows you to find rates that work for you and your customers. The right shipping profile can allow you to boost profits, maximize conversion without sacrificing on margin, or boost AOV.

## How does it work?

Intelligems typically runs shipping tests using a Shopify feature called the [Third Party Rate Carrier API](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/enabling-shipping-carriers). This feature allows Intelligems to calculate a user's shipping rate based on which test group they are in, what products they are purchasing, and where they will be shipping to. Because Intelligems will be providing shipping rates while you are running a test, we will automatically remove the rates that you select to test when you start your test.

Intelligems also provides features to manage the onsite merchandising required for a shipping test. A few examples of this include:

* A shipping progress bar. If you are testing your shipping threshold, you will likely want to use the Intelligems [shipping progress bar](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration) (which can be found in your **Global Styles** components)while your test is live so that the correct threshold displays in your cart for each group.
* An onsite editor to display different language for each group. If you have any text on the site that mentions your control shipping options, such as in your announcement bar or on a shipping FAQ page, you can use the Intelligems [Find & Replace](https://docs.intelligems.io/general-features/onsite-editor) feature to show the correct copy for each test group.

{% hint style="danger" %}
To activate the third-party carrier-calculated shipping, your store needs to be on the Advanced or Shopify Plus plan. This is a Shopify limitation.\
\
If you're on the Shopify plan, then you can add this feature for a monthly fee (paid to Shopify) or switch from monthly to yearly billing. For more information, contact [Shopify Support](https://help.shopify.com/questions).
{% endhint %}

## How can I get started?

Before you can run a shipping test using Intelligems, you'll need to add the Intelligems script to your theme; [here is our help guide](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) on adding that snippet.

Once the snippet has been added to your theme, see the guides below for more information on shipping testing:

{% content-ref url="how-to-set-up-a-shipping-test" %}
[how-to-set-up-a-shipping-test](https://docs.intelligems.io/shipping-testing/how-to-set-up-a-shipping-test)
{% endcontent-ref %}

{% content-ref url="shipping-test-qa-checklist" %}
[shipping-test-qa-checklist](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist)
{% endcontent-ref %}

{% content-ref url="starting-a-shipping-test" %}
[starting-a-shipping-test](https://docs.intelligems.io/shipping-testing/starting-a-shipping-test)
{% endcontent-ref %}

{% content-ref url="ending-a-shipping-test" %}
[ending-a-shipping-test](https://docs.intelligems.io/shipping-testing/ending-a-shipping-test)
{% endcontent-ref %}

{% content-ref url="shipping-progress-bar-integration" %}
[shipping-progress-bar-integration](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration)
{% endcontent-ref %}

{% content-ref url="shipping-testing-faqs" %}
[shipping-testing-faqs](https://docs.intelligems.io/shipping-testing/shipping-testing-faqs)
{% endcontent-ref %}


# How to Set Up a Shipping Test

This guide will walk you through the steps to set up a shipping test in Intelligems.

## Step 1: Create a new test

Go to the **Tests** tab in the left menu in the Intelligems app. Click **Create New Test** above the experiments table.

Enter a **Name** and **Description** for your test. This information is internal only - add enough detail so you'll remember your goals when reviewing results weeks later. Select **Shipping Test** and then **Create Test**.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fxs6mHvC2P0HURw1UbVRR%2FOct-13-2025%2015-41-07.gif?alt=media&#x26;token=288c8738-a79a-47d4-addd-e29c8babe540" alt=""><figcaption></figcaption></figure>

## Step 2: Create your test groups

Create 2-5 groups by clicking **+**. Name each group and use the slider to allocate traffic percentage. Click **Next step** when ready.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FUr8A7mZESuYUlzIi2yYy%2Ftest%20groups.gif?alt=media&#x26;token=9f5ffb49-6f33-43c0-a5da-faad984fc30b" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The more groups you have, the longer it will take to get statistically significant results. You’ll need about 300 orders for each group in the test to detect a 10% change in conversion with 90% confidence.
{% endhint %}

## Step 3: Select shipping profiles and zones to test

Using the expander for each shipping profile, select the zone(s) where the Intelligems rate will be added. The Intelligems rate will *only* apply to the profiles and zones selected here and will apply to *all* orders that meet the criteria for the selected profiles and zones, subject to other cart value and weight criteria which you'll configure in the next step.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FYpuxta94XsPyPMLVHH2r%2FSelect%20Profile.gif?alt=media&#x26;token=c9205f3c-9c85-4335-801e-a998cd02ed64" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Consider carefully which profile(s) you add the Intelligems rate to. If your store's products are spread across multiple profiles, adding the Intelligems rate to a subset of profiles may lead to unexpected behavior at checkout. Learn more about how Shopify combines rates [here.](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/shipping-profiles/combined-shipping-rates)
{% endhint %}

## Step 4: Select the rates you want to replace for this test

Once you have selected the profiles and zones you want Intelligems rates to apply to, you will select which rates from those zones you want to test. These rates will be hidden during the test and replaced by an Intelligems rate, which will vary by test group.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FKfkyRaVoj08cNoCwe0uV%2FRates%20To%20Remove.gif?alt=media&#x26;token=7bc1eef7-3453-43c4-8992-6027604e0ba4" alt=""><figcaption></figcaption></figure>

## Step 6: Configure the Intelligems rate(s)

In this step, you will configure the rate(s) to be added to the previously selected profiles and zones for each test group.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FEid9l5RmMO0gz0Rnizji%2FSet%20Rates%20Per%20Group.gif?alt=media&#x26;token=bc3466f5-2254-4fba-8bd5-e37124766c8a" alt=""><figcaption></figcaption></figure>

For each group, choose the rate type that most closely aligns with what you're *testing* (i.e. what you want to change in each test group). See below for some tips on when to select each rate type and examples of combined rates:

## Different Rate Types

![Rates in blue are provided by Intelligems; rates in green are configured in Shopify](https://hs.intelligems.io/hs-fs/hubfs/8-png.png?width=600\&height=48\&name=8-png.png)

#### **Flat Rate:** You are testing rate(s) that are not set up with conditions in Shopify ("flat rates")

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/2-1.png?width=447&#x26;height=95&#x26;name=2-1.png" alt=""><figcaption><p>Example 1: Testing a single flat rate</p></figcaption></figure>

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/1-1.png?width=449&#x26;height=97&#x26;name=1-1.png" alt=""><figcaption><p>Example 2: Testing multiple flat rates</p></figcaption></figure>

#### **Flat Rate with Threshold**: You are testing a flat rate and the threshold for free shipping

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/3-1.png?width=449&#x26;height=115&#x26;name=3-1.png" alt=""><figcaption><p>Example 3: Testing flat rate and a threshold</p></figcaption></figure>

#### **Threshold Only**: You are testing a free shipping threshold but want to keep your existing rates for those that do not reach the threshold&#x20;

{% hint style="danger" %}
Thresholds in a shipping test are based on the **pre-discount subtotal**. This means that discount codes and automatic discounts applied at checkout may put the shopper below the threshold but still give them free shipping. This is a limitation of Shopify's Third Party Rate Carrier feature.
{% endhint %}

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/4.png?width=449&#x26;height=92&#x26;name=4.png" alt=""><figcaption><p>Example 4: Testing a free threshold with rates under threshold provided by third party app</p></figcaption></figure>

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/5.png?width=448&#x26;height=118&#x26;name=5.png" alt=""><figcaption><p>Example 5: Testing a free threshold with weight-based rates under threshold configured in Shopify</p></figcaption></figure>

#### **Tiered by Price or Weight**:

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/6.png?width=449&#x26;height=115&#x26;name=6.png" alt=""><figcaption><p>Example 6: Testing rates for each weight-based tier</p></figcaption></figure>

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/7.png?width=445&#x26;height=91&#x26;name=7.png" alt=""><figcaption><p>Example 7: Testing rates and conditions for each weight-based tier</p></figcaption></figure>

#### **Custom**: Have something else you want to test?&#x20;

[Let us know](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we'll see what we can do!

## Step 7: Review your rates

Use the drop-downs to review profiles, zones, and test groups.

1. Select profile and zone to preview
2. Select test group for cart preview
3. Input sample cart totals and weight to see what shipping options will be available at checkout

{% hint style="warning" %}
Rates displayed at checkout during the test may differ from preview if order products are included in multiple shipping profiles.
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FqHeF9q58jO34UbWm6sZJ%2Fimage.png?alt=media&#x26;token=5d01b2d0-08dc-4ef6-a937-f11458a87220" alt=""><figcaption><p>Review combined rates</p></figcaption></figure>

## Step 8: Enable & customize your progress bar if needed

If you currently show a shipping progress bar on your site or if you would like to include one for your test and you are testing shipping thresholds, it is recommended to use the built-in option from Intelligems found in the [**Global Styles**](https://app.intelligems.io/global-styles/experiences) components so that the bar will update with the test group. Adding the Intelligems progress bar typically requires adding a component to your theme's liquid code and customizing the bar's style in the Intelligems app.

Learn more about adding the Intelligems shipping progress bar and other components [here](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration).

See below for a few examples of a configured shipping progress bar during a live test.

<table data-header-hidden><thead><tr><th></th><th width="180"></th><th></th></tr></thead><tbody><tr><td><img src="https://d33v4339jhl8k0.cloudfront.net/docs/assets/624c7e54ed4a0c44b4e6013a/images/627c03f7b2de5178f8882dd8/file-GLKo2WKNwT.png" alt=""></td><td><img src="https://d33v4339jhl8k0.cloudfront.net/docs/assets/624c7e54ed4a0c44b4e6013a/images/627c03ff68d51e779443f8bf/file-CFmEk6N22o.png" alt=""></td><td><img src="https://d33v4339jhl8k0.cloudfront.net/docs/assets/624c7e54ed4a0c44b4e6013a/images/627c0405c01fce37d9b12613/file-JoWvYs5xWG.png" alt=""></td></tr><tr><td>Example 1: Under the Free Shipping Threshold</td><td>Example 2: Exceeded the Free Shipping Threshold</td><td>Example 3: Under the Cart Minimum Threshold</td></tr></tbody></table>

## Step 9: Edit content on your site if needed <a href="#step-7-edit-content-on-your-site" id="step-7-edit-content-on-your-site"></a>

This step is also optional. This tool allows you to dynamically update content on your site based on a visitor's test group. Check out [this article](https://docs.intelligems.io/content-testing/find-and-replace) for more details on configuring this option.

## Step 10: Set up targeting if needed

Targeting is an optional step. By default, a visitor will be immediately assigned to one of the test groups using its random split-test mechanism. This assignment is determined at the first visit and is stored via a first‐party cookie, ensuring that the visitor remains in the same group on subsequent visits during the shipping test period.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

## Step 11: Save and Preview your Test

Once you have completed all the steps, you'll be able to save your test with the green **Save** button in the top right.

In the **Preview** tab, you'll find a few options to load the test's preview:

* **Open Full Screen Preview:** this will open your website with the Intelligems widget loaded, so you can easily alternate between test groups to preview each group's experience, as well as do onsite edits if necessary (see [Step 8](#step-8-edit-content-on-your-site-if-needed) for more details). You can also choose which theme you'd like to preview in if you need to be somewhere other than your live theme!&#x20;
* **Open Mobile Preview:** you'll see a QR code for each test group, so you can load the preview directly on your mobile device.&#x20;
* **Copy Preview URL:** this will copy the preview URL to your clipboard automatically.

Once the test is saved, you should be able to see Intelligems as a rate carrier in your Shopify shipping settings for each profile and zone you selected in step 2. If you do not see it there automatically, you may need to click 'Add rate' and select it from the carrier options.

{% hint style="info" %}
Don’t worry, this won’t set the test live yet and you can come back and edit if you need to make changes!
{% endhint %}

## Step 12: Enter the test goals

Here you will choose the primary goal for the test. This will not affect what data is tracked or displayed, but will allow Intelligems to show the most important analytics first.

## What happens next?

Now that you've created your shipping test, you can QA your test using [this checklist](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist)!


# Shipping Test QA Checklist

{% hint style="info" %}
This QA list is specific to a shipping test. If you are QAing a price test, please check out [this article](https://help.intelligems.io/qaing-your-new-test)!
{% endhint %}

## Prerequisites: How Shipping Tests Work:

When you create and save your shipping test, Intelligems will automatically be added as a [third party rate carrier](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/enabling-shipping-carriers) in your Shopify admin. With the Intelligems rate carrier installed, once you start your test, Intelligems will provide rates to shoppers at checkout based on their test group, cart value and item weight, if relevant.

## What to Check First:

Before heading to your site to preview your test, there are a few things you should check to make sure your integration is functional:

* [ ] Is Intelligems JavaScript in your live theme? Check out [this article](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) for more information on where to find this.
* [ ] Has Intelligems been added as a rate provider in Shopify? You can follow the steps below to check this:
  1. From your Shopify admin console, navigate to 'Settings' in the lower left corner and select the 'Shipping and Delivery' tab.
  2. Select the shipping profile you've chosen to run your shipping test in.
  3. Scroll down to the zone you've chosen to run your shipping test in.
  4. In the zone you'll be testing in, you should see "Intelligems Shipping (Rates priovided by app)" under "Carrier and app rates" like the screenshot below.

     <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FeA1vVZRSyxMyGgWrLL48%2FScreenshot%202024-02-22%20at%2011.44.04%20AM.png?alt=media&#x26;token=4057f81f-f650-4cc9-925f-09709f1f0eb9" alt=""><figcaption></figcaption></figure>
  5. If you do not see 'Intelligems Shipping (Rates provided by app)' listed, please [reach out to Intelligems Support ](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)for help troubleshooting.

## Previewing your Test:

Once you have confirmed both of those items are true, you can preview the test on your live site. Enter Preview mode by clicking on the eyeball icon next to your test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FeOup1vjmEJoyeyEF1FZP%2FScreenshot%202024-12-05%20at%2010.13.31%20AM.png?alt=media&#x26;token=9e5408be-2ae7-45ab-8a06-a995f254a0a9" alt=""><figcaption></figcaption></figure>

This will open your site up in a new window with the Intelligems preview widget enabled. In the preview widget, you'll see:

1. The name of the test you are previewing in the top left
2. A dropdown to switch between different test groups in the bottom left
3. A toggle to highlight any replacements in the top right
4. An edit button in the bottom right: this enables integration mode, where you can edit price selectors and text replacements

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FVuDCUAgvnX9tu5qFDtLG%2Fimage.png?alt=media&#x26;token=0ee7a70f-8beb-4cb3-a16e-ce06228f0f27" alt=""><figcaption></figcaption></figure>

### Step 1: Confirm that Onsite Edits are working correctly

Did you set up any [Onsite Edits](https://docs.intelligems.io/general-features/onsite-editor) for your test? If so, view any locations you used the Onsite Editor to change shipping prices or language on your store, such as a banner or FAQ page. Confirm copy or images are correctly updating when switching the test group in the Intelligems Preview Widget. Note that you may need to hard refresh when switching groups in the widget!

### Step 2: Confirm that the Intelligems Progress Bar is working correctly

Did you add the Intelligems [Progress Bar](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration)[ ](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration)to your cart? If so, confirm that the threshold is updating when you switch test groups (if you are testing thresholds), and that the math is correct on the bar as you add and remove items to the cart.

### Step 3: Confirm that you are getting the correct shipping rates in cart

Choose one of the test groups, and empty your cart if it is not already. Add a product, or a few products, to your cart and proceed to the checkout page. Enter address information (either your own, or a test address that is within the profile/zone you are testing) so that you can proceed to the shipping step. Confirm that your test rate(s) are showing up here. A few things to note:

* Your test rate will include "Intelligems Preview:" at the beginning of the rate name. This is expected, and will only show up in Preview Mode so that you know where the rate is being provided from in case it has the same name as your normal rates.
* You will still see the rate(s) that you've chosen to test. This is because Intelligems removes the rates you are testing from Shopify when you start your test.
* Be sure to test multiple scenarios to ensure the rates are always being provided correctly. This list is not exhaustive, and these may not all be applicable to your site, but a few scenarios we recommend testing include:
  * Below your shipping threshold
  * Above your shipping threshold
  * Different shipping tiers
  * When using a discount
  * Adding to cart from different locations on the site
  * Adding products from different shipping profiles and zones
  * Test on multiple devices and browsers (such as desktop Chrome and mobile Safari) to confirm there are no discrepancies.

Complete these steps in each test group, being sure to empty your cart when you switch to a new test group! If you notice any issues, or have any questions, please feel free to [reach out to Intelligems support!](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)

### What happens next?

Now that you've completed the QA checklist for your shipping test, you can start the test!


# Starting a Shipping Test

{% hint style="info" %}
The contents of this article are only relevant if you are using the Intelligems Carrier Rate Implementation of the shipping test. If you are using checkout scripts to run your shipping test, [please reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to get your test launched!

Additionally, to use the Intelligems Rate Carrier out of the box, your store needs to be on the Advanced Shopify or Plus plan. If you're on the Shopify plan or lower, then you'll need to reach out to Shopify Support to enable third-party carrier-calculated shipping; see more on that [here](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/enabling-shipping-carriers). Additionally, please note that as of January 1st, 2023, Shopify will be no longer support this feature for Shopify Basic plans.
{% endhint %}

## **Step 1: Confirm Intelligems JavaScript is in Your Live Theme**

In addition to Intelligems JavaScript, confirm any other theme changes completed during the integration are in your live theme as well. **If not**, please publish the script and any changes before proceeding.

## **Step 2: Press the Start Button**

In the Intelligems app, navigate to the A/B Tests tab and click the green play button next to the shipping test you are wanting to start.

## Step 3: Verify that Intelligems has been Added as a Rate Provider

1. From the Shopify admin console, navigate to Settings → Shipping and Delivery.
2. Select the relevant shipping profile(s).

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F21SocbISS80poBrghOFj%2FScreenshot%202024-12-05%20at%2011.46.16%E2%80%AFAM.png?alt=media&#x26;token=1505081b-5f0a-4b80-8732-031fffd9e279" alt=""><figcaption></figcaption></figure>

3. Scroll down to the section titled "Shipping zones" and navigate to the region(s) you've chosen to run your shipping test in. Verify that Intelligems is installed as a rate provider. This will look like the below.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FGHxE2KIF9BDVui1qtvBs%2FScreenshot%202024-12-05%20at%2011.48.56%E2%80%AFAM.png?alt=media&#x26;token=314abe07-64ed-4886-ade9-57d4f29b8ec7" alt=""><figcaption></figcaption></figure>

## **Step 4: Check Your Site**

Now that the test is live, we recommend going through the add to cart and checkout process in a few incognito browsers so you can get added to different test groups and ensure everything is working as expected. If you have not already QA'ed your test before launching it, we recommend going through [this checklist](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist). [Please reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) with any issues!


# Ending a Shipping Test

Follow these steps to end a Shipping Test in the Intelligems app.

{% hint style="info" %}
The contents of this article are only relevant if you are using the Intelligems Carrier Rate Implementation of the shipping test. If you are using checkout scripts to run your shipping test, please[ reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to end your test!
{% endhint %}

## Step 1: Press the Stop Button

To end a test, navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems portal. Once you're there, locate the test you'd like to end in the Intelligems tests console. Click the stop button.

## Step 2: Configure the Shipping Rates in Shopify to Roll Out

Navigate to "Settings" → "Shipping and Delivery" from within the Shopify admin console and select the shipping profile(s) you'd like to update. Update to match what you'd like to roll out.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F21SocbISS80poBrghOFj%2FScreenshot%202024-12-05%20at%2011.46.16%E2%80%AFAM.png?alt=media&#x26;token=1505081b-5f0a-4b80-8732-031fffd9e279" alt=""><figcaption></figcaption></figure>

## Step 3: Update Your Progress Bar, if Applicable

If you used an Intelligems shipping progress bar during your test, you can continue to use it for a Shopify-powered free shipping offer. You'll simply need to create a sitewide [free shipping offer experience](https://docs.intelligems.io/personalizations/personalization-modifications/offer-modifications#free-shipping-offer) in Intelligems and select the "powered by Shopify" option.

## Step 4: Update Any References to the Shipping Policy on Your Site, if Needed

Often these are addressed using the Intelligems Onsite Edit feature during the test, but will revert to whatever is configured in your theme once the test has ended. If you've chosen to roll out a new shipping fee, you'll want to change these in your theme. A few spots to check include:

* Banner Text
* Shipping Policy Page
* FAQ's

{% hint style="success" %}
We recommend executing all steps of these instructions as concurrently as possible to ensure a seamless experience for your store's customers!
{% endhint %}


# Shipping Progress Bar Integration

## Overview

Intelligems offers a progress bar for Shopify carts / slide-out carts that shows visitors how much they have left to spend before reaching free shipping. The progress bar can be used as part of a shipping threshold test (visitors will be shown the correct bar based on their test group) or outside of a test.

{% hint style="info" %}
You'll need the Intelligems JavaScript snippet added to your theme to render the Intelligems shipping progress bar. If you haven't done so, see our integration guide [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
{% endhint %}

## Step 1: Add the shipping progress bar to your Shopify theme

Paste the following code snippet into your Shopify theme code, in the theme file that renders your cart. This file may be called something like cart.liquid, slideout-cart.liquid, etc. We recommend adding this code snippet at the top of the section that relates to your cart:

```html
<ig-shipping-progress-container></ig-shipping-progress-container>
```

{% hint style="danger" %}
If you already have a progress bar, remember to comment out the existing progress bar to avoid showing two!
{% endhint %}

## Step 2: Customization / Styling

You can customize the Intelligems Cart Progress Bar in the Global Styless tab. Some examples of stylizing options available include:

* Bar Styles
* Bar Colors
* Text Options

## Integrating with Rebuy Carts

1. Create a Rebuy custom smart cart template. Follow [this](https://help.rebuyengine.com/en/articles/6120362-how-to-use-a-custom-template-with-smart-cart) article for instructions.
2. Edit the template to replace the Rebuy progress bar with the Intelligems progress bar snippet. See Step 1 above.

## Using the Progress Bar With Your Existing Shopify Rates

You can use the Intelligems Shipping Progress Bar with your existing Shopify rates using an Intelligems Offer Experience. You'll simply add the code snippet above to your Shopify theme and configure the visual appearance of the progress bar in the Intelligems app. Then in the Intelligems app, create a new free shipping offer, ensure you opt for the offer to be "powered by Shopify", and save your offer.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fg18Uo8SzEkxOeAkgaXcR%2FShipping%20Progress%20Bars.png?alt=media&#x26;token=e25d2a97-b925-430c-9bd9-87d835246629" alt=""><figcaption><p>Edit Shipping Progress Bar</p></figcaption></figure>


# Shipping Testing FAQs

Common Questions about Shipping Testing

<details>

<summary>Is a shipping threshold based on a pre or post discount subtotal?</summary>

The shipping threshold is based on the pre-discount subtotal.

When Shopify is providing shipping rates, they use a visitor's post-discount subtotal to determine whether that visitor qualifies for free shipping. However, Shopify only provides the pre-discount subtotal to the Third Party Rate Carrier, which is what Intelligems uses to run shipping tests. Because of this, while running a shipping test with Intelligems, we will use a visitor's pre-discount subtotal to determine whether they qualify for free shipping. This is a limitation of Shopify's Third Party Rate Carrier feature.

</details>

<details>

<summary>I have more than one ship-from location! Can I test my shipping prices?</summary>

Shipping from multiple locations can cause issues with shipping tests due to Shopify's Third Party Rate Carrier feature. This feature treats products from different locations as separate carts, leading to multiple shipping charges if a customer buys products from different locations.&#x20;

To determine if this setup will affect your shipping tests, consider whether customers often buy products from different locations simultaneously. If they do, your current setup may not work well for shipping tests. If they don't, your setup should be fine, but be aware that some customers might have questions.

</details>

<details>

<summary>I want to test my shipping threshold! What should I do about the progress bar in my cart?</summary>

There are two options for how to correctly update your progress bar for a shipping threshold test!

**Option 1:** Use Intelligems' progress bar! See our integration guide [here](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration) on how to integrate this with your site.

**Option 2 (more advanced):** Use our [JavaScript API](https://docs.intelligems.io/developer-resources/javascript-api/user-object) to look up which test group a visitor is in, then update your progress bar with custom code. This is only necessary if your progress bar has a unique design or specific tiers you want to preserve.

</details>

<details>

<summary>What happens when I end my shipping test?</summary>

If the test was run using the Third Party Rate Carrier, the rate carrier will no longer provide shipping rates, and we will restore the rates that we removed when you started the test.

</details>

<details>

<summary>Can I run more than one shipping test at the same time?</summary>

No, you cannot even have more than one pending and/or running shipping test at the same time! This is because Intelligems installs the rate carrier when you set up a shipping test, and it can cause issues if you create or start another shipping test at the same time. If you want to create a new shipping test, you'll need to end any live shipping tests, and/or delete any pending shipping tests.

</details>

<details>

<summary>Can I run a shipping test on specific products?</summary>

At the moment, Intelligems doesn't support running shipping tests at the **product level. S**hipping tests can only be applied **sitewide** or based on broader cart conditions like cart value or destination.

This limitation exists because Shopify doesn’t offer a straightforward way to assign different shipping rules to specific products within the same test environment. Since shipping is calculated at the cart level, it's tricky to ensure a consistent and accurate experience when trying to apply different shipping logic to only a subset of products without causing conflicts or confusion at checkout.

That said, if you’re looking to test how shipping impacts conversion or AOV, we can help you structure a sitewide test that isolates the variable cleanly. Feel free to reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) with any additional questions.

</details>

<details>

<summary>Can I run a shipping test in a currency other than my store's default currency?</summary>

**Yes, you can run shipping tests in currencies other than your store's default currency. You can update the currency for the shipping rates by using the Rate Currency dropdown at the top of the "Set Rates Per Group" test setup step.**&#x20;

However, there's an important technical limitation to be aware of:

**How shipping thresholds are calculated:**

* Shipping thresholds (like "free shipping over $50") will always be calculated using your store's **default currency**
* This happens because Shopify's third-party rate carrier API (which Intelligems uses to run shipping tests) only receives cart totals in the store's default currency
* The threshold amounts you set in your shipping test will be interpreted in your default currency, regardless of what currency the customer is viewing

**Example:**

* Store default currency: USD
* Customer viewing in: EUR
* Shipping test threshold: $50 free shipping
* The system will check if the cart total is ≥ $50 USD (converted from the EUR cart value), not €50

</details>

<details>

<summary>I duplicated my shipping test. What are the steps I need to take to complete the setup?</summary>

Once you've duplicated a shipping test, you will need to edit the test and select the profiles, zones and rates that you'd like to test. [Here is a video](https://www.loom.com/share/e7dd1ec7b5174eb6ac0fefdf7ea6df75) walking through these steps. Please reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions!&#x20;

</details>


# Content Testing - Getting Started

There are a variety of ways to set up content tests with Intelligems. The five main options are listed below, but they can also be used in conjunction with one another.

1. Testing specific URLs using a page redirect. This is best for pages limited to certain pages and involve redirecting from one URL to another.
2. Testing smaller components on your site using our onsite editor. This is best for smaller changes, such as copy changes, color changes, image swaps, and more.
3. Testing a theme template. This is best for testing different templates across a section of your site, such as all product pages or collection pages.
4. Testing an entire theme. This is best for large changes and will involve redirecting from your live theme to one or multiple preview themes.
5. Testing using our JavaScript API. This is best for more custom scenarios.

See the guides below for more information on setting up these options:

{% content-ref url="content-testing-getting-started/how-to-set-up-a-split-url-test" %}
[how-to-set-up-a-split-url-test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test)
{% endcontent-ref %}

{% content-ref url="content-testing-getting-started/how-to-set-up-an-onsite-edits-test" %}
[how-to-set-up-an-onsite-edits-test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)
{% endcontent-ref %}

{% content-ref url="content-testing-getting-started/how-to-set-up-a-template-test" %}
[how-to-set-up-a-template-test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-template-test)
{% endcontent-ref %}

{% content-ref url="content-testing-getting-started/how-to-set-up-a-theme-test" %}
[how-to-set-up-a-theme-test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-theme-test)
{% endcontent-ref %}

{% content-ref url="content-testing-getting-started/how-to-set-up-a-test-using-our-javascript-api" %}
[how-to-set-up-a-test-using-our-javascript-api](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-test-using-our-javascript-api)
{% endcontent-ref %}


# How to Set Up a Split URL Test

Page redirect testing allows you to split-test URLs to determine which is the best for conversion, revenue, and profit.

{% embed url="<https://www.loom.com/share/d106c570d0224bbeaacb317712654dc6>" %}
Video: How to create and set up a Split URL Test with Intelligems
{% endembed %}

## **Step 1: Create a new test**

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click 'Create New Test' above the experiments table. Give it a name, and a helpful description. Then select "Content Test" , then "Split URL Test", then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FYgbXTcztGcAZQpU1iDIH%2FStep%201.gif?alt=media&#x26;token=500b6fa2-1aae-40d5-b0b6-5ef6afd60149" alt=""><figcaption></figcaption></figure>

## **Step 2: Create your test groups**

Create a test group for each redirect variation you want to include in the test. Fill in the Test Name and Test Description for the experiment you are creating. This information is all internal - the more detail you include here the better! Tests can be live for several weeks, and your future self will thank you for including the details here.

You can add new groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider to allocate what percentage of traffic will go to each group. Click ‘Next Step’ when you are done.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FiM5J7If40luIhZexuvnB%2FStep%202.gif?alt=media&#x26;token=57d11f86-50f0-4de9-a96f-2d184eeb903b" alt=""><figcaption></figcaption></figure>

## **Step 3:** Set up redirects

There are two types of redirects:

* **Simple Redirects** - this type of redirect is best used when targeting a small quantity of specific URLs
* **Advanced Redirects** - this type of redirect is best used when targeting many URLs that have a similar pattern

### Simple Redirect Setup

Enter the URL you want to *redirect from* in the Origin URL field. Then, for each test group enter the URL you want to *redirect to*.

In the example below, we redirect from <https://deepdish-pizza.myshopify.com/page-a> to <https://deepdish-pizza.myshopify.com/page-b>. When visitors land on <https://deepdish-pizza.myshopify.com/page-a>, those in the Control Group will remain at the original URL, while those in the test group "Redirect Test Group" will be redirected to <https://deepdish-pizza.myshopify.com/page-b>. Create a Redirect for each origin URL you want to redirect from.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FHE3o4T9wIPcRxVsfRPdR%2FScreenshot%202024-12-06%20at%2012.55.02%E2%80%AFPM.png?alt=media&#x26;token=90506dd7-8c1e-42ef-abf7-7d6cfa9bfa1f" alt=""><figcaption></figcaption></figure>

### Advanced Redirect Setup

Advanced redirects allow for more flexibility when defining the criteria for a qualifying page URL.

Start by choosing a matching option and entering a value to match against.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FkkByCvbn7ljjbsjNgQcO%2Fstep%203.gif?alt=media&#x26;token=7f9ef0c3-45b4-4155-84ac-47ee5e489655" alt=""><figcaption></figcaption></figure>

Here are some examples of different matching options with values:

* **matches exactly** - `https://deepdish-pizza.myshopify.com/en-us/cool-collections/product-a`
* **contains** - `sofa`
* **ends with -** `/products/product-a` Note: this will evaluate the URL Path and ignore query parameters. So `https://example.com/products/product-a?utm_source=abc` DOES meet the conditions here
* matches regex - `^.*\/[a-zA-Z]{2}-[a-zA-Z]{2}\/pages\/abc$` This regex expression checks for a URL in the pattern `example.com/en-US/pages/abc.`

Make sure all matching conditions are case *insensitive.*

{% hint style="warning" %}
**Products Redirects**

For most product redirects, it would be better to use ENDS WITH than CONTAINS.

For example, if you use contains `/products/product-abc` but you also have a `/products/product-abc-plus`, then that would match both products. If you were looking to just target the non-plus version, you should use ENDS WITH.
{% endhint %}

{% hint style="info" %}
Note: "/cool-collections" will be evaluated differently than "cool-collections". A redirect set to look for "cool-collections" (without a leading /) will evaluate to true for pages <https://deepdish-pizza.myshopify.com/en-us/cool-collections> AND <https://deepdish-pizza.myshopify.com/en-us-cool-collections> whereas a redirect set to look for "/cool-collections" will only evaluate to true for <https://deepdish-pizza.myshopify.com/en-us/cool-collections>.
{% endhint %}

After selecting a matching option and entering a condition, select which type of Redirect Type to use:

* Replace Full URL - this option updates the entire URL
* Replace Matching Text - this option will allow you to find specific values in the current page URL and replace them with text of your choosing

If you choose `Replace Full URL`, you'll need to enter a full valid URL for each test group redirect. If you choose `Replace Matching Text`, you'll need to enter valid find and replace values.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FYbxeLPrHiwey9HfSKqxx%2Fstep%204.gif?alt=media&#x26;token=b26da8de-6621-432a-b885-5d8b2f4d6efe" alt=""><figcaption></figcaption></figure>

### Additional Features

#### Redirect One Time vs. Redirect Every Time

Selecting `Redirect One Time` ensures that this redirect only fires one time for each visitor. On subsequent visits to the origin URL, visitors will be left on that page and not redirected again. This is the default behavior when creating a redirect.

An example of when you'd want to choose `Redirect One Time`: say you're sending some traffic from a Facebook ad to your homepage, and you want to test to see if using a landing page from the ad would be better. If you didn't select `Redirect One Time` for this, then visitors from the ad who are in the test group would be redirected to the landing page every time they tried to go to the homepage.

An example of when you'd want to select `Redirect Every Time`: say you're testing two versions of a collection page. You would want your visitors in the test group to be redirected every time they went to that collection page so they always see the same version.

You can test different URLs in the Redirect Checker to see where a user in each test group would get redirected.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FeH3gwObbrJnD8qEj1Imj%2Fstep%205.gif?alt=media&#x26;token=46567608-d70e-44b4-95a9-3b166b9cbe46" alt=""><figcaption></figcaption></figure>

#### Query Parameters

You can add or modify query parameters for each redirect. Query parameters will *not* be evaluated when deciding if an origin URL qualifies for a redirect. Only the domain and pathname will be evaluated.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fe3jxy07TwzzkBM7ngX6j%2Fstep%206.gif?alt=media&#x26;token=e25fe30e-c381-41e7-8cc0-f871b0d35a0f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: Query parameters from the origin URL *will be persisted* to the redirect URL even if they are not added in Intelligems. Use Intelligems query parameters to add new values or modify existing values.
{% endhint %}

#### Subdomain Redirects

Intelligems allows you to test redirects between subdomains. All subdomains used in a redirect test must be registered as a subdomain on your primary domain.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fb2nY2OGIdiaXUm47fP1E%2Fstep%207.gif?alt=media&#x26;token=37fb03ed-5327-417d-92e8-2d5b195c9750" alt=""><figcaption></figcaption></figure>

## **Step 4: Set up targeting if needed**

Targeting is an optional step. By default, a visitor will only be included in a split URL test if they visit the origin URL. When a visitor lands on the origin URL, they are randomized into a test group. If they are not in the control group, they are redirected to the specified destination URL.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

### **Example: Creating a Split URL Test for a Meta Campaign**

{% embed url="<https://www.loom.com/share/2a716fb9605e4c649fab9f88fa6e36b4?sid=e23fe9c9-4c1a-478a-9913-a1a9395e332f>" %}

## **Step 5: Set Your Test Goals**

Finally, select whether analytics should by default consider only orders containing certain products you want to test (for example something related to a particular PDP), or orders containing any products in your shop.\
\
You can always change this later after the test has started by changing the option in your Analytics filters.&#x20;

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FlezSQlH6wjhXj6xsl64f%2Fstep%208.gif?alt=media&#x26;token=cfaeadfd-45c0-4f4b-a4d4-aae81de8910d" alt=""><figcaption></figcaption></figure>


# How to Set Up an Onsite Edits Test

Onsite Edits tests allow you to test smaller components on your site using our Onsite Editor. This is best for smaller changes, such as copy changes, color changes, image swaps, and more.

{% embed url="<https://www.loom.com/share/8abe3a73a3dc4e769be4839a90ba7c9e>" %}
How to use the onsite editor
{% endembed %}

## **Step 1: Create a new test**

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click 'Create New Test' above the experiments table. Give it a name, and a specific description of what you're testing. Select "Content Test", then "Onsite Edits", then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FjlKNMeJVW6ZFrXO5JGSD%2FStep%201.gif?alt=media&#x26;token=8f81f125-6a7c-4e8e-9f74-9a6071e981ce" alt=""><figcaption></figcaption></figure>

## **Step 2: Create your test groups**

Create a test group for each variation you want to include in the test. Fill in the Test Name and Test Description for the experiment you are creating. This information is all internal - the more detail you include here the better! Tests can be live for several weeks, and your future self will thank you for including the details here.

You can add new groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider to allocate what percentage of traffic will go to each group. Click ‘Continue’ when you are done.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F2SCIJvjUTevR5gQlq2Rn%2FStep%202%20.gif?alt=media&#x26;token=90e5c6b4-c971-4b05-b6bb-adb4821c48c8" alt=""><figcaption></figcaption></figure>

## **Step 3: Set up targeting if needed**

Targeting is an optional step. By default, a visitor will be immediately assigned to one of the test groups using its random split-test mechanism. This assignment is determined at the first visit and is stored via a first‐party cookie, ensuring that the visitor remains in the same group on subsequent visits during the edits test period. Onsite Edits are made at the selector level; these same selectors can and do appear on many pages throughout the site.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

## Step 4: Select "Add & Edit changes in Visual Editor"

Selecting this will save your test and take you to your website with our widget open and edit mode enabled. From here, you can set up any Onsite Edits you would like. See each of the guides below for more information on setting up different types of onsite edits.

* [Onsite Editor](https://docs.intelligems.io/general-features/onsite-editor)
* [Image Onsite Editor](https://docs.intelligems.io/general-features/image-onsite-editor)
* [CSS & JavaScript Injection](https://docs.intelligems.io/general-features/css-and-javascript-injection)

## Step 5: Set Your Test Goals

Finally, select whether analytics should by default consider only orders containing certain products you want to test (for example something related to a particular PDP), or orders containing any products in your shop.\
\
You can always change this later after the test has started by changing the option in your Analytics filters.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F9XiQdweqkXxbF6C4ni3w%2FStep%203.gif?alt=media&#x26;token=ab1046eb-ca39-4814-8715-0204083547d8" alt=""><figcaption></figcaption></figure>


# How to Set Up a Template Test

Template testing allows you to split-test Shopify templates to determine which is the best for conversion, revenue, and profit. Take a look at Shopify's documentation on templates [here](https://help.shopify.com/en/manual/online-store/themes/theme-structure/templates)!

{% embed url="<https://www.loom.com/share/09533b20ec24444191e621001893c7b8>" %}
Video: Setting up a template test in Intelligems
{% endembed %}

{% hint style="warning" %}
Make sure that the Intelligems template snippet is installed in your theme. If you are using the Intelligems Theme Block, it will automatically be added. If you are using the Intelligems javascript snippet, [more information can be found here](https://docs.intelligems.io/developer-resources/intelligems-theme-snippets). This snippet must be included in your theme for template tests to work properly.
{% endhint %}

{% hint style="warning" %}
All templates for a Template Test must be in a live theme.
{% endhint %}

## **Step 1: Create a new test**

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click 'Create New Test' above the experiments table. Select "Content Test" , then "Template Test", then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FlZNT5plPG99jO0SAo3j4%2FStep%201.gif?alt=media&#x26;token=05c4376a-9b24-4477-9fd3-7b5953c266a7" alt=""><figcaption></figcaption></figure>

## **Step 2: Create your test groups**

Create a test group for each template variation you want to include in the test. Fill in the Test Name and Test Description for the experiment you are creating. This information is all internal; the more detail you include here the better. Tests can be live for several weeks, and your future self will thank you for including the details here.

You can add new groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider to allocate what percentage of traffic will go to each group. Click ‘Continue’ when you are done.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FxTzFqNK8tip04GoGiutp%2FTest%20Groups.gif?alt=media&#x26;token=b2473bd7-b6c2-4989-af4c-c8a7720e2958" alt=""><figcaption></figcaption></figure>

## **Step 3:** Assign a template for each test group

Select a template for each test group. You can choose an existing template or duplicate the template selected for the control group by selecting `Duplicate Control:`

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F5UhzXAaz62jV68XWWNNU%2FStep%202.gif?alt=media&#x26;token=7ef4c316-337c-40ff-b88c-a48cff7d3343" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Please note that only templates chosen for your test groups will be tested. For example, if you choose `product-template-a` (control group) vs. `product-template-b`, only products assigned to the template in the control group will be affected by the test.

If you're testing templates, a visitor will only be included in the test if they visit a page that is by default assigned to the template selected for the control group. Therefore, the template that is currently in use on your site must be chosen as the control group.
{% endhint %}

You can hover over each test group screenshot to view the following options:

* Edit in Shopify: links to the test group template in your Shopify admin (must be a live theme)
* Quick View: opens a snapshot with a desktop and mobile preview of the test group template
* View in Browser: links to a preview of the template in a new tab
* Template Name: opens edit mode for the test group template

If you have made changes to a selected template in Shopify, you can use the "refresh" button next to the test group name to refresh the screenshot shown.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FbRxOsREceLtgr5rKXbfy%2FStep%204.gif?alt=media&#x26;token=9f0efa64-5223-4bd6-9a56-58a5a091d5b8" alt=""><figcaption></figcaption></figure>

## **Step 4: Set up targeting if needed**

Targeting is an optional step. By default, a visitor will only be included in a template test if they visit a page that is by default assigned to the template selected for the control group. Therefore, the template that is currently in use on your site must be chosen as the control group.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

## Step 5: Set Your Test Goals

Finally, select whether analytics should by default consider only orders containing certain products you want to test (for example something related to a particular PDP), or orders containing any products in your shop.\
\
You can always change this later after the test has started by changing the option in your Analytics filters.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fvye4zpgbBQQIDgwhRGo6%2FGoals.gif?alt=media&#x26;token=d4af6661-9bba-4582-84ad-828c5e6070eb" alt=""><figcaption></figcaption></figure>


# How to Set Up a Theme Test

Theme testing allows you to split test Shopify themes to determine which is the best for conversion, revenue, and profit.

{% embed url="<https://www.loom.com/share/d4d81d1875804300bfbe52e3d88b65ae?live_rewind=1>" %}

## **Step 1: Create a new test**

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click 'Create New Test' above the experiments table. Select "Content Test" , then "Theme Test", then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FSZ9uKgcNFivr3vDzqJNs%2FStep%201.gif?alt=media&#x26;token=2bfedc04-7464-492d-9af8-1d3abb5ea566" alt=""><figcaption></figcaption></figure>

## **Step 2: Create your test groups**

Create a test group for each theme you want to include in the test. Fill in the Test Name and Test Description for the experiment you are creating. This information is all internal - the more detail you include here the better! Tests can be live for several weeks, and your future self will thank you for including the details here.

You can add new groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider to allocate what percentage of traffic will go to each group. Click ‘Continue’ when you are done.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FxTzFqNK8tip04GoGiutp%2FTest%20Groups.gif?alt=media&#x26;token=b2473bd7-b6c2-4989-af4c-c8a7720e2958" alt=""><figcaption></figcaption></figure>

## **Step 3:** Select the themes you want to test

Select the theme you'd like to test for each test group.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F9yoAUYXEu3cu3VzEWyK2%2FStep%202.gif?alt=media&#x26;token=ae558c90-2759-4cd5-a987-bc30f48c7159" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Make sure the [Intelligems script is installed](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) in all themes that you're testing! This is how we will hide the preview bar at the bottom of the theme. If you have checkout.liquid, ensure you have installed the Intelligems script on this page as well, so that the preview bar is hidden at checkout (if you do not have checkout.liquid, the bar will be hidden automatically).
{% endhint %}

{% hint style="info" %}
Product page templates are set at the product level, and the template name must be available in the live theme. When testing two different themes, make sure the template names match, so that the templates you've chosen for each product exist in both themes. If the product pages look correct when previewing the test theme(s), then you're good to go!
{% endhint %}

## **Step 4: Set up targeting if needed**

Targeting is an optional step. By default, a visitor will be immediately assigned to one of the test groups using its random split-test mechanism. This assignment is determined at the first visit and is stored via a first‐party cookie, ensuring that the visitor remains in the same group on subsequent visits during the theme test period. Every theme that you include in your test configuration—both the live theme and the test themes—is part of the theme test.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

## Step 5: Set Your Test Goals

Finally, select whether analytics should by default consider only orders containing certain products you want to test (for example something related to a particular PDP), or orders containing any products in your shop.\
\
You can always change this later after the test has started by changing the option in your Analytics filters.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fvye4zpgbBQQIDgwhRGo6%2FGoals.gif?alt=media&#x26;token=d4af6661-9bba-4582-84ad-828c5e6070eb" alt=""><figcaption></figcaption></figure>

## Previewing Themes through Shopify Admin

When trying to preview a theme through Shopify Admin, you might get redirected to a different theme if that theme has been used in an Intelligems theme test. Let's look at an example when there is a live Intelligems theme test:

Control Group: Default Theme (Theme ID: 1)

Test Group: Secondary Theme (Theme ID: 2)

If you preview Secondary Theme from Shopify Admin and have not been previously included in the live Intelligems theme test, you'll be randomly assigned a test group when you enter Secondary Theme. Depending on your test group assignment, you'll either remain in the Secondary Theme if you were assigned to the test group, or you'll be redirected to the Default Theme indicating you were assigned to the Control Group.

Let's say you were assigned the test group and remain in Secondary Theme. If you were to preview the Default Theme from Shopify Admin, you'll be redirected to the Secondary Theme since that is the theme assigned to your test group. If you wish to preview the Default Theme, you can use the Intelligems preview widget to switch your group.

## Why am I still being redirected away from a theme when I don't have a theme test live?

This is to ensure all users who were assigned a preview theme during your test do not remain in a preview theme once that test is ended. This redirection will only happen for themes that were included in an Intelligems theme test and will only occur once. After your initial redirection, you'll be able to preview that theme through Shopify Admin normally.


# How to Set Up a Test using our JavaScript API

Intelligems allows you to set up powerful custom tests using its window object API.

## **Step 1: Create a new test**

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click "Create New Test" above the experiments table.

Fill in the Name and Description for the experiment you are creating. This information is all internal - the more detail you include here the better! Tests can be live for several weeks, and your future self will thank you for including the details here. Select 'Content Test", then "Onsite Edits", and then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FeFLfoxkPKPoQQUaS73QN%2FAPI-%20Create%20New%20Test.gif?alt=media&#x26;token=46779aa2-9078-4c02-ae67-11e4339e3003" alt=""><figcaption></figcaption></figure>

## **Step 2: Create your test groups**

Create between two and five groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider to allocate what percentage of traffic will go to each group. When you are done adding groups, click "Next step" in the top right.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FZbyxqCX2H6NgZ6ycHPCs%2FCreate%20Test%20Groups.gif?alt=media&#x26;token=c60b45a8-6749-4aa2-9f03-08198ccd8743" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The more groups you have, the longer it will take to get statistically significant results. You’ll need about 300 orders for each group in the test to detect a 10% change in conversion with 90% confidence.
{% endhint %}

## Step 3: Skip "Modifications"

No need to set up any Content Edits, Styles or JavaScript in this step of the set up if you are planning to use our JavaScript API. Go ahead and move on to step 4.

## **Step 4: Set up targeting if needed**

Targeting is an optional step. This tool allows you to apply specific conditions to certain site visitors.

There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

## Step 5: Choose how you'd like to measure your results and save your test

Finally, select whether analytics should by default consider only orders containing certain products you want to test (for example something related to a particular PDP), or orders containing any products in your shop. You can change this later after the test has started by changing the option in your Analytics filters. Go ahead and save the test, and move on to step 6.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FXPBl2k1zjZ820OMwJCYq%2Fimage.png?alt=media&#x26;token=28fcf285-d0e2-4e5c-b636-92448f361687" alt=""><figcaption></figcaption></figure>

## Step 6: Get relevant IDs

Custom content tests require you to know the experiment ID and test group IDs so that you can branch your design or logic accordingly. You can get this information by clicking the "Show Info" button in the more menu:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F1peMjMRgXmTlRzWfmCGK%2FGet%20Relevant%20IDs.gif?alt=media&#x26;token=aa8600b0-5179-440e-9f11-4d390f0ff861" alt=""><figcaption></figcaption></figure>

## Step 7: Use the Intelligems window object API to set up your custom test

Now that you have your test group IDs, you can use Intelligems' [window object Javascript API](https://docs.intelligems.io/developer-resources/javascript-api) to get the current user's test group for the given experiment. Once you know the user's test group, you can branch logic and styling with it. For example, you might set a class or show/hide an element to affect styling, or conditional logic in your own Javascript code to provide a different experience.


# Content Test QA Checklist

{% hint style="info" %}
This QA list is specific to a content test. If you are QAing a [shipping test](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist) or a [pricing test](https://docs.intelligems.io/price-testing/price-test-qa-checklist), please check out QA checklists for those types of tests!
{% endhint %}

Once your content test is setup, you'll need to QA your site to make sure everything is working as it should be. Before heading to your site, there are a few things you should check first to make sure your integration is functional:

* [ ] Is Intelligems JavaScript in your live theme? Check out [this article](https://docs.intelligems.io/developer-resources/intelligems-javascript) for more information on where to find this.
* [ ] Are you running a [Theme test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-theme-test)? If you are, is Intelligems JavaScript in the themes you are testing as well? Including in checkout.liquid, if you have that file?
* [ ] Are you running a [Theme Template test](https://docs.intelligems.io/content-testing/how-to-set-up-a-content-test/how-to-set-up-a-template-test) on specific templates only? If you are, have you added [this snippet](https://docs.intelligems.io/developer-resources/intelligems-javascript#template-testing-snippet) to your theme yet?

Once you have confirmed all of the above, you can preview the test on your live site. Enter Preview mode by clicking the `...` next to your test and select `Preview`

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FRvF5EuxjerzLdavTX0c6%2FScreenshot%202023-08-30%20at%2010.19.27%20AM.png?alt=media&#x26;token=0248cfa8-efcd-41d4-98cb-af2748d1bdac" alt=""><figcaption></figcaption></figure>

This will open your site up in a new window with the Intelligems preview widget enabled. In the preview widget, you'll see:

1. The name of the test you are previewing in the top left
2. A dropdown to switch between different test groups in the bottom left
3. A toggle to highlight any replacements in the top right
4. An edit button in the bottom right; this enables integration mode, where you can edit any replacements

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fa76ZRgerGtWVK3SkWr51%2Fimage.png?alt=media&#x26;token=495d4e1f-0418-4351-8a37-9b8b821a8ae9" alt=""><figcaption></figcaption></figure>

Now that you are on your site, use the preview widget to toggle between your test groups to make sure the correct content is showing on your site for each test group. What you should check depends on what type of content test you are previewing. For a few areas you should check for each test type, see below.

#### Theme Tests

* [ ] When you switch test groups in the dropdown, does the theme update to display the correct theme? You can check this based on differences that you know of in the test theme, or by searching the source code for the current theme name. You should also see a message similar to the below at the bottom of the preview widget for any themes that are not currently live.

  <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FR9sabTtuEFhVU5QXI8BO%2FScreenshot%202023-10-20%20at%203.38.01%20PM.png?alt=media&#x26;token=efe77db0-385d-4a88-98e9-505a535dee3d" alt=""><figcaption></figcaption></figure>
* [ ] Does a Shopify preview bar show at the bottom of your window when you are in a test theme? This shouldn't happen; confirm that the Intelligems JavaScript is in all themes included in the test in both the theme.liquid and the checkout.liquid files.

#### Theme Template Tests

* [ ] When you switch test groups in the dropdown, are the correct templates used where they are being tested? You can check this based on differences that you know of in the templates.

#### Page Redirect Tests

* [ ] Go to a page that is included in a redirect while in a non-control group in the preview widget. Are you redirected to the correct link?
* [ ] Check the above for each test group and page being tested. You'll need to navigate away from the test page and go back once you have changed groups to be redirected.
* [ ] Do you have the Redirect Once checkbox selected for any of your redirects? Read more about how that functions [here](https://docs.intelligems.io/content-testing/how-to-set-up-a-content-test/how-to-set-up-a-page-redirect-test#redirect-once) and confirm you have the correct setting on for your test.

#### Find & Replace Tests

* [ ] Navigate to a location on your website where you have set up a text, image, or CSS / JS replacement. Switch groups in the widget and confirm that the content is updating as expected.
* [ ] Continue the above until you have checked all locations where a replacement has been set up.
* [ ] Do a sweep of the site to make sure content is not being updated somewhere that it shouldn't be. Our replacements are based on selectors. If there is a selector that is the exact same somewhere else on the site, the content there could be updated inadvertently. To avoid this happening, try setting up [Page Targeting](https://docs.intelligems.io/content-testing/targeting#what-is-intelligems-page-targeting) or including a "Find" in your Find & Replace.

#### A few other things to keep in mind:

* [ ] Do you have Page Targeting set up on your test? If so, if you are on a URL that does not match your targeting, you'll see a message like the below in the preview widget. This will confirm that your page targeting is working as expected since you are not meeting any of the conditions.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FcQzDkkvCsYyBYWOUXzeZ%2Fimage.png?alt=media&#x26;token=f6af2709-6dd6-42e5-8c75-662832eaacb7" alt=""><figcaption></figcaption></figure>

* [ ] You can further confirm that Page Targeting is working by going to one of the URLs that does match your targeting. Once you do so, you'll see the widget will no longer show a message on the bottom about being excluded.


# Ending a Theme Test

{% hint style="danger" %}
After ending a theme test, we recommend you not delete any theme that was in the test for at least two months
{% endhint %}

During the experiment, visitors are sent to draft themes, and their browser will "remember" which theme to open the next time they visit your store via a session cookie. Once the test is over, if a visitor who was in one of the test groups re-visits your store and the cookie is still active, Shopify will load the draft theme, and Intelligems will then immediately reset them back to the live theme.

However, if the draft theme that was in the test has since been deleted, Intelligems won't be loaded and won't have the opportunity to reset the visitor's theme. Instead, the visitor see an error from Shopify, since they're trying to load a theme that does not exist.\
\
So, it's important to leave any themes that were tested in draft mode (rather than deleting them) for a while after the experiment, to ensure any returning visitors are reset back to the live theme.


# Content Testing FAQs

Common Questions about Content Testing

## General

<details>

<summary>Why should I run a template or content replacement test instead of a theme test?</summary>

Theme tests are a great way to test large changes to your store, or experiments that would otherwise require a developer to implement. There are a few drawbacks to keep in mind, however, so you may choose to run a template test or content replacement test instead:

1. A theme test means you have multiple live themes. Your customers are accessing your store via multiple themes, so you need to ensure any changes unrelated to the test (e.g., adding a landing page, editing copy or imagery) are made in all themes in the test.
2. Every visitor goes through a redirect. As mentioned above, theme tests are relatively high performing, but every visitor placed into a non-control group will still go through a one-time redirect to bring them to the correct theme for their group. While the UX impact of this one-time redirect is generally low, you may be able to avoid it altogether by using a content replacement test to dynamically edit content or inject HTML/CSS/JS.
3. You won't be able to delete any themes in the test for a while. During the experiment, visitors are sent to draft themes, and their browser will "remember" which theme to open the next time they visit your store via a session cookie. Once the test is over, if a visitor who was in one of the test groups re-visits your store and the cookie is still active, Shopify will first load the draft theme, and Intelligems will then immediately reset them back to the live theme. However, if the draft theme that was in the test has since been deleted, Intelligems won't be loaded and won't have the opportunity to reset the visitor's theme. Instead, the visitor see an error from Shopify, since they're trying to load a theme that does not exist.\
   \
   So, it's important to leave any themes that were tested in draft mode (rather than deleting them) for a while after the experiment (we recommend at least 1 week), to ensure any returning visitors are reset back to the live theme.

</details>

<details>

<summary>I'm running a content test and noticed the control content (i.e. URL, theme, language, etc.) flashes for a second before I see the test group content. How can I fix this?</summary>

Intelligems has two options for installing our JavaScript in your theme:

1. By using our app embed
2. By manually installing it into the theme code

The app embed works really well in most cases, but it can cause some flashing for certain tests and sites. If you notice this happening on your site, we recommend following these steps:

1. Turn the app embed off in all theme included in the test. You can do this by going to Shopify and in the online store section, click "Customize" next to each theme. In the left side menu, click the bottom option, which is "App Embeds". Turn the toggle off next to Intelligems and hit save.
2. Follow [these steps](https://docs.intelligems.io/developer-resources/intelligems-theme-snippets#option-2-add-script-tag-in-theme-head) to manually add the Intelligems script tag to your theme's head in the theme.liquid and all theme.\*.liquid files.

If you still notice any flashing after making that change, please reach out to our support team [here](https://docs.intelligems.io/content-testing/broken-reference) - there are a few settings we can turn on that allows us to load more information more quickly to avoid any flashing.

</details>

<details>

<summary>Can I test the One Page vs Three Page checkout, or test specific components on the checkout page, such as whether to include upsells?</summary>

Unfortunately we cannot A/B test the One Page vs Three Page checkout currently - this option has to be either on or off, so there isn't a way for us to turn it on for some visitors and not others. This is a Shopify limitation.

We can test other components on the checkout page if you are on Shopify Plus. You can test components on that page using our Checkout Experiences feature, which you can read more about [here](https://docs.intelligems.io/checkout/testing-checkout-experiences). This feature is limited to Shopify Plus because it uses Shopify's Checkout Blocks feature, which is only available for brands on Shopify Plus.&#x20;

</details>

## Split URL Tests

<details>

<summary>Why must visitors visit the Origin URL to be included in the test?</summary>

Visitors must visit the Origin URL because this is the only page where Intelligems can detect their arrival and assign them to a test group. When a visitor lands on the Origin URL, our system:

1. Identifies that they've entered the test
2. Assigns them to either the Control Group or a test variation
3. Redirects test group visitors to their designated destination URL

Without visiting the Origin URL first, there's no trigger point for test group assignment, so visitors remain outside the test entirely. This also keeps the test's denominator limited to people who have been exposed to the test, keeping your data as actionable as possible.

Another thing to note is that URL redirect tests work in **one direction only**: from the Origin URL to the test destination URLs. Therefore, if a visitor lands directly on a destination URL (bypassing the Origin URL), they won't be included in the test. This is because:

* They never triggered the test assignment process
* Intelligems doesn't know they should be part of the test
* They won't be tracked in test results or analytics

To ensure accurate test results, visitors must enter through the Origin URL to be properly allocated and tracked.

</details>

<details>

<summary>I got an error that said I am on the wrong destination URL for my test group while previewing my test - what does this mean?</summary>

In a split URL test, Intelligems monitors site visitors who visit your Origin URL, then either keeps them there or redirects them based on their assigned test group. Our preview widget detected that you're on a destination URL for a test group that you're not currently previewing. Please note, Intelligems will not redirect you away from a destination URL, as our redirects only function in one direction: from the origin to the destination.

To continue testing your split URL test, please navigate to the Origin URL again.

</details>

<details>

<summary>I got an error that said I have enabled the setting for "Redirect One Time" for this test, and I have already been redirected while previewing my test - what does this mean?</summary>

Intelligems has two options for how a visitor can be redirect in a split URL test -

1. Redirect One Time: A visitor will only be redirected the first time they land on the origin URL
2. Redirect Every Time: A visitor will be redirected every time they land on the origin URL

Because you have enabled "Redirect One Time" for your test, and you have already been redirected one time, Intelligems will not redirect you again, unless you clear your redirect history by clicking the button to do so in the preview widget.

If you'd prefer to change this setting, please see our help guide [here](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test#redirect-one-time-vs.-redirect-every-time) on where you can do so.

</details>

## Onsite Edits Tests

<details>

<summary>What is a query selector and why does Intelligems use them?</summary>

A query selector is a way to select an element on a webpage using CSS-style syntax in JavaScript. In this case, we created a query selector based on the element you clicked on, which means it automatically targets that specific part of the page. However, this selector is just a starting point—you can edit it to be more general, more specific, or to target a different element altogether, depending on what you need your code to do.

</details>

<details>

<summary>Can we test an image vs. a video (MP4)?</summary>

Yes! This can be done using an [HTML Onsite Edit](https://docs.intelligems.io/general-features/onsite-editor).

</details>

<details>

<summary>Can we test our Pop-Ups with Intelligems?</summary>

Yes!

### **Overview**

Testing pop-ups is a common way to evaluate the impact of on-site messaging, promotions, or lead capture strategies without making permanent code changes.

With Intelligems, you can run A/B or multivariate tests on pop-ups to measure their effect on conversion rates, email capture rates, or profit per visitor.

Pop-ups are often powered by third-party apps (e.g. Klaviyo, Justuno, Alia, Privy, Postscript etc.), or sometimes implemented natively in a Shopify theme. Intelligems can generally integrate with either approach by letting you toggle visibility, edit content, or inject custom logic on who sees the pop-up.

### Test Setup Types

Pop-ups can be tested using multiple Intelligems test setups. The right choice depends on how the pop-up is built and what aspect you want to test:

#### 1. Onsite Edits Test - CSS or Javascript **Injection**

* **Best for:**
  * Turning a third-party app’s pop-up hide/show.
  * Swapping content or offers inside an existing pop-up container.
  * Changing timing (e.g., show at 5s vs. 20s).
* **How it works:** Use Intelligems’ editor to show, hide, or modify a pop-up on-page.

**Example to show the Pop Up:**

```css
#my-popup {
    display: block;
}
```

***

**Example to hide the Pop Up:**

```css
#my-popup {
    display: none !important;
}
```

**Notes:** We generally recommend having the Pop-Up on your theme and using Intelligems to Show/Hide it rather than "injecting" the popup itself. If you want to change which popup is displaying, you should either:

1. Have multiple present in your theme, with all but one hidden by default, then use CSS to swap which one is hidden
2. Use JS to "tell" the popup provider which version to render

If you would like us to take a deeper look at your set up, please reach out to our support team for help!

#### 2. **Split URL Test**

* **Best for:**
  * Comparing two entirely different pop-up designs built in Shopify or a page builder (e.g. Replo, Shogun).
  * Testing different pop-up apps without overlap.
* **How it works:** Control and variant each point to different Shopify pages or landing pages, each with their own pop-up configuration.
* **Notes:** Each page must be self-contained with its own tracking and pop-up triggers.

***

### Setup

To test pop-ups with Intelligems, you’ll generally follow one of these approaches:

1. **Follow the steps to set up an** [**Onsite Edits Test**](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)
   * In Control: no pop-up (or your original pop-up).
   * In Variant: show new pop-up design, offer, or timing.
2. **Swap Pop-Up Content**

   In your new group, adjust the pop up using the one of the methods described above. This can be useful for testing offers (e.g. “10% Off” vs. “Free Shipping”).
3. **Adjust Targeting & Triggering**
   * Combine Intelligems audience targeting with your pop-up (e.g. first-time visitors vs. returning customers).
   * Change when or how the pop-up fires (e.g. on scroll, after X seconds, exit intent).
   * Compare whether different timing increases conversions without disrupting browsing.

### Use Custom Events to Filter Results

#### Tracking Engagement with Custom Events

For deeper analysis, you can use [**custom events**](https://docs.intelligems.io/analytics/custom-events) to track whether a visitor actually engaged with a pop-up. This allows you to segment and filter results in reporting (e.g., conversion rates among users who saw or clicked the pop-up vs. those who did not).

**Why this matters:**

By tagging these events, you can evaluate whether the pop-up itself is influencing conversion behavior — not just whether the variant group had higher performance. This makes results easier to interpret and helps confirm if engagement with the pop-up is the driver of uplift.

### Best Practices

* **Isolate one variable at a time**: Test *either* the offer, design, or timing, but not all at once, to avoid confounding results.
* **Connect to downstream KPIs**: Go beyond email sign-ups—measure profit per visitor by adding your COGS in Intelligems to confirm the pop-up improves business results.
* **Consider device experience**: Pop-ups can behave differently on mobile vs. desktop. Always QA on both.

### Limitations

* **Third-party app restrictions**: Some pop-up apps don’t expose all timing/triggering logic to external scripts. In these cases, Intelligems can usually control *visibility* or *injection*, but not the app’s internal scheduling.
* **Theme-level vs. app-level**: If the pop-up is baked into the theme code, edits must be structured as content tests. If powered by an app, you may need to coordinate app settings with Intelligems settings and targeting.

</details>

## Template Tests

<details>

<summary>Why must visitors visit a page assigned to the Control Group's template in Shopify to be included in a Template test?</summary>

Visitors must visit a page that uses the Control Group's template because this is the only way Intelligems can detect their arrival and assign them to a test group. When a visitor lands on a page using the control template, our system:

1. Identifies that they've entered the test
2. Assigns them to either the Control Group or a test variation
3. Dynamically serves the appropriate template based on their test group

Without visiting a page that uses the control template, there's no trigger point for test group assignment, so visitors remain outside the test entirely.

You can check which pages are assigned to a template in Shopify by following [these steps](https://www.loom.com/share/5f4cd7c9e008488287d4086d370a50f3?sid=b4028c6b-b07d-4b6b-8690-ff1507766205), or in your Shopify admin.

If your control template isn't assigned to any pages in Shopify, no visitors will be included in your test. To fix this:

1. Assign your control template to relevant pages in Shopify
2. Or choose a different template to use as your Control that's already assigned to pages you want to test

</details>

<details>

<summary>How can I roll out a winning homepage template?</summary>

Shopify doesn't allow you to switch homepage templates. The winning template will have to be recreated in the original template.

An easy way to do this is within the theme editor. Find the test template and copy its contents into the default template (usually `index.json`).

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FWU5KFmuLEdiuZNY2HVjr%2Fimage%20\(13\).png?alt=media\&token=16677177-3642-413c-8bd1-1999c2188396)

</details>

## Theme Tests

<details>

<summary>Why do I see the Shopify theme preview bar during my theme test?</summary>

During a properly functioning Intelligems theme test, visitors will never see the Shopify theme preview bar. If you're seeing the preview bar, it's likely because the Intelligems JavaScript is not installed in all themes being tested. The Intelligems script needs to be in the live theme, plus all themes in the test.

If the script is in only the live theme, for example, visitors will be put into test groups and will be redirected to a draft theme, but since the Intelligems script is not in the draft theme, the preview bar will not be hidden once they're there, and Intelligems' analytics tracking will not function properly.

To fix this issue, install the Intelligems script in the live theme and all themes that you're testing. Since theme tests require a redirect, we recommend installing the Intelligems script synchronously by adding the script tag to your theme's head in the theme.liquid and all theme.\*.liquid files (learn more [here](https://docs.intelligems.io/developer-resources/intelligems-theme-snippets#option-2-add-script-tag-in-theme-head)).

</details>

<details>

<summary>How does a theme test impact page load speeds?</summary>

Theme tests are relatively high performing, however, there may be a performance impact on a visitor's first page view. If Intelligems detects that a visitor is in the wrong theme, it will immediately reload the page in the correct theme. From then on, that visitor will be in the correct theme for their test group, which may be an unpublished theme. Our benchmarking shows that there is no performance impact on these subsequent page views, even for unpublished themes. If you're concerned abotu the potential performance impact of a reload on the first page view, you might consider using an onsite edit test instead.

</details>


# Getting Started with Experiences

Experiences allow you to custom tailor every visitor’s shopping experience with targeted offers, layouts, branding and copy - saving time and maximizing profits.

{% embed url="<https://www.youtube.com/watch?v=HVfyqao3XRg>" %}

## What are Experiences?

An Experience shows one or more site modifications to all visitors or a targeted audience, temporarily or permanently.

With a broad range of Modifications including URL redirects, text changes, offers and price changes, layout changes, javascript injections, Global Style components like progress bar, quantity buttons, slideouts, and more, an Experience can be used to completely overhaul your site or simply fine tune text and layouts.

{% hint style="info" %}
**How do Experiences relate to Personalizations?** Intelligems Personalizations have been upgraded and renamed to Experiences. Experiences offer the same discounts, targeting, and testing features of Campaigns, but go above and beyond allowing you to serve additional site changes to your visitors, target with more sophistication, add more flexible components, better analyze metrics, and more.
{% endhint %}

## What can you achieve with Experiences?

While Intelligems’ testing tools allow you to pit experiences against each other to find which ones produce the best results, Experiences allow you to act on those findings and show the right experience to the right shop visitors quickly, all without writing code.

With Experiences you can:

* **Deploy, test, and target offers:** Offer codeless promotions, volume discounts, and free gifts, displaying popups, progress bars, quantity buttons, and other components. For example, you can offer a discount and modified copy to all returning visitors. To make informed decisions, you can also test offers against each other to determine which ones work best for a target audience before deploying them.
* **Quickly ship codeless edits**: Immediately go live with changes without Shopify limitations or developer delays. For example, you could deploy a warning about delayed international shipping to everyone outside your country.
* **Maintain consistency from ads to Landing Pages:** Send visitors to unique landing pages with personalized content and offers. For example, you can show a banner at the top of your PDP only to visitors arriving from an Instagram campaign by redirecting them to a different page, or swapping your Shopify page layout depending on the audience. You can do all of this without having to manage multiple links.
* **Personalize product discovery:** Boost conversions by showing different collections for certain customers. For example, redirect athletes to a version of your home page that highlights sports-related products in your main collection.
* **Overhaul your site’s look and feel:** Show a completely different Shopify theme with altered navigation for users in a different country.
* **Lower your prices:** Show lower prices for one or more products during a special event or when overstocked.
* **(Coming soon) Take action on your test results:** Quickly roll out winning variants to all visitors or specific customer segments.

## How do you make and use an Experience?

Before using Experiences and most other Intelligems features, you'll need to add the Intelligems script to your theme; [here is our help guide](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme). Once you've done that:

* **Step 1 - Initialize:** There are three ways to create an Experiences.
  * Option 1: Go to the Experiences > Site Content > Select which type of Content change(s) you want to create
  * Option 2: Go to Experiences > Offers > Select which type of Offer(s) you want to create
  * Option 3: Go to one of your tests and use the “Roll out” button to Roll a winning test group into a Experience. This will carry out many of the steps below automatically, saving you time.
* **Step 2 - Modifications:** Add one or more modifications based on your goal, whether it’s a simple text change, adding a component like progress bar, quantity button, or slideout,  or as complicated as a rebrand with interactive javascript elements. Click [here](https://docs.intelligems.io/personalizations/personalization-modifications) to read more about Modifications.
* **Step 3 - Targeting:** Decide who should see the Experience, if not all visitors to your site. Intelligems allows you to limit visitors to those that match robust rules, those coming in via a special link, and those shopping in a certain currency. You can also limit which site pages the modifications should appear on, if not all. Click [here](https://docs.intelligems.io/personalizations/targeting-personalizations) to read more about Targeting.
* **Step 4 - Preview:** Make sure everything looks and works as you’d expect before activating it. Click [here](https://docs.intelligems.io/personalizations/previewing-personalizations) to read more about Previewing.
* **Step 5 - Activate it:** Once you’re ready, activate it. You can pause and resume as many times as you need, which is useful for recurring promotions.

You can also:

* **Track Stats:** Check how many visitors saw each Experience and which ones delivered the most orders and revenue.
* **Update:** Edit a Experience at any time to change its modifications, targeting, and more.
* **Combine:** Stack Experiences, allowing a visitor to be presented with more than one Experience at the same time. For example, a visitor can be exposed to a “New visitors discount” Experience while also seeing the homepage layout tweaks of the “Mobile users Optimization” Experience.
* **Duplicate:** When creating multiple similar Experiences, you can save time by duplicating an existing one and editing it rather than starting from scratch. This is also a handy way to preview changes you want to make to an active Experience without needing to turn it off.
* **Launch Offers:** One type of modification within an Experience is an "Offer". An example of this may be a discount or free gift with purchase. Intelligems allows you to launch Offers as an Experience, outside of a test.&#x20;
* **Launch Checkout Blocks:** With Checkout, you can launch content blocks on your Checkout page for Shopify Plus customers. Trust badges, social proof, shipping messages, you name it. More blocks coming soon.&#x20;

{% hint style="info" %}
**Pricing:** While you can create Experiences - Site Content and Offers - on any Intelligems plan, you'll need to be on Plus or Blue to test Offers.
{% endhint %}

## Next Steps

See the guides below to delve deeper into Personalizations:

{% content-ref url="personalization-modifications" %}
[personalization-modifications](https://docs.intelligems.io/personalizations/personalization-modifications)
{% endcontent-ref %}

{% content-ref url="targeting-personalizations" %}
[targeting-personalizations](https://docs.intelligems.io/personalizations/targeting-personalizations)
{% endcontent-ref %}

{% content-ref url="previewing-personalizations" %}
[previewing-personalizations](https://docs.intelligems.io/personalizations/previewing-personalizations)
{% endcontent-ref %}

{% content-ref url="../offer-experiences/testing-offer-personalizations" %}
[testing-offer-personalizations](https://docs.intelligems.io/offer-experiences/testing-offer-personalizations)
{% endcontent-ref %}

{% content-ref url="personalizations-faqs" %}
[personalizations-faqs](https://docs.intelligems.io/personalizations/personalizations-faqs)
{% endcontent-ref %}


# Experience Modifications

This article walks you through the first step of setting up an Experience - choosing the Modifications that determine what changes will be applied to your site.

When setting up a Experience, you can add one or more modifications based on your goal - whether it’s as simple as a text change or as complicated as a rebrand with interactive javascript elements.

There are 3 classes of modifications:

* **Content changes -** these modify your text, layouts, and functionality.
* **Price changes -** used to update the prices on one or more products directly
* **Offers -** these deliver discounts and other promotions that appear on the PDP, in the cart, and at checkout without the need for coupon codes.

You can combine several modifications in one Experience, subject to limitations.

You can also limit which site pages your changes apply to by using [Page Targeting](https://docs.intelligems.io/targeting-personalizations#page-targeting).

## **URL Redirects**

URL Redirects allow you to set rules that re-route visitors from one page to another permanently or on a one time basis. This is useful in a variety of scenarios, and especially for showing a different version of a PDP to visitors coming from a specific channel or campaign.

**When to use Redirects:** URL redirects should be limited to a particular audience. When an Experience is aimed at all visitors rather than a specific segment, it’s best practice to just update all of your links directly in Shopify. This ensures better performance and keeps your baseline site set up the way you want it.

You can read more about URL Redirects [here](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test).

{% hint style="danger" %}
**Mixing URL Redirects with other Modifications:** Any modifications mixed with URL Redirects in the same Experience will not take effect until visitors hit the redirect origin page. For example, if your Experience contains a redirect from page A to page B, and also contains CSS change and Content Edit modifications, the CSS and Content Edits will not be visible until a visitor has visited page A. Once they have, all modifications will take effect and continue taking effect on all pages where they are applicable. To get around this, you can create two Experiences with identical audiences - one with the URL Redirect and the other with remaining modifications.
{% endhint %}

## **Content Edits**

Content Edits allow you spot edit, hide and rearrange text and page elements on various page of your site. Content Edits are made by clicking elements directly in your site using our visual builder. To make one or more content edits:

* Add the Content Edits modification
* Click to enter the visual editor in a new tab. Once you're there, click the icons on the top left to select text, images, and other page elements that you wish to change.
  * Read more about editing site images [here](https://docs.intelligems.io/general-features/image-onsite-editor)
  * Read more about editing other site elements [here](https://docs.intelligems.io/general-features/onsite-editor)
  * You can also change CSS and javascript here. Read more [here](https://docs.intelligems.io/general-features/css-and-javascript-injection)
* Once you’ve finished making changes, click Save. You can close this tab.
* Return to your original Personalization’s browser tab where you will see the list of edits you’ve made and can continue editing your Personalization.

{% hint style="info" %}
*You cannot use Content Edits if you have a headless storefront.*
{% endhint %}

## **Styles & Javascript**

If you're a technical user, you can use this Modification to inject custom CSS or Javascript into your site’s pages for visitors to this Experience. CSS modifications can be used to hide buttons or text, change layouts and spacing, swap backgrounds, or change your color palette and fonts. Javascript changes can be used to pop up messages, modify button behavior, send information elsewhere, and much more.

{% hint style="info" %}
You can find additional tips and tricks for writing effective CSS and javascript [here](https://docs.intelligems.io/general-features/css-and-javascript-injection), including how to ensure the page has loaded before your code runs.
{% endhint %}

## **Theme Changes**

This modification allows you completely overhaul your site - from branding to navigation - by showing a different Shopify theme for visitors in this Experience.

To set up a theme change, choose the theme you’d like to be shown instead of your shop’s live theme, making sure the theme is integrated so that Intelligems can function correctly.

Note that an Experience can not contain both a Theme Change and Template Change modification, as a particular template may not be present in the target theme.

{% hint style="danger" %}
Theme changes can leave your site unstable so generally should be[ applied directly in Shopify](https://help.shopify.com/en/manual/online-store/themes/adding-themes) if you are targeting all visitors. If you are targeting a specific audience, you should follow a number of precautions, preview carefully, and test your live site frequently. [Learn more here](https://docs.intelligems.io/personalizations/theme-personalization-precautions).
{% endhint %}

{% hint style="danger" %}
To ensure that your shop continues to function smoothly, do not delete your chosen theme for at least a month, even after stopping an Experience. [Learn more here](https://docs.intelligems.io/personalizations/theme-personalization-precautions).
{% endhint %}

{% hint style="info" %}
You cannot have more than one theme change active at the same time across your Personalizations and tests. Multiple theme changes can cause endless loops or failure in redirection. If you do have multiple theme changes live, make sure that your tests and Personalizations are targeting exclusive audiences.
{% endhint %}

## **Template Changes**

Template Changes allow you to overhaul the layout and appearance of a particular page or types of pages on your site by swapping out one page template in your site for another. You can read more about Shopify templates [here](https://help.shopify.com/en/manual/online-store/themes/theme-structure/templates).

You can read more about the ins and outs of Template Changes [here](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-template-test).

{% hint style="info" %}
Note that an Experience can not contain both a Theme Change and Template Change modification.
{% endhint %}

{% hint style="info" %}
We encourage using Template Changes targeted to specific audiences, but if you are targeting all visitors it's best to just change the template directly in Shopify to maximize performance, stability, and prevent unforeseen interactions between tests and Experiences.
{% endhint %}

Note also that each Experience is limited to swapping one single template for another. If you’d like to swap more than one template you can create multiple Experiences and assign them the same audience.

## **Offers**

There are multiple Offer modifications:

* Amount off products
* Amount off orders
* Volume discounts
* Free shipping
* Free gift

Offers can be configured to display customizable popups, progress bars, and quantity button components. Learn more about **Global Styles components**.&#x20;

Unlike Price Modifications, Offers do not update prices on your site pages and collections. Instead, like Shopify discount codes, they update the costs and totals shown in your cart and at checkout. If you want to update the prices shown on your site’s pages directly, use a Price modification instead.

[Have a look at this guide](https://docs.intelligems.io/offer-experiences/offer-modifications) for more details on offers and how to set them up.

{% hint style="info" %}
You cannot combine Offers and Price Modifications in a single Personalization
{% endhint %}

## **Price Changes**

Unlike offers, Price changes allow you to modify the actual price and compare-to (strikeout) price shown on individual PDPs and other pages across your site, rather than just showing a discount in your cart and at checkout.

To set up the Price Modification

* Tag Prices: before you display new prices, you must indicate to Intelligems where prices appear across the pages of your theme. This can be done in two ways: 1. (recommended) ask the Intelligems team do this for you as part of your site’s Integration process 2. Do it yourself in the onsite editor, [closely following these instructions](https://docs.intelligems.io/getting-started/price-testing-integration-guides). This only needs to be done one time.
* Select one or more products whose prices you’d like to reduce
* Enter new prices as well as compare-to prices. You can do this by
  * Manually typing them in
  * Using the quick-fill option to quickly reduce by a certain amount or percent
  * Downloading a spreadsheet of products selected, specifying new prices in the `Price-Control Group`, and `Compare Price - Control Group` columns, and uploading it again. Find out more about filling out the spreadsheet [here](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test#uploading-a-spreadsheet).
* Note that you can only reduce prices on products in a Personalization for technical reasons.

{% hint style="info" %}
You cannot combine Price Modifications and Offers in a single Experience
{% endhint %}

{% hint style="info" %}
Duplicate products and Subscriptions products are not supported for Experiences.
{% endhint %}

{% hint style="info" %}
Price Modifications do not work across currencies. Any Experience using a Price Modification will have [currency targeting ](https://docs.intelligems.io/targeting-personalizations#currency-targeting)activated and set to the default store currency. This means only visitors using the store's default currency will see the Experience.
{% endhint %}

Click [here](https://docs.intelligems.io/price-testing/price-testing-getting-started) to read more about price changes.

## Next Steps

Once you’ve set up your Modifications, you can go on to:

* Preview them to make sure everything functions correctly on your site before activating the Experience. Click [here](https://docs.intelligems.io/personalizations/previewing-personalizations) to read our Preview guide.
* Optionally Set Audience Targeting to limit who should see this Experience and which pages, if not all, the modifications should appear on. Click [here](https://docs.intelligems.io/personalizations/targeting-personalizations) to read the full Targeting guide.


# Theme Experience Precautions

## Setting up Experiences involving a Theme Change

A few reminders to make sure your Theme Experiences runs smoothly:

* Make sure the [Intelligems script is installed](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) in all themes that you're testing! This is how we will hide the preview bar at the bottom of the theme. If you have checkout.liquid file, ensure you have installed the Intelligems script on this page as well, so that the preview bar is hidden at checkout. If you do not have checkout.liquid, the bar will be hidden automatically.
* Product page templates are set at the product level, and the template name must be available in the live theme. When testing two different themes, make sure the template names match, so that the templates you've chosen for each product exist in both themes. If the product pages look correct when previewing the test theme(s), then you're good to go!

## Ending Experiences involving a Theme Change

{% hint style="warning" %}
After ending a Theme Experience, we recommend you do not delete the theme that was present in the Experience for at least a month.
{% endhint %}

While the Experience is active, visitors are sent to draft themes, and their browser will "remember" which theme to open the next time they visit your store via a session cookie. Once the Experience is stopped, if a visitor who was exposed to the Experience re-visits your store and the cookie is still active, Shopify will load the draft theme, and Intelligems will then immediately reset them back to the live theme.

However, if the draft theme that was in the Experience has since been deleted, Intelligems won't be loaded and won't have the opportunity to reset the visitor's theme. Instead, the visitor sees an error from Shopify, since they're trying to load a theme that does not exist. So, its important to leave any themes that were in a Experience in draft mode (rather than deleting them) for at least 30 days after the Experience has been stopped, to ensure any returning visitors are reset back to the live theme correctly.


# Adding Targeting to an Experience

Once you’ve set up Modifications, go to the Targeting tab to optionally decide who should see the Experience once it’s active. Experiences by default show to all visitors.

## **Audience Targeting**

Intelligems offers three ways of picking an audience for an Experience.

* **Common Audience:** limit to users on certain devices, new or returning, channels, or countries. You can read about this in depth [**here**](https://docs.intelligems.io/content-testing/targeting/audience-targeting).
* **Custom Audiences:** use additional conditions such as cookie, landing page, custom javascript, and define complex logic to combine them. You can read about this in depth [here](https://docs.intelligems.io/general-features/targeting/audience-targeting#custom-audiences).
* **Link-based:** This option is used if you would prefer for the Experience to only be accessible for a link. Intelligems will create a custom link for you, which you will then need to use in the locations you wish to drive traffic from. \*\*\*\*To use this option, select "Link" and input what page you'd like visitors to land on - if not just the homepage. After saving your Experience, your unique link will be accessible here or from the Experience list. You can change this link at any time if you’d prefer to have some people land on a different page. The Intelligems link builder simply appends a special parameter to whatever URL you specify, which ensures that a visitor coming through that link is assigned that Experience going forward as long as it’s active - regardless of the presence of the link on subsequent visits.

{% hint style="info" %}
**Audiences ignored in Tests:** Intelligems allows you to test Experiences containing Offers against eachother to see which one is more effective before activating it. Note that the audience targeting rules of individual Experiences are ignored when testing in lieu of test-wide audience targeting settings. [Learn more about testing Experiences](https://docs.intelligems.io/offer-experiences/testing-offer-personalizations).
{% endhint %}

## **Currency Targeting**

You can also show Experiences only to users shopping in a certain currency if your site supports multiple currencies. This can be combined with any of the audience targeting settings.

Read more about currency targeting in the context of tests [here](https://docs.intelligems.io/general-features/targeting/currency-targeting).

## **Page Targeting**

By default, your modifications apply to all site pages. But you may for example decide that a certain popup or javascript button behavior should be limited only to one or more product pages. Use Page Targeting to limit which pages your modifications apply to.

Page targeting can be used if your Modifications are limited to Template Changes, Content Edits, CSS/JS, and Offers.

Note that the same targeting applies to all modifications in the Experience. There is currently no way to limit some Modifications to one page and others to another. Here is how page targeting acts for each modification:

* Template change, Onsite Edits, CSS/JS: the changes are only shown on selected page(s)
* Offers: popup components only display on selected page(s). There is no way to hide updated prices, progress bar components, or quantity buttons from the cart and checkout pages.

## Next Steps

Once you’ve set up your Targeting, you can go on to:

* **Preview:** Make sure everything looks and functions correctly on your site before activating the Personalization. Click [here](https://docs.intelligems.io/personalizations/previewing-personalizations) to read our Preview guide.
* **Activate the** Experienc&#x65;**:** You can pause and resume as many times as you need, which helps with recurring promotions.


# Targeting Modes for Experiences

Intelligems offers two broad modes of Audience Targeting: **Permanent** and **Temporary.**

* [**Permanent**](#permanent-audience) **-** is useful if once someone is eligible for an Experience, and as long as that personalization is active you want them to continue to receive that experience.
* [**Temporary**](#temporary-audience) - is useful if the conditions by which someone qualifies may "expire". For example, if you target New Visitors, a new visitor will see a Experience but eventually no longer qualify. Similarly, if someone who comes via a specific link qualifies, after a certain amount of time they may no longer qualify.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FHc817s5tVzafWvycojKB%2FScreenshot%202024-10-03%20at%2012.29.37%E2%80%AFPM.png?alt=media&#x26;token=481154bf-e4b5-4a13-a874-236c749dafee" alt=""><figcaption></figcaption></figure>

## **Permanent Audience**

A **Permanent Audience** is a group of users that are permanently included or excluded from an Experience. Once a user is evaluated and placed in or excluded from a permanent audience, their status remains unchanged for the duration of the experiment.

#### Characteristics:

* **Static Assignment**: Once assigned, users in a permanent audience will not be re-evaluated for inclusion or exclusion based on behavior or conditions.
* **No Expiration**: Users who are included or excluded from a permanent audience are never automatically re-evaluated after a certain time period.

### Temporary Audience

A **Temporary Audience** is a group of users who are dynamically included or excluded from an Experience based on an evaluation frequency. Users in a temporary audience are re-evaluated periodically to determine if they should remain included in the experiment or be excluded.

#### Characteristics:

* **Dynamic Assignment**: Users are periodically evaluated to see if they should remain in the audience. This re-evaluation happens after a set period (called the **evaluation frequency**).
* **Evaluation Frequency**: This is the number of days between re-evaluations. During each re-evaluation, the user can be included or excluded based on the defined conditions.


# Previewing Experiences

Once you’ve set up Modifications, you can go to the Preview tab to make sure everything looks and works well before activating it, or just to see how an active Experience appears to visitors.

## How does Preview help?

* Before you’ve ever activated an Experience, preview to make sure everything looks good
* While an Experience is active, preview to see what it looks like for its target audience

{% hint style="info" %}
At the moment you cannot preview an Experience that has been previously active but is now stopped. To work around this, you can either re-activate the Experience, or you can duplicate it and preview the duplicated version.
{% endhint %}

## How to Preview your Experience

In an Experience, go to the Preview tab.

#### **STEP 1: Save your changes**

The Intelligems preview (screenshots and full screen) will only show what’s already saved in your Experience. If you’ve made additional changes since your last save, you should save the Experience to see them in the Preview.

If you are editing an active Experience, you may not feel comfortable saving your changes just to preview, since saving would automatically apply these changes to visitors. To work around this, you should *either re-activate the Experience, or you can duplicate it and preview the duplicated version.*

#### **STEP 2: Optionally adjust which page you want to see**

To save you time, Intelligems automatically determines which site page our preview should ‘center’ on. This means which page is shown in screenshots and as the first page when you open full screen preview. The automated logic works as follows:

* By default the home page of your site is shown.
* If you have page targeting set up to a single page, that page will be used. This is useful, for instance, when personalizing a particular PDP for a given audience.
* If you have a single redirect modification, the target URL of that redirect will be used.
* If you have both of the above, the page targeting will be used.

If you prefer to override this and always see previews beginning on a particular page, whether it’s the home page or another, simply choose Custom URL in the top left picker, type in a URL, and save. Intelligems will continue showing previews of this URL until you choose another URL or reset it to automatic mode.

#### **STEP 3: View screenshots and Full Screen Preview**

* **Screenshots:** Have a look at the screenshots for a rough at-a-glance view of your site. These should never be used as a substitute for a full screen preview.
* **Full Screen Preview:** Click the “Full Screen Preview” button to view your site in the browser as visitors in the Experience would see it. Or click the “Mobile Preview” button to get a link for your mobile device.

#### **TIP: In full screen preview, make sure to “include” yourself:**

If your Experience is targeted to a Particular audience, it may be that your own circumstances (location, device, etc) make you ineligible for the Experience. To account for this, full screen preview allows you to view the site in two ways:

* **As yourself:** If you do not match the Experience audience, you will receive a message like the one below. This helps you confirm that the targeting is excluding people correctly. Click the “Include” button to force yourself into the audience of the Experience - this will allow you to see what it will look like for those visitors.

  <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FlkT7sSxOWKoi6ck4pOKD%2Fimage.png?alt=media&#x26;token=28c13b6d-3318-4b7a-8f25-0b0055baaa81" alt=""><figcaption></figcaption></figure>
* **As a member of the audience**: once you click “Include” you will see the site as it appears for the Experience's audience. This is the mode you should spend most of your time in.

Other buttons in this blue banner that you may find useful are:

* **The refresh icon:** This resets the preview so that your site appears the way it did when you first previewed it. This can be handy when using a URL Redirect modification that's set to only redirect from Page A to Page B *a single time*. Clicking refresh will allow you to test the redirect more than once.
* **Highlight Replaces:** If you have used Content Edits in your Experience, this toggle will show which elements on each page have been affected.

## Next Steps

Once you’ve Previewed your Experience, you can go on to:

* **Fine tune your modifications:** Click [here](https://docs.intelligems.io/personalizations/personalization-modifications) to read our Modifications guide.
* **Activate the Experience**: If everything looks good, activate your Experience or leave it pending until ready. You can pause and resume as many times as you need, which helps with recurring promotions.


# Scheduling Experiences

## **Scheduling Experiences Overview**

The **Scheduling Experiences** feature allows you to control *when* specific modifications will appear on your site by setting start and end times. This makes it easy to automate updates, ensuring that changes go live exactly when you want and stop at the right time. Whether it’s a promotional banner for a flash sale or a seasonal announcement, scheduling makes it easy to automate time-sensitive personalizations without having to manually turn them on and off.

## **Why Would I Need to Use Scheduling for Experiences?**

Scheduling is essential for making sure your Experiences are displayed at the right moment without requiring constant oversight. This feature allows you to time your modifications to align with key business events and user behavior patterns. For example:

* **Launching Timed Promotions:** Automatically show a discount banner during a flash sale.
* **Managing Seasonal Campaigns:** Set up a special message for a holiday campaign, so it starts and stops exactly as needed.
* **Future Planning:** Schedule Experiences to launch new content or variations at a future date, so you can "set it and forget it."

## **How to Set Up a Schedule**

You can choose to set a schedule **when creating a new Experience** or add a schedule to **an existing Experience**.

1. **Where to Find Scheduling:**

   * **Scheduling for New Experience:** After you save your Experience, go to the header and select the **down arrow** next to **Activate**. From the dropdown menu, select **Schedule**. This will open the schedule dialogue where you can define the start and end times for your Experience.

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FWURDgT79TDNq4jvsRGnv%2FFrame%201.png?alt=media&#x26;token=77a06759-66c2-4eeb-8d60-a5c1b99ad186" alt=""><figcaption></figcaption></figure>

   * **Scheduling for Existing Experiences:** In your personalizations list, click the **three-dot menu** on the right of a personalization and select **Schedule Experience**.

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FjGbj6oPONBfl2YsGyu26%2FFrame%202.png?alt=media&#x26;token=f71304f4-12d5-4148-9e24-1c1f45ca82e0" alt=""><figcaption></figcaption></figure>
2. **Set Up Timing:**

   * **Start Date & Time**: Set the exact date and time when your Experience should begin displaying (e.g., October 15th at 8:00 AM).

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FLQGIqb8RzihdhoAYTHWa%2FScreenshot%202024-10-09%20at%208.34.13%E2%80%AFPM.png?alt=media&#x26;token=865c8d03-a225-4b16-927f-2cbd32be75b9" alt=""><figcaption></figcaption></figure>

   * **End Date & Time (Optional)**: If your Experience should only run for a limited period, set an end date and time. Leaving this field blank means the Experience will run indefinitely until you manually stop it.

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FGyXUeOiiQfqvHXFAlhrZ%2FScreenshot%202024-10-09%20at%208.34.47%E2%80%AFPM.png?alt=media&#x26;token=4b9cdded-b6d6-47e4-9682-58ab7762dd8a" alt=""><figcaption></figcaption></figure>
3. **Review and Confirm:**

   * Use the **Preview** feature to check that the Experience appears as expected.

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FPoOn3f1fwADB9KMjwT4W%2FScreenshot%202024-10-09%20at%208.35.20%E2%80%AFPM.png?alt=media&#x26;token=f49a2b2e-db12-4f7e-91e3-a60f801512e3" alt=""><figcaption></figcaption></figure>

## **Example Use Cases**

* **Time-Limited Offers:** Show a banner for a single-day event (e.g., “24-Hour Flash Sale”).
* **Seasonal Promotions:** Set a start date for a holiday campaign and let it run indefinitely until you want to turn it off manually.
* **Ongoing Variations:** Use scheduling to launch new variants for long-term testing without setting an expiration date.

For more information, refer to our Experiences Guide​ ([Intelligems Docs](https://docs.intelligems.io/personalizations/personalizations-getting-started)).


# Rolling Out Tests

Quickly apply the most successful variant in an experiment to all visitors or to a limited audience by rolling it out as an Experience.

## Why Roll out tests?

When viewing the results of your Intelligems experiment, you may find that one variant performed better than others across all audiences, or only for a limited audience.

* **If one variant performed better across all audiences:** you’ll want to end the test and show the winning variant to all visitors. Replicating the changes in Shopify takes time, is error-prone, and may require developer support. With Intelligems Rollouts you can apply your changes in a few clicks - optimizing your site as quickly as possible.
* **If a variant performed better across a specific audience only**: it may be impossible to deploy this change in Shopify. With Intelligems Rollouts you can apply these changes to one or more specific audiences in a few clicks.

{% hint style="success" %}
**One test, multiple rollouts:** You may find that you want several rollouts from a single test. For instance if your group 1 performs better for audience A while group 2 performs better for audience B, you can roll out group 1 only to audience A and separately roll out group 2 to audience B.
{% endhint %}

## How do Rollouts work?

Rolling out a winning test variant **ends the test and creates an Experience** with the same site modifications as the variant. You can [learn more about Experiences here](https://docs.intelligems.io/personalizations/personalizations-getting-started) but in general, you can

* **Limit the audience:** configure the Experience to target all site visitors or a particular audience, including only visitors holding a special link.
* **Start whenever:** turn it on immediately or only once you’re ready.
* **Stop or resume any time:** for example, you may roll out a test variant just for a few days while you work on implementing your changes natively in Shopify and once you’re ready, you can turn off the resulting Experience.

**What kinds of tests can you roll out?**

A test can be rolled out if it is active, paused, or ended.

* CONTENT TESTS: can be rolled out
* OFFER TESTS: can be rolled out
* PRICE TESTS: a particular variant in a price test can be rolled out to all Visitors on your site, but it can not be rolled out to a specific audience only. Additionally, price tests can only be rolled out *once*, the moment you end them.
* SHIPPING TESTS: cannot be rolled out due to technical limitations

**Native Rollouts:** There are two situations in which Intelligems, for technical and safety reasons, rolls out changes *“natively”* - meaning directly to Shopify rather than to an Experience. This occurs when

* You choose to roll out a **theme test** to All Visitors: It’s much safer and more performant for Intelligems to change the Shopify theme directly.
* You roll out a Price test: for technical reasons Intelligems must update your Shopify prices directly.

## How to roll out a test

**Step 1: Open the Rollout Wizard**

The Rollout Wizard guides you through a few steps to roll out a test variant into a single Experience. If you are rolling out more than once from the same test, you'll need to go through the wizard multiple times. When you complete the Rollout Wizard you'll still have a chance to review and modify the resulting Experience before activating it.

There are several ways to reach the Rollout Wizard.

* FROM THE TESTS LIST: click the Stop Test button or the Roll Out button
* FROM THE ANALYTICS PAGE: The same two buttons are available at the top of a test’s Analytics page

  <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FwDywGgI7MIVzUmMb1WYi%2Fimage.png?alt=media&#x26;token=ef6cdfd4-b6cd-4881-aa7b-fbd583c1804b" alt=""><figcaption><p>Rolling out a test group from the top of the test's Analytics page</p></figcaption></figure>
* FROM THE ANALYTICS AUDIENCES TABLE:
  * In the All Visitors tab at the bottom of the Analytics Overview page, click the name of the variant you’d like to roll out
  * From one of the Audience tabs of this table, you can roll out a variant to a specific audience that it performed best for

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F2JTtM56Z5s2WVjYBZmVv%2Fimage.png?alt=media&#x26;token=f7d0ea68-5a12-4be9-b493-32871eb91b5e" alt=""><figcaption><p>Rolling out a test group to a particular audience from the Audiences Table in Analytics</p></figcaption></figure>

**Step 2: Choose the group you want to roll out**

This is usually the winner, based on your primary goal. If you’re reached the wizard from the Audiences table, a group will be pre-selected for you.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FOM6dzInppwJo0EwYI8Cm%2Fimage.png?alt=media&#x26;token=a0f2654b-9cbc-4034-9d3d-6cd9097c759b" alt=""><figcaption><p>Selecting a test group to roll out</p></figcaption></figure>

{% hint style="info" %}
**Price Tests:** If you’re rolling out a Price test, this is as far as the wizard goes. You can now click Roll Out. Intelligems will apply your prices directly to Shopify, for all visitors.

**Warning:** If your test contained any additional on-site edits such as text changes, those will ***not*** be rolled out. You can either apply those in Shopify yourself or create an Experience from scratch with those changes.
{% endhint %}

**Step 3: Choose the audience you’d like to roll this variant out to**

You can build an audience of your choosing using our robust audience targeting conditions and combination logic. You can also show the resulting Experience only to visitors with a special link, which is handy for rolling out offers.

Intelligems will automatically suggest an audience for you depending on your test settings and how you entered the Rollout Wizard. You can change or clear this if you wish.

* If your test is targeted to a specific audience, we’ll copy that audience over
* If you come in from Analytics and you had filters active, we’ll copy those filters
* If you come from an audience in the Analytics table, we’ll copy that as well.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fd3VIuh3efONlNu6ST06O%2Fimage.png?alt=media&#x26;token=4f67ad84-08e6-4f1b-b58f-a00414048d1d" alt=""><figcaption><p>Selecting an audience for your roll out</p></figcaption></figure>

If your test made use of Advanced Targeting, we will not be able to auto-suggest an audience for the Experience but you should be able to build it yourself if needed.

{% hint style="info" %}
**Other types of targeting:** The test you’re rolling out may have used additional types of targeting:

* **Currency or Page Targeting** will be copied into the resulting Experience but you should check to make sure before activating the Experience. This does not apply when rolling out price tests or rolling out theme tests to all visitors, since these kinds of changes are applied directly to Shopify.
* **Mutually exclusive behavior** will not be rolled out. If your test was in a Mutual Exclusion Group (meaning visitors cannot see it and another test at the same time), the resulting Experience will have no such limitations.
  {% endhint %}

**Step 3.5: Additional step for theme rollouts**

If you are rolling out a Theme test to all visitors, Intelligems will roll out natively - meaning it will apply the new theme directly to your Shopify store rather than creating an Experience. However, if your test also contained additional changes such as onsite edits - for example text, colors, CSS, javascript - you'll be asked whether you want to discard those changes or roll them out separately as an Experience.

{% hint style="warning" %}
If you do choose to roll them out as an Experience, you should activate the resulting Experience as soon as possible, since the Theme change will be applied to Shopify as soon as you finish the Rollout Wizard.
{% endhint %}

**Step 4: Confirm the changes and roll out**

Look over the summary of your Rollout, fixing anything if needed. If everything looks good, click Roll Out and End Test (or “Roll Out” if your test has already ended).

Your test will end if it’s not already ended and you will be taken to a draft of your resulting Experience where you can

* give it a more descriptive name
* check to make sure everything looks okay and make any changes
* click the “Activate” button whenever you’re ready to activate your Rollout Experience

{% hint style="info" %}
**Cleaning up after Offer Rollouts:** Offer tests can be created by choosing one or more already-existing Offer Experiences and testing them against each other. When you roll out a winning group in an Offer Test, Intelligems creates a new Experience from the winning group. At this point you may want to do some tidying up in your Experiences list to:

* remove the Offer Experience that gave rise to your winning group
* remove the other Offer Experiences that gave rise to your non-winning groups, if you’re not planning on using them or testing them again
  {% endhint %}


# Offer Experiences

A complete guide to using Intelligems Offers to create promotions, discounts, and special deals that boost sales and improve customer experience.

## Offers User Guide

## What are Offers?

Offers are powerful tools that help you create promotions and discounts for your online store. Think of them as digital coupons that work automatically when customers meet certain conditions.

With Offers, you can:

* Give discounts on specific products or entire orders
* Offer free shipping when customers spend enough
* Create volume discounts that reward bigger purchases
* Give free gifts to encourage more sales
* Test different promotions to see which works best

The best part? Offers work automatically. Once you set them up, customers get the deals without needing special codes or complicated steps.

### How to Access Offers

You can find the Offers feature in your Intelligems dashboard:

1. Log into your Intelligems account
2. Go to <https://app.intelligems.io/experiences/offers>
3. Click "Create New Offer" to get started

## Types of Offers

Intelligems gives you five different types of offers. Each one works best for different goals.

#### 1. Amount off Products

This offer gives customers money off specific products you choose.

**When to use it:**

* You want to promote certain items
* You have products that aren't selling well
* You want to clear out old inventory

**How it works:**

* Pick which products get the discount
* Choose how much money to take off (like $5 off or 20% off)
* Set any minimum requirements (like "buy 2 to get the deal")

**Example:** Take $10 off all winter coats when customers buy any coat.

#### 2. Amount off Order

This offer takes money off the customer's entire order total.

**When to use it:**

* You want to encourage bigger purchases
* You want to reward loyal customers
* You're running a store-wide sale

**How it works:**

* Set the discount amount (like $15 off or 10% off)
* Choose minimum purchase requirements (like "spend $100 to get $15 off")
* The discount applies to the whole order

**Example:** Get $20 off your order when you spend $150 or more.

#### 3. Volume Discounts

These offers give bigger discounts when customers buy more items. You can create up to four different discount levels.

**When to use it:**

* You want customers to buy more items
* You sell products that work well together
* You want to increase your average order size

**How it works:**

* Create different discount tiers (like 10% off for 2 items, 20% off for 4 items)
* Choose whether to base it on number of items or dollar amount
* Customers automatically get the best discount they qualify for

**Example:**

* Buy 2 items: Get 10% off
* Buy 4 items: Get 20% off
* Buy 6 items: Get 30% off

#### 4. Free Shipping

This offer removes shipping costs when customers meet your requirements.

**When to use it:**

* Shipping costs are stopping customers from buying
* You want to encourage larger orders
* You're competing with stores that offer free shipping

**How it works:**

* Set minimum requirements (like "free shipping on orders over $50")
* Choose which countries get free shipping
* Pick which shipping methods to make free

**Example:** Free shipping on all orders over $75 within the United States.

#### 5. Free Gift

This offer adds a free product to the customer's cart when they meet your requirements.

**When to use it:**

* You want to introduce customers to new products
* You have sample sizes or promotional items
* You want to make customers feel special

**How it works:**

* Choose which product to give away for free
* Set requirements for getting the gift (like "spend $100")
* Decide if the gift gets added automatically or if customers choose it

**Example:** Get a free travel-size lotion with any purchase over $60.

## Setting Up Your First Offer

Follow these simple steps to create any type of offer:

#### Step 1: Choose Your Offer Type

1. Go to the Offers page in your dashboard
2. Click "Create New Offer"
3. Pick one of the five offer types
4. Give your offer a clear name (like "Summer Sale - 20% Off Dresses")

#### Step 2: Configure Your Offer

1. **Set the discount amount** - Choose how much to discount (percentage or dollar amount)
2. **Pick eligible products** - Select which products the offer applies to (or leave blank for all products)
3. **Configure item mix settings** - By default, customers can mix and match eligible products to qualify for your discount. Enable "Require same item purchases" if customers must buy multiple units/subtotal of the *same* product to reach discount thresholds (useful for creating product-specific volume discounts)
4. **Set minimum requirements** - Decide if customers need to spend a certain amount or buy a certain number of items
5. **Choose stacking options** - Decide if this offer can combine with other offers

#### Step 3: Add Components (Optional)

You can add special features called components (via [**Global Styles**](https://docs.intelligems.io/general-features/global-styles)) to help customers understand and use your offer:

* **Quantity Buttons** - Help customers quickly add multiple items
* **Progress Bar** - Show customers how close they are to earning the discount
* **Offer Message** - Display promotional text on your website

#### Step 4: Set Up Targeting (Optional)

You can limit who sees your offer:

* **By location** - Only show to customers in certain countries
* **By device** - Only show to mobile or desktop users
* **By customer type** - Only show to new or returning customers

#### Step 5: Preview and Activate

1. Use the preview feature to see how your offer will look
2. Test the offer to make sure it works correctly
3. Click "Activate" to make it live on your website

### Understanding Offer Components

#### [Quantity Buttons](https://docs.intelligems.io/offer-experiences/quantity-buttons)

These buttons appear on product pages and help customers quickly add multiple items to their cart.

**What they do:**

* Show customers different quantity options (like 1, 2, 3, or 5 items)
* Make it easy to reach volume discount tiers
* Display the savings for each quantity

**When to use them:**

* You have volume discounts set up
* Customers often buy multiple quantities of your products
* You want to encourage larger purchases

**How to set them up:**

1. Add the quantity buttons component when creating your offer
2. Customize the button colors and styles in Global Styles
3. Add the code snippet to your product pages (your developer can help with this)

#### [Progress Bar](https://docs.intelligems.io/offer-experiences/progress-bars)

This bar shows customers how much more they need to spend or buy to earn rewards.

**What it does:**

* Displays in the shopping cart
* Shows progress toward the next discount tier
* Updates automatically as customers add items

**When to use it:**

* You have minimum purchase requirements
* You want to encourage customers to add more items
* You have multiple discount tiers

**How to set it up:**

1. Add the progress bar component when creating your offer
2. Customize the colors and messages in Global Styles
3. Add the code snippet to your cart page (your developer can help with this, following [this guide](https://docs.intelligems.io/offer-experiences/offers-integrating-widgets#offer-progress-bar))

#### [Offer Message](https://docs.intelligems.io/offer-experiences/slide-outs)

This component displays promotional messages about your offer throughout your website.

**What it does:**

* Shows offer details to customers
* Can appear as pop-ups or banners
* Helps customers understand the deal

**When to use it:**

* You want to promote your offer prominently
* You need to explain complex offer rules
* You want to create urgency or excitement

**How to set it up:**

1. Add the offer message component when creating your offer
2. Write clear, simple text about your offer
3. Choose where and how the message appears

## Best Practices for Successful Offers

#### Keep It Simple

* Use clear, easy-to-understand language
* Avoid complicated rules or requirements
* Make the benefit obvious to customers

#### Test Your Offers

* Try different discount amounts to see what works best
* Test different minimum requirements
* Compare offers against each other to find winners

#### Make Requirements Achievable

* Don't set minimum purchases too high
* Make sure customers can realistically reach discount tiers
* Consider your average order value when setting requirements

#### Promote Your Offers

* Use the offer message component to highlight deals
* Mention offers in your marketing emails
* Add offer details to your website's announcement bar

#### Monitor Performance

* Check your analytics regularly to see how offers are performing
* Look at metrics like conversion rate and average order value
* Adjust offers based on what the data tells you

#### Time Your Offers Well

* Consider seasonal trends and shopping patterns
* Avoid running too many offers at the same time
* Plan offers around holidays and special events

#### Use Clear Messaging

* Tell customers exactly what they need to do to get the deal
* Use action words like "Buy," "Get," and "Save"
* Include the discount amount in your messaging

## Common Questions

**Can I run multiple offers at the same time?** Yes, but be careful about how they interact. You can choose whether offers "stack" (combine) or work separately.

**How do customers see the offers?** Offers appear automatically when customers meet the requirements. They'll see discounts in their cart and at checkout.

**Can I change an offer after it's live?** Yes, you can edit offers anytime. Changes take effect immediately.

**Do I need technical skills to set up offers?** Basic offers require no technical skills. Enabling components like progress bars and quantity buttons for the first time may need help from a developer, as you'll need to add some short code snippets to your theme.

**How do I know if my offers are working?** Check your Intelligems analytics dashboard to see offer performance, including how many customers used each offer and the impact on sales.

## Getting Help

If you need assistance with setting up offers:

* Check the technical integration guides for detailed setup instructions
* Contact Intelligems support for help with complex configurations
* Work with your developer for custom implementations

For more technical details about integrating offer components, see [Integrating Components with Offers](https://docs.intelligems.io/offer-experiences/offers-integrating-widgets).

To learn about testing different offers against each other, see [Testing Offer Experiences](https://docs.intelligems.io/offer-experiences/testing-offer-personalizations).


# Experiences FAQs

<details>

<summary>Checklist: What to consider before activating a Experience</summary>

* **Unforeseen combinations:** Because a visitor can be subject to multiple Experiences at the same time, you should be careful when designing and targeting your Experiences to make sure that you don't create conflicts or unpredictable states for users. For example, you wouldn't want the same visitor to be redirected from page A to B but also from A to C. Likewise, you don't want a visitor experiencing a theme change as well as a template change where the new theme doesn't actually contain the new template. Try to avoid having too many broadly-targeted Experiences active at the same time and take stock of your Experiences regularly. Make sure you [follow the precautions ](https://docs.intelligems.io/personalizations/theme-personalization-precautions)when using theme changes.
* **Interactions with tests:** You should also be careful to make sure your active Experiences don't conflict with any active tests.
* **Performance of non-native changes:** While Experiences can help you enact quick site changes without the need to go into Shopify, some changes will likely perform better and more safely if they are implemented 'natively' in Shopify. For example, URL redirects, price changes, and theme changes targeting all visitors (rather than a specific audience) should ideally be done in Shopify. If you have the option, consider minimizing how many of these types of Experiences you run.

</details>

<details>

<summary>When does a visitor start seeing my Experience? And what happens if I stop it?</summary>

A site visitor starts seeing a Personalization the moment they become eligible for it, according to its targeting criteria. Even if they are not eligible on their first site visit or the first few pages they browse on your site, they still remain eligible.

The moment you stop a Personalization, visitors who saw the Personalization will cease to see it. This is critical for time-limited sales and events.

</details>

<details>

<summary>Do I need to be on a certain plan to use Experiences?</summary>

You can create and launch Experiences on any of our plans.

* The use of Content modifications (URL Redirect, Content Edit, Styles & JS, theme change, and template change) is available on all plans.

- The ability to test Offers requires the Plus or Blue plan.

When editing an active Experience you will not be able to add these types of modifications without the corresponding plan unless you first stop the Experience.

The Intelligems free trial will allow you to activate Experiences with all of the above modifications during your trial period.

[See our Pricing Page for more information](https://www.intelligems.io/pricing).

</details>

<details>

<summary>Why am I not able to Preview or why is Preview unavailable?</summary>

It may be that you are not in the target audience of the Experience, so Intelligems is effectively showing you what a visitor sees when they are outside the target audience. To "force" yourself into the Experience, click the "Include" button at the bottom right of the blue Preview widget in the Full Screen preview.

It may also be that you have paused an Experience that was once active but is now stopped. Intelligems currently does not support the preview of such Experiences. To get around this, you can duplicate the Experience and preview its duplicate, or stop the Experience temporarily.

It may also be that you have not yet saved your most recent changes in this Experience. The Preview shows only saved changes. Save your changes and then click Preview again. Read more on the [Previews](https://docs.intelligems.io/previewing-personalizations#tip-in-full-screen-preview-make-sure-to-include-yourself) page.

</details>

<details>

<summary>Can the same visitor be exposed to multiple Experiences at once?</summary>

Yes, absolutely! For example, a new visitor on a mobile device may be exposed to a "New Visitors" Experience with a "20% off" offer, and a "Mobile" Experience that moves the Call to Action button higher up on the page.

You should be careful when designing and targeting your Experiences to make sure that you don't create conflicts or unpredictable states for users. For example, you wouldn't want the same visitor to be redirected from page A to B but also from A to C. Likewise you don't want a visitor experiencing a theme change as well as a template change where the new theme doesn't actually contain the new template. You should try to avoid having too many broadly-targeted Experiences active at the same time.

You should make sure your active Experiences don't conflict with any active *tests*.

Experiences cannot be made mutually exclusive the way that tests can, but this feature is coming soon.

</details>

<details>

<summary>What happens if two Experiences seen by a visitor are in 'conflict'?</summary>

You should aim to avoid scenarios where the same visitor is exposed to two active Experiences that both use a theme change, a Template change on the same origin template, or similar. Intelligems will break the tie at random, potentially leading to unpredictable experiences.

</details>

<details>

<summary>When using a popup component in an Offer Experience, how can I prevent the pop-up from displaying on a specific page of my site?</summary>

On any page you want to remove the pop-up, add the following snippet. For example, to remove on the home page, add this snippet to `templates/index.liquid`

```
<style>
  #ig-discount-message-box {
    display: none;
  }
</style>
```

</details>

<details>

<summary>Can I make price changes to subscription products?</summary>

At this time, price changes are only supported for non-subscription products.

</details>

<details>

<summary>Can I use Experiences to serve different prices to different customer segments?</summary>

Intelligems allows you price products differently based on the customer, but you cannot raise prices over the Shopify list price for technical reasons.

</details>

<details>

<summary>What does Discount Synchronization Error mean and how do I fix it?</summary>

You may see a "Discount Synchronization Error" when you create, edit, start, or pause an offer. This means that Intelligems received an error from Shopify when updating your discounts in Shopify.

⚠️ **This may be affecting live Intelligems offers and your customers' ability to redeem them.**

The limitation is that you can only have 5 Automatic Discounts active in Shopify at any given time (see [Shopify docs](https://community.shopify.com/c/shopify-functions/app-automatic-discount-limitation/m-p/1966961/highlight/true#M349)). Intelligems does its best to combine all of the offers you create in the platform into as few discounts in Shopify.

You may have other apps or automatic discounts active that also count towards the limit. To check, navigate to Shopify Admin > Discounts and then add a filter for Status = Active and Method = Automatic.

To resolve this error, you can either:

* [Archive](https://docs.intelligems.io/offer-experiences/offers-limits#archiving-offers) existing Intelligems offers that you're no longer using within Intelligems
* Deactivate or delete non-Intelligems discounts that are currently active in Shopify

If neither of these actions resolve the error, please [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we'd be glad to help!

</details>


# Getting Started with Offer Experiences

Offers are special Experience Modifications that allow you to serve discounts and promotions to your visitors without code leakage, test them against each other, and track their success.

## What are Offers?

Offers are Intelligems tool built to serve your visitors promotions, volume based discounts, and gifts with purchases. Just like any other [modification in an Experience](https://docs.intelligems.io/personalizations/personalization-modifications), Offers can be targeted to the right channels and visitors to optimize discount spend and maximize your bottom line. They can also be configured to display useful site components such as popups, cart progress bars, and quantity buttons using our **Global Styles components**.

Offers can also be tested against each other: creating a test with multiple Offer Experiences (Experiences containing an Offer) lets you take the guess work out of your discount strategy by discovering which offer works best before activating it.

{% hint style="info" %}
When setting up an Experience containing an Offer, it can be useful to mix in a Content Edit modification as well. This allows you to fine-tune any text on the site that mentions your offer, such as in your announcement bar or on the homepage.
{% endhint %}

## Types of Offers

There are multiple types of Offer modifications.

* Amount off products
* Amount off orders
* Volume discounts
* Free shipping
* Free gift

{% hint style="info" %}
You can place at only Offer one into each Experience.
{% endhint %}

Each one can optionally be configured to display popups, progress bars, and other **Global Styles components** to help you communicate the offers to visitors.

## **Promotions**

* **Eligible Products:** Select which products are eligible for your Promotion. If no products are selected, then all products will be eligible.
* **Should Stack:** Select whether the offer should combine with other offers that are running at the same time in different Experiences. If you leave this unchecked, customers will not be able to stack multiple Experiences containing offers together.
* **Offer Type and Amount:** This can be a percentage off, dollar amount off per order, or dollar amount off per item.
* **Minimum Purchase Requirement:** The number of units or dollar amount needed to achieve the discount. "No Minimum Requirement" will be selected by default.
* **Maximum Discount Amount:** The maximum dollar amount discount that a customer can receive in the case of a percentage off offer.
* **Discount Title:** This is the discount name that'll be visible at checkout for customers who receive the discount.

{% embed url="<https://www.loom.com/share/661b30d4e53c449d87620069633dd998?sid=560dcce7-c7fd-4734-99a2-98c04bc4837f>" %}

{% embed url="<https://www.loom.com/share/96710d42ae4341f2b33512a3366293b4?sid=25e37c92-8972-43fe-81a8-94aeb3e13fbb>" %}

## Gift with Purchase

* **Select a Gift with Purchase:** Select which product will be provided as a gift with purchase. Note that you can only select one product, and one variant if there are multiple variants of that product. If you would like your customers to be able to choose a variant, please note that Intelligems does not currently provide the front end component for this.
* **Should Stack:** Select whether the offer should combine with other offers that are running at the same time in different Experiences. If you leave this unchecked, customers will not be able to stack multiple Experiences containing offers together.
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

  <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FPcY96glQ6PSbsVAlgGy6%2Fimage.png?alt=media&#x26;token=67061237-1f24-45aa-bc66-eb8a13a3da7d" alt=""><figcaption><p>Discount Label Placement</p></figcaption></figure>

{% embed url="<https://www.loom.com/share/d111b5f7b7574d4e8ca3a73c3615cedf?sid=6e1e2b3c-7803-4c9f-b825-af418d23e4e8>" %}

## Volume Discounts

To configure a Volume Discount, fill out the following fields:

* **Eligible Products:** Select which products are eligible for your Volume Discount. If no products are selected, then all products will be eligible.
* **Should Stack:** Select whether the offer should combine with other offers that are running at the same time in different Experiences. If you leave this unchecked, customers will not be able to stack multiple Experiences containing offers together.
* **Discount Tiers:** You are able to create up to four different discount tiers using the blue + sign. For each tier, you will select:
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
**Pop Up / Slide Out Messages** are only shown on the homepage and cannot be configured to be shown on any other pages at this time.&#x20;
{% endhint %}

* **Quantity Buttons:** These buttons will appear on your product pages for customers to quickly add multiple units to cart. They are automatically installed via the Intelligems script. If you have any trouble with these showing up inside an Offer Experience, email <support@intelligems.io>.&#x20;
* **Shipping Progress Bar & Offer Progress Bar:** This bar will appear in the cart view to show your customers how much more they need to purchase to achieve specific discounts or free shipping, prompting them to buy more to get the best deal without ever leaving their cart. More info [here](https://docs.intelligems.io/offer-experiences/offers-integrating-widgets).

{% hint style="danger" %}
**Headless Stores:** Components do not work out-of-the-box and customers must build their own front-end implementation.
{% endhint %}

## Testing Offers

You can test offers against each other to see which one is best. You can do this in two ways: create and Offer and then add it to a Test or Create an Offer Test. Both flows achieve the same results. You can follow either setup flow below.&#x20;

### Setting Up an Offer Test from Offer Creation Flow

{% embed url="<https://www.loom.com/share/3c872bdb406c4355a3785c1ee0f966fa?sid=0dbe6e51-3cf7-49ae-8644-1f03f059733e>" %}

### Setting up an Offer Test from Test Creation Flow

{% embed url="<https://www.loom.com/share/402158d0b8c845c39e07477e3b401e84>" %}

You can read our [full guide here](https://docs.intelligems.io/offer-experiences/testing-offer-personalizations).

## How do Offers Work?

Intelligems uses [Shopify Discount Functions ](https://shopify.dev/docs/api/functions/reference/product-discounts)to provide the offers you set up in the Intelligems app. The necessary Function will be created automatically when you create a new Offer Experience or Offer test in the Intelligems app, but will not be available to customers until you start your Offer test or activate your the Experience containing your offer.


# Integrating Components with Offers

Learn how to add the Intelligems Offer Quantity Buttons to your product pages and Offer Progress Bar and Shipping Progress Bar to your cart via Offers.

### Overview

Intelligems offers quantity buttons for product pages so customers can quickly add multiple units to cart and achieve various discount tiers.

Intelligems offers a progress bar for Shopify carts and slide-out carts that will show your customers how much more they need to purchase to achieve specific discounts, prompting them to buy more to get the best deal without ever leaving their cart. See below for an example of what this looks like!

{% hint style="danger" %}
You'll need the Intelligems JavaScript snippet installed in your theme to use Intelligems offer components. If you haven't already added it, see our integration guide[ here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme). Quantity buttons and progress bars require an additional short code snippet, which you can find below.
{% endhint %}

## Offer Message

No installation required. This component is automatically available to be added to an Offer once Intelligems is installed in your theme.&#x20;

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

No installation required. This component is automatically available to be added to an Offer once Intelligems is installed in your theme.&#x20;

You can customize the Intelligems Offer quantity buttons in the [**Global Styles**](https://docs.intelligems.io/general-features/global-styles) located in the left menu. Stylizing options include:

* Button styles
* Button primary, secondary and border colors
* Customizable for both desktop and mobile

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FCRjOATNnViLiEyiE2dl2%2FGlobal%20Styles.png?alt=media&#x26;token=77667ed3-7c61-4739-90b5-e9ccd0905e96" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Note that quantity buttons will only reflect your store's default currency, so if you are choosing to use quantity buttons for your Offer Experience or Offer Test, you should also set up targeting for your store's default currency.&#x20;
{% endhint %}

**If you want to use components with multiple currencies, follow the steps below:**&#x20;

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

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F6bAmGWelpAV22PfyAaFR%2FScreenshot%202025-11-04%20at%202.06.59%E2%80%AFPM.png?alt=media&#x26;token=2908fc71-12ea-4f13-a5e0-4e7ff24a8077" alt=""><figcaption></figcaption></figure>

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


# Quantity Buttons

Add fully customizable Quantity Buttons component to an Experience or Test

### Overview

Quantity Buttons replace standard quantity selectors within an Offer Experience with promotional buttons that highlight savings and encourage larger purchases. They showcase volume discounts and tiered pricing to drive higher average order values.&#x20;

{% hint style="warning" %}
**Important:**&#x20;

* Quantity Buttons are automatically installed via the Intelligems script
* You must select specific products for Quantity Buttons to be available as a component option when setting up an Offer
* To set up a Price Test with Quantity Buttons [follow these steps](https://docs.intelligems.io/offer-experiences/broken-reference).&#x20;
  {% endhint %}

{% hint style="info" %}
**Note**: Quantity Buttons are only available on Volume discount Offers.
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FlEi5IyZZgCQwjL2X7feE%2FQuantity%20button%20config5.png?alt=media&#x26;token=6d2c3c3f-3e6d-49f8-b83e-c17eba569588" alt=""><figcaption></figcaption></figure>

### Key Features

* **Multiple Button Styles**: Choose from Classic List, Image Cards, or Compact layouts
* **Dynamic Pricing Display**: Real-time pricing, savings calculations, and discount percentages
* **Enhanced Text Customization**: Add badges, labels, subtitles, and custom messaging
* **Free Shipping & Gift Integration**: Display badges and callouts directly on buttons

### Button Styles

**Classic List**\
Clean, vertical layout with organized quantity tiers. Best for traditional presentations with detailed pricing.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F6tSiub1gQsX05rPmysEF%2FScreenshot%202025-10-13%20at%203.22.14%E2%80%AFPM.png?alt=media&#x26;token=492a2d31-b4f2-46da-b097-9981bd75335b" alt="" width="563"><figcaption></figcaption></figure>

**Image Cards**\
Includes product images for each option. Ideal for bundles, gift sets, and visual product storytelling.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FycJcT8zdvPVSodlJdzD4%2FAccordionA.png?alt=media&#x26;token=12b8b055-b293-4d4f-a951-4f6444837264" alt=""><figcaption></figcaption></figure>

**Compact**\
Space-saving horizontal layout for quick comparison. Perfect for limited space and mobile experiences.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FELyOvO9kd2jQI3zRNuol%2FAccordionC.png?alt=media&#x26;token=34cc208b-695d-4de8-90fa-75675838c99a" alt=""><figcaption></figcaption></figure>

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

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FTnWLuiGvyy38cRdnOPrQ%2FQuantity%20button%20configvariables.png?alt=media&#x26;token=0616a823-985f-4398-889f-731bb83be943" alt=""><figcaption></figcaption></figure>

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

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F0kM3Jqsf5Msix5iAQLa8%2FOffer%20setup%20-%20expanded%20viewVD.png?alt=media&#x26;token=14d1511d-557f-49c4-9969-6b2dc42227ee" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}

### Tips

* **Compelling Tiers**: Clear value progression with meaningful savings increases
* **Visual Hierarchy**: Use badges and colors to guide toward preferred options
* **Mobile-First**: Ensure touch-friendly sizes and spacing
* **A/B Testing**: Test layouts, messaging, and promotional strategies
  {% endhint %}

### Troubleshooting

**Buttons Not Appearing**: Verify Offer is active, products selected, and requirements met

**Pricing Issues**: Check discount calculations and product pricing in offer settings

**Variable Display**: Verify variable syntax and test with different product selections

**Previous Variant & Quantity buttons displaying:** Hide these elements with a Content Edit&#x20;

Still having trouble? Email <support@intelligems.io>

Last updated: 7/29/25


# Progress Bars

Add a fully customizable Progress Bar component to an Experience or Test

### Overview

Progress bars visually show customers their progress toward rewards like discounts or free shipping in an Offer Experience or Offer Test. They motivate customers by showing "how close am I to unlocking this discount?" and help drive larger cart values.

{% hint style="warning" %}
**Important:** To add these components to your site, please follow [these installation instructions](https://docs.intelligems.io/offer-experiences/offers-integrating-widgets)
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FRJEdIAY3l8PnpjMO3OM0%2FQuantity%20button%20config.png?alt=media&#x26;token=a0caf840-921e-4152-a59c-3345330265c1" alt=""><figcaption></figcaption></figure>

### Key Features

* **Visual Progress Tracking**: Real-time updates as cart contents change
* **Multiple Tier Support**: Show progress across several reward levels
* **Dynamic Updates**: Automatic updates without page refresh
* **Enhanced Styling**: Customize colors, thickness, corner radius, and spacing

### Requirements

Progress bars require a minimum purchase requirement (dollar amount or quantity) to function. This must be manually set for Amount off products, Amount off order, and Free gift offers. Without a defined threshold, there's no target to measure progress against.

On Volume discount and Free shipping Offers, Progress bars are automatically available to use.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F3KEBYVQcFLf72KCRlRkW%2FAmount%20off%20products%20-%20Offer%20settings%20-%20expanded.png?alt=media&#x26;token=02190cbc-d25e-4f63-9acf-65e5a97be55a" alt=""><figcaption></figcaption></figure>

### Configuration

#### Basic Setup

* **Item Quantity**: Set quantity-based thresholds (e.g., "Buy 3 items for 15% off")
* **Dollar Amount**: Set spending-based thresholds (e.g., "Spend $75 for free shipping")
* **Multiple Tiers**: Configure escalating rewards at different levels

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F0sFfZixdM6EFms64M60T%2FOffer%20setup%20-%20expanded%20view.png?alt=media&#x26;token=bd9dac75-5b11-4dc8-84bb-2558364f4a69" alt=""><figcaption></figcaption></figure>

#### Styling Controls

* **Bar Appearance**: Colors, thickness and corner radius
* **Text**: Dynamic progress messaging, completion text, breakpoint labels
* **Typography**: Font size & font style

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FhyIf44cJaVbBvheM6sEX%2FQuantity%20button%20config1.png?alt=media&#x26;token=de417e21-5d93-4e18-9b93-fb8118e431d5" alt=""><figcaption></figcaption></figure>

### Dynamic Variables

#### Progress Variables

* `{Amount remaining}`: Show remaining amount needed
* `{Discount amount}`: Display discount value

**Example Usage:** "Spend {Amount remaining} more to unlock {Discount amount} off!"

### Example Use Cases

**Free Shipping Threshold**\
"Spend $15 more to get free shipping!" → "You've unlocked free shipping!"

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FYV4KOkbnWQyGtgtABdIA%2FAccordion1.png?alt=media&#x26;token=e06d9263-d76e-41d5-9904-d4115ae679b6" alt=""><figcaption></figcaption></figure>

\
**Volume Discount**\
"Buy 2 more items to unlock 15% off!" with locks on milestones

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FL5xE1wFLJ9CwlbmEtAFQ%2FAccordion3.png?alt=media&#x26;token=50381916-87c9-4de1-9824-c8d981dca36d" alt=""><figcaption></figcaption></figure>

\
**Gift with purchase**\
"Spend $20 more to get a free tote bag!" with gift icon breakpoint

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F9XrJM5vq9RIgrlmps5xc%2FAccordion4.png?alt=media&#x26;token=763060f3-9e54-4973-ba8c-0695ec6e1a52" alt=""><figcaption></figcaption></figure>

### How It Works

**Amount off products, Amount off order, and Free gift Offers:**

1. Configure discount value
2. Set minimum purchase requirement ($ amount or quantity)
3. Add which products this Offer should apply to (or leave empty to apply to all products)
4. Add Progress Bar component to your offer
5. Set progress and completion messaging
6. Configure styling to match your brand
7. Preview with different cart values

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FElrQUtHM54z8s5rm2ZV4%2FAmount%20off%20order%20-%20Offer%20settings.png?alt=media&#x26;token=d02a279f-6f1a-40ba-93fe-5d89698fde82" alt=""><figcaption></figcaption></figure>

\
**Volume discount Offers:**

1. Configure discount trigger and discount value
2. Add which products this Offer should apply to (or leave empty to apply to all products)
3. Configure Offer tiers
4. Set progress and completion messaging
5. Configure styling to match your brand
6. Preview with different cart values

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FQqueBDQTDy4SMMTHCxxc%2FOffer%20setup%20-%20expanded%20view1.png?alt=media&#x26;token=9cac3bca-979c-446b-ba9a-98e82c55cdca" alt=""><figcaption></figcaption></figure>

\
**Free shipping Offers:**

1. Choose to set minimum purchase requirement ($ amount or quantity) or not
2. Add which products this Offer should apply to (or leave empty to apply to all products)
3. Configure free shipping options
4. Add progress bar component to your Offer
5. Set progress and completion messaging
6. Configure styling to match your brand
7. Preview with different cart values

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FFFtpeQJt0koOYvRPW5Yh%2FOffer%20setup%20-%20expanded%20view2.png?alt=media&#x26;token=35542975-ea4c-46ce-b8ba-eaf1807d89ce" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}

### Tips

* **Set Achievable Goals**: Start with 1.5-2x your average order value
* **Use Brand Colors**: Integrate with your site's color scheme
* **Be Specific**: Use exact amounts ("$15 more") not vague language
* **Test Mobile**: Ensure proper display on all devices
  {% endhint %}

### Troubleshooting

**Progress Bar Not Displaying**: Verify minimum purchase requirement is set (for Amount off products/order/Free gift offers) and offer is active

**Styling Issues**: Use offer preview to see actual site styling; component preview shows general appearance only

Last updated: 7/29/25


# Offer Messages

Add a slideout message to your Offers and other Experiences

### Overview

Offer Messages are promotional call-outs that appear as overlays to highlight special offers and drive engagement. They capture customer attention at key moments in the shopping journey. They can be added to an Offer Experience or Offer Test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F3aRkHGaOfdYcVjAgrXF6%2FOffer%20message%20-%20pop%20up%20message.png?alt=media&#x26;token=b103f521-dae9-4823-ac6c-83a16dcdc6f4" alt=""><figcaption></figcaption></figure>

### Key Features

* **Visibility:** Offer messages are only visible on the homepage
* **2 Display Styles**: Choose from Pop up and Slide out presentation formats
* **Smooth Animations**: Slide out messages feature elegant entrance animations
* **Flexible Placement**: Position in top-left or top-right corners for optimal visibility
* **Advanced Text Customization**: Full control over titles and descriptions

### Message Styles

**Pop Up**\
Standard promotional overlay for high-priority announcements and urgent offers.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FmOk3NWQFXRJQICq7iFF7%2FFrame%202147226290.png?alt=media&#x26;token=b73ca9a5-2047-4826-8751-9c61ff92bf74" alt=""><figcaption></figcaption></figure>

**Slide Out**\
Smooth animated entrance for subtle promotional messaging without disrupting site flow.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F5kN2rVuO53L5lydqTWNM%2FFrame%202910.png?alt=media&#x26;token=acaa1a41-52b8-4373-8022-4a8644810cf0" alt=""><figcaption></figcaption></figure>

### Configuration

#### Content Setup

* **Title**: Primary headline that captures attention
* **Description**: Supporting text explaining offer details

**Default Template:**

```
Header: "Special offer"
Body: "Get [discount/offer details] when you [action]. Limited time."
```

#### Styling Options

* **Appearance**: Corner radius, color themes, typography
* **Placement**: Top-left or top-right positioning

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FHlfp1JeTqmiuArtfXQ0R%2FQuantity%20button%20config3.png?alt=media&#x26;token=5785f43b-ab62-438d-9a59-a33e04d7f268" alt=""><figcaption></figcaption></figure>

### Example Use Cases

**Limited-Time Promotions** Pop up with "48-hour flash sale - 30% off everything!" for maximum urgency

**Free Shipping Threshold** Slide out with "Free shipping on orders over $75!" for ongoing awareness

**Welcome Offers** Pop up for new visitors: "Welcome! Get 15% off your first order"

### How It Works

1. Configure discount value
2. Add which products this Offer should apply to (or leave empty to apply to all products)
3. Add Offer message component to your offer
4. Configure Offer message content
5. Choose style (Pop up or Slide out)
6. Set styling and placement preferences
7. Preview and test

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FgBaYKgqLgGpAT4eRz8cd%2FOffer%20message%20-%20pop%20up%20message2.png?alt=media&#x26;token=05d54fa7-13d7-4ae4-8e6a-bc74c1476ea2" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}

### Tips

* **Clear Value Props**: Immediately communicate what customers receive
* **Action Language**: Use "Save," "Get," "Unlock" in your messaging
* **Target Relevant Audiences**: Use device type, visitor type, and traffic source targeting for better relevance
* **Mobile Optimization**: Ensure messages are easily dismissible on mobile devices
  {% endhint %}

### Troubleshooting

**Message Not Appearing**: Check offer status and targeting criteria (device type, visitor type, traffic source, countries)

Last updated: 7/29/25


# Upgrade Offer components

Update your existing offers to use the latest component versions for improved performance and styling options.

## Steps to upgrade

#### 1. Locate your offer

Navigate to the offer containing the component you want to upgrade.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FTgemsk7Hq9k0dMdcv9u5%2FScreenshot%202025-08-05%20at%202.27.14%E2%80%AFPM.png?alt=media&#x26;token=ad8160c7-0f5b-4857-9f48-b0968c06364c" alt=""><figcaption></figcaption></figure>

#### 2. Access component settings

In the Mods section, click the three-dot menu next to the component you want to upgrade, then select "Edit component."

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F5D5wn96NMbQtVKdeCdBx%2FFrame%202147226308.png?alt=media&#x26;token=555f0890-51a8-4913-88cb-9e6137f052db" alt=""><figcaption></figcaption></figure>

#### 3. Open styling options

The Color & Style section is collapsed by default. Click to expand it.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FBMfsYLpQq0tzRsHqalGX%2FFrame%202147226306.png?alt=media&#x26;token=cf06e4c4-d3f9-4337-9e53-8e2957d1c249" alt=""><figcaption></figcaption></figure>

#### 4. Change component style

Click the "Change \[button] \[bar] \[message] style" link to view available component options.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FdZBHMNgoeiLVGxJa7ozd%2FFrame%202147226309.png?alt=media&#x26;token=d0a2a406-7d0d-47a0-9aaa-7b07b418ec2f" alt=""><figcaption></figcaption></figure>

#### 5. Select new component

Choose your preferred component from the available options.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FcU8FhD5bfj1cHRa7jldv%2FScreenshot%202025-08-05%20at%202.28.31%E2%80%AFPM.png?alt=media&#x26;token=36f09013-0772-460d-85ff-a03e8024820a" alt=""><figcaption></figcaption></figure>

#### 6. Configure your component

Adjust color & styling as needed for your offer.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FU9IE9kh5o0u7bxNui6yf%2FScreenshot%202025-08-05%20at%202.30.24%E2%80%AFPM.png?alt=media&#x26;token=a27c4736-bff4-46de-90b3-487718b760d8" alt=""><figcaption></figcaption></figure>

#### 7. Save changes

Click "Save" to apply your component upgrade.

{% hint style="info" %}
**Note:** If your offer uses multiple components, the system will prompt you to review each one. You can skip components that don't need updates, but you'll need to confirm changes on each screen before finalizing.
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fd3MqlWQ42sgIWWgagvMR%2FFrame%202147226307.png?alt=media&#x26;token=d78bd625-ad8c-486a-bb2d-99d8ba07dd17" alt=""><figcaption></figcaption></figure>


# Offer Experiences Library

Learn how to build 8 Offer Experiences in your store

We built Offer Experiences to be a robust tool to power any almost any offer you can imagine, right inside of Intelligems.&#x20;

## How to Think About Offers

Every great promotion/offer comes down to three simple questions: **When**, **Who**, and **What**. Together, these three pieces form the backbone of your offer strategy:

* **When** is the offer available? (Timing Strategy)
  * Evergreen / always-on like free shipping threshold, bundles, quantity discounts etc.
  * Event-based like welcome offer, winback, post-purchase upsell
  * Calendar-based like holiday sales, early access, seasonal clearance, product release
* **Who** gets to see or redeem it? (Audience)
  * Public / all visitors
  * Earned audience like VIP, email or SMS subscribers, loyalty members
  * Partner / affiliate
* **What** is the actual benefit? (Mechanism)
  * Monetary discounts like $ or % off
  * Volume incentives like BXGY, quantity discounts, tiered offers
  * Value additions like GWP, free shipping, extended returns, lifetime warranty

When you combine these, you’ve got the full picture of your offer. And the final piece to keep in mind is the **Why** — the goal you’re trying to achieve, whether that’s boosting conversion, increasing order value, rewarding loyalty, or driving urgency.

Put simply: *a strong offer connects the right incentive, to the right people, at the right time — all in service of your bigger growth goals.*&#x20;

## 8 Offers To Build Right Now with Intelligems

1. [Holiday Sale](https://docs.intelligems.io/offer-experiences/offers-library/how-to-set-up-a-holiday-sale)
2. [Early Access Sale](https://docs.intelligems.io/offer-experiences/offers-library/how-to-set-up-an-early-access-sale)
3. [Buy More, Save More Volume ($) Discount](https://docs.intelligems.io/offer-experiences/offers-library/how-to-set-up-a-buy-more-save-more-volume-discount)
4. [Buy More, Save More Quantity (units) Discount](https://docs.intelligems.io/offer-experiences/offers-library/how-to-set-up-a-buy-more-save-more-quantity-discount)
5. [Partner Exclusive Discount (Influencer, Ambassador, Affiliate)](https://docs.intelligems.io/offer-experiences/offers-library/how-to-set-up-a-partner-offer-influencer-ambassador-affiliate-etc.)
6. [Free Gift with Purchase Threshold](https://docs.intelligems.io/offer-experiences/offers-library/how-to-set-up-a-free-gift-with-purchase-threshold-offer)&#x20;
7. [Seasonal Clearance Extra % Off Discount](https://docs.intelligems.io/offer-experiences/offers-library/how-to-set-up-seasonal-clearance-discount)
8. [Free Shipping Threshold](https://docs.intelligems.io/offer-experiences/offers-library/how-to-set-up-a-free-shipping-threshold-offer)


# How to Set Up a Holiday Sale

Steps to launch a Holiday Sale using an Offer Experience

## Holiday Sale

You can use Offers to power your holiday sales. Whether you're running the offer to 100% of traffic, or a segment in Klaviyo, Intelligems makes it easy to create, schedule, and automate your offer. Our customers user Offers to power their holiday sales like Valentine's Day, Mother's Day, 4th of July, Black Friday, etc.

{% hint style="info" %}
Offer Experiences are available on Core, Plus, and Blue Plans. Testing your Offers against each other is only available on Plus and Blue.&#x20;
{% endhint %}

**Goal:** Increase revenue, move through inventory, make money!

**Who:** All visitors

**What:** 30% off your order

**When:** Fall Sale Event (example)

**Offer Type:** Percentage off your order; most common use case

**Amount:** 30%

* This amount might be set based on the goal of the sale, competitive landscape, or MAP policy with retailers

**Offer Experience:**&#x20;

* Timing: Time-limited, typically 3-5 days
* Where:&#x20;
  * Website
    * Homepage
    * PDP banners
    * Cart
    * Checkout
  * Email & SMS
  * Paid ads
  * Influencer posts
  * Other marketing channels
* Activation: Automatic, no code, with a scheduled start time and scheduled end time

**Why it works:** Customers expect deals during holidays, especially when competitors are running sales, and it's a natural urgency moment since it's time-bound.&#x20;

### How to Set Up This Offer in Intelligems

{% embed url="<https://www.loom.com/share/0b78f3282d864f6281da6ae9766c36bc?sid=805939c9-cf3d-46a2-a425-e1501d8df3b9>" %}

1. Go to Experiences > **Offers**
2. Select **Amount off Order**
3. Add an Offer name (internal name)
4. Add a Discount name that matches the sale. This will be shown to shoppers in their cart and at checkout.&#x20;
   1. e.g. Fall 30% off Sale
5. Select discount value
   1. Choose **percentage off order** to offer a discount amount on their order
   2. Choose **dollar off per order** to offer a flat dollar amount discount on their order
6. Choose if you want minimum purchase requirements
   1. Select quantity of items if you want a customer to purchase a minimum X units to qualify for the discount
   2. Select subtotal of items if you want a customer to purchase a minimum $ amount to qualify for the discount
7. Leave the box unchecked if there are no minimum requirements for the discount to be applied
8. Select which products you want this discount to be applied to. It will apply to all products by default if no products are selected.&#x20;
   1. You can select products based on Product Type, Vendor, Status, Collections, and also search for individual products

{% hint style="info" %}
We recommend setting up a Sale collection in Shopify and then select that collection\\

{% endhint %}

9. Choose if you want this discount to combine with other Shopify discounts
   1. Examples: a Welcome Offer, loyalty, affiliate, influencer, or any other discount you have live in your Shopify backend that is set up to be combined with other discounts
10. Add components like **Progress Bar** or **Offer message** to support the discount messaging
11. Configure your components
    1. Make sure you've previously installed these components in your theme via Global Styles tab
12. Click **Complete offer setup**
13. At this point, you can make additional modifications by clicking **+ Add modification**
    1. You can update the content, launch a different Theme or Template, and update styles or javascript
14. Add **Targeting** to choose which shoppers you want to see this 30% off discount Offer. It will be set to all visitors by default.&#x20;
    1. If you're running a specific offer to a smaller group of your shoppers, you can select your audience in the Targeting tab
15. **Save** your Offer
16. **Preview** your Offer on desktop and mobile
17. When everything looks good, **Schedule Your Experience** or **Activate** to go live
    1. You can select a Start time and Stop time when Scheduling
18. Double-check everything else on your list to make sure you're supporting this sale like email, sms, and other marketing channels.&#x20;


# How to Set Up an Early Access Sale

Steps to launch an Early Access sale using an Offer Experience

## Early Access Sale

You can use Offers to power your Early Access Sales. If you'd like to create a rich experience for VIP customers that you offer Early Access to, use build an Offer that updates the content, powers the discount automatically, and makes the customer feel special.&#x20;

{% hint style="info" %}
Offer Experiences are available on Core, Plus, and Blue Plans. Testing your Offers against each other is only available on Plus and Blue.
{% endhint %}

**Goal:** Create VIP early access moment; replicate the public sale experience

**Who:** VIP customers

**What:** 25% off your order

**When:** 2-5 days before the public sale launches

**Offer Type:** Percentage off your order; most common use case

**Amount:** 25%

* This amount might be set based on the goal of the sale, competitive landscape, or MAP policy with retailers

**Offer Experience:**&#x20;

* Timing: Time-limited, typically 2-5 days
* Where:&#x20;
  * Website
    * Homepage
    * PDP banners
    * Cart
    * Checkout
  * Email & SMS to VIP customers
  * VIP Facebook or WhatsApp group
* Activation: Automatic, no code, with a scheduled start time and scheduled end time

**Why it works:** Customers love feeling like VIPs and getting early access to sales, plus it's a natural urgency moment since it's time-bound.&#x20;

### How to Set Up This Offer in Intelligems

{% embed url="<https://www.loom.com/share/d57f558e19a743d396d0c692bc485f35?sid=40bbddb4-f8a2-4144-8bec-57aa65fa306c>" %}

1. Go to Experiences > **Offers**
2. Select **Amount off Order**
3. Add an Offer name (internal name) like Early Access 25% off
4. Add a Discount name that matches the sale. This will be shown to shoppers in their cart and at checkout.&#x20;
   1. e.g. Exclusive Early Access 25% off
5. Select discount value
   1. Choose **percentage off order** to offer a discount amount on their order
   2. Choose **dollar off per order** to offer a flat dollar amount discount on their order
6. Choose if you want minimum purchase requirements
   1. Select quantity of items if you want a customer to purchase a minimum X units to qualify for the discount
   2. Select subtotal of items if you want a customer to purchase a minimum $ amount to qualify for the discount
7. Leave the box unchecked if there are no minimum requirements for the discount to be applied
8. Select which products you want this discount to be applied to. It will apply to all products by default if no products are selected.&#x20;
   1. You can select products based on Product Type, Vendor, Status, Collections, and also search for individual products

{% hint style="info" %}
We recommend setting up a Sale collection in Shopify and then select that collection\\

{% endhint %}

9. Choose if you want this discount to combine with other Shopify discounts
   1. Examples: a Welcome Offer, loyalty, affiliate, influencer, or any other discount you have live in your Shopify backend that is set up to be combined with other discounts
10. Add components like **Progress Bar** or **Offer message** to support the discount messaging
11. Configure your components
    1. Make sure you've previously installed these components in your theme via Global Styles tab
12. Click **Complete offer setup**
13. At this point, you can make additional modifications by clicking **+ Add modification**
    1. You can update the content, launch a different Theme or Template, and update styles or javascript
    2. We recommend launching your public Sale theme to this audience with some additional content edits using the words Early Access across the site to make it feel special
14. Add **Targeting** to choose which shoppers you want to see this 25% off discount Offer. In this case, select **Link** and choose homepage or drive to the sale collection page
15. Copy that link
16. **Save** your Offer
17. **Preview** your Offer on desktop and mobile
18. When everything looks good, **Schedule Your Experience** or **Activate** to go live
    1. You can select a Start time and Stop time when scheduling
19. Share the link with your VIP Early Access customers via SMS, email etc.&#x20;

{% hint style="info" %}
Shoppers will only be able to access that Offer via that link. All other visitors will see your current site with no Offer.&#x20;
{% endhint %}

20. Double-check everything else on your list to make sure you're supporting this Early Access sale as intended.&#x20;


# How to Set Up a Buy More, Save More Volume Discount

Steps to launch a Buy More, Save More Volume Discount using an Offer Experience

## Buy More, Save More Volume Discount

You can use Offers to power your spend more, save more tiered volume discount. Use tiered thresholds to nudge bigger baskets (e.g. spend $100, get 10% off, spend $200, get 20% off). Intelligems makes creating and powering these offers, including a progress bar, super simple.&#x20;

{% hint style="info" %}
Offer Experiences are available on Core, Plus, and Blue Plans. Testing your Offers against each other is only available on Plus and Blue.
{% endhint %}

**Goal:** Increase AOV

**Who:** All shoppers

**What:** Tiered %/$ off thresholds

**When:** Evergreen or during sale period

**Offer Type:** Volume Discount

**Amount:** Spend $100, get 10% off; Spend $200, get 20% off; Spend $300, get 30% off

* This amount might be set based on the goal of the sale, competitive landscape, or MAP policy with retailers

**Offer Experience:**&#x20;

* Timing: Always on
* Where:&#x20;
  * Website
    * Homepage
    * PDP messaging
    * Cart Progress Bar
* Activation: Automatic based on subtotal threshold

**Why it works:** Gamifies shoppers to spend more to get to the next tier with even bigger savings, increasing AOV

### How to Set Up This Offer in Intelligems

{% embed url="<https://www.loom.com/share/f4882cc1e3984048a93597c9afe09352?sid=89efbb40-9d7d-44aa-8ee6-258b3bd73fab>" %}

1. Go to Experiences > **Offers**
2. Select **Volume Discount**
3. Add an Offer name (internal name) like Spend $100, Get 10% Scaling
4. Create three offer tiers
5. Add a discount name to match each offer tier. This will be shown to shoppers in their cart and at checkout.&#x20;
   1. e.g. Spend $100, Save 10%; Spend $200, Save 20%
6. Select discount value
   1. Choose **Percentage off** and **Subtotal of items** to offer a discount amount on their order
   2. You can also select Dollar off per order or Dollar off per item as options. More on that setup here.&#x20;
7. Select which products you want this discount to be applied to. It will apply to all products by default if no products are selected.&#x20;
   1. You can select products based on Product Type, Vendor, Status, Collections, and also search for individual products

{% hint style="info" %}
We recommend setting up a Sale collection in Shopify and then select that collection\\

{% endhint %}

9. Set up each of your tiers
   1. Spend $100, get 10% off
   2. Spend $200, get 20% off
   3. Spend $300, get 30% off
      1. You have the ability to also make a tier **Free shipping** or **Free gift** in combination with a % off discount
10. Choose if you want this discount to combine with other Shopify discounts
11. Add components like **Progress Bar** or **Offer message** to support the discount messaging
12. Configure your components
    1. Make sure you've previously installed these components in your theme via Global Styles tab
13. Click **Complete offer setup**
14. At this point, you can make additional modifications by clicking **+ Add modification**
    1. You can update the content, launch a different Theme or Template, and update styles or javascript
15. Add **Targeting** to choose which shoppers you want to see this Buy More, Save More Offer
16. **Save** your Offer
17. **Preview** your Offer on desktop and mobile
18. When everything looks good, **Schedule Your Offer Experience** or **Activate** to go live
    1. You can select a Start time and Stop time when scheduling
19. Boost your AOV!




---

[Next Page](/llms-full.txt/1)

