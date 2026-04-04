# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/how-to-install-osm-shopify-app.md

# How to install the Shopify On-site messaging app

## Read this guide to learn how to add the Klarna On-site messaging Shopify app to your Shopify store.

## Prerequisites

Before you begin, you must integrate Klarna Payments or enable Klarna for Shopify Payments. The On-Site Messaging app will rely on your integration to connect to your store.

We highly recommend that you are using [Online Store 2.0](https://www.shopify.com/partners/blog/shopify-online-store) and that you have upgraded to Checkout Extensibility for the best experience using this app. This installation guide is applicable for stores compatible with the Klarna OSM Shopify app. If your store isn’t compatible with the app, you can install Klarna On-site messaging manually using JavaScript. For more details, refer to the [manual OSM installation guide](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/manual-osm-shopify-integration/).

## 1. Install the Klarna On-site messaging Shopify app

- Install the Klarna On-site messaging app from the [Shopify App Store](https://apps.shopify.com/klarna-on-site-messaging).
- Click Install App.
- Grant permissions and confirm installation.

## 2. Connect your account

After installing the app, Klarna will try to connect your account automatically. If we detect your myshopify.com domain in our system, we'll link your store for you.

If not, follow these steps to connect manually:

- In your Shopify Admin, go to:  **Apps**\> **Klarna On-site Messaging**\> **Settings**
- Enter your Klarna Merchant ID (MID)
- Click Connect


![ A Klarna merchant account linked to a Shopify store.](a962fb0e-fdbe-472d-b0c7-710c7a83ede3_Klarna_Shopify_OSM_Account_setup_2023_08-01.jpeg)
*A Klarna merchant account linked to a Shopify store.*

You can find your Klarna MID in the Klarna Merchant Portal and it starts with a K, N or A and is followed by 6-7 digits. If you are not integrating Klarna Payments directly through Klarna please reach out to your payment partner for this. If you are getting a 404 error, please follow the steps [outlined here](https://docs.klarna.com/platform-solutions/shopify/klarna-osm-app-for-shopify/troubleshooting/#common-warnings-and-errors-error-request-failed-with-the-status-code-404) to troubleshoot.

## 3. Add placements

The final step is to add placements. If your store uses a theme that supports [Online Store 2.0](https://www.shopify.com/partners/blog/shopify-online-store) app blocks, follow the [App Blocks Guide](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/app-block-placements/)Vintage themes are no longer supported.

## Extended Access

The extended access setting enhances your Klarna integration allow us to gather additional information about orders placed with Klarna in your store and display it to the customer. These extended access features are enabled by default when you install the On-Site messaging app, but can be disabled by deselecting the Extended Access option in the app settings.

We access minimal data as needed for the following additional features:

- Updating Klarna’s merchant_reference_1 field with the corresponding [Shopify order name](https://shopify.dev/api/admin-graphql/2022-10/objects/Order#field-order-name). This allows us to display the correct order ID to your customers in the Klarna app. This also makes it easier for you and Klarna support teams to find orders quickly and easily in our systems if needed. (October 11, 2022)
- The Klarna order ID is added as a Shopify order note on the Shopify backend. This is also helpful information you can provide to Klarna merchant support if needed. (November 3, 2022)
- A Klarna tag is added to Shopify orders placed through Klarna. (September 20, 2023)
- Product URL and image URL are added to the Klarna order shortly after the order is placed. This allows your customers to see their order details in the Klarna app and emails from Klarna.

You can manage the **Extended Access** setting in **Apps**\> **Klarna On-site Messaging**\> **Settings.**

![ Extend Access is an optional configuration that provides additional permissions to enhance the Klarna On-site messaging app’s functionalities.](ff93388b-4422-4bd9-ace7-af6217f0358b-Extended-Access.jpeg " Extend Access is an optional configuration that provides additional permissions to enhance the Klarna On-site messaging app’s functionalities.") When Extended Access is enabled in a Shopify store, additional order details are visible in the Merchant portal, for example, the Shopify order ID as **Reference** and an image of the product.


![klarna docs image](fbd97a86-b42f-445b-a402-aa1a68b02117-SKOSM+Ext-Access.jpg)image

## Uninstalling the Klarna On-Site Messaging App

If you no longer want to use the Klarna On-site messaging (OSM) Shopify app in your store, do the following to remove all inserted code for your store:

1.  Disconnect the account from the Klarna OSM Shopify app in **Shopify admin**\> **Settings**\> **Apps**.
2.  Delete the app from **Shopify admin**\> **Apps** as shown on the screenshot below.


![Uninstalling the Klarna On-site messaging app from a Shopify store.](uninstall_the_app_in_Shopify.png)
*Uninstalling the Klarna On-site messaging app from a Shopify store.*

Deleting the Klarna OSM Shopify app removes all code from your store. You can confirm the code is deleted by viewing the HTML source and searching for the following code elements:

- To check that the JavaScript libraries loaded in your store have been deleted, search for the asyncLoad function in the source code.
- To check that the placement code has been deleted, search for the klarna-placement HTML element in the source code.

If you already removed the Klarna On-site messaging Shopify app, but the KlarnaThemeGlobals code was not removed from your theme (if added to your theme prior to 2022-Dec-13), you can manually remove it from the theme.liquid file in your **Shopify admin**\> **Sales channels**\> **Online Store**\> **Themes**\> **…**\> **Edit code**.