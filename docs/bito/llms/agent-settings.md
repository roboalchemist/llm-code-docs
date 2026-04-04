# Source: https://docs.bito.ai/ai-code-reviews-in-git/agent-settings.md

# Agent settings

Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) supports different configuration methods depending on the deployment environment:

1. **Bito-hosted** – The agent runs on Bito's infrastructure and is configured through the [Bito web UI](https://alpha.bito.ai/).
2. **Self-hosted** – The agent runs on user-managed infrastructure and is configured by editing the [`bito-cra.properties` file](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file).

The sections below provide configuration guidance for each setup.

## Bito-hosted agent configuration

In Bito-hosted AI Code Review Agent, you can configure the agent through the [Bito web UI](https://alpha.bito.ai/).

To customize an existing agent, open the [**Code Review > Repositories**](https://alpha.bito.ai/home/ai-agents/code-review-agent) page and click the **Settings** button next to the Agent instance to be modified.

The agent settings page allows configuration of options such as:

* **Agent name** – Define a unique name for easy identification.
* **Review options** – Choose the review mode (Essential or Comprehensive), set feedback language, and enable features like auto-review, incremental review, summaries, and change walkthroughs.
* **Custom guidelines** – Create and apply custom code review rules tailored to your team’s standards directly from the dashboard.
* **Filters** – Exclude specific files, folders, or branches from review to focus on relevant code.
* **Tools** – Enable additional checks, such as secret scanning and static analysis.
* **Chat** – Configure how the agent responds to follow-up questions in pull request comments and manage automatic replies.

These settings tailor the agent’s behavior to match team workflows and project needs. For detailed guidance, see [Create or customize an Agent instance](https://docs.bito.ai/ai-code-review-agent/install-run-using-bito-cloud/create-or-customize-an-agent-instance).

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="install-run-using-bito-cloud/create-or-customize-an-agent-instance">create-or-customize-an-agent-instance</a></td></tr></tbody></table>

{% embed url="<https://youtu.be/Oj4A8wd1bio>" %}

## Self-hosted agent configuration

In self-hosted deployments, configuration is managed by editing the [`bito-cra.properties` file](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file). This file defines how the agent operates and connects to required services.

Key configuration options include:

* **Mode**
  * `mode = cli`: Processes a single pull request using a manual URL input.
  * `mode = server`: Runs as a webhook service and listens for incoming events from Git platforms.
* **Authentication**
  * `bito_cli.bito.access_key`: Required for authenticating the agent with the Bito platform.
  * `git.provider`, `git.access_token`, etc.: Required for connecting to the appropriate Git provider (e.g., GitHub, GitLab, Bitbucket).
* **General feedback settings**
  * `code_feedback`: Enables or disables general feedback comments in reviews.
* **Analysis tools**
  * `static_analysis`: Enables static code analysis.
  * `dependency_check`: Enables open-source dependency scanning.
  * `dependency_check.snyk_auth_token`: Required when using Snyk for vulnerability detection.
* **Review format and scope**
  * `review_comments`: Defines output style (e.g., single post or inline comments).
  * `review_scope`: Limits the review focus to specific concerns such as security, performance, or style.
* **Filters**
  * `include_source_branches` and `include_target_branches`: Restrict reviews to pull requests that match specified source and target branch patterns.
  * `exclude_files`: Skips selected files based on glob patterns.
  * `exclude_draft_pr`: Skips draft pull requests when enabled (default: `True`).

Each property is documented in detail on the [bito-cra.properties file documentation](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) page.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Learn more</strong></mark></td><td><a href="install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file">agent-configuration-bito-cra.properties-file</a></td></tr></tbody></table>
