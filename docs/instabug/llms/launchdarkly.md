# Source: https://docs.instabug.com/product-guides-and-integrations/integrations/launchdarkly.md

# Launchdarkly

### Integrate Luciq with Launchdarkly

With the integration, you will be able to monitor and control your feature flags from within Luciq in addition to various automations that can be set up on feature flags.

### SDK Setup

Whenever you use a feature flag in Launchdarkly, make sure to call Luciq’s addFeatureFlag API, explained here. This ensures that any feature flags in any session are correctly counted and monitored from both within Luciq and Launchdarkly.

Example of the code snippet

{% code title="Kotlin" %}

```kotlin
LDClient.init(application, ldConfig, context)

// Boolean flag
val BOOLEAN_FLAG_KEY = "sample-flag"

val featureEnabled = LDClient.get().boolVariation(BOOLEAN_FLAG_KEY, false)
if (featureEnabled) {
    Luciq.addFeatureFlag(LCQFeatureFlag(BOOLEAN_FLAG_KEY))
    // logic to execute if flag enabled
} else {
    Luciq.removeFeatureFlag(BOOLEAN_FLAG_KEY)
}

// Multivariats flag
val STRING_FLAG_KEY = "sample-string-flag"

val stringFlag = LDClient.get().stringVariation(STRING_FLAG_KEY, null)

if (stringFlag != null) {
    Luciq.addFeatureFlag(LCQFeatureFlag(STRING_FLAG_KEY, stringFlag))
} else {
    Luciq.removeFeatureFlag(STRING_FLAG_KEY)
}
```

{% endcode %}

Another approach would be using the following snippet which allows Luciq to listen to all feature flags coming of Launchdarkly’s client. However, this may result in inaccurate data if you are not using the same enabled feature flags in you code.

{% code title="Kotlin" %}

```kotlin
LDClient.init(application, ldConfig, context)
// Get all mobile enabled feature flags
for ((key, value) in LDClient.get().allFlags()) {
    if (value.type == LDValueType.BOOLEAN && value.booleanValue()) {
        Luciq.addFeatureFlag(LCQFeatureFlag(key))
    } else if (value.type == LDValueType.STRING || value.type == LDValueType.NUMBER) {
        Luciq.addFeatureFlag(LCQFeatureFlag(key, value.toString().replace("\"", "")))
    }
}
```

{% endcode %}

## Dashboard Setup

Within the Settings tab, you will find Launchdarkly integration in the list of integrations available.

{% stepper %}
{% step %}

#### Add Launchdarkly integration token

Get your LaunchDarkly integration token and add it.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FmMnmU3bUT3tQri8wUKRl%2Fimage.png?alt=media&#x26;token=96cba532-4e5f-445c-9a4b-182af29a7ebd" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Select project and environment

Select your project and environment that you want to control feature flags in.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F9FIZeBHEtQy3amYRFpJk%2Fimage.png?alt=media&#x26;token=a60726ca-e52e-4a0c-a54c-969bf3694d7e" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Test your integration

At this point, we just need to test your integration so that we're sure everything is working smoothly.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FTm4FFu12YX1PxEN49KRY%2Fimage.png?alt=media&#x26;token=65b71c73-9553-4457-b3b5-23cfdfaf22d4" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Name and finish

All done! Your integration is now set up, just give your integration a name and you're ready to go.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FRxG5grCcYMmO9ax9yiOw%2Fimage.png?alt=media&#x26;token=2727b424-e1bb-4658-954c-904d13099421" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### Control Feature Flags

After the setup, you can now create rules on a specific feature flag to turn it off whenever it passes a certain threshold of a specific metric.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F2kVmGqi0r5zTfB2XRSIi%2Fimage.png?alt=media&#x26;token=f05083d0-8586-40df-a296-b8b2974f416b" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Notes:

* To use the action of Turn off using Launchdarkly, you must add a condition of feature flag names.
* The action of Turn off using launchdarkly sends a value of OFF to Launchdarkly for the specific feature flag that passed the threshold added.
  {% endhint %}

### Get Launchdarkly API token

{% stepper %}
{% step %}
Go to Settings → Authorization page: <https://app.launchdarkly.com/settings/authorization>

From Access Tokens section, click create token.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F4rwuGaG4XkOGPXhfhLgL%2Fimage.png?alt=media&#x26;token=cda22923-b224-43e1-b33e-61366e4b6a42" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
Enter the integration name, make sure to select Writer role, and select API version to 20240415, then Save.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F0pX4j3DPUXjeERwbbJ17%2Fimage.png?alt=media&#x26;token=f0058901-184f-44ad-9f03-642bd9b833e3" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
Copy the generated token before leaving the page, to use it in integration step.
{% endstep %}
{% endstepper %}
