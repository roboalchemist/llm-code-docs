# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/setup-app-ratings-and-reviews.md

# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/setup-app-ratings-and-reviews.md

# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-app-ratings-and-reviews.md

# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/setup-app-ratings-and-reviews.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-app-ratings-and-reviews.md

# Setup App Ratings & Reviews

#### Custom App Rating Prompt

If you’re using a custom app rating prompt, you have to make sure to call the below API once the user clicks on the CTA that redirects to the store.

{% tabs %}
{% tab title="Swift" %}

```swift
Luciq.willRedirectToAppStore()
```

{% endtab %}

{% tab title="Objective-C" %}

```objective-c
[Luciq willRedirectToAppStore];
```

{% endtab %}
{% endtabs %}

When the above API is used, we will be able to detect the suspected sessions for the reviews submitted through the custom prompt. This will give you valuable insights into what happened during the session.
