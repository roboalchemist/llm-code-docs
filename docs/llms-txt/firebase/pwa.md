# Source: https://firebase.google.com/docs/web/pwa.md.txt

<br />

Progressive Web Apps (PWAs) are web apps that follow a[set of guidelines](https://developers.google.com/web/progressive-web-apps/checklist)meant to ensure that your users have a reliable, fast, and engaging experience.

Firebase offers several services that can help you efficiently add progressive features to your app to meet many PWA best practices, including:

|                               **PWA best practice**                               |                                                                                                                     **How Firebase services can help**                                                                                                                     |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Safe and secure](https://firebase.google.com/docs/web/pwa#safe_and_secure)       | - **Firebase Hosting**provisions SSL certificates at no cost for your custom domain and default Firebase subdomain. - **Firebase Authentication**enables you to sign in users across devices securely. - **FirebaseUI**implements best practices for authentication flows. |
| [Fast load time](https://firebase.google.com/docs/web/pwa#fast_load_time)         | - **Firebase Hosting**supports HTTP/2 and can cache both your static and dynamic content on a global CDN. - The**FirebaseJavaScriptSDK**is modular, and you can dynamically import libraries when they're needed.                                                          |
| [Network resilience](https://firebase.google.com/docs/web/pwa#network_resilience) | - With**Cloud Firestore**, you can store and access data in real time and offline. - **Firebase Authentication**maintains a user's authentication state, even offline.                                                                                                     |
| [Engage users](https://firebase.google.com/docs/web/pwa#engage_users)             | - **Firebase Cloud Messaging**enables you to send push messages to your users' devices. - With**Cloud Functions for Firebase**, you can automate re-engagement messages based on cloud events.                                                                             |

This page offers an overview of how the Firebase platform can help you to build a modern, high-performance PWA using our cross-browser[FirebaseJavaScriptSDK](https://firebase.google.com/docs/reference/js/).

Visit our[getting started guide](https://firebase.google.com/docs/web/setup)to add Firebase to your web app.

## Safe and secure

From serving your site to implementing an authentication flow, it's critical that your PWA provides a secure and trusted workflow.

### Serve your PWA over HTTPS

![Performant hosting service](https://firebase.google.com/static/docs/projects/images/hosting_serve-https.png)

HTTPS protects the integrity of your website and protects the privacy and security of your users. PWAs must be served over HTTPS.

[Firebase Hosting](https://firebase.google.com/docs/hosting/), by default, serves your app's content over HTTPS. You can serve your content on a no-cost Firebase-subdomain or on your own[custom domain](https://firebase.google.com/docs/hosting/custom-domain). Our hosting service provisions an SSL certificate for your custom domain automatically and at no cost.

Visit the[getting started guide forFirebase Hosting](https://firebase.google.com/docs/hosting/quickstart)to learn how you can host your PWA on the Firebase platform.

### Offer a secure authentication flow

![Drop-in responsive authentication flow](https://firebase.google.com/static/images/firebaseui_sign-in.png)

[FirebaseUI](https://github.com/firebase/firebaseui-web)provides a drop-in*responsive* authentication flow based on[Firebase Authentication](https://firebase.google.com/docs/auth/web/start), allowing your app to integrate a sophisticated and secure sign-in flow with low effort.FirebaseUIautomatically adapts to the screen size of a user's devices and follows best practices for auth flows.

FirebaseUIsupports multiple sign-in providers. Add theFirebaseUIauth flow into your app with just a few lines of code configured for sign-in providers:  

```gdscript
// FirebaseUI config.
var uiConfig = {
  signInSuccessUrl: '<var translate="no">URL</var>',  // the URL to direct to upon success
  signInOptions: [
    firebase.auth.GoogleAuthProvider.PROVIDER_ID,
    firebase.auth.EmailAuthProvider.PROVIDER_ID
  ]
};

// Initialize the FirebaseUI widget using Firebase.
var ui = new firebaseui.auth.AuthUI(firebase.auth());
ui.start('#firebaseui-auth-container', uiConfig);
```

Visit[our documentation in GitHub](https://github.com/firebase/firebaseui-web)to learn more about the various configuration options offered byFirebaseUI.

### Sign in users across devices

![Sign-in across devices](https://firebase.google.com/static/docs/projects/images/auth_sign-in-across-devices.png)

By using[FirebaseUI](https://firebase.google.com/docs/auth/)to integrate[one-tap sign in](https://github.com/firebase/firebaseui-web#credential-helper), your app can automatically sign in users, even on different devices that they've set up with their sign-in credentials.

Enable one-tap sign-in usingFirebaseUIby changing one line of configuration:  

```gdscript
// FirebaseUI config.
var uiConfig = {
  signInSuccessUrl: '<var translate="no">URL</var>',  // the URL to direct to upon success
  authMethod: 'https://accounts.google.com',
  signInOptions: firebase.auth.GoogleAuthProvider.PROVIDER_ID,
  // Enable one-tap sign-in.
  credentialHelper: firebaseui.auth.CredentialHelper.GOOGLE_YOLO
};
```

Visit[our documentation in GitHub](https://github.com/firebase/firebaseui-web)to learn more about the various configuration options offered byFirebaseUI.

## Fast load time

Having great performance improves the user experience, helps retain users, and increases conversion. Great performance, such as low "time to[first meaningful paint](https://developers.google.com/web/tools/lighthouse/audits/first-meaningful-paint)" and "[time to interactive](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive)", is an important requirement for PWAs.

### Serve your static assets efficiently

![Performant hosting service](https://firebase.google.com/static/docs/projects/images/hosting_asset-serving.png)

[Firebase Hosting](https://firebase.google.com/docs/hosting/)serves your content[over a global CDN](https://www.youtube.com/watch?v=LOeioOKUKI8&t=263s)and is HTTP/2 compatible. When you host your static assets with Firebase, we configure all this for you -- there's nothing extra that you need to do to take advantage of this service.

### Cache your dynamic content

WithFirebase Hosting, your web app can also serve*dynamic content* that's generated server-side by[Cloud Functions](https://firebase.google.com/docs/hosting/functions)or a[Cloud Runcontainerized app](https://firebase.google.com/docs/hosting/cloud-run). Using this service, you can[cache your dynamic content](https://firebase.google.com/docs/hosting/manage-cache)on a powerful global CDN with one line of code:  

```text
res.set('Cache-Control', 'public, max-age=300, s-maxage=600');
```

This service allows you to avoid additional calls to your back-end, speed up responses, and decrease costs.

Visit[our documentation](https://firebase.google.com/docs/hosting/serverless-overview)to learn how you can serve dynamic content (powered byCloud FunctionsorCloud Run) and enable CDN-caching withFirebase Hosting.

### Load services only when they're needed

TheFirebaseJavaScriptSDK can be[partially imported](https://firebase.google.com/docs/web/setup)to keep initial download size minimal. Take advantage of this modular SDK to import the Firebase services that your app needs only when they're needed.

For example, to increase your app's initial paint speed your app can first load[Firebase Authentication](https://firebase.google.com/docs/auth/). Then, when your app needs them, you can load other Firebase services, like[Cloud Firestore](https://firebase.google.com/docs/firestore/).

Using a package manager such as webpack, you can first loadFirebase Authentication:  

```python
import firebase from 'firebase/app';
import 'firebase/auth';

// Load Firebase project configuration.
const app = firebase.initializeApp(firebaseConfig);
```

Then, when you need to access your data layer, load theCloud Firestorelibrary using[dynamic imports](https://webpack.js.org/guides/code-splitting/#dynamic-imports):  

```gdscript
import('firebase/firestore').then(() => {
  const firestore = app.firestore();
  // Use Cloud Firestore ...
});
```

## Network resilience

Your users might not have dependable internet access. PWAs should behave similar to native mobile apps and should function offline whenever possible.

### Access your app data offline

[Cloud Firestore](https://firebase.google.com/docs/firestore/)supports[offline data persistence](https://firebase.google.com/docs/firestore/manage-data/enable-offline)which enables your app's data layer to transparently work offline. Combined with Service Workers to[cache your static assets](https://developers.google.com/web/ilt/pwa/caching-files-with-service-worker), your PWA can fully function offline. You can enable offline data persistence with one line of code:  

```gdscript
firebase.firestore().enablePersistence().then(() => {
  const firestore = app.firestore();
  // Use Cloud Firestore ...
});
```

### Maintain auth state offline

[Firebase Authentication](https://firebase.google.com/docs/auth/web/start)keeps a local cache of sign-in data, allowing a previously signed-in user to remain authenticated even when they're offline. The sign-in state observer will function normally and trigger even if your user reloads the app while offline:  

```text
firebase.auth().onAuthStateChanged((user) => {
  if (user) {
    // User is signed-in ...
  } else {
    // User is signed out ...
  }
});
```

Visit our documentation to get started with[Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart)and[Firebase Authentication](https://firebase.google.com/docs/auth/web/start).

## Engage users

Your users want to know when you release new features for your app, and you want to keep user engagement high. Set up your PWA to proactively and responsibly reach out to your users.

### Display push notifications to your users

With[Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/js/client), you can push relevant notifications from your server to your users' devices. This service allows you to display timely notifications to your users even when the app is closed.

### Automate user re-engagement

Using[Cloud Functions for Firebase](https://firebase.google.com/docs/functions/), send your users re-engagement messages based on cloud events, for example a[data write toCloud Firestore](https://firebase.google.com/docs/functions/firestore-events)or a[user account deletion](https://firebase.google.com/docs/functions/auth-events). You can also send a push notification to a user[when that user gets a new follower](https://github.com/firebase/functions-samples/tree/Node-8/fcm-notifications):  

```gdscript
// Send push notification when user gets a new follower.
exports.sendNotification = functions.database.ref('/followers/{userUID}/{followerUID}')
    .onWrite((change, context) => {
      const userUID = context.params.userUID;
      const followerUID = context.params.followerUID;

      const tokens = getUserDeviceTokens(userUID);
      const name = getUserDisplayName(followerUID);

      // Notification details.
      const payload = {
        notification: {
          title: 'You have a new follower!',
          body: `${name} is now following you.`
        }
      };
      return admin.messaging().sendToDevice(tokens, payload);
    });
```