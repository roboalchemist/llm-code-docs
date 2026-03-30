# Source: https://firebase.google.com/docs/remote-config/server.md.txt

:
<button value="node.js" default="">Node.js</button> <button value="python">Python</button> <button value="go">Go</button> <button value="java">Java</button>

<br />

:

Firebase Remote Config supports server-side configuration using the Firebase
Admin Node.js SDK v12.1.0+.
This capability empowers you to dynamically manage the behavior and configuration
of server-side applications using Remote Config. This includes serverless
implementations like [Cloud Functions](https://firebase.google.com/docs/functions).

Unlike Firebase client SDKs, which fetch a client-specific configuration
*derived* from the Remote Config template, the server-side
Remote Config SDK downloads a *complete* Remote Config template
from Firebase. Your server can then evaluate the template with each
incoming request and use its own logic to serve a customized response with
very low latency. You can use
[conditions](https://firebase.google.com/docs/remote-config/parameters?template_type=server#condition-rule-types)
to control and customize responses based on random percentages and client
attributes defined in
[custom signals](https://firebase.google.com/docs/remote-config/parameters?template_type=server#custom-signals).

With server-side Remote Config, you can:

- Define configuration parameters for applications running on or accessed through your server, allowing for use cases like remotely configuring AI model parameters and prompts and other integrations, to ensure your API keys stay secure.
- Dynamically adjust parameters in response to changes in your environment or other application changes, like updating LLM parameters and model endpoints.
- Control costs by remotely updating the APIs your server calls.
- Generate custom configurations on-the-fly for clients that access your server.
- Record which clients received a parameter value and use this in Cloud Functions as part of an entitlement verification system.

You can deploy server-side Remote Config on Cloud Run,
Cloud Functions, or self-hosted server environments.

> [!WARNING]
> Remote Config in server environments is a Preview release. This means
> that the functionality might change and the release may receive limited
> support.
>
> As you use server-side Remote Config, we encourage you to
> [share your feedback with us](https://firebase.google.com/docs/remote-config/survey).

## Before you begin

Follow the instructions in [Add the Firebase Admin SDK to your
server](https://firebase.google.com/docs/admin/setup) to create a Firebase
project, set up a service account, and add the Firebase Admin Node.js SDK to
your server.

### Step 1: Initialize the Firebase Admin Node.js SDK and authorize API requests

When you initialize the Admin SDK with no parameters, the SDK uses [Google
Application Default
Credentials](https://developers.google.com/identity/protocols/application-default-credentials)
and reads options from the `GOOGLE_APPLICATION_CREDENTIALS` environment
variable. To initialize the SDK and add Remote Config:

    import { initializeApp } from "firebase-admin/app";
    import { getRemoteConfig } from "firebase-admin/remote-config";

    // Initialize Firebase
    const firebaseApp = initializeApp();

### Step 2: Identify default parameter values for your server application

Identify the variables in your app that you want to dynamically update with
Remote Config. Then, consider which variables must be set by default in
your application and what their default values should be. This ensures that
your application runs successfully even if its connection to the
Remote Config backend server is interrupted.

For example, if you are writing a server application that manages a
generative AI function, you might set a default model name, prompt preamble,
and a generative AI configuration, like the following:

| **Parameter name** | **Description** | **Type** | **Default value** |
|---|---|---|---|
| `model_name` | Model API name | String | `gemini-2.0-flash` |
| `preamble_prompt` | Prompt to prepend to the user's query | String | `I'm a developer who wants to learn about Firebase and you are a helpful assistant who knows everything there is to know about Firebase!` |
| `generation_config` | Parameters to send to the model | JSON | `{"stopSequences": ["I hope this helps"], "temperature": 0.7, "maxOutputTokens": 512, "topP": 0.1, "topK": 20}` |

### Step 3: Configure your server application

After you've determined the parameters you want to use with
Remote Config, configure your application to set default values, fetch
the server-specific Remote Config template, and use its values. The
following steps describe how to configure your Node.js application.

1. Access and load the template.

       // Initialize server-side Remote Config
       const rc = getRemoteConfig(firebaseApp);
       const template = rc.initServerTemplate();

       // Load Remote Config
       await template.load();

   If you're using Node.js within a [Cloud Functions](https://firebase.google.com/docs/functions), you
   can use the asynchronous `getServerTemplate` to initialize and load the
   template in a single step:

       // Initialize server-side Remote Config
       const rc = getRemoteConfig(firebaseApp);
       const template = await rc.getServerTemplate();

2. To ensure that your application runs successfully even if its connection to
   the Remote Config backend server is interrupted, add default values for
   each parameter to your app. To do this, add a `defaultConfig` inside your
   `initServerTemplate` or `getServerTemplate` template function:

       const template = rc.initServerTemplate({
         defaultConfig: {
           model_name: "gemini-pro",
           generation_config: '{"stopSequences": [], "temperature": 0.7, "maxOutputTokens": 512, "topP": 0.1, "topK": 20}',
           preamble_prompt: "I'm a developer who wants to learn about Firebase and you are a helpful assistant who knows everything there is to know about Firebase!"
         },
       });

       // Load Remote Config
       await template.load()

3. After the template loads, use `template.evaluate()` to import parameters and
   values from the template:

       // Add template parameters to config
       const config = template.evaluate();

4. Optionally, if you set
   [conditions](https://firebase.google.com/docs/remote-config/parameters?template_type=server#condition-rule-types)
   in your Remote Config template, define and provide the
   values you want:

   - If using [percentage
     conditions](https://firebase.google.com/docs/remote-config/parameters?template_type=server#user-in-random-percentage), add the `randomizationId` that you want to use to evaluate your condition(s) within the `template.evaluate()` function.
   - If using [custom
     signals](https://firebase.google.com/docs/remote-config/parameters?template_type=server#custom-signals), define the attributes and their values. Custom signals are available with Firebase Admin Node.js SDK 12.5.0 and higher.

   For example, you might set a Firebase [installation
   ID](https://firebase.google.com/docs/projects/manage-installations#retrieve_client_identifiers) as
   the `randomizationId`, or a user ID, to ensure that each user that
   contacts your server is added to the proper randomized group,
   `version` as a custom signal to target specific client versions, and
   `platform` as a custom signal to target client platform.

   > [!NOTE]
   > **Note:** The following example is simplified. In a real-world scenario, you'd likely configure your server to create unique randomization IDs for every client. This ensures that Remote Config consistently delivers the same values to each user, based on their assigned group in percentage-based conditions.

   For more information about conditions, see [Condition rule
   types](https://firebase.google.com/docs/remote-config/parameters?template_type=server#condition-rule-types).

       // Add template parameters to `config`. Evaluates the
       // template and returns the parameter value assigned to
       // the group assigned to the {randomizationId} and version.
       const config = template.evaluate({
         randomizationId: "2ac93c28-c459-4760-963d-a3974ec26c04",
         version: "1.0",
         platform: "Android"
       });

   > [!IMPORTANT]
   > **Important:** If no `randomizationId` or custom signal is specified when evaluating the template, the default value from the Remote Config template is returned.

5. Next, extract the parameter values you need from the config constant. Use `getters` to cast the values from Remote Config into the expected format. The following types are supported:

   - Boolean: `getBoolean`
   - Object: `getValue`
   - Number: `getNumber`
   - String: `getString`

   For example, if you are
   [implementing Vertex AI on your
   server](https://cloud.google.com/nodejs/docs/reference/vertexai/latest)
   and want to change the model and model parameters, you might want to
   configure parameters for `model_name` and `generation_config`. Here's an
   example of how you could access Remote Config's values:

       // Replace defaults with values from Remote Config.
       const generationConfig =
         JSON.parse(
           config.getString('generation_config'));

       const is_ai_enabled = config.getBool('is_ai_enabled');

       const model = config.getString('model_name');

       // Generates a prompt comprised of the Remote Config
       // parameter and prepends it to the user prompt
       const prompt = `${config.getString('preamble_prompt')} ${req.query.prompt}`;

6. If your server is long-running, as opposed to a serverless environment,
   use `setInterval` to periodically reload the template to confirm that you're
   fetching the most up-to-date template from the Remote Config server.

### Step 4: Set server-specific parameter values in Remote Config

Next, create a server Remote Config template and configure parameters and
values to use in your app.

To create a server-specific Remote Config template:

1. Open the [Firebase console Remote Config parameters
   page](https://console.firebase.google.com/project/_/config) and, from the **Client/Server** selector, select **Server**.
2. Define Remote Config parameters with the same names and data types as the parameters that you defined in your app and provide values. These values will override the `defaultConfig` you set in [Configure your
   server application](https://firebase.google.com/docs/remote-config/server#configure-server-app) when you fetch and evaluate the template and assign these values to your variables.
3. Optionally, set conditions to persistently apply values to a random sample of instances or custom signals you define. For more information about conditions, see [Condition rule
   types](https://firebase.google.com/docs/remote-config/parameters?template_type=server#condition-rule-types).
4. When you've finished adding parameters, click **Publish changes**.
5. Review the changes and click **Publish changes** again.

### Step 5: Deploy with Cloud Functions or Cloud Run

If your server application is lightweight and event-driven, you should consider
deploying your code using
[Cloud Functions](https://firebase.google.com/docs/functions). For example,
say you have an app that includes character dialogue powered by a generative AI
API (for example, Google AI or Vertex AI). In this case, you could host
your LLM-serving logic in a function that your app calls on-demand.

- To work through a solution that uses 2nd gen Cloud Functions with
  server-side Remote Config, see
  [Use server-side Remote Config with Cloud Functions and
  Vertex AI](https://firebase.google.com/docs/remote-config/solution-server).

- To learn more about deploying your app with Cloud Functions, see [Get
  started: write, test, and deploy your first
  functions](https://firebase.google.com/docs/functions/get-started?gen=2nd).

- Try out a sample callable function with server-side Remote Config and
  App Check at
  [Call the Vertex AI Gemini API with Remote Config and
  App Check](https://github.com/firebase/functions-samples/tree/main/Node/call-vertex-remote-config-server).

If you're building a server-rendered web app, [App Hosting](https://firebase.google.com/docs/app-hosting) has support for popular web frameworks.

Otherwise, you might consider [Cloud Run](https://cloud.google.com/run). To deploy
your server app with Cloud Run, follow the guide at [Quickstart: Deploy a
Node.js service to Cloud
Run](https://www.google.com/url?q=https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-nodejs-service).

For more information about the best use cases for Cloud Run and
Cloud Functions, refer to [Cloud Functions vs. Cloud Run: when to use
one over the
other](https://cloud.google.com/blog/products/serverless/cloud-run-vs-cloud-functions-for-serverless).

> [!NOTE]
> **Note:** Cloud Functions, App Hosting and Cloud Run require billing accounts. See [Cloud Functions pricing](https://firebase.google.com/pricing) and [Cloud Run
> pricing](https://cloud.google.com/run/pricing) for more information.