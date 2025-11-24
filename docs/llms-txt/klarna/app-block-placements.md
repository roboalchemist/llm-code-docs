# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/app-block-placements.md

# App Block placements

## Display Klarna On-Site Messaging on your Shopify store by installing the app and customizing dynamic or static placements across key pages for a tailored shopping experience.

## Prerequisites

To add app block placements you need to first have [installed the Klarna On-Site Messaging app](https://docs.klarna.com/platform-solutions/shopify/klarna-osm-app-for-shopify/how-to-install-osm-shopify-app) correctly. You also need to have a theme that supports [Online Store 2.0](https://www.shopify.com/partners/blog/shopify-online-store) app blocks. For vintage themes please see [Vintage Ad Placements](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/vintage-ad-placements).

## Placements

Placements are containers for the different messaging assets we offer. Placements are either dynamic, that is, the messaging is updated based on the purchase amount, or static, meaning that the messaging isn’t linked to the amount and isn’t updated dynamically. You can add placements to the following types of pages in your Shopify store:

- **Product Page** supports amount-based (dynamic) and non-amount based (static) placements.
- **Cart Page** supports amount-based (dynamic) and non-amount based (static) placements.
- **Home Page** supports non-amount based (static) placements.
- **Collections** **Page** supports non-amount based (static) placements.
- **Static Page**supports non-amount based (static) placements.

If you’re not sure which placements to pick, see the [answer in our Frequently asked questions](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/frequently-asked-questions). 

## Adding placements

### Open theme customizer

You can navigate to App Blocks through the On-Site Messaging home page by clicking **Go to App Block Instructions** and then proceeding to click **Open customizer**. You can also navigate to **Store admin**\> **Sales channels**\> **Online store**, and click **Customize.**


![Shopify_-_Admin_-_Online_Store.png](Shopify_-_Admin_-_Online_Store.png)
*Shopify_-_Admin_-_Online_Store.png*

### Add the Klarna app block and position it in the template

From the select box in the top center of the theme editor, select the desired theme, for example, **Products**\> **Default product**.


![Shopify_-_Admin_-_Theme_editor_-_template_menu.png](Shopify_-_Admin_-_Theme_editor_-_template_menu.png)
*Shopify_-_Admin_-_Theme_editor_-_template_menu.png*

Then, in the left-side menu, use the **Add block** option to add a **Klarna Placement**, available under **APPS**, as shown in the screenshot.


![Shopify_-_Admin_-_Theme_editor_-_add_app_block.png](Shopify_-_Admin_-_Theme_editor_-_add_app_block.png)
*Shopify_-_Admin_-_Theme_editor_-_add_app_block.png*

If you are not able to find Klarna On-Site Messaging under APPS, you may need to instead use the [CSS method](https://docs.klarna.com/platform-solutions/shopify/klarna-osm-app-for-shopify/vintage-ad-placements) in the vintage ad placement installation method.After inserting the block, drag the **Klarna Placement** App Block to the desired location in the template, for example, below **Price**.


![After inserting the block, drag the Klarna Placement App Block to the desired location in the template.](Shopify_-_Admin_-_Theme_editor_-_add_app_block_-_SKOSM_block.png)
*After inserting the block, drag theKlarna PlacementApp Block to the desired location in the template.*

### Select placement type and select theme

You can edit the configuration options within the **Klarna Placement** app block by selecting between options in the side panel. You have a choice of:

1.  **Placement type** - this determines the content and general design of the placment
2.  **Theme** - applies some basic formatting
3.  **Padding**
4.  Message prefix

Not sure which placement to choose? [Read our recommendations here](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/frequently-asked-questions.md). Continue reading on this page to learn more about customizing the placements.


![The configuration options available within the Klarna Placement app block.](Shopify_-_Admin_-_Theme_editor_-_app_block_panel.png)
*The configuration options available within the Klarna Placement app block.*

## Customizing placements

If you want to customize the the placements in your Shopify store, you can do it in one of the following ways:

1.  Edit the underlying CSS styling in your store’s source code, as described in the [Customize placements with CSS](https://docs.klarna.com/conversion-boosters/on-site-messaging/additional-resources/styling-on-site-messaging-with-css.md) article on Klarna.Docs.
2.  Edit the placements in the Klarna Merchant portal, as described in the [Customize placements through Merchant portal](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/app-block-placements) article on Klarna.Docs.

Note that only the **Custom** theme is customizable. If you use the default or dark theme, you won’t be able to see any customizations in the storefront. Some customization options, that is, changes in padding and alignment, affect the placement itself and not the contents of the placement. These options are available in the Klarna On-site messaging Shopify app in Shopify admin.  Customizations in the app and the Merchant portal impact the placement differently and you may need to apply the custom styling in both to see the desired result. Examples of such customization are the Merchant portal placement text alignment within the placement and the **Ad Position** alignment in the Klarna OSM Shopify app* *that affects the position of a placement on the page. Additionally, only selected Klarna placements support text alignment within the placement, and some themes may not honor the styling for placement alignment on the page.

## Locale and language

Klarna’s On-site Messaging app ensures the currency your customers see in the placement matches the currency displayed on your storefront. Learn more [here](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/frequently-asked-questions.md).

## Checkout Messaging - Available on Shopify+

Checkout On-site Messaging is only available for Shopify plus merchants, and you must reach out to merchant@klarna.com to have it added to your account. Ensure you have completed the steps outlined in the article [Install the On-site messaging app](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/how-to-install-osm-shopify-app) before proceeding with adding checkout messaging. You will also need to ensure you have upgraded to the [Shopify Checkout Extensibility](https://www.shopify.com/plus/upgrading-to-checkout-extensibility). From within the the Customizer, add a product to your cart. Then navigate to **Checkout and customer accounts**.


![Shopify_-_Theme_Customizer_-_Select_Customer_Accounts.png](Shopify_-_Theme_Customizer_-_Select_Customer_Accounts.png)
*Shopify_-_Theme_Customizer_-_Select_Customer_Accounts.png*

You will then land in the checkout. To add the placement on each page of the checkout, click **Add app block** and then click **Klarna On-site Messaging**. The app block will be added, and you will be able to set the Checkout Behavior. Toggle on **Include app block in Shop Pay**. Save the theme.


![Shopify_-_Admin_-_Theme_editor_-_Checkout_-_add_app_block_-_SKOSM.png](Shopify_-_Admin_-_Theme_editor_-_Checkout_-_add_app_block_-_SKOSM.png)
*Shopify_-_Admin_-_Theme_editor_-_Checkout_-_add_app_block_-_SKOSM.png*

The app block will be added, and you will be able to set the Checkout Behavior. Toggle on **Include app block in Shop Pay**. Save the theme.


![Shopify_-_Admin_-_Theme_editor_-_Checkout_-_SKOSM_block_setting.png](Shopify_-_Admin_-_Theme_editor_-_Checkout_-_SKOSM_block_setting.png)
*Shopify_-_Admin_-_Theme_editor_-_Checkout_-_SKOSM_block_setting.png*

Repeat these steps on each page of the checkout by navigating to the Shipping and Payment screens. Make sure to save the theme each time.


![Shopify_-_Admin_-_Theme_editor_-_Checkout_-_navigate.png](Shopify_-_Admin_-_Theme_editor_-_Checkout_-_navigate.png)
*Shopify_-_Admin_-_Theme_editor_-_Checkout_-_navigate.png*

Ensure that you have added the placement to the Payment Page, and that the **Include app block in Shop Pay** setting is toggled on. Save the theme.


![Shopify_-_Admin_-_Theme_editor_-_Checkout_-_Payment_page_-_SKOSM_app_block.png](Shopify_-_Admin_-_Theme_editor_-_Checkout_-_Payment_page_-_SKOSM_app_block.png)
*Shopify_-_Admin_-_Theme_editor_-_Checkout_-_Payment_page_-_SKOSM_app_block.png*

### Checkout Placement Settings

There are a few customization options available for the checkout placement. It can be enabled or disabled within the ShopPay checkout. We recommend this to be enabled as customers may struggle to navigate to Klarna from the ShopPay checkout without guidance. You can add this by clicking **Checkout behavior** in the app settings and checking the box **Include app block in Shop Pay**. We offer customized messaging for this purpose that can be enabled by reaching out to your partner success team or merchant@klarna.com.


![ An example of customized messaging in the ShopPay checkout.](ZtHB3EaF0TcGJlsM_image-89-.jpeg)
*An example of customized messaging in the ShopPay checkout.*

Error messaging in the settings are descriptive and will explain in what cases (and with which settings) the messaging will not show to your customers. An example of this is if a customer country is not enabled on your Klarna merchant ID. In such a case the messaging would not be displayed to customers in that country as they would not be able to proceed with Klarna as a payment method.