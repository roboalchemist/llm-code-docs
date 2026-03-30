# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/manage-testing-and-production-app-versions.md

# Manage testing and production app versions

When developing an application, to manage the production and test versions:&#x20;

* the developer writes and tests the code with the test application in Make.
* the developer tracks changes in the local `git` repository, pulling changes from the test application.
* the developer pushes the changes to the production application from the local testing app when they finish the development and testing.

This process improves the maintenance and stability of the application because the development does not influence the production version of the application. In addition, all changes can be tracked in a `git` repository, providing a clear and organized development workflow.

## Prerequisites

To start the development of testing and production app versions, the following is needed:

* The production version of an app in Make. If you already have an app that is in use, use it as the production app.
* The cloned production version in a local workspace. [Clone the app to the local workspace](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/local-development-for-apps/clone-make-app-to-local-workspace), if you haven't done so already.
* The testing version of an app in Make. Create a new app in Make, with no content, that will function as the testing version of the app.
* Optional: use version control with Git. To properly track all changes in the local app, it is recommended to use a Git repository, for example, GitHub.

## Development flow

Below is a diagram explaining how a developer can develop testing and production app versions.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-5bb500a7b304ca6eb00463d41730e514bb9a65a4%2FFigJam%20basics%20(4).png?alt=media" alt="" width="188"><figcaption></figcaption></figure></div>

## Create a testing version of an app

First, [create a testing version of the Make app](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/local-development-for-apps/create-a-new-app-origin).

Once the origin for the testing app is successfully created, you need to deploy the current code from the app that already exists, which we can call "Production".

{% stepper %}
{% step %}
Right-click on the **makecomapp.json** file and select **Deploy to Make (beta)**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d99f91e7a016e8d9f04f424a5d4f62ed0228f83f%2FScreenshot%202024-05-09%20at%2021.47.11.png?alt=media" alt="" width="432"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Select the app origin that represents the testing app.
{% endstep %}

{% step %}
Press **Enter** to confirm the creation of the component.

If you don't want to create the component, click **Ignore permanently/do not map with remote** option.
{% endstep %}
{% endstepper %}

The app is deployed to Make.

## Develop the components in the testing app

Now, you can start developing new components or editing the current components in the Testing app in Make, and thoroughly test the app in the Scenario Builder.

## Pull changes from the testing app to the local app

Once you finish the development of new changes and components in the testing app, you can [push the changes to the local app](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/local-development-for-apps/pull-changes-from-make-app).

## Deploy the changes from the local app to the production app

To synchronize the changes made to the testing app with the production app, [follow these steps](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/local-development-for-apps/deploy-changes-from-local-app-to-make-app)
