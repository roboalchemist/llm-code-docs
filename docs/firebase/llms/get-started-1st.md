# Source: https://firebase.google.com/docs/functions/1st-gen/get-started-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Get started: write, test, and deploy your first functions](https://firebase.google.com/docs/functions/get-started).

To get started withCloud Functions, try working through this tutorial, which starts with the required setup tasks and works through creating, testing, and deploying two related functions:

- An "add message" function that exposes a URL that accepts a text value and writes it toCloud Firestore.
- A "make uppercase" function that triggers on aCloud Firestorewrite and transforms the text to uppercase.

We've chosenCloud Firestoreand HTTP-triggered JavaScript functions for this sample in part because these background triggers can be thoroughly tested through the[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite). This toolset also supportsRealtime Database, PubSub, Auth, and HTTP callable triggers. Other types of background triggers such asRemote Config, TestLab, and Analytics triggers can all be[tested interactively](https://firebase.google.com/docs/functions/local-shell)using toolsets not described in this page.
| **Note:** You can emulate functions in any Firebase project, but to deploy to the Node.js 14 runtime environment, your project must be on the[Blaze pricing plan](https://firebase.google.com/pricing). See[Cloud Functionspricing](https://firebase.google.com/support/faq#functions-pricing).

The following sections of this tutorial detail the steps required to build, test, and deploy the sample. If you'd rather just run the code and inspect it, jump to[Review complete sample code](https://firebase.google.com/docs/functions/1st-gen/get-started-1st#review_complete_sample_code).

## Create a Firebase Project

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

## Set up Node.js and the Firebase CLI

You'll need a[Node.js](https://nodejs.org/)environment to write functions, and you'll need theFirebaseCLI to deploy functions to theCloud Functionsruntime. For installing Node.js and[npm](https://www.npmjs.org/),[Node Version Manager](https://github.com/creationix/nvm/blob/master/README.md)is recommended.
| **Important:** Node.js versions 20 and 22 are supported. See[Set runtime options](https://firebase.google.com/static/docs/functions/1st-gen/manage-functions-1st#1g-set-node.js)for important information regarding ongoing support for these versions of Node.js.

Once you have Node.js and npm installed,[install theFirebaseCLI](https://firebase.google.com/docs/cli#setup_update_cli)via your preferred method. To install the CLI via npm, use:  

    npm install -g firebase-tools

This installs the globally available firebase command. If the command fails, you may need to[change npm permissions](https://docs.npmjs.com/getting-started/fixing-npm-permissions). To update to the latest version of`firebase-tools`, rerun the same command.
| In many cases, new features and bug fixes are available only with the latest version of the Firebase CLI and the`firebase-functions`SDK. It's a good practice to frequently update both the Firebase CLI and the SDK with these commands inside the`functions`folder of your Firebase project:  
|
| ```
| npm install firebase-functions@latest firebase-admin@latest --save
| npm install -g firebase-tools
| ```

## Initialize your project

When you initializeFirebaseSDK forCloud Functions, you create an empty project containing dependencies and some minimal sample code, and you choose either TypeScript or JavaScript for composing functions. For the purposes of this tutorial, you'll also need to initializeCloud Firestore.

To initialize your project:

1. Run`firebase login`to log in via the browser and authenticate theFirebaseCLI.

   | **Note:** If you are using a device without an accessible localhost, add the`--no-localhost`flag.
2. Go to your Firebase project directory.

3. Run`firebase init firestore`. For this tutorial, you can accept the default values when prompted for Firestore rules and index files. If you haven't usedCloud Firestorein this project yet, you'll also need to select a starting mode and location for Firestore as described in[Get started withCloud Firestore](https://firebase.google.com/docs/firestore/quickstart#create).

4. Run`firebase init functions`. The CLI prompts you to choose an existing codebase or initialize and name a new one. When you're just getting started, a single codebase in the default location is adequate; later, as your implementation expands, you might want to[organize functions in codebases](https://firebase.google.com/docs/functions/organize-functions#organize_functions_in_codebases).

5. The CLI gives you the following options for language support:

   - JavaScript
   - Python
   - TypeScript See[Write Functions with TypeScript](https://firebase.google.com/docs/functions/typescript)for more information.

   For this tutorial, select**JavaScript**.
6. The CLI gives you an option to install dependencies with npm. It is safe to decline if you want to manage dependencies in another way, though if you do decline you'll need to run`npm install`before emulating or deploying your functions.

After these commands complete successfully, your project structure looks like this:  

    myproject
     +- .firebaserc    # Hidden file that helps you quickly switch between
     |                 # projects with `firebase use`
     |
     +- firebase.json  # Describes properties for your project
     |
     +- functions/     # Directory containing all your functions code
          |
          +- .eslintrc.json  # Optional file containing rules for JavaScript linting.
          |
          +- package.json  # npm package file describing your Cloud Functions code
          |
          +- index.js      # main source file for your Cloud Functions code
          |
          +- node_modules/ # directory where your dependencies (declared in
                           # package.json) are installed

The`package.json`file created during initialization contains an important key:`"engines": {"node": "16"}`. This specifies your Node.js version for writing and deploying functions. You can[select other supported versions](https://firebase.google.com/docs/functions/manage-functions#set_nodejs_version).

## Import the required modules and initialize an app

After you have completed the setup tasks, you can open the source directory and start adding code as described in the following sections. For this sample, your project must import theCloud Functionsand Admin SDK modules using Node`require`statements. Add lines like the following to your`index.js`file:

<br />

```gdscript
// The Cloud Functions for Firebase SDK to create Cloud Functions and set up triggers.
const functions = require('firebase-functions/v1');

// The Firebase Admin SDK to access Firestore.
const admin = require("firebase-admin");
admin.initializeApp();https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-firestore/functions/index.js#L20-L25
```

<br />

These lines load the`firebase-functions`and`firebase-admin`modules, and initialize an`admin`app instance from whichCloud Firestorechanges can be made. Wherever[Admin SDK](https://firebase.google.com/docs/admin/setup)support is available, as it is forFCM,Authentication, andFirebase Realtime Database, it provides a powerful way to integrate Firebase usingCloud Functions.

TheFirebaseCLI automatically installs the Firebase andFirebaseSDK forCloud FunctionsNode modules when you initialize your project. To add 3rd party libraries to your project, you can modify`package.json`and run`npm install`. For more information, see[Handle Dependencies](https://firebase.google.com/docs/functions/handle-dependencies).

## Add the`addMessage()`function

For the`addMessage()`function, add these lines to`index.js`:

<br />

```gdscript
// Take the text parameter passed to this HTTP endpoint and insert it into
// Firestore under the path /messages/:documentId/original
exports.addMessage = functions.https.onRequest(async (req, res) => {
  // Grab the text parameter.
  const original = req.query.text;
  // Push the new message into Firestore using the Firebase Admin SDK.
  const writeResult = await admin
    .firestore()
    .collection("messages")
    .add({ original: original });
  // Send back a message that we've successfully written the message
  res.json({ result: `Message with ID: ${writeResult.id} added.` });
});https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-firestore/functions/index.js#L29-L45
```

<br />

The`addMessage()`function is an HTTP endpoint. Any request to the endpoint results in ExpressJS-style[Request](http://expressjs.com/en/4x/api.html#req)and[Response](http://expressjs.com/en/4x/api.html#res)objects passed to the[`onRequest()`](https://firebase.google.com/docs/reference/functions/firebase-functions.https#httpsonrequest)callback.

HTTP functions are synchronous (similar to[callable functions](https://firebase.google.com/docs/functions/callable)), so you should send a response as quickly as possible and defer work usingCloud Firestore. The`addMessage()`HTTP function passes a text value to the HTTP endpoint and inserts it into the database under the path`/messages/:documentId/original`.

## Add the`makeUppercase()`function

For the`makeUppercase()`function, add these lines to`index.js`:

<br />

```gdscript
// Listens for new messages added to /messages/:documentId/original and creates an
// uppercase version of the message to /messages/:documentId/uppercase
exports.makeUppercase = functions.firestore
  .document("/messages/{documentId}")
  .onCreate((snap, context) => {
    // Grab the current value of what was written to Firestore.
    const original = snap.data().original;

    // Access the parameter `{documentId}` with `context.params`
    functions.logger.log("Uppercasing", context.params.documentId, original);

    const uppercase = original.toUpperCase();

    // You must return a Promise when performing asynchronous tasks inside a Functions such as
    // writing to Firestore.
    // Setting an 'uppercase' field in Firestore document returns a Promise.
    return snap.ref.set({ uppercase }, { merge: true });
  });https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-firestore/functions/index.js#L49-L70
```

<br />

The`makeUppercase()`function executes whenCloud Firestoreis written to. The`ref.set`function defines the document to listen on. For performance reasons, you should be as specific as possible.

Braces---for example,`{documentId}`---surround "parameters," wildcards that expose their matched data in the callback.

Cloud Firestoretriggers the[`onCreate()`](https://firebase.google.com/docs/reference/functions/firebase-functions.firestore.documentbuilder#firestoredocumentbuilderoncreate)callback whenever new messages are added.
| **Caution:** Be careful to avoid any situation in which the function's result actually retriggers the function, creating an infinite loop --- for example, a function triggered by writes to a specificCloud Firestoredocument that terminates by writing to that same path. Also make sure to write functions in an[idempotent](https://en.wikipedia.org/wiki/Idempotence)way, so that they produce the same result if they run multiple times for a single event.

Event-driven functions such asCloud Firestoreevents are asynchronous. The callback function should return either a`null`, an Object, or a[Promise](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Promise). If you do not return anything, the function times out, signaling an error, and is retried. See[Sync, Async, and Promises](https://firebase.google.com/docs/functions/terminate-functions).

## Emulate execution of your functions

The[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite)allows you to build and test apps on your local machine instead of deploying to a Firebase project. Local testing during development is strongly recommended, in part because it lowers the risk from coding errors that could potentially incur cost in a production environment (for example, an infinite loop).

To emulate your functions:

1. Run`firebase emulators:start`and check the output for the URL of theEmulator Suite UI. It defaults to[localhost:4000](http://localhost:4000), but may be hosted on a different port on your machine. Enter that URL in your browser to open theEmulator Suite UI.

2. Check the output of the`firebase emulators:start`command for the URL of the HTTP function`addMessage()`. It will look similar to`http://localhost:5001/MY_PROJECT/us-central1/addMessage`, except that:

   1. `MY_PROJECT`will be replaced with your project ID.
   2. The port may be different on your local machine.
3. Add the query string`?text=uppercaseme`to the end of the function's URL. This should look something like:`http://localhost:5001/MY_PROJECT/us-central1/addMessage?text=uppercaseme`. Optionally, you can change the message "uppercaseme" to a custom message.

4. Create a new message by opening the URL in a new tab in your browser.

5. View the effects of the functions in theEmulator Suite UI:

   1. In the**Logs** tab, you should see new logs indicating that the functions`addMessage()`and`makeUppercase()`ran:

      `i functions: Beginning execution of "addMessage"`

      `i functions: Beginning execution of "makeUppercase"`
   2. In the**Firestore**tab, you should see a document containing your original message as well as the uppercased version of your message (if it was originally "uppercaseme", you'll see "UPPERCASEME").

## Deploy functions to a production environment

Once your functions are working as desired in the emulator, you can proceed to deploying, testing, and running them in the production environment. Keep in mind that to deploy to the Node.js 14 runtime environment, your project must be on the[Blaze pricing plan](https://firebase.google.com/pricing). See[Cloud Functionspricing](https://firebase.google.com/support/faq#functions-pricing).

To complete the tutorial, deploy your functions and then execute`addMessage()`to trigger`makeUppercase()`.

1. Run this command to deploy your functions:

   <br />

   ```
    firebase deploy --only functions
    
   ```

   <br />

   After you run this command, theFirebaseCLI outputs the URL for any HTTP function endpoints. In your terminal, you should see a line like the following:  

       Function URL (addMessage): https://us-central1-MY_PROJECT.cloudfunctions.net/addMessage

   The URL contains your project ID as well as a region for the HTTP function. Though you don't need to worry about it now, some production HTTP functions should specify a[location](https://firebase.google.com/docs/functions/locations)to minimize network latency.

   If you encounter access errors such as "Unable to authorize access to project," try checking your[project aliasing](https://firebase.google.com/docs/cli#project_aliases).
2. Using the`addMessage()`URL output by the CLI, add a text query parameter, and open it in a browser:

       https://us-central1-MY_PROJECT.cloudfunctions.net/addMessage?text=uppercasemetoo

   The function executes and redirects the browser to theFirebaseconsole at the database location where the text string is stored. This write event triggers`makeUppercase()`, which writes an uppercase version of the string.

After deploying and executing functions, you can view logs in the[Google Cloudconsole](https://console.cloud.google.com/functions/list). If you need to[delete functions](https://firebase.google.com/docs/functions/manage-functions#delete_functions)in development or production, use theFirebaseCLI.

In production, you may want to optimize function performance and control costs by setting minimum and maximum numbers of instances to run. See[Control scaling behavior](https://firebase.google.com/docs/functions/manage-functions#min-max-instances)for more information on these runtime options.
| **Note:** Deployment of functions fromFirebaseCLI is subject to rate limits. See[Quota limits forFirebaseCLI deployment](https://firebase.google.com/docs/functions/quotas#quota_limits_for_firebase_cli_deployment).

## Review complete sample code

Here's the completed`functions/index.js`containing the functions`addMessage()`and`makeUppercase()`. These functions allow you to pass a parameter to an HTTP endpoint that writes a value toCloud Firestore, and then transforms it by uppercasing all characters in the string.  

```gdscript
// The Cloud Functions for Firebase SDK to create Cloud Functions and set up triggers.
const functions = require('firebase-functions/v1');

// The Firebase Admin SDK to access Firestore.
const admin = require("firebase-admin");
admin.initializeApp();

// Take the text parameter passed to this HTTP endpoint and insert it into
// Firestore under the path /messages/:documentId/original
exports.addMessage = functions.https.onRequest(async (req, res) => {
  // Grab the text parameter.
  const original = req.query.text;
  // Push the new message into Firestore using the Firebase Admin SDK.
  const writeResult = await admin
    .firestore()
    .collection("messages")
    .add({ original: original });
  // Send back a message that we've successfully written the message
  res.json({ result: `Message with ID: ${writeResult.id} added.` });
});

// Listens for new messages added to /messages/:documentId/original and creates an
// uppercase version of the message to /messages/:documentId/uppercase
exports.makeUppercase = functions.firestore
  .document("/messages/{documentId}")
  .onCreate((snap, context) => {
    // Grab the current value of what was written to Firestore.
    const original = snap.data().original;

    // Access the parameter `{documentId}` with `context.params`
    functions.logger.log("Uppercasing", context.params.documentId, original);

    const uppercase = original.toUpperCase();

    // You must return a Promise when performing asynchronous tasks inside a Functions such as
    // writing to Firestore.
    // Setting an 'uppercase' field in Firestore document returns a Promise.
    return snap.ref.set({ uppercase }, { merge: true });
  });https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-firestore/functions/index.js#L19-L71
```

## Next steps

In this documentation, you can learn more about how to[manage functions](https://firebase.google.com/docs/functions/manage-functions)forCloud Functionsas well as how to to handle all event types supported byCloud Functions.

To learn more aboutCloud Functions, you could also do the following:

- Read about[use cases forCloud Functions](https://firebase.google.com/docs/functions/use-cases).
- Try the[Cloud Functionscodelab](https://codelabs.developers.google.com/codelabs/firebase-cloud-functions/#0).
- Review and run[code samples on GitHub](https://github.com/firebase/functions-samples)