# Source: https://firebase.google.com/docs/studio/solution-build-with-ai.md.txt

<br />

| **Preview:** Firebase Studiois in Preview, which means that the product is not subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

This guide shows you how to use[theApp Prototyping agent](https://firebase.google.com/docs/studio/get-started-ai)to rapidly develop and publish a full-stack app with the help of Gemini inFirebase. You'll use a natural-language prompt to generate a Next.js app that identifies food items from a picture or in-browser camera provided by a logged-in user and generates a recipe that contains the identified ingredients. Users can then choose to store the recipe in a searchable database.

You'll then refine and improve the app, before ultimately publishing toFirebase App Hosting.
| **Important:** Data persistence withCloud FirestoreandFirebase Authenticationis rolling out incrementally and may not be universally available.
|
| If data persistence is not available in your workspace yet,Geminimay use local browser storage and mock authentication data if you request a database and/or authentication in your blueprint. You can still use additional prompting orCodeview to implement data persistence.

Other technologies you'll use as you proceed through this guide include:

- a[Firebase Studioworkspace](https://firebase.google.com/docs/studio/get-started-workspace)
- a[Firebase project](https://firebase.google.com/docs/projects/learn-more)
- [Firebase App Hosting](https://firebase.google.com/docs/app-hosting)
- [Cloud Firestore](https://firebase.google.com/docs/firestore)
- [Firebase Authentication](https://firebase.google.com/docs/auth)
- [Firebase App Check](https://firebase.google.com/docs/app-check)

| **Important:** TheApp Prototyping agentsupports creating apps with the Next.js framework. To use AI assistance with other frameworks inFirebase Studio, see[Try Gemini inFirebase](https://firebase.google.com/docs/studio/try-gemini)withFirebase Studio.

## Step 1: Generate your app

1. Log into your Google Account and open[Firebase Studio](https://studio.firebase.google.com/).

2. In the**Prototype an app with AI**field, enter the following prompt, which will create an image-based recipe app that uses the browser camera and generative AI.

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

   - Because your app uses AI, you're prompted to add or generate a[Gemini APIkey](https://ai.google.dev/gemini-api/docs/api-key). If you click Auto-generate, theApp Prototyping agentprovisions a Firebase project and aGemini APIkey for you.

   | **Important:** If you choose**Auto-generate** , theApp Prototyping agentcreates a[Firebase project](https://firebase.google.com/docs/projects/learn-more)on your behalf with a prefix that matches the name of yourFirebase Studioworkspace and creates a newGemini APIkey in the project. It also stores the key within yourFirebase Studioworkspace in an`.env`file. To access your new project at any time, click the project name at the top of the page. To access yourGemini APIkey to copy or delete in the future, use the[Google Cloudconsole](https://console.cloud.google.com/apis/credentials).

## Step 2: Test, refine, debug, and iterate

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

## (Optional) Step 3: Publish your app withApp Hosting

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

## (Recommended) Step 4: Test your published app

When publishing is complete and your app is deployed to Firebase,Cloud FirestoreandFirebase Authenticationare ready to test in production.

#### Generate indexes for yourCloud Firestoredatabase

When you deploy your app toCloud Firestore, indexes are not generated automatically. This means that, after you publish, you may need to generate indexes for your queries.

You may see this surfaced in error messages or in your browser's[Developer console](https://firebase.google.com/docs/studio/debug).

To generate indexes after publishing:

1. **From a published app:** In the**App overview** pane (click**Publish** if it's not visible), locate and click the**Visit your app**link.

   **From theFirebase Studiopreview:** Open your browser's Developer console and locate the error 200 message thatCloud Firestoregenerates.
2. Test all flows within your app. An error may appear that says something like, "Error loading recipes. The query requires an index. You can create it here:" with a link to theFirebaseconsole.

3. Follow the link to navigate to theFirebaseconsole and a recommended index appears.

4. Click**Save**to accept the recommended index.

5. Return to your app and reload the page.

6. Continue testing all flows in your app to add indexes where necessary.

| **Tip:** You can askGeminito generate your indexes for you; but be sure to double-check its output.

Learn more at[Manage indexes inCloud Firestore](https://firebase.google.com/docs/firestore/query-data/indexing).

#### ViewCloud FirestoreandFirebase Authenticationdata in theFirebaseconsole

You can view live data from your app in theFirebaseconsole after publishing.

- To view your liveCloud Firestoredatabase, open the[Firebaseconsole](https://console.firebase.google.com//_/firestore)and choose**Build** \>**Firestore Database**from the navigation menu.

  From here, you can inspect stored data, view and test your security rules, and create indexes. Learn more at[Cloud Firestore](https://firebase.google.com/docs/firestore).
- To view your liveFirebase Authenticationdata, open the[Firebaseconsole](https://console.firebase.google.com//_/auth)and choose**Build** \>**Authentication**from the navigation menu.

  From here, you can inspect your authentication configuration and app users. Learn more at[Firebase Authentication](https://firebase.google.com/docs/auth).

#### Test Cloud Firestore rules in production

After publishing your app, you should test yourCloud Firestoresecurity rules again, against your production environment. This helps to ensure that your data is accessible to authorized users and protected from unauthorized access.

You can test your rules using all of the following methods:

- **Application Testing**: Interact with your deployed application, performing operations that trigger various data access patterns (reads, writes, deletes) for different user roles or states. This real-world testing helps confirm that your rules are correctly enforced in practice.

- **Rules Playground** : For targeted checks, use the[Rules Playground](https://firebase.google.com/docs/rules/simulator)in theFirebaseconsole. This tool lets you simulate requests (reads, writes, deletes) against yourCloud Firestoredatabase using your production rules. You can specify the user authentication state, the path to the data, and the type of operation to see if your rules permit or deny access as intended.

  | **Note:** **When you deploy security rules during the[publishing process](https://firebase.google.com/docs/studio/deploy-app#app-hosting)or with the[FirebaseCLI](https://firebase.google.com/docs/cli#deployment), the rules defined in your project directory overwrite any existing rules in theFirebaseconsole.** So, if you choose to define or edit your security rules using theFirebaseconsole, make sure that you also update the rules defined in your project directory.
- **Unit Testing** : For more comprehensive testing, you can write[unit tests for your security rules](https://firebase.google.com/docs/firestore/security/test-rules-emulator). TheFirebase Studiopreview backend powered by theFirebase Local Emulator Suitelets you run these tests locally, simulating the behavior of your production rules. This is a robust way to verify complex rule logic and confirm coverage for various scenarios. After deployment, you should double-check that your unit tests using the emulator work as expected and cover all scenarios.