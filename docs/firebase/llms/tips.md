# Source: https://firebase.google.com/docs/functions/tips.md.txt

<br />

This document describes best practices for designing, implementing, testing, and deployingCloud Functions.
| **Note:** Several of the recommendations in this document center around what is known as a*cold start*. Functions are stateless, and the execution environment is often initialized from scratch, which is called a cold start. Cold starts can take significant amounts of time to complete. It is best practice to avoid unnecessary cold starts, and to streamline the cold start process to whatever extent possible (for example, by avoiding unnecessary dependencies).

## Correctness

This section describes general best practices for designing and implementingCloud Functions.

### Write idempotent functions

Your functions should produce the same result even if they are called multiple times. This lets you retry an invocation if the previous invocation fails part way through your code. For more information, see[retrying event-driven functions](https://firebase.google.com/docs/functions/retries).

### Do not start background activities

Background activity is anything that happens after your function has terminated. A function invocation finishes once the function returns or otherwise signals completion, such as by calling the`callback`argument in Node.js event-driven functions. Any code run after graceful termination cannot access the CPU and will not make any progress.
| **Note:** If a Node.js event-driven function returns a Promise,Cloud Functionsensures that the Promise is settled before terminating.

In addition, when a subsequent invocation is executed in the same environment, your background activity resumes, interfering with the new invocation. This may lead to unexpected behavior and errors that are hard to diagnose. Accessing the network after a function terminates usually leads to connections being reset (`ECONNRESET`error code).

Background activity can often be detected in logs from individual invocations, by finding anything that is logged after the line saying that the invocation finished. Background activity can sometimes be buried deeper in the code, especially when asynchronous operations such as callbacks or timers are present. Review your code to make sure all asynchronous operations finish before you terminate the function.

### Always delete temporary files

Local disk storage in the temporary directory is an in-memory filesystem. Files that you write consume memory available to your function, and sometimes persist between invocations. Failing to explicitly delete these files may eventually lead to an out-of-memory error and a subsequent cold start.

You can see the memory used by an individual function by selecting it in the[list of functions](https://console.cloud.google.com/functions/list)in the Google Cloud console and choosing the*Memory usage*plot.

If you need access to long term storage, consider usingCloud Runvolume mounts with[Cloud Storage](https://firebase.google.com/run/docs/configuring/services/cloud-storage-volume-mounts)or[NFS volumes](https://firebase.google.com/run/docs/configuring/services/nfs-volume-mounts).

You can reduce memory requirements when processing larger files using pipelining. For example, you can process a file on Cloud Storage by creating a read stream, passing it through a stream-based process, and writing the output stream directly to Cloud Storage.

### Functions Framework

To ensure that the same dependencies are installed consistently across environments, we recommend that you include the Functions Framework library in your package manager and pin the dependency to a specific version of Functions Framework.

To do this, include your preferred version in the relevant lock file (for example,`package-lock.json`for Node.js, or`requirements.txt`for Python).

If Functions Framework is not explicitly listed as a dependency, it will automatically be added during the build process using the latest available version.

## Tools

This section provides guidelines on how to use tools to implement, test, and interact withCloud Functions.

### Local development

Function deployment takes a bit of time, so it is often faster to test the code of your function locally.
Firebase developers can use the[Firebase CLICloud FunctionsEmulator](https://firebase.google.com/docs/functions/local-emulator).

### Avoid deployment timeouts during initialization

If your function deployment fails with a timeout error, it likely means that your function's global scope code is taking too long to execute during the deployment process.

TheFirebaseCLI has a default timeout for discovering your functions during deployment. If initialization logic in your functions' source code (loading modules, making network calls, so on) exceeds this timeout, deployment may fail.

To avoid the timeout, use one of the following strategies:

#### (Recommended) use`onInit()`to defer initialization

Use the`onInit()`hook to avoid running the initialization code during deployment. Code inside the`onInit()`hook will only run when the function is deployed to Cloud Run functions, not during the deployment process itself.  

### Node.js

```javascript
const { onInit } = require('firebase-functions/v2/core');
const { onRequest } = require('firebase-functions/v2/https');

// Example of a slow initialization task
function slowInitialization() {
  // Simulate a long-running operation (e.g., loading a large model, network request).
  return new Promise(resolve => {
      setTimeout(() => {
          console.log("Slow initialization complete");
          resolve("Initialized Value");
      }, 20000); // Simulate a 20-second delay
  });
}
let initializedValue;

onInit(async () => {
  initializedValue = await slowInitialization();
});

exports.myFunction = onRequest((req, res) => {
  // Access the initialized value. It will be ready after the first invocation.
  res.send(`Value: ${initializedValue}`);
});
```

### Python

```python
from firebase_functions.core import init
from firebase_functions import https_fn
import time

# Example of a slow initialization task
def _slow_initialization():
  time.sleep(20)  # Simulate a 20-second delay
  print("Slow initialization complete")
  return "Initialized Value"

_initialized_value = None

@init
def initialize():
  global _initialized_value
  _initialized_value = _slow_initialization()

@https_fn.on_request()
def my_function(req: https_fn.Request) -> https_fn.Response:
  # Access the initialized value. It will be ready after the first invocation.
  return https_fn.Response(f"Value: {_initialized_value}")
```

#### (Alternative) Increase the Discovery Timeout

If you cannot refactor your code to use`onInit()`, you can increase the CLI's deployment timeout using the`FUNCTIONS_DISCOVERY_TIMEOUT`environment variable:  

    $ export FUNCTIONS_DISCOVERY_TIMEOUT=30
    $ firebase deploy --only functions

### Use Sendgrid to send emails

Cloud Functionsdoes not allow outbound connections on port 25, so you cannot make non-secure connections to an SMTP server. The recommended way to send emails is to use a third party service such as[SendGrid](https://sendgrid.com/). You can find other options for sending email in the[Sending Email from an Instance](https://cloud.google.com/compute/docs/tutorials/sending-mail)tutorial for Google Compute Engine.

## Performance

This section describes best practices for optimizing performance.

### Avoid low concurrency

Because cold starts are expensive, being able to reuse recently started instances during a spike is a great optimization to handle load. Limiting concurrency limits how existing instances can be leveraged, therefore incurring more cold starts.
[Increasing concurrency](https://firebase.google.com/docs/functions/manage-functions?gen=2nd#allow_concurrent_requests)helps defer multiple requests per instance, making spikes of load easier to handle.

<br />

| **Note:** As efficiency increases and their required number is reduced, individual function instances may use more memory to hold requests and require more CPU to process them.

### Use dependencies wisely

Because functions are stateless, the execution environment is often initialized from scratch (during what is known as a*cold start*). When a cold start occurs, the global context of the function is evaluated.

If your functions import modules, the load time for those modules can add to the invocation latency during a cold start. You can reduce this latency, as well as the time needed to deploy your function, by loading dependencies correctly and not loading dependencies your function doesn't use.

### Use global variables to reuse objects in future invocations

There is no guarantee that the state of a function will be preserved for future invocations. However,Cloud Functionsoften recycles the execution environment of a previous invocation. If you declare a variable in global scope, its value can be reused in subsequent invocations without having to be recomputed.

This way you can cache objects that may be expensive to recreate on each function invocation. Moving such objects from the function body to global scope may result in significant performance improvements. The following example creates a heavy object only once per function instance, and shares it across all function invocations reaching the given instance:  

### Node.js

```javascript
console.log('Global scope');
const perInstance = heavyComputation();
const functions = require('firebase-functions');

exports.function = functions.https.onRequest((req, res) => {
  console.log('Function invocation');
  const perFunction = lightweightComputation();

  res.send(`Per instance: ${perInstance}, per function: ${perFunction}`);
});
```

### Python

```python
import time

from firebase_functions import https_fn

# Placeholder
def heavy_computation():
  return time.time()

# Placeholder
def light_computation():
  return time.time()

# Global (instance-wide) scope
# This computation runs at instance cold-start
instance_var = heavy_computation()

@https_fn.on_request()
def scope_demo(request):

  # Per-function scope
  # This computation runs every time this function is called
  function_var = light_computation()
  return https_fn.Response(f"Instance: {instance_var}; function: {function_var}")
  
```

This HTTP function takes a request object (`flask.Request`), and returns the response text, or any set of values that can be turned into a`Response`object using[`make_response`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.make_response).

It is particularly important to cache network connections, library references, and API client objects in global scope. See[Optimizing networking](https://firebase.google.com/docs/functions/networking)for examples.
| **Note:** Background tasks should not be performed outside of the duration of a request. If you need to initialize a global variable with the result from an expensive background task, perform the task during your function's execution and store its result before sending a response.

### Reduce cold starts by setting a minimum number of instances

By default, Cloud Functions scales the number of instances based on the number of incoming requests. You can change this default behavior by setting a minimum number of instances that Cloud Functions must keep ready to serve requests. Setting a minimum number of instances reduces cold starts of your application. We recommend setting a minimum number of instances, and completing initialization at load time, if your application is latency-sensitive.
See[Control scaling behavior](https://firebase.google.com/docs/functions/manage-functions#min-max-instances)for more information on these runtime options.

<br />

### Notes about cold start and initialization

Global initialization happens at load time. Without it, the first request would need to complete initialization and load modules, thereby incurring higher latency.

However, global initialization also has an impact on cold starts. To minimize this impact, initialize only what is needed for the first request, to keep the first request's latency as low as possible.

This is especially important if you configured min instances as described above for a latency-sensitive function. In that scenario, completing initialization at load time and caching useful data ensures that the first request doesn't need to do it and is served with low latency.

If you initialize variables in global scope, depending on the language, long initialization times can result in two behaviors: - for some combination of languages and async libraries, the function framework can run asynchronously and return immediately, causing code to continue running in the background, which could cause issues such as[not being able to access the CPU](https://firebase.google.com/docs/functions/tips#do_not_start_background_activities). To avoid this, you should block on module initialization as described below. This also ensures that requests are not served until the initialization is complete. - on the other hand, if the initialization is synchronous, the long initialization time will cause longer cold starts, which could be an issue especially with low concurrency functions during spikes of load.
| **Note:** if you chose to use longer cold start times and min_instances, we also recommend that you use high concurrency in order to better support spikes of traffic.

#### Example of prewarming an async node.js library

Node.js with Firestore is an example of async node.js library. In order to take advantage of min_instances, the following code completes loading and initialization at load time, blocking on the module loading.

TLA is used, which means ES6 is required, using an`.mjs`extension for the node.js code or adding`type: module`to the package.json file.  

```javascript
{
  "main": "main.js",
  "type": "module",
  "dependencies": {
    "@google-cloud/firestore": "^7.10.0",
    "@google-cloud/functions-framework": "^3.4.5"
  }
}
```  

### Node.js

```javascript
import Firestore from '@google-cloud/firestore';
import * as functions from '@google-cloud/functions-framework';

const firestore = new Firestore({preferRest: true});

// Pre-warm firestore connection pool, and preload our global config
// document in cache. In order to ensure no other request comes in,
// block the module loading with a synchronous global request:
const config = await firestore.collection('collection').doc('config').get();

functions.http('fetch', (req, res) => {

// Do something with config and firestore client, which are now preloaded
// and will execute at lower latency.
});
```

#### Examples of global initialization

### Node.js

```javascript
const functions = require('firebase-functions');
let myCostlyVariable;

exports.function = functions.https.onRequest((req, res) => {
  doUsualWork();
  if(unlikelyCondition()){
      myCostlyVariable = myCostlyVariable || buildCostlyVariable();
  }
  res.status(200).send('OK');
});
```

### Python

```python
from firebase_functions import https_fn

# Always initialized (at cold-start)
non_lazy_global = file_wide_computation()

# Declared at cold-start, but only initialized if/when the function executes
lazy_global = None

@https_fn.on_request()
def lazy_globals(request):

  global lazy_global, non_lazy_global

  # This value is initialized only if (and when) the function is called
  if not lazy_global:
      lazy_global = function_specific_computation()

  return https_fn.Response(f"Lazy: {lazy_global}, non-lazy: {non_lazy_global}.")
  
```

This HTTP function uses lazily-initialized globals. It takes a request object (`flask.Request`), and returns the response text, or any set of values that can be turned into a`Response`object using[`make_response`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.make_response).

This is particularly important if you define several functions in a single file, and different functions use different variables. Unless you use lazy initialization, you may waste resources on variables that are initialized but never used.
| **Note:** this technique can also be used when importing dependencies in Node.js and Python, albeit at the expense of code readability.

### Additional resources

Find out more about optimizing performance in the "Google Cloud Performance Atlas" video[Cloud FunctionsCold Boot Time](https://www.youtube.com/watch?v=IOXrwFqR6kY).