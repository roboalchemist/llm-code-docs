# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/webhooks-pipeline-integration.md

# Webhooks Pipeline Integration

You can configure source control systems to notify OX using a webhook on relevant events. Webhooks can be set up once for each group or project.

This method is useful for customers managing many repositories or using UI-driven CI/CD.

Webhook settings control how OX interacts with your source control system to report scan statuses and trigger scans automatically.

These settings define whether OX sends status updates, such as scan started/finished, back to the platform, and which branch events trigger scans.

**To set webhooks:**

1. Go to the **Applications** page and select the applications in which you want to apply pipeline scan.
2. Click the **Pipeline Settings icon** at the top.
3. In the **Webhooks** section of the **Pipelines** dialog, perform webhook configuration by source control platform, as follows:

   * For GitLab Webhooks integration, enable **GitLab Commit Status and Merge Request Notes Reporting**.

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-937254487c35c4954a67f68e0994023a652e3072%2FGitLab_webhook.png?alt=media" alt=""><figcaption></figcaption></figure>

   * For GitHub App integration, enable **GitHub Checks**.

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b459935debb998df3808eef411249631337bac63%2FGH_webhook_enable.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

   * For Bitbucket App integration, enable **Bitbucket Code Insights and Build Status Reporting**.

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e51ab4471cc43bf3b3871071a720f1cd2c263910%2FBB_webhooks_enable%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
4. Define which branches and events to monitor. You can use default options (e.g., `main`, `protected`) or patterns like `release-*`.

| Setting                        | Description                                                                                                                                 | Recommendation                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Branch Event Types to Scan     | Specifies the types of branch events (Push, Pull Request) that trigger scans.                                                               | Choose Pull Request for protected/default branches. Customize for others as needed. |
| Branch Filters (Name Patterns) | Define naming patterns for branches to include in scan events. You can use wildcard (`*`) to include multiple branches with similar naming. | Use this to scan custom branch types, e.g., `release-*` or `feature-*`.             |

1. Select **SAVE**.
