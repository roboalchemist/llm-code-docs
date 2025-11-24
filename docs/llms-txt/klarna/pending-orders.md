# Source: https://docs.klarna.com/payments/after-payments/order-management/more-actions/pending-orders.md

# Pending orders

## Learn how we handle the orders we detect as potentially fraudulent and how you help us in this process.

When we find suspicious orders, we ask you to delay the shipment so that we can perform a manual assessment and come to a resolution. While the assessment occurs, we set the orders' status to pending. This functionality is only available for merchants in the US and UK and isn't enabled by default, it needs to be activated for your account upon request. In a nutshell, the pending orders process implies:

1.  We identify an order as potentially fraudulent.
2.  We set the order's status to pending.
3.  We assess the order manually.
4.  After the assessment is completed, we send you the order's status.
5.  You check the order's status and inform your customer.

## During the fraud assessment

Once your customer pays with Klarna and an order is created, we perform a fraud assessment. This step is reflected in the order through the parameter `fraud_status`, with the possible values of `ACCEPTED`, `REJECTED`, or `PENDING`. If the `fraud_status` parameter is set to `PENDING`, the order is under fraud assessment. We put it on hold and ask you not to ship it until we finish the order review. During this step, you have to notify your customer that the order is in progress and the shipment won't occur immediately.

## After the fraud assessment

Usually, the assessment process takes us from 4 to 8 business hours, but it could last a maximum of 24 hours. After we complete the assessment, the `fraud_status` parameter in the order is set to `ACCEPTED` or `REJECTED`, depending on our resolution.

### Events and notifications

When we have the assessment resolution, we'll inform you through HTTP push notifications. We send a `POST` request to the notification URL you included when [initiating a payment](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/other-actions/authorization-callback.md). The body of the `POST` request includes the `order_id`, the timestamp of the decision in [this date format](https://docs.klarna.com/klarna-payments/api), and one of the following events:

- `FRAUD_RISK_ACCEPTED`: An order was accepted after the assessment.
- `FRAUD_RISK_REJECTED`: An order was rejected after the assessment.

When you have pending orders activated, the two possible initial values for the `fraud_status` parameter are:

- `ACCEPTED`: We automatically accepted the order when it was created.
- `PENDING`: We're waiting for the fraud assessment.

After the assessment, the `fraud_status` parameter can change from `PENDING` to the `FRAUD_RISK_ACCEPTED` or `FRAUD_RISK_REJECTED` status. We'll send you push notifications about the assessment when the `fraud_status` changes. We send the notifications every 10 minutes for 24 hours or until you reply to our `POST` request with a `200` code. After 24 hours, we stop sending notifications. The following is an example of a notification for an accepted order after a fraud assessment:

``` json
{
  "order_id": "de305d54-75b4-431b-adb2-eb6b9e546014",
  "event_type": "FRAUD_RISK_ACCEPTED"
}
```

Sample of a notification after fraud assessment. We highly recommend you validate the notification. You can \[ check the details of your order\] and confirm that the `fraud_status` parameter matches the notification.

## Overriding the fraud resolution

You can override our resolution of the fraud assessment and reject an order we accepted or, the other way around, accept an order we rejected. To reject an order we accepted, you simply send an API request to \[ cancel the order\]. To accept an order we rejected, you have to capture it within 4 hours after receiving the `POST` request and send an API request to [capture the order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/capture-and-track-orders.md). By accepting an order we rejected, you take over any fraud risk related to the order. Besides, if you don't capture the order within 4 hours, we'll cancel the order.