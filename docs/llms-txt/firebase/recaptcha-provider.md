# Source: https://firebase.google.com/docs/app-check/web/recaptcha-provider.md.txt

This page shows you how to enableApp Checkin a web app, using the built-in reCAPTCHA v3 provider. When you enableApp Check, you help ensure that only your app can access your project's Firebase resources. See an[Overview](https://firebase.google.com/docs/app-check)of this feature.

<br />

| App Checkalso supports[reCAPTCHA Enterprise](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider), which has more security features and fraud signals than reCAPTCHA v3. reCAPTCHA Enterprise gives you up to 10,000 assessments per month at no cost.
|
| <br />
|
| **You should use reCAPTCHA Enterprise for new integrations, and we strongly recommend that developers of apps using reCAPTCHA v3 upgrade when possible.**
|
| To learn the differences between reCAPTCHA v3 and reCAPTCHA Enterprise, see the[comparison of features](https://cloud.google.com/recaptcha-enterprise/docs/compare-versions).

<br />

Note that reCAPTCHA v3 is invisible to users. The reCAPTCHA v3 provider will not require users to solve a challenge at any time. See the[reCAPTCHA v3 documentation](https://developers.google.com/recaptcha/docs/v3).

If you want to useApp Checkwith your own custom provider, see[Implement a customApp Checkprovider](https://firebase.google.com/docs/app-check/web/custom-provider).

## 1. Set up your Firebase project

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup)if you haven't already done so.

2. [Register your site for reCAPTCHA v3](https://www.google.com/recaptcha/admin/create)and get your reCAPTCHA v3 site key and secret key.

3. Register your apps to useApp Checkwith the reCAPTCHA provider in the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole. You will need to provide the*secret key*you got in the previous step.

   You usually need to register all of your project's apps, because once you enable enforcement for a Firebase product, only registered apps will be able to access the product's backend resources.
4. <br />

   <br />

   **Optional** : In the app registration settings, set a custom time-to-live (TTL) forApp Checktokens issued by the provider. You can set the TTL to any value between 30 minutes and 7 days. When changing this value, be aware of the following tradeoffs:
   - Security: Shorter TTLs provide stronger security, because it reduces the window in which a leaked or intercepted token can be abused by an attacker.
   - Performance: Shorter TTLs mean your app will perform attestation more frequently. Because the app attestation process adds latency to network requests every time it's performed, a short TTL can impact the performance of your app.
   - Quota and cost: Shorter TTLs and frequent re-attestation deplete your quota faster, and for paid services, potentially cost more. See[Quotas \& limits](https://firebase.google.com/docs/app-check#quotas_limits).

   The default TTL of**1 day** is reasonable for most apps. Note that theApp Checklibrary refreshes tokens at approximately half the TTL duration.

   <br />

   <br />

### Configure advanced settings (optional)

When a user visits your web app, reCAPTCHA v3 evaluates the level of risk the user interaction poses, and returns a score between 0.0 and 1.0; 1.0 is very likely a good interaction, 0.0 is very likely a bot.App Checklets you configure an**app risk**threshold so you can adjust your tolerance for this risk.

For most use cases, the default threshold value of**0.5** is recommended. If your use case requires adjustment, it can be configured in the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole for each of your web apps.

#### Details

App Checkuses your configured app risk threshold as the minimum reCAPTCHA v3 score required for a user interaction to be deemed legitimate. All reCAPTCHA v3 scores strictly less than your configured app risk threshold will be rejected. When adjusting your app risk threshold, be aware of the following:

- To monitor the reCAPTCHA v3 score distribution for your web app, visit the[reCAPTCHA Admin console](https://www.google.com/recaptcha/admin)and select the site corresponding to your web app.
- If you have**low** app risk tolerance,**move the slider to the left**to increase the app risk threshold.

  - A value of 1.0 is not recommended, as this setting can also potentially deny access for legitimate users who do not meet this high trust threshold.

  | **Warning:** Before increasing the app risk threshold, you should consider temporarily unenforcing App Check protection for all currently enforced services to avoid disrupting your legitimate users. You should[monitor App Check request metrics](https://firebase.google.com/docs/app-check/monitor-metrics)to verify that traffic has not been disrupted before resuming enforcement.
- If you have**high** app risk tolerance,**move the slider to the right**to decrease the app risk threshold.

  - A value of 0.0 is not recommended, as this setting disables abuse protection.

Consult the[reCAPTCHA v3 documentation](https://developers.google.com/recaptcha/docs/v3)for additional details.

## 2. Add theApp Checklibrary to your app

[Add Firebase to your web app](https://firebase.google.com/docs/web/setup)if you haven't already. Be sure to import theApp Checklibrary.

## 3. InitializeApp Check

Add the following initialization code to your application, before you access any Firebase services. You will need to pass your reCAPTCHA*site key* , which you created in the reCAPTCHA console, to`activate()`.  

### Web

```javascript
import { initializeApp } from "firebase/app";
import { initializeAppCheck, ReCaptchaV3Provider } from "firebase/app-check";

const app = initializeApp({
  // Your firebase configuration object
});

// Pass your reCAPTCHA v3 site key (public key) to activate(). Make sure this
// key is the counterpart to the secret key you set in the Firebase console.
const appCheck = initializeAppCheck(app, {
  provider: new ReCaptchaV3Provider('abcdefghijklmnopqrstuvwxy-1234567890abcd'),

  // Optional argument. If true, the SDK automatically refreshes App Check
  // tokens as needed.
  isTokenAutoRefreshEnabled: true
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/appcheck-next/index/appcheck_initialize.js#L8-L23
```

### Web

```javascript
firebase.initializeApp({
  // Your firebase configuration object
});

const appCheck = firebase.appCheck();
// Pass your reCAPTCHA v3 site key (public key) to activate(). Make sure this
// key is the counterpart to the secret key you set in the Firebase console.
appCheck.activate(
  'abcdefghijklmnopqrstuvwxy-1234567890abcd',

  // Optional argument. If true, the SDK automatically refreshes App Check
  // tokens as needed.
  true);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/appcheck/index.js#L6-L18
```
| **Note:** The SDK will not automatically refresh App Check tokens by default. That functionality must be explicitly enabled by providing`true`as a second argument to`activate()`or by calling`firebase.appCheck().setTokenAutoRefreshEnabled(true)`. For more, see[the App Check reference docs](https://firebase.google.com/docs/reference/js/firebase.appcheck.AppCheck).

## Next steps

Once theApp Checklibrary is installed in your app, deploy it.

The updated client app will begin sendingApp Checktokens along with every request it makes to Firebase, but Firebase products will not require the tokens to be valid until you enable enforcement in theApp Checksection of the Firebase console.

### Monitor metrics and enable enforcement

Before you enable enforcement, however, you should make sure that doing so won't disrupt your existing legitimate users. On the other hand, if you're seeing suspicious use of your app resources, you might want to enable enforcement sooner.

To help make this decision, you can look atApp Checkmetrics for the services you use:

- [MonitorApp Checkrequest metrics](https://firebase.google.com/docs/app-check/monitor-metrics)forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [MonitorApp Checkrequest metrics forCloud Functions](https://firebase.google.com/docs/app-check/monitor-functions-metrics).

### EnableApp Checkenforcement

When you understand howApp Checkwill affect your users and you're ready to proceed, you can enableApp Checkenforcement:

- [EnableApp Checkenforcement](https://firebase.google.com/docs/app-check/enable-enforcement)forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).
- [EnableApp Checkenforcement forCloud Functions](https://firebase.google.com/docs/app-check/cloud-functions).

### UseApp Checkin debug environments

If, after you have registered your app forApp Check, you want to run your app in an environment thatApp Checkwould normally not classify as valid, such as locally during development, or from a continuous integration (CI) environment, you can create a debug build of your app that uses theApp Checkdebug provider instead of a real attestation provider.

See[UseApp Checkwith the debug provider in web apps](https://firebase.google.com/docs/app-check/web/debug-provider).