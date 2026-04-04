# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket.md

# Guide for Bitbucket

Speed up code reviews by configuring the [AI Code Review Agent](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent) with your Bitbucket repositories. In this guide, you'll learn how to set up the Agent to receive automated code reviews that trigger whenever you create a pull request, as well as how to manually initiate reviews using [available commands](https://docs.bito.ai/bito-dev-agents/ai-code-review-agent/available-commands).

{% hint style="info" %}
The **Free Plan** offers **AI-generated pull request summaries** to provide a quick overview of changes. For advanced features like **line-level code suggestions**, consider upgrading to the **Team Plan**. For detailed pricing information, visit our [**Pricing**](https://bito.ai/pricing/) page.

[**Get a 14-day FREE trial of Bito's AI Code Review Agent.**](https://alpha.bito.ai/home/welcome)
{% endhint %}

## Video tutorial

{% embed url="<https://youtu.be/s4iKC4QRAqE>" %}

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

Since we are setting up the Agent for Bitbucket, select **Bitbucket** to proceed.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ff6khlPh27gsqOuxtn1DX%2Fscrnli_8CcC8oU24XyHAx.png?alt=media&#x26;token=4172d5ad-bdc6-48bc-983e-c147b6e35d0f" alt="" width="563"><figcaption></figcaption></figure>

### **Step 4: Connect Bito to Bitbucket**

To enable pull request reviews, you’ll need to connect your Bito workspace to your Bitbucket account.

{% hint style="info" %}
If your [Bitbucket access control settings](https://support.atlassian.com/bitbucket-cloud/docs/control-access-to-your-private-content/) block external services from interacting with the Bitbucket server, whitelist all of Bito's gateway IP addresses to ensure Bito can access your repositories. The Agent response can come from any of these IPs.

* **List of IP addresses to whitelist:**
  * **`18.188.201.104`**
  * **`3.23.173.30`**
  * **`18.216.64.170`**

See the [Bitbucket documentation](https://support.atlassian.com/bitbucket-cloud/docs/control-access-to-your-private-content/) for more information.
{% endhint %}

Click **Install Bito App for Bitbucket**. This will redirect you to Bitbucket.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FMkEhUlMUfiK26rbEV9lS%2Fscrnli_jBYatEquCn4pVe.png?alt=media&#x26;token=9e3b91d5-1858-4e85-8405-2f1623aaf5a4" alt=""><figcaption></figcaption></figure>

Now, authorize the Bito App to access your Bitbucket repositories.

Select your Bitbucket workspace from the **Authorize for workspace** dropdown menu and then click **Grant access**. Once completed, you will be redirected to Bito.

{% hint style="info" %}
**Note:** You'll only see Bitbucket workspaces where you have **Admin** access. If no workspaces appear in the dropdown, it means your account doesn’t have admin access to any workspace. To connect a workspace, make sure you have admin access for it.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fv0VauXquH5Q6mJg7vTYZ%2Ftinywow_scrnli_24x3kCekLNju4h_84371899.png?alt=media&#x26;token=97b84b58-d5b6-42a7-8e02-571626b5e0bc" alt=""><figcaption></figcaption></figure>

### **Step 5: Enable AI Code Review Agent on repositories**

After connecting Bito to your Bitbucket account, you'll see a list of repositories that Bito has access to.

Use the toggles in the **Code Review Status** column to **enable** or **disable** the Agent for each repository.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBopXIGtuWOCxzt8W6gDv%2Fscrnli_Nf0yfPc0l2qOe9_1.png?alt=media&#x26;token=0784b195-5887-4d30-81b6-76a62831c8e5" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To customize the Agent’s behavior, you can edit existing configurations or create new Agents as needed.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endhint %}

### **Step 6: Automated and manual pull request reviews**&#x20;

Once a repository is enabled, you can invoke the AI Code Review Agent in the following ways:

1. **Automated code review:** By default, the Agent automatically reviews all new pull requests and provides detailed feedback.
2. **Manually trigger code review:** To initiate a manual review, simply type **`/review`** in the comment box on the pull request and click **Add comment now** to submit it. This action will start the code review process.

{% hint style="info" %}
**Note:** After typing **`/review`**, add a space inside the comment box to ensure that **`/review`** is not highlighted as a Bitbucket slash command so that the comment can be posted correctly.
{% endhint %}

The AI-generated code review feedback will be posted as comments directly within your pull request, making it seamless to view and address suggestions right where they matter most.&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FfXuf3LO3sIqG6dPwz4fk%2Fscrnli_9_18_2024_8-01-14%20AM.png?alt=media&#x26;token=7b067b12-0e48-4900-89fa-878db4ace071" alt=""><figcaption></figcaption></figure>

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

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FUBoXJAhcEjR9SPwNbVKz%2Fscrnli_9_18_2024_8-43-54%20AM.png?alt=media&#x26;token=ed39dd98-bc00-4f32-9abb-27a6c0aedef7" alt=""><figcaption></figcaption></figure>

### Screenshot # 2

{% hint style="info" %}
**Changelist** showing key changes and impacted files in a pull request.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FyH8h3KVhYqjy8nSHQCby%2Fchangelist_by_bito.png?alt=media&#x26;token=99c64f3d-f554-47fd-aab7-f2d8d9994c09" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

### Screenshot # 3

{% hint style="info" %}
*AI code review feedback posted as comments on the pull request.*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJmIqJ9p3s7J67rWEMWRk%2Fscrnli_9_18_2024_8-44-53%20AM_b.png?alt=media&#x26;token=66ca75ba-35d1-40c0-961a-d550b1132d9f" alt=""><figcaption></figcaption></figure>
