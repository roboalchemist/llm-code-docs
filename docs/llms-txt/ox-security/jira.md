# Source: https://docs.ox.security/ticketing-and-messaging/ticket-management/jira.md

# Jira

Jira is a powerful project management and issue-tracking tool widely used by development teams to plan, track, and manage software projects.

It provides robust workflows, automation, and integrations that streamline collaboration between teams.

Integrating OX Security with Jira enhances security visibility within your existing development workflows.

This integration allows security issues and vulnerabilities detected by OX to be automatically logged as Jira issues, ensuring they are tracked, prioritized, and resolved alongside other development tasks.

By seamlessly embedding security insights into Jira, teams can maintain a proactive approach to risk management while minimizing workflow disruptions.

## Jira Cloud and Jira On-Prem

OX supports integrating with both JIRA Cloud and JIRA On-Prem for ticketing automation.

When integrating OX with JIRA On-Prem, you can automatically create and update tickets based on issues detected in your environment. Unlike JIRA Cloud, JIRA On-Prem requires additional configuration steps, particularly around the URL format and authentication method.

When connecting OX to a JIRA On-Prem instance, you need to decide what authentication method to use for the connection. You define the method by defining the URL format, as follows:

* Token-based authentication (this method is recommended, as it is more secure)

```
https://<domain>/release/v${version}/api/2/bearer
```

* Basic username-password authentication

```
https://<domain>/release/v${version}/api/2
```

The integration process includes the following:

1. [Prerequisites](#prerequisites)
2. Get Jira tokens: for [Jira on Cloud](#getting-jira-cloud-token), for [Jira On-Prem](#getting-jira-on-prem-token)

* Connect to: [Jira on Cloud](#connecting-to-jira-on-the-cloud), [Jira On-Prem](#connecting-to-jira-on-prem)
* [Add Jira tickets](#adding-jira-tickets)

## Prerequisites

A Jira account.

## Getting Jira Cloud token

1. Log in to your Atlassian account.
2. From your profile picture in the top-right corner, select **Profile**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6b5617b62a8f5c3ef43eeca6f0ee6e6d7d682e80%2FJira1.png?alt=media" alt=""><figcaption></figcaption></figure>

1. In your profile settings page, select **Manage your account** and then select **Security**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07fa5acb0c5831162372b106ede180093a234af7%2FJira2.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Scroll down to the **API Tokens** section, select **Create and manage API tokens**, and then select **Create API token.**

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-837b4750b225ff1519b0c63bad737531a5825621%2FJira3.png?alt=media" alt=""><figcaption></figcaption></figure>

1. In the **Create API token** dialog, define the following.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ca9a43b8418c216d216c399590a5053eb03a5a7b%2FJira4.png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter      | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| **Name**       | A significant name that makes it easy to identify the purpose of the token. |
| **Expires on** | Set the expiration date as far as possible.                                 |

1. Select **Create**. The dialog with the token appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8d205fb97fbb61b35b868293c32448b318474916%2FJira5%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. Copy the token and store it in a safe location.\
   After closing this dialog you cannot see it again.

## Getting Jira On-Prem token

1. Log in to your Atlassian account.
2. Click your profile avatar and select **Profile**.
3. Navigate to **Personal Access Tokens**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-cc4789c05eb7c631bdbcef1fa0a84523d50013ef%2Fonprem_jira_personal%20access_token.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Click **Create token**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-61b8997dfd4858f8e2c498512e3f2a236d717b03%2Fonprem_jira_create_token.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Provide a name and expiration period, then click **Create**.
2. Copy the token and store it in a safe location.\
   After closing this dialog, you cannot see it again.

   > **Note:** This process may differ slightly based on your JIRA On-Prem version.

## Connecting to Jira on the Cloud

1. In the **OX app**, go to **Connectors** and search for Jira.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c6f44ee1247382415c721a60e695720924006a62%2FJira_connect_icon.png?alt=media" alt="" width="195"><figcaption></figcaption></figure>

1. Select **Jira** and set the following parameters in the **Configure your Jira credentials** dialog.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6cff819917ba7d4cc6dd55fb95203f035b9fe4fa%2FJira_connect.png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter         | Description                                         |
| ----------------- | --------------------------------------------------- |
| **Jira Host URL** | Add your organization account URL.                  |
| **User Name**     | Type the email address used as your Jira user name. |
| **Token Name**    | Paste the Jira token you have created.              |

1. Select **CONNECT**. The success message appears.

## Connecting to Jira On-Prem

1. In the **OX app**, go to **Connectors** and search for Jira.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c6f44ee1247382415c721a60e695720924006a62%2FJira_connect_icon.png?alt=media" alt="" width="195"><figcaption></figcaption></figure>

1. Select **Jira** and set the following parameters in the **Configure your Jira credentials** dialog.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2671a09bb7aa0c562b598f90c346efd50ee6e76c%2FJira_on_prem_connect.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

<table><thead><tr><th width="188.3333740234375">Parameter</th><th width="305.9998779296875">Description</th></tr></thead><tbody><tr><td><strong>Jira Host URL</strong></td><td><p>Add the URL format that defines the <a href="#jira-cloud-and-jira-on-prem">authentication method for the Jira on-prem</a> connection, where:<br></p><ul><li><code>&#x3C;domain></code> : The base domain of the JIRA server</li><li><code>&#x3C;version></code> : The JIRA version</li></ul></td></tr><tr><td><strong>User Name</strong></td><td>Type your JIRA username.</td></tr><tr><td><strong>Token Name</strong></td><td>Based on the authentication method you are using, paste the Jira token you have created, or add your actual JIRA password.</td></tr></tbody></table>

1. Select **CONNECT**. The success message appears.

## Adding Jira tickets

After establishing the connection with Jira, you can add Jira tickets for a variety of tasks and issues in OX using one of the following methods:

* Adding a new ticket to an issue, or bulk of issues.
* Adding a new ticket as a scheduled task using workflows.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9eb60a075f5d9855d44556de36a9a4bbda79cf52%2FWF_Jira_ticket.png?alt=media" alt="" width="204"><figcaption></figcaption></figure>

**To add a new Jira ticket in OX:**

1. In the Issues page, identify and select the issue for which you want to add a new ticket in Jira.
2. Select the Jira icon.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4eb8c5280041c629e4d38764f78ac7b20534a7c6%2FJira_icon_issue.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Set the ticket mandatory parameters in the **Create Jira Issue** dialog.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-cb1e873a2858331d9767cf9ffe35a59bf77b6cf6%2FJira_create_issue.png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter      | Description                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------- |
| **Summary**    | The title of the ticket that describes the problem/issue, as it appears in the OX Issues page. |
| **Project**    | The name of the project, as it's defined in Jira.                                              |
| **Issue Type** | Select the issue type.                                                                         |

1. (Optional)Set the other Jira ticket parameters.
2. Select **SUBMIT**.

The new ticket appears in Jira.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1f02a7c71ef197d950390c3a1cdfa4050a41e9e6%2FJira_new_ticket.png?alt=media" alt=""><figcaption></figcaption></figure>
