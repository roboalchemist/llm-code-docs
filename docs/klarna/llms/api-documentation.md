# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/api-documentation.md

# Hosted Payment Page API

This page will take you through the *Hosted Payment Page API* and explain how to interact with it and its concepts. Please make sure to understand why you should use the Hosted Payment Page and the Overview of the system before reading this documentation. The Hosted Payment Page works with a *Payment Provider* from the Klarna ecosystem, and you will need to create a *KP Session* before being able to create an *HPP Session*. A different integration guide is available for both platforms.

- Read HPP with **Klarna Payments** integration guide

In this document, the term *Payment Provider* refers to *Klarna Payments* and *Payment Session* refers to the corresponding *KP Session.*

## Ecosystem overview: components and objects

**Klarna’s Hosted Payment Page** (*HPP*) requires that you integrate different server-side REST APIs from the Klarna environment and thus requires no client-side integration. The different APIs correspond to different Klarna products and have some defined objects that interact with each other.


![ Klarna Ecosystem](18970044-119b-4dc9-af79-fb1b9755d94c_HPP_components.jpeg)
*Klarna Ecosystem*

### 1. Payment Provider API

The *Hosted Payment Page* supports **Klarna Payments**, which will be referred to in this documentation as the *Payment Provider*. a. **Klarna Payments REST API**: create Payment Session, place Order

- **KP Session**: a *Payment Session* on *Klarna Payments API*. It contains everything regarding the transaction and has a 48 hours lifetime. A *KP Session* is considered as *incomplete* until a *KP Authorization Token* has been used to create an *OM Order*.
- **KP Authorization Token**: an authorization for the payment of a *KP Session* to the corresponding Consumer. The token is valid for 60 minutes and has to be used by your backend to create the corresponding *OM Order*. An authorization can be given multiple times to the same Consumer for the same *KP Session*, but only one can be used to create an *OM Order*.

### 2. Hosted Payment Page REST API

The Hosted Payment Page REST API can be used to let Klarna host the client-side integration of Klarna Payments for you. You will have to create a Session and then distribute it.

- **HPP Session**: a session on HPP that is linked to a *Payment Session*. When a *Payment Session* is being completed, canceled or expires, it is also the case for the *HPP Session*. An *HPP Session* has an unique URL where the Consumer can be redirected to and can be *distributed* via different distribution methods.

### 3. Order Management REST API: capture payment

- **OM Order**: a due payment from the Consumer for defined goods. It is created using a *KP Authorization Token* with the *KP Session*. The *OM Order* will allow you to capture the payment when goods or service have been delivered, and manage the post purchase experience of the Consumer.

In the Klarna Payments integration case, when placing the order with the *KP Authorization Token*, you can configure it to automatically capture the payment. In that case you won’t have to integrate the *Order Management API*outside of refunds. This should be limited to digital goods or when you limit it to some payment meth

## HPP Session

### Session Lifecycle


![ HPP Session Lifecycle](d64da141-0bfe-4c09-842b-158cdd13c7ff_HPP_lifecycle.jpeg)
*HPP Session Lifecycle*

### Session Lifetime

*KP Session* and *HPP Session* both have an expiration time, but the expiration is driven by the *Payment Session* which usually expires 48 hours after its creation. A Consumer will be able to pay on HPP until 1 hour before the *Payment Session* expiration.

## Authentication

Klarna uses HTTP’s Basic auth to authenticate requests from Merchants. Use your API Credentials to add the corresponding HTTP headers to your requests, the credentials consist of two elements:

- **Username**: a username linked to your Merchant ID at Klarna
- **Password**: a unique password that is associated with the username

Use your credentials to generate the token: Base64(username:password)

| Username | DemoMerchant |
|----|----|
| Password | DemoPassword |
| Calculated basic auth \|\| RGVtb01lcmNoYW50OkRlbW9QYXNzd29yZA== |  |
| Example of request | curl -X GET <https: api.klarna.com="" payments="" sessions="" v1=""></https:><session_id> --header "Authorization: Basic RGVtb01lcmNoYW50OkRlbW9QYXNzd29yZA==" --header "Content-Type: application/json" |

## Environments and tests

Klarna offers a test environment named Playground and a Production environment. The different APIs are available on each environment. URL structures are the same for both environment, targeted environment will be defined by the domain you are using. To be able to test your integration, you will need a Test Account. You can find more in our \[ environments and testing guidelines\].

## API updates

The HPP API follows the same rules as other Klarna public APIs, we try to update our APIs regularly in a non breaking way, ensuring backward compatibility. You can find more in our [API updates guidelines](https://docs.klarna.com/api/api-urls/#api-updates) and see how we define backward compatibility and non-breaking changes.

## Response codes

- Accept any 2xx codes as success, do not code for a specific error response code
- Interpret any 4xx as an error, do not code for a specific error response code
- Interpret any 5xx as an error, do not code for a specific error response code</session_id>