# Source: https://docs.instabug.com/references/other/encrypt-user-defaults.md

# Encrypt User Defaults

This API allows you to set whether data stored by the SDK in user defaults should be encrypted or not. Values stored in user defaults are encrypted by default. Set this property to false to override this behavior and store values as plaintext instead.

{% hint style="info" %}
📘 App Launch Time

While the impact of the SDK on app launch time is minimal, setting this property to false will reduce it even further, at the tradeoff of storing some data locally as plaintext.
{% endhint %}

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.userDefaultsEncryptionEnabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
Luciq.userDefaultsEncryptionEnabled = NO;
```

{% endtab %}
{% endtabs %}
