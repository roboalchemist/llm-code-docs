# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/custom-settings/setting-custom-data.md

# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/custom-settings/setting-custom-data.md

# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/custom-settings/setting-custom-data.md

# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/identify-users/setting-custom-data.md

# Setting Custom Data

### User Attributes

You can assign custom attributes to your users and they will show up on your Luciq dashboard with each report. These attributes can later be used to filter reports in your dashboard.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FCPf0eDxYMtTAKwBnQ6XH%2Fimage.png?alt=media&#x26;token=9034124e-c72c-4ba5-b1c0-e4f27ea35e69" alt=""><figcaption></figcaption></figure>

To add a new user attribute use the following method.

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
Luciq.setUserAttribute("Age", "18");
Luciq.setUserAttribute("Logged", "True");
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Disclaimers:

* Each Bug or Crash Report could have up to 100 user attributes only.
* The character limit for the Keys and Values is 90 characters each.
  {% endhint %}

You can also retrieve the current value of a certain user attribute, or retrieve all user attributes.

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
// Getting attribute
const attribute = await Luciq.getUserAttribute('Logged in');

// Loading all attributes
const attributes = await Luciq.getAllUserAttributes();
```

{% endcode %}
{% endtab %}
{% endtabs %}

Or remove the current value of a certain user attribute

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
Luciq.removeUserAttribute("Completed IAP");
```

{% endcode %}
{% endtab %}
{% endtabs %}

### User Events

You can log custom user events throughout your application. Custom events are automatically included with each report.

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
Luciq.logUserEventWithName("OnFeedbackButtonClicked");
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Tags

You can add custom tags to your bug and crash reports. These tags can later be used to filter reports or set custom rules from your dashboard.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FM1nZoDPT3QZdXtQuVECl%2Fimage.png?alt=media&#x26;token=55911436-f6b4-4f64-b545-44a794bd1b10" alt=""><figcaption></figcaption></figure>

The example below demonstrates how to add tags to a report.

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
Luciq.appendTags(["Tag 1", "Tag 2"]);
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}

### Adding tags before sending reports

Sometimes it's useful to be able to add a tag to a bug report before it's been sent. In these cases, the perfect solution would be use the event handlers of the bug reporting class.
{% endhint %}

You can also get all the currently set tags as follows.

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
const tags = await Luciq.getTags();
```

{% endcode %}
{% endtab %}
{% endtabs %}

Last, you can reset all the tags.

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
Luciq.resetTags();
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Managing Tags

If you'd like to remove a particular tag from your dashboard to prevent it from appearing again when entering a new tag manually, you can do so by navigating to the tags page under the settings options and remove the tag. You can also edit and rename the tag.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FNuikjhKNRfi4pRiBBwnT%2Fimage.png?alt=media&#x26;token=d1c71fe2-f5e1-4fd0-8d2d-245b6cc66f6b" alt=""><figcaption></figcaption></figure>

***

### Feature Flags

In certain scenarios, you might find that you're rolling out different experiments to different users, where your user base would see different features depending on what's enabled for them. In scenarios such as these, you'll want to keep track of the enabled experiments for each user and even filter by them.

**Notes:**

1. **Feature Flag Naming**: Each feature flag name should not exceed 70 characters and each variant name should not exceed 70 characters. Otherwise, they will get ignored by the SDK. Note that feature flag names are case-insensitive.
2. **Feature Flag Persistence**: Feature flag persist beyond individual sessions and are not automatically removed at the end of a session. Additionally, calling the logOut function does not impact the existence of the feature flag. The feature flag is only removed when you call the removing method or the clearing method.
3. The amount of feature flags sent in a session is 200 with maximum of 1 variant per a multivariate feature flag. For example, a feature flag that has 3 variants sent within 1 session will only be sent to our backend as the last variant, and not all 3.

For more information on feature flags, visit Feature Flags.

#### Adding Feature Flags

#### Boolean Feature Flags - Example Usage

Below is an example of where in your code you would use feature flag. In this example, you are experimenting with feature logic that controls whether or not the user has a Dark Mode toggle available.

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
const boolFeatureFlag: FeatureFlag = {name: 'Boolean Feature Flag'}
Luciq.addFeatureFlags([boolFeatureFlag]);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Multivariant Feature Flags - Example Usage

Below is an example of where in your code you would use feature flag with multiple variants. In this example, you are experimenting with feature logic that controls multiple versions of a specific feature.

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
const featureFlag: FeatureFlag = {name: 'Boolean Feature Flag'}
Luciq.addFeatureFlags([featureFlag]);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Removing Feature Flags

If your feature flag is concluded or you would like to simply remove it, you can use this method:

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
Luciq.removeFeatureFLag('FeatureFlag'); // remove single key
Luciq.removeFeatureFlags(['featureFlagA', 'featureFlagB']); // remove multiple feature flags at once
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Clearing Feature Flags

You can use the below method to clear all the Feature Flags from your reports:

{% tabs %}
{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
Luciq.removeAllFeatureFlags();
```

{% endcode %}
{% endtab %}
{% endtabs %}
