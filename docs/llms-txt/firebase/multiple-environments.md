# Source: https://firebase.google.com/docs/app-hosting/multiple-environments.md.txt

<br />

It's common to have multiple environments deployed from the same codebase, each with slightly different configuration. For example, you might want to assign less CPU and RAM to your staging environment, or you might want to make sure your production environment keeps at least 1 instance active and ready to serve requests. You might also want to specify different environment variables and secrets depending on the environment and resources you want to use.

This guide describes how to deploy a production and staging environment, each to a separate Firebase project. Following the same principles, you can deploy to other different kinds of environments. To learn more about environments, check out the[Overview of environments](https://firebase.google.com/docs/projects/dev-workflows/overview-environments)and[General best practices for setting up Firebase projects](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices).

### Prerequisites

- Your application code is already stored in GitHub.
- You have already created a distinct project for each of your environments---for example`my-production-firebase-project`and`my-staging-firebase-project`. Make sure to to tag your production Firebase project with the["production" environment type](https://firebase.google.com/docs/projects/dev-workflows/overview-environments#prod-environment).
- In each project, you've created anApp Hostingbackend, with the live branch set to the GitHub branch you want to deploy (such as`main`). See[Get started withApp Hosting](https://firebase.google.com/docs/app-hosting/get-started)for more information.

| **Note:** While it is technically possible to deploy multiple environoments to multiple backends created in the same project, it isn't recommended. See[GCP guidance](https://cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines#deployment-environment)and[Firebase guidance](https://firebase.google.com/docs/projects/dev-workflows/overview-environments)on setting up and deploying across multiple environments.

### Step 0: Create a default configuration in apphosting.yaml

App Hostingsupports a configuration file called`apphosting.yaml`to manage runtime settings (CPU, concurrency, memory limits, etc.) and environment variables for your app. It also supports references to secrets managed with Cloud Secret Manager, making it safe to check into source control. For more information, see[Configure a backend](https://firebase.google.com/docs/app-hosting/configure#configure-backend).

To get started, create an`apphosting.yaml`file in your app's root directory. This is the fallback configuration file that is used when an environment-specific configuration file isn't found. The values stored in`apphosting.yaml`should be defaults that are safe to use for all environments.

The next sections explain how to override default values in`apphosting.yaml`for specific environments. This example flow creates a staging environment.

### Step 1: Set Environment name

EachApp Hostingbackend has an**Environment name**setting. This field is used to map your backend to an environment-specific configuration file, and can be changed at any time. You can only set one environment name per backend.

To set your backend's environment name,

1. In the Firebase console, select your staging project (in this example, my-staging-firebase-project).
2. SelectApp Hostingfrom the left nav.
3. Click**View dashboard**on your chosen backend.
4. In the**Settings** tab, select**Environment**.
5. Under**Environment name,** enter the name of your environment. You can name the environment whatever you like. In this example, it's**staging**.
6. Click**Save**.

When anApp Hostingrollout is triggered for your backend (either on git push or manually through the console),App Hostingwill check for an`apphosting.`<var translate="no">ENVIRONMENT_NAME</var>`.yaml`file before falling back to`apphosting.yaml`.

### Step 2: Create your environment-specific`apphosting.yaml`file

For your environment-specific configuration, create a file with the name`apphosting.`<var translate="no">ENVIRONMENT_NAME</var>`.yaml`in order to specify environment-specific overrides. This file has the same format as the default[apphosting.yaml](https://firebase.google.com/docs/app-hosting/configure)and must be located in your app's root directory alongside`apphosting.yaml`.

At build time,App Hostingmerges these two files, with priority given to values in the environment-specific YAML file over the base`apphosting.yaml`file.

In this example, you'll create a file named`apphosting.staging.yaml`in the app's root directory:  


    runConfig:
      cpu: 1
      memoryMiB: 512
      concurrency: 5

    env:
    -   variable: API_URL
        value: api.staging.service.com
        availability:
          -   BUILD

    -   variable: DATABASE_URL
        secret: secretStagingDatabaseURL

Suppose you already had an`apphosting.yaml`that looked like:  

    runConfig:
      cpu: 3
      memoryMiB: 1024
      maxInstances: 4
      minInstances: 0
      concurrency: 100

    env:
    -   variable: API_URL
        value: api.service.com
        availability:
          -   BUILD
          -   RUNTIME

    -   variable: STORAGE_BUCKET
        value: mybucket.firebasestorage.app
        availability:
          -   RUNTIME

    -   variable: API_KEY
        secret: secretIDforAPI

The final merged output, which you can inspect in your Cloud Build logs, would look like this:  

    runConfig:
      cpu: 1
      memoryMiB: 512
      maxInstances: 4
      minInstances: 0
      concurrency: 5

    env:
    -   variable: API_URL
        value: api.staging.service.com
        availability:
          -   BUILD

    -   variable: STORAGE_BUCKET
        value: mybucket.firebasestorage.app
        availability:
          -   RUNTIME

    -   variable: API_KEY
        secret: secretIDforAPI

    -   variable: DATABASE_URL
        secret: secretStagingDatabaseURL

Note that certain`runConfig`values such as CPU have been overwritten as well as any overlapping environment variables.
| **Note:** You'll still need to grant the proper service accounts access to any secrets that you create, the same as you would for`apphosting.yaml`secrets. See[store and access secret parameters](https://firebase.google.com/docs/app-hosting/configure#secret-parameters)for more information._

### Step 3: Deploy your codebase

Once you are finished editing your environment specific`apphosting.`<var translate="no">ENVIRONMENT_NAME</var>`.yaml`file, push your file to GitHub:  

    $ git add apphosting.<ENVIRONMENT_NAME>.yaml
    $ git commit -m "Added environment specific yaml file"
    $ git push

Any backends tagged with this environment name will use the specific override values you have specified in its corresponding YAML file, and fall back to`apphosting.yaml`when a value isn't found. For backends without an associated environment name, you can continue to use apphosting.yaml.

## Next steps

- Go deeper: walk through a Firebase codelab that integrates a hosted app with Firebase Authentication and Google AI features:[Next.js](https://firebase.google.com/codelabs/firebase-nextjs)\|[Angular](https://firebase.google.com/codelabs/firebase-web)
- [Connect a custom domain](https://firebase.google.com/docs/app-hosting/custom-domain).
- [Configure your backend](https://firebase.google.com/docs/app-hosting/configure).
- [Monitor rollouts, site usage, and logs](https://firebase.google.com/docs/app-hosting/rollouts).