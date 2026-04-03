# Source: https://firebase.google.com/docs/functions/2nd-gen-upgrade.md.txt

<br />

Apps using 1st gen functions should consider migrating to 2nd gen using the instructions in this guide. 2nd gen functions use Cloud Run to provide better performance, better configuration, better monitoring, and more.
| **Note:** Cloud Functions for Firebase(2nd gen) also provides Python support. You can[get started](https://firebase.google.com/docs/functions/get-started)with Python using our basic tutorial's snippets and instructions.

The examples in this page assume you're using JavaScript with CommonJS modules (`require`style imports), but the same principles apply to JavaScript with ESM (`import ... from`style imports) and TypeScript.

## The migration process

1st gen and 2nd gen functions can coexist side-by-side in the same file. This allows for easy migration piece by piece, as you're ready. We recommend migrating one function at a time, performing testing and verification before proceeding.

## Verify Firebase CLI and`firebase-function`s versions

Make sure you're using at least Firebase CLI version`12.00`and`firebase-functions`version`4.3.0`. Any newer version will support 2nd gen as well as 1st gen.

## Update imports

2nd gen functions import from the`v2`subpackage in the`firebase-functions`SDK. This different import path is all the Firebase CLI needs to determine whether to deploy your function code as a 1st or 2nd gen function.

The`v2`subpackage is modular, and we recommend only importing the specific module that you need.

**Before: 1st gen**  

    const functions = require("firebase-functions/v1");

**After: 2nd gen**  

    // explicitly import each trigger
    const {onRequest} = require("firebase-functions/v2/https");
    const {onDocumentCreated} = require("firebase-functions/v2/firestore");

## Update trigger definitions

Since the 2nd gen SDK favors modular imports, update trigger definitions to reflect the changed imports from the previous step.

The arguments passed to callbacks for some triggers have changed. In this example, note that the arguments to the`onDocumentCreated`callback have been consolidated into a single`event`object. Additionally, some triggers have convenient new configuration features, like the`onRequest`trigger's`cors`option.

**Before: 1st gen**  

    const functions = require("firebase-functions/v1");

    exports.date = functions.https.onRequest((req, res) => {
      // ...
    });

    exports.uppercase = functions.firestore
      .document("my-collection/{docId}")
      .onCreate((change, context) => {
        // ...
      });

**After: 2nd gen**  

    const {onRequest} = require("firebase-functions/v2/https");
    const {onDocumentCreated} = require("firebase-functions/v2/firestore");

    exports.date = onRequest({cors: true}, (req, res) => {
      // ...
    });

    exports.uppercase = onDocumentCreated("my-collection/{docId}", (event) => {
      /* ... */
    });

## Use parameterized configuration

2nd gen functions drop support for`functions.config`in favor of a more secure interface for[defining configuration parameters declaratively](https://firebase.google.com/docs/functions/config-env?gen=2nd#params)inside your codebase. With the new`params`module, the CLI blocks deployment unless all parameters have a valid value, ensuring that a function isn't deployed with missing configuration.

### Migrate to the`params`subpackage

If you have been using environment configuration with`functions.config`, you can migrate your existing configuration by refactoring it as[parameterized configuration](https://firebase.google.com/docs/functions/config-env#params). For example:

**Before: 1st gen**  

    const functions = require("firebase-functions/v1");

    exports.date = functions.https.onRequest((req, res) => {
      const date = new Date();
      const formattedDate =
    date.toLocaleDateString(functions.config().dateformat);

      // ...
    });

**After: 2nd gen**  

    const {onRequest} = require("firebase-functions/v2/https");
    const {defineString} = require("firebase-functions/params");

    const dateFormat = defineString("DATE_FORMAT");

    exports.date = onRequest((req, res) => {
      const date = new Date();
      const formattedDate = date.toLocaleDateString(dateFormat.value());

      // ...
    });

### Migrating Nested Configuration

If your`functions.config()`usage involved nested objects, the`defineJsonSecret`parameter type offers a straightforward migration path. You can store the entire JSON structure from`functions.config()`directly in a single secret.

For example, if you had:

**Before: 1st gen**  

    const functions = require("firebase-functions/v1");

    exports.myFunction = functions.https.onRequest((req, res) => {
      const apiKey = functions.config().someapi.key;
      const webhookSecret = functions.config().someapi.webhookSecret;
      // ...
    });

You can migrate by storing the entire`someapi`object as a JSON string in a secret named`SOMEAPI_CONFIG`and use`defineJsonSecret`:

**After: 2nd gen**  

    const {onRequest} = require("firebase-functions/v2/https");
    const {defineJsonSecret} = require("firebase-functions/params");

    const someApiConfig = defineJsonSecret("SOMEAPI_CONFIG");

    exports.myFunction = onRequest(<mark>{ secrets: [someApiConfig] }</mark>, (req, res) => {
      const apiKey = someApiConfig.value().key;
      const webhookSecret = someApiConfig.value().webhookSecret;
      // ...
    });

Note that, unlike`functions.config()`, any secret defined with`defineSecret`or`defineJsonSecret`must be explicitly bound to the function using the`{
secrets: [...] }`option to be accessible at runtime.

This preserves the configuration structure and minimizes code changes. You can use the Firebase CLI to help export your existing`functions.config()`JSON and set it as the value for the new secret. See[Managing secrets](https://firebase.google.com/docs/functions/config-env?gen=2nd#managing_secrets)for instructions on setting secret values, including how to set JSON secrets from a file or stdin.

### Set parameter values

The first time you deploy, the Firebase CLI prompts for all values of parameters, and save the values in a dotenv file. To export your`functions.config`values, run`firebase functions:config:export`.

For additional safety, you can also specify parameter[types](https://firebase.google.com/docs/functions/config-env?gen=2nd#parameter_types)and[validation rules](https://firebase.google.com/docs/functions/config-env?gen=2nd#configure_behavior).

### Special case: API Keys

The`params`module integrates with Cloud Secret Manager, which provides fine-grained access control to sensitive values like API keys. See[secret parameters](https://firebase.google.com/docs/functions/config-env?gen=2nd#secret-parameters)and[Structured JSON Secrets](https://firebase.google.com/docs/functions/config-env?gen=2nd#json-secrets)for more information.

**Before: 1st gen**  

    const functions = require("firebase-functions/v1");

    exports.getQuote = functions.https.onRequest(async (req, res) => {
      const quote = await fetchMotivationalQuote(functions.config().apiKey);
      // ...
    });

**After: 2nd gen**  

    const {onRequest} = require("firebase-functions/v2/https");
    const {defineSecret} = require("firebase-functions/params");

    // Define the secret parameter
    const apiKey = defineSecret("API_KEY");

    exports.getQuote = onRequest(
      // make the secret available to this function
      { secrets: [apiKey] },
      async (req, res) => {
        // retrieve the value of the secret
        const quote = await fetchMotivationalQuote(apiKey.value());
        // ...
      }
    );

## Set runtime options

Configuration of[runtime options](https://firebase.google.com/docs/functions/manage-functions?gen=2nd#set_runtime_options)has changed between 1st and 2nd gen. 2nd gen also adds a new capability to set options for all functions.

**Before: 1st gen**  

    const functions = require("firebase-functions/v1");

    exports.date = functions
      .runWith({
        // Keep 5 instances warm for this latency-critical function
        minInstances: 5,
      })
      // locate function closest to users
      .region("asia-northeast1")
      .https.onRequest((req, res) => {
        // ...
      });

    exports.uppercase = functions
      // locate function closest to users and database
      .region("asia-northeast1")
      .firestore.document("my-collection/{docId}")
      .onCreate((change, context) => {
        // ...
      });

**After: 2nd gen**  

    const {onRequest} = require("firebase-functions/v2/https");
    const {onDocumentCreated} = require("firebase-functions/v2/firestore");
    const {setGlobalOptions} = require("firebase-functions/v2");

    // locate all functions closest to users
    setGlobalOptions({ region: "asia-northeast1" });

    exports.date = onRequest({
        // Keep 5 instances warm for this latency-critical function
        minInstances: 5,
      }, (req, res) => {
      // ...
    });

    exports.uppercase = onDocumentCreated("my-collection/{docId}", (event) => {
      /* ... */
    });

## Update default service account (optional)

While 1st gen functions use the Google app engine default service account to authorize access to Firebase APIs, 2nd gen functions use the Compute Engine default service account. This difference can lead to permissions issues for functions migrated to 2nd gen in cases where you have granted special permissions to the 1st gen service account. If you haven't changed any service account permissions, you can skip this step.

The recommended solution is to explicitly assign the existing 1st gen App Engine default service account to functions that you want to migrate to 2nd gen, overriding the 2nd gen default. You can do this by making sure each migrated function sets the correct value for`serviceAccountEmail`:  

    const {onRequest} = require("firebase-functions/https");
    const {onDocumentCreated} = require("firebase-functions/v2/firestore");
    const {setGlobalOptions} = require("firebase-functions");

    // Use the App Engine default service account for all functions
    setGlobalOptions({serviceAccountEmail: '<my-project-number>@<wbr>appspot.gserviceaccount.com'});

    // Now I use the App Engine default service account.
    exports.date = onRequest({cors: true}, (req, res) => {
      // ...
    });

    // I do too!
    exports.uppercase = onDocumentCreated("my-collection/{docId}", (event) => {
      // ...
    });

Alternatively, you could make sure to modify the service account details to match all the necessary permissions on both the App Engine default service account (for 1st Gen) and the Compute Engine default service account (for 2nd Gen).

## Use concurrency

A significant advantage of 2nd gen functions is the ability of a single function instance to serve more than one request at once. This can dramatically reduce the number of cold starts experienced by end users. By default, concurrency is set at 80, but you can set it to any value from 1 to 1000:  

    const {onRequest} = require("firebase-functions/v2/https");

    exports.date = onRequest({
        // set concurrency value
        concurrency: 500
      },
      (req, res) => {
        // ...
    });

Tuning concurrency can improve performance and reduce cost of functions. Learn more about concurrency in[Allow concurrent requests](https://firebase.google.com/docs/functions/manage-functions#allow_concurrent_requests).

### Audit global variable usage

1st gen functions written without concurrency in mind might use global variables that are set and read on each request. When concurrency is enabled and a single instance starts handling multiple requests at once, this may introduce bugs in your function as concurrent requests start setting and reading global variables simultaneously.

While upgrading, you can set your function's CPU to`gcf_gen1`and set`concurrency`to 1 to restore 1st gen behavior:  

    const {onRequest} = require("firebase-functions/v2/https");

    exports.date = onRequest({
        // TEMPORARY FIX: remove concurrency
        cpu: "gcf_gen1",
        concurrency: 1
      },
      (req, res) => {
        // ...
    });

However, this is not recommended as a long-term fix, as it forfeits the performance advantages of 2nd gen functions. Instead, audit usage of global variables in your functions, and remove these temporary settings when you're ready.

## Migrate traffic to the new 2nd gen functions

Just as when[changing a function's region or trigger type](https://firebase.google.com/docs/functions/manage-functions?gen=2nd#modify), you'll need to give the 2nd gen function a new name and slowly migrate traffic to it.

It is not possible to upgrade a function from 1st to 2nd gen with the same name and run`firebase deploy`. Doing so will result in the error:  

    Upgrading from GCFv1 to GCFv2 is not yet supported. Please delete your old function or wait for this feature to be ready.

Before you follow these steps, first ensure that your function is[idempotent](https://firebase.google.com/docs/functions/tips#write_idempotent_functions), since both the new version and the old version of your function will be running at the same time during the change. For example, if you have a 1st gen function that responds to write events in Firestore, ensure that responding to a write twice, once by the 1st gen function and once by the 2nd gen function, in response to those events leaves your app in a consistent state.

1. Rename the function in your functions code. For example, rename`resizeImage`to`resizeImageSecondGen`.
2. Deploy the function, so that both the original 1st gen function and 2nd gen function are running.
   1. In the case of callable, Task Queue, and HTTP triggers, begin pointing all clients to the 2nd gen function by updating client code with the 2nd gen function's name or URL.
   2. With background triggers, both the 1st gen and 2nd gen functions will respond to every event immediately upon deploy.
3. When all traffic is migrated off, delete the 1st gen function using the firebase CLI's`firebase functions:delete`command.
   1. Optionally, rename the 2nd gen function to match the name of the 1st gen function.