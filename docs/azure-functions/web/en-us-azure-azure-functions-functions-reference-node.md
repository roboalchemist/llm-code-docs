# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript

Title: Node.js developer reference for Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript

Published Time: Mon, 02 Mar 2026 18:37:16 GMT

Markdown Content:
This guide is an introduction to developing Azure Functions using JavaScript or TypeScript. The article assumes that you have already read the [Azure Functions developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference).

Important

The content of this article changes based on your choice of the Node.js programming model in the selector at the top of this page. The version you choose should match the version of the [`@azure/functions`](https://www.npmjs.com/package/@azure/functions) npm package you're using in your app. If you don't have that package listed in your `package.json`, the default is v3. Learn more about the differences between v3 and v4 in the [migration guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-node-upgrade-v4).

As a Node.js developer, you might also be interested in one of the following articles:

| Getting started | Concepts | Guided learning |
| --- | --- | --- |
| * [Node.js function using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code?pivot=programming-language-javascript) * [Node.js function with terminal/command prompt](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-javascript) * [Node.js function using the Azure portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal) | * [Developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference) * [Hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) * [Performance considerations](https://learn.microsoft.com/en-us/azure/azure-functions/functions-best-practices) | * [Create serverless applications](https://learn.microsoft.com/en-us/training/paths/create-serverless-applications/) * [Refactor Node.js and Express APIs to Serverless APIs](https://learn.microsoft.com/en-us/training/modules/shift-nodejs-express-apis-serverless/) |

*   The Node.js programming model shouldn't be confused with the Azure Functions runtime: 
    *   **Programming model**: Defines how you author your code and is specific to JavaScript and TypeScript.
    *   **Runtime**: Defines underlying behavior of Azure Functions and is shared across all languages.

*   The version of the programming model is strictly tied to the version of the [`@azure/functions`](https://www.npmjs.com/package/@azure/functions) npm package. It's versioned independently of the [runtime](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions). Both the runtime and the programming model use the number 4 as their latest major version, but that's a coincidence.
*   You can't mix the v3 and v4 programming models in the same function app. As soon as you register one v4 function in your app, any v3 functions registered in _function.json_ files are ignored.

The following table shows each version of the Node.js programming model along with its supported versions of the Azure Functions runtime and Node.js.

| [Programming Model Version](https://www.npmjs.com/package/@azure/functions?activeTab=versions) | Support Level | [Functions Runtime Version](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions) | [Node.js Version](https://github.com/nodejs/release#release-schedule) | Description |
| --- | --- | --- | --- | --- |
| 4.x | GA | 4.25+ | 22.x 20.x, 18.x | Supports a flexible file structure and code-centric approach to triggers and bindings. |
| 3.x | GA | 4.x | 20.x, 18.x, 16.x, 14.x | Requires a specific file structure with your triggers and bindings declared in a "function.json" file |
| 2.x | n/a | 3.x | 14.x, 12.x, 10.x | Reached end of support on December 13, 2022. See [Functions Versions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions) for more info. |
| 1.x | n/a | 2.x | 10.x, 8.x | Reached end of support on December 13, 2022. See [Functions Versions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions) for more info. |

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_1_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_1_typescript)

The required folder structure for a JavaScript project looks like the following example:

```
<project_root>/
 | - .vscode/
 | - node_modules/
 | - myFirstFunction/
 | | - index.js
 | | - function.json
 | - mySecondFunction/
 | | - index.js
 | | - function.json
 | - .funcignore
 | - host.json
 | - local.settings.json
 | - package.json
```

The main project folder, _<project\_root>_, can contain the following files:

*   **.vscode/**: (Optional) Contains the stored Visual Studio Code configuration. To learn more, see [Visual Studio Code settings](https://code.visualstudio.com/docs/getstarted/settings).
*   **myFirstFunction/function.json**: Contains configuration for the function's trigger, inputs, and outputs. The name of the directory determines the name of your function.
*   **myFirstFunction/index.js**: Stores your function code. To change this default file path, see [using scriptFile](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#using-scriptfile).
*   **.funcignore**: (Optional) Declares files that shouldn't get published to Azure. Usually, this file contains _.vscode/_ to ignore your editor setting, _test/_ to ignore test cases, and _local.settings.json_ to prevent local app settings being published.
*   **host.json**: Contains configuration options that affect all functions in a function app instance. This file does get published to Azure. Not all options are supported when running locally. To learn more, see [host.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-host-json).
*   **local.settings.json**: Used to store app settings and connection strings when it's running locally. This file doesn't get published to Azure. To learn more, see [local.settings.file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file).
*   **package.json**: Contains configuration options like a list of package dependencies, the main entrypoint, and scripts.

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_2_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_2_typescript)

The recommended folder structure for a JavaScript project looks like the following example:

```
<project_root>/
 | - .vscode/
 | - node_modules/
 | - src/
 | | - functions/
 | | | - myFirstFunction.js
 | | | - mySecondFunction.js
 | - test/
 | | - functions/
 | | | - myFirstFunction.test.js
 | | | - mySecondFunction.test.js
 | - .funcignore
 | - host.json
 | - local.settings.json
 | - package.json
```

The main project folder, _<project\_root>_, can contain the following files:

*   **.vscode/**: (Optional) Contains the stored Visual Studio Code configuration. To learn more, see [Visual Studio Code settings](https://code.visualstudio.com/docs/getstarted/settings).
*   **src/functions/**: The default location for all functions and their related triggers and bindings.
*   **test/**: (Optional) Contains the test cases of your function app.
*   **.funcignore**: (Optional) Declares files that shouldn't get published to Azure. Usually, this file contains _.vscode/_ to ignore your editor setting, _test/_ to ignore test cases, and _local.settings.json_ to prevent local app settings being published.
*   **host.json**: Contains configuration options that affect all functions in a function app instance. This file does get published to Azure. Not all options are supported when running locally. To learn more, see [host.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-host-json).
*   **local.settings.json**: Used to store app settings and connection strings when it's running locally. This file doesn't get published to Azure. To learn more, see [local.settings.file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file).
*   **package.json**: Contains configuration options like a list of package dependencies, the main entrypoint, and scripts.

The v3 model registers a function based on the existence of two files. First, you need a `function.json` file located in a folder one level down from the root of your app. Second, you need a JavaScript file that [exports](https://nodejs.org/api/modules.html#modules_module_exports) your function. By default, the model looks for an `index.js` file in the same folder as your `function.json`. If you're using TypeScript, you must use the [`scriptFile`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#using-scriptfile) property in `function.json` to point to the compiled JavaScript file. To customize the file location or export name of your function, see [configuring your function's entry point](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node#configure-function-entry-point).

The function you export should always be declared as an [`async function`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/async_function) in the v3 model. You can export a synchronous function, but then you must call [`context.done()`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#contextdone) to signal that your function is completed, which is deprecated and not recommended.

Your function is passed an [invocation `context`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#invocation-context) as the first argument and your [inputs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#inputs) as the remaining arguments.

The following example is a simple function that logs that it was triggered and responds with `Hello, world!`:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_3_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_3_typescript)

```
{
  "bindings": [
    {
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "authLevel": "anonymous",
      "methods": ["get", "post"]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "res"
    }
  ]
}
```

```
module.exports = async function (context, request) {
  context.log("Http function was triggered.");
  context.res = { body: "Hello, world!" };
};
```

The programming model loads your functions based on the `main` field in your `package.json`. You can set the `main` field to a single file or multiple files by using a [glob pattern](https://wikipedia.org/wiki/Glob_(programming)). The following table shows example values for the `main` field:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_4_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_4_typescript)

| Example | Description |
| --- | --- |
| **`src/index.js`** | Register functions from a single root file. |
| **`src/functions/*.js`** | Register each function from its own file. |
| **`src/{index.js,functions/*.js}`** | A combination where you register each function from its own file, but you still have a root file for general app-level code. |

In order to register a function, you must import the `app` object from the `@azure/functions` npm module and call the method specific to your trigger type. The first argument when registering a function is the function name. The second argument is an `options` object specifying configuration for your trigger, your handler, and any other inputs or outputs. In some cases where trigger configuration isn't necessary, you can pass the handler directly as the second argument instead of an `options` object.

Registering a function can be done from any file in your project, as long as that file is loaded (directly or indirectly) based on the `main` field in your `package.json` file. The function should be registered at a global scope because you can't register functions once executions start.

The following example is a simple function that logs that it was triggered and responds with `Hello, world!`:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_5_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_5_typescript)

```
const { app } = require("@azure/functions");

app.http("helloWorld1", {
  methods: ["POST", "GET"],
  handler: async (request, context) => {
    context.log("Http function was triggered.");
    return { body: "Hello, world!" };
  },
});
```

Your function is required to have exactly one primary input called the trigger. It might also have secondary inputs and/or outputs. Inputs and outputs are configured in your `function.json` files and are also referred to as [bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings).

Inputs are bindings with `direction` set to `in`. The main difference between a trigger and a secondary input is that the `type` for a trigger ends in `Trigger`, for example type [`blobTrigger`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger) vs type [`blob`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input). Most functions only use a trigger, and not many secondary input types are supported.

Inputs can be accessed in several ways:

*   **_[Recommended]_ As arguments passed to your function:** Use the arguments in the same order that they're defined in `function.json`. The `name` property defined in `function.json` doesn't need to match the name of your argument, although we recommend it for the sake of organization.

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_6_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_6_typescript)

```
module.exports = async function (context, myTrigger, myInput, myOtherInput) { ... };
```

* * *

*   **As properties of [`context.bindings`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#contextbindings):** Use the key matching the `name` property defined in `function.json`.

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_7_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_7_typescript)

```
module.exports = async function (context) {
  context.log("This is myTrigger: " + context.bindings.myTrigger);
  context.log("This is myInput: " + context.bindings.myInput);
  context.log("This is myOtherInput: " + context.bindings.myOtherInput);
};
```

* * *

Outputs are bindings with `direction` set to `out` and can be set in several ways:

*   **_[Recommended for single output]_ Return the value directly:** If you're using an async function, you can return the value directly. You must change the `name` property of the output binding to `$return` in `function.json` like in the following example:

```
{
  "name": "$return",
  "type": "http",
  "direction": "out"
}
```

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_8_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_8_typescript)

```
module.exports = async function (context, request) {
  return {
    body: "Hello, world!",
  };
};
```

* * *

*   **_[Recommended for multiple outputs]_ Return an object containing all outputs:** If you're using an async function, you can return an object with a property matching the name of each binding in your `function.json`. The following example uses output bindings named "httpResponse" and "queueOutput":

```
{
    "name": "httpResponse",
    "type": "http",
    "direction": "out"
},
{
    "name": "queueOutput",
    "type": "queue",
    "direction": "out",
    "queueName": "helloworldqueue",
    "connection": "storage_APPSETTING"
}
```

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_9_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_9_typescript)

```
module.exports = async function (context, request) {
  let message = "Hello, world!";
  return {
    httpResponse: {
      body: message,
    },
    queueOutput: message,
  };
};
```

* * *

*   **Set values on `context.bindings`:** If you're not using an async function or you don't want to use the previous options, you can set values directly on `context.bindings`, where the key matches the name of the binding. The following example uses output bindings named "httpResponse" and "queueOutput":

```
{
    "name": "httpResponse",
    "type": "http",
    "direction": "out"
},
{
    "name": "queueOutput",
    "type": "queue",
    "direction": "out",
    "queueName": "helloworldqueue",
    "connection": "storage_APPSETTING"
}
```

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_10_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_10_typescript)

```
module.exports = async function (context, request) {
  let message = "Hello, world!";
  context.bindings.httpResponse = {
    body: message,
  };
  context.bindings.queueOutput = message;
};
```

* * *

You can use the `dataType` property on an input binding to change the type of your input. However, the approach has some limitations:

*   In Node.js, only `string` and `binary` are supported (`stream` isn't)
*   For HTTP inputs, the `dataType` property is ignored. Instead, use properties on the `request` object to get the body in your desired format. For more information, see [HTTP request](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#http-request).

In the following example of a [storage queue trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger), the default type of `myQueueItem` is a `string`, but if you set `dataType` to `binary`, the type changes to a Node.js `Buffer`.

```
{
  "name": "myQueueItem",
  "type": "queueTrigger",
  "direction": "in",
  "queueName": "helloworldqueue",
  "connection": "storage_APPSETTING",
  "dataType": "binary"
}
```

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_11_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_11_typescript)

```
const { Buffer } = require("node:buffer");

module.exports = async function (context, myQueueItem) {
  if (typeof myQueueItem === "string") {
    context.log("myQueueItem is a string");
  } else if (Buffer.isBuffer(myQueueItem)) {
    context.log("myQueueItem is a buffer");
  }
};
```

Your function is required to have exactly one primary input called the trigger. It might also have secondary inputs, a primary output called the return output, and/or secondary outputs. Inputs and outputs are also referred to as [bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings) outside the context of the Node.js programming model. Before v4 of the model, these bindings were configured in `function.json` files.

The trigger is the only required input or output. For most trigger types, you register a function by using a method on the `app` object named after the trigger type. You can specify configuration specific to the trigger directly on the `options` argument. For example, an HTTP trigger allows you to specify a route. During execution, the value corresponding to this trigger is passed in as the first argument to your handler.

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_12_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_12_typescript)

```
const { app } = require('@azure/functions');

app.http('helloWorld1', {
    route: 'hello/world',
    handler: async (request, context) => {
        ...
    }
});
```

The return output is optional, and in some cases configured by default. For example, an HTTP trigger registered with `app.http` is configured to return an HTTP response output automatically. For most output types, you specify the return configuration on the `options` argument with the help of the `output` object exported from the `@azure/functions` module. During execution, you set this output by returning it from your handler.

The following example uses a [timer trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer) and a [storage queue output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-output):

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_13_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_13_typescript)

```
const { app, output } = require('@azure/functions');

app.timer('timerTrigger1', {
    schedule: '0 */5 * * * *',
    return: output.storageQueue({
        connection: 'storage_APPSETTING',
        ...
    }),
    handler: (myTimer, context) => {
        return { hello: 'world' }
    }
});
```

In addition to the trigger and return, you might specify extra inputs or outputs on the `options` argument when registering a function. The `input` and `output` objects exported from the `@azure/functions` module provide type-specific methods to help construct the configuration. During execution, you get or set the values with `context.extraInputs.get` or `context.extraOutputs.set`, passing in the original configuration object as the first argument.

The following example is a function triggered by a [storage queue](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger), with an extra [storage blob input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input) that is copied to an extra [storage blob output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-output). The queue message should be the name of a file and replaces `{queueTrigger}` as the blob name to be copied, with the help of a [binding expression](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-expressions-patterns).

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_14_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_14_typescript)

```
const { app, input, output } = require("@azure/functions");

const blobInput = input.storageBlob({
  connection: "storage_APPSETTING",
  path: "helloworld/{queueTrigger}",
});

const blobOutput = output.storageBlob({
  connection: "storage_APPSETTING",
  path: "helloworld/{queueTrigger}-copy",
});

app.storageQueue("copyBlob1", {
  queueName: "copyblobqueue",
  connection: "storage_APPSETTING",
  extraInputs: [blobInput],
  extraOutputs: [blobOutput],
  handler: (queueItem, context) => {
    const blobInputValue = context.extraInputs.get(blobInput);
    context.extraOutputs.set(blobOutput, blobInputValue);
  },
});
```

The `app`, `trigger`, `input`, and `output` objects exported by the `@azure/functions` module provide type-specific methods for most types. For all the types that aren't supported, a `generic` method is provided to allow you to manually specify the configuration. The `generic` method can also be used if you want to change the default settings provided by a type-specific method.

The following example is a simple HTTP triggered function using generic methods instead of type-specific methods.

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_15_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_15_typescript)

```
const { app, output, trigger } = require("@azure/functions");

app.generic("helloWorld1", {
  trigger: trigger.generic({
    type: "httpTrigger",
    methods: ["GET", "POST"],
  }),
  return: output.generic({
    type: "http",
  }),
  handler: async (request, context) => {
    context.log(`Http function processed request for url "${request.url}"`);

    return { body: `Hello, world!` };
  },
});
```

Several binding extensions now enable you to work directly with the Azure SDK types.

SDK bindings capability in Azure Functions enables you to work directly with the Azure Blob storage SDK types like `BlobClient` and `ContainerClient` instead of raw data. This provides full access to all SDK methods when working with blobs.

To configure your project to work with SDK types:

1.   Add the `@azure/functions-extensions-blob` extension preview packages to the `package.json` file in the project, which should include at least these packages:

```
"dependencies": {
  "@azure/functions": "4.7.2-preview",
  "@azure/functions-extensions-blob": "0.2.0-preview"
},
```

1.   Add `enableHttpStream: true` in your `app.setup` to support streaming types:

```
import { app } from '@azure/functions';

app.setup({
    enableHttpStream: true,
});
```

This example shows how to get the BlobClient from both a Storage Blob trigger and from the input binding on an HTTP trigger:

```
import "@azure/functions-extensions-blob"; // This is the mandatory first import for SDK binding
import { StorageBlobClient } from "@azure/functions-extensions-blob";
import { app, InvocationContext } from "@azure/functions";

export async function storageBlobTrigger(
  blobStorageClient: StorageBlobClient, // SDK binding provides this client
  context: InvocationContext
): Promise<void> {
  context.log(`Blob trigger processing: ${context.triggerMetadata.name}`);

  // Access to full SDK capabilities
  const blobProperties = await blobStorageClient.blobClient.getProperties();
  context.log(`Blob size: ${blobProperties.contentLength}`);

  // Download blob content
  const downloadResponse = await blobStorageClient.blobClient.download();
  context.log(`Content: ${downloadResponse}`);
}

// Register the function
app.storageBlob("storageBlobTrigger", {
  path: "snippets/{name}",
  connection: "AzureWebJobsStorage",
  sdkBinding: true, // Enable SDK binding
  handler: storageBlobTrigger,
});
```

This example shows how to get the `ContainerClient` from both a Storage Blob input binding using an HTTP trigger:

```
import "@azure/functions-extensions-blob"; // This is the mandatory first import for SDK binding
import { StorageBlobClient } from "@azure/functions-extensions-blob";
import {
  app,
  HttpRequest,
  HttpResponseInit,
  input,
  InvocationContext,
} from "@azure/functions";

const blobInput = input.storageBlob({
  path: "snippets",
  connection: "AzureWebJobsStorage",
  sdkBinding: true,
});

export async function listBlobs(
  request: HttpRequest,
  context: InvocationContext
): Promise<HttpResponseInit> {
  // Get input binding for a specific container
  const storageBlobClient = context.extraInputs.get(
    blobInput
  ) as StorageBlobClient;

  // List all blobs in the container
  const blobs = [];
  for await (const blob of storageBlobClient.containerClient.listBlobsFlat()) {
    blobs.push(blob.name);
  }

  return { jsonBody: { blobs } };
}

app.http("listBlobs", {
  methods: ["GET"],
  authLevel: "function",
  extraInputs: [blobInput],
  handler: listBlobs,
});
```

Keep these considerations in mind when working with SDK types:

*   Always have `import "@azure/functions-extensions-blob"` first in your files to ensure side effects run.
*   Set `sdkBinding: true` in your binding configuration.
*   Use the appropriate client type for your operation: 
    *   `blobClient` for operations on a single blob
    *   `containerClient` for operations on a container

*   Handle errors appropriately with `try`/`catch` blocks
*   For large blob operations, consider using streaming methods to avoid memory issues.

For more information, see these [Blob Storage SDK Bindings for Node.js Samples](https://github.com/Azure-Samples/azure-functions-blob-sdk-bindings-nodejs): for more examples on how to incorporate SDK Bindings for Blob into your function app.

*   [BlobClient](https://github.com/Azure-Samples/azure-functions-blob-sdk-bindings-nodejs/tree/main/blobClientSdkBinding)
*   [ContainerClient](https://github.com/Azure-Samples/azure-functions-blob-sdk-bindings-nodejs/tree/main/containerClientInputBinding)
*   [Readable Stream](https://github.com/Azure-Samples/azure-functions-blob-sdk-bindings-nodejs/tree/main/blobClientWithReadableStream)

This example uses the SDK type [`ServiceBusReceivedMessage`](https://learn.microsoft.com/en-us/javascript/api/@azure/service-bus/servicebusreceivedmessage) obtained from `ServiceBusMessageContext` provided by the Service Bus trigger:

```
import '@azure/functions-extensions-servicebus'; // Ensure the Service Bus extension is imported
import { app, InvocationContext } from '@azure/functions';
import { ServiceBusMessageContext } from '@azure/functions-extensions-servicebus';
import { parseBody } from '../servicebus-helpers'; // Interim helper until #50 lands

// This sample uses sdkBinding = true with manual message completion.
// With v0.4.0, message.body is returned as a raw Buffer instead of auto-parsed object.
export async function serviceBusQueueTrigger(
    serviceBusMessageContext: ServiceBusMessageContext,
    context: InvocationContext
): Promise<void> {
    const message = serviceBusMessageContext.messages[0];

    // v0.4.0: message.body is a Buffer — use parseBody<T>() helper for one-line parsing
    const bodyData = parseBody(message);
    context.log('Parsed message body:', bodyData);

    // Get current retry count from custom properties, default to 0
    const currentRetryCount = message.applicationProperties?.retryCnt
        ? parseInt(message.applicationProperties.retryCnt as string)
        : 0;
    context.log(`Current retry count: ${currentRetryCount}`);

    if (currentRetryCount >= 3) {
        // After 3 retries, complete the message to remove it from the queue
        context.log(`Maximum retry count (3) reached. Completing message to prevent infinite loop.`);
        await serviceBusMessageContext.actions.complete(message);
        context.log('Message completed after maximum retries');
    } else {
        // Abandon with updated retry count
        const newRetryCount = currentRetryCount + 1;
        const propertiesToModify = {
            retryCnt: newRetryCount.toString(),
            lastRetryTime: new Date().toISOString(),
            errorMessage: 'Processing failed',
        };

        context.log(`Abandoning message with retry count: ${newRetryCount}`);
        await serviceBusMessageContext.actions.abandon(message, propertiesToModify);
    }

    context.log('triggerMetadata: ', context.triggerMetadata);
}

app.serviceBusQueue('serviceBusQueueTrigger1', {
    connection: 'ServiceBusConnection',
    queueName: 'testqueue',
```

For another example using SDK types see the [exponential backoff strategy sample](https://github.com/Azure/azure-functions-nodejs-extensions/blob/main/azure-functions-nodejs-extensions-servicebus/samples/serviceBusTriggerExponentialBackOff/src/functions/serviceBusTopicTrigger.ts).

Each invocation of your function is passed an invocation `context` object, used to read inputs, set outputs, write to logs, and read various metadata. In the v3 model, the context object is always the first argument passed to your handler.

The `context` object has the following properties:

| Property | Description |
| --- | --- |
| **`invocationId`** | The ID of the current function invocation. |
| **`executionContext`** | See [execution context](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#contextexecutioncontext). |
| **`bindings`** | See [bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#contextbindings). |
| **`bindingData`** | Metadata about the trigger input for this invocation, not including the value itself. For example, an [event hub trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger) has an `enqueuedTimeUtc` property. |
| **`traceContext`** | The context for distributed tracing. For more information, see [`Trace Context`](https://www.w3.org/TR/trace-context/). |
| **`bindingDefinitions`** | The configuration of your inputs and outputs, as defined in `function.json`. |
| **`req`** | See [HTTP request](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#http-request). |
| **`res`** | See [HTTP response](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#http-response). |

The `context.executionContext` object has the following properties:

| Property | Description |
| --- | --- |
| **`invocationId`** | The ID of the current function invocation. |
| **`functionName`** | The name of the function that is being invoked. The name of the folder containing the `function.json` file determines the name of the function. |
| **`functionDirectory`** | The folder containing the `function.json` file. |
| **`retryContext`** | See [retry context](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#contextexecutioncontextretrycontext). |

The `context.executionContext.retryContext` object has the following properties:

| Property | Description |
| --- | --- |
| **`retryCount`** | A number representing the current retry attempt. |
| **`maxRetryCount`** | Maximum number of times an execution is retried. A value of `-1` means to retry indefinitely. |
| **`exception`** | Exception that caused the retry. |

The `context.bindings` object is used to read inputs or set outputs. The following example is a [storage queue trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger), which uses `context.bindings` to copy a [storage blob input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input) to a [storage blob output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-output). The queue message's content replaces `{queueTrigger}` as the file name to be copied, with the help of a [binding expression](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-expressions-patterns).

```
{
    "name": "myQueueItem",
    "type": "queueTrigger",
    "direction": "in",
    "connection": "storage_APPSETTING",
    "queueName": "helloworldqueue"
},
{
    "name": "myInput",
    "type": "blob",
    "direction": "in",
    "connection": "storage_APPSETTING",
    "path": "helloworld/{queueTrigger}"
},
{
    "name": "myOutput",
    "type": "blob",
    "direction": "out",
    "connection": "storage_APPSETTING",
    "path": "helloworld/{queueTrigger}-copy"
}
```

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_16_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_16_typescript)

```
module.exports = async function (context, myQueueItem) {
  const blobValue = context.bindings.myInput;
  context.bindings.myOutput = blobValue;
};
```

The `context.done` method is deprecated. Before async functions were supported, you would signal your function is done by calling `context.done()`:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_17_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_17_typescript)

```
module.exports = function (context, request) {
  context.log("this pattern is now deprecated");
  context.done();
};
```

We recommend that you remove the call to `context.done()` and mark your function as async so that it returns a promise (even if you don't `await` anything). As soon as your function finishes (in other words, the returned promise resolves), the v3 model knows your function is done.

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_18_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_18_typescript)

```
module.exports = async function (context, request) {
  context.log("you don't need context.done or an awaited call");
};
```

Each invocation of your function is passed an invocation `context` object, with information about your invocation and methods used for logging. In the v4 model, the `context` object is typically the second argument passed to your handler.

The `InvocationContext` class has the following properties:

| Property | Description |
| --- | --- |
| **`invocationId`** | The ID of the current function invocation. |
| **`functionName`** | The name of the function. |
| **`extraInputs`** | Used to get the values of extra inputs. For more information, see [extra inputs and outputs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#extra-inputs-and-outputs). |
| **`extraOutputs`** | Used to set the values of extra outputs. For more information, see [extra inputs and outputs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#extra-inputs-and-outputs). |
| **`retryContext`** | See [retry context](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#retry-context). |
| **`traceContext`** | The context for distributed tracing. For more information, see [`Trace Context`](https://www.w3.org/TR/trace-context/). |
| **`triggerMetadata`** | Metadata about the trigger input for this invocation, not including the value itself. For example, an [event hub trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger) has an `enqueuedTimeUtc` property. |
| **`options`** | The options used when registering the function, after they've been validated and with defaults explicitly specified. |

The `retryContext` object has the following properties:

| Property | Description |
| --- | --- |
| **`retryCount`** | A number representing the current retry attempt. |
| **`maxRetryCount`** | Maximum number of times an execution is retried. A value of `-1` means to retry indefinitely. |
| **`exception`** | Exception that caused the retry. |

For more information, see [`retry-policies`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-error-pages#retry-policies).

In Azure Functions, it's recommended to use `context.log()` to write logs. Azure Functions integrates with Azure Application Insights to better capture your function app logs. Application Insights, part of Azure Monitor, provides facilities for collection, visual rendering, and analysis of both application logs and your trace outputs. To learn more, see [monitoring Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-monitoring).

Note

If you use the alternative Node.js `console.log` method, those logs are tracked at the app-level and will _not_ be associated with any specific function. We _highly recommend_ that your use `context` for logging instead of `console` so that all logs are associated with a specific function.

The following example writes a log at the default "information" level, including the invocation ID:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_19_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_19_typescript)

```
context.log(`Something has happened. Invocation ID: "${context.invocationId}"`);
```

In addition to the default `context.log` method, the following methods are available that let you write logs at specific levels:

| Method | Description |
| --- | --- |
| **`context.log.error()`** | Writes an error-level event to the logs. |
| **`context.log.warn()`** | Writes a warning-level event to the logs. |
| **`context.log.info()`** | Writes an information-level event to the logs. |
| **`context.log.verbose()`** | Writes a trace-level event to the logs. |

| Method | Description |
| --- | --- |
| **`context.trace()`** | Writes a trace-level event to the logs. |
| **`context.debug()`** | Writes a debug-level event to the logs. |
| **`context.info()`** | Writes an information-level event to the logs. |
| **`context.warn()`** | Writes a warning-level event to the logs. |
| **`context.error()`** | Writes an error-level event to the logs. |

Azure Functions lets you define the threshold level to be used when tracking and viewing logs. To set the threshold, use the `logging.logLevel` property in the `host.json` file. This property lets you define a default level applied to all functions, or a threshold for each individual function. To learn more, see [How to configure monitoring for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/configure-monitoring).

By default, Azure Functions writes output as traces to Application Insights. For more control, you can instead use the [Application Insights Node.js SDK](https://github.com/microsoft/applicationinsights-node.js) to send custom logs, metrics, and dependencies to your Application Insights instance.

Note

Methods in the Application Insights Node.js SDK might change over time. There might be minor syntax differences from the examples shown here. For the latest API usage examples, see the [Application Insights Node.js SDK documentation](https://github.com/microsoft/applicationinsights-node.js).

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_20_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_20_typescript)

```
const appInsights = require("applicationinsights");
appInsights.setup();
const client = appInsights.defaultClient;

module.exports = async function (context, request) {
  // Use this with 'tagOverrides' to correlate custom logs to the parent function invocation.
  var operationIdOverride = {
    "ai.operation.id": context.traceContext.traceparent,
  };

  client.trackEvent({
    name: "my custom event",
    tagOverrides: operationIdOverride,
    properties: { customProperty2: "custom property value" },
  });
  client.trackException({
    exception: new Error("handled exceptions can be logged with this method"),
    tagOverrides: operationIdOverride,
  });
  client.trackMetric({
    name: "custom metric",
    value: 3,
    tagOverrides: operationIdOverride,
  });
  client.trackTrace({
    message: "trace message",
    tagOverrides: operationIdOverride,
  });
  client.trackDependency({
    target: "http://dbname",
    name: "select customers proc",
    data: "SELECT * FROM Customers",
    duration: 231,
    resultCode: 0,
    success: true,
    dependencyTypeName: "ZSQL",
    tagOverrides: operationIdOverride,
  });
  client.trackRequest({
    name: "GET /customers",
    url: "http://myserver/customers",
    duration: 309,
    resultCode: 200,
    success: true,
    tagOverrides: operationIdOverride,
  });
};
```

The `tagOverrides` parameter sets the `operation_Id` to the function's invocation ID. This setting enables you to correlate all of the automatically generated and custom logs for a given function invocation.

HTTP and webhook triggers use request and response objects to represent HTTP messages.

HTTP and webhook triggers use `HttpRequest` and `HttpResponse` objects to represent HTTP messages. The classes represent a subset of the [fetch standard](https://developer.mozilla.org/docs/Web/API/fetch), using Node.js's [`undici`](https://undici.nodejs.org/) package.

The request can be accessed in several ways:

*   **As the second argument to your function:**

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_21_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_21_typescript)

```
module.exports = async function (context, request) {
    context.log(`Http function processed request for url "${request.url}"`);
```

* * *

*   **From the `context.req` property:**

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_22_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_22_typescript)

```
module.exports = async function (context, request) {
    context.log(`Http function processed request for url "${context.req.url}"`);
```

* * *

*   **From the named input bindings:** This option works the same as any non HTTP binding. The binding name in `function.json` must match the key on `context.bindings`, or "request1" in the following example:

```
{
  "name": "request1",
  "type": "httpTrigger",
  "direction": "in",
  "authLevel": "anonymous",
  "methods": ["get", "post"]
}
```

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_23_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_23_typescript)

```
module.exports = async function (context, request) {
    context.log(`Http function processed request for url "${context.bindings.request1.url}"`);
```

* * *

The `HttpRequest` object has the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **`method`** | `string` | HTTP request method used to invoke this function. |
| **`url`** | `string` | Request URL. |
| **`headers`** | `Record<string, string>` | HTTP request headers. This object is case sensitive. It's recommended to use `request.getHeader('header-name')` instead, which is case insensitive. |
| **`query`** | `Record<string, string>` | Query string parameter keys and values from the URL. |
| **`params`** | `Record<string, string>` | Route parameter keys and values. |
| **`user`** | `HttpRequestUser \| null` | Object representing logged-in user, either through Functions authentication, SWA Authentication, or null when no such user is logged in. |
| **`body`** | `Buffer \| string \| any` | If the media type is "application/octet-stream" or "multipart/*", `body` is a Buffer. If the value is a JSON parse-able string, `body` is the parsed object. Otherwise, `body` is a string. |
| **`rawBody`** | `string` | The body as a string. Despite the name, this property doesn't return a Buffer. |
| **`bufferBody`** | `Buffer` | The body as a buffer. |

The request can be accessed as the first argument to your handler for an HTTP triggered function.

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_24_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_24_typescript)

```
async (request, context) => {
    context.log(`Http function processed request for url "${request.url}"`);
```

The `HttpRequest` object has the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **`method`** | `string` | HTTP request method used to invoke this function. |
| **`url`** | `string` | Request URL. |
| **`headers`** | [`Headers`](https://developer.mozilla.org/docs/Web/API/Headers) | HTTP request headers. |
| **`query`** | [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) | Query string parameter keys and values from the URL. |
| **`params`** | `Record<string, string>` | Route parameter keys and values. |
| **`user`** | `HttpRequestUser \| null` | Object representing logged-in user, either through Functions authentication, SWA Authentication, or null when no such user is logged in. |
| **`body`** | [`ReadableStream \| null`](https://developer.mozilla.org/docs/Web/API/ReadableStream) | Body as a readable stream. |
| **`bodyUsed`** | `boolean` | A boolean indicating if the body is already read. |

In order to access a request or response's body, the following methods can be used:

| Method | Return Type |
| --- | --- |
| **`arrayBuffer()`** | [`Promise<ArrayBuffer>`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) |
| **`blob()`** | [`Promise<Blob>`](https://developer.mozilla.org/docs/Web/API/Blob) |
| **`formData()`** | [`Promise<FormData>`](https://developer.mozilla.org/docs/Web/API/FormData) |
| **`json()`** | `Promise<unknown>` |
| **`text()`** | `Promise<string>` |

Note

The body functions can be run only once. Subsequent calls resolve with empty strings/ArrayBuffers.

The response can be set in several ways:

*   **Set the `context.res` property:**

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_25_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_25_typescript)

```
module.exports = async function (context, request) {
    context.res = { body: `Hello, world!` };
```

* * *

*   **Return the response:** If your function is async and you set the binding name to `$return` in your `function.json`, you can return the response directly instead of setting it on `context`.

```
{
  "type": "http",
  "direction": "out",
  "name": "$return"
}
```

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_26_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_26_typescript)

```
module.exports = async function (context, request) {
    return { body: `Hello, world!` };
```

* * *

*   **Set the named output binding:** This option works the same as any non HTTP binding. The binding name in `function.json` must match the key on `context.bindings`, or "response1" in the following example:

```
{
  "type": "http",
  "direction": "out",
  "name": "response1"
}
```

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_27_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_27_typescript)

```
module.exports = async function (context, request) {
    context.bindings.response1 = { body: `Hello, world!` };
```

* * *

*   **Call `context.res.send()`:** This option is deprecated. It implicitly calls `context.done()` and can't be used in an async function.

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_28_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_28_typescript)

```
module.exports = function (context, request) {
    context.res.send(`Hello, world!`);
```

* * *

If you create a new object when setting the response, that object must match the `HttpResponseSimple` interface, which has the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **`headers`** | `Record<string, string>` (optional) | HTTP response headers. |
| **`cookies`** | `Cookie[]` (optional) | HTTP response cookies. |
| **`body`** | `any` (optional) | HTTP response body. |
| **`statusCode`** | `number` (optional) | HTTP response status code. If not set, defaults to `200`. |
| **`status`** | `number` (optional) | The same as `statusCode`. This property is ignored if `statusCode` is set. |

You can also modify the `context.res` object without overwriting it. The default `context.res` object uses the `HttpResponseFull` interface, which supports the following methods in addition to the `HttpResponseSimple` properties:

| Method | Description |
| --- | --- |
| **`status()`** | Sets the status. |
| **`setHeader()`** | Sets a header field. NOTE: `res.set()` and `res.header()` are also supported and do the same thing. |
| **`getHeader()`** | Get a header field. NOTE: `res.get()` is also supported and does the same thing. |
| **`removeHeader()`** | Removes a header. |
| **`type()`** | Sets the "content-type" header. |
| **`send()`** | This method is deprecated. It sets the body and calls `context.done()` to indicate a sync function is finished. NOTE: `res.end()` is also supported and does the same thing. |
| **`sendStatus()`** | This method is deprecated. It sets the status code and calls `context.done()` to indicate a sync function is finished. |
| **`json()`** | This method is deprecated. It sets the "content-type" to "application/json", sets the body, and calls `context.done()` to indicate a sync function is finished. |

The response can be set in several ways:

*   **As a simple interface with type `HttpResponseInit`:** This option is the most concise way of returning responses.

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_29_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_29_typescript)

```
return { body: `Hello, world!` };
```

* * *

The `HttpResponseInit` interface has the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **`body`** | `BodyInit` (optional) | HTTP response body as one of [`ArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [`AsyncIterable<Uint8Array>`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array), [`Blob`](https://developer.mozilla.org/docs/Web/API/Blob), [`FormData`](https://developer.mozilla.org/docs/Web/API/FormData), [`Iterable<Uint8Array>`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array), [`NodeJS.ArrayBufferView`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams), `null`, or `string`. |
| **`jsonBody`** | `any` (optional) | A JSON-serializable HTTP Response body. If set, the `HttpResponseInit.body` property is ignored in favor of this property. |
| **`status`** | `number` (optional) | HTTP response status code. If not set, defaults to `200`. |
| **`headers`** | [`HeadersInit`](https://developer.mozilla.org/docs/Web/API/Headers) (optional) | HTTP response headers. |
| **`cookies`** | `Cookie[]` (optional) | HTTP response cookies. |

*   **As a class with type `HttpResponse`:** This option provides helper methods for reading and modifying various parts of the response like the headers.

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_30_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_30_typescript)

```
const response = new HttpResponse({ body: `Hello, world!` });
response.headers.set("content-type", "application/json");
return response;
```

* * *

The `HttpResponse` class accepts an optional `HttpResponseInit` as an argument to its constructor and has the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **`status`** | `number` | HTTP response status code. |
| **`headers`** | [`Headers`](https://developer.mozilla.org/docs/Web/API/Headers) | HTTP response headers. |
| **`cookies`** | `Cookie[]` | HTTP response cookies. |
| **`body`** | [`ReadableStream | null`](https://developer.mozilla.org/docs/Web/API/ReadableStream) | Body as a readable stream. |
| **`bodyUsed`** | `boolean` | A boolean indicating if the body has been read from already. |

HTTP streams is a feature that makes it easier to process large data, stream OpenAI responses, deliver dynamic content, and support other core HTTP scenarios. It lets you stream requests to and responses from HTTP endpoints in your Node.js function app. Use HTTP streams in scenarios where your app requires real-time exchange and interaction between client and server over HTTP. You can also use HTTP streams to get the best performance and reliability for your apps when using HTTP.

Important

HTTP streams aren't supported in the v3 model. [Upgrade to the v4 model](https://learn.microsoft.com/en-us/azure/azure-functions/functions-node-upgrade-v4) to use the HTTP streaming feature. The existing `HttpRequest` and `HttpResponse` types in programming model v4 already support various ways of handling the message body, including as a stream.

*   The [`@azure/functions` npm package](https://www.npmjs.com/package/@azure/functions) version 4.3.0 or later.
*   [Azure Functions runtime](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions) version 4.28 or later.
*   [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) version 4.0.5530 or a later version, which contains the correct runtime version.

Use these steps to enable HTTP streams in your function app in Azure and in your local projects:

1.   If you plan to stream large amounts of data, modify the [`FUNCTIONS_REQUEST_BODY_SIZE_LIMIT`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#functions_request_body_size_limit) setting in Azure. The default maximum body size allowed is `104857600`, which limits your requests to a size of ~100 MB.

2.   For local development, also add `FUNCTIONS_REQUEST_BODY_SIZE_LIMIT` to the [local.settings.json file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file).

3.   Add the following code to your app in any file included by your [main field](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node#registering-a-function).

    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_31_javascript)
    *   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_31_typescript)

```
const { app } = require("@azure/functions");

app.setup({ enableHttpStream: true });
```

* * *

This example shows an HTTP triggered function that receives data via an HTTP POST request, and the function streams this data to a specified output file:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_32_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_32_typescript)

```
const { app } = require('@azure/functions');
const { createWriteStream } = require('fs');
const { Writable } = require('stream');

app.http('httpTriggerStreamRequest', {
    methods: ['POST'],
    authLevel: 'anonymous',
    handler: async (request, context) => {
        const writeStream = createWriteStream('<output file path>');
        await request.body.pipeTo(Writable.toWeb(writeStream));

        return { body: 'Done!' };
    },
});
```

This example shows an HTTP triggered function that streams a file's content as the response to incoming HTTP GET requests:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_33_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_33_typescript)

```
const { app } = require('@azure/functions');
const { createReadStream } = require('fs');

app.http('httpTriggerStreamResponse', {
    methods: ['GET'],
    authLevel: 'anonymous',
    handler: async (request, context) => {
        const body = createReadStream('<input file path>');

        return { body };
    },
});
```

For a ready-to-run sample app using streams, check out this example on [GitHub](https://github.com/Azure-Samples/azure-functions-nodejs-stream).

*   Use `request.body` to obtain the maximum benefit from using streams. You can still continue to use methods like `request.text()`, which always return the body as a string.

Use a hook to execute code at different points in the Azure Functions lifecycle. Hooks are executed in the order they're registered and can be registered from any file in your app. There are currently two scopes of hooks, "app" level and "invocation" level.

Invocation hooks are executed once per invocation of your function, either before in a `preInvocation` hook or after in a `postInvocation` hook. By default your hook executes for all trigger types, but you can also filter by type. The following example shows how to register an invocation hook and filter by trigger type:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_34_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_34_typescript)

```
const { app } = require('@azure/functions');

app.hook.preInvocation((context) => {
    if (context.invocationContext.options.trigger.type === 'httpTrigger') {
        context.invocationContext.log(
            `preInvocation hook executed for http function ${context.invocationContext.functionName}`
        );
    }
});

app.hook.postInvocation((context) => {
    if (context.invocationContext.options.trigger.type === 'httpTrigger') {
        context.invocationContext.log(
            `postInvocation hook executed for http function ${context.invocationContext.functionName}`
        );
    }
});
```

The first argument to the hook handler is a context object specific to that hook type.

The `PreInvocationContext` object has the following properties:

| Property | Description |
| --- | --- |
| **`inputs`** | The arguments passed to the invocation. |
| **`functionHandler`** | The function handler for the invocation. Changes to this value affect the function itself. |
| **`invocationContext`** | The [invocation context](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#invocation-context) object passed to the function. |
| **`hookData`** | The recommended place to store and share data between hooks in the same scope. You should use a unique property name so that it doesn't conflict with other hooks' data. |

The `PostInvocationContext` object has the following properties:

| Property | Description |
| --- | --- |
| **`inputs`** | The arguments passed to the invocation. |
| **`result`** | The result of the function. Changes to this value affect the overall result of the function. |
| **`error`** | The error thrown by the function, or null/undefined if there's no error. Changes to this value affect the overall result of the function. |
| **`invocationContext`** | The [invocation context](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#invocation-context) object passed to the function. |
| **`hookData`** | The recommended place to store and share data between hooks in the same scope. You should use a unique property name so that it doesn't conflict with other hooks' data. |

App hooks are executed once per instance of your app, either during startup in an `appStart` hook or during termination in an `appTerminate` hook. App terminate hooks have a limited time to execute and don't execute in all scenarios.

The Azure Functions runtime currently [doesn't support](https://github.com/Azure/azure-functions-host/issues/8222) context logging outside of an invocation. Use the Application Insights [npm package](https://www.npmjs.com/package/applicationinsights) to log data during app level hooks.

The following example registers app hooks:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_35_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_35_typescript)

```
const { app } = require('@azure/functions');

app.hook.appStart((context) => {
    // add your logic here
});

app.hook.appTerminate((context) => {
    // add your logic here
});
```

The first argument to the hook handler is a context object specific to that hook type.

The `AppStartContext` object has the following properties:

| Property | Description |
| --- | --- |
| **`hookData`** | The recommended place to store and share data between hooks in the same scope. You should use a unique property name so that it doesn't conflict with other hooks' data. |

The `AppTerminateContext` object has the following properties:

| Property | Description |
| --- | --- |
| **`hookData`** | The recommended place to store and share data between hooks in the same scope. You should use a unique property name so that it doesn't conflict with other hooks' data. |

By default, Azure Functions automatically monitors the load on your application and creates more host instances for Node.js as needed. Azure Functions uses built-in (not user configurable) thresholds for different trigger types to decide when to add instances, such as the age of messages and queue size for QueueTrigger. For more information, see [How the Consumption and Premium plans work](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling).

This scaling behavior is sufficient for many Node.js applications. For CPU-bound applications, you can improve performance further by using multiple language worker processes. You can increase the number of worker processes per host from the default of 1 up to a max of 10 by using the [FUNCTIONS_WORKER_PROCESS_COUNT](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#functions_worker_process_count) application setting. Azure Functions then tries to evenly distribute simultaneous function invocations across these workers. This behavior makes it less likely that a CPU-intensive function blocks other functions from running. The setting applies to each host that Azure Functions creates when scaling out your application to meet demand.

Warning

Use the `FUNCTIONS_WORKER_PROCESS_COUNT` setting with caution. Multiple processes running in the same instance can lead to unpredictable behavior and increase function load times. If you use this setting, we _highly recommend_ that you offset these downsides by [running from a package file](https://learn.microsoft.com/en-us/azure/azure-functions/run-functions-from-deployment-package).

You can see the current version that the runtime is using by logging `process.version` from any function. See [`supported versions`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#supported-versions) for a list of Node.js versions supported by each programming model.

The way that you upgrade your Node.js version depends on the OS on which your function app runs.

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_36_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_36_linux)

When it runs on Linux, the Node.js version is set by the [linuxFxVersion](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion) site setting. This setting can be updated using the Azure CLI.

For more information about Node.js versions, see [Supported versions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#supported-versions).

Before upgrading your Node.js version, make sure your function app is running on the latest version of the Azure Functions runtime. If you need to upgrade your runtime version, see [Migrate apps from Azure Functions version 3.x to version 4.x](https://learn.microsoft.com/en-us/azure/azure-functions/migrate-version-3-version-4?pivots=programming-language-javascript).

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_37_azure-cli_linux)
*   [Azure portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_37_azure-portal_linux)

Run the Azure CLI [`az functionapp config set`](https://learn.microsoft.com/en-us/cli/azure/functionapp/config#az-functionapp-config-set) command to update the Node.js version for your function app running on Linux:

```
az functionapp config set --linux-fx-version "node|22" --name "<FUNCTION_APP_NAME>" \
 --resource-group "<RESOURCE_GROUP_NAME>"
```

This sets the base image of the Linux function app to Node.js version 22.

After changes are made, your function app restarts. To learn more about Functions support for Node.js, see [Language runtime support policy](https://learn.microsoft.com/en-us/azure/azure-functions/language-support-policy).

Environment variables can be useful for operational secrets (connection strings, keys, endpoints, etc.) or environmental settings such as profiling variables. You can add environment variables in both your local and cloud environments and access them through `process.env` in your function code.

The following example logs the `WEBSITE_SITE_NAME` environment variable:

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_38_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_38_typescript)

```
module.exports = async function (context) {
  context.log(`WEBSITE_SITE_NAME: ${process.env["WEBSITE_SITE_NAME"]}`);
};
```

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_39_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_39_typescript)

```
async function timerTrigger1(myTimer, context) {
  context.log(`WEBSITE_SITE_NAME: ${process.env["WEBSITE_SITE_NAME"]}`);
}
```

When you run locally, your functions project includes a [`local.settings.json` file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local), where you store your environment variables in the `Values` object.

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "node",
    "CUSTOM_ENV_VAR_1": "hello",
    "CUSTOM_ENV_VAR_2": "world"
  }
}
```

When you run in Azure, the function app lets you set and use [Application settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings), such as service connection strings, and exposes these settings as environment variables during execution.

There are several ways that you can add, update, and delete function app settings:

*   [In the Azure portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings#settings)
*   [By using the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/functionapp/config/appsettings#az-functionapp-config-appsettings-set)
*   [By using Azure PowerShell](https://learn.microsoft.com/en-us/powershell/module/az.functions/update-azfunctionappsetting)

Changes to function app settings require your function app to be restarted.

There are several Functions environment variables specific to Node.js:

This setting allows you to specify custom arguments when starting your Node.js process. It's most often used locally to start the worker in debug mode, but can also be used in Azure if you need custom arguments.

Warning

If possible, avoid using `languageWorkers__node__arguments` in Azure because it can have a negative effect on cold start times. Rather than using prewarmed workers, the runtime has to start a new worker from scratch with your custom arguments.

This setting adjusts the default log level for Node.js-specific worker logs. By default, only warning or error logs are shown, but you can set it to `information` or `debug` to help diagnose issues with the Node.js worker. For more information, see [configuring log levels](https://learn.microsoft.com/en-us/azure/azure-functions/configure-monitoring#configure-log-levels).

Note

As ECMAScript modules are currently a preview feature in Node.js 14 or higher in Azure Functions.

[ECMAScript modules](https://nodejs.org/docs/latest-v14.x/api/esm.html#esm_modules_ecmascript_modules) (ES modules) are the new official standard module system for Node.js. So far, the code samples in this article use the CommonJS syntax. When running Azure Functions in Node.js 14 or higher, you can choose to write your functions using ES modules syntax.

To use ES modules in a function, change its filename to use a `.mjs` extension. The following _index.mjs_ file example is an HTTP triggered function that uses ES modules syntax to import the `uuid` library and return a value.

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_40_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_40_typescript)

```
import { v4 as uuidv4 } from "uuid";

async function httpTrigger1(context, request) {
  context.res.body = uuidv4();
}

export default httpTrigger;
```

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_41_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_41_typescript)

```
import { v4 as uuidv4 } from "uuid";

async function httpTrigger1(request, context) {
  return { body: uuidv4() };
}

app.http("httpTrigger1", {
  methods: ["GET", "POST"],
  handler: httpTrigger1,
});
```

The `function.json` properties `scriptFile` and `entryPoint` can be used to configure the location and name of your exported function. The `scriptFile` property is required when you're using TypeScript and should point to the compiled JavaScript.

By default, a JavaScript function is executed from `index.js`, a file that shares the same parent directory as its corresponding `function.json`.

`scriptFile` can be used to get a folder structure that looks like the following example:

```
<project_root>/
 | - node_modules/
 | - myFirstFunction/
 | | - function.json
 | - lib/
 | | - sayHello.js
 | - host.json
 | - package.json
```

The `function.json` for `myFirstFunction` should include a `scriptFile` property pointing to the file with the exported function to run.

```
{
  "scriptFile": "../lib/sayHello.js",
  "bindings": [
    ...
  ]
}
```

In the v3 model, a function must be exported using `module.exports` in order to be found and run. By default, the function that executes when triggered is the only export from that file, the export named `run`, or the export named `index`. The following example sets `entryPoint` in `function.json` to a custom value, "logHello":

```
{
  "entryPoint": "logHello",
  "bindings": [
    ...
  ]
}
```

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_42_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_42_typescript)

```
async function logHello(context) {
  context.log("Hello, world!");
}

module.exports = { logHello };
```

We recommend that you use VS Code for local debugging, which starts your Node.js process in debug mode automatically and attaches to the process for you. For more information, see [run the function locally](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code?pivot=programming-language-javascript#run-the-function-locally).

If you're using a different tool for debugging or want to start your Node.js process in debug mode manually, add `"languageWorkers__node__arguments": "--inspect"` under `Values` in your [local.settings.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file). The `--inspect` argument tells Node.js to listen for a debug client, on port 9229 by default. For more information, see the [Node.js debugging guide](https://nodejs.org/en/learn/getting-started/debugging).

This section describes several impactful patterns for Node.js apps that we recommend you follow.

When you create a function app that uses the App Service plan, we recommend that you select a single-vCPU plan rather than a plan with multiple vCPUs. Today, Functions runs Node.js functions more efficiently on single-vCPU VMs, and using larger VMs doesn't produce the expected performance improvements. When necessary, you can manually scale out by adding more single-vCPU VM instances, or you can enable autoscale. For more information, see [Scale instance count manually or automatically](https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-get-started?toc=/azure/app-service/toc.json).

When you develop Azure Functions in the serverless hosting model, cold starts are a reality. _Cold start_ refers to the first time your function app starts after a period of inactivity, taking longer to start up. For Node.js apps with large dependency trees in particular, cold start can be significant. To speed up the cold start process, [run your functions as a package file](https://learn.microsoft.com/en-us/azure/azure-functions/run-functions-from-deployment-package) when possible. Many deployment methods use this model by default, but if you're experiencing large cold starts you should check to make sure you're running this way.

When you use a service-specific client in an Azure Functions application, don't create a new client with every function invocation because you can hit connection limits. Instead, create a single, static client in the global scope. For more information, see [managing connections in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/manage-connections).

When writing Azure Functions in Node.js, you should write code using the `async` and `await` keywords. Writing code using `async` and `await` instead of callbacks or `.then` and `.catch` with Promises helps avoid two common problems:

*   Throwing uncaught exceptions that [crash the Node.js process](https://nodejs.org/api/process.html#process_warning_using_uncaughtexception_correctly), potentially affecting the execution of other functions.
*   Unexpected behavior, such as missing logs from `context.log`, caused by asynchronous calls that aren't properly awaited.

In the following example, the asynchronous method `fs.readFile` is invoked with an error-first callback function as its second parameter. This code causes both of the issues previously mentioned. An exception that isn't explicitly caught in the correct scope can crash the entire process (issue #1). Returning without ensuring the callback finishes means the http response sometimes has an empty body (issue #2).

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_43_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_43_typescript)

```
// DO NOT USE THIS CODE
const { app } = require('@azure/functions');
const fs = require('fs');

app.http('httpTriggerBadAsync', {
    methods: ['GET', 'POST'],
    authLevel: 'anonymous',
    handler: async (request, context) => {
        let fileData;
        fs.readFile('./helloWorld.txt', (err, data) => {
            if (err) {
                context.error(err);
                // BUG #1: This will result in an uncaught exception that crashes the entire process
                throw err;
            }
            fileData = data;
        });
        // BUG #2: fileData is not guaranteed to be set before the invocation ends
        return { body: fileData };
    },
});
```

In the following example, the asynchronous method `fs.readFile` is invoked with an error-first callback function as its second parameter. This code causes both of the issues previously mentioned. An exception that isn't explicitly caught in the correct scope can crash the entire process (issue #1). Calling the deprecated `context.done()` method outside of the scope of the callback can signal the function is finished before the file is read (issue #2). In this example, calling `context.done()` too early results in missing log entries starting with `Data from file:`.

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_44_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_44_typescript)

```
// NOT RECOMMENDED PATTERN
const fs = require("fs");

module.exports = function (context) {
  fs.readFile("./hello.txt", (err, data) => {
    if (err) {
      context.log.error("ERROR", err);
      // BUG #1: This will result in an uncaught exception that crashes the entire process
      throw err;
    }
    context.log(`Data from file: ${data}`);
    // context.done() should be called here
  });
  // BUG #2: Data is not guaranteed to be read before the Azure Function's invocation ends
  context.done();
};
```

Use the `async` and `await` keywords to help avoid both of these issues. Most APIs in the Node.js ecosystem have been converted to support promises in some form. For example, starting in v14, Node.js provides an `fs/promises` API to replace the `fs` callback API.

In the following example, any unhandled exceptions thrown during the function execution only fail the individual invocation that raised the exception. The `await` keyword means that steps following `readFile` only execute after it's complete.

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_45_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_45_typescript)

```
// Recommended pattern
const { app } = require('@azure/functions');
const fs = require('fs/promises');

app.http('httpTriggerGoodAsync', {
    methods: ['GET', 'POST'],
    authLevel: 'anonymous',
    handler: async (request, context) => {
        try {
            const fileData = await fs.readFile('./helloWorld.txt');
            return { body: fileData };
        } catch (err) {
            context.error(err);
            // This rethrown exception will only fail the individual invocation, instead of crashing the whole process
            throw err;
        }
    },
});
```

With `async` and `await`, you also don't need to call the `context.done()` callback.

*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_46_javascript)
*   [TypeScript](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=javascript#tabpanel_46_typescript)

```
// Recommended pattern
const fs = require("fs/promises");

module.exports = async function (context) {
  let data;
  try {
    data = await fs.readFile("./hello.txt");
  } catch (err) {
    context.log.error("ERROR", err);
    // This rethrown exception will be handled by the Functions Runtime and will only fail the individual invocation
    throw err;
  }
  context.log(`Data from file: ${data}`);
};
```

See the [Node.js Troubleshoot guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-node-troubleshoot).

For more information, see the following resources:

*   [Best practices for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-best-practices)
*   [Azure Functions developer reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference)
*   [Azure Functions triggers and bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings)
