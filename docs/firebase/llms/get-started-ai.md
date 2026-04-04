# Source: https://firebase.google.com/docs/studio/get-started-ai.md.txt

<br />

Firebase Studioincludes a web-based interface that lets you rapidly prototype and generate AI-forward web apps using multimodal prompts, including natural language, images, and drawing tools. The agent supports Next.js apps, with other platforms and frameworks planned in the future.

TheApp Prototyping agentis a streamlined no-code development flow that uses generative AI to develop, test, iterate, and publish a full-stack, agentic web app. You describe your app idea in natural language with an optional image, and the agent generates an app blueprint, code, and a web preview. To assist in the development and publishing of your full-stack app,Firebase Studiocan automatically provision the following services for you:

- **If your app uses AI:** Firebase Studioadds theGeminiDeveloper API to your app, using the power of[Genkit](https://firebase.google.com/docs/genkit)flows to work withGemini. You can use your ownGemini APIkey or letFirebase Studioprovision a Firebase project and Gemini API key for you.
- **If you want to publish your app to the web:** Firebase Studiocreates a project and provides a quick way to publish your app with[Firebase App Hosting](https://firebase.google.com/docs/app-hosting).

| **Important:** When theApp Prototyping agentsets up theGemini APIkey and other Firebase services, it creates a new Firebase project to associate with the workspace. At this time, this is the only project that can be associated when publishing from theApp Prototyping agentview. Note that you can publish to other Firebase projects by[checking your code into GitHub](https://firebase.google.com/docs/studio/github)and[creating anApp Hostingbackend](https://firebase.google.com/docs/app-hosting/get-started). You can also use[Code view](https://firebase.google.com/docs/studio/google-integrations)to integrate Firebase services.

You can refine the app using natural language, images, and drawing tools, edit code directly, roll back changes, publish the app, and monitor its performance---all fromFirebase Studio.
| **Note:** TheApp Prototyping agentcan help you build web apps with Next.js. Support for other platforms and frameworks is coming soon!

## Get started

To get started with theApp Prototyping agent, follow these steps:

1. Log into your Google Account and open[Firebase Studio](https://studio.firebase.google.com/).

2. In the**Prototype an app with AI**field, describe your app idea in natural language.

   For example, you could enter a prompt like the following to create a recipe generation app:  

       Use secure coding practices to create an error-free web app that lets
       users upload a photo or take a picture with their browser
       camera. The app identifies the food in the picture and generates a
       recipe and accompanying image that includes that food.

       If no food product is identified, generate a random dessert recipe.

   | **Tip:** For best results, be as specific as possible in your prompt. Include the features you want, user workflows, and data requirements. Optionally, click**Improve prompt** to askGeminito refine your initial prompt. Also understand that the most effective development processes with AI are iterative and you can continue to refine and add features collaboratively withGemini. Learn more about crafting[effective prompts](https://firebase.google.com/docs/studio/prompting).
3. Optionally, upload an image to accompany your prompt. For example, you can upload an image that contains the color scheme you want your app to use and tellFirebase Studioto use it. Images must be less than 3 MiB.

4. Click**Prototype with AI**.

   TheApp Prototyping agentgenerates an app blueprint based on your prompt, returning a proposed app name, required features, and style guidelines.
5. Review the blueprint. If necessary, make a few changes. For example, you could change the proposed app name or color scheme using one of these options:

   - Clickedit**Customize** and edit the blueprint directly. Make your changes and click**Save**.

   - In the**Describe...**field in the chat pane, add clarifying questions and context. You can also upload additional images.

6. Click**Prototype this app**.

   | **Important:** Geminican generate output that seems plausible but is factually incorrect. It may respond with inaccurate information that doesn't represent Google's views. Validate all output from Gemini before you use it and do not use untested generated code in production. Do not enter personally-identifiable information (PII) or user data into the chat.
7. TheApp Prototyping agentbegins coding your app.

   - If your app uses AI, you're prompted to add or generate a[Gemini APIkey](https://ai.google.dev/gemini-api/docs/api-key). If you click Auto-generate, theApp Prototyping agentprovisions a Firebase project and aGemini APIkey for you.

   | **Important:** If you choose**Auto-generate** , theApp Prototyping agentcreates a[Firebase project](https://firebase.google.com/docs/projects/learn-more)on your behalf with a prefix that matches the name of yourFirebase Studioworkspace and creates a newGemini APIkey in the project. It also stores the key within yourFirebase Studioworkspace in an`.env`file. To access your new project at any time, click the project name at the top of the page. To access yourGemini APIkey to copy or delete in the future, use the[Google Cloudconsole](https://console.cloud.google.com/apis/credentials).

## Test, refine, debug, and iterate

After the initial app is generated, you can test, refine, debug, and iterate.

- **Review and interact with your app:** After code generation completes, a preview of your app appears. You can interact with the preview directly to test it. Learn more at[Preview your app](https://firebase.google.com/docs/studio/preview-apps).

- **AddCloud FirestoreandFirebase Authentication:** During the iteration phase, you can ask theApp Prototyping agentto add user authentication and a database usingCloud FirestoreandFirebase Authentication. For example, give users the ability to save and download recipes with a prompt like the following:

      Add user authentication to the app. Authenticated users can:

        - Download the recipe and its generated image as a PDF (Print).

        - Save the recipe as public or private and make accessible to a search
          feature. For now, just save the text, not the image, to the database.

      Important: Only authenticated users can download the PDF.

  | **Tip:** TheApp Prototyping agentcan addCloud FirestoreandFirebase Authenticationto your app during the iteration phase, not in the initial app blueprint.
- **Fix any errors as they occur:** In most cases, theApp Prototyping agentprompts you to fix any errors that arise. Click**Fix Error**to allow it to attempt a fix.

  If you receive errors that you're not prompted to fix automatically, copy the error and any relevant context (for example, "Can you fix this error in my Firebase initialization code?") into the chat window and send it toGemini.
  | **Tip:** Geminiexplains its reasoning, but you can also ask it to explain its plan before it executes it.
- **Test and iterate using natural language:** Test your app thoroughly and work with theApp Prototyping agentto iterate on the code and blueprint until you're happy with it.

  While inPrototyperview, you can also use the following features:
  - Click![Annotate icon](https://firebase.google.com/static/docs/studio/images/icons/annotate-icon.png)**Annotate** to draw directly on the Preview window. Use the available shape, image, and text tools, along with an optional text prompt, to visually describe what you want theApp Prototyping agentto change.

  - Click![Select icon](https://firebase.google.com/static/docs/studio/images/icons/select-icon.png)**Select** to select a specific element and enter instructions for theApp Prototyping agent. This lets you quickly target a specific icon, button, piece of text, or other element. When you click an image, you also have the option of searching for and selecting a stock image from[Unsplash](https://unsplash.com).

  Optionally, you can click![Link icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-link.svg)**Share preview link** to share your app publicly and temporarily usingFirebase Studio[public previews](https://firebase.google.com/docs/studio/preview-apps#share).
- **Create a Firebase project:** TheApp Prototyping agentprovisions a[Firebase project](https://firebase.google.com/docs/projects/learn-more)on your behalf when you:

  - Auto-generate a Gemini API key
  - Ask to connect your app to a Firebase project
  - Ask for help connecting your app to Firebase services, such asCloud FirestoreorFirebase Authentication
  - Click the**Publish** button and set upFirebase App Hosting

  To change the Firebase project connected to your workspace, prompt theApp Prototyping agentwith the project ID you want to use instead. For example, "Switch to Firebase project with ID`<your-project-id>`."
- **Test the app and verifyCloud Firestoredatabase rules:**In the app preview pane, upload an image that shows different foods to test your app's ability to identify the ingredients and generate and save recipes.

  Sign in as different users and generate recipes: make sure that authenticated users can see their private recipes and recipes and that all users see public recipes.

  When you ask theApp Prototyping agentto addCloud Firestore, it writes and deploysCloud Firestoredatabase rules for you. Review the rules in the[Firebaseconsole](https://console.firebase.google.com/project/_/firestore/databases/-default-/rules).
- **Debug and iterate directly in the code:** Click![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)**Switch to Code** to openCodeview, where you can see all of your app's files and modify your code directly. You can switch back toPrototypermode at any time.

  While inCodeview, you can also use the following helpful features:
  - Firebase Studio's[built-in debugging and reporting features](https://firebase.google.com/docs/studio/debug)to inspect, debug, and audit your app.

  - [AI assistance usingGemini](https://firebase.google.com/docs/studio/try-gemini)either inline within your code or usingGeminiinteractive chat(both are available by default). Interactive chatcan diagnose issues, provide solutions, and run tools to help fix your app faster. To access chat, clickspark**Gemini**at the bottom of the workspace.

    | **Note:** Apps created with theApp Prototyping agentdefault to thePrototyperchat inCodeview. To useGeminiinteractive chatinstead, under**Gemini** , click**+** , then select**New Chat** . To return toPrototyperchat, clickhistory**Recent chats** , and then choose**Prototyper chat**.
  - [Access theFirebase Local Emulator Suiteto view database and authentication data](https://firebase.google.com/docs/emulator-suite). To open the emulator in your workspace:

    1. Click![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)**Switch to Code** and open the**Firebase Studio** extension (`Ctrl+',Ctrl+'`, or`Cmd+',Cmd+'`on MacOS).

    2. Scroll to**Backend ports**and expand it.

    3. In the**Actions** column that corresponds to**Port 4000** , click**Open in new window**.

- **Test and measure your generative AI feature performance:**You can use the Genkit Developer UI to run your Genkit AI flows, test, debug, interact with different models, refine your prompts, and more.

  To load your Genkit flows in the Genkit Developer UI and start testing:
  1. From the terminal in yourFirebase Studioworkspace, run the following command to source yourGemini APIkey and start the Genkit server:

          npm run genkit:watch

  2. Click the Genkit Developer UI link. The Genkit Developer UI opens in a new window with your flows, prompts, embedders, and a selection of different available models.

  Learn more about the Genkit Developer UI at[Genkit Developer Tools](https://genkit.dev/docs/devtools/).

## Publish your app withFirebase App Hosting

After you've tested your app and are satisfied with it in your workspace, you can publish it to the web with[Firebase App Hosting](https://firebase.google.com/docs/app-hosting).
| **Important:** Firebase App Hostingrequires aCloud Billingaccount. When you link a billing account to a Firebase project, then your project is automatically upgraded to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)and yourGemini APIand other Firebase and Google Cloud service usage is upgraded to the paid tier. You will be charged for usage of paid services that exceed the no-cost quota. Learn more at[UnderstandApp Hostingcosts](https://firebase.google.com/docs/app-hosting/costs),[Firebase pricing](https://firebase.google.com/pricing), and[GeminiDeveloper API pricing](https://ai.google.dev/gemini-api/docs/pricing).

When you set upApp Hosting,Firebase Studiocreates a[Firebase project](https://firebase.google.com/docs/studio/firebase-projects)for you (if one was not already created by auto-generating aGemini APIkey or other backend services) and guides you through linking aCloud Billingaccount.

To publish your app:

1. Click**Publish** to set up your[Firebase project](https://firebase.google.com/docs/studio/firebase-projects)and publish your app. The**Publish your app**pane appears.

   | **Important:** If you did not[auto-generate aGemini APIkey](https://firebase.google.com/docs/studio/get-started-ai#get-started)or prompt theApp Prototyping agentto create a Firebase project,Firebase Studioprovisions a[Firebase project](https://firebase.google.com/docs/studio/firebase-projects)on your behalf when you click**Publish**. You can access the Firebase project by clicking the project name at the top of the page.
2. In the**Firebase project** step, theApp Prototyping agentdisplays the Firebase project associated with the workspace. If a Firebase project doesn't already exist, theApp Prototyping agentcreates a new project for you. Click**Next**to proceed.

3. In the**LinkCloud Billingaccount**step, choose one of the following:

   - Select theCloud Billingaccount that you want to link to your Firebase project.

   - If you don't have aCloud Billingaccount or want to create a new one, click**Create aCloud Billingaccount** . This opens theGoogle Cloudconsole, where you can[create a new self-serveCloud Billingaccount](https://cloud.google.com/billing/docs/how-to/create-billing-account). After you create the account, return toFirebase Studioand select the account from the**LinkCloud Billing**list.

4. Click**Next** .Firebase Studiolinks the billing account to the project associated with your workspace, created either when you auto-generated aGemini APIkey or when you clicked**Publish**.

   | **Important:** Firebase App Hostingrequires aCloud Billingaccount. When you link a billing account to a Firebase project, then your project is automatically upgraded to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)and yourGemini APIand other Firebase and Google Cloud service usage is upgraded to the paid tier. You will be charged for usage of paid services that exceed the no-cost quota. Learn more at[UnderstandApp Hostingcosts](https://firebase.google.com/docs/app-hosting/costs),[Firebase pricing](https://firebase.google.com/pricing), and[GeminiDeveloper API pricing](https://ai.google.dev/gemini-api/docs/pricing).
5. Click**Set up services** . TheApp Prototyping agentbegins provisioning Firebase services.

6. Click**Publish now** .Firebase Studiosets up Firebase services and then launches theApp Hostingrollout. This can take up to several minutes to complete. To learn more about what's happening behind the scenes, see[TheApp Hostingbuild process](https://firebase.google.com/docs/app-hosting/build).

   | **Tip:** If you don't want to publish now, you can click**Publish later**.
7. When the publish step completes, the**App overview** appears with a URL and app insights powered byApp Hostingobservability. To use a custom domain (like example.com or app.example.com) instead of the Firebase-generated domain, you can[add a custom domain](https://firebase.google.com/docs/app-hosting/custom-domain)in theFirebaseconsole.

| **Tip:** If you receive any errors during publishing, see[I received a "Failed to publish app" error after publishing](https://firebase.google.com/docs/studio/troubleshooting#failed-to-publish)for instructions on how to find and fix publishing errors.

For more information aboutApp Hosting, see[UnderstandApp Hostingand how it works](https://firebase.google.com/docs/app-hosting/about-app-hosting).

## Secure your app withFirebase App Checkand reCAPTCHA Enterprise

If you've integrated Firebase or Google Cloud services into your app,Firebase App Checkhelps protect your app backends from abuse by preventing unauthorized clients from accessing your Firebase resources. It works with both Google services (including Firebase and Google Cloud services) and your own custom backends to keep your resources safe.

We recommend addingApp Checkto any app you post publicly to protect your backend resources from abuse.

This section guides you through setting upApp CheckwithinFirebase Studiousing[reCAPTCHA Enterprise](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider)for a web app created by theApp Prototyping agent, but you can set upApp Checkwithin any app that implements Firebase services and can implement custom providers. Learn more at[Firebase App Check](https://firebase.google.com/docs/app-check).

ReCAPTCHA Enterprise provides[up to 10,000 assessments at no-cost](https://cloud.google.com/recaptcha/docs/compare-tiers).

### Step 1: Set up reCAPTCHA Enterprise for your app

1. Open the[reCAPTCHA Enterprise](https://console.cloud.google.com/security/recaptcha?project=_)section of theGoogle Cloudconsole.

2. Select the name of your Firebase project from theGoogle Cloudconsole project picker.

3. If you're prompted to enable the reCAPTCHA Enterprise API, do so.

4. Click**Get started** , and add a**Display name**for your reCAPTCHA site key.

5. Accept the default**Web** **Application type**key.

6. Click**Add a domain** and add a domain. You'll want to add yourApp Hostingdomain (for example,`studio--`<var translate="no">PROJECT_ID</var>`.`<var translate="no">REGION</var>`.hosted.app`) and any custom domains you use with or plan to use with your app.

7. Click**Next step**.

8. Leave**Will you use challenges?**unselected.

9. Click**Create key**.

10. Copy and save your**Key ID** and proceed to[**ConfigureApp Check**](https://firebase.google.com/docs/studio/get-started-ai#configure-app-check).

### Step 2: ConfigureApp Check

1. Open the[Firebaseconsole](https://console.firebase.google.com/project/_/appcheck)and click**Build** \>**App Check**from the navigation menu.

2. Click**Get started** , then click**Register**next to your app.

3. Click to expand**ReCAPTCHA**and paste the Key ID you generated for reCAPTCHA Enterprise.

4. Click**Save**.

### Step 3: AddApp Checkto your code

1. Return toFirebase Studioand inCodeview, add the site key you generated to your`.env`file:

       NEXT_PUBLIC_RECAPTCHA_SITE_KEY=<var translate="no">RECAPTCHA_SITE_KEY</var>

2. If you don't already have your Firebase configuration saved to`.env`, obtain it:

   - From the[Firebaseconsole](http://console.firebase.google.com/project/_/settings), open**Project settings**and locate it within your the section that corresponds with your app.

   - From the Terminal inCodeview:

     1. Log into Firebase:`firebase auth login`
     2. Select your project:`firebase use `<var translate="no">FIREBASE_PROJECT_ID</var>
     3. Obtain the Firebase config:`firebase apps:sdkconfig`
3. Add the configuration to your`.env`file so that it looks like the following:

       NEXT_PUBLIC_FIREBASE_API_KEY=<var translate="no">FIREBASE_API_KEY</var>
       NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=<var translate="no">FIREBASE_AUTH_DOMAIN</var>
       NEXT_PUBLIC_FIREBASE_PROJECT_ID=<var translate="no">FIREBASE_PROJECT_ID</var>
       NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=<var translate="no">FIREBASE_STORAGE_BUCKET</var>
       NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=<var translate="no">FIREBASE_MESSAGING_SENDER_ID</var>
       NEXT_PUBLIC_FIREBASE_APP_ID=<var translate="no">FIREBASE_APP_ID</var>
       NEXT_PUBLIC_RECAPTCHA_SITE_KEY=<var translate="no">RECAPTCHA_SITE_KEY</var>

4. AddApp Checkto your app code. You can askGeminito addApp Checkwith reCAPTCHA Enterprise to your app (be sure to specify "reCAPTCHA Enterprise" and be sure to double-check it!), or follow the steps in[InitializeApp Check](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider#initialize).

5. Re-publish your site toApp Hosting. Try testing your database and authentication features to generate some data.

6. Verify thatApp Checkis receiving requests in theFirebaseconsole by opening**Build** \>**App Check**.

7. Click to inspectCloud Firestore. After you verify that requests arrive, click**Enforce** to enforceApp Check.

8. Repeat verification and enforcement forFirebase Authentication.

If, after you have registered your app forApp Check, you want to run your app in an environment thatApp Checkwould normally not classify as valid, such as locally during development, or from a continuous integration (CI) environment, you can create a debug build of your app that uses theApp Checkdebug provider instead of a real attestation provider. Learn more at[UseApp Checkwith the debug provider in web apps](https://firebase.google.com/docs/app-check/web/debug-provider).

## Monitor your app

The**App overview** panel inFirebase Studioprovides key metrics and information about your app, letting you monitor your web app's performance usingApp Hosting's built-in observability tools. After your site rolls out, you can access the overview by clicking**Publish**. From this panel, you can:

- Click**Publish**to release a new version of your app.
- Share the link to your app or open your app directly in**Visit your app**.
- Review a summary of your app's performance over the last 7 days, including the total number of requests and the status of your latest rollout. Click**View details** to access even more information in the[Firebaseconsole](https://console.firebase.google.com/project/_/apphosting/).
- View a graph of the number of the number of requests your app has received over the last 24 hours, broken down by HTTP status code.
- View the activation status of Firebase services likeFirebase AuthenticationandCloud Firestore.

If you close the App overview panel, you can re-open it at any time by clicking**Publish**.

Learn more about managing and monitoringApp Hostingrollouts at[Manage rollouts and releases](https://firebase.google.com/docs/app-hosting/rollouts).

## Roll back your deployment

If you've deployed successive versions of your app toApp Hosting, you can roll it back to one of the earlier versions. You can also remove it.

- To roll back a published site:

  1. Open[App Hostingin theFirebaseconsole](http://console.firebase.google.com/project/_/apphosting).

  2. Locate your app's backend, click**View** , and then click**Rollouts**.

  3. Next to the deployment you want to roll back to, click**More** more_vert, then choose**Roll back to this build**, and confirm.

  Learn more at[Manage rollouts and releases](https://firebase.google.com/docs/app-hosting/rollouts).
- To remove yourApp Hostingdomain from the web:

  1. From the[Firebaseconsole](https://console.firebase.google.com/project/_/apphosting), open**App Hosting** , and click**View** in theFirebase Studioapp section.

  2. In the**Backend information** section, click**Manage** . The**Domains**page loads.

  3. Next to your domain, click**More** more_vert, then choose**Disable domain**, and confirm.

  This removes your domain from the web. To fully remove yourApp Hostingbackend, follow the instructions in[Delete a backend](https://firebase.google.com/docs/app-hosting/configure#delete-backend).

## UseGenkitMonitoring for your deployed features

You can monitor yourGenkitfeature steps, inputs, and outputs by enabling telemetry to your AI flow code.Genkit's telemetry feature lets you monitor the performance and usage of your AI flows. This data can help you identify areas for improvement, troubleshoot issues, optimize your prompts and flows for better performance and cost efficiency, and track the usage of your flows over time.

To set up monitoring inGenkit, you add telemetry to theGenkitAI flows and then view the results in theFirebaseconsole.
| **Important:** Genkit Monitoring relies on telemetry data written to Google Cloud Logging, Metrics, and Trace, which are paid services. View the[Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing)page for pricing details and to learn about free-of-charge tier limits.

### Step 1: Add telemetry to yourGenkitflow code inFirebase Studio

To set up monitoring in your code:

1. If you aren't already inCodeview, click![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)**Switch to Code**to open it.

2. Check`package.json`to verify the version ofGenkitthat's installed.

3. Open the terminal (`Ctrl-Shift-C`, or`Cmd-Shift-C`in MacOS).

4. Click inside the terminal and install the Firebase plugin, using the version that matches your`package.json`file. For example, if theGenkitpackages in your`package.json`are at 1.0.4, you should run the following command to install the plugin:

       npm i --save @genkit-ai/firebase@1.0.4

5. From**Explorer** , expand`src > ai > flows`. One or more TypeScript files that contain yourGenkitflows appear in the`flows`folder.

6. Click one of the flows to open it.

   | **Tip:** Note the`prompt`section of the file: You can edit this manually to refineGemini's responses.
7. At the bottom of the imports section of the file, add the following to import and enable`FirebaseTelemetry`:

       import { enableFirebaseTelemetry } from '@genkit-ai/firebase';

       enableFirebaseTelemetry();

   | **Tip:** To learn more about advanced telemetry options inGenkit, see[Advanced configuration](https://firebase.google.com/docs/genkit/observability/advanced-configuration#default-configuration).

### Step 2: Set up permissions

Firebase Studioenabled the[required APIs](https://firebase.google.com/docs/genkit/observability/getting-started#enable-apis)for you when it set up your Firebase project, but you also need to provide permissions to theApp Hostingservice account.

To set up permissions:

1. Open the[Google CloudIAM console](https://console.cloud.google.com/iam-admin/iam)select your project, then grant the following roles to the**App Hosting service account**:

   - **Monitoring Metric Writer** (`roles/monitoring.metricWriter`)
   - **Cloud Trace Agent** (`roles/cloudtrace.agent`)
   - **Logs Writer** (`roles/logging.logWriter`)
2. [Re-publish your app](https://firebase.google.com/docs/studio/deploy-app#app-hosting)toApp Hosting.

3. When publishing is complete, load your app and start using it. After five minutes, your app should start logging telemetry data.

### Step 3: Monitor your generative AI features on theFirebaseconsole

When telemetry is configured,Genkitrecords the number of requests, success, and latency for all of your flows, and, for each specific flow,Genkitcollects stability metrics, shows detailed graphs, and logs captured traces.

To monitor your AI features implemented withGenkit:

1. After five minutes, openGenkitin the[Firebaseconsole](https://console.firebase.google.com/project/_/genkit)and reviewGenkit's prompts and responses.

   Genkitcompiles the following**Stability metrics**:
   - **Total requests:**The total number of requests received by your flow.
   - **Success rate:**The percentage of requests that were successfully processed.
   - **95th percentile latency:**The 95th percentile latency of your flow, which is the time it takes for 95% of requests to be processed.
   - **Token usage:**

     - Input tokens: The number of tokens sent to the model in the prompt.
     - Output tokens: The number of tokens generated by the model in the response.
   - **Image usage:**

     - **Input images:**The number of images sent to the model in the prompt.
     - **Output images:**The number of images generated by the model in the response.

   If you expand stability metrics, detailed graphs are available:
   - Request volume over time.
   - Success rate over time.
   - Input and output tokens over time.
   - Latency (95th and 50th percentile) over time.

Learn more aboutGenkitat[Genkit](https://firebase.google.com/docs/genkit).
| **Tip:** For a guided tour of the full application lifecycle with theApp Prototyping agent, from inception through monitoring your published web app, check out[Develop, publish, and monitor a full-stack web app withFirebase Studio](https://firebase.google.com/docs/studio/solution-build-with-ai).

## Next steps

- [Develop, publish, and monitor a full-stack web app withFirebase Studio](https://firebase.google.com/docs/studio/solution-build-with-ai).
- [Develop applications with any framework with a template or solution](https://firebase.google.com/docs/studio/get-started-template).