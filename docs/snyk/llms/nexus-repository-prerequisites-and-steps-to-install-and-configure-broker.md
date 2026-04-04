# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/nexus-repository-prerequisites-and-steps-to-install-and-configure-broker.md

# Nexus Repository - prerequisites and steps to install and configure Broker

{% hint style="info" %}
**Feature availability**

Integration with Nexus Repository Manager is available only with Enterprise plans. For more information, see [plans and pricing](https://snyk.io/plans/).
{% endhint %}

Before installing, review the general instructions for the installation method you plan to use, [Helm](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/install-and-configure-broker-using-helm) or [Docker](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/install-and-configure-broker-using-docker).

Before installing the Snyk Nexus Repository Broker, ask your Snyk account team to provide you with a Broker token or generate it from the Snyk Web UI.

You must have Docker or a way to run Docker Linux containers.\
Some Docker deployments for Windows run only Windows containers. Ensure that your deployment is capable of running Linux containers.

For convenience, instructions to obtain or generate the Broker token follow. When you are done, continue with the steps to install using [Docker](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/nexus-repository-prerequisites-and-steps-to-install-and-configure-broker/nexus-repository-install-and-configure-using-docker) or [Helm](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/nexus-repository-prerequisites-and-steps-to-install-and-configure-broker/nexus-repository-install-and-configure-using-helm).

## Obtain Broker token for Nexus integration

1. Go to **Settings** > **Integrations** > **Package Repositories** > **Nexus**
2. Verify that you see the screen to configure Nexus.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fa0021d88a8a73c478de36114cb294ad2275c5b0%2FScreenshot%202022-07-15%20at%2015.15.11.png?alt=media" alt="Configure Nexus"><figcaption><p>Configure Nexus</p></figcaption></figure>

{% hint style="info" %}
If you do not see the Snyk Broker switch, you do not have the necessary permissions and can only add a publicly accessible instance.

Submit a request to [Snyk Support](https://support.snyk.io) if you want to add a private registry.
{% endhint %}

When you have permissions to add a private registry, continue with the instructions to [generate a Broker token from the Web UI](#generate-a-broker-token-from-the-web-ui).

## Generate a Broker token from the Web UI

1. In the Nexus integration settings, move the Snyk Broker on/off switch to **on** to display a form for generating a Broker token.
2. Select **Generate and Save.**
3. Copy the token that was generated to use when you set up the Broker Client.
