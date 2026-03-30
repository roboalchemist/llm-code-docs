# Source: https://docs.buildnatively.com/natively-platform/features/deeplinks/universal-links.md

# Universal Links

Deeplinks (Or Universal Links) is a useful feature for associating your website domain with your mobile native app. Also, your users will be able to click a deep URL (Url with some path or parameter), and they will be redirected to the same page in the app.

* [iOS](#ios)
* [Android](#android)
* [How to enable Deeplinks?](#how-to-enable-deeplinks-universal-links)

## iOS

[Universal Links](https://www.singular.net/glossary/universal-links/) are Apple’s deep linking technology, designed to replace the older URI-scheme deep linking method. They are available for devices running iOS 9 and above.

While Universal Links allow for deep linking behavior similar to URI schemes, they function very differently behind the scenes. Universal Links look like normal HTTPS URLs, e.g. “<https://www.linkedin.com”>. When a user clicks a Universal Click, the user’s device opens the app that the link was configured for. If the app is not installed on the device, the user is taken to the actual URL in their mobile browser.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-4f097c9772a02a85d25f33de34067642e69f0c86%2FSCR-20220526-hjp.jpeg?alt=media) ![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-4963aa28fe777a0b1a0694b8ce4d66df8407abd4%2FIMG_2397.gif?alt=media)

To configure your app to work with Universal Links (Associated Domains) feature you need to do the following steps:

1. [Add](#add-associated-domains-feature-to-bundle-identifier) the Associated Domains feature to your Bundle Identifier.
2. [Setup](https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks#ios) your website to work with Apple's Associated Domains.
3. [Enable](#how-to-enable-deeplinks-universal-links) the Universal Links feature and fill out all relevant information.

### Add Associated Domains feature to Bundle Identifier

* Open the [Apple Developer homepage](https://developer.apple.com/account) and select [**Certificates, IDs & Profiles**](https://developer.apple.com/account/resources/certificates/list) \*\*\*\* (left menu)
* Click on the [Identifiers](https://developer.apple.com/account/resources/identifiers/list)
* Select previously [created Bundle Identifier](https://docs.buildnatively.com/natively-platform/features/deeplinks/broken-reference)
* Scroll down and enable **Associated Domains**
* Click **Save & Confirm**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-1fa93db60f51750b48ac0c7a71534839d3160509%2FScreen%20Recording%202022-05-18%20at%2014.22.34.gif?alt=media)

## Android

To configure your app to work with Universal Links (Associated Domains) feature, you need to do the following steps:

1. [Setup](https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks#android) your website to work with Associated Domains.
2. [Enable](#how-to-enable-deeplinks-universal-links) the Universal Links feature and fill out all relevant information.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-e02ff86d52ef12c4e0b852425b83604a1c97c408%2Ftelegram-cloud-document-2-5382327357489027926.gif?alt=media)

### How to enable Deeplinks (Universal Links)?

Turn on the **Universal Links** feature on the **Native Feature** step and fill out the following information:

* **Associated Domain -** is your website domain. We will prefill it with your [App URL](https://docs.buildnatively.com/natively-platform/features/deeplinks/broken-reference)'s domain. You can modify this value, but make sure you've entered a valid domain. Changing this field in the future will require a rebuild.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fb0lm1N5nve3Pq8XmzQUo%2FDeeplinks.png?alt=media&#x26;token=9e902b30-fbfe-4c92-9b13-2a3727889adb" alt=""><figcaption></figcaption></figure>

##
