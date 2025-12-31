# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab-self-managed.md

# Guide for GitLab (Self-Managed)

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent) with your GitLab (Self-Managed) server. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a merge request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial

coming soon...

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

For more information, please refer to the following GitLab documentation:

* [SAML SSO for GitLab.com groups](https://docs.gitlab.com/user/group/saml_sso/)
* [SAML SSO for GitLab Self-Managed](https://docs.gitlab.com/integration/saml/)
* [Password generation for users created through SAML](https://docs.gitlab.com/integration/saml/#password-generation-for-users-created-through-saml)

## Installation and configuration steps

Follow the step-by-step instructions below to install the **AI Code Review Agent** using **Bito Cloud**:

### **Step 1: Log in to Bito**

[Log in to Bito Cloud](https://alpha.bito.ai/) and select a workspace to get started.

### **Step 2: Open the Code Review Agents setup**

Click [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) under the **CODE REVIEW** section in the sidebar.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7jB4NvihTZqLpAX1nuaf%2Fscrnli_KuCSLAb2uwZqov.png?alt=media&#x26;token=8c7fdbb7-2358-40ed-9a5f-db23cb11be40" alt=""><figcaption></figcaption></figure>

### **Step 3: Select your Git provider**&#x20;

Bito supports integration with the following Git providers:&#x20;

* GitHub&#x20;
* GitHub (Self-Managed)&#x20;
* GitLab&#x20;
* GitLab (Self-Managed)&#x20;
* Bitbucket
* Bitbucket (Self-Managed)

Since we are setting up the Agent for GitLab (Self-Managed) server, select **GitLab (Self-Managed)** to proceed.

{% hint style="info" %}
**Supported versions:**

* **GitLab (Self-Managed):** 15.5 and above
  {% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FtgUKG7gdgn9GJgSAASFy%2Fscrnli_QBt6t8kukXYaYE.png?alt=media&#x26;token=b312f994-faf6-49cd-a930-3ee640293f46" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Connect Bito to GitLab** &#x20;

To enable merge request reviews, you’ll need to connect your Bito workspace to your GitLab (Self-Managed) server.

{% hint style="info" %}
If your network blocks external services from interacting with the GitLab server, whitelist all of Bito's gateway IP addresses in your firewall to ensure Bito can access your self-hosted repositories. The Agent response can come from any of these IPs.&#x20;

* **List of IP addresses to whitelist:**&#x20;
  * **`18.188.201.104`**
  * **`3.23.173.30`**
  * **`18.216.64.170`**
    {% endhint %}

You need to enter the details for the below mentioned input fields:&#x20;

* **Hosted GitLab URL:** This is the domain portion of the URL where you GitLab Enterprise Server is hosted (e.g., `https://yourcompany.gitlab.com`). Please check with your GitLab administrator for the correct URL.&#x20;
* **Personal Access Token:** Generate a **GitLab Personal Access Token** with **`api`** scope in your GitLab (Self-Managed) account and enter it into the **Personal Access Token** input field. For guidance, refer to the instructions in the [Prerequisites](#prerequisites) section.

Click **Validate** to ensure the token is functioning properly.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fomu0dVL9I0CTQ8yC7MHO%2Fscrnli_27slie02tJkRAf_1.png?alt=media&#x26;token=e2689d19-c041-48aa-90ed-6b678c224dc4" alt=""><figcaption></figcaption></figure>

If the token is successfully validated, you can select your **GitLab Group** from the dropdown menu.

* **Note:** You can select multiple groups after the setup is complete.

Click **Connect Bito to GitLab** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FU4h3BLObcIsIEN0lU95i%2Fscrnli_1L3maXu3pJtiCd.png?alt=media&#x26;token=32be430f-2b99-428b-9f47-c47067966e60" alt=""><figcaption></figcaption></figure>

### **Step 5: Enable AI Code Review Agent on repositories**&#x20;

After connecting Bito to your GitLab self-managed server, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FeXTvPIXX2uSyhuWGCLNI%2Fscrnli_BYisAy83ZXjb8j_1.png?alt=media&#x26;token=1b4968fe-9740-498f-aebc-7e854cdf0ccf" alt=""><figcaption></figcaption></figure>

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

## Managing multiple GitLab groups in Bito Cloud

[Bito Cloud](https://alpha.bito.ai/) allows you to connect and manage multiple GitLab groups for **GitLab (Self-Managed)** integrations. Use the instructions below to add or remove GitLab groups for AI code reviews.

### How to add multiple GitLab groups?

You can connect more than one GitLab group to Bito for AI code reviews.

Follow these steps to add additional groups:

1. Go to the [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F4CZ7NBraXiiD6Iqq7j5a%2Fscrnli_Y8WOHXWq804QA4.png?alt=media&#x26;token=bb9bd6b7-f997-4e59-8cac-344ed3bbc532" alt=""><figcaption></figcaption></figure>

2. At the top-center of the page, click the **“+” (plus) icon** next to the currently selected GitLab group name, then select **Add group** from the dropdown menu.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FMslGYbmuoV1rRShmx5Jl%2Fscrnli_W8jQLW06Gxuqt0_1.png?alt=media&#x26;token=f7f30d4e-aae6-46f5-92c9-1e5cb065287c" alt=""><figcaption></figcaption></figure>

3. A popup will appear. Use the **dropdown menu** to select a GitLab group you want to add.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FbLf4ueoWPOLRQ3CxwrWI%2Fscrnli_8ZF0yXi7X0hXsw_1.png?alt=media&#x26;token=91597a4e-b462-4400-8a14-65df4307c75c" alt=""><figcaption></figcaption></figure>

4. Click the **Add group** button.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F0WHxXbmnKKK9RmWfr5pF%2Fscrnli_cz6US78Ei0o7Xj_1.png?alt=media&#x26;token=322cf8e0-0e92-43a0-9d6b-f8486e560f86" alt=""><figcaption></figcaption></figure>

Once added, all repositories from that group will be listed and available for AI code reviews under the default agent.

{% hint style="info" %}
**Note:** This **multiple GitLab groups** feature is currently available **only for GitLab (Self-Managed)** integrations.
{% endhint %}

### How to remove a GitLab group?

To disconnect a GitLab group from Bito Cloud:

1. Go to the [**Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FR7Z8pmGAEEi2saOB0MPM%2Fscrnli_Y8WOHXWq804QA4.png?alt=media&#x26;token=f6dbf22d-bfb4-498c-8a87-91508990d724" alt=""><figcaption></figcaption></figure>

2. At the top-center of the page, click the **three dots icon** next to the currently selected GitLab group name, then select **Manage groups** from the dropdown menu.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FdULLEBhV1cLCGuKDWgKm%2Fscrnli_EPno749Af0t5m9_1.png?alt=media&#x26;token=cf282900-50a1-489e-8a03-d19970dcb48e" alt=""><figcaption></figcaption></figure>

3. A popup will appear showing a list of connected groups. Click the **“✕” (cross) icon** next to the group you want to remove.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7RcLErjIG7OHFhhhQUkk%2Fscrnli_ObMG7t14A0Z347_1.png?alt=media&#x26;token=3a242425-7690-46fb-bac0-7a7e448779b5" alt=""><figcaption></figcaption></figure>

3. Confirm the removal in the prompt.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOwjpuYuS6IufShaNMcgZ%2Fscrnli_gARi37sN912InC_1.png?alt=media&#x26;token=65fdba44-9333-4607-9b01-cddfe458c2ad" alt=""><figcaption></figcaption></figure>

Once removed, the repositories from that group will no longer appear in Bito or be included in AI code reviews.

### How to select one or more GitLab Groups?

When you have **multiple GitLab groups connected** in Bito Cloud, the group name at the top-center of the [Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) page becomes a **dropdown menu**.

From this dropdown, you can:

* Select **a single group**
* Select **multiple groups as needed**
* Select **All groups**

The list of repositories displayed below will update automatically based on your selection—showing only the repositories from the selected groups.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FA2eUv2Rf6isNoIbtEovO%2F1_scrnli_XOow3dK4CvFTuP.png?alt=media&#x26;token=a9cfb7fd-fde1-42f6-b93c-8fc594a3cbc9" alt=""><figcaption></figcaption></figure>

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
