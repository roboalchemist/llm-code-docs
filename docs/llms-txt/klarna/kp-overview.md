# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md

# Klarna payments -Adobe Commerce

## Learn about the features offered by Klarna payments in the Klarna Adobe Commerce extension.

## Overview

The Klarna payments extension lets you add any of Klarna's payment methods to your checkout page in Adobe Commerce. The key features supported by Klarna payments in the extension are:

- Availability in all [markets](https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md) where Klarna is available
- All [payment methods](https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md) available in each market
- [Authorization callback](https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md)
- [Business to business (B2B)](https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md) purchases
- [Extra merchant data (EMD](https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md))
- [Merchant references](https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md)
- \[ Klarna payments GraphQL\]

The following features are currently not supported:

- [Recurring payments and tokenization](https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/subscriptions-and-on-demand)
- [Store views for multi-currency support](https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md)
- [Deferred Total Calculation](https://experienceleague.adobe.com/en/docs/commerce-operations/performance-best-practices/high-throughput-order-processing#deferred-total-calculation) - this Adobe Commerce feature is not currently supported for the Klarna payments integration, but will be reviewed in the future for support if reasonable.

For more information about Klarna payments, refer to the [dedicated section](https://docs.klarna.com/klarna-payments) of our product documentation. **Prerequisite**: When using the Klarna m2-klarna Adobe Commerce extension, for a direct integration of Klarna Payments, you will need a Klarna merchant account, for which you can [sign up here](https://klarna.com/signup).

## Markets

Klarna payments can be used in all markets where Klarna is available without any technical restrictions, including North America, Europe, and Oceania. For a detailed list of supported countries [here](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales.md). The store has to be configured to match the market's specifics, for example, the correct tax and currency settings. Once that’s configured, the Klarna payments API has to be configured in the Admin\> **Stores**\> **Configuration**\> **Sales**\> **Payment Methods**\> **Klarna**\> **General settings**.


![ Edit the shop's admin settings to enable Klarna payments](ZwamYIF3NbkBXFEU_ACGeneralsettings.jpeg)
*Edit the shop's admin settings to enable Klarna payments*

## Payment methods

The Klarna extension support all Klarna’s payment methods. Klarna handles the configuration of the payment methods within Klarna, so you don’t need to configure individual payment method settings in the shop or in the extension. You can also use Klarna payments in Adobe Commerce's Progressive Web Apps (PWA) environment. The extension’s configuration in PWA is the same as the configuration of Klarna payments in a non-Adobe Commerce PWA environment. However, an additional request must be sent to a specific endpoint in the extension in the PWA environment. [Learn more about Adobe Commerce's PWA environment](https://developer.adobe.com/commerce/pwa-studio/).

## Authorization callback

Introduced in [m2-klarna extension version 2.0.5](https://commercemarketplace.adobe.com/klarna-m2-klarna.html#product.info.details.release_notes) (released May 2023), the authorization callback supports server-side communication for the creation of Klarna payments orders, as client-side order creation may not be successful for all orders. While orders may still be created successfully for many orders via the client-side authorization (e.g. if the shop doesn't accept the server-side authorization callback), client-side order creation cannot cover all order scenarios fully, thus the server-side authorization callback is *required*to be able to successfully complete all order creation scenarios. For more about the Klarna Payments authorization callbacks, refer to the [Authorization callbacks article](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/other-actions/authorization-callback.md). The shop's web server must allow public access for Klarna to call the shop's authorization callback provided within the m2-klarna extension: **<https: %7bshop=""> url}/checkout/klarna/authorize?dryRun=true** It is important this request from Klarna can reach the shop's functional code for the authorization data to be processed; the request should not be blocked by security interceptors, e.g. CAPTCHA, Cloudfare, etc. You can confirm public access by calling the API by sending a POST request,e.g. with cURL. Any response other than the pattern of the example below means the endpoint is not accessible functionally. Even if the response is 200, if the response does not include the "message" param, the endpoint is not functional.

``` http
curl --request POST \
  --url 'https://{shop url}/checkout/klarna/authorize?dryRun=true' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json'
```

authorize dryRun request

``` http
{
  "code": 200
  "message": "The {full path to the url} is accessible.",
  "timestamp": {request timestamp}
}
```

authorize dryRun success response (with variable data bracketed)

## Business to business (B2B)

Klarna payments allows business to business (B2B) purchases. The following updates are required for B2B purchases to work:

1.  B2B must be enabled by Klarna for the Merchant ID (MID).
2.  You have to enable B2B in the Admin. You can find the configuration option in **Stores**\> **Configuration**\> **Sales**\> **Payment Methods**\> **Klarna**\> **Klarna Payments**.

Since currently there’s no supported Adobe Commerce standard selector for customers to flag the order as business to consumer (B2C) or B2B, an order is only considered a B2B one when a customer enters data in the **Company Name** billing address field.


![ You can enable B2B payments in the Klarna Payments settings in the Adobe Commerce Admin.](Zwam74F3NbkBXFGa_ACKlarnaPaymentsconfiguration.jpeg)
*You can enable B2B payments in the Klarna Payments settings in the Adobe Commerce Admin.*

## Extra merchant data (EMD)

In some cases, we require additional information regarding the customer and the purchase in order to make a correct risk assessment. This information, called Extra merchant data (EMD), may consist of data about the customer performing the transaction, the product/services associated with the transaction, or the seller and their affiliates. The following method returns the request instance, which is later converted to an array and sent as a request to Klarna:

``` php
\Klarna\Kp\Model\Api\Builder\Request::generateCreateSessionRequest()
\Klarna\Kp\Model\Api\Builder\Request::generateUpdateSessionRequest()
\Klarna\Kp\Model\Api\Builder\Request::generatePlaceOrderRequest()
```

It returns the instance `Klarna\Kp\Api\Data\RequestInterface` (`Klarna\Kp\Model\Api\Request`). To add EMD, create an [after plugin](https://developer.adobe.com/commerce/php/development/components/plugins/#after-methods) on this method. To insert the EMD in the request, use the `setAttachment` method on the request instance.

## Merchant references

To include [merchant_reference1](https://docs.klarna.com/api/payments/#operation/createOrder!path=merchant_reference1&t=request) and [merchant_reference2](https://docs.klarna.com/api/payments/#operation/createOrder!path=merchant_reference2&t=request) data fields, for example, to match the order's merchant references as included in Klarna's settlement files, you can create an [after plugin](https://developer.adobe.com/commerce/php/development/components/plugins/#after-methods) for the \Klarna\Kp\Model\Api\Builder\Nodes\MerchantReferences::addToRequest() method.

## Configuration

You can quickly enable Klarna payments in the Admin by changing a few settings. Before proceeding, make sure you have your \[ API credentials set up\].

### Steps to configure Klarna payments

To configure Klarna payments in the Klarna extension, follow these steps:

1.  In the Adobe Commerce Admin, go to **Stores**\> **Configuration**\> **Sales**\> **Payment Methods**\> **Klarna**\> **General Settings**
2.  Expand the **Klarna Payments** section and set **Enable** to *Yes*.

4\. If your Klarna account supports business to business (B2B) payments, set **Enable B2B** to *Yes*. Note the following:

- Since currently there’s no supported Adobe Commerce standard selector for customers to flag the order as business to consumer (B2C) or B2B, an order is only considered a B2B one when a customer enters data in the **Company Name** billing address field.
- Your Merchant ID (MID) has to be enabled for B2B by Klarna. This option is currently available only is selected regions.

## Multiple step checkout

If you customize checkout to consist of multiple steps or pages and offer payment methods that pull funds directly from the customer, for example, a direct bank transfer, you have to appropriately customize the Klarna payments integration to finalize the authorization, as covered in the [authorization guide](https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md).

## GraphQL checkouts

Headless e-commerce architecture is based on a headless content management system (CMS) that stores, manages, and delivers content without a front end and only through an API. On a headless platform, the front end (or the head) has been decoupled and removed, leaving only the back end. Back-end developers use APIs to deliver things like products, blog posts, or customer reviews. Front-end developers work on how to present that content using any framework they desire. GraphQL is a query language developers can use to retrieve data from a server. Adobe Commerce uses GraphQL as an alternative way of retrieving front-end information. For more information about GraphQL, refer to the [GraphQL checkout tutorial](https://devdocs.magento.com/guides/v2.3/graphql/tutorials/checkout/index.html).

### Workflow

Klarna payments requires cart information to initiate the payment session. For this reason, the below steps can be executed only after a cart has been created. Please follow Adobe's [GraphQL checkout tutorial](https://devdocs.magento.com/guides/v2.4/graphql/tutorials/checkout/index.html) to create a cart.

1.  The Progressive Web App (PWA) client calls the [`createKlarnaPaymentsSession`](https://devdocs.magento.com/guides/v2.4/graphql/mutations/create-klarna-payments-session.html) mutation to generate the `client_token` and retrieve a list of `payment_categories`.This step can be executed at any time after the cart is created. However, we recommend that you add products to the cart and set the billing address, shipping address, and shipping method on the cart before you perform this step.
2.  Adobe Commerce forwards the request to Klarna.
3.  Klarna returns the `client_token` and the `payment_categories` available to the customer.
4.  Adobe Commerce forwards the token to the client.
5.  The client sends the cart query to retrieve the available payment methods.
6.  Adobe Commerce must always retrieve the latest status information from Klarna before returning the Klarna payments method as an option to the customer. This is important to ensure that the latest available payment options are always shown to the customer.
7.  Klarna returns an updated list of `payment_categories`.
8.  Adobe Commerce returns all available payment methods, including Klarna payment methods.
9.  The PWA client renders the Klarna payment widget.The PWA client uses the `client_token` and `payment_categories` to initialize the [Klarna payments JavaScript SDK](https://docs.klarna.com/payments/web-payments/additional-resources/klarna-payments-sdk-reference.md).
10. The PWA client sends the [authorization](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-2-checkout.md) directly to Klarna.On the checkout page, the customer selects Klarna as the payment method and clicks **Place Order**. When this happens, the PWA client must send the `authorize()` call to Klarna. Then, the customer follows the authorization steps on the Klarna inline modal. During this phase, the communication between the PWA client and Klarna is handled directly by the Klarna Payments JS SDK.
11. Klarna returns the `authorization_token` in response to the authorize call. Note: that [Klarna m2-klarna extension flow is built to handle Klarna sharing the authorization_token either (or both) via client side or server side calls](https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/kp-overview.md), but the Klarna authorization callback can be optional for graphQL with [PPP-1503 (v3.1.1+](https://commercemarketplace.adobe.com/klarna-m2-klarna.html#product.info.details.release_notes))
12. Set the payment method providing the `authorization_token` as part of the [`setPaymentMethodOnCart`](https://devdocs.magento.com/guides/v2.4/graphql/mutations/set-payment-method.html) mutation.The client uses the [`setPaymentMethodOnCart`](https://devdocs.magento.com/guides/v2.4/graphql/mutations/set-payment-method.html) mutation to set the payment method to `klarna_`<identifier-value>. The `authorization_token` is passed in the klarna object.
13. Adobe Commerce returns an updated cart object.
14. The PWA client runs the [`placeOrder`](https://developer.adobe.com/commerce/webapi/graphql/schema/cart/mutations/place-order/) mutation.
15. Adobe Commerce sends the place order request to Klarna.
16. Klarna sends the response to Adobe Commerce.
17. Adobe Commerce creates an order and sends an order ID in response to the [`placeOrder`](https://developer.adobe.com/commerce/webapi/graphql/schema/cart/mutations/place-order/) mutation.

{{#mermaid:
sequenceDiagram
autonumber
participant A as Client
participant B as Adobe Commerce
participant C as Klarna Payments
alt Initialization
A ->> B: Run the createKlarnaPaymentsSession mutation
B ->> C: Adobe Commerce forwards the request
C ->>B: Klarna returns the client_token and payment_categories
B ->>A: Adobe Commerce forwards the response
else Widget rendering
A ->>B: Get available payment methods
B ->>C: Get latest status
C ->>B: Klarna returns latest status
B ->>A: Available payment methods
A ->>A: PWA renders KP widget
else Authorization
A ->>C: PWA client sends the authorize() directly to Klarna
C ->>A: Klarna returns the authorization_token
else Set payment method on created
A ->>B: Set the payment method providing the authorization_token
B ->>A: Adobe Commerce returns an updated Cart Object
else Place order
A ->>B: Run the placeOrder mutation
B ->>C: Adobe Commerce sends the place order request to Klarna
C ->>B: Klarna sends the response to Adobe Commerce
B ->>A: Adobe Commerce creates the order
end
}}

### Cart updates

During the purchase flow, the cart can be updated by adding additional products, applying coupons, and changing the billing or shipping address. All these events might cause a change in Klarna options for the specific customer. In order to always present customers with the latest available payment options provided by Klarna, the PWA client must:

1.  Perform a cart update.
2.  Adobe Commerce returns an updated cart object.
3.  Send the cart query to retrieve the latest available payment methods.
4.  Adobe Commerce sends another request to Klarna with the latest information available from the cart.
5.  Klarna returns a new list of payment methods. Note that the list might contain different options for the customer.
6.  Adobe Commerce returns an updated cart object.
7.  [Reload the widget](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-2-checkout.md) on the client side.

{{#mermaid:
sequenceDiagram
autonumber
participant A as Client
participant B as Adobe Commerce
participant C as Klarna Payments
alt Cart Update
A ->> B: Perform cart update (e.g. add product, apply coupon...)
B ->> A: Adobe Commerce returns an updated Cart Object
else Widget reloading
A ->>B: Get available payment methods
B ->>C: Get latest status
C ->>B: Klarna returns latest status
B ->>A: Available payment methods
A ->>A: PWA renders KP widget
end
}} When you set the payment method to Klarna in the [`setPaymentMethodOnCart`](https://devdocs.magento.com/guides/v2.4/graphql/mutations/set-payment-method.html) mutation, the payment_method object must contain a klarna object.

#### Examples

The following example shows the [`setPaymentMethodOnCart`](https://devdocs.magento.com/guides/v2.4/graphql/mutations/set-payment-method.html) mutation constructed for the Klarna payment method. **Request**

``` null
mutation {
  setPaymentMethodOnCart(input: {
    cart_id: "3WxC8gQn4Fbo55yqVLSiUFJ9fmEwnlxG"
    payment_method: {
      code: "klarna_pay_later"
      klarna: {
        authorization_token: "e9abc610-6748-256f-a506-355626551326"
      }
    }
  }) {
  cart {
    selected_payment_method {
      code
    }
  }
}
```

A sample `setPaymentMethodOnCart` mutation for the Klarna payment method. **Response**

``` null
{
  "data": {
    "setPaymentMethodOnCart": {
     "cart": {
       "selected_payment_method": {
         "code": "klarna_pay_later"
        }
      }
    }
  }
}
```

A sample response to the `setPaymentMethodOnCart` mutation.</identifier-value></https:>