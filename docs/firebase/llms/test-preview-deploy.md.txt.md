# Source: https://firebase.google.com/docs/hosting/test-preview-deploy.md.txt

Before deploying to your live site, you'll want to view and test your changes.
Firebase Hosting enables you to view and test changes locally and interact
with emulated backend project resources. If you need your teammates to view and
test your changes, Hosting can create sharable, temporary preview URLs for
your site. We even support a
[GitHub integration](https://firebase.google.com/docs/hosting/github-integration) to deploy from a pull
request.

## Before you begin

Complete the steps listed on the
[Hosting Get Started page](https://firebase.google.com/docs/hosting/quickstart), specifically the
following tasks:

1. Install or update the Firebase CLI to its latest version.
2. Connect the local project directory (containing your app's content) to your Firebase project.

You can optionally deploy your app's Hosting content and config, but it's
not a prerequisite for the steps on this page.

> [!CAUTION]
> We recommend setting up a separate Firebase project for testing and developing your web app. You want to protect your production site from unintentional changes to your project resources (databases, storage, rules, functions, etc.) during testing and development.

## **Step 1:** Test locally

If you're making quick iterations or you want your app to interact with emulated
backend project resources, you can test your Hosting content and config
locally. When testing locally, Firebase serves your web app at a locally hosted
URL.

Hosting is part of the [Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite),
which enables your app to interact with your *emulated* Hosting content and
config, as well as optionally your *emulated* project resources (functions,
databases, and rules).

1. *(Optional)* By default, your locally hosted app will interact with *real* ,
   not *emulated* , project resources (functions, database, rules, etc.).
   You can instead optionally connect your app to use any *emulated* project
   resources that you've configured. Learn more:
   [Realtime Database](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=RTDB) \|
   [Cloud Firestore](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=Firestore) \|
   [Cloud Functions](https://firebase.google.com/docs/emulator-suite/connect_functions)

2. From the root of your local project directory, run the following command:

   ```
   firebase emulators:start
   ```
3. Open your web app at the local URL returned by the CLI (usually
   `http://localhost:5000`).

4. To update the local URL with changes, refresh your browser.

### Test from other local devices

By default, the emulators only respond to requests from `localhost`. This
means that you'll be able to access your hosted content from your computer's web
browser but not from other devices on your network. If you'd like to test from
other local devices, configure your `firebase.json` like so:

    "emulators": {
        // ...

        "hosting": {
          "port": 5000,
          "host": "0.0.0.0"
        }
      }

<br />

#### Test locally using `firebase serve` *(not recommended)*

<br />

> [!CAUTION]
> `firebase serve` is not recommended. Instead, we recommend [testing locally with the
> Firebase Local Emulator Suite](https://firebase.google.com/docs/hosting/test-preview-deploy#test-locally).

When using `firebase serve`, your app interacts with an *emulated* backend for
your Hosting content and config (and optionally functions) but your *real*
backend for all other project resources.

1. From the root of your local project directory, run the following command:

   ```
   firebase serve --only hosting
   ```

   > [!NOTE]
   > **Note:** By running this command with the `--only hosting` flag, you're only emulating your Hosting content and config. If you *also* want to emulate functions, run this command with the flag `--only hosting,functions`.

2. Open your web app at the local URL returned by the CLI (usually
   `http://localhost:5000`).

3. To update the local URL with changes, refresh your browser.

##### Use `firebase serve` to test from other local devices

By default, `firebase serve` only responds to requests from `localhost`. This
means that you'll be able to access your hosted content from your computer's web
browser but not from other devices on your network. If you'd like to test from
other local devices, use the `--host` flag, like so:

```
firebase serve --host 0.0.0.0  // accepts requests to any host
```

<br />

<br />

## **Step 2:** Preview and share

If you want others to view changes to your web app before going live, you can
use preview channels.

After you deploy to a preview channel, Firebase serves your web app at a
"preview URL", which is a sharable, temporary URL. When using a preview URL,
your web app interacts with your *real* backend for all project resources (with
the exception of any ["pinned" functions in your rewrites
config](https://firebase.google.com/docs/hosting/full-config#pintag-in-rewrites-to-function)).

Note that although preview URLs are difficult to guess (as they contain a random
hash), they are public. So, anyone who knows the URL can access it.

1. From the root of your local project directory, run the following command:

   ```
   firebase hosting:channel:deploy CHANNEL_ID
   ```

   Replace <var translate="no">CHANNEL_ID</var> with a string with no spaces
   (for example, `feature_mission-2-mars`). This ID will be used to construct
   the preview URL associated with the preview channel.

   > [!NOTE]
   > **Note:** You don't need to pass the `--only hosting` flag because this command *only* deploys your Hosting content and config (along with any ["pinned"
   > functions in your rewrites
   > config](https://firebase.google.com/docs/hosting/full-config#pintag-in-rewrites-to-function)). Apps served at preview URLs *always* interact with *real* project resources (except for deployed "pinned" functions).

2. Open your web app at the preview URL returned by the CLI. It will look
   something like this:
   `PROJECT_ID*--*CHANNEL_ID*-*RANDOM_HASH.web.app`

3. To update your preview URL with changes, run the same command again. Make
   sure to specify the same `CHANNEL_ID` in the command.

Learn about [managing preview channels](https://firebase.google.com/docs/hosting/manage-hosting-resources),
including how to set a channel's expiration.

Firebase Hosting supports a GitHub Action that automatically creates and
updates a preview URL when you commit changes to a pull request. Learn how to
[set up and use this GitHub Action](https://firebase.google.com/docs/hosting/github-integration).

## **Step 3:** Deploy live

When you're ready to share your changes with the world, deploy your Hosting
content and config to your live channel. Firebase offers a couple different
options for this step depending on your use case (see options below).

### Option 1: Clone from a preview channel to your live channel

This option provides confidence that you're deploying to your live channel the
*exact* content and config that you tested in a preview channel. Learn more
about
[cloning versions](https://firebase.google.com/docs/hosting/manage-hosting-resources#version-cloning).

1. From any directory, run the following command:

   ```
   firebase hosting:clone SOURCE_SITE_ID:SOURCE_CHANNEL_ID TARGET_SITE_ID:live
   ```

   Replace each placeholder with the following:
   - <var translate="no">SOURCE_SITE_ID</var> and <var translate="no">TARGET_SITE_ID</var>: These are the IDs
     of the Hosting sites that contain the channels.

     - For your default Hosting site, use your Firebase project ID.
     - You can specify sites that are in the same Firebase project or even in different Firebase projects.
   - <var translate="no">SOURCE_CHANNEL_ID</var>: This is the identifier for the channel that
     is currently serving the version you want to deploy to your live channel.

     - For a live channel, use `live` as the channel ID.
2. [View your changes](https://firebase.google.com/docs/hosting/test-preview-deploy#view-changes) (next step).

### Option 2: Deploy from your local project directory to your live channel

This option provides you flexibility to adjust configurations specific to the
live channel or to deploy even if you haven't used a preview channel.

1. From the root of your local project directory, run the following command:

   ```
   firebase deploy --only hosting
   ```

   > [!NOTE]
   > **Note:** By running this command with the `--only hosting` flag, you're only deploying your Hosting content and config (along with any ["pinned"
   > functions in your rewrites
   > config](https://firebase.google.com/docs/hosting/full-config#pintag-in-rewrites-to-function)). If you *also* want to [deploy other project resources or
   > configurations](https://firebase.google.com/docs/cli#partial_deploys) (like backend-triggered functions or Cloud Storage rules), run this command with a comma-separated list in the flag (for example, `--only hosting,storage`).

2. [View your changes](https://firebase.google.com/docs/hosting/test-preview-deploy#view-changes) (next step).

> [!NOTE]
> **Note:** For Spark plan projects, Firebase blocks upload and hosting of certain executable file types for Windows (files with `.exe`, `.dll` and `.bat` extensions), Android (`.apk` extension) and Apple (`.ipa` extension) by Cloud Storage for Firebase and Firebase Hosting. This policy exists to prevent abuse on our platform. Projects on the Blaze plan are not affected. For more information, see [this FAQ](https://firebase.google.com/docs/hosting/faq-and-troubleshooting#hosting-exe-restrictions).

## **Step 4:** View your changes on your live site

Both of the options above deploy your Hosting content and config to the
following sites:

- The Firebase-provisioned subdomains for your default Hosting site and any
  additional Hosting sites:  

  `SITE_ID.web.app` (like `PROJECT_ID.web.app`)  

  `SITE_ID.firebaseapp.com` (like `PROJECT_ID.firebaseapp.com`)

- Any [custom domains](https://firebase.google.com/docs/hosting/custom-domain) that you've connected to
  your Hosting site(s)

To restrict the deploy to a specific Hosting site,
[specify a deploy target](https://firebase.google.com/docs/hosting/multisites#cli-commands-with-deploy-targets)
in your CLI command.

## Other deploy activities and information

### Add a comment for the deploy

You can optionally add a comment to a deploy. This comment will display with the
other deployment information on the
[Hosting dashboard](https://console.firebase.google.com/project/_/hosting/main)
in the Firebase console. For example:

```
firebase deploy --only hosting -m "Deploying the best new feature ever."
```

### Add predeploy and postdeploy scripted tasks

You can optionally connect shell scripts to the `firebase deploy` command to
perform predeploy or postdeploy tasks. For example, a postdeploy hook could
notify administrators of new site content deploys. Refer to the
[Firebase CLI documentation](https://firebase.google.com/docs/cli#hooks) for more details.

### Caching deployed content

When a request is made for *static content* , Firebase Hosting automatically
caches the content on the CDN. If you redeploy your site's content, Firebase
automatically clears *all your cached static content* across the CDN so that new
requests receive your new content.

Note that you can configure the
[caching of dynamic content](https://firebase.google.com/docs/hosting/manage-cache).

### Serving over HTTPS

> [!CAUTION]
> Firebase Hosting is SSL-only, meaning that content is only served over HTTPS.

Make sure that all external resources that are not hosted on
Firebase Hosting are loaded over SSL (HTTPS),including any external scripts.
Most browsers do not allow users to load "mixed content" (SSL and non-SSL
traffic).

### Deleting files

In Firebase Hosting, the primary way to delete selected files
from a deployed site is to delete the files locally, and then redeploy.

## Next steps

- Integrate with GitHub and iterate your previewed content by
  [setting up the GitHub Action](https://firebase.google.com/docs/hosting/github-integration).

- Learn about further hosting capabilities:

  - [Configure hosting behavior](https://firebase.google.com/docs/hosting/full-config)
  - [Connect a custom domain](https://firebase.google.com/docs/hosting/custom-domain)
  - [Serve dynamic content and host microservices](https://firebase.google.com/docs/hosting/serverless-overview)
- Take a look at the full documentation for the [Firebase CLI](https://firebase.google.com/docs/cli).

- Prepare to launch your app:


  - Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) for your project in the Google Cloud console.
  - Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage) in the Firebase console to get an overall picture of your project's usage across multiple Firebase services. You can also visit the [Hosting *Usage*
    dashboard](https://console.firebase.google.com/project/_/hosting/usage) for more detailed usage information.
  - Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).