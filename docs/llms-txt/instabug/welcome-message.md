# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/custom-settings/sdk-customization/welcome-message.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/custom-settings/sdk-customization/welcome-message.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/custom-settings/sdk-customization/welcome-message.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/sdk-customizations/welcome-message.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/custom-settings/sdk-customization/welcome-message.md

# Welcome Message

### Setting the welcome message mode

By default, a welcome message that explains how to [show Luciq](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-bug-reporting/showing-luciq) will be shown to your app users within 10 seconds of starting their first session after the SDK is integrated. The welcome mode can be set to live, beta, or disabled using the method below. The default welcome mode is set to live.

The popups that appear follow the [color theme](https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/sdk-customization/ui-color-and-theme) and [primary color](https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/sdk-customization/ui-color-and-theme) that you set for the SDK.

You can also edit the content of the message using the method and keys found in the [Locale](https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/sdk-customization/sdk-locale) page.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.welcomeMessageMode = LCQWelcomeMessageMode.beta // For beta testers
Luciq.welcomeMessageMode = LCQWelcomeMessageMode.live // For live users
Luciq.welcomeMessageMode = LCQWelcomeMessageMode.disabled // Disable welcome message
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setWelcomeMessageMode:LCQWelcomeMessageModeBeta]; // For beta testers
[Luciq setWelcomeMessageMode:LCQWelcomeMessageModeLive]; // For live users
[Luciq setWelcomeMessageMode:LCQWelcomeMessageModeDisabled]; // Disable welcome message
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Showing the welcome message manually

Instead of showing the welcome message automatically, you can manually show the welcome message in either live or beta mode using the following method.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.showWelcomeMessage(with: LCQWelcomeMessageMode.beta) // For beta testers
Luciq.showWelcomeMessage(with: LCQWelcomeMessageMode.live) // For live users
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Instabug showWelcomeMessageWithMode:IBGWelcomeMessageModeBeta]; // For beta testers
[Instabug showWelcomeMessageWithMode:IBGWelcomeMessageModeLive]; // For live users
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}

### Invocation Method Set to None?

If your [invocation method](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-bug-reporting/showing-luciq) is set to "none", the welcome message will not appear to your users.
{% endhint %}

### Live welcome message

This mode is primarily aimed at users of your production builds, or live apps.

A single popup appears to your users with instructions on how to show Luciq depending on the invocation method you're using.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2F7tlSbX7E0KmDWN7Th1I1%2Fimage.png?alt=media&#x26;token=d022c01a-a074-43ce-8d84-e2a06bbaf1fe" alt=""><figcaption><p><br><em>Examples of the welcome message that appears to users in live apps depending on the invocation method set.</em></p></figcaption></figure>

### Beta welcome message

This mode is primarily aimed at beta testers of your development builds, or beta apps.

A three-step on-boarding flow appears to your testers. First, your testers see a welcome message customized for beta testers. The second screen explains how to show Luciq depending on the invocation method you're using. The third and last screen reminds your testers to use the latest version of your application in order to access all your latest fixes and features.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FqcJoTjgiGVhwU6w5W7lV%2Fimage.png?alt=media&#x26;token=d2e763bd-2771-4d20-a15e-74efe017bef7" alt=""><figcaption><p><br><em>An example of the three-step on-boarding flow that appears to users in beta apps.</em></p></figcaption></figure>
