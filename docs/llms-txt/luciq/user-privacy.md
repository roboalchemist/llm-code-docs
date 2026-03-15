# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/privacy-settings/user-privacy.md

# User Privacy

We understand user privacy is of key to you, specially having our SDK on production. In this guide, we will show you how to mark views containing sensitive information as private. By doing so, these views will be masked on screenshots captured to your users' devices (before being sent to Luciq servers) and automatically appear with a black overlay (over whole screen, labels, texts or media) in any screenshot on Luciq's dashboard to protect your user’s sensitive data.

{% hint style="info" %}
Repro steps screenshots are disabled by default on crash reporting.
{% endhint %}

1. Identify the View: Determine which view in your app contains sensitive information that should be kept private. For example, a payment details screen or a user's personal profile.
2. Identify Sensitive Information: Determine which information on each view that you need to hide. Do you want to hide the whole screen? text fields? media? labels?
3. Deciding on the content of the screenshots\
   Luciq provides you with multiple ways to easily protect your users sensitive data, whether you want to hide the content of a whole specific screen or certain text fields, labels and media, we got you covered!

**Auto masking**\
You can automatically mask sensitive data when screenshots are captured, while protecting the user's privacy by default using auto masking feature. Keep in mind that this feature affects both Bug and Crash Reporting.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FKKe7si3o5DRzgsyNjore%2Fimage.png?alt=media&#x26;token=df199eec-ca16-492a-9071-7e9d9867031e" alt=""><figcaption></figcaption></figure>

*Masking text inputs*\
You can use this to hide any text fields captured on all your screenshots

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setAutoMaskScreenshots([.textInputs])
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setAutoMaskScreenshots: LCQAutoMaskScreenshotOptionTextInputs];
```

{% endcode %}
{% endtab %}
{% endtabs %}

*Masking labels*\
This can be utilized to hide text labels including buttons and titles

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setAutoMaskScreenshots([.labels])
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setAutoMaskScreenshots: LCQAutoMaskScreenshotOptionLabels];
```

{% endcode %}
{% endtab %}
{% endtabs %}

*Masking images and videos*\
If your users might be sharing private images or videos on the app, in which you wouldn't want access to, you can utilize the following property to hide it.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setAutoMaskScreenshots([.media])
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setAutoMaskScreenshots: LCQAutoMaskScreenshotOptionMedia];
```

{% endcode %}
{% endtab %}
{% endtabs %}

*Masking nothing*\
You can also disable auto-masking all together if you need using the following property

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setAutoMaskScreenshots([.maskNothing])
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setAutoMaskScreenshots: LCQAutoMaskScreenshotOptionMaskNothing];
```

{% endcode %}
{% endtab %}
{% endtabs %}

*Mix and match*\
You can combine different masking options according to your needs. For example, if you want to mask both text Inputs and labels, you can use the following API

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setAutoMaskScreenshots([.textInputs, .labels])
```

{% endcode %}
{% endtab %}
{% endtabs %}

**Hide a whole screen**\
In case you need to add an extra layer of privacy and prevent sensitive information from being captured in screenshots. This property will hide the overall screen when the view appears in a screenshot

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
view.Luciq_privateView = true
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
view.Luciq_privateView = YES;
```

{% endcode %}
{% endtab %}
{% endtabs %}

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FKajNy6zsykAHGgd2MNgx%2Fimage.png?alt=media&#x26;token=076cb18d-4f59-43d3-b175-1820f5de3a83" alt=""><figcaption><p><em>Example of private view</em></p></figcaption></figure>
