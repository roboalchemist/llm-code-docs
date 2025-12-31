# Source: https://docs.intelligems.io/general-features/targeting/currency-targeting.md

# Currency Targeting

## What is Intelligems Currency & Country Targeting?

Intelligems currency and country targeting allows you to limit your test to a single currency and/or a list of specific countries.

{% hint style="warning" %}
Your store must have Shopify Markets enabled or use localization. Intelligems currently supports Cookies: Shopify Markets (`cart_currency`), localization (`localization`), Global-E (`GlobalE_Data`), and Coin Currency App (`coin-currency`). If you do not use one of these cookies, please reach out to Intelligems Support.
{% endhint %}

## How does Intelligems Currency & Country Targeting work?

* A user can go from **excluded to included** if they meet the inclusion criteria within their **first 3 page views** of your store. After their initial page views, if a user is excluded they will remain excluded for the duration of that browsing period. An excluded user's page views and orders will not be included in the test results.
* A user can go from **included to excluded** if they no longer meet the inclusion criteria at **any time** during their browsing period.
* By default, all users will be **included** in the test unless otherwise specified.

## What types of tests can I use Intelligems Currency & Country Targeting for?

Currency & Country Targeting is available for all test types!

* For Price Tests, you'll see that the ability to change the Currency & Country Targeting is unavailable - Price Tests will only run in your store's default currency. If you are looking to run Price Tests in non-store-default currencies, please see our [Multi-Currency Testing doc](https://docs.intelligems.io/price-testing/multi-currency-testing).
* If you would like to set up Country Targeting for your Price Test, please [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we can help you set this up on the backend.

## Example of Intelligems Currency & Country Targeting

**Currency targeted to USD**: In this example, customers shopping in USD and located in the selected countries will be **included** in the test. Users who do not meet the currency and country requirements will be **excluded** from the test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-25314eee2ddc1b32bf39782620ec7bec69827b38%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

## What experience will non-store-default visitors have in a Price Test?

Non-store-default visitors will not be included in test analytics.

Non-store-default visitors will be exposed to the following prices:

**For Price Tests using Checkout Scripts or Functions:**

* *If your non-store currency prices are auto-converted* -> non-store-default visitors will see converted prices of the highest price in the test
* *If your non-store currency prices are manually set* -> non-store-default visitors will see your manually set price

**For Price Tests using duplicate products:**

* Non-store-default visitors will see the control price
