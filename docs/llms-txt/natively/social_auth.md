# Source: https://docs.buildnatively.com/natively-platform/features/social_auth.md

# Social Auth

### What is Social Auth?

The Social Auth functionality enables Natively to manage third-party OAuth integrations directly within the application. To adhere to the policies of Google and Facebook, which prohibit developers from utilizing web authorization within WKWebView (iOS) and WebView (Android), Natively reroutes users to the official operating system browsers: Chrome (for Android) and Safari (for iOS). This measure is taken to circumvent potential security risks.

{% hint style="info" %}
Currently, Natively accommodates social authorization exclusively for Google, Facebook and KakaoTalk. However, the scope for adding more options in the future remains open. Please share your suggestions for additional integrations by submitting a request [here](https://ideas.buildnatively.com).
{% endhint %}

{% hint style="warning" %}
You're required to integrate [Sign In with Apple](https://docs.buildnatively.com/natively-platform/features/social_auth/sign-in-with-apple) feature if you have any other social authorization.
{% endhint %}

### How to set up Social Auth?

1. Turn on the [**Universal Links**](https://docs.buildnatively.com/natively-platform/features/deeplinks/universal-links) feature.
2. Enter your app domain - a domain that will be associated with your application (We need it to redirect users back to your app after authorization). For example, app.buildnatively.com.
3. Setup [Universal Links](https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks) **(This step is very important! Otherwise, Social Auth will not work.)**
4. **Make sure to enable** [**Associated Domain for iOS.**](https://docs.buildnatively.com/natively-platform/deeplinks/universal-links#add-associated-domains-feature-to-bundle-identifier)
5. Verify if Universal Links works. [iOS](https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks#verify-ios-domain-works) and [Android](https://docs.buildnatively.com/guides/setup-website-universal-links-deeplinks#verify-android-domain-works).
6. Turn on the **Social Auth** feature in the Natively app dashboard.
7. Provide the **Redirect URI** - the link where users will be sent after successfully authenticating with the OAuth provider (e.g., Google). This is where the authentication token will be handled by your web app.
   * Example for Bubble.io Apps: `yourprojectid.bubbleapps.io/api/1.1/oauth_redirect`
8. **(Optional)** Add **custom OAuth URLs** here. Any domain listed will be opened in a ephemeral session on iOS.
   * Result: This prevents iOS from using previously stored account data. Users will be required to manually enter their login credentials (email and password) every time they authenticate, even if they have previously logged in on that device.
   * Example for Google: `accounts.google.com/o/oauth2`
9. Rebuild your app
10. Test

### IMPORTANT!

You need to make sure your **redirect URL** for Facebook/Google has the same domain that you're using in Universal Links (This is needed to redirect the user back with an auth token in such url so that you can handle it in the web app)

For example, in Bubble you can turn on the generic URL in Facebook or Google plugins:

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FiAs0QEAwg42fUAJK7hgd%2FSCR-20230904-m02.png?alt=media&#x26;token=7ef143ae-285d-46e2-a249-2c8ade981abe" alt=""><figcaption></figcaption></figure>

and, of course, update it on Google and Facebook developer accounts (if needed).
