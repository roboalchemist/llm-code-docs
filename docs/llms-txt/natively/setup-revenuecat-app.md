# Source: https://docs.buildnatively.com/guides/setup-revenuecat-app.md

# Setup RevenueCat App

[RevenueCat](https://www.revenuecat.com/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner) makes implementing in-app purchases and subscriptions easy by handling all purchase validation operations. With RevenueCat, you can allow users to purchase subscriptions, make sure your user pays for some features, and more. You can use [**RevenueCat**](https://www.revenuecat.com/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner) to setup **Stripe.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fvvztd880wN4vkwgKx4PG%2Frevenue_cat_flow.png?alt=media\&token=0295d94c-289a-4bdb-b61d-fcc634ecb96f)

## Video Guides

{% embed url="<https://youtu.be/OVF9FsqCajA>" %}
Part 1
{% endembed %}

{% embed url="<https://youtu.be/e5BUWvcCmEI>" %}
Part 2
{% endembed %}

{% embed url="<https://youtu.be/KqC4jR3Breg>" %}

## Prerequisites

If you are new to RevenueCat, it's recommended you read this first: [What is RevenueCat?](https://www.revenuecat.com/docs/welcome/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner)

## RevenueCat Integration

Integrating the RevenueCat in your app comprises of the following steps:

### **1. Revenue Cat's initial setup**

Follow the first 2 steps of the following guide by RevenueCat to create and configure your RevenueCat app:

{% embed url="<https://www.revenuecat.com/docs/getting-started/?utm_campaign=natively&utm_content=partner&utm_medium=referral&utm_source=solp>" %}

### 2. Connect Revenue Cat with your Natively App

After successfully creating Android/iOS app in the RevenueCat you need to link it with the Natively. For such purpose, follow the next steps:

1. Open your Natively's app dashboard from desktop
2. Go to **Features -> In-app Purchases** and enable it.
3. Enter your **Public app-specific API Keys** to relevant fields. You can find it in your [RevenueCat](https://www.revenuecat.com/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner) project **API Keys -> SDK API keys**

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FmCacx0i6L4L7AtMCiBAn%2Frc_public_keys.png?alt=media&#x26;token=cedef7d1-96b1-488a-a9df-997f5c94d9b8" alt="RevenueCat Public API Keys"><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FHJ2hBG3RFWqLt3OQ3OFL%2Frc_natively.png?alt=media&#x26;token=2bb545b2-1a3d-446b-abe2-0a4fcc64c27f" alt="Natively: In-app Purchases feature"><figcaption></figcaption></figure>

4. Save the changes.&#x20;
5. Order a new build. We will inject the following keys into your app code.

### 3. Google Play / App Store products setup

Before incorporating subscriptions into your app, you will first need to create the subscription products in the Google Play Store and App Stores.

#### Google Play Store

To create a subscription product in the Google Play Store:

1. Open your app on the [Google Play Console](https://play.google.com/console).
2. Open the **Subscriptions** tab (from the left side menu). Check if you see **Create subscription** button. If you do, you can skip this step.&#x20;
3. If you see a message saying '***Your app doesn't have any in-app products yet**'* like in this picture:

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FLwh48BsHBP4HpAuOQrkp%2Fimage.png?alt=media\&token=a739b79e-f28f-42e5-84ed-4b070410b272)

You will need to complete the following steps:

1. Download the **AAB file** of your app, that was delivered on your email (or from the Natively dashboard)
2. Go to the Play Console. Open your **Closed testing** track and create a new release.
3. Upload your **AAB** file, enter the Release name and create the release.
4. Go back to the **Subscriptions** tab again. It should let you manage subscriptions now.
5. Now, follow [this guide](https://www.revenuecat.com/docs/android-products/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner) by RevenueCat to configure your products or subscriptions on Google Play.

#### App Store

To create a subscription product in App Store:

1. Open [App Store Connect Portal](https://appstoreconnect.apple.com/) and navigate to your app.
2. Follow [this guide](https://www.revenuecat.com/docs/ios-products/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner) by RevenueCat to configure your products or subscriptions for App Store
3. Make sure that the state of your purchases is **Ready to Submit**.
4. Navigate to the [Agreements](https://appstoreconnect.apple.com/agreements) page and sign the ***Paid Apps*** agreement. The state must be ***Active*** before making purchases, even in the sandbox mode.
5. Navigate the [Testers](https://appstoreconnect.apple.com/access/testers) page and add sandbox testers. Make sure to confirm the emails of all sandbox testers.

### 4. Revenue Cat products setup

RevenueCat uses an **Entitlements** system to control access to premium features, and **Offerings** to manage the set of products you offer to customers.

Learn more about configuring products in RevenueCat [here](https://www.revenuecat.com/docs/entitlements?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner).&#x20;

{% hint style="info" %}
You must create at least one entitlement and at least one offering for using RevenueCat with Natively.
{% endhint %}

After the creation, the Products, Entitlements, and Offers will look like this:

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FnhBB5WrJjh9Jhywr8dca%2Frc_entitlements.png?alt=media&#x26;token=08236c04-08ef-4eb0-a752-0b0db34bbacd" alt="RevenueCat: Entitlements"><figcaption><p>Add at least 1 Entitelement</p></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FeegYTV58s8rt1cjEE3MQ%2Frc_offerings.png?alt=media&#x26;token=85574ad1-6001-4f5a-a7fb-20df822c9ab4" alt="RevenueCat: Offerings"><figcaption><p>Add at lest 1 Offering</p></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FFC5BpbmQPhj1Kzl8rsLI%2Frc_products.png?alt=media&#x26;token=c2df6053-eadc-4c24-aa90-f21c137496f6" alt="RevenueCat: Products"><figcaption><p>Add iOS &#x26; Android (Stripe is optional)</p></figcaption></figure>

{% hint style="info" %}
To use a Stripe with Android & iOS subscription/products, check [this](https://www.revenuecat.com/docs/stripe/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner) page for more details.
{% endhint %}

#### Connect to Google Play Store

To allow RevenueCat servers to communicate with Google on your behalf, please follow the instructions present on this page:

{% embed url="<https://www.revenuecat.com/docs/creating-play-service-credentials/?utm_campaign=natively&utm_content=partner&utm_medium=referral&utm_source=solp>" %}

{% hint style="info" %}
It may take a few hours for these credentials to propagate. Until then, your purchases can fail with "*There was a credentials issue. Check the underlying error for more details*".
{% endhint %}

#### Connect to Apple App Store

To connect the RevenueCat servers to App Store, follow the instructions present on this page:

{% embed url="<https://www.revenuecat.com/docs/itunesconnect-app-specific-shared-secret/?utm_campaign=natively&utm_content=partner&utm_medium=referral&utm_source=solp>" %}

And this one:

{% embed url="<https://www.revenuecat.com/docs/app-store-connect-api-key-configuration>" %}

### 5. Development

{% content-ref url="integration/in-app-purchases" %}
[in-app-purchases](https://docs.buildnatively.com/guides/integration/in-app-purchases)
{% endcontent-ref %}

### 6. Testing

#### Creating Test Users

**Test on Android**: To create test users to try Play Store purchases in the sandbox mode, follow [this guide](https://www.revenuecat.com/docs/google-play-store#create-a-test-user-and-configure-licensing-testing?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner) by RevenueCat. You need to create a test user, configure licensing testing, create a closed track, and add a tester.

**Test on iOS**: To create test users to try App Store purchases in the sandbox mode, follow [this guide](https://www.revenuecat.com/docs/apple-app-store#create-a-sandbox-test-account/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner) by RevenueCat.
