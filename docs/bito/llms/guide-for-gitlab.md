# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab.md

# Guide for GitLab

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent) with your GitLab repositories. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a pull request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial

{% embed url="<https://youtu.be/wG09qSWFkzQ>" %}

## Prerequisites

Before proceeding, ensure you've completed all necessary prerequisites.

#### 1. Create a GitLab Personal Access Token:

For GitLab merge request code reviews, a token with **`api`** scope is required. Make sure that the token is created by a GitLab user who has the **`Maintainer`** access role.

[**View Guide**](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)

{% hint style="info" %}
**Important:** Bito posts comments using the GitLab user account linked to the Personal Access Token used during setup. To display "Bito" instead of your name, create a separate user account (e.g., Bito Agent) and use its token for integration.
{% endhint %}

{% hint style="info" %}
We recommend setting the **token expiration** to at least one year. This prevents the token from expiring early and avoids disruptions in the AI Code Review Agent's functionality.&#x20;

Additionally, we highly recommend updating the token before expiry to maintain seamless integration and code review processes.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FghbsjA3aafRQJBQGnksv%2Fimage%20(1).png?alt=media&#x26;token=6feb55f7-39b3-4d61-8e46-f6b233e64849" alt=""><figcaption><p><strong>GitLab Personal Access Token</strong></p></figcaption></figure>

#### 2. Authorizing a GitLab Personal Access Token for use with SAML single sign-on:

If your GitLab organization enforces SAML Single Sign-On (SSO), you must authorize your Personal Access Token through your Identity Provider (IdP); otherwise, Bito's AI Code Review Agent won't function properly.

For more information, please refer to these GitLab documentation:

* <https://docs.gitlab.com/ee/user/group/saml_sso/>
* <https://docs.gitlab.com/ee/integration/saml.html>
* <https://docs.gitlab.com/ee/integration/saml.html#password-generation-for-users-created-through-saml>

## Installation and configuration steps

Follow the step-by-step instructions below to install the **AI Code Review Agent** using **Bito Cloud**:

### **Step 1: Log in to Bito**

[Log in to Bito Cloud](https://alpha.bito.ai/) and select a workspace to get started.

### **Step 2: Open the Code Review Agents setup**

Click [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) under the **CODE REVIEW** section in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7jB4NvihTZqLpAX1nuaf%2Fscrnli_KuCSLAb2uwZqov.png?alt=media&#x26;token=8c7fdbb7-2358-40ed-9a5f-db23cb11be40" alt=""><figcaption></figcaption></figure>

### **Step 3: Select your Git provider**

Bito supports integration with the following Git providers:&#x20;

* GitHub&#x20;
* GitHub (Self-Managed)&#x20;
* GitLab&#x20;
* GitLab (Self-Managed)&#x20;
* Bitbucket
* Bitbucket (Self-Managed)

Since we are setting up the Agent for GitLab, select **GitLab** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FETj8JmXkQeBAQ5zufjHv%2Fscrnli_7Ci4O6tHHXY58F.png?alt=media&#x26;token=329d6d37-630a-409a-9f2d-b4226d8f8290" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Connect Bito to GitLab**

To enable merge request reviews, you’ll need to connect your Bito workspace to your GitLab account.

You can either connect using **OAuth (recommended)** for a seamless, one-click setup or manually enter your **Personal Access Token**.

To connect via OAuth, simply click the **Connect with OAuth (Recommended)** button. This will redirect you to the GitLab website, where you'll need to log in. Once authenticated, you'll be redirected back to Bito, confirming a successful connection.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrCeLccv5wvxww06Lpqtw%2Fscrnli_5jI39Zex0s92SO.png?alt=media&#x26;token=df661bf6-2cdc-4d01-8225-01e4d6bd0f6a" alt=""><figcaption></figcaption></figure>

If you prefer not to use OAuth, you can connect manually using a **Personal Access Token**.

Start by [generating a Personal Access Token](https://gitlab.com/-/user_settings/personal_access_tokens) with **`api`** scope in your GitLab account. For guidance, refer to the instructions in the [Prerequisites](#prerequisites) section.

Once generated, click the **Alternatively, use Personal or Group Access Token** button.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FX6IlUtc5Y6XaJoOB9dxv%2Fscrnli_sH76XQeLbsU3aw.png?alt=media&#x26;token=60bdc89d-7345-46b6-ba52-ab34e642b70c" alt=""><figcaption></figcaption></figure>

Now, enter the token into the **Personal Access Token** input field in Bito.

Click **Validate** to ensure the token is functioning properly.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fe2YSKEAzCLXKoy8nhTJE%2Fscrnli_ykor6MMedHkkFM.png?alt=media&#x26;token=a226253e-dc53-4684-8c3d-0a875d93d158" alt=""><figcaption></figcaption></figure>

If you've successfully connected via OAuth or manually validated your token, you can select your **GitLab Group** from the dropdown menu.

Click **Connect Bito to GitLab** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FzxcJdx9oRmZZzLNJTJo8%2Fscrnli_mC61ET3jriAsRg.png?alt=media&#x26;token=a6474328-07a5-470a-aeee-f713dd03b145" alt=""><figcaption></figcaption></figure>

&#x20;

### **Step 5: Enable AI Code Review Agent on repositories**&#x20;

After connecting Bito to your GitLab account, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F0TyvAqlOA5QYyh4Kv6JD%2Fscrnli_RtCVLzUlR23QJr_1.png?alt=media&#x26;token=c156d679-7e13-4700-a9ef-4693836d23e8" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual merge request reviews**&#x20;

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new merge requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the merge request and submit it. This action will start the code review process.

The AI-generated code review feedback will be posted as comments directly within your merge request, making it seamless to view and address suggestions right where they matter most.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBBOvTOprCCheQBy3MaQ1%2Fscrnli_9_18_2024_8-51-21%20AM.png?alt=media&#x26;token=633cd07e-24c6-4eec-b285-d83754d798cf" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** To enhance efficiency, the automated code reviews are only triggered for merge requests merging into the repository’s default branch. This prevents unnecessary processing and Advanced AI requests usage.

To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review merge requests when the source or target branch matches the list.

The **Include Source/Target Branches** filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
{% endhint %}

{% hint style="info" %}
The AI Code Review Agent automatically reviews code changes up to 5000 lines when a merge request is created. For larger changes, you can use the **`/review`** command.
{% endhint %}

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the merge request.
{% endhint %}

### **Step 7: Specialized commands for code reviews**

Bito also offers **specialized commands** that are designed to provide detailed insights into specific areas of your source code, including security, performance, scalability, code structure, and optimization.&#x20;

* **`/review security`**: Analyzes code to identify security vulnerabilities and ensure secure coding practices.&#x20;
* **`/review performance`**: Evaluates code for performance issues, identifying slow or resource-heavy areas.&#x20;
* **`/review scalability`**: Assesses the code's ability to handle increased usage and scale effectively.&#x20;
* **`/review codeorg`**: Scans for readability and maintainability, promoting clear and efficient code organization.&#x20;
* **`/review codeoptimize`**: Identifies optimization opportunities to enhance code efficiency and reduce resource usage.&#x20;

By default, the **`/review`** command generates inline comments, meaning that code suggestions are inserted directly beneath the code diffs in each file. This approach provides a clearer view of the exact lines requiring improvement. However, if you prefer a code review in a single post rather than separate inline comments under the diffs, you can include the optional parameter: **`/review #inline_comment=False`**&#x20;

For more details, refer to [Available Commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

### **Step 8: Chat with AI Code Review Agent**

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

To start the conversation, type your question in the comment box within the inline suggestions on your merge request, and then submit it. Typically, Bito AI responses are delivered in about 10 seconds. On GitHub and Bitbucket, you need to manually refresh the page to see the responses, while GitLab updates automatically.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FivCegqSzdY80hPdZIMGN%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=528ddcda-100d-49a8-b6b5-2b9767a23785" alt="" width="563"><figcaption></figcaption></figure>

### Step 9: Configure Agent settings

[Agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) let you control how reviews are performed, ensuring feedback is tailored to your team’s needs. By adjusting the options, you can:

* Make reviews more focused and actionable.
* Apply your own coding standards.
* Reduce noise by excluding irrelevant files or branches.
* Add extra checks to improve code quality and security.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)

## Screenshots

### Screenshot # 1

{% hint style="info" %}
*AI-generated merge request (MR) summary*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FZ08V4Js5ORq7j6n0qR5S%2Fscrnli_9_18_2024_8-20-30%20AM.png?alt=media&#x26;token=80e6b92c-95e2-4d1b-939c-1f976136bac2" alt=""><figcaption></figcaption></figure>

### Screenshot # 2

{% hint style="info" %}
**Changelist** showing key changes and impacted files in a merge request.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FyH8h3KVhYqjy8nSHQCby%2Fchangelist_by_bito.png?alt=media&#x26;token=99c64f3d-f554-47fd-aab7-f2d8d9994c09" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

### Screenshot # 3

{% hint style="info" %}
*AI code review feedback posted as comments on the merge request.*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FRGVVrPpKePySgQWiOrd6%2Fscrnli_9_18_2024_8-38-48%20AM_cropped.png?alt=media&#x26;token=20b082f1-dd87-437c-b1dc-268c9564a27a" alt=""><figcaption></figcaption></figure>
