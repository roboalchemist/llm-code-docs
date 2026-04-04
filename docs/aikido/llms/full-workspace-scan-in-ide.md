# Source: https://help.aikido.dev/ide-plugins/features/full-workspace-scan-in-ide.md

# Full Workspace Scan in IDE

The Aikido Workspace Scan lets you analyze your entire project at once, so you can quickly review security issues across all files, not just the ones you have open.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FPsJBSHcBV9fTPU7l7oD2%2Fide_full_scan.gif?alt=media&#x26;token=894aa9e1-0c1c-4c83-a7a0-226e568fadb3" alt=""><figcaption></figcaption></figure>

#### When to Use a Full Scan

Use full scans when:

* You want a security baseline for your repository.
* You’re about to push significant code changes.

For regular development, open/save scans continue to provide instant feedback as you write code.

#### Run a Full Scan

You can start a full scan directly from the Aikido panel in VS Code:

1. Open the Aikido sidebar.
2. Click Workspace Scan at the top of the view.
3. Select whether you want to scan:
   * **Entire workspace** – runs a complete analysis of all source files in your project.
   * **Changed files only** – scans only files that have been modified since your last Git commit.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FjGncndInq5deEkvFLyc1%2FScreenshot%202025-11-06%20at%2010.14.00.png?alt=media&#x26;token=0fee4efc-262b-46f6-967e-eb8d73c6009e" alt=""><figcaption></figcaption></figure>

During the scan, Aikido checks for:

* Code issues (SAST) — insecure coding patterns and misconfigurations.
* Secrets — exposed tokens, passwords, and API keys.

Results appear inline in your editor and in the Scan Results panel, grouped by category. You can hover over each finding for more details or open it in Aikido for deeper triage.

{% hint style="warning" %}
The workspace scan does not run automatically. You’ll need to start a new scan manually whenever you want updated results.&#x20;
{% endhint %}
