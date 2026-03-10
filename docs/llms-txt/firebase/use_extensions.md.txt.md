# Source: https://firebase.google.com/docs/emulator-suite/use_extensions.md.txt

> [!NOTE]
> **Beta.** This emulator is currently in beta. It might be
> changed in backward-incompatible ways. As always, feedback is greatly
> appreciated. Let us know what you think!

Before using the Extensions emulator with your app, make sure that
you [understand the overall Firebase Local Emulator Suite workflow](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=Firestore),
and that you [install and configure](https://firebase.google.com/docs/emulator-suite/install_and_configure)
the Local Emulator Suite and review its [CLI commands](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

This guide also assumes you are familiar with [Firebase Extensions](https://firebase.google.com/docs/extensions)
and how to [use them in your Firebase apps](https://firebase.google.com/docs/extensions/overview-use-extensions).

## What can I do with the Extensions emulator?

With the Extensions emulator, you can install and manage extensions in a
safe local environment and better understand their capabilities while minimizing
billing costs. The emulator runs your extension's functions locally, including
background event-triggered functions using the emulators for
Cloud Firestore, Realtime Database, Cloud Storage for Firebase, Authentication and
Pub/Sub, and Eventarc-triggered functions implemented in
Cloud Functions v2.

> [!NOTE]
> **Note:** Some extensions may call Google Cloud APIs and access services for which emulators do not exists in the Local Emulator Suite. Running the extension will still access those live services and may result in billing costs. Be sure to review extension descriptions carefully before evaluating them, so you understand billing impacts. We recommend you create and use a demo project for running the Extensions emulator, as described next.

## Choose a Firebase project

The Firebase Local Emulator Suite emulates products for a single Firebase project.

To select the project to use, before you start the emulators, in the CLI run
`firebase use` in your working directory. Or, you can pass
the `--project` flag to each emulator
command.

> [!NOTE]
> **Note:** It's generally a good practice to use one project ID for all emulator invocations, so the Emulator Suite UI, different product emulators, and all running instances of a particular emulator can communicate correctly in all cases. In fact, by default, the Local Emulator Suite will warn on detecting multiple project IDs in use, though you can override this behavior. For guidance on setting and managing project IDs, see the [Installation and configuration guide](https://firebase.google.com/docs/emulator-suite/install_and_configure#project_id_configuration).

Local Emulator Suite supports emulation of *real* Firebase projects and
*demo* projects.

| Project type | Features | Use with emulators |
|---|---|---|
| Real | A real Firebase project is one you created and configured (most likely via the Firebase console). Real projects have live resources, like database instances, storage buckets, functions, or any other resource you set up for that Firebase project. | When working with real Firebase projects, you can run emulators for any or all of the supported products. For any products you are not emulating, your apps and code will interact with the *live* resource (database instance, storage bucket, function, etc.). |
| Demo | A demo Firebase project has no *real* Firebase configuration and no live resources. These projects are usually accessed via codelabs or other tutorials. Project IDs for demo projects have the `demo-` prefix. | When working with demo Firebase projects, your apps and code interact with emulators *only*. If your app attempts to interact with a resource for which an emulator isn't running, that code will fail. |

We recommend you use demo projects wherever possible. Benefits include:

- Easier setup, since you can run the emulators without ever creating a Firebase project
- Stronger safety, since if your code accidentally invokes non-emulated (production) resources, there is no chance of data change, usage and billing
- Better offline support, since there is no need to access the internet to download your SDK configuration.

> [!NOTE]
> **Note:** If you want to emulate cross-service interactions such as database-triggered Cloud Functions or Security Rules that rely on Authentication you must make sure that the project ID in your code (in `initializeApp()`, etc.) matches the project ID used by the Firebase CLI.

## Install and evaluate an extension

Using the Extensions emulator to evaluate whether an extension meets your
needs is straightforward.

Let's assume you're interested in the Trigger Email
(`firestore-send-email`) [extension](https://firebase.google.com/docs/extensions/official/firestore-send-email),
though the following workflow covers any extension. When run with local emulators,
Trigger Email will automatically make use of the Cloud Firestore and
Cloud Functions emulators.

To evaluate an extension locally:

1. Add the extension to the local extensions manifest. An extensions manifest is
   a list of extension instances and their configurations.

   ```
   firebase ext:install --local firebase/firestore-send-email
   ```

   Running the above command will prompt you to configure the latest version of
   `firebase/firestore-send-email` extension and save the configuration to
   the manifest, but it won't deploy the configuration to your project. For
   more about this, see [Manage extensions configuration with manifests](https://firebase.google.com/docs/extensions/manifest)
2. Start the Local Emulator Suite as you would normally.

   ```
   firebase emulators:start
   ```

Now, using the `firestore-send-email` extension instance listed in
your manifest, the Local Emulator Suite will download the source code of
that extension to `~/.cache/firebase/extensions`. Once soures have been
downloaded, the Local Emulator Suite will start and you'll be able to
trigger any of the extension's background triggered functions and connect your
app to the Local Emulator Suite to test their integration with your app.

You can use Emulator Suite UI to add data to the email documents collection
and set up other backend resources, as required by the Trigger Email extension.

Alternatively, for non-interactive testing environments like continuous
integration workflows, you can write a test script for evaluating the extension
that, among other steps, populates necessary Cloud Firestore data and
triggers functions. You would then invoke the Local Emulator Suite
to execute your test script:

    firebase emulators:exec my-test.sh

> [!NOTE]
> **Note:** You can use the Extensions emulator to evaluate extensions that publish custom events. The Extensions emulator works together with the Cloud Functions emulator to help you test custom event-handling functions you implement with Cloud Functions v2 code. See [Connect your app to the Cloud Functions Emulator](https://firebase.google.com/docs/emulator-suite/connect_functions).

## How testing with the Extensions emulator differs from production

The Extensions emulator lets you test extensions in a way that closely
matches the production experience. However, there are some differences from
production behavior.

### Cloud IAM

The Firebase Emulator Suite does not attempt to replicate or respect any
IAM-related behavior for running. Emulators adhere to the Firebase Security
Rules provided, but in situations where IAM would normally be used, for example
to set Cloud Functions invoking service account and thus permissions, the
emulator is not configurable and will use the globally-available account on
your developer machine, similar to running a local script directly.

### Triggering type limitation

Currently, the Firebase Local Emulator Suite only supports HTTP request-triggered
functions, Eventarc custom event triggers for extensions, and background
event-triggered functions for Cloud Firestore, Realtime Database,
Cloud Storage for Firebase, Authentication and Pub/Sub. To evaluate extensions
that use other types of triggered functions, you need to
[install your extension](https://firebase.google.com/docs/extensions/install-extensions)
in a test Firebase project.

## What next?

- For a curated set of videos and detailed how-to examples, follow the [Firebase Emulators Training Playlist](https://firebase.google.com/learn/pathways/firebase-emulators).