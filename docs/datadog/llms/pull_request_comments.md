# Source: https://docs.datadoghq.com/security/code_security/dev_tool_int/pull_request_comments.md

---
title: Pull Request Comments
description: >-
  Learn how to set up pull request comments for repositories scanned by Code
  Security.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Developer Tool Integrations > Pull
  Request Comments
---

# Pull Request Comments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Code Security posts comments directly on pull requests (PRs) in your source code management (SCM) system when vulnerabilities are detected on enabled repositories. This help you see and fix issues in context before merging code. The comments are diff-aware, meaning they only flag new issues introduced on lines modified in the PR.

There are two types of PR comments:

- **Inline comment**: Flags an individual Code Security finding on specific lines of code and suggests a remediation (if available).

  {% image
     source="https://datadog-docs.imgix.net/images/code_security/github_inline_pr_comment_light.56fc78618e068d8e89f68dd2a3952ec8.png?auto=format"
     alt="A Datadog bot has posted an inline comment on a GitHub pull request flagging a \"Critical: Code Vulnerability\". The comment suggests replacing the code os.system(command) with os.system(shlex.quote(command)) to sanitize the process call." /%}

- **Summary comment**: Combines all findings from Datadog into a single comment. This comment appears only if your PR contains issues requiring attention. After those findings are addressed, the comment is automatically edited to confirm that your PR is now clear.

  {% image
     source="https://datadog-docs.imgix.net/images/code_security/github_summary_comment_injections_light.01f2b25f02f57f28d295157c4ea13a94.png?auto=format"
     alt="A Datadog bot has posted a summary comment on a GitHub pull request. The comment has a \"Warnings\" section that lists four critical code vulnerabilities, such as SQL and command injections, with links to the specific files and lines of code." /%}

You can configure PR comments at the organization or repository level in [Repository Settings](https://app.datadoghq.com/security/configuration/code-security/settings), with the following controls:

- Enabling/disabling PR comments by scan type (SAST, static SCA, Secrets, IaC)
- Setting severity thresholds for each scan type
- Excluding findings from test files or dev/test dependencies

Learn more about [PR comments across Datadog](https://docs.datadoghq.com/integrations/guide/source-code-integration/?tab=codesecurity#pr-comments).

**Note**: PR comments are not PR checks. To set up checks, see [PR Gates](https://docs.datadoghq.com/quality_gates/?tab=staticanalysis#setup).

## Prerequisites{% #prerequisites %}

- You must have the Datadog source code integration for your provider enabled. PR comments are supported for [GitHub](https://docs.datadoghq.com/integrations/github/), [GitLab](https://docs.datadoghq.com/integrations/gitlab-source-code/), and [Azure DevOps](https://docs.datadoghq.com/integrations/azure-devops-source-code/#source-code-functionality) repositories.
- Your repositories must have the relevant Code Security product(s) enabled. To enable Code Security in-app, navigate to the [**Code Security** Settings page](https://app.datadoghq.com/security/configuration/code-security/setup).

{% alert level="info" %}
PR comments are not supported for pull requests in public repositories, or on pull requests targeting a destination branch in a different repository from the source branch (that is, forked repositories trying to merge into the main repository).
{% /alert %}

## Set up pull request comments{% #set-up-pull-request-comments %}

Follow the steps below based on your source code management provider.

{% tab title="GitHub" %}

{% alert level="info" %}
If you are using Datadog-hosted scanning, enable the toggle for your desired scan type (for example, Static Code Analysis (SAST)) after completing the GitHub setup steps. If you are using [GitHub Actions](https://docs.datadoghq.com/security/code_security/static_analysis/github_actions/) to run your scans, trigger the action on `push` for comments to appear once the GitHub setup is complete.
{% /alert %}

### Connect your GitHub account(s) to Datadog{% #connect-your-github-accounts-to-datadog %}

For setup instructions, read the [Datadog GitHub source code integration](https://docs.datadoghq.com/integrations/github/) documentation.

### Create or update a GitHub App{% #create-or-update-a-github-app %}

If you already have a GitHub App connected to Datadog, update it. Otherwise, create a new GitHub App.

{% alert level="info" %}
The permissions you grant to the GitHub App determine which [GitHub integration](https://docs.datadoghq.com/integrations/github/) features are available for setup.
{% /alert %}

#### Create and install a GitHub App{% #create-and-install-a-github-app %}

1. In Datadog, navigate to [**Integrations > GitHub Applications > Add New GitHub Application**](https://app.datadoghq.com/integrations/github/add).

1. Fill out any required details, such as the GitHub organization name.

1. Under **Select Features**, check the **Code Security: Pull Request Review Comments** box.

1. Under **Edit Permissions**, verify that the **Pull Requests** permission is set to **Read & Write**.

1. Click **Create App in GitHub**.

1. Enter a name for your app, and submit it.

1. Click **Install GitHub App**.

1. Choose which repositories the app should be installed into, then click **Install & Authorize**.

   {% image
      source="https://datadog-docs.imgix.net/images/ci/static-analysis-install-github-app.20998ca8474fa8e4f3e096ddb823a5a1.png?auto=format"
      alt="GitHub App installation screen" /%}

#### Update an existing GitHub App{% #update-an-existing-github-app %}

1. In Datadog, navigate to [**Integrations > GitHub Applications**](https://app.datadoghq.com/integrations/github/configuration), and search for the GitHub App you want to use for Code Security.

   {% image
      source="https://datadog-docs.imgix.net/images/ci/static-analysis-existing-github-app.a6d765f608e1d6d15c1ed6a4bb4420d3.png?auto=format"
      alt="Example of a Static Code Analysis comment on a pull request" /%}

1. On the **Features** tab, look at the **Code Security: Pull Request Comments** section to determine whether your GitHub App needs additional permissions. If so, click **Update permissions in GitHub** to edit the app settings.

1. Under **Repository permissions**, set the **Pull Requests** access to **Read and write**.

   {% image
      source="https://datadog-docs.imgix.net/images/ci/static-analysis-pr-read-write-permissions.e278d572519092019f660c91088d18a4.png?auto=format"
      alt="The dropdown for the pull request read and write permission" /%}

1. Under the **Subscribe to events** heading, check the **Pull request** box.

   {% image
      source="https://datadog-docs.imgix.net/images/ci/static-analysis-pr-review-comment.2df7886ef18da37fad9ea759f9bcec3d.png?auto=format"
      alt="The checkbox for the pull request review comment permission" /%}

{% /tab %}

{% tab title="GitLab" %}
See the [GitLab Source Code](https://docs.datadoghq.com/integrations/gitlab-source-code/) setup instructions to connect GitLab repositories to Datadog.
{% /tab %}

{% tab title=" DevOps" %}
See the [Azure source code setup instructions][9] to connect Azure DevOps repositories to Datadog.
{% /tab %}

## Configuration options{% #configuration-options %}

Before enabling PR comments, ensure that **at least one Code Security scan capability is enabled in the repository.** Even if PR comments are configured at the organization level, they are only added in repositories where a supported scan type (for example, SAST, SCA, or IaC) is active. Repositories without any enabled scan types will not receive PR comments.

PR comments can be configured at the organization level or at the repository level:

- **Organization level:** Settings apply to all repositories in the organization that have at least one scan capability enabled.
- **Repository level:** Settings override the organization defaults for the selected repository.

When configuring PR comments, you can:

- Enable or disable comments for specific scan types (SAST, SCA, IaC).
- Set minimum severity thresholds to control when comments appear.
- Exclude comments for findings in test files or dev/test dependencies to avoid noise from low-priority issues.

## Configure PR comments at the organization level{% #configure-pr-comments-at-the-organization-level %}

1. In Datadog, navigate to [**Security** > **Code Security** > **Settings**](https://app.datadoghq.com/security/configuration/code-security/settings).
1. In **Repository Settings**, click **Global PR Comment Configuration**.
1. Configure the settings:
   - **Enable PR comments for all scan types and severities**: Enable this to apply PR comments across all types and severities.
   - **Enable for Static Analysis (SAST)**: Toggle this option to enable PR comments for SAST. If enabled, specify a minimum severity threshold. Additionally, select **Exclude PR comments if violations are detected in test files** to prevent comments on issues found in test files.
   - **Enable for Software Composition Analysis (SCA)**: Toggle this option to enable PR comments for SCA. If enabled, specify a minimum severity threshold. Additionally, select **Exclude PR comments if violations are detected in test or dev dependencies** to prevent comments on issues found in dependencies existing only in development or test environments.
   - **Enable for Infrastructure-as-Code (IaC)**: Toggle this option to enable PR comments for IaC. If enabled, specify a minimum severity threshold.
1. Click **Save**.

## Configure PR comments at the repository level{% #configure-pr-comments-at-the-repository-level %}

1. In Datadog, navigate to [**Security** > **Code Security** > **Settings**](https://app.datadoghq.com/security/configuration/code-security/settings).
1. In **Repository Settings**, select a repository from the list.
1. Configure the settings:
   - **Enable PR comments for all scan types and severities**: Enable this to apply PR comments across all types and severities.
   - **Enable for Static Analysis (SAST)**: Toggle this option to enable PR comments for SAST. If enabled, specify a minimum severity threshold. Additionally, select **Exclude PR comments if violations are detected in test files** to prevent comments on issues found in test files.
   - **Enable for Software Composition Analysis (SCA)**: Toggle this option to enable PR comments for SCA. If enabled, specify a minimum severity threshold. Additionally, select **Exclude PR comments if violations are detected in test or dev dependencies** to prevent comments on issues found in dependencies existing only in development or test environments.
   - **Enable for Infrastructure-as-Code (IaC)**: Toggle this option to enable PR comments for IaC. If enabled, specify a minimum severity threshold.
   - **Block all comments in this repository**: Enable this to disable all comments for this repository, overriding global settings.
1. Click **Save Configuration**.
