# Source: https://docs.stripe.com/payments/paymentintents/lifecycle.md

# How PaymentIntents and SetupIntents work

Learn how PaymentIntents and SetupIntents work within the payment flow.

The main difference between the [Payment Intents](https://docs.stripe.com/api/payment_intents.md) API and [Setup Intents](https://docs.stripe.com/api/setup_intents.md) API is their purpose:

- **Payment Intents API**: Used to collect payment and charge a customer immediately. It creates a charge and processes a transaction to collect funds.
- **Setup Intents API:** Used to collect and save payment method details for future use without creating a charge. Sets up payment credentials without processing any payment.

| Payment Intent API                                                         | Setup Intents API                                                                                                          |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Creates an immediate charge                                                | Creates no charge                                                                                                          |
| Tracks a payment’s lifecycle                                               | Tracks the progress of setting up a payment method                                                                         |
| Uses 3D secure to authenticate the customer for the applicable transaction | Uses 3D secure to authenticate a payment method without charging it, and creates a mandate or agreement for future charges |

*Asynchronous* (Asynchronous refers to events happening at independent times in independent systems) payments can be challenging to manage because they can depend on customer actions that happen outside of your application. For example, a user might need to confirm a payment using *3D Secure* (3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments).

To simplify payment management, Stripe uses a state machine that allows you to track the state of a payment flow. To learn the states for each API, select the applicable tab below:

# PaymentIntents

> This is a PaymentIntents for when payment-setup-intent is paymentintent. View the full page at https://docs.stripe.com/payments/paymentintents/lifecycle?payment-setup-intent=paymentintent.

When the PaymentIntent is created, it has a status of `requires_payment_method`1 [until a payment method is attached](https://docs.stripe.com/payments/payment-methods/overview.md).

We recommend creating the PaymentIntent as soon as you know how much you want to charge, so that Stripe can record all the attempted payments.

After the customer provides their payment information, the PaymentIntent is ready to be confirmed.

In most integrations, this state is skipped because payment method information is submitted at the same time that the payment is confirmed.

If the payment requires additional actions, such as authenticating with [3D Secure](https://docs.stripe.com/payments/3d-secure.md), the PaymentIntent has a status of `requires_action`1.

After required actions are handled, the PaymentIntent moves to `processing` for *asynchronous payment methods* (Asynchronous payment methods can take up to several days to confirm whether the payment has been successful. During this time, the payment can't be guaranteed), such as bank debits. These types of payment methods can take up to a few days to process. Other payment methods, such as cards, are processed more quickly and don’t go into the `processing` status.

If you’re separately [authorizing and capturing funds](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md), your PaymentIntent can instead move to `requires_capture`. In that case, attempting to capture the funds moves it to `processing`.

A PaymentIntent with a status of succeeded means that the payment flow it is driving is complete.

The funds are now in your account and you can confidently fulfill the order. If you need to refund the customer, you can use the Refunds API.

If the payment attempt fails (for example due to a decline), the PaymentIntent’s status returns to `requires_payment_method` so that the payment can be retried.

You can cancel a PaymentIntent at any point before it’s in a `processing`2 or `succeeded` state. Canceling it invalidates the PaymentIntent for future payment attempts, and can’t be undone. If any funds have been held, cancellation releases them.

PaymentIntents might also be automatically transitioned to the `canceled` state after they have been [confirmed](https://docs.stripe.com/api/payment_intents/confirm.md) too many times.

1 Versions of the API before [2019-02-11](https://docs.stripe.com/upgrades.md#2019-02-11) show `requires_source` instead of `requires_payment_method` and `requires_source_action` instead of `requires_action`.

2 You can cancel a PaymentIntent in the `processing` state when the associated Payment Method is ACH, ACSS, AU BECS, BACS, NZ BECS, and SEPA. However, it might fail due to a limited and varying cancellation time window.


# SetupIntents

> This is a SetupIntents for when payment-setup-intent is setupintent. View the full page at https://docs.stripe.com/payments/paymentintents/lifecycle?payment-setup-intent=setupintent.

When the SetupIntent is created, it has a status of `requires_payment_method`1 until a payment method is attached.

After the customer provides their payment method information, the SetupIntent is ready to be confirmed.

In most integrations, this state is skipped because payment method information is submitted at the same time that the SetupIntent is confirmed.

If the setup requires additional actions, such as authenticating with 3D Secure , the SetupIntent has a status of `requires_action`1.

After required actions are handled, the SetupIntent moves to `processing`. Although some payment methods (for example, cards) can process quickly, other payment methods can take up to several days to process.

A SetupIntent with a status of `succeeded` means that the setup is successful.

You can now attach this payment method to a Customer object and use this payment method for future payments.

If the setup fails, SetupIntent’s status returns to `requires_payment_method`.

You can cancel a SetupIntent at any point before it is `processing` or `succeeded`.

1 Versions of the API before [2019-02-11](https://docs.stripe.com/upgrades.md#2019-02-11) show `requires_source` instead of `requires_payment_method` and `requires_source_action` instead of `requires_action`.

