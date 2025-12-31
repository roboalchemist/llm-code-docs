# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance.md

# Create or customize an Agent instance

{% embed url="<https://youtu.be/Oj4A8wd1bio>" %}

[Connecting your Bito workspace to GitHub, GitLab, or Bitbucket](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/..#connect-bito-to-your-git-provider) provides immediate access to the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview). To get you started quickly, Bito offers a **Default Agent** instance—pre-configured and ready to deliver AI-powered code reviews for pull requests and code changes within supported IDEs such as VS Code and JetBrains.

While the **Default Agent** is ready for use right away, Bito also gives you the option to **create new Agent instances** or **customize existing ones** to suit your specific requirements. This flexibility ensures that the Agent can adapt to a range of workflows and project needs.

For example, you might configure one Agent to disable automatic code reviews for certain repositories, another to exclude specific Git branches from review, and yet another to filter out particular files or folders.

This guide will walk you through how to create or customize an Agent instance, unlocking its full potential to streamline your code reviews.

## Creating or customizing AI Code Review Agents&#x20;

Once Bito is connected to your GitHub/GitLab/Bitbucket account, you can easily create a new Agent or customize an existing one to suit your workflow.&#x20;

1. To **create a new Agent**, navigate to the [Code Review > Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) dashboard and click the **New Agent** button to open the Agent configuration form.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fe9yWzaBjGDsbCO0TPlE0%2Fscrnli_bfuIbaAP51Klgu.png?alt=media&#x26;token=db8e0ec4-34d8-4684-b4ad-770f36b1d10b" alt=""><figcaption></figcaption></figure>

2. If you’d like to **customize an existing agent**, simply go to the same [Code Review > Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) dashboard and click the **Settings** button next to the Agent instance you wish to modify.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FNxy8j3UEcxh947QxMj9h%2Fscrnli_4T03Igj7d1r855.png?alt=media&#x26;token=698cb777-e48f-4e1b-bbbf-9e24a317f30f" alt=""><figcaption></figcaption></figure>

Once you have selected an Agent to customize, you can modify its settings in the following areas:&#x20;

&#x20;

## 1. General settings&#x20;

### Agent name&#x20;

Assign a unique alphanumeric name to your Agent. This name acts as an identifier and allows you to invoke the Agent in supported clients using the **`@<agent_name>`** command.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FXEjUlDn834h978fCjNH0%2Fscrnli_ZCd0tIRfH725KX_1.png?alt=media&#x26;token=00e30f6d-66df-42f4-a3cb-58ad67f0eb36" alt=""><figcaption></figcaption></figure>

## 2. Customization options&#x20;

Bito provides six tabs for in-depth Agent customization.

These include:

1. Review
2. Custom Guidelines
3. Filters
4. Tools
5. Chat
6. Functional Validation

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F2GeZTPCoolZnQ3jvhFBE%2F10.png?alt=media&#x26;token=886fb830-8c2a-4402-9654-a21ccf8d48f1" alt=""><figcaption></figcaption></figure>

Let's have a look at each tab in detail.

### a. Review

In this tab, you can configure how and when the Agent performs reviews:&#x20;

* **Review language:** Select the output language for code review feedback.
  &#x20;Bito supports over 20 languages, including English, Hindi, Chinese, and Spanish. The AI code review feedback will be posted on the pull requests in the selected language.&#x20;
* **Review feedback mode:** Choose between **Essential** and **Comprehensive** review modes and tailor review request settings to fit your team's unique workflow requirements.
  * In **Essential** mode, only critical issues are posted as inline comments, and other issues appear in the main review summary under "Additional issues".
  * In **Comprehensive** mode, Bito also includes minor suggestion and potential nitpicks as inline comments.
* **Automatic review:** Toggle to enable or disable automatic reviews when a pull request is created and ready for review.&#x20;
* **Automatic incremental review:** Toggle to enable or disable reviews for new commits added to a pull request. Only changes since the last review are assessed.
  * **Batch time:** Specifies how long the AI Code Review Agent waits before running an incremental review after new commits are pushed. The value can range from **`0m` (review immediately)** to **`24h` (review after 24 hours)**. Lower values result in more frequent incremental reviews.

    **Examples:**

    * `10s` → waits **10 seconds** before running the review
    * `12m` → waits **12 minutes** before running the review
    * `1h10m` → waits **1 hour and 10 minutes** before running the review
* **Request changes comments:**  Enable this option to get Bito feedback as **"Request changes"** review comments. Depending on your organization's Git settings, you may need to resolve all comments before merging.
* **Draft pull requests:** By default, the Agent excludes draft pull requests from automated reviews. Disable this toggle to include drafts.&#x20;
* **Automatic summary:** Toggle to enable automatic generation of AI summaries for changes, which are appended to the pull request description.&#x20;
* **Change Walkthrough:** Enable this option to generate a table of changes and associated files, posted as a comment on the pull request.
* **Allow config file settings:** Enabling this setting will allow Agent Settings to be overridden at a repository level by placing a `.bito.yaml` file in the root folder of that repository. [**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/agent-settings/repo-level-settings)
* **Auto-apply agent rules:** Automatically detect and apply best-practice guidelines from agent configuration files like `CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, `.windsurf/rules`, or `GEMINI.md`. When enabled, Bito uses these files to guide its code review. [**Learn more**](https://docs.bito.ai/implementing-custom-code-review-rules#id-3-use-project-specific-guideline-files)
* **Generate interaction diagrams:** When enabled, Bito will generate interaction diagrams during code reviews to visualize the architecture and impacted components in the submitted changes. Currently, it is supported for GitHub and GitLab.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FpxtYSjIHTkO3bijBl9EO%2F1_1.png?alt=media&#x26;token=2bb7e440-4016-4533-b708-4abc4b1555bf" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FVzcTL5nQ0caUVHuKWfyb%2F2.png?alt=media&#x26;token=e47027db-2e68-4334-810f-9965addbf9f3" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKAAly95OdJxOiYDYBuUJ%2F3.png?alt=media&#x26;token=257dffd9-25cd-4add-8216-3128312463f4" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FISyUsZj0LOXlI0aR0CAT%2F4.png?alt=media&#x26;token=01bf1c7f-057e-41df-a33c-3b2829725766" alt=""><figcaption></figcaption></figure>

### b. Custom Guidelines

Create, apply, and manage custom code review guidelines to align the AI agent’s reviews with your team’s specific coding standards.

The agent will follow your guidelines when reviewing pull requests.

[**Learn more**](https://docs.bito.ai/implementing-custom-code-review-rules#id-2-create-custom-code-review-guidelines)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqmcctH3kkEwx9t59Iuny%2F5_1.png?alt=media&#x26;token=484f6982-f678-4667-b317-799ac42f64d9" alt=""><figcaption></figcaption></figure>

### c. Filters

Use filters to customize which files, folders, and Git branches are reviewed when the Agent triggers automatically on pull requests:

* **Exclude Files and Folders:** A list of files/folders that the AI Code Review Agent will not review if they are present in the diff. You can specify the files/folders to exclude from the review by name or glob/regex pattern. The Agent will automatically skip any files or folders that match the exclusion list. This filter applies to both manual reviews initiated through the **`/review`** command and automated reviews.&#x20;
* **Include Source/Target Branches:** This filter defines which pull requests trigger automated reviews based on their source or target branch, allowing you to focus on critical code and avoid unnecessary reviews or AI usage. By default, pull requests merging into the repository’s default branch are subject to review. To review additional branches, you can use the [Include Source/Target Branches filter](https://docs.bito.ai/excluding-files-folders-or-branches-with-filters#include-source-target-branches-filter). Bito will review pull requests when the source or target branch matches the list. This filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.
* **Exclude Labels:** Specify pull request (PR) labels to exclude from review by name or glob/regex pattern. The agent will skip any PRs tagged with these labels in GitHub or GitLab.

{% hint style="info" %}
For more information and examples, see [Excluding Files, Folders, or Branches with Filters](https://docs.bito.ai/ai-code-reviews-in-git/excluding-files-folders-or-branches-with-filters).
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FoDyUYEgeEgHaETBSs13m%2F6_1.png?alt=media&#x26;token=1bf3dc7f-f41e-4249-9e24-180b559287b8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FRdy2ev0LKHpQikPc8DOb%2Fscrnli_spc1zf61Vl2Olo.png?alt=media&#x26;token=4435cf84-ec24-4eac-b73c-f1cbc404d7d4" alt=""><figcaption></figcaption></figure>

### d. Tools

Enhance the Agent’s reviews by enabling additional tools for static analysis, security checks, and secret detection:&#x20;

* **Secret Scanner:** Enable this tool to detect and report secrets left in code changes.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBxRWhwG67YXEY1YzCS5X%2F7.png?alt=media&#x26;token=80f4d8dd-0afe-441f-9c2c-c76c1027a89c" alt=""><figcaption></figcaption></figure>

### e. Chat

You can chat with the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git) to ask follow-up questions, request alternative solutions, or get clarification on review comments. From this tab, you can manage how the agent responds to these interactions.

* **Auto reply:** Enable Bito to automatically reply to user questions posted as comments on its code review suggestions—no need to tag `@bitoagent` or `@askbito`.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FHlkbzLfeOebXiSPeQVDh%2F8.png?alt=media&#x26;token=0546df4a-2861-4712-82c2-1eaddc8e3a0b" alt=""><figcaption></figcaption></figure>

### f. Functional Validation

Automatically validate pull requests against Jira tickets. Ticket references are detected in the PR description, title, or branch name.

[**Learn more**](https://docs.bito.ai/ai-code-reviews-in-git/jira-integration)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqDvk5U9eGFLX3zZXJlBs%2F9.png?alt=media&#x26;token=4c202619-86c9-47d5-964b-54e82a8e3db3" alt=""><figcaption></figcaption></figure>

If you are editing an existing agent, click **Save** to apply the changes.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FhFyPs3udWaoGryZNNtIu%2Fscrnli_Dy0cDQUimhLw3F.png?alt=media&#x26;token=a7623f7c-0e0d-47a9-ab88-605ec686ca7e" alt=""><figcaption></figcaption></figure>

## 3. Select repositories for code review

1. If you are creating a new agent instance, click **Select repositories** after configuration to choose the Git repositories the agent will review.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FovkmqjzPOyWwf2grajKm%2F11.png?alt=media&#x26;token=5f66a283-5fd7-4b41-8cdd-991f04284bf3" alt=""><figcaption></figcaption></figure>

2. To enable code review for a specific repository, simply select its corresponding checkbox. You can also enable repositories later, after the Agent has been created. Once done, click **Save and continue** to save the new Agent configuration.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F4l97XCS4fu5KW3aU5H7w%2Fscrnli_D5yUG72YO9dlpi_1.png?alt=media&#x26;token=f9c1c2fd-1a2e-4303-a527-f55e549e0c13" alt=""><figcaption></figcaption></figure>

3. When you save the configuration, your new Agent instance will be added and available on the [**Code Review > Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F9EdG6H9gT3WQKHGTgMbf%2Fscrnli_P0jT2f89e9j4He.png?alt=media&#x26;token=f38b7ff1-6192-4b16-bb5d-2e5e316ae737" alt=""><figcaption></figcaption></figure>
