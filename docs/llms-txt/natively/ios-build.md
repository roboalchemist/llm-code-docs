# Source: https://docs.buildnatively.com/natively-platform/app-info/ios-build.md

# iOS App

{% embed url="<https://app.arcade.software/share/3xBLgiVJIbZpn8Axtn8e>" %}

## Prerequisites

* Create an [Apple account](https://appleid.apple.com/account?appId=632\&returnUrl=https%3A%2F%2Fdeveloper.apple.com%2Faccount%2F)
* [Purchase an Apple Developer membership](https://developer.apple.com/programs/enroll/). Please see [this](https://developer.apple.com/programs/) link for more details on the Apple Developer program.

## App Store Credentials&#x20;

Please follow these steps to generate your API Key:

* Open an [App Store Connect](https://appstoreconnect.apple.com/) page and navigate to [Users and Access - Integrations](https://appstoreconnect.apple.com/access/integrations/api)

{% hint style="info" %}
In the [organization](https://developer.apple.com/programs/enroll/) type of apple account, **only admins or the owner** can access this tab. But in [personal](https://developer.apple.com/programs/enroll/) only the **owner**.
{% endhint %}

* If you see the **Request Access** button, click on it.
* If you haven't added any key before, click on the **Generate API Key**. Otherwise, select the **Add button (+).**
* A popup will appear. Enter your API Key Information:
  * **Name:** Enter a name for the key. This is a reference and is not part of the key itself.
  * **Access:** Select the access type **App Manager**
* When you are done, select **Generate.**
* Find the row for the API Key you just generated and select **Download API Key.** A popup will appear, select **Download.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-1b2b4f4b44e6c620804e9b869caf73d004daad16%2FSCR-20220530-td1.png?alt=media)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fzc81KcJEEyy6d5soerSP%2Fimage.png?alt=media&#x26;token=85055ad5-133b-494e-8269-495535282d81" alt=""><figcaption></figcaption></figure>

## Bundle Identifier

{% hint style="warning" %}
The Bundle Identifier is a unique identifier for your app. Once set, it can only be changed if your app or developer account is suspended. Please find more details in our [FAQ](https://docs.buildnatively.com/getting-started/faq#how-do-i-change-my-app-ios-or-android-bundle-id-bundle-identifier)
{% endhint %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FnZJ1cF3xOg1q79mQm2d5%2FiOS.png?alt=media&#x26;token=dfefccb4-7718-4e7a-9df7-0d40ac99a78b" alt=""><figcaption></figcaption></figure>

### Generate Bundle ID

Natively will automatically generate a bundle identifier for your app, otherwise, you can create your own.

### Create Own Bundle ID

A Bundle Identifier (ID) is a unique number that identifies your app inside of the Apple ecosystem.

{% hint style="info" %}
If it's a personal Apple account, only the owner can create a Bundle ID
{% endhint %}

Please follow these steps to create a Bundle ID or use a shortcut [link](https://developer.apple.com/account/resources/identifiers/bundleId/add/bundle) to skip these steps:

* Open the [Apple Developer homepage](https://developer.apple.com/account) and select [**Certificates, IDs & Profiles**](https://developer.apple.com/account/resources/certificates/list) \*\*\*\* (left menu) and then select [**Identifiers**](https://developer.apple.com/account/resources/identifiers/list)**.**
* Click on the [**Add button (+)**](https://developer.apple.com/account/resources/identifiers/add/bundleId)**.**
* Select **App IDs** and then click **Continue.**
* Select **App** and then click **Continue.**
* Enter the [App Bundle Information](https://help.apple.com/app-store-connect/#/deveaec374de):
  * **Bundle ID:** Enter a package name (i.e. com.yourcompany.appname)
  * **Description:** Provide a short description of your app (can be anything, this will not appear in the App Store).
  * **Capabilities:** skip for now.
* When you are done, select **Register.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-30154eb085be7dcd544bdfdc18197ef20eeb8fec%2FSCR-20220530-tlu.png?alt=media)

* Return to our platform and fill the **Bundle Identifier** field with Bundle ID (Note: **No need to copy** App ID Prefix it's not [App Store App ID](#app-store-app-id))

### Demo:

![Create Bundle Id](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-c8b021af6ec27cc252124d0c907b13afe5af0705%2Fbundleid.gif?alt=media)

## App Store App Id

[App Store Connect](https://help.apple.com/app-store-connect/#/dev2cd126805) is used to submit apps to the App Store, manage apps, and more.

* Navigate to [App Store Connect](https://appstoreconnect.apple.com/) and then select [My Apps](https://appstoreconnect.apple.com/apps).
* Click on the **Add button (+)** and then select **New App.**
* A popup will appear. Enter your app information:
  * **Platform:** for mobile apps, this will be **iOS**.
  * **Name:** Enter a Name for your app (this is the name that will show in the App Store).
  * **Primary Language** for your app.
  * **Bundle ID:** Select the **Bundle ID** you created in the [previous step](#bundle-identifier).
  * **SKU**: Enter a unique identifier. You can also add your **Bundle ID** here, as long as it is unique.
  * User Access: **Set the user access.** If you select Limited Access, you will need to select the users that you would like to be able to access this app. This will only appear if you have other users included in your App Store Connect account.
* When you are done, select **Create.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-e487c02f2e43f7252ff6ca4c98fd1088a099cc8c%2FSCR-20220530-tj3.png?alt=media)

* Then you will be navigated to the main dashboard for your app. (Note: sometimes it takes a few minutes to create the app, just reload the page and navigate to your app)
* Select **App Information** (under **General** in the left Sidebar\*\*).\*\*
* Scroll down to **General Information** and find your **Apple ID.**
* Select the **Apple ID** and \*\*\*\* copy it.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-b1cae21ae1cae4504e27b7acc02766077c17f36e%2FSCR-20220530-tjy.png?alt=media)

* Return to our platform and fill the **App Store App Id** field with **Apple ID**

### Demo:

![Create App](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-e8f1898655d5df911d878ab5fbbf1c5463956a58%2Fappid.gif?alt=media)
