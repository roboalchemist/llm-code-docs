# Source: https://firebase.google.com/docs/functions/1st-gen/manage-functions-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Manage functions](https://firebase.google.com/docs/functions/manage-functions).

You can deploy, delete, and modify functions usingFirebaseCLI commands or by setting runtime options in your functions source code.

## Deploy functions

To deploy functions, run thisFirebaseCLI command:  

```
firebase deploy --only functions
```

By default, theFirebaseCLI deploys all of the functions inside your source at the same time. If your project contains more than 5 functions, we recommend that you use the`--only`flag with specific function names to deploy only the functions that you've edited.[Deploying specific functions](https://firebase.google.com/docs/cli#deploy_specific_functions)this way speeds up the deployment process and helps you avoid running into deployment quotas. For example:  

```
firebase deploy --only functions:addMessage,functions:makeUppercase
```

When deploying large numbers of functions, you may exceed the standard quota and receive HTTP 429 or 500 error messages. To solve this, deploy functions in groups of 10 or fewer.

See the[FirebaseCLI reference](https://firebase.google.com/docs/cli)for the full list of available commands.

By default, theFirebaseCLI looks in the`functions/`folder for the source code. If you prefer, you can[organize functions](https://firebase.google.com/docs/functions/1st-gen/organize-functions-1st)in codebases or multiple sets of files.

## Delete functions

You can delete previously deployed functions in these ways:

- *explicitly* in theFirebaseCLI with`functions:delete`
- *explicitly* in the[Google Cloudconsole](https://console.cloud.google.com/functions/list).
- *implicitly*by removing the function from source prior to deployment.

All deletion operations prompt you to confirm before removing the function from production.

Explicit function deletion in theFirebaseCLI supports multiple arguments as well as functions groups, and allows you to specify a function running in a particular region. Also, you can override the confirmation prompt.  

```
# Delete all functions that match the specified name in all regions.
firebase functions:delete myFunction
```  

```
# Delete a specified function running in a specific region.
firebase functions:delete myFunction --region us-east-1
```  

```
# Delete more than one function
firebase functions:delete myFunction myOtherFunction
```  

```
# Delete a specified functions group.
firebase functions:delete groupA
```  

```
# Bypass the confirmation prompt.
firebase functions:delete myFunction --force
```

With implicit function deletion,`firebase deploy`parses your source and removes from production any functions that have been removed from the file.

## Modify a function's name, region or trigger

If you are renaming or changing the regions or trigger for functions that are handling production traffic, follow the steps in this section to avoid losing events during modification. Before you follow these steps, first ensure that your function is[idempotent](https://firebase.google.com/docs/functions/tips#write_idempotent_functions), since both the new version and the old version of your function will be running at the same time during the change.

### Rename a function

To rename a function, create a new renamed version of the function in your source and then run two separate deployment commands. The first command deploys the newly named function, and the second command removes the previously deployed version. For example, if you have a Node.js function called`webhook`that you'd like to change to`webhookNew`, revise the code as follows:  

    // before
    const functions = require('firebase-functions/v1');

    exports.webhook = functions.https.onRequest((req, res) => {
        res.send("Hello");
    });

    // after
    const functions = require('firebase-functions/v1');

    exports.webhookNew = functions.https.onRequest((req, res) => {
        res.send("Hello");
    });

Then run the following commands to deploy the new function:  

```
# Deploy new function called webhookNew
firebase deploy --only functions:webhookNew

# Wait until deployment is done; now both webhookNew and webhook are running

# Delete webhook
firebase functions:delete webhook
```

### Change a function's region or regions

If you are changing the specified[regions](https://firebase.google.com/docs/functions/locations)for a function that's handling production traffic, you can prevent event loss by performing these steps in order:

1. Rename the function, and change its region or regions as desired.
2. Deploy the renamed function, which results in temporarily running the same code in both sets of regions.
3. Delete the previous function.

For example, if you have a function called`webhook`that is currently in the default functions region of`us-central1`, and you want to migrate it to`asia-northeast1`, you need to first modify your source code to rename the function and revise the region.  

    // before
    const functions = require('firebase-functions/v1');

    exports.webhook = functions
        .https.onRequest((req, res) => {
                res.send("Hello");
        });

    // after
    const functions = require('firebase-functions/v1');

    exports.webhookAsia = functions
        .region('asia-northeast1')
        .https.onRequest((req, res) => {
                res.send("Hello");
        });

Then deploy by running:  

```
firebase deploy --only functions:webhookAsia
```

Now there are two identical functions running:`webhook`is running in`us-central1`, and`webhookAsia`is running in`asia-northeast1`.

Then, delete`webhook`:  

```
firebase functions:delete webhook
```

Now there is only one function -`webhookAsia`, which is running in`asia-northeast1`.

### Change a function's trigger type

As you develop yourCloud Functions for Firebasedeployment over time, you may need to change a function's trigger type for various reasons. For example, you might want to change from one type ofFirebase Realtime DatabaseorCloud Firestoreevent to another type.

It is not possible to change a function's event type by just changing the source code and running`firebase deploy`. To avoid errors, change a function's trigger type by this procedure:

1. Modify the source code to include a new function with the desired trigger type.
2. Deploy the function, which results in temporarily running both the old and new functions.
3. Explicitly delete the old function from production using theFirebaseCLI.

For instance, if you had a Node.js function named`objectChanged`that has the legacy`onChange`event type, and you'd like to change it to`onFinalize`, first rename the function and edit it to have the`onFinalize`event type.  

    // before
    const functions = require('firebase-functions/v1');

    exports.objectChanged = functions.storage.object().onChange((object) => {
        return console.log('File name is: ', object.name);
    });

    // after
    const functions = require('firebase-functions/v1');

    exports.objectFinalized = functions.storage.object().onFinalize((object) => {
        return console.log('File name is: ', object.name);
    });

Then run the following commands to create the new function first, before deleting the old function:  

```
# Create new function objectFinalized
firebase deploy --only functions:objectFinalized

# Wait until deployment is done; now both objectChanged and objectFinalized are running

# Delete objectChanged
firebase functions:delete objectChanged
```

## Set runtime options

Cloud Functions for Firebaselets you select runtime options such as the Node.js runtime version and per-function timeout, memory allocation, and minimum/maximum function instances.

As a best practice, these options (except for Node.js version) should be set on a configuration object inside the function code. This[`RuntimeOptions`](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions)object is the source of truth for your function's runtime options, and will override options set via any other method (such as via the Google Cloud console or gcloud CLI).

If your development workflow involves manually setting runtime options via Google Cloud console or gcloud CLI and you*don't* want these values to be overridden on each deploy, set the`preserveExternalChanges`option to`true`. With this option set to`true`, Firebase merges the runtime options set in your code with the settings of the currently-deployed version of your function with the following priority:

1. Option is set in functions code: override external changes.
2. Option is set to`RESET_VALUE`in functions code: override external changes with the default value.
3. Option is not set in functions code, but is set in currently deployed function: use the option specified in the deployed function.

Using the`preserveExternalChanges: true`option is*not recommended*for most scenarios because your code will no longer be the full source of truth for runtime options for your functions. If you do use it, check the Google Cloud console or use the gcloud CLI to view a function's full configuration.

### Set Node.js version

TheFirebaseSDK forCloud Functionsallows a selection of Node.js runtime. You can choose to run all functions in a project exclusively on the runtime environment corresponding to one of these supported Node.js versions:

- **Node.js 22**
- **Node.js 20**
- **Node.js 18 (deprecated)**

See the[support schedule](https://cloud.google.com/functions/docs/runtime-support#node.js)for important information regarding ongoing support for these versions of Node.js.

To set the Node.js version:

You can set the version in the`engines`field in the`package.json`file that was created in your`functions/`directory during initialization. For example, to use only version 20, edit this line in`package.json`:  

      "engines": {"node": "22"}

If you are using Yarn package manager or have other specific requirements for the`engines`field, you can set the runtime for theFirebaseSDK forCloud Functionsin`firebase.json`instead:  

      {
        "functions": {
          "runtime": "nodejs22"
        }
      }

The CLI uses the value set in`firebase.json`in preference to any value or range that you set separately in`package.json`.

#### Upgrade your Node.js runtime

To upgrade your Node.js runtime:

1. Make sure your project is on the[Blaze pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).
2. Make sure you are usingFirebaseCLI v11.18.0 or later.
3. Change the`engines`value in the`package.json`file that was created in your`functions/`directory during initialization. For example, if you are upgrading from version 16 to version 18, the entry should look like this:`"engines": {"node": "18"}`
4. Optionally, test your changes using the[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite).
5. Redeploy all functions.

### Choose a Node.js module system

The default module system in Node.js is CommonJS (CJS), but current Node.js versions also support ECMAScript Modules (ESM).Cloud Functionssupports both.

By default, your functions use CommonJS. That means imports and exports look like this:  

    const functions = require("firebase-functions/v1");

    exports.helloWorld = functions.https.onRequest(async (req, res) => res.send("Hello from Firebase!"));

To use ESM instead, set the`"type": "module"`field in your`package.json`file :  

      {
       ...
       "type": "module",
       ...
      }

Once you set this, use ESM`import`and`export`syntax:  

    import functions from "firebase-functions/v1";

    export const helloWorld = functions.https.onRequest(async (req, res) => res.send("Hello from Firebase!"));

Both module systems are fully supported. You can choose whichever best fits your project. Learn more in the[Node.js documentation on modules](https://nodejs.org/api/esm.html).

### Control scaling behavior

By default,Cloud Functions for Firebasescales the number of running instances based on the number of incoming requests, potentially scaling down to zero instances in times of reduced traffic. However, if your app requires reduced latency and you want to limit the number of cold starts, you can change this default behavior by specifying a minimum number of container instances to be kept warm and ready to serve requests.

Similarly, you can set a maximum number to limit the scaling of instances in response to incoming requests. Use this setting as a way to control your costs or to limit the number of connections to a backing service such as to a database.

#### Reduce the number of cold starts

To set minimum number of instances for a function in source code, use the[`runWith`](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder#functionbuilderrunwith)method. This method accepts a JSON object conforming to the[`RuntimeOptions`](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions#runtimeoptions_interface)interface, which defines the value for`minInstances`. For example, this function sets a minimum of 5 instances to keep warm:  

    exports.getAutocompleteResponse = functions
        .runWith({
          // Keep 5 instances warm for this latency-critical function
          minInstances: 5,
        })
        .https.onCall((data, context) => {
          // Autocomplete a user's search term
        });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/runtime-options/functions/index.js#L20-L27

| **Note:** A minimum number of instances kept running incur billing costs at idle rates. Typically, to keep one idle function instance warm costs less than $6.00 a month. The Firebase CLI provides a cost estimate at deployment time for functions with reserved minimum instances. Refer to[Cloud FunctionsPricing](https://cloud.google.com/run/pricing)to calculate costs.

Here are some things to consider when setting a value for`minInstances`:

- IfCloud Functions for Firebasescales your app above your`minInstances`setting, you'll experience a cold start for each instance above that threshold.
- Cold starts have the most severe effect on apps with spiky traffic. If your app has spiky traffic and you set a`minInstances`value high enough that cold starts are reduced on each traffic increase, you'll see significantly reduced latency. For apps with constant traffic, cold starts are not likely to severely affect performance.
- Setting minimum instances can make sense for production environments, but should usually be avoided in testing environments. To scale to zero in your test project but still reduce cold starts in your production project, you can set`minInstances`based on the`FIREBASE_CONFIG`environment variable:

      // Get Firebase project id from `FIREBASE_CONFIG` environment variable
      const envProjectId = JSON.parse(process.env.FIREBASE_CONFIG).projectId;

      exports.renderProfilePage = functions
          .runWith({
            // Keep 5 instances warm for this latency-critical function
            // in production only. Default to 0 for test projects.
            minInstances: envProjectId === "my-production-project" ? 5 : 0,
          })
          .https.onRequest((req, res) => {
            // render some html
          });  
      https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/runtime-options/functions/index.js#L31-L42

#### Limit the maximum number of instances for a function

To set maximum instances in function source code, use the[`runWith`](https://firebase.google.com/docs/reference/functions/firebase-functions.functionbuilder#functionbuilderrunwith)method. This method accepts a JSON object conforming to the[`RuntimeOptions`](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions#runtimeoptions_interface)interface, which defines values for`maxInstances`. For example, this function sets a limit of 100 instances in order to not overwhelm a hypothetical legacy database:  

    exports.mirrorOrdersToLegacyDatabase = functions
        .runWith({
          // Legacy database only supports 100 simultaneous connections
          maxInstances: 100,
        })
        .firestore.document("orders/{orderId}")
        .onWrite((change, context) => {
          // Connect to legacy database
        });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/runtime-options/functions/index.js#L46-L54

If an HTTP function is scaled up to the`maxInstances`limit, new requests are queued for 30 seconds and then rejected with a response code of`429 Too Many Requests`if no instance is available by then.

To learn more about best practices for using maximum instances settings, check out these[best practices for using`maxInstances`](https://cloud.google.com/functions/docs/max-instances#limits_best_practices).

### Set a service account

The default service account for 1st gen functions,<var translate="no">PROJECT_ID</var>@appspot.gserviceaccount.com (named*App Engine default service account*), has a broad set of permissions to allow you to interact with other Firebase and Google Cloud services.

You might want to override the default service account and limit a function to the exact resources needed. You can do this by creating a custom service account and assigning it to the appropriate function using the`.runWith()`method. This method takes an object with configuration options, including the`serviceAccount`property.  

    const functions = require("firebase-functions/v1");

    exports.helloWorld = functions
        .runWith({
            // This function doesn't access other Firebase project resources, so it uses a limited service account.
            serviceAccount:
                "my-limited-access-sa@", // or prefer the full form: "my-limited-access-sa@my-project.iam.gserviceaccount.com"
        })
        .https.onRequest((request, response) => {
            response.send("Hello from Firebase!");
        });

### Set timeout and memory allocation

In some cases, your functions may have special requirements for a long timeout value or a large allocation of memory. You can set these values either in the Google Cloud Console or in the function source code (Firebase only).

To set memory allocation and timeout in functions source code, use the[`runWith`](https://firebase.google.com/docs/reference/functions/function_builder.functionbuilder#runwith)parameter introduced inFirebaseSDK forCloud Functions2.0.0. This runtime option accepts a JSON object conforming to the[`RuntimeOptions`](https://firebase.google.com/docs/reference/functions/function_configuration.runtimeoptions)interface, which defines values for`timeoutSeconds`and`memory`. For example, this storage function uses 1GB of memory and times out after 300 seconds:  

    exports.convertLargeFile = functions
        .runWith({
          // Ensure the function has enough memory and time
          // to process large files
          timeoutSeconds: 300,
          memory: "1GB",
        })
        .storage.object()
        .onFinalize((object) => {
          // Do some complicated things that take a lot of memory and time
        });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/runtime-options/functions/index.js#L58-L68

The maximum value for`timeoutSeconds`is`540`, or 9 minutes. The amount of memory granted to a function corresponds to the CPU allocated for the function, as detailed in this list of valid values for`memory`:

- `128MB`--- 200MHz
- `256MB`--- 400MHz
- `512MB`--- 800MHz
- `1GB`--- 1.4 GHz
- `2GB`--- 2.4 GHz
- `4GB`--- 4.8 GHz
- `8GB`--- 4.8 GHz

To set memory allocation and timeout in theGoogle Cloudconsole:

1. In the GoogleGoogle Cloudconsole select**Cloud Functions**from the left menu.
2. Select a function by clicking on its name in the functions list.
3. Click the**Edit**icon in the top menu.
4. Select a memory allocation from the drop-down menu labeled**Memory allocated**.
5. Click**More** to display the advanced options, and enter a number of seconds in the**Timeout**text box.
6. Click**Save**to update the function.