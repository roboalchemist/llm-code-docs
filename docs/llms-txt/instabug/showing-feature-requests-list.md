# Source: https://docs.instabug.com/android/set-up-luciq-for-android/in-app-feature-requests/showing-feature-requests-list.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-feature-requests/showing-feature-requests-list.md

# Showing feature requests list

The following method can be used to display the Feature Requests page to your users. Once you display the page, your users can submit new feature requests, add comments, and up-vote other feature requests.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
FeatureRequests.show()
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[LCQFeatureRequests show];
```

{% endcode %}
{% endtab %}
{% endtabs %}

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2Fffkbq2EeOtjdcHjsuAKH%2Fimage.png?alt=media&#x26;token=133ea12a-9943-45f3-a6c0-5a0b515880df" alt=""><figcaption><p><em>This is what the list of in-app feature requests looks like.</em></p></figcaption></figure>

{% hint style="info" %}

### When to Show Feature Requests

In order to get the feature requests page to show reliably, the above API should be linked with an action inside your application, such as the press of a button.
{% endhint %}
