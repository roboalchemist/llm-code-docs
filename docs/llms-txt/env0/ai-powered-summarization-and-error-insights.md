# Source: https://docs.envzero.com/guides/admin-guide/environments/ai-powered-summarization-and-error-insights.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ai Powered Summaries & Error Insights

> Use AI-powered error insights and plan/apply summarization in env zero to debug deployments faster

env zero offers AI-generated insights, helping your day to day work, analyzing what has occurred in your deployments in env zero. You can use AI to help analyze the cause of an error in a deployment, or summarize what has occurred in that deployment

### AI-Powered Error Insights

When an error occurs in your deployment logs, env zero can analyze it, explain what the error means and what's the likely cause of the error, and suggest possible ways to resolve it. Error Insights could help you save time when debugging and fixing IaC issues and errors, and is especially helpful with people who are not well-versed in that IaC.

If an Error Insight is available, an "Ask AI" button will appear next to the error message. Clicking this button will generate an AI-powered explanation and potential fixes.

<img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/04/99ea503fa335cf129ffc8701de88003328a8923a6b179b8ada3869402519551d-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=e6d979a0c5ca00380fc821fd06bb11cb" alt="" width="2776" height="968" data-path="images/changelogs/2025/04/99ea503fa335cf129ffc8701de88003328a8923a6b179b8ada3869402519551d-image.png" />

<img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/04/5eb0f795df37bb2cc197b659c1a2b25cb005b4138e6611cf99d17739dba32a8b-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=d118b0c12a4d717f4e9c32016b7098fc" alt="" width="2892" height="1928" data-path="images/changelogs/2025/04/5eb0f795df37bb2cc197b659c1a2b25cb005b4138e6611cf99d17739dba32a8b-image.png" />

### AI-Powered Plan and Apply Summarization

For successful OpenTofu, Terraform, and Terragrunt plan/apply runs, env zero can generate a summary highlighting the most important changes. The summary can help you have a better picture of what are the expected or performed run changes to your cloud resources, help you identify specific things that require a closer look, and in general - help you gain a better understanding of the resource changes faster

In plan logs, the summary provides an overview of proposed infrastructure modifications, highlighting any significant or sensitive changes, and offers recommendations for the configuration or for things to look out for.

In apply logs, the summary highlights the changes that were successfully applied, how they were applied compared to the plan, and additional insights.

If summarization is available, a "Summarize" button will be shown in the respective logs.

<img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/04/6abfc950ed31ebeb4043037fdf182cb49a836f824ae0a0e24ad11aa9be8bafcf-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=ec6fab3ff452536f66ee9e53ca24c750" alt="" width="2724" height="874" data-path="images/changelogs/2025/04/6abfc950ed31ebeb4043037fdf182cb49a836f824ae0a0e24ad11aa9be8bafcf-image.png" />

<img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/04/74826f277c87ee85f50364a0886472c9f4329e0784721db3dc70b1d07521b94d-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=f33c9f3ebed33c012c92a276686f56a4" alt="" width="2914" height="1928" data-path="images/changelogs/2025/04/74826f277c87ee85f50364a0886472c9f4329e0784721db3dc70b1d07521b94d-image.png" />

#### Security and Privacy

When the feature is enabled, and when an AI-Powered Summary or Error Insight is explicitly requested, env zero leverages AI in order to analyze deployment specific data relevant for the analysis. This includes the error message and the command that ran, environment variables with redacted values for sensitive variables, the plan file, and apply command logs.

All data is used solely by env zero, never shared with third parties or used for training models.

Built with [Mintlify](https://mintlify.com).
