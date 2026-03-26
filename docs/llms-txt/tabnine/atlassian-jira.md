# Source: https://docs.tabnine.com/main/welcome/readme/integrations/atlassian-jira.md

# Atlassian Jira Integration

AI agents to implement and validate Jira issues\\

You can now connect Tabnine to Atlassian Jira and take advantage of two new AI agents:

* **Jira Implementation Agent:** A user can ask Tabnine to implement a Jira issue that’s been assigned to them. Tabnine generates code for the requirements outlined in the Jira issue.
* **Jira Validation Agent:** A user can ask Tabnine to review their implementation. When a user has written code for a Jira issue, Tabnine can check if their code accurately captures the requirements outlined in the Jira issue, offering suggestions if it doesn’t.

As the first AI code assistant to offer an integration with Atlassian Jira, Tabnine enables you to accomplish macro-level tasks with a single click. You can directly ask Tabnine to implement a story, bug, task, or subtask — there’s no need to decipher requirements in a Jira issue, break it down into tasks, and feed specific prompts into an AI chat window.

## How does this capability work

To use the new agents, you must first connect Tabnine to Jira. After the connection is established, all the Jira issues assigned to you as an individual user are available in Tabnine.

You can then select a specific issue and ask Tabnine to implement it. Once you hit Enter, Tabnine generates code to meet the requirements of the Jira issue. From there, you can review and revise the code as needed before inserting it.

In addition to code generation, you can validate code with this functionality. Simply select the code you’ve written and ask AI chat if it aligns with the requirements outlined in the Jira issue.

[Learn more](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/jira-connection)

## Jira issues that can be implemented with Tabnine

There’s no technical limitation on the type of Jira issues that Tabnine can implement. To ensure the most relevant and accurate output, we recommend using Tabnine for issues like stories, bugs, tasks, and subtasks (i.e., issues that represent defined and specific units of work). This keeps the communication with AI concise and makes it easier to check the responses. During implementation, you can then ask Tabnine to refine the output (as needed), review the reference files used to generate the output, and work through the follow-up questions suggested by Tabnine.

[Learn more](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/jira-connection#does-the-jira-connection-work-with-any-issue-format)

## Supported matrix

|                                           | Jira Cloud | Jira Data Center\* |
| ----------------------------------------- | ---------- | ------------------ |
| Tabnine Dev                               | Yes        | No                 |
| Tabnine Enterprise (SaaS)                 | Yes        | Yes                |
| Tabnine Enterprise (private installation) | Yes\*\*    | Yes\*\*            |

* This feature supports the same [languages](https://docs.tabnine.com/main/welcome/readme/supported-languages) and [IDEs](https://docs.tabnine.com/main/welcome/readme/supported-ides) as the AI chat.
* To establish a connection between Tabnine and Jira, you need access to an internet connection and a browser. It’s not supported in VDI environments.
* We currently support parent issues in Jira. Issues that are children of a parent issue need to be implemented individually.
* Inline actions currently don’t support this capability.\
  \
  \*Jira Data Center version 8.20 and higher.\
  \*\*Jira Data Center: Tabnine version 5.11.0 or higher; Jira Cloud: Tabnine version 5.12.0\\

## **Enabling the Jira connection for Tabnine Enterprise**

{% hint style="info" %}
**Enterprise Self-Hosted**

Starting from version 5.12.0, the Jira connection feature for Enterprise customers in private installations is license-dependent. If this feature is not enabled for your account, contact your Tabnine Account Manager or email <support@tabnine.com>.
{% endhint %}

The Jira connection is disabled by default for Tabnine Enterprise customers. Team administrators can enable or disable this feature for the entire team through the Tabnine Admin UI. Tabnine supports integration with either [Jira Cloud](#setting-up-the-integration-for-jira-cloud) or [Jira Data Center](#setting-up-the-tabnine-integration-with-jira-data-center).

**Notes**

* Regardless of the admin setup, the end user flow and experience are the same for both integration options.
* The integration may take up to **one hour** to fully populate and become visible in users' IDEs.

### **Setting up the integration for Jira Cloud (Tabnine Enterprise SaaS)**

Enabling the Jira Cloud connection for Tabnine Enterprise SaaS is straightforward. Team administrators can toggle the feature directly in the Tabnine Admin Console.

**Steps:**

1. Log in to the Tabnine Admin Console.
2. Navigate to the [**Personalization**](https://app.tabnine.com/profile/personalization) screen.
3. Toggle the **Enable connection to Jira** switch.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b3817330a6c9973294a874f947e3e3a4400d56b0%2Fsaas%20ent%20admin%20personalization.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Setting up the integration for Jira Cloud (Tabnine Enterprise Self - Hosted)

{% hint style="info" %}
This setup is available for Tabnine Enterprise customers with private installations (version 5.12.0 or higher).
{% endhint %}

Integrating Tabnine private installation with Jira Cloud requires additional configuration, as it involves creating a dedicated OAuth 2.0 App in Atlassian.

#### **Step 1: Create an OAuth 2.0 App**

1. Go to the Atlassian Developer Console.
2. From the **Resources** menu, select **Developer Console**.
3. Click **Create App**, then select **OAuth 2.0 (3LO Integration)**.
4. Enter a name for your application and accept Atlassian’s developer terms.

   <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-dff1801c9f2d41d17816b4224c01f83b533f4ac3%2FJira%20SH-cloud1.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
5. You'll be redirected to the **My Apps** overview page.

   * Navigate to **Authorization** and provide a callback URL.

   <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0c33c15da63c910f5692541dae3bc10a42331543%2FJira%20SH%20-Cloud%202.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
6. Add the following required permissions to your app:

   * `read:me`
   * `read:account`
   * `read:jira-work`
   * `read:jira-user`

   <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7cc8a1d728b4af220e3f59e010e678302101d45d%2FJira%20SH%20-Cloud%203.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

   <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-bddd35fe35b2458d0b4dfb280d91e7e796686ca5%2FJira%20SH%20-Cloud%204.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
7. Go to **Distribution** and complete the form to share your app.

   <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fe47c1cee3b08b590db64cb6a810b27aa92af22b%2FJira%20SH%20-Cloud%205.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

#### **Step 2: Enter OAuth Application credentials in the Tabnine Admin Console**

1. Copy your OAuth 2.0 application credentials from Atlassian:
   * Navigate to **Overview > App Details**.
   * Copy the **Client ID** and **Client Secret**.
2. Log in to the Tabnine Admin Console:

   * Navigate to **Settings > Workspace**.
   * Locate the **Enable Jira connection** section.
   * Enable the **Jira Cloud** option.
   * Enter the following details:
     * Client ID
     * Client Secret
     * Jira Data Center URL (if applicable)
   * Click **Save**.

   <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-4ac0c7da6040e9efad60e6b92d92beab0aac46dd%2FSH%20Jira%20Cloud%206.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### **Setting up the Tabnine integration with Jira Data Center**

{% hint style="info" %}
**Note**

* The Tabnine integration with Jira Data Center is available to Tabnine Enterprise customers with private installation (version 5.11.0 or higher).
* Supports Jira Data Center version 8.20 and higher.
  {% endhint %}

Integrating Tabnine with Jira Data Center requires additional configuration beyond simply enabling the toggle. Follow these steps:

#### Step 1: Set up a Tabnine application link in your Jira Data Center installation

1. Go to [Atlassian Developer](https://developer.atlassian.com/).
2. Navigate to **Resources** **> Developer Console.**
3. Click on **Create App** and then click on **OAuth 2.0 (3LO Integration)**.
4. Enter a name for your application and accept Atlassian’s developer terms.
5. Navigate to **Administration > Applications > Application links**.
6. Select **Create link**.
7. Choose **External application**, and set the direction to **Incoming**.
8. In the following screen, complete the fields as follows:
   * **Name:** Enter a unique name for the application link.
   * **Redirect URL:** Enter the callback URL from the Tabnine admin application. This URL will redirect users after authorization and should be your Tabnine server URL followed by `/app/auth/jira`. For example: `https://private-tabnine.company.com/app/auth/jira`.
   * **Permission:** Set the permission to **Read** (defines which permissions the application has on your instance).

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-78828f55e05cbc8d3e92feadceb803a3ce830049%2FJira%20DC%20-%20create%20link.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

#### Step 2: Enter Data Center Application credentials in the Tabnine Admin Console

After creating the application link in your Data Center instance, input the application credentials in the Tabnine Admin Console:

1. Ensure you have the **Client ID** and **Client Secret** from your Jira Data Center application:
   * Go to **Administration > Application links** in your Jira Data Center.
   * Locate the relevant application link and select **More actions > View credentials**.
   * Copy the **Client ID** and **Client Secret**.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-417e519356863acfef25670624edf2bd0b1367f5%2FJira%20DC%20-%20credentials.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

2. In the Tabnine Admin Console:

   * Navigate to **Settings > Workspace**.
   * Find the **Enable Jira connection** section and toggle it on.
   * Click **Edit.**
   * Enter the **Client ID**, **Client Secret**, and your **Jira Data Center URL**.
   * Click **Save**.

   <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-1091293ad0e94d6d792e50ce7948ecc5ad88781f%2FJira%20DC%20Tabnine%20credentials.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

\*Configure CA for Jira Integration with Jira Data Center Using a Self-Signed Certificate (If Needed): To enable secure communication between Jira Data Center and Tabnine's authentication service when using a self-signed certificate, you need to configure a Certificate Authority (CA) and add it to the Helm values of Tabnine’s auth service. This ensures the authentication service recognizes and trusts the self-signed certificate. Follow these steps to set up the CA:

1. Set the environment variable Set the Base64-encoded CA certificate as the JIRA\_DC\_ADD\_SSL\_CERTIFICATE\_BASE64 environment variable:

JIRA\_DC\_ADD\_SSL\_CERTIFICATE\_BASE64=$(cat full-chain.pem | base64)

2. Add CA cert to the local trust store We need this step to avoid TLS issues in the IDE using the Jira connection.
3. Verify the Configuration Verify that Tabnine’s authentication service can connect securely to Jira Data Center using the self-signed certificate by initiating Jira connection flow from IDE.

## FAQ

#### **What context is utilized by Tabnine for the Jira connection?**

For the Jira connection, Tabnine leverages the text in the Jira issue’s title and description as context for implementing the issue and for reviewing the implementation. We currently don't use the following as context:

* Images that are included in the Jira issue
* Comments added to the issue
* History
* Links in the issue
* Related issues
* Design specs like Figma

In addition to using the information in Jira issues as context, Tabnine continues to use locally available code and information in your IDE and (for Enterprise users) your organization’s global codebases to generate responses tailored to you and your organization.

[Learn more](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/jira-connection#does-the-jira-connection-work-with-any-issue-format)

#### Who has access to this capability?

This capability is available to Tabnine users on the Pro and Enterprise tiers.

#### What control do Tabnine administrators have?

This feature is disabled by default for Enterprise customers, but enabled by default for all other Tabnine chat users.

Tabnine administrators (at enterprise SaaS or private installation) can enable it. The administrators can enable the feature themselves without contacting our Support team. Once enabled, this feature is available to all Tabnine users at the company. The end users of Tabnine can then connect Tabnine to Jira themselves. Please note, this is a client-side integration.

Tabnine leverages Jira user permissions during connection ensuring that only issues assigned to a developer are accessible to them.
