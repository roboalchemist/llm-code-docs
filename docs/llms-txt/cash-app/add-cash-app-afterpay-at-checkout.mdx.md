# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/shopify/add-cash-app-afterpay-at-checkout.mdx

***

## stoplight-id: q3krc9umjl3w2

# Add Cash App Afterpay at Checkout

Before you start, ensure that you have Shopify installed and working.

<Info>
  The Shopify App Store listing and app logo will reflect the new Cash App Afterpay brand, while the payment app itself continues to be called **Afterpay US**. Your customers will see the updated branding at checkout.

  For a list of requirements before you add Cash App Afterpay, see the [Requirements](#requirements) section at the bottom of this page.
</Info>

## Overview

The Cash App Afterpay integration process can be completed in three stages:

* [Download the Afterpay US payment app](#download-the-afterpay-us-payment-app)
* [Connect your Business Hub account](#connect-your-business-hub-account)
* [Confirm and activate](#confirm-and-activate)

## Download the Afterpay US payment app

Do the following:

1. Click [here](https://accounts.shopify.com/store-login?redirect=settings%2Fpayments/alternative-providers/84934657) to download the Afterpay US payment app.
2. When the **Install app** screen appears, click **Install**.
3. Once installed, Afterpay US (New) appears in your list of apps.

## Connect your Business Hub account

After you install the Afterpay US app, you are automatically redirected to the Business Hub to verify your merchant account.

Follow these steps to connect your account:

### Step 1: Log into Business Hub

Log into your Business Hub user account.

<Tip>
  If you have trouble accessing your Business Hub account, try [resetting your password](https://hub.us.afterpay.com/forgot-password). If you need an account to be created, contact your team's main internal onboarding contact.
</Tip>

### Step 2: Select your merchant account

1. From the dropdown menu, select the merchant account that should be associated with your storefront.
2. Ensure that this is the correct account for your specific Shopify store.

### Step 3: Complete connection

1. Click the **Connect** button to link your Business Hub merchant account with Shopify.
2. Wait for the connection process to complete.
3. Once you have a successful connection, you're automatically returned to Shopify.

## Confirm and activate

After successfully verifying your Business Hub merchant account, you return to Shopify. A screen appears with two toggle switches and a *More actions* menu. Do the following:

1. Activate the payment gateway. Keep **Test mode** inactive, and click **Activate**. This screenshot shows the result:

   <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Shopify-Cash-AfterpayUS-activated.png" />

   <Warning>
     **Do not enable Test mode.**

      If you enable Test mode, the integration fails. The 

     **Enable test mode**

      function is only for use on dedicated test websites. Contact your Afterpay Account Manager if you need test credentials.
   </Warning>
2. Go to your online store and verify that Afterpay is a checkout option.

### Managing merchant integration

If you ever need to change which merchant account is connected to your Shopify store, it's a simple process:

1. In your Shopify admin, go to Settings → Payments
2. Click into the Afterpay US (New) payment app
3. Then, click More actions → Manage
4. This will take you back to the Business Hub where you can select a different merchant account
5. Choose the new account you want to use and click Connect

That's it! The new merchant account will now be connected to your Shopify store.

## Requirements

To avoid issues installing the new Afterpay US app, check that you have Shopify installed and working.

Make sure that your company or organization meets the following requirements:

Your business address is in one of the the following:

* Australia
* Canada
* Hong Kong SAR
* New Zealand
* United Kingdom
* United States

You must ship to the United States.

You must accept USD (United States Dollars) as a currency.
