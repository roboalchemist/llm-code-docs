# Source: https://docs.instabug.com/references/report-data/tags.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/custom-settings/user-identification/tags.md

# Tags

You can add custom tags to your bug and crash reports. These tags can later be used to filter reports or set custom rules from your dashboard.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FSx5nbz5JcahUaWbYB3NN%2Fimage.png?alt=media&#x26;token=ab2d98f5-00f7-4364-a25b-f2f8e0cb6b8f" alt=""><figcaption></figcaption></figure>

The example below demonstrates how to add tags to a report.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.appendTags(["Design", "Flow"])
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq appendTags:@[@"Design", @"Flow"]];
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}

### Adding tags before sending reports

Sometimes it's useful to be able to add a tag to a bug report before it's been sent. In these cases, the perfect solution would be use the event handlers of the bug reporting class. You can find more details [here](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-bug-reporting/bug-reporting-callbacks).
{% endhint %}

You can also get all the currently set tags as follows.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let tags = Luciq.getTags()
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSString *tags = [Luciq getTags];
```

{% endcode %}
{% endtab %}
{% endtabs %}

Last, you can reset all the tags.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.resetTags()
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq resetTags];
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Managing Tags

If you'd like to remove a particular tag from your dashboard to prevent it from appearing again when entering a new tag manually, you can do so by navigating to the tags page under the settings options and remove the tag. You can also edit and rename the tag.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FVOj54ZXwCZG8MexhSYeY%2Fimage.png?alt=media&#x26;token=7be4294e-85dd-4032-89a2-f1c14fd2a98e" alt=""><figcaption></figcaption></figure>
