# Source: https://docs.bito.ai/quickstart.md

# Quickstart

This guide will help you set up and start using Bito's AI-powered tools. Whether you're looking to enhance feedback of your coding agents with [AI Architect](https://docs.bito.ai/ai-architect/overview) or automate code reviews with our [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview), you'll find everything you need below.

### AI Architect

{% stepper %}
{% step %}

### Install AI Architect

#### Bito-hosted

1. Contact <support@bito.ai>

#### Self-hosted

1. Download from [GitHub](https://github.com/gitbito/ai-architect)
2. Run setup and configure your repositories
3. Start indexing to build knowledge graph of your codebase
4. Get your MCP server URL and access token

[Complete installation guide →](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted)
{% endstep %}

{% step %}

### Connect to your AI coding agent

You can connect AI Architect to your AI coding tools using **either an automated installer or a manual configuration**, depending on the agent and your environment.

* **Automated setup (recommended)**\
  The installer will automatically configure AI Architect for all compatible AI coding tools on your system.

  [**Quick MCP Integration Guide**](https://docs.bito.ai/ai-architect/quick-mcp-integration-with-ai-coding-agents)
* **Manual setup**

  If you prefer hands-on control over your configuration or encounter issues with automated setup, we provide detailed step-by-step guides for each supported AI coding tool:

  * [**Guide for Claude Code**](https://docs.bito.ai/ai-architect/guide-for-claude-code)
  * [**Guide for Cursor**](https://docs.bito.ai/ai-architect/guide-for-cursor)
  * [**Guide for Windsurf**](https://docs.bito.ai/ai-architect/guide-for-windsurf)
  * [**Guide for GitHub Copilot (VS Code)**](https://docs.bito.ai/ai-architect/guide-for-github-copilot-vs-code)
  * [**Guide for Junie (JetBrains)**](https://docs.bito.ai/ai-architect/guide-for-junie-jetbrains)
  * [**Guide for JetBrains AI Assistant**](https://docs.bito.ai/ai-architect/guide-for-jetbrains-ai-assistant)
    {% endstep %}
    {% endstepper %}

### AI Code Reviews in Git

{% stepper %}
{% step %}

### Sign up for Bito

Create your account at [alpha.bito.ai](https://alpha.bito.ai/home/welcome) to get started.
{% endstep %}

{% step %}

### Connect your Git provider

Select your preferred Git platform and follow the guided setup to install the agent:

* [GitHub](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-github)
* [GitHub (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-github-self-managed)
* [GitLab](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab)
* [GitLab (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-gitlab-self-managed)
* [Bitbucket](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket)
* [Bitbucket (Self-Managed)](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/guide-for-bitbucket-self-managed)

Once installed, the agent will be linked to your repositories and ready to assist.
{% endstep %}

{% step %}

### Review pull requests

The AI agent will automatically review **new pull requests** and leave inline comments with suggestions.\
You can also **manually trigger a review** by commenting `/review` on any pull request.

[See full list of available commands](https://docs.bito.ai/ai-code-reviews-in-git/available-commands)
{% endstep %}

{% step %}

### Chat with the agent

You can reply to comments posted by the Bito AI agent in a pull request to ask follow-up questions or request clarification. The agent will respond with context-aware answers to help you understand the feedback better.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/chat-with-ai-code-review-agent)
{% endstep %}

{% step %}

### Configure agent settings

To customize your agent, go to [Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) and click the **Settings** button next to the relevant agent. From there, you can choose the review feedback mode, enable or disable automatic reviews, define custom guidelines to align with your team’s standards, and more.

[Learn more](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance)
{% endstep %}
{% endstepper %}
