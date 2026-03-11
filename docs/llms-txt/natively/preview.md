# Source: https://docs.buildnatively.com/natively-platform/preview.md

# Preview

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FWcDuaA8m1Jw0pCfOudVF%2FFile%20(1).jpg?alt=media&#x26;token=c958b255-308a-49b3-b1db-3d46031fb0ae" alt="" width="188"><figcaption></figcaption></figure>

* Install the Natively Preview app from [App Store](https://apps.apple.com/us/app/natively-preview/id1626045691) and [Google Play](https://play.google.com/store/apps/details?id=com.ncnp.app)
* Open your app details screen, and click the App you want to run in Preview.
* **(Important)** If you are using the [Push Notifications](https://docs.buildnatively.com/natively-platform/features/notifications/onesignal-notifications) feature, set "preview" in [**mode (headers)**](https://docs.buildnatively.com/guides/integration/how-to-get-started#mode-headers-optional) if you're using the bubble plugin or [set it in JS SDK](https://docs.buildnatively.com/guides/integration/how-to-get-started#javascript-sdk)

{% hint style="danger" %}
**The following** native features **will not work** in the Natively Preview app:\
\- Background Location\
\- In-App Purchases\
\- Deeplinks\
\- Facebook/AppsFlyer analytics\
\- Apple's HealthKit\
\- Social Auth\
\- Admob
{% endhint %}

{% hint style="danger" %}
The appearance settings you have configured **will not be reflected** in the Natively preview app.
{% endhint %}

{% hint style="warning" %}
Natively Preview app operates using a pre-configured sandbox environment. Consequently, devices running the Preview app will not appear as new subscriptions in your personal OneSignal dashboard. To test your specific OneSignal integration and see active subscriptions, you must generate your own build of your application.
{% endhint %}
