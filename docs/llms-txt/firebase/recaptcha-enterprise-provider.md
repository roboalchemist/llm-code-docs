# Source: https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider.md.txt

This page shows you how to enableApp Checkin a web app, using the reCAPTCHA Enterprise provider. When you enableApp Check, you help ensure that only your app can access your project's backend resources. See an[Overview](https://firebase.google.com/docs/app-check)of this feature.

Note thatApp Checkuses reCAPTCHA Enterprise score-based site keys, which make it invisible to users. The reCAPTCHA Enterprise provider will not require users to solve a challenge at any time.

If your use case requires reCAPTCHA Enterprise features not implemented byApp Check, or if you want to useApp Checkwith your own custom provider, see[Implement a customApp Checkprovider](https://firebase.google.com/docs/app-check/web/custom-provider).

## 1. Set up your Firebase project

1. [Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup)if you haven't already done so.

2. Open the[reCAPTCHA Enterprise](https://console.cloud.google.com/security/recaptcha?project=_)section of the Cloud console and do the following:

   1. If you're prompted to enable the reCAPTCHA Enterprise API, do so.
   2. Create a**Website** -type key. You will need to specify domains on which you host your web app. Leave the "Use checkbox challenge" option**unselected**.
3. Register your apps to useApp Checkwith the reCAPTCHA Enterprise provider in the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole. You will need to provide the site key you got in the previous step.

   You usually need to register all of your project's apps, because once you enable enforcement for a Firebase product, only registered apps will be able to access the product's backend resources.
4. <br />

   <br />

   **Optional** : In the app registration settings, set a custom time-to-live (TTL) forApp Checktokens issued by the provider. You can set the TTL to any value between 30 minutes and 7 days. When changing this value, be aware of the following tradeoffs:
   - Security: Shorter TTLs provide stronger security, because it reduces the window in which a leaked or intercepted token can be abused by an attacker.
   - Performance: Shorter TTLs mean your app will perform attestation more frequently. Because the app attestation process adds latency to network requests every time it's performed, a short TTL can impact the performance of your app.
   - Quota and cost: Shorter TTLs and frequent re-attestation deplete your quota faster, and for paid services, potentially cost more. See[Quotas \& limits](https://firebase.google.com/docs/app-check#quotas_limits).

   The default TTL of**1 hour** is reasonable for most apps. Note that theApp Checklibrary refreshes tokens at approximately half the TTL duration.

   <br />

   <br />

### Configure advanced settings (optional)

When a user visits your web app, reCAPTCHA Enterprise evaluates the level of risk the user interaction poses, and returns a score between 0.0 and 1.0, in increments of 0.1. The score 1.0 indicates that the interaction poses low risk and is very likely legitimate, whereas 0.0 indicates that the interaction poses high risk and might be fraudulent.App Checklets you configure an**app risk**threshold so you can adjust your tolerance for this risk.

For most use cases, the default threshold value of**0.5** is recommended. If your use case requires adjustment, it can be configured in the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole for each of your web apps.

#### Details

App Checkuses your configured app risk threshold as the minimum reCAPTCHA Enterprise score required for a user interaction to be deemed legitimate. All reCAPTCHA Enterprise scores strictly less than your configured threshold will be rejected. When adjusting your app risk threshold, be aware of the following:

- Out of the 11 possible reCAPTCHA Enterprise score levels, only the following four score levels are available before you add a[Google Cloud Billing account](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#cloud-billing-accounts)to your project: 0.1, 0.3, 0.7, and 0.9. During this time,App Checkwill correspondingly only allow app risk threshold values of 0.1, 0.3, 0.5, 0.7, and 0.9. An app risk threshold value of 0.5 is still recommended for most use cases.

  - To enable all 11 reCAPTCHA Enterprise score levels, add a Google Cloud Billing account to your project. One way to do so is to[upgrade to the Blaze pricing plan](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#switch-between-pricing-plans). Once you have done so,App Checkwill allow you to configure any app risk threshold values between 0.0 and 1.0, in increments of 0.1.

    | **Note:** After a Google Cloud Billing account is added to your project, an automatic security review is triggered for your project. For more information, see the[reCAPTCHA Enterprise documentation](https://cloud.google.com/recaptcha/docs/interpret-assessment-website#interpret_scores).
- To monitor the distribution of high and low reCAPTCHA Enterprise scores for your web app, visit the reCAPTCHA Enterprise page in the[Google Cloudconsole](https://console.cloud.google.com/security/recaptcha)and select the site key used by your web app.

- If you have**low** app risk tolerance,**move the slider to the left**to increase the app risk threshold.

  - A value of 1.0 is not recommended, as this setting can also potentially deny access for legitimate users who do not meet this high trust threshold.

  | **Warning:** Before increasing the app risk threshold, you should consider temporarily unenforcing App Check protection for all currently enforced services to avoid disrupting your legitimate users. You should[monitor App Check request metrics](https://firebase.google.com/docs/app-check/monitor-metrics)to verify that traffic has not been disrupted before resuming enforcement.
- If you have**high** app risk tolerance,**move the slider to the right**to decrease the app risk threshold.

  - A value of 0.0 is not recommended, as this setting disables abuse protection.

Consult the[reCAPTCHA Enterprise documentation](https://cloud.google.com/recaptcha/docs/interpret-assessment-website)for additional details.

## 2. Add theApp Checklibrary to your app

[Add Firebase to your web app](https://firebase.google.com/docs/web/setup)if you haven't already. Be sure to import theApp Checklibrary.

## 3. InitializeApp Check

Add the following initialization code to your application, before you access any Firebase services. You will need to pass your reCAPTCHA Enterprise site key, which you created in the Cloud console, to`activate()`.  

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from the namespaced API.  

```python
import { initializeApp } from "firebase/app";
import { initializeAppCheck, ReCaptchaEnterpriseProvider } from "firebase/app-check";

const app = initializeApp({
  // Your Firebase configuration object.
});

// Create a ReCaptchaEnterpriseProvider instance using your reCAPTCHA Enterprise
// site key and pass it to initializeAppCheck().
const appCheck = initializeAppCheck(app, {
  provider: new ReCaptchaEnterpriseProvider(/* reCAPTCHA Enterprise site key */),
  isTokenAutoRefreshEnabled: true // Set to true to allow auto-refresh.
});
```
| **Note:** The SDK will not automatically refreshApp Checktokens by default. That functionality must be explicitly enabled by setting**isTokenAutoRefreshEnabled** to**true** in the options passed to**initializeAppCheck()** or by calling**setTokenAutoRefreshEnabled(appCheck, true)** . For more, see[the App Check reference docs](https://firebase.google.com/docs/reference/js/app-check).

### Web

```gdscript
firebase.initializeApp({
  // Your Firebase configuration object.
});

// Create a ReCaptchaEnterpriseProvider instance using your reCAPTCHA Enterprise
// site key and pass it to activate().
const appCheck = firebase.appCheck();
appCheck.activate(
  new firebase.appCheck.ReCaptchaEnterpriseProvider(
    /* reCAPTCHA Enterprise site key */
  ),
  true // Set to true to allow auto-refresh.
);
```
| **Note:** The SDK will not automatically refreshApp Checktokens by default. That functionality must be explicitly enabled by providing**true** as a second argument to**activate()** or by calling**firebase.appCheck().setTokenAutoRefreshEnabled(true)** . For more, see[the App Check reference docs](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck).

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

## Note on cost

App Checkcreates an assessment on your behalf to validate the user's response token each time a browser running your web app refreshes itsApp Checktoken. Your project will be charged for each assessment created above the no-cost quota. See[reCAPTCHA pricing](https://cloud.google.com/security/products/recaptcha#pricing)for details.

By default, your web app will refresh this token twice every**1 hour** . To control how frequently your app refreshesApp Checktokens (and thus how frequently new assessments are created),[configure their TTL](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider#set-ttl).