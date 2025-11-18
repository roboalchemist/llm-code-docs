# Source: https://docs.klarna.com/payments/in-store-payments/integrate-klarna-in-store/api-integration.md

# In-store API integration

## Use Klarna API to integrate In-store with your store's solution.

Klarna In-store uses the [Klarna payments](https://docs.klarna.com/payments/web-payments/before-you-start/what-is-klarna-payments.md) solution to make in-store payments possible. When integrating Klarna In-store with your system, you will receive all flavours of Scan QR: dynamic QR, payment link and static QR. Depending on your store setup, refer to one of the step-by-step guides:

## Dynamic QR and payment link

Here’s the process in a nutshell:

1.  As a partner, you create a payment session.
2.  You share a QR code or a payment link with a customer who's buying in a physical store.
3.  The customer scans the QR code or receives the payment link.
4.  The customer completes the payment.
5.  An order is placed and an order identifier is automatically created.

## Static QR

You can also let your customers pay with Klarna by scanning a static, printed QR code.

1.  The customer scans the QR code and receives a short code.
2.  The customer provides the short code to the cashier, who, in turn, enters the short code into the point-of-sale system. 
3.  As a partner, you create a payment session with the short code.
4.  The customer completes the payment.
5.  An order is placed and an order identifier is automatically created.

You can also use our API to \[ cancel the payment\] if it's no longer needed or if the session has expired on your end. Refer to the documentation for each step for technical details, call descriptions, and sample requests and responses.