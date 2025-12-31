# Source: https://firebase.google.com/docs/functions/oncallgenkit.md.txt

<br />

Cloud Functions for Firebase has an`onCallGenkit`method that lets you create a[callable function](https://firebase.google.com/docs/functions/callable?gen=2nd)with a Genkit action (a Flow). These functions can be called with`genkit/beta/client`or the[Cloud Functions client SDKs](https://firebase.google.com/docs/functions/callable?gen=2nd#call_the_function), which automatically add auth information.

## Before you begin

- You should be familiar with Genkit's concept of[flows](https://genkit.dev/docs/flows/), and how to write them. The instructions on this page assume that you already have defined some flows that you want to deploy.
- It's helpful, but not required, if you've used Cloud Functions for Firebase before.

## Set up a Firebase project

1. Create a new Firebase project using the[Firebase console](https://console.firebase.google.com/), or choose an existing one.

2. Upgrade the project to the Blaze plan, which is required for Cloud Functions production deployment.

3. Install the[Firebase CLI](https://firebase.google.com/docs/cli).

4. Log in with the Firebase CLI:

       firebase login
       firebase login --reauth # alternative, if necessary
       firebase login --no-localhost # if running in a remote shell

5. Create a new project directory:

       export PROJECT_ROOT=~/tmp/genkit-firebase-project1
       mkdir -p $PROJECT_ROOT

6. Initialize a Firebase project in the directory:

       cd $PROJECT_ROOT
       firebase init functions

The rest of this page assumes that you've chosen to write your functions in JavaScript.

## Wrap the flow in`onCallGenkit`

After you've set up a Firebase project with Cloud Functions, you can copy or write flow definitions in the project's`functions`directory. Here is an example flow to demonstrate this:  

```javascript
const ai = genkit({
  plugins: [googleAI()],
  model: gemini15Flash,
});

const jokeTeller = ai.defineFlow({
  name: "jokeTeller",
  inputSchema: z.string().nullable(),
  outputSchema: z.string(),
  streamSchema: z.string(),
}, async (jokeType = "knock-knock", {sendChunk}) => {
  const prompt = `Tell me a ${jokeType} joke.`;

  // Call the `generateStream()` method to
  // receive the `stream` async iterable.
  const {stream, response: aiResponse} = ai.generateStream(prompt);

  // Send new words of the generative AI response
  // to the client as they are generated.
  for await (const chunk of stream) {
    sendChunk(chunk.text);
  }

  // Return the full generative AI response
  // to clients that may not support streaming.
  return (await aiResponse).text;
},
);https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/genkit-helloworld/functions/index.js#L39-L66
```

To deploy a flow like this one, wrap it with`onCallGenkit`, available in`firebase-functions/https`. This helper method has all the features of[callable functions](https://firebase.google.com/docs/functions/callable), and it automatically supports both streaming and JSON responses.  

```javascript
const {onCallGenkit} = require("firebase-functions/https");
```  

```javascript
exports.tellJoke = onCallGenkit({
  // Bind the Gemini API key secret parameter to the function.
  secrets: [apiKey],
},
// Pass in the genkit flow.
jokeTeller,
);https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/genkit-helloworld/functions/index.js#L70-L78
```

### Make API credentials available to deployed flows

Once deployed, your flows need a way to authenticate with any remote services they rely on. At a minimum, most flows need credentials for accessing the model API service they use.

For this example, do one of the following, depending on the model provider you chose:  

### Gemini (Google AI)

1. Make sure Google AI is[available in your region](https://ai.google.dev/available_regions).

2. [Generate an API key](https://aistudio.google.com/app/apikey)for the Gemini API using Google AI Studio.

3. Store your API key in Cloud Secret Manager:

       firebase functions:secrets:set GOOGLE_GENAI_API_KEY

   This step is important to prevent accidentally leaking your API key, which grants access to a potentially metered service.

   See[Store and access sensitive configuration information](https://firebase.google.com/docs/functions/config-env?gen=2nd#secret-manager)for more information on managing secrets.
4. Edit`src/index.js`and add the following after the existing imports:

   <br />

   ```javascript
   const {defineSecret} = require("firebase-functions/params");
   ```  

   ```javascript
   // Store the Gemini API key in Cloud Secret Manager.
   const apiKey = defineSecret("GOOGLE_GENAI_API_KEY");https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/genkit-helloworld/functions/index.js#L34-L35
   ```

   <br />

   Then, in the callable function definition, declare that the function needs access to this secret value:  

   ```javascript
   // Bind the Gemini API key secret parameter to the function.
   secrets: [apiKey],https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/genkit-helloworld/functions/index.js#L72-L73
   ```

Now, when you deploy this function, your API key will be stored in Cloud Secret Manager, and available from the Cloud Functions environment.

### Gemini (Vertex AI)

1. In the Cloud console,[Enable the Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=_)for your Firebase project.

2. On the[IAM](https://console.cloud.google.com/iam-admin/iam?project=_)page, ensure that the**Default compute service account** is granted the**Vertex AI User**role.

The only secret you need to set up for this tutorial is for the model provider, but in general, you must do something similar for each service your flow uses.

### (Optional) Add App Check enforcement

[Firebase App Check](https://firebase.google.com/docs/app-check)uses native attestation to verify that your API is only being called by your application.`onCallGenkit`supports App Check enforcement declaratively.  

    export const generatePoem = onCallGenkit({
      enforceAppCheck: true,
      // Optional. Makes App Check tokens only usable once. This adds extra security
      // at the expense of slowing down your app to generate a token for every API
      // call
      consumeAppCheckToken: true,
    }, generatePoemFlow);

### Configure CORS (Cross-Origin Resource Sharing)

Use the`cors`option to control which origins can access your function.

By default, callable functions have CORS configured to allow requests from all origins. To allow some cross-origin requests, but not all, pass a list of specific domains or regular expressions that should be allowed. For example:  

    export const tellJoke = onCallGenkit({
      cors: 'mydomain.com',
    }, jokeTeller);

### Complete example

After you've made all of the changes described above, your deployable flow will look something like the following example:  

```javascript
const {onCallGenkit} = require("firebase-functions/https");
const {defineSecret} = require("firebase-functions/params");

// Dependencies for Genkit.
const {gemini15Flash, googleAI} = require("@genkit-ai/googleai");
const {genkit, z} = require("genkit");

// Store the Gemini API key in Cloud Secret Manager.
const apiKey = defineSecret("GOOGLE_GENAI_API_KEY");

const ai = genkit({
  plugins: [googleAI()],
  model: gemini15Flash,
});

const jokeTeller = ai.defineFlow({
  name: "jokeTeller",
  inputSchema: z.string().nullable(),
  outputSchema: z.string(),
  streamSchema: z.string(),
}, async (jokeType = "knock-knock", {sendChunk}) => {
  const prompt = `Tell me a ${jokeType} joke.`;

  // Call the `generateStream()` method to
  // receive the `stream` async iterable.
  const {stream, response: aiResponse} = ai.generateStream(prompt);

  // Send new words of the generative AI response
  // to the client as they are generated.
  for await (const chunk of stream) {
    sendChunk(chunk.text);
  }

  // Return the full generative AI response
  // to clients that may not support streaming.
  return (await aiResponse).text;
},
);

exports.tellJoke = onCallGenkit({
  // Bind the Gemini API key secret parameter to the function.
  secrets: [apiKey],
},
// Pass in the genkit flow.
jokeTeller,
);https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/genkit-helloworld/functions/index.js#L18-L79
```

## Deploy flows to Firebase

After you've defined flows using`onCallGenkit`, you can deploy them as you would deploy other functions:  

    cd $PROJECT_ROOT
    firebase deploy --only functions