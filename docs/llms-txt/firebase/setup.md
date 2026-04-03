# Source: https://firebase.google.com/docs/ios/setup.md.txt

# Source: https://firebase.google.com/docs/games/setup.md.txt

# Source: https://firebase.google.com/docs/cpp/setup.md.txt

# Source: https://firebase.google.com/docs/unity/setup.md.txt

# Source: https://firebase.google.com/docs/flutter/setup.md.txt

# Source: https://firebase.google.com/docs/android/setup.md.txt

# Source: https://firebase.google.com/docs/admin/setup.md.txt

# Source: https://firebase.google.com/docs/web/setup.md.txt

# Source: https://firebase.google.com/docs/android/setup.md.txt

# Source: https://firebase.google.com/docs/admin/setup.md.txt

# Source: https://firebase.google.com/docs/web/setup.md.txt

<br />

Follow this guide to use theFirebaseJavaScriptSDK in your web app or as a client for end-user access, for example, in a Node.js desktop or IoT application.

## **Step 1**: Create a Firebase project and register your app

Before you can add Firebase to your JavaScript app, you need to create a Firebase project and register your app with that project. When you register your app with Firebase, you'll get a Firebase configuration object that you'll use to connect your app with your Firebase project resources.
| **Note:** Upgrading from the version 8 Firebase SDK? Check out our[upgrade guide](https://firebase.google.com/docs/web/modular-upgrade).

Visit[Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more)to learn more about Firebase projects and best practices for adding apps to projects.

#### **Create a Firebase project**

### New to Firebase or Cloud

Follow these steps if you're new to Firebase orGoogle Cloud.  
You can also follow these steps if you want to create a wholly new Firebase project (and its underlyingGoogle Cloudproject).

1. Sign into the[Firebaseconsole](https://console.firebase.google.com/).
2. Click the button to create a new Firebase project.
3. In the text field, enter a**project name**.

   If you're part of aGoogle Cloudorg, you can optionally select which folder you create your project in.
   | Your project name is used as a display name in Firebase interfaces, and Firebase auto-creates a unique project ID based on this project name. Note that you can optionally click the**Edit** icon now to set your preferred project ID, but you cannot change this ID after project creation. Learn about[how Firebase uses the project ID](https://firebase.google.com/docs/projects/learn-more#project-id).
4. If prompted, review and accept the[Firebase terms](https://firebase.google.com/terms), then click**Continue**.
5. *(Optional)* Enable AI assistance in theFirebaseconsole (called "Gemini in Firebase"), which can help you get started and streamline your development process.
6. *(Optional)* Set upGoogle Analyticsfor your project, which enables an optimal experience using these Firebase products:[Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),[Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),[Crashlytics](https://firebase.google.com/docs/crashlytics),[In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and[Remote Config](https://firebase.google.com/docs/remote-config)(including[Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing[Google Analyticsaccount](https://support.google.com/analytics/answer/1009618)or create a new account. If you create a new account, select your[Analyticsreporting location](https://firebase.google.com/docs/projects/locations), then accept the data sharing settings andGoogle Analyticsterms for your project.
   | You can always set upGoogle Analyticslater in the[*Integrations*tab](https://console.firebase.google.com/project/_/settings/integrations)of yoursettings*Project settings*.
7. Click**Create project**.

Firebase creates your project, provisions some initial resources, and enables important APIs. When the process completes, you'll be taken to the overview page for your Firebase project in theFirebaseconsole.

### Existing Cloud project

Follow these steps if you want to start using Firebase with an existingGoogle Cloudproject. Learn more about and troubleshoot["adding Firebase" to an existingGoogle Cloudproject](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project).

1. Sign into the[Firebaseconsole](https://console.firebase.google.com/)with the account that gives you access to the existingGoogle Cloudproject.
2. Click the button to create a new Firebase project.
3. At the bottom of the page, click**Add Firebase to Google Cloud project**.
4. In the text field, start entering the**project name**of the existing project, and then select the project from the displayed list.
5. Click**Open project**.
6. If prompted, review and accept the[Firebase terms](https://firebase.google.com/terms), then click**Continue**.
7. *(Optional)* Enable AI assistance in theFirebaseconsole (called "Gemini in Firebase"), which can help you get started and streamline your development process.
8. *(Optional)* Set upGoogle Analyticsfor your project, which enables an optimal experience using these Firebase products:[Firebase A/B Testing](https://firebase.google.com/docs/ab-testing),[Cloud Messaging](https://firebase.google.com/docs/cloud-messaging),[Crashlytics](https://firebase.google.com/docs/crashlytics),[In-App Messaging](https://firebase.google.com/docs/in-app-messaging), and[Remote Config](https://firebase.google.com/docs/remote-config)(including[Personalization](https://firebase.google.com/docs/remote-config/personalization)).

   Either select an existing[Google Analyticsaccount](https://support.google.com/analytics/answer/1009618)or create a new account. If you create a new account, select your[Analyticsreporting location](https://firebase.google.com/docs/projects/locations), then accept the data sharing settings andGoogle Analyticsterms for your project.
   | You can always set upGoogle Analyticslater in the[*Integrations*tab](https://console.firebase.google.com/project/_/settings/integrations)of yoursettings*Project settings*.
9. Click**Add Firebase**.

Firebase[adds Firebase to your existing project](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_what-happens-when-add-firebase). When the process completes, you'll be taken to the overview page for your Firebase project in theFirebaseconsole.

#### **Register your app**

After you have a Firebase project, you can register your web app with that project.

1. In the center of the[Firebase console's project overview page](https://console.firebase.google.com/), click the**Web** icon (plat_web) to launch the setup workflow.

   If you've already added an app to your Firebase project, click**Add app**to display the platform options.
2. Enter your app's nickname.  
   This nickname is an internal, convenience identifier and is only visible to you in the Firebase console.

3. Click**Register app**.

4. Follow the on-screen instructions to add and initialize the Firebase SDK in your app.

   You can also find more detailed instructions for adding, initializing, and using the Firebase SDK in the next steps of this getting started page.

If you don't already have a JavaScript project and just want to try out a Firebase product, you can download one of our[quickstart samples](https://firebase.google.com/docs/samples).

## **Step 2**: Install the SDK and initialize Firebase

This page describes setup instructions for the Firebase JS SDK's modular API, which uses a[JavaScript Module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)format.

This workflow uses npm and requires module bundlers or JavaScript framework tooling because the modular API is optimized to work with[module bundlers](https://firebase.google.com/docs/web/module-bundling)to eliminate unused code (tree-shaking) and decrease SDK size.
| **Note:** Using the modular API is strongly recommended, especially for production apps. If you need support for calling the API in other ways, like`window.firebase`, see[Upgrade from the namespaced API to the modular API](https://firebase.google.com/docs/web/modular-upgrade#window-compat)or[Alternative ways to add Firebase](https://firebase.google.com/docs/web/alt-setup).

1. Install Firebase using npm:

   ```
   npm install firebase
   ```
2. Initialize Firebase in your app and create a Firebase App object:

   ```javascript
   import { initializeApp } from 'firebase/app';

   // TODO: Replace the following with your app's https://firebase.google.com/docs/web/learn-more#config-object
   const firebaseConfig = {
     //...
   };

   const app = initializeApp(firebaseConfig);
   ```

   A Firebase App is a container-like object that stores common configuration and shares authentication across Firebase services. After you initialize a Firebase App object in your code, you can add and start using Firebase services.

   If your app includes dynamic features based on server-side rendering (SSR), you'll need to take some additional steps to ensure that your configuration persists across server rendering and client rendering passes. In your server logic, implement the[`FirebaseServerApp`](https://firebase.google.com/docs/reference/js/app.firebaseserverapp)interface to optimize your app's[session management with service workers](https://firebase.google.com/docs/auth/web/service-worker-sessions#server_side_changes).
   | Do you use ESM and want to use browser modules? Replace all your`import`lines to use the following pattern:  
   | `import { } from 'https://www.gstatic.com/firebasejs/12.7.0/firebase-`<var translate="no">SERVICE</var>`.js'`  
   | (where<var translate="no">SERVICE</var>is an SDK name such as`firebase-firestore`).
   |
   | Using browser modules is a quick way to get started, but we recommend using a module bundler for production.

## **Step 3**: Access Firebase in your app

Firebase services (likeCloud Firestore,Authentication,Realtime Database,Remote Config, and more) are available to import within individual sub-packages.

The example below shows how you could use theCloud FirestoreLite SDK to retrieve a list of data.  

```javascript
import { initializeApp } from 'firebase/app';
import { getFirestore, collection, getDocs } from 'firebase/firestore/lite';
// Follow this pattern to import other Firebase services
// import { } from 'firebase/<service>';

// TODO: Replace the following with your app's https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  //...
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Get a list of cities from your database
async function getCities(db) {
  const citiesCol = collection(db, 'cities');
  const citySnapshot = await getDocs(citiesCol);
  const cityList = citySnapshot.docs.map(doc => doc.data());
  return cityList;
}
```

## **Step 4**: Use a module bundler (webpack/Rollup) for size reduction

| **Note:** You can skip this step if you are using a JavaScript framework CLI tool like the[Angular CLI](https://angular.io/cli),[Next.js](https://nextjs.org/),[Vue CLI](https://cli.vuejs.org/), or[Create React App](https://reactjs.org/docs/create-a-new-react-app.html). Check out[our guide on module bundling](https://firebase.google.com/docs/web/module-bundling)for more information.

The Firebase Web SDK is designed to work with module bundlers to remove any unused code (tree-shaking). We strongly recommend using this approach for production apps. Tools such as the[Angular CLI](https://angular.io/cli),[Next.js](https://nextjs.org/),[Vue CLI](https://cli.vuejs.org/), or[Create React App](https://reactjs.org/docs/create-a-new-react-app.html)automatically handle module bundling for libraries installed through npm and imported into your codebase.

See our guide[Using module bundlers with Firebase](https://firebase.google.com/docs/web/module-bundling)for more information.

## Available Firebase services for web

Now that you're setup to use Firebase, you can start adding and using any of the following available Firebase services in your web app.

The following commands show how to import Firebase libraries installed locally with[`npm`](https://npmjs.com). For alternative import options, see the[available libraries documentation](https://firebase.google.com/docs/web/learn-more#available-libraries).
-

  #### [Firebase AI Logicfor Web](https://firebase.google.com/docs/ai-logic/get-started)^1^

  import { } from 'firebase/ai';
-

  #### [Analytics for Web](https://firebase.google.com/docs/analytics/get-started?platform=web)

  import { } from 'firebase/analytics';
-

  #### [App Check for Web](https://firebase.google.com/docs/app-check/web/recaptcha-provider)

  import { } from 'firebase/app-check';
-

  #### [Authentication for Web](https://firebase.google.com/docs/auth/web/start)

  import { } from 'firebase/auth';
-

  #### [Cloud Firestore for Web](https://firebase.google.com/docs/firestore/quickstart)

  import { } from 'firebase/firestore';
-

  #### [Cloud Functions for Web](https://firebase.google.com/docs/functions/callable#call_the_function)

  import { } from 'firebase/functions';
-

  #### [Cloud Messaging for Web](https://firebase.google.com/docs/cloud-messaging/js/client)

  import { } from 'firebase/messaging';
-

  #### [Cloud Storage for Web](https://firebase.google.com/docs/storage/web/start)

  import { } from 'firebase/storage';
-

  #### [Data Connect for Web](https://firebase.google.com/docs/data-connect/quickstart#web)

  import { } from 'firebase/data-connect';
-

  #### [Performance Monitoring for Web](https://firebase.google.com/docs/perf-mon/get-started-web)

  import { } from 'firebase/performance';
-

  #### [Realtime Database for Web](https://firebase.google.com/docs/database/web/start)

  import { } from 'firebase/database';
-

  #### [Remote Config for Web](https://firebase.google.com/docs/remote-config/get-started?platform=web)

  import { } from 'firebase/remote-config';

^**1** *Firebase AI Logicwas formerly called "Vertex AI in Firebase" with the package`firebase/vertexai`.*^

## Next steps

**Learn about Firebase:**

- Explore[sample Firebase apps](https://firebase.google.com/docs/samples).

- Get hands-on experience with the[Firebase Web Codelab](https://firebase.google.com/codelabs/firebase-nextjs).

- Explore the[open source code in GitHub](https://github.com/firebase/firebase-js-sdk).

- Review the[supported environments](https://firebase.google.com/docs/web/environments-js-sdk)for theFirebaseJavaScriptSDK.

- Speed up your development with additional Firebase-maintained open source libraries, like[AngularFire](https://firebaseopensource.com/projects/angular/angularfire2/),[RxFire](https://github.com/firebase/firebase-js-sdk/tree/master/packages/rxfire#rxfire), and[FirebaseUI for web](https://firebaseopensource.com/projects/firebase/firebaseui-web/).

- Prepare to launch your app:

  - Set up[budget alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)for your project in theGoogle Cloudconsole.
  - Monitor the[*Usage and billing*dashboard](https://console.firebase.google.com/project/_/usage)in theFirebaseconsole to get an overall picture of your project's usage across multiple Firebase services.
  - Review the[Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).