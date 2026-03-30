# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/webhooks-pipeline-integration/gitlab-webhooks.md

# GitLab Webhooks

OX Security integrates with GitLab webhooks to enable commit status updates and merge request comments after scans.

> **Note:** GitLab webhook integrations do not support IDP-based credentials (such as OAuth or SSO). You must use personal or group access tokens.

### Step 1: Configure webhooks in GitLab

After configuring your connector in the OX platform, create a webhook in GitLab. You can set it at the group level or project level.

| Field            | Value                                                                                                                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **URL**          | `https://api.cloud.ox.security/api/gitlab/webhooks`                                                                                                                                                                                     |
| **Secret token** | [Your OX Security integration key.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/creating-ci-cd-integration-key) |
| **Triggers**     | Enable **Merge request events** and **Push events**, depending on your needs.                                                                                                                                                           |

### Step 2: [Enable scanning with webhooks in OX Security](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/webhooks-pipeline-integration)

**For example:**

* **Commit status:** Appears as an external stage check in GitLab.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-540226aec781a3de125e8cecde4a937a1f4bb0ff%2FGL_webhook_commit_status.png?alt=media" alt="" width="353"><figcaption></figcaption></figure>

* **Merge request note:** A comment with scan details is added to the merge request.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a5c33101dcd217021e97edaa7825505373fbcae8%2FGL_webhook_merge_request_note.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
