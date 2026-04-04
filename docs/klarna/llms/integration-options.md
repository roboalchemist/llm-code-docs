# Source: https://docs.klarna.com/payments/after-payments/order-management/before-you-start/integration-options.md

# Integration options

## Now that you're ready to use Order management, learn the different integration options.

Get a glimpse of the options you have to access Order management and perform different actions on your orders.

If you have yet to decide which is the best integration option for your business, see the [Touchpoints section.](https://docs.klarna.com/payments/after-payments/order-management/before-you-start/what-is-order-management/#touchpoints)

## Order management API

The Order management API consists of endpoints for handling an order after your customer has completed the purchase. Use the API to perform all actions related to managing your orders.

### Authentication

Order management API uses HTTP basic authentication. To authenticate, use your [API credentials](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/settings/) that consist of:

- a username linked to your Merchant ID at Klarna
- a password associated with your username

You can use the same set of credentials for multiple Klarna APIs, including Order management and Klarna payments.

If you're using an API platform to store your credentials, you can add them in relevant fields. Otherwise, ensure to include the Base64-encoded *username:password* in the Authorization header field of each API request, as shown below.

``` http
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

*Authorization request header with Base64-encoded credentials.*

## Merchant portal

The [Merchant portal](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/merchant-portal-user-guide/) is an alternative way of managing orders through a user interface.

For more details about the Merchant portal and API credentials, see the \[ Before you start section.\]

## Platform solutions

You can also use Order management if your online store runs on a third-party platform, such as Shopify or Magento.

For more information about third-party integrations, see the [Platform solutions documentation.](https://docs.klarna.com/platform-solutions/)