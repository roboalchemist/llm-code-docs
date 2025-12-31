# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/payments/order-management-in-prestashop.md

# Order Management in Prestashop

## Order Management on PrestaShop outlines how Klarna orders are handled within the admin panel, including automated or manual capture, refund processing for captured orders, and integration features like partial actions, shipment tracking, and status synchronization to streamline operations.

The order management in this module works differently compared to previous PrestaWorks Klarna modules, particularly you need to configure the capture upon fulfillment feature for orders to captured upon fulfillment. Even if you have used a Klarna module in PrestaShop previously, please review this section carefully.

## Order handling

Klarna module allows you to manage and see the order information. To see that you need to navigate to the **Orders -\> Orders** page in the PrestaShop admin panel. There you will find all of the orders created in your shop including those processed by the Klarna module. Those orders will be set to different statuses depending on the payment state. You can see additional order information by clicking on the “View” button.

## Capture

Since version 1.0.4, order capture upon fulfillment feature was added, providing 3 ways to capture your orders. You can capture orders automatically when it reaches the desired PrestaShop order status using the Capture upon fulfillment functionality, please refer to that section of the document. You can also capture manually from the PrestaShop orders management page. If the order was processed by the Klarna system in the detailed order view you will see a new section added.


![image](Zz3xnK8jQArT1E5e%20PrestaShoporders.jpeg)
 To capture the order, click the first button with the label **CAPTURE PAYMENT**. Once the button is clicked the payment will be captured and the order status will be set to the one that was defined in the Order Status Mapping settings. ***While orders can also be managed within the [Klarna Merchant Portal](https://portal.klarna.com), it is recommended to do order management within your PrestaShop admin*** , it is recommended to do order management within your PrestaShop admin to keep the data in sync between Klarna and your shop.  Updates made in the Klarna Merchant Portal will not update the order in your PrestaShop store.   You can access the Klarna Merchant Portal order by clicking the Klarna reference number. Inside the Klarna merchant portal, you can view more information about the order and transaction information.


![Prestashop manage order settings](Zz3yCK8jQArT1E58_PrestaShopManageKlarnaorder.jpeg)
*Prestashop manage order settings*

### Partial capture

As of version 1.1.0, partial capture is supported. You can select items that can be captured from your order management page, or capture the order amount instead of the items included in the order. To partially capture orders, you need to click on the **CAPTURE ORDER** button on the order management page.  You will get a modal that displays the order's line items in more detail, you will see all of the items that are available to capture as well as the total amount.

![Partial capture in Prestashop](Zz31aq8jQArT1E9e_PrestaShopPartialcapture.jpeg "Partial capture in Prestashop") To capture individual items you need to select the checkbox for the desired order line items. Once that is done the amount to be captured will appear on the button and it will become active. Keep in mind that you are not able to capture more than the order amount that is available to capture, so if that becomes the case, the button will become inactive once again. Similarly, with order *amount*capture, you enter the amount in the field which is presented when you click the link **Capture amount.** You can partially capture orders as long as there is available funds to capture. As soon as you partially capture the order status will be set to the one that was defined in the Order Status Mapping settings. All of the captures can be seen in PrestaShop Klarna order details, and in the Klarna Merchant Portal.

## Cancel order

Before an order is captured, you could cancel it. To cancel, click the **CANCEL ORDER** button and the order status will be set to the one that was defined in the Order Status Mapping settings.

## Refunds

Only captured Klarna orders can be refunded. In the order list you will see orders with the status “Payment accepted”, these orders can be refunded. The refund can be initiated by clicking the **Refund**button on the order management page. Once the order is captured the Klarna section will change and have the refund button. When the button is clicked you will see a modal with items available for refund action. To initiate a full refund select all of the items (or enter the whole order amount) and click refund. As soon as you issue the refund the order status will be set to the one that was defined in the Order Status Mapping settings. The list of refunds can be seen in PrestaShop Klarna order details, and in the Klarna Merchant Portal.


![Refunds in Prestashop](Zz32xq8jQArT1E_S_PrestaShopPartialrefund.jpeg)
*Refunds in Prestashop*

### Partial Refund

Partial refund functionality was included in the 1.2.0 Klarna Payments module version. Same as with the **Partial Capture,**you can refund part of your Klarna order or a selected amount of that order. To partially refund an order, you need to navigate to the orders management page, click on the order that was captured, or at least partially captured. Same as for a full refund, you will find a refund button in the Klarna Payments management section. Once the button is clicked a modal will open up and there you will be able to either refund items or the amount you define.

## Shipment tracking information

As of version 1.2.0**,**Shipment Tracking Information feature was included. When you capture the order, shipping information is automatically sent to Klarna with the order’s capture call.

## Initial payment method

The customer’s initial payment method cannot be displayed on the order confirmation page, and thus the same field in the PrestaShop back office, as Klarna only provides this initial payment method data for an order in English.

## Automatic order status synchronization

The setting “Enable automatic order status change” allows you to manage how the PrestaShop order statuses should behave based on Klarna order status. The toggle option can be found in the "Additional settings" section. By default the toggle is enabled meaning that:

- PrestaShop order statuses will be updated according to Klarna's order status
- The update is done only once to the same status, so you can still set custom order status if needed, as it will not be overridden.

If the toggle is deactivated:

- PrestaShop statuses will not be updated according to Klarna, only the initial status for new orders will be added, allowing you to customize PrestaShop statuses to your liking.


![Automatic order status change in Prestashop](Zz35xq8jQArT1FCi_PrestaShopautomaticorderstatuschange.jpeg)
*Automatic order status change in Prestashop*