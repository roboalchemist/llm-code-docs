# Messaging with buttons

Integrate messaging directly with your buttons to promote Pay Later offers and other PayPal value propositions to your customers. Adding messaging can help improve conversion and attract new customers.

![image](https://www.paypalobjects.com/ppdevdocs/paylater-horizontal-two%20button-100.png)

**info**
**Note:** Messaging is currently only supported for US merchants and US customers. Merchants must be eligible for Pay Later to display Pay Later offers with buttons. Other PayPal value propositions will still show, if ineligible for Pay Later.

## Know before you code

### Prerequisites

This feature modifies an existing [checkout integration](/docs/checkout/standard/) and uses the following:

- [PayPal JavaScript SDK](/sdk/js/configuration/)
- [Orders REST API - Create order endpoint](/docs/api/orders/v2/#orders_create)

### Explore PayPal APIs with Postman

You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

Include your messaging options to the buttons configuration object. Learn more about the full list of available options by reviewing the [JavaScript SDK reference](https://developer.paypal.com/sdk/js/) page. To display the strongest message to the customer, use `message.amount` with the current total based on the product or cart.

**Note:** The message.amount option functions independently from the captured order total and has no impact on it.

#### Button Examples

The message content adapts to the buttons that are displayed:

| Description | Options | Buttons |
| --- | --- | --- |
| Vertical Stack | `paypal.Buttons({<br>  style: { layout: "vertical" },<br>  message: { amount: 100 }<br>})`<br>**Note:** The message is positioned to the top to make room for the text that accompanies the debit/credit Card button. | ![image](https://www.paypalobjects.com/ppdevdocs/paylater-payin4-100-vertical.png) |
| Horizontal Stack | `paypal.Buttons({<br>  style: { layout: "horizontal" },<br>  message: { amount: 100 }<br>})` | ![image](https://www.paypalobjects.com/ppdevdocs/paylater-payin4-horizontal-two%20button-100.png) |
| Standalone PayPal | `paypal.Buttons({<br>  fundingSource: paypal.FUNDING.PAYPAL,<br>  message: { amount: 20 }<br>})` | ![image](https://www.paypalobjects.com/ppdevdocs/paypal-standalone-non-paylater.png.png) |
| Standalone Pay Later | `paypal.Buttons({<br>  fundingSource: paypal.FUNDING.PAYLATER,<br>  message: { amount: 100 }<br>})` | ![image](https://www.paypalobjects.com/ppdevdocs/paylater-paylater-100-standalone.png) |

Learn more about standalone button integration best practices by reviewing the [Standalone Buttons](/docs/checkout/standard/customize/standalone-buttons/) page.

## Update the message amount

As the product count or cart total changes, you can update the `message.amount` to reflect the latest total.

```javascript
buttons.updateProps({
  message: {
    amount: 200, // Update to your cart or product total amount
    align: 'center',
    color: 'black',
  }
});
```

**info**
**Note:** Ensure that all previously specified message options are passed into `updateProps` including any options that have not changed; otherwise, they will be overwritten with default values.

## Complete your integration

Return to the [Set up standard payments](/docs/checkout/standard/) guide to create and capture the order.

## See also

### Pay Later messaging

Learn more about adding messaging next to your product price and cart totals by reviewing the [Pay Later Messages](/docs/checkout/pay-later/us/integrate/) page.

### Javascript SDK

Learn more about passing parameters to customize your integration by reviewing the [JavaScript SDK](/docs/checkout/advanced/customize/3d-secure/sdk/) page.