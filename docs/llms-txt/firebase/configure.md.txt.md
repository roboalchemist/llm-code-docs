# Source: https://firebase.google.com/docs/app-hosting/configure.md.txt

App Hosting has been designed for ease of use and low maintenance,
with default settings optimized for most use cases. At the same time,
App Hosting provides tools for you to manage and configure backends
for your specific needs. This guide describes those tools and processes.

## Set and update environment variables

Sometimes you may need additional configuration for your build process.
App Hosting offers environment
configuration to store and retrieve this
type of data for your project through the Firebase console and alternatively
in `apphosting.yaml`.

Setting environment variables in the console is the quickest way to get started.
Use `apphosting.yaml` if you need to [store and access secret
parameters](https://firebase.google.com/docs/app-hosting/configure#secret-parameters), set variables that
are only available at build or run time, or share environment variables across multiple
environments. With both the console and `apphosting.<env>.yaml`, you can [set different values for different
environments](https://firebase.google.com/docs/app-hosting/multiple-environments#step-2:).

### Firebase console

![A screen capture of the Firebase console dialog for adding environment variables](https://firebase.google.com/static/docs/app-hosting/images/env-vars.png)

### `apphosting.yaml`

    env:
    -   variable: STORAGE_BUCKET
        value: mybucket.firebasestorage.app

> [!CAUTION]
> **Caution:** Console-based and file-based configuration have a few key differences, so make sure to review this section carefully. Most importantly: **values set in
> the console always override, or take precedence over, values set in
> `apphosting.yaml`** . See [variable hierarchy](https://firebase.google.com/docs/app-hosting/configure#variable-hierarchy).

### Update variables

You can add and edit environment variables in the Firebase console
in the **Settings** tab for a backend.
Navigate to **View Backend** \>\> **Settings** \>\> **Environment** and then
add, edit, or delete environment variables.

To add and edit environment variables in `apphosting.yaml,`
[create and edit](https://firebase.google.com/docs/app-hosting/configure#configure-backend) the file manually.

Your changes will only take effect with your next rollout, and won't affect the
current one. Either save and create a new rollout or save your variables and
deploy later.

### Set variable availability

Environment variables created in the Firebase console are available at both
build time and run time. This is also the default condition for variables
defined in `apphosting.yaml` unless you have narrowed that scope using the
`availability` property. In `apphosting.yaml` (but not in the console),
you can restrict an environment variable to be
available to only the build environment or available only to the runtime
environment.

    env:
    -   variable: STORAGE_BUCKET
        value: mybucket.firebasestorage.app
        availability:
        -   BUILD
        -   RUNTIME

For Next.js apps, you can also use the `NEXT_PUBLIC_` prefix the same way you
would in your dotenv file to make a variable accessible in the browser.

    env:
    -   variable: NEXT_PUBLIC_STORAGE_BUCKET
        value: mybucket.firebasestorage.app
        availability:
        -   BUILD
        -   RUNTIME

### dotenv files for Next.js

For Next.js apps, [dotenv files containing environment
variables](https://nextjs.org/docs/pages/building-your-application/configuring/environment-variables)
work with App Hosting.

When creating or updating a backend,
you can transfer environment variables from your dotenv file to the Firebase
console by copy and pasting the entire contents of the dotenv file into the
first "Key" field in the "Add new" form in **Environment Variables Settings**.

All the environment variables copied this way should be neatly formatted into
the form with no need to enter each one individually, as long as the input
has a format like the following:

    KEY1=value1
    KEY2=value2
    KEY3=value3

For complex or granular environment variable control with any framework, we
recommend using
[`apphosting.yaml`](https://firebase.google.com/docs/app-hosting/configure#configure-backend).

### Variable hierarchy

Firebase App Hosting applies your variables in an order of precedence based on
their source. For example, values set in the console always override, or take
precedence over, values set in `apphosting.yaml` and dotenv files.

> [!TIP]
> **Tip:** In the Firebase console you can click on a specific rollout to view the details of the rollout. Navigate to **Environment variables in this build** at the bottom of the rollout details panel to review the list of environment variables used during the rollout and their sources.

Here is the full order of precedence:

1. **Firebase console** → variables set in the console
2. **`apphosting.<env>.yaml`** → variables specified in an environment specific yaml file such as `apphosting.staging.yaml` (see [Deploy multiple environments](https://firebase.google.com/docs/app-hosting/multiple-environments#step-2:))
3. `apphosting.yaml` → variables specified in the `apphosting.yaml` file
4. **Firebase system** → variables set by Firebase that contain values for `firebase_config json` or `firebase_webapp_config`, as well as environment variables that set the hostnames and ports for SSR apps (set by App Hosting adapters in [`bundle.yaml`](https://github.com/FirebaseExtended/firebase-framework-tools/tree/main?tab=readme-ov-file#app-hosting-output-bundle))

### Reserved names and limitations

Valid variable keys must start with an uppercase letter and contain only
uppercase letters, digits, and underscores. Some environment variable keys are
reserved for internal use. Don't use any of these keys in your configuration
files:

- Empty strings ("")
- Variables that contain "="
- Any variable beginning with `X_FIREBASE_`
- `PORT`
- `K_SERVICE`
- `K_REVISION`
- `K_CONFIGURATION`
- Duplicate Keys

## Create and edit `apphosting.yaml`

For advanced configuration such as secrets or runtime settings
such as concurrency, CPU, and memory limits, you'll need to create and edit the
`apphosting.yaml` file in your app's root directory. This file
supports references to secrets managed
with Cloud Secret Manager, making it safe to check into source control.

To create `apphosting.yaml`, run the following command:

    firebase init apphosting

This creates a basic starter `apphosting.yaml` file with example (commented)
configuration. After editing, a typical `apphosting.yaml` file might look like
the following, with settings for the backend's Cloud Run service, some
environment variables, and some references to secrets managed by Cloud Secret
Manager:

    # Settings for Cloud Run
    runConfig:
      minInstances: 2
      maxInstances: 100
      concurrency: 100
      cpu: 2
      memoryMiB: 1024

    # Environment variables and secrets
    env:
      - variable: STORAGE_BUCKET
        value: mybucket.firebasestorage.app
        availability:
          - BUILD
          - RUNTIME

      - variable: API_KEY
        secret: myApiKeySecret

        # Same as API_KEY above but with a pinned version.
      - variable: PINNED_API_KEY
        secret: myApiKeySecret@5

        # Same as API_KEY above but with the long form secret reference as defined by Cloud Secret Manager.
      - variable: VERBOSE_API_KEY
        secret: projects/test-project/secrets/secretID

        # Same as API_KEY above but with the long form secret reference with pinned version.
      - variable: PINNED_VERBOSE_API_KEY
        secret: projects/test-project/secrets/secretID/versions/5

The rest of this guide provides more information and context for these example
settings.

## Configure Cloud Run service settings

With `apphosting.yaml` settings, you can configure how your
Cloud Run service is
provisioned. The available settings for the
[Cloud Run service](https://cloud.google.com/run/docs/configuring/services/memory-limits) are provided in the `runConfig` object:

- `cpu` -- Number of CPUs used for each serving instance (default 0).
- `memoryMiB` -- Amount of memory allocated for each serving instance in MiB (default 512)
- `maxInstances` -- Maximum number of containers to ever run at a time (default of 100 and managed by quota)
- `minInstances` -- Number of containers to always keep alive (default 0).
- `concurrency` -- Maximum number of requests that each serving instance can receive (default 80).

Note the important relationship between `cpu` and `memoryMiB`; memory can be set
to any integer value between 128 to 32768, but increasing the memory limit may
require increasing CPU limits:

- Over 4GiB requires at least 2 CPUs
- Over 8GiB requires at least 4 CPUs
- Over 16GiB requires at least 6 CPUs
- Over 24GiB requires at least 8 CPUs

Similarly, the value of `cpu` affects concurrency settings. If you set a value
less than 1 CPU, you must set concurrency to 1, and CPU will only be allocated
during request processing.

## Override build and run scripts

App Hosting infers your app's build and start command based on the detected
framework. If you want to use a custom build or start command, you can override
App Hosting's defaults in `apphosting.yaml`.

    scripts:
      buildCommand: next build --no-lint
      runCommand: node dist/index.js

The build command override takes precedence over any other build commands and
opts your app out of the framework adapters and disables any framework specific
optimizations that App Hosting provides. It's best used when your app features
are not well supported by the adapters. If you want to change your build command
but still use our provided adapters, set your build script in `package.json`
instead as described in [App Hosting framework adapters](https://firebase.google.com/docs/app-hosting/frameworks-tooling#app-hosting-framework-adapters).

Use the run command override when there is a specific
command you want to use to start your app that's different from the
App Hosting-inferred command.

## Configure build output

App Hosting optimizes your app deploys by default by deleting unused output
files as indicated by the framework. If you want to further optimize your app
deploy size or ignore the default optimizations, you can override this in
`apphosting.yaml`.

    outputFiles:
      serverApp:
        include: [dist, server.js]

The `include` parameter takes in a list of directories and files relative to the
app root directory that are necessary to deploy your app. If you want to make sure
that all files are kept, set include to `[.]` and all files will be deployed.

## Store and access secret parameters

Sensitive information such as API keys should be stored as secrets. You can
reference secrets in `apphosting.yaml` to avoid checking sensitive information
into source control.

Parameters of type `secret` represent string parameters which have a value
stored in [Cloud Secret Manager](https://cloud.google.com/security/products/secret-manager).
Instead of
deriving the value directly, secret parameters check against existence in Cloud
Secret Manager, and load the values during rollout.

      -   variable: API_KEY
          secret: myApiKeySecret

Secrets in Cloud Secret manager can have multiple versions. By default, the
value of a secret parameter available to your live backend is pinned to the
latest available version of the secret at the time the backend was built. If you
have requirements for versioning and lifecycle management of parameters, you can
pin to specific versions with Cloud Secret Manager. For example, to pin to
version 5:

      - variable: PINNED_API_KEY
        secret: myApiKeySecret@5

You can create secrets with the CLI command `firebase apphosting:secrets:set`,
and you will be prompted to add necessary permissions. This flow gives you the
option to automatically add the secret reference to `apphosting.yaml`.

To use the full suite of Cloud Secret Manager functionality, you can instead use
the Cloud Secret Manager console. If you do this, you'll need to grant
permissions to your App Hosting backend with the CLI command `firebase
apphosting:secrets:grantaccess`.

## Configure VPC access

Your App Hosting backend can connect to a [Virtual Private Cloud
(VPC)](https://cloud.google.com/vpc/docs) network. For more information and an
example, see [Connect Firebase App Hosting to a VPC network](https://firebase.google.com/docs/app-hosting/vpc-network).

Use the `vpcAccess` mapping in your `apphosting.yaml` file to configure access.
Use either a fully qualified network/connector name or an ID. Using IDs allows
for portability between staging and production environments with different
connectors/networks.

### Direct VPC Egress Configuration (`apphosting.yaml`):

    runConfig:
      vpcAccess:
        egress: PRIVATE_RANGES_ONLY # Default value
        networkInterfaces:
          # Specify at least one of network and/or subnetwork
          - network: my-network-id
            subnetwork: my-subnetwork-id

### Serverless Connector Configuration (`apphosting.yaml`):

    runConfig:
      vpcAccess:
        egress: ALL_TRAFFIC
        connector: connector-id

## Manage backends

Commands for basic management of App Hosting backends are
provided in the [Firebase CLI](https://firebase.google.com/docs/cli#apphosting-commands)and
the Firebase console. This section
describes some of the more common management tasks, including creating and
deleting backends.

### Create a backend

An App Hosting backend is the collection of managed resources that
App Hosting creates to build and run your web app.

> [!CAUTION]
> A project Owner must create the *first* App Hosting backend. After this initial setup, App Hosting Admins can also create and manage additional backends. To see all your organization's repositories, ensure you have the **Organization Admin** role in GitHub. A standard member role only shows repositories you've personally created. For details, see [Firebase App Hosting IAM roles](https://firebase.google.com/docs/projects/iam/roles-predefined-product#app-hosting).

**Firebase console** : From the **Build** menu, select **App Hosting** and then
**Create backend** (if this is the first backend in your Firebase project,
select **Get started**).

**CLI:** (Version 13.15.4 or later) To create a backend, run the following
command from the root of your local project directory, supplying your
[projectID](https://firebase.google.com/docs/projects/learn-more#project-id) as an argument:

    firebase apphosting:backends:create --project PROJECT_ID

For both console or CLI, follow the prompts to choose a
[region](https://firebase.google.com/docs/app-hosting/about-app-hosting#locations), set up a
[GitHub connection](https://firebase.google.com/docs/app-hosting/about-app-hosting#repo-integration),
and configure these basic deployment settings:

- Set **your app's root directory** (defaults to `/`)

  This is usually where your `package.json` file is located.

<!-- -->

- Set the **live branch**

  This is the branch of your GitHub repository that gets deployed to your
  live URL. Often, it's the branch into which feature branches or development
  branches are merged.
- Accept or decline **automatic rollouts**

  Automatic rollouts are enabled by default. At completion of backend creation,
  you can choose for your app to be deployed to App Hosting immediately.
- Assign a name to your backend.

### Delete a backend

To fully remove a backend, first use the Firebase CLI or the
Firebase console to delete it, and then manually
remove related assets, taking special care not to delete any resources that
might be used by other backends or other aspects of your Firebase project.

**Firebase console** : From the **Setting** menu, select **Delete backend**.

**CLI:** (Version 13.15.4 or later)

1. Run the following command to delete the App Hosting Backend.
   This disables all domains for your backend and deletes the associated
   Cloud Run service:

       firebase apphosting:backends:delete BACKEND_ID --project PROJECT_ID

2. (Optional) In the
   Google Cloud Console tab for [Artifact Registry](https://console.cloud.google.com/artifacts),
   delete the image for your backend in "firebaseapphosting-images".

3. In [Cloud Secret Manager](https://cloud.google.com/security/products/secret-manager),
   delete any secrets with "apphosting" in the secret name, **taking special
   care to make sure these secrets are not used by other backends or
   other aspects of your Firebase project**.