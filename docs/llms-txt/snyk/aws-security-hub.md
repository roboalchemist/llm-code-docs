# Source: https://docs.snyk.io/integrations/event-forwarding/aws-security-hub.md

# AWS Security Hub

The [AWS Security Hub](https://aws.amazon.com/security-hub/) integration sends Snyk issues to Security Hub, allowing you to centralize your security reporting, build custom alerting, and trigger automation. After it is configured, the integration automatically uploads Snyk issues to Security Hub as security findings. When issues are updated or new remediations become available, the corresponding Security Hub findings are automatically updated.

There are two steps required to configure the integration:

1. Configure Security Hub to accept findings from Snyk in the Security Hub console.
2. Configure Snyk to send findings to Security Hub in the Snyk dashboard.

## Configuring Security Hub to accept Snyk findings

Go the the Security Hub console for the AWS account and region you want to receive Snyk findings. Navigate to the **Integrations** section and search for **Snyk**. On the **Snyk** integration tile, click **Accept findings** and follow the prompts.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-9b4dfd9bfe6d5051074f281700f9ba6d0ef081ca%2Fintegrations-eventforwarding-securityhub-aws-acceptfindings.png?alt=media" alt="Search for Snyk integration"><figcaption><p>Search for Snyk integration</p></figcaption></figure>

After this step is done, you can continue setting up the integration in the Snyk dashboard.

## Configuring Snyk to send findings to Security Hub

Navigate to [the Snyk integrations page](https://app.snyk.io/integrations) and search for **Security Hub** or navigate to the **Cloud events** section. Click on the **Security Hub** tile to start creating a new integration.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-794b50990aee84c7a05ae09914d54bc8739b3609%2Fintegrations-eventforwarding-eventbridge-tile.png?alt=media" alt="Create new Security Hub integration"><figcaption><p>Create new Security Hub integration</p></figcaption></figure>

Enter a **name** for the integration, along with the **AWS Account ID** and **AWS Region** where you enabled the Snyk partner integration in step one.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-635d164f1f06c9522f9e80d7f14769c277e1a919%2Fintegratinos-eventforwarding-securityhub-dialog.png?alt=media" alt="Enter integration details"><figcaption><p>Enter integration details</p></figcaption></figure>

After this step is complete, Snyk begins sending new issue events to Security Hub.

{% hint style="info" %}
Issues on existing Projects will not be sent to Security Hub unless those issues are updated. To backfill issues from existing projects, you can delete and re-import them.
{% endhint %}

## Snyk App authorization

If this is the first time you have set up an AWS Security Hub integration for your Organization, you will be prompted to complete the Snyk App authorization flow.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e196210936998bd407164c4d2293df32848c63b7%2Fintegrations-eventforwarding-securityhub-auth.png?alt=media" alt="Snyk App authorization" width="375"><figcaption><p>Snyk App authorization</p></figcaption></figure>

After completing the authorization flow you will be redirected to the settings page for the integration.

## Managing and deleting a Security Hub integration

Navigate to the [Security Hub integration settings page](https://app.snyk.io/manage/integrations/aws-securityhub) in the Snyk dashboard and click on the name of the integration you want to manage.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ae4a9ef2cf7a9a63cfa6ed8b508aaecf3294e04c%2Fintegrations_awb_security_hub.png?alt=media" alt="Select integration to manage"><figcaption><p>Select integration to manage</p></figcaption></figure>

Clicking on the name of an integration opens the settings page for that integration, where you can view and update configuration information for the integration.

To delete an integration, scroll to the bottom of the integration settings page and click the **Remove integration** button.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ae43b9c7f3138018944944613b381e34041fbae3%2Fintegrations-eventforwarding-securityhub-delete.png?alt=media" alt="Remove integration"><figcaption><p>Remove integration</p></figcaption></figure>

After the integration is deleted, Snyk will no longer send issues to Security Hub. Issues that have already been sent to Security Hub will remain there until they are archived.
