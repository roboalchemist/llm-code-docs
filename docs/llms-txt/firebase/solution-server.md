# Source: https://firebase.google.com/docs/remote-config/solution-server.md.txt

<br />

This guide describes how to get started using[2nd genCloud Functions](https://firebase.google.com/docs/functions/version-comparison#new-in-2nd-gen)with[server-sideRemote Config](https://firebase.google.com/docs/remote-config/server)to make server-side calls to the[Vertex AIGemini API](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal).

In this tutorial, you'll addRemote Configto a chatbot-like function that uses aGeminimodel to answer user questions.Remote Configwill manageGemini APIinputs (including a prompt that you'll prepend to incoming user queries), and you can update these inputs on-demand from theFirebaseconsole. You'll also use theFirebase Local Emulator Suiteto test and debug the function, and then, after verifying that it works, you'll deploy and test it onGoogle Cloud.
| **Important:** Vertex AIandCloud Functionsrequire a billing account. Review[Vertex AIpricing](https://cloud.google.com/vertex-ai/pricing)and[Cloud Functionspricing](https://firebase.google.com/pricing)before proceeding. If you're new to Firebase andGoogle Cloud, check to see if you're eligible for a[$300 credit](https://firebase.google.com/support/faq#pricing-free-trial)and a Free TrialCloud Billingaccount.

## Prerequisites

This guide assumes that you're familiar with using JavaScript to develop applications.

### Set up a Firebase project

**If you do not already have a Firebase project:**

1. Sign into the[Firebaseconsole](https://console.firebase.google.com/).

2. Click**Create project**, and then use either of the following options:

   - **Option 1** : Create a new Firebase project (and its underlyingGoogle Cloudproject automatically) by entering a new project name in the first step of the "Create project" workflow.
   - **Option 2** : "Add Firebase" to an existingGoogle Cloudproject by selecting yourGoogle Cloudproject name from the drop-down menu in the first step of the "Create project" workflow.
3. When prompted, you do***not*** need to set upGoogle Analyticsto use this solution.

4. Continue to follow the on-screen instructions to create your project.

**If you already have a Firebase project:**

Proceed to[Configure your development environment](https://firebase.google.com/docs/remote-config/solution-server#prereq-setup-env).

### Configure your development environment

You'll need a[Node.js](https://nodejs.org/)environment to write functions, and you'll need theFirebaseCLI to deploy functions to theCloud Functionsruntime.

1. Install[Node.js](https://nodejs.org/)and[npm](https://www.npmjs.org/).

   For installing Node.js and[npm](https://www.npmjs.org/), we recommend using[Node Version Manager](https://github.com/creationix/nvm/blob/master/README.md).
   | **Important:** We recommend using Node.js v20 or later. See[Set runtime options](https://firebase.google.com/docs/functions/manage-functions#set_nodejs_version)for important information about ongoing support for Node.js versions.
2. [Install theFirebaseCLI](https://firebase.google.com/docs/cli#setup_update_cli)using your preferred method. For example, to install the CLI using npm, run this command:

       npm install -g firebase-tools@latest

   This command installs the globally-available`firebase`command. If this command fails, you may need to[change npm permissions](https://docs.npmjs.com/getting-started/fixing-npm-permissions).

   To update to the latest version of`firebase-tools`, rerun the same command.
3. Install`firebase-functions`and`firebase-admin`and use`--save`to save them to your`package.json`:

       npm install firebase-functions@latest firebase-admin@latest --save

| **Tip:** In many cases, new features and bug fixes are available only with the latest version of theFirebaseCLI and the`firebase-functions`SDK. It's a good practice to frequently update both theFirebaseCLI and the SDK with these commands inside the`functions`folder of your codebase.

You're now ready to proceed to[implementation](https://firebase.google.com/docs/remote-config/solution-server#implementation)of this solution.

## Implementation

Follow these steps to create, test, and deploy your 2nd genCloud FunctionswithRemote ConfigandVertex AI:

1. [EnableVertex AIrecommended APIs in theGoogle Cloudconsole](https://firebase.google.com/docs/remote-config/solution-server#implementation-enable-apis).
2. [Initialize your project and install Node dependencies](https://firebase.google.com/docs/remote-config/solution-server#implementation-initialize-and-install).
3. [Configure IAM permissions for yourAdmin SDKservice account and save your key](https://firebase.google.com/docs/remote-config/solution-server#implementation-configure-permissions-and-save-key).
4. [Create the function](https://firebase.google.com/docs/remote-config/solution-server#implementation-create-function).
5. [Create a server-specificRemote Configtemplate](https://firebase.google.com/docs/remote-config/solution-server#implementation-create-template).
6. [Deploy your function and test it in theFirebase Local Emulator Suite](https://firebase.google.com/docs/remote-config/solution-server#implementation-deploy-and-test-in-emulator).
7. [Deploy your function toGoogle Cloud](https://firebase.google.com/docs/remote-config/solution-server#implementation-deploy-function-to-cloud).

### Step 1: EnableVertex AIrecommended APIs in theGoogle Cloudconsole

1. Open the[Google Cloudconsole](https://console.cloud.google.com?project=_), and when prompted, select your project.
2. In the**Search** field at the top of the console, enter**Vertex AI** and wait for**Vertex AI**to appear as a result.
3. Select**Vertex AI** . TheVertex AIdashboard appears.
4. Click**Enable All Recommended APIs**.

   It might take a few moments for API enablement to complete. Keep the page active and open until enablement finishes.
5. If billing isn't enabled, you'll be prompted to add or link aCloud Billingaccount. After enabling a billing account, return to theVertex AIdashboard and verify that all recommended APIs are enabled.

| **Important:** Vertex AIandCloud Functionsrequire a billing account. Review[Vertex AIpricing](https://cloud.google.com/vertex-ai/pricing)and[Cloud Functions pricing](https://firebase.google.com/pricing)for pricing information.

### Step 2: Initialize your project and install Node dependencies

1. Open a terminal on your computer and navigate to the directory where you plan to create your function.
2. Log into Firebase:

       firebase login

3. Run the following command to initializeCloud Functions for Firebase:

       firebase init functions

4. Select**Use an existing project**and specify your project ID.

5. When prompted to select the language to use, choose**Javascript**and press Enter.

6. For all other options, select the defaults.

   A`functions`directory is created in the current directory. Inside, you'll find an`index.js`file that you'll use to build out your function, a`node_modules`directory that contains the dependencies for your function, and a`package.json`file that contains the package dependencies.
7. Add theAdmin SDKandVertex AIpackages by running the following commands, using`--save`to ensure that it's saved to your`package.json`file:

       cd functions
       npm install firebase-admin@latest @google-cloud/vertexai --save

Your`functions/package.json`file should now look like the following, with the latest versions specified:  

      {
        "name": "functions",
        "description": "Cloud Functions for Firebase",
        "scripts": {
          "serve": "firebase emulators:start --only functions",
          "shell": "firebase functions:shell",
          "start": "npm run shell",
          "deploy": "firebase deploy --only functions",
          "logs": "firebase functions:log"
        },
        "engines": {
          "node": "20"
        },
        "main": "index.js",
        "dependencies": {
          "@google-cloud/vertexai": "^1.1.0",
          "firebase-admin": "^12.1.0",
          "firebase-functions": "^5.0.0"
        },
        "devDependencies": {
          "firebase-functions-test": "^3.1.0"
        },
        "private": true
      }

Note that if you're using ESLint, you'll see a stanza that includes it. In addition, make sure that the node engine version matches your installed version of Node.js and the version you ultimately run onGoogle Cloud. For example, if the`engines`stanza in your`package.json`is configured as Node version 18 and you're using Node.js 20, update the file to use 20:  

      "engines": {
        "node": "20"
      },

### Step 3: Configure IAM permissions for yourAdmin SDKservice account and save your key

In this solution, you'll use the FirebaseAdmin SDKservice account to run your function.

1. In theGoogle Cloudconsole, open the[*IAM \& Admin*page](https://console.cloud.google.com/iam-admin/iam?project=_), and locate theAdmin SDKservice account (named`firebase-adminsdk`).
2. Select the account and click**Edit principal**. The Edit access page appears.
3. Click**Add another role** , select**Remote ConfigViewer**.
4. Click**Add another role** , select**AI platform developer**.
5. Click**Add another role** , select**Vertex AIuser**.
6. Click**Add another role** , select**Cloud Run Invoker**.
7. Click**Save**.

Next, export the credentials for theAdmin SDKservice account and save them in your`GOOGLE_APPLICATION_CREDENTIALS`environment variable.

1. In theGoogle Cloudconsole, open the[*Credentials*page](https://console.cloud.google.com/apis/credentials?project=_).
2. Click the**Admin SDK** service account to open the*Details*page.
3. Click**Keys**.
4. Click**Add key** \>**Create new key**.
5. Ensure that**JSON** is selected as the**Key type** , then click**Create**.
6. Download the key to a safe place on your computer.
7. From your terminal, export the key as an environment variable:

       export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"

| **Tip:** If you plan to use multiple terminal windows for this session, consider adding`GOOGLE_APPLICATION_CREDENTIALS`as a system variable.

### Step 4: Create the function

In this step, you'll construct a function that handles user input and generates AI-powered responses. You'll combine multiple code snippets to build a comprehensive function that initializes theAdmin SDKandVertex AIGemini API, configures default parameters usingRemote Config, fetches the latestRemote Configparameters, processes user input, and streams a response back to the user.
| **Important:** The code for this function is provided in multiple snippets. You must combine them all into a single`index.js`file before running the function.

1. In your codebase, open`functions/index.js`in a text editor or IDE.
2. Delete the existing content and then add theAdmin SDK,Remote Config, and theVertex AISDK and initialize the app by pasting the following code into the file:

       const { onRequest } = require("firebase-functions/https");
       const logger = require("firebase-functions/logger");

       const { initializeApp } = require("firebase-admin/app");
       const { VertexAI } = require('@google-cloud/vertexai');
       const { getRemoteConfig } = require("firebase-admin/remote-config");

       // Set and check environment variables.
       const project = process.env.GCLOUD_PROJECT;

       // Initialize Firebase.
       const app = initializeApp();  
       https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/remote-config-server-with-vertex/functions/index.js#L2-L13

3. Configure default values that your function will use if it can't connect to theRemote Configserver. This solution configures`textModel`,`generationConfig`,`safetySettings`,`textPrompt`, and`location`asRemote Configparameters that correspond withRemote Configparameters that you'll configure further on in this guide. For more information about these parameters, see[Vertex AI Node.js client](https://cloud.google.com/nodejs/docs/reference/aiplatform/latest).

   Optionally, you can also configure a parameter to control whether or not you access theVertex AIGemini API(in this example, a parameter called`vertex_enabled`). This setup can be useful when testing your function. In the following code snippets, this value is set to`false`, which will skip usingVertex AIwhile you test basic function deployment. Setting it to`true`will invoke theVertex AIGemini API.  

       // Define default (fallback) parameter values for Remote Config.
       const defaultConfig = {

         // Default values for Vertex AI.
         model_name: "gemini-1.5-flash-002",
         generation_config: [{
           "stopSequences": [], "temperature": 0.7,
           "maxOutputTokens": 64, "topP": 0.1, "topK": 20
         }],
         prompt: "I'm a developer who wants to learn about Firebase and you are a \
           helpful assistant who knows everything there is to know about Firebase!",
         safety_settings: [{
           "category":
             "HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT",
           "threshold": "HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE"
         }],
         location: 'us-central1',

         // Disable Vertex AI Gemini API access for testing.
         vertex_enabled: false
       };  
       https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/remote-config-server-with-vertex/functions/index.js#L17-L37

4. Create the function and set up[server-sideRemote Config](https://firebase.google.com/docs/remote-config/server):

       // Export the function.
       exports.generateWithVertex = onRequest(async (request, response) => {

         try {

           // Set up Remote Config.
           const rc = getRemoteConfig(app);

           // Get the Remote Config template and assign default values.
           const template = await rc.getServerTemplate({
             defaultConfig: defaultConfig
           });

           // Add the template evaluation to a constant.
           const config = template.evaluate();

           // Obtain values from Remote Config.
           const textModel = config.getString("model_name") ||
               defaultConfig.model_name;
           const textPrompt = config.getString("prompt") || defaultConfig.prompt;
           const generationConfig = config.getString("generation_config") ||
               defaultConfig.generation_config;
           const safetySettings = config.getString("safety_settings") ||
               defaultConfig.safety_settings;
           const location = config.getString("location") ||
               defaultConfig.location;
           const vertexEnabled = config.getBoolean("is_vertex_enabled") ||
               defaultConfig.vertex_enabled;  
       https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/remote-config-server-with-vertex/functions/index.js#L41-L68

5. Set upVertex AIand add the chat and response logic:

         // Allow user input.
         const userInput = request.query.prompt || '';

         // Instantiate Vertex AI.
           const vertex_ai = new VertexAI({ project: project, location: location });
           const generativeModel = vertex_ai.getGenerativeModel({
             model: textModel,
             safety_settings: safetySettings,
             generation_config: generationConfig,
           });

           // Combine prompt from Remote Config with optional user input.
           const chatInput = textPrompt + " " + userInput;

           if (!chatInput) {
             return res.status(400).send('Missing text prompt');
           }
           // If vertexEnabled isn't true, do not send queries to Vertex AI.
           if (vertexEnabled !== true) {
             response.status(200).send({
               message: "Vertex AI call skipped. Vertex is not enabled."
             });
             return;
           }

           logger.log("\nRunning with model ", textModel, ", prompt: ", textPrompt,
             ", generationConfig: ", generationConfig, ", safetySettings: ",
             safetySettings, " in ", location, "\n");

           const result = await generativeModel.generateContentStream(chatInput); 
           response.writeHead(200, { 'Content-Type': 'text/plain' });

           for await (const item of result.stream) {
             const chunk = item.candidates[0].content.parts[0].text;
             logger.log("Received chunk:", chunk);
             response.write(chunk);
           }

           response.end();

         } catch (error) {
           logger.error(error);
           response.status(500).send('Internal server error');
         }
       });  
       https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/remote-config-server-with-vertex/functions/index.js#L72-L116

6. Save and close the file.

| **Tip:** Learn more about usingVertex AIwith Node.js to generate multi-modal and streamed responses at[Vertex AI for Node.js quickstart](https://cloud.google.com/nodejs/docs/reference/vertexai/latest).

### Step 5: Create a server-specificRemote Configtemplate

Next, create a server-sideRemote Configtemplate and configure parameters and values to use in your function. To create a server-specificRemote Configtemplate:

1. Open theFirebaseconsole and, from the navigation menu, expand**Run** and select[**Remote Config**](https://console.firebase.google.com/project/_/config).
2. Select**Server** from the**Client/Server** selector at the top of theRemote Configpage.

   - If this is your first time usingRemote Configor server templates, click**Create Configuration** . The**Create your first server-side parameter**pane appears.
   - If this is not your first time usingRemote Configserver templates, click**Add parameter**.
3. Define the followingRemote Configparameters:

   | **Parameter name**  |                                                                                                                                    **Description**                                                                                                                                     | **Type** |                                                             **Default value**                                                             |
   |---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------|
   | `model_name`        | Model name For up-to-date lists of model names to use in your code, see[Model versions and lifecycles](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versioning)or[Available model names](https://firebase.google.com/docs/ai-logic/models#available-model-names). | String   | `gemini-2.0-flash`                                                                                                                        |
   | `prompt`            | Prompt to prepend to the user's query.                                                                                                                                                                                                                                                 | String   | `I'm a developer who wants to learn about Firebase and you are a helpful assistant who knows everything there is to know about Firebase!` |
   | `generation_config` | [Parameters to send to the model](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/GenerationConfig).                                                                                                                                                                         | JSON     | `[{"stopSequences": ["I hope this helps"],"temperature": 0.7,"maxOutputTokens": 512, "topP": 0.1,"topK": 20}]`                            |
   | `safety_settings`   | [Safety settings forVertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-attributes#gemini-TASK-samples-nodejs).                                                                                                                               | JSON     | `[{"category": "HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "HarmBlockThreshold.BLOCK_LOW_AND_ABOVE"}]`                   |
   | `location`          | [Location to run theVertex AIservice and model](https://cloud.google.com/vertex-ai/docs/general/locations).                                                                                                                                                                            | String   | `us-central1`                                                                                                                             |
   | `is_vertex_enabled` | Optional parameter that controls whether queries are sent toVertex AI.                                                                                                                                                                                                                 | Boolean  | `true`                                                                                                                                    |

   | **Important:** Models are updated frequently. For a current list of models thatVertex AIsupports, see[Model versions and lifecycle](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versioning).
4. When you've finished adding parameters, double-check your parameters and that their data types are correct, then click**Publish changes**.

### Step 6: Deploy your function and test it in theFirebase Local Emulator Suite

Now you're ready to deploy and test your function locally with theFirebase Local Emulator Suite.

1. Make sure that you've set`GOOGLE_APPLICATION_CREDENTIALS`as an environment variable as described in[Step 3: Configure IAM permissions for yourAdmin SDKservice account and save your key](https://firebase.google.com/docs/remote-config/solution-server#implementation-configure-permissions-and-save-key). Then, from the parent directory of your`functions`directory, deploy your function to the Firebase emulator:

       firebase emulators:start --project <var label="project_id" translate="no">PROJECT_ID</var> --only functions

   | **Tip:** You can also run functions in the emulator by running`npm run serve`from the`functions`directory.
2. Open[the emulator's logs page](http://localhost:4000/logs?q=metadata.emulator.name%3D%22functions%22). This should show that your function has loaded.

3. Access your function by running the following command, where<var label="project_id" translate="no">PROJECT_ID</var>is your project ID and<var label="location" translate="no">LOCATION</var>is the region that you deployed the function to (for example,`us-central1`):

       curl http://localhost:5001/<var label="project_id" translate="no">PROJECT_ID</var>/<var label="location" translate="no">LOCATION</var>/generateWithVertex

   | **Tip:** This link will also appear in your console output after starting the emulator. You can also cut and paste it into a browser.
4. Wait for a response, then return to the Firebase Emulator logs page or your console and check for any errors or warnings.

5. Try sending some user input, noting that because`is_vertex_enabled`is configured in yourRemote Configserver template, this should access theGeminimodel through theVertex AIGemini APIand that this may incur charges:

       curl http://localhost:5001/<var label="project_id" translate="no">PROJECT_ID</var>/<var label="location" translate="no">LOCATION</var>/generateWithVertex?prompt=Tell%20me%20everything%20you%20know%20about%20cats

6. Make changes to yourRemote Configserver template on theFirebaseconsole, then re-access your function to observe changes.

| **Tip:** For more information about testingCloud Functionswith Firebase, see[Test functions interactively](https://firebase.google.com/docs/functions/local-shell).

### Step 7: Deploy your function toGoogle Cloud

After you've tested and verified your function, you're ready to deploy toGoogle Cloudand test the live function.
| **Important:** While testing functions in the Firebase emulator is a no-cost action, any calls toVertex AIwhen using the emulator are still charged. Also, after you deploy the functions, any invocation of those functions can incur costs. Review[Vertex AIpricing](https://cloud.google.com/vertex-ai/pricing)and[Cloud Functions pricing](https://firebase.google.com/pricing)before proceeding.

#### Deploy your function

Deploy your function using theFirebaseCLI:  

    firebase deploy --only functions

#### Block unauthenticated access to the function

When functions are deployed using Firebase, unauthenticated invocations are allowed by default if your organization's policy doesn't restrict it. During testing and before securing with[App Check](https://firebase.google.com/docs/app-check), we recommend blocking unauthenticated access.

To block unauthenticated access to the function:

1. In theGoogle Cloudconsole, open[Cloud Run](https://console.cloud.google.com/run).

2. Click`generateWithVertex`, then click the**Security**tab.

3. Enable**Require authentication** and then click**Save**.

#### Configure your user account to use theAdmin SDKservice account credentials

Because theAdmin SDKservice account has all the necessary roles and permissions to run the function and interact with theRemote Configand theVertex AIGemini API, you'll want to use it to run your function. To do this, you must be able to create tokens for the account from your user account.

The following steps describe how to configure your user account and the function to run with theAdmin SDKservice account privileges.

1. In theGoogle Cloudconsole, enable the[**IAM Service Account Credentials API**](https://console.cloud.google.com/apis/enableflow?apiid=iamcredentials.googleapis.com&project=_).
2. Give your user account the**Service Account Token Creator** role: From theGoogle Cloudconsole, open**IAM \& Admin** \>**IAM** , select your user account, and then click**Edit principal** \>**Add another role**.
3. Select**Service Account Token Creator** , then click**Save**.

   For more detailed information about service account impersonation, refer to[Service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation)in theGoogle Clouddocumentation.
4. Open the[Google CloudconsoleCloud Functionspage](https://console.cloud.google.com/functions/list?project=_)and click the**generateWithVertex** function in the**Functions**list.

5. Select**Trigger** \>**Edit** and expand**Runtime, build, connections and security settings**.

6. From the**Runtime** tab, change the**Runtime service account** to the**Admin SDK account**.

7. Click**Next** , then click**Deploy**.

#### Set up the gcloud CLI

To securely run and test your function from the command line, you'll need to authenticate with theCloud Functionsservice and obtain a valid authentication token.

To enable token generation, install and configure the gcloud CLI:

1. If not already installed on your computer, install the gcloud CLI as described in[Install the gcloud CLI](https://cloud.google.com/sdk/docs/install).

2. Obtain access credentials for yourGoogle Cloudaccount:

       gcloud auth login

3. Set your project ID in gcloud:

       gcloud config set project <var label="project_id" translate="no">PROJECT_ID</var>

#### Test your function

You're now ready to test your function inGoogle Cloud. To test the function, run the following command:  

    curl -X POST https://<var label="location" translate="no">LOCATION</var>-<var label="project_id" translate="no">PROJECT_ID</var>.cloudfunctions.net/generateWithVertex \
      -H "Authorization: bearer $(gcloud auth print-identity-token)" \
      -H "Content-Type: application/json"

Try again with user-supplied data:  

    curl -X POST https://<var label="location" translate="no">LOCATION</var>-<var label="project_id" translate="no">PROJECT_ID</var>.cloudfunctions.net/generateWithVertex?prompt=Tell%20me%20everything%20you%20know%20about%20dogs \
     -H "Authorization: bearer $(gcloud auth print-identity-token)" \
     -H "Content-Type: application/json"

You can now make changes to yourRemote Configserver template, publish those changes, and test different options.

## Next steps

- Firebase recommends using[App Check](https://firebase.google.com/docs/app-check)to secureCloud Functions. See[EnableApp Checkenforcement forCloud Functions](https://firebase.google.com/docs/app-check/cloud-functions)for more information about securing your function withApp Check
- Try out a sample callable function with server-sideRemote ConfigandApp Checkat[Call theVertex AIGemini APIwithRemote ConfigandApp Check](https://github.com/firebase/functions-samples/tree/main/Node/call-vertex-remote-config-server).
- Learn more about[Cloud Functionsfor Firebase](https://firebase.google.com/docs/functions).
- Learn more about[usingRemote Configin server environments](https://firebase.google.com/docs/remote-config/server).