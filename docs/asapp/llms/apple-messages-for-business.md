# Source: https://docs.asapp.com/agent-desk/integrations/apple-messages-for-business.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Apple Messages for Business

Apple Messages for Business is a service that enables your organization to communicate directly with your customers through your Customer Service Platform (CSP), which in this case will be ASAPP, using the Apple Messages for Business app.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8feefc5-c783-d2ae-5698-5d3058141af9.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=cc031558b3c159ce510dd62dfb43361a" data-og-width="980" width="980" data-og-height="646" height="646" data-path="image/uuid-a8feefc5-c783-d2ae-5698-5d3058141af9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8feefc5-c783-d2ae-5698-5d3058141af9.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=ce4431dd576b3fe1ba818e8db74a1954 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8feefc5-c783-d2ae-5698-5d3058141af9.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=be7e7133436ef1bf62de88e7e4ad41f1 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8feefc5-c783-d2ae-5698-5d3058141af9.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c2a3776a5349079c0c21c77aea281e20 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8feefc5-c783-d2ae-5698-5d3058141af9.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=98e5fb4f9e91dbf2434ac020269b883a 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8feefc5-c783-d2ae-5698-5d3058141af9.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=6f00ed95e1db5bfe90e1e009860ee79b 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8feefc5-c783-d2ae-5698-5d3058141af9.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=802ab88b8d3557ced9211e2499fecef6 2500w" />
</Frame>

<Note>
  All third party specifications are subject to change by Apple. As such, this section may become out-of-date. ASAPP will always attempt to use the most up-to-date third-party documentation. If you come across any errors or out-of-date content, please contact your ASAPP representative.
</Note>

## Quick Start Guide

1. Register for an Apple Messages for Business account
2. Specify Entry Points
3. Complete User Experience Review
4. Determine Launch & Throttling Strategy

### Register for an Apple Messages for Business Account

Before integrating with ASAPP's Apple Messages for Business adapter, you must register an account with Apple. See [Apple Messages for Business Getting Started](https://register.apple.com/resources/messages/messaging-documentation/register-your-acct#getting-started) documentation for more details.

### Specify Entry Points

Entry points are where your customers start conversations with your business. You can select from Apple and ASAPP entry points.

#### Apple Entry Points

Apple supports multiple entry points for customers to engage using the Messages app. See [Apple Messages for Business Entry Points](https://register.apple.com/resources/messages/messaging-documentation/customer-journey#entry-points) documentation for more information.

#### ASAPP Entry Point

ASAPP supports the Chat Instead entry point. See the [Chat Instead](/agent-desk/integrations/chat-instead "Chat Instead") documentation for more information.

### Complete User Experience Review

Apple requires a Brand Experience QA review before you can launch the channel. Please work with your Engagement Manager to prepare and schedule for the QA review. See the [Apple User Experience Review](https://register.apple.com/resources/messages/messaging-documentation/pass-apple-qa) documentation for more information.

### Determine Launch & Throttling Strategy

Depending on the entry points configured, your Engagement Manager will share launch best practices and throttling strategies.

## Customer Authentication

Apple Messages for Business supports Customer Authentication, which allows for a better and personalized customer experience. You can implement Authentication using OAuth.

### OAuth

* Requires OAuth 2.0 implemented by customer
* No support for biometric (fingerprint/Face Id) authentication on device
* Does not require native iOS app

User Authentication in Apple Messages for Business can utilize a standards-based approach using an OAuth 2.0 flow with additional key validation and OAuth token encryption steps.

This approach requires customers to implement and host a login page that Apple Messages for Business will invoke to authenticate the user. Users will have to sign-in with their credentials every time their OAuth token expires.

<Note>
  Additional steps are required to support authorization for users with devices running versions older than iOS 15. Consult your ASAPP account team for more information.
</Note>

#### Latest Authentication Flow

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4981a05a-081b-9180-1ac9-12f640edffd0.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=28e24962e5d908ada739f7404cd8fe40" data-og-width="1230" width="1230" data-og-height="942" height="942" data-path="image/uuid-4981a05a-081b-9180-1ac9-12f640edffd0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4981a05a-081b-9180-1ac9-12f640edffd0.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=42d9b9774b3e32b714e7d3674dce298b 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4981a05a-081b-9180-1ac9-12f640edffd0.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=0203570c564c6921fe1697b844863484 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4981a05a-081b-9180-1ac9-12f640edffd0.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=9a06299d773666b50cf8e4386479fee0 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4981a05a-081b-9180-1ac9-12f640edffd0.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=f0256f9257564a78948e41f9cf16fd00 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4981a05a-081b-9180-1ac9-12f640edffd0.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a0c53dfc18f04c43656458941274dc31 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4981a05a-081b-9180-1ac9-12f640edffd0.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a1321d2266264e393786ca1d6352792b 2500w" />
</Frame>

#### Old Authentication Flow

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a1eb95-8d3b-f80b-e3bb-7c6cd50a8654.jpeg?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=3c15439586977768539b45c9c2ea4494" data-og-width="945" width="945" data-og-height="765" height="765" data-path="image/uuid-b9a1eb95-8d3b-f80b-e3bb-7c6cd50a8654.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a1eb95-8d3b-f80b-e3bb-7c6cd50a8654.jpeg?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c15c8493daa80b18a445a59ce3751be5 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a1eb95-8d3b-f80b-e3bb-7c6cd50a8654.jpeg?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e3b2e0a094a7fd7cf5c786db7877cd66 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a1eb95-8d3b-f80b-e3bb-7c6cd50a8654.jpeg?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=9d9fc0683faf6862bbf992be7cc49985 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a1eb95-8d3b-f80b-e3bb-7c6cd50a8654.jpeg?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c17cd260b9ea06534f5cfece440c62aa 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a1eb95-8d3b-f80b-e3bb-7c6cd50a8654.jpeg?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=59c59d332c5e73864834d3e76db8f3a3 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a1eb95-8d3b-f80b-e3bb-7c6cd50a8654.jpeg?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1036b68352d9c7a125097f89744ece8d 2500w" />
</Frame>

ASAPP requires the following customer functionalities to support the older authentication flow:

* An OAuth 2.0 login flow, including a login page that supports form autofill. This page must be Apple-compliant. See the [Authentication Message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#authentication-message) documentation for more details.
* Provide an API endpoint for ASAPP to obtain an external user identifier. This should be the same identifier that is supplied via the ASAPP web and mobile SDKs as the CustomerId.
* Provide an endpoint through which to obtain an access token by supplying an authcode. This endpoint must support URL encoded parameters.
* Provide an endpoint that can accepted POST requests in the following format:

  ```json  theme={null}
       Content-Type: application/x-www-form-urlencoded
       grant_type=authorization_code&code=xxxx
       &client_id=yyyy&client_secret=zzzz
  where:
  xxxx=authorization_code value
  yyyy=client_id value
  zzzz=client_secret value
  ```

<Note>
  The authorization request from the device to the customer's login page will always contain response\_type, client\_id, redirect\_uri, scope and state and will be application/x-www-form-urlencoded

  Also note that the older authentication flow is backwards-compatible for iOS versions 16+.
</Note>
