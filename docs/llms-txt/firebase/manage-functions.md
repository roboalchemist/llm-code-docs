# Source: https://firebase.google.com/docs/functions/manage-functions.md.txt

<br />

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

By default, theFirebaseCLI looks in the`functions/`folder for the source code. If you prefer, you can[organize functions](https://firebase.google.com/docs/functions/organize-functions)in codebases or multiple sets of files.

### Clean up deployment artifacts

As part of functions deployment, container images are generated and stored inArtifact Registry. These images are not required for your deployed functions to run;Cloud Functionsfetches and retains a copy of the image on the initial deployment, but the stored artifacts are not necessary for the function to work at runtime.

While these container images are often small, they can accumulate over time and contribute to your storage costs. You might prefer to retain them for a period of time if you're planning to inspect the built artifacts or run container vulnerability scans.

To help manage storage costs,FirebaseCLI 14.0.0 and higher lets you configure an[Artifact Registrycleanup policy](https://cloud.google.com/artifact-registry/docs/repositories/cleanup-policy)for repositories that store deployment artifacts after each function deployment.

You can manually set up or edit a cleanup policy using the`functions:artifacts:setpolicy`command:  

    firebase functions:artifacts:setpolicy

By default, this command configuresArtifact Registryto automatically delete container images older than 1 day. This provides a reasonable balance between minimizing storage costs and allowing for potential inspection of recent builds.

You can customize the retention period using the`--days`option:  

    firebase functions:artifacts:setpolicy --days 7  # Delete images older than 7 days

If you deploy functions to multiple regions, you can set up a cleanup policy for a specific location using the`--location`option:  

    $ firebase functions:artifacts:setpolicy --location europe-west1

#### Opt out of artifact cleanup

If you prefer to manage image cleanup manually, or if you do not want any images deleted, you can opt out of cleanup policies entirely:  

    $ firebase functions:artifacts:setpolicy --none

This command removes any existing cleanup policy that theFirebaseCLI has set up and prevents Firebase from setting up a cleanup policy after function deployments.

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

To rename a function, create a new renamed version of the function in your source and then run two separate deployment commands. The first command deploys the newly named function, and the second command removes the previously deployed version. For example, if you have an HTTP-triggered webhook you'd like to rename, revise the code as follows:  

### Node.js

    // before
    const {onRequest}  = require('firebase-functions/v2/https');

    exports.webhook = onRequest((req, res) => {
        res.send("Hello");
    });

    // after
    const {onRequest}  = require('firebase-functions/v2/https');

    exports.webhookNew = onRequest((req, res) => {
        res.send("Hello");
    });

### Python

    # before
    from firebase_functions import https_fn

    @https_fn.on_request()
    def webhook(req: https_fn.Request) -> https_fn.Response:
        return https_fn.Response("Hello world!")

    # after
    from firebase_functions import https_fn

    @https_fn.on_request()
    def webhook_new(req: https_fn.Request) -> https_fn.Response:
        return https_fn.Response("Hello world!")

Then run the following commands to deploy the new function:  

```
# Deploy new function
firebase deploy --only functions:webhookNew

# Wait until deployment is done; now both functions are running

# Delete webhook
firebase functions:delete webhook
```

### Change a function's region or regions

If you are changing the specified[regions](https://firebase.google.com/docs/functions/locations)for a function that's handling production traffic, you can prevent event loss by performing these steps in order:

1. Rename the function, and change its region or regions as desired.
2. Deploy the renamed function, which results in temporarily running the same code in both sets of regions.
3. Delete the previous function.

For example, if you have aCloud Firestore-triggered function that is currently in the default functions region of`us-central1`, and you want to migrate it to`asia-northeast1`, you need to first modify your source code to rename the function and revise the region.  

### Node.js

    // before
    exports.firestoreTrigger = onDocumentCreated(
      "my-collection/{docId}",
      (event) => {},
    );

    // after
    exports.firestoreTriggerAsia = onDocumentCreated(
      {
        document: "my-collection/{docId}",
        region: "asia-northeast1",
      },
      (event) => {},
    );

The updated code should specify the correct event filter (in this case`document`) along with the region. See[Cloud Functionslocations](https://firebase.google.com/docs/functions/locations)for more information.

### Python

    # Before
    @firestore_fn.on_document_created("my-collection/{docId}")
    def firestore_trigger(event):
        pass

    # After
    @firestore_fn.on_document_created("my-collection/{docId}",
                                      region="asia-northeast1")
    def firestore_trigger_asia(event):
        pass

Then deploy by running:  

```
firebase deploy --only functions:firestoreTriggerAsia
```

Now there are two identical functions running:`firestoreTrigger`is running in`us-central1`, and`firestoreTriggerAsia`is running in`asia-northeast1`.

Then, delete`firestoreTrigger`:  

```
firebase functions:delete firestoreTrigger
```

Now there is only one function -`firestoreTriggerAsia`, which is running in`asia-northeast1`.

### Change a function's trigger type

As you develop yourCloud Functions for Firebasedeployment over time, you may need to change a function's trigger type for various reasons. For example, you might want to change from one type ofFirebase Realtime DatabaseorCloud Firestoreevent to another type.

It is not possible to change a function's event type by just changing the source code and running`firebase deploy`. To avoid errors, change a function's trigger type by this procedure:

1. Modify the source code to include a new function with the desired trigger type.
2. Deploy the function, which results in temporarily running both the old and new functions.
3. Explicitly delete the old function from production using theFirebaseCLI.

For instance, if you had a function that was triggered when an object was deleted, but then you enabled[object versioning](https://cloud.google.com/storage/docs/object-versioning)and would like to subscribe to the archive event instead, first rename the function and edit it to have the new trigger type.  

### Node.js

    // before
    const {onObjectDeleted} = require("firebase-functions/v2/storage");

    exports.objectDeleted = onObjectDeleted((event) => {
        // ...
    });

    // after
    const {onObjectArchived} = require("firebase-functions/v2/storage");

    exports.objectArchived = onObjectArchived((event) => {
        // ...
    });

### Python

    # before
    from firebase_functions import storage_fn

    @storage_fn.on_object_deleted()
    def object_deleted(event):
      # ...

    # after 
    from firebase_functions import storage_fn

    @storage_fn.on_object_archived()
    def object_archived(event):
      # ...

Then run the following commands to create the new function first, before deleting the old function:  

```
# Create new function objectArchived
firebase deploy --only functions:objectArchived

# Wait until deployment is done; now both objectDeleted and objectArchived are running

# Delete objectDeleted
firebase functions:delete objectDeleted
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

Node.js Versions 14 and 16 were decommissioned in early 2025. Deployment with these versions is disabled. See the[support schedule](https://cloud.google.com/functions/docs/runtime-support#node.js)for important information regarding ongoing support for these versions of Node.js.

To set the Node.js version:

You can set the version in the`engines`field in the`package.json`file that was created in your`functions/`directory during initialization. For example, to use only version 20, edit this line in`package.json`:  

      "engines": {"node": "20"}

If you are using Yarn package manager or have other specific requirements for the`engines`field, you can set the runtime for theFirebaseSDK forCloud Functionsin`firebase.json`instead:  

      {
        "functions": {
          "runtime": "nodejs20" // or nodejs22
        }
      }

The CLI uses the value set in`firebase.json`in preference to any value or range that you set separately in`package.json`.

#### Upgrade your Node.js runtime

To upgrade your Node.js runtime:

1. Make sure your project is on the[Blaze pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).
2. Make sure you are usingFirebaseCLI v11.18.0 or later.
3. Change the`engines`value in the`package.json`file that was created in your`functions/`directory during initialization. For example, if you are upgrading from version 18 to version 20, the entry should look like this:`"engines": {"node": "20"}`
4. Optionally, test your changes using the[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite).
5. Redeploy all functions.

### Choose a Node.js module system

The default module system in Node.js is CommonJS (CJS), but current Node.js versions also support ECMAScript Modules (ESM).Cloud Functionssupports both.

By default, your functions use CommonJS. That means imports and exports look like this:  

    const {onRequest} = require("firebase-functions/https");

    exports.helloWorld = onRequest(async (req, res) => res.send("Hello from Firebase!"));

To use ESM instead, set the`"type": "module"`field in your`package.json`file :  

      {
       ...
       "type": "module",
       ...
      }

Once you set this, use ESM`import`and`export`syntax:  

    import {onRequest} from "firebase-functions/https";

    export const helloWorld = onRequest(async (req, res) => res.send("Hello from Firebase!"));

Both module systems are fully supported. You can choose whichever best fits your project. Learn more in the[Node.js documentation on modules](https://nodejs.org/api/esm.html).

### Set Python version

FirebaseSDK forCloud Functionsversions 12.0.0 and higher allow selection of the Python runtime. Set the runtime version in`firebase.json`as shown:  

      {
        "functions": {
          "runtime": "python310" // or python311
        }
      }

### Control scaling behavior

By default,Cloud Functions for Firebasescales the number of running instances based on the number of incoming requests, potentially scaling down to zero instances in times of reduced traffic. However, if your app requires reduced latency and you want to limit the number of cold starts, you can change this default behavior by specifying a minimum number of container instances to be kept warm and ready to serve requests.

Similarly, you can set a maximum number to limit the scaling of instances in response to incoming requests. Use this setting as a way to control your costs or to limit the number of connections to a backing service such as to a database.

Using these settings together with the per-instance*concurrency*setting (new in 2nd gen), you can control and tune the scaling behavior for your functions. The nature of your application and function will determine which settings are most cost effective and will result in the best performance.

For some apps with low traffic, a lower CPU option without multi-concurrency is optimal. For others where cold starts are a critical issue, setting high concurrency and minimum instances means that a set of instances are always kept warm to handle large spikes in traffic.

For smaller-scale apps that receive very little traffic, setting low maximum instances with high concurrency means that the app can handle bursts of traffic without incurring excessive costs. However, keep in mind that when maximum instances is set too low, requests may be dropped when the ceiling is reached.

#### Allow concurrent requests

InCloud Functions for Firebase(1st gen), each instance could handle one request at a time, so scaling behavior was set only with minimum and maximum instances settings. In addition to controlling the number of instances, inCloud Functions for Firebase(2nd gen) you can control the number of requests each instance can serve at the same time with the`concurrency`option. The default value for concurrency is 80, but you can set it to any integer between 1 and 1000.

Functions with higher concurrency settings can absorb spikes of traffic without cold starting because each instance likely has some headroom. If an instance is configured to handle up to 50 concurrent requests but is currently handling only 25, it can handle a spike of 25 additional requests without requiring a new instance to cold start. By contrast, with a concurrency setting of just 1, that spike in requests could lead to 25 cold starts.

This simplified scenario demonstrates the potential efficiency gains of concurrency. In reality, scaling behavior to optimize efficiency and reduce cold starts with concurrency is more complex. Concurrency inCloud Functions for Firebase2nd gen is powered byCloud Run, and followsCloud Run's rules of[container instance autoscaling](https://cloud.google.com/run/docs/about-instance-autoscaling).
| **Important:** Concurrency is available only to functions with at least 1 full CPU. Setting a function's CPU to a fractional value or setting CPU to`gcf_gen1`for a function with less than 2GB RAM will disable concurrency. See[Override CPU defaults](https://firebase.google.com/docs/functions/manage-functions#override-CPU).

When experimenting with higher concurrency settings inCloud Functions for Firebase(2nd gen), keep the following in mind:

- Higher concurrency settings may require higher CPU and RAM for optimal performance until reaching a practical limit. A function that does heavy image or video processing, for example, might lack the resources to handle 1000 concurrent requests, even when its CPU and RAM settings are maximized.
- SinceCloud Functions for Firebase(2nd gen) is powered byCloud Run, you can refer also toGoogle Cloudguidance for[optimizing concurrency](https://cloud.google.com/run/docs/tips/general#optimize_concurrency).
- Make sure to test multiconcurrency thoroughly in a test environment before switching to multiconcurrency in production.

#### Keep a minimum number of instances warm

You can set minimum number of instances for a function in source code. For example, this function sets a minimum of 5 instances to keep warm:  

### Node.js

    const { onCall } = require("firebase-functions/v2/https");

    exports.getAutocompleteResponse = onCall(
      {
        // Keep 5 instances warm for this latency-critical function
        minInstances: 5,
      },
      (event) => {
        // Autocomplete user's search term
      }
    );

### Python

    @https_fn.on_call(min_instances=5)
    def get_autocomplete_response(event: https_fn.CallableRequest) -> https_fn.Response:

| **Note:** A minimum number of instances kept running incur billing costs at idle rates. A function with the 1st gen default 256MiB memory allocation costs about $3/mo (with[`gcf_gen_1`CPU allocation](https://firebase.google.com/docs/functions/manage-functions#override-CPU)and concurrency disabled) or about $8/mo with 1CPU and concurrency enabled. TheFirebaseCLI provides a cost estimate at deployment time for functions with reserved minimum instances. Refer to[Cloud Runpricing](https://cloud.google.com/run/pricing)to calculate costs.

Here are some things to consider when setting a minimum instances value:

- IfCloud Functions for Firebasescales your app above your setting, you'll experience a cold start for each instance above that threshold.
- Cold starts have the most severe effect on apps with spiky traffic. If your app has spiky traffic and you set a value high enough that cold starts are reduced on each traffic increase, you'll see significantly reduced latency. For apps with constant traffic, cold starts are not likely to severely affect performance.
- Setting minimum instances can make sense for production environments, but should usually be avoided in testing environments. To scale to zero in your test project but still reduce cold starts in your production project, you can set a minimum instances value in your parameterized configuration:

  ### Node.js

      const { onRequest } = require('firebase-functions/https');
      const { defineInt, defineString } = require('firebase-functions/params');

      // Define some parameters
      const minInstancesConfig = defineInt('HELLO_WORLD_MININSTANCES');
      const welcomeMessage = defineString('WELCOME_MESSAGE');

      // To use configured parameters inside the config for a function, provide them 
      // directly. To use them at runtime, call .value() on them.
      export const helloWorld = onRequest(
        { minInstances: minInstancesConfig },
      (req, res) => {
          res.send(`${welcomeMessage.value()}! I am a function.`);
        }
      );

  ### Python

      MIN_INSTANCES = params.IntParam("HELLO_WORLD_MININSTANCES")
      WELCOME_MESSAGE = params.StringParam("WELCOME_MESSAGE")

      @https_fn.on_request(min_instances=MIN_INSTANCES.value())
      def get_autocomplete_response(event: https_fn.Request) -> https_fn.Response:
          return https_fn.Response(f"{WELCOME_MESSAGE.value()} I'm a function.")

#### Limit the maximum number of instances for a function

You can set a value for maximum instances in function source code. For example, this function sets a limit of 100 instances in order to not overwhelm a hypothetical legacy database:  

### Node.js

    const { onMessagePublished } = require("firebase-functions/v2/pubsub");

    exports.mirrorevents = onMessagePublished(
      { topic: "topic-name", maxInstances: 100 },
      (event) => {
        // Connect to legacy database
      }
    );

### Python

    @pubsub_fn.on_message_published(topic="topic-name", max_instances=100)
    def mirrorevents(event: pubsub_fn.CloudEvent):
    #  Connect to legacy database

| **Note:** for more control over invocation rates and throttling, consider[task queue functions](https://firebase.google.com/docs/functions/task-functions).

If an HTTP function is scaled up to the maximum instances limit, new requests are queued for 30 seconds and then rejected with a response code of`429 Too Many Requests`if no instance is available by then.

To learn more about best practices for using maximum instances settings, check out these[best practices for setting maximum instances](https://cloud.google.com/functions/docs/max-instances#limits_best_practices).

### Set a service account

The default service accounts for functions have a broad set of permissions to allow you to interact with other Firebase and Google Cloud services:

- **2nd gen functions:** <var translate="no">PROJECT_NUMBER</var>-compute@developer.gserviceaccount.com (named*Compute Engine default service account*)
- **1st gen functions:** <var translate="no">PROJECT_ID</var>@appspot.gserviceaccount.com (named*App Engine default service account*)

You might want to override the default service account and limit a function to the exact resources needed. You can do this by creating a custom service account and assigning it to the appropriate function using the`serviceAccount`configuration value:  

    const { onRequest } = require("firebase-functions/https");

    exports.helloWorld = onRequest(
        {
            // This function doesn't access other Firebase project resources, so it uses a limited service account.
            serviceAccount:
                "my-limited-access-sa@", // or prefer the full form: "my-limited-access-sa@my-project.iam.gserviceaccount.com"
        },
        (request, response) => {
            response.send("Hello from Firebase!");
        },
    );

If you want to set the same service account for all of your functions, you can do that with the[setGlobalOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions#setglobaloptions)function.

### Set timeout and memory allocation

In some cases, your functions may have special requirements for a long timeout value or a large allocation of memory. You can set these values either in theGoogle Cloudconsole or in the function source code (Firebase only), using timeout values within these maximum duration limits:

- HTTP and callable functions: 3600 seconds (60 minutes)
- Scheduled/Task queue functions: 1800 seconds (30 minutes)
- Other event-driven functions: 540 seconds (9 minutes)

To set memory allocation and timeout in functions source code, use the global options for memory and timeout seconds to customize the virtual machine running your functions. For example, thisCloud Storagefunction uses 1GiB of memory and times out after 300 seconds:  

### Node.js

    exports.convertLargeFile = onObjectFinalized({
      timeoutSeconds: 300,
      memory: "1GiB",
    }, (event) => {
      // Do some complicated things that take a lot of memory and time
    });

### Python

    @storage_fn.on_object_finalized(timeout_sec=300, memory=options.MemoryOption.GB_1)
    def convert_large_file(event: storage_fn.CloudEvent):
    # Do some complicated things that take a lot of memory and time.

To set memory allocation and timeout in theGoogle Cloudconsole:

1. In theGoogle Cloudconsole select**Cloud Functions for Firebase**from the left menu.
2. Select a function by clicking on its name in the functions list.
3. Click the**Edit**icon in the top menu.
4. Select a memory allocation from the drop-down menu labeled**Memory allocated**.
5. Click**More** to display the advanced options, and enter a number of seconds in the**Timeout**text box.
6. Click**Save**to update the function.

### Override CPU defaults

Up to 2GB of memory allocated, each function inCloud Functions for Firebase(2nd gen) defaults to one CPU, and then increases to 2 CPU for 4 and 8GB. Note that*this is significantly different from 1st gen default behavior*in ways that could lead to slightly higher costs for low-memory functions as expressed in the following table:

| RAM allocated | Version 1 default CPU (fractional) | Version 2 default CPU | Price increase per ms |
|---------------|------------------------------------|-----------------------|-----------------------|
| 128MB         | 1/12                               | 1                     | 10.5x                 |
| 256MB         | 1/6                                | 1                     | 5.3x                  |
| 512MB         | 1/3                                | 1                     | 2.7x                  |
| 1GB           | 7/12                               | 1                     | 1.6x                  |
| 2GB           | 1                                  | 1                     | 1x                    |
| 4GB           | 2                                  | 2                     | 1x                    |
| 8GB           | 2                                  | 2                     | 1x                    |
| 16 GB         | n/a                                | 4                     | n/a                   |

If you prefer 1st gen behavior for your 2nd gen functions, set 1st gen defaults as a global option:  

### Node.js

    // Turn off Firebase defaults
    setGlobalOptions({ cpu: 'gcf_gen1' });

### Python

    # Use 1st gen behavior
    set_global_options(cpu="gcf_gen1")

For CPU-intensive functions, 2nd gen provides the flexibility to configure additional CPU. You can boost CPU on a per-function basis as shown:  

### Node.js

    // Boost CPU in a function:
    export const analyzeImage = onObjectFinalized({ cpu: 2 }, (event) => {
      // computer vision goes here
    });

### Python

    # Boost CPU in a function:
    @storage_fn.on_object_finalized(cpu=2)
    def analyze_image(event: storage_fn.CloudEvent):
    # computer vision goes here