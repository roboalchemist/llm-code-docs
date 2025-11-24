# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/payments-for-shopify/troubleshoot-your-installation.md

# Troubleshoot Klarna Payments

## In this section you can read about some common Klarna payments with Shopify integration errors and learn how to fix them in your store. You will also read about some limitations that can affect your Klarna with Shopify integration.

## Klarna payments app issues

## Check that the new Klarna payments app is installed in your store

By Shopify’s design, new payments apps aren't displayed under a store's **Apps** menu. To verify you have the app installed in your store:

- Go to **Shopify admin**\> **Settings**\> **Payments**. 
- Look for the *Klarna* payment method.

◦ If the payment method is active in your store, it will be included in the displayed list of active payment methods for your store and you can view the details of the payment method by clicking the **Manage** link. ◦ If the button says **Uninstall Klarna**, the app is currently installed in your store. Note that payments apps can only be uninstalled from a store when the payment method is deactivated. ◦ If the payment method isn’t active in your store, you have to search for it, by payment methods or by provider, click **Activate** which will take you to the payment methods details. Once you’re there, if the app is already installed in your store, you'll have the option to click another green **Activate Klarna** button within the payment method to activate the payment method in your store's checkout.

- If you’re shown an **About Klarna** page with a green **Connect** button, the app isn’t currently installed in your store.

### Klarna app isn’t the same as Klarna as payment method

The **Klarna** payment method, also known as gateway, isn’t the same as the **Klarna** app. New payment app integrations require an app. The payment method and the app work together for a successful integration. Uninstalling or installing the app does impact the integration, so please be careful to only uninstall the Klarna app when necessary. On the other hand, deactivating or activating the Klarna payment method impacts the storefront's checkout, that is, if the Klarna payment method displays or not, but the visibility of the payment method in checkout has no effect on the integration working successfully and doesn’t update Klarna's database.

## Klarna payment method issues

### Make sure the Klarna payment method displays in your store's checkout

If the Klarna payment method doesn’t display in your checkout, make sure the Klarna payment method is active in your **Shopify store admin**\> **Settings**\> **Payments**. If the payment method is active, but doesn't display, try the following:

- Check for [custom script code](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/shopify-plus-custom-scripts) in the Script Editor app. Note that Script Editor is only supported for Shopify for live stores that use Shopify Plus. 
- Check for any custom CSS code that might change the display of your store's checkout. 

If there is no custom code, contact Shopify for support.

### “Your payment can’t be processed for technical reasons” error in checkout

Upon redirection from Shopify to Klarna’s hosted payment page, the payment method error "Your payment can’t be processed for technical reasons. Try again or use a different payment method." may appear to the customer. The most common reason for this error is that the Integration guides steps within the [Klarna Merchant portal](https://portal.klarna.com/) haven’t been completed fully. Activating the payment method and the subsequent activation of the required unlisted Klarna unlisted payments app in your Shopify store admin are only 2 of the 3 required steps for the Klarna payment method to work successfully in checkout. You’ll also need to have active Klarna API credentials. You can sign up for a new account to receive the API credentials at [<http: business="" klarna.com="">](http://klarna.com/business). Once you have the Klarna API credentials, within Klarna's Merchant portal, complete the Shopify [Integration guides steps](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/how-to-install-klarna-payments-on-shopify). This error could also be caused by other issues, such as a Klarna merchant account configured for a different currency than the store's base currency. For support, please contact [Merchant support](http://klarna.com/merchant-support).


![ If a payment processing error occurs, an error message will be shown to the customer in the Shopify store. ](d8a6a55e-4a19-497e-aced-7205b0536c32_Screenshot+2023-07-24+182636.jpeg)
*If a payment processing error occurs, an error message will be shown to the customer in the Shopify store.*

### "Klarna is connected but you can’t use it to accept payments" message within the payment method

The “Klarna is connected but you can’t use it to accept payments” warning message in your payment method in your Shopify store indicates that you haven’t finished setting up your account or it is still being approved, and the payments app's ready flag is set to *false* in your store. To resolve this, click the **Manage** link within the payment method and complete the steps in the Integration guides in the Klarna Merchant Portal, particularly step 4 (Test), which sets the ready flag to *true* for the payment method's app in your Shopify store.

### The Klarna page loads after redirect, but no payment methods are available or order is rejected

If the Klarna page loads, but no payment methods are available or order is rejected, that means your Shopify integration was successful, but no payment methods are available for the entered customer data for your Klarna merchant account. To fix the issue:

- Make sure to enter valid customer data, not test data.
- Make sure your store's single base currency matches your Klarna account configuration. Read more about the [currency requirement](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/known-constraints.md).

## Installation and Merchant portal issues

### “You are connected to Klarna but you can’t use it” error

If the Klarna payment method says, "You are connected to Klarna but you can’t use it to accept payments because your account is still being approved ....", you don’t need to wait for approval. Follow the [Installation steps](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/how-to-install-klarna-payments-on-shopify) to complete the integration in Klarna's [Merchant portal](https://portal.klarna.com/)\> **Integration guides**.

### Enable the "Integration guides" link in the Merchant Portal if it doesn't show for your Klarna merchant account

Contact Klarna Merchant support team who can enable the Integration guides app for your account if you’re contracted directly with Klarna. If you aren’t contracted directly with Klarna, for example, you’re contracted instead via Shopify Payments, Mollie, or another payment service provider (PSP), you should follow your integrator's steps for activating Klarna. You can confirm if Integration guides are enabled by checking the left navigation for **Integration guides** in the [Klarna Merchant portal](https://portal.klarna.com/). If the left side navigation menu isn't showing at all for any Merchant Portal apps in your browser, click the Merchant Portal menu navigation, that is, the black circle with 3 white lines inside, at the top left of the screen to open the menu.

### Page spins infinitely within Integration guides app in Merchant portal

- Confirm that you have the Integration guides app enabled for your account. If you don't see the Integration guides app in the Merchant Portal menu, [request Klarna to enable the Integration guides app for your account](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/troubleshoot-your-installation).
- Try using a new incognito Chrome browser window to avoid cached data. We suggest using Chrome as not all browser types are supported.
- If you previously completed the integration through step 4 of the Integration guide (Test), and then uninstalled the Klarna app, you'll need to wait [48 hours](https://shopify.dev/apps/webhooks/configuration/mandatory-webhooks#shop-redact) or request Klarna Merchant support to do a database update before you’re able to redo the integration.
- If you have multiple Klarna merchant accounts, that is, a different merchant ID for each of multiple Shopify stores, make sure the correct Klarna merchant ID is selected in the Klarna Merchant portal for the appropriate associated Shopify store.

If you see the error stating "You already have a store that is integrated with Klarna...", please contact Merchant support and provide the displayed `correlation_id`.

### "Unexpected error" when trying to complete the integration

If you see the “Unexpected error” message when going through the integration steps, uninstall the Klarna app from within the Klarna payment method in your Shopify admin, under **Settings**\> **Payments**). Don’t uninstall the "Klarna Payments" HPSDK app from the store's Apps menu, as the HPSDK app doesn’t impact the new payments app integration, but is used for order management for previously placed HPSDK Klarna orders. New payments apps, like the Klarna app, aren’t displayed within the store's Apps menu. You can only uninstall the new payment apps from within the payment method's configuration when the payment method isn’t active. If the payment method isn’t currently active in your store, search for the Klarna payment method and click **Activate** to get to the payment method's configuration options. Once there, you can check if you can uninstall the app. Once you’ve uninstalled the Klarna app, you can [retry the installation steps](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/how-to-install-klarna-payments-on-shopify) in the Integration guides app in the Klarna Merchant portal. If you previously completed the integration through step 4 of the Integration guides (Test), and then uninstalled the "Klarna" app, you'll need to wait [48 hours](https://shopify.dev/apps/webhooks/configuration/mandatory-webhooks#shop-redact) or request Klarna Merchant support to do a database update before you're able to redo the integration.

## Connection issues

### Update the database after uninstalling the Klarna app

If you previously completed the integration through **Integration guides** step \#4 (Test), then uninstalled the Klarna app, you need to [wait 48 hours](https://shopify.dev/apps/webhooks/configuration/mandatory-webhooks#shop-redact) or request your region’s Klarna Merchant support team to manually update the database before you can redo the integration.

### Confirm that your store is configured in Klarna's database 

If you've confirmed that the app is installed in your store, to next verify the database connection, log into the [Klarna Merchant portal](https://portal.klarna.com/), select **Integration guides** from the left-side menu and select the **Shopify** option. 

- If you’re taken directly to directly Step 4 (Test), your store already has an entry in the database already. If that page doesn't load, or loads with an error, [refer to this solution from the troubleshooting guide](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/troubleshoot-your-installation).
- If the page loads at any other step, please complete the Integration guides flow to get a valid entry in our database. 

Note that even though you’ll generate a set of API credentials during the Integration guides flow, you don’t need to enter those credentials anywhere in your Shopify store, as the code does it for you.

## Known constraints

### 1. Klarna Payments accepts orders only for customer billing addresses in the markets that match the store base currency

- Currently, Klarna Payments accepts orders only for customers with billing addresses in the markets that match the currency of the order. See the [list of supported markets and currencies in Klarna payments documentation](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales.md).
- Customers in non-supported markets based on the order's currency are shown an error message on Klarna payment page load that the Klarna order can’t be placed or an error in Shopify checkout ("Your payment can’t be processed for technical reasons. Try again or use a different payment method."), depending upon the Klarna account configuration and Shopify store settings, for example, when theKlarna account doesn't support the store's single base currency.
- Shopify limits Klarna payments as an alternative payment method, the same for all alternative payments methods, to always transact only in the store’s single base currency, [as documented in this Shopify help article](https://help.shopify.com/en/manual/payments/shopify-payments/multi-currency/conversions#shopify-payments-and-other-payment-providers). Even if the store displays prices in multiple currencies, including in checkout or using Shopify Markets, Shopify will update the order's currency to the store's single base currency when redirecting to the alternative payment provider. 
- If you need to support multiple currencies with Klarna, you can use multiple Shopify stores or an alternative checkout, for example, [Global-e](https://www.global-e.com/).
- For example, if the store base currency is SEK, Klarna payments will be able to accept orders for customers whose billing country is Sweden. Customers with addresses in other countries will see an error message, for example one shown in the screenshot below. The exact error message may differ depending on region and Klarna product (for example: "We can't offer you this payment method right now" or “Option not available”.) For stores with base currency of EUR, Klarna can accept orders for multiple regions which transact in EUR. For other countries, a single region is supported for each currency.


![ The exact error message may differ based on region and other data.](ZkIlBkFLKBtrW0nD_image-46-.jpeg)
*The exact error message may differ based on region and other data.*

### 2. Klarna requests customers to enter their phone number

Even if customers previously entered their phone number in Shopify checkout, Shopify may not share that phone number with payments integrations when email is required in checkout. Thus [Klarna may ask the customer to enter their phone number again](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/how-to-handle-customer-data.md).

### 3. Renaming the payment method isn’t supported

While some [Shopify custom script code](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/shopify-plus-custom-scripts) works for payment methods integrated via Shopify's new payments app integrations, [renaming the payment method isn’t currently supported by Shopify](https://community.shopify.com/c/payments-shipping-and/can-you-add-or-change-the-name-of-payment-options/m-p/2040190) in the payments app, as payment providers can configure translations for the payment method name. If you wish to rename the Klarna payment method you may choose to use a third party app such as Payfy or BSure Checkout Rules. You can find the list of translated payment method names in [this article](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/language-locale-and-translations.md).

### 4. The amount paid by the customer to Klarna doesn't match the Shopify order total

If customers update a related, but different Shopify session separately from the Shopify session used to place the Klarna order, the order totals between the Shopify and Klarna orders may not match, but the **Paid by customer** amount for the Shopify order should always match the Klarna order total. While not ideal, this is working as expected and designed. Make sure to only fulfill order line items paid for by the customer.


![klarna docs image](3c75a614-a516-4c48-b010-2dd25862257c_order+total+mismatch.jpeg)image

## Feedback and support

Need help? We're happy to assist! Reach out to [your region’s merchant support team](http://klarna.com/merchant-support). You can also refer to [Shopify community](https://community.shopify.com/) for questions, support, and feedback, or visit the [Shopify help center](https://help.shopify.com/).</http:>