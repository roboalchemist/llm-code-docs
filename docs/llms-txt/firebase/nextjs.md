# Source: https://firebase.google.com/docs/hosting/frameworks/nextjs.md.txt

<br />

Using theFirebaseCLI, you can deploy your Next.js Web apps to Firebase and serve them withFirebase Hosting. The CLI respects your Next.js settings and translates them to Firebase settings with zero or minimal extra configuration on your part. If your app includes dynamic server-side logic, the CLI deploys that logic toCloud Functions for Firebase.
| **Note:** Framework-awareHostingis an early public preview. This means that the functionality might change in backward-incompatible ways. A preview release is not subject to any SLA or deprecation policy and may receive limited or no support.
| **Caution:** For developers creating a full-stack Next.js app, we strongly recommend[Firebase App Hosting](https://firebase.google.com/docs/app-hosting). If you're already using the frameworks experiment in the Firebase CLI, we recommend "graduating" toApp Hosting. WithApp Hosting, you'll have a unified solution to manage everything from CDN to server-side rendering, along with improved GitHub integration.

## Before you begin

Before you get started deploying your app to Firebase, review the following requirements and options:

- FirebaseCLI version 12.1.0 or later. Make sure to[install the CLI](https://firebase.google.com/docs/cli#install_the_firebase_cli)using your preferred method.
- Optional: Billing enabled on your Firebase project (required if you plan to use SSR)

- Optional: use the experimental ReactFire library to benefit from its Firebase-friendly features

## Initialize Firebase

To get started, initialize Firebase for your framework project. Use theFirebaseCLI for a new project, or modify`firebase.json`for an existing project.

### Initialize a new project

1. In theFirebaseCLI, enable the web frameworks preview:  

   ```
   firebase experiments:enable webframeworks
   ```
2. Run the initialization command from the CLI and then follow the prompts:

   ```
   firebase init hosting
   ```

   <br />

3. Answer yes to "Do you want to use a web framework? (experimental)"

4. Choose your hosting source directory. If this is an existing Next.js app, the CLI process completes, and you can proceed to the next section.

5. If prompted, choose Next.js.

## Serve static content

After initializing Firebase, you can serve static content with the standard deployment command:  

    firebase deploy

You can[view your deployed app](https://firebase.google.com/docs/hosting/test-preview-deploy#view-changes)on its live site.

## Pre-render dynamic content

TheFirebaseCLI will detect usage of[getStaticProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)and[getStaticPaths](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths).

### Optional: integrate with the Firebase JS SDK

When including Firebase JS SDK methods in both server and client bundles, guard against runtime errors by checking`isSupported()`before using the product. Not all products are[supported in all environments](https://firebase.google.com/docs/web/environments-js-sdk#other_environments).
| **Tip:** consider using[ReactFire](https://github.com/FirebaseExtended/reactfire#reactfire), which does this for you automatically.

### Optional: integrate with the Firebase Admin SDK

Admin SDK bundles will fail if included in your browser build; refer to them only inside[getStaticProps](https://nextjs.org/docs/basic-features/data-fetching/get-static-props)and[getStaticPaths](https://nextjs.org/docs/basic-features/data-fetching/get-static-paths).

## Serve fully dynamic content (SSR)

TheFirebaseCLI will detect usage of[getServerSideProps](https://nextjs.org/docs/basic-features/data-fetching/get-server-side-props). In such cases, the CLI will deploy functions toCloud Functions for Firebaseto run dynamic server code. You can view information about these functions, such as their domain and runtime configuration, in the[Firebase console](https://console.firebase.google.com/project/_/functions).

## ConfigureHostingbehavior with`next.config.js`

### Image Optimization

Using[Next.js Image Optimization](https://nextjs.org/docs/basic-features/image-optimization)is supported, but it will trigger creation of a function (in[Cloud Functions for Firebase](https://firebase.google.com/docs/functions)), even if you're not using SSR.
| **Note:** Because of this, image optimization andHostingpreview channels don't interoperate well together.

### Redirects, Rewrites, and Headers

TheFirebaseCLI respects[redirects](https://nextjs.org/docs/api-reference/next.config.js/redirects),[rewrites](https://nextjs.org/docs/api-reference/next.config.js/rewrites), and[headers](https://nextjs.org/docs/api-reference/next.config.js/headers)in`next.config.js`, converting them to their respective equivalentFirebase Hostingconfiguration at deploy time. If a Next.js redirect, rewrite, or header cannot be converted to an equivalentFirebase Hostingheader, it falls back and builds a function---even if you aren't using image optimization or SSR.

### Optional: integrate with Firebase Authentication

The web framework-aware Firebase deployment tooling will automatically keep client and server state in sync using cookies. There are some methods provided for accessing the authentication context in SSR:

- The Express`res.locals`object will optionally contain an authenticated Firebase App instance (`firebaseApp`) and the currently signed-in user (`currentUser`). This can be accessed in`getServerSideProps`.
- The authenticated Firebase App name is provided on the route query (`__firebaseAppName`). This allows for manual integration while in context:

    // get the authenticated Firebase App
    const firebaseApp = getApp(useRouter().query.__firebaseAppName);