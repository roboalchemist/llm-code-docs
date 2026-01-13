# Source: https://docs.snyk.io/integrations/jira-and-slack-integrations/jira-integration.md

# Jira integration

{% hint style="info" %}
For Snyk Infrastructure as Code, see [Jira Integration for IaC](https://docs.snyk.io/scan-with-snyk/snyk-iac/snyk-iac-integrations/jira-integration-for-iac).
{% endhint %}

## Set up your Jira integration

Snyk Jira integration allows you to manually raise Jira issues in the Snyk UI for vulnerabilities or license issues. The Jira integration also includes the API endpoints [Create jira issue](https://docs.snyk.io/snyk-api/reference/jira-v1#org-orgid-project-projectid-issue-issueid-jira-issue) and [List all jira issues](https://docs.snyk.io/snyk-api/reference/jira-v1#org-orgid-project-projectid-jira-issues).

{% hint style="info" %}
If your Jira instance is private, use [the Snyk Broker deployment method](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/jira-prerequisites-and-steps-to-install-and-configure-broker/jira-install-and-configure-using-docker).
{% endhint %}

## Prerequisites for Jira integration with Snyk

* Snyk supports Jira from version 5 to version 10.
* The following [Jira permissions](https://confluence.atlassian.com/adminjiraserver073/managing-project-permissions-861253293.html) are required: **Browse Projects** and **Create Issues.**

## How to set up your Jira integration

It is best practice to set up a new user in Jira for this integration, instead of using the credentials of an existing account.

Cloud-hosted Jira implementations require a username and API token authentication. Jira API tokens are generated in [Atlassian API tokens](https://id.atlassian.com/manage/api-tokens). Self-hosted implementations can also authenticate with a username and password.

Enter the Jira account credentials in the Snyk Web UI: **Organization Settings > Integrations** page: Base URL, Username/email, and API token.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-437372ae509ef78b397bbb49854db9409a9abe0d%2FJiraSettings_nonBroker.png?alt=media" alt="Jira settings"><figcaption><p>Jira settings</p></figcaption></figure>

After the details have been entered into the integration, press **Save and continue**.

{% hint style="info" %}
If the connection is not successful, check that the Base URL starts with exactly `https://` It must not have capitals or be http.
{% endhint %}

If the connection is successful, you will see the connection details in orange at the top of the page.

Fill in the following fields:

* Default Project (required) - Select a Jira Project from the list.
* Default Issue Type (required) - Select an issue type from the list. The list is populated from available issue types within your project.
* Ignored Fields (optional) - Specified fields will be excluded from the prompt users see when creating Jira issues within Snyk. For custom fields, use the [custom field id](https://confluence.atlassian.com/jirakb/find-my-custom-field-id-number-in-jira-744522503.html) in the format `customfield_XXXXXX`.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-2b57a4aa0988d19bbaa70db75e3c85fc34ab1419%2FJiraSettings.png?alt=media" alt=""><figcaption><p>A successful connection</p></figcaption></figure>

## Create a Jira issue

After you set up the Jira integration connection, open one of your Snyk Projects in the Snyk Web UI. A new button, **Create an issue**, appears at the bottom of each vulnerability and license issue card. This button allows you to create a Jira issue.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-395ff258c8b7c8d68deb580a19d277a391817259%2FJira%20-%20new%20button.png?alt=media" alt="Create an issue button"><figcaption><p>Create an issue button</p></figcaption></figure>

If the `Create an issue` button is not visible in the UI, ensure that `Group by none` is selected at the top of the Project's vulnerabilities table. This will then show the `Create an issue` button against the Project vulnerabilities.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6c832566faa61484b2dc45a70edfd3d253767a87%2Fimage%20(285).png?alt=media" alt=""><figcaption><p>Setting Group by none will show the Create Jira ticket button</p></figcaption></figure>

When you select **Create an issue**, a Jira issue creation form appears. This form includes the Snyk issue details, which are copied into the associated fields. You can review and edit this form before creating the issue.

Select the Jira project to which you want to send the issue. The fields in the example that follows are based on the fields that the specific Project has, so switching between Projects may show different options.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-27cd7c0668eb99772b4660b740c58d1194bf1cf9%2Fuuid-67202f8e-7f70-1e84-6044-f65ec36138b3-en.png?alt=media&#x26;token=ac3bdd37-24af-4840-8b4a-9d419a207666" alt="Crate a Jira issue"><figcaption><p>Crate a Jira issue</p></figcaption></figure>

After you create a Jira issue, the Jira key with a link is displayed on the issue card. If you are using the Jira API, you can generate multiple Jira issues for the same issue in Snyk.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-444166c38a1a601ad0f1f6f167b65a115536b54b%2FJira%20-%20Button%20with%20a%20link.png?alt=media" alt="Jira key on issue card"><figcaption><p>Jira key on issue card</p></figcaption></figure>

## Integrate with Jira using Snyk Broker

See [Set up Snyk Broker with Jira](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/jira-prerequisites-and-steps-to-install-and-configure-broker/jira-install-and-configure-using-docker).

## See also

[Snyk Security in Jira Cloud](https://docs.snyk.io/integrations/jira-and-slack-integrations/snyk-security-in-jira-cloud-integration)
