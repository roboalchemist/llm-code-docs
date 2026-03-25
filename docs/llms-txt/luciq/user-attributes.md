# Source: https://docs.luciq.ai/references/user-identification-data/user-attributes.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/user-identification/user-attributes.md

# User Attributes

You can assign custom attributes to your users and they will show up on your Luciq dashboard with each report. These attributes can later be used to filter reports in your dashboard.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FjJXWNJgWg1dC34TIVl1q%2Fimage.png?alt=media&#x26;token=a785b782-e4f1-4080-9ac6-670018afa119" alt=""><figcaption></figcaption></figure>

To add a new user attribute, use the following method.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setUserAttribute("True", withKey: "Logged in")
Luciq.setUserAttribute("False", withKey: "Completed IAP")
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setUserAttribute:@"True" withKey:@"Logged in"];
[Luciq setUserAttribute:@"18" withKey:@"Age"];
```

{% endcode %}
{% endtab %}
{% endtabs %}

You can also retrieve or remove the current value of a certain user attribute.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let loggedIn = Luciq.userAttribute(forKey: "Logged in")
Luciq.removeUserAttribute(forKey: "Logged in")
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSString *loggedIn = [Luciq userAttributeForKey:@"Logged in"];
[Luciq removeUserAttributeForKey:@"Logged in"];
```

{% endcode %}
{% endtab %}
{% endtabs %}

Or retrieve all user attributes.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let allUserAttributes = Luciq.userAttributes()
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSDictionary *allUserAttributes = [Luciq userAttributes];
```

{% endcode %}
{% endtab %}
{% endtabs %}
