# Source: https://help.aikido.dev/aikido-autofix/ai-autofix-for-sast-and-iac-issues.md

# AutoFix for SAST and IaC Issues

{% hint style="info" %}
Aikido Local Scan accounts DO NOT have access to AutoFix within the UI, but it is available for the IDE plugins.&#x20;
{% endhint %}

The goal of Aikido has always been to save you time by reducing noise, focusing on the issues that truly matter. With the introduction of the **AI Autofix** feature, Aikido takes this one step further.

### Key Features of AI Autofix <a href="#key-features-of-ai-autofix" id="key-features-of-ai-autofix"></a>

* **Preview Changes:** Review detailed previews of AI-generated fixes before implementing them to ensure alignment with your standards.
* **Create Pull Requests (PRs):** Generate pull requests directly in your Source Control Management (SCM) system from the Autofix interface.
* **Direct IDE Integration:** Apply fixes instantly to your codebase via the VS Code integration, saving even more time.

  ![AI-generated patch enhances JSONP security by escaping callback, mitigating XSS vulnerabilities in PHP code.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-32d5b1e5f89adb77c5e011267240e20e6c00eff6%2Fai-autofix-for-sast-and-iac-issues_859a9d47-c060-4244-8c32-89fff802c11e.png?alt=media)

***

### Important Info <a href="#important-info" id="important-info"></a>

* **We do not use your code for training / fine-tuning**
  * Code snippets required for generating fixes are securely transmitted to **AWS Bedrock** over encrypted channels. Aikido **nor** [AWS Bedrock](https://aws.amazon.com/bedrock/security-compliance/) use your code for training or fine-tuning AI models.
* **Speed**
  * Simple fixes are typically generated in under 5 seconds. Larger or more complex fixes may take up to 30 seconds, depending on file size and issue complexity.
* **Confidence Levels**
  * Fixes are categorized into confidence levels: **High**, **Medium**, and **Low**. Manual reviews before merging are recommended.

    ![Low confidence warning: Further validation of similar fixes needed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-039f56ad7b2a1eda8cae600b1e4402982b967d7b%2Fai-autofix-for-sast-and-iac-issues_2c623f8c-0bb2-444c-8071-d957e38e3f99.png?alt=media)

***

### How to use the AI Autofix functionality <a href="#how-to-use-the-ai-autofix-functionality" id="how-to-use-the-ai-autofix-functionality"></a>

* **Step 1**. Navigate to the SAST or IaC [Autofix Page. ](https://app.aikido.dev/issues/fix/sast)All potential fixes are grouped by type and location.

  ![Aikido Autofix dashboard showing critical SAST issues and options to fix or preview autofix.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1f1e7e39971f879388f73f4b415bcd7ea90a1c9d%2Fai-autofix-for-sast-and-iac-issues_2b801f85-4354-421b-b93d-7ff66d316815.png?alt=media)
* **Step 2.** Select one or multiple fixes to preview or create a PR for.

  ![Security scan identifies path traversal vulnerabilities in two PHP files, both with medium severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-bc47688addc5daf0d7d1ef2acd6c32ca8417f569%2Fai-autofix-for-sast-and-iac-issues_b9f2fa3e-053f-492c-8a1d-3f0ed3b90a2c.png?alt=media)
* **Step 3.** Preview and Apply.
  * **Create a PR**: Automatically generate a pull request in your SCM.
  * **Apply Directly**: Instantly implement the fix in your codebase via VS Code integration.

![Code patch preview adding file path validation to prevent path traversal vulnerabilities in PHP files.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a3256e43dbf04ebeaeaabe46c0b4d48693d20276%2Fai-autofix-for-sast-and-iac-issues_f6ac142a-2711-4ce2-b4d4-db6ae64938b2.png?alt=media)

***
