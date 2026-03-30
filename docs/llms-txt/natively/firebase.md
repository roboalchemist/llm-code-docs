# Source: https://docs.buildnatively.com/natively-platform/features/deeplinks/firebase.md

# Firebase (Deprecated)

{% hint style="warning" %}
On August 25th, 2025, Firebase Dynamic Links was shut down.
{% endhint %}

[Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links) are links that work the way you want, on multiple platforms, and whether or not your app is already installed.

{% embed url="<https://youtu.be/LvY1JMcrPF8>" %}

With Dynamic Links, your users get the best available experience for the platform they open your link on. If a user opens a Dynamic Link on iOS or Android, they can be taken directly to the linked content in your native app. If a user opens the same Dynamic Link in a desktop browser, they can be taken to the equivalent content on your website.

In addition, Dynamic Links work across app installs: if a user opens a Dynamic Link on iOS or Android and doesn't have your app installed, the user can be prompted to install it; then, after installation, your app starts and can access the link.

{% hint style="danger" %}
Right now, we don't support 'custom domain' (only xxxx.page.link) & links analytics. We might consider adding this in the future.
{% endhint %}

## Create a new Firebase Project

* Go to <https://console.firebase.google.com/>
* Click New Project, enter the project name

{% hint style="info" %}
You can use the same one for Android push notifications.
{% endhint %}

## Enable Dynamic Links

* Go to **All products** tab, scroll down, click **Dynamic Links**, and then **Get started**
* Fill out **Domain** field

{% hint style="info" %}
For now, we support only Google domains (xxxxxx.page.link). Custom domain support will be added in the future.
{% endhint %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FflXvLzlvG2W6Y1bln7vV%2F2%20add%20link.gif?alt=media&#x26;token=413ea9a2-d7e2-41ee-9750-bc65a18b7278" alt=""><figcaption></figcaption></figure>

## Set your first allowed domains

* Click on **Dynamic Links** in the left menu and then click **Set domains**

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FDpwctAb1yCat8wDw35zL%2FSCR-20221025-old.png?alt=media&#x26;token=98a2189c-4a91-4dda-9b62-6a5d7337b3cf" alt=""><figcaption></figcaption></figure>

* Add allowed domains (a URLs related to  your website)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FdNGnnBoySnJsIOl2MVjf%2F3%20set%20allowed%20domains.png?alt=media&#x26;token=eb0e6d3f-836d-4223-824c-a2c5cb5f8760" alt=""><figcaption></figcaption></figure>

## **Add Android & iOS apps**

* Go to **Project Overview** and click **Add App** at the top

{% tabs %}
{% tab title="🍏 Setup iOS App" %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F04VGJ54b0CKxE7EloMcy%2F4%20add%20ios%20app.gif?alt=media&#x26;token=cbcce5a7-f976-4257-a1ce-966bc5f9f466" alt=""><figcaption></figcaption></figure>

* Add your Bundle ID & App Store ID (You can find this IDs in your App Store Connect account)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FejQAFiCePZc9lqIckT9V%2F4%201%20apple%20id%20.png?alt=media&#x26;token=ca362084-583b-44f2-9100-dabb0f8b1c3f" alt=""><figcaption></figcaption></figure>

* **Download & Save** a config file (you will need it later)
* **Go to** the [Apple Developer homepage](https://developer.apple.com/account) and select [**Certificates, IDs & Profiles**](https://developer.apple.com/account/resources/certificates/list) \*\*\*\* (left menu)
* Click on the [Identifiers](https://developer.apple.com/account/resources/identifiers/list)
* Select previously [created Bundle Identifier](https://docs.buildnatively.com/natively-platform/features/deeplinks/broken-reference)
* Scroll down and enable **Associated Domains**
* Click **Save & Confirm**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-1fa93db60f51750b48ac0c7a71534839d3160509%2FScreen%20Recording%202022-05-18%20at%2014.22.34.gif?alt=media)
{% endtab %}

{% tab title="🤖 Setup Android App" %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FHAskXHO2djFxB0tr37Du%2F5%20add%20android%20app.gif?alt=media&#x26;token=9902a311-0b64-44cd-96e8-4c842291fb13" alt=""><figcaption></figcaption></figure>

* Add your Bundle ID (You can find this IDs in your Google Developer Console account or in **Publish** section in Natively)
* Skip SHA-1 field (we will add it in next step)
* **Download & Save** config file (we will need it later)
* Make sure to finish flow and navigate to **Project Overview**
* Go to Project settings, scroll down, select Android app

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FVTQ5Xsq5Mp6x6An01UZ3%2FSCR-20221025-nkq.png?alt=media&#x26;token=7a1f996d-fe3c-4618-ba0b-a64e03aca00d" alt=""><figcaption></figcaption></figure>

* Now we need to add app's fingerprints
* You can find these values in your Google Developer Console
* Go to Setup -> App Integrity -> App Signing
* Copy **SHA-1** & **SHA-256** values from **App signing key ceritifcate** section and add it to your firebase Android app

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FjxaBGeEcGsXc394p04Kn%2F5%201%20android%20keys.png?alt=media&#x26;token=a9d4934b-4e02-4547-b46b-b132b7db26fc" alt=""><figcaption></figcaption></figure>

* Copy **SHA-1** & **SHA-256** values from **Upload key ceritifcate** section and add it to your firebase Android app

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FjfCJTRO1JzDVktQtVD66%2F5%202%20android%20keys.png?alt=media&#x26;token=813265a5-c877-47a6-a148-602c2c8a5243" alt=""><figcaption></figcaption></figure>

* Make sure you've added 4 SHA keys

{% hint style="info" %}
If you don't see App integrity keys, make sure you've uploaded at least 1 build of your app to Google Play Console
{% endhint %}
{% endtab %}
{% endtabs %}

## Enable Deeplinks on the Natively platform

That's it. At this step, you need to switch to the Natively app and fill out a few fields

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FMajHn0vlrDymxEb1heCL%2FSCR-20221025-p56.png?alt=media&#x26;token=352f4785-5797-4bb0-a3bc-87ee6282926d" alt=""><figcaption></figcaption></figure>

* Your Firebase Dynamic Links domain
* iOS Config file (GoogleService-Info.plist)
* Android Config file (google-services.json)

## Create Dynamic Links

There are 3 ways (supported by Natively) how you can create a Dynamic Link:

* Using the [Firebase console](https://console.firebase.google.com/project/_/durablelinks/links/). This is useful if you're creating promo links to share on social media.
* Using the [REST API](https://firebase.google.com/docs/dynamic-links/rest). This is the preferred way to dynamically create links on platforms that don't have a Builder API. The [Analytics REST API](https://firebase.google.com/docs/reference/dynamic-links/analytics) can be used to track the performance of promo campaigns created in the console.
* [Manually](https://firebase.google.com/docs/dynamic-links/create-manually). If you don't need to track click data and you don't care if the links are long, you can manually construct Dynamic Links using URL parameters, and by doing so, avoid an extra network round trip.
