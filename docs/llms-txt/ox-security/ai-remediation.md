# Source: https://docs.ox.security/fix-with-ox/ai-remediation.md

# AI Remediation

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

OX AI Remediation allows fixing security issues faster and more efficiently by providing tailored and AI-generated fix suggestions directly in your workflows.

Instead of receiving general guidance, you can now get precise recommendations and even ready-to-apply code changes based on the exact issue information, as follows:

* Providing a detailed explanation and fix per occurrence of the issue in case of aggregations.
* Generating suggested code changes automatically.
* Allowing developers to apply fixes directly from the Git platform and IDE.

### Supported Issue Types

Currently available for a subset of Code Security issues, specifically focused on JavaScript, Java, Python, C#, and with a severity level of Medium or higher.

## How It Works

1. **Issue Detection and Aggregation:** When OX detects a security issue in the code, it identifies all occurrences (aggregations). Each aggregation is analyzed separately to generate a contextual explanation and fix.
2. **AI-Generated Fixes:** For each issue, AI generates a fix suggestion tailored to the specific code segment. The suggestion includes a description, a recommendation, and a remediation proposal.
3. **Your Actions:** Depending on the interface.

### **AI suggestions in Git (GitHub, GitLab)**

AI suggestions are added as comments in the pull/merge request.

* **Commit Suggestion:** Applies the fix directly.
* **Add Suggestion to Batch:** Collects multiple fixes to apply in one commit.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2b25c1ad4e143d049c6e24c136fb4d1e010a6ed9%2FAI_Remediation_in_Git.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### **AI suggestions in IDE Extension**

Issues appear with the full AI-generated description and fix.\
You can apply the fix for each aggregation from within the environment.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0657a2d0fdd11b522f973c54d8e2a237289d7d52%2FAI_Remediation_in_IDE.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### **AI suggestions in OX UI**

1. In the **Active Issues** page, go to **Filters** and select **Actions > AI Codefix Available**.
2. Select an issue for which you want to get suggestions and go to issue's **Commits**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-12631cd2011e7d2c6b7fc0d6e4029095dab3968a%2FAI_Remediation_in_OX_UI%201.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select a fix for the specific commit. AI Remediation suggestion appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0cb1fe990605a46eb173c17e2388ac7775a2b650%2FAI_Remediation_in_OX_UI.png?alt=media" alt=""><figcaption></figcaption></figure>

## Disabling AI Remediation

The capability is enabled by default for customers who have requested access to this beta version. You can disable it at any moment.

**To disable AI Remediation:**

1. In the OX platform, go to **Settings > AI**.
2. In the **AI Settings** tab, disable the option that you want.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e361fb43437243ce727dc288b1635c16779afc38%2FDisable_AI_Remediation%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

> **Note:** Refer to [AI Privacy](https://docs.ox.security/fix-with-ox/ai-remediation/ai-privacy) for information on AI Remediation capability privacy.
