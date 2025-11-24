# Source: https://docs.klarna.com/payments/after-payments/order-management/before-you-start/order-management-in-a-nutshell.md

# Order management in a nutshell

## Here you can find a high-level description of how Order management works.

When your customers pay with Klarna and their orders are created, you need Order management to finalize the purchase journey. With this solution, you perform different order operations before, during, and after fulfilling the order. Here’s an overview of the order management operations:


![ Order management integration.](e4f32619-d4bd-4290-8b61-diagrams-Order-managementdec.jpg)
*Order management integration.*

You can manage orders through a set of server-side calls. They can be grouped into 3 main categories: **View and change orders** This category includes the following requests:

- Check the details of an order.
- Update the order amount.
- Update merchant references.
- Update customer address.
- Cancel an order.

**Capture and track orders** This category includes the following requests:

- Capture the full order amount.
- Capture part of the order amount.
- Check the details of a capture.
- Add shipping information.
- Send customer communications.

**Refund and extend orders** This category includes the following requests:

- Refund an order.
- Refund with return fees.
- Extend order authorization.
- Release order authorization.
- Extend payment date.