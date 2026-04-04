# Source: https://docs.fiddler.ai/reference/settings.md

# Administration

## Overview

The Settings page provides centralized management for your organization's configuration, user access, and integrations. Access the **Settings** page from the left navigation bar in the Fiddler UI.

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-07d2109bb085f78bc474ffc712d5b6ca2b3ee76a%2Fsettings-homepage%20(1).png?alt=media" alt="Fiddler home page showing the user menu open and highlighting the Settings link."><figcaption></figcaption></figure>

## Settings Tabs

The Settings page is organized into the following tabs:

* **General** - Organization information and user details
* **Access** - User and team management
* **Credentials** - Personal access token management
* **LLM Gateway** - LLM provider and API credential management
* **Email Configuration** - Email notification settings
* **PagerDuty Integration** - PagerDuty alert configuration
* **Webhook Integration** - Webhook service management

## General

The **General** tab displays your organization's configuration and current user information.

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-1b0535067c0945e0eb098b107dfa38d47f37c7c7%2Fsettings-example-page%20(1).png?alt=media" alt="General tab of the Settings page."><figcaption></figcaption></figure>

### Organization Information

* **Organization Name** - Your organization's display name in Fiddler
* **Organization ID** - Unique identifier for your organization
* **Version** - Current Fiddler platform version

### User Information

* **User Name** - Your display name in the system
* **Email** - Email address associated with your account

## Access

The **Access** tab provides centralized management for users and teams within your organization.

### Users

The **Users** sub-tab displays all users who are members of your organization.

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-692dee24d4562fab40da0cf45ce9cd0200cfb4d7%2Fsettings-user-tab%20(1).png?alt=media" alt="Users sub-tab of the Access tab on the Settings page showing a list of users."><figcaption></figcaption></figure>

This view shows:

* User names and email addresses
* Organization roles (Org Admin or Org Member)
* Account status (Active/Inactive)
* Last login information

> **Note**
>
> User invitations are managed through the Fiddler AuthN console:
>
> * Email authentication users must be invited by AuthN Org Owners or Org User Managers
> * SSO users are automatically created upon first login to Fiddler

### Teams

The **Teams** sub-tab displays all teams defined within your organization. Teams provide a way to organize users and manage project-level access controls.

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-46b9d06c49442081f0612ad6a03844aa1757fcc8%2Fsettings-teams-tab%20(1).png?alt=media" alt="Teams sub-tab of the Access tab on the Settings page showing a list of teams"><figcaption></figcaption></figure>

#### Creating Teams

Create a new team by clicking the plus (**`+`**) icon in the top-right corner.

> **Important**
>
> Only users with the Org Admin role can create teams. The plus (**`+`**) icon will not be visible for Org Members.

When creating a team:

1. Enter a unique team name
   1. Team names may not include spaces, but mixed-case alphanumeric characters are valid
2. Add team members from existing users
3. Assign appropriate project permissions
4. Click **Create** to save the team

#### Team Synchronization

If your organization uses SSO with group synchronization enabled, teams can be automatically created and managed based on your identity provider groups. See [Mapping Identity Provider Groups to Fiddler Teams](https://docs.fiddler.ai/reference/access-control/mapping-ad-groups-to-fiddler-teams) for configuration details.

## Credentials

The **Credentials** tab manages personal access tokens used for programmatic access to Fiddler through the Fiddler Python client, Fiddler SDKs, and REST APIs.

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-6384e969c50a587df40fe0adeacae426eb551b73%2Fsettings-credentials-tab%20(1).png?alt=media" alt="Credentials tab showing personal access tokens with Create Key button highlighted."><figcaption></figcaption></figure>

### Creating Personal Access Tokens

Both Org Admins and Org Members can create personal access tokens:

1. Click **Create Key** to generate a new token
2. Once you have a token, the Create Key will be removed
3. To generate a new token, delete your current token and the Create Key will return
4. Use the token for authentication in the Fiddler Python client, Fiddler SDKs, and REST APIs\`

### Token Management

* Each user can create multiple personal access tokens
* Tokens should be rotated regularly for security
* Revoke unused or compromised tokens immediately
* Personal access tokens inherit the permissions of the user who created them

> **Security Best Practice**
>
> Treat personal access tokens like passwords. Never share them or commit them to version control systems.

## LLM Gateway

The **LLM Gateway** tab allows you to configure and manage LLM provider credentials for AI-powered features throughout the Fiddler platform.

Configure LLM providers to enable:

* **Custom Evaluators** - Use your preferred LLM to evaluate model outputs
* **Content Analysis** - Assess response quality and monitor trust metrics

Supported providers include OpenAI, Anthropic, Gemini, and Fiddler. You can add multiple API credentials per provider for redundancy, load balancing, and key rotation.

For detailed configuration instructions, see [LLM Gateway Configuration](https://docs.fiddler.ai/reference/settings/llm-gateway).

## Email Configuration

The **Email Configuration** tab manages the email provider for your organization.

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-6b0a93b5a6fdabf6a28f71de9b0d53fc73429b78%2Fsettings-email-configuration-tab%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

Configure:

* Selecting SES or SMTP for email delivery
* Fiddler Cloud customers leverage AWS SES
* You may choose to use your own SMTP server by entering your own SMTP connection and credentials details

## PagerDuty Integration

The **PagerDuty Integration** tab enables configuration of PagerDuty services for alert escalation.

Setup includes:

* PagerDuty service integration keys
* Severity mapping for alerts
* Escalation policy configuration
* Test alert functionality

## Webhook Integration

The **Webhook Integration** tab manages webhook configurations for connecting Fiddler alerts to your notification and communication platforms.

### Supported Webhook Types

Fiddler supports three webhook provider types:

* **Slack** - Direct integration with Slack channels
* **Microsoft Teams** - Native Teams channel integration
* **Other** - Custom webhook endpoints for any platform

### Creating a Webhook

Click the plus (**`+`**) icon to configure a new webhook:

![Create Webhook Service modal dialog](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-7a649332335e58620b933ede8d669d9386171f2d%2Fa0b33c4-screenshot-2023-10-10-at-124631-pm.png?alt=media)

#### Slack Webhook Configuration

1. Enter a unique name in the **Service Name** field
2. Select **Slack** from the **Provider** dropdown
3. Enter your Slack webhook URL (format: `https://hooks.slack.com/services/...`)
4. Click **Test** to verify the connection
5. Click **Create** once the test succeeds

> **Reference**
>
> See [Slack's webhook documentation](https://api.slack.com/messaging/webhooks) for creating webhook URLs.

#### Microsoft Teams Webhook Configuration

1. Enter a unique name in the **Service Name** field
2. Select **MS Teams** from the **Provider** dropdown
3. Enter your Teams webhook URL provided by your administrator
4. Click **Test** to verify the connection
5. Click **Create** once the test succeeds

> **Reference**
>
> See [Microsoft Teams webhook documentation](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet#create-an-incoming-webhook) for setup instructions.

#### Custom Webhook Configuration

1. Enter a unique name in the **Service Name** field
2. Select **Other** from the **Provider** dropdown
3. Enter your platform's webhook URL
4. Click **Test** to verify the endpoint
5. Click **Create** once the test succeeds

### Managing Webhooks

Edit or delete existing webhooks using the menu (**...**) icon for each webhook:

1. Select the webhook's menu icon
2. Choose **Edit Webhook** to modify configuration
3. Choose **Delete Webhook** to remove the webhook

> **Important**
>
> You cannot delete webhooks that are currently linked to active alerts. Remove the webhook from all alerts before deletion.

## Access Requirements

Different settings require specific permissions:

| Setting                       | Org Admin | Org Member |
| ----------------------------- | --------- | ---------- |
| View General tab              | ✓         | ✓          |
| View Access > Users           | ✓         | ✓          |
| View Access > Teams           | ✓         | ✓          |
| Create/Edit Teams             | ✓         | ✗          |
| Create Personal Access Tokens | ✓         | ✓          |
| Configure LLM Gateway         | ✓         | ✗          |
| Configure Email Settings      | ✓         | ✗          |
| Configure PagerDuty           | ✓         | ✗          |
| Create/Edit Webhooks          | ✓         | ✗          |

## Related Documentation

* [Role-Based Access Control](https://docs.fiddler.ai/reference/access-control/role-based-access) - Understanding user roles and permissions
* [Single Sign-On Configuration](https://docs.fiddler.ai/reference/access-control/sso-authentication-guide) - Setting up SSO authentication
* [Inviting Users](https://docs.fiddler.ai/access-control/email-login#adding-users-to-fiddler) - Adding users through the AuthN console
* [Alert Configuration](https://docs.fiddler.ai/observability/platform/alerts-platform) - Using webhooks and integrations for alerts

***

:question: Questions? [Talk](https://www.fiddler.ai/contact-sales) to a product expert or [request](https://www.fiddler.ai/demo) a demo.

:bulb: Need help? Contact us at <support@fiddler.ai>.
