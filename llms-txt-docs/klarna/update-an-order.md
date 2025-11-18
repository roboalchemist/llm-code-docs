# Source: https://docs.klarna.com/payments/after-payments/order-management/manage-orders-in-the-merchant-portal/update-an-order.md

# Update an order

## Here you find the different options for updating an order in the Merchant portal.

Let's say your customer contacts you to add or remove an item from their order. In this scenario, you can easily handle the order updates within the Merchant portal. You can only update the orders that you’ve partially captured or not captured at all. So you can only apply changes on the order items you haven't shipped. The main way to update an order in the Merchant portal is by editing order lines in the order details. The key updates you can make to an order are:

- Adding items
- Removing items
- Applying discounts

## Adding items

You can add to the order as many items as you need by adding a new [order line](https://portal.klarna.com?help-page=article%3Awhat-are-order-lines) per item. Doing so increases the authorized order amount based on the price of the added items. Keep in mind that when you increase an authorized amount, we run a second risk assessment on the customer. If the update is rejected, your customer has to place a new order in your online store for the new items. Only specific payment methods support increasing the authorized amount. For more information, see the [conditions for updating an order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/view-and-change-orders.md).

## Removing items

You can remove any item from the order by deleting its corresponding order line. This action decreases the authorized order amount based on the price of the removed items.

## Applying discounts

You have two ways to apply discounts to orders:

- Adding a discount to the total order amount by including discount lines. 
- Adding a discount to a specific item in the order by editing the item's amount.

When you apply the changes, the updated amount replaces the original order amount. If you want to read more about editing order lines, see the [Help](https://portal.klarna.com?help-page=article%3Awhat-is-a-part-capture) section in the Merchant portal. The following image illustrates the order updates you can make by editing order lines in the Merchant portal.


![ Updating an order in the Merchant portal. ](640513d8-6372-4e08-8a98-f101970a8a01_Order+management_Merchant+portal_Update+order.jpeg)
*Updating an order in the Merchant portal.*