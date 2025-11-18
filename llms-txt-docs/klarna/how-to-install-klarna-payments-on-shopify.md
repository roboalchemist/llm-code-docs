# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/payments-for-shopify/how-to-install-klarna-payments-on-shopify.md

# Installing Klarna Payments for Shopify

## Successfully integrate Klarna Payments with your Shopify store by following the step-by-step installation guide, verifying store setup, and ensuring required customer details for smooth transactions.

In order to go live with Klarna payments on Shopify, you need to log in into the Klarna Merchant portal. If you don’t yet have a Klarna merchant account, you can sign up [here](https://portal.klarna.com/products/signup/basic-info). Once the below steps are started, we recommend that you complete at the minimum steps 1 through 4 to avoid a [partial entry in Klarna's database, which results in an incomplete integration](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/troubleshoot-your-installation/#installation-and-merchant-portal-issues-unexpected-error-when-trying-to-complete-the-integration).<em>Make sure you are logged in to the correct Shopify store.</em> Once a store is associated with a merchant ID, that merchant ID will be blocked from use for another store. Each Shopify store must have its own unique Klarna merchant ID. If you connect Klarna to the wrong Shopify store, deactivate the payment method and uninstall the app. [Wait 48 hours](https://shopify.dev/apps/webhooks/configuration/mandatory-webhooks#shop-redact) for the association to be removed, and then try the installation over again. If you are stuck, reach out to Merchant support.

## Installation steps

### Step 1: Log into Shopify & check your settings, and log into Klarna Merchant Portal

Make sure your Shopify settings are ready to work with Klarna.

Navigate to **Shopify admin**\> **Settings**\> **Checkout**

1.  Under **Customer Contact Method**, select only **Email**. If the customer's email address isn't shared with Klarna, the customer will receive an error message from Klarna and will need to return to the Shopify checkout to enter their email. [Read more about contact options in Shopify documentation](https://help.shopify.com/en/manual/orders/notifications).
2.  Under **Customer Information\> Full Name** select **Require** **first and last name**
3.  Under **Customer Information\> Shipping address phone number** select **Required**


![Ensure these settings are selected before you integrate with Klarna.](Shopify_-_Admin_-_Checkout_Settings.png)
*Ensure these settings are selected before you integrate with Klarna.*

**Everything is now ready!** Log into both your Shopify admin as the full account owner and the Klarna Merchant portal. Follow the steps below, or watch [this video](https://www.youtube.com/watch?v=6DMr3a75VuY) to learn how to install the app.

### Step 2: Navigate to Integration Guides\> Shopify

In the [Klarna Merchant Portal](https://portal.klarna.com/integration-guides), click the **Integration guides** from the left side navigation. Click the **Shopify** option. If you don't have the **Integration guides** option displayed for your account when logged into Klarna Merchant portal, contact Merchant Support.


![Start the installation by choosing Shopify in the Klarna Merchant portal Integration guides.|365x365px](Klarna_-_MP_-_IG_-_Partner_Selection.png)
*Start the installation by choosingShopifyin the Klarna Merchant portalIntegration guides.|365x365px*

### Step 3: Start the Installation

Click **Continue** to start the integration process. Then click **Install Klarna Shopify Application.** Note: while this app is a public app, it isn't listed in the [Shopify app store](https://apps.shopify.com/), and won’t be displayed in your store's **Apps** menu like other apps, which is expected for Shopify new payments apps.


![Click Install Shopify Klarna Application to start the installation process|320x320px](Klarna_-_MP_-_IG_-_Shopify_-_Install_app.png)
*ClickInstall Shopify Klarna Applicationto start the installation process|320x320px*

### Step 4: Install the app in Shopify

You will then be redirected to Shopify. Click **Install** on the first page you land on, and click **Install** on the next page as well.


![Click Install to continue installing Klarna Payments to your store. |320x320px](Shopify_-_KP_App_-_Install.png)
*ClickInstallto continue installing Klarna Payments to your store. |320x320px*

### Step 5: Generate Credentials & Verify Integration

Generate and connect new [Klarna API credentials](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test/#getting-test-credentials-for-apis). Download these API credentials to your local computer, even though you won't need to use them anywhere. This step is required to move forward. In this step, the integration is verified.


![Click Generate and connect credentials to connect your store to Klarna. Then click Continue integration. |320x320px](Klarna_-_MP_-_IG_-_Shopify_-_Generate_Credentials.png)
*ClickGenerate and connect credentialsto connect your store to Klarna. Then clickContinue integration.|320x320px*

Click **Verify integration** to check that your Klarna Shopify integration is set up correctly.


![Click Verify integration to check that your Klarna Shopify integration is set up correctly.|320x320px](Klarna_-_MP_-_IG_-_Shopify_-_Verify_Integration.png)
*ClickVerify integrationto check that your Klarna Shopify integration is set up correctly.|320x320px*

### Step 6: Activate Klarna

Click **Next**, and you will land on the **Activate** page. Click **Next** again to be redirected to Shopify to activate Klarna in your checkout.


![To activate the Klarna payment method in your checkout, you’ll be redirected to your Shopify store admin.|320x320px](Klarna_-_MP_-_IG_-_Shopify_-_Activate.png)
*To activate the Klarna payment method in your checkout, you’ll be redirected to your Shopify store admin.|320x320px*

Activating the payment method in your store enables Klarna to display in checkout. Make sure to verify that Klarna loads successfully though as this step does no validation if the integration was completed successfully.


![Activate Klarna in your Shopify store.|320x320px](Shopify_-_Admin_-_Activate_Klarna.png)
*Activate Klarna in your Shopify store.|320x320px*

### Step 7: Check that Klarna appears in the checkout

**Klarna is now live in your Shopify store!** Check the integration by adding a product to your cart. Navigate to your checkout page, and see if the Klarna radio button appears. Click the **Pay Now** or **Complete** button to make sure the Klarna payment flow starts. Placing a [test order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-in-the-merchant-portal/capture-an-order/) isn't necessary, but you can learn how place test orders here. <em>Alternative payment methods will not show if logged in to ShopPay.</em> If you are logged in to ShopPay, no alternative payment methods will show. Klarna does not have an express button.

### What next?

**Next, we recommend you to proceed with installing the Klarna On-Site Messaging app to further boost your sales through Klarna.** [Learn about the Klarna On-Site Messaging app here.](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/how-to-install-osm-shopify-app/)

## Deactivating & uninstalling Klarna from Shopify

Deactivating Klarna means that Klarna will no longer appear in the checkout to your customers. If you uninstall the payments app completely, you will remove Klarna from the checkout, and you will not be able to manage any of your existing Klarna orders. To remove Klarna from your Shopify checkout, deactivate the alternative payment method in **Shopify admin**\> **Settings**\> **Payments**. We do not recommend uninstalling the app until all Klarna orders have been finalized, or your return window has passed for all existing Klarna orders. You will not be able to process refunds or captures if the app is completely uninstalled. After uninstalling the app, you need to wait for 48 hours until you can reinstall Klarna again through the Merchant Portal.


![ An example of Klarna in Payments settings where the red deactivate button needs to be clicked to uninstall Klarna|320x320px](Zp4dOx5LeNNTxVv1_image-75.jpeg)
*An example of Klarna in Payments settings where the red deactivate button needs to be clicked to uninstall Klarna|320x320px*

## Appearance in checkout: Language, locale, and translations

Klarna configures the translations for the Klarna payment method. For each supported language, one translation is available. Read more about it [in the Shopify documentation](https://shopify.dev/apps/payments/creating-a-payments-app/creating-a-payments-app#payments-app-extension-configuration-fields). Remember that you will only be able to offer Klarna in the base currency of your Shopify store - multiple currencies on a single Shopify store are not supported with the direct integration. Note the following rules which govern which translation is displayed in the checkout:

- The displayed translation isn't determined by the customer's country or storefront language.
- The translation used in the store's checkout is determined by the store's single checkout language, which is configured in the store’s Shopify admin under **Settings**\> **Checkout and accounts**\> **Manage checkout language**.

The following table shows translated payment method name in each language:

| **Language** | **Translated payment method name**        |
|--------------|-------------------------------------------|
| Czech        | Klarna - Zaplať ve 3 splátkách            |
| Danish       | Klarna - Betal nu eller senere            |
| Dutch        | Klarna - Betaal nu of betaal later        |
| English      | Klarna - Flexible payments                |
| Finnish      | Klarna - Maksa heti tai myöhemmin         |
| French       | Klarna - Payer maintenant, ou plus tard   |
| German       | Klarna - Sofort oder später bezahlen      |
| Greek        | Klarna - 3 άτοκες δόσεις                  |
| Hungary      | Klarna - Fizetés most vagy fizetés később |
| Italian      | Klarna - Paga in 3 rate                   |
| Norwegian    | Klarna - Betal nå eller senere            |
| Polish       | Klarna - Kup teraz, zapłać później        |
| Portuguese   | Klarna - 3 pagamentos sem juros           |
| Spanish      | Klarna - Paga a plazos sin intereses      |
| Swedish      | Klarna - Betala nu eller senare           |

Currently, payment methods can’t be renamed for Shopify Plus merchants via custom scripts. This is a known constraint and you can [read more about it in this Klarna.Docs article](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/known-constraints/#4-renaming-the-payment-method-isnt-supported). You can, however, use third party apps such as Payfy or BSure Checkout Rules to rename the payment method.

### Language and locale

The locale for Klarna payments hosted payment page is set based on the store's language concatenated with the customer's billing address country. For example, the English language selected for a customer with a US billing address entered in Shopify checkout would result in a request locale of en-US when Klarna payments is loaded. If the requested locale is supported by Klarna payments, per [Available purchase countries, currencies and locales,](https://docs.klarna.com/klarna-payments/in-depth-knowledge/puchase-countries-currencies-locales/) the locale will be honored. If the locale isn't supported, English is used as a fallback. Locale isn't configurable in Klarna. You can configure your store's language in the Shopify admin under **Settings**\> **Languages**. One way to check a store's Shopify language is via the browser’s developer tools, for example, by entering Shopify.locale in your browser's developer tools’ **Console**, as shown on the following snippet.

``` http
Shopify.locale
```

Enter Shopify.locale in the Developer tools' console to check a Shopify store's language.


![ You can check a store's Shopify language in your console.|740x740px](ZkIv2kFLKBtrW0xU_locale.jpeg)
*You can check a store's Shopify language in your console.|740x740px*