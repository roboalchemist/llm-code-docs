# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/sandbox/sandbox-app.mdx

***

## stoplight-id: 0938df2ca110c

# Sandbox App

## Overview

The Sandbox App allows our third-party integrators to verify that their API/SDK code is implemented properly.

We created the Sandbox App so that it mimics the Cash App experience without using our existing flows in our Production environment. This keeps our Production environment safer since we do not expose it to external parties. The Production environment will have the latest version of the Cash App that we distribute to our Partners.

Therefore, the Sandbox App is very useful to Partners because they don't have to download and set up Cash App with a Production (i.e., real bank) account. We provide them an experience that is almost identical to what actual users might see inside of Cash App when they use Cash App Pay for payments.

## Benefits of using Sandbox App for testing

These are the benefits of using the Sandbox App for testing:

* It allows for deep-linked testing during development in Sandbox

* It enables development teams outside the US who don't have access to Cash App via the App Store to test a deep-linked end-to-end journey

* Production testing with the actual Cash App should only be completed as a final step after Partner Certification. The Cash App we deliver to our Partners should ONLY ever be used in the Production environment

* Partners do not have to create a Production account just to test their integration

# Sandbox App: Testing and Usage

Prerequisites to using the Sandbox app are:

* Partners must have the API credentials, and must have integrated with our API via the Pay Kit SDK

* Once they have integrated with Cash App Pay, they can use the Sandbox App to validate their integration

## Download and Install instructions

Contact the Partner Engineering team or your Cash App Point of Contact to set up the API credentials for your integration and to get the download and install instructions for the Sandbox App (both for Android and iOS).

The download links for the Sandbox App (for both Android and iOS) are as follows:

* **iOS link:** [https://testflight.apple.com/join/TZY8IaM9](https://testflight.apple.com/join/TZY8IaM9)

* **Android link:** [https://appdistribution.firebase.dev/i/fd95262a158a32fd](https://appdistribution.firebase.dev/i/fd95262a158a32fd)

# Use Cases

There are currently two Use Cases for the Sandbox App. We recommend that Partners test both these with the Sandbox App. They are:

* **Desktop:** Scan a QR code from the Merchant's website on a desktop by loading a QR code via the Pay Kit SDK

* **Mobile:** Install the Sandbox App in a mobile device. Using the mobile device's browser, navigate to the Merchant's website and click on the **Pay Kit** button. This should deep link them into the Sandbox App. Mobile has the option for both Android and iOS

## Use Case 1: Scan QR code using the in-app scanner

1 On Desktop, navigate to our [Sandbox testing](https://sandbox.pay.withcash.app/checkout) store. Click on the **Cash App Pay** button. This displays the QR code.

![Sandbox test store](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/sandbox-test-store.png)

![Sandbox test store QR code](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/sandbox-test-store-qr-code.png)

2 Open the Sandbox App and tap the **Open Scanner** button.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/sandbox-app-qr-scanner.png" alt="Sandbox app QR scanner" />

3 Scan the QR code on the Desktop using the Sandbox App.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/sandbox-scan-desktop-qr.png" alt="Scan sandbox desktop QR code" />

<Note>You can use the native camera on mobile device to scan the QR code on the Desktop. Tapping on the link from the QR code scan will deep link you to the Sandbox app. There may be slight variations in the deep linking based on the native camera app that you use. For example, you may have to click on a link to go to the Sandbox app.</Note>
4 **Approve** the payment in the Sandbox App.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/approve-payment.png" alt="Approve payment" />

<Note>You can also **Decline** the payment and the Sandbox App will ask you to go back to the Sandbox testing store.</Note>
5 You can see Cash App Pay has confirmed the payment by displaying the amount.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/order-confirmation.png" alt="Order confirmation" />

6 Observe the linked account. `$CASHTAG_C_TOKEN` is our fake account used inside the Sandbox.

![Cashtag token](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/cashtag-token.png)

## Use Case 2: Scan QR codes using a mobile device camera

1 On mobile, navigate to our [Sandbox testing](https://sandbox.pay.withcash.app/checkout). Click on the **Cash App Pay** button.

![Sandbox test store](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/sandbox-test-store.png)

2 You are redirected back to the Sandbox App. **Approve** the payment in the Sandbox App.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/approve-payment.png" alt="Approve payment" />

3 You can see Cash App Pay has confirmed the payment by displaying the amount.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/order-confirmation.png" alt="Order confirmation" />

4 Observe the linked account. `$CASHTAG_C_TOKEN` is our fake account used inside the Sandbox.

![Cashtag token](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/cashtag-token.png)

<Note>
  You can also **Decline** the payment and the Sandbox App will ask you to go back to the shopping website.
</Note>

## Use Case 3: Testing Payment Errors in the Sandbox App

1 On mobile, navigate to our [Sandbox testing](https://sandbox.pay.withcash.app/checkout). Click on the **Cash App Pay** button.

![Sandbox test store](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/sandbox-test-store.png)

2 You are redirected back to the Sandbox App. Click **View more options** in the Sandbox App.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/cap-sand-view-more-opts.jpeg" alt="cap-sand-view-more-opts.jpeg" />

3 The first of several test options appear, in the picture below they are *Account Ineligibilty Overrides* **Customer Ineligible**, and *Payment Overrides* **Connection Error** and **Compliance**.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/2.PNG" alt="2.PNG" />

4 Scroll down for more test options. In the picture below there are two more *Payment Overrides* **Insufficient Funds** and **Other**.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/3.PNG" alt="3.PNG" />

5 Scroll down for final set of test options. In the picture below there are three more *Payment Overrides* **Risk**, **Too Large** and **Too Small**.

6 See the *Magic Values* table in the [Developer Sandbox page](/cash-app-pay-partner-api/guides/technical-guides/sandbox/developer-sandbox#magic-values) for details about testing these payment errors.

# FAQs

**Who is the main audience for this app?**

The main audience for this app is the developers of the businesses to whom we give the Cash App Pay API credentials. We will also give them the links to the Sandbox apps (both Android and iOS).

**Is the Sandbox app widely available for external users?**

No. the App is not widely available for external users.

**Can we use it on Desktop?**

You need a Desktop to test the Pay Kit web SDK. The Pay Kit SDK loads the Merchant website which displays the QR code you have to scan using the Sandbox App. We may consider building a special version of the Sandbox iOS for desktop simulators.

**Is there a difference between the iOS and Android app?**

There are no functional differences between the Android and iOS apps, as the apps are written using a single codebase.
