# Source: https://docs.intelligems.io/price-testing/price-testing-faqs.md

# Price Testing FAQs

## General

<details>

<summary>How many products can I add to a price test?</summary>

We limit price tests to 500 products by default, but you can [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to ask for a limit increase.

</details>

<details>

<summary>Can I price test just one variant of a product?</summary>

Products get added to a price test at the product level, which means all variants are technically included in a test, but if you are only looking to test one (or a few) variants of the product, you can set the price to be the same as the control price in all test groups for the variants that you do not want to test.

Here's an example of what that would look like if we only wanted to test the "Cream / Small" variant of our Ceramic Dinner Plate product:

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f3fa40454ab626c7c4a4af1e4678fd0ed0e98883%2FScreenshot%202024-07-08%20at%203.35.14%20PM.png?alt=media" alt="" data-size="original">

</details>

<details>

<summary>Can I Price Test Shopify Bundle products?</summary>

Shopify Bundle products cannot be price tested due to a limitation with Cart Transform Functions. Both bundle products and our price testing feature rely on Shopify's Cart Transform functionality, but **Shopify only allows one cart transform function to run per line item**.

**What are cart transform functions?**

Cart transform functions are Shopify's mechanism for modifying cart contents, pricing, and line items dynamically. They're essential for creating product bundles and implementing dynamic pricing features.

**Why does this create a conflict?**

* **Bundle products** use Cart Transform Functions to group items together and apply bundle pricing
* **Our price testing** uses cart transform functions to display different prices to different customer segments
* Since only one transform can run per line item, these two features cannot operate simultaneously

**Are there any workarounds?**

Currently, there are no reliable workarounds due to this Shopify platform limitation. You'll need to choose between:

* Using bundle products with standard pricing
* Price testing individual (non-bundle) products

**Will this limitation be resolved?**

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

<details>

<summary>Why does Intelligems update my Shopify prices when I start a test?</summary>

Intelligems automatically updates your Shopify prices to the highest price in your test. This ensures accurate pricing across your store and connected channels.

**Technical requirements**

**Shopify Checkout Scripts** can only decrease prices dynamically. Setting the highest price in Shopify allows the script to apply lower test prices at checkout.

**Shopify Functions** can increase prices, but we still set the highest price in Shopify as best practice, which we explain more below. If you would prefer not to increase your prices in Shopify and you are using our Functions integration, please [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) as we can enable this advanced setting in your account.

**Multi-channel accuracy**

Your Shopify product data feeds into other channels like Google Shopping, Facebook, Instagram, and Shopify Markets. When these channels display your products, they sync with your Shopify prices.

Setting the highest test price in Shopify prevents customers from seeing a lower price in Google Shopping (or other channels) and then encountering a higher price on your site. This creates a better customer experience and prevents potential conversion issues.

**What this means for you**

When you start a price test, any channel connected to Shopify will display the highest price from your test. This includes:

* Google Shopping feeds
* Facebook and Instagram shops
* Shopify Markets
* Third-party marketplaces
* Email marketing platforms syncing product data

If you're running tests across multiple channels, factor this into your test strategy to ensure consistent pricing where needed.

Please note that if you are only testing lower prices, your Shopify prices will not be altered when you start a price test.

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

If you need to use duplicate products for one of the above or another reason, please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for assistance enabling this feature in your account. Once enabled, one duplicate product will be created automatically for every product and every price point that you add to a price test.

</details>

<details>

<summary>What will duplicate products look like in Shopify and how can I find them?</summary>

The duplicate products will be nearly identical to the original products with a few key differences:

1. They will have different product and variant IDs. Note that duplicates will have the same SKUs as their originals.
2. They will be tagged with a ‘price\_test’ tag, as well as a tag with the experiment ID, test group ID and a unique ID to that product.
3. They will be set to Unlisted status when created.

</details>

<details>

<summary>Can I delete duplicate products once a price test is over?</summary>

We typically recommend waiting a few days after a test is over before doing this. Customers will not be able to see them unless the duplicate products are still in their cart. Keeping the duplicates live for a few days will allow these edge-case customers to be able to check out, creating a better customer experience.

When ending a test, you'll be asked if you would like to archive the products now or within 48 hours. Intelligems will automatically archive duplicates after 48 hours.

Additionally, if you have subscriptions, you should make sure any subscriptions that occurred on the duplicate products get mapped to non-duplicate products.

Other than that, there are no issues with deleting them, but archiving may be a safer option in case you need to make any changes later. You'll be able to find all duplicate products created by Intelligems by searching for the products with the tag 'price\_test' in Shopify.

</details>
