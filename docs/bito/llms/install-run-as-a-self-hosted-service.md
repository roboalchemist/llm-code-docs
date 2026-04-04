# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service.md

# Install/run as a self-hosted service

The self-hosted AI Code Review Agent offers a more private and customizable option for teams looking to enhance their code review processes within their own infrastructure, while maintaining complete control over their data. This approach is ideal for organizations with specific compliance, security, or customization requirements.

## Understanding CLI vs webhooks service

When setting up the AI Code Review Agent, you have the flexibility to choose between two primary modes of operation: **CLI** and **webhooks service**.

* **CLI** allows developers to manually initiate code reviews directly from terminal. This mode is ideal for quick, on-demand code reviews without the need for continuous monitoring or integration.
* **Webhooks service** transforms the Agent into a persistent service that automatically triggers code reviews based on specific events, such as pull requests or comments on pull requests. This mode is suitable for teams looking to automate their code review processes.

For more details, visit the [**CLI vs webhooks service**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/cli-vs-webhooks-service) page.

## Deployment Options

Based on your needs and the desired integration level with your development workflow, choose one of the following options to install and run the AI Code Review Agent:

{% hint style="info" %}
Before proceeding, ensure you've completed all necessary [**prerequisites for self-hosted**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/prerequisites) AI Code Review Agent.
{% endhint %}

1. [**Install/run via CLI**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-cli): Ideal for developers seeking a simple, interactive way to conduct code reviews from the command line.
2. [**Install/run via webhooks service**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-webhooks-service): Perfect for teams looking to automate code reviews through external events, enhancing their CI/CD workflow.
3. [**Install/run via GitHub Actions**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-github-actions): A great option for GitHub users to seamlessly integrate automated code reviews into their GitHub Actions workflows.
