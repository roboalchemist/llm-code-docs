# Source: https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/extended-authorization-expiration.md

# Extended authorization expiration

## Support longer fulfillment times with an extended authorisation.

In certain business models and market segments, the fulfillment of online orders may take longer due to the nature of the products offered. These extended timelines are clearly communicated upfront to manage customer expectations and highlight the unique value of the products. Some examples include:

- **Businesses specializing in handmade creations**, such as artisanal crafts, bespoke jewelry, or custom furniture, often require additional time to produce each item with care and precision.
- **Companies offering personalized or made-to-order products**, like monogrammed clothing, custom artwork, or tailored skincare solutions, need extra time to process specifications and complete customization.
- **Small-batch or limited-edition production models**, often seen in boutique fashion or gourmet food businesses, may experience longer fulfillment times due to limited resources or intentional production pacing.

For these use cases, Klarna sets a default predefined authorization period of up to 180 days instead of the standard 28 days. This allows enough time to complete fulfillment and capture the order. This configuration is define during the onboarding to Klarna services.

## Ad hoc authorization extension

In the case of a merchant where the fulfillment time is typically within the standard 28 days for Klarna authorization, but there is a rare or exceptional situation that genuinely requires more time to fulfill an order before it expires, you can extend the authorization period using the Order Management API. This option is designed to provide flexibility when unexpected delays occur—not as a routine practice.To extend an order’s authorization, the system adds your account's configured expiration period to the date you initiate the extension. For example, if an order is placed on January 1 and your account has a 28-day expiration period, extending the order on January 15 will move the new expiration date to February 13. Keep in mind:

- Extending an order multiple times on the same day will result in the same expiration date.
- You can only extend an order within 180 days of its creation.
- Once an order expires, it can no longer be extended via this API.
- Orders placed using the "Pay Now by Card" method cannot be extended.
- In the U.S., orders using the "Financing" payment method ("Slice it 2.0" or "Fixed Sum Credit") are also not eligible for extension.

To extend an order, send a **POST** request to the following endpoint: `{apiUrl}/ordermanagement/v1/orders/{order_id}/extend-authorization-time` Provide `order_id` as a path parameter. The `order_id` is the identifier you get in a successful response when \[ placing a new order\]. You don't need a request body for this `POST` method. **Use this feature judiciously, and only when absolutely necessary.**

### Success response

If the request is successful, you'll receive a 204 No content response.

### Error response

​If your request contains errors, you'll receive an error response. Make sure the order is not expired or canceled and the `order_id` is correct.

``` json
{
"error_code": "NOT_ALLOWED",
"error_messages": [
"Order is expired. Authorization time cannot be extended."
],
"correlation_id": "ef30ffe5-5c42-485a-85b6-8aeb24689bc8"
}
```

Sample of an error response to extend order authorization. ​You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs section. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/extendAuthorizationTime)