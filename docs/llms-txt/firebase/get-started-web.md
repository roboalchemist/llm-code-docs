# Source: https://firebase.google.com/docs/perf-mon/get-started-web.md.txt

<br />

| TheFirebaseJavaScriptSDK forPerformance Monitoringis a**beta** release.  
| This product might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Before you begin

If you haven't already, visit[Add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup)to learn how to:

- Create a Firebase project

- Register your web app with Firebase

  | To usePerformance Monitoringin a web app, you*must* add your app as a Firebase Web App in theFirebaseconsole.
  |
  | If you already use Firebase products in your existing web app and you want to start using thePerformance MonitoringSDK, you must update your[Firebase config object](https://firebase.google.com/docs/web/setup#config-object)to include your`appID`.

Note that when you add Firebase to your app, you might complete some of the steps described later on this page (for example, adding the SDK and initializing Firebase).

## **Step 1** : Add and initializePerformance Monitoring

1. If you haven't already,[install the Firebase JS SDK and initialize Firebase](https://firebase.google.com/docs/web/setup#add-sdk-and-initialize).

2. Add thePerformance MonitoringJS SDK and initializePerformance Monitoring:

### Web

<br />

| [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular web API and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from the namespaced API.

<br />

```python
import { initializeApp } from "firebase/app";
import { getPerformance } from "firebase/performance";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Performance Monitoring and get a reference to the service
const perf = getPerformance(app);
```

### Web

<br />

| [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular web API and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from the namespaced API.

<br />

```python
import firebase from "firebase/compat/app";
import "firebase/compat/performance";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);


// Initialize Performance Monitoring and get a reference to the service
const perf = firebase.performance();
```

## **Step 2**: Add the first input delay polyfill library

To measure the[first input delay metric](https://firebase.google.com/docs/perf-mon/page-load-traces#input-delay), you need to add the polyfill library for this metric. For installation instructions, refer to the library's[documentation](https://github.com/GoogleChromeLabs/first-input-delay).

Adding this polyfill library is not required forPerformance Monitoringto report the other web app metrics.

## **Step 3**: Generate performance events for initial data display

Firebase starts processing the events when you successfully add the SDK to your app. If you're still developing locally, interact with your app to generate events for initial data collection and processing.
| **Note:** ThePerformance MonitoringSDK batches events locally then sends them to Firebase periodically (every 10 seconds). So, there's a delay between an app interaction and when Firebase receives the event information from your app.

1. Serve and view your web app in a local environment.

2. Generate events by loading subpages for your site, interacting with your app, and/or triggering network requests. Make sure to keep the browser tab open for at least 10 seconds after the page loads.

3. Go to the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)of theFirebaseconsole. You should see your initial data display within a few minutes.

   If you don't see a display of your initial data, review the[troubleshooting tips](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=ios#sdk-detected-no-data).

## **Step 4** :*(Optional)*View log messages for performance events

1. Open your browser's developer tools (for example,[Network tab for Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/network/)or in the[Network Monitor for Firefox](https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor)).

2. Refresh your web app in the browser.

3. Check your log messages for any error messages.

4. After a few seconds, look for a network call to`firebaselogging.googleapis.com`in your browser's developer tools. The presence of that network call shows that the browser is sending performance data to Firebase.

If your app isn't logging performance events, review the[troubleshooting tips](https://firebase.google.com/docs/perf-mon/troubleshooting?platform=web#app-not-logging-events).

## **Step 5** :*(Optional)*Add custom monitoring for specific code

To monitor performance data associated with specific code in your app, you can instrument[**custom code traces**](https://firebase.google.com/docs/perf-mon/custom-code-traces).

With a custom code trace, you can measure how long it takes your app to complete a specific task or set of tasks, such as loading a set of images or querying your database. The default metric for a custom code trace is its duration, but you can also add custom metrics, such as cache hits and memory warnings.

In your code, you define the beginning and the end of a custom code trace (and add any desired custom metrics) using the API provided by thePerformance MonitoringSDK.

Visit[Add monitoring for specific code](https://firebase.google.com/docs/perf-mon/custom-code-traces)to learn more about these features and how to add them to your app.

## **Step 6**: Deploy your app then review results

After you've validatedPerformance Monitoring, you can deploy the updated version of your app to your users.

You can monitor performance data in the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)of theFirebaseconsole.

## Next steps

- Get hands-on experience with the[Firebase Performance Monitoringfor Web Codelab](https://codelabs.developers.google.com/codelabs/firebase-perf-mon-web/).

- Learn more about data automatically collected byPerformance Monitoring:

  - Data for[page loading](https://firebase.google.com/docs/perf-mon/page-load-traces)in your app
  - Data for[HTTP/S network requests](https://firebase.google.com/docs/perf-mon/network-traces?platform=web)issued by your app
- [View, track, and filter](https://firebase.google.com/docs/perf-mon/console?platform=web)your performance data in theFirebaseconsole

- Add monitoring for specific tasks or workflows in your app by[instrumenting custom code traces](https://firebase.google.com/docs/perf-mon/custom-code-traces?platform=web)

- [Use attributes to filter performance data](https://firebase.google.com/docs/perf-mon/attributes?platform=web)