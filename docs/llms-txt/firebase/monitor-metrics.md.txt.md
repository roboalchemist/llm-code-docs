# Source: https://firebase.google.com/docs/app-check/monitor-metrics.md.txt

After you add the App Check SDK to your app, but before you enable
App Check enforcement, you should make sure that doing so won't disrupt your
existing legitimate users.

An important tool you can use to make this decision for
Firebase AI Logic, Data Connect, Realtime Database, Cloud Firestore, Cloud Storage, Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New) is the App Check request metrics screen.

To view the App Check request metrics for a product, open the
[**App Check**](https://console.firebase.google.com/project/_/appcheck) section of the
Firebase console. For example:

![Metrics page](https://firebase.google.com/static/docs/app-check/app-check-metrics.png)

The request metrics for each product are broken down into four categories:

- **Verified** requests are those that have a valid App Check token. After
  you enable App Check enforcement, only requests in this category will
  succeed.

- **Outdated client** requests are those that are missing an App Check
  token. These requests might be from an older version of the Firebase SDK
  before App Check was included in the app.

- **Unknown origin** requests are those that are missing an App Check token,
  and don't look like they come from the Firebase SDK. These might be from
  requests made with stolen API keys or forged requests made without the
  Firebase SDK.

- **Invalid** requests are those that have an invalid
  App Check token, which might be from an inauthentic client attempting to
  impersonate your app, or from emulated environments.

The distribution of these categories for your app should inform when you decide
to enable enforcement. Here are some guidelines:

- If almost all of the recent requests are from verified clients, consider
  enabling enforcement to start protecting your backend resources.

- If a significant portion of the recent requests are from likely-outdated
  clients, to avoid disrupting users, consider waiting for more users to update
  your app before enabling enforcement. Enforcing App Check on a released
  app will break prior app versions that are not integrated with the
  App Check SDK.

- If your app hasn't launched yet, you should enable App Check enforcement
  immediately, since there aren't any outdated clients in use.

## Next steps

When you understand how App Check will affect your users and you're ready to
proceed, you can [enable App Check enforcement](https://firebase.google.com/docs/app-check/enable-enforcement)
for Firebase AI Logic, Data Connect, Realtime Database, Cloud Firestore, Cloud Storage, Authentication, Google Identity for iOS, Maps JavaScript API, and Places API (New).