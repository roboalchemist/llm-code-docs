# Source: https://firebase.google.com/docs/studio/deploy-app.md.txt

# Publish your app with Firebase Studio

Firebase Studio offers multiple publishing options, allowing you to
choose the method that best suits your project's needs. Here's an overview of
the available options:

- [**Firebase App Hosting**](https://firebase.google.com/docs/studio/deploy-app#app-hosting): Ideal for publishing
  dynamic Next.js and Angular applications, App Hosting offers
  built-in framework support, GitHub integration, and integration with
  other Firebase products like Firebase Authentication, Cloud Firestore, and
  Firebase AI Logic.

  If you developed a Next.js app with
  [the App Prototyping agent](https://firebase.google.com/docs/studio/get-started-ai), you can
  publish directly from
  Firebase Studio in just a few clicks.
- [**Firebase Hosting:**](https://firebase.google.com/docs/studio/deploy-app#firebase-hosting) Well-suited for hosting web
  apps and static web content (HTML, CSS, JavaScript, images, and other
  static assets) and single-page apps. Firebase Hosting provides fast
  content delivery through a global CDN, free SSL certificates, and
  custom domain support.

  If you developed a static or single-page web app in Firebase Studio,
  you can publish directly from Firebase Studio by prompting
  [Gemini in Firebase](https://firebase.google.com/docs/studio/try-gemini) to publish your app.
- [**Cloud Run:**](https://firebase.google.com/docs/studio/deploy-app#cloud-run) Use Cloud Run to deploy
  containerized applications. It's a good choice for publishing scalable
  and portable applications that can run on any platform.

- **Other deployment options:** Deploy to the hosting solution of your
  choice, including other platforms or your own server.

## Publish and monitor your app with Firebase App Hosting

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

### (Cloud Firestore only) Add indexes and verify security rules in production

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

### Monitor your app with App Hosting observability

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

### Roll back your App Hosting site

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

## Firebase Hosting

You can publish static and single-page web apps to Firebase Hosting from
your Firebase Studio workspace.

If you don't have the required Firebase project permissions, ask a
Firebase project Owner to assign you the applicable role in the
[Firebase console Users and Permissions
page](https://firebase.google.com/docs/studio/https://console.firebase.google.com/project/_/settings/iam).
If you have questions about accessing your Firebase project,
including finding or assigning an Owner, see [Permissions and access to
Firebase projects](https://firebase.google.com/support/faq#projects-permissions-and-access).

> [!NOTE]
> **Note:** Unlike Firebase App Hosting, a Cloud billing account isn't required to set up Firebase Hosting.

### Publish with Gemini in Firebase

1. In the Gemini in Firebase chat, enter a prompt such as "Publish my app."

2. Gemini in Firebase guides you through the necessary steps. This may
   include [creating a Firebase project and registering your
   app](https://firebase.google.com/docs/web/setup) if you haven't done so already.

> [!TIP]
> **Tip:** If the publishing process fails, enter the "Publish my app" prompt again to retry the process.

### Publish from the Firebase Studio panel

Firebase Hosting is optimized for static sites and single-page applications.
If your project has dynamic content, Gemini in Firebase might not initiate
the publishing flow. If this happens but you still want to use
Firebase Hosting, publish your project from the Firebase Studio panel:

1. If you haven't done so already,
   [create a Firebase project and register your app](https://firebase.google.com/docs/web/setup).

2. Open your
   [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/)
   workspace.

   - If you're using the App Prototyping agent, click ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg) **Switch to Code** to open Code view.
3. In the navigation pane, click the Firebase Studio icon to open the
   panel, then expand the **Firebase Hosting** section.

4. Click **Authenticate Firebase** and follow the prompts in
   the Terminal window to authenticate your Firebase account.

5. Click **Initialize Firebase Hosting** and follow the prompts in the
   Terminal window to set up your deployment configuration.

6. To deploy your app, click either **Deploy to Production** or
   **Deploy to Channel** from the **Firebase Hosting** section of the
   Firebase Studio panel.

## Cloud Run

Before you deploy using Cloud Run, make sure you [set up a Google Cloud
project and enable
Cloud Billing](https://cloud.google.com/billing/docs/how-to/create-billing-account).

1. Open your
   [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/)
   workspace. If you're using the App Prototyping agent, click
   ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)
   **Switch to Code** to open Code view.

2. Click the Firebase Studio icon in the navigation pane to open the
   Firebase Studio panel and click **Deploy to Cloud Run**.

3. Select **Allow this workspace to access Google Cloud resources using my
   Google Account** and then select a Google Cloud project with billing
   enabled from the dialog windows.

4. Click **Authenticate** from the **Cloud Run** section of the
   Firebase Studio panel and follow the prompts to authenticate.

5. Click **Deploy** and follow the prompts to set up your deployment
   configuration and deploy your app.

## Next steps

- [Learn more about Firebase integrations](https://firebase.google.com/docs/studio/google-integrations).