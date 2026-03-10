# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/woo-commerce/currency-conversion.mdx

***

## stoplight-id: 52hpyaffr2djw

# Currency Conversion

Version 3.5.0 and later versions of the Cash App Afterpay plugin for WooCommerce support currency conversion. This is a great feature for merchants who operate in multiple countries with multiple currencies.

## Prerequisites

Before you implement currency conversion, check that:

* You are a merchant enabled for Cross-Border-Trade (CBT) to other countries

* You have a third-party currency conversion plugin. This plugin sends the customer’s selected currency to payment gateways

## Implementation

To implement the currency convertor, do the following:

1. Open **WordPress admin** and navigate to **WooCommerce**.

2. Click **Settings**, and then click the **Payments** tab. The Cash App Afterpay Gateway information appears.

   ![woo-currency-convert-1.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-currency-convert-1.png)

3. Scroll down the page and ensure that these fields contain the correct information:

   * **Enable/Disable**: **Enable Cash App Afterpay** is checked.

   * **Title**: This is what appears as the payment method title on your checkout page. **Cash App Afterpay** is a good default title.

   * **API Environment**: Select **Sandbox** for testing or **Production** for actual use with real customers and real money.

   * **Merchant ID**: Cash App Afterpay gives you the merchant IDs for both Sandbox testing and production use.

   * **Secret Key**: Cash App Afterpay gives you the secret keys for both Sandbox testing and production use.

   * **Minimum Payment Amount**: This is set in your Cash App Afterpay merchant account.

   * **Maximum Payment Amount**: This is set in your Cash App Afterpay merchant account.

   * **Settlement Currency**: This is set in your Cash App Afterpay merchant account.

   * **Merchant Country**: This must be the country where your Cash App Afterpay merchant account is located.

   * **Excluded Categories**: Enter any excluded categories of product or service here and separate each category with a comma. For example, pornography, gambling, firearms, and so on.

   The next section is entitled **Cross Border Trade Configuration**. This section controls the currency conversion.

   ![woo-currency-conversion-2.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-currency-conversion-2.png)

4. Scroll down the page and ensure that these fields contain the correct information:

   * **Enable Multicurrency**: With this enabled, overseas customers are now able to use Cash App Afterpay with their local currency selected and pay the exact amount that they see in checkout

   * With **Enable Multicurrency** disabled, Cash App Afterpay is not available when a foreign currency is selected. However, overseas customers may still be able to log into their local Afterpay/Clearpay customer account to complete the order, and pay in their local currency. This method uses Cash App Afterpay exchange rates (mostly likely different from the rates used on the merchant site). This has always been the default behaviour for cross border trade (CBT) before this multicurrency feature was introduced

   * **CBT Countries**: Cash App Afterpay populates this field, which is a list of countries that have been enabled for CBT. After payment, the currency is converted to your currency for settlement

   * **CBT Limits**: This field shows the exchange rates used. These rates are automatically checked every 15 minutes and updated thens

5. The other fields on this page are not relevant to currency conversion. Scroll down to the bottom of the page and click **Save Changes**.

## The Store Page

Assuming you, the merchant, have applied the correct settings, your store page should behave like this:

* When the customer pays in your local currency, the prices are displayed in your local currency

* When the customer selects their local currency, the prices change to their local currency

See the screenshots below for an example:

![woo-currency-conversion-3.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-currency-conversion-3.png)

In the screenshot above, the store is based in the USA and the customer wants to pay with US dollars. The prices for the items are in US dollars.

![woo-currency-conversion-4.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-currency-conversion-4.png)

In the screenshot above, the customer wants to pay in Australian dollars. The customer clicks the **AUD** button on the right side of the page. The prices automatically change from US dollars to Australian dollars.
