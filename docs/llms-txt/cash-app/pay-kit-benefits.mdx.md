# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/pay-kit-benefits.mdx

***

## stoplight-id: 6x9bjud27989b

# Pay Kit Overview

Pay Kit is Cash App Pay’s JavaScript SDK that allows you to accept Cash App Pay online (both on the web and mobile).
Here are some of the things that you can do using Pay Kit:

* Rendering Cash App Pay button to an HTML element
* Customize the Cash App Pay button
* Fully managed and branded UI
* Advanced controls to support:
  * Validating a customer’s information
  * Using custom elements in checkout
  * Upselling to the customer

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/easy-name.png" alt="Screenshot 2023-01-12 at 9.42.58 AM.png" />

# Benefits of using Pay Kit

Pay Kit is the recommended integration path for partners integrating with Cash App. This is because Cash App Pay controls the end-to-end experience. These are some of the benefits our partners will experience:

* [Simplified Integration Path](#simplified-integration-path)
* [First-party Support](#first-party-support)

{/* * [Commerce and merchant services](#commerce-and-merchant-services)*/}

## Simplified Integration Path

Pay Kit SDK provides a streamlined integration path for developers by abstracting the Cash App Pay **customer linking** step to a drop-in Javascript library. The following are some of the attributes of a Simplified Integration Path that our partners can benefit from:

* **Supports desktop and mobile UX:** Pay Kit will automatically detect the customer device and facilitate the relevant Cash App Pay customer flow. On desktop devices, a QR code will be displayed to customers that they can scan with their phone to approve the payment. On mobile devices (iOS/Android), the customer will be redirected directly to Cash App to approve the payment.

{/* * **Supports forward and backward navigation:** Pay Kit handles both forward-navigation and backward-navigation scenarios on mobile.*/}

* **QR code rotation:** Pay Kit automatically rotates QR codes every 30 seconds for added security. Your development team does not have to create additional programming for doing this. Thus saving your engineering team's time and effort. <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/easy-name2.png" alt="Screenshot 2023-01-12 at 9.45.49 AM.png" />

* **Cash App brand adherence:** Pay Kit ensures that you adhere to Cash App Pay's brand guidelines and requirements. Any branding and UI updates are automatic and do not need any intervention from your engineering teams.

* **Customer linking state changes:** Pay Kit emits a number of events throughout the lifecycle of a payment. One of the most important ones is `CUSTOMER_REQUEST_APPROVED` which is emitted after a customer approves a payment action such as a one-time payment.

## First-party support

Pay Kit is the recommended integration path for partners integrating with Cash App. Therefore, we can provide first-party support for partners integrated via Pay Kit in case things go wrong. In additon, Pay Kit pushes these upgrades automatically without additional development work required from partners or merchants.

{/*
## Commerce and Merchant Services
Cash App's **In-App Shopping and Incentives** is one of the main reasons that customers must try Cash App Pay beyond the inherent benefits of it being faster and easier to use than other payment methods. From a business perspective, In-App Shopping and Incentives helps us in new customer acquisition or new order acquisition for our merchants. 

Currently, the In-App Shopping and Incentives experience relies on Pay Kit to skip the normal Cash App Pay grant flow; instead, Cash App passes the grant token directly to the merchant website via a silent authentication process. Partners integrating via Pay Kit can expect In-App Shopping and Incentives functionality to work out of the box without additional development work. However, partners not utilizing Pay Kit are not eligible for In-App Shopping and Incentives as there is no available integration path independent from Pay Kit at the moment.

>**Note:** Pay Kit has the functionality to display merchants within Cash App’s **Discover** section.  Currently this feature is limited to merchants using PayKit web.


<img src="../../../../assets/images/Screenshot_20230112-103933 (1).png" style="width:300px;height:600px;" />

*/}
