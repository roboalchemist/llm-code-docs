# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket-self-managed.md

# Guide for Bitbucket (Self-Managed)

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git) with your Bitbucket (Self-Managed) server. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a pull request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial <a href="#video-tutorial" id="video-tutorial"></a>

{% embed url="<https://youtu.be/ZAawiQ22PMc>" %}

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before proceeding, ensure you've completed all necessary prerequisites.

### **1. Create a Bitbucket Personal Access Token:**

For Bitbucket pull request code reviews, a token with **`Project Admin`**  permission is required. Make sure that the token is created by a Bitbucket user who has the **`Admin`**  privileges.

{% hint style="info" %}
**Important:** Bito posts comments using the Bitbucket user account linked to the Personal Access Token used during setup. To display "Bito" instead of your name, create a separate user account (e.g., Bito Agent) and use its token for integration.
{% endhint %}

You can use the **Create Token** button that appears once you provide the **Hosted Bitbucket URL** and your **Bitbucket username**.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F5YvKDBUEIefxIpKB5GaV%2Fscrnli_g528adnNaTXmWg_1.png?alt=media&#x26;token=cf2dced9-b5ae-4ea9-bd6b-6ce1e7d1ba92" alt="" width="563"><figcaption></figcaption></figure>

Or directly visit the URL of your self-hosted Bitbucket.

To create a token for your user account:

1. Go to **Profile picture** > **Manage account** > **HTTP access tokens**.
2. Select **Create token**.
3. Set the token name, permissions, and expiry.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFgvm4olJ3yhyo0xOiWnf%2Fscrnli_Rr1m0ddO4rSyCR_1%20(2).png?alt=media&#x26;token=07dadb9b-3494-480e-8c35-aeca49af780b" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FWaRUeDccyy6D63BTQPyZ%2Fscrnli_um1SDww4ZRtLsi_1%20(1).png?alt=media&#x26;token=10217b14-4a6d-4795-a987-e8f05a7b1aa6" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FlPWS1DtbgwvmwitUYvqt%2Fscrnli_mR0r6q2h3RV3kJ_1%20(1).png?alt=media&#x26;token=4ae08d23-8710-4a7d-babc-1064b3062aea" alt="" width="563"><figcaption></figcaption></figure>

<a href="https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html" class="button primary">View Bitbucket documentation</a>

### **2. Authorizing a Bitbucket Personal Access Token for use with SAML single sign-on:**

If your Bitbucket organization enforces SAML Single Sign-On (SSO), you must authorize your Personal Access Token through your Identity Provider (IdP); otherwise, Bito's AI Code Review Agent won't function properly.

For more information, please refer to [Bitbucket SAML SSO documentation](https://support.atlassian.com/bitbucket-data-center/kb/how-to-configure-saml-sso-for-bitbucket-data-center-with-okta/).

## Installation and configuration steps <a href="#installation-and-configuration-steps" id="installation-and-configuration-steps"></a>

Follow the step-by-step instructions below to install the **AI Code Review Agent** using **Bito Cloud**:

### **Step 1: Log in to Bito** <a href="#step-1-log-in-to-bito" id="step-1-log-in-to-bito"></a>

[Log in to Bito Cloud](https://alpha.bito.ai/) and select a workspace to get started.

### **Step 2: Open the Code Review Agents setup** <a href="#step-2-open-the-code-review-agents-setup" id="step-2-open-the-code-review-agents-setup"></a>

Click [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) under the **CODE REVIEW** section in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FaRd44Mm4ssRuJq0JPTDY%2Fscrnli_F8cTXu9Nhus5wi.png?alt=media&#x26;token=1caf8b4c-1f2d-4fee-a4b2-68bfc7cc5925" alt=""><figcaption></figcaption></figure>

### **Step 3: Select your Git provider** <a href="#step-3-select-your-git-provider" id="step-3-select-your-git-provider"></a>

Bito supports integration with the following Git providers:

* GitHub
* GitHub (Self-Managed)
* GitLab
* GitLab (Self-Managed)
* Bitbucket
* Bitbucket (Self-Managed)

Since we are setting up the Agent for Bitbucket (Self-Managed) server, select **Bitbucket (Self-Managed)** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Frk0l6UdSGntsYtRlPDik%2Fscrnli_v4wqkwtzxUUXo8.png?alt=media&#x26;token=15097f2d-9e3f-45d1-8602-8bda679b0ef0" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Connect Bito to Bitbucket** <a href="#step-4-connect-bito-to-bitbucket" id="step-4-connect-bito-to-bitbucket"></a>

To enable pull request reviews, you’ll need to connect your Bito workspace to your Bitbucket (Self-Managed) server.

{% hint style="info" %}
If your network blocks external services from interacting with the Bitbucket server, whitelist all of Bito's gateway IP addresses in your firewall to ensure Bito can access your self-hosted repositories. The Agent response can come from any of these IPs.

* **List of IP addresses to whitelist:**
  * **`18.188.201.104`**
  * **`3.23.173.30`**
  * **`18.216.64.170`**
    {% endhint %}

You need to enter the details for the below mentioned input fields:

* **Hosted Bitbucket URL:** This is the domain portion of the URL where your Bitbucket Enterprise server is hosted (e.g., `https://bitbucket.mycompany.com`). Please check with your Bitbucket administrator for the correct URL.
* **Bitbucket username:** This is your Bitbucket username used for login. Please check it from your user profile page or ask your Admin.
* **Personal Access Token:** Generate a **Bitbucket Personal Access Token** with **`Project Admin`**  permission in your Bitbucket (Self-Managed) account. Ensure you have Bitbucket **Admin** privileges. Enter the token into the **Personal Access Token** input field. You can use the **Create Token** button that appears once you provide the **Hosted Bitbucket URL** and your **Bitbucket username**.

  For guidance, refer to the instructions in the [Prerequisites](#prerequisites) section.

{% hint style="info" %}
**Important:** Bito posts comments using the Bitbucket user account linked to the Personal Access Token used during setup. To display "Bito" instead of your name, create a separate user account (e.g., Bito Agent) and use its token for integration.
{% endhint %}

Click **Validate** to ensure the token is functioning properly.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJfYP00SupO4zpbSiTm5F%2Fscrnli_UJQnm8OmlV2PmM_1.png?alt=media&#x26;token=296c329a-1095-4455-8d5a-7dbdd917b086" alt="" width="563"><figcaption></figcaption></figure>

If the token is successfully validated, click **Connect Bito to Bitbucket** to proceed.

### **Step 5: Enable AI Code Review Agent on repositories** <a href="#step-5-enable-ai-code-review-agent-on-repositories" id="step-5-enable-ai-code-review-agent-on-repositories"></a>

After connecting Bito to your Bitbucket self-managed server, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FU0qx8lO9O8t6dj1lhX1r%2Fscrnli_XExOnuPOb2H8eW_1.png?alt=media&#x26;token=e6075bf3-fc4f-42ec-9ff6-396e2cd5894f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual merge request reviews** <a href="#step-6-automated-and-manual-merge-request-reviews" id="step-6-automated-and-manual-merge-request-reviews"></a>

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new pull requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the pull request and submit it. This action will start the code review process.

The AI-generated code review feedback will be posted as comments directly within your pull request, making it seamless to view and address suggestions right where they matter most.

{% hint style="info" %}
**Note:** To enhance efficiency, the automated code reviews are only triggered for pull requests merging into the repository’s default branch. This prevents unnecessary processing and Advanced AI requests usage.

To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review pull requests when the source or target branch matches the list.

The **Include Source/Target Branches** filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
{% endhint %}

{% hint style="info" %}
The AI Code Review Agent automatically reviews code changes up to 5000 lines when a pull request is created. For larger changes, you can use the **`/review`** command.
{% endhint %}

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the pull request.
{% endhint %}

### **Step 7: Specialized commands for code reviews** <a href="#step-7-specialized-commands-for-code-reviews" id="step-7-specialized-commands-for-code-reviews"></a>

Bito also offers **specialized commands** that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.

* **`/review security`**: Analyzes code to identify security vulnerabilities and ensure secure coding practices.
* **`/review performance`**: Evaluates code for performance issues, identifying slow or resource-heavy areas.
* **`/review scalability`**: Assesses the code's ability to handle increased usage and scale effectively.
* **`/review codeorg`**: Scans for readability and maintainability, promoting clear and efficient code organization.
* **`/review codeoptimize`**: Identifies optimization opportunities to enhance code efficiency and reduce resource usage.

By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**

For more details, refer to [Available Commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands).

### **Step 8: Chat with AI Code Review Agent** <a href="#step-8-chat-with-ai-code-review-agent" id="step-8-chat-with-ai-code-review-agent"></a>

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

To start the conversation, type your question in the comment box within the inline suggestions on your pull request, and then submit it. Typically, Bito AI responses are delivered in about 10 seconds. On GitHub and Bitbucket, you need to manually refresh the page to see the responses, while GitLab updates automatically.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

### Step 9: Configure Agent settings

[Agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) let you control how reviews are performed, ensuring feedback is tailored to your team’s needs. By adjusting the options, you can:

* Make reviews more focused and actionable.
* Apply your own coding standards.
* Reduce noise by excluding irrelevant files or branches.
* Add extra checks to improve code quality and security.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
