# Source: https://firebase.google.com/docs/hosting/quickstart.md.txt

[Video](https://www.youtube.com/watch?v=P0x0LmiknJc)

Firebase Hosting gives you a fast, secure, and reliable way to host your
app's static assets (HTML, CSS, JavaScript, media files, etc.) as well as to
[serve dynamic content and host microservices](https://firebase.google.com/docs/hosting/serverless-overview).

Our production-grade hosting is backed by a global content delivery network
(CDN). Hosting serves your content over SSL, by default, and can be used
with your own [custom domain](https://firebase.google.com/docs/hosting/custom-domain) or on your project's
subdomains at no cost on `web.app` and `firebaseapp.com`.

## Before you begin

Before you can set up Firebase Hosting, you need to
[create a Firebase project](https://firebase.google.com/docs/web/setup).

## **Step 1** : Install the Firebase CLI

Visit the Firebase CLI documentation to learn how to
[install the CLI](https://firebase.google.com/docs/cli#install_the_firebase_cli) or
[update to its latest version](https://firebase.google.com/docs/cli#update-cli).

> [!NOTE]
> **Note:** You can also run Firebase CLI commands in Cloud Shell. [Cloud Shell](https://firebase.google.com/docs/cloud-shell) is a browser-based, pre-authenticated command-line environment, accessible from the Firebase console, and comes with the Firebase CLI pre-installed. This makes it a convenient option for getting started quickly, provided you add your project files to the Cloud Shell environment.

## **Step 2**: Initialize your project

To connect your local project files to your Firebase project, run the following
command from the root of your local project directory:

```
firebase init hosting
```

During project initialization, from the Firebase CLI prompts:

1. **Select a Firebase project to connect to your local project directory.**

   The selected Firebase project is your "default" Firebase project for your
   local project directory. To connect additional Firebase projects to your
   local project directory, set up [project aliases](https://firebase.google.com/docs/cli#project_aliases).
2. **Specify a directory to use as your public root directory.**

   This directory contains all your publicly served static files, including your
   `index.html` file and any other assets that you want to deploy to
   Firebase Hosting.
   - The default for the public root directory is called `public`.

     - You can specify your public root directory now or you can
       [specify it later](https://firebase.google.com/docs/hosting/full-config#public) in your
       `firebase.json` configuration file.

     - If you select the default and don't already have a directory called
       `public`, Firebase creates it for you.

   - If you don't already have a valid `index.html` file or `404.html` file in
     your public root directory, Firebase creates them for you.

3. **Choose a configuration for your site.**

   If you select to make a one-page app, then Firebase automatically adds
   [rewrite configurations](https://firebase.google.com/docs/hosting/full-config#rewrites) for you.

At the end of initialization, Firebase automatically creates and adds two files
to the root of your local app directory:

- A `firebase.json` configuration file that lists your project configuration.
  Learn more about this file on the
  [configure hosting behavior](https://firebase.google.com/docs/hosting/full-config) page.

- A `.firebaserc` file that stores your
  [project aliases](https://firebase.google.com/docs/cli#project_aliases).

## **Step 3**: Deploy to your site

To deploy to your site, run the following command from the root of your local
project directory:

```
firebase deploy --only hosting
```

> [!NOTE]
> **Note:** By running this command with the `--only hosting` flag, you're only deploying your Hosting content and config. If you *also* want to [deploy other project resources or configurations](https://firebase.google.com/docs/cli#partial_deploys) (like functions or database rules), run this command with a comma-separated list in the flag (for example, `--only hosting,functions`).

This command deploys your Hosting content and config to the following
Firebase-provisioned subdomains:

- `PROJECT_ID.web.app`
- `PROJECT_ID.firebaseapp.com`

Learn more about
[deploys and even locally testing your site](https://firebase.google.com/docs/hosting/test-preview-deploy).

## Next steps

Now your site is ready to share with the world!

- Continue to improve your site. Test locally, share changes at a temporary
  preview URL, then deploy to your live site. Follow this
  [step-by-step guide](https://firebase.google.com/docs/hosting/test-preview-deploy).

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