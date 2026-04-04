# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/google-cloud-integration/google-cloud-integration-web-ui/step-1-download-service-account-iac-template-web-ui.md

# Step 1: Download service account IaC template (Web UI)

Before you can create a Cloud Environment, you must download an infrastructure as code (IaC) template declaring a tightly-scoped Google service account that gives Snyk permission to scan the configuration of resources in your Google Project.

The template also enables a set of [Google service APIs](https://cloud.google.com/service-usage/docs/enabled-service) for your Google Cloud Project. This ensures that Snyk can use the necessary APIs to scan your Project's resources.

You will use this IaC template to provision the role in [Step 2: Create the Google service account](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/google-cloud-integration/google-cloud-integration-web-ui/step-2-create-the-google-service-account-web-ui).

## Download the IaC template

1. In the [Snyk Web UI](https://app.snyk.io/), navigate to **Integrations** > **Cloud platforms**.
2. Select **Google Cloud**.
3. In the **Add Google Cloud Environment** modal, select the **Terraform** button to download a `snyk-permissions-google.tf` file:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-add0f578edd744db13b510458991b0a2cd1252b0%2FBildschirmfoto%202023-07-18%20um%2012.16.54.png?alt=media" alt=""><figcaption><p>The Add Google Cloud Environment modal</p></figcaption></figure>

You can now proceed to [Step 2: Create the Google service account.](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/google-cloud-integration/google-cloud-integration-web-ui/step-2-create-the-google-service-account-web-ui)

{% hint style="info" %}
You can also add a cloud environment from **Settings** > **Cloud environments**. See [View Environments, Add a Cloud environment](https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/manage-cloud-environments/view-add-and-remove-environments).
{% endhint %}
