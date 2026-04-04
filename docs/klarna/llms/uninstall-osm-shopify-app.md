# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/uninstall-osm-shopify-app.md

# Uninstall the Klarna On-site messaging Shopify app

## This article outlines how you can remove the Klarna On-site messaging Shopify app from your store.

If you no longer want to use the Klarna On-site messaging (OSM) Shopify app in your store, do the following to remove all inserted code for your store:

1.  Disconnect the account from the Klarna OSM Shopify app in **Shopify admin**\> **Settings**\> **Apps**.
2.  Delete the app from **Shopify admin**\> **Apps** as shown on the screenshot below.


![ Uninstalling the Klarna On-site messaging app from a Shopify store.](befe5bc6-3443-479d-9bb1-159732f3bda6-shopify-skosm-delete-app.jpeg)
*Uninstalling the Klarna On-site messaging app from a Shopify store.*

Deleting the Klarna OSM Shopify app removes all code from your store. You can confirm the code is deleted by viewing the HTML source and searching for the following code elements:

- To check that the JavaScript libraries loaded in your store have been deleted, search for the `asyncLoad` function in the source code.
- To check that the placement code has been deleted, search for the `klarna-placement` HTML element in the source code.

If you already removed the Klarna On-site messaging Shopify app, but the `KlarnaThemeGlobals` code was not removed from your theme (if added to your theme prior to 2022-Dec-13), you can manually remove it from the `theme.liquid` file in your **Shopify admin**\> **Sales channels**\> **Online Store**\> **Themes**\> **…**\> **Edit code**.