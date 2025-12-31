# Source: https://firebase.google.com/docs/studio/monitor.md.txt

After you publish your apps, you should monitor and secure them:

- If you publish withFirebase Hosting, you can link your Firebase project toCloud Loggingto monitor usage and access web request logs. Learn more at[View, search, and filter your web request logs withCloud Logging](https://firebase.google.com/docs/hosting/web-request-logs-and-metrics).

- If you use theApp Prototyping agentto publish withFirebase App Hosting, you can use its observability features to[monitor your web site's performance](https://firebase.google.com/docs/studio/monitor#observability). You can also[write logs toCloud Loggingand view logs and metrics in theFirebaseconsole](https://firebase.google.com/docs/app-hosting/logging).

- If you use AI in your app withGenkit, you can[monitor how your generative AI features are running in production](https://firebase.google.com/docs/studio/monitor#genkit-monitoring).

- If your app includes Firebase services, secure them with[Firebase App Check](https://firebase.google.com/docs/studio/monitor#app-check).

## Monitor your site performance withApp Hostingobservability

The**App overview** panel inFirebase Studioprovides key metrics and information about your app, letting you monitor your web app's performance usingApp Hosting's built-in observability tools. After your site rolls out, you can access the overview by clicking**Publish**. From this panel, you can:

- Click**Publish**to release a new version of your app.
- Share the link to your app or open your app directly in**Visit your app**.
- Review a summary of your app's performance over the last 7 days, including the total number of requests and the status of your latest rollout. Click**View details** to access even more information in the[Firebaseconsole](https://console.firebase.google.com/project/_/apphosting/).
- View a graph of the number of the number of requests your app has received over the last 24 hours, broken down by HTTP status code.
- View the activation status of Firebase services likeFirebase AuthenticationandCloud Firestore.

If you close the App overview panel, you can re-open it at any time by clicking**Publish**.

Learn more about managing and monitoringApp Hostingrollouts at[Manage rollouts and releases](https://firebase.google.com/docs/app-hosting/rollouts).

## GenkitMonitoring for your deployed features

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

## Protect your app withFirebase App Check

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

10. Copy and save your**Key ID** and proceed to[**ConfigureApp Check**](https://firebase.google.com/docs/studio/monitor#configure-app-check).

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

## Next steps

- [Customize yourFirebase Studioworkspace](https://firebase.google.com/docs/studio/customize-workspace).

- [Develop, publish, and monitor a full-stack web app with theApp Prototyping agent](https://firebase.google.com/docs/studio/solution-build-with-ai).