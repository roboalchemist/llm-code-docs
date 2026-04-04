# Flitt Documentation

Source: https://docs.flitt.com/llms-full.txt

---

# Payment API reference

> Flitt payment API Reference.

# Home page. Explore the methods to integrate Flitt

Flitt Payment API Reference

# Flitt Payment API Documentation. Explore the methods to integrate Flitt

- ## **How to start & Testing**

  ______________________________________________________________________

  **Start** integration and **testing** without registration. Create payments using test data and determine which type of integration suits you best.

  [Getting started](/getting-started/get-started/)

- ## **Redirect**

  ______________________________________________________________________

  **Redirect** is a good option if you want the customer to see all payment methods on a single Flitt-hosted page.

  [Redirect](/getting-started/redirect)

- ## **Embedded**

  ______________________________________________________________________

  Integrate **Embedded** checkout if you want the customer to have a seamless process without redirections.

  [Embedded](/getting-started/embedded/)

- ## **Direct**

  ______________________________________________________________________

  Use the **Direct** integration type if bank cards need to be process on your [PCI compliant](/pcidss-compliance/) backend.

  [Direct](/getting-started/direct)

- ## **Apple Pay**

  ______________________________________________________________________

  **Apple Pay** integration for in-app purchases and on the web.

  [Apple Pay](/api/applepay-getting-started/)

- ## **Google Pay**

  ______________________________________________________________________

  **Google Pay** integration for in-app purchases and on the web.

  [Google Pay](/api/googlepay-getting-started/)

- ## **CMS&CRM plugins**

  ______________________________________________________________________

  We created ready to use **CMS&CRM plugins** for any CMS or CRM or Site builder you need. Just download and install the plugin for your site.

- ## **Subscription & Recurring**

  ______________________________________________________________________

  Manage **Subscription & Recurring** with any tools, provided in API, SDK&Mobile, CMS&CRM plugins and Landing pages.

- ## **Withdrawal**

  ______________________________________________________________________

  **Withdrawal** is a card payout which credits funds to a card previously participated in a debit transaction.
# API Reference

# Apple Pay direct integration

Direct integration can be done in two ways

1. [Using decrypted PAN (DPAN)](/api/applepay-direct/#using-decrypted-pan-dpan)
1. [Using encrypted payment data](/api/applepay-direct/#using-encrypted-payment-data)

Both types of integration require [Apple Pay API](https://developer.apple.com/documentation/applepayontheweb) to be implemented by merchant.

## Using decrypted PAN (DPAN)

Integration with DPAN assumes that [Payment Data Cryptography](https://developer.apple.com/documentation/PassKit/payment-token-format-reference#Verify-the-signature-and-decrypt-the-payment-data) is performed on merchant side.

To create order using DPAN, merchant needs to use [create order with direct](/api/create-order-direct/) method.

While the [parameters](/api/order-parameters-direct/) are still as described, the parameters which are related to card data should contain information from Apple Pay decrypted payment data:

Apple Pay DPAN data parameters

| Parameters    | Type         | Mandatory | Description                                                                                                                                                                                         |
| ------------- | ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `card_number` | string(19)   | optional  | `applicationPrimaryAccountNumber` from Apple Pay `data` object                                                                                                                                      |
| `expiry_date` | string(4)    | optional  | DPAN expiry date in format MMYY                                                                                                                                                                     |
| `cavv`        | string(2048) | optional  | Apple Pay one-time `onlinePaymentCryptogram` from `data.paymentData` dictionary                                                                                                                     |
| `eci`         | string(2048) | optional  | Apple Pay `eciIndicator` from `data.paymentData` dictionary                                                                                                                                         |
| `wallet`      | string(2048) | optional  | Wallet type: `applepay`                                                                                                                                                                             |
| `schemeid`    | string(2048) | optional  | Visa/MasterCard identifier of CIT - client initiated transaction, returned in initial purchase in field `additional_info->schemeid`, see [response parameters](/api/order-parameters/#__tabbed_2_2) |

see [response parameters](/api/order-parameters/#__tabbed_1_2)

Pay attention

**Apple Pay and 3DSecure**

3DSecure authentication is never triggered for Apple Pay payments on Flitt side

Pay attention

**Recurring payments with Apple Pay**

Flitt supports recurring payments for Apple Pay.

Depending on the parameters which are sent during [order creation](/api/create-order-direct/), order is considered as CIT (client initiated transaction) or MIT (merchant initiated transaction)

CIT: `cavv` is mandatory, `schemeid` must not be present

MIT: `schemeid` is mandatory, `cavv` must not be present

Examples

**Request example of client initiated transaction:**

```
{
  "request": {
    "order_id": "test_12343242",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "amount": 1000,
    "currency": "GEL",
    "card_number": "4111111111111111",
    "cavv": "AEH2lSgIQ9/OAALA1DWsGgADFA==",
    "eci": "05",
    "wallet": "applelepay",
    "expiry_date": "1135",
    "client_ip": "8.8.8.8",
    "server_callback_url": "https://myserver.com/callback",
    "signature": "0c0c2374c73267e7be560d80834e4ba28ccda7aa"
  }
}

```

**Request example of merchant initiated transaction:**

```
{
  "request": {
    "order_id": "test_12343243",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "amount": 1000,
    "currency": "GEL",
    "card_number": "4111111111111111",
    "schemeid":"885056510569385"
    "eci": "05",
    "wallet": "applelepay",
    "expiry_date": "1135",
    "client_ip": "8.8.8.8",
    "server_callback_url": "https://myserver.com/callback",
    "signature": "0c0c2374c73267e7be560d80834e4ba28ccda7aa"
  }
}

```

## Using encrypted payment data

Integration with encrypted payment data assumes that [Payment Data](https://developer.apple.com/documentation/PassKit/payment-token-format-reference#Payment-token-structure) obtained from Apple Pay is not decrypted on merchant side.

Instead of that, `container` parameter must be transferred with method [create order with direct](/api/create-order-direct/) to Flitt.

While the [parameters](/api/order-parameters-direct/) are still as described, the parameters `card_number`, `expiry_date`, `cavv`, `eci`, `wallet` , `schemeid` which are related to card data must be replaced with `container` parameter.

Apple Pay request example with container

```
{
  "request": {
    "amount": "100",
    "currency": "GEL",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "order_id": "test_12343244",
    "sender_email": "inga.abashidze123@gmail.com",
    "container": "ewogICJ0b2tlbiI6IHsKICAgICJwYXltZW50TWV0aG9kIjogewogICAgICAibmV0d29yayI6ICJNYXN0ZXJDYXJkIiwKICAgICAgInR5cGUiOiAiQ3JlZGl0IiwKICAgICAgImRpc3BsYXlOYW1lIjogIk1hc3RlckNhcmQgMzA0MSIKICAgIH0sCiAgICAidHJhbnNhY3Rpb25JZGVudGlmaWVyIjogIjIzYTJmMGZjYjYxODU1OTQ4NDNjMzA4N2NhNmUzOTFlZmE0NGE2ZjZmMjcyMzMzYzdhMmFlOWI5NDEyMzc4NTUiLAogICAgInBheW1lbnREYXRhIjogewogICAgICAiZGF0YSI6ICI2dzRrUjF0dDdVNTE5Li4udlV6KzBRb3RSTGRtOWVsdi9LTFNIdVBhMWc4RXpoOWREY0Z5OEZIQ05NTDY5bGNjb3BaVHc5NC9Qa1pyN2l4ZVh0ZXIxOHFkQXl1SnNHVnY4ZWdmTWlSQjMrd09Hb3NIcSIsCiAgICAgICJzaWduYXR1cmUiOiAiTUlBR0NTcUdTSWIzRFFFSEFxQ0FNSUFDQVFFeEQuLi5HMnVTd0NJRURIbS9aTzJmQXFEUmV6b3J5cGhKd1BjSnBRa0xweU4xSVEvRy9wSDRhMUFBQUFBQUFBIiwKICAgICAgImhlYWRlciI6IHsKICAgICAgICAicHVibGljS2V5SGFzaCI6ICJMWm94YVZBU2h2cFFLa0owLi4uWTNJYkNrMVlRZmFnV1dRPSIsCiAgICAgICAgImVwaGVtZXJhbFB1YmxpY0tleSI6ICJNRmt3RXdZSEtvWkl6ajBDLi5pU3piazV1dUUvZzFWRkNoZz09IiwKICAgICAgICAidHJhbnNhY3Rpb25JZCI6ICIyM2EyZjBmY2I2MTg1NTk0OC4uMzkxZWZhNDRhNmY2ZjI3MjMzM2M3YTJhZTliOTQxMjM3ODU1IgogICAgICB9LAogICAgICAidmVyc2lvbiI6ICJFQ192MSIKICAgIH0KICB9Cn0=",
    "signature": "fc30eee74814ad64bfbc153f8f9f1387821beb57"
  }
}

```

where `container` is BASE64 encoded JSON object which have next structure:

Apple Pay container structure

```
{
  "token": {
    "paymentMethod": {
      "network": "MasterCard",
      "type": "Credit",
      "displayName": "MasterCard 3041"
    },
    "transactionIdentifier": "23a2f0fcb6185594843c3087ca6e391efa44a6f6f272333c7a2ae9b941237855",
    "paymentData": {
      "data": "6w4kR1tt7U519...vUz+0QotRLdm9elv/KLSHuPa1g8Ezh9dDcFy8FHCNML69lccopZTw94/PkZr7ixeXter18qdAyuJsGVv8egfMiRB3+wOGosHq",
      "signature": "MIAGCSqGSIb3DQEHAqCAMIACAQExD...G2uSwCIEDHm/ZO2fAqDRezoryphJwPcJpQkLpyN1IQ/G/pH4a1AAAAAAAA",
      "header": {
        "publicKeyHash": "LZoxaVAShvpQKkJ0...Y3IbCk1YQfagWWQ=",
        "ephemeralPublicKey": "MFkwEwYHKoZIzj0C..iSzbk5uuE/g1VFChg==",
        "transactionId": "23a2f0fcb61855948..391efa44a6f6f272333c7a2ae9b941237855"
      },
      "version": "EC_v1"
    }
  }
}

```

# Apple Pay integration instructions

## Integrations

Apple Pay payments from Flitt are available both for web and mobile.

Apple Pay on web can be integrated with several options:

- with [redirect](/getting-started/redirect/) to Flitt payment page
- with Apple Pay button [embedded](/api/embedded-custom/#example-applepaygooglepay-buttons) into your website
- directly with [Apple Pay API](https://developer.apple.com/documentation/apple_pay_on_the_web/).

Apple Pay in mobile application can be integrated with Flitt SDK depending on the programming language or framework:

- [Objective-C](/api/mobile/ios/)
- [Swift](/api/mobile/ios-swift/)
- [React Native](/api/mobile/apple-reactnative/)
- [Flutter](/api/mobile/apple-flutter/)
- [in web-view with JavaScript](/api/mobile/apple-webview/)

## Steps for mobile

### Create payment

To start accept payments in your mobile application, first you need to create payment in Flitt.

This is usually done on mobile application backend.

Before you start integration of Apple Pay on mobile, you will need to [Register Apple Merchant ID](/api/applepay-getting-started/#register-apple-merchant-id) and [Create Apple Pay certificates](/api/applepay-getting-started/#create-new-apple-pay-certificates).

Follow instructions bellow.

### Register Apple Merchant ID

Register Apple Merchant ID following the instruction [register merchant ID](https://developer.apple.com/documentation/passkit/apple_pay/setting_up_apple_pay_requirements) at Apple Developer site.

Fill out the form with a description and identifier. Your description is for your own needs and may be changed in the future (we recommend using the name of your mobile application). The identifier must be unique (in all Apple applications, not just yours) and cannot be changed later (although you can always create another). We recommend using merchant.flitt.com.{{Your_app_name}}. Keep this value for future reference when developing the application.

Detailed instruction:

- Go to the Dashboard of your account in Apple Developer <https://developer.apple.com/account/#>

- Open menu [Identifiers](https://developer.apple.com/account/resources/identifiers/list)

- click `Identifiers +` to create Merchant ID: <https://developer.apple.com/account/resources/identifiers/add/bundleId>

- in Register a new identifier choose to register `Merchant IDs`

- Fill out Description and Identifier (merchant.flitt.com.{{your_app_bundle_id}}.):

### Create new Apple Pay certificates

You need to add the certificates to your application to encrypt payment data. To do this, follow 3 steps:

- Use [Keychain Access](https://developer.apple.com/help/account/create-certificates/create-a-certificate-signing-request) on Mac to generate Certificate Signing Request files.

  On other platforms you can use **openssl** commands:

  **Apple Merchant Identity Certificate:**

  ```
  openssl genrsa -out merchant.key 2048
  openssl req -new -key merchant.key -out merchant.csr

  ```

  **Apple Processing Certificate:**

  ```
  openssl ecparam -out processing.key -name prime256v1 -genkey
  openssl req -new -sha256 -key processing.key -nodes -out processing.csr

  ```

- Use these CSR files to generate certificates

  section **Apple Pay Payment Processing Certificate:**

  section **Apple Pay Merchant Identity Certificate:**

- Download and send obtained certificates to Flitt support.

# Apple Pay integration instructions for web

Integrating Apple Pay into a website can be done either through:

- [Redirect method](/getting-started/redirect/)
- [simple embedded with Vue.js](/api/embedded-custom/#example-of-apple-pay-and-google-pay-buttons)
- [advanced embedded with JavaScript](/sdk-and-mobile/sdk/wallets/)
- Directly with [Apple Pay API](https://developer.apple.com/documentation/apple_pay_on_the_web/).

Redirect and embedded methods require integration only with Flitt's API or SDK and thus less coding and complexity.

Integrating Apple Pay with Apple Pay API directly requires additional Apple certificates management and encryption/decryption procedures coding.

Direct method also involves different approaches depending on tokenized Primary Account Number (DPAN) or an encrypted payment container is used during payment flow processing.

## Apple Pay with redirect to Flitt checkout page

Refer to [create order](/api/create-order/) to create order on your backend or frontend and redirect payer to the checkout page. Apple Pay button will automatically appear at checkout page. The payment is processed on Flittâs secure platform, reducing complex coding and the risk of handling sensitive data.

## Apple Pay button, embedded to merchant website

Embedded method provides a seamless checkout experience without leaving the merchant website, which can increase conversion rate.

Apple Pay can be embedded in two methods.

**Method with vue.js**

Simple: embedded with [Vue.js](/api/embedded-custom/#example-of-apple-pay-and-google-pay-buttons). This is the easiest way which require less code development.

**Example vue.js Apple Pay button:**

See the Pen [Flitt - Apple, Google Pay buttons](https://codepen.io/flitt/pen/PorvvEw) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

**Method with JavaScript**

Refer to [advanced embedded with JavaScript](/sdk-and-mobile/sdk/wallets/) document to get instruction on how to implement it. This method provide more control on Apple Pay button behavior and is more flexible if you need to implement additional logic during button display and user click.

**Verify your domain in Apple Pay developer account**

- To embedd Apple Pay button from Flitt, you must register all of your web domains where button will be displayed. This relates to top-level domains (for example, site.com) and subdomains (for example, shop.site.com, www.site.com), both production and development sites.
- Request Flitt support for `apple-developer-merchantid-domain-association.txt` file.
- When received, place that file at https://example.com/.well-known/apple-developer-merchantid-domain-association where `example.com` is your domain or subdomain.
- Tell Flitt to activate your domain with Apple.

## Direct integration with Apple Pay API with decrypted card token

1 [Configur Your Apple Pay Environment](https://developer.apple.com/documentation/apple_pay_on_the_web/configuring_your_environment)

1.1 Configure Merchant ID and Certificates

1.2 Register and Verify Your Domain

2 Integrate [Apple Payment Request API](https://developer.apple.com/documentation/apple_pay_on_the_web/payment_request_api)

2.1 Show Apple Pay Buttons on you site. See [Apple reference](https://developer.apple.com/documentation/applepayjs/displaying_apple_pay_buttons)

2.2 [Construct a PaymentRequest](https://webkit.org/blog/8182/introducing-the-payment-request-api-for-apple-pay/) with parameters:

configuration example

```
const applePayMethod = {
  supportedMethods: "https://apple.com/apple-pay",
  data: {
      version: 3,
      merchantIdentifier: "merchant.com.example",
      merchantCapabilities: ["supports3DS", "supportsCredit", "supportsDebit"],
      supportedNetworks: ["masterCard", "visa"],
      countryCode: "GE",
  },
};

```

where `merchant.com.example` is your Apple Merchant ID from step 1.1

3 Acquire a payment session from Apple with [merchant validation](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/providing_merchant_validation) process. This should be done on your backend as oposit to all other steps, done on frontend.

4 Handle Payment Authorization

5 Obtain PaymentResponse and related [ApplePayPayment](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypayment) dictionary

6 Extract [token](https://developer.apple.com/documentation/passkit_apple_pay_and_wallet/pkpayment/1619239-token) from ApplePayPayment

7 Decrypt [paymentData](https://developer.apple.com/documentation/passkit_apple_pay_and_wallet/apple_pay/payment_token_format_reference)

After decryption the result format should be as follows:

```
{
  "applicationPrimaryAccountNumber": "",
  "applicationExpirationDate": "",
  "currencyCode": "",
  "transactionAmount": ,
  "deviceManufacturerIdentifier": "",
  "paymentDataType": "",
  "paymentData": {
    "onlinePaymentCryptogram": ""
  }
}

```

8 Send parameters to Flitt [Payment (direct)](/api/order-parameters-direct/) request

Apple Pay parameter `applicationPrimaryAccountNumber` as Flitt `card_number`

Apple Pay parameter `applicationExpirationDate` as Flitt `expiry_date`

Apple Pay parameter `onlinePaymentCryptogram` as Flitt `cavv`

and additionally Flitt parameter `wallet` = `applepay`

Example Apple Pay request to Flitt

```
{
  "request": {
    "order_id": "Order_id123",
    "merchant_id": 1549901,
    "order_desc": "Apple Pay Payment with card token",
    "amount": 1000,
    "currency": "GEL",
    "client_ip": "2.2.2.2",
    "server_callback_url": "https://server.com/callback",
    "preauth": "Y",
    "version": "1.0.1",
    "card_number": "4444555566661111",
    "expiry_date": "0527",
    "cavv": "AEBBjhMvE4xRAg97n9DpAoABFA==",
    "wallet": "applepay"
    "signature": "64d565cdf9bfb2ad556eac54bd57706e5dc6c412",
  }
}

```

# Signature generation for request and response

## Signature algorithm

Parameter `signature` in [create order](/api/create-order/) request and response and in [callbacks](/api/callbacks/) is generated with `sha1` function. `sha1` is applied to the string, which contains merchant payment secret key and all request or response parameters, concatenated in alphabetic order and separated by `|` symbol.

Example

Merchant request:

```
curl -i -X POST \
-H "Content-Type:application/json" \
-d \
'{
"request": {
"server_callback_url": "http://myshop/callback/",
"order_id": "TestOrder2",
"currency": "GEL",
"merchant_id": 1549901,
"order_desc": "Test payment",
"amount": 1000,
"signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
}
}' \
'https://pay.flitt.com/api/checkout/url'

```

String used for signature build:

```
test|1000|GEL|1549901|Test payment|TestOrder2|http://myshop/callback/

```

Where `test` is payment secret key from [test data](/api/testing/)

If parameter is absent or is empty then there is no need to add `|` symbol.

Signature validation example for `response_url` and `server_callback_url` POST response:

```
namespace Ipsp;
/**
 * Class Signature
   * @package Ipsp
   */
class Signature {
      /**
       * @var
       */
      private static $password;
      /**
       * @var
       */
      private static $merchant;
      /**
       * Set merchant password
       * @param String $password
       * @return mixed
       */
      public static function password($password){
          self::$password = $password;
      }
      /**
       * Set merchant id
       * @param String $merchant
       * @return mixed
       */
      public static function merchant( $merchant ){
          self::$merchant = $merchant;
      }
      /**
       * Generate request params signature
       * @param array $params
       * @return string
       */
      public static function generate(Array $params){
          $params['merchant_id'] = self::$merchant;
          $params = array_filter($params,'strlen');
          ksort($params);
          $params = array_values($params);
          array_unshift( $params , self::$password );
          $params = join('|',$params);
          return(sha1($params));
      }
      /**
       * Sign params with signature
       * @param array $params
       * @return array
       */
      public static function sign(Array $params){
          if(array_key_exists('signature',$params)) return $params;
          $params['signature'] = self::generate($params);
          return $params;
      }
      /**
       * Clean array params
       * @param array $data
       * @return array
       */
      public static function clean(Array $data){
          if( array_key_exists('response_signature_string',$data) )
              unset( $data['response_signature_string'] );
          unset( $data['signature'] );
          return $data;
      }
      /**
       * Check response params signature
       * @param array $response
       * @return bool
       */
      public static function check(Array $response){
          if(!array_key_exists('signature',$response)) return FALSE;
          $signature = $response['signature'];
          $response  = self::clean($response);
          return $signature == self::generate($response);
      }
}

```

```
from hashlib import sha1

def get_signature(secret_key, params):
    """
    :param secret_key: merchant secret
    :param params: POST parameters
    :return: signature string
    """
    data = [secret_key]
    data.extend([str(params[key]) for key in sorted(iter(params.keys()))
                 if params[key] != '' and not params[key] is None
                 and key != 'signature'])
    return sha1('|'.join(data).encode('utf-8')).hexdigest()

```

## Solving problems with `signature` generation and validation

There are two typical cases when the `signature` parameter verification error occurs.

### Case 1: in response to Flitt API call

When request for the create order, reverse, get status or any other request with the parameter `signature` is sent from merchant to the Flitt API, and the response is returned:

```
    {
        "response": {
            "error_code": 1014,
            "error_message": "Invalid signature",
            "request_id": "3mwpcKoenYZ0w",
            "response_status": "failure"
        }
    }

```

If the request is sent to the Flitt API, and the response is returned as `"error_message": "Invalid signature"`, perform the following checks:

- check that you used the correct payment secret key from the Technical Settings menu in the [Merchant Portal](https://portal.flitt.com):
- if the request contains non-Latin encoding, then it is sent in encoding UTF-8
- make sure that a parameter with a value of 0 is not null by your programming language
- log the line in the program code to which you apply SHA1 during the generation of the signature parameter. Compare it with the string that returned in the error text (marked in red): ``` âInvalid signature signature: ``6bd069be8a6e2f2bbe176df00ba63cc681ca38aa``; response_signature_string: ``**********|125|GEL|1549901|demo order 789|Demo123456``â. ``` Note that in the text of the error the merchantâs payment key will be masked with `*` symbol
- check if you send empty parameters in the API request. If yes, then in the line that participates in the signature, the | separator symbol for each such empty parameter does not need to be included
- if you are developing with the PHP programming language, use the example function [`php-inline public static function generate(Array $params)`](/api/building-signature/#__tabbed_1_1):
- make sure that the result of the SHA1 function is lowercase. Correct: `6bd069be8a6e2f2bbe176df00ba63cc681ca38aa`. Incorrect: `6BD069BE8A6E2F2BBE176DF00BA63CC681CA38AA`
- make sure that the signature parameter is not included in your signature calculation
- make sure that if you use the API endpoint /api/recurring, then you only include the necessary parameters in the signature, but not those from the /api/redirect endpoint

### Case 2: in callback to `server_callback_url` or redirect to `response_url`

When the Flitt server returned a POST response or callback to `server_callback_url` or `response_url` and you try to generate own signature and compare it with the `signature` parameter from the POST response, the `signatures` do not match

If the Flitt API returned a POST response to the pages specified in the `server_callback_url` or `response_url` parameters, but when you try to generate a signature and compare it with the signature parameter in the POST response, the signature does not match

```
{
    "response": {
        "rrn": "",
        "masked_card": "",
        "sender_cell_phone": "",
        "sender_account": "",
        "currency": "GEL",
        "fee": "",
        "reversal_amount": "0",
        "settlement_amount": "0",
        "actual_amount": "",
        "response_description": "",
        "sender_email": "",
        "order_status": "expired",
        "response_status": "success",
        "order_time": "28.02.2018 19:18:16",
        "actual_currency": "",
        "order_id": "TestOrder2",
        "tran_type": "purchase",
        "eci": "",
        "settlement_date": "",
        "payment_system": "",
        "approval_code": "",
        "merchant_id": 1549901,
        "settlement_currency": "",
        "payment_id": 83456044,
        "card_bin": "",
        "response_code": "",
        "card_type": "",
        "amount": "1000",
        "signature": "268b8f189f97c85696134fe6ae0f7f5ab93f28d5",
        "product_id": "",
        "merchant_data": "",
        "rectoken": "",
        "rectoken_lifetime": "",
        "verification_status": "",
        "parent_order_id": "",
        "fee_oplata": "0",
        "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": null, \"transaction_id\": null, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": null, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": null, \"card_product\": null, \"card_category\": null, \"timeend\": \"01.03.2018 05:18:17\", \"ipaddress_v4\": \"52.30.149.20\", \"payment_method\": null}",
        "response_signature_string": "**********|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": null, \"transaction_id\": null, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": null, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": null, \"card_product\": null, \"card_category\": null, \"timeend\": \"01.03.2018 05:18:17\", \"ipaddress_v4\": \"52.30.149.20\", \"payment_method\": null}|1000|GEL|0|1549901|TestOrder2|expired|28.02.2018 19:18:16|83456044|success|0|0|purchase"
    }
}

```

To diagnose the cause of a signature mismatch, follow these steps:

- make sure that the parameter with a value of 0 is not brought to empty or null in your programming language
- make sure that the response_signature_string and signature parameters are not included in the signature calculation (the response_signature_string parameter is returned only if the merchant is in test mode and contains hint how the signature was formed in response)
- if the request contains non-Latin letters, then it is sent in UTF-8
- in the program code, pledge a line to which you apply SHA1 during the formation of the signature parameter. Compare it with the string that returned in the `response_signature_string` parameter
- check if empty parameters are returned in the response. If yes, then in the string which participates in the signature, it is not necessary to include the symbol separator | for each empty parameter
- make sure that the result of the SHA1 function is lowercase. Correct: `6bd069be8a6e2f2bbe176df00ba63cc681ca38aa`. Incorrect: `6BD069BE8A6E2F2BBE176DF00BA63CC681CA38AA`

# Receiving Callbacks

To receive callback responses from Flitt following server IP addresses must be allowed in the merchant site firewall:

`54.154.216.60, 3.75.125.89`

The callback is considered to be processed successfully by the merchant if HTTP 200 OK status returned.

Otherwise, Flitt will repeat callback attempts with such time intervals: 2, 60, 300, 600, 3600, 86400 seconds.

Callback will not follow redirects.

Other callback parameters are:

- Method: `POST`,

- Headers:

  `"Content-Type": ["application/json; charset=UTF-8"]`

  `"user-agent": ["Mozilla/5.0 (X11; Linux x86_64; Twisted) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"]`

- Timeout: `30` seconds

- Follow redirect: `NO`

Callback example

```
{
  "rrn": "111111111111",
  "masked_card": "444455XXXXXX1111",
  "sender_cell_phone": "",
  "sender_account": "",
  "currency": "GEL",
  "fee": "",
  "reversal_amount": "0",
  "settlement_amount": "0",
  "actual_amount": "200",
  "response_description": "",
  "sender_email": "test@test.com",
  "order_status": "approved",
  "response_status": "success",
  "order_time": "13.07.2024 01:23:59",
  "actual_currency": "GEL",
  "order_id": "test33694502191",
  "tran_type": "purchase",
  "eci": "5",
  "settlement_date": "",
  "payment_system": "card",
  "approval_code": "123456",
  "merchant_id": 1549901,
  "settlement_currency": "",
  "payment_id": 805243692,
  "card_bin": 444455,
  "response_code": "",
  "card_type": "VISA",
  "amount": "200",
  "signature": "b7884b5c4906956fbac4d20390388d913a78c0b0",
  "product_id": "",
  "merchant_data": "Test merchant data",
  "rectoken": "",
  "rectoken_lifetime": "",
  "verification_status": "",
  "parent_order_id": "",
  "fee_oplata": "0",
  "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_test\": true}",
  "response_signature_string": "**********|200|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_**********\": true}|200|123456|444455|VISA|GEL|5|0|444455XXXXXX1111|Test merchant data|1549901|**********33694502191|approved|13.07.2024 01:23:59|805243692|card|success|0|111111111111|**********@**********.com|0|purchase"
}

```

Subscription can be stopped or started.

In order to stop or start previously created subscription, send POST request:

Stop/start subscription

`POST /api/subscription`

Request parameters

| Parameters    | Type          | Mandatory | Description                                                                                                                                                                                               |
| ------------- | ------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `order_id`    | string(1024)  | mandatory | Order ID which is generated by merchant                                                                                                                                                                   |
| `merchant_id` | integer(12)   | mandatory | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                       |
| `signature`   | string(40)    | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) |
| `action`      | string(10000) | mandatory | `stop` or `start`                                                                                                                                                                                         |

| Parameters        | Type         | Description                                                                                                                                                                                                            |
| ----------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `order_id`        | string(1024) | Order ID which is generated by merchant.                                                                                                                                                                               |
| `merchant_id`     | integer(12)  | Merchant unique ID. Generated by Flitt during merchant registration.                                                                                                                                                   |
| `response_status` | string(50)   | Request processing status. If request did not pass validation then `failure`, else `success`                                                                                                                           |
| `signature`       | string(40)   | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response |
| `status`          | string(1024) | `disabled` or `active`                                                                                                                                                                                                 |

Example

Request:

```
curl -L 'https://pay.flitt.com/api/subscription' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "order_id": "test_subscription11",
    "merchant_id": 1549901,
    "action": "start",
    "signature": "a7adf395dae783a4676abbafe7f2479b2f6cfbca"
  }
}'

```

Response:

```
{
    "response": {
        "response_status": "success",
        "merchant_id": 1549901,
        "order_id": "test_subscription11",
        "status": "active",
        "signature": "a7adf395dae783a4676abbafe7f2479b2f6cfbca"
    }
}

```

Request:

```
curl -L 'https://pay.flitt.com/api/subscription' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "order_id": "test_subscription11",
    "merchant_id": 1549901,
    "action": "stop",
    "signature": "07736b7a2687b7429af7334f756ddcfb597456f1"
  }
}'

```

Response:

```
{
    "response": {
        "response_status": "success",
        "merchant_id": 1549901,
        "order_id": "test_subscription11",
        "status": "disabled",
        "signature": "07736b7a2687b7429af7334f756ddcfb597456f1"
    }
}

```

# Capture parameters

Request parameters

| Parameters    | Type         | Mandatory | Description                                                                                                                                                                                                            |
| ------------- | ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `version`     | string(10)   | optional  | Protocol version. Default value: 1.0.1 Version 1.0 is deprecated                                                                                                                                                       |
| `order_id`    | string(1024) | mandatory | Order ID which is generated by merchant                                                                                                                                                                                |
| `merchant_id` | integer(12)  | mandatory | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                                    |
| `amount`      | integer(12)  | mandatory | Order amount without separator                                                                                                                                                                                         |
| `currency`    | string(3)    | mandatory | Order currency. Supported values: EUR â Euro USD â US Dollar GBP â Pound sterling mandatory CZK â Czech Republic Koruna GEL - Georgian lari UZS - Uzbekistan sum [Full list of supported currencies](/api/currencies/) |
| `signature`   | string(40)   | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response |

| Parameters             | Type         | Description                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `order_id`             | string(1024) | Order ID which is generated by merchant.                                                                                                                                                                                                                                                                                                                         |
| `merchant_id`          | integer(12)  | Merchant unique ID. Generated by Flitt during merchant registration.                                                                                                                                                                                                                                                                                             |
| `capture_status`       | string(50)   | Capture operation status. Can contain the following values: `hold` â capture has been created, but not approved yet; merchant must continue to request the status of the order `captured` â capture completed successfully, funds are charged from the payerâs account and soon will be credited of the merchant; merchant can provide the service or ship goods |
| `response_status`      | string(50)   | Request processing status. If parameters sent by merchant did not pass validation then failure, else success                                                                                                                                                                                                                                                     |
| `response_code`        | integer(4)   | Capture decline response code. Possible codes see in Response codes                                                                                                                                                                                                                                                                                              |
| `response_description` | string(1024) | Capture response code description, see Response codes                                                                                                                                                                                                                                                                                                            |

Examples

```
{
  "request": {
    "version": "1.0.1",
    "order_id": "test_12343242113",
    "currency": "GEL",
    "merchant_id": 1549901,
    "amount": 100,
    "signature": "1efcb015c89da38977ae1e734aade413b95ca900"
  }
}

```

```
{
    "response": {
        "capture_status": "captured",
        "order_id": "test_12343242112",
        "response_description": "",
        "response_code": "",
        "merchant_id": 1549901,
        "response_status": "success"
    }
}

```

```
{
    "response": {
        "error_code": 1016,
        "error_message": "Merchant not found",
        "request_id": "Mfqk42OKu69BI",
        "response_status": "failure"
    }
}

```

Changelog

This changelog tracks all changes to Flitt API

## February 5, 2024

- Parameter `reservation_data` added for split payments to provide additional data about products for fiscalisation.

# Capture the order

Order can be captured fully or partially. Parameter `amount` must be passed in [capture request](../capture-parameters/#__tabbed_2_1) equal to [order](../order-parameters/#__tabbed_2_2) `actual_amount` value if full capture is required.

Pay attention

Multiple captures are not allowed.

## The correct sequence of steps for the capture operation

The capture operation is designed to charge the amount previously held on the card.

Hold must be done with [pre-payment request](../order-parameters/) with the parameter `preauth = Y` .

This payment flow is executed with two stages. The first stage is a payment operation with preliminary hold of the amount. The second stage is the capture of a held amount.

The capture can be performed both with full and partial amount.

Note

The pre-payment and capture operations are available only for the card payment method. The other payment methods do not support these operations and the full amount will be automatically charged according to the one-stage flow:

## Reverse of pre-payment

If the capture operation has not yet been completed, then acquiring fee is not charged for pre-payment and reverse operations.

Instant cancellation of the held amount takes place when reverse is performed for pre-payment.

If the capture operation has not yet been completed, then only reversal of the full holding amount is available. Partial reverse is not allowed for pre-payment.

If a partial capture operation is performed, the rest of the amount will be automatically returned to the payerâs card and reverse operation is no longer necessary.

Example

For example, if the pre-payment amount is 1000 and 200 amount should be reversed, then payment must be captured with amount 800.\
The rest of amount of 200 should not be reversed, otherwise the amount 200 will be reversed twice.

Only single full/partial capture is available for pre-payment operation. For a captured payment operation, several sequential partial reverses are available.

## Idempotent capture key

Capture operation does not require idempotent key as capture can be securely retried. When capture with the same `amount` is retried, current `capture_status` of the payment is returned.

### Endpoint for order capture

Capture the order

`POST /api/capture/order_id`

This endpoint expects `POST` request in `JSON` format with [parameters](/api/capture-parameters/#__tabbed_2_1).

Normal response will contain `capture_status` parameter which indicates if capture is successful or not.

Request and response examples

```
curl -L 'https://pay.flitt.com/api/capture/order_id' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "version": "1.0.1",
    "order_id": "test_12343242113",
    "currency": "GEL",
    "merchant_id": 1549901,
    "amount": 100,
    "signature": "1efcb015c89da38977ae1e734aade413b95ca900"
  }
}'

```

```
{
    "response": {
        "capture_status": "captured",
        "order_id": "test_12343242113",
        "response_description": "",
        "response_code": "",
        "merchant_id": 1549901,
        "response_status": "success"
    }
}

```

```
{
    "response": {
        "error_code": 1007,
        "error_message": "Parameter `signature` is incorrect",
        "request_id": "HGh7ami3WN0ci",
        "response_status": "failure"
    }
}

```

# Create order for PCIDSS merchants

These edpoints relate to the flow, when merchant is PCI DSS compliant and card data collected on behalf of merchant site or application.

Note

This flow will consist from two steps.

- Step 1: Obtain ACS URL from issuing bank and redirect caldholder to this URL for 3DSecure authentication.
- Step 2: Obtain result from ACS URL and perform financial transaction - purchase.

*Endpoint for order creation*

Step 1. Starting 3DSecure authentication

`POST /api/3dsecure_step1`

This endpoint expects `POST` request in `JSON` format with [parameters](/api/order-parameters/#__tabbed_1_1).

If the card is enrolled in 3D-Secure service, response will contain parameters:

| Parameter       | Type          | Description                                                                                |
| --------------- | ------------- | ------------------------------------------------------------------------------------------ |
| response_status | string(50)    | if no error ocured always returned success success                                         |
| acs_url         | string(2048)  | URL of cardholder issuing bank Access Control Server where he must enter 3DSecure password |
| pareq           | string(20480) | Parameter which must be submeted to acs_url                                                |
| md              | string(1024)  | Unique 3DSecure request ID. Generated by Flitt payment gateway                             |

A merchant receiving this response must build an HTML form and using it submit customer to acs_url. HTML form must be of the following content:

```
<form name="MPIform" action='${acs_url}' method="POST">
  <input type="hidden" name="PaReq" value='${pareq}'>
  <input type="hidden" name="MD" value='${md}'>
  <input type="hidden" name="TermUrl" value='${TermUrl}'>
</form>

```

where `${TermUrl}` â is merchant URL where customer will be redirected after 3DSecure authentication at `acs_url`.

The following parameters are returned to URL `TermUrl` after cardholder password verification:

| Parameter | Type          | Description                                                   |
| --------- | ------------- | ------------------------------------------------------------- |
| pares     | string(20480) | Payer authentication result.Is BASE64 string                  |
| md        | string(1024)  | Unique 3DSecure request ID.Generated by Flitt payment gateway |

Request and response examples

```
curl -i -X POST \
-H "Content-Type:application/json" \
-d \
'
{
  "request": {
    "order_id": "test_12343242",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "amount": 1000,
    "currency": "GEL",
    "card_number": "4444555566661111",
    "cvv2": "111",
    "expiry_date": "1125",
    "client_ip": "8.8.8.8",
    "server_callback_url": "https://myserver.com/callback",
    "signature": "0c0c2374c73267e7be560d80834e4ba28ccda7aa"
  }
}
' \
'https://pay.flitt.com/api/3dsecure_step1'

```

```
{
    "response": {
        "response_status": "success",
        "acs_url": "https://pay.flitt.com/test/testacs/",
        "pareq": "eJxtU21vgjAQ/u6vIP4A+gJRNKVJHUvUiRpwS/aRYYNsgljA6b8fLTpFuISE5+5pe/fcHdnsBOeOz8NScNrTKiMuz/Mg4lq8tfuDyqxRv46o6Jp5/HjHynfiIo8PKUU61DEBN9gkuVyEuyAtmm4VCsLjZLakpjUyDUTAFbZ5CRczhxpDDCsjoIZtWhoknC7Y5mM2Z762Zv6GaRO2fGMEqFD7RHgo00JcqIktAm6gTSvFnu6KIsvHQD6uysn1ffal708EyGizZNBdM1mX0p13ZXKOt9R12O/Th5ffn3jl/NgESEb73DYoOMUQmdDCloaGY4jGaECA8nconsgiKdYh1F7fvUrz2tFmZjJXdqVL1R8dHUqWQvA0vNDRUEp5Q20iP2eHlMtLCfj/f5KvWyfyMu2cobCopsFNVsZ8yhdHL1rNkedH0Ev8yLblVClCZyZx1W4DozqV+Ln3BDy+WKV1XwHZYrUttEdAY5f+AHcC0ak=",
        "md": "2001876637"
    }
}

```

Request and response examples

see [response parameters](/api/order-parameters/#__tabbed_1_2)

```
{
    "response": {
        "error_code": 1011,
        "error_message": "Parameter `amount` is missing",
        "request_id": "5htKi0wf7zEHn",
        "response_status": "failure"
    }
}

```

*Endpoint for 3DSecure authentication completion*

Step 2. Complete 3D-Secure authentication and perform purchase transaction

`POST /api/3dsecure_step2`

This endpoint expects `POST` request in `JSON` format with parameters:

| Parameter   | Type          | Mandatory | Description                                                                                                                                                                       |
| ----------- | ------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| merchant_id | integer(12)   | mandatory | Merchant unique ID. Generated by Flitt during merchant registration.                                                                                                              |
| order_id    | string(1024)  | mandatory | Order ID which is generated by merchant.                                                                                                                                          |
| pares       | string(20480) | mandatory | Parameter returned by issuing bank to URL TermUrl after password verification                                                                                                     |
| md          | string(1024)  | mandatory | Unique 3DSecure request ID. Generated by Flitt payment gateway                                                                                                                    |
| version     | string(10)    | optional  | Protocol version. Default value: 1.0                                                                                                                                              |
| signature   | string(40)    | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation](/api/building-signature/). |

Request

```
curl -i -X POST \
-H "Content-Type:application/json" \
-d \
'
{
    "request": {
        "order_id": "test_123432421",
        "merchant_id": "1549901",
        "pares": "eJzFWFuTosgSft9f0dH7aMxwF9lweqO4g4JcFXxDRO6Ccin01y/aPb093T3nTOzGiVMRhlZWVlZ+mfkVKfM/h7J46KNzk1bHb4/YV/TxITqG1T49xt8eXUf8Mnv88+m3uZOco4i3o7A7R0+/PYxjrkVNE8TRQ7r/9jilZhRGPz6v3FcNYEXNfQ2b0hhOEij1Zvmu8nLq03joV3yOfJ/+qKRF5zAJju2P4vtSEJ5YRX8iZwxJYHPkZfpRr4zOCv9E0Dg6jjnyPP3xFOTzY+ZGdxM30SdWh3T/pPEAvvvguhNjmhN+myM3jY/79kEbPeEoRqIzDHvAmD9I6g+MniN3+Uf1+uYBKKtu9A2/uf9W8FF9zM95zN/liaFnc+R19lExGurqGN2MzpHX3++C8jn6eR0cn9A3g6DJ6ehX8D51jvfJuW1avoU/vcHHx+zd5R/VmzZou+bJnyMvvz6BHPT9EwcAx15WciwtHNeKfNWPwMsYM3FX+SQGYfqEUiP+8ftzu6CIq3PaJuUtTD8K3sXqLdgxcrfqfyOw0/g4un+OHka6HZtvj0nb1n8gCITwKyS+VucYuVUngjLIqLBv0vj392y5mYj2yvFQ/WMbdztccKyOaRgU6TVoR75pUZtU+4dXYJ/ZdaybaQyxBO7LaPtLiJHHLzcJSmDUI/LJKa+Af8X8e7fPTfClSQLsU8tWdIhuRR09uJby7fH3n10vrxv4NI6a9p/48TMf3phdB0UXPRELlLTEgEh7ccMxxVmAV4rVYZDb5Fh9bzU/4kFeAb0vqb8z/kkp3IP7bNMmtwIakXDfxaqQIylGe+JF161w6vvu/lTn1K7tFwUhL69omYk+ikpldg2Wu1N74LFFutsryLK4YtOBF2pyEh8L8ULwkhyRlclhxoIk+ZnLxhKeu9oCUD6mnK1a9PEsmpb4AuoiOtuRp7A8E5dEKVUDWpku+26PbSGu0xd1ra0TObyyMit8e0b1xvkfkS2iy0e89xWPQhk+aIOfZOO2zEXnNj2MpT1epJqicGbGcSBoOM7kEi3wZsn14MUO0Nk4PyV5KjEQZYHpioAHE81sIGf6/No0JQGqa/cqmBogJYC5wrhbNnHx4m+sJLwKmgaqZ/mg8a5QuJo5g/zzXl6AWxh4ZuvjApSTUNccE2pXgI+acOUow+Yuy28y7FWWcWzGC0sN5He7bKJx67U2CA4w2FhfsyB2OEHvdxJz86HXrBiK8f08WYCMEmz21U4Su62sxW4pdj4eD7wDls97K4cVt6qLCsPyCtpnWeOoxbYOcSG2NxS69dTO96x6h1PJjmOdcY4HG71QBPEa4kwWbEQ02DCdZgHIx99x7sd9OhpKBaop0kEDqMTZJ8lWdgRvCre4gjF8OuA5NjUXbGzyzWXay37aH3DzSAWLaOEuVxolT2JmpUTyShDqNg6HlPQGGSEbYgVbJPV5w7AHsafAubxOsIkIpS2bTpzEWoTbNZzsG3lKdMZ65eYyLx3JXWTgcmC154tDePTpqDlJ5snx4biO3JNSY7OtZTipry/9rCeQU2vvKds8TU1vCEU6iI284HDHNhUemIB9j4l9xsQCTR6pVBesoRQmV+nVFqdbftvOWGkj+cFuYVwEQQKcZ1CUh3WEPisErKdLkXZKVKdMI8YIeMkZf8dWK6REOOew8s1eViUmnCIYSuETT2pdQu30Iq13ZOKIOslP8+mWWbqljSDmGmlRwh8MkaVtouW6zpNyV0FLVD3kxaF23d2qhbAsk3aOvGfGr/PneB35E6cxgMpYgooK9CSUkDFXsGU+i40mgIG7AvW5xnwHFGvnTc0sxprhfU9NtpJ41UwIuWf5UoC6aa/NN/WuOZzM1nsOu+xwBtVY0uMdAdV4DeoZQHXev+pYNcqUu2zk0ncZNLJPeMSD1SsX0BFEKea+pw08Dxbf+QAwVl3zgnHDddsLBk261fZyoye/WN/2DOad6IpkHgRpYC8nFjVdB/kV68Znji+eEKHy1OvShihog80Mi+SOSy7RjPZiXjK8DghctVtYWF3RWVn2tI6Vp6oY9su2BRW1UM4bJlrp0wkyIWyyVfJucT5Npuulcxlsqi1peZQRazleBZ1/2gK45wZbPCmdmDVdljQTzxt6yHYV1cDn+q5IKb1jY++Y93xsbljWtqMVAup+jyi+USUgljFlL9h6jSx4Ft7iJduaEDjsMR6vCp0hD65uWkfytKIbO/PaeiPvLToNRKEWFGh+dq/9ej4sDcy+50O558NT+x1hj3c6Tw1uQ5RKX2+uQLv7ZWkC64y3uSkjP+Uu13os2rcFOjFdt5eloprFJw5mWQL5ZR3ga6spgq5ZSO2M3BRG6qGOjLOnoUSupXFhM/3YeRtJLk1yEYvlKUDtSMTAwUB8AmwiQQVTtYoyanaU0OQ85cLVbjhzEwg0y+CVYimvJhRmXrJaFxmZm+T4dDe4Qb1t8PUGwevQmNJla8oXL/XNf8Pdyrlx9/Q3d42jaF8jP50Uu/8nd7WrO2jij9x9kf2PasWE8fb+fFYX1VZJ+lAHd8xghIaCsf7V8XHOgoVE79PgzJsxRrtZ2atBI4t2tkmM/Y5BmNrb9huw6EIGnk4ZTxx7dwonndr6injSyd7jJllORzm5Fumsz3mRsFD0cJSLKVytu8PVLERAT0yv3jia1OymlwtMPA2ud+Fq1mFkKK2RYUKtI5g78Xlt7U7bYuUpZVQUer/BDo1Kyam9Psiz6FKAWGMBkLI4UO7Y5FvvYaErlvUFUc8JImFMjJUOaUV3w0KP8MLfY3KnajK481yBVq1JEfhPupVr52Y2ZvPf9EWWAHn4vV9I7n1RWDL9Xnlfj/DulwBNURupDA4f8iU+50sASrTdtp55Ktix5Q7wOC2lvEKCJe5vxrYoQcmLs5hkkF7lKuJu9gCL6Zmr5hRydlQGp2gmrahzUy5lbz3pNuF0c54q4ooEhyE1+4m0QYyxm6s7kqlmUc9cnN4PqmbmGeR1765Iq/FYyJx9q7MNctXj7WqxMKpypS6DnU2N1VdwVZfTNIkMzq3X/a/8fVb52NfOkQ+d8JvO+eUFDPLyBubpt/Hv59v3M38BUoNF+A==",
        "md": "2003330322",
        "signature": "32b08ca114659b8c18ab9576cf1d5ffdb9c711f2"
    }
}
' \
'https://pay.flitt.com/api/3dsecure_step2'

```

see [response parameters](/api/order-parameters/#__tabbed_1_2)

```
{
    "response": {
        "error_code": 1011,
        "error_message": "Parameter `amount` is missing",
        "request_id": "5htKi0wf7zEHn",
        "response_status": "failure"
    }
}

```

Withdrawal can be performed only after initial purchase with the `rectoken` which will be referencing the purchase.

## Step 1. Create purchase

To create purchase, refer to any of the ways to start accepting payments:

- [create order with redirect](/api/create-order/)
- [create order with direct](/api/create-order-direct/)
- [embedded checkout](/api/embedded-custom/)
- [SDK](/sdk-and-mobile/sdk/about-sdk/)
- [CRM&CMS](/no-code/cms-plugins/)
- [Apple Pay](/api/applepay-web/)
- [Google Pay](/api/googlepay-web/)

Additional parameter must be sent during purchase [order creation](/api/create-order/) to obtain `rectoken` in response:

| Parameter           | Value | Description                                                           |
| ------------------- | ----- | --------------------------------------------------------------------- |
| `required_rectoken` | `Y`   | Flag which indicates whether card token will be returned in response. |

## Step 2. Create a withdrawal that references the purchase

*Endpoint for withdrawal creation*

Withdrawal operation

`POST /api/p2pcredit`

This endpoint expects `POST` request in `JSON` format with [parameters](/api/create-order-p2pcredit/#__tabbed_1_1).

Request parameters

One of the parameters `receiver_rectoken` or `external_rectoken` is mandatoiry!

| Parameters            | Type         | Mandatory | Description                                                                                                                                                                                                            |
| --------------------- | ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `version`             | string(10)   | optional  | Protocol version. Default value: 1.0.1 Version 1.0 is deprecated                                                                                                                                                       |
| `order_id`            | string(1024) | mandatory | Order ID which is generated by merchant                                                                                                                                                                                |
| `merchant_id`         | integer(12)  | mandatory | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                                    |
| `order_desc`          | string(1024) | mandatory | Order description. Generated by merchant in UTF-8 always                                                                                                                                                               |
| `amount`              | integer(12)  | mandatory | Order amount without separator. 1020 (GEL) means 10 lari and 20 tetri                                                                                                                                                  |
| `currency`            | string(3)    | mandatory | Order currency. Supported values: EUR â Euro USD â US Dollar GBP â Pound sterling mandatory CZK â Czech Republic Koruna GEL - Georgian lari UZS - Uzbekistan sum [Full list of supported currencies](/api/currencies/) |
| `server_callback_url` | string(2048) | optional  | Merchant site URL, where host-to-host callback will be sent after payment completion. See [Callbacks](/api/callbacks) for more details on callbacks.                                                                   |
| `signature`           | string(40)   | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response |
| `merchant_data`       | string(2048) | optional  | Any arbitrary set of data that a merchant wants to get back in the response to `response_url` or/and `server_callback_url`, and also in reports                                                                        |
| `product_id`          | string(1024) | optional  | Merchant product or service id                                                                                                                                                                                         |
| `receiver_rectoken`   | string(40)   | optional  | Card token from initial purchase operation, returned by Flitt in parameter `rectoken`                                                                                                                                  |
| `external_rectoken`   | string(40)   | optional  | Card token from initial purchase operation, returned by UFC in parameter `TRANSACTION_ID`                                                                                                                              |

see [response parameters](/api/order-parameters/#__tabbed_1_2)

Examples

**Request example with Flitt token:**

```
{
  "request": {
    "order_id": "test_1234312142",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "amount": 1000,
    "currency": "GEL",
    "receiver_rectoken": "I0wh7fBmFIdcY6K3Px2QugVrVR65sPafeZkPmRanOiRnXG",
    "server_callback_url": "https://myserver.com/callback",
    "signature": "51e59ffd263d071da8e1a1fc10b981f459dbe6f1"
  }
}

```

**Request example with UFC token:**

```
{
  "request": {
    "order_id": "test_12343242",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "amount": 1000,
    "currency": "GEL",
    "external_rectoken": "bAt6JLX52DUbibbzD9gDFl5Ppr4=",
    "server_callback_url": "https://myserver.com/callback",
    "signature": "1c1c2374c73267e7be560d80834e4ba28ccda9aa"
  }
}

```

**Normal final response:** see [list of test cards](/api/testing/)

```
{
  "response": {
    "product_id": "",
    "masked_card": "444455XXXXXX6666",
    "currency": "GEL",
    "response_description": "",
    "order_status": "approved",
    "response_status": "success",
    "order_time": "21.09.2024 01:22:02",
    "order_id": "test_1234312142",
    "tran_type": "p2p credit",
    "payment_system": "card",
    "approval_code": "",
    "merchant_id": 1549901,
    "payment_id": 818990350,
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "1000",
    "signature": "e7e8b3641dab8eee546e8183b9180e67f1568deb",
    "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": null, \"transaction_id\": 2019043606, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"21.09.2024 01:22:03\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"is_test\": true}"
  }
}

```

**Response in case of error:**

```
{
  "response": {
    "error_code": 1002,
    "error_message": "Application error",
    "request_id": "ghfIuTtVrbWYY",
    "response_status": "failure"
  }
}

```

# Create recurring order with saved card

*Endpoint for order creation*

Flitt host-to-host enpoint

`POST /api/recurring`

This endpoint expects `POST` request in `JSON` format with [request parameters](/api/order-parameters-recurring/#__tabbed_1_1).

Normal response will contain [response parameters](/api/order-parameters/#__tabbed_2_2).

Request is always executed as host-to-host and response is returned in the context of the same request.

Redirect and 3DSecure flows are not available for this enpoint.

If 3DSecure flow is required, follow [payment direct](/api/order-parameters-direct/) specifications.

Request and response examples

```
curl -L 'https://pay.flitt.com/api/recurring/' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "order_id": "test_recurring_payment123",
    "order_desc": "Debit by token transaction",
    "currency": "GEL",
    "amount": "4600",
    "rectoken": "I0wh7fBmFIdcY6K3Px2QugVrVR65sPafeZkPmRanOiRnXG",
    "signature": "34cda2e7a60c5aee343515fde5deef5403f87f86",
    "merchant_id": "1549901"
  }
}'

```

```
{
    "response": {
        "rrn": "332518927710",
        "masked_card": "444455XXXXXX6666",
        "sender_cell_phone": "",
        "sender_account": "",
        "currency": "GEL",
        "fee": "",
        "reversal_amount": "0",
        "settlement_amount": "0",
        "actual_amount": "4600",
        "response_description": "",
        "sender_email": "",
        "order_status": "approved",
        "response_status": "success",
        "order_time": "09.10.2024 21:20:46",
        "actual_currency": "GEL",
        "order_id": "test_recurring_payment123",
        "tran_type": "purchase",
        "eci": "7",
        "settlement_date": "",
        "payment_system": "card",
        "approval_code": "418900",
        "merchant_id": 1549901,
        "settlement_currency": "",
        "payment_id": 822895805,
        "card_bin": 444455,
        "response_code": "",
        "card_type": "VISA",
        "amount": "4600",
        "signature": "bb62bd1236695ba6f2252d1cec18ce04d2005559",
        "product_id": "",
        "merchant_data": "",
        "rectoken": "I0wh7fBmFIdcY6K3Px2QugVrVR65sPafeZkPmRanOiRnXG",
        "rectoken_lifetime": "",
        "verification_status": "",
        "parent_order_id": "",
        "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": null, \"transaction_id\": 2025817355, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"09.10.2024 21:20:47\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"is_test\": true, \"schemeid\": \"mBS8MDuWOpyhdw8aveS\"}",
        "response_signature_string": "**********|4600|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": null, \"transaction_id\": 2025817355, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"09.10.2024 21:20:47\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"is_**********\": true, \"schemeid\": \"mBS8MDuWOpyhdw8aveS\"}|4600|418900|444455|VISA|GEL|7|444455XXXXXX6666|1549901|**********_recurring_payment123|approved|09.10.2024 21:20:46|822895805|card|I0wh7fBmFIdcY6K3Px2QugVrVR65sPafeZkPmRanOiRnXG|success|0|332518927710|0|purchase"
    }
}

```

```
{
    "response": {
        "error_code": 1016,
        "error_message": "Merchant not found",
        "request_id": "3bplo0AeRPxlP",
        "response_status": "failure"
    }
}

```

# Create order

Create order - it actually were most of the integrations start off.

*Endpoints for order creation*

## Flitt hosted checkout page with checkout url

Flitt hosted checkout page with checkout url

`POST /api/checkout/url`

This endpoint expects `POST` request in `JSON` format with [parameters](/api/order-parameters/#__tabbed_1_1).

Normal response will contain `checkout_url` parameter - the URL of checkout page where payer should be redirected.

Request and response examples

```
curl -i -X POST \
-H "Content-Type:application/json" \
-d \
'{
"request": {
"server_callback_url": "http://myshop/callback/",
"order_id": "TestOrder2",
"currency": "GEL",
"merchant_id": 1549901,
"order_desc": "Test payment",
"amount": 1000,
"signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
}
}' \
'https://pay.flitt.com/api/checkout/url'

```

```
{
    "response":{
        "response_status":"success",
        "checkout_url":"https://pay.flitt.com/merchants/5ad6b888f4becb0c33d543d54e57d86c/default/index.html?token=8a09f9d937f43ad6fb40d6b40282d7277a48582a"
    }
}

```

```
{
    "response":{
        "response_status":"failure",
        "error_message":"Parameter `amount` is mandatory",
        "error_code":"1008"
    }
}

```

## Merchant embedded checkout page with payment token

This endpoint is preferred to be used for mobile application which process:

- [Apple Pay](/api/applepay-getting-started/)
- [Google Pay](/api/googlepay-getting-started/)
- [Mobile card form](/sdk-and-mobile/sdk/about-sdk/)
- [JavaScript SDK](/sdk-and-mobile/sdk/js/)

Merchant embedded checkout page with payment token

`POST /api/checkout/token`

This endpoint expects `POST` request in `JSON` format with [parameters](/api/order-parameters/#__tabbed_1_1) similar to `/api/checkout/url/` endpoint.

The difference is that normal response will contain `token` parameter - the payment token, which can be further used in JavaScript and mobile SDKs.

Request and response examples

```
curl -i -X POST \
-H "Content-Type:application/json" \
-d \
'{
"request": {
"server_callback_url": "http://myshop/callback/",
"order_id": "TestOrder2",
"currency": "GEL",
"merchant_id": 1549901,
"order_desc": "Test payment",
"amount": 1000,
"signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
}
}' \
'https://pay.flitt.com/api/checkout/token'

```

```
{
    "response": {
        "token": "9f0124be2b72333fb0e809f82c8f7e4eaeb6ec6e",
        "response_status": "success"
    }
}

```

```
{
    "response":{
        "response_status":"failure",
        "error_message":"Parameter `amount` is mandatory",
        "error_code":"1008"
    }
}

```

## Flitt hosted checkout page with redirect

Flitt hosted checkout page with redirect

`POST /api/checkout/redirect`

This endpoint expects `POST` request wit HTML form with [parameters](/api/order-parameters/#__tabbed_1_1).

Normal response will contain HTTP code `302 Found` and `Location` url where payer will be automaticaly redirected by his browser.

In case of error, `/api/checkout/redirect` page will contain html content with Request ID, 4-digit 2XXX error code and error localized description.

Request and response examples

```
<form method="POST" action="https://pay.flitt.com/api/checkout/redirect">
    <input type="text" class="form-input" id="order_id" name="order_id" value="test8651190566">
    <input type="text" class="form-input" id="merchant_id" name="merchant_id" value="1549901">
    <input type="text" class="form-input" id="order_desc" name="order_desc" value="Test order">
    <input type="text" class="form-input" id="amount" name="amount" value="200">
    <input type="text" class="form-input" id="currency" name="currency" value="GEL">
    <input type="text" class="form-input" id="response_url" name="response_url" value="https://site.com/test/responsepage/">
    <input type="text" class="form-input" id="signature" name="signature" value="31c758a76a5dae87f087df171092684130a12bf3">
    <button type="submit">Pay</button>
</form>

```

```
Request URL: https://api.flitt.com/api/checkout/redirect/
Request Method: POST
Status Code: 302 Found
Location: https://pay.flitt.com/merchants/5ad6b888f4becb0c33d543d54e57d86c/default/index.html?token=8a09f9d937f43ad6fb40d6b40282d7277a48582a

```

Code

```
$ curl -L 'https://pay.flitt.com/api/checkout/url' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "version": "1.0.1",
    "order_id": "test_order_id_132412412",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test order",
    "amount": 10025,
    "response_url": "https://example.com/thankyoupage",
    "server_callback_url": "https://example.com/api/callback",
    "signature": "7f52380cefaf3cb793746e2deeb56cf7cd75d532"
  }
}'

```

response:

```
{
  "response": {
    "checkout_url": "https://pay.flitt.com/merchants/5ad6b888f4becb0c33d543d54e57d86c/default/index.html?token=03fb1c589f8fcabc80f609c70af541fc636df112",
    "payment_id": "805230052",
    "response_status": "success"
  }
}

```

**Composer installation**

```
composer require flittpayments/php-sdk

```

**Manual installation**

```
git clone -b master https://github.com/flittpayments/php-sdk.git

```

**Simple Start**

```
require 'vendor/autoload.php';
\Flitt\Configuration::setMerchantId(1549901);
\Flitt\Configuration::setSecretKey('test');

$checkoutData = [
    'currency' => 'GEL',
    'amount' => 1000
];
$data = \Flitt\Checkout::url($data);
$url = $data->getUrl();
//$data->toCheckout() - redirect to checkout

```

**Example**

```
cd ~/php-sdk
php -S localhost:8000

```

[Checkout example](https://github.com/flittpayments/php-sdk/tree/master/examples)

**Simple Start** Include checkout.js file

```
<script src="https://pay.flitt.com/latest/checkout-vue/checkout.js"></script>

```

Add CSS:

```
<link rel="preload" href="https://pay.flitt.com/latest/checkout-vue/checkout.css" as="style">
<link href="https://pay.flitt.com/latest/checkout-vue/checkout.css" rel="stylesheet">

```

HTML congtainer:

```
<div id="checkout-container"></div>

```

JavaScript code:

```
var Options = {
  options: {
    methods: ["card"],
    methods_disabled: [],
    card_icons: ["mastercard", "visa"],
    theme: {
      type: "light",
      preset: "reset"
    }
  },
  params: {
    merchant_id: 1549901,
    currency: "GEL",
    amount: 500,
    order_desc: "Demo order"
  },
  css_variable: {
    main: '#7d8ff8',
    card_bg: '#353535',
    card_shadow: '#9ADBE8'
  }
};
checkout("#checkout-container", Options);

```

**1.Installation**

**Node** If youâre using [Npm](https://npmjs.com/) in your project, you can add @flittpayments/js-sdk dependency to package.json with following command:

```
npm i --save @flittpayments/js-sdk

```

or add dependency manually:

```
{
  "dependency": {
    "@flittpayments/js-sdk":"^2.0"
  }
}

```

**Manual installation** If you do not use NodeJS, you can download the latest release. Or clone from GitHub the latest developer version

```
git clone git@github.com:flittpayments/js-sdk.git

```

**Quick start**

```
<script src="https://cdn.jsdelivr.net/npm/@flittpayments/js-sdk"></script>

```

**2. Develop html card form using your own design.**

**Basic template**

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  </head>
  <body>
    <script src="https://cdn.jsdelivr.net/npm/@flittpayments/js-sdk"></script>
    <script>
    $checkout('Api').scope(function(){
        this.request('api.checkout.form','request', { Parameters } ).done(function(model){
            model.sendResponse();
            console.log(model.attr('order'));
        }).fail(function(model){
            console.log(model.attr('error'));
        });
    });
    </script>
  </body>
</html>

```

Basic template example: <https://github.com/flittpayments/js-sdk#basic-template>

**3. Create order using Integration Schema C for JavaScript SDK.**

Add parameters `required_rectoken=Y` and `server_callback_url` in your request to obtain recurring token (if you are planning recurring payments) in server callback (`rectoken` parameter).

```
curl -i -X POST \
-H "Content-Type:application/json" \
-d \
'{
"request": {
"server_callback_url": "http://myshop/callback/",
"order_id": "TestOrder2",
"currency": "GEL",
"merchant_id": 1549901,
"order_desc": "Test payment",
"amount": 1000,
"signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
}
}' \
'https://pay.flitt.com/api/checkout/token'

```

Documentation: https://docs.flitt.com/docs/page/3/?la=en#chapter-3-6-c. Save host-to-host token parameter from response.

**4. Load host-to-host token from step 3 in your card details form.**

```
{
 "payment_system":"card",
 "token":"host-to-host generated token",
 "card_number":"16/19-digits number",
 "expiry_date":"Supported formats: MM/YY, MM/YYYY, MMYY, MMYYYY",
 "cvv2":"3-digits number"
 }

```

from card form to payment gateway using JavaScript API $checkout('Api'). https://github.com/flittpayments/js-sdk#host-to-host-token

**5. Use .on('success') and .on('error') JavaScript callbacks to get result on payment processing.**

success â order is approved and amount will be charged error â order is declined and amount will not be charged

model.attr('error.message') will contain localized error message in case of payment decline. Order information on order status and details will be returned in model.data.order.order_data

JavaScript callback example:

```
console.log('success',JSON.stringify(model.attr("order").order_data));

```

```
{
  "response": {
    "rrn": "111111111111",
    "masked_card": "444455XXXXXX1111",
    "sender_cell_phone": "",
    "sender_account": "",
    "currency": "GEL",
    "fee": "",
    "reversal_amount": "0",
    "settlement_amount": "0",
    "actual_amount": "200",
    "response_description": "",
    "sender_email": "test@test.com",
    "order_status": "approved",
    "response_status": "success",
    "order_time": "13.07.2024 01:23:59",
    "actual_currency": "GEL",
    "order_id": "test33694502191",
    "tran_type": "purchase",
    "eci": "5",
    "settlement_date": "",
    "payment_system": "card",
    "approval_code": "123456",
    "merchant_id": 1549901,
    "settlement_currency": "",
    "payment_id": 805243692,
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "200",
    "signature": "b7884b5c4906956fbac4d20390388d913a78c0b0",
    "product_id": "",
    "merchant_data": "Test merchant data",
    "rectoken": "",
    "rectoken_lifetime": "",
    "verification_status": "",
    "parent_order_id": "",
    "fee_oplata": "0",
    "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_test\": true}",
    "response_signature_string": "**********|200|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_**********\": true}|200|123456|444455|VISA|GEL|5|0|444455XXXXXX1111|Test merchant data|1549901|**********33694502191|approved|13.07.2024 01:23:59|805243692|card|success|0|111111111111|**********@**********.com|0|purchase"
  }
}

```

Example: <https://jsfiddle.net/flitt/on8ydsgq/1/>

**6. Process final response received as server callbacks to `server_callback_url`.**

Format of final response: [Response](/api/order-parameters/#__tabbed_1_2)

**Installation** SDK availble on [NuGet](https://www.nuget.org/packages/FlittSDK/)

**Simple start**

```
using FlittSDK;
using FlittSDK.Checkout;

Config.MerchantId = 1549901;
Config.SecretKey = "test";

var req = new CheckoutRequest {
  order_id = Guid.NewGuid().ToString("N"),
  amount = 100000,
  order_desc = "checkout json demo",
  currency = "GEL"
};
var resp = new Url().Post(req);
if (resp.Error == null) {
 string url = resp.checkout_url;
}

```

To check example: you can use build-in ISS server <http://localhost:7777/>

**Installation**

```
npm install @flittpayments/flitt-node-js-sdk

```

**Manual installation**

```
git clone -b master https://github.com/flittpayments/node-js-sdk.git

```

**Simple start**

```
const FlittPay = require('@flittpayments/flitt-node-js-sdk')

const flitt = new FlittPay(
  {
    merchantId: 1549901,
    secretKey: 'test'
  }
)
const requestData = {
  order_id: 'Your Order Id',
  order_desc: 'test order',
  currency: 'GEL',
  amount: '1000'
}
flitt.Checkout(requestData).then(data => {
  console.log(data)
}).catch((error) => {
  console.log(error)
})

```

[Example checkout](https://github.com/flittpayments/node-js-sdk/tree/master/examples)

**Installation**

```
pip install flittpayments

```

**Simple start**

```
from flittpayments import Api, Checkout
api = Api(merchant_id=1549901,
          secret_key='test')
checkout = Checkout(api=api)
data = {
    "currency": "USD",
    "amount": 10000
}
url = checkout.url(data).get('checkout_url')

```

# Reverse the order

Order can be reversed fully or partially. Parameter `amount` must be passed in [reverse request](../reversal-parameters/#__tabbed_2_1) equal to [order](../order-parameters/#__tabbed_2_2) `actual_amount` value if full reverse is required. Multiple partial reverses are allowed while sum of all partial reverses is less or equal to order `actual_amount`.

## Idempotent reversal key

Idempotent reversal key `reverse_id` in [reverse request](../reversal-parameters/) is used to provide safe reverse retries. Usually it is not required for full reverse. In case of partial reverse, idempotent key can protect from multiple retries in case of error.

For example, if order amount is 1000 GEL and partial reversal with amount 100 GEL is sent and failed due to network error, to be sure, that one more attempt of 100 GEL reverse will lead to single partial reversal and not a duplicate (100 + 100 = 200 GEL), each attempt must be sent with the same `reverse_id` parameter value.

*Endpoint for order reverse*

Reverse the order

`POST /api/reverse/order_id`

This endpoint expects `POST` request in `JSON` format with [parameters](/api/reversal-parameters/#__tabbed_2_1).

Normal response will contain `reverse_status` parameter which indicates if reversal is successful or not.

Request and response examples

```
curl -L 'https://pay.flitt.com/api/reverse/order_id' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "order_id": "test_12343242111",
    "currency": "GEL",
    "amount": "1",
    "signature": "29a569275265925c2ec356d3adada1929fd8bb8c",
    "merchant_id": "1549901"
  }
}'

```

```
{
    "response": {
        "reverse_status": "approved",
        "order_id": "test_12343242111",
        "response_description": "",
        "response_code": "",
        "merchant_id": 1549901,
        "response_status": "success",
        "signature": "c703b3ce82aecfd2de633319685223347140717d",
        "reverse_id": "",
        "reversal_amount": "1",
        "transaction_id": "2011273408"
    }
}

```

```
{
    "response": {
        "error_code": 1007,
        "error_message": "Parameter `signature` is incorrect",
        "request_id": "HGh7ami3WN0ci",
        "response_status": "failure"
    }
}

```

List of supported currencies for bank cards processing:

| Merchant country | Currency code | Currency name        |
| ---------------- | ------------- | -------------------- |
| Georgia          | GEL           | Georgian Lari        |
| Georgia          | USD           | United States dollar |
| Georgia          | EUR           | Euro                 |
| Armenia          | AMD           | Armenian Dram        |
| Azerbaijan       | AZN           | Azerbaijanian Manat  |
| Kazakhstan       | KZT           | Tenge                |
| Moldova          | MDL           | Moldovian Leu        |
| Uzbekistan       | UZS           | Uzbekistan Sum       |

## Delayed payments (customer re-pays payment without new payment request)

**Payment conversion**

The most common decline reasons for payments by card are:

1. insufficient funds
1. invalid card details (cvv2, expiry date, card number)
1. internet payments are not allowed for the card or internet limit is low
1. issuing bank declined payment by other reasons
1. Flitt/bank antifraud system declined payment

In cases 1-3 customer usually can solve the issue promptly enough contacting bank support to: clarify correct expiry date, CVV2, recharge card, increase limit. Therefore, to allow the customer to retry without re-creating the order parameter delayed=Y is added in the protocol .

**Delayed order**

The delayed payment (this is by default, `delayed=Y`) differs from the non-delayed payment (`delayed=N`) in that the client can try to pay it many times until the payment lifetime specified in the `lifetime` parameter expires.

In this case, the merchant will receive the response to `server_callback_url` as many times as the customer tries to pay the payment.

The client is redirected to response_url only after the expiration of the orderâs lifetime (`lifetime` parameter) if at that moment the client is trying to make a re-payment. If the client is not at the time of payment on the payment page, the merchant may never receive a response to `response_url`. Therefore, for payments with the `delayed = Y` parameter, we recommend that you use the `server_callback_url` parameter.

Returned `order_status` status with `delayed = Y`

- processing â the client tried to make a payment attempt but received a refusal from the bank, non-empty parameters `response_code`, `response_description` are returned to `server_callback_url`, the `lifetime` of the order lifetime has not yet expired
- created â the client was redirected to the payment page but has not yet entered payment details
- expired â the client did not enter payment details and the order expired
- declined â is the same as processing, but the lifetime of the order has expired

Returned `order_status` status with `delayed = N`

- declined â the client tried to make an attempt to pay, but received a refusal from the bank, non-empty parameters `response_code`, `response_description` are returned to `response_url` and `server_callback_url`
- created â the client was redirected to the payment page but has not yet entered payment details
- expired â the client did not enter payment details and the order expired

# Create an embedded checkout page with an individual design. Version 2.0

Project at GitHub: <https://github.com/flittpayments/checkout-vue>

You can design your own checkout page hosted on your website as a regular HTML + CSS code.

We developed pre-designed example (HTML/CSS/JavaScript) which you can try to use on your site:

Google Pay policy

Before integrating Google Payâ¢ with the Flitt embedded method, please adhere to [Google Pay APIs Acceptable Use Policy](https://payments.developers.google.com/terms/aup)

By starting the integration you confirm that you accept the terms defined in the [Google Pay API Terms of Service](https://payments.developers.google.com/terms/sellertos).

## Basic checkout design example. Card, Apple Pay, Google Payâ¢

See the Pen [Flitt - custom checkout light](https://codepen.io/flitt/pen/OJeYwvO) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

First, you need to import JavaScript SDK:

```
https://pay.flitt.com/latest/checkout-vue/checkout.js

```

Then CSS files:

```
https://pay.flitt.com/latest/checkout-vue/checkout.css

```

Checkout page is configured with JavaScript code:

Configuration example

```
var Options = {
    options: {
        methods: ['card'],
        methods_disabled: [],
        card_icons: ['mastercard', 'visa', 'maestro'],
        active_tab: 'card',
        fields: false,
        title: 'my_title',
        link: 'https://shop.com',
        full_screen: true,
        button: true,
        email: true
    },
    params: {
        merchant_id: 1549901,
        required_rectoken: 'y',
        currency: 'GEL',
        amount: 500,
        order_desc: 'my_order_desc',
        response_url: 'http://shop.com/thankyoupage'
    }
}
checkout("#app", Options);

```

JavaScript configuration has the following structure:

Configuration structure

```
{
  options: {},
  params: {},
  button: {}, // button config 
  fields_custom: [],
  messages: {},
  css_variable: {},
}

```

Configure payment page form customization options

| Parameter name           | Parameter type | Default value          | Description                                                                                                                    |
| ------------------------ | -------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `methods`                | Array          | ['card']               | support `card`, `most_popular`, `banks`, `wallets`.                                                                            |
| `methods_disabled`       | Array          | []                     | support `card`, `most_popular`, `banks`, `wallets`.                                                                            |
| `wallet_methods_enabled` | Array          | ['apple', 'google']    | support `apple`, `google`.                                                                                                     |
| `card_icons`             | Array          | ['mastercard', 'visa'] | support `mastercard`, `visa`, `prostir`, `diners`, `american_express` , `jcb`, `maestro`, `union_pay`                          |
| `banks_icons`            | Array          | []                     |                                                                                                                                |
| `local_methods_icons`    | Array          | []                     |                                                                                                                                |
| `crypto_icons`           | Array          | []                     |                                                                                                                                |
| `loans_icons`            | Array          | []                     |                                                                                                                                |
| `emoney_icons`           | Array          | []                     |                                                                                                                                |
| `wallets_icons`          | Array          | []                     |                                                                                                                                |
| `title`                  | String         |                        |                                                                                                                                |
| `link`                   | String         |                        | format url                                                                                                                     |
| `full_screen`            | Boolean        | true                   |                                                                                                                                |
| `locales`                | Array          | [all]                  | support `az`, `cs`, `da`, `de`, `en`, `es`, `fi`, `fr`, `hu`, `it`, `ka`, `ko`, `lv`, `nl`, `pl`, `ro`, `ru`, `sk`, `uk`, `zh` |
| `api_domain`             | String         | 'pay.flitt.com'        |                                                                                                                                |
| `endpoint`               | Object         |                        |                                                                                                                                |
| `active_tab`             | String         | 'card'                 | support `card`, `most_popular`, `banks`, `wallets`                                                                             |
| `active_method`          | String         | ''                     |                                                                                                                                |
| `logo_url`               | String         |                        | format url                                                                                                                     |
| `offerta_url`            | String         |                        | format url                                                                                                                     |
| `default_country`        | String         |                        |                                                                                                                                |
| `countries`              | Array          |                        |                                                                                                                                |
| `theme`                  | Object         |                        |                                                                                                                                |
| `show_menu_first`        | Boolean        | false                  |                                                                                                                                |
| `disable_request`        | Boolean        | false                  | no requests are sent to the server                                                                                             |
| `subscription`           | Object         |                        |                                                                                                                                |
| `loading`                | String         |                        | format url                                                                                                                     |
| `amount_readonly`        | Boolean        | true                   |                                                                                                                                |
| `autosubmit`             | Boolean        | false                  |                                                                                                                                |
| `show_amount`            | Boolean        | true                   |                                                                                                                                |
| `show_email`             | Boolean        | false                  |                                                                                                                                |
| `show_fee`               | Boolean        | true                   |                                                                                                                                |
| `show_lang`              | Boolean        | true                   |                                                                                                                                |
| `show_link`              | Boolean        | true                   |                                                                                                                                |
| `show_order_desc`        | Boolean        | true                   |                                                                                                                                |
| `show_pay_button_amount` | Boolean        | true                   | displaying the amount on the button                                                                                            |
| `show_pay_button`        | Boolean        | true                   |                                                                                                                                |
| `show_processed`         | Boolean        | true                   |                                                                                                                                |
| `show_secure_message`    | Boolean        | true                   |                                                                                                                                |
| `show_test_mode`         | Boolean        | true                   |                                                                                                                                |
| `show_title`             | Boolean        | true                   |                                                                                                                                |

**options.theme**

| Name     | Type   | Default   | Description                                                                                                                                                                            |
| -------- | ------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`   | String | 'light'   | support `light`, `dark`.                                                                                                                                                               |
| `preset` | String | 'black'   | support `reset`, `black`, `silver`, `vibrant_silver`, `vibrant_gold`, `solid_black`, `black_and_white`, `euphoric_pink`, `heated_steel`, `nude_pink`, `tropical_gold`, `navy_shimmer`. |
| `layout` | String | 'default' | support `default`, `plain`, `wallets_only`.                                                                                                                                            |

**options.subscription**

| Name        | Type1   | Default                  | Description                                                                      |
| ----------- | ------- | ------------------------ | -------------------------------------------------------------------------------- |
| `type`      | String  | 'disable'                | support `disable`, `hidden`, `shown_edit_on`, `shown_edit_off`, `shown_readonly` |
| `periods`   | Array   | ['day', 'week', 'month'] | support `day`, `week`, `month`.                                                  |
| `quantity`  | Boolean | false                    |                                                                                  |
| `trial`     | Boolean | false                    |                                                                                  |
| `unlimited` | Boolean | true                     |                                                                                  |
| `readonly`  | Boolean | false                    |                                                                                  |

Order parameters described in [Request parameters](/api/order-parameters/#__tabbed_2_1)

| Parameter name      | Parameter type | Default value    | Description                 |
| ------------------- | -------------- | ---------------- | --------------------------- |
| `merchant_id`       | Integer        | 1549901          |                             |
| `order_desc`        | String         |                  |                             |
| `amount`            | Integer        | null             |                             |
| `currency`          | String         | 'GEL'            |                             |
| `response_url`      | String         |                  | format url                  |
| `lang`              | String         | browser language |                             |
| `required_rectoken` | String         |                  | support `Y`, `N`, `y`, `n`. |
| `verification`      | String         |                  | support `Y`, `N`, `y`, `n`. |
| `token`             | String         |                  | length 40                   |
| `button`            | String         |                  | length 20-80                |
| `offer`             | Boolean        | false            |                             |
| `recurring_data`    | Object         |                  |                             |
| `custom`            | Object         |                  |                             |
| `customer_data`     | Object         |                  |                             |

**params.recurring_data**

Subscription parameters values: period, frequency, start date, end date, regular amount

| Name             | Type    | Default | Description                     |
| ---------------- | ------- | ------- | ------------------------------- |
| `every`          | Integer | 1       |                                 |
| `period`         | String  | 'month' | support `day`, `week`, `month`. |
| `amount`         | Integer | 0       |                                 |
| `end_time`       | String  |         | format YYYY-MM-DD               |
| `start_time`     | String  |         | format YYYY-MM-DD               |
| `quantity`       | Integer | 0       |                                 |
| `trial_period`   | String  | ''      |                                 |
| `trial_quantity` | Integer | 0       |                                 |

**params.customer_data**

| Name               | Type   | Default | Description          |
| ------------------ | ------ | ------- | -------------------- |
| `customer_name`    | String |         |                      |
| `customer_address` | String |         |                      |
| `customer_zip`     | String |         |                      |
| `customer_city`    | String |         |                      |
| `customer_country` | String |         | dictionary countries |
| `customer_state`   | String |         |                      |
| `phonemobile`      | String |         | format phone         |
| `email`            | String |         | format email         |

Messages localization

```
{
  messages: {
    {en}: {
      {id}: {value},
      ...
    },
    ...
  },
}

```

```
{
  css_variable: {
    main: {hex color value},
    card_bg: {hex color value},
    card_shadow: {hex color value}
  }
}       

```

```
{
  fields_custom: {
    id-1: {
      name: 'id-1',
      label: 'label1',
      value: 'value1',
      readonly: true,
      p: 1
    },
    id-2: {
      name: 'id-2',
      label: 'label2',
      value: 'value2',
      p: 2
    },
    id-3: {
      name: 'id-3',
      label: 'label3',
      type: 'checkbox',
      required: true,
      p: 3
    }
  }
}

```

Below are examples of ready-made designs of payment pages in different styles.

## Plain checkout design example for cards

See the Pen [Flitt - layout plain](https://codepen.io/flitt/pen/vEEmoOw) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Plain checkout design example for cards with JS code submit button

See the Pen [Flitt - layout plain with submit button](https://codepen.io/flitt/pen/qEONWoY) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example style light background, blue card

See the Pen [Flitt - custom checkout light](https://codepen.io/flitt/pen/KKjLBdo) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example style dark background, blue card

See the Pen [Flitt - custom checkout dark](https://codepen.io/flitt/pen/ZEdZwRR) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example for compact region

With parameters `full_screen: false`, `hide_title: true`, `hide_link: true`

See the Pen [Flitt - custom checkout. Additional fields. Version 2.0](https://codepen.io/flitt/pen/BaggpVw) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example with additional merchant fields

See the Pen [Flitt - custom checkout. Additional fields. Version 2.0](https://codepen.io/flitt/pen/bGPyOWz) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example with subscription

After the first successful payment, payment gateway will create a calendar with scheduled regular payments. The frequency and frequency are set in the parameters of the payment page.

See the Pen [Flitt - custom checkout. Subscription. Version 2.0](https://codepen.io/flitt/pen/eYwabEJ) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example with subscription and localization of custom fields

See the Pen [Flitt - custom checkout. Subscription. Version 2.0](https://codepen.io/flitt/pen/vYqwvWj) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example with extended payment methods

See the Pen [Flitt - custom checkout. Version 2.0](https://codepen.io/flitt/pen/VwJOqQQ) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example with handling of pay-button click event

See the Pen [Flitt - checkout with own submit buttons. Version 2.0](https://codepen.io/flitt/pen/oNrRJyp) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example with JavaScript callbacks

You can catch `response_code` value and replace a code message with yours custom. See all [codes](/api/response-codes/#javascript-response-codes).

See the Pen [Flitt - custom checkout. Javascript calbacks. Version 2.0](https://codepen.io/flitt/pen/vYqwwXP) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example of Apple Pay and Google Pay buttons

See the Pen [Flitt - Apple, Google Pay buttons](https://codepen.io/flitt/pen/PorvvEw) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

## Example with order created on backend

**Create order at your server:**

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token' 

```

**Receive order token:**

```
{
  "response":{
    "response_status":"success",
    "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
  }
} 

```

**Load checkout page with order token as a parameter:**

```
var Options = {
  options: {
    methods: ['card'],
    methods_disabled: [],
    card_icons: ['mastercard', 'visa', 'maestro'],
    active_tab: 'card',
    fields: false,
    title: 'Demo checkout',
    link: 'https://shop.com',
    full_screen: true,
    button: true,
    email: true
  },
  params: {
    token: "13c178ad84446ef36eaab365b1e12e6987e9b3d9"
  }
}
checkout("#checkout-container", Options);

```

## Using color presets and personal log

You can use gradient color presets with object **theme** in the **options** section.

```
options: {
  methods: ['card'],
  ...
  ,
  theme: {
    type: "light",
    preset: "black"
}

```

**type** attribute can have "light" or "dark" value.

**preset** attribute can have one of the following values:

```
vibrant_gold
vibrant_silver
euphoric_pink
black
solid_black
silver
black_and_white
heated_steel
nude_pink
tropical_gold
navy_shimmer

```

euphoric_pink preset example

See the Pen [Flitt - minimal checkout ligt euphoric_pink v2.0](https://codepen.io/flitt/pen/RwzzKMo) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

All gradients naming you can match as follows (click to enlarge image):

You can use custom flat colors with `css_variable` parameter (to use it, you need to set `preset: "reset"`) as well as own logo with `logo_url` parameter:

Example with main color: valencia #D94343 for card background and fuchsia_blue: #7054C7 for button color

See the Pen [Flit - custom colors](https://codepen.io/flitt/pen/YzobowX) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

We recommend to use such colors:

valencia: #D94343

flame_pea: #DF583D

jaffa: #E86F33

zest: #E58626

gamboge: #EBA212

citron: #A9B221

sushi: #82B536

chelsea_cucumber: #6BA854

fruit_salad: #54A868

breaker_bay: #54A199

pelorous: #43ABBF

havelock_blue: #57A4DC

curious_blue: #4F8BE0

indigo: #6073D1

fuchsia_blue: #7054C7

studio: #8453B5

wisteria: #9D55B5

fuchsia_pink: #BA5BB2

mulberry: #C74E8A

cabaret: #D4486B

Fiscalisation process consist of several steps

```
sequenceDiagram
  Merchant->>Flitt API: 1. create purchase with reservation_data.products parameter
  Flitt API->>Merchant: 2. Purchase is approved  
  loop Fiscalisation
    Flitt API->>Goverment fiscal server: 3. Sending payment data to goverment fiscal server
    Goverment fiscal server->>Flitt API: 4. Succesfull fiscalisation
  end
  Merchant->>Flitt API: 5. Polling purchase fiscal data     
```

1. You should create purchase. Additional attribute `products` of parameter `reservation_data` must be provided when creating purchase. Check [description](/api/reservation_data/) of this parameter.
1. Flitt approves payments through payment institution and send response to `server_callback_url` ad `response_url`
1. After payment is completed successfully, Flitt sends attribute `products` of parameter `reservation_data` along with other payment data to the government fiscal server.
1. Government fiscalises payment and provide receipt URL with detailed data.
1. You should pool fiscal data using `POST https://pay.flitt.com/api/fiscal_data` request described bellow

## Creating order

Create order with [redirect](/api/create-order/), [direct](/api/order-parameters-direct/) or any other [type of integration](/). Pass BASE64 parameter `reservation_data` in order purchase could be fiscalised.

Pay attention

Fiscalisation is available only in Uzbekistan.

Fiscalisation is available only for purchase without pre-authorisation (parameter `preauth = N` or empty).

Example

```
    curl -L 'https://pay.flitt.com/api/checkout/3dsecure_step1' \
    -H 'Content-Type: application/json' \
    -d '{
          "request": {
            "merchant_id": 1549901,
            "order_desc": "test order",
            "amount": "200000",
            "currency": "UZS",
            "card_number": "860049XXXXXX6478",
            "expiry_date": "0399",
            "cvv2": "***",
            "preauth": "N",
            "reservation_data": "ewogICJwcm9kdWN0cyI6IFsKICAgIHsKICAgICAgImlkIjogMSwKICAgICAgIm5hbWUiOiAiUHJvZHVjdCBBIiwKICAgICAgInByaWNlIjogMTAwLjAwLAogICAgICAicXVhbnRpdHkiOiAyLAogICAgICAidmF0X3BlcmNlbnQiOiAyMCwKICAgICAgImNvZGUiOiAiMDA3MDIwMDEwMDEwMDAwMDEiLAogICAgICAidW5pdHMiOiAxLAogICAgICAiZGlzY291bnQiOiAxMC4wMCwKICAgICAgInBhY2thZ2VfY29kZSI6ICI1Njc4IiwKICAgICAgInRvdGFsX2Ftb3VudCI6IDE5MC4wMAogICAgfSwKICAgIHsKICAgICAgImlkIjogMSwKICAgICAgIm5hbWUiOiAiUHJvZHVjdCBCIiwKICAgICAgInByaWNlIjogMTAwLjAwLAogICAgICAicXVhbnRpdHkiOiAyLAogICAgICAidmF0X3BlcmNlbnQiOiAyMCwKICAgICAgImNvZGUiOiAiMDA3MDIwMDEwMDEwMDAwMDEiLAogICAgICAidW5pdHMiOiAxLAogICAgICAiZGlzY291bnQiOiAxMC4wMCwKICAgICAgInBhY2thZ2VfY29kZSI6ICI1Njc5IiwKICAgICAgInRvdGFsX2Ftb3VudCI6IDE5MC4wMAogICAgfQogIF0KfQ==",
            "order_id": "flittpg16968413",
            "signature": "0d75c7ea9c0f2d6ada857fe5c462d0c232513f34"
          }
        }'

```

```
    curl -L 'https://pay.flitt.com/api/checkout/url' \
    -H 'Content-Type: application/json' \
    -d '{
          "request": {
            "merchant_id": 1549901,
            "order_desc": "test order",
            "amount": "200000",
            "currency": "UZS",
            "preauth": "N",
            "reservation_data": "ewogICJwcm9kdWN0cyI6IFsKICAgIHsKICAgICAgImlkIjogMSwKICAgICAgIm5hbWUiOiAiUHJvZHVjdCBBIiwKICAgICAgInByaWNlIjogMTAwLjAwLAogICAgICAicXVhbnRpdHkiOiAyLAogICAgICAidmF0X3BlcmNlbnQiOiAyMCwKICAgICAgImNvZGUiOiAiMDA3MDIwMDEwMDEwMDAwMDEiLAogICAgICAidW5pdHMiOiAxLAogICAgICAiZGlzY291bnQiOiAxMC4wMCwKICAgICAgInBhY2thZ2VfY29kZSI6ICI1Njc4IiwKICAgICAgInRvdGFsX2Ftb3VudCI6IDE5MC4wMAogICAgfSwKICAgIHsKICAgICAgImlkIjogMSwKICAgICAgIm5hbWUiOiAiUHJvZHVjdCBCIiwKICAgICAgInByaWNlIjogMTAwLjAwLAogICAgICAicXVhbnRpdHkiOiAyLAogICAgICAidmF0X3BlcmNlbnQiOiAyMCwKICAgICAgImNvZGUiOiAiMDA3MDIwMDEwMDEwMDAwMDEiLAogICAgICAidW5pdHMiOiAxLAogICAgICAiZGlzY291bnQiOiAxMC4wMCwKICAgICAgInBhY2thZ2VfY29kZSI6ICI1Njc5IiwKICAgICAgInRvdGFsX2Ftb3VudCI6IDE5MC4wMAogICAgfQogIF0KfQ==",
            "order_id": "flittpg16968414",
            "signature": "1fdb9eb25a985960a86585aa856218dca90e86f9"
          }
        }'

```

```
    curl -L 'https://pay.flitt.com/api/recurring' \
    -H 'Content-Type: application/json' \
    -d '{
          "request": {
            "merchant_id": 1549901,
            "order_desc": "test order",
            "amount": "200000",
            "currency": "UZS",
            "preauth": "N",
            "rectoken": "6aDyYLI2n7aq6ZHBBIiwwglz97emriquch",
            "reservation_data": "ewogICJwcm9kdWN0cyI6IFsKICAgIHsKICAgICAgImlkIjogMSwKICAgICAgIm5hbWUiOiAiUHJvZHVjdCBBIiwKICAgICAgInByaWNlIjogMTAwLjAwLAogICAgICAicXVhbnRpdHkiOiAyLAogICAgICAidmF0X3BlcmNlbnQiOiAyMCwKICAgICAgImNvZGUiOiAiMDA3MDIwMDEwMDEwMDAwMDEiLAogICAgICAidW5pdHMiOiAxLAogICAgICAiZGlzY291bnQiOiAxMC4wMCwKICAgICAgInBhY2thZ2VfY29kZSI6ICI1Njc4IiwKICAgICAgInRvdGFsX2Ftb3VudCI6IDE5MC4wMAogICAgfSwKICAgIHsKICAgICAgImlkIjogMSwKICAgICAgIm5hbWUiOiAiUHJvZHVjdCBCIiwKICAgICAgInByaWNlIjogMTAwLjAwLAogICAgICAicXVhbnRpdHkiOiAyLAogICAgICAidmF0X3BlcmNlbnQiOiAyMCwKICAgICAgImNvZGUiOiAiMDA3MDIwMDEwMDEwMDAwMDEiLAogICAgICAidW5pdHMiOiAxLAogICAgICAiZGlzY291bnQiOiAxMC4wMCwKICAgICAgInBhY2thZ2VfY29kZSI6ICI1Njc5IiwKICAgICAgInRvdGFsX2Ftb3VudCI6IDE5MC4wMAogICAgfQogIF0KfQ==",
            "order_id": "flittpg16968414",
            "signature": "1fdb9eb25a985960a86585aa856218dca90e86f9"
          }
        }'

```

## Pooling fiscal data

To obtain fiscal data, order must be either [captured](/api/capture-parameters/) or approved without `preauth = Y` parameter.

### Parameters

Request parameters

`POST https://pay.flitt.com/api/fiscal_data`

| Parameter name | Type         | Description | Example                                                                                                                                                                                                                |
| -------------- | ------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `order_id`     | string(1024) | mandatory   | Order ID which is generated by merchant                                                                                                                                                                                |
| `merchant_id`  | integer(12)  | mandatory   | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                                    |
| `signature`    | string(40)   | mandatory   | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response |

Request eamples

```
curl -L 'https://pay.flitt.com/api/fiscal_data' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "merchant_id": 1549901,
    "order_id": "6120b190-2a39-4fde-acae-a9761e7e58bd",
    "signature": "b8f84562d3e2a971aea7d173c6fb59084f414d23"
  }
}'

```

Response examples

```
{
    "response": {
        "error": "Merchant account not found",
        "response_status": "success"
    }
}

```

```
{
    "response": {
        "order_id": "6120b190-2a39-4fde-acae-a9761e7e58bd",
        "fiscalisation_data": {
            "2079125283": {
                "message": {
                    "ru": "Ð¤Ð¸ÑÐºÐ°Ð»ÑÐ½ÑÐµ Ð´Ð°Ð½Ð½ÑÐµ Ð½Ðµ Ð½Ð°Ð¹Ð´ÐµÐ½Ñ.",
                    "uz": "Fiskal ma`lumotlar topilmadi.",
                    "en": "Fiscal data not found."
                },
                "code": -31603
            }
        },
        "response_status": "success"
    }
}

```

```
{
    "response": {
        "order_id": "pgtest000-1_02",
        "fiscalisation_data": {
            "9002999267": {
                "status_code": 0,
                "message": "",
                "terminal_id": "EZ000000000658",
                "date": "",
                "fiscal_sign": "",
                "qr_code_url": "https://ofd.soliq.uz/epi?t=XXX&r=XXX&c=XXX&s=XXX",
                "type": 0,
                "receipt_id": 3340,
                "external": true,
                "processed_date": 1736320610322
            }
        },
        "response_status": "success"
    }
}

```


# Get capture status

Capture status should be obtained through `capture_amount` attribute in `additional_info` in [Get order status](../order-status/) request. In case when full capture is processed, `capture_amount` will be equal to order `actual_amount`. In case when partial capture is processed, `capture_amount` will be lower then `actual_amount`.

Example of partially captured order

**Order status request:**

```
curl -L 'https://pay.flitt.com/api/status/order_id' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "order_id": "test_12343242113",
    "version": "1.0.1",
    "merchant_id": "1549901",
    "signature": "28abd3db20cad9b8257b5cca88f0bf1c450bd2fd"
  }
}'

```

**Order status response:**

`additional_info` with `capture_status` and `capture_amount` is highlighted. It is less, than order `actual_amount`, what mean, that order was partially captured.

```
{
    "response": {
        "rrn": "111111111111",
        "masked_card": "444455XXXXXX6666",
        "sender_cell_phone": "",
        "sender_account": "",
        "currency": "GEL",
        "fee": "",
        "reversal_amount": "0",
        "settlement_amount": "0",
        "actual_amount": "15118",
        "response_description": "",
        "sender_email": "",
        "order_status": "approved",
        "response_status": "success",
        "order_time": "30.08.2024 12:39:48",
        "actual_currency": "GEL",
        "order_id": "test_12343242113",
        "tran_type": "purchase",
        "eci": "7",
        "settlement_date": "",
        "payment_system": "card",
        "approval_code": "123456",
        "merchant_id": 1549901,
        "settlement_currency": "",
        "payment_id": 814543587,
        "card_bin": 444455,
        "response_code": "",
        "card_type": "VISA",
        "amount": "1000",
        "signature": "c7cac63ddb9bf54b0511ddbf9ddab1351f8260b6",
        "product_id": "",
        "merchant_data": "",
        "rectoken": "",
        "rectoken_lifetime": "",
        "verification_status": "",
        "parent_order_id": "",
        "fee_oplata": "0",
        "additional_info": "{\"capture_status\": \"captured\", \"capture_amount\": 1.0, \"reservation_data\": null, \"transaction_id\": 2011462103, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"30.08.2024 12:40:32\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"is_test\": true}",
        "response_signature_string": "**********|15118|GEL|{\"capture_status\": \"captured\", \"capture_amount\": 1.0, \"reservation_data\": null, \"transaction_id\": 2011462103, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"30.08.2024 12:40:32\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"is_**********\": true}|1000|123456|444455|VISA|GEL|7|0|444455XXXXXX6666|1549901|**********_12343242113|approved|30.08.2024 12:39:48|814543587|card|success|0|111111111111|0|purchase"
    }
}

```

# Get reversal status

Reversal status should be obtained through [Get order status](../order-status/) request. `reversal_amount` in the order status response accumulates all the reverses, which were successfully processed for the order. In case when full reversal is processed, `reversal_amount` will be equal to `actual_amount`. In case when partial reversal or several reversals are processed, `reversal_amount` will be equal to the sum of all partial reversals been processed.

Example of partially reversed order

**Order status request:**

```
curl -L 'https://pay.flitt.com/api/status/order_id' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "order_id": "test_12343242111",
    "version": "1.0.1",
    "merchant_id": "1549901",
    "signature": "64bbd2d53ee60f88b8184751cc05bd0a846f5768"
  }
}'

```

**Order status response:**

`reversal_amount` is highlighted. It is less, than order `actual_amount`, what mean, that order was partially reversed.

```
{
    "response": {
        "rrn": "111111111111",
        "masked_card": "444455XXXXXX6666",
        "sender_cell_phone": "",
        "sender_account": "",
        "currency": "GEL",
        "fee": "",
        "reversal_amount": "48",
        "actual_amount": "15118",
        "settlement_amount": "0",
        "response_description": "",
        "sender_email": "",
        "order_status": "approved",
        "response_status": "success",
        "order_time": "28.08.2024 21:20:02",
        "actual_currency": "GEL",
        "order_id": "test_12343242111",
        "tran_type": "purchase",
        "eci": "7",
        "settlement_date": "",
        "payment_system": "card",
        "approval_code": "123456",
        "merchant_id": 1549901,
        "settlement_currency": "",
        "payment_id": 814277784,
        "card_bin": 444455,
        "response_code": "",
        "card_type": "VISA",
        "amount": "1000",
        "signature": "8c06dd297c43833ded498b342a6225423f8494b3",
        "product_id": "",
        "merchant_data": "",
        "rectoken": "",
        "rectoken_lifetime": "",
        "verification_status": "",
        "parent_order_id": "",
        "fee_oplata": "0",
        "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": null, \"transaction_id\": 2011273408, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"28.08.2024 21:20:05\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"is_test\": true}",
        "response_signature_string": "**********|15118|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": null, \"transaction_id\": 2011273408, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"28.08.2024 21:20:05\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"is_**********\": true}|1000|123456|444455|VISA|GEL|7|0|444455XXXXXX6666|1549901|**********_12343242111|approved|28.08.2024 21:20:02|814277784|card|success|48|111111111111|0|purchase"
    }
}

```

# Geting payment key in Merchant Portal

# Preparation

During your integration, please follow the Google Payâ¢ API documentation:

For Android:

- [Google Pay Android developer documentation](https://developers.google.com/pay/api/web/overview)
- [Google Pay Android integration checklist](https://developers.google.com/pay/api/android/guides/test-and-deploy/integration-checklist)
- [Google Pay Android brand guidelines](https://developers.google.com/pay/api/android/guides/brand-guidelines)

For web:

- [Google Pay Web developer documentation](https://developers.google.com/pay/api/web/)
- [Google Pay Web integration checklist](https://developers.google.com/pay/api/web/guides/test-and-deploy/integration-checklist)
- [Google Pay Web Brand Guidelines](https://developers.google.com/pay/api/web/guides/brand-guidelines)

# Google Pay direct integration

Google Pay direct integration can be done in two ways

1. [Using decrypted PAN (DPAN)](/api/googlepay-direct/#using-decrypted-pan-dpan)
1. [Using encrypted payment data](/api/googlepay-direct/#using-encrypted-payment-data)

Both types of integration require [Google Pay API](https://developers.google.com/pay/api/web/overview) to be implemented by merchant.

Use the defined values during your integration:

Google Pay parameters

```
gatewayMerchantId: <your Flitt merchant_id>
gatewayID: flitt

```

Google Pay

Pay attentionm that Flitt supports only following configuration:

Allowed payment methods : **CARD**

Allowed authorization methods: **[PAN_ONLY,CRYPTOGRAM_3DS]**

Allowed card networks: **[MASTERCARD,VISA]**

Tokenization specification: **PAYMENT_GATEWAY**

## Using decrypted PAN (DPAN)

Integration with DPAN assumes that [Payment Data Cryptography](https://developers.google.com/pay/api/web/guides/resources/payment-data-cryptography) is performed on merchant side.

To create order using DPAN, merchant needs to use [create order with direct](/api/create-order-direct/) method.

While the [parameters](/api/order-parameters-direct/) are still as described, the parameters which are related to card data should contain information from Google Pay decrypted payment data:

Google Pay DPAN data parameters

| Parameters    | Type         | Mandatory | Description                                                                                                                                                                                         |
| ------------- | ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `card_number` | string(19)   | optional  | `pan` from Google Pay `paymentMethodDetails` object                                                                                                                                                 |
| `expiry_date` | string(4)    | optional  | DPAN expiry date in format MMYY                                                                                                                                                                     |
| `cavv`        | string(2048) | optional  | Google Pay one-time `cryptogram` from `paymentMethodDetails` object                                                                                                                                 |
| `eci`         | string(2048) | optional  | Google Pay `eciIndicator` from `paymentMethodDetails` object                                                                                                                                        |
| `wallet`      | string(2048) | optional  | Wallet type: `googlepay`                                                                                                                                                                            |
| `schemeid`    | string(2048) | optional  | Visa/MasterCard identifier of CIT - client initiated transaction, returned in initial purchase in field `additional_info->schemeid`, see [response parameters](/api/order-parameters/#__tabbed_2_2) |

see [response parameters](/api/order-parameters/#__tabbed_1_2)

Pay attention

**Google Pay and 3DSecure**

3DSecure authentication will be required for Google Pay in Georgia for both authorization methods **PAN_ONLY, CRYPTOGRAM_3DS** and 3DS will be required for **PAN_ONLY** in other regions like Moldova, Armenia.

Consider this when implementing [create order with direct](/api/create-order-direct/) as it can require two-steps flow:

- create order: `POST /api/3dsecure_step1`
- submit 3DSecure data: `POST /api/3dsecure_step2`

Pay attention

**Recurring payments with Google Pay**

Flitt supports recurring payments for Google Pay.

Depending on the parameters which are sent during [order creation](/api/create-order-direct/), order is considered as CIT (client initiated transaction) or MIT (merchant initiated transaction)

CIT: `cavv` is mandatory, `schemeid` must not be present

MIT: `schemeid` is mandatory, `cavv` must not be present

Examples

**Request example of client initiated transaction:**

```
{
  "request": {
    "order_id": "test_12343242",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "amount": 1000,
    "currency": "GEL",
    "card_number": "4111111111111111",
    "cavv": "AEH2lSgIQ9/OAALA1DWsGgADFA==",
    "eci": "05",
    "wallet": "googlepay",
    "expiry_date": "1135",
    "client_ip": "8.8.8.8",
    "server_callback_url": "https://myserver.com/callback",
    "signature": "0c0c2374c73267e7be560d80834e4ba28ccda7aa"
  }
}

```

**Request example of merchant initiated transaction:**

```
{
  "request": {
    "order_id": "test_12343243",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "amount": 1000,
    "currency": "GEL",
    "card_number": "4111111111111111",
    "schemeid":"885056510569385"
    "eci": "05",
    "wallet": "googlepay",
    "expiry_date": "1135",
    "client_ip": "8.8.8.8",
    "server_callback_url": "https://myserver.com/callback",
    "signature": "0c0c2374c73267e7be560d80834e4ba28ccda7aa"
  }
}

```

## Using encrypted payment data

Integration with encrypted payment data assumes that [Payment Data](https://developers.google.com/pay/api/web/guides/resources/payment-data-cryptography) obtained from Google Pay is not decrypted on merchant side.

Instead of that, `container` parameter must be transferred with method [create order with direct](/api/create-order-direct/) to Flitt.

While the [parameters](/api/order-parameters-direct/) are still as described, the parameters `card_number`, `expiry_date`, `cavv`, `eci`, `wallet` , `schemeid` which are related to card data must be replaced with `container` parameter.

Google Pay request example with container

```
{
  "request": {
    "amount": "100",
    "currency": "GEL",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "order_id": "test_12343243",
    "container": "ewogICJzaWduYXR1cmUiOiAiTUVZQ0lRRE4yYjR5eXdPT0xubmRxWi9kNG5QcmplYnQuLi5Fb05oNVhYUlRKc3JiTThPNE9wUzBrakNMTjNwNSIsCiAgImludGVybWVkaWF0ZVNpZ25pbmdLZXkiOiB7CiAgICAic2lnbmVkS2V5IjogIntcImtleVZhbHVlXCI6XCJNRmt3RXdZSEtvWkl6ajBDQVFZSUtvWkl6ajBEQVFjRC4uLitTb0w2RzhRMzRvUmhFeDVpVXUzS1VBZVRTbDNKakFtaTIyNnRURCtQeTJRXFx1MDAzZFxcdTAwM2RcIixcImtleUV4cGlyYXRpb25cIjpcIjE3NDk4MDQ5NzYwMDBcIn0iLAogICAgInNpZ25hdHVyZXMiOiBbCiAgICAgICJNRVlDSVFEZTdQcXNEa2NnU1cvLy9WL3BKb21BQ3EvM2pQcSt2dmJhLy4uLlBVcnNJWktTYndOYVVaRFpxV0lUMW9BUkNVIgogICAgXQogIH0sCiAgInByb3RvY29sVmVyc2lvbiI6ICJFQ3YyIiwKICAic2lnbmVkTWVzc2FnZSI6ICJ7XCJlbmNyeXB0ZWRNZXNzYWdlXCI6XCJ5TXV3UGFRR1Rqdkw4cENFc0NvbkEwTlNWdzBNUWErSm4yYUpTc2l1UzVyZ0tLVlcybXIyclR2WjhHWVlPTnRuaXpRSGZQd1VUL010dnRrbW9vc1A5YnJ1TjMxRVVIWmY1Nnhla21jUDk3NUVvUG1BZUlXVGNXRzNkejJmUWNPU1hxbkJGY044UEpIVTFNSjBybFhhbUNYNGZ3eVkrOUhiV3cyZUNQTTY5Nk55cXh5eUkwdEpOYzNyTDVxSkltVDguLi5CdkpjVVFIK1FEWHNwbHZRa1lieENqRytxNDQvS2xLdG13NDdKUXRzSnQyYXNZdkdBTTFpSTB3T29zekhpOUxtYjNMRGg2dHVjc2tSSGtmTDM0ODdqelpDQ2hJNi8yVllZL3ZUaitrZWVPV0lOTmtVWkxVZTB1ejFqcWdFRlh1dkZVcnFQMzd5UHJpRWcrN2lMMjJwb1JBSVJXL0YwdVpBeVIvTnNpUXBPQ2VVTUJqcDhcXHUwMDNkXCIsXCJlcGhlbWVyYWxQdWJsaWNLZXlcIjpcIkJBaCtrRXVXWXdRdWxNU1J4aTFYOFdHYXdZWWZoU3BYenJmZEowK3FsbkNMRUE5R2tsRzJEdGwraHltSm5qamJVSHNjUE9lZCtWVDVWcGtySlowRFpBa1xcdTAwM2RcIixcInRhZ1wiOlwiYUVESHpsSGRJMlVoL3BrVDkvRnJRMjg1K0F2U2pkcGtYZnl5eFladTc5SVxcdTAwM2RcIn0iCn0=",
    "signature": "3cfdd28f00ae8f3db6f4dfb816af3a693e0719c8"
  }
}    

```

where `container` is BASE64 encoded JSON object which have next structure:

Google Pay container structure

```
{
  "signature": "MEYCIQDN2b4yywOOLnndqZ/d4nPrjebt...EoNh5XXRTJsrbM8O4OpS0kjCLN3p5",
  "intermediateSigningKey": {
    "signedKey": "{\"keyValue\":\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcD...+SoL6G8Q34oRhEx5iUu3KUAeTSl3JjAmi226tTD+Py2Q\\u003d\\u003d\",\"keyExpiration\":\"1749804976000\"}",
    "signatures": [
      "MEYCIQDe7PqsDkcgSW///V/pJomACq/3jPq+vvba/...PUrsIZKSbwNaUZDZqWIT1oARCU"
    ]
  },
  "protocolVersion": "ECv2",
  "signedMessage": "{\"encryptedMessage\":\"yMuwPaQGTjvL8pCEsConA0NSVw0MQa+Jn2aJSsiuS5rgKKVW2mr2rTvZ8GYYONtnizQHfPwUT/MtvtkmoosP9bruN31EUHZf56xekmcP975EoPmAeIWTcWG3dz2fQcOSXqnBFcN8PJHU1MJ0rlXamCX4fwyY+9HbWw2eCPM696NyqxyyI0tJNc3rL5qJImT8...BvJcUQH+QDXsplvQkYbxCjG+q44/KlKtmw47JQtsJt2asYvGAM1iI0wOoszHi9Lmb3LDh6tucskRHkfL3487jzZCChI6/2VYY/vTj+keeOWINNkUZLUe0uz1jqgEFXuvFUrqP37yPriEg+7iL22poRAIRW/F0uZAyR/NsiQpOCeUMBjp8\\u003d\",\"ephemeralPublicKey\":\"BAh+kEuWYwQulMSRxi1X8WGawYYfhSpXzrfdJ0+qlnCLEA9GklG2Dtl+hymJnjjbUHscPOed+VT5VpkrJZ0DZAk\\u003d\",\"tag\":\"aEDHzlHdI2Uh/pkT9/FrQ285+AvSjdpkXfyyxYZu79I\\u003d\"}"
}

```

# Google Payâ¢ integration instructions

Google Pay payments from Flitt are available both for web and mobile.

Google Pay on web can be integrated with several options:

- with [redirect](/getting-started/redirect/) to Flitt payment page
- with Google Pay button [embedded](/api/embedded-custom/#example-applepaygooglepay-buttons) into your website
- [direct](/api/googlepay-direct) integration using Google Pay API

Google Pay in mobile application can be integrated with Flitt SDK depending on the programming language or framework:

- [Android](/api/mobile/android/)
- [React Native](/api/mobile/googlepay-reactnative/)
- [Flutter](/api/mobile/googlepay-flutter/)
- [in web-view with JavaScript](/api/mobile/googlepay-webview/)

# Integration

Integrating Google Payâ¢ into a website can be done either through:

- [Redirect method](/getting-started/redirect/)
- [Embedded method](/getting-started/embedded/)
- Directly with [Google Pay API](https://developers.google.com/pay/api/web/guides/tutorial).

Redirect and embedded methods require integration only with Flitt's API or SDK and thus less coding and complexity.

Integrating Google Pay with Google Pay API directly requires additional Apple certificates management and encryption/decryption procedures coding.

Direct method also involves different approaches depending on tokenized Primary Account Number (DPAN) or an encrypted payment container is used during payment flow processing.

## Google Pay with redirect to Flitt checkout page

Refer to [create order](/api/create-order/) to create order on your backend or frontend and redirect payer to the checkout page. Google Pay button will automatically appear at checkout page. The payment is processed on Flittâs secure platform, reducing complex coding and the risk of handling sensitive data.

## Google Pay button, embedded to merchant website

Embedded method provides a seamless checkout experience without leaving the merchant website, which can increase conversion rate.

Embedded Google Pay button can be placed in a way to fit the look and feel of the website, providing a more cohesive brand experience.

This type of integration also gives greater control over the checkout process and design.

Meanwhile, this method is more complex than redirect method to implement, requiring more development resources and expertise.

**Example Google Pay button:**

See the Pen [Flitt - Apple, Google Pay buttons](https://codepen.io/flitt/pen/PorvvEw) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

**Verify your domain in Google Pay developer account**

- To embedd Google Pay button from Flitt, you must register all of your web domains where button will be displayed. This relates to top-level domains (for example, site.com) and subdomains (for example, shop.site.com, www.site.com), both production and development sites.
- Tell Flitt to activate your domain with Google.

## Google Pay direct integration

Please follow [Google Pay direct](/api/googlepay-direct/) instructions.

Installment payment is executed in 2 steps (only TBC bank is supported as for now)

## Step 1: Create payment

Refer to [Create order](/api/create-order/) page to create test order with a simple code.

First, you need to create payment token from your backend.

To do this in a proper way, choose your integration type: Redirect/Iframe or Embedded

Send request from backend to /api/checkout/url endpoint:

```
curl -L 'https://sandbox.pay.flitt.dev/api/checkout/url' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "server_callback_url": "https://testapi.com/api/callback/",
    "order_id": "test_installment_1",
    "currency": "GEL",
    "merchant_id": 1549901,
    "payment_systems": "installments",
    "payment_method": "x",
    "order_desc": "Test installment payment",
    "amount": 10000,
    "response_url": "https://example.com",
    "signature": "1570574166888217a8d5fb78227ff17c1488be72"
  }
}'

```

The response will contain the checkout URL. Redirect customer to this URL or load it in Iframe.

```
{
   "response": {
       "checkout_url": "https://sandbox.pay.flitt.dev/merchants/7ee242403e07af2d3fe9f208b66faec8bae2fe96/default/index.html?token=93dfba14daaa2cb01916606b54d0f3e935786cf7",
       "payment_id": "150009301",
       "response_status": "success"
   }
}

```

Send request from backend to /api/checkout/token endpoint:

```
curl -L 'https://sandbox.pay.flitt.dev/api/checkout/token' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "server_callback_url": "https://testapi.com/api/callback/",
    "order_id": "test_installment_1",
    "currency": "GEL",
    "merchant_id": 1549901,
    "payment_systems": "installments",
    "payment_method": "x",
    "order_desc": "Test installment payment",
    "amount": 10000,
    "response_url": "https://example.com",
    "signature": "1570574166888217a8d5fb78227ff17c1488be72"
  }
}'

```

The response will contain the payment token.

```
{
    "response": {
        "token": "3bd24c7be3bb750d60c2188df3e392bf9c2d3646",
        "response_status": "success"
    }
}

```

Follow instructions on [Embedded](api/embedded-custom/#example-with-order-created-on-backend) checkout page to complete integration.

Pay attention

To create installment payment, the mandatory parameters

`payment_systems = installments`

`payment_method = tbc|x`

must be sent during create order request.

Supported values for `payment_method` are:

| Value | Description                                                          |
| ----- | -------------------------------------------------------------------- |
| `tbc` | TBC Bank                                                             |
| `x`   | Demo Bank for testing purpose only. See [Testing](/api/testing) page |

Order can be created only within [Redirect](/getting-started/redirect/) or [Embedded](api/embedded-custom/#example-with-order-created-on-backend) flow and yet not supported for [Direct](/getting-started/direct/).

Refer to [create order](/api/create-order/) and [parameters](/api/order-parameters/) specifications to get details on how to create order.

## Step 2: Strong Customer Authentication (SCA)

After the order is created, in case of [Redirect](/getting-started/redirect/) flow customer need to be redirected to `checkout_url` URL for Strong Customer Authentication within TBC bank.

Buy Now, Pay Later (BNPL) and installment payments allow customers to split the cost of a purchase into multiple payments.

Customers may choose to pay in 4 equal installments with 0% fees or extend the repayment period beyond 4 months with applicable interest.

The repayment period is selected by the customer during the checkout process.

The minimum transaction amount for this payment method is 50 GEL.

The pre-approved customer limit for BNPL and installment payments typically ranges from 50 GEL to 5,000 GEL.

BNPL and installments are only supported for TBC bank customers. Other Georgian banks will be implemented soon.

# API Reference

Flitt API provides powerful tools for implementation of online payments scenarios. You can develope your own payment flow of any type of complexity in a simple way with Flitt API: card payments, 3DSecure, subscriptions, splits, mobile wallets (Apple, Google Pay), online banking (Open Banking), electronic fiscalisation, etc.

API is organized around FORM-encoded request \<-> response or JSON-encoded request \<-> response bodies flow. So you can choose FORM or JSON for request body, and response body will have the same format as request.

You can use the Flitt API in [test mode](/api/testing/) without any functionality restrictions. Depending on merchant test or live status you use, all requests are executed in corresponding test or live mode. Test mode never affects your live finances.

## Authentication

All API requests must be made over HTTPS with method POST. Flitt uses parameter `signature` to authenticate each request. Signature is a result of SHA1 hash function, generated by merchant with its payment key.

Use payment key to build `signature` for each API request according to section [Building signature](/api/building-signature/). API request example:

```
curl -L 'https://pay.flitt.com/api/checkout/url' \
-H 'Content-Type: application/json' \
-d '{
    "request": {
        "server_callback_url": "...",
        "order_id": "test_order1231",
        "currency": "GEL",
        "merchant_id": 1549901,
        "order_desc": "Test payment",
        "amount": 100,
        "signature": "487690517384b11725ac02d37f79fe677174291f"
    }
}'

```

Use test payment key, merchant id and cards from [Testing mode](/api/testing/) section.

Note

When your merchant is in test mode, response can contain additional parameter `response_signature_string` which will be absent in the live mode. This is useful to analyze the reasons when request is rejected because an incorrect signature is build in request.

Warning

Do not send any sensitive information to Flitt API with test payment key and merchant taken from [Testing mode](/api/testing/) section.

## Declines and errors

**Normal** response means that the request is processed successfully. Normal response contains `"response_status": "success"`

Normal response

```
{
    "response": {
        "checkout_url": "https://pay.flitt.com/merchants/..../index.html?token=...",
        "payment_id": "738303484",
        "response_status": "success"
    }
}

```

**Decline** is a normal response, when request is processed successfully, but payment declined by some reason. Response with declined payment contains `response_code` and `response_description` parameters. Please refer [Response codes](/api/response-codes) section.

Normal response with decline

```
{
   "response": {
       "rrn": "",
       "masked_card": "444411XXXXXX6666",
       "sender_cell_phone": "",
       "sender_account": "",
       "currency": "GEL",
       "fee": "",
       "reversal_amount": "0",
       "settlement_amount": "0",
       "actual_amount": "",
       "response_description": "General decline",
       "sender_email": "",
       "order_status": "declined",
       "response_status": "success",
       "order_time": "27.09.2022 22:43:38",
       "actual_currency": "",
       "order_id": "TestOrder238947272719",
       "tran_type": "purchase",
       "eci": "",
       "settlement_date": "",
       "payment_system": "card",
       "approval_code": "",
       "merchant_id": 1549901,
       "settlement_currency": "",
       "payment_id": 526886172,
       "card_bin": 444411,
       "response_code": 1000,
       "card_type": "VISA",
       "amount": "200",
       "signature": "fd5d3d61698ad80e91415eea42180db91b90fddd",
       "product_id": "",
       "merchant_data": "",
       "rectoken": "",
       "rectoken_lifetime": "",
       "verification_status": "",
       "parent_order_id": ""
   }
}

```

**Error** is returned in response when Flitt payment gateway can't process the request. In this case, response contains `error_message` and `error_code` parameters and `"response_status": "failure"`.

Response with error

```
{
    "response": {
        "error_code": 1011,
        "error_message": "Parameter `amount` is missing",
        "request_id": "eZIT2An0VLAY2",
        "response_status": "failure"
    }
}

```

# Accept purchase

Get order status

`POST /api/status/order_id`

This endpoint expects `POST` request in `JSON` format with [parameters](/api/order-status/#__tabbed_1_1).

Normal response will contain the same parameters, as accept purchase [normal response](/api/order-parameters/#__tabbed_1_2).

| Parameters    | Type         | Mandatory | Description                                                                                                                                                                                                            |
| ------------- | ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `version`     | string(10)   | optional  | Protocol version. Default value: 1.0.1 Version 1.0 is deprecated                                                                                                                                                       |
| `order_id`    | string(1024) | mandatory | Order ID which is generated by merchant                                                                                                                                                                                |
| `merchant_id` | integer(12)  | mandatory | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                                    |
| `signature`   | string(40)   | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response |

see [response parameters](/api/order-parameters/#__tabbed_1_2)

Examples

```
curl -L 'https://pay.flitt.com/api/transaction_list' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "version": "1.0.1",
    "order_id": "TestOrder1",
    "merchant_id": "1549901",
    "signature": "f62ae444f85ef2dd936e064960698e1fa1be6e92"
  }
}'

```

```
{
    "response": [
        {
            "id": 2008762318,
            "payment_id": 812945884,
            "parent_tran_id": null,
            "timestart": "22.08.2024 00:51:11",
            "timeend": "22.08.2024 00:51:16",
            "duration": 4492,
            "merchant_id": 1549901,
            "tran_type": "purchase",
            "sender_country": "US",
            "sender_email": "test@test.com",
            "amount": 20.0,
            "currency": "GEL",
            "actual_amount": 302.35,
            "actual_currency": "GEL",
            "expire_month": "08",
            "expire_year": "2024",
            "cavv": "CAACByOHgGKTUReYJYeAAAAAAAA=",
            "eci": "05",
            "md": "2008762318",
            "veres_status": "Y",
            "pares_status": "Y",
            "ipaddress_v4": "178.54.60.26",
            "payment_system": "card",
            "card_last_digits": "1111",
            "card_bin": "444455",
            "reversal_amount": 0.0,
            "capture_amount": null,
            "sender_approval_code": "123456",
            "sender_rrn": "111111111111",
            "capture_status": null,
            "transaction_status": "approved",
            "response_code": null,
            "settlement_amount": 0.0,
            "settlement_currency": null,
            "settlement_date": null,
            "fee": null,
            "preauth": false,
            "settlement_status": null,
            "rectoken": null,
            "istest": true,
            "client_fee": 0.0,
            "ip_country": "UA",
            "verification_code": null,
            "receiver_rrn": null,
            "receiver_approval_code": null,
            "receiver_country": null,
            "protocol": "alfa",
            "rectoken_lifetime": null,
            "order_id": "TestOrder31",
            "binmanagement_enabled": "True",
            "masked_card": "444455XXXXXX1111",
            "card_type": "VISA"
        }
    ]
}

```

```
{
    "response": {
        "error_code": 1002,
        "error_message": "Application error",
        "request_id": "VkPdYwnPAaSz9",
        "response_status": "failure"
    }
}

```

```
{
    "response": []
}

```

Open banking payment is executed in 2 steps

## Step 1: Create payment

Refer to [Create order](/api/create-order/) page to create test order with a simple code.

First, you need to create payment token from your backend.

To do this in a proper way, choose your integration type: Redirect/Iframe or Embedded

Send request from backend to /api/checkout/url endpoint:

```
curl -L 'https://pay.flitt.com/api/checkout/url' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "server_callback_url": "https://testapi.com/api/callback/",
    "order_id": "test_open_banking4",
    "currency": "GEL",
    "merchant_id": 1549901,
    "payment_systems": "opb",
    "payment_method": "x",
    "order_desc": "Test open banking payment",
    "amount": 99999,
    "response_url": "https://example.com",
    "signature": "035acfeca204b350957f45d3f9f6385eafe9cf6b"
  }
}'

```

The response will contain the checkout URL. Redirect customer to this URL or load it in Iframe.

```
{
   "response": {
       "checkout_url": "https://pay.flitt.com/merchants/7ee242403e07af2d3fe9f208b66faec8bae2fe96/default/index.html?token=93dfba14daaa2cb01916606b54d0f3e935786cf7",
       "payment_id": "150009301",
       "response_status": "success"
   }
}

```

Send request from backend to /api/checkout/token endpoint:

```
curl -L 'https://pay.flitt.com/api/checkout/token' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "server_callback_url": "https://testapi.com/api/callback/",
    "order_id": "test_open_banking4",
    "currency": "GEL",
    "merchant_id": 1549901,
    "payment_systems": "opb",
    "payment_method": "x",
    "order_desc": "Test open banking payment",
    "amount": 99999,
    "response_url": "https://example.com",
    "signature": "035acfeca204b350957f45d3f9f6385eafe9cf6b"
  }
}'

```

The response will contain the payment token.

```
{
    "response": {
        "token": "3bd24c7be3bb750d60c2188df3e392bf9c2d3646",
        "response_status": "success"
    }
}

```

Follow instructions on [Embedded](api/embedded-custom/#example-with-order-created-on-backend) checkout page to complete integration.

Pay attention

To create Open Banking Payment, the mandatory parameter `payment_systems = opb` must be sent during create order request.

Additionally `payment_method` parameter can be sent if payment have to be processed through a specified issuing bank.

Supported values for `payment_method` are:

| Value     | Description                                                          |
| --------- | -------------------------------------------------------------------- |
| `tbc`     | TBC Bank                                                             |
| `bog`     | Bank of Georgia                                                      |
| `liberty` | Liberty Bank                                                         |
| `credo`   | Credo Bank                                                           |
| `x`       | Demo Bank for testing purpose only. See [Testing](/api/testing) page |

Order can be created only within [Redirect](/getting-started/redirect/) or [Embedded](api/embedded-custom/#example-with-order-created-on-backend) flow and yet not supported for [Direct](/getting-started/direct/).

Refer to [create order](/api/create-order/) and [parameters](/api/order-parameters/) specifications to get details on how to create order.

## Step 2: Strong Customer Authentication (SCA)

After the order is created, customer need to be redirected to `checkout_url` URL for Strong Customer Authentication within his bank.

## How it works

If only `payment_systems = opb` specified, then customer will be redirected to Flitt checkout page.

On the checkout page customer will choose his bank and will be redirected to SCA page of his bank.

If additionally `payment_method` is sent, customer will be redirected to SCA page of his bank without visiting Flitt checkout page:

Open Banking payments are transactions processed in accordance with the Open Banking standard in Georgia.

This payment method enables merchants to accept direct bank payments securely and efficiently.

It is aligned with the Payment Services Directive 2 (PSD2), which mandates Strong Customer Authentication (SCA) to enhance security.

# Accept purchase

Request parameters

| Parameters            | Type         | Mandatory | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------- | ------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `version`             | string(10)   | optional  | Protocol version. Default value: 1.0.1 Version 1.0 is deprecated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `order_id`            | string(1024) | mandatory | Order ID which is generated by merchant                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `merchant_id`         | integer(12)  | mandatory | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `order_desc`          | string(1024) | mandatory | Order description. Generated by merchant in UTF-8 always                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `amount`              | integer(12)  | mandatory | Order amount without separator. 1020 (GEL) means 10 lari and 20 tetri                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `currency`            | string(3)    | mandatory | Order currency. Supported values: EUR â Euro USD â US Dollar GBP â Pound sterling mandatory CZK â Czech Republic Koruna GEL - Georgian lari UZS - Uzbekistan sum [Full list of supported currencies](/api/currencies/)                                                                                                                                                                                                                                                                                                                                        |
| `card_number`         | string(19)   | optional  | Payer card number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `cvv2`                | string(4)    | optional  | Card CVV2/CVC2 code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `expiry_date`         | string(4)    | optional  | Card expiry date in format MMYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `client_ip`           | string(4)    | optional  | Client IP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `server_callback_url` | string(2048) | optional  | Merchant site URL, where host-to-host callback will be sent after payment completion. See [Callbacks](/api/callbacks/) for more details on callbacks.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `signature`           | string(40)   | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response                                                                                                                                                                                                                                                                                                                                        |
| `lifetime`            | integer(9)   | optional  | Order lifetime in seconds. After this period of time, the order will change status to âexpiredâ if the client has not paid it Default value: 36000 Maximum allowed value: 69120000                                                                                                                                                                                                                                                                                                                                                                            |
| `merchant_data`       | string(2048) | optional  | Any arbitrary set of data that a merchant wants to get back in the response to `response_url` or/and `server_callback_url`, and also in reports                                                                                                                                                                                                                                                                                                                                                                                                               |
| `preauth`             | string(1)    | optional  | Parameter supported only for Visa/MasterCard payment method **N** â the amount is debited from the customerâs card immediately and settled to the merchant account, in accordance with the rules of settlements. **Y** â amount is held on the customer card account and not charged until the merchant sends a `capture` request to confirm. Default value: **N**                                                                                                                                                                                            |
| `sender_email`        | string(256)  | optional  | Customer email                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `delayed`             | string(1)    | optional  | [Delayed order](/api/delayed/) flag. **Y** â allows the customer to pay the order during period sent by the merchant in lifetime parameter. Merchant must expect several host-to-host callbacks and browser redirects at the same order. Customer will have the possibility to try to pay the same `order_id`, if the previous attempt failed **N** â after payment is declined `order_id` customer will be redirected to the merchant site to recreate the order. In this case, only one callback will be sent to `server_callback_url` Default value: **Y** |
| `lang`                | string(2)    | optional  | Payment page language. Supported values: az â Azerbaijani da â Danish nl â Dutch fi â Finnish ka â Georgian ko â Korean ru â Russian zh â Chinese uk â Ukrainian en â English lv â Latvian fr â French cs â Czech ro â Romanian it â Italian sk â Slovak pl â Polish es â Spanish hu â Hungarian de â German                                                                                                                                                                                                                                                  |
| `product_id`          | string(1024) | optional  | Merchant product or service id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `required_rectoken`   | string(1)    | optional  | Flag which indicates whether card token will be returned in response. See [Recuring payment](/getting-started/recurring/) Default value: N                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `verification`        | string(1)    | optional  | If **Y** sent, order will be automatically reversed after successful approval Default value: **N**                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `rectoken`            | string(40)   | optional  | Card token for recurring transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `cavv`                | string(2048) | optional  | Card 3DSecure authentication result CAVV value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `eci`                 | string(2048) | optional  | Card 3DSecure authentication result ECI value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `wallet`              | string(2048) | optional  | Wallet type: `applepay` or `googlepay`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `schemeid`            | string(2048) | optional  | Identifier of CIT - client initiated transaction, returned in initial purchase in field `additional_info->schemeid`, see [response parameters](/api/order-parameters/#__tabbed_2_2)                                                                                                                                                                                                                                                                                                                                                                           |

see [response parameters](/api/order-parameters/#__tabbed_1_2)

Examples

**Request example:**

```
{
  "request": {
    "order_id": "test_12343242",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "amount": 1000,
    "currency": "GEL",
    "card_number": "4444555566661111",
    "cvv2": "111",
    "expiry_date": "1125",
    "client_ip": "8.8.8.8",
    "server_callback_url": "https://myserver.com/callback",
    "signature": "0c0c2374c73267e7be560d80834e4ba28ccda7aa"
  }
}

```

**Normal final response:** see [list of test cards](/api/testing/)

```
{
  "response": {
    "rrn": "111111111111",
    "masked_card": "444455XXXXXX1111",
    "sender_cell_phone": "",
    "sender_account": "",
    "currency": "GEL",
    "fee": "",
    "reversal_amount": "0",
    "settlement_amount": "0",
    "actual_amount": "200",
    "response_description": "",
    "sender_email": "test@test.com",
    "order_status": "approved",
    "response_status": "success",
    "order_time": "13.07.2024 01:23:59",
    "actual_currency": "GEL",
    "order_id": "test33694502191",
    "tran_type": "purchase",
    "eci": "5",
    "settlement_date": "",
    "payment_system": "card",
    "approval_code": "123456",
    "merchant_id": 1549901,
    "settlement_currency": "",
    "payment_id": 805243692,
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "200",
    "signature": "b7884b5c4906956fbac4d20390388d913a78c0b0",
    "product_id": "",
    "merchant_data": "Test merchant data",
    "rectoken": "",
    "rectoken_lifetime": "",
    "verification_status": "",
    "parent_order_id": "",
    "fee_oplata": "0",
    "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_test\": true}",
    "response_signature_string": "**********|200|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_**********\": true}|200|123456|444455|VISA|GEL|5|0|444455XXXXXX1111|Test merchant data|1549901|**********33694502191|approved|13.07.2024 01:23:59|805243692|card|success|0|111111111111|**********@**********.com|0|purchase"
  }
}

```

**Normal response if 3DSecure is required:** see [list of 3DSecure test cards](/api/testing)

```
{
    "response": {
        "response_status": "success",
        "acs_url": "https://pay.flitt.com/test/testacs/",
        "pareq": "eJxtU21vgjAQ/u6vIP4A+gJRNKVJHUvUiRpwS/aRYYNsgljA6b8fLTpFuISE5+5pe/fcHdnsBOeOz8NScNrTKiMuz/Mg4lq8tfuDyqxRv46o6Jp5/HjHynfiIo8PKUU61DEBN9gkuVyEuyAtmm4VCsLjZLakpjUyDUTAFbZ5CRczhxpDDCsjoIZtWhoknC7Y5mM2Z762Zv6GaRO2fGMEqFD7RHgo00JcqIktAm6gTSvFnu6KIsvHQD6uysn1ffal708EyGizZNBdM1mX0p13ZXKOt9R12O/Th5ffn3jl/NgESEb73DYoOMUQmdDCloaGY4jGaECA8nconsgiKdYh1F7fvUrz2tFmZjJXdqVL1R8dHUqWQvA0vNDRUEp5Q20iP2eHlMtLCfj/f5KvWyfyMu2cobCopsFNVsZ8yhdHL1rNkedH0Ev8yLblVClCZyZx1W4DozqV+Ln3BDy+WKV1XwHZYrUttEdAY5f+AHcC0ak=",
        "md": "2001876637"
    }
}

```

**Response in case of error:**

```
{
    "response": {
        "error_code": 1011,
        "error_message": "Parameter `amount` is missing",
        "request_id": "5htKi0wf7zEHn",
        "response_status": "failure"
    }
}

```

# Accept payment with saved card

Request parameters

| Parameters            | Type         | Mandatory | Description                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `version`             | string(10)   | optional  | Protocol version. Default value: 1.0.1 Version 1.0 is deprecated                                                                                                                                                                                                                                                                                                   |
| `order_id`            | string(1024) | mandatory | Order ID which is generated by merchant                                                                                                                                                                                                                                                                                                                            |
| `merchant_id`         | integer(12)  | mandatory | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                                                                                                                                                                                |
| `order_desc`          | string(1024) | mandatory | Order description. Generated by merchant in UTF-8 always                                                                                                                                                                                                                                                                                                           |
| `amount`              | integer(12)  | mandatory | Order amount without separator. 1020 (GEL) means 10 lari and 20 tetri                                                                                                                                                                                                                                                                                              |
| `currency`            | string(3)    | mandatory | Order currency. Supported values: EUR â Euro USD â US Dollar GBP â Pound sterling mandatory CZK â Czech Republic Koruna GEL - Georgian lari UZS - Uzbekistan sum [Full list of supported currencies](/api/currencies/)                                                                                                                                             |
| `rectoken`            | string(40)   | mandatory | Card token for recurring transactions.                                                                                                                                                                                                                                                                                                                             |
| `signature`           | string(40)   | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response                                                                                                                                             |
| `cvv2`                | string(4)    | optional  | Card CVV2/CVC2 code                                                                                                                                                                                                                                                                                                                                                |
| `client_ip`           | string(4)    | optional  | Client IP                                                                                                                                                                                                                                                                                                                                                          |
| `server_callback_url` | string(2048) | optional  | Merchant site URL, where host-to-host callback will be sent after payment completion. See [Callbacks](/api/callbacks/) for more details on callbacks.                                                                                                                                                                                                              |
| `lifetime`            | integer(9)   | optional  | Order lifetime in seconds. After this period of time, the order will change status to âexpiredâ if the client has not paid it Default value: 36000 Maximum allowed value: 69120000                                                                                                                                                                                 |
| `merchant_data`       | string(2048) | optional  | Any arbitrary set of data that a merchant wants to get back in the response to `response_url` or/and `server_callback_url`, and also in reports                                                                                                                                                                                                                    |
| `preauth`             | string(1)    | optional  | Parameter supported only for Visa/MasterCard payment method **N** â the amount is debited from the customerâs card immediately and settled to the merchant account, in accordance with the rules of settlements. **Y** â amount is held on the customer card account and not charged until the merchant sends a `capture` request to confirm. Default value: **N** |
| `sender_email`        | string(256)  | optional  | Customer email                                                                                                                                                                                                                                                                                                                                                     |
| `product_id`          | string(1024) | optional  | Merchant product or service id                                                                                                                                                                                                                                                                                                                                     |

see [response parameters](/api/order-parameters/#__tabbed_1_2)

Examples

**Request example:**

```
{
  "request": {
    "order_id": "test_12343242",
    "merchant_id": "1549901",
    "order_desc": "Test order",
    "amount": 1000,
    "currency": "GEL",
    "rectoken": "JcZoqYNosx1HjDoHXWlFU0avVnzYsFAbLBbA",
    "server_callback_url": "https://myserver.com/callback",
    "signature": "0c0c2374c73267e7be560d80834e4ba28ccda7aa"
  }
}

```

**Normal final response:** see [list of test cards](/api/testing/)

```
{
  "response": {
    "rrn": "111111111111",
    "masked_card": "444455XXXXXX1111",
    "sender_cell_phone": "",
    "sender_account": "",
    "currency": "GEL",
    "fee": "",
    "reversal_amount": "0",
    "settlement_amount": "0",
    "actual_amount": "1000",
    "response_description": "",
    "sender_email": "test@test.com",
    "order_status": "approved",
    "response_status": "success",
    "order_time": "13.07.2024 01:23:59",
    "actual_currency": "GEL",
    "order_id": "test_12343242",
    "tran_type": "purchase",
    "eci": "5",
    "settlement_date": "",
    "payment_system": "card",
    "approval_code": "123456",
    "merchant_id": 1549901,
    "settlement_currency": "",
    "payment_id": 805243692,
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "1000",
    "signature": "b7884b5c4906956fbac4d20390388d913a78c0b0",
    "product_id": "",
    "merchant_data": "Test merchant data",
    "rectoken": "",
    "rectoken_lifetime": "",
    "verification_status": "",
    "parent_order_id": "",
    "fee_oplata": "0",
    "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_test\": true}",
    "response_signature_string": "**********|200|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_**********\": true}|200|123456|444455|VISA|GEL|5|0|444455XXXXXX1111|Test merchant data|1549901|**********33694502191|approved|13.07.2024 01:23:59|805243692|card|success|0|111111111111|**********@**********.com|0|purchase"
  }
}

```

**Response in case of error:**

```
{
    "response": {
        "error_code": 1011,
        "error_message": "Parameter `amount` is missing",
        "request_id": "5htKi0wf7zEHn",
        "response_status": "failure"
    }
}

```

# Accept purchase

Request parameters

| Parameters                  | Type          | Mandatory | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `version`                   | string(10)    | optional  | Protocol version. Default value: 1.0.1 Version 1.0 is deprecated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `order_id`                  | string(1024)  | mandatory | Order ID which is generated by merchant                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `merchant_id`               | integer(12)   | mandatory | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `order_desc`                | string(1024)  | mandatory | Order description. Generated by merchant in UTF-8 always                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `amount`                    | integer(12)   | mandatory | Order amount without separator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `currency`                  | string(3)     | mandatory | Order currency. Supported values: AMD â Armenian Dram AZN â Azerbaijanian Manat KZT â Tenge MDL â Moldovian Leu GEL - Georgian lari UZS - Uzbekistan sum [Full list of supported currencies](/api/currencies/)                                                                                                                                                                                                                                                                                                                                                |
| `response_url`              | string(2048)  | optional  | Merchant site URL, where a customer will be redirected after payment completion                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `server_callback_url`       | string(2048)  | optional  | Merchant site URL, where host-to-host callback will be sent after payment completion. See [Callbacks](/api/callbacks/) for more details on callbacks.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `signature`                 | string(40)    | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/)                                                                                                                                                                                                                                                                                                                                                     |
| `lifetime`                  | integer(9)    | optional  | Order lifetime in seconds. After this period of time, the order will change status to âexpiredâ if the client has not paid it Default value: 36000 Maximum allowed value: 69120000                                                                                                                                                                                                                                                                                                                                                                            |
| `merchant_data`             | string(2048)  | optional  | Any arbitrary set of data that a merchant wants to get back in the response to `response_url` or/and `server_callback_url`, and also in reports                                                                                                                                                                                                                                                                                                                                                                                                               |
| `preauth`                   | string(1)     | optional  | Parameter supported only for Visa/MasterCard payment method **N** â the amount is debited from the customerâs card immediately and settled to the merchant account, in accordance with the rules of settlements. **Y** â amount is held on the customer card account and not charged until the merchant sends a `capture` request to confirm. Default value: **N**                                                                                                                                                                                            |
| `sender_email`              | string(256)   | optional  | Customer email                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `delayed`                   | string(1)     | optional  | [Delayed order](/api/delayed/) flag. **Y** â allows the customer to pay the order during period sent by the merchant in lifetime parameter. Merchant must expect several host-to-host callbacks and browser redirects at the same order. Customer will have the possibility to try to pay the same `order_id`, if the previous attempt failed **N** â after payment is declined `order_id` customer will be redirected to the merchant site to recreate the order. In this case, only one callback will be sent to `server_callback_url` Default value: **Y** |
| `lang`                      | string(2)     | optional  | Payment page language. Supported values: az â Azerbaijani da â Danish nl â Dutch fi â Finnish ka â Georgian ko â Korean ru â Russian zh â Chinese uk â Ukrainian en â English lv â Latvian fr â French cs â Czech ro â Romanian it â Italian sk â Slovak pl â Polish es â Spanish hu â Hungarian de â German                                                                                                                                                                                                                                                  |
| `product_id`                | string(1024)  | optional  | Merchant product or service id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `required_rectoken`         | string(1)     | optional  | Flag which indicates whether card token will be returned in response. See [Recuring payment](/getting-started/recurring/) Default value: N                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `verification`              | string(1)     | optional  | If **Y** sent, order will be automatically reversed after successful approval Default value: **N**                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `rectoken`                  | string(40)    | optional  | Card token for recurring transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `receiver_rectoken`         | string(40)    | optional  | Card token for payout transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `design_id`                 | string(6)     | optional  | ID of checkout design which is set in merchant portal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `subscription`              | string(1)     | optional  | **Y** â enable scheduled payments **N** â by default, disable scheduled payments                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `subscription_callback_url` | string(2048)  | optional  | Merchant site URL, where host-to-host callback will be sent after scheduled payment completion                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `chargeback_callback_url`   | string(2048)  | optional  | Url for chargeback callbacks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `cancel_url`                | string(2048)  | optional  | The URL, where customer will be redirected if clicks "Cancel" button on checkout page                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `reservation_data`          | string(10000) | optional  | BASE64 encoded JSON data, refer to [Additional Data](/api/reservation_data) details page                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

| Parameters             | Type          | Description                                                                                                                                                                                                                                                                    |
| ---------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `order_id`             | string(1024)  | Order ID which is generated by merchant.                                                                                                                                                                                                                                       |
| `merchant_id`          | integer(12)   | Merchant unique ID. Generated by Flitt during merchant registration.                                                                                                                                                                                                           |
| `amount`               | integer(12)   | Order amount in cents without separator                                                                                                                                                                                                                                        |
| `currency`             | string(3)     | Order currency. Supported values: see [Currencies](/api/currencies/)                                                                                                                                                                                                           |
| `order_status`         | string(50)    | Order processing status. Can contain the following values:                                                                                                                                                                                                                     |
| `response_status`      | string(50)    | Request processing status. If parameters sent by merchant did not pass validation then failure, else success                                                                                                                                                                   |
| `signature`            | string(40)    | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response                                                         |
| `tran_type`            | string(50)    | Supported values:                                                                                                                                                                                                                                                              |
| `sender_cell_phone`    | string(16)    | Customer mobile phone number                                                                                                                                                                                                                                                   |
| `sender_account`       | string(16)    | Customer payment account                                                                                                                                                                                                                                                       |
| `masked_card`          | string(19)    | Masked card number                                                                                                                                                                                                                                                             |
| `card_bin`             | integer(6)    | Card bin â usually first 6 digits 444444r                                                                                                                                                                                                                                      |
| `card_type`            | string(50)    | Supported values: VISA, MasterCard, Humo, UzCard                                                                                                                                                                                                                               |
| `rrn`                  | string(50)    | Commonly not unique transaction ID returned by bank.                                                                                                                                                                                                                           |
| `approval_code`        | string(6)     | Commonly not unique authorization code returned by bank.                                                                                                                                                                                                                       |
| `response_code`        | integer(4)    | Order decline response code. Possible codes see in Response codes                                                                                                                                                                                                              |
| `response_description` | string(1024)  | Order response code description, see Response codes                                                                                                                                                                                                                            |
| `reversal_amount`      | integer(12)   | The total amount of all reversals for current order                                                                                                                                                                                                                            |
| `settlement_amount`    | integer(12)   | The settlement amount for current order                                                                                                                                                                                                                                        |
| `settlement_currency`  | string(3)     | The currency of order settlement                                                                                                                                                                                                                                               |
| `order_time`           | string(19)    | Order creation date `DD.MM.YYYY hh:mm:ss`                                                                                                                                                                                                                                      |
| `settlement_date`      | string(10)    | Settlement date in format `DD.MM.YYYY`                                                                                                                                                                                                                                         |
| `eci`                  | integer(2)    | Ecommerce Indicator â parameter specifies whether 3DSecure authentication was performed or not. Supported values: 5 â full 3DSecure authentication performed 6 â merchant supports 3DSecure, but issuing bank does not 7 â neither merchant nor issuing bank supports 3DSecure |
| `fee`                  | integer(12)   | Fee charged by Flitt                                                                                                                                                                                                                                                           |
| `payment_system`       | string(50)    | Payment system which was used for payment. Supported payment systems list see [Supported payment systems](/supported-payment-systems)                                                                                                                                          |
| `sender_email`         | string(254)   | Customer email                                                                                                                                                                                                                                                                 |
| `payment_id`           | integer(19)   | Unique payment ID generated by Flitt payment gateway                                                                                                                                                                                                                           |
| `actual_amount`        | integer(12)   | The actual amount held or charged from card.                                                                                                                                                                                                                                   |
| `actual_currency`      | string(3)     | The actual currency authorized from card                                                                                                                                                                                                                                       |
| `product_id`           | string(1024)  | Merchant product or service ID                                                                                                                                                                                                                                                 |
| `merchant_data`        | string(2048)  | Any arbitrary set of data that a merchant sends in a request                                                                                                                                                                                                                   |
| `verification_status`  | string(50)    | Code verification result.                                                                                                                                                                                                                                                      |
| `rectoken`             | string(40)    | Flag which indicates whether Flitt must return card token â token to access card funds without cardholder interaction                                                                                                                                                          |
| `rectoken_lifetime`    | string(19)    | Token lifetime in format `DD.MM.YYYY hh:mm:ss`                                                                                                                                                                                                                                 |
| `additional_info`      | string(20480) | Additional field in JSON format                                                                                                                                                                                                                                                |

Examples

```
{
  "request": {
    "version": "1.0.1",
    "order_id": "TestOrder2",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "amount": 1000,
    "currency": "GEL",
    "response_url": "http://myshop/thank_you_page",
    "server_callback_url": "http://myshop/callback/",
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}

```

```
{
  "response": {
    "rrn": "111111111111",
    "masked_card": "444455XXXXXX1111",
    "sender_cell_phone": "",
    "sender_account": "",
    "currency": "GEL",
    "fee": "",
    "reversal_amount": "0",
    "settlement_amount": "0",
    "actual_amount": "200",
    "response_description": "",
    "sender_email": "test@test.com",
    "order_status": "approved",
    "response_status": "success",
    "order_time": "13.07.2024 01:23:59",
    "actual_currency": "GEL",
    "order_id": "test33694502191",
    "tran_type": "purchase",
    "eci": "5",
    "settlement_date": "",
    "payment_system": "card",
    "approval_code": "123456",
    "merchant_id": 1549901,
    "settlement_currency": "",
    "payment_id": 805243692,
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "200",
    "signature": "b7884b5c4906956fbac4d20390388d913a78c0b0",
    "product_id": "",
    "merchant_data": "Test merchant data",
    "rectoken": "",
    "rectoken_lifetime": "",
    "verification_status": "",
    "parent_order_id": "",
    "fee_oplata": "0",
    "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_test\": true}",
    "response_signature_string": "**********|200|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_**********\": true}|200|123456|444455|VISA|GEL|5|0|444455XXXXXX1111|Test merchant data|1549901|**********33694502191|approved|13.07.2024 01:23:59|805243692|card|success|0|111111111111|**********@**********.com|0|purchase"
  }
}

```

```
{
    "response": {
        "error_code": 1011,
        "error_message": "Parameter `amount` is missing",
        "request_id": "5htKi0wf7zEHn",
        "response_status": "failure"
    }
}

```

# Order status

Get order status

`POST /api/status/order_id`

This endpoint expects `POST` request in `JSON` format with [parameters](/api/order-status/#__tabbed_1_1).

Normal response will contain the same parameters, as accept purchase [normal response](/api/order-parameters/#__tabbed_1_2).

| Parameters    | Type         | Mandatory | Description                                                                                                                                                                                                            |
| ------------- | ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `version`     | string(10)   | optional  | Protocol version. Default value: 1.0.1 Version 1.0 is deprecated                                                                                                                                                       |
| `order_id`    | string(1024) | mandatory | Order ID which is generated by merchant                                                                                                                                                                                |
| `merchant_id` | integer(12)  | mandatory | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                                    |
| `signature`   | string(40)   | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response |

see [response parameters](/api/order-parameters/#__tabbed_1_2)

Examples

```
curl -L 'https://pay.flitt.com/api/status/order_id' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "order_id": "TestOrder2",
    "version": "1.0.1",
    "merchant_id": "1549901",
    "signature": "bb0798a53ab63eb99584859ba46deb9d461b3993"
  }
}'

```

```
{
    "response": {
        "rrn": "",
        "masked_card": "",
        "sender_cell_phone": "",
        "sender_account": "",
        "currency": "GEL",
        "fee": "",
        "reversal_amount": "0",
        "settlement_amount": "0",
        "actual_amount": "",
        "response_description": "",
        "sender_email": "",
        "order_status": "expired",
        "response_status": "success",
        "order_time": "28.02.2018 19:18:16",
        "actual_currency": "",
        "order_id": "TestOrder2",
        "tran_type": "purchase",
        "eci": "",
        "settlement_date": "",
        "payment_system": "",
        "approval_code": "",
        "merchant_id": 1549901,
        "settlement_currency": "",
        "payment_id": 83456044,
        "card_bin": "",
        "response_code": "",
        "card_type": "",
        "amount": "1000",
        "signature": "268b8f189f97c85696134fe6ae0f7f5ab93f28d5",
        "product_id": "",
        "merchant_data": "",
        "rectoken": "",
        "rectoken_lifetime": "",
        "verification_status": "",
        "parent_order_id": "",
        "fee_oplata": "0",
        "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": null, \"transaction_id\": null, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": null, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": null, \"card_product\": null, \"card_category\": null, \"timeend\": \"01.03.2018 05:18:17\", \"ipaddress_v4\": \"52.30.149.20\", \"payment_method\": null}",
        "response_signature_string": "**********|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": null, \"transaction_id\": null, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": null, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": null, \"card_product\": null, \"card_category\": null, \"timeend\": \"01.03.2018 05:18:17\", \"ipaddress_v4\": \"52.30.149.20\", \"payment_method\": null}|1000|GEL|0|1549901|TestOrder2|expired|28.02.2018 19:18:16|83456044|success|0|0|purchase"
    }
}

```

```
{
    "response": {
        "error_code": 1002,
        "error_message": "Application error",
        "request_id": "VkPdYwnPAaSz9",
        "response_status": "failure"
    }
}

```

## Interaction scheme A (with customer redirection to payment page)

```
sequenceDiagram
  Customer->>Merchant: 1. Customer populates shopping cart
  Merchant-->>Customer: 2. Merchant creates HTML form with order details
  Customer->>Merchant: 3. Customer submits payment form
  Merchant->>Flitt: 4. Merchant creates order and <br/>redirects customer to Flitt hosted page
  Flitt-->>Customer: 5. Flitt displays payment page to Customer
  Customer->>Flitt: 6. Customer provides payment details
  Flitt->>Customer`s PI: 7. Flitt checks if 3DSecure or SCA required 
  loop 3DSecure/SCA
    Customer`s PI-->>Customer`s PI: 8. Customer is authenticated if required <br/>by his payment institution
  end
  Customer`s PI->>Flitt: 9. Customer's PI returns authentication result  
  Flitt->>Customer`s PI: 10. Flitt initiates the charge by sending payment request to customer's PI
  Customer`s PI->>Flitt: 11. Customer's PI returns payment result to Flitt
  Flitt-->>Merchant: 12. Flitt redirects customer back to Merchant <br/>with order status  
  Merchant-->>Customer: 13. Merchants shows result page to customer with order status
  Flitt-->>Merchant: 14. Flitt sends server-to-server callback <br/>to Merchant with order status   
```

1. Customer chooses products or services in merchant online shop or mobile app and adds them to his cart.
1. Merchant creates HTML form with [request parameters](/api/create-order/) to be submitted to Flitt.
1. At merchant site customer submits HTML form in browser or mobile application.
1. Merchant redirects customer in browser to Flitt url https://pay.flitt.com/api/checkout/redirect/, sending parameters with HTTPS POST method.
1. Flitt creates order and renders hosted payment page with all available methods.
1. Customer provides payment details at payment page on Flitt site.
1. Flitt checks if strong customer authentication is requires.
1. Flitt redirects customer to his payment institution for authentication (3DSecure/password/OTP) via browser.
1. Payment institution returns customer back to Flitt with authentication result.
1. Flitt initiates payment by sending request to customer payment institution (PI).
1. Customer's payment institution returns payment result to Flitt.
1. Flitt redirects customer to merchant site by sending payment result using HTTPS POST or GET.
1. Merchant shows result page with payment details.
1. To ensure that merchant received response with payment details, Flitt also sends callback with payment result parameters to merchant site using host-to-host HTTPS POST.

## Interaction scheme B (with preliminary host-to-host request to get payment page URL)

```
sequenceDiagram
  Customer->>Merchant: 1. Customer populates shopping cart
  Merchant-->>Flitt: 2. Merchant submits JSON request to Flitt url https://pay.flitt.com/api/checkout/url/.
  Flitt->>Merchant: 3. Flitt returns to merchant `checkout_url` parameter
  Merchant->>Customer: 4. Merchant creates order and <br/>redirects customer to Flitt hosted page
  Flitt-->>Customer: 5. Flitt displays payment page to Customer
  Customer->>Flitt: 6. Customer provides payment details
  Flitt->>Customer`s PI: 7. Flitt checks if 3DSecure or SCA required 
  loop 3DSecure/SCA
    Customer`s PI-->>Customer`s PI: 8. Customer is authenticated if required <br/>by his payment institution
  end
  Customer`s PI->>Flitt: 9. Customer's PI returns authentication result  
  Flitt->>Customer`s PI: 10. Flitt initiates the charge by sending payment request to customer's PI
  Customer`s PI->>Flitt: 11. Customer's PI returns payment result to Flitt
  Flitt-->>Merchant: 12. Flitt redirects customer back to Merchant <br/>with order status  
  Merchant-->>Customer: 13. Merchants shows result page to customer with order status
  Flitt-->>Merchant: 14. Flitt sends server-to-server callback <br/>to Merchant with order status   
```

1. Customer chooses products or services in merchant online shop or mobile app and adds them to his cart.
1. Merchant creates JSON request with [request parameters](/api/create-order/) and submit it host-to-host to Flitt url https://pay.flitt.com/api/checkout/url/.
1. Flitt returns to merchant [interim response](/api/create-order/#__tabbed_1_2) with `checkout_url` parameter with URL were customer should be redirected to provide payment details.
1. Merchant redirect customer to Flitt hosted payment page with all available methods.
1. Customer provides payment details at payment page on Flitt site.
1. Flitt checks if strong customer authentication is requires.
1. Flitt redirects customer to his payment institution for authentication (3DSecure/password/OTP) via browser.
1. Payment institution returns customer back to Flitt with authentication result.
1. Flitt initiates payment by sending request to customer payment institution (PI).
1. Customer's payment institution returns payment result to Flitt.
1. Flitt redirects customer to merchant site by sending payment result using HTTPS POST or GET.
1. Merchant shows result page with payment details.
1. To ensure that merchant received response with payment details, Flitt also sends callback with payment result parameters to merchant site using host-to-host HTTPS POST.

## API general

All requests are sent over HTTPS with POST method.

Request and response format is JSON.

The response JSON structure is always a dict (associative array).

If the `err_code` or `error` key is present, the request is not completed. In this case, `err_code` and `error` parameter in response is a error description message.

Key error codes:

- `Authorization token required` â the `token` is not passed in the request header
- `Invalid auth token` â the `token` is either invalid or outdated
- `Merchant not found` â merchant not found
- `you have no access to this report` â either `report_id` is invalid or you have no access to the report

Example of response in case of error

```
{
   "error": "Authorization token required",
   "err_code": "Authorization token required"
}

```

The authorization token must be sent in the `Authorization` HTTP header of your request.

Example of a request header with access token

```
curl 'https://portal.flitt.com/api/extend/company/report/' \
-H "Authorization: Token 4cDY6LgviVN85g70eDHXygrmYTourFAT"

```

## Authentication

Before getting data from report, you need to obtain access token.

A JSON POST request should be sent to endpoint: https://portal.flitt.com/authorizer/token/application/get

Parameters of authentication request

| Parameter        | Mandatory | Type         | Description                                                           | Example                                                                                                                             |
| ---------------- | --------- | ------------ | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `application_id` | mandatory | string(20)   | Company ID. Please contact Flitt support to obtain ID and secret key. | 1234                                                                                                                                |
| `date`           | mandatory | string(1024) | Date in any format. Date is a salt for sha512 signature hash          | 2020-04-06 11:15:27 or 1586171872 or any other string                                                                               |
| `signature`      | mandatory | string(128)  | Signature                                                             | 7eec02ed1088b47da639549a109c0e98 a75e2d8c76dfa33db4ee18359b2ea677 dda37516abc0e439b286261a48d49d3e 2fd885d9f09c8ff5c7308afe4180688a |

The `signature` is formed by concatenating the application private key, application id, and date parameter through a vertical bar | (in utf-8 encoding).

Sha512 hash function should be applied to the resulting string.

Code example of obtaining a signature

```
from datetime import datetime
import hashlib

date = str(datetime.now())
company_id = str(%your_company_id%)
signature = hashlib.sha512('|'.join(['%your_company_private_key%', company_id, date]).encode('utf-8')).hexdigest()

```

```
<?php
$date = strtotime("now");
$company_id = %application_id%;
$signature = hash('sha512', join('|',array('%your_company_private_key%', $company_id, $date)));

```

If request is successful, the token will be contained in the `token` parameter of the JSON response and will expire in 1 hour Otherwise, the response will contain the keys `error_code` and `error_message`.

Example of curl request

```
curl 'https://portal.flitt.com/authorizer/token/application/get' \
    -H "Content-Type: application/json; charset=utf-8" \
    -X POST  --data-binary @- <<EOF
    {
        "signature": "5124cef4e69a015c1662f0ff963adc9f85ff60e365445ffcf6688737da726becb298211e5040c9ac74e3f56ff1065b42c281e300370436bec539f6b2679b91ee",
        "application_id": "2",
        "date": "2024-04-06 11:15:27"
    }
EOF

```

Example of response in case of error

```
{
  "request_id": "SuVhZRMS7JDD2iGS",
  "token": "Yq0GXWeOZ1m8BsiCa4iQPDB84Wjw346",
  "expires_in": 3602
}

```

```
{
  "error_code": 403,
  "error_message": "Incorrect signature",
  "request_id": "cGeC7PH59ESqQw30"
}

```

## Obtain report data

The request should be sent as POST to the endpoint: https://portal.flitt.com/api/extend/company/report/

Parameters of request of obtaining report data

| Parameter     | Mandaroty | Type           | Description                                                                                                | Example                                                                     |
| ------------- | --------- | -------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `filters`     | mandatory | JSON objects[] | A set of filters, individual within each report (report_id)                                                | âfiltersâ: [ { âsâ: âsettlement_dateâ, âmâ: âdateisâ, âvâ: â2019-01-24â } ] |
| `merchant_id` | mandatory | integer(12)    | Merchant unique ID. Generated by Flitt during merchant registration.                                       | 1549901                                                                     |
| `report_id`   | mandatory | integer(12)    | Report unique ID (see List of available reports)                                                           | 688                                                                         |
| `on_page`     | mandatory | integer(12)    | The limit of records that are returned in the context of single request (from 10 to 500 recommended)       | 500                                                                         |
| `page`        | mandatory | integer(12)    | Records page offset. For example, with on_page = 50, to get data from 51 to 100, you need to pass page = 2 | 2                                                                           |

| Parameter      | Mandaroty | Type             | Description                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                       |
| -------------- | --------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`         | mandatory | JSON objects[][] | Dataset as a sorted two-dimensional JSON array                                                                                                                  | âdataâ: \[ [ 1234567890, 10000000001 ], [ 1234567891, 10000000002 ] \]                                                                                                                                                                                                                                                                        |
| `fields`       | mandatory | string[]         | List of returned fields                                                                                                                                         | âfieldsâ: [ âpayment_idâ, âorder_timeâ, âorder_statusâ, âactual_amountâ, âcurrencyâ, âfeeâ, âorder_idâ, âsettlement_amountâ, âsettlement_currencyâ, âsettlement_dateâ, âsettlement_statusâ, âodb_refâ, âtran_timeâ, âsettlement_typeâ, âpayment_systemâ, âsender_emailâ, âorder_descâ, âmerchant_dataâ, âsettlement_descâ, âtransaction_idâ ] |
| `rows_count`   | mandatory | integer(12)      | Number of records in the full data set                                                                                                                          | 500                                                                                                                                                                                                                                                                                                                                           |
| `rows_on_page` | mandatory | integer(12)      | Number of records returned in the context of this request                                                                                                       | 50                                                                                                                                                                                                                                                                                                                                            |
| `rows_page`    | mandatory | integer(12)      | Range offset in the full data set. For example, if rows_on_page = 50 and rows_page = 2, then records from 51 to 100 are returned in the context of this request | 2                                                                                                                                                                                                                                                                                                                                             |

Example of request and response

```
curl 'https://portal.flitt.com/api/extend/company/report/' \
-H "Authorization: Token k1y0qXZ6KgO4GIfkeRlEznao0zbzYdhf" \
-d @- << EOF
{
  "on_page": 10,
  "page": 1,
  "filters": [
    {
      "s": "settlement_date",
      "m": "from",
      "v": "2019-01-24"
    },
    {
      "s": "settlement_date",
      "m": "to",
      "v": "2019-01-27"
    },
    {
      "s": "actual_amount",
      "m": "=",
      "v": "630.00"
    }
  ],
  "merchant_id": 1398432,
  "report_id": "403"
}
EOF

```

```
{
  "data": [
    [
      1234567890,
      "2025-01-23 10:58:38",
      "approved",
      "630.00",
      "GEL",
      "11.97",
      "test-25697841-1",
      "618.03",
      "EUR",
      "2025-01-24 08:00:00",
      "completed",
      "2426012568",
      "2025-01-23 10:58:38",
      "purchase",
      "Visa/MC",
      "test@test.com",
      "Test order 1",
      "[]",
      "Test payment 1",
      10000000001
    ],
    [
      1234567891,
      "2025-01-23 10:56:51",
      "approved",
      "572.86",
      "GEL",
      "10.88",
      "test-94341241-1",
      "561.98",
      "EUR",
      "2025-01-24 08:00:00",
      "completed",
      "2426012568",
      "2025-01-23 10:56:51",
      "purchase",
      "Visa/MC",
      "test2@test.com",
      "Test order 2",
      "[]",
      "Test payment 2",
      10000000002
    ]
  ],
  "rows_count": 2,
  "fields": [
    "payment_id",
    "order_time",
    "order_status",
    "actual_amount",
    "currency",
    "fee",
    "order_id",
    "settlement_amount",
    "settlement_currency",
    "settlement_date",
    "settlement_status",
    "odb_ref",
    "tran_time",
    "settlement_type",
    "payment_system",
    "sender_email",
    "order_desc",
    "merchant_data",
    "settlement_desc",
    "transaction_id"
  ],
  "rows_page": 1,
  "rows_on_page": 10
}

```

## Use filters

`filter` is an array of JSON objects.

Each `filter` object must contain following attributes:

**s** â field name, to which the filter is applied

**m** â search operand (=, \<, > etc., depending on field type )

**v** â field value to be filtered

Filter example

```
[
    {
      "s": "settlement_date",
      "m": "dateis",
      "v": "2019-01-24"
    }
]

```

### Operands depending on field type

Example

**float**: â=â, â>â, â\<â, â!=â, âisnullâ, ânotnullâ

**int**: â=â, â>â, â\<â, â!=â, âanyâ, âisnullâ, ânotnullâ

**date**: âdateisâ, âfromâ, âtoâ, âisnullâ, ânotnullâ, ânotdateâ

**text**: â=â, â!=â, âlikeâ, â!likeâ, âstartâ, âemptyâ, âanyâ, ânotnullâ

**bool**: istrue

**select**: â=â, â!=â, âanyâ

**array**: in_array

**daterange**: âdaterangeâ

### Unobvious search modes

Example

**any**:

`{âsâ: âidâ, âmâ: â=â, âvâ: â10,20,30â}` â filter values specified with comma separator

filter is applied as id in (10,20,30)

**from**:

`{âsâ: âtimestartâ, âmâ: âfromâ, âvâ: â2020-01-10â}` - filter is applied as timestart >= â2020-01-10â

`{âsâ: âtimestartâ, âmâ: âfromâ, âvâ: â-2â}` - filter is applied as timestart >= now() â 2 days

**to**:

`{âsâ: âtimestartâ, âmâ: âtoâ, âvâ: â2020-01-10â}` - filter is applied as timestart < â2020-01-11â

**dateis** â âdaye equalâ â data filtered from specified day start (00:00) till next day start (00:00) (not including next day)

**like** â filters partial fragment match

**!like** â partial fragment must not match

**start** â âstarting fromâ

### List of available reports

Parameters of request of obtaining report data

| Report ID | Fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Mandatory filter fields                                            | Filter example                                                                                                                                                                                                                 | Description                 |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| 500       | `chargeback_createtime` - datetime(YYYY-MM-DD HH24:MI:SS) `tran_id` - integer(12) `sender_email` - string(1000) `status` - string(1000) `tran_timestart` - datetime(YYYY-MM-DD HH24:MI:SS) `tran_timeend` - datetime(YYYY-MM-DD HH24:MI:SS) `tran_type` - string(1000) `protocol` - string(1000) `currency` - string(3) `amount` - decimal(19,2) `payout_date` - datetime(YYYY-MM-DD HH24:MI:SS) `payout_amoun` - datetime(YYYY-MM-DD HH24:MI:SS)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `tran_id` OR `chargeback_createtime`                               | \[ { "on_page": 5, "page": 1, "filters": [ { "s": "chargeback_createtime", "m": "from", "v": "2019-12-11" }, { "s": "chargeback_createtime", "m": "to", "v": "2019-12-13" } ], "merchant_id": 1549901, "report_id": "500" } \] | Chargebacks report          |
| 528       | `tran_id` - integer(12) `parent_tran_id` - integer(12) `sender_email` - string(1000) `status` - string(1000) `tran_timestart` - datetime(YYYY-MM-DD HH24:MI:SS) `tran_timeend` - datetime(YYYY-MM-DD HH24:MI:SS) `tran_type` - string(1000) `currency` - string(3) `actual_amount` - decimal(19,2) `payout_date` - datetime(YYYY-MM-DD HH24:MI:SS) `payout_amoun` - decimal(19,2) `order_desc` - string(1000) `checkout_url` - string(1000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `tran_id` OR `tran_timestart`                                      | \[ { "on_page": 5, "page": 1, "filters": [ { "s": "tran_timestart", "m": "from", "v": "2019-12-11" }, { "s": "tran_timeend", "m": "to", "v": "2019-12-13" } ], "merchant_id": 1549901, "report_id": "528" } \]                 | Success transactions report |
| 745       | `payment_id` - integer(12) `order_timestart` - datetime(YYYY-MM-DD HH24:MI:SS) `order_timeend` - datetime(YYYY-MM-DD HH24:MI:SS) `order_status` - string(1000) `amount` - decimal(19,2) `actual_amount` - decimal(19,2) `transaction_id` - integer(19) `currency` - string(3) `actual_currency` - string(3) `order_type` - string(1000) `approval_code` - string(6) `card_bin` - string(6) `eci` - string(2) `fee` - decimal(19,2) `masked_card` - string(19) `order_id` - string(1000) `payment_system` - string(1000) `response_code` - integer(4) `response_description` - string(1000) `reversal_amount` - decimal(19,2) `rrn` - string(1000) `sender_email` - string(1000) `settlement_amount` - decimal(19,2) `settlement_currency` - string(3) `settlement_date` - datetime(YYYY-MM-DD HH24:MI:SS) `merchant_data` - string(1000) `order_desc` - string(1000) `payer_country` - string(1000) `bank_name` - string(1000) `bank_country` - string(3) `card_expire_date` - datetime(MM/YYYY) `card_brand` - string(1000) `fee_name` - string(1000) `fee_type` - string(1000) `fee_percent_value` - decimal(19,3) `fee_fix_value` - decimal(19,3) | `order_timestart` OR `order_timeend` OR `payment_id` OR `order_id` | \[ { "on_page": 5, "page": 1, "filters": [ { "s": "order_timestart", "m": "from", "v": "2019-12-11" }, { "s": "order_timestart", "m": "to", "v": "2019-12-13" } ], "merchant_id": 1549901, "report_id": "745" } \]             | All transactions report     |
| 969       | `payment_id` - integer(12) `tran_id` - integer(12) `order_id` - string(1000) `tran_timeend` - datetime(YYYY-MM-DD HH24:MI:SS) `actual_amount` - decimal(19,2) `settlement_currency` - string(3) `fee` - decimal(19,2) `settlement_amount` - decimal(19,2) `settlement_date` - datetime(YYYY-MM-DD HH24:MI:SS) `batch_id` - integer(12) `order_type` - string(1000) `order_status` - string(1000) `card_brand` - string(1000) `payment_system` - string(1000) `masked_card` - string(19) `rrn` - integer(12) `approval_code` - string(6) `order_desc` - string(1000) `merchant_data` - string(1000) `payer_country` - string(1000) `bank_name` - string(1000) `card_expire_date` - datetime(MM/YYYY) `card_brand` - string(1000) `fee_name` - string(1000) `fee_type` - string(1000) `fee_percent_value` - decimal(19,3) `fee_fix_value` - decimal(19,3)                                                                                                                                                                                                                                                                                              | `settlement_date` OR `tran_timeend` OR `payment_id` OR `order_id`  | \[ { "on_page": 5, "page": 1, "filters": [ { "s": "settlement_date", "m": "from", "v": "2025-03-11" }, { "s": "settlement_date", "m": "to", "v": "2025-03-12" } ], "merchant_id": 1549901, "report_id": "969" } \]             | Reimbursement report        |

Any request to API must contain root element `request`

```
{
    "request": {
        ...
        {request parameters}
        ...
    }
}

```

Every response will contain root element `response`

```
{
    "response": {
        ...
        {response parameters}
        ...
        "response_status": "success"
    }
}

```

Pay attention

Parameter `response_status` contains status only for HTTP request, but not for payment or reversal or capture status.\
Order status will be returned in `order_status` parameter.\
Reversal status will be returned in `reversal_amount` parameter, which will have not 0 value.\
Capture status will be returned in `capture_status` parameter.

Example

```
{
  "request": {
    "version": "1.0.1",
    "order_id": "test_order_id_132412412",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test order",
    "amount": 10025,
    "response_url": "https://example.com/thankyoupage",
    "server_callback_url": "https://example.com/api/callback",
    "signature": "7f52380cefaf3cb793746e2deeb56cf7cd75d532"
  }
}

```

```
{
  "response": {
    "rrn": "111111111111",
    "masked_card": "444455XXXXXX1111",
    "sender_cell_phone": "",
    "sender_account": "",
    "currency": "GEL",
    "fee": "",
    "reversal_amount": "0",
    "settlement_amount": "0",
    "actual_amount": "200",
    "response_description": "",
    "sender_email": "test@test.com",
    "order_status": "approved",
    "response_status": "success",
    "order_time": "13.07.2024 01:23:59",
    "actual_currency": "GEL",
    "order_id": "test33694502191",
    "tran_type": "purchase",
    "eci": "5",
    "settlement_date": "",
    "payment_system": "card",
    "approval_code": "123456",
    "merchant_id": 1549901,
    "settlement_currency": "",
    "payment_id": 805243692,
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "200",
    "signature": "b7884b5c4906956fbac4d20390388d913a78c0b0",
    "product_id": "",
    "merchant_data": "Test merchant data",
    "rectoken": "",
    "rectoken_lifetime": "",
    "verification_status": "",
    "parent_order_id": "",
    "fee_oplata": "0",
    "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_test\": true}",
    "response_signature_string": "**********|200|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_**********\": true}|200|123456|444455|VISA|GEL|5|0|444455XXXXXX1111|Test merchant data|1549901|**********33694502191|approved|13.07.2024 01:23:59|805243692|card|success|0|111111111111|**********@**********.com|0|purchase"
  }
}

```

Additional parameter `reservation_data` can be sent with [create purchase](/api/order-parameters) request.

Example:

```
{
  "request": {
    "response_url": "https://site.com/responsepage/",
    "order_id": "test_reservation_data_12345",
    "order_desc": "Test payment",
    "currency": "GEL",
    "amount": "100",
    "signature": "dcf5a9a582872bf0ba89bb77a25c3894671b423a",
    "merchant_id": "1549901",
    "reservation_data": "ewogICJwaG9uZW1vYmlsZSI6ICIrMTIzNDU2NzgiLAogICJjdXN0b21lcl9hZGRyZXNzIjogIjE1IGdhbm5ldCBzdHJlZXQgZWxzcGFyayIsCiAgImN1c3RvbWVyX2NvdW50cnkiOiAiVVMiLAogICJjdXN0b21lcl9zdGF0ZSI6ICJOWSIsCiAgImN1c3RvbWVyX25hbWUiOiAiQnJhbmRvbiBOeWF0aGkiLAogICJjdXN0b21lcl9jaXR5IjogIk5ldyBZb3JrIiwKICAiY3VzdG9tZXJfemlwIjogIjE0MDEiLAogICJhY2NvdW50IjogImlkMzI2NDg0ODAiCn0="
  }
}

```

`reservation_data` â it is JSON data, encoded with BASE64 algorithm. It has the following structure:

JSON:

```
{
  "phonemobile": "+12345678",
  "customer_address": "15 gannet street elspark",
  "customer_country": "US",
  "customer_state": "NY",
  "customer_name": "Brandon Nyathi",
  "customer_city": "New York",
  "customer_zip": "1401",
  "account": "id32648480",
  "uuid": "00002415-0000-1000-8000-00805F9B34FB"
}

```

All parameters must be alphanumeric, and contain latin characters, digits and separator symbols

| Parameter name     | Mandatory | Type        | Description                                                                                   | Example                              |
| ------------------ | --------- | ----------- | --------------------------------------------------------------------------------------------- | ------------------------------------ |
| `phonemobile`      | no        | AN(16)      | Cllient mobile phone                                                                          | +12345678                            |
| `customer_address` | no        | AN(1024)    | Client address                                                                                | 15 gannet street elspark             |
| `customer_country` | no        | AN(2)       | Client billing country ISO code                                                               | UK                                   |
| `customer_name`    | no        | AN(1024)    | Payer name                                                                                    | Brandon Nyathi                       |
| `customer_city`    | no        | AN(1024)    | Payer city                                                                                    | New York                             |
| `customer_zip`     | no        | AN(250)     | ZIP code                                                                                      | 1401                                 |
| `account`          | no        | AN(250)     | Client account id in merchant system                                                          | id32648480                           |
| `uuid`             | no        | AN(250)     | Device UUID                                                                                   | 00002415-0000-1000-8000-00805F9B34FB |
| `settlement_id`    | no        | AN(32)      | ID to be passed to settlements reports for reconciliation process automation                  | SettlementID::12311233443            |
| `3ds_mandatory`    | no        | boolean     | Parameter to force payment without 3DS. Can be used only after approval from Flitt risk team. | `true` or `false`                    |
| `fields_custom[]`  | no        | JSON object | JSON list of additional fields to be displayed on checkout                                    |                                      |
| `products[]`       | no        | JSON object | JSON list of products to be fiscalised                                                        |                                      |

`fields_custom` is a JSON object which allows to add custom input fields to checkout page

```
"fields_custom": [
    {
      "name": "id-1",
      "label": "label1",
      "value": "1",
      "valid": {
        "pattern": "^[0-9]+$",
        "max_length": 222,
        "min_length": 10
      },
      "readonly": false,
      "required": true,
      "type": "input",
      "p": 1
    },
    {
      "name": "id-2",
      "label": "label2",
      "value": "",
      "p": 2
    },
    {
      "name": "id-3",
      "label": "label3",
      "type": "checkbox",
      "required": true,
      "p": 3
    }
  ]

```

`products` is a JSON object which contains data to be fiscalised

```
    "products": [
        {
            "id": 1,
            "name": "Product A",
            "price": 100.00,
            "quantity": 2,
            "vat_percent": 20,
            "code": "00702001001000001",
            "units": 1,
            "discount": 10.00,
            "package_code": "5678",
            "total_amount": 190.00
        },
        {
            "id": 1,
            "name": "Product B",
            "price": 100.00,
            "quantity": 2,
            "vat_percent": 20,
            "code": "00702001001000001",
            "units": 1,
            "discount": 10.00,
            "package_code": "5679",
            "total_amount": 190.00
        }
    ]

```

Description of `products` JSON object:

| Parameter name | Mandatory | Type   | Description                                               | Example           |
| -------------- | --------- | ------ | --------------------------------------------------------- | ----------------- |
| `id`           | no        | number | ID of product                                             | 1                 |
| `discount`     | no        | number | Discount based on quantity of goods or services in tiyins | 100.20            |
| `name`         | no        | string | Product name                                              | Scooters rental   |
| `price`        | no        | number | Price per unit of goods or services in tiyins             | 122.56            |
| `quantity`     | no        | number | Quantity of goods or services                             | 2                 |
| `code`         | no        | number | Product and service identification code                   | 00702001001000001 |
| `units`        | no        | number | Unit code                                                 | 241092            |
| `vat_percent`  | no        | number | Percentage of VAT paid for this product                   | 20                |
| `package_code` | no        | number | Product packaging code                                    | 123456            |
| `total_amount` | no        | number | Total amount of all products and services                 | 245.12            |

# Response codes

## API response codes

| Code | Text                                                                                                           | Description of the possible reason                                                                                                                                                                       | Where client can solve the problem |
| ---- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| 1000 | General decline                                                                                                | The cause of the error is unknown, detailed analysis is needed, contact the support service                                                                                                              | Flitt                              |
| 1002 | Application error                                                                                              | The cause of the error is unknown, the detailed analysis is needed, contact the support service                                                                                                          | Flitt                              |
| 1003 | Invalid CVV2 code                                                                                              | Incorrect CVV2 code. In some cases, you can get this error if the validity period of card was incorrect                                                                                                  | issuing bank                       |
| 1004 | Do not honor                                                                                                   | The card is blocked, the status was set, or itâs closed for online payments                                                                                                                              | issuing bank                       |
| 1005 | Invalid format                                                                                                 | Invalid data format. Probable cause is too small payment amount                                                                                                                                          | issuing bank                       |
| 1006 | Merchant is not configured correctly                                                                           | Merchant settings on the side of Flint are not correct                                                                                                                                                   | Flitt                              |
| 1007 | Parameter `{param_name}` is incorrect                                                                          | One or more of the received parameters have an incorrect format, size or an invalid value                                                                                                                | merchant                           |
| 1009 | Parameter `{param_name}` is empty                                                                              | One or more of the received parameters are empty                                                                                                                                                         | merchant                           |
| 1010 | Request Is empty                                                                                               | Submitted request is empty                                                                                                                                                                               | merchant                           |
| 1011 | Parameter `{param_name}` is missing                                                                            | One or more required parameters are not sent                                                                                                                                                             | merchant                           |
| 1012 | Currency `{currency}` is not available for this merchant `1549901`                                             | The merchant uses a currency that is not allowed or not configured on the Flint side                                                                                                                     | merchant                           |
| 1013 | Duplicate order `{order_id}` for merchant `1549901`                                                            | The passed parameter order_id is not unique for this merchant                                                                                                                                            | merchant                           |
| 1014 | Invalid signature                                                                                              | The signature generated by the merchant in the request is not correct                                                                                                                                    | merchant                           |
| 1015 | Invalid card number                                                                                            | Incorrect card number                                                                                                                                                                                    | issuing bank                       |
| 1016 | Merchant `1549901` not found                                                                                   | Merchant is not registered                                                                                                                                                                               | Flitt                              |
| 1017 | No available payment systems                                                                                   | Merchant is not allowed to use any of the payment methods that were sent in the request                                                                                                                  | Flitt                              |
| 1018 | Order `{order_id}` not found                                                                                   | Error is returned when requesting order status or reverse if no order is found                                                                                                                           | Flitt                              |
| 1019 | Order `{order_id}` already has been completed                                                                  | Was made an attempt to pay the expired order                                                                                                                                                             | merchant                           |
| 1021 | Unsupported Content-Type `{content_type}`                                                                      | When requesting a Flitt server, a non-HTTP header of Content-Type                                                                                                                                        | merchant                           |
| 1023 | Invalid amount                                                                                                 | Incorrect amount                                                                                                                                                                                         | merchant                           |
| 1024 | 3DSecure authentication failed                                                                                 | 3DSecure password verification error                                                                                                                                                                     | issuing bank                       |
| 1025 | Invalid card expiry date                                                                                       | Invalid card validity period                                                                                                                                                                             | issuing bank                       |
| 1026 | Only redirect method allowed                                                                                   | The protocol used by the merchant is not allowed                                                                                                                                                         | merchant                           |
| 1027 | Preauth not allowed                                                                                            | Preauthorization is not available                                                                                                                                                                        | Flitt                              |
| 1028 | Custom design not found                                                                                        | Custom design not found                                                                                                                                                                                  | merchant                           |
| 1034 | Please do not use symbol `{separator}` in parameters                                                           | The separator character can not be used in request parameters                                                                                                                                            | merchant                           |
| 1035 | Token not found                                                                                                | An attempt to charge the client card by itâs token is unsuccessful. The token may have expired, or an invalid value has been used                                                                        | merchant                           |
| 1036 | Invoice is paid                                                                                                | Invoice is paid                                                                                                                                                                                          | merchant                           |
| 1037 | Decline, not sufficient funds                                                                                  | Decline, not sufficient funds                                                                                                                                                                            | merchant                           |
| 1040 | Transaction amount exceeds card internet limit                                                                 | Transaction amount exceeds card internet limit                                                                                                                                                           | merchant                           |
| 1041 | Card is in black list                                                                                          | Card is in black list                                                                                                                                                                                    | Flitt                              |
| 1042 | Stolen card                                                                                                    | Stolen card                                                                                                                                                                                              | merchant                           |
| 1043 | Restricted Card                                                                                                | Restricted Card                                                                                                                                                                                          | merchant                           |
| 1044 | Lost card                                                                                                      | Lost card                                                                                                                                                                                                | merchant                           |
| 1045 | Card is blocked by acquirer bank                                                                               | Card is blocked by acquirer bank                                                                                                                                                                         | Flitt                              |
| 1046 | Request contains non utf-8 symbol                                                                              | Request contains non utf-8 symbol                                                                                                                                                                        | merchant                           |
| 1047 | Card exceeds withdrawal frequency limit                                                                        | Card exceeds withdrawal frequency limit                                                                                                                                                                  | merchant                           |
| 1048 | Card exceeds withdrawal amount limit                                                                           | Card exceeds withdrawal amount limit                                                                                                                                                                     | merchant                           |
| 1049 | Unknown payment system error                                                                                   | Unknown payment system error                                                                                                                                                                             | Flitt                              |
| 1051 | Declined by antifraud                                                                                          | Declined by antifraud                                                                                                                                                                                    | Flitt                              |
| 1052 | Order has expired                                                                                              | Order has expired                                                                                                                                                                                        | merchant                           |
| 1053 | 3DSecure card verification failed. Directory server or issuer not available.                                   | 3DSecure card verification failed. Directory server or issuer not available.                                                                                                                             | merchant                           |
| 1054 | Session expired                                                                                                | Session expired                                                                                                                                                                                          | merchant                           |
| 1055 | P2P limit exceeded                                                                                             | P2P limit exceeded                                                                                                                                                                                       | Flitt                              |
| 1057 | Sender card declined by issuer                                                                                 | Sender card declined by issuer (is blocked)                                                                                                                                                              | merchant                           |
| 1058 | Receiver card declined by issuer                                                                               | Receiver card declined by issuer (is blocked)                                                                                                                                                            | merchant                           |
| 1059 | Transaction with rectoken not allowed for merchant                                                             | Transaction with rectoken not allowed for merchant                                                                                                                                                       | Flitt                              |
| 1060 | Recurring transaction not allowed for merchant                                                                 | Recurring transaction not allowed for merchant                                                                                                                                                           | Flitt                              |
| 1061 | PIN tries exceeded                                                                                             | PIN tries exceeded                                                                                                                                                                                       | merchant                           |
| 1062 | Not permitted to merchant                                                                                      | Transaction is not permitted to merchant                                                                                                                                                                 | Flitt                              |
| 1063 | Not permitted to client                                                                                        | Transaction is not permitted to client                                                                                                                                                                   | merchant                           |
| 1064 | Call your bank                                                                                                 | Call your bank                                                                                                                                                                                           | merchant                           |
| 1065 | Invalid transaction                                                                                            | The transaction was rejected by the issuer bank                                                                                                                                                          | merchant                           |
| 1066 | System malfunction                                                                                             | System failure of acquirer bank                                                                                                                                                                          | Flitt                              |
| 1067 | Incorrect PIN                                                                                                  | Incorrect PIN                                                                                                                                                                                            | merchant                           |
| 1068 | Format error                                                                                                   | Data format error                                                                                                                                                                                        | merchant                           |
| 1069 | Reverse not allowed. Turnover is not enough.                                                                   | Reverse not allowed. Turnover is not enough.                                                                                                                                                             | Flitt                              |
| 1070 | Transaction is routed to another terminal                                                                      | Transaction is routed to another terminal                                                                                                                                                                | Flitt                              |
| 1072 | Recurring chain declined                                                                                       | Recurring chain declined                                                                                                                                                                                 | merchant                           |
| 1073 | 3DSecure is mandatory for Maestro cards                                                                        | 3DSecure is mandatory for Maestro cards                                                                                                                                                                  | merchant                           |
| 1074 | P2P credit allowed only by rectoken                                                                            | P2P credit allowed only by rectoken                                                                                                                                                                      | Flitt                              |
| 1078 | Token deactivated by bank                                                                                      | Token deactivated by bank                                                                                                                                                                                | Flitt                              |
| 1075 | 3DSecure is mandatory                                                                                          | 3DSecure is mandatory                                                                                                                                                                                    | merchant                           |
| 1079 | Card is blocked by issuing bank                                                                                | Card is blocked by issuing bank                                                                                                                                                                          | merchant                           |
| 1076 | An error occurred while processing your payment. Invalid IBAN. Check the IBAN you entered, or use another IBAN | An error occurred while processing your payment. Invalid IBAN. Check the IBAN you entered, or use another IBAN                                                                                           | merchant                           |
| 1080 | Decline, exceeds receiving card count limit                                                                    | Decline, exceeds receiving card count limit                                                                                                                                                              | merchant                           |
| 1077 | Merchant is not activated yet. Only test IBAN allowed                                                          | Merchant is not activated yet. Only test IBAN allowed                                                                                                                                                    | Flitt                              |
| 1081 | Insufficient funds on balance (p2p credit)                                                                     | Insufficient funds on balance (p2p credit)                                                                                                                                                               | Flitt                              |
| 1082 | Token has expired                                                                                              | Token has expired                                                                                                                                                                                        | merchant                           |
| 1083 | Decline, exceeds receiving card amount limit                                                                   | Decline, exceeds receiving card amount limit                                                                                                                                                             | merchant                           |
| 1087 | Terminal closed by acquiring bank                                                                              | Terminal blocked by acquiring bank                                                                                                                                                                       | Flitt                              |
| 1086 | Transaction already finished                                                                                   | Transaction already finished                                                                                                                                                                             | merchant                           |
| 1084 | Only full refund allowed                                                                                       | Only full refund allowed                                                                                                                                                                                 | Flitt                              |
| 1088 | Lookup code attempts limit exceeded                                                                            | Lookup code attempts limit exceeded                                                                                                                                                                      | Flitt                              |
| 1089 | Acquiring bank request timeout                                                                                 | Acquiring bank request timeout                                                                                                                                                                           | merchant                           |
| 1090 | P2P card credit not allowed for this country                                                                   | P2P card credit not allowed for this country                                                                                                                                                             | Flitt                              |
| 1091 | Card not enrolled. Lookup required                                                                             | Lookup for p2p transfer is required                                                                                                                                                                      | Flitt                              |
| 1092 | Invalid phone number                                                                                           | Phone number, provided by the customer is not valid                                                                                                                                                      |                                    |
| 1096 | Invalid E-mail                                                                                                 | Email, provided by the customer is not valid                                                                                                                                                             |                                    |
| 1097 | Decline, refer to card issuer                                                                                  | Issuing bank declined transaction                                                                                                                                                                        | issuing bank                       |
| 1098 | SEPA: The customerâs payment is accepted, but then canceled before collection.                                 | merchant                                                                                                                                                                                                 |                                    |
| 1099 | P2P credit is not available for this IP address                                                                | Merchant need to provide servers IP list to Flitt support                                                                                                                                                | Flitt                              |
| 1100 | Operation not allowed                                                                                          | This type of API operation is not allowed to merchant. Please contact Flitt support                                                                                                                      | Flitt                              |
| 1102 | Antifraud decline. Prepaid cards are blocked                                                                   | Prepaid cards are limited prior agreement with the merchant                                                                                                                                              | merchant                           |
| 1103 | Receipt created                                                                                                | Payment by receipt method. A receipt has been generated for the customer and payment is expected through the bank account.                                                                               | merchant                           |
| 1104 | Country not allowed by bank-acquirer                                                                           | The acquiring bank has limited certain countries                                                                                                                                                         | Flitt                              |
| 1105 | Antifraud decline. Only full 3D-Secure allowed.                                                                | Only payments with full 3D-Secure authentication are allowed                                                                                                                                             | Flitt                              |
| 1106 | Split error. Split payments not allowed for merchant.                                                          | Splitting API not activated for this merchant                                                                                                                                                            | merchant                           |
| 1107 | Split error. Settlement merchants have another company.                                                        | An attempt to split the payment with an incorrect recipient                                                                                                                                              | merchant                           |
| 1108 | Split error. Merchants in purchase and reverse do not match.                                                   | An error occurred while trying to make a reverse on a split payment. The merchant_id specified in the reverse does not match the merchant_id that was involved in the splitting of the original purchase | merchant                           |
| 1109 | Order already captured with different amount                                                                   | Attempt to re-capture on a partialy-completed purchase                                                                                                                                                   | merchant                           |
| 1111 | Your card is not supported. Please use card of                                                                 | The card of this payment system is not supported                                                                                                                                                         | Flitt                              |
| 1114 | Settlement not allowed until order is captured                                                                 | Before splitting the pre-authorization payment, it must be completed (perform the capture operation)                                                                                                     | merchant                           |
| 1115 | Pick up card (no fraud)                                                                                        | The issuing bank requests the card pick up, but the claim is not fraudulent                                                                                                                              |                                    |
| 1116 | Pick up card, special condition (fraud account)                                                                | The issuing bank requests the card pick up, the claim is related to the fact of fraud or compromise                                                                                                      | Flitt                              |
| 1117 | Security violation                                                                                             | Operations with this card are limited by the issuing bank                                                                                                                                                |                                    |
| 1120 | Splitting amount does not correspond to purchase or capture amount                                             | An attempt to split a payment into an amount that differs from the original payment, or a capture operation                                                                                              | Flitt                              |
| 1122 | Connection closed unexpectedly                                                                                 | Technical error while connecting the acquiring bank                                                                                                                                                      | Flitt                              |
| 1123 | Acquiring bank request timeout. Transaction reversed.                                                          | Timeout of connection with the acquiring bank. The technical reverse of the operation has been performed                                                                                                 | Flitt                              |
| 1125 | Maestro cards are not allowed                                                                                  | Maestro cards are limited to accept                                                                                                                                                                      | Flitt                              |

## JavaScript response codes

These codes can be caught and customized with [JavaScript callbacks](https://docs.flitt.com/api/embedded-custom/#example-with-javascript-callbacks) when integrated with [Embedded checkout](https://docs.flitt.com/api/embedded-custom/)

| Code | Text                                                                                                                                   |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 2000 | Payment declined by issuing bank. Possibly internet payments not allowed for this card. Please refer to your bank for details.         |
| 2001 | This currency not allowed.                                                                                                             |
| 2002 | Possibly your cookies are disabled. Please enable cookies in browser settings and try again.                                           |
| 2003 | Merchant is configured incorrectly.                                                                                                    |
| 2004 | Duplicate order. Please return to the shop site and try again.                                                                         |
| 2005 | No available payment methods                                                                                                           |
| 2006 | Order lifetime has expired. Please return to the shop site and try again.                                                              |
| 2007 | Invalid signature.                                                                                                                     |
| 2008 | Order parameters are incorrect.                                                                                                        |
| 2009 | Order has already been paid.                                                                                                           |
| 2013 | Invalid card number. Check the card number you entered, or use another card.                                                           |
| 2014 | Invalid order amount                                                                                                                   |
| 2015 | Error while checking 3DSecure password. Maybe you entered the wrong password. Try to make a payment again, or contact the issuing bank |
| 2016 | Wrong card expiry date. Please enter valid expiry date printed on the front side of the card and repeat payment.                       |
| 2017 | Wrong CVV2 code. Please enter the 3-digit code on the reverse side of the card and repeat payment.                                     |
| 2018 | Payment declined by issuing bank. Possibly internet payments not allowed for this card. Please refer to your bank for details.         |
| 2019 | Insufficient funds.                                                                                                                    |
| 2021 | This type of order is prohibited for the merchant                                                                                      |
| 2023 | Payment attempts limit exceeded. Please try again later.                                                                               |
| 2025 | Internet payments not allowed for this card or amount limit exceeded for internet payments.                                            |
| 2038 | 3DSecure is mandatory. Only cards enrolled in 3DSecure with password are allowed.                                                      |
| 2039 | Your card is not supported. Please use card of                                                                                         |
| 2040 | Payment rejected by antifraud system                                                                                                   |

# Reverse parameters

Request parameters

| Parameters    | Type         | Mandatory | Description                                                                                                                                                                                                            |
| ------------- | ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `version`     | string(10)   | optional  | Protocol version. Default value: 1.0.1 Version 1.0 is deprecated                                                                                                                                                       |
| `order_id`    | string(1024) | mandatory | Order ID which is generated by merchant                                                                                                                                                                                |
| `merchant_id` | integer(12)  | mandatory | Merchant unique ID. Generated by Flitt during merchant registration                                                                                                                                                    |
| `amount`      | integer(12)  | mandatory | Order amount without separator                                                                                                                                                                                         |
| `currency`    | string(3)    | mandatory | Order currency. Supported values: EUR â Euro USD â US Dollar GBP â Pound sterling mandatory CZK â Czech Republic Koruna GEL - Georgian lari UZS - Uzbekistan sum [Full list of supported currencies](/api/currencies/) |
| `email`       | string(254)  | optional  | Merchant staff emailm who initiated the reversal                                                                                                                                                                       |
| `comment`     | string(1024) | optional  | Merchant comment on reversal reason UTF-8                                                                                                                                                                              |
| `reverse_id`  | string(50)   | optional  | Idempotent reversal key to retry refund safely. Merchant should generate unique value for each retry per order_id                                                                                                      |
| `signature`   | string(40)   | mandatory | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response |

| Parameters             | Type         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `order_id`             | string(1024) | Order ID which is generated by merchant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `merchant_id`          | integer(12)  | Merchant unique ID. Generated by Flitt during merchant registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `currency`             | string(3)    | Order currency. Supported values: see [Currencies](/api/currencies/)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `reverse_status`       | string(50)   | Order processing status. Can contain the following values: `created` â order has been created, but the customer has not entered payment details yet; merchant must continue to request the status of the order `processing` â order is still in processing by payment gateway; merchant must continue to request the status of the order `declined` â order is declined by Flitt payment gateway or by a bank or by an external payment system `approved` â order completed successfully, funds are held on the payerâs account and soon will be credited of the merchant; merchant can provide the service or ship goods `expired` â order `lifetime` expired. `reversed` â previously approved transaction was fully reversed. In this case, parameter `reversal_amount` will be equal to actual_amount |
| `response_status`      | string(50)   | Request processing status. If parameters sent by merchant did not pass validation then failure, else success                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `reverse_id`           | string(50)   | optional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `transaction_id`       | string(50)   | optional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `signature`            | string(40)   | Order signature. Required to verify merchant request consistency and authenticity. Signature generation algorithm please see at [Signature generation for request and response](/api/building-signature/) and response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `response_code`        | integer(4)   | Order decline response code. Possible codes see in Response codes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `response_description` | string(1024) | Order response code description, see Response codes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `comment`              | string(1024) | Merchant comment on reversal reason UTF-8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

Examples

```
{
  "request": {
    "order_id": "test_12343242111",
    "currency": "GEL",
    "amount": "1",
    "signature": "29a569275265925c2ec356d3adada1929fd8bb8c",
    "merchant_id": "1549901"
  }
}

```

```
{
    "response": {
        "reverse_status": "approved",
        "order_id": "test_12343242111",
        "response_description": "",
        "response_code": "",
        "merchant_id": 1549901,
        "response_status": "success",
        "signature": "3656398d3e2aaf83138223cf97ce497871495904",
        "reverse_id": "",
        "reversal_amount": "16",
        "transaction_id": "2011080263"
    }
}

```

```
{
    "response": {
        "error_code": 1007,
        "error_message": "Parameter `signature` is incorrect",
        "request_id": "e96rGwTzLjFmR",
        "response_status": "failure"
    }
}

```

# Split payments

API allows splitting the payment to multiple recipients. The example shows the work with two recipients, although there may be several. The requisites of all recipients are transmitted in the request in the parameter receiver and can be any of the following entities:

- bank account details
- details stored under a certain merchant_id in the Flitt system

To split the payment you should follow steps:

1. Create a server-server request (Flitt hosted page purchase request: https://portal.flitt.com/ru/info/api/v1.0/3 or merchant hosted page (PCI DSS) https://docs.flitt.com/docs/page/4/)
1. Redirect the client in the browser to payment page and request card details
1. Process the response of the result of the payment to the page in the browser response response_url and callback to the server page server_callback_url
1. Send splitting request at https://pay.flitt.com/api/settlement passing it the parameter operation_id equal to the order_id from step 1 and the splitting instruction in the parameter receiver.

## Splitting request

The request is sent using the POST method in the JSON format to the URL: `https://pay.flitt.com/api/settlement`

**Request**:

```
{
  "request": {
    "version": 2.0,
    "data": "ewogIm9yZ...Qp9",
    "signature": "943571471619207087eb57e2b4ef69affd337b1a"
  }
}

```

`data` is a base64 encoded format data set:

```
{
  "order": {
    "server_callback_url": "http://site.com/callback",
    "currency": "GEL",
    "amount": 300,
    "order_type": "settlement",
    "response_url": "http://site.com/test/responsepage/",
    "order_id": "settlement_test1234561467462099.19",
    "operation_id": "test1234561467462099.19",
    "order_desc": "test order",
    "merchant_id": 700001,
    "receiver": [
      {
        "requisites": {
          "amount": 100,
          "settlement_description": "Purpose of payment for bank transfer",
          "merchant_id": 500001,
          "fee_partner_amount": 102
        },
        "type": "merchant"
      },
      {
        "requisites": {
          "amount": 200,
          "settlement_description": "Purpose of payment for bank transfer",
          "merchant_id": 600001,
          "fee_partner_amount": 102
        },
        "type": "merchant"
      }
    ]
  }
}

```

### Final response (financial result)

The response is returned in JSON format to `server_callback_url` and `response_url` after the client completes the payment. Response format:

```
{
  "response": {
    "version": "2.0",
    "data": "...",
    "signature": "54aeeadf05b04e2e4097a4aa5907c3a62684d058"
  }
}

```

where `data` is a base64 encoded data set containing information about all financial transactions and their status

```
{
  "order": {
    "rrn": "",
    "masked_card": "444455XXXXXX6666",
    "sender_cell_phone": "",
    "response_status": "success",
    "sender_account": "",
    "fee": "",
    "rectoken_lifetime": "",
    "reversal_amount": "0",
    "settlement_amount": "0",
    "actual_amount": "2000",
    "order_status": "approved",
    "response_description": "",
    "verification_status": "",
    "order_time": "07/02/2016 15:21:39",
    "actual_currency": "GEL",
    "order_id": "test1234561467462099.19",
    "parent_order_id": "",
    "merchant_data": "",
    "tran_type": "purchase",
    "eci": "",
    "settlement_date": "",
    "payment_system": "card",
    "rectoken": "",
    "approval_code": "478450",
    "merchant_id": 600001,
    "settlement_currency": "",
    "payment_id": 1586193,
    "transaction": [
      {
        "status": "approved",
        "amount": 20.0,
        "fee": 0.0,
        "reversal_amount": 0.0,
        "parent_tran_id": null,
        "receiver": {},
        "merchant_id": 600001,
        "type": "purchase",
        "id": 1001543960,
        "doc_no": null
      }
    ],
    "product_id": "",
    "currency": "GEL",
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "2000",
    "sender_email": "demo@flitt.com"
  }
}

```

## Signature calculation

Parameter is calculated as function sha1(password + '|' + data)

## Return of funds

When returning funds you must specify in the parameters `receiver-> requisites->` from which merchant which part of the original amount should be refunded. The amount will be returned to the payer's card either online or according to the rules of the bank within a few days if void is not possible.

POST: `https://pay.flitt.com/api/reverse/order_id`

### Example parameter data:

```
{
  "order": {
    "order_id": "test1234561467462099.19",
    "currency": "GEL",
    "amount": "300",
    "merchant_id": "700001",
    "receiver": [
      {
        "requisites": {
          "amount": 100,
          "merchant_id": "500001"
        },
        "type": "merchant"
      },
      {
        "requisites": {
          "amount": 200,
          "merchant_id": "600001"
        },
        "type": "merchant"
      }
    ]
  }
}{
  "order": {
    "order_id": "test1234561467462099.19",
    "currency": "GEL",
    "amount": "300",
    "merchant_id": "700001",
    "receiver": [
      {
        "requisites": {
          "amount": 100,
          "merchant_id": "500001"
        },
        "type": "merchant"
      },
      {
        "requisites": {
          "amount": 200,
          "merchant_id": "600001"
        },
        "type": "merchant"
      }
    ]
  }
}

```

where: `order_id` and `merchant_id` are the identifiers of the original payment.

### Example of a response for a successful reverse:

```
{
  "order": {
    "reverse_status": "approved",
    "reversal_amount": "300",
    "order_id": " test1234561467462099.19 ",
    "response_status": " success ",
    "response_code": " ",
    "response_description": " ",
    "merchant_id": 700001
  }
}

```

### Example of a response in the event of a failure:

```
{
  " order ": {
    "reverse_status": "declined",
    "reversal_amount": "300",
    "order_id": "test1234561467462099.19",
    "response_status": "success",
    "response_code": "1016",
    "response_description": "Merchant not found",
    "merchant_id ": 700001
  }
}

```

To create subscription, please refer to comon instruction on how to [create order](/api/create-order/).

Pay attention

Subscription payments does not work for [Direct](/getting-started/direct/) integration type.

Also, [Open Banking](/api/opb_intro/) method does not suport subscription yet.

For enabling subscription payments for JavaScrip type of integration, please refer to [Embedded example with subscription](/api/embedded-custom/#example-with-subscription)

In order to create subscritpion, additional parameters must be sent in request to `/api/checkout/redirect`, `/api/checkout/token` or `/api/checkout/url` endpoints.

```
{
  ...
  "subscription": "Y",
  "recurring_data": {
    "every": 5,
    "period": "day",
    "amount": 1000,
    "state": "Y",
    "readonly": "Y",
    "quantity": 100,
    "trial_period": "month",
    "trial_quantity": 1
  }
}

```

`recurring_data` properties description

| Property         | Default falue                                                       | Type                                            | Description                                                                                                          |
| ---------------- | ------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `start_time`     | Time of payment aproval                                             | Date in format `YYYY-MM-DD HH24:MI:SS`          | Don't specify if you need to make forst charge not from a particular date, but from date of customer initial payment |
| `end_time`       | Time of payment aproval + quantity * period * every                 | Date in format `YYYY-MM-DD HH24:MI:SS`          | If not specified, it is calculated as the date of the last period, considering quantity, every and poeriod values    |
| `amount`         | No default value, property is mandatory                             | Integer(12)                                     | Amount of each schedulled charge. Amount without separator. 1020 (GEL) means 10 lari and 20 tetri                    |
| `period`         | No default value, property is mandatory                             | `day` or `week` or `month`                      | Frequency, provided as on of the available values: `day`, `week`, `month`                                            |
| `every`          | No default value, property is mandatory                             | Integer(12)                                     | Number of days, weeks, months between schedulled charges.                                                            |
| `quantity`       | No default value, either `quantity` or `end_time` must be specified | Integer(6)                                      | Number of schedulled charges                                                                                         |
| `trial_period`   | Trial is disabled by default                                        | `day` or `week` or `month`                      | Number of days, weeks, months for trial period between initial order approval and first scheduilled payment          |
| `trial_quantity` | No default value, must be specifiedm if `trial_period` not empty    | Integer(12)                                     | Number of trial periods, when customer is not charged                                                                |
| `state`          | Y                                                                   | `y` or `Y` `n` or `N` `hidden` `shown_readonly` | Property to display or hide form with other properties on checkout page                                              |

`state` parameter can accept the following values:

| Value            | Description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| `y` or `y`       | Enable calendar on checkout page and allow client to disable it        |
| `n` or `N`       | Disable calendar on checkout page and allow client to enable it        |
| `hidden`         | Enable calendar on checkout page but do not show it to client          |
| `shown_readonly` | Enable calendar on checkout page and do not allow client to disable it |

Code

```
curl -L 'https://pay.flitt.com/api/checkout/url' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "order_id": "test_subscription5",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "amount": 100,
    "subscription": "Y",
    "recurring_data": {
      "every": 5,
      "period": "day",
      "amount": 1000,
      "state": "Y",
      "readonly": "Y",
      "quantity": 100,
      "trial_period": "month",
      "trial_quantity": 1
    },
    "signature": "4120ca8501b8003bb4860c6fc354c9e3ceb85d0c"
  }
}'

```

```
<?php
require_once '../configuration.php';
require_once SDK_ROOTPATH . '/../vendor/autoload.php';


//Payment subscription url scheme B(host-to-host)
try {
  //Minimal data set, all other required params will generated automatically
  $data = [
      'currency' => 'GEL',
      'amount' => 1000, // convert to 10.00$
      'recurring_data' => [
          'start_time' => '2021-12-24',
          'amount' => 1000,
          'every' => 30,
          'period' => 'day',
          'state' => 'y',
          'readonly' => 'y'
      ]

  ];
  //Call method to generate url
  \Flitt\Configuration::setApiVersion('2.0'); //allow only json, api protocol 2.0
  $url = Flitt\Subscription::url($data);
  //getting returned data
  ?>
  <!doctype html>
  <html lang="en-US">
  <head>
      <meta charset="UTF-8">
      <title>Generate subscription Payment Url</title>
      <style>
          table tr td, table tr th {
              padding: 10px;
          }
      </style>
  </head>
  <body>
  <table style="margin: auto;" border="1">
      <thead>
      <tr>
          <th style="text-align: center" colspan="2">Request Data</th>
      </tr>
      <tr>
          <th style="text-align: left"
              colspan="2"><?php printf("<pre>%s</pre>", json_encode(['request' => $data], JSON_PRETTY_PRINT)) ?></th>
      </tr>
      </thead>
      <tbody>
      <tr>
          <td>Payment id:</td>
          <td><?= $url->getData()['payment_id'] ?></td>
      </tr>
      <tr>
          <td>Normal response:</td>
          <td>
              <pre><?php print_r($url->getData()) ?></pre>
          </td>
      </tr>
      <tr>
          <td>Response subscription url:</td>
          <td><a href="<?php print_r($url->getUrl()) ?>"><?php print_r($url->getUrl()) ?></a></td>
      </tr>
      </tbody>
  </table>
  </body>
  </html>
  <?php
} catch (\Exception $e) {
  echo "Fail: " . $e->getMessage();
}

```

```
'use strict'

const FlittPay = require('../lib')
const util = require('../lib/util')

const flitt = new FlittPay(
  {
    merchantId: 1549901,
    secretKey: 'test'
  }
)
const date = new Date().toISOString().slice(0, 10)
const OrderId = util.generateOrderId()

const data = {
  order_desc: 'test order',
  order_id: OrderId,
  currency: 'GEL',
  amount: 1000,
  recurring_data:
  {
    every: 5,
    period: 'day',
    amount: 1000,
    start_time: date,
    state: 'y',
    Readonly: 'n'
  }
}
flitt.Subscription(data).then(data => {
  console.log(data)
}).catch((error) => {
  console.log(error)
})
const StopData = {
  order_id: OrderId,
  action: 'stop'
}

flitt.SubscriptionActions(StopData).then(data => {
  console.log(data)
}).catch((error) => {
  console.log(error)
})

```

See:

- [checkout_subscription.aspx](https://github.com/flittpayments/c-sharp-sdk/blob/main/FlittSDKSamples/checkout_subscription.aspx)
- [checkout_subscription.aspx.cs](https://github.com/flittpayments/c-sharp-sdk/blob/main/FlittSDKSamples/checkout_subscription.aspx.cs)
- [checkout_settlement.aspx.designer.cs](https://github.com/flittpayments/c-sharp-sdk/blob/main/FlittSDKSamples/checkout_settlement.aspx.designer.cs)

Subscription payments mean a type of payment when a customer is charged with fixed, predictable frequency: daily, weekly, monthly, yearly.

It differs from [recurring](/getting-started/recurring/) payment (payment with saved card) which are usually not scheduled.

After subscription order is created, payer is redirected to Flitt checkout page, where schedule is displayed.

Subscription payments are available only for methods: cards Visa/MasterCard/Amex, Apple pay and Google Pay.

## Test merchant data

| Parameter                     | Value                                                      |
| ----------------------------- | ---------------------------------------------------------- |
| merchant_id                   | 1549901                                                    |
| test secret key for purchases | test                                                       |
| test secret key for payouts   | testcredit                                                 |
| currency                      | See full list of [supported currencies](/api/currencies/). |

## Test payment data

Testing with cards

| Card number        | Brand      | Expiry date | CVV2 | 3DSecure                                | Response type |
| ------------------ | ---------- | ----------- | ---- | --------------------------------------- | ------------- |
| `4444555566661111` | Visa       | any         | any  | yes                                     | approve       |
| `4444111166665555` | Visa       | any         | any  | yes                                     | decline       |
| `4444555511116666` | Visa       | any         | any  | no                                      | approve       |
| `4444111155556666` | Visa       | any         | any  | no                                      | decline       |
| `5555666644441111` | MasterCard | any         | any  | yes                                     | approve       |
| `6666444455551111` | MasterCard | any         | any  | yes                                     | approve       |
| `4444555566669999` | Visa       | any         | any  | yes, frictionless                       | approve       |
| `4444666655559999` | Visa       | any         | any  | yes, challenge                          | approve       |
| `4444999966665555` | Visa       | any         | any  | yes, frictionless                       | decline       |
| `4444666699995555` | Visa       | any         | any  | yes, challenge                          | decline       |
| `2222555566663333` | MasterCard | any         | any  | yes                                     | decline       |
| `4444777799991111` | Visa       | any         | any  | managed by `reservation_data` parameter | approve       |
| `9860010099998881` | Humo       | any         | any  | yes                                     | approve       |
| `8600202020202023` | UzCard     | any         | any  | yes                                     | approve       |
| `9860010088889992` | Humo       | any         | any  | OTP = 111111                            | approve       |
| `8600202020202023` | UzCard     | any         | any  | OTP = 111111                            | approve       |

## Testing Apple Pay on web

Testing Apple Pay on web

If your merchant is in test mode, Flitt will automaticaly convert any real wallet tokenized card into test token.

You just need to make a test payment and use your real Apple wallet card.

## Testing Apple Pay in app

Testing Apple Pay in app

Please refer to [Apple Pay sandbox instruction](https://developer.apple.com/apple-pay/sandbox-testing/)

1. Register in Apple Pay developer account. You will need to make enrollment and pay $99.

1. Register a Merchant ID in your developer account.

1. Create your Payment Processing Certificate.

1. Create your Merchant Identity Certificate.

1. Upload your certificates in Flitt Merchant Portal in Merchant settings->>Payment methods->>Apple

1. Sign in to App Store Connect.

1. On the homepage, click Users and Access.

1. Under Sandbox, click Testers.

1. Click â+â to set up your tester accounts.

1. Complete the tester information form and click Invite.

1. Sign out of your Apple Account on all testing devices and sign back in with your new sandbox tester account.

1. Add test card to your Apple wallet:

   ```
   4761 1200 1000 0492
   01/27
   CVV: 480

   ```

1. Wait will card will be added to your wallet as Visa Test Card

1. Test payment with Visa Test Card

## Testing Open Banking

Testing with Open Banking

| Parameter      | Value | Comment                                 |
| -------------- | ----- | --------------------------------------- |
| payment_method | x     | Testing is possible only with Demo Bank |

To test Open Banking, create payment with parameter `payment_method = x` or click Demo Bank icon on checkout page.

# Android SDK

Android SDK allows you to accept Google Pay payments from Android application.

The latest version of Android SDK you can always find in our public repository

<https://github.com/flittpayments/android-sdk>

In the [demo directory](https://github.com/flittpayments/android-sdk/tree/main/app/src/main/java/com/flitt/android/demo) you can find an example of an application which implements Google Pay functionality

Also, you can refer the central Maven repository: <https://central.sonatype.com/search?q=flitt-android>

**1 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
    {
      "response":{
        "response_status":"success",
        "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
      }
    }

```

**2 Setup your application**

Add dependencies to your project in app/build.gradle. This implementation requires Google Play services 17.0.0 or greater

```
implementation 'com.google.android.gms:play-services-base:17.0.0'
implementation 'com.google.android.gms:play-services-wallet:19.4.0'
implementation 'com.flitt:flitt-android:1.2.0'

```

**3 Update AndroidManifest.xml to enable Google Pay API if required**

Add the following lines:

```
<uses-permission android:name="android.permission.INTERNET" />
<meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true"
>

```

For more information please follow Google Pay API [setup instruction](https://developers.google.com/pay/api/android/guides/setup)

**4 Setup your MearchantId**

Create an instance of Cloudipsp with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

Attach webview, which will responsible for payer redirection to 3DSecure page

```
webView = findViewById(R.id.web_view);
cloudipsp = new Cloudipsp(<your merchant_id>, webView);

```

**5 Process payment once payer sumbits data and card object is returned**

Pass payment token from step 1 to method `payToken`

```
final Card card = getCard();
    if (card != null) {
       cloudipsp.payToken(card, token, this);
    }

```

**6 Follow Demo folder on our GitHub to see examples on how to add card form to your application**

<https://github.com/flittpayments/android-sdk/tree/main/app/src/main/java/com/flitt/android/demo>

**1 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
    {
      "response":{
        "response_status":"success",
        "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
      }
    }

```

**2 Setup your application**

Add dependencies to your project in app/build.gradle.This implementation requires Google Play services 17.0.0 or greater

```
implementation("com.google.android.gms:play-services-base:17.0.0")
implementation("com.google.android.gms:play-services-wallet:19.4.0")
implementation("com.flitt:flitt-android:1.2.0")

```

**3 Update AndroidManifest.xml to enable Google Pay API if required.**

```
<uses-permission android:name="android.permission.INTERNET" />
<meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true"
>

```

**4 Setup your MearchantId**

Create an instance of Cloudipsp with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

Attach webview, which will responsible for payer redirection to 3DSecure page

```
webView = findViewById(R.id.web_view);
cloudipsp = new Cloudipsp(<your merchant_id>, webView);

```

**5 Process payment once payer sumbits data and card object is returned**

Pass payment token from step 1 to method `payToken`

```
final Card card = getCard();
    if (card != null) {
       cloudipsp.payToken(card, token, this);
    }

```

**6 Follow Demo folder on our GitHub to see examples on how to add card form to your application**

<https://github.com/flittpayments/android-sdk/tree/main/app/src/main/java/com/flitt/android/demo>

# Flutter SDK for Mobile(iOS)

Getting Started

This project is a starting point for a Flutter [plug-in package](https://flutter.dev/developing-packages/), a specialized package that includes platform-specific implementation code for Android and/or iOS.

For help getting started with Flutter, view [online documentation](https://flutter.dev/docs), which offers tutorials, samples, guidance on mobile development, and a full API reference.

Flutter SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS and Android applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/flutter>

You can find demo app in [example](https://github.com/flittpayments/flutter/tree/main/example) directory

Before SDK integration, pass the steps to [register Apple Merchant ID](/api/applepay-getting-started/)

After creation, put the generated MerchantID in settings:

XCode -> Target -> Capabilities -> Apple Pay -> Merchant IDS

# iOS SDK (Swift)

iOS SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/ios-sdk>

To run the sample of application, run the command

```
git clone git@github.com:flittpayments/ios-sdk.git
cd ios-sdk/Example
pod install

```

iOS SDK is also available through CocoaPods. To install it, simply add the following line to your Podfile:

```
pod 'Flitt'

```

Example for Swift you can find by the link <https://github.com/flittpayments/ios-sdk/tree/master/ExampleSwift>

Integrate SDK putting the generated MerchantID in 2 places

1. In XCode -> Target -> Capabilities -> Apple Pay -> Merchant IDS

1. In integration SDK set `merchant_id` received during registration in Flitt [Merchant Portal](https://portal.flitt.com) in constructor instead of test 900234

   ```
   <textField opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="left" contentVerticalAlignment="center" text="1396424" borderStyle="roundedRect" placeholder="Enter merchant id" textAlignment="natural" minimumFontSize="17" translatesAutoresizingMaskIntoConstraints="NO" id="8pz-e9-tsn">

   ```

   github line link: <https://github.com/flittpayments/ios-sdk/blob/master/ExampleSwift/ExampleSwift/Base.lproj/Main.storyboard#L19>

# iOS SDK (Objective-C)

iOS SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/ios-sdk>

To run the sample of application, run the command

```
git clone git@github.com:flittpayments/ios-sdk.git
cd ios-sdk/Example
pod install

```

iOS SDK is also available through CocoaPods. To install it, simply add the following line to your Podfile:

```
pod 'Flitt'

```

Example for Objective-C you can find by the link <https://github.com/flittpayments/ios-sdk/tree/master/Example>

Integrate SDK putting the generated MerchantID in 2 places

1. In XCode -> Target -> Capabilities -> Apple Pay -> Merchant IDS

1. In integration SDK set `merchant_id` received during registration in Flitt [Merchant Portal](https://portal.flitt.com) in constructor instead of test 1396424

   ```
   - (void)viewDidLoad {
       [super viewDidLoad];

        self.api = [PSCloudipspApi apiWithMerchant:1396424 andCloudipspView:nil];
   }   

   ```

github line link: <https://github.com/flittpayments/ios-sdk/blob/master/Example/Cloudipsp/CDStartViewController.m#L24>

# React Native SDK

React Native SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your React applications.

The latest version of SDK you can always find in our public repository

<https://github.com/flittpayments/react-native>

## Step 1: Integrate Apple Pay in your application setting

See Apple Pay Merchant IDs settings in XCode: ApplePayMerchant -> Target -> Capabilities -> Apple Pay -> Merchant IDS

# Apple Pay purchases in mobile via web-view

You can use **web-view** integration of Apple Pay in your mobile application. **Web-view** integration is actually a replacement of native SDKs with the JavaScript SDK.

## How to integrate

Use <https://codepen.io/flitt/pen/GRVXjKY> code as an example.

### Step 1. Create endpoint on your backend

Endpoint will be requested by your frontend to obtain payment `token` value. Endpoint should be integrated as described in [instructions](https://docs.flitt.com/api/create-order/#merchant-embedded-checkout-page-with-payment-token). It means, that backend will `POST https://pay.flitt.com/api/checkout/token` the order data and obtain `token` value in response

### Step 2. Rewrite function `request()` from [code example](https://codepen.io/flitt/pen/GRVXjKY)

```
    function request() {
      return new Promise((resolve) =>
        setTimeout(() => resolve("_token"), 300)
      );
    }

```

to obtain payment `token` from your backend. Here `_token` should be replaced with backend `token` value.

### Step 3. Place your merchant_id and initial amount into `params` block

```
    const params = {
      merchant_id: 1549901,
      currency: "GEL",
      amount: 100
    };

```

this is required to draw initial Apple Pay button

### Step4. Obtain payment token from backend.

As soon as Apple Pay button is clicked, `request()` function will be executed to request new `token` from your backend endpoint from Step 1. Apple Pay button will use `token` string returned.

### Step5. Process callback on frontend with receipt object

Analyze `receipt` object to get the payment result. But you should not trust this response, until your backend receives callback and validate response `signature`.

### Step6. Process callback on your backend, specified in `server_callback_url` parameters.

Check `orders_status` and `signature` parameters to validate the result.

# Flutter SDK for Mobile(iOS)

Getting Started

This project is a starting point for a Flutter [plug-in package](https://flutter.dev/developing-packages/), a specialized package that includes platform-specific implementation code for Android and/or iOS.

For help getting started with Flutter, view [online documentation](https://flutter.dev/docs), which offers tutorials, samples, guidance on mobile development, and a full API reference.

Flutter SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS and Android applications.

The latest version of the iOS SDK you can always find in our public repository

\[https://github.com/flittpayments/flutter(https://github.com/flittpayments/flutter)

You can find demo app in [example](https://github.com/flittpayments/flutter/tree/main/example) directory

Android SDK allows you to accept Google Payâ¢ payments from Android application.

# Google Pay Android SDK

Android SDK allows you to accept Google Pay payments from Android application.

The latest version of Android SDK you can always find in our public repository

<https://github.com/flittpayments/android-sdk>

In the [demo directory](https://github.com/flittpayments/android-sdk/tree/main/app/src/main/java/com/flitt/android/demo) you can find an example of an application which implements Google Pay functionality

Also, you can refer the central Maven repository: <https://central.sonatype.com/artifact/com.flitt/flitt-android> and use SDK as maven dependency.

**1 Setup your application**

Add dependencies to your project in app/build.gradle. This implementation requires Google Play services 17.0.0 or greater

```
implementation 'com.google.android.gms:play-services-base:17.0.0'
implementation 'com.google.android.gms:play-services-wallet:19.4.0'
implementation 'com.flitt:flitt-android:1.2.0'

```

**2 Update AndroidManifest.xml to enable Google Pay API.**

Add the following lines:

```
<uses-permission android:name="android.permission.INTERNET" />
<meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true"
>

```

For more information please follow Google Pay API [setup instruction](https://developers.google.com/pay/api/android/guides/setup)

**3 Setup your MearchantId**

Create an instance of Cloudipsp with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

```
cloudipsp = new Cloudipsp(<your merchant_id>, webView);

```

**4 Create Google Pay button in your application layout**

```
<Button
    android:id="@+id/google_pay_button"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Pay with Google Pay" />

```

And add CloudIpspdWebView Component

```
<com.flittpayments.android.CloudipspWebView
    android:id="@+id/webView"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:visibility="gone" 
/>

```

**5 Implement the Activity.java file as follows:**

```
import com.flittpayments.android.Cloudipsp

Public class MainActivity extends AppCompatActivity implements
        View.OnClickListener, // Implementing OnClickListener for handling button clicks
        Cloudipsp.PayCallback, // Implementing Cloudipsp.PayCallback for payment callbacks
        Cloudipsp.GooglePayCallback { // Implementing Cloudipsp.GooglePayCallback for Google Pay callbacks

}

```

**6 Make sure that Google Pay is supported on the device and user account**

```
googlePayButton = findViewById(R.id.google_pay_button); // Initialize Button from layout

// Check if Google Pay is supported and set button visibility accordingly
if (Cloudipsp.supportsGooglePay(this)) {
    googlePayButton.setVisibility(View.VISIBLE); // Show Google Pay button
} else {
    googlePayButton.setVisibility(View.GONE); // Hide Google Pay button if unsupported
    Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show(); // Show unsupported message
}

```

**7 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
{
  "response":{
    "response_status":"success",
    "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
  }
}

```

**8 Add click listener on Google Pay button**

```
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main); // Set the layout for this activity

    // Initialize UI elements
    webView = findViewById(R.id.webView); // Initialize CloudipspWebView from layout
    googlePayButton = findViewById(R.id.google_pay_button); // Initialize Button from layout

    googlePayButton.setOnClickListener(this); // Set click listener for Google Pay button

    if (Cloudipsp.supportsGooglePay(this)) {
        googlePayButton.setVisibility(View.VISIBLE); 
    } else {
        googlePayButton.setVisibility(View.GONE); 
        Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show();
    }
}

@Override
public void onClick(View v) {
    if (v.getId() == R.id.google_pay_button) {
        processGooglePay(); 
    }
}

```

**9 Process googlePay**

Declare and initialize CloudipspWebView

```
private CloudipspWebView webView;

```

Initialize CloudipspWebView from Layout

```
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main); 

    webView = findViewById(R.id.webView); // Initialize CloudipspWebView 

}

```

Initialize Cloudipsp with 0 merchant ID and WebView (token instead of merchant ID will be taken from step 7)

```
private void processGooglePay() {
    cloudipsp = new Cloudipsp(0, webView);
}

```

Handle Google Pay initialization if needed

```
@Override
public void onGooglePayInitialized(GooglePayCall result) {
    Toast.makeText(this, "Google Pay initialized", Toast.LENGTH_LONG).show(); // Show Google Pay initialization message
    this.googlePayCall = result; // Store Google Pay call result
}

```

Initiate the payment process, call method â `googlePayInitialize` with token

```
if (Cloudipsp.supportsGooglePay(context)) {
    cloudipsp?.googlePayInitialize(
        paymentToken,
        context.findActivity(),
        MainActivity.RC_GOOGLE_PAY,
        googlePayCallback
    )
}

```

cloudipsp.googlePayInitialize get 4 params : paymentToken , activity , request code And Google Pay callback

WebView 3DSecure confirmation

After initiating the payment process, the configured 3DS WebView will open. In test mode, it should look like this :

Handle payment failure

```
@Override
public void onPaidFailure(Cloudipsp.Exception e) {
    if (e instanceof Cloudipsp.Exception.Failure) {
        Cloudipsp.Exception.Failure f = (Cloudipsp.Exception.Failure) e;
        Toast.makeText(this, "Failure\nErrorCode: " +
                f.errorCode + "\nMessage: " + f.getMessage() + "\nRequestId: " + f.requestId, Toast.LENGTH_LONG).show(); // Show specific failure details
    } else if (e instanceof Cloudipsp.Exception.NetworkSecurity) {
        Toast.makeText(this, "Network security error: " + e.getMessage(), Toast.LENGTH_LONG).show(); // Show network security error
    } else if (e instanceof Cloudipsp.Exception.ServerInternalError) {
        Toast.makeText(this, "Internal server error: " + e.getMessage(), Toast.LENGTH_LONG).show(); // Show internal server error
    } else if (e instanceof Cloudipsp.Exception.NetworkAccess) {
        Toast.makeText(this, "Network error", Toast.LENGTH_LONG).show(); // Show network access error
    } else {
        Toast.makeText(this, "Payment Failed", Toast.LENGTH_LONG).show(); // Show generic payment failure
    }
    e.printStackTrace(); // Print stack trace for debugging
}

```

**10 Complete payment**

Pass the result from onActivityResult to the SDK.

```
@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    switch (requestCode) {
        case RC_GOOGLE_PAY:
            if (!cloudipsp.googlePayComplete(resultCode, data, googlePayCall, this)) {
                Toast.makeText(this, R.string.e_google_pay_canceled, Toast.LENGTH_LONG).show(); // Show payment canceled message
            }
            break;
    }
}

```

Handle Result of payment

```
@Override
public void onPaidProcessed(Receipt receipt) {
    Toast.makeText(this, "Paid " + receipt.status.name() + "\nPaymentId:" + receipt.paymentId, Toast.LENGTH_LONG).show(); // Show payment success message
}

```

Handle back navigation

```
@Override
public void onBackPressed() {
    if (webView.waitingForConfirm()) {
        webView.skipConfirm(); // Skip confirmation in WebView if waiting
    } else {
        super.onBackPressed(); // Otherwise, perform default back button behavior
    }
}

```

If your activity is destroyed and recreated (e.g., due to a screen rotation), onSaveInstanceState() ensures that googlePayCall, which is presumably a critical object related to payment processing, is saved (`putParcelable()`) and restored (`onRestoreInstanceState()`) properly.

```
private GooglePayCall googlePayCall; // <- this should be serialized on saving instance state

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main); // Set the layout for this activity

    if (savedInstanceState != null) {
        googlePayCall = savedInstanceState.getParcelable(K_GOOGLE_PAY_CALL);
    }
}

```

Save instance

```
@Override
protected void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);
    outState.putParcelable(K_GOOGLE_PAY_CALL, googlePayCall);
}

```

Complete example of MainActivity code ( java )

```
package com.example.cloudipspAndroidSdkExampleJava;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.flittpayments.android.Cloudipsp;
import com.flittpayments.android.CloudipspWebView;
import com.flittpayments.android.GooglePayCall;
import com.flittpayments.android.Order;
import com.flittpayments.android.Receipt;

public class MainActivity extends AppCompatActivity implements
        View.OnClickListener, // Implementing OnClickListener for handling button clicks
        Cloudipsp.PayCallback, // Implementing Cloudipsp.PayCallback for payment callbacks
        Cloudipsp.GooglePayCallback { // Implementing Cloudipsp.GooglePayCallback for Google Pay callbacks

    private static final int RC_GOOGLE_PAY = 100500;
    private static final String K_GOOGLE_PAY_CALL = "google_pay_call";
    private Cloudipsp cloudipsp;
    private GooglePayCall googlePayCall; // <- this should be serialized on saving instance state
    private CloudipspWebView webView;
    private Button googlePayButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main); // Set the layout for this activity

        // Initialize UI elements
        webView = findViewById(R.id.webView); // Initialize CloudipspWebView from layout
        googlePayButton = findViewById(R.id.google_pay_button); // Initialize Button from layout
        googlePayButton.setOnClickListener(this); // Set click listener for Google Pay button

        // Check if Google Pay is supported and set button visibility accordingly
        if (Cloudipsp.supportsGooglePay(this)) {
            googlePayButton.setVisibility(View.VISIBLE); // Show Google Pay button
        } else {
            googlePayButton.setVisibility(View.GONE); // Hide Google Pay button if unsupported
            Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show(); // Show unsupported message
        }

        if (savedInstanceState != null) {
            googlePayCall = savedInstanceState.getParcelable(K_GOOGLE_PAY_CALL);
        }
    }

    @Override
    public void onBackPressed() {
        if (webView.waitingForConfirm()) {
            webView.skipConfirm(); // Skip confirmation in WebView if waiting
        } else {
            super.onBackPressed(); // Otherwise, perform default back button behavior
        }
    }


    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.google_pay_button) {
            processGooglePay(); // Handle click on Google Pay button
        }
    }

    private void processGooglePay() {
        cloudipsp = new Cloudipsp(0, webView);
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putParcelable(K_GOOGLE_PAY_CALL, googlePayCall);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        switch (requestCode) {
            case RC_GOOGLE_PAY:
                if (!cloudipsp.googlePayComplete(resultCode, data, googlePayCall, this)) {
                    Toast.makeText(this, R.string.e_google_pay_canceled, Toast.LENGTH_LONG).show(); // Show payment canceled message
                }
                break;
        }
    }

    @Override
    public void onPaidProcessed(Receipt receipt) {
        Toast.makeText(this, "Paid " + receipt.status.name() + "\nPaymentId:" + receipt.paymentId, Toast.LENGTH_LONG).show(); // Show payment success message
    }

    @Override
    public void onPaidFailure(Cloudipsp.Exception e) {
        if (e instanceof Cloudipsp.Exception.Failure) {
            Cloudipsp.Exception.Failure f = (Cloudipsp.Exception.Failure) e;
            Toast.makeText(this, "Failure\nErrorCode: " +
                    f.errorCode + "\nMessage: " + f.getMessage() + "\nRequestId: " + f.requestId, Toast.LENGTH_LONG).show(); // Show specific failure details
        } else if (e instanceof Cloudipsp.Exception.NetworkSecurity) {
            Toast.makeText(this, "Network security error: " + e.getMessage(), Toast.LENGTH_LONG).show(); // Show network security error
        } else if (e instanceof Cloudipsp.Exception.ServerInternalError) {
            Toast.makeText(this, "Internal server error: " + e.getMessage(), Toast.LENGTH_LONG).show(); // Show internal server error
        } else if (e instanceof Cloudipsp.Exception.NetworkAccess) {
            Toast.makeText(this, "Network error", Toast.LENGTH_LONG).show(); // Show network access error
        } else {
            Toast.makeText(this, "Payment Failed", Toast.LENGTH_LONG).show(); // Show generic payment failure
        }
        e.printStackTrace(); // Print stack trace for debugging
    }

    @Override
    public void onGooglePayInitialized(GooglePayCall result) {
        // Handle Google Pay initialization if needed
        Toast.makeText(this, "Google Pay initialized", Toast.LENGTH_LONG).show(); // Show Google Pay initialization message
        this.googlePayCall = result; // Store Google Pay call result
    }
}

```

**1 Setup your application**

Add dependencies to your project in app/build.gradle.This implementation requires Google Play services 17.0.0 or greater

```
implementation("com.google.android.gms:play-services-base:17.0.0")
implementation("com.google.android.gms:play-services-wallet:19.4.0")
implementation("com.flittpayments:android:+")

```

**2 Update AndroidManifest.xml to enable Google Pay API.**

```
<uses-permission android:name="android.permission.INTERNET" />
<meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true"
>

```

**3 Setup your MearchantId**

Create an instance of Cloudipsp with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

```
cloudipsp = new Cloudipsp(<your merchant_id>, webView);

```

**4 Create Google Pay button in your application layout**

```
<Button
    android:id="@+id/google_pay_button"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Pay with Google Pay" />

```

And add CloudIpspdWebView Component

```
<com.flittpayments.android.CloudipspWebView
    android:id="@+id/webView"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:visibility="gone" 
/>

```

**5 Implement the Activity.kt file as follows**

```
import com.flittpayments.android.Cloudipsp
class MainActivity : AppCompatActivity(), View.OnClickListener, Cloudipsp.PayCallback, Cloudipsp.GooglePayCallback {
}

```

**6 Make sure that Google Pay is supported on the device and user account**

```
googlePayButton = findViewById(R.id.google_pay_button); // Initialize Button from layout

// Check if Google Pay is supported and set button visibility accordingly
if (Cloudipsp.supportsGooglePay(this)) {
    googlePayButton.setVisibility(View.VISIBLE); // Show Google Pay button
} else {
    googlePayButton.setVisibility(View.GONE); // Hide Google Pay button if unsupported
    Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show(); // Show unsupported message
}

```

**7 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
{
  "response":{
    "response_status":"success",
    "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
  }
}

```

**8 Add click listener on Google Pay button**

```
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main) // Set the layout for this activity

    // Initialize UI elements
    webView = findViewById(R.id.webView) // Initialize CloudipspWebView from layout
    googlePayButton = findViewById(R.id.google_pay_button) // Initialize Button from layout
    googlePayButton.setOnClickListener(this) // Set click listener for Google Pay button

    // Check if Google Pay is supported and set button visibility accordingly
    if (Cloudipsp.supportsGooglePay(this)) {
        googlePayButton.visibility = View.VISIBLE // Show Google Pay button
    } else {
        googlePayButton.visibility = View.GONE // Hide Google Pay button if unsupported
        Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show() // Show unsupported message
    }
}

override fun onClick(v: View) {
    if (v.id == R.id.google_pay_button) {
        processGooglePay() // Handle click on Google Pay button
    }
}

```

**9 Process googlePay**

Declare and initialize CloudipspWebView

```
private lateinit var webView: CloudipspWebView

```

Initialize CloudipspWebView from Layout

```
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main) // Set the layout for this activity
    webView = findViewById(R.id.webView) // Initialize CloudipspWebView from layout
}

```

Initialize Cloudipsp with 0 merchant ID and WebView (token instead of merchant ID will be taken from step 7)

```
private fun processGooglePay() {
    cloudipsp = Cloudipsp(0, webView) 
}

```

Handle Google Pay initialization if needed

```
override fun onGooglePayInitialized(result: GooglePayCall) {
    // Handle Google Pay initialization if needed
    Toast.makeText(this, "Google Pay initialized", Toast.LENGTH_LONG).show() // Show Google Pay initialization message
    googlePayCall = result // Store Google Pay call result
}

```

Initiate the payment process, call method â `googlePayInitialize` with token

```
if (Cloudipsp.supportsGooglePay(context)) {
    cloudipsp?.googlePayInitialize(
        paymentToken,
        context.findActivity(),
        MainActivity.RC_GOOGLE_PAY,
        googlePayCallback
    )
}

```

cloudipsp.googlePayInitialize get 4 params : paymentToken , activity , request code And Google Pay callback

WebView 3DSecure confirmation

After initiating the payment process, the configured 3DS WebView will open. In test mode, it should look like this :

Handle payment failure

```
override fun onPaidFailure(e: Cloudipsp.Exception) {
    when (e) {
        is Cloudipsp.Exception.Failure -> {
            Toast.makeText(this, "Failure\nErrorCode: ${e.errorCode}\nMessage: ${e.message}\nRequestId: ${e.requestId}", Toast.LENGTH_LONG).show() // Show specific failure details
        }
        is Cloudipsp.Exception.NetworkSecurity -> {
            Toast.makeText(this, "Network security error: ${e.message}", Toast.LENGTH_LONG).show() // Show network security error
        }
        is Cloudipsp.Exception.ServerInternalError -> {
            Toast.makeText(this, "Internal server error: ${e.message}", Toast.LENGTH_LONG).show() // Show internal server error
        }
        is Cloudipsp.Exception.NetworkAccess -> {
            Toast.makeText(this, "Network error", Toast.LENGTH_LONG).show() // Show network access error
        }
        else -> {
            Toast.makeText(this, "Payment Failed", Toast.LENGTH_LONG).show() // Show generic payment failure
        }
    }
    e.printStackTrace() // Print stack trace for debugging
}

```

**10 Complete payment**

Pass the result from onActivityResult to the SDK.

```
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    super.onActivityResult(requestCode, resultCode, data)
    when (requestCode) {
        RC_GOOGLE_PAY -> {
            if (!cloudipsp?.googlePayComplete(resultCode, data, googlePayCall, this)!!) {
                Toast.makeText(this, R.string.e_google_pay_canceled, Toast.LENGTH_LONG).show() // Show payment canceled message
            }
        }
    }
}

```

Handle Result of payment

```
override fun onPaidProcessed(receipt: Receipt) {
    Toast.makeText(this, "Paid ${receipt.status.name}\nPaymentId:${receipt.paymentId}", Toast.LENGTH_LONG).show() // Show payment success message
}

```

Handle back navigation

```
override fun onBackPressed() {
    if (webView.isWaitingForConfirm) {
        webView.skipConfirm() // Skip confirmation in WebView if waiting
    } else {
        super.onBackPressed() // Otherwise, perform default back button behavior
    }
}

```

Save instance

```
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putParcelable(K_GOOGLE_PAY_CALL, googlePayCall)
}

```

Complete example of MainActivity code

```
package com.example.cloudipspAndroidSdkExampleKotlin

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.flittpayments.android.Cloudipsp
import com.flittpayments.android.CloudipspWebView
import com.flittpayments.android.GooglePayCall
import com.flittpayments.android.Order
import com.flittpayments.android.Receipt

class MainActivity : AppCompatActivity(), View.OnClickListener, Cloudipsp.PayCallback, Cloudipsp.GooglePayCallback {

    private val RC_GOOGLE_PAY = 100500
    private val K_GOOGLE_PAY_CALL = "google_pay_call"
    private var cloudipsp: Cloudipsp? = null
    private var googlePayCall: GooglePayCall? = null // <- this should be serialized on saving instance state
    private lateinit var webView: CloudipspWebView
    private lateinit var googlePayButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main) // Set the layout for this activity

        // Initialize UI elements
        webView = findViewById(R.id.webView) // Initialize CloudipspWebView from layout
        googlePayButton = findViewById(R.id.google_pay_button) // Initialize Button from layout
        googlePayButton.setOnClickListener(this) // Set click listener for Google Pay button

        // Check if Google Pay is supported and set button visibility accordingly
        if (Cloudipsp.supportsGooglePay(this)) {
            googlePayButton.visibility = View.VISIBLE // Show Google Pay button
        } else {
            googlePayButton.visibility = View.GONE // Hide Google Pay button if unsupported
            Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show() // Show unsupported message
        }
        if (savedInstanceState != null) {
            googlePayCall = savedInstanceState.getParcelable(K_GOOGLE_PAY_CALL)
        }
    }

    override fun onBackPressed() {
        if (webView.waitingForConfirm()) {
            webView.skipConfirm() // Skip confirmation in WebView if waiting
        } else {
            super.onBackPressed() // Otherwise, perform default back button behavior
        }
    }

    override fun onClick(v: View) {
        if (v.id == R.id.google_pay_button) {
            processGooglePay() // Handle click on Google Pay button
        }
    }


    if (Cloudipsp.supportsGooglePay(context)) {
        cloudipsp?.googlePayInitialize(
            paymentToken,
            context.findActivity(),
            MainActivity.RC_GOOGLE_PAY,
            googlePayCallback
        )
    }
    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putParcelable(K_GOOGLE_PAY_CALL, googlePayCall)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        when (requestCode) {
            RC_GOOGLE_PAY -> {
                if (!cloudipsp?.googlePayComplete(resultCode, data, googlePayCall, this)!!) {
                    Toast.makeText(this, R.string.e_google_pay_canceled, Toast.LENGTH_LONG).show() // Show payment canceled message
                }
            }
        }
    }

    override fun onPaidProcessed(receipt: Receipt) {
        Toast.makeText(this, "Paid ${receipt.status.name}\nPaymentId:${receipt.paymentId}", Toast.LENGTH_LONG).show() // Show payment success message
    }

    override fun onPaidFailure(e: Cloudipsp.Exception) {
        when (e) {
            is Cloudipsp.Exception.Failure -> {
                Toast.makeText(this, "Failure\nErrorCode: ${e.errorCode}\nMessage: ${e.message}\nRequestId: ${e.requestId}", Toast.LENGTH_LONG).show() // Show specific failure details
            }
            is Cloudipsp.Exception.NetworkSecurity -> {
                Toast.makeText(this, "Network security error: ${e.message}", Toast.LENGTH_LONG).show() // Show network security error
            }
            is Cloudipsp.Exception.ServerInternalError -> {
                Toast.makeText(this, "Internal server error: ${e.message}", Toast.LENGTH_LONG).show() // Show internal server error
            }
            is Cloudipsp.Exception.NetworkAccess -> {
                Toast.makeText(this, "Network error", Toast.LENGTH_LONG).show() // Show network access error
            }
            else -> {
                Toast.makeText(this, "Payment Failed", Toast.LENGTH_LONG).show() // Show generic payment failure
            }
        }
        e.printStackTrace() // Print stack trace for debugging
    }

    override fun onGooglePayInitialized(result: GooglePayCall) {
        // Handle Google Pay initialization if needed
        Toast.makeText(this, "Google Pay initialized", Toast.LENGTH_LONG).show() // Show Google Pay initialization message
        googlePayCall = result // Store Google Pay call result
    }
}

```

## Google Pay mobile application approval

1. Before integrating Flitt mobile SDK, register merchant in Flitt [Merchant Portal](https://portal.flitt.com) and request Flitt support support@flitt.com to enable Google Pay on your account. You will get a merchant ID in test mode.

1. Build your app using Flitt merchant ID in test mode with Flitt SDK. Flitt SDK will use `ENVIRONMENT_TEST` mode and

   ```
   gatewayMerchantId: <your Flitt merchant_id>
   gatewayID: flitt

   ```

1. Follow instructions to request Google for production access: <https://developers.google.com/pay/api/android/guides/test-and-deploy/publish-your-integration>

1. Google will review the application according to its integration checklist and provide recommendations if necessary.

1. If all requirements are met, production access is granted.

1. Request Flitt support to switch your merchant ID to live with `ENVIRONMENT_PRODUCTION` mode.

1. Submit production APK pointing to live merchant ID to Google for approval.

# Flutter SDK for Mobile(Android)

Getting Started

This project is a starting point for a Flutter [plug-in package](https://flutter.dev/developing-packages/), a specialized package that includes platform-specific implementation code for Android and/or iOS.

For help getting started with Flutter, view [online documentation](https://flutter.dev/docs), which offers tutorials, samples, guidance on mobile development, and a full API reference.

Flutter SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Payâ¢ in any of your iOS and Android applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/flutter>

You can find demo app in [example](https://github.com/flittpayments/flutter/tree/main/example) directory

## Google Pay mobile application approval

1. Before integrating Flitt mobile SDK, register merchant in Flitt [Merchant Portal](https://portal.flitt.com) and request Flitt support support@flitt.com to enable Google Pay on your account. You will get a merchant ID in test mode.

1. Build your app using Flitt merchant ID in test mode with Flitt SDK. Flitt SDK will use `ENVIRONMENT_TEST` mode and

   ```
   gatewayMerchantId: <your Flitt merchant_id>
   gatewayID: flitt

   ```

1. Follow instructions to request Google for production access: <https://developers.google.com/pay/api/android/guides/test-and-deploy/publish-your-integration>

1. Google will review the application according to its integration checklist and provide recommendations if necessary.

1. If all requirements are met, production access is granted.

1. Request Flitt support to switch your merchant ID to live with `ENVIRONMENT_PRODUCTION` mode.

1. Submit production APK pointing to live merchant ID to Google for approval.

## Step by step instruction to implement Google Payâ¢ with React-Native

Use the [Flitt React-Native Android SDK](https://github.com/flittpayments/react-native) to start accepting Google Pay in your Android apps.

See example how to process Google Pay in [Flitt Github repo](https://github.com/flittpayments/react-native/blob/main/Example/ApplePayGpay.tsx)

**1 Installation**

```
npm install @flittpayments/react-native-flitt --save
# or
yarn add @flittpayments/react-native-flitt

```

**2 Add lines to** android/settings.gradle\*\*:\*\*

```
include ':flittpayments_react-native-flitt'
project(':flittpayments_react-native-flitt').projectDir = new File(rootProject.projectDir, '../node_modules/@flittpayments/react-native-flitt/android')

```

**3 Add dependencies to** android/app/build.gradle\*\*\*\*

```
implementation project(':flittpayments_react-native-flitt')
implementation 'com.google.android.gms:play-services-base:16.0.1'
implementation 'com.google.android.gms:play-services-wallet:16.0.1'

```

**4 Specify meta-data in AndroidManifest.xml**

```
<application â¦ >

  <meta-data
        android:name="com.google.android.gms.wallet.api.enabled"
        android:value="true"
  />

</application>

```

Required permission

```
<uses-permission android:name="android.permission.INTERNET" />

```

**5 Make sure that Google Pay is supported on the device and user account**

```
import { Cloudipsp } from '@flittpayments/react-native-flitt';
const supportsGooglePay = await Cloudipsp.supportsGooglePay();

```

Function to check if the device supports Apple Pay or Google Pay:

```
// State to manage if the device supports Apple Pay or Google Pay
const [supportedPayments, setSupportedPayments] = useState({
   applePay:false,
   googlePay:false
});

const isSupportingAppleOrGPay = async () => {
    const isIOS = Platform.OS === 'ios';

    // Check for Apple Pay support on iOS devices
    if (isIOS) {
        const supportsApplePay = await Cloudipsp.supportsApplePay();
        if (supportsApplePay) {
            setSupportedPayments({ ...supportedPayments,applePay:true });
            return;
        }
        Alert.alert('Apple Pay is not supported on this device');
    }

    // Check for Google Pay support on Android devices
    const supportsGooglePay = await Cloudipsp.supportsGooglePay();
    if (supportsGooglePay) {
        setSupportedPayments( { ...supportedPayments, googlePay: true } );
        return;
    }
    Alert.alert('Google Pay is not supported on this device');
};

// useEffect to run the payment support check when the component mounts
useEffect(() => {
    isSupportingAppleOrGPay();
}, []);

```

**6 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
{
  "response":{
    "response_status":"success",
    "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
  }
}

```

**7 Payment process**

```
import { CloudipspWebView } from '@flittpayments/react-native-flitt';

       // State to manage the visibility of the WebView
const [webView, setWebView] = useState(0);

// Reference to the Cloudipsp WebView component
const _cloudipspWebViewRef = useRef<CloudipspWebView>(null);

```

Function to initialize the Cloudipsp instance with the Merchant ID ( this function should be called inside `handleGooglePayPress` ) the second param of this class will be called inside `cloudipsp.googlePay(order)`

```
const _cloudipsp = (): Cloudipsp => {
    return new Cloudipsp(Merchant, (payConfirmator) => {
        setWebView(1); // Show the WebView for payment confirmation
        return payConfirmator(_cloudipspWebViewRef.current!);
    });
};

```

Process with googlePayToken function. Pass payment token, obtained in step 6

```
// Function to handle the Google Pay button press
const handleGooglePayPressWithToken = async () => {

    const cloudipsp = _cloudipsp(); // Initialize the payment process with the merchant ID

    try {
        // Process the Google Pay transaction and return the receipt
        const receipt = await cloudipsp.googlePayToken('b3c178ad84446ef36eaab365b1e12e6987e9b3d9');
        setWebView(0); // Hide the WebView after payment processing
        console.log('Payment successful:', receipt);
    } catch (error) {
        // Handle payment errors
        console.error('Payment error:', error);
    }
};

```

Full code example can be found in [Flitt Github repo](https://github.com/flittpayments/react-native/blob/main/Example/ApplePayGpay.tsx)

## Google Pay mobile application approval

1. Before integrating Flitt mobile SDK, register merchant in Flitt [Merchant Portal](https://portal.flitt.com) and request Flitt support support@flitt.com to enable Google Pay on your account. You will get a merchant ID in test mode.

1. Build your app using Flitt merchant ID in test mode with Flitt SDK. Flitt SDK will use `ENVIRONMENT_TEST` mode and

   ```
   gatewayMerchantId: <your Flitt merchant_id>
   gatewayID: flitt

   ```

1. Follow instructions to request Google for production access: <https://developers.google.com/pay/api/android/guides/test-and-deploy/publish-your-integration>

1. Google will review the application according to its integration checklist and provide recommendations if necessary.

1. If all requirements are met, production access is granted.

1. Request Flitt support to switch your merchant ID to live with `ENVIRONMENT_PRODUCTION` mode.

1. Submit production APK pointing to live merchant ID to Google for approval.

# Google Payâ¢ purchases in mobile via web-view

You can use **web-view** integration of Google Pay in your mobile application. **Web-view** integration is actually a replacement of native SDKs with the JavaScript SDK.

## How to integrate

Use <https://codepen.io/flitt/pen/GRVXjKY> code as an example.

### Step 1. Create endpoint on your backend

Endpoint will be requested by your frontend to obtain payment `token` value. Endpoint should be integrated as described in [instructions](https://docs.flitt.com/api/create-order/#merchant-embedded-checkout-page-with-payment-token). It means, that backend will `POST https://pay.flitt.com/api/checkout/token` the order data and obtain `token` value in response

### Step 2. Rewrite function `request()` from [code example](https://codepen.io/flitt/pen/GRVXjKY)

```
    function request() {
      return new Promise((resolve) =>
        setTimeout(() => resolve("_token"), 300)
      );
    }

```

to obtain payment `token` from your backend. Here `_token` should be replaced with backend `token` value.

### Step 3. Place your merchant_id and initial amount into `params` block

```
    const params = {
      merchant_id: 1549901,
      currency: "GEL",
      amount: 100
    };

```

this is required to draw initial Google Pay button

### Step4. Obtain payment token from backend.

As soon as Google Pay button is clicked, `request()` function will be executed to request new `token` from your backend endpoint from Step 1. Google Pay button will use `token` string returned.

### Step5. Process callback on frontend with receipt object

Analyze `receipt` object to get the payment result. But you should not trust this response, until your backend receives callback and validate response `signature`.

### Step6. Process callback on your backend, specified in `server_callback_url` parameters.

Check `orders_status` and `signature` parameters to validate the result.

# iOS SDK (Swift)

iOS SDK allows you to accept payment from Visa/MasterCard and Apple Pay in any of your iOS applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/ios-sdk>

To run the sample of application, run the command

```
git clone git@github.com:flittpayments/ios-sdk.git
cd ios-sdk/Example
pod install

```

iOS SDK is also available through CocoaPods. To install it, simply add the following line to your Podfile:

```
pod 'Flitt'

```

Example for Swift you can find by the link <https://github.com/flittpayments/ios-sdk/tree/master/ExampleSwift>

**1 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
    {
      "response":{
        "response_status":"success",
        "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
      }
    }

```

**2 Define properties**

`PSCardInputView` is required to securely process card data inputs. Card data can't be obtained by application due to PCI DSS requirements.\
`PSCloudipspWKWebView` is required to redirect payer to webview during 3DSecure authentication.\
`PSCloudipspApi` is main class for payment initiation.

```
@property (nonatomic, weak) IBOutlet PSCardInputView *cardInputView;
@property (nonatomic, strong) PSCloudipspWKWebView *webView;
@property (nonatomic, strong) PSCloudipspApi *api;

```

**3 Create layouts for card inputs**

```
// LAYOUT FIELDS
self.cardNumberTextField = [[PSCardNumberTextField alloc] initWithFrame:CGRectMake(20, 8, 280, 30)];
self.cardNumberTextField.placeholder = @"Card Number";
[self.fields addObject:self.cardNumberTextField];

self.expMonthTextField = [[PSExpMonthTextField alloc] initWithFrame:CGRectMake(20, 46, 136, 30)];
self.expMonthTextField.placeholder = @"MM";
[self.fields addObject:self.expMonthTextField];

self.expYearTextField = [[PSExpYearTextField alloc] initWithFrame:CGRectMake(164, 46, 136, 30)];
self.expYearTextField.placeholder = @"YY";
[self.fields addObject:self.expYearTextField];

self.cvvTextField = [[PSCVVTextField alloc] initWithFrame:CGRectMake(20, 84, 280, 30)];
self.cvvTextField.placeholder = @"CVV";
[self.fields addObject:self.cvvTextField];

self.cardInputLayout = [[PSCardInputLayout alloc] initWithFrame:CGRectMake(0, 216, 320, 122)
                                            cardNumberTextField:self.cardNumberTextField
                                              expMonthTextField:self.expMonthTextField
                                               expYearTextField:self.expYearTextField
                                                   cvvTextField:self.cvvTextField];
[self.scrollView addSubview:self.cardInputLayout];

```

**4 Create layout for payment button**

```
    // PAY CONTROL
    self.payButton = [[UIButton alloc] initWithFrame:CGRectMake(20, CGRectGetMaxY(self.cardInputLayout.frame), 280, 30)];
    [self.payButton setTitle:@"Pay" forState:UIControlStateNormal];
    [self.payButton setBackgroundColor:[UIColor colorWithRed:255.f/255.f green:204.f/255.f blue:102.f/255.f alpha:1.0]];
    self.payButton.layer.cornerRadius = 5.f;
    [self.payButton addTarget:self action:@selector(pay:) forControlEvents:UIControlEventTouchUpInside];
    [self.scrollView addSubview:self.payButton];

```

**5 Setup 3DSecure webview**

```
#pragma mark - Setup WebView

- (void)setupWebView {
    self.webView = [[PSCloudipspWKWebView alloc] initWithFrame:CGRectMake(0, 64, self.view.bounds.size.width, self.view.bounds.size.height - 66)];
    [self.view insertSubview:self.webView aboveSubview:self.scrollView];
}

```

**6 Initialize PSCloudipspApi object**

```
self.api = [PSCloudipspApi apiWithMerchant:1396424 andCloudipspView:self.webView];

```

where `1396424` should be replaced with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

**7 Process payment on pay button click using payment token obtained on step 1**

```
- (IBAction)pay:(UIButton *)sender {
    PSCard *card = [self.cardInputLayout confirm:self];
    if (card != nil) {
        [self taskWillStarted];
        [self.api pay:card withToken:token andDelegate:self];
    }
}

```

**8 Process payment result from `PSReceipt` object**

```
#pragma mark - PayCallbackDelegate


- (void)onPaidProcess:(PSReceipt *)receipt {
    self.result = [NSString stringWithFormat:NSLocalizedString(@"PAID_STATUS_KEY", nil), [PSReceipt getStatusName:receipt.status], (long)receipt.paymentId];
    [self taskDidFinished];
    [self navigate];
    //for getting all response fields
    //[PSReceiptUtils dumpFields:receipt];
}

- (void)onPaidFailure:(NSError *)error {
    if ([error code] == PSPayErrorCodeFailure) {
        NSDictionary *info = [error userInfo];
        self.result = [NSString stringWithFormat:@"PayError. Code %@\nDescription: %@", [info valueForKey:@"error_code"], [info valueForKey:@"error_message"]];
    } else {
        self.result = [NSString stringWithFormat:@"Error: %@", [error localizedDescription]];
    }
    [self navigate];
    [self taskDidFinished];
}

```

# iOS SDK (Objective-C)

iOS SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/ios-sdk>

To run the sample of application, run the command

```
git clone git@github.com:flittpayments/ios-sdk.git
cd ios-sdk/Example
pod install

```

Cloudipsp SDK is also available through CocoaPods. To install it, simply add the following line to your Podfile:

```
pod 'Flitt'

```

Example for Objective-C you can find by the link <https://github.com/flittpayments/ios-sdk/tree/master/Example>

Use the [Flitt React Native](https://github.com/flittpayments/react-native) to start accepting Google Pay, Apple Pay and cards in your apps.

**Installation**

```
npm install @flittpayments/react-native-flitt --save
# or
yarn add @flittpayments/react-native-flitt

```

### Android Setup

**1 Add lines to** android/settings.gradle\*\*:\*\*

```
include ':flittpayments_react-native-flitt'
project(':flittpayments_react-native-flitt').projectDir = new File(rootProject.projectDir, '../node_modules/@flittpayments/react-native-flitt/android')

```

**2 Add dependencies to** android/app/build.gradle\*\*\*\*

```
dependencies {
    implementation project(':flittpayments_react-native-flitt')
    // Important: This specific version is required for GooglePayButton to work correctly
    implementation 'com.google.android.gms:play-services-wallet:19.4.0'
}

```

**3 MainApplication.java**

Register the package in your MainApplication.java file:

```
@Override
protected List<ReactPackage> getPackages() {
    @SuppressWarnings("UnnecessaryLocalVariable")
    List<ReactPackage> packages = new PackageList(this).getPackages();
    packages.add(new RNFlittPackage());
    return packages;
}

```

**4 Specify meta-data in AndroidManifest.xml**

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

<application ... >
<meta-data
android:name="com.google.android.gms.wallet.api.enabled"
android:value="true" />
        </application>

```

### iOS Setup

**1 Register as an Apple Developer**

To implement Apple Pay, you need to [Register Apple Merchant ID](/api/applepay-getting-started/#register-apple-merchant-id) and [Create Apple Pay certificates](/api/applepay-getting-started/#create-new-apple-pay-certificates)

**2 Configure Apple Pay in Xcode**

- In Xcode, select your project
- Go to the "Signing & Capabilities" tab
- Click "+ Capability" and add "Apple Pay"
- Add your Merchant ID to the Apple Pay section
- Configure your payment processing certificate in the Apple Developer portal

**3 Update Info.plist** Add the following to your Info.plist:

```
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>

```

\*\* Check exaple folder on our GitHub on how to implement payments with cards and wallets\*\*

- [Basic Usage](https://github.com/flittpayments/react-native#basic-usage)
- [card form](https://github.com/flittpayments/react-native/blob/master/Example/index.tsx)
- [Apple and Google Pay](https://github.com/flittpayments/react-native/blob/master/Example/ApplePayGpay.tsx)

\*\* If you need Google and Apple Pay, refer to these articles:\*\*

- [Apple Pay](/api/applepay-getting-started/)
- [Google Pay](/api/googlepay-getting-started/)
# Mobile SDKs

# Android SDK

Android SDK allows you to accept Google Pay payments from Android application.

The latest version of Android SDK you can always find in our public repository

<https://github.com/flittpayments/android-sdk>

In the [demo directory](https://github.com/flittpayments/android-sdk/tree/main/app/src/main/java/com/flitt/android/demo) you can find an example of an application which implements Google Pay functionality

Also, you can refer the central Maven repository: <https://central.sonatype.com/search?q=flitt-android>

**1 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
    {
      "response":{
        "response_status":"success",
        "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
      }
    }

```

**2 Setup your application**

Add dependencies to your project in app/build.gradle. This implementation requires Google Play services 17.0.0 or greater

```
implementation 'com.google.android.gms:play-services-base:17.0.0'
implementation 'com.google.android.gms:play-services-wallet:19.4.0'
implementation 'com.flitt:flitt-android:1.2.0'

```

**3 Update AndroidManifest.xml to enable Google Pay API if required**

Add the following lines:

```
<uses-permission android:name="android.permission.INTERNET" />
<meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true"
>

```

For more information please follow Google Pay API [setup instruction](https://developers.google.com/pay/api/android/guides/setup)

**4 Setup your MearchantId**

Create an instance of Cloudipsp with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

Attach webview, which will responsible for payer redirection to 3DSecure page

```
webView = findViewById(R.id.web_view);
cloudipsp = new Cloudipsp(<your merchant_id>, webView);

```

**5 Process payment once payer sumbits data and card object is returned**

Pass payment token from step 1 to method `payToken`

```
final Card card = getCard();
    if (card != null) {
       cloudipsp.payToken(card, token, this);
    }

```

**6 Follow Demo folder on our GitHub to see examples on how to add card form to your application**

<https://github.com/flittpayments/android-sdk/tree/main/app/src/main/java/com/flitt/android/demo>

**1 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
    {
      "response":{
        "response_status":"success",
        "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
      }
    }

```

**2 Setup your application**

Add dependencies to your project in app/build.gradle.This implementation requires Google Play services 17.0.0 or greater

```
implementation("com.google.android.gms:play-services-base:17.0.0")
implementation("com.google.android.gms:play-services-wallet:19.4.0")
implementation("com.flitt:flitt-android:1.2.0")

```

**3 Update AndroidManifest.xml to enable Google Pay API if required.**

```
<uses-permission android:name="android.permission.INTERNET" />
<meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true"
>

```

**4 Setup your MearchantId**

Create an instance of Cloudipsp with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

Attach webview, which will responsible for payer redirection to 3DSecure page

```
webView = findViewById(R.id.web_view);
cloudipsp = new Cloudipsp(<your merchant_id>, webView);

```

**5 Process payment once payer sumbits data and card object is returned**

Pass payment token from step 1 to method `payToken`

```
final Card card = getCard();
    if (card != null) {
       cloudipsp.payToken(card, token, this);
    }

```

**6 Follow Demo folder on our GitHub to see examples on how to add card form to your application**

<https://github.com/flittpayments/android-sdk/tree/main/app/src/main/java/com/flitt/android/demo>

# Flutter SDK for Mobile(iOS)

Getting Started

This project is a starting point for a Flutter [plug-in package](https://flutter.dev/developing-packages/), a specialized package that includes platform-specific implementation code for Android and/or iOS.

For help getting started with Flutter, view [online documentation](https://flutter.dev/docs), which offers tutorials, samples, guidance on mobile development, and a full API reference.

Flutter SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS and Android applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/flutter>

You can find demo app in [example](https://github.com/flittpayments/flutter/tree/main/example) directory

Before SDK integration, pass the steps to [register Apple Merchant ID](/api/applepay-getting-started/)

After creation, put the generated MerchantID in settings:

XCode -> Target -> Capabilities -> Apple Pay -> Merchant IDS

# iOS SDK (Swift)

iOS SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/ios-sdk>

To run the sample of application, run the command

```
git clone git@github.com:flittpayments/ios-sdk.git
cd ios-sdk/Example
pod install

```

iOS SDK is also available through CocoaPods. To install it, simply add the following line to your Podfile:

```
pod 'Flitt'

```

Example for Swift you can find by the link <https://github.com/flittpayments/ios-sdk/tree/master/ExampleSwift>

Integrate SDK putting the generated MerchantID in 2 places

1. In XCode -> Target -> Capabilities -> Apple Pay -> Merchant IDS

1. In integration SDK set `merchant_id` received during registration in Flitt [Merchant Portal](https://portal.flitt.com) in constructor instead of test 900234

   ```
   <textField opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="left" contentVerticalAlignment="center" text="1396424" borderStyle="roundedRect" placeholder="Enter merchant id" textAlignment="natural" minimumFontSize="17" translatesAutoresizingMaskIntoConstraints="NO" id="8pz-e9-tsn">

   ```

   github line link: <https://github.com/flittpayments/ios-sdk/blob/master/ExampleSwift/ExampleSwift/Base.lproj/Main.storyboard#L19>

# iOS SDK (Objective-C)

iOS SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/ios-sdk>

To run the sample of application, run the command

```
git clone git@github.com:flittpayments/ios-sdk.git
cd ios-sdk/Example
pod install

```

iOS SDK is also available through CocoaPods. To install it, simply add the following line to your Podfile:

```
pod 'Flitt'

```

Example for Objective-C you can find by the link <https://github.com/flittpayments/ios-sdk/tree/master/Example>

Integrate SDK putting the generated MerchantID in 2 places

1. In XCode -> Target -> Capabilities -> Apple Pay -> Merchant IDS

1. In integration SDK set `merchant_id` received during registration in Flitt [Merchant Portal](https://portal.flitt.com) in constructor instead of test 1396424

   ```
   - (void)viewDidLoad {
       [super viewDidLoad];

        self.api = [PSCloudipspApi apiWithMerchant:1396424 andCloudipspView:nil];
   }   

   ```

github line link: <https://github.com/flittpayments/ios-sdk/blob/master/Example/Cloudipsp/CDStartViewController.m#L24>

# React Native SDK

React Native SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your React applications.

The latest version of SDK you can always find in our public repository

<https://github.com/flittpayments/react-native>

## Step 1: Integrate Apple Pay in your application setting

See Apple Pay Merchant IDs settings in XCode: ApplePayMerchant -> Target -> Capabilities -> Apple Pay -> Merchant IDS

# Apple Pay purchases in mobile via web-view

You can use **web-view** integration of Apple Pay in your mobile application. **Web-view** integration is actually a replacement of native SDKs with the JavaScript SDK.

## How to integrate

Use <https://codepen.io/flitt/pen/GRVXjKY> code as an example.

### Step 1. Create endpoint on your backend

Endpoint will be requested by your frontend to obtain payment `token` value. Endpoint should be integrated as described in [instructions](https://docs.flitt.com/api/create-order/#merchant-embedded-checkout-page-with-payment-token). It means, that backend will `POST https://pay.flitt.com/api/checkout/token` the order data and obtain `token` value in response

### Step 2. Rewrite function `request()` from [code example](https://codepen.io/flitt/pen/GRVXjKY)

```
    function request() {
      return new Promise((resolve) =>
        setTimeout(() => resolve("_token"), 300)
      );
    }

```

to obtain payment `token` from your backend. Here `_token` should be replaced with backend `token` value.

### Step 3. Place your merchant_id and initial amount into `params` block

```
    const params = {
      merchant_id: 1549901,
      currency: "GEL",
      amount: 100
    };

```

this is required to draw initial Apple Pay button

### Step4. Obtain payment token from backend.

As soon as Apple Pay button is clicked, `request()` function will be executed to request new `token` from your backend endpoint from Step 1. Apple Pay button will use `token` string returned.

### Step5. Process callback on frontend with receipt object

Analyze `receipt` object to get the payment result. But you should not trust this response, until your backend receives callback and validate response `signature`.

### Step6. Process callback on your backend, specified in `server_callback_url` parameters.

Check `orders_status` and `signature` parameters to validate the result.

# Flutter SDK for Mobile(iOS)

Getting Started

This project is a starting point for a Flutter [plug-in package](https://flutter.dev/developing-packages/), a specialized package that includes platform-specific implementation code for Android and/or iOS.

For help getting started with Flutter, view [online documentation](https://flutter.dev/docs), which offers tutorials, samples, guidance on mobile development, and a full API reference.

Flutter SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS and Android applications.

The latest version of the iOS SDK you can always find in our public repository

\[https://github.com/flittpayments/flutter(https://github.com/flittpayments/flutter)

You can find demo app in [example](https://github.com/flittpayments/flutter/tree/main/example) directory

Android SDK allows you to accept Google Payâ¢ payments from Android application.

# Google Pay Android SDK

Android SDK allows you to accept Google Pay payments from Android application.

The latest version of Android SDK you can always find in our public repository

<https://github.com/flittpayments/android-sdk>

In the [demo directory](https://github.com/flittpayments/android-sdk/tree/main/app/src/main/java/com/flitt/android/demo) you can find an example of an application which implements Google Pay functionality

Also, you can refer the central Maven repository: <https://central.sonatype.com/artifact/com.flitt/flitt-android> and use SDK as maven dependency.

**1 Setup your application**

Add dependencies to your project in app/build.gradle. This implementation requires Google Play services 17.0.0 or greater

```
implementation 'com.google.android.gms:play-services-base:17.0.0'
implementation 'com.google.android.gms:play-services-wallet:19.4.0'
implementation 'com.flitt:flitt-android:1.2.0'

```

**2 Update AndroidManifest.xml to enable Google Pay API.**

Add the following lines:

```
<uses-permission android:name="android.permission.INTERNET" />
<meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true"
>

```

For more information please follow Google Pay API [setup instruction](https://developers.google.com/pay/api/android/guides/setup)

**3 Setup your MearchantId**

Create an instance of Cloudipsp with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

```
cloudipsp = new Cloudipsp(<your merchant_id>, webView);

```

**4 Create Google Pay button in your application layout**

```
<Button
    android:id="@+id/google_pay_button"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Pay with Google Pay" />

```

And add CloudIpspdWebView Component

```
<com.flittpayments.android.CloudipspWebView
    android:id="@+id/webView"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:visibility="gone" 
/>

```

**5 Implement the Activity.java file as follows:**

```
import com.flittpayments.android.Cloudipsp

Public class MainActivity extends AppCompatActivity implements
        View.OnClickListener, // Implementing OnClickListener for handling button clicks
        Cloudipsp.PayCallback, // Implementing Cloudipsp.PayCallback for payment callbacks
        Cloudipsp.GooglePayCallback { // Implementing Cloudipsp.GooglePayCallback for Google Pay callbacks

}

```

**6 Make sure that Google Pay is supported on the device and user account**

```
googlePayButton = findViewById(R.id.google_pay_button); // Initialize Button from layout

// Check if Google Pay is supported and set button visibility accordingly
if (Cloudipsp.supportsGooglePay(this)) {
    googlePayButton.setVisibility(View.VISIBLE); // Show Google Pay button
} else {
    googlePayButton.setVisibility(View.GONE); // Hide Google Pay button if unsupported
    Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show(); // Show unsupported message
}

```

**7 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
{
  "response":{
    "response_status":"success",
    "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
  }
}

```

**8 Add click listener on Google Pay button**

```
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main); // Set the layout for this activity

    // Initialize UI elements
    webView = findViewById(R.id.webView); // Initialize CloudipspWebView from layout
    googlePayButton = findViewById(R.id.google_pay_button); // Initialize Button from layout

    googlePayButton.setOnClickListener(this); // Set click listener for Google Pay button

    if (Cloudipsp.supportsGooglePay(this)) {
        googlePayButton.setVisibility(View.VISIBLE); 
    } else {
        googlePayButton.setVisibility(View.GONE); 
        Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show();
    }
}

@Override
public void onClick(View v) {
    if (v.getId() == R.id.google_pay_button) {
        processGooglePay(); 
    }
}

```

**9 Process googlePay**

Declare and initialize CloudipspWebView

```
private CloudipspWebView webView;

```

Initialize CloudipspWebView from Layout

```
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main); 

    webView = findViewById(R.id.webView); // Initialize CloudipspWebView 

}

```

Initialize Cloudipsp with 0 merchant ID and WebView (token instead of merchant ID will be taken from step 7)

```
private void processGooglePay() {
    cloudipsp = new Cloudipsp(0, webView);
}

```

Handle Google Pay initialization if needed

```
@Override
public void onGooglePayInitialized(GooglePayCall result) {
    Toast.makeText(this, "Google Pay initialized", Toast.LENGTH_LONG).show(); // Show Google Pay initialization message
    this.googlePayCall = result; // Store Google Pay call result
}

```

Initiate the payment process, call method â `googlePayInitialize` with token

```
if (Cloudipsp.supportsGooglePay(context)) {
    cloudipsp?.googlePayInitialize(
        paymentToken,
        context.findActivity(),
        MainActivity.RC_GOOGLE_PAY,
        googlePayCallback
    )
}

```

cloudipsp.googlePayInitialize get 4 params : paymentToken , activity , request code And Google Pay callback

WebView 3DSecure confirmation

After initiating the payment process, the configured 3DS WebView will open. In test mode, it should look like this :

Handle payment failure

```
@Override
public void onPaidFailure(Cloudipsp.Exception e) {
    if (e instanceof Cloudipsp.Exception.Failure) {
        Cloudipsp.Exception.Failure f = (Cloudipsp.Exception.Failure) e;
        Toast.makeText(this, "Failure\nErrorCode: " +
                f.errorCode + "\nMessage: " + f.getMessage() + "\nRequestId: " + f.requestId, Toast.LENGTH_LONG).show(); // Show specific failure details
    } else if (e instanceof Cloudipsp.Exception.NetworkSecurity) {
        Toast.makeText(this, "Network security error: " + e.getMessage(), Toast.LENGTH_LONG).show(); // Show network security error
    } else if (e instanceof Cloudipsp.Exception.ServerInternalError) {
        Toast.makeText(this, "Internal server error: " + e.getMessage(), Toast.LENGTH_LONG).show(); // Show internal server error
    } else if (e instanceof Cloudipsp.Exception.NetworkAccess) {
        Toast.makeText(this, "Network error", Toast.LENGTH_LONG).show(); // Show network access error
    } else {
        Toast.makeText(this, "Payment Failed", Toast.LENGTH_LONG).show(); // Show generic payment failure
    }
    e.printStackTrace(); // Print stack trace for debugging
}

```

**10 Complete payment**

Pass the result from onActivityResult to the SDK.

```
@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    switch (requestCode) {
        case RC_GOOGLE_PAY:
            if (!cloudipsp.googlePayComplete(resultCode, data, googlePayCall, this)) {
                Toast.makeText(this, R.string.e_google_pay_canceled, Toast.LENGTH_LONG).show(); // Show payment canceled message
            }
            break;
    }
}

```

Handle Result of payment

```
@Override
public void onPaidProcessed(Receipt receipt) {
    Toast.makeText(this, "Paid " + receipt.status.name() + "\nPaymentId:" + receipt.paymentId, Toast.LENGTH_LONG).show(); // Show payment success message
}

```

Handle back navigation

```
@Override
public void onBackPressed() {
    if (webView.waitingForConfirm()) {
        webView.skipConfirm(); // Skip confirmation in WebView if waiting
    } else {
        super.onBackPressed(); // Otherwise, perform default back button behavior
    }
}

```

If your activity is destroyed and recreated (e.g., due to a screen rotation), onSaveInstanceState() ensures that googlePayCall, which is presumably a critical object related to payment processing, is saved (`putParcelable()`) and restored (`onRestoreInstanceState()`) properly.

```
private GooglePayCall googlePayCall; // <- this should be serialized on saving instance state

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main); // Set the layout for this activity

    if (savedInstanceState != null) {
        googlePayCall = savedInstanceState.getParcelable(K_GOOGLE_PAY_CALL);
    }
}

```

Save instance

```
@Override
protected void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);
    outState.putParcelable(K_GOOGLE_PAY_CALL, googlePayCall);
}

```

Complete example of MainActivity code ( java )

```
package com.example.cloudipspAndroidSdkExampleJava;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.flittpayments.android.Cloudipsp;
import com.flittpayments.android.CloudipspWebView;
import com.flittpayments.android.GooglePayCall;
import com.flittpayments.android.Order;
import com.flittpayments.android.Receipt;

public class MainActivity extends AppCompatActivity implements
        View.OnClickListener, // Implementing OnClickListener for handling button clicks
        Cloudipsp.PayCallback, // Implementing Cloudipsp.PayCallback for payment callbacks
        Cloudipsp.GooglePayCallback { // Implementing Cloudipsp.GooglePayCallback for Google Pay callbacks

    private static final int RC_GOOGLE_PAY = 100500;
    private static final String K_GOOGLE_PAY_CALL = "google_pay_call";
    private Cloudipsp cloudipsp;
    private GooglePayCall googlePayCall; // <- this should be serialized on saving instance state
    private CloudipspWebView webView;
    private Button googlePayButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main); // Set the layout for this activity

        // Initialize UI elements
        webView = findViewById(R.id.webView); // Initialize CloudipspWebView from layout
        googlePayButton = findViewById(R.id.google_pay_button); // Initialize Button from layout
        googlePayButton.setOnClickListener(this); // Set click listener for Google Pay button

        // Check if Google Pay is supported and set button visibility accordingly
        if (Cloudipsp.supportsGooglePay(this)) {
            googlePayButton.setVisibility(View.VISIBLE); // Show Google Pay button
        } else {
            googlePayButton.setVisibility(View.GONE); // Hide Google Pay button if unsupported
            Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show(); // Show unsupported message
        }

        if (savedInstanceState != null) {
            googlePayCall = savedInstanceState.getParcelable(K_GOOGLE_PAY_CALL);
        }
    }

    @Override
    public void onBackPressed() {
        if (webView.waitingForConfirm()) {
            webView.skipConfirm(); // Skip confirmation in WebView if waiting
        } else {
            super.onBackPressed(); // Otherwise, perform default back button behavior
        }
    }


    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.google_pay_button) {
            processGooglePay(); // Handle click on Google Pay button
        }
    }

    private void processGooglePay() {
        cloudipsp = new Cloudipsp(0, webView);
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putParcelable(K_GOOGLE_PAY_CALL, googlePayCall);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        switch (requestCode) {
            case RC_GOOGLE_PAY:
                if (!cloudipsp.googlePayComplete(resultCode, data, googlePayCall, this)) {
                    Toast.makeText(this, R.string.e_google_pay_canceled, Toast.LENGTH_LONG).show(); // Show payment canceled message
                }
                break;
        }
    }

    @Override
    public void onPaidProcessed(Receipt receipt) {
        Toast.makeText(this, "Paid " + receipt.status.name() + "\nPaymentId:" + receipt.paymentId, Toast.LENGTH_LONG).show(); // Show payment success message
    }

    @Override
    public void onPaidFailure(Cloudipsp.Exception e) {
        if (e instanceof Cloudipsp.Exception.Failure) {
            Cloudipsp.Exception.Failure f = (Cloudipsp.Exception.Failure) e;
            Toast.makeText(this, "Failure\nErrorCode: " +
                    f.errorCode + "\nMessage: " + f.getMessage() + "\nRequestId: " + f.requestId, Toast.LENGTH_LONG).show(); // Show specific failure details
        } else if (e instanceof Cloudipsp.Exception.NetworkSecurity) {
            Toast.makeText(this, "Network security error: " + e.getMessage(), Toast.LENGTH_LONG).show(); // Show network security error
        } else if (e instanceof Cloudipsp.Exception.ServerInternalError) {
            Toast.makeText(this, "Internal server error: " + e.getMessage(), Toast.LENGTH_LONG).show(); // Show internal server error
        } else if (e instanceof Cloudipsp.Exception.NetworkAccess) {
            Toast.makeText(this, "Network error", Toast.LENGTH_LONG).show(); // Show network access error
        } else {
            Toast.makeText(this, "Payment Failed", Toast.LENGTH_LONG).show(); // Show generic payment failure
        }
        e.printStackTrace(); // Print stack trace for debugging
    }

    @Override
    public void onGooglePayInitialized(GooglePayCall result) {
        // Handle Google Pay initialization if needed
        Toast.makeText(this, "Google Pay initialized", Toast.LENGTH_LONG).show(); // Show Google Pay initialization message
        this.googlePayCall = result; // Store Google Pay call result
    }
}

```

**1 Setup your application**

Add dependencies to your project in app/build.gradle.This implementation requires Google Play services 17.0.0 or greater

```
implementation("com.google.android.gms:play-services-base:17.0.0")
implementation("com.google.android.gms:play-services-wallet:19.4.0")
implementation("com.flittpayments:android:+")

```

**2 Update AndroidManifest.xml to enable Google Pay API.**

```
<uses-permission android:name="android.permission.INTERNET" />
<meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true"
>

```

**3 Setup your MearchantId**

Create an instance of Cloudipsp with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

```
cloudipsp = new Cloudipsp(<your merchant_id>, webView);

```

**4 Create Google Pay button in your application layout**

```
<Button
    android:id="@+id/google_pay_button"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Pay with Google Pay" />

```

And add CloudIpspdWebView Component

```
<com.flittpayments.android.CloudipspWebView
    android:id="@+id/webView"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:visibility="gone" 
/>

```

**5 Implement the Activity.kt file as follows**

```
import com.flittpayments.android.Cloudipsp
class MainActivity : AppCompatActivity(), View.OnClickListener, Cloudipsp.PayCallback, Cloudipsp.GooglePayCallback {
}

```

**6 Make sure that Google Pay is supported on the device and user account**

```
googlePayButton = findViewById(R.id.google_pay_button); // Initialize Button from layout

// Check if Google Pay is supported and set button visibility accordingly
if (Cloudipsp.supportsGooglePay(this)) {
    googlePayButton.setVisibility(View.VISIBLE); // Show Google Pay button
} else {
    googlePayButton.setVisibility(View.GONE); // Hide Google Pay button if unsupported
    Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show(); // Show unsupported message
}

```

**7 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
{
  "response":{
    "response_status":"success",
    "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
  }
}

```

**8 Add click listener on Google Pay button**

```
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main) // Set the layout for this activity

    // Initialize UI elements
    webView = findViewById(R.id.webView) // Initialize CloudipspWebView from layout
    googlePayButton = findViewById(R.id.google_pay_button) // Initialize Button from layout
    googlePayButton.setOnClickListener(this) // Set click listener for Google Pay button

    // Check if Google Pay is supported and set button visibility accordingly
    if (Cloudipsp.supportsGooglePay(this)) {
        googlePayButton.visibility = View.VISIBLE // Show Google Pay button
    } else {
        googlePayButton.visibility = View.GONE // Hide Google Pay button if unsupported
        Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show() // Show unsupported message
    }
}

override fun onClick(v: View) {
    if (v.id == R.id.google_pay_button) {
        processGooglePay() // Handle click on Google Pay button
    }
}

```

**9 Process googlePay**

Declare and initialize CloudipspWebView

```
private lateinit var webView: CloudipspWebView

```

Initialize CloudipspWebView from Layout

```
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main) // Set the layout for this activity
    webView = findViewById(R.id.webView) // Initialize CloudipspWebView from layout
}

```

Initialize Cloudipsp with 0 merchant ID and WebView (token instead of merchant ID will be taken from step 7)

```
private fun processGooglePay() {
    cloudipsp = Cloudipsp(0, webView) 
}

```

Handle Google Pay initialization if needed

```
override fun onGooglePayInitialized(result: GooglePayCall) {
    // Handle Google Pay initialization if needed
    Toast.makeText(this, "Google Pay initialized", Toast.LENGTH_LONG).show() // Show Google Pay initialization message
    googlePayCall = result // Store Google Pay call result
}

```

Initiate the payment process, call method â `googlePayInitialize` with token

```
if (Cloudipsp.supportsGooglePay(context)) {
    cloudipsp?.googlePayInitialize(
        paymentToken,
        context.findActivity(),
        MainActivity.RC_GOOGLE_PAY,
        googlePayCallback
    )
}

```

cloudipsp.googlePayInitialize get 4 params : paymentToken , activity , request code And Google Pay callback

WebView 3DSecure confirmation

After initiating the payment process, the configured 3DS WebView will open. In test mode, it should look like this :

Handle payment failure

```
override fun onPaidFailure(e: Cloudipsp.Exception) {
    when (e) {
        is Cloudipsp.Exception.Failure -> {
            Toast.makeText(this, "Failure\nErrorCode: ${e.errorCode}\nMessage: ${e.message}\nRequestId: ${e.requestId}", Toast.LENGTH_LONG).show() // Show specific failure details
        }
        is Cloudipsp.Exception.NetworkSecurity -> {
            Toast.makeText(this, "Network security error: ${e.message}", Toast.LENGTH_LONG).show() // Show network security error
        }
        is Cloudipsp.Exception.ServerInternalError -> {
            Toast.makeText(this, "Internal server error: ${e.message}", Toast.LENGTH_LONG).show() // Show internal server error
        }
        is Cloudipsp.Exception.NetworkAccess -> {
            Toast.makeText(this, "Network error", Toast.LENGTH_LONG).show() // Show network access error
        }
        else -> {
            Toast.makeText(this, "Payment Failed", Toast.LENGTH_LONG).show() // Show generic payment failure
        }
    }
    e.printStackTrace() // Print stack trace for debugging
}

```

**10 Complete payment**

Pass the result from onActivityResult to the SDK.

```
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    super.onActivityResult(requestCode, resultCode, data)
    when (requestCode) {
        RC_GOOGLE_PAY -> {
            if (!cloudipsp?.googlePayComplete(resultCode, data, googlePayCall, this)!!) {
                Toast.makeText(this, R.string.e_google_pay_canceled, Toast.LENGTH_LONG).show() // Show payment canceled message
            }
        }
    }
}

```

Handle Result of payment

```
override fun onPaidProcessed(receipt: Receipt) {
    Toast.makeText(this, "Paid ${receipt.status.name}\nPaymentId:${receipt.paymentId}", Toast.LENGTH_LONG).show() // Show payment success message
}

```

Handle back navigation

```
override fun onBackPressed() {
    if (webView.isWaitingForConfirm) {
        webView.skipConfirm() // Skip confirmation in WebView if waiting
    } else {
        super.onBackPressed() // Otherwise, perform default back button behavior
    }
}

```

Save instance

```
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putParcelable(K_GOOGLE_PAY_CALL, googlePayCall)
}

```

Complete example of MainActivity code

```
package com.example.cloudipspAndroidSdkExampleKotlin

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.flittpayments.android.Cloudipsp
import com.flittpayments.android.CloudipspWebView
import com.flittpayments.android.GooglePayCall
import com.flittpayments.android.Order
import com.flittpayments.android.Receipt

class MainActivity : AppCompatActivity(), View.OnClickListener, Cloudipsp.PayCallback, Cloudipsp.GooglePayCallback {

    private val RC_GOOGLE_PAY = 100500
    private val K_GOOGLE_PAY_CALL = "google_pay_call"
    private var cloudipsp: Cloudipsp? = null
    private var googlePayCall: GooglePayCall? = null // <- this should be serialized on saving instance state
    private lateinit var webView: CloudipspWebView
    private lateinit var googlePayButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main) // Set the layout for this activity

        // Initialize UI elements
        webView = findViewById(R.id.webView) // Initialize CloudipspWebView from layout
        googlePayButton = findViewById(R.id.google_pay_button) // Initialize Button from layout
        googlePayButton.setOnClickListener(this) // Set click listener for Google Pay button

        // Check if Google Pay is supported and set button visibility accordingly
        if (Cloudipsp.supportsGooglePay(this)) {
            googlePayButton.visibility = View.VISIBLE // Show Google Pay button
        } else {
            googlePayButton.visibility = View.GONE // Hide Google Pay button if unsupported
            Toast.makeText(this, R.string.e_google_pay_unsupported, Toast.LENGTH_LONG).show() // Show unsupported message
        }
        if (savedInstanceState != null) {
            googlePayCall = savedInstanceState.getParcelable(K_GOOGLE_PAY_CALL)
        }
    }

    override fun onBackPressed() {
        if (webView.waitingForConfirm()) {
            webView.skipConfirm() // Skip confirmation in WebView if waiting
        } else {
            super.onBackPressed() // Otherwise, perform default back button behavior
        }
    }

    override fun onClick(v: View) {
        if (v.id == R.id.google_pay_button) {
            processGooglePay() // Handle click on Google Pay button
        }
    }


    if (Cloudipsp.supportsGooglePay(context)) {
        cloudipsp?.googlePayInitialize(
            paymentToken,
            context.findActivity(),
            MainActivity.RC_GOOGLE_PAY,
            googlePayCallback
        )
    }
    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putParcelable(K_GOOGLE_PAY_CALL, googlePayCall)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        when (requestCode) {
            RC_GOOGLE_PAY -> {
                if (!cloudipsp?.googlePayComplete(resultCode, data, googlePayCall, this)!!) {
                    Toast.makeText(this, R.string.e_google_pay_canceled, Toast.LENGTH_LONG).show() // Show payment canceled message
                }
            }
        }
    }

    override fun onPaidProcessed(receipt: Receipt) {
        Toast.makeText(this, "Paid ${receipt.status.name}\nPaymentId:${receipt.paymentId}", Toast.LENGTH_LONG).show() // Show payment success message
    }

    override fun onPaidFailure(e: Cloudipsp.Exception) {
        when (e) {
            is Cloudipsp.Exception.Failure -> {
                Toast.makeText(this, "Failure\nErrorCode: ${e.errorCode}\nMessage: ${e.message}\nRequestId: ${e.requestId}", Toast.LENGTH_LONG).show() // Show specific failure details
            }
            is Cloudipsp.Exception.NetworkSecurity -> {
                Toast.makeText(this, "Network security error: ${e.message}", Toast.LENGTH_LONG).show() // Show network security error
            }
            is Cloudipsp.Exception.ServerInternalError -> {
                Toast.makeText(this, "Internal server error: ${e.message}", Toast.LENGTH_LONG).show() // Show internal server error
            }
            is Cloudipsp.Exception.NetworkAccess -> {
                Toast.makeText(this, "Network error", Toast.LENGTH_LONG).show() // Show network access error
            }
            else -> {
                Toast.makeText(this, "Payment Failed", Toast.LENGTH_LONG).show() // Show generic payment failure
            }
        }
        e.printStackTrace() // Print stack trace for debugging
    }

    override fun onGooglePayInitialized(result: GooglePayCall) {
        // Handle Google Pay initialization if needed
        Toast.makeText(this, "Google Pay initialized", Toast.LENGTH_LONG).show() // Show Google Pay initialization message
        googlePayCall = result // Store Google Pay call result
    }
}

```

## Google Pay mobile application approval

1. Before integrating Flitt mobile SDK, register merchant in Flitt [Merchant Portal](https://portal.flitt.com) and request Flitt support support@flitt.com to enable Google Pay on your account. You will get a merchant ID in test mode.

1. Build your app using Flitt merchant ID in test mode with Flitt SDK. Flitt SDK will use `ENVIRONMENT_TEST` mode and

   ```
   gatewayMerchantId: <your Flitt merchant_id>
   gatewayID: flitt

   ```

1. Follow instructions to request Google for production access: <https://developers.google.com/pay/api/android/guides/test-and-deploy/publish-your-integration>

1. Google will review the application according to its integration checklist and provide recommendations if necessary.

1. If all requirements are met, production access is granted.

1. Request Flitt support to switch your merchant ID to live with `ENVIRONMENT_PRODUCTION` mode.

1. Submit production APK pointing to live merchant ID to Google for approval.

# Flutter SDK for Mobile(Android)

Getting Started

This project is a starting point for a Flutter [plug-in package](https://flutter.dev/developing-packages/), a specialized package that includes platform-specific implementation code for Android and/or iOS.

For help getting started with Flutter, view [online documentation](https://flutter.dev/docs), which offers tutorials, samples, guidance on mobile development, and a full API reference.

Flutter SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Payâ¢ in any of your iOS and Android applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/flutter>

You can find demo app in [example](https://github.com/flittpayments/flutter/tree/main/example) directory

## Google Pay mobile application approval

1. Before integrating Flitt mobile SDK, register merchant in Flitt [Merchant Portal](https://portal.flitt.com) and request Flitt support support@flitt.com to enable Google Pay on your account. You will get a merchant ID in test mode.

1. Build your app using Flitt merchant ID in test mode with Flitt SDK. Flitt SDK will use `ENVIRONMENT_TEST` mode and

   ```
   gatewayMerchantId: <your Flitt merchant_id>
   gatewayID: flitt

   ```

1. Follow instructions to request Google for production access: <https://developers.google.com/pay/api/android/guides/test-and-deploy/publish-your-integration>

1. Google will review the application according to its integration checklist and provide recommendations if necessary.

1. If all requirements are met, production access is granted.

1. Request Flitt support to switch your merchant ID to live with `ENVIRONMENT_PRODUCTION` mode.

1. Submit production APK pointing to live merchant ID to Google for approval.

## Step by step instruction to implement Google Payâ¢ with React-Native

Use the [Flitt React-Native Android SDK](https://github.com/flittpayments/react-native) to start accepting Google Pay in your Android apps.

See example how to process Google Pay in [Flitt Github repo](https://github.com/flittpayments/react-native/blob/main/Example/ApplePayGpay.tsx)

**1 Installation**

```
npm install @flittpayments/react-native-flitt --save
# or
yarn add @flittpayments/react-native-flitt

```

**2 Add lines to** android/settings.gradle\*\*:\*\*

```
include ':flittpayments_react-native-flitt'
project(':flittpayments_react-native-flitt').projectDir = new File(rootProject.projectDir, '../node_modules/@flittpayments/react-native-flitt/android')

```

**3 Add dependencies to** android/app/build.gradle\*\*\*\*

```
implementation project(':flittpayments_react-native-flitt')
implementation 'com.google.android.gms:play-services-base:16.0.1'
implementation 'com.google.android.gms:play-services-wallet:16.0.1'

```

**4 Specify meta-data in AndroidManifest.xml**

```
<application â¦ >

  <meta-data
        android:name="com.google.android.gms.wallet.api.enabled"
        android:value="true"
  />

</application>

```

Required permission

```
<uses-permission android:name="android.permission.INTERNET" />

```

**5 Make sure that Google Pay is supported on the device and user account**

```
import { Cloudipsp } from '@flittpayments/react-native-flitt';
const supportsGooglePay = await Cloudipsp.supportsGooglePay();

```

Function to check if the device supports Apple Pay or Google Pay:

```
// State to manage if the device supports Apple Pay or Google Pay
const [supportedPayments, setSupportedPayments] = useState({
   applePay:false,
   googlePay:false
});

const isSupportingAppleOrGPay = async () => {
    const isIOS = Platform.OS === 'ios';

    // Check for Apple Pay support on iOS devices
    if (isIOS) {
        const supportsApplePay = await Cloudipsp.supportsApplePay();
        if (supportsApplePay) {
            setSupportedPayments({ ...supportedPayments,applePay:true });
            return;
        }
        Alert.alert('Apple Pay is not supported on this device');
    }

    // Check for Google Pay support on Android devices
    const supportsGooglePay = await Cloudipsp.supportsGooglePay();
    if (supportsGooglePay) {
        setSupportedPayments( { ...supportedPayments, googlePay: true } );
        return;
    }
    Alert.alert('Google Pay is not supported on this device');
};

// useEffect to run the payment support check when the component mounts
useEffect(() => {
    isSupportingAppleOrGPay();
}, []);

```

**6 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
{
  "response":{
    "response_status":"success",
    "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
  }
}

```

**7 Payment process**

```
import { CloudipspWebView } from '@flittpayments/react-native-flitt';

       // State to manage the visibility of the WebView
const [webView, setWebView] = useState(0);

// Reference to the Cloudipsp WebView component
const _cloudipspWebViewRef = useRef<CloudipspWebView>(null);

```

Function to initialize the Cloudipsp instance with the Merchant ID ( this function should be called inside `handleGooglePayPress` ) the second param of this class will be called inside `cloudipsp.googlePay(order)`

```
const _cloudipsp = (): Cloudipsp => {
    return new Cloudipsp(Merchant, (payConfirmator) => {
        setWebView(1); // Show the WebView for payment confirmation
        return payConfirmator(_cloudipspWebViewRef.current!);
    });
};

```

Process with googlePayToken function. Pass payment token, obtained in step 6

```
// Function to handle the Google Pay button press
const handleGooglePayPressWithToken = async () => {

    const cloudipsp = _cloudipsp(); // Initialize the payment process with the merchant ID

    try {
        // Process the Google Pay transaction and return the receipt
        const receipt = await cloudipsp.googlePayToken('b3c178ad84446ef36eaab365b1e12e6987e9b3d9');
        setWebView(0); // Hide the WebView after payment processing
        console.log('Payment successful:', receipt);
    } catch (error) {
        // Handle payment errors
        console.error('Payment error:', error);
    }
};

```

Full code example can be found in [Flitt Github repo](https://github.com/flittpayments/react-native/blob/main/Example/ApplePayGpay.tsx)

## Google Pay mobile application approval

1. Before integrating Flitt mobile SDK, register merchant in Flitt [Merchant Portal](https://portal.flitt.com) and request Flitt support support@flitt.com to enable Google Pay on your account. You will get a merchant ID in test mode.

1. Build your app using Flitt merchant ID in test mode with Flitt SDK. Flitt SDK will use `ENVIRONMENT_TEST` mode and

   ```
   gatewayMerchantId: <your Flitt merchant_id>
   gatewayID: flitt

   ```

1. Follow instructions to request Google for production access: <https://developers.google.com/pay/api/android/guides/test-and-deploy/publish-your-integration>

1. Google will review the application according to its integration checklist and provide recommendations if necessary.

1. If all requirements are met, production access is granted.

1. Request Flitt support to switch your merchant ID to live with `ENVIRONMENT_PRODUCTION` mode.

1. Submit production APK pointing to live merchant ID to Google for approval.

# Google Payâ¢ purchases in mobile via web-view

You can use **web-view** integration of Google Pay in your mobile application. **Web-view** integration is actually a replacement of native SDKs with the JavaScript SDK.

## How to integrate

Use <https://codepen.io/flitt/pen/GRVXjKY> code as an example.

### Step 1. Create endpoint on your backend

Endpoint will be requested by your frontend to obtain payment `token` value. Endpoint should be integrated as described in [instructions](https://docs.flitt.com/api/create-order/#merchant-embedded-checkout-page-with-payment-token). It means, that backend will `POST https://pay.flitt.com/api/checkout/token` the order data and obtain `token` value in response

### Step 2. Rewrite function `request()` from [code example](https://codepen.io/flitt/pen/GRVXjKY)

```
    function request() {
      return new Promise((resolve) =>
        setTimeout(() => resolve("_token"), 300)
      );
    }

```

to obtain payment `token` from your backend. Here `_token` should be replaced with backend `token` value.

### Step 3. Place your merchant_id and initial amount into `params` block

```
    const params = {
      merchant_id: 1549901,
      currency: "GEL",
      amount: 100
    };

```

this is required to draw initial Google Pay button

### Step4. Obtain payment token from backend.

As soon as Google Pay button is clicked, `request()` function will be executed to request new `token` from your backend endpoint from Step 1. Google Pay button will use `token` string returned.

### Step5. Process callback on frontend with receipt object

Analyze `receipt` object to get the payment result. But you should not trust this response, until your backend receives callback and validate response `signature`.

### Step6. Process callback on your backend, specified in `server_callback_url` parameters.

Check `orders_status` and `signature` parameters to validate the result.

# iOS SDK (Swift)

iOS SDK allows you to accept payment from Visa/MasterCard and Apple Pay in any of your iOS applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/ios-sdk>

To run the sample of application, run the command

```
git clone git@github.com:flittpayments/ios-sdk.git
cd ios-sdk/Example
pod install

```

iOS SDK is also available through CocoaPods. To install it, simply add the following line to your Podfile:

```
pod 'Flitt'

```

Example for Swift you can find by the link <https://github.com/flittpayments/ios-sdk/tree/master/ExampleSwift>

**1 Initiate payment on backend and obtain payment token**

Create order at your server:

```
curl -i -X POST \
 -H "Content-Type:application/json" \
 -d \
'{
  "request": {
    "server_callback_url": "http://myshop/callback/",
    "order_id": "TestOrder_JSSDK_v2",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test payment",
    "lifetime" : 999999,
    "amount": 1000,
    "signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
  }
}' \
 'https://pay.flitt.com/api/checkout/token'

```

Receive payment token:

```
    {
      "response":{
        "response_status":"success",
        "token":"b3c178ad84446ef36eaab365b1e12e6987e9b3d9"
      }
    }

```

**2 Define properties**

`PSCardInputView` is required to securely process card data inputs. Card data can't be obtained by application due to PCI DSS requirements.\
`PSCloudipspWKWebView` is required to redirect payer to webview during 3DSecure authentication.\
`PSCloudipspApi` is main class for payment initiation.

```
@property (nonatomic, weak) IBOutlet PSCardInputView *cardInputView;
@property (nonatomic, strong) PSCloudipspWKWebView *webView;
@property (nonatomic, strong) PSCloudipspApi *api;

```

**3 Create layouts for card inputs**

```
// LAYOUT FIELDS
self.cardNumberTextField = [[PSCardNumberTextField alloc] initWithFrame:CGRectMake(20, 8, 280, 30)];
self.cardNumberTextField.placeholder = @"Card Number";
[self.fields addObject:self.cardNumberTextField];

self.expMonthTextField = [[PSExpMonthTextField alloc] initWithFrame:CGRectMake(20, 46, 136, 30)];
self.expMonthTextField.placeholder = @"MM";
[self.fields addObject:self.expMonthTextField];

self.expYearTextField = [[PSExpYearTextField alloc] initWithFrame:CGRectMake(164, 46, 136, 30)];
self.expYearTextField.placeholder = @"YY";
[self.fields addObject:self.expYearTextField];

self.cvvTextField = [[PSCVVTextField alloc] initWithFrame:CGRectMake(20, 84, 280, 30)];
self.cvvTextField.placeholder = @"CVV";
[self.fields addObject:self.cvvTextField];

self.cardInputLayout = [[PSCardInputLayout alloc] initWithFrame:CGRectMake(0, 216, 320, 122)
                                            cardNumberTextField:self.cardNumberTextField
                                              expMonthTextField:self.expMonthTextField
                                               expYearTextField:self.expYearTextField
                                                   cvvTextField:self.cvvTextField];
[self.scrollView addSubview:self.cardInputLayout];

```

**4 Create layout for payment button**

```
    // PAY CONTROL
    self.payButton = [[UIButton alloc] initWithFrame:CGRectMake(20, CGRectGetMaxY(self.cardInputLayout.frame), 280, 30)];
    [self.payButton setTitle:@"Pay" forState:UIControlStateNormal];
    [self.payButton setBackgroundColor:[UIColor colorWithRed:255.f/255.f green:204.f/255.f blue:102.f/255.f alpha:1.0]];
    self.payButton.layer.cornerRadius = 5.f;
    [self.payButton addTarget:self action:@selector(pay:) forControlEvents:UIControlEventTouchUpInside];
    [self.scrollView addSubview:self.payButton];

```

**5 Setup 3DSecure webview**

```
#pragma mark - Setup WebView

- (void)setupWebView {
    self.webView = [[PSCloudipspWKWebView alloc] initWithFrame:CGRectMake(0, 64, self.view.bounds.size.width, self.view.bounds.size.height - 66)];
    [self.view insertSubview:self.webView aboveSubview:self.scrollView];
}

```

**6 Initialize PSCloudipspApi object**

```
self.api = [PSCloudipspApi apiWithMerchant:1396424 andCloudipspView:self.webView];

```

where `1396424` should be replaced with your MerchantID identifier from [Flitt Merchant Portal](https://portal.flitt.com)

**7 Process payment on pay button click using payment token obtained on step 1**

```
- (IBAction)pay:(UIButton *)sender {
    PSCard *card = [self.cardInputLayout confirm:self];
    if (card != nil) {
        [self taskWillStarted];
        [self.api pay:card withToken:token andDelegate:self];
    }
}

```

**8 Process payment result from `PSReceipt` object**

```
#pragma mark - PayCallbackDelegate


- (void)onPaidProcess:(PSReceipt *)receipt {
    self.result = [NSString stringWithFormat:NSLocalizedString(@"PAID_STATUS_KEY", nil), [PSReceipt getStatusName:receipt.status], (long)receipt.paymentId];
    [self taskDidFinished];
    [self navigate];
    //for getting all response fields
    //[PSReceiptUtils dumpFields:receipt];
}

- (void)onPaidFailure:(NSError *)error {
    if ([error code] == PSPayErrorCodeFailure) {
        NSDictionary *info = [error userInfo];
        self.result = [NSString stringWithFormat:@"PayError. Code %@\nDescription: %@", [info valueForKey:@"error_code"], [info valueForKey:@"error_message"]];
    } else {
        self.result = [NSString stringWithFormat:@"Error: %@", [error localizedDescription]];
    }
    [self navigate];
    [self taskDidFinished];
}

```

# iOS SDK (Objective-C)

iOS SDK allows you to accept payment from Visa/MasterCard, Apple Pay, Google Pay in any of your iOS applications.

The latest version of the iOS SDK you can always find in our public repository

<https://github.com/flittpayments/ios-sdk>

To run the sample of application, run the command

```
git clone git@github.com:flittpayments/ios-sdk.git
cd ios-sdk/Example
pod install

```

Cloudipsp SDK is also available through CocoaPods. To install it, simply add the following line to your Podfile:

```
pod 'Flitt'

```

Example for Objective-C you can find by the link <https://github.com/flittpayments/ios-sdk/tree/master/Example>

Use the [Flitt React Native](https://github.com/flittpayments/react-native) to start accepting Google Pay, Apple Pay and cards in your apps.

**Installation**

```
npm install @flittpayments/react-native-flitt --save
# or
yarn add @flittpayments/react-native-flitt

```

### Android Setup

**1 Add lines to** android/settings.gradle\*\*:\*\*

```
include ':flittpayments_react-native-flitt'
project(':flittpayments_react-native-flitt').projectDir = new File(rootProject.projectDir, '../node_modules/@flittpayments/react-native-flitt/android')

```

**2 Add dependencies to** android/app/build.gradle\*\*\*\*

```
dependencies {
    implementation project(':flittpayments_react-native-flitt')
    // Important: This specific version is required for GooglePayButton to work correctly
    implementation 'com.google.android.gms:play-services-wallet:19.4.0'
}

```

**3 MainApplication.java**

Register the package in your MainApplication.java file:

```
@Override
protected List<ReactPackage> getPackages() {
    @SuppressWarnings("UnnecessaryLocalVariable")
    List<ReactPackage> packages = new PackageList(this).getPackages();
    packages.add(new RNFlittPackage());
    return packages;
}

```

**4 Specify meta-data in AndroidManifest.xml**

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

<application ... >
<meta-data
android:name="com.google.android.gms.wallet.api.enabled"
android:value="true" />
        </application>

```

### iOS Setup

**1 Register as an Apple Developer**

To implement Apple Pay, you need to [Register Apple Merchant ID](/api/applepay-getting-started/#register-apple-merchant-id) and [Create Apple Pay certificates](/api/applepay-getting-started/#create-new-apple-pay-certificates)

**2 Configure Apple Pay in Xcode**

- In Xcode, select your project
- Go to the "Signing & Capabilities" tab
- Click "+ Capability" and add "Apple Pay"
- Add your Merchant ID to the Apple Pay section
- Configure your payment processing certificate in the Apple Developer portal

**3 Update Info.plist** Add the following to your Info.plist:

```
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>

```

\*\* Check exaple folder on our GitHub on how to implement payments with cards and wallets\*\*

- [Basic Usage](https://github.com/flittpayments/react-native#basic-usage)
- [card form](https://github.com/flittpayments/react-native/blob/master/Example/index.tsx)
- [Apple and Google Pay](https://github.com/flittpayments/react-native/blob/master/Example/ApplePayGpay.tsx)

\*\* If you need Google and Apple Pay, refer to these articles:\*\*

- [Apple Pay](/api/applepay-getting-started/)
- [Google Pay](/api/googlepay-getting-started/)
# SDKs for frontend and backend

## Mobile SDKS

Flitt mobile SDKs provide possibility to embed card payment form and Apple/Google Pay buttons directly into you application.

The main advantages to use Flitt mobile SDKs are:

- you are not required to be a PCI DSS compliant as your application and backend will not access, transmit or store sensitive payment data

- Flitt SDK allows payment methods to be natively embedded in application layout and are easily designed with branded styles and colors

- For Apple and Google Pay Flitt SDK make integration much more simple.\
  No need to pass encrypted payloads to your backend. No need to integrate [Google Pay API](https://developers.google.com/pay/api/android/overview) and [Apple Pay API](https://developer.apple.com/documentation/passkit_apple_pay_and_wallet/apple_pay) and deal with certificates management and decryption. SDK will handle all the integration with Apple and Google on its own.

- **How embedded mobile card form can look like**

  ______________________________________________________________________

- **How embedded mobile card form can look like**

  ______________________________________________________________________

### Steps to integrate mobile SDK

#### Step 1. Create payment token on backend

Use [Merchant embedded checkout page with payment token](/api/create-order/#merchant-embedded-checkout-page-with-payment-token) instructions to create payment and obtain payment `token`.

#### Step 2. Create payment form in mobile application

Use one of Flitt mobile SDKs depending on the framework or programming language your application is developed with:

- [iOS SDK (Objective-C) for cards](/api/mobile/ios/)
- [iOS SDK (Objective-C) for Apple Pay](/api/mobile/apple-ios/)
- [iOS SDK (Swift) for cards](/api/mobile/ios-swift/)
- [iOS SDK (Swift) for Apple Pay](/api/mobile/apple-ios-swift/)
- [React Native for cards](/api/mobile/reactnative/)
- [React Native for Apple Pay](/api/mobile/apple-reactnative/)
- [React Native for Google Pay](/api/mobile/googlepay-reactnative/)
- [Flutter for cards](/api/mobile/flutter/)
- [Flutter for Apple Pay](/api/mobile/apple-flutter/)
- [Flutter for Google Pay](/api/mobile/googlepay-flutter/)
- [Android (Java) for cards](/api/mobile/android/)
- [Android (Java)for Google Pay](/api/mobile/googlepay-android/)

Refer to example applications in each repository to create card payment form or Apple Pay/Google Pay button

#### Step 3. Pass payment token from *Step 1* from your backend to mobile application.

Each SDK have method to process payment with token:

- iOS Apple Pay: [`applePayWithToken()`](https://github.com/flittpayments/ios-sdk/blob/master/Cloudipsp/PSCloudipspApi.h#L60)
- iOS with card: [`withToken()`](https://github.com/flittpayments/ios-sdk/blob/master/Cloudipsp/PSCloudipspApi.h#L54C3-L54C12)
- Android (Java) Google Pay: [`googlePayInitialize(final String token...)`](https://github.com/flittpayments/android-sdk/blob/master/library/src/main/java/com/cloudipsp/android/Cloudipsp.java#L136)
- Android (Java) with card: [`payContinue(final String token...)`](https://github.com/flittpayments/android-sdk/blob/master/library/src/main/java/com/cloudipsp/android/Cloudipsp.java#L524)
- React Native Google Pay: [`googlePayToken()`](https://github.com/flittpayments/react-native/blob/2f2ca76c24e2f0e90d4fb90e146dee4b42f4fe02/src/Cloudipsp.ts#L156)
- React Native Apple Pay: [`applePayToken()`](https://github.com/flittpayments/react-native/blob/2f2ca76c24e2f0e90d4fb90e146dee4b42f4fe02/src/Cloudipsp.ts#L94)
- React Native with card: [`payToken()`](https://github.com/flittpayments/react-native/blob/2f2ca76c24e2f0e90d4fb90e146dee4b42f4fe02/src/Cloudipsp.ts#L74)
- Flutter Google Pay: [`googlePayToken()`](https://github.com/flittpayments/flutter/blob/7bc950056d2242d315c349b26ae8319b1c2c9c8f/lib/src/cloudipsp.dart#L237)
- Flutter Apple Pay: [`applePayToken()`](https://github.com/flittpayments/flutter/blob/7bc950056d2242d315c349b26ae8319b1c2c9c8f/lib/src/cloudipsp.dart#L173)
- Flutter with card: [`payToken()`](https://github.com/flittpayments/flutter/blob/7bc950056d2242d315c349b26ae8319b1c2c9c8f/lib/src/cloudipsp.dart#L128)

## Backend SDKS

[Python](/sdk-and-mobile/sdk/python/)

[PHP](/sdk-and-mobile/sdk/php/)

[C#](/sdk-and-mobile/sdk/csharp/)

[Node.js](/sdk-and-mobile/sdk/nodejs/)

## Frontend SDKs

[JavaScript](/sdk-and-mobile/sdk/js/)

[Vue-js](/api/embedded-custom/)

# C# SDK

C# SDK allows you to accept payment with Visa/MasterCard cards on your website.

Lates version of C# SDK you can always find in our public repository:

<https://github.com/flittpayments/c-sharp-sdk>

# Step by step implementation case

You will find all code examples by [link](https://github.com/flittpayments/c-sharp-sdk/tree/main/FlittSDKSamples)

- [create order](/api/create-order/#__tabbed_2_1) and obtain payment token:

  for this step you need `class Token`

  if you are planing to use recurring payments in future, add parameter `recurring = 'y'` in request:

  ```
  using FlittSDK;
  using FlittSDK.Checkout;

  Config.MerchantId = 1549901;
          Config.SecretKey = "test";

          var req = new TokenRequest {
              order_id = Guid.NewGuid().ToString("N"),
              amount = 100000,
              order_desc = "checkout json demo",
              currency = "GEL"
          };
          var resp = new Token().Post(req);
          if (resp.Error == null) {
              string token = resp.token;
          };

  ```

  in response you will receive payment token in parameter `resp.token`:

- send payment token from `resp.token` to frontend.

  You can choose 2 solutions for web payment form implementation on frontend: [Embedded iframe](/api/embedded-custom/) or [JavaScript native](/sdk-and-mobile/sdk/js/) form both for cards and Apple/Google Pay

  For JavaScript native frontend form pass payment token to JavaScript payment form in dictionary

  ```
      {
       "payment_system":"card",
       "token": `resp.token`,
       "card_number":"16/19-digits number",
       "expiry_date":"Supported formats: MM/YY, MM/YYYY, MMYY, MMYYYY",
       "cvv2":"3-digits number"
       }

  ```

  For Embedded IFrame form pass payment token to payment form in `Options` object (see [example](/api/embedded-custom/#example-with-order-created-on-backend))

  ```
  var Options = {
    options: {
      methods: ['card'],
      methods_disabled: [],
      card_icons: ['mastercard', 'visa', 'maestro'],
      active_tab: 'card',
      fields: false,
      title: 'Demo checkout',
      link: 'https://shop.com',
      full_screen: true,
      button: true,
      email: true
    },
    params: {
      token: `resp.token`
    }
  }
  checkout("#checkout-container", Options);

  ```

  Solution for mobile application you can choose depending on programming language framework you application is developed:

- [Apple Pay](/api/applepay-getting-started/)

- [Google Pay](/api/googlepay-getting-started/)

# JavaScript SDK

JavaScript SDK provides customizable card form to be securely embedded into any html-page.

Example: <https://jsfiddle.net/flitt/0sqtb43m/4/>

**1.Installation**

**Node** If youâre using [Npm](https://npmjs.com/) in your project, you can add `@flittpayments/js-sdk` dependency to `package.json` with following command:

```
npm i --save @flittpayments/js-sdk

```

or add dependency manually:

```
{
  "dependency": {
    "@flittpayments/js-sdk":"^1.2"
  }
}

```

**Manual installation** If you do not use NodeJS, you can download the latest release. Or clone from GitHub the latest developer version

```
git clone git@github.com:flittpayments/js-sdk.git

```

**Quick start**

```
<script src="https://cdn.jsdelivr.net/npm/@flittpayments/js-sdk"></script>

```

**2. Develop html card form using your own design.**

**Basic template**

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  </head>
  <body>
    <script src="https://cdn.jsdelivr.net/npm/@flittpayments/js-sdk"></script>
    <script>
    $checkout('Api').scope(function(){
        this.request('api.checkout.form','request', { Parameters } ).done(function(model){
            model.sendResponse();
            console.log(model.attr('order'));
        }).fail(function(model){
            console.log(model.attr('error'));
        });
    });
    </script>
  </body>
</html>

```

Basic template example: <https://github.com/flittpayments/js-sdk#basic-template>

**3. Create order using Integration Schema C for JavaScript SDK.**

Add parameters `required_rectoken=Y` and `server_callback_url` in your request to obtain recurring token (if you are planning recurring payments) in server callback (`rectoken` parameter).

```
curl -i -X POST \
-H "Content-Type:application/json" \
-d \
'{
"request": {
"server_callback_url": "http://myshop/callback/",
"order_id": "TestOrder2",
"currency": "GEL",
"merchant_id": 1549901,
"order_desc": "Test payment",
"amount": 1000,
"signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
}
}' \
'https://pay.flitt.com/api/checkout/token'

```

Documentation: [create order](/api/create-order/#merchant-embedded-checkout-page-with-payment-token).

Save `token` parameter from response.

```
{
    "response": {
        "response_status": "success",
        "token": "7ddb3fbb03d60787b3972ef8d6fad0f97f7d2f86"
    }
}

```

**4. Load host-to-host token from step 3 into your card details form.**

```
{
 "payment_system":"card",
 "token":"host-to-host generated token",
 "card_number":"16/19-digits number",
 "expiry_date":"Supported formats: MM/YY, MM/YYYY, MMYY, MMYYYY",
 "cvv2":"3-digits number"
 }

```

**5. Use `.on('success')` and `.on('error')` JavaScript callbacks to get result on payment processing.**

`success` â order is approved and amount will be charged `error` â order is declined and amount will not be charged

`model.attr('error.message')` will contain localized error message in case of payment decline. Order information on order status and details will be returned in `model.data.order.order_data`

JavaScript callback example:

```
console.log('success',JSON.stringify(model.attr("order").order_data));

```

```
{
  "response": {
    "rrn": "111111111111",
    "masked_card": "444455XXXXXX1111",
    "sender_cell_phone": "",
    "sender_account": "",
    "currency": "GEL",
    "fee": "",
    "reversal_amount": "0",
    "settlement_amount": "0",
    "actual_amount": "200",
    "response_description": "",
    "sender_email": "test@test.com",
    "order_status": "approved",
    "response_status": "success",
    "order_time": "13.07.2024 01:23:59",
    "actual_currency": "GEL",
    "order_id": "test33694502191",
    "tran_type": "purchase",
    "eci": "5",
    "settlement_date": "",
    "payment_system": "card",
    "approval_code": "123456",
    "merchant_id": 1549901,
    "settlement_currency": "",
    "payment_id": 805243692,
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "200",
    "signature": "b7884b5c4906956fbac4d20390388d913a78c0b0",
    "product_id": "",
    "merchant_data": "Test merchant data",
    "rectoken": "",
    "rectoken_lifetime": "",
    "verification_status": "",
    "parent_order_id": "",
    "fee_oplata": "0",
    "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_test\": true}",
    "response_signature_string": "**********|200|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_**********\": true}|200|123456|444455|VISA|GEL|5|0|444455XXXXXX1111|Test merchant data|1549901|**********33694502191|approved|13.07.2024 01:23:59|805243692|card|success|0|111111111111|**********@**********.com|0|purchase"
  }
}

```

**6. Process final response received as server callbacks to `server_callback_url`.**

Format of final response: [Response](/api/order-parameters/#__tabbed_1_2)

# Node.js SDK

Node.js SDK allows you to accept payment with Visa/MasterCard cards on your website.

The latest version of Node.js SDK you can always find in our public repository:

<https://github.com/flittpayments/node-js-sdk>

**Installation**

```
npm install @flittpayments/flitt-node-js-sdk

```

**Manual installation**

```
git clone -b master https://github.com/flittpayments/node-js-sdk.git

```

**Simple start**

```
const FlittPay = require('@flittpayments/flitt-node-js-sdk')

const flitt = new FlittPay(
  {
    merchantId: 1549901,
    secretKey: 'test'
  }
)
const requestData = {
  order_id: 'Your Order Id',
  order_desc: 'test order',
  currency: 'GEL',
  amount: '1000'
}
flitt.Checkout(requestData).then(data => {
  console.log(data)
}).catch((error) => {
  console.log(error)
})

```

# PHP SDK

PHP SDK allows you to accept payment with Visa/MasterCard cards on your website.

Lates version of PHP SDK you can always find in our public repository:

<https://github.com/flittpayments/php-sdk>

SDK documentation:

<https://flittpayments.github.io/php-docs/>

**Composer installation**

```
composer require flittpayments/php-sdk

```

**Manual installation**

```
git clone -b master https://github.com/flittpayments/php-sdk.git

```

**Simple Start**

```
require 'vendor/autoload.php';
\Flitt\Configuration::setMerchantId(1549901);
\Flitt\Configuration::setSecretKey('test');

$checkoutData = [
    'currency' => 'GEL',
    'amount' => 1000
];
$data = \Flitt\Checkout::url($checkoutData);
$url = $data->getUrl();
//$data->toCheckout() - redirect to checkout

```

**Example**

```
cd ~/php-sdk
php -S localhost:8000

```

[Checkout example](https://github.com/flittpayments/php-sdk/tree/master/examples)

# Python SDK

Python SDK allows you to accept payment with Visa/MasterCard cards on your website.

Lates version of Python SDK you can always find in our public repository:

<https://github.com/flittpayments/python>

**Installation**

```
pip install flittpayments

```

**Simple start**

```
from flittpayments import Api, Checkout
api = Api(merchant_id=1549901,
          secret_key='test')
checkout = Checkout(api=api)
data = {
    "currency": "USD",
    "amount": 10000
}
url = checkout.url(data).get('checkout_url')

```

# Create an embedded Apple Pay and Google Pay buttons with JavaScript SDK

Project at GitHub: <https://github.com/flittpayments/js-sdk>

You can place Apple Pay and Google Pay buttons on your website as a regular HTML + JS code.

We developed pre-designed example (HTML/JavaScript) which you can try to use on your site:

## Basic example with both Apple Pay and Google Pay

See the Pen [ApplePay Payment Buttons](https://codepen.io/flitt/pen/dPGVGbj) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

Instead of

```
<script src='https://cdn.jsdelivr.net/npm/@flittpayments/js-sdk/dist/umd/checkout.js'></script>
<div class='payment-button-container'></div>

```

you can use

```
npm i @flittpayments/js-sdk
import $checkout from "@flittpayments/js-sdk";

```

# Step by step implementation case

**Step 1**

Create endpoint on your backend which will be called by your frontend application to obtain payment token.

Endpoint should be integrated as described in instructions at [Merchant embedded checkout page with payment token](https://docs.flitt.com/api/create-order/#merchant-embedded-checkout-page-with-payment-token)

This is mean, that backend will send [parameters](https://docs.flitt.com/api/order-parameters/#__tabbed_1_1) with POST method to <https://pay.flitt.com/api/checkout/token> endpoint and obtain token in response.

```
{
    "response": {
        "token": "07288bca0faaf2dc1870153d31bb7fc0c9f4cc4e",
        "response_status": "success"
    }
}

```

**Step 2**

Obtain payment token from your backend.

**Step 3**

Place your `merchant_id` and `token` values into block:

```
data: {
  merchant_id: 1549901,
  token: "<token obtained from backend>"
}

```

If you need only Apple Pay, set in [JS code](http://localhost:8000/sdk-and-mobile/sdk/wallets/#basic-example-with-both-apple-pay-and-google-pay) parameter

`methods: ["apple"],`

If you need only Google Pay, set in [JS code](http://localhost:8000/sdk-and-mobile/sdk/wallets/#basic-example-with-both-apple-pay-and-google-pay) parameter

`methods: ["google"],`

**Step 4**

Process callback on frontend with `model` object:

```
  .on("success", function (model) {
    console.log(model);
  })
  .on("error", function (model) {
    console.log(model);
  });

```

**Step 5**

Process callback on your backend (see [parameter](https://docs.flitt.com/api/order-parameters/#__tabbed_1_1) `server_callback_url`).

Check `orders_status` and `signature` to validate the result.

**Step 6 for (Apple Pay only)**

**Verify your domain in Apple Pay developer account**

- To embedd Apple Pay button from Flitt, you must register all of your web domains where button will be displayed. This relates to top-level domains (for example, site.com) and subdomains (for example, shop.site.com, www.site.com), both production and development sites.
- Request Flitt support for `apple-developer-merchantid-domain-association.txt` file.
- When received, place that file at https://example.com/.well-known/apple-developer-merchantid-domain-association where `example.com` is your domain or subdomain.
- Tell Flitt to activate your domain with Apple.
# Getting started

**Direct** integration type allows to accept payments with card data collected on your site and passed to Flitt API.

Direct integration will require from merchant the PCIDSS [SAQ D](/pcidss-compliance/#saq-d-requested-by-flitt) compliance.

How it works:

- A merchant website or mobile application creates the payment form with card number, cvv2 and expiry date fields and collects card data
- A merchant website or mobile application sends card data to merchant backend API
- Merchant backend stores and transits or only transmits without storage the card data to Flitt API (step 1)
- If card is enrolled in 3D-Secure, Flitt API returns to the merchant URL and the data which need to be submitted for 3DS-Secure cardholder authentication
- Merchant backend transmit 3D-Secure data to its website or mobile application with instruction to redirect customer to his bank's 3D-Secure authentication page
- Merchant backend application receives 3D-Secure authentication result and transmits it to Flitt API (step 2)
- Merchant backend receives callback with payment final result

Refer to API description on how to procceed with direct integration:

- [Parameters](/api/order-parameters-direct/) required to be passed to Flitt API endpoint
- Endpoints to [create order](/api/create-order-direct/) and proceed with 3D-Secure authentication

You can use the **Embedded** integration type if you do not want the customer to leave your site during the checkout process and prefer to have a seamless process without redirections. Embedded is a good option if you want the customer to provide payment details on your site and do not process and do not store sensitive payment data.

Embedded

See the Pen [Flitt - custom checkout. Compact region](https://codepen.io/flitt/pen/BaggpVw) by Flitt.com ([@flitt](https://codepen.io/flitt)) on [CodePen](https://codepen.io).

Embedded integration type usually requires skills of frontend developer to integrate source of Javascript + HTML + CSS code in your site. But, if you do not have the ability to develop the code, and your system allows easily to embed JavaScript code, you can use [Embedded Custom checkout](/api/embedded-custom/) prebuild JavaScript + HTML + CSS fragment and insert it into your site.

The main difference between Embedded and Redirect is that customer will see only your site pages with the payment form seamlessly embedded in your site. Instead of been redirected to `https://pay.flitt.com` during Redirect type integration, checkout payment form will be loaded in iframe, natively integrated in your site. Embedded checkout page can be customized with your brand logo and colors in order your customers experienced a frictionless flow and were not distracted from the checkout process.

If you do not want to involve developer to integrate payments in your site or your CMS/CRM/Landing builder/Blog platform does not allow embedded JavaScript code, look at [Redirect](/getting-started/redirect/)

We prepared a set of [Design presets](/getting-started/presets/) for your Embedded checkout page in order you could make a quick decision with a good combination of payment page design which will interflow with your site native design.

For frontend developer to implement Embedded integration please see API reference [Embedded/Custom checkout](/api/embedded-custom/) section. Also, we implemented the Embedded checkout version in our [CRM&CMS plugins](/no-code/cms-plugins) which we have developed.

#### For developers

Embedded checkout allows customising the design of checkout page with JavaScript code. With JavaScript, you can:

- Enable or disable payment methods, change order and priority to display to a customer
- Change design drastically or just change theme or amend some components style
- Enable and configure subscription payments
- Set payment attributes, such as order parameters, language, default payment methods countries
- Add additional fields to the checkout page
- Enable Apple Pay and Google Pay
- Handle JavaScript callbacks and events

See full description of possibilities in [Embedded/Custom checkout](/api/embedded-custom/) section.

# Get started with Flitt

### Step 1. Obtain test data

Refer to [Testing](/api/testing/) page to obtain test merchant, payment secret key and card data.

### Step 2. Create test order

Refer to [Create order](/api/create-order/) page to create test order with a simple code.

For example:

```
curl -i -X POST \
-H "Content-Type:application/json" \
-d \
'{
"request": {
"server_callback_url": "http://myshop/callback/",
"order_id": "TestOrder2",
"currency": "GEL",
"merchant_id": 1549901,
"order_desc": "Test payment",
"amount": 1000,
"signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
}
}' \
'https://pay.flitt.com/api/checkout/url'

```

### Step 3. Choose your integration type

Some more code examples

```
$ curl -L 'https://pay.flitt.com/api/checkout/url' \
-H 'Content-Type: application/json' \
-d '{
  "request": {
    "version": "1.0.1",
    "order_id": "test_order_id_132412412",
    "currency": "GEL",
    "merchant_id": 1549901,
    "order_desc": "Test order",
    "amount": 10025,
    "response_url": "https://example.com/thankyoupage",
    "server_callback_url": "https://example.com/api/callback",
    "signature": "7f52380cefaf3cb793746e2deeb56cf7cd75d532"
  }
}'

```

response:

```
{
  "response": {
    "checkout_url": "https://pay.flitt.com/merchants/5ad6b888f4becb0c33d543d54e57d86c/default/index.html?token=03fb1c589f8fcabc80f609c70af541fc636df112",
    "payment_id": "805230052",
    "response_status": "success"
  }
}

```

**Composer installation**

```
composer require cloudipsp/php-sdk-v2

```

**Manual installation**

```
git clone -b master https://github.com/flittpayments/php-sdk.git

```

**Simple Start**

```
require 'vendor/autoload.php';
\Cloudipsp\Configuration::setMerchantId(1549901);
\Cloudipsp\Configuration::setSecretKey('test');

$checkoutData = [
    'currency' => 'GEL',
    'amount' => 1000
];
$data = \Cloudipsp\Checkout::url($checkoutData);
$url = $data->getUrl();
$data->toCheckout();

```

**Simple Start** Include checkout.js file

```
<script src="https://pay.flitt.com/latest/checkout-vue/checkout.js"></script>

```

Add CSS:

```
<style>body {margin: 0;}</style>
<link rel="preload" href="https://pay.flitt.com/icons/dist/fonts/inter-regular.woff2" as="font" type="font/woff2" crossorigin="anonymous">
<link rel="preload" href="https://pay.flitt.com/icons/dist/fonts/inter-medium.woff2" as="font" type="font/woff2" crossorigin="anonymous">
<link rel="preload" href="https://pay.flitt.com/icons/dist/fonts/inter-semibold.woff2" as="font" type="font/woff2" crossorigin="anonymous">
<link rel="preload" href="https://pay.flitt.com/icons/dist/fonts/cvv.woff" as="font" type="font/woff" crossorigin="anonymous">
<link rel="preload" href="https://pay.flitt.com/icons/dist/fonts/card-number.woff" as="font" type="font/woff" crossorigin="anonymous">
<link rel="preload" href="https://pay.flitt.com/latest/checkout-vue/checkout.css" as="style">
<link href="https://pay.flitt.com/latest/checkout-vue/checkout.css" rel="stylesheet">

```

HTML congtainer:

```
<div id="checkout-container"></div>

```

JavaScript code:

```
var Options = {
  options: {
    methods: ["card"],
    methods_disabled: [],
    full_screen: false,
    title: "Example title.",
    active_tab: 'card',
    theme: {
      type: "light",
      preset: "black"
    },
  },
  params: {
    merchant_id: 1549901,
    currency: "GEL",
    order_id: new Date().getTime(),
    amount: 5000,
    order_desc: "Test payment"
  }
};
checkout("#checkout-container", Options);

```

**1.Installation**

**Node** If youâre using [Npm](https://npmjs.com/) in your project, you can add @flittpayments/js-sdk dependency to package.json with following command:

```
npm i --save @flittpayments/js-sdk

```

or add dependency manually:

```
{
  "dependency": {
    "@flittpayments/js-sdk":"^2.0"
  }
}

```

**Manual installation** If you do not use NodeJS, you can download the latest release. Or clone from GitHub the latest developer version

```
git clone git@github.com:flittpayments/js-sdk.git

```

**Quick start**

```
<script src="https://cdn.jsdelivr.net/npm/@flittpayments/js-sdk"></script>

```

**2. Develop html card form using your own design.**

**Basic template**

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  </head>
  <body>
    <script src="https://cdn.jsdelivr.net/npm/@flittpayments/js-sdk"></script>
    <script>
    $checkout('Api').scope(function(){
        this.request('api.checkout.form','request', { Parameters } ).done(function(model){
            model.sendResponse();
            console.log(model.attr('order'));
        }).fail(function(model){
            console.log(model.attr('error'));
        });
    });
    </script>
  </body>
</html>

```

Basic template example: <https://github.com/flittpayments/js-sdk#basic-template>

**3. Create order using Integration Schema C for JavaScript SDK.**

Add parameters `required_rectoken=Y` and `server_callback_url` in your request to obtain recurring token (if you are planning recurring payments) in server callback (`rectoken` parameter).

```
curl -i -X POST \
-H "Content-Type:application/json" \
-d \
'{
"request": {
"server_callback_url": "http://myshop/callback/",
"order_id": "TestOrder2",
"currency": "GEL",
"merchant_id": 1549901,
"order_desc": "Test payment",
"amount": 1000,
"signature": "91ea7da493a8367410fe3d7f877fb5e0ed666490"
}
}' \
'https://pay.flitt.com/api/checkout/token'

```

Documentation: https://docs.flitt.com/docs/page/3/?la=en#chapter-3-6-c. Save host-to-host token parameter from response.

**4. Load host-to-host token from step 3 in your card details form.**

```
{
 "payment_system":"card",
 "token":"host-to-host generated token",
 "card_number":"16/19-digits number",
 "expiry_date":"Supported formats: MM/YY, MM/YYYY, MMYY, MMYYYY",
 "cvv2":"3-digits number"
 }

```

from card form to payment gateway using JavaScript API $checkout('Api'). Instruction: https://github.com/flittpayments/js-sdk#host-to-host-token

**5. Use .on('success') and .on('error') JavaScript callbacks to get result on payment processing.**

success â order is approved and amount will be charged error â order is declined and amount will not be charged

model.attr('error.message') will contain localized error message in case of payment decline. Order information on order status and details will be returned in model.data.order.order_data

JavaScript callback example:

```
console.log('success',JSON.stringify(model.attr("order").order_data));

```

```
{
  "response": {
    "rrn": "111111111111",
    "masked_card": "444455XXXXXX1111",
    "sender_cell_phone": "",
    "sender_account": "",
    "currency": "GEL",
    "fee": "",
    "reversal_amount": "0",
    "settlement_amount": "0",
    "actual_amount": "200",
    "response_description": "",
    "sender_email": "test@test.com",
    "order_status": "approved",
    "response_status": "success",
    "order_time": "13.07.2024 01:23:59",
    "actual_currency": "GEL",
    "order_id": "test33694502191",
    "tran_type": "purchase",
    "eci": "5",
    "settlement_date": "",
    "payment_system": "card",
    "approval_code": "123456",
    "merchant_id": 1549901,
    "settlement_currency": "",
    "payment_id": 805243692,
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "200",
    "signature": "b7884b5c4906956fbac4d20390388d913a78c0b0",
    "product_id": "",
    "merchant_data": "Test merchant data",
    "rectoken": "",
    "rectoken_lifetime": "",
    "verification_status": "",
    "parent_order_id": "",
    "fee_oplata": "0",
    "additional_info": "{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_test\": true}",
    "response_signature_string": "**********|200|GEL|{\"capture_status\": null, \"capture_amount\": null, \"reservation_data\": \"{}\", \"transaction_id\": 1994930931, \"bank_response_code\": null, \"bank_response_description\": null, \"client_fee\": 0.0, \"settlement_fee\": 0.0, \"bank_name\": null, \"bank_country\": null, \"card_type\": \"VISA\", \"card_product\": \"empty_visa\", \"card_category\": null, \"timeend\": \"13.07.2024 01:24:08\", \"ipaddress_v4\": \"178.54.60.26\", \"payment_method\": \"card\", \"version_3ds\": 1, \"is_**********\": true}|200|123456|444455|VISA|GEL|5|0|444455XXXXXX1111|Test merchant data|1549901|**********33694502191|approved|13.07.2024 01:23:59|805243692|card|success|0|111111111111|**********@**********.com|0|purchase"
  }
}

```

Example: <https://jsfiddle.net/flitt/on8ydsgq/1/>

**6. Process final response received as server callbacks to `server_callback_url`.**

Format of final response: [Response](/api/order-parameters/#__tabbed_1_2)

**Installation** SDK availble on [NuGet](https://www.nuget.org/packages/FlittSDK/)

**Simple start**

```
using FlittSDK;
using FlittSDK.Checkout;

Config.MerchantId = 1549901;
Config.SecretKey = "test";

var req = new CheckoutRequest {
  order_id = Guid.NewGuid().ToString("N"),
  amount = 100000,
  order_desc = "checkout json demo",
  currency = "GEL"
};
var resp = new Url().Post(req);
if (resp.Error == null) {
 string url = resp.checkout_url;
}

```

**Installation**

```
npm install @flittpayments/flitt-node-js-sdk

```

**Manual installation**

```
git clone -b master https://github.com/flittpayments/node-js-sdk.git

```

**Simple start**

```
const FlittPay = require('@flittpayments/flitt-node-js-sdk')

const flitt = new FlittPay(
  {
    merchantId: 1549901,
    secretKey: 'test'
  }
)
const requestData = {
  order_id: 'Your Order Id',
  order_desc: 'test order',
  currency: 'GEL',
  amount: '1000'
}
flitt.Checkout(requestData).then(data => {
  console.log(data)
}).catch((error) => {
  console.log(error)
})

```

**Installation**

```
pip install flittpayments

```

**Simple start**

```
from flittpayments import Api, Checkout
api = Api(merchant_id=1549901,
          secret_key='test')
checkout = Checkout(api=api)
data = {
    "currency": "GEL",
    "amount": 10000
}
url = checkout.url(data).get('checkout_url')

```


We prepared a preset of colors and themes for your checkout page in order you could make a quick decision with a good combination of payment page design.

You will be able to make themes configuration manually in your [Merchant Portal](https://portal.flitt.com/mportal/#/) account where you do not need to involve a developer or designer. In your Merchant Portal account, you can set light or dark theme with the prefered color set and configure which payment method will be displayed on the Redirect checkout page in which order.

Payment with saved card is also called **recurring payment**

Recurring payment is executed in 2 steps

## Step 1: save card and obtain card token

Before executing recurring payments, `rectoken` must be received. `rectoken` is a token which references card data, securely stored on the payment gateway side.

To obtain `rectoken`, the parameter `required_rectoken=Y` must be sent during [create order](/api/create-order/) request. There are two options to obtain token:

**Option 1. During card verification.**

Send parameter `verification=Y` among with `required_rectoken=Y` during [create order](/api/create-order/) request with small amount value (for example amount = 100). In this case, amount value will be held on the card, and will be reversed. `rectoken` will be returned in response to `response_url` and in server callback response to `server_callback_url`

**Option 2. During the first purchase.** During [create order](/api/create-order/) request send amount value of the actual purchase value. In this case, amount value will be charged from the card, and `rectoken` will be returned in response to `response_url` and in server callback response to `server_callback_url`.

## Step 2: execute recurring payment without customer participation

[Create payment with saved card](/api/create-order-recurring/) passing recurring token in `rectoken` parameter

You can use the **Redirect** integration type if you are fine with redirecting customer from your site to payment page hosted on Flitt side. Redirect is a good option if you want the customer to see all payment methods on a single page.

If you do not want the customer to leave your site during the checkout process and prefer to have a seamless process without redirections, look at [Embedded](/getting-started/embedded/) or [Direct](/getting-started/direct/) integration type.

The main difference between Redirect and Embedded/Direct is that customers will see `https://pay.flitt.com` page with the payment form instead of your site domain name.

Redirect checkout page can be customized with [Design presets](/getting-started/presets/) which can be combined with your brand logo and colors. This will improve the user experience of your customers during online payments and will not distract them from the checkout process.

## For developers

To implement Redirect integration type please see API reference [create order](/api/create-order/) section.

We prepared code examples and [SDK](/sdk-and-mobile/sdk/about-sdk/) for different programming languages to make integration for you more simple.

- [JavaScript](/sdk-and-mobile/sdk/js)
- [PHP](/sdk-and-mobile/sdk/php)
- [Python](/sdk-and-mobile/sdk/python)
- [C#](/sdk-and-mobile/sdk/csharp)
- [Node.js](/sdk-and-mobile/sdk/nodejs)

Example

```
<script type="text/x-vue-template" id="f-fields">
  <div>
    <input-amount name="amount" label="my_amount"></input-amount>
    <input-text
      name="order_desc"
      value="order_desc"
      label="Product Description"
      description="description"
      custom
    ></input-text>
  </div>
</script>

<script>
  checkout('#app', {
    options: {
      fields: true,
    },
    params: {
      currency: 'GEL',
      merchant_id: 1549901,
      amount: 100,
      response_url: 'http://example.com/result/',
      api_domain: 'pay.flitt.com',
    },
  })
</script>

```

```
require 'vendor/autoload.php';
\Cloudipsp\Configuration::setMerchantId(1549901);
\Cloudipsp\Configuration::setSecretKey('test');

$checkoutData = [
    'currency' => 'GEL',
    'amount' => 1000
];
$data = \Cloudipsp\Checkout::url($data);
$url = $data->getUrl();
//$data->toCheckout() - redirect to checkout

```

```
from cloudipsp import Api, Checkout
api = Api(merchant_id=1549901,
          secret_key='test')
checkout = Checkout(api=api)
data = {
    "currency": "GEL",
    "amount": 10000
}
url = checkout.url(data).get('checkout_url')

```

```
using CloudIpspSDK;
using CloudIpspSDK.Checkout;

Config.MerchantId = 1549901;
Config.SecretKey = "test";

var req = new CheckoutRequest {
  order_id = Guid.NewGuid().ToString("N"),
  amount = 100000,
  order_desc = "checkout json demo",
  currency = "GEL"
};
var resp = new Url().Post(req);
if (resp.Error == null) {
 string url = resp.checkout_url;
}

```

```
const CloudIpsp = require('cloudipsp-node-js-sdk')

const checkout = new CloudIpsp(
  {
    merchantId: 1549901,
    secretKey: 'test'
  }
)
const requestData = {
  order_id: 'Your Order Id',
  order_desc: 'test order',
  currency: 'GEL',
  amount: '1000'
}
checkout.Checkout(requestData).then(data => {
  console.log(data)
}).catch((error) => {
  console.log(error)
})

```

Also, you can use Redirect with any [CMS&CRM](/no-code/cms-plugins) system which we support.
# CMS plugins

## CMS plugins

- [WHMCS](https://github.com/flittpayments/WHMCS)
- [Restrict Content Pro](https://github.com/flittpayments/wordpress/tree/main/Restrict_Content_Pro)
- [Easy Digital Downloads](https://github.com/flittpayments/wordpress/tree/main/easy-digital-downloads-fondy)
- [WordPress Pay Memberships Pro](https://github.com/flittpayments/wordpress/tree/main/Paid_Membership_Pro)
- [WordPress WooCommerce](https://github.com/flittpayments/wordpress/tree/main/woocommerce)
- [WordPress gravityforms](https://github.com/flittpayments/wordpress/tree/main/fondy-gravityforms-payment)

## Integration with e-commerce platforms

- [Shopify](https://apps.shopify.com/flitt-payments)
- [Tilda](/no-code/cms/tilda)

How to setup Tilda for Flitt

## Step 1. Ensure your plan is at least **Tilda Personal**

## Step 2. Go to site settings

## Step 3. Select menu Payment Systems

## Step 4. Select Custom Payment Gateway

## Step 5. Select template Fondy

## Step 6. Setup your Flitt merchant ID, payment key from your [Merchant Portal](https://portal.flitt.com) account

## Step 7. Change title to: Flitt - Cards, Apple/Google Pay

## Step 7. Press **Add** button. Your payments are ready. Test it in your store.
# Other pages

# Flitt Bug Bounty

## General Requirements

We assess the criticality of security issues with [Common Vulnerability Scoring System v4](https://www.first.org/cvss/calculator/4.0):

| Severity level | CVSS score |
| -------------- | ---------- |
| None           | 0.0        |
| Low            | 0.1 â 3.9  |
| Medium         | 4.0 â 6.9  |
| High           | 7.0 â 8.9  |
| Critical       | 9.0 â 10.0 |

As usual practice for rewards programs, we ask you to use common sense when looking for security bugs.

Expect us to eliminate the vulnerability within a reasonable time.

Avoid compromising data of other users and accounts, try to use only your personal or dummy data to search for vulnerabilities.

When reporting potential vulnerabilities, please consider realistic attack scenarios and the security impact of the behavior. The following issues will be rejected, except in rare circumstances demonstrating clear security impact.

1. Theoretical vulnerabilities that require unlikely user interaction or circumstances. For example:
   - Vulnerabilities only affecting users of unsupported or end-of-life browsers or operating systems
   - Broken link hijacking
   - Tabnabbing
   - Content spoofing and text injection issues
   - Self-exploitation, such as self-XSS or self-DoS (unless it can be used to attack a different account)
1. Theoretical vulnerabilities that do not demonstrate real-world security impact. For example:
   - Clickjacking on pages with no sensitive actions
   - Cross-Site Request Forgery (CSRF) on forms with no sensitive actions (e.g., Logout)
   - Permissive CORS configurations without demonstrated security impact
   - Software version disclosure / Banner identification issues / Descriptive error messages or headers (e.g., stack traces, application or server errors)
   - Open redirects (unless you can demonstrate additional security impact)
   - Wordpress user disclosure using REST API
1. Optional security hardening steps / Missing best practices. For example:
   - SSL/TLS Configurations
   - Lack of SSL Pinning
   - Cookie handling (e.g., missing HttpOnly/Secure flags)
   - Content-Security-Policy configuration opinions
   - Optional email security features (e.g., SPF/DKIM/DMARC configurations)
   - Most issues related to rate limiting
1. Vulnerabilities that may require hazardous testing. This type of testing must never be attempted unless explicitly authorized:
   - Issues relating to excessive traffic/requests (e.g., DoS, DDoS)
   - Any other issues where testing may affect the availability of systems
   - Social engineering attacks (e.g., phishing, opening support requests)
   - Attacks that are noisy to users or admins (e.g., spamming notifications or forms)

## Testing Requirements

The list of domains that are participating in the reward program:

```
    *.flitt.com
    *.flitt.dev

```

As with most security reward programs, there are some limitations:

- we reward only the first person who informed us about the problem
- publicly disclosed problems for which sufficient time has not waited for elimination are not rewarded
- your safety research must not violate the law

Note

Flitt reserves the right to revise the amount of reward depending on the particular case or the circumstances.

## Notifications

If you think you have found a bug in Flitt security, contact us at email `YnVnYm91bnR5QGZsaXR0LmNvbQ==` and attach a detailed report on the problem found.

We will respond as quickly as possible to your message.

We ask you not to disclose the problem until it is fixed by Flitt specialists.

# PCIDSS compliance

## PCIDSS RoC (Report on Compliance)

A Report on Compliance (ROC) tests the standards that are in place to protect the credit card information stored. ROC & Quarterly External ASV Scans are required for all Level 1 Merchants. A Level 1 Merchant is a retailer that has more than 6 million annual transactions with Visa and/or Mastercard.

A Report on Compliance is a report documenting detailed results from a PCI DSS assessment. A ROC must be completed by a Qualified Security Assessor (QSA) after an audit, and subsequently submitted to the merchantâs acquirer. The acquirer, after accepting the ROC, sends it to the payment brand for verification.

## PCIDSS SAQ A, A-EP, D compliance

There are three Self-Assessment Questionnaire (SAQ) types within the new PCI DSS 4.0 standard available for e-commerce websites. They are titled A, A-EP (electronic processing), and D.

| Merchant level | No of transactions annually | Redirect | Iframe/Embedded | Direct POST | JavaScript | XML/JSON | Other |
| -------------- | --------------------------- | -------- | --------------- | ----------- | ---------- | -------- | ----- |
| 1              | Over 6 million              | RoCA     | RoCA            | RoCA-EP     | RoCA-EP    | RoC      | RoC   |
| 2              | 1 â 6 million               | SAQ A    | SAQ A           | SAQ A-EP    | SAQ A-EP   | SAQ D    | SAQ D |
| 3              | 20 000 â 1 million          | SAQ A    | SAQ A           | SAQ A-EP    | SAQ A-EP   | SAQ D    | SAQ D |
| 4              | Under 20 000                | SAQ A    | SAQ A           | SAQ A-EP    | SAQ A-EP   | SAQ D    | SAQ D |

RoCA â Partial Report on Compliance validating the scope, eligibility, and requirements listed in SAQ A

RoCA-EP â Partial Report on Compliance validating the scope, eligibility, and requirements listed in SAQ A-EP

To identify which type is required, the merchant should analyze several factors.

### SAQ A (not requested by Flitt)

If your website uses an iFrame or Hosted Page implementation, you will be responsible for complying with SAQ A. In this case, the user is taken to a payment page that is hosted by the service provider. This can be done by introducing a redirect, where the user is taken to another page (i.e., hosted page), or can happen on the same page in the form of an iFrame.

Please refer to description of

- [hosted page (redirect)](/getting-started/redirect/)
- [iFrame (embedded)](/getting-started/embedded/)
- [Interaction scheme A (with customer redirection to the payment page)](/api/payment-flow/#interaction-scheme-a-with-customer-redirection-to-payment-page)
- [Interaction scheme B (with host-to-host request to obtain payment page URL)](/api/payment-flow/#interaction-scheme-b-with-preliminary-host-to-host-request-to-get-payment-page-url)

### SAQ A-EP (not requested by Flitt)

If merchant web site is hosting credit card form, it is required to comply with SAQ A-EP.

This SAQ is applied if merchant uses a [JavaScript](/getting-started/direct/) card form implementation.

In either case, you are capturing the information via your own form, using actions and methods to push to an API.

A solution like client-side encryption or tokenization can help merchants to comply with SAQ A-EP.

Note

Neither SAQ A nor SAQ A-EP allows a merchant to store or transmit credit card data through own servers and network. All processing of cardholder data is outsourced to Flitt as a PCI DSS validated third-party payment processor.

### SAQ D (requested by Flitt)

These are e-commerce firms that do not meet any of the criteria above. Service providers and merchants who do not meet the criteria for any of the above questionnaires.

SAQ D for Merchants applies to SAQ-eligible merchants not meeting the criteria for any other SAQ type. Examples of merchant environments that would use SAQ D may include but are not limited to:

- E-commerce merchants who accept cardholder data on their website.
- Merchants with electronic storage of cardholder data
- Merchants that donât store cardholder data electronically but that do not meet the criteria of another SAQ type
- Merchants with environments that might meet the criteria of another SAQ type, but that have additional PCI DSS requirements applicable to their environment

### Recommendations for Flitt merchants

With SAQ A, D and A-EP you can use any Flitt integrations except [Direct](/getting-started/direct/) method:

- [Hosted Payment Page](/getting-started/redirect/)
- Payment buttons
- Payment links
- [Embedded](/getting-started/embedded/) checkout page
- [JavaScript SDK](/sdk-and-mobile/sdk/js/)
- [Apple Pay](/api/applepay-web/)
- [Google Pay](/api/googlepay-web/)

Direct method requires card data storage on merchant own server. In this case, PCI DSS RoC is mandatory:

Level 1: Merchants processing over 6 million card transactions per year. Level 2: Merchants processing 1 to 6 million transactions per year. Level 3: Merchants handling 20,000 to 1 million transactions per year. Level 4: Merchants handling fewer than 20,000 transactions per year.

If you need to host credit card form on your site, but you do not have RoC, you can use [Embedded](/api/embedded-custom/) or [JavaScript SDK](/sdk-and-mobile/sdk/js/) checkout page.

# Supported Countries

## 1. The countries in which we serve the partners

- Georgia
- Uzbekistan
- Moldova
- Armenia
- Kazakhstan

## 2. Countries from which customers can pay to merchants

All countries where Visa and MasterCard cards are issued, about 210 countries of the world.

# Supported payment systems

| Payment system code | Description                         |
| ------------------- | ----------------------------------- |
| `card`              | Visa/MasterCard/Maestro/Humo/Uzcard |

Large language models (LLMs) can help you to develop Flitt integrations.

**Documentation in plain text format**

Flitt documentation is available as plain text markdown files by adding `/index.md` to the end of any url.

For example, the plain text version of this page can be accessed at [https://docs.flitt.com/llms.md](/llms/index.md).

Plain text `.md` documentation format can be useful in such cases:

- Optimal tokens for LLM to process.
- All the content is rendered in the plain text file including sub menus and tabs which can be not visible in HTML version.
- LLMs can easily parse and understand markdown structure.
- File `/llms.txt` hosted at [https://docs.flitt.com/llms.txt](/llms.txt) can instruct AI tools and agents how to retrieve the plain text versions of our pages.
- The `/llms.txt` file is an emerging convention designed to help websites communicate rules and guidelines for Large Language Models (LLMs), similar to how `robots.txt` guides web crawlers.
