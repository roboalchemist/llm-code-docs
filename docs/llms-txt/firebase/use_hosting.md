# Source: https://firebase.google.com/docs/emulator-suite/use_hosting.md.txt

<br />

Before you start prototyping and testing your web app with theFirebase Hostingemulator, make sure that you[understand the overallFirebase Local Emulator Suiteworkflow](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=Firestore), and that you[install and configure](https://firebase.google.com/docs/emulator-suite/install_and_configure)theLocal Emulator Suiteand review its[CLI commands](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

You should also be familiar with the features and implementation workflow forFirebase Hosting. Start with the[introduction toFirebase Hosting](https://firebase.google.com/docs/hosting).

## What can I do with theFirebase Hostingemulator?

TheFirebase Hostingemulator provides high-fidelity local emulation ofHostingservices, providing much of the functionality found in[productionHosting](https://firebase.google.com/docs/hosting/quickstart). TheHostingemulator lets you:

- Prototype your static sites and web apps without incurring storage or access charges
- Prototype, test and debug HTTPS functions before deploying to your Hosting site
- Test sites and web apps in containerized, continuous integration workflows.

## Choose a Firebase project

TheFirebase Local Emulator Suiteemulates products for a single Firebase project.

To select the project to use, before you start the emulators, in the CLI run`firebase use`in your working directory. Or, you can pass the`--project`flag to each emulator command.
| **Note:** It's generally a good practice to use one project ID for all emulator invocations, so theEmulator Suite UI, different product emulators, and all running instances of a particular emulator can communicate correctly in all cases. In fact, by default, theLocal Emulator Suitewill warn on detecting multiple project IDs in use, though you can override this behavior. For guidance on setting and managing project IDs, see the[Installation and configuration guide](https://firebase.google.com/docs/emulator-suite/install_and_configure#project_id_configuration).

Local Emulator Suitesupports emulation of*real* Firebase projects and*demo*projects.

| Project type |                                                                                                                      Features                                                                                                                       |                                                                                                                       Use with emulators                                                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Real         | A real Firebase project is one you created and configured (most likely via theFirebaseconsole). Real projects have live resources, like database instances, storage buckets, functions, or any other resource you set up for that Firebase project. | When working with real Firebase projects, you can run emulators for any or all of the supported products. For any products you are not emulating, your apps and code will interact with the*live*resource (database instance, storage bucket, function, etc.). |
| Demo         | A demo Firebase project has no*real*Firebase configuration and no live resources. These projects are usually accessed via codelabs or other tutorials. Project IDs for demo projects have the`demo-`prefix.                                         | When working with demo Firebase projects, your apps and code interact with emulators*only*. If your app attempts to interact with a resource for which an emulator isn't running, that code will fail.                                                         |

We recommend you use demo projects wherever possible. Benefits include:

- Easier setup, since you can run the emulators without ever creating a Firebase project
- Stronger safety, since if your code accidentally invokes non-emulated (production) resources, there is no chance of data change, usage and billing
- Better offline support, since there is no need to access the internet to download your SDK configuration.

| **Note:** If you want to emulate cross-service interactions such as database-triggeredCloud FunctionsorRulesthat rely onAuthenticationyou must make sure that the project ID in your code (in`initializeApp()`, etc.) matches the project ID used by theFirebaseCLI.

## Core prototyping workflow

If you're making quick iterations or you want your app to interact with emulated backend project resources, you can test yourHostingcontent and config locally. When testing locally, Firebase serves your web app at a locally hosted URL.

1. *(Optional)* By default, your locally hosted app will interact with*real* , not*emulated* , project resources (functions, database, rules, etc.). You can instead optionally connect your app to use any*emulated* project resources that you've configured. Learn more:[Realtime Database](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=RTDB)\|[Cloud Firestore](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=Firestore)\|[Cloud Functions](https://firebase.google.com/docs/emulator-suite/connect_functions)

2. From the root of your local project directory, run the following command:

   ```
   firebase emulators:start
   ```
3. Open your web app at the local URL returned by the CLI (usually`http://localhost:5000`).

4. To update the local URL with changes, refresh your browser.

### Test from other local devices

By default, the emulators only respond to requests from`localhost`. This means that you'll be able to access your hosted content from your computer's web browser but not from other devices on your network. If you'd like to test from other local devices, configure your`firebase.json`like so:  

    "emulators": {
        // ...

        "hosting": {
          "port": 5000,
          "host": "0.0.0.0"
        }
      }

## Generate auth tokens for continuous integration workflows

If your continuous integration workflows rely on Firebase Hosting, then you will need to log in using a token in order to run`firebase emulators:exec`. The other emulators do not require login.
| **Note:** If you have configured hosting in`firebase.json`but do not need it in CI test setups, use the`--only`flag to`emulators:start`or`emulators:exec`to include only the emulators that you need.

To generate a token, run`firebase login:ci`on your local environment; this should not be performed from a CI system. Follow instructions to authenticate. You should only need to perform this step once per project, since the token will be valid across builds. The token should be treated like a password; make sure it is kept secret.

If your CI environment allows you to specify environment variables that can be used in the build scripts, simply create an environment variable called`FIREBASE_TOKEN`, with the value being the access token string. TheFirebaseCLI will automatically pick up the`FIREBASE_TOKEN`environment variable and the emulators will start properly.

As a last resort, you can simply include the token in your build script, but make sure that untrusted parties do not have access. For this hard-coded approach, you can add`--token "YOUR_TOKEN_STRING_HERE"`to the`firebase emulators:exec`command.

## What next?

- Run a quickstart using theHostingemulator by following the[Firebase web codelab](https://firebase.google.com/codelabs/firebase-web).
- Understand how to prototype HTTPS functions using theHostingemulator as described in the[Hosting guides for functions](https://firebase.google.com/docs/hosting/functions).
- For a curated set of videos and detailed how-to examples, follow the[Firebase Emulators Training Playlist](https://firebase.google.com/learn/pathways/firebase-emulators).