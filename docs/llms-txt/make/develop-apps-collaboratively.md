# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/develop-apps-collaboratively.md

# Develop apps collaboratively

Collaborative development is facilitated by the Git for apps feature in the VS Code extension. The supported operations are documented in this [section](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/local-development-for-apps).

## Prerequisites

To start collaborative development, make sure that you have set up the [testing and production app versions](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/manage-testing-and-production-app-versions).

Each collaborating developer should have their testing app in Make, connected to the local app from the Git repository.

## Roles

* **Owner of the production app**: Every app in Make can be owned by a single Make account. The owner of the production app manages the deployment of the new local app version to the Make app.
* **Developers of the testing apps**: Each developer manages their own testing app in Make, which is connected to the local app from the Git repository.

## Collaborative development flow

Below is a diagram explaining how developers can collaborate on app development.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-21e24864ce9a9d4c98d103c49b3c6083bb9f112a%2FFigJam%20basics%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
