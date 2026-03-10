# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/shopify/add-cash-app-pay-at-checkout.mdx

***

## stoplight-id: 70txheffr0mzj

# Add Cash App Pay at Checkout

Cash App Pay is a fast and simple payment method that lets customers pay for purchases either by scanning a simple QR code or by tapping Cash App Pay at checkout to be redirected to Cash App.

You can use your existing Cash App Afterpay integration to enable this feature, and it works on Desktop, Mobile, and in a native app.

**Prerequisites**

Before you integrate Cash App Pay into Shopify ensure that you are:

* An existing Cash App Afterpay merchant on Shopify with a proven integration

* A US merchant

<Info>
  Cash App Pay will appear as another payment option on your payment page alongside Cash App Afterpay. It will <em>not</em> be just a tender type within a Cash App Afterpay payment.
</Info>

## Overview

The Cash App Pay integration process can be completed in three stages:

* [Download the Cash App Pay payment application](#download-the-cash-app-pay-payment-application)

* [Connect your Account](#connect-your-account)

* [Final Confirmation and Activation](#final-confirmation-and-activation)

<Warning>
  You must use your Cash App Afterpay production merchant ID and your Cash App Afterpay production secret Key in the Cash App Pay integration process. Your sandbox credentials will not work for account activation, even if you are in a sandbox environment.
</Warning>

## Download the Cash App Pay payment application

1. Go to the [Cash App Pay](https://apps.shopify.com/cash-app-pay) page on the Shopify App Store.

2. Login to Shopify.

3. Download the Cash App Pay application. The Install app screen appears. See the picture below:

![cap-shop-payment-app-activation-1.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/cap-shop-payment-app-activation-1-2.png)

4. Shopify asks you to grant Cash App Pay (Cash App Afterpay) permission to *View personal data* and *View and edit store data*. Click **Install** to continue.

## Connect your account

To connect your account, do the following:

1. After downloading and installing the Cash App Pay app, from the following screen, click **Connect to Cash App Pay**.

![cap-shop-payment-app-activation-2.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/cap-shop-payment-app-activation-2.png)

2. The *Connect to Cash App Pay* screen appears:

![cap-shop-payment-app-activation-3-small.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/cap-shop-payment-app-activation-3-small.png)

3. Enter your Cash App Afterpay production merchant ID in the **Merchant ID** field.

4. Enter your Cashs App Afterpay production secret key in the **Secret Key** field.

5. Click **Continue**.

<Warning>
  In step 3 above, you must use your Cash App Afterpay 

  **Production**

   merchant ID. In step 4 above, you must use your Cash App Afterpay 

  **Production**

   secret key. Your Sandbox credentials 

  **will not work**

   for account activation, even if you are in a Sandbox environment.
</Warning>

## Final Confirmation and Activation

After you click **Continue** in Step 5 above, you are redirected to the following page for final confirmation:

![cap-shop-payment-app-activation-4-small.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/cap-shop-payment-app-activation-4-small.png)

Do the following:

1. Ensure the *Cash App Pay* toggle switch is enabled (black).

2. Ensure *Test Mode* is off (grey).

3. Click **Activate**.

Your customers should now have Cash App Pay available as a payment method alongside Cash App Afterpay at checkout.

!\[Screenshot 2025-03-20 at 4.22.03 PM.png]\(../../../assets/images/Screenshot 2025-03-20 at 4.22.03 PM.png)
