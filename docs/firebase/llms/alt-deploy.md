# Source: https://firebase.google.com/docs/app-hosting/alt-deploy.md.txt

<br />

Most of the time, we recommend using[automatic rollouts](https://firebase.google.com/docs/app-hosting/rollouts)or[manually-triggered rollouts](https://firebase.google.com/docs/app-hosting/rollouts#manually-trigger)from the Firebase console. However, you may have a use for a more customized deployment flow.App Hostinghas multiple options for custom deployment.

## Deploy from source with theFirebaseCLI

FirebaseCLI 14.4.0 and higher lets you push your app's source code and configuration directly from your local machine to Firebase. This is convenient if you have other Firebase deployments (such as security rules or functions) and want to deploy your web app and backend services together with a single CLI command.

On deployment,App Hostinguploads your source code to a Google Cloud Storage bucket, runs your framework build command in Cloud Build, and deploys the final artifacts to Cloud Run and Cloud CDN.App Hostinguses the same[build process](https://firebase.google.com/docs/app-hosting/build)for local source deployments as GitHub deployments. If you have a`.gitignore`file in your project, the files and folders it lists are excluded from your deployment.
| **Note:** Make sure you have a project on the Blaze Pay-as-you-go plan and that you are using`firebase-tools`version 14.4.0 or higher.

To deploy your app from local source:

1. Run`firebase init apphosting`in your local project directory.
2. At the prompt, select**Use an existing project**, and then select the chosen Firebase project.
3. Select either a new or existing backend to deploy to; this step sets up App Hosting deployments for your local directory, prompting you for the informationApp Hostingneeds to successfully deploy your app:

   1. The ID of the backend to deploy to
   2. The region to deploy to (if creating a new backend)
   3. The path to the root directory of the application code

   App Hostingsaves your deployment preferences in`firebase.json`(creating the file in your local project if it doesn't exist). Once initialization completes successfully, you can run`firebase deploy`to deploy your source code toApp Hosting.

If you have local source deployments set up for multiple backends (meaning there are multiple`backendId`entries in`firebase.json`),`firebase deploy`will deploy to each of those backends. To deploy to a specific backend, use`firebase deploy --only apphosting:backendId`

### Example firebase.json

    {
      "apphosting": [
        {
          "backendId": "my-backend",
          // rootDir specifies the directory containing the app to deploy, but the entire
          // parent directory of firebase.json will be zipped and uploaded to ensure that
          // dependencies outside of the app directory will be available at build time.
          "rootDir": "./my-app",
          "ignore": [
            "node_modules",
            ".git",
            "firebase-debug.log",
            "firebase-debug.*.log",
            "functions",
          ],
        },
      ]
    }

## Deploy using Terraform

If you need greater control over the build process and deployed environment, you can deploy using Terraform. Terraform lets you define and manage yourApp Hostingresources using declarative configuration files, and provides the ability to deploy your own prebuilt container image directly toApp Hostinginstead of relying onApp Hostingto build from your source code.

If you're new to Terraform, see[Get started with Terraform and Firebase](https://firebase.google.com/docs/projects/terraform/get-started). If you're already familiar with Terraform, you can get started with sample configuration files and other[App Hostingresources](https://firebase.google.com/docs/projects/terraform/get-started#resources-app-hosting).

## Deploy using Firebase Studio

When you create a web app with the App Prototyping agent inFirebase Studio, you can publish, or deploy, to FirebaseApp Hostingdirectly fromFirebase Studio. See[Publish your app with App Hosting](https://firebase.google.com/docs/studio/deploy-app#publish).

## Set up a GitHub connection for CI/CD

You have the option to connect a GitHub repository at any time in the**Deployment** tab of a backend's settings in theFirebaseconsole. This allows you to deploy an app prototype from a local environment likeFirebase Studioor another IDE and then transition to an automated CI/CD pipeline when you're ready.