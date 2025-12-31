# Source: https://firebase.google.com/docs/emulator-suite/use_app_hosting.md.txt

<br />

You can perform local tests of your app prior toApp Hostingdeployment using theApp Hostingemulator, which is part of the Firebase Local Emulator Suite.

Before using theApp Hostingemulator, make sure that you[understand the overall FirebaseLocal Emulator Suiteworkflow](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=Firestore), and that you[install and configure](https://firebase.google.com/docs/emulator-suite/install_and_configure)theLocal Emulator Suiteand review its[CLI commands](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup).

This topic assumes you are already familiar withApp Hosting. If needed, review the[App Hostingintroduction](https://firebase.google.com/docs/app-hosting)and other materials to help you[understand howApp Hostingworks](https://firebase.google.com/docs/app-hosting/about-app-hosting).

## What can I do with theApp Hostingemulator?

TheApp Hostingemulator lets you test and refine your web applications locally. This can streamline your development process and enhance the quality of web apps built using Firebase and deployed onApp Hosting.

TheApp Hostingemulator:

1. Lets you run your web app locally, with environment variables and secrets defined in`apphosting.yaml`configuration files.
2. Can override environment variables and secrets for use in the emulator with the`apphosting.emulator.yaml`file.
3. Can be used alongside other Firebase emulators. If you're using the Firestore, Auth, or any other emulator, theLocal Emulator Suiteensures that these emulators are started first before theApp Hostingemulator.

## Configure the emulator

To get started, install and initialize theLocal Emulator Suiteas described in[Install, configure and integrate Local Emulator Suite](https://firebase.google.com/docs/emulator-suite/install_and_configure). In addition to any other Firebase emulators that you want to set up, make sure to select`App Hosting
Emulator`. The CLI prompts you for someApp Hostingemulator values, including:

- Your app's root directory relative to the project; this is important if you are using[monorepos withApp Hosting](https://firebase.google.com/docs/app-hosting/monorepos).
- Whether you want to override any values for local development.
- Whether you want to grant teammates access to secrets for local development.

    firebase init emulators
    === Emulators Setup
    ? Which Firebase emulators do you want to set up? Press Space to select emulators, then Enter to confirm your choices. (Press
    <space> to select, <a> to toggle all, <i> to invert selection, and <enter> to proceed)
    â¯â¯ App Hosting Emulator
     â¯ Firestore Emulator
     â¯ Database Emulator
     â¯ Hosting Emulator
     â¯ Pub/Sub Emulator
     â¯ Storage Emulator
     â¯ Eventarc Emulator
    (Move up and down to reveal more choices)

    ? Specify your app's root directory relative to your project (./)

    ? The App Hosting emulator uses a file called apphosting.emulator.yaml to
    override values in apphosting.yaml for local testing. This codebase does not
    have one, would you like to create it? (Y/n)

    ? Which environment variables would you like to override? (Press <space> to
    select, <a> to toggle all, <i> to invert selection, and <enter> to proceed)
    â¯â¯ MEMCACHE_ADDR
     â¯ API_KEY

    ? What new value would you like for plaintext MEMCACHE_ADDR?

    ? What would you like to name the secret reference for API_KEY? (test-api-key)

    ? What new value would you like for secret TESTKEY [input is hidden]? [input is hidden]

    ? Your config has secret values. Please provide a comma-separated list of users
    or groups who should have access to secrets for local development:

    â  Successfully set IAM bindings on secret test-api-key.

Any values you provide in this setup flow are used to update yourApp Hostingemulator configuration in`firebase.json`. You can also configure the App Hosting emulator by updating`firebase.json`directly. The schema for the App Hosting emulator is:  

    {
      ...
      "emulators": {
        "apphosting": {
          "startCommand": <command> [optional]
          "rootDirectory": <path> [optional]
          }
        }
      }

- `startCommand`is automatically generated and set when the emulator is initialized. If not provided, the emulator will detect and run your package manager's dev command.
- `rootDirectory`is used to support monorepo project setups. If your web app is in a subdirectory, you need to provide the path of that directory relative to the root (the location of`firebase.json`).

### Manage emulation

Emulator initialization creates an`apphosting.emulator.yaml`file in your app's root directory. This configuration file has the same schema as the[`apphosting.yaml`](https://firebase.google.com/docs/app-hosting/configure#configure-backend)file used in production, but instead is meant strictly for local development. By default, the emulator reads configuration from your`apphosting.yaml`file, but if an`apphosting.emulator.yaml`file is present, then configurations in that file are prioritized and given precedence.

The`apphosting.emulator.yaml`file is designed to be safe to commit and share with colleagues. To help ensure you don't accidentally commit sensitive data to source repositories, any environment variable that is a secret in`apphosting.yaml`must also be a secret in`apphosting.emulator.yaml`. If a secret does not need change between production and local development (e.g. a Gemini API key), it does not need to be added to`apphosting.emulator.yaml`; instead[grant your team access to the secret](https://firebase.google.com/docs/emulator-suite/use_app_hosting#grant-secret-access).

If your application uses many secrets (for example, API keys for three different services, with different values for each of production, staging, and local development) you may exceed Cloud Secret Manager's free tier and pay $0.06 per additional secret per month. If you prefer to manage local configuration outside of source control to avoid this fee, you can use the legacy`apphosting.local.yaml`file. Unlike`apphosting.emulator.yaml`this file is allowed to provide plaintext values for environment variables that are secret values in`apphosting.yaml`.
| **Caution:** The`apphosting.local.yaml`file should not be committed to your source code repository, as the file may contain secret values in plain text.

### Grant users or groups access to secrets

Secrets stored in`apphosting.emulator.yaml`are read when the emulator starts up. This means that your development team needs access to the secret. You can use the`apphosting:secrets:grantaccess`command to grant access to a secret to either a user or a group by email.  

    firebase apphosting:secrets:grantaccess test-api-key --emails my-team@my-company.com

Where applicable, consider using test-only keys in`apphosting.emulator.yaml`that don't have access to production data, cannot have global side effects (sending emails, charging credit cards), and/or have lower quotas. This helps ensure that unreviewed code has fewer real-world consequences.

Consider using Google Groups to manage access to secrets rather than granting access to individual users. This will simplify onboarding new members to your developer team because adding them to the group will grant them access to all the secrets they need. You may already have an appropriate group where developers communicate with each other. Controlling access by Google Groups also helps ensure that developers who leave your team lose access to all secrets when they are removed from the email group. If the secret has access to production data or real-world side effects, it still may be appropriate to rotate your key and give it a new value with`firebase apphosting:secrets:set`however.

### Run the emulator

    firebase emulators:start

This will start all the emulators defined in your`firebase.json`file including theApp Hostingemulator.