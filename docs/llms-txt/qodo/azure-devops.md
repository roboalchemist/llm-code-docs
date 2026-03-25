# Source: https://docs.qodo.ai/qodo-documentation/code-review/integrations/ticketing-integrations/azure-devops.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/install/azure-devops.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/integrations/ticketing-integrations/azure-devops.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation/azure-devops.md

# Azure DevOps

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

This page describes how to integrate Qodo and Azure DevOps.

### Before you start

**Qodo is built to work natively with Azure DevOps.** \
\
This integration is designed for Microsoft customers, using Microsoft Entra ID
\
(formerly Azure Active Directory) to authenticate the Qodo application and authorize
\
access to Azure DevOps APIs. It relies on Azure DevOps service hooks and native pull
\
request workflows. Qodo uses ticket information already associated with pull requests,
\
including Azure Boards work items and integrated external ticket systems, to provide
\
additional context and perform ticket compliance checks without requiring separate tools
\
or workflows.

You can configure Qodo for a single repository or project, or expand it across multiple
\
projects within your Azure DevOps organization. Repository-level configuration provides
\
more granular control, while project-level configuration allows you to select which
\
repositories are included.&#x20;

Setup typically takes around 20 minutes and includes creating a Microsoft Entra ID
\
application, configuring authentication, and setting up webhooks.

Once configured, Qodo will monitor pull requests and publish outputs such as reviews, descriptions, and improvement suggestions directly to your Azure DevOps pull requests.

### Prerequisites

To install Qodo on Azure DevOps you need:

* A single-tenant Qodo environment configured for Azure DevOps, including the Qodo webhook
  \
  endpoint, provided by Qodo. Azure connection details (tenant ID, client ID, and client secret) are generated as part of the Microsoft Entra ID application registration during setup.\
  Multi-tenant customers should contact Qodo to discuss the appropriate configuration.
* Permissions to create an app registration in Microsoft Entra ID.
* Permissions to create users in Microsoft Entra ID and add users to the Azure DevOps
  \
  organization (Microsoft Entra ID User Administrator and Azure DevOps Organization Owner),
  \
  and access to the Azure DevOps projects that will be integrated with Qodo.

### Step 1: Create an application registration \[Microsoft Azure portal]

1. Sign in to the [Microsoft Azure portal.](https://portal.azure.com/)
2. Use the search bar to navigate to **App registrations**.
3. Click **New registration** and enter the following:
   * **Application Name**: Qodo
   * **Supported account types:** Select **Accounts in any organizational directory (Any Microsoft Entra ID tenant – Multitenant)**
   * **Application Logo**:&#x20;

     ```
     https://www.qodo.ai/wp-content/uploads/2025/03/qodo-logo.svg
     ```
4. Navigate to **Manage** → **Authentication** → **Add Redirect URL**&#x20;
   1. In the popup, select **Web Applications** → **Web**
   2. Enter the following callback URL: `https://register.oauth.app.azure.merge.qodo.ai/oauth/callback`
   3. Click **Configure.** &#x20;
5. Navigate to **Manage** → **Certificates & secrets** → **New client secret**&#x20;

   1. In the popup, add a description and select an expiration.&#x20;
   2. Click **Add** to generate a client secret and save the Value. This will not be visible later.&#x20;

   <figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F06QeJdMnbaTGmJAUztAB%2Fimage.png?alt=media&#x26;token=f52a1d6f-6802-4ff6-b720-e1932d05e63f" alt=""><figcaption></figcaption></figure>
6. Navigate to **Manage** → **API permissions** → **Add a permission**
   1. In the popup, select the Azure DevOps card.
   2. Add the Azure DevOps permission (`user_impersonation`), and grant admin consent for the directory.
   3. Click **Add permissions.**

The **Overview** page displays all the relevant information for the following steps. Copy and save Application (client) ID and Directory (tenant) ID.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FlcC4VXy86u8D5DYRVen4%2Fimage.png?alt=media&#x26;token=1db9b6b7-82ff-4eed-8fb6-9535d31b1bcf" alt=""><figcaption></figcaption></figure>

### Step 2: Create a new user \[Microsoft Azure portal]

1. In the Microsoft Azure portal, create a new user named `Qodo` that will be used as a bot (service) account for Qodo.
   1. Navigate to **Manage** → **Users** → **New user**
   2. In the popup, enter the user details and assign it the *Cloud Application Administrator* role.

### Step 3: Create a service account \[Azure DevOps]

{% hint style="info" %}

The Microsoft Entra ID user that authenticates and creates the OAuth token must be the same user
\
(same email / UPN) that is added to the Azure DevOps organization. If these do not match,
\
the integration will not work.\
\
When using non-Azure domains (for example, Gmail), Azure may automatically create an
\
`@onmicrosoft.com` user. In this case, ensure that the same identity (email / UPN) is used
\
consistently in both Microsoft Entra ID and Azure DevOps.
{% endhint %}

1. Sign in to the Azure DevOps portal (for example, `https://dev.azure.com/<YOUR_ORGANIZATION>`).
2. Navigate to **Organization settings → Users**, and add the `Qodo` user created in the previous step to the Azure DevOps organization.
3. Assign the user Access Level: **Basic** and add it to the **Project Administrators** group for the project the bot should access.

### Step 4: Register the application with Qodo \[Qodo]

This step is performed using a Qodo-hosted registration page to connect your Microsoft Entra ID application to your Qodo environment.

1. Open an incognito or private browser window and verify that no Microsoft account is currently signed in. This step is important to ensure you authenticate using the correct service (bot) account.
2. Sign in to Microsoft Entra ID using the dedicated service account created in Step 2.
3. In the same browser window, navigate to: `https://register.oauth.app.azure.merge.qodo.ai/`
4. In the registration form, provide the following details from the app registration in the Micrososft Azure portal:
   * **OAuth Application ID** from the **Overview** tab (Application (client) ID)
   * **OAuth Application secret** (use the secret **value**, not the secret ID)
   * **Entra Tenant ID** where the application was created (from the **Overview** tab, Directory (tenant) ID)
5. Submit the form.

After successful registration, a new window will open displaying a **Webhook Secret Token**. Save this value securely—you will use it when configuring Azure DevOps webhooks in Step 5.

### Step 5: Set up webhooks \[Azure DevOps]

Webhooks are required to enable two-way communication, allowing Qodo to receive pull request events from Azure DevOps.

{% hint style="info" %}
A single-tenant Qodo environment is required.
{% endhint %}

1. Navigate to the Azure DevOps project where you want to install Qodo.
2. Open **Project settings → Service hooks**.
3. Create a new **Web Hook** subscription.
4. Configure the web hook to trigger on the relevant pull request events, such as:
   * PR Created
   * PR Updated
   * PR Commented&#x20;
   * PR Merged
5. Set the URL to your single-tenant Qodo endpoint (provided by your Qodo contact).\
   The webhook URL should follow this pattern: `qodo-merge.<your-company-name>.st.qodo.ai`
6. Add the following HTTP header:&#x20;

   ```
   X-Webhook-Secret: <webhook secret token>
   ```
7. Click **Test** to verify that the webhook endpoint is reachable and correctly configured.
8. Click **Finish** to create the webhook.

Once configured, the webhook should appear in the Service Hooks list similar to the example below.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FExHzKieODpAMg0nLAVva%2FADO.png?alt=media&#x26;token=31feb490-ad2c-44a5-9bb3-23182c01d468" alt=""><figcaption></figcaption></figure>

### Step 6: Verify the installation \[Azure DevOps]

1. Open a new pull request in the configured Azure DevOps project and confirm that Qodo is triggered automatically.
2. Add a comment to the pull request using one of the supported commands to verify two-way communication:
   * `/improve`
   * `/describe`
   * `/ask`
   * `/review`
