# Source: https://firebase.google.com/docs/studio/solution-build-with-ai.md.txt

# Develop, publish, and monitor a full-stack web app with the App Prototyping agent

<br />

> [!WARNING]
> **Preview:** Firebase Studio is in Preview, which means that the product is not subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

This guide shows you how to use
[the App Prototyping agent](https://firebase.google.com/docs/studio/get-started-ai) to
rapidly develop and publish a full-stack app with the help of
Gemini in Firebase. You'll use a natural-language prompt to generate a
Next.js app that identifies food items from a picture or
in-browser camera provided by a logged-in user and generates a recipe that
contains the identified ingredients. Users can then
choose to store the recipe in a searchable database.

You'll then refine and improve the app, before ultimately publishing to
Firebase App Hosting.
**Important:** Data persistence with Cloud Firestore and
Firebase Authentication is rolling out incrementally and may not be universally
available.

If data persistence is not available in your workspace yet,
Gemini may use local browser storage and mock authentication data
if you request a database and/or authentication in your
blueprint. You can still use additional prompting or Code
view to implement data persistence.

Other technologies you'll use as you proceed through this guide include:

- a [Firebase Studio workspace](https://firebase.google.com/docs/studio/get-started-workspace)
- a [Firebase project](https://firebase.google.com/docs/projects/learn-more)
- [Firebase App Hosting](https://firebase.google.com/docs/app-hosting)
- [Cloud Firestore](https://firebase.google.com/docs/firestore)
- [Firebase Authentication](https://firebase.google.com/docs/auth)
- [Firebase App Check](https://firebase.google.com/docs/app-check)

> [!IMPORTANT]
> **Important:** The App Prototyping agent supports creating apps with the Next.js framework. To use AI assistance with other frameworks in Firebase Studio, see [Try Gemini in Firebase](https://firebase.google.com/docs/studio/try-gemini) with Firebase Studio.

## Step 1: Generate your app

1. Log into your Google Account and open
   [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

2. In the **Prototype an app with AI** field, enter the following prompt, which
   will create an image-based recipe app that uses the browser camera
   and generative AI.

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

   - Because your app uses AI, you're prompted to add or generate a [Gemini API key](https://ai.google.dev/gemini-api/docs/api-key). If you click Auto-generate, the App Prototyping agent provisions a Firebase project and a Gemini API key for you.

   > [!IMPORTANT]
   > **Important:** If you choose **Auto-generate** , the App Prototyping agent creates a [Firebase project](https://firebase.google.com/docs/projects/learn-more) on your behalf with a prefix that matches the name of your Firebase Studio workspace and creates a new Gemini API key in the project. It also stores the key within your Firebase Studio workspace in an `.env` file. To access your new project at any time, click the project name at the top of the page. To access your Gemini API key to copy or delete in the future, use the [Google Cloud console](https://firebase.google.com/docs/studio/https://console.cloud.google.com/apis/credentials).

## Step 2: Test, refine, debug, and iterate

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

## (Optional) Step 3: Publish your app with App Hosting

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

## (Recommended) Step 4: Test your published app

When publishing is complete and your app is deployed to Firebase,
Cloud Firestore and Firebase Authentication are ready to test in production.

#### Generate indexes for your Cloud Firestore database

When you deploy your app to Cloud Firestore, indexes are not generated
automatically. This means that, after you publish, you may need to generate
indexes for your queries.

You may see this surfaced in error messages or in your browser's
[Developer console](https://firebase.google.com/docs/studio/debug).

To generate indexes after publishing:

1. **From a published app:** In the **App overview** pane
   (click **Publish** if it's not visible), locate and click the
   **Visit your app** link.

   **From the Firebase Studio preview:** Open your browser's
   Developer console and locate the error 200 message that
   Cloud Firestore generates.
2. Test all flows within your app. An error may appear that says something
   like, "Error loading recipes. The query requires an index. You can
   create it here:" with a link to the Firebase console.

3. Follow the link to navigate to the Firebase console and a recommended
   index appears.

4. Click **Save** to accept the recommended index.

5. Return to your app and reload the page.

6. Continue testing all flows in your app to add indexes where necessary.

> [!TIP]
> **Tip:** You can ask Gemini to generate your indexes for you; but be sure to double-check its output.

Learn more at [Manage indexes in
Cloud Firestore](https://firebase.google.com/docs/firestore/query-data/indexing).

#### View Cloud Firestore and Firebase Authentication data in the Firebase console

You can view live data from your app in the Firebase console after
publishing.

- To view your live Cloud Firestore database, open the
  [Firebase console](https://firebase.google.com/docs/studio/https://console.firebase.google.com//_/firestore)
  and choose **Build** \> **Firestore Database** from the navigation menu.

  From here, you can inspect stored data, view and test your security
  rules, and create indexes. Learn more at [Cloud Firestore](https://firebase.google.com/docs/firestore).
- To view your live Firebase Authentication data, open the
  [Firebase console](https://firebase.google.com/docs/studio/https://console.firebase.google.com//_/auth) and choose
  **Build** \> **Authentication** from the navigation menu.

  From here, you can inspect your authentication configuration and app users.
  Learn more at [Firebase Authentication](https://firebase.google.com/docs/auth).

#### Test Cloud Firestore rules in production

After publishing your app, you should test your Cloud Firestore security rules
again, against your production environment. This helps to ensure that your data
is accessible to authorized users and protected from unauthorized access.

You can test your rules using all of the following methods:

- **Application Testing**: Interact with your deployed application,
  performing operations that trigger various data access patterns (reads,
  writes, deletes) for different user roles or states. This real-world
  testing helps confirm that your rules are correctly enforced in
  practice.

- **Rules Playground** : For targeted checks, use the [Rules
  Playground](https://firebase.google.com/docs/rules/simulator) in the Firebase console. This tool
  lets you simulate requests (reads, writes, deletes) against your
  Cloud Firestore database using your production rules. You can specify the
  user authentication state, the path to the data, and the type of
  operation to see if your rules permit or deny access as intended.

  > [!NOTE]
  > **Note:** **When you deploy security rules during the [publishing
  > process](https://firebase.google.com/docs/studio/deploy-app#app-hosting) or with the
  > [Firebase CLI](https://firebase.google.com/docs/cli#deployment),
  > the rules defined in your project directory overwrite any existing rules
  > in the Firebase console.** So, if you choose to define or edit your security rules using the Firebase console, make sure that you also update the rules defined in your project directory.

- **Unit Testing** : For more comprehensive testing, you can write
  [unit tests for your security
  rules](https://firebase.google.com/docs/firestore/security/test-rules-emulator).
  The Firebase Studio preview backend powered by the
  Firebase Local Emulator Suite lets you run these tests locally,
  simulating the behavior of your production rules. This is a robust way
  to verify complex rule logic and confirm coverage for various
  scenarios. After deployment, you should double-check that your unit
  tests using the emulator work as expected and cover all scenarios.