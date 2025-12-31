# Source: https://firebase.google.com/docs/hosting/frameworks/angular.md.txt

<br />

With the Firebase framework-aware CLI, you can deploy your Angular application to Firebase and serve dynamic content to your users.
| **Note:** Framework-awareHostingis an early public preview. This means that the functionality might change in backward-incompatible ways. A preview release is not subject to any SLA or deprecation policy and may receive limited or no support.
| **Caution:** For developers creating a full-stack Angular app, we strongly recommend[Firebase App Hosting](https://firebase.google.com/docs/app-hosting). If you're already using the frameworks experiment in the Firebase CLI, we recommend "graduating" toApp Hosting. WithApp Hosting, you'll have a unified solution to manage everything from CDN to server-side rendering, along with improved GitHub integration.

## Before you begin

Before you get started deploying your app to Firebase, review the following requirements and options:

- FirebaseCLI version 12.1.0 or later. Make sure to[install the CLI](https://firebase.google.com/docs/cli#install_the_firebase_cli)using your preferred method.
- Optional: Billing enabled on your Firebase project (required if you plan to use SSR)

- Optional: AngularFire

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

4. Choose your hosting source directory; this could be an existing Angular app.

5. If prompted, choose Angular.

### Initialize an existing project

Change your hosting config in`firebase.json`to have a`source`option, rather than a`public`option. For example:  

    {
      "hosting": {
        "source": "./path-to-your-angular-workspace"
      }
    }

## Serve static content

After initializing Firebase, you can serve static content with the standard deployment command:  

    firebase deploy

## Pre-render dynamic content

To prerender dynamic content in Angular, you need to set up Angular SSR.  

    ng add @angular/ssr

See the[Angular Prerendering (SSG) guide](https://angular.dev/guide/ssr)for more information.

### Optional: add a server module

#### Deploy

When you deploy with`firebase deploy`, Firebase builds your browser bundle, your server bundle, and prerenders the application. These elements are deployed toHostingandCloud Functions for Firebase.

#### Custom deploy

TheFirebaseCLI assumes that you have a single application defined in your`angular.json`with a production build configuration.

If need to tailor the CLI's assumptions, you can either use the`FIREBASE_FRAMEWORKS_BUILD_TARGET`environment variable or add[AngularFire](https://github.com/angular/angularfire#readme)and modify your`angular.json`:  

    {
      "deploy": {
        "builder": "@angular/fire:deploy",
        "options": {
          "version": 2,
          "buildTarget": "OVERRIDE_YOUR_BUILD_TARGET"
        }
      }
    }

### Optional: integrate with the Firebase JS SDK

When including Firebase JS SDK methods in both server and client bundles, guard against runtime errors by checking`isSupported()`before using the product. Not all products are[supported in all environments](https://firebase.google.com/docs/web/environments-js-sdk#other_environments).
| **Tip:** consider using[AngularFire](https://github.com/angular/angularfire#readme), which does this for you automatically.

### Optional: integrate with the Firebase Admin SDK

Admin bundles will fail if they are included in your browser build, so consider providing them in your server module and injecting as an optional dependency:  

    // your-component.ts
    import type { app } from 'firebase-admin';
    import { FIREBASE_ADMIN } from '../app.module';

    @Component({...})
    export class YourComponent {

      constructor(@Optional() @Inject(FIREBASE_ADMIN) admin: app.App) {
        ...
      }
    }

    // app.server.module.ts
    import * as admin from 'firebase-admin';
    import { FIREBASE_ADMIN } from './app.module';

    @NgModule({
      ...
      providers: [
        ...
        { provide: FIREBASE_ADMIN, useFactory: () => admin.apps[0] || admin.initializeApp() }
      ],
    })
    export class AppServerModule {}

    // app.module.ts
    import type { app } from 'firebase-admin';

    export const FIREBASE_ADMIN = new InjectionToken<app.App>('firebase-admin');

## Serve fully dynamic content with SSR

### Optional: integrate with Firebase Authentication

The web framework-aware Firebase deployment tooling automatically keeps client and server state in sync using cookies. The Express`res.locals`object will optionally contain an authenticated Firebase App instance (`firebaseApp`) and the currently signed in user (`currentUser`). This can be injected into your module via the REQUEST token (exported from @nguniversal/express-engine/tokens).