# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/manage-cloud-environments/view-add-and-remove-environments.md

# View, add, and remove environments

To view all Snyk environments in an Organization, navigate to your Organization **Settings** > **Cloud environments**.

The cloud environments table displays the following information for each environment:

* Name
* Native ID (for example, AWS account ID, Google project ID, Azure subscription, CLI)
* Kind (for example, AWS, Google, Azure, CLI)
* Date onboarded

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-48bd8cb520d036ac8b97dedb169ee54b2d05e160%2Fsnyk-cloud-environments-page.png?alt=media" alt=""><figcaption><p>The Snyk environments page in the Snyk Web UI</p></figcaption></figure>

## Add a cloud environment

To add a cloud environment, select the **Add environment** drop-down and select the cloud provider. Follow the steps in [AWS Integration: Web UI](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-web-ui), [Google Cloud Integration: Web UI](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/google-cloud-integration/google-cloud-integration-web-ui), or [Azure Integration: Web UI](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/azure-integration-for-cloud-configurations/azure-integration-web-ui) to create the environment.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-297009cf98fc9e5c712166777033ac2ac6f623d7%2Fsnyk-cloud-environments-page-add-env.png?alt=media" alt=""><figcaption></figcaption></figure>

You can also add an environment using the Snyk API:

* [AWS Integration: API](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-api)
* [Google Cloud Integration: API](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/google-cloud-integration/google-cloud-integration-api)
* [Azure Integration: API](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/azure-integration-for-cloud-configurations/azure-integration-api)

## Remove a cloud environment

To remove a cloud environment:

1. In the **Actions** column, select the three dots for the environment you want to remove.
2. Select **Remove**.
3. In the confirmation modal, select **Yes, remove**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-acb39eee067fb5d8a6cfe4cdb983ae73977e39f8%2Fsnyk-cloud-remove-env-ui.png?alt=media" alt=""><figcaption></figcaption></figure>

You can also remove an environment using the [Snyk API](https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/remove-a-cloud-environment#api).
