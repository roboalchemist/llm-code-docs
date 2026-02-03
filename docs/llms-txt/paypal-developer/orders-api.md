# Track packages with the Orders API

If you sell tangible goods, send tracking information to PayPal as soon as you ship items to your customers.

Providing tracking information and item-level details can also help you improve the customer experience and reduce your operational cost with features such as:

- Reduce dispute costs by allowing payers to dispute individual items instead of the entire order.
- Quicker access to money in payment and dispute holds. Adding tracking to an order qualifies holds for early release.
- Real-time package tracking updates inside the PayPal app and through push notifications (see **Keep customers informed** section), which reduces the need for third-party apps to provide order tracking on PayPal orders.
- Improved seller risk profiles built from shipping and order status, which helps lower reserve requirements.

Adding tracking information can also streamline and automate disputes. Instead of manually calling the Disputes API or using the Resolution Center to respond to disputes individually, the Tracking API streamlines resolution of "item not received" and "significantly not as described" disputes.

## Keep customers informed

PayPal sends push notifications from the PayPal app to update customers on shipping statuses when you provide a tracking number. Customers receive these notifications if they enable push notifications for the PayPal app in their device settings. Customers can manage push notification preferences in the PayPal app.

PayPal sends customers an email with tracking information. You can turn this feature on or off in the API call.