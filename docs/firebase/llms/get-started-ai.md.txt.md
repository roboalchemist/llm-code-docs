# Source: https://firebase.google.com/docs/studio/get-started-ai.md.txt

# Get started with the App Prototyping agent

<br />

Firebase Studio includes a web-based interface that lets you rapidly
prototype and generate AI-forward web apps using multimodal prompts, including
natural language, images, and drawing tools. The agent supports
Next.js apps, with other platforms and frameworks planned in the future.

The App Prototyping agent is a streamlined no-code development flow that
uses generative AI to develop, test, iterate, and publish a full-stack,
agentic web app. You describe your app idea in natural language with an
optional image, and
the agent generates an app blueprint, code, and a web preview. To
assist in the development and publishing of your full-stack app,
Firebase Studio can automatically provision the following services for you:

- **If your app uses AI:** Firebase Studio adds the Gemini Developer API to your app, using the power of [Genkit](https://firebase.google.com/docs/genkit) flows to work with Gemini. You can use your own Gemini API key or let Firebase Studio provision a Firebase project and Gemini API key for you.
- **If you want to publish your app to the web:** Firebase Studio creates a project and provides a quick way to publish your app with [Firebase App Hosting](https://firebase.google.com/docs/app-hosting).

> [!IMPORTANT]
> **Important:** When the App Prototyping agent sets up the Gemini API key and other Firebase services, it creates a new Firebase project to associate with the workspace. At this time, this is the only project that can be associated when publishing from the App Prototyping agent view. Note that you can publish to other Firebase projects by [checking your code into
> GitHub](https://firebase.google.com/docs/studio/github) and [creating an App Hosting
> backend](https://firebase.google.com/docs/app-hosting/get-started). You can also use [Code
> view](https://firebase.google.com/docs/studio/google-integrations) to integrate Firebase services.

You can refine the app using natural language, images, and drawing tools,
edit code directly, roll back changes, publish the app,
and monitor its performance---all from Firebase Studio.

> [!NOTE]
> **Note:** The App Prototyping agent can help you build web apps with Next.js. Support for other platforms and frameworks is coming soon!

## Get started

To get started with the App Prototyping agent, follow these steps:

1. Log into your Google Account and open
   [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

2. In the **Prototype an app with AI** field, describe your app idea in
   natural language.

   For example, you could enter a prompt like the following to create a
   recipe generation app:

       Use secure coding practices to create an error-free web app that lets
       users upload a photo or take a picture with their browser
       camera. The app identifies the food in the picture and generates a
       recipe and accompanying image that includes that food.

       If no food product is identified, generate a random dessert recipe.

   > [!TIP]
   > **Tip:** For best results, be as specific as possible in your prompt. Include the features you want, user workflows, and data requirements. Optionally, click **Improve prompt** to ask Gemini to refine your initial prompt. Also understand that the most effective development processes with AI are iterative and you can continue to refine and add features collaboratively with Gemini. Learn more about crafting [effective prompts](https://firebase.google.com/docs/studio/prompting).

3. Optionally, upload an image to accompany your prompt. For example, you
   can upload an image that contains the color scheme you want your app to
   use and tell Firebase Studio to use it. Images must be less than 3 MiB.

4. Click **Prototype with AI**.

   The App Prototyping agent generates an app blueprint based on your
   prompt, returning a proposed app name, required features,

   and style guidelines.
5. Review the blueprint. If necessary, make a few changes. For example,
   you could change the proposed app name or color scheme using one of
   these options:

   - Click **Customize** and edit the
     blueprint directly. Make your changes and click **Save**.

   - In the **Describe...** field in the chat pane, add clarifying questions
     and context. You can also upload additional images.

6. Click **Prototype this app**.

   **Important:** Gemini can
   generate output that seems plausible but is
   factually incorrect. It may respond with inaccurate information
   that doesn't represent Google's views. Validate all output from
   Gemini before you use it and do not use untested
   generated code in production. Do not enter personally-identifiable
   information (PII) or user data into the chat.
7. The App Prototyping agent begins coding your app.

   - If your app uses AI, you're prompted to add or generate a [Gemini API key](https://ai.google.dev/gemini-api/docs/api-key). If you click Auto-generate, the App Prototyping agent provisions a Firebase project and a Gemini API key for you.

   > [!IMPORTANT]
   > **Important:** If you choose **Auto-generate** , the App Prototyping agent creates a [Firebase project](https://firebase.google.com/docs/projects/learn-more) on your behalf with a prefix that matches the name of your Firebase Studio workspace and creates a new Gemini API key in the project. It also stores the key within your Firebase Studio workspace in an `.env` file. To access your new project at any time, click the project name at the top of the page. To access your Gemini API key to copy or delete in the future, use the [Google Cloud console](https://firebase.google.com/docs/studio/https://console.cloud.google.com/apis/credentials).

## Test, refine, debug, and iterate

After the initial app is generated, you can test, refine, debug, and iterate.


- **Review and interact with your app:** After code generation completes,
  a preview of your app appears. You can interact with the preview directly to
  test it. Learn more at [Preview your app](https://firebase.google.com/docs/studio/preview-apps).

- **Add Cloud Firestore and Firebase Authentication:** During the iteration phase,
  you can ask the App Prototyping agent to add user authentication and a
  database using Cloud Firestore and Firebase Authentication. For example, give users
  the ability to save and download recipes with a prompt like the following:

      Add user authentication to the app. Authenticated users can:

        - Download the recipe and its generated image as a PDF (Print).

        - Save the recipe as public or private and make accessible to a search
          feature. For now, just save the text, not the image, to the database.

      Important: Only authenticated users can download the PDF.

  > [!TIP]
  > **Tip:** The App Prototyping agent can add Cloud Firestore and Firebase Authentication to your app during the iteration phase, not in the initial app blueprint.

- **Fix any errors as they occur:** In most cases, the App Prototyping agent
  prompts you to fix any errors that arise. Click **Fix Error** to allow
  it to attempt a fix.

  If you receive errors that you're not prompted to fix automatically,
  copy the error and any relevant context (for example, "Can you fix this
  error in my Firebase initialization code?") into the chat window and
  send it to Gemini.

  > [!TIP]
  > **Tip:** Gemini explains its reasoning, but you can also ask it to explain its plan before it executes it.

- **Test and iterate using natural language:** Test your app thoroughly and
  work with the App Prototyping agent to iterate on the code and blueprint
  until you're happy with it.

  While in Prototyper view, you can also use the following features:
  - Click ![Annotate icon](https://firebase.google.com/static/docs/studio/images/icons/annotate-icon.png)
    **Annotate** to draw directly on the Preview window. Use the available
    shape, image, and text tools, along with an optional text prompt, to
    visually describe what you want the App Prototyping agent to change.

  - Click ![Select icon](https://firebase.google.com/static/docs/studio/images/icons/select-icon.png)
    **Select** to select a specific element and enter instructions for
    the App Prototyping agent. This lets you quickly target a specific icon,
    button, piece of text, or other element. When you click an image, you also
    have the option of searching for and selecting a stock image from
    [Unsplash](https://unsplash.com).

  Optionally, you can click ![Link
  icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-link.svg)
  **Share preview link** to share your app publicly and temporarily using
  Firebase Studio [public previews](https://firebase.google.com/docs/studio/preview-apps#share).
- **Create a Firebase project:** The App Prototyping agent provisions a
  [Firebase project](https://firebase.google.com/docs/projects/learn-more) on your behalf when you:

  - Auto-generate a Gemini API key
  - Ask to connect your app to a Firebase project
  - Ask for help connecting your app to Firebase services, such as Cloud Firestore or Firebase Authentication
  - Click the **Publish** button and set up Firebase App Hosting

  To change the Firebase project connected to your workspace, prompt
  the App Prototyping agent with the project ID you want to use instead. For
  example, "Switch to Firebase project with ID `<your-project-id>`."
- **Test the app and verify Cloud Firestore database rules:** In the app
  preview pane, upload an image that shows different foods to test your
  app's ability to identify the ingredients and generate and save recipes.

  Sign in as different users and generate recipes: make sure that
  authenticated users can see their private recipes and recipes and that
  all users see public recipes.

  When you ask the App Prototyping agent to add Cloud Firestore, it writes
  and deploys Cloud Firestore database rules for you. Review the rules in the
  [Firebase console](https://firebase.google.com/docs/studio/https://console.firebase.google.com/project/_/firestore/databases/-default-/rules).
- **Debug and iterate directly in the code:** Click ![Code switch
  icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)
  **Switch to Code** to open Code view, where you can see
  all of your app's files and modify your code directly. You can switch back
  to Prototyper mode at any time.

  While in Code view, you can also use the following
  helpful features:
  - Firebase Studio's
    [built-in debugging and reporting features](https://firebase.google.com/docs/studio/debug) to
    inspect, debug, and audit your app.

  - [AI assistance using Gemini](https://firebase.google.com/docs/studio/try-gemini)
    either inline within your code or using Gemini interactive chat
    (both are available by default). Interactive chat can
    diagnose issues, provide solutions, and run tools to help fix your app
    faster.
    To access chat, click
    spark**Gemini**
    at the bottom of the workspace.

    > [!NOTE]
    > **Note:** Apps created with the App Prototyping agent default to the Prototyper chat in Code view. To use Gemini interactive chat instead, under **Gemini** , click **+** , then select **New Chat** . To return to Prototyper chat, click history **Recent chats** , and then choose **Prototyper chat**.

  - [Access the Firebase Local Emulator Suite to view database and
    authentication data](https://firebase.google.com/docs/emulator-suite). To open the emulator in
    your workspace:

    1. Click ![Code switch
       icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)
       **Switch to Code** and open the **Firebase Studio** extension
       (`Ctrl+',Ctrl+'`, or `Cmd+',Cmd+'` on MacOS).

    2. Scroll to **Backend ports** and expand it.

    3. In the **Actions** column that corresponds to **Port 4000** , click
       **Open in new window**.

- **Test and measure your generative AI feature performance:** You can use
  the Genkit Developer UI to run your Genkit AI flows, test, debug, interact
  with different models, refine your prompts, and more.

  To load your Genkit flows in the Genkit Developer UI and start testing:
  1. From the terminal in your Firebase Studio workspace, run the
     following command to source your Gemini API key and start the
     Genkit server:

          npm run genkit:watch

  2. Click the Genkit Developer UI link. The Genkit Developer UI opens in
     a new window with your flows, prompts, embedders, and a selection of
     different available models.

  Learn more about the Genkit Developer UI at [Genkit Developer
  Tools](https://genkit.dev/docs/devtools/).

## Publish your app with Firebase App Hosting

After you've tested your app and are satisfied with it in your workspace,
you can publish it to the web with
[Firebase App Hosting](https://firebase.google.com/docs/app-hosting).

> [!CAUTION]
> **Important:** Firebase App Hosting requires a Cloud Billing account. When you link a billing account to a Firebase project, then your project is automatically upgraded to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) and your Gemini API and other Firebase and Google Cloud service usage is upgraded to the paid tier. You will be charged for usage of paid services that exceed the no-cost quota. Learn more at [Understand
> App Hosting costs](https://firebase.google.com/docs/app-hosting/costs), [Firebase pricing](https://firebase.google.com/pricing), and [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing).

When you set up App Hosting, Firebase Studio creates a
[Firebase project](https://firebase.google.com/docs/studio/firebase-projects)
for you (if one was not already created by auto-generating a Gemini API key
or other backend services)
and guides you through linking a Cloud Billing account.

To publish your app:

1. Click **Publish** to set up your
   [Firebase project](https://firebase.google.com/docs/studio/firebase-projects) and publish your app.
   The **Publish your app** pane appears.

   > [!IMPORTANT]
   > **Important:** If you did not [auto-generate a Gemini API
   > key](https://firebase.google.com/docs/studio/get-started-ai#get-started) or prompt the App Prototyping agent to create a Firebase project, Firebase Studio provisions a [Firebase
   > project](https://firebase.google.com/docs/studio/firebase-projects) on your behalf when you click **Publish**. You can access the Firebase project by clicking the project name at the top of the page.

2. In the **Firebase project** step, the App Prototyping agent displays the
   Firebase project associated with the workspace. If a Firebase project
   doesn't already exist, the App Prototyping agent creates a new project for
   you. Click **Next** to proceed.

3. In the **Link Cloud Billing account** step, choose one of the following:

   - Select the Cloud Billing account that you want to link to your Firebase
     project.

   - If you don't have a Cloud Billing account or want to create a new one,
     click **Create a Cloud Billing account** . This opens the
     Google Cloud console, where you can [create a new self-serve
     Cloud Billing
     account](https://cloud.google.com/billing/docs/how-to/create-billing-account).
     After you create the account, return to Firebase Studio and select
     the account from the **Link Cloud Billing** list.

4. Click **Next** . Firebase Studio links the billing account to the project
   associated with your workspace, created either when you auto-generated a
   Gemini API key or when you clicked **Publish**.

   > [!CAUTION]
   > **Important:** Firebase App Hosting requires a Cloud Billing account. When you link a billing account to a Firebase project, then your project is automatically upgraded to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) and your Gemini API and other Firebase and Google Cloud service usage is upgraded to the paid tier. You will be charged for usage of paid services that exceed the no-cost quota. Learn more at [Understand
   > App Hosting costs](https://firebase.google.com/docs/app-hosting/costs), [Firebase pricing](https://firebase.google.com/pricing), and [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing).

5. Click **Set up services** . The App Prototyping agent begins
   provisioning Firebase services.

6. Click **Publish now** . Firebase Studio sets up Firebase services
   and then launches the App Hosting rollout. This can take up to several
   minutes to complete.
   To learn more about what's happening behind the scenes, see
   [The App Hosting build process](https://firebase.google.com/docs/app-hosting/build).

   > [!TIP]
   > **Tip:** If you don't want to publish now, you can click **Publish later**.

7. When the publish step completes, the **App overview** appears with a
   URL and app insights powered by App Hosting observability. To use a
   custom domain (like example.com or app.example.com) instead of the
   Firebase-generated domain, you can [add a custom
   domain](https://firebase.google.com/docs/app-hosting/custom-domain) in the Firebase console.

> [!TIP]
> **Tip:** If you receive any errors during publishing, see [I received a "Failed to
> publish app" error after
> publishing](https://firebase.google.com/docs/studio/troubleshooting#failed-to-publish) for instructions on how to find and fix publishing errors.

For more information about App Hosting, see
[Understand App Hosting and how it
works](https://firebase.google.com/docs/app-hosting/about-app-hosting).

## Secure your app with Firebase App Check and reCAPTCHA Enterprise

If you've integrated Firebase or Google Cloud services into your app,
Firebase App Check helps protect your app backends from abuse by preventing
unauthorized clients from accessing your Firebase resources. It works with
both Google services (including Firebase and Google Cloud services) and
your own custom backends to keep your resources safe.

We recommend adding App Check to any app you post publicly to protect your
backend resources from abuse.

This section guides you through setting up App Check within
Firebase Studio using [reCAPTCHA
Enterprise](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider) for a web app
created by the App Prototyping agent, but you can set up App Check within
any app that implements Firebase services and can implement custom providers.
Learn more at [Firebase App Check](https://firebase.google.com/docs/app-check).

ReCAPTCHA Enterprise provides [up to 10,000 assessments at
no-cost](https://cloud.google.com/recaptcha/docs/compare-tiers).

### Step 1: Set up reCAPTCHA Enterprise for your app

1. Open the [reCAPTCHA Enterprise](https://console.cloud.google.com/security/recaptcha?project=_)
   section of the Google Cloud console.

2. Select the name of your Firebase project from the Google Cloud console
   project picker.

3. If you're prompted to enable the reCAPTCHA Enterprise API, do so.

4. Click **Get started** , and add a **Display name** for your reCAPTCHA
   site key.

5. Accept the default **Web** **Application type** key.

6. Click **Add a domain** and add a domain. You'll want to add your
   App Hosting domain (for example,
   `studio--PROJECT_ID.REGION.hosted.app`)
   and any custom domains you use with or plan to use with your app.

7. Click **Next step**.

8. Leave **Will you use challenges?** unselected.

9. Click **Create key**.

10. Copy and save your **Key ID** and proceed to [**Configure App Check**](https://firebase.google.com/docs/studio/get-started-ai#configure-app-check).

### Step 2: Configure App Check

1. Open the
   [Firebase console](https://firebase.google.com/docs/studio/https://console.firebase.google.com/project/_/appcheck)
   and click **Build** \> **App Check** from the navigation menu.

2. Click **Get started** , then click **Register** next to your app.

3. Click to expand **ReCAPTCHA** and paste the Key ID you generated for
   reCAPTCHA Enterprise.

4. Click **Save**.

### Step 3: Add App Check to your code

1. Return to Firebase Studio and in Code view, add
   the site key you generated to your `.env` file:

       NEXT_PUBLIC_RECAPTCHA_SITE_KEY=RECAPTCHA_SITE_KEY

2. If you don't already have your Firebase configuration saved to `.env`,
   obtain it:

   - From the
     [Firebase console](http:https://console.firebase.google.com/project/_/settings),
     open **Project settings** and locate it within your the section that
     corresponds with your app.

   - From the Terminal in Code view:

     1. Log into Firebase: `firebase auth login`
     2. Select your project: `firebase use FIREBASE_PROJECT_ID`
     3. Obtain the Firebase config: `firebase apps:sdkconfig`
3. Add the configuration to your `.env` file so that it looks like the
   following:

       NEXT_PUBLIC_FIREBASE_API_KEY=FIREBASE_API_KEY
       NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=FIREBASE_AUTH_DOMAIN
       NEXT_PUBLIC_FIREBASE_PROJECT_ID=FIREBASE_PROJECT_ID
       NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=FIREBASE_STORAGE_BUCKET
       NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=FIREBASE_MESSAGING_SENDER_ID
       NEXT_PUBLIC_FIREBASE_APP_ID=FIREBASE_APP_ID
       NEXT_PUBLIC_RECAPTCHA_SITE_KEY=RECAPTCHA_SITE_KEY

4. Add App Check to your app code. You can ask Gemini to add
   App Check with reCAPTCHA Enterprise to your app (be sure to
   specify "reCAPTCHA Enterprise" and be sure to double-check it!), or
   follow the steps in [Initialize
   App Check](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider#initialize).

5. Re-publish your site to App Hosting. Try testing your
   database and authentication features to generate some data.

6. Verify that App Check is receiving requests in the
   Firebase console by opening **Build** \> **App Check**.

7. Click to inspect Cloud Firestore. After you verify that requests arrive,
   click **Enforce** to enforce App Check.

8. Repeat verification and enforcement for Firebase Authentication.

If, after you have registered your app for App Check, you want to run your
app in an environment that App Check would normally not classify as valid,
such as locally during development, or from a continuous integration (CI)
environment, you can create a debug build of your app that uses the
App Check debug provider instead of a real attestation provider. Learn more
at [Use App Check with the debug provider in web
apps](https://firebase.google.com/docs/app-check/web/debug-provider).

## Monitor your app

The **App overview** panel in Firebase Studio provides key
metrics and information about your app, letting you monitor your web app's
performance using App Hosting's built-in observability tools. After your
site rolls out, you can access the overview by clicking **Publish**. From this
panel, you can:

- Click **Publish** to release a new version of your app.
- Share the link to your app or open your app directly in **Visit your app**.
- Review a summary of your app's performance over the last 7 days, including the total number of requests and the status of your latest rollout. Click **View details** to access even more information in the [Firebase console](https://firebase.google.com/docs/studio/https://console.firebase.google.com/project/_/apphosting/).
- View a graph of the number of the number of requests your app has received over the last 24 hours, broken down by HTTP status code.
- View the activation status of Firebase services like Firebase Authentication and Cloud Firestore.

If you close the App overview panel, you can re-open it at any time by
clicking **Publish**.

Learn more about managing and monitoring App Hosting rollouts at
[Manage rollouts and releases](https://firebase.google.com/docs/app-hosting/rollouts).

## Roll back your deployment

If you've deployed successive versions of your app to App Hosting, you can
roll it back to one of the earlier versions. You can also remove it.

- To roll back a published site:

  1. Open [App Hosting in the
     Firebase console](http:https://console.firebase.google.com/project/_/apphosting).

  2. Locate your app's backend, click **View** , and then click **Rollouts**.

  3. Next to the deployment you want to roll back to, click **More**
     , then choose **Roll
     back to this build**, and confirm.

  Learn more at [Manage rollouts and releases](https://firebase.google.com/docs/app-hosting/rollouts).
- To remove your App Hosting domain from the web:

  1. From the
     [Firebase console](https://firebase.google.com/docs/studio/https://console.firebase.google.com/project/_/apphosting),
     open **App Hosting** , and click **View** in the
     Firebase Studio app section.

  2. In the **Backend information** section, click **Manage** . The
     **Domains** page loads.

  3. Next to your domain, click **More** , then choose **Disable domain**,
     and confirm.

  This removes your domain from the web. To fully remove your
  App Hosting backend, follow the instructions in [Delete a
  backend](https://firebase.google.com/docs/app-hosting/configure#delete-backend).

## Use Genkit Monitoring for your deployed features

You can monitor your Genkit feature steps, inputs, and outputs by enabling
telemetry to your AI flow code. Genkit's telemetry feature lets you monitor
the
performance and usage of your AI flows. This data can help you identify areas
for improvement, troubleshoot issues, optimize your prompts and flows for better
performance and cost efficiency, and track the usage of your flows over time.

To set up monitoring in Genkit, you add telemetry to the Genkit AI flows
and then view the results in the Firebase console.

> [!IMPORTANT]
> **Important:** Genkit Monitoring relies on telemetry data written to Google Cloud Logging, Metrics, and Trace, which are paid services. View the [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing) page for pricing details and to learn about free-of-charge tier limits.

### Step 1: Add telemetry to your Genkit flow code in Firebase Studio

To set up monitoring in your code:

1. If you aren't already in Code view, click
   ![Code switch
   icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)
   **Switch to Code** to open it.

2. Check `package.json` to verify the version of Genkit that's installed.

3. Open the terminal (`Ctrl-Shift-C`, or `Cmd-Shift-C` in MacOS).

4. Click inside the terminal and install the Firebase plugin, using the
   version that matches your `package.json` file. For example, if the
   Genkit packages in your
   `package.json` are at 1.0.4, you should run the following command to
   install the plugin:

       npm i --save @genkit-ai/firebase@1.0.4

5. From **Explorer** , expand `src > ai > flows`. One or more TypeScript files
   that contain your Genkit flows appear in the `flows` folder.

6. Click one of the flows to open it.

   > [!TIP]
   > **Tip:** Note the `prompt` section of the file: You can edit this manually to refine Gemini's responses.

7. At the bottom of the imports section of the file, add the following to
   import and enable `FirebaseTelemetry`:

       import { enableFirebaseTelemetry } from '@genkit-ai/firebase';

       enableFirebaseTelemetry();

   > [!TIP]
   > **Tip:** To learn more about advanced telemetry options in Genkit, see [Advanced
   > configuration](https://firebase.google.com/docs/genkit/observability/advanced-configuration#default-configuration).

### Step 2: Set up permissions

Firebase Studio enabled the [required
APIs](https://firebase.google.com/docs/genkit/observability/getting-started#enable-apis) for you when it
set up your Firebase project, but you also need to provide permissions to the
App Hosting service account.

To set up permissions:

1. Open the
   [Google Cloud IAM console](https://firebase.google.com/docs/studio/https://console.cloud.google.com/iam-admin/iam)
   select your project, then grant the following roles to the **App Hosting
   service account**:

   - **Monitoring Metric Writer** (`roles/monitoring.metricWriter`)
   - **Cloud Trace Agent** (`roles/cloudtrace.agent`)
   - **Logs Writer** (`roles/logging.logWriter`)
2. [Re-publish your app](https://firebase.google.com/docs/studio/deploy-app#app-hosting) to App Hosting.

3. When publishing is complete, load your app and start using it. After five
   minutes, your app should start logging telemetry data.

### Step 3: Monitor your generative AI features on the Firebase console

When telemetry is configured, Genkit records the number of requests,
success, and latency for all of your flows, and, for each specific flow,
Genkit collects stability metrics, shows detailed graphs, and logs
captured traces.

To monitor your AI features implemented with Genkit:

1. After five minutes, open Genkit in the
   [Firebase console](https://firebase.google.com/docs/studio/https://console.firebase.google.com/project/_/genkit)
   and review Genkit's prompts and responses.

   Genkit compiles the following **Stability metrics**:
   - **Total requests:** The total number of requests received by your flow.
   - **Success rate:** The percentage of requests that were successfully processed.
   - **95th percentile latency:** The 95th percentile latency of your flow, which is the time it takes for 95% of requests to be processed.
   - **Token usage:**

     - Input tokens: The number of tokens sent to the model in the prompt.
     - Output tokens: The number of tokens generated by the model in the response.
   - **Image usage:**

     - **Input images:** The number of images sent to the model in the prompt.
     - **Output images:** The number of images generated by the model in the response.

   If you expand stability metrics, detailed graphs are available:
   - Request volume over time.
   - Success rate over time.
   - Input and output tokens over time.
   - Latency (95th and 50th percentile) over time.

Learn more about Genkit at [Genkit](https://firebase.google.com/docs/genkit).

> [!TIP]
> **Tip:** For a guided tour of the full application lifecycle with the App Prototyping agent, from inception through monitoring your published web app, check out [Develop, publish, and monitor a full-stack web
> app with Firebase Studio](https://firebase.google.com/docs/studio/solution-build-with-ai).

## Next steps

- [Develop, publish, and monitor a full-stack web app with
  Firebase Studio](https://firebase.google.com/docs/studio/solution-build-with-ai).
- [Develop applications with any framework with a template or
  solution](https://firebase.google.com/docs/studio/get-started-template).