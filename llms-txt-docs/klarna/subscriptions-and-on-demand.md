# Source: https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/use-cases/subscriptions-and-on-demand.md

# Subscriptions and on-demand

## How to combine login and tokenized payments

## Introduction

Sign in with Klarna goes beyond the typical social login functionality of signing in or signing up. It's designed to enhance user experiences across various touchpoints, particularly in shopping, but its versatility makes it ideal for a wide range of applications. Whether you're creating seamless onboarding paths for on-demand mobility services, food delivery apps, or subscription-based platforms, Sign in with Klarna offers a tailored solution. As businesses increasingly adopt tokenized payments to enhance security and streamline user experiences, we've developed a flow that seamlessly integrates account creation and payment setup. With Sign in with Klarna, consumers can sign up and set up payments in a single, effortless step—without any redirects or additional work on your end, apart from enabling this best-in-class flow.

## Tokenized payment use cases

- Subscriptions: allows customers to sign up for a subscription using Klarna as their payment method. Once complete, the payment preferences are tokenized and automatically used for renewals by the merchant using the token to create orders. Shoppers can manage their preferences at any time in the Klarna App.
- On-demand: allows customers to add Klarna as a payment method in a digital wallet for one-click purchases of on-demand services. Shoppers can update their payment preferences at any time in the Klarna App.

Both use cases are facilitated by the "customer token"[\#Representation of payment data tied to a specific customer and merchant.](https://docs-portal-eu.staging.c2c.klarna.net#representation-of-payment-data-tied-to-a-specific-customer-and-merchant). Learn more about customer tokens [here](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/use-cases/subscriptions-and-on-demand/). ![ Example of on-demand flow.](ZsiIjkaF0TcGJW4g_SIWKTokenizedPayments.jpeg " Example of on-demand flow.") The tokenized payment flow is supported in the Klarna Mobile SDK for:

- **iOS:** Version 2.6.23 and later
- **Android:** Version 2.6.21 and later

## How to integrate

### 1. Initialize the SDK and the Identity product and render Sign in with Klarna button.

Make sure to request the correct scope for your use case:

| Use case     | Scope                          |
|--------------|--------------------------------|
| On-demand    | `payment:customer_present`     |
| Subscription | `payment:customer_not_present` |

#### Web SDK

``` javascript
const siwkButton = klarna.Identity.button({
  scope: "profile:name profile:email payment:customer_present",
  redirectUri: "http://localhost:3000/callback",
});
```

Web SDK

#### Mobile SDK

**KlarnaSignInButton** initializer has new argument of tokenizationDelegate to received the **KlarnaSignInTokenizationDelegate** instance. Pass the **KlarnaSignInTokenizationCallback** instance into the **KlarnaSignInButton** constructor. Mobile SDK 

### iOS


``` swift
let signInButton = KlarnaSignInButton(clientId: clientID,
                                  scope: scope,
                                  market: market,
                                  locale: locale,
                                  presentationContext: self,
                                  theme: klarnaTheme,
                                  environment: env,
                                  region: reg,
                                  returnUrl: URL(string: "https://sneakers.com")!,
                                  eventHandler: self,
                                  tokenizationDelegate: self)
```



### Android


``` kotlin
//Create an instance of KlarnaSignInButton and pass the callback
val button = KlarnaSignInButton(... tokenizationCallback =  yourSignInTokenizationCallbackInstance)
```

### 2. Handle the tokenization event

#### Web SDK

Handle the `tokenizationTrigger` event by making a call to the Klarna Payments API through your backend to create a [new payment session.](https://docs.klarna.com/api/payments/#operation/createCreditSession)

``` javascript
siwkButton.on("tokenizationTrigger", async (callback) =&gt; {
  const response = await fetch("https://merchant-backend.com/payment", {
    method: "POST",
  });
  callback(response.session_id)
});
```

Web SDK

#### Mobile SDK

The **KlarnaSignInButton** now has a new protocol called **KlarnaSignInTokenizationDelegate** that needs to be implemented. The delegate implementation must provide the tokenization ID to the completion handler in order to continue the flow. The **KlarnaSignInButton** now has a new callback called **KlarnaSignInTokenizationCallback** that needs to be implemented. The callback implementation must provide the tokenization ID to the completion handler in order to continue the flow. 

### iOS


``` swift
@available(iOS 13.0, *)
extension AnyKlarnaSignInTokenizationDelegateImpl: KlarnaSignInTokenizationDelegate {
    func onTokenization(_ klarnaComponent: KlarnaComponent, completionHandler: @escaping (String) -&gt; Void) {
        let tokenizationId = ... // your implementation to get the tokenizationId here
        completionHandler(tokenizationId)
    }
}
```



### Android


``` kotlin
class YourSignInTokenizationCallback : KlarnaSignInTokenizationCallback {
    override fun onTokenization(klarnaComponent: KlarnaComponent, completionHandler: (String) -&gt; Unit) {
        val tokenizationId = ... // your implementation to get the tokenizationId here
        completionHandler(tokenizationId)
    }
}
```

When creating the payment [session](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/), remember to:

- Add the `intent` as `tokenize` to trigger the tokenization flow.
- Set up the authorization webhook in the `merchant_urls` object.
- Set `order_amount` and `order_lines` amount value to 0.



### On-demand


``` bash
curl --request POST \
  --url https://api.klarna.com/payments/v1/sessions \
  --header 'Authorization: Basic token' \
  --header 'Content-Type: application/json' \
  --data '{
  "purchase_currency": "EUR",
  "order_amount": 0,
  "purchase_country": "DE",
  "order_lines": [
    {
      "unit_price": 0,
      "quantity": 1,
      "total_amount": 0,
      "name": "Adding Klarna as a payment method"
    }
  ],
  "intent": "tokenize",
  "merchant_urls": {
    "authorization": "https://merchant-backend.com/authorization-webhook"
  },
  "attachment": {
    "body": {
    // EMD
    },
    "content_type": "application/vnd.klarna.internal.emd-v2+json"
  }
}'
```



### Subscription


``` bash
curl --request POST \
  --url https://api.klarna.com/payments/v1/sessions \
  --header 'Authorization: Basic token' \
  --header 'Content-Type: application/json' \
  --data '{
  "purchase_currency": "EUR",
  "order_amount": 0,
  "purchase_country": "DE",
  "order_lines": [
    {
      "unit_price": 0,
      "quantity": 1,
      "total_amount": 0,
      "name": "Adding Klarna as a payment method",
      "subscription": {
        "name": "Coffee",
        "interval": "MONTH",
        "interval_count": 12
      }
    }
  ],
  "intent": "buy_and_tokenize",
  "merchant_urls": {
    "authorization": "https://merchant-backend.com/authorization-webhook"
  }
}'
```

When offering on-demand services with Klarna, you must include the customer_tokens [EMD package](https://www.google.com/url?q=https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/extra-merchant-data/&amp;sa=D&amp;source=docs&amp;ust=1724416392286272&amp;usg=AOvVaw2uhLnjEl6jET0pzMfx8d6W), to enable Klarna to perform accurate underwriting and fraud checks when the customer adds Klarna as a payment option for future on-demand payments. After the customer consents to share their data, Klarna will automatically create an HPP session connected to the payment `session_id` provided in the response of the `create_session`.

### 3. Handle signin event

You can read the tokens from the `signin` event response, the `id_token` will contain requested customer data. The [refresh_token](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/additional-resources/other-operations/#refresh-token)`refresh_token` can be used to fetch access token, allowing you to either retrieve customer data or log in customers during the purchase flow at a later time. 

### Web SDK


``` javascript
siwkButton.on("signin", async (signinResponse) =&gt; {
  "user_account_linking": {
    "user_account_linking_refresh_token": string;
    "user_account_linking_id_token": string;
  }
});
```



### Mobile SDK - iOS


``` swift
@available(iOS 13.0, *)
extension SignInViewController: KlarnaEventHandler {
    func klarnaComponent(_ klarnaComponent: KlarnaComponent, dispatchedEvent event: KlarnaProductEvent) {
         if event.action == .klarnaSignInToken {
            // Authorization went through
            let token = event.params["klarnaToken"]
        }
    }
}
```



### Mobile SDK - Android


``` kotlin
val eventHandler = object : KlarnaEventHandler {
   override fun onEvent(klarnaComponent: KlarnaComponent, event: KlarnaProductEvent) {
      when(event.action) {
         KlarnaSignInEvent.SIGN_IN_TOKEN -&gt; {
            // User is authorized. You can read the results      
            // in event.params attribute by casting it to the
            // KlarnaSignInToken model.
            val token =
               event.params[KlarnaSignInEvent.ParamKey.KlarnaSignInToken] 
               as? KlarnaSignInToken
            val accessToken = token?.accessToken
            ...
         }
      }
   }
}
```

### 4. Handle payment request state webhook

You should receive the `authorization_token` in a webhook to the URL that you provided in the create session call. Make sure to generate a `customer_token` using the `authorization_token` following [our documentation](https://docs.klarna.com/api/payments/#operation/purchaseToken). After that, customer_token can be charged.