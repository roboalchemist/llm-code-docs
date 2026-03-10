# Source: https://firebase.google.com/docs/hosting/frameworks/flutter.md.txt

With the Firebase framework-aware CLI, you can deploy your Flutter application
to Firebase.

> [!NOTE]
> **Note:** Framework-aware Hosting is an early public preview. This means that the functionality might change in backward-incompatible ways. A preview release is not subject to any SLA or deprecation policy and may receive limited or no support.

## Before you begin

Before you get started deploying your app to Firebase,
review the following requirements and options:

- Firebase CLI version 12.1.0 or later. Make sure to [install the CLI](https://firebase.google.com/docs/cli#install_the_firebase_cli) using your preferred method.
- Optional: Billing enabled on your Firebase project (required if you plan to use SSR)

## Initialize Firebase

To get started, initialize Firebase for your framework project.
Use the Firebase CLI for a new project, or modify `firebase.json` for an
existing project.

### Initialize a new project

1. In the Firebase CLI, enable the web frameworks preview:

   ```
   firebase experiments:enable webframeworks
   ```
2. Run the initialization command from the CLI and then follow the prompts:

   ```
   firebase init hosting
   ```

   <br />

3. Answer yes to "Do you want to use a web framework? (experimental)"

4. Choose your hosting source directory; this could be an existing Flutter app.

5. If prompted, choose Flutter Web.

### Initialize an existing project

Change your hosting config in `firebase.json` to have a `source` option, rather
than a `public` option. For example:

    {
      "hosting": {
        "source": "./path-to-your-flutter-app"
      }
    }

## Serve static content

After initializing Firebase, you can serve static content with the standard
deployment command:

    firebase deploy