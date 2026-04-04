# Source: https://posthog.com/docs/feature-flags/testing.md

# Testing your feature flag - Docs

Once you've written your code, it's a good idea to test that each variant behaves as you'd expect. There are 3 ways you can do this:

## Method 1: Assign a user a specific flag value

For boolean flags, you can roll out the flag to a specific user. For multivariate flags, you can assign a user to a specific variant by **adding an optional override** to your [release conditions](/docs/feature-flags/creating-feature-flags.md#release-conditions).

To do this:

1.  Go to your feature flag.

2.  Ensure the feature flag is enabled by checking the "Enable feature flag" box.

3.  Add a new condition set with the condition to `email = your_email@domain.com`. Set the rollout percentage for this set to 100%.

    -   in cases where `email` is not available (such as when your users are logged out), you can use a parameter like `utm_source` and append `?utm_source=your_variant_name` to your URL.

4.  If it is a multivariant flag, set the optional override to the variant you want to assign these users to.
5.  Click "Save".

## Method 2: Use `posthog.featureFlags.overrideFeatureFlags()`

> **Note:** The `posthog.featureFlags.overrideFeatureFlags()` method is only available in the [JavaScript web](/docs/libraries/js.md) and [React Native](/docs/libraries/react-native.md) SDKs.

You can add a manual override directly in your code by calling `posthog.featureFlags.overrideFeatureFlags()`:

JavaScript

PostHog AI

```javascript
posthog.featureFlags.overrideFeatureFlags( {
    flags: {
        'your_boolean_feature_flag_key': true // for boolean feature flags
        'your_multivariate_feature_flag_key': 'your_variant_name', // for multivariate feature flags
    }
})
```

## Method 3: Use the PostHog toolbar

> **Note:** The [PostHog toolbar](/docs/toolbar.md) is only available for the [JavaScript web SDK](/docs/libraries/js.md).

The toolbar enables you to test your feature flags. You can enable, disable, or override your feature flags, and then view how your website or app changes with the new feature flags values.

To do this, click on the "Feature Flags" button in the toolbar, search for any feature flag, and click on the toggles to change its value.

Overriding feature flags will only affect *your* browser. You may also need to refresh the page to see how your change affect your website. It does not affect feature flags evaluation for your backend.

You can also view feature flags as another user by clicking the person icon and entering their distinct ID. This loads the flag values that user would see, displaying "Viewing as: \[distinct\_id\]" at the bottom of the panel. Click **Clear** to return to your own flags.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better