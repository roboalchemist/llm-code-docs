# Source: https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks.md

# Setup website Universal Links (Deeplinks)

{% embed url="<https://www.youtube.com/watch?v=ZegNTNAOJVM>" %}

## Android

### Setup Associated Domain

#### Create assetlinks.json file

* Download the following template file and open it.

{% file src="<https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-54b07d39453dd6e52c0917ae298838bbd4c81735%2Fassetlinks.json?alt=media>" %}

* Replace [**BUNDLE\_ID**](https://docs.buildnatively.com/guides/broken-reference) \*\*\*\* with your IDs
* Replace PRODUCTION\_SHA256 & STAGING\_SHA256 with your fingerprint value

{% hint style="info" %}
If you don't see 'App sigining' content, you need to [upload](https://support.google.com/googleplay/android-developer/answer/9845334#zippy=%2Cinternal-test-manage-up-to-testers) your app first.
{% endhint %}

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-adc9f644a15ca0c8b894694f5c04b656b1099a9a%2Fimage.png?alt=media)

* In the final result you should get something like this:

```
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "com.example.app",
      "sha256_cert_fingerprints":
        [
          "E7:8B: (YOUR KEY HERE) :BB:98",
          "0F:38: (YOUR KEY HERE) :1B:F2"
        ]
    }
  }
]
```

* Save the file as **assetlinks.json**

#### Setup your bubble.io website

* Open your bubble project
* Go to the **Settings -> SEO / metatags**
* Scroll down and find **Hosting files in the root directory** section
* Set name to **.well-known/assetlinks.json** and upload your file
* Publish the changes

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-e18da03cad5ae3ff3b22aca926dc67c957217baa%2Fimage.png?alt=media)

### Verify Android Domain Works

{% embed url="<https://developers.google.com/digital-asset-links/tools/generator>" %}

## iOS

### Prerequisites

* [Add](https://docs.buildnatively.com/guides/broken-reference) the Associated Domains feature to your Bundle Identifier.

### Setup Associated Domain

#### Create apple-app-site-association file

* Download the following template file and open it.

{% file src="<https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-c225432635c1de6a0f4d1b5153ee4bb9b8108db4%2Fapple-app-site-association?alt=media>" %}

* Replace **TEAM\_ID &** [**BUNDLE\_ID**](https://docs.buildnatively.com/guides/broken-reference) \*\*\*\* with your IDs
  * To find **TEAM\_ID**, open the Apple's developer website
  * Click Membership
  * Copy your Team ID

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-8dd62e1bf6e96266426014cf304c8716378561d4%2FSCR-20220518-kxn.png?alt=media)

* In the final result you should get something like this:

```
{
	"applinks": {
		"apps": [],
		"details": [{
			"appID": "TEAM_ID.BUNDLE_ID",
			"paths": [
				"*"
			]
		}]
	}
}
```

* Save the file as **apple-app-site-association**

#### Setup your bubble.io website

* Open your bubble project
* Go to the **Settings -> SEO / metatags**
* Scroll down and find **Hosting files in the root directory** section
* Set name to **.well-known/apple-app-site-association** and upload your file
* Publish the changes

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-e200a8cf001d4eab3745e155193f1437ad5c07c1%2FSCR-20220518-l60.png?alt=media)

### Verify iOS Domain Works

{% embed url="<https://branch.io/resources/aasa-validator/>" %}

{% hint style="info" %}
If your app supports both Android and iOS, you must upload both the [`assetlinks.json`](https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks#create-assetlinks.json-file) file for Android and the [`apple-app-site-association`](https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks#create-apple-app-site-association-file) file for iOS to your web server.
{% endhint %}

## Enable the Universal Links feature

[Enable](https://docs.buildnatively.com/natively-platform/features/deeplinks#android) the Universal Links feature and fill out all relevant information.
