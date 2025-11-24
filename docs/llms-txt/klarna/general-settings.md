# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/general-settings.md

# Settings used by Klarna on Adobe Commerce

## Learn which settings available in Adobe Commerce settings are used by the Klarna extension.

The [Adobe Commerce Admin](https://experienceleague.adobe.com/docs/commerce-admin/start/admin/admin.html) lets you configure and manage your store. Not all configuration options available in Admin impact Klarna. Klarna uses the following key settings:

- Klarna payment method setup
- Catalog and cart price rule
- Currency
- Delivery methods
- Products
- Shop URL
- Taxes: rules, zones, rates, and calculation configurations

## Klarna payment method setup

Once you’ve installed the extension from the Adobe Commerce marketplace, you need to set up some settings for Klarna in the Admin so that the payment method is usable. The most important settings are related to the Klarna API. Apart from that, there are other settings to configure so that Klarna will operate smoothly in your store.

You can find Klarna's configuration in the Admin in **Stores**\> **Configuration**\> **Sales**\> **Payment Methods**\> **Klarna**:


![Group_41_(1).png](Group_41_(1).png)
*Group_41_(1).png*

![Additional Klarna settings are available in the Payment Methods menu in the Admin.](Group_51.png)
*Additional Klarna settings are available in the Payment Methods menu in the Admin.*

## Catalog and cart price rule

With catalog and cart price rules you can allow your customers to buy products at reduced prices.

You can find the price rules in **Marketing**\> **Promotions**.


![You can apply the catalog and cart price rules to make the products in your store available at reduced prices.](Group_52.png)
*You can apply the catalog and cart price rules to make the products in your store available at reduced prices.*

Since the rules have an impact on the price of a product and the shipping costs, it also affects creating orders with Klarna. Klarna takesthese rules into account and sends the adjusted prices through the API.

## Currency

Using Klarna requires the correct currency setup. You can find the currency configuration options in **Stores**\> **Configuration**\> **General**\> **Currency Setup**.


![Group_41_(1).png](Group_41_(1).png)
*Group_41_(1).png*

![Configure the currency that will be sent to Klarna.](Group_71_(1).png)
*Configure the currency that will be sent to Klarna.*

The selected **Currency value** will be sent through the Klarna API. If the currency configuration is incorrect, Klarna API requests may fail. For example, if a customer places an order with the billing address in Germany, but the currency is the US Dollar, the request will fail. In this case, a currency mismatch error between the address and the currency is returned and the desired Klarna product can’t be used.

## Delivery methods

When a customer reaches the checkout, they can choose the desired delivery method for their order. You can configure this setting in **Stores**\> **Configuration**\> **Sales**\> **Delivery Methods**.


![Choose the delivery methods for Klarna orders placed in your Adobe Commerce store.|center](Group_72.png)
*Choose the delivery methods for Klarna orders placed in your Adobe Commerce store.|center*

The selected Delivery method can affect the total order value. Klarna takes this into account and this shipping cost information is sent to Klarna via the API integration.

## Products

To sell something in an online shop, products have to be configured. You can set up products in **Catalog**\> **Products**.


![Add, remove, and edit products in the Catalog menu in the Admin.](Group_73.png)
*Add, remove, and edit products in the Catalog menu in the Admin.*

Having the correct product configuration is critical as some information, for example, price, tax, and customer name, is passed to Klarna via the API during the Klarna order creation process. The details are later visible in the [Klarna merchant portal](https://portal.klarna.com).

## Shop URL

The shop’s URL must be correctly configured so that the correct URL is used on all store pages. Klarna uses the base URL setting to ensure our products work correctly. For example, Klarna needs a secure base URL for API callbacks and if the URL isn’t correct, Klarna won’t work correctly. You can set the base URL in **Stores**\> **Configuration**\> **Web**.


![The URL options of a store are available in the Configuration menu in the Adobe Commerce Admin.](Group_74.png)
*The URL options of a store are available in theConfigurationmenu in the Adobe Commerce Admin.*

## Taxes

Tax settings are important to make sure you're following the tax rules of your country. You need to set them up in 3 places:

- To configure tax zones and tax rates, go to **Stores**\> **Tax Zones and Rates**.


![Group_80.png](Group_80.png)
*Group_80.png*

- To configure tax rules, go to **Stores**\> **Tax Rules**.


![Group_80_(1).png](Group_80_(1).png)
*Group_80_(1).png*

- To configure tax calculations, go to **Stores**\> **Configuration**\> **Sales**\> **Tax**.


![Group_41_(1).png](Group_41_(1).png)
*Group_41_(1).png*

![You can change various tax settings of your products in the Admin.|center](Group_81.png)
*You can change various tax settings of your products in the Admin.|center*

Each of these settings plays a part when you're creating an order with Klarna. The tax calculation settings are especially important because they determine how taxes are applied and how prices for products and delivery are calculated. Klarna takes these settings into account and sends the prices through the API.