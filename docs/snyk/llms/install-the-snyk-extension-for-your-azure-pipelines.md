# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/azure-pipelines-integration/install-the-snyk-extension-for-your-azure-pipelines.md

# Install the Snyk extension for your Azure pipelines

To start using the Snyk task as part of your pipeline build, from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Snyk.snyk-security-scan), install the extension into your Azure DevOps instance for your Organization.

## **Prerequisites for installing Snyk extension for Azure pipelines**

* Create a Snyk account at [https://snyk.io/](https://snyk.io).
* Ensure you are an owner or administrator of this account.

## **Step for installing the Snyk extension for Azure pipelines**

1. Log in to your Snyk account.
2. Token:
   1. For **free plans**, navigate to your **General Account Settings** and find, copy, and save your personal API token.
   2. For **paid plans**, navigate to the Organization where you want to integrate; then navigate to **Settings** to create a new service account token. Copy and save the new service account token.
3. Access your Azure DevOps account and navigate to the **Extensions > Browse marketplace.**
4. Search for the **Snyk Security Scan** extension and click **Get it free**.
5. Create a new **Service Connection** in your Project using **Project Settings** > **Pipelines** > **Service Connections**.
6. Select the **Snyk Authentication** service connection:
   1. In the Snyk Authentication service connection form, enter the **Snyk API Token or Snyk PAT**.
   2. Click **Save**, ensuring the new service connection appears in your list of service connections.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3b65137b95f6bd6e2e22a711a096c7d9b4b1a24f%2Fap_-_search.jpg?alt=media&#x26;token=b5f58de1-a58c-432f-8af0-6f0323e37df3" alt="Create your first service connection"><figcaption><p>Create your first service connection</p></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-56cabd77f4727460a9a8bdbefc7320a0f2917d7b%2FAzure-authentication-connection-setup.png?alt=media" alt="New Snyk authentication service connection" width="389"><figcaption><p>New Snyk authentication service connection</p></figcaption></figure>

{% hint style="info" %}
If you are hosted in a region other than `SNYK-US-01`, see the section [Regional API endpoints](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/azure-pipelines-integration/regional-api-endpoints).
{% endhint %}
