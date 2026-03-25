# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/codepush-for-react-native.md

# CodePush for React Native

### Initialization

To integrate Luciq with CodePush, pass the codePushVersion to allow you to change the reported versions.

{% code title="JavaScript" %}

```javascript
Luciq.init({
  token: '<User-App-token>',
  codePushVersion: '<Code-push-version>',
  invocationEvents: [<Invocation-events>],
  // ...  Other optional arguments here
});
```

{% endcode %}

Make sure to replace "User-App-token", "Code-push-version", and "Invocation-events" with your actual Luciq token, CodePush version, and invocation events.

### Native Initialization

To send the CodePush version from your native side, use the APIs for your platform:

{% tabs %}
{% tab title="iOS — Swift" %}

```swift
//This should be called before startingWithToken.

Luciq.setCodePushVersion("")
```

{% endtab %}

{% tab title="iOS — Objective-C" %}

```objc
//This should be called before startingWithToken.

[Luciq setCodePushVersion:@""];
```

{% endtab %}

{% tab title="Android — Java" %}

```java
new Luciq.Builder(application,"LUCIQ_TOKEN")
    .setCodePushVersion("")
    .build()
```

{% endtab %}

{% tab title="Android — Kotlin" %}

```kotlin
Luciq.Builder(application, "LUCIQ_TOKEN")
	.setCodePushVersion("")
	.build()
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}

### Character Limit

* The total length of the combined app version and codePushVersion should **not exceed 40 characters**. Exceeding the limit will result in trimming the excess characters.
* The combined versions will show as: "+codepush:". For example, if the app version is 1.0.0 (1), it would show as 1.0.0 (1)+codepush:1.0.6 (2) on the Luciq Dashboard.
  {% endhint %}
