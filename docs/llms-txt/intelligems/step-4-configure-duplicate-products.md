# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-duplicate-products/step-4-configure-duplicate-products.md

# Step 4: Configure duplicate products

When you create and save a new price test in the Intelligems app, we will create a duplicate of each product that is in the test in your Shopify account. We will use these duplicate products to run your test. In most instances, we recommend using the original PDPs and only introducing the duplicate products upon add-to-cart.

To make sure that products are not displaying multiple times in places like third-party channels and collections, inventory is being properly tracked, shipping profiles are set up correctly, and discount codes still work, you'll need to follow the below steps to make a few changes to how the duplicate products are set up in Shopify.

{% hint style="info" %}
You'll need to follow these steps for *every* price test you set up.
{% endhint %}

<details>

<summary>Step 1: Finding duplicate products in Shopify</summary>

The tag `price_test` will be added to all duplicates created by Intelligems, as well as a few additional tags specific to each test and test group.

However, the easiest place to access and check the status of your duplicate products is from directly within the Intelligems app! Next to any price test in the app, click the three dots on the far right to see more options, then select "View Duplicates". This will bring you to the duplicates status page.

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-d346bf7e1f492ed7a7ce1c744be6465e8cbc000b%2F13%20-%20View%20Duplicates.gif?alt=media)

From here, you can:

* See the status of duplicate products - you'll be warned about any issues in the top left, as well as in the `Shopify Status` and `Sync Status` columns!
* View duplicate products in Shopify - you can view all duplicates for this test by clicking the `View Duplicates in Shopify` button at the top, or individual duplicates by clicking on the icon in the `View in Shopify` column!

Navigating to your duplicate products through the Intelligems app will automatically filter your Shopify products by a tag that we have added for the experiment ID, meaning you will only see duplicate products for that specific test. There should be one product for each non-control group. So, if your test has three groups total, you should see two duplicate products.

\
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

<summary>Step 3: Configure inventory tracking</summary>

The following steps will allow you to keep an accurate count of duplicate products sold during the test and reconcile inventory after the test. However, stores manage inventory differently - some through Shopify, some through an app, and some have another method. Please consider how selling duplicate products will impact your inventory tracking before following these steps and launching a test.

If you have inventory that turns over or sells out quickly, it may make sense to use this [Duplicate SKU Sync App](https://apps.shopify.com/duplicate-sku-sync) so that the inventory syncs between your products.

If your store uses a third-party application to manage inventory, please skip these steps. Please also note that third party apps that track inventory by SKU should not be affected by duplicating products as SKUs are copied to the duplicates. However, any app that uses product IDs or variant IDs to track inventory may need to be configured with the duplicate products. [Please reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have questions or concerns!

**1.** Set the inventory quantities for all duplicate products to zero, either through Shopify’s bulk editor or by clicking into the Shopify product page for each duplicate product.

**2.** Turn on `Continue selling when out of stock` for all variants.

If you use Shopify to track inventory, you'll need to reset this option to 'Stop selling when out of stock' once an item in your store goes out of stock.

</details>

<details>

<summary>Step 4: Add duplicate products to custom shipping profiles, if necessary</summary>

*This step is only necessary if you have custom shipping profiles configured through Shopify. If only the General Shipping profile is used, you can skip this step.*

If any of the products you are testing are in a custom shipping profile, you'll need to add the duplicate products to the same profile following these steps:

**1.** From the Shopify admin console, navigate to `Settings` → `Shipping and Delivery`.

**2.** Click `Manage rates` for the relevant custom shipping profiles.

**3.** Within the shipping profile, click `Manage Products`.

**4.** Add the relevant duplicate products and variants to each custom shipping profile. You can search for `price_test` to show only the duplicate products. Click `Done` when you have selected all of the relevant products.

**5.** Back on the shipping profile page, click "Save".

</details>

<details>

<summary>Step 5: Add duplicate products to discount codes</summary>

*This step is only necessary if you have discount codes configured for specific products or collections. If you do not have discount codes or all your discount codes are configured to apply store-wide, then you can skip these steps.*

**1.** Navigate to the `Discounts` tab on the left hand side of the Shopify admin page.

**2.** Filter for the discount code(s) you would like to add the duplicate products to. To quickly filter to discounts that may need to be edited, add a filter for `Active` status, and `Amount off products` and `Buy X Get Y` for type.

**3.** Select any codes that apply to `Specific products` where the products they apply to are part of the test. Use the search bar or browse feature to add all duplicate products that the discount should apply to. Keep in mind there should be one version of each product for each group in the test.

If you have any discount codes that apply to `Specific collections`, you'll need to create a collection with the duplicate product(s) first, then add that collection to the discount.

</details>

<details>

<summary>Step 6: Configuring search apps, if necessary</summary>

If you use a search app, such as Searchanise, you may need to hide duplicate products in the search app. You can do this by adding `price_test` to "Hide products with these tags" in your search app settings.

</details>

<details>

<summary>Step 7: Configure duplicate products in third-party apps</summary>

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
