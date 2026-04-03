# Source: https://firebase.google.com/docs/emulator-suite/use_extensions.md.txt

<br />

| **Beta.**This emulator is currently in beta. It might be changed in backward-incompatible ways. As always, feedback is greatly appreciated. Let us know what you think!

Before using theExtensionsemulator with your app, make sure that you[understand the overallFirebase Local Emulator Suiteworkflow](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=Firestore), and that you[install and configure](https://firebase.google.com/docs/emulator-suite/install_and_configure)theLocal Emulator Suiteand review its[CLI commands](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

This guide also assumes you are familiar with[Firebase Extensions](https://firebase.google.com/docs/extensions)and how to[use them in your Firebase apps](https://firebase.google.com/docs/extensions/overview-use-extensions).

## What can I do with theExtensionsemulator?

With theExtensionsemulator, you can install and manage extensions in a safe local environment and better understand their capabilities while minimizing billing costs. The emulator runs your extension's functions locally, including background event-triggered functions using the emulators forCloud Firestore,Realtime Database,Cloud Storage for Firebase,AuthenticationandPub/Sub, and Eventarc-triggered functions implemented inCloud Functionsv2.
| **Note:** Some extensions may callGoogle CloudAPIs and access services for which emulators do not exists in theLocal Emulator Suite. Running the extension will still access those live services and may result in billing costs. Be sure to review extension descriptions carefully before evaluating them, so you understand billing impacts. We recommend you create and use a demo project for running theExtensionsemulator, as described next.

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

## Install and evaluate an extension

Using theExtensionsemulator to evaluate whether an extension meets your needs is straightforward.

Let's assume you're interested in the Trigger Email (`firestore-send-email`)[extension](https://firebase.google.com/docs/extensions/official/firestore-send-email), though the following workflow covers any extension. When run with local emulators, Trigger Email will automatically make use of theCloud FirestoreandCloud Functionsemulators.

To evaluate an extension locally:

1. Add the extension to the local extensions manifest. An extensions manifest is a list of extension instances and their configurations.

   ```
   firebase ext:install --local firebase/firestore-send-email
   ```

   Running the above command will prompt you to configure the latest version of`firebase/firestore-send-email`extension and save the configuration to the manifest, but it won't deploy the configuration to your project. For more about this, see[Manage extensions configuration with manifests](https://firebase.google.com/docs/extensions/manifest)
2. Start theLocal Emulator Suiteas you would normally.

   ```
   firebase emulators:start
   ```

Now, using the`firestore-send-email`extension instance listed in your manifest, theLocal Emulator Suitewill download the source code of that extension to`~/.cache/firebase/extensions`. Once soures have been downloaded, theLocal Emulator Suitewill start and you'll be able to trigger any of the extension's background triggered functions and connect your app to theLocal Emulator Suiteto test their integration with your app.

You can useEmulator Suite UIto add data to the email documents collection and set up other backend resources, as required by the Trigger Email extension.

Alternatively, for non-interactive testing environments like continuous integration workflows, you can write a test script for evaluating the extension that, among other steps, populates necessaryCloud Firestoredata and triggers functions. You would then invoke theLocal Emulator Suiteto execute your test script:  

    firebase emulators:exec my-test.sh

| **Note:** You can use theExtensionsemulator to evaluate extensions that publish custom events. TheExtensionsemulator works together with theCloud Functionsemulator to help you test custom event-handling functions you implement withCloud Functionsv2 code. See[Connect your app to theCloud FunctionsEmulator](https://firebase.google.com/docs/emulator-suite/connect_functions).

## How testing with theExtensionsemulator differs from production

TheExtensionsemulator lets you test extensions in a way that closely matches the production experience. However, there are some differences from production behavior.

### Cloud IAM

The Firebase Emulator Suite does not attempt to replicate or respect any IAM-related behavior for running. Emulators adhere to the Firebase Security Rules provided, but in situations where IAM would normally be used, for example to set Cloud Functions invoking service account and thus permissions, the emulator is not configurable and will use the globally-available account on your developer machine, similar to running a local script directly.

### Triggering type limitation

Currently, theFirebase Local Emulator Suiteonly supports HTTP request-triggered functions, Eventarc custom event triggers for extensions, and background event-triggered functions forCloud Firestore,Realtime Database,Cloud Storage for Firebase,AuthenticationandPub/Sub. To evaluate extensions that use other types of triggered functions, you need to[install your extension](https://firebase.google.com/docs/extensions/install-extensions)in a test Firebase project.

## What next?

- For a curated set of videos and detailed how-to examples, follow the[Firebase Emulators Training Playlist](https://firebase.google.com/learn/pathways/firebase-emulators).