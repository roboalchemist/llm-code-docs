# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/azure-devops-artifact-feed-private-packages.md

# Azure DevOps Artifact Feed - Private Packages

For node project, the connection with an Azure DevOps Artifact Feed can be configured by providing an `.npmrc` file in the Aikido Autofix configuration

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on "Connect Registry", an select "NPM"

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FJv1x3YMsHLEz7bOVgVVr%2Fimage.png?alt=media&#x26;token=c92ea5f3-20d6-4267-9509-3ade6d3cfc91" alt=""><figcaption></figcaption></figure>

1. Fill in the `.nmprc` file like described below

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fq8UBDnB1jzgWRz4DV0HS%2Fimage.png?alt=media&#x26;token=861a4aba-fd5b-4db6-bc52-9171d4cc8420" alt=""><figcaption></figcaption></figure>

1. Click "Connect Registry" to save the configuration.

### Obtaining the .npmrc for Azure DevOps

1. In Azure Devops, navigate to the "Artifacts" page of the project, click on "Connect to Feed" button and select "NPM" from the list
2. You will now land on page describing how to setup the project, select "Other" From the project setup tabs, you should see a page with setup instructions similar to this. Follow the steps and paste the `.npmrc` content into Aikido.

![Azure npm registry setup instructions with authentication and access token configuration steps.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f28f1a8c4c8d0fcd33b598a02636306a1907088f%2Fnpm-private-packages_96a38411-3187-43bf-84b0-02d5ec4785b8.png?alt=media)
