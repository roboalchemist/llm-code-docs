# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/integrate-luciq-on-react-native/one-code-apps-for-react-native.md

# One Code Apps For React Native

### Overview

The **One Code Apps** feature enables teams with **shared code base applications** to integrate multiple app variants under a single Luciq app token. This is ideal for organizations that release the same app to different brands, markets, or regions but want to consolidate stability and performance monitoring.

Instead of creating a separate Luciq application for each variant, you integrate all variants using **one Luciq app token** and identify each variant via the **bundle-id using the App variant API**.

### Integrating One Code Apps

{% stepper %}
{% step %}

#### Get Your Luciq App Token

From your Luciq dashboard, go to your application’s settings and copy the **app token** — this will be used for all variants.
{% endstep %}

{% step %}

#### Set the App Variant Name

Call the method before initializing the SDK:

{% code title="RN JavaScript" %}

```javascript
// Should be called before init
Luciq.setAppVariant("bundle-id/brand-name")
```

{% endcode %}
{% endstep %}
{% endstepper %}

{% hint style="success" %}
Best Practice

Use the **same variant name format** across all apps (e.g., bundle ID or a consistent naming convention) to make filtering easier in the dashboard.

We recommend using the unique part of the bundle-id. For example, if your bundle-id is: com.example.123245r454523452.MyApp.Uk, consider setting the app variant as **MyApp UK**.
{% endhint %}
