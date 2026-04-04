# Source: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/llms.txt

# Amazon Q Developer User Guide

> User Guide for Amazon Q Developer.

- [What is Amazon Q Developer?](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html)
- [With the Q CLI](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line.html)
- [In chat applications](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-chat-applications.html)
- [Supported Regions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/regions.html)
- [Amazon Q Developer service rename](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/service-rename.html)
- [Document history](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/getting-started-q-dev.html)

- [Tiers of service](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-tiers.html): With Amazon Q Developer, you either use Amazon Q Developer at the Free or Pro tier.
- [Get started with a personal account](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/getting-started-builderid.html): If you want to use Amazon Q Developer for personal projects, and you don't need to administer other users, you'll want to get started with a personal account, also known as a Builder ID.

### [Get started with IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/getting-started-idc.html)

IAM Identity Center is a service that is used by administrators to manage the identities of end users.

- [Step 1: Choose a deployment option](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/deployment-options.html): Before you can subscribe users, you'll need to decide which AWS account or accounts you'll be working in.

### [Step 2: Subscribe users](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/subscribe-users.html)

After choosing a deployment option as described in , you are ready to subscribe workforce users.

- [In a standalone account](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/subscribe-standalone.html): Learn how to subscribe yourself (and a few others) to Amazon Q Developer Pro if you have a standalone AWS account.
- [In a management account](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/subscribe-management.html): Learn how to subscribe users to Amazon Q Developer Pro if you have an AWS management account.
- [In a member account](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/subscribe-member.html): Learn how to subscribe users to Amazon Q Developer Pro if you have an AWS member account.

### [Pro tier subscriptions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-general.html)

An Amazon Q Developer Pro subscription, also called a Pro tier subscription, is a paid version of the Amazon Q Developer service.

- [Supported Regions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-regions.html): Region information for the Pro tier varies depending on whether you're an end-user with a personal account (Builder ID), or you're an administrator of IAM Identity Center workforce users.
- [Subscription billing](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/tracking-across-org-cost-usage.html): Billing information for the Pro tier varies depending on whether you're an end-user with a personal account (Builder ID), or you're an administrator of IAM Identity Center workforce users.
- [Subscription statuses](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-status.html): Subscription status information varies depending on whether you're an end-user with a personal account (Builder ID), or you're an administrator of IAM Identity Center workforce users.
- [Finding the Start URL](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/manage-account-details.html)
- [Managing the encryption method](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/manage-encryption.html)

### [Q Developer profile](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/subscribe-understanding-profile.html)

Learn about the Amazon Q Developer profile and how it's used within the context of a Amazon Q Developer Pro deployment.

- [Creating the profile](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/subscribe-create-profile.html): Learn how to create the Amazon Q Developer profile.
- [Deleting the profile](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/subscribe-delete-profile.html): Learn how to safely delete the Amazon Q Developer profile.
- [Enabling profile sharing](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-profile-sharing.html)

### [Troubleshooting subscriptions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-troubleshooting.html)

Learn how to resolve common issues with Amazon Q Developer Pro subscriptions, including user access problems, activation emails, and subscription usage across AWS environments.

- [Unable to subscribe users](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/unable-to-subscribe-standalone.html): Resolve issues preventing you from subscribing users to Amazon Q Developer Pro, including permission problems, region availability, and account configuration challenges.
- [Users not receiving activation emails](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/users-not-receiving-emails.html): Troubleshoot issues with Amazon Q Developer Pro activation emails not reaching users, including email configuration problems and delivery delays.
- [Users unable to use their subscription on AWS websites](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/unable-to-use-pro-on-websites.html): Solve problems preventing users from accessing Amazon Q Developer Pro features on AWS websites and the console, including identity configuration issues and subscription activation delays.
- [Users unable to use their subscription in the IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/unable-to-use-pro-in-ide.html): Resolve issues preventing users from accessing Amazon Q Developer Pro features within integrated development environments (IDEs), including authentication problems and subscription activation delays.
- [Can't see subscribed users](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/users-not-appearing.html): Resolve the issue where you can't see users that you've subscribed to Amazon Q Developer Pro.
- [Viewing an aggregate list of subscriptions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/subscribe-visibility.html): If you have an organization managed by AWS Organizations, you can configure Amazon Q to display an aggregated list of Amazon Q Developer Pro subscriptions across all the accounts in your organization.
- [Unsubscribing](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-unsubscribe.html): How you unsubscribe from the Pro tier depends on whether you're an end-user with a personal account (Builder ID) or an administrator of IAM Identity Center workforce users.
- [Upgrading to the Pro tier](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/upgrade-to-pro.html): How you upgrade to the Pro tier from the Free tier depends on whether you're an end-user with a personal account (Builder ID) or whether you're an administrator of IAM Identity Center workforce users.
- [Upgrade to Kiro](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/upgrade-to-kiro.html): The Amazon Q Developer CLI has been rebranded to Kiro.


## [On AWS](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-on-aws.html)

### [Chatting about AWS](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-with-q.html)

- [Using Q artifacts in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-artifacts.html): Amazon Q artifacts enable Amazon Q to deliver responses enriched with table and chart visualizations.
- [Chatting about your resources](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-actions.html): Amazon Q Developer answers questions about your AWS account resources to help you understand your AWS infrastructure through natural language prompts.
- [Asking Amazon Q to troubleshoot your resources](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-actions-troubleshooting.html): In the AWS Management Console, you can ask Amazon Q to troubleshoot issues you're having with your AWS resources.
- [Chatting about your costs](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-costs.html): Amazon Q Developer is a generative artificial intelligence (AI) powered conversational assistant that can help you understand, build, extend, and operate AWS applications.
- [Chatting about your network security](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-network-security.html)
- [Chatting about email sending](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-email.html): Amazon Q can help you set up email sending in Amazon Simple Email Service (Amazon SES), helping you to optimize your sending delivery and engagement rates, and troubleshoot sending problems.
- [Chatting about your telemetry and operations](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-ops.html): Amazon Q analyzes your CloudWatch telemetry and operational data to help manage your AWS environment.

### [Using plugins](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/plugins.html)

Amazon Q Developer integrates with third party monitoring tools and security platforms so you can access your AWS application insights without leaving the AWS builder environment.

- [CloudZero](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/cloudzero-plugin.html): CloudZero is a cloud cost optimization platform that evaluates costs to improve cloud efficiency.
- [Datadog](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/datadog-plugin.html): Datadog is a monitoring and security platform that provides infrastructure, application, and network monitoring and analytics.
- [Wiz](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/wiz-plugin.html): Wiz is a cloud security platform that provides security posture management, risk assessment and prioritization, and vulnerability management.
- [Console-to-Code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/console-to-code.html)
- [Diagnosing console errors](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/diagnose-console-errors.html): Learn how to diagnose common console errors with Amazon Q Developer.â
- [Chatting with Support](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/support-chat.html): Learn how to contact and then chat with Support by using Amazon Q Developerâ.


## [In your IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html)

- [Installing Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html): Learn how to set up Amazon Q Developer in an IDE.

### [Chatting about code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-chat.html)

Learn how to chat with Amazon Q Developerâ in IDEs.

### [Reviewing code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-reviews.html)

Describes how to run code reviews with Amazon Q and how to address generated code issues.

- [Starting a review](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/start-review.html): Learn how to start an auto-review or a project or file code review with Amazon Q

### [Addressing code issues](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/address-code-issues.html)

Learn how to address code issues generated by Amazon Q code reviews.

- [Address issues in JetBrains and Visual Studio Code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/address-issues-jetbrains-visualstudiocode.html): Learn how to address code issues in JetBrains and Visual Studio Code IDEs.
- [Address issues in Visual Studio](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/address-issues-visualstudio.html): Learn how to address code issues in Visual Studio.
- [Filtering code issues](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/filter-code-issues.html)
- [Code issue severity](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-issue-severity.html): Learn more about how code issue severity in Amazon Q code reviews is determined and what each severity level means.

### [Transforming code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transform-in-IDE.html)

Amazon Q Developer can transform your code in integrated development environments (IDEs) by performing automated language and operating system (OS)-level upgrades and conversions.

### [Transforming Java applications](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transform-java.html)

### [Upgrading Java versions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-transformation.html)

Upgrade Java applications with Amazon Q Developer

- [How it works](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/how-CT-works.html): Learn more about Amazon Q Developer upgrades Java applications.â
- [Converting embedded SQL](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transform-sql.html): The Amazon Q Developer agent for code transformation in the IDE can help you convert embedded SQL to complete Oracle to PostgreSQL database migration with AWS Database Migration Service (AWS DMS).

### [Transforming code on the command line](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transform-CLI.html)

You can transform your applications from the command line with the Amazon Q Developer command line transformation tool.

- [Running a transformation on the command line](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/run-CLI-transformations.html): Complete these steps to transform your code on the command line with the Amazon Q Developer command line tool.
- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/troubleshooting-CLI-transformations.html): The following information can help you troubleshoot common issues when transforming applications on the command line with Amazon Q Developer.
- [Version history](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transform-CLI-versions.html): Review the following information for details about current and past releases of the Amazon Q Developer command line transformation tool.
- [Viewing job history](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transformation-job-history.html): View and manage your Java transformation job history in IDEs and the command line.
- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/troubleshooting-code-transformation.html): The following information can help you troubleshoot common issues when transforming Java applications with Amazon Q Developer.

### [Transforming .NET applications](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transform-dotnet-IDE.html)

Learn how to port Windows-based .NET applications to Linux-compatible cross-platform .NET applications with Amazon Q Developer.

- [Porting a .NET application](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/port-dotnet-application.html): Learn how to port a .NET application with Amazon Q Developer in Visual Studio
- [How it works](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/how-dotnet-transformation-works.html): Learn more about how Amazon Q Developer transforms .NET applications in the IDE.
- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/troubleshooting-dotnet-transformation-IDE.html): Learn how to troubleshoot issues when transforming .NET applications in the IDE with Amazon Q Developer
- [Explaining and updating code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/explain-update-code.html): Explain, refactor, optimize, and fix code with Amazon Q. â
- [Chatting inline](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-inline-chat.html): Learn how to chat with Amazon Q Developerâ in your IDE's main coding window using the inline chat feature.

### [Adding context to the chat](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/ide-chat-context.html)

When you chat with Amazon Q in the integrated development environment (IDE), you can provide Amazon Q with additional context, such as files and folders, that Amazon Q can use to tailor and improve its answers.

- [Adding workspace context](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/workspace-context.html): When you chat with Amazon Q in the integrated development environment (IDE), you can add @workspace to your question to automatically include the most relevant chunks of your workspace code as context.
- [Saving prompts](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/context-prompt-library.html): You can build a library of common prompts that you can use when chatting with Amazon Q in the IDE.
- [Pinning context items](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/context-pinning.html)
- [Creating project rules](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/context-project-rules.html): You can build a library of project rules that you can use when chatting with Amazon Q in the IDE.
- [Generating a memory bank](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/context-memory-bank.html): Amazon Q can automatically generate memory bank files that provide a quick index of your project's structure, technology stack, and product information.
- [Chat history compaction](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/ide-chat-history-compaction.html): Learn how to use chat history compaction to manage context window limits when chatting with Amazon Q Developer in your IDE.
- [Managing conversations](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/ide-chat-conversation.html): When you chat with Amazon Q in the integrated development environment (IDE), Amazon Q saves each of your chat tabs as a separate conversation.
- [Using shortcut keys in chat](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-ides-chat-shortcuts.html): Amazon Q provides keyboard shortcuts to help you interact with the agentic chat interface efficiently.
- [Selecting models](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-ides-chat-models.html): You can select the model you want Amazon Q to use while chatting in the IDE.

### [Generating inline suggestions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/inline-suggestions.html)

Amazon Q can provide you with code recommendations in real time.

### [Suggestions in AWS coding environments](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/setting-up-AWS-coding-env.html)

AWS coding environments with Amazon Q Developer

- [Amazon SageMaker AI Studio](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/sagemaker-setup.html): You can chat with Amazon Q inside Amazon SageMaker AI Studio.
- [JupyterLab](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/jupyterlab-setup.html): This page describes how to set up and activate Amazon Q Developer for JupyterLab.
- [Amazon EMR Studio](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/emr-setup.html): This page describes how to set up and activate Amazon Q Developer for Amazon EMR Studio.
- [AWS Glue Studio](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/glue-setup.html): This page describes how to set up and activate Amazon Q Developer for AWS Glue Studio Notebook.
- [AWS Lambda](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/lambda-setup.html): How to activate Amazon Q Developer in the Lambda console.
- [With other services](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/other-setup.html)
- [Using shortcut keys](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/actions-and-shortcuts.html): User actions in Amazon Q
- [Using code references](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-reference.html): Describes how to read code references in Amazon Q.

### [Code examples](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/inline-suggestions-code-examples.html)

Code examples for Amazon Q

- [Single-line code completion](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/single-line-completion.html): When you start typing out single lines of code, Amazon Q makes suggestions based on your current and previous inputs.
- [Full function generation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/full-function-generation.html): Amazon Q can generate an entire function based on a comment that you've written.
- [Block completion](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-block.html): Block completion is used to complete your if/for/while/try code blocks.
- [Docstring, JSDoc, and Javadoc completion](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/docstring-javadoc.html): Amazon Q can help you generate or complete documentation inside your code.
- [Line-by-line recommendations](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/line-by-line-1.html): Depending on your use case, Amazon Q may not be able to generate an entire function block in one recommendation.
- [Supported languages](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-language-ide-support.html): You can use the following features of Amazon Q Developer in the IDE with any programming language:


## [Using MCP](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/qdev-mcp.html)

- [MCP overview](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/qdev-mcp-overview.html): MCP (Model Context Protocol) is an open protocol that standardizes how AI assistants communicate with external tools.
- [In the CLI](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-mcp-config-CLI.html): This page covers CLI-specific options for configuring MCP servers.
- [With the IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/mcp-ide.html): This page covers IDE-specific options for configuring MCP servers.
- [MCP security](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-mcp-security.html): When using MCP servers with Amazon Q Developer CLI, it's important to understand the security implications and best practices.
- [MCP governance](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/mcp-governance.html): Pro-tier customers using IAM Identity Center as the sign-in method can control MCP access for users within their organization.


## [Third-party integration](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/third-party-integration.html)

### [GitLab Duo](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/gitlab-with-amazon-q.html)

GitLab Duo with Amazon Q provides a suite of artificial intelligence (AI) experiences, such as propose code implementation for your idea, review merge requests for quality and vulnerabilities, and suggest unit tests.

- [GitLab Duo concepts](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/gitlab-concepts.html): Here are some concepts and terms to know when using GitLab Duo with Amazon Q.
- [Getting started](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/gitlab-getting-started.html): GitLab Duo with Amazon Q brings artificial intelligence (AI) capabilities directly into your software development operations and source code management workflows.
- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/gitlab-troubleshooting.html): Consult the following section to troubleshoot common onboarding problems when using GitLab Duo with Amazon Q.

### [GitHub (Preview)](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/amazon-q-for-github.html)

- [Quickstart](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/github-quickstart.html)
- [Developing features and iterating](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/github-feature-development.html)
- [Reviewing code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/github-code-reviews.html)
- [Increase usage limits and configuration](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/github-register-app-install.html)
- [Configuring](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/github-configuration.html)
- [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/github-troubleshooting.html): Consult the following section to troubleshoot common problems when using Amazon Q Developer for GitHub.
- [Creating project rules](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/third-party-context-project-rules.html): You can build a library of project rules that you can use with Amazon Q Developer in GitLab or GitHub.


## [Security](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security.html)

### [Data protection](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Q Developer.

- [Data storage](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/data-storage.html): Learn about where Amazon Q Developer stores and processes your data.
- [Data encryption](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/data-encryption.html): Learn how Amazon Q Developer encrypts your data at rest and in transit.
- [Service improvement](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/service-improvement.html): Learn how AWS uses data to improve Amazon Q Developer and your control options.
- [Opt out of data sharing in the IDE and command line](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/opt-out-IDE.html): Learn how to opt out of sharing your data with Amazon Q Developer in your integrated development environment (IDE).
- [Cross-region processing](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/cross-region-processing.html): The following sections describe how cross-region inference and cross-region calls are used to provide the Amazon Q Developer service.

### [Identity and access management](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam.html)

Learn how to authenticate requests and manage access for your Amazon Q Developer resources.

- [How Amazon Q works with IAM](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html): Before you use IAM to manage access to Amazon Q Developer, learn what IAM features are available to use with Amazon Q Developer.

### [Manage access to Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)

### [Identity-based policy examples for Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_id-based-policy-examples.html)

The following example IAM policies control permissions for various Amazon Q Developer actions.

- [Administrator permissions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/id-based-policy-examples-admins.html): The following policies allow Amazon Q Developer administrators to perform administrative tasks in the Amazon Q subscription management console and Amazon Q Developer console.
- [User permissions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/id-based-policy-examples-users.html): The following policies allow users to access features of Amazon Q Developer on AWS apps and websites, including the AWS Management Console, AWS Console Mobile Application, and AWS Documentation site.
- [Manage access to Amazon Q Developer for integration](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-kms-policies.html): For third-party integrations, you must use the AWS Key Management Service (KMS) to manage access to Amazon Q Developer instead of IAM policies that are neither identity-based or resource-based.
- [Amazon Q permissions reference](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html): Amazon Q Developer uses two types of APIs to provide the service:
- [AWS managed policies for Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/managed-policy.html): An AWS managed policy is a standalone policy that is created and administered by AWS.

### [Using service-linked roles](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/using-service-linked-roles.html)

How to use service-linked roles to give Amazon Q Developer access to resources in your AWS account.

- [For Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/using-service-linked-roles-qdev.html): How to use service-linked roles to give Amazon Q Developer access to resources in your AWS account.
- [For User Subscriptions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/using-service-linked-roles-user-subs.html): How to use service-linked roles to give Amazon Q Developer access to resources in your AWS account.
- [Compliance validation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Q Developer features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/infrastructure-security.html): Learn how Amazon Q Developer isolates service traffic.
- [Firewalls, proxies, and data perimeters](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/firewall.html): Learn how to configure your firewall or proxy server to allowlist Amazon Q URLs so that Amazon Q functions as expected.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/vpc-interface-endpoints.html): You can use an interface endpoint to create a private connection between your VPC and Amazon Q Developer without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.


## [Monitoring and tracking](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/monitoring-overview.html)

- [With AWS CloudTrail](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/logging-using-cloudtrail.html): Learn about logging Amazon Q Developer with AWS CloudTrail.

### [With CloudWatch](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/monitoring-cloudwatch.html)

Learn how to use monitoring-cloudwatch to monitor Amazon Q Developer metrics, track usage patterns, and set up alerts for your development environment.

- [Identifying actions by specific users](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/monitoring-telemetry.html): Learn how to track and analyze individual user actions in Amazon Q Developer using CloudWatch Logs telemetry events.
- [Accessing customization-related logs](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/customizations-optimize-accessing-logs.html): Accessing Amazon CloudWatch Logs

### [Viewing usage metrics (dashboard)](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/dashboard.html)

Learn about the Amazon Q Developer dashboard, and the usage metrics presented in it.

- [Dashboard metrics](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/dashboard-metrics-descriptions.html): Learn about the usage metrics presented on the Amazon Q Developer dashboard.
- [Disabling the dashboard](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/dashboard-disabling.html): Learn how to disable the Amazon Q Developer dashboard so that it's hidden from view.
- [Troubleshooting the dashboard](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/dashboard-troubleshooting.html): Learn how to troubleshoot issues with the Amazon Q Developer dashboard.

### [Viewing per-user activity](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-user-telemetry.html)

Learn how to access telemetry data, understand usage metrics, and leverage insights for optimizing your Amazon Q Developer implementation.

- [User activity report metrics](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/user-activity-metrics.html): The following table describes the metrics that are included in the user activity reports generated by Amazon Q Developer.

### [Logging users' prompts](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-prompt-logging.html)

Administrators can enable the logging of all inline suggestions and chat conversations that users have with Amazon Q in their integrated development environment (IDE).

- [Prompt log examples](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-prompt-log-examples.html): This section provides examples of prompt logs generated by Amazon Q Developer.


## [Troubleshooting](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-troubleshooting.html)

- [Log access and analysis](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/troubleshooting-q-logs.html): Learn how to find, access, and analyze logs for Amazon Q Developer CLI and Visual Studio Code extension to troubleshoot issues effectively.
