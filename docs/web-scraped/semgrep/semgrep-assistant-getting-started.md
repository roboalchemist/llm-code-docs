# Enable Semgrep Assistant

Source: https://semgrep.dev/docs/semgrep-assistant/getting-started

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Semgrep Assistant- Getting started**On this page- [Deployment](/docs/tags/deployment)- [Semgrep Assistant](/docs/tags/semgrep-assistant)Enable Semgrep Assistant

This article walks you through enabling Semgrep Assistant for your deployment.

Prerequisites
- You have completed a [Semgrep core deployment](/docs/deployment/core-deployment).
- You have set rules to **Comment** or **Block** mode in your [** Policies page](https://semgrep.dev/orgs/-/policies).

- Azure DevOps Cloud- Bitbucket Cloud- GitHub- GitLabSemgrep Assistant extends standard Semgrep capabilities by providing contextually aware AI-generated suggestions. Building that context requires Azure DevOps permissions, specifically code access granted through an access token you generate through Azure DevOps. Ensure that the token has the following scopes:

- `Code: Read &amp; write`
- `Pull Request Threads: Read &amp; write`
You can provide this token to Semgrep by adding [Azure DevOps as a source code manager](/docs/deployment/connect-scm#connect-to-cloud-hosted-orgs).

Semgrep recommends using a service account, not a personal account, to [generate the personal access token](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate) provided to Semgrep. Regardless of whether you use a personal or service account, the account must be assigned the **Owner** or **Project Collection Administrator** role for the organization.

Semgrep Assistant extends standard Semgrep capabilities by providing contextually aware AI-generated suggestions. Building that context requires Bitbucket permissions, specifically code access granted through an access token you generate through Bitbucket. Your token must be a [Workspace Access Token](https://support.atlassian.com/bitbucket-cloud/docs/workspace-access-tokens/), which are available to users with a Bitbucket Cloud Premium plan or higher. The token must have the following scopes:

- `Projects: Read`
- `Repositories: Read`
- `Pull requests: Read &amp; Write`
- `Webhooks: Read and write`
You can provide this token to Semgrep by [adding Bitbucket as a source code manager](/docs/deployment/connect-scm#connect-to-cloud-hosted-orgs).

Semgrep Assistant extends normal Semgrep capabilities by providing contextually aware AI-generated suggestions. In order to build that context, it requires GitHub permissions in addition to the
[** standard permissions required for Semgrep](/docs/deployment/checklist#permissions).

Semgrep Assistant requires [read access to your code in GitHub](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28). This is done through a private Semgrep GitHub app that you install during Assistant setup. This private Semgrep GitHub app:

- Is fully under your control so you can revoke access or specific permissions at any time by visiting **Settings &gt; Applications** in GitHub.
- Only accesses source code repositories on a file-by-file basis; it does not need or request org-level access to your codebase.
- Can be configured to limit its scope to specific repositories. You do not need to give read access to all repositories in your GitHub organization.
### Enable Assistant[​](#enable-assistant)
- Sign in to [Semgrep AppSec Platform](https://semgrep.dev/login).
- Click **[** Settings](https://semgrep.dev/orgs/-/settings/)**.
- In the **Assistant** section, click the **** Allow code snippets in AI prompts** toggle.
*
This launches the **Set up Semgrep Assistant** prompt.
- Select a source code manager (SCM) by clicking **github.com**.
- Semgrep provides you with information on why Assistant requires access to your source code. Click **Accept &amp; Enable Assistant** to proceed.
- You are redirected to the page where you can add a GitHub Private App that grants Semgrep read access to your code.

Enter your GitHub information. Select whether you&#x27;re installing the app on an **organization** or **Personal Account**, and provide its name.
- Click **Review permissions** to see the permissions requested by Semgrep.
- Click **Register GitHub App** to proceed.
- When prompted, click **Continue** to allow redirection to GitHub to finalize app creation. Follow the instructions to finish creating and installing a private `semgrep-app`.

- You are redirected to Semgrep AppSec Platform&#x27;s **Source Code Managers** page. Navigate back to the **General &gt; Assistant** page. Verify that all of the features are enabled:

**Allow code snippets in AI prompts**: Required for Semgrep to auto-triage findings, provide AI remediation guidance, and tag findings with code context.
- **Weekly priority emails**: Enable weekly emails to all organization admins with information on Assistant&#x27;s top three backlog tasks across all findings.
- **Noise filter for Code PR/MR comments**: Enable the filtering of findings flagged as false positives. You can choose to suppress any PR or MR comments Semgrep might push, or you can choose to show developers information regarding false positives using PR or MR comments.
- **Remediation**: Enable Assistant-generated autofix suggestions in comments from Assistant. You can also set the minimum confidence level for Assistant-written fixes if the Semgrep rule doesn&#x27;t include a human-written autofix.

Semgrep Assistant extends normal Semgrep capabilities by providing contextually aware AI-generated suggestions. In order to build that context, Semgrep Assistant requires the **API scope** to run in both GitLab SaaS and GitLab self-managed instances. This can be specified at either the [project access token level](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html) or [personal access token level](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

- You can revoke [project access tokens](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html#revoke-a-project-access-token) or [personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#revoke-a-personal-access-token) at any time.
- Semgrep Assistant only accesses source code repositories (projects) on a file-by-file basis; it does not need or request org-level access to your codebase.
- The token can be configured to limit its scope to specific projects or individuals. You do not need to give read access to all projects in your GitLab organization.
## Enable Assistant
- Sign in to [Semgrep AppSec Platform *](https://semgrep.dev/login) using your GitLab account.
- Click **[** Settings](https://semgrep.dev/orgs/-/settings/)**.
- In the **Assistant** section, click the **** Allow code snippets in AI prompts** toggle.

This launches the **Set up Semgrep Assistant** prompt.
- Follow the on-screen instructions to complete the setup process.
- Navigate back to the **Deployment** page. Under the **Assistant** section, verify that all of the features are enabled:

**Allow code snippets in AI prompts**: Required for Semgrep to auto-triage findings, provide AI remediation guidance, and tag findings with code context.
- **Weekly priority emails**: Enable weekly emails to all organization admins with information on Assistant&#x27;s top three backlog tasks across all findings.
- **Noise filter for Code PR/MR comments**: Enable the filtering of findings flagged as false positives. You can choose to suppress any PR or MR comments Semgrep might push, or you can choose to show developers information regarding false positives using PR or MR comments.
- **Remediation**: Enable Assistant-generated autofix suggestions in comments from Assistant. You can also set the minimum confidence level for Assistant-written fixes if the Semgrep rule doesn&#x27;t include a human-written autofix.

Once you have enabled Semgrep Assistant, you can [customize your deployment by enabling or disabling the Assistant features](/docs/semgrep-assistant/customize) that best fit your software development lifecycle.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Deployment](/docs/tags/deployment)- [Semgrep Assistant](/docs/tags/semgrep-assistant)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/semgrep-assistant/getting-started.md)Last updated on **Aug 13, 2025**