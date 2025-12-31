# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-github-self-managed.md

# Guide for GitHub (Self-Managed)

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent) with your self-managed GitHub Enterprise server. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a pull request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial

coming soon...

## Prerequisites

Before proceeding, ensure you've completed all necessary prerequisites.

#### 1. Create a GitHub Personal Access Token (classic):

For GitHub pull request code reviews, ensure you have a **CLASSIC** personal access token with **`repo`** scope. We do not support fine-grained tokens currently.

[**View Guide**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBZH0vDwrPqYQPMIxIyNW%2Fimage.png?alt=media&#x26;token=a4c42d8d-61a5-4cdb-87a1-622c0ba8f1ae" alt=""><figcaption><p><strong>GitHub Personal Access Token (classic)</strong></p></figcaption></figure>

#### 2. Authorizing a GitHub Personal Access Token for use with SAML single sign-on:

If your GitHub organization enforces [SAML Single Sign-On (SSO)](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/enforcing-saml-single-sign-on-for-your-organization), you must authorize your Personal Access Token (classic) through your Identity Provider (IdP); otherwise, Bito's AI Code Review Agent won't function properly.

For detailed instructions, please refer to the [GitHub documentation](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).

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

Since we are setting up the Agent for self-managed GitHub Enterprise server, select **GitHub (Self-Managed)** to proceed.

{% hint style="info" %}
**Supported versions:**

* **GitHub Enterprise Server:** 3.0 and above
  {% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FhJOg0OlVYrzpFw1KP3yw%2Fscrnli_Jk7BcFXL0xXyja.png?alt=media&#x26;token=3bfd22c4-99bc-494c-a426-c6ae7215d466" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Register & install the Bito App for GitHub**&#x20;

To enable pull request reviews, you need to register and install the **Bito’s AI Code Review Agent** app on your self-managed GitHub Enterprise server.

{% hint style="info" %}
If your network blocks external services from interacting with the GitHub server, whitelist all of Bito's gateway IP addresses in your firewall to ensure Bito can access your self-hosted repositories. The Agent response can come from any of these IPs.&#x20;

* **List of IP addresses to whitelist:**&#x20;
  * **`18.188.201.104`**
  * **`3.23.173.30`**
  * **`18.216.64.170`**&#x20;
    {% endhint %}

You need to enter the details for the below mentioned input fields:&#x20;

* **Hosted GitHub URL:** This is the domain portion of the URL where you GitHub Enterprise Server is hosted (e.g., `https://yourcompany.github.com`). Please check with your GitHub administrator for the correct URL.&#x20;
* **Personal Access Token:** Generate a **Personal Access Token (classic)** with **“repo”** scope in your GitHub (Self-Managed) account and enter it into the **Personal Access Token** input field. We do not support fine-grained tokens currently. For guidance, refer to the instructions in the [Prerequisites](#prerequisites) section.&#x20;

Click **Validate** to ensure the login credentials are working correctly. If the credentials are successfully validated, click the **Install Bito App for GitHub** button. This will redirect you to your GitHub (Self-Managed) server.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FeiSAyQzwhsWkr9bPZrce%2Fscrnli_rCj22uk5HFb2t2_1.png?alt=media&#x26;token=d17d9f8e-c8a3-472e-a13f-8fa4b13e8109" alt=""><figcaption></figcaption></figure>

Before proceeding, you’ll be asked to **enter your GitHub App name** — this is the name that will appear in your GitHub Apps list and during installations. Choose a clear, recognizable name (for example, “Bito Code Reviewer”).

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXWiiC7FFRU0ZXKy9TZcL%2Fscrnli_98w41S7XJ9u6zO.png?alt=media&#x26;token=20db7387-9ddd-4529-bdf8-6c20c358f9fa" alt=""><figcaption></figcaption></figure>

Now select where you want to install the app: &#x20;

* Choose **All repositories** to enable Bito for every repository in your account.&#x20;
* Or, select **Only select repositories** and pick specific repositories using the dropdown menu.&#x20;

{% hint style="info" %}
Bito app uses these permissions:&#x20;

* **Read** access to metadata&#x20;
* **Read** and **write** access to code, issues, and pull requests&#x20;
* **Read** access to organization members
  {% endhint %}

Click **Install & Authorize** to proceed. Once completed, you will be redirected to Bito.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FpkNPb32ypSep8KvCjxhE%2Fscrnli_53aedt4Zg9v0Rm.png?alt=media&#x26;token=210bfd9b-ea7a-449d-8e07-1f080c0ddd82" alt=""><figcaption></figcaption></figure>

### **Step 5: Enable AI Code Review Agent on repositories**&#x20;

After connecting Bito to your self-managed GitHub Enterprise server, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8ou5QfEk0k1I9iskh94k%2Fscrnli_zBhAS7sgD29mGl_1.png?alt=media&#x26;token=0a4afced-697e-4926-a0a9-659a9b4fc3ab" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual pull request reviews**&#x20;

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new pull requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the pull request and submit it. This action will start the code review process.

The AI-generated code review feedback will be posted as comments directly within your pull request, making it seamless to view and address suggestions right where they matter most.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FryhzTFegsxvL4eoZewT7%2Fscrnli_2_28_2024_8-57-29%20PM.png?alt=media&#x26;token=af92cdfb-089b-4f95-8200-52adebe366dd" alt=""><figcaption></figcaption></figure>

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

To start the conversation, type your question in the comment box within the inline suggestions on your pull request, and then submit it. Typically, Bito AI responses are delivered in about 10 seconds. On GitHub and Bitbucket, you need to manually refresh the page to see the responses, while GitLab updates automatically.

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
*AI-generated pull request (PR) summary*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fk5wsTj4siolCcaZqHRIX%2Fscrnli_9_13_2024_12-33-56%20PM.png?alt=media&#x26;token=63cb7da9-21ca-41a1-83ba-9b107d07a6cf" alt=""><figcaption></figcaption></figure>

### Screenshot # 2

{% hint style="info" %}
**Changelist** showing key changes and impacted files in a pull request.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FyH8h3KVhYqjy8nSHQCby%2Fchangelist_by_bito.png?alt=media&#x26;token=99c64f3d-f554-47fd-aab7-f2d8d9994c09" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

### Screenshot # 3

{% hint style="info" %}
*AI code review feedback posted as comments on the pull request.*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FP0sUIAZ3Lq0FqL9ytfPF%2Fscrnli_9_13_2024_12-49-29%20PM_cropped_3.png?alt=media&#x26;token=d74d3b27-4831-4735-9559-6f9da191e910" alt=""><figcaption></figcaption></figure>
