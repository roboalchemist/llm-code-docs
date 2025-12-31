# Source: https://firebase.google.com/docs/app-check/monitor-metrics.md.txt

After you add theApp CheckSDK to your app, but before you enableApp Checkenforcement, you should make sure that doing so won't disrupt your existing legitimate users.

An important tool you can use to make this decision forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New) is theApp Checkrequest metrics screen.

To view theApp Checkrequest metrics for a product, open the[**App Check**](https://console.firebase.google.com/project/_/appcheck)section of theFirebaseconsole. For example:

![Metrics page](https://firebase.google.com/static/docs/app-check/app-check-metrics.png)

The request metrics for each product are broken down into four categories:

- **Verified** requests are those that have a validApp Checktoken. After you enableApp Checkenforcement, only requests in this category will succeed.

- **Outdated client** requests are those that are missing anApp Checktoken. These requests might be from an older version of the Firebase SDK beforeApp Checkwas included in the app.

- **Unknown origin** requests are those that are missing anApp Checktoken, and don't look like they come from the Firebase SDK. These might be from requests made with stolen API keys or forged requests made without the Firebase SDK.

- **Invalid** requests are those that have an invalidApp Checktoken, which might be from an inauthentic client attempting to impersonate your app, or from emulated environments.

The distribution of these categories for your app should inform when you decide to enable enforcement. Here are some guidelines:

- If almost all of the recent requests are from verified clients, consider enabling enforcement to start protecting your backend resources.

- If a significant portion of the recent requests are from likely-outdated clients, to avoid disrupting users, consider waiting for more users to update your app before enabling enforcement. EnforcingApp Checkon a released app will break prior app versions that are not integrated with theApp CheckSDK.

- If your app hasn't launched yet, you should enableApp Checkenforcement immediately, since there aren't any outdated clients in use.

## Next steps

When you understand howApp Checkwill affect your users and you're ready to proceed, you can[enableApp Checkenforcement](https://firebase.google.com/docs/app-check/enable-enforcement)forFirebase AI Logic,Data Connect,Realtime Database,Cloud Firestore,Cloud Storage,Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).