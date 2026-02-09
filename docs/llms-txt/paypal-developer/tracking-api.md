# Add Tracking API Overview

As a merchant, you can use the Add Tracking API to send shipment tracking numbers to PayPal for PayPal transactions.

PayPal uses these numbers to discern and investigate fraudulent customers and keep customers informed. If you sell tangible goods, you are encouraged to send these numbers to PayPal as soon as you ship items to your customers. This information enables you to access funds more quickly, provide seller protection, and keep customers informed.

## Access funds more quickly

If the funds for a tangible goods sale are on hold, the fastest way that you can access these funds is to send PayPal the tracking number for the on-hold transaction. PayPal tracks these numbers and, upon delivery of the shipment, releases funds.

Holds can occur for any of these reasons:

- You are a new seller.
- You have been inactive for sometime.
- Your selling pattern has recently changed.
- You are selling high risk items.

Whenever a hold occurs, provide PayPal with proof of shipment so that PayPal can resolve the hold as soon as possible.

## Get seller protection

To determine your seller protection eligibility for a PayPal transaction, the tracking number is essential.

If a customer makes an `Item not Received` claim against you, send a number as early as possible. This action enables PayPal to settle this claim on your behalf without disturbing you.

Also, PayPal uses the number to determine whether the item was successfully delivered to the right destination and closes the claim on your behalf.

## Keep customers informed

To keep customers informed about their transactions:

- PayPal updates the tracking details on the **Transaction Details** page when you send a tracking number to PayPal.
- PayPal sends an email with the tracking information to customers. You can turn this feature on or off in the API call.
- PayPal sends push notifications from the PayPal app to update customers on shipping statuses when customers submit a tracking number. Customers receive these notifications if they have enabled push notifications for the PayPal app in their device settings. Customers can manage push notification preferences in the PayPal app.