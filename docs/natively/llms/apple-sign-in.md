# Source: https://docs.buildnatively.com/guides/integration/apple-sign-in.md

# Apple Sign In

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

{% hint style="warning" %}
Sign In with Apple should be only displayed on iOS devices otherwise, it will not work (for Android or Web)&#x20;
{% endhint %}

### 🧋 Bubble.io Plugin

#### Natively - Apple Sign In

#### Events:

* Apple Sign In Success
* Apple Sign In Failed

#### States:

* Email
* Given Name
* Family Name
* Error
* Subject - unique identifier based on your app + user iCloud (it's unique)
* Initial Sign In - mean that user signin/signup for the first time to your app

#### Actions:

* Sign In with Apple

<details>

<summary>How to set up Sign In with Apple in Bubble?</summary>

1. Add **Natively - Apple Sign In** element on the page.

2. Create a "Sign In with Apple" button (you can use a simple image or HTML/CSS). Find some examples [here](https://appleid.apple.com/signinwithapple/button).<br>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FkKIwTlbsfB2zWQZlGeJx%2Fimage.png?alt=media&#x26;token=98dd4cdd-ca44-4091-93f2-33f185ef89d5" alt=""><figcaption></figcaption></figure>

3. Add "Apple Sign In Success" event and the following actions<br>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FO8TQ8PWERGs5LcXd4wyg%2FSCR-20230905-sjd.png?alt=media&#x26;token=5e616807-d799-4efe-bf74-71a1aeaa62e7" alt=""><figcaption></figcaption></figure>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F38SrYFkkwpaeYAI8E6vI%2FSCR-20230905-sjk.png?alt=media&#x26;token=b6b27a67-9ca2-4c0a-8860-0d3dbda93627" alt=""><figcaption></figcaption></figure>

</details>

###

### IMPORTANT for Bubble Plugin and JS SDK devs.

{% hint style="info" %}
The Subject assigned to a user will persist consistently with each login, irrespective of their choice to conceal their email address or not. This value remains unchanged even when they switch to different iOS devices. This consistency is due to the fact that the Subject is intrinsically linked to the individual's iCloud account, ensuring a seamless user experience across different devices.
{% endhint %}

{% hint style="danger" %}
Apple allows users to hide their email addresses when logging into an app. If this option is selected, Apple generates a unique forwarding email address that relays any received emails to the user's actual email address, which will be disclosed to you. Note that this forwarding email address is only revealed during the user's initial login to your app. In subsequent logins, this information will not be accessible, leaving the email field vacant.

Alternatively, if a user decides to disclose their email address, it will be consistently available for you to utilize each time they log in.
{% endhint %}

{% hint style="info" %}
During the testing phase, you might wish to reset your Apple ID for your application to mimic a first-time sign-up experience once more. To accomplish this, navigate to your iOS Settings and tap on your name displayed at the top. Proceed to 'Password & Security' followed by 'Apps Using Your Apple ID'. Find and select your application in the list. You can choose "Stop Using Apple ID" at this stage, effectively resetting the Apple ID association with that specific app. Consequently, all fields should be present during your next Apple sign-in, offering a fresh start as though it's an initial login attempt.
{% endhint %}

### 🛠 JavaScript SDK

#### NativelyAppleSignInService

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const appleService = new NativelyAppleSignInService()
const apple_signin_callback = function(resp) {
        console.log(resp);
        if (resp.status) {
            console.log(resp.email);
            console.log(resp.subject); // unique identifier based on your app + user iCloud (it's unique)
            console.log(resp.givenname);
            console.log(resp.familyname);
            console.log(resp.initial); // mean that user signin/signup for the first time to your app
        } else {
            console.log(resp.message);
        }
};
appleService.signin(apple_signin_callback);
```

{% endcode %}
