# Source: https://docs.buildnatively.com/guides/generate-ios-push-key.md

# Generate iOS Push Key (NEW)

{% hint style="warning" %}
This page is no longer being updated. Please refer to our [Push Notifications - OneSignal](https://docs.buildnatively.com/guides/integration/push-notifications-onesignal) for current configurations and support.
{% endhint %}

## Prerequisites

* Created [Bundle Identifier](https://docs.buildnatively.com/natively-platform/app-info/ios-build#bundle-identifier) & [AppStore App Id](https://docs.buildnatively.com/natively-platform/app-info/ios-build#app-store-app-id)

### Generate Push Key

## Step 2. Generate a new p8 key

Log in to your [Paid Apple Developer Account](https://developer.apple.com/) and navigate to **Certificates, Identifiers & Profiles** > **Keys** and select the **Blue +** button.

<figure><img src="https://files.readme.io/1e2ff6e-Apple_Key_Page.jpg" alt="2616"><figcaption><p>Apple Developer Account - Keys Page</p></figcaption></figure>

Select **Apple Push Notifications service (APNs)**, and enter a name for the key.

<figure><img src="https://files.readme.io/312d551-Apple_Key_Page_-_Register.jpg" alt="2622"><figcaption><p>Apple Developer Account - Register a New Key Page. Select APNs.</p></figcaption></figure>

Select **Continue,** and on the next page, select **Register**.

**Download** your new key and save it in a secure place. You can only download it once, so don't lose it. Then, click **Done,** and you will have a new key.

> 🚧
>
> Previous Token Revokation
>
> You can have up to two .p8 keys in your Apple account. If you need to generate a third key, you will need to revoke one of your existing keys and it can no longer be used.

*Note: .p8 keys are in the “keys” section of the Apple developer account and the .p12 certificates are under “certificates”. In your Apple account, you can only have two .p8 keys, but you can have both active .p12s and .p8s.*

### Gather all required data

1. Now you have .p8 downloaded
2. Also you will need **Key ID** and **Team ID**&#x20;

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FyXdQUMQ77GY6vK6NfjN9%2Fimage.png?alt=media&#x26;token=71de39b6-1e72-4cbb-8bc6-991c3208d5ee" alt=""><figcaption></figcaption></figure>

3. Get your **Bundle ID**

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FHZzzbtWquP1FH2dTDjHo%2Fimage.png?alt=media&#x26;token=4f9b69c6-6821-4a80-890a-cf693617a5bb" alt=""><figcaption></figcaption></figure>

Now you have all the data to continue configuring your [One Signal App](https://docs.buildnatively.com/guides/setup-one-signal-app)
