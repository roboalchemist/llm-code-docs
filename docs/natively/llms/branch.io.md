# Source: https://docs.buildnatively.com/natively-platform/features/deeplinks/branch.io.md

# Branch.io

Branch deep linking technology guarantees reliable journeys to the app, even if the app is not installed, by directing users to the appropriate app store. With Branch, you can track deep link performance, optimize user journeys, and enhance security, allowing for a flawless user experience and effective marketing campaigns.

### Before you begin

[Sign-up for Branch](https://dashboard.branch.io/) - Credit card is needed within the first 30 days.

When you first create your account, you'll be directed to configure your account and default link behaviors.

### Branch.io settings

1. Go to 'Configuration' tab of the sidebar.
2. **Default URL:** Insert your app's URL

#### Configure Android redirects

1. Check the box ‘I have an Android App’
2. **Android URI Scheme:** enter your app's bundle ID in lowercase, followed by a colon and two forward slashes (://). For example, if your bundle ID is "com.example.natively," the URI scheme would be `com.example.natively://`
3. If your app is already published
   * Choose ‘Google Play Search’ and find the app in the searchbox
4. If your app is not yet published
   * Choose ‘Custom URL’
   * Paste the App’s URL
   * Paste the App’s bundle ID
5. Check the box ‘Enable App Links’
   * Paste the SHA256 Cert Fingerprints which can be find in Play Console > Setup > App signing > Upload key certificate

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F7MUQoh1XnGVX2brpfY6N%2FConfiguration-android-published-app.png?alt=media&#x26;token=c987fb25-38b6-43da-894c-b0349775ebbf" alt=""><figcaption></figcaption></figure>

#### Configure iOS redirects

1. Check the box ‘I have an iOS App’
2. iOS URI Scheme: enter your app's bundle ID in lowercase, followed by a colon and two forward slashes (://). For example, if your bundle ID is "com.example.natively," the URI scheme would be `com.example.natively://`
3. If your app is already published
   * Choose ‘Apple Store Search’ and find the app in the searchbox
4. If your app is not yet published
   * Choose ‘Custom URL’
   * Paste the App’s URL
   * Paste the App Store App ID
5. Check the box ‘Enable Universal Links’
   * **Bundle Identifiers:** insert the App’s bundle ID
   * **Apple App Prefix:** Can be found here: <https://developer.apple.com/account/resources/identifiers/bundleId/> \
     Choose the identifier of the app.
6. Check the box ‘Enable NativeLink’
   * Audience Rule: All iOS traffic

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FaNAJUmhQG3ilxae3r04J%2FConfiguration-ios-published-app.png?alt=media&#x26;token=8c02c213-f055-4bf3-aa3a-fe88a913f60f" alt=""><figcaption></figcaption></figure>

#### Link domain

1. Set up subdomain or your own domain
2. **Default Link Domain**: provide the default link domain (e.g. yourdomain.app.link)
3. **Alternate Link Domain**: provide the default link domain (e.g. yourdomain-alternate.app.link)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FwanfFB0DKQbJoeSYtwQR%2Flink-domains%20(1).png?alt=media&#x26;token=1a66dc62-20ef-4344-a6c0-7986909fd53c" alt=""><figcaption></figcaption></figure>

#### Save the changes!

### Natively settings

1. Go to <https://dashboard.branch.io/account-settings/profile> and copy the Branch key
2. Go to Natively dashboard > Features > Deeplinks > Branchio
   * Insert the Default link domain (Look at the 'Link domain' paragraph)
   * Insert the Alternate link domain from (Look at the 'Link domain' paragraph)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FFyjHFsJUkWz7W7A0MKCa%2Fbranchio-key.png?alt=media&#x26;token=d6d6f201-8850-41a1-8963-198c2e2e7ec6" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fil2cPB4GAmWesMsJcOxy%2Fnatively-settings.png?alt=media&#x26;token=f25aee92-5e61-4e48-9bd6-607b896c1b8a" alt=""><figcaption></figcaption></figure>

#### Save the changes and rebuild your app

**An example of a deep link:**

<https://yourdomain.app.link/?$deeplink\\_path=https://yourdomain.io/test/reset\\_pw?test><br>

#### A scheme of a deep link:

#### &#x20;{default\_link\_domain}/?$deeplink\_path={url}

### &#x20;Important

Developers are required to fill out Google’s updated Data Safety section in the Google Play Console.\
Without an approval in the Data Safety section, your new app submission or app update may be rejected.\
\
Detailed information on completing the Google Play Store questions when submitting your app for release or update: <https://help.branch.io/using-branch/docs/answering-the-google-play-store-privacy-questions>\ <br>
