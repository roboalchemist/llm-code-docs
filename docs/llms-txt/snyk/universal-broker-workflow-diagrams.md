# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/universal-broker/using-the-api-to-set-up-universal-broker/universal-broker-workflow-diagrams.md

# Universal Broker workflow diagrams

The following workflow diagrams illustrate the steps that are implemented in the `snyk broker config` tool when you use the commands to automate. The same workflows are implemented when you use the API.

## Create a deployment workflow

You start the workflow and choose to use an existing deployment or create a new one. The deployment is then created.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b4e3280fa59eadd00a239b0cd1493b5a285c1e61%2FCreate-deployment-workflow.png?alt=media" alt="" width="375"><figcaption><p>Use or create a new deployment</p></figcaption></figure>

## Create connection workflow

You start the workflow and select a deployment. You create a new connection for that deployment, selecting a connection type and entering the required parameters. You can use an existing or create a new credentials reference. The connection is then created.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1df995378c231b580d979a5a33b2ba7b25e5fe5a%2FCreate-connecton-workflow.png?alt=media" alt="" width="563"><figcaption><p>Create a connection</p></figcaption></figure>

## Integrate connection workflow

You start the workflow and select a deployment. You select an existing connection to integrate with an Organization and enter the Org ID for that Organization. The connection is then integrated with the Organization by Org ID. The connection is ready.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-13918e24eb8fd20b7c1c46ec94e6726735ae37b8%2FIntegrate-connection-workflow.png?alt=media" alt="" width="375"><figcaption><p>Integrate a connection with an Organizaton</p></figcaption></figure>
