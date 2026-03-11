# Source: https://docs.buildnatively.com/guides/generate-ios-push-certificate.md

# Generate iOS Push Certificate (Legacy)

{% hint style="warning" %}
This page is no longer being updated. Please refer to our [Push Notifications - OneSignal](https://docs.buildnatively.com/guides/integration/push-notifications-onesignal) for current configurations and support.
{% endhint %}

## Prerequisities

* Created [Bundle Identifier](https://docs.buildnatively.com/guides/broken-reference) & [AppStore App Id](https://docs.buildnatively.com/guides/broken-reference)
* [Mac OS](#mac-os), [Windows, or Linux](#windows-and-linux)

## Mac OS

* Open a Keychain Access and select

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-3b6420bee50ae01da278132d14bac0051ac6b1c5%2Fmac1.png?alt=media)

* Enter your email, name, and select **Saved to disk.** Click **Continue.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-db584562866d1e9d151e4f104480ea097e2e7f4d%2Fmac2.jpeg?alt=media)

* After we've created the **Certificate Request** file:
  * Open the [Apple Developer homepage](https://developer.apple.com/account) and select [**Certificates, IDs & Profiles**](https://developer.apple.com/account/resources/certificates/list) \*\*\*\* (left menu)
  * Click on the [**Add button (+)**](https://developer.apple.com/account/resources/certificates/add)\*\*\*\*
  * Select **Apple Push Notification service SSL (Sandbox & Production)**
  * Click **Choose File** and select the **CertificateSigningRequest.certSigningRequest** file.
  * Click **Continue** & **Download**.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-83122537bf1d99b7d7b6e7375a8c4e678ece03c9%2F16.gif?alt=media)

* Double click on the aps.cer file, and open a Keychain Access.
* Open **login -> Certificates** and select your certificate. (You can search it by your app bundle id)

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-e099fc6c671a529bd20e9bd7d2ab5edb7e19f778%2Fmac3.png?alt=media)

* Right-click on it and click **Export "Apple Push Service: ..."**. \*\*\*\* After that \*\*\*\* select a place where you want to save an exported file.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-e57c4f172c5cd34b9b023ae0744e265b9bfc54f0%2Fmac4.png?alt=media)

* Enter a password (you will use it for OneSignal later) and click **OK.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-009980d7c45c8d1a3bd4840c4c47ee1511092860%2Fmac5.png?alt=media)

* That's it, we've generated our .p12 certificate that can be used for OneSignal Push Notifications.

## Windows & Linux

* Install [Keychain Explorer](https://keystore-explorer.org/downloads.html) tool.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-2da1eaf4315d75a7062361f16a3282ec30d8d5b4%2F1.png?alt=media)

* Open KeyStore Explorer and click **Create a new KeyStore**.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-357b0e1b0947b66f86681f5c40dc49b4e48e9185%2F2.png?alt=media)

* Select **PKCS #12** Type and click **OK.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-408a824da33eb38a3ef364efbc7586d071d23a98%2F3.png?alt=media)

* After KeyStore was created, right-click on empty space and select **Generate Key Pair.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-6372a9dcc758e212fe356391c18938a83d086cb2%2F4.png?alt=media)

* Make sure that all parameters match a screenshot one and click **OK**.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-d36d380880cf2a0bd6ca9b6f4e4094a846601b2b%2F5.png?alt=media)

* Click **Contacts** button

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-57d3a413a49dfd1d2eed7d3e2153bb8269c68dc6%2F6.png?alt=media)

* We need 3 parameters (**Common Name,** **Email,** and **Country**). You can select them in the dropdown list and remove the rest through **(-)** button.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-84a28c48b4734a4e9cff2a93420ef2c2503d8aa1%2F7.png?alt=media)

* Enter all information. Make sure the **Country** parameter has a 2 symbols value (USA - **US**, Ukraine - **UA**, Germany - **GE**, etc.). You can find your country code [here](https://cheapsslsecurity.com/p/what-is-ssl-country-code-and-how-do-i-get-one-for-my-csr/).

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-abbd0214cd47a2fae387bbca9adefe033223fe9c%2F8.png?alt=media)

* Make sure that all parameters match a screenshot one and click **OK**. (Next two popups will be with name and password, you can click **OK** without editing on both of them).

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-f7cf3e4dd29153613119456c3de98db12a639732%2F9.png?alt=media)

* Right-click on your new Key Pair and select **Generate CSR**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-1218427a5c3292a80c5668302b5505a5c9a435ec%2F12.png?alt=media)

* Click **Browse.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-41532cc7a5b5f9299283283155148a88b0711155%2F13.png?alt=media)

* Select a directory where you want to save your file, enter a filename (*YOURFILENAME***.csr**) \*\*\*\* and click **Choose**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-66555763541a3dddeafa306633be78a3c0581d3b%2F14.png?alt=media)

* Make sure that all parameters match a screenshot one and click **OK**.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-c9a15ee02ba01d59df4094055c2b8991b6521a15%2F15.png?alt=media)

* After we've created **CSR** file, open your [Apple Developer account:](https://developer.apple.com/account)
  * Open the [Apple Developer homepage](https://developer.apple.com/account) and select [**Certificates, IDs & Profiles**](https://developer.apple.com/account/resources/certificates/list) \*\*\*\* (left menu)
  * Click on the [**Add button (+)**](https://developer.apple.com/account/resources/certificates/add)\*\*\*\*
  * Select **Apple Push Notification service SSL (Sandbox & Production)**
  * Click **Choose File** and select the CSR file.
  * Click **Continue** & **Download**.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-83122537bf1d99b7d7b6e7375a8c4e678ece03c9%2F16.gif?alt=media)

* Open Keychain Explorer, right-click on your Key Pair, and select **Import CA Reply -> From File.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-0a835f2ddf0584e36088052b1468698075595f40%2FSCR-20220518-fub.png?alt=media)

* Select downloaded earlier Apple's aps.cer and click **Import.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-945f959893d1266268e8a224f358d0105ab21e55%2FSCR-20220518-fuo.png?alt=media)

* Right-click on your previously imported Key Pair and click **Export -> Export Key Pair.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-dc80f65288511c1ccf077765f0cdb8ec0e9246ed%2FSCR-20220518-fxa.png?alt=media)

* Enter a password (you will use it for OneSignal later) and click **Export.**

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-e34336027d2c50ef336d9ae2dbeefded3b9d2363%2FSCR-20220518-fxn.png?alt=media)

* That's it, we generated our .p12 certificate that can be used for OneSignal Push Notifications.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-482644a9c29258acc8772730021d3c8c3fed7cc6%2FSCR-20220518-fy5.png?alt=media)
