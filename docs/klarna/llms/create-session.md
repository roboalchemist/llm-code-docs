# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/api-documentation/create-session.md

# Create session with Hosted Payment Page - API Details

When you have created a *Payment Session* with the *Payment Provider*’s API, you will be able to create an **HPP Session**. This *HPP Session* will let you show the Payment Provider’s interface to the Consumer without any iframe integration on your website. The HPP Session is deeply linked to the *Payment Session*, both Sessions will have a tied lifecycle meaning that the *HPP Session* will expire 1 hour before the *Payment Session*, see session lifetime. Additionally, when the *Payment Session* status is updated, *HPP Session*’s one is too. Multiple *HPP Sessions*can be linked to the same *KP Session*if you need to have multiple customization at the same time, although it is considered as a bad practice. This is not the case with a*KCO Order*and may lead to unexpected behaviors. All the customization of the appearance of the Hosted Payment Page is done in this call, see ourcustomization guide.

| **Description** | **Creates a session with HPP-API** |
|----|----|
| Reference | For a full explanation of required and accepted (optional) parameters, check HPP Create Session Options below. |
| Url structure | <https:></https:><environment-domain>/hpp/v1/sessions |
| Example | curl -X POST <https: api.playground.klarna.com="" hpp="" sessions="" v1=""> --header "Authorization: Basic <token> " --header "Content-Type: application/json" --header “Cache-Control: no-cache” --data “<parameters>” |

## Examples

### Request for Klarna Payments (KP)

``` json
{
    "payment_session_url": "https://<environment-domain>/payments/v1/sessions/<kp_session_id>",
    "merchant_urls": {
        "success": "https://example.com/success?token=<random_uuid>&sid={{session_id}}&authorization_token={{authorization_token}}",
        "cancel": "https://example.com/cancel?token=<random_uuid>&sid={{session_id}}",
        "back": "https://example.com/back?token=<random_uuid>&sid={{session_id}}",
        "failure": "https://example.com/fail?token=<random_uuid>&sid={{session_id}}",
        "error": "https://example.com/error?token=<random_uuid>&sid={{session_id}}"
    }
}
```

### Request for Klarna Payments (KP) with Place Order

``` json
{
    "payment_session_url": "https://<environment-domain>/payments/v1/sessions/<kp_session_id>",
    "merchant_urls": {
        "success": "https://example.com/success?token=<random_uuid>&sid={{session_id}}ℴ_id={{order_id}}",
        "cancel": "https://example.com/cancel?token=<random_uuid>&sid={{session_id}}",
        "back": "https://example.com/back?token=<random_uuid>&sid={{session_id}}",
        "failure": "https://example.com/fail?token=<random_uuid>&sid={{session_id}}",
        "error": "https://example.com/error?token=<random_uuid>&sid={{session_id}}"
    },
    "options": {
      "place_order_mode": "PLACE_ORDER"
    }
}
```

### HPP Session Creation Response

``` json
{
    "session_id": "<hpp_session_id>",
    "redirect_url": "https://pay.klarna.com/eu/hpp/payments/2OCkffK",
    "session_url": "https://api.klarna.com/hpp/v1/sessions/<hpp_session_id>",
    "qr_code_url": "https://pay.klarna.com/eu/hpp/payments/<hpp_session_id>/qr",
    "distribution_url": "https://api.klarna.com/hpp/v1/sessions/<hpp_session_id>/distribution",
    "expires_at": "2019-05-29T08:22:05.563Z",
    "distribution_module": {
      "token": "<distribution_token>",
      "standalone_url": "https://pay.klarna.com/eu/hpp/distributions/<distribution_id>?profile_id={{profile_id}}&view_id={{view_id}}",
      "generation_url": "https://api.playground.klarna.com/hpp/v1/sessions/<hpp_session_id>/distribution-module/token"
    }
}
```

The integration layer should use the URLs sent back in the create session call when interacting with the HPP Session as the structure of the URLs may change. Do not recreate URLs by generating a made up structure.

## How to create the Request

### Payment Session URL

After creating the **KP Session** or **KCO Order** you need to compute the corresponding URL to one of them. To do so, simply use the URL that you are using to access them via API.

| Payment Provider | URL Structure |
|----|----|
| Klarna Payments | <https:></https:><environment-domain>/payments/v1/sessions/<kp_session_id> |

Exact domain names for environments and regions can be found in our environments and testing guidelines.

### Merchants URLs

Merchant URLs are used to redirect the Consumer’s browser to your website after a successful payment, a rejection or a cancellation by the Consumer. When you let success, cancel or failure empty or null, the Consumer will be shown a generic action confirmation page. See our customization guide to get to see how these pages look like. When error is empty or null, the failure definition will be used. On all of these links you can use placeholders to get more context on the transaction, for example the  tag will be replaced by the identifier of the HPP Session.

| **Name** | **Requirement** | **Usage** |
|----|----|----|
| success | Optional | Consumer will get redirected there after a successful authorization of payment for both KP and KCO. When using KP as Payment Provider, a place holder will be required to get the KP Authorization Token to place the order. |
| cancel | Optional | Consumer will get redirected there when clicking on the cancellation button. *[See back button versus cancel button chapter](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/before-you-start/distribute-session/#cancel-and-back-what-are-the-differences).* |
| back | Optional | Consumer will get redirected there when clicking on the back button. *[See back button versus cancel button chapter.](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/before-you-start/distribute-session/#cancel-and-back-what-are-the-differences)* |
| failure | Optional | Consumer will get redirected there when payment is refused by Klarna. If an error occurs and noerrorURL was given, then the consumer will also get redirect to this URL. |
| error | Optional | Consumer will get redirected there when an error occurred in the flow. If this parameter is not set and afailureURL is present, the Consumer will get redirected there. |
| status_update | Optional | Url that will be used for callbacks. [Learn more about callbacks](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/status-callbacks/). |

| Tag | Place holder usage |
|---|------------------|
|  | The identifier of the HPP Session. |
|  | Authorization token to use to place the order with KP API. This placeholder works only for KP as Payment Provider in a success URL. |
|  | Order identifier to use to handle post-purchase experience. This placeholder works only for KCO or when usingplace_order_modewith KP as Payment Provider. |

### Branding Customization

You can use optional parameters to customize the look and feel of the Hosted Payment Page to better match your own brand. Please refer to our customization page. All customization parameters are described in our customization guide for the Hosted Payment Page.

### Payment provider specific parameters

#### Klarna Payments

The **Klarna Payments** integration has some specific parameters that you can pass to the HPP Session creation call to better configure what the consumer will see. Please read our KP integration guide.

## How to interpret the Response

The *HPP Session* is created on a successful response. It contains different URLs that you may use to interact with depending on the way you intend to distribute the *Payment Page*. It is recommended to use these links directly and to avoid recreating them in your backend as the way they are defined may change without notice.

| Field Key | Type | Description |
|---------|----|-----------|
| session_id | String | Generated identifier for the Session, referenced as HPP Session ID afterwards. |
| session_url | API Endpoint URL | Use this URL to read the HPP Session you just created. This endpoint requires Merchant Credentials to accept requests. |
| distribution_url | API Endpoint URL | Use this URL to distribute to your Consumer the HPP Session you just created by Email or SMS. Learn more in the [distribution of the HPP Session chapter](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/distribute-session/) . This endpoint requires Merchant Credentials to accept requests. |
| redirect_url | Public URL | Use this URL to redirect directly the Consumer’s browser to the Payment Page or the HPP Session you just created. Learn more in the [distribution of the HPP Session chapter](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/distribute-session/) . |
| qr_code_url | Public URL | Use this URL to display a QR Code to your Consumer, so that they will access the Payment Page or the HPP Session you just created by scanning it with their phone. Learn more in the [distribution of the HPP Session chapter](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/distribute-session/) . |
| expires_at | Date | Date when this session will not be able for the consumer to pay anymore. You can read more about lifetime in our [session lifetime article](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/#hpp-session-session-lifetime) . [Dates format is described here](https://docs.klarna.com/api/api-urls/#data-types) . |
| distribution_module | Object containing following fields: * token * standalone_url * generation_url | Distribution module data |</kp_session_id></environment-domain></hpp_session_id></distribution_id></distribution_token></hpp_session_id></hpp_session_id></hpp_session_id></hpp_session_id></random_uuid></random_uuid></random_uuid></random_uuid></random_uuid></kp_session_id></environment-domain></random_uuid></random_uuid></random_uuid></random_uuid></random_uuid></kp_session_id></environment-domain></parameters></token></https:></environment-domain>