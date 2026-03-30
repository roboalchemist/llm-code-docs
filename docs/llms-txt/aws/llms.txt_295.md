# Source: https://docs.aws.amazon.com/devopsagent/latest/userguide/llms.txt

# AWS DevOps Agent User Guide

> AWS DevOps Agent User Guide

## [About AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html)

- [What is a DevOps Agent Web App?](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-what-is-a-devops-agent-web-app.html): AWS DevOps Agent uses a dual-console architecture that separates administrative functions from day-to-day operational activities.
- [What are DevOps Agent Spaces?](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-what-are-devops-agent-spaces.html): A DevOps Agent Space is a logical container that defines the tools and infrastructure that AWS DevOps Agent has access to.
- [What is a DevOps Agent Topology?](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-what-is-a-devops-agent-topology.html): AWS DevOps Agent's automatically discovers and visualizes the resources and relationships within your applications and uses the resulting topology to understand your infrastructure during incident investigations and when making preventative recommendations.
- [DevOps Agent Runbooks](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-devops-agent-runbooks.html): You can configure runbooks to guide the AWS DevOps Agent as it performs incident response investigations and incident prevention evaluations.
- [Public preview pricing and limits](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-public-preview-pricing-and-limits.html)


## [Getting started with AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent.html)

- [Creating an Agent Space](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-creating-an-agent-space.html): An Agent Space defines the tools and infrastructure that AWS DevOps Agent has access to.
- [CLI onboarding guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-cli-onboarding-guide.html)
- [Creating a test environment](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-creating-a-test-environment.html): This guide provides hands-on tests to validate AWS DevOps Agentâs incident response functionality using sample architecture.
- [Getting started with AWS DevOps Agent using AWS CDK](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-getting-started-with-aws-devops-agent-using-aws-cdk.html)
- [Getting started with AWS DevOps Agent using Terraform](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-getting-started-with-aws-devops-agent-using-terraform.html): AWS DevOps Agent helps you monitor and manage your AWS infrastructure using AI-powered insights.


## [Working with DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/working-with-devops-agent.html)

- [Autonomous incident response](https://docs.aws.amazon.com/devopsagent/latest/userguide/working-with-devops-agent-autonomous-incident-response.html)
- [Proactive incident prevention](https://docs.aws.amazon.com/devopsagent/latest/userguide/working-with-devops-agent-proactive-incident-prevention.html): AWS DevOps Agent analyzes patterns across your incident investigations to deliver targeted recommendations that continuously improve your operational posture and prevent future incidents.
- [On Demand DevOps Tasks](https://docs.aws.amazon.com/devopsagent/latest/userguide/working-with-devops-agent-on-demand-devops-tasks.html): AWS DevOps Agent On Demand Tasks is a generative artificial intelligence (AI) powered conversational assistant that enables operations teams to query their application architecture, analyze system health, and access investigation insights using natural language.


## [Configuring capabilities for AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent.html)

- [AWS EKS access setup](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-aws-eks-access-setup.html): You can enable AWS DevOps Agent to describe your Kubernetes cluster objects, retrieve pod logs and cluster events, for either public or private AWS EKS clusters (only accessible with a VPC).

### [Connecting to CI/CD pipelines](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-index.html)

CI/CD pipeline integration enables AWS DevOps Agent to monitor deployments and correlate code changes with operational incidents during investigations.

- [Connecting GitHub](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-connecting-github.html): GitHub integration enables AWS DevOps Agent to access code repositories and receive deployment events during incident investigations.
- [Connecting GitLab](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-connecting-gitlab.html): GitLab integration enables AWS DevOps Agent to monitor deployments from GitLab Pipelines to inform causal investigations during incident response.
- [Associating AWS resources with project deployments](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-associating-aws-resources-with-project-deployments.html): After connecting projects to your Agent Space, you must configure the association between projects and AWS resources to enable AWS DevOps Agent to track deployments of CloudFormation templates, CDK, Elastic Container Repository images, and Terraform.
- [Connecting MCP Servers](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-mcp-servers.html): Model Context Protocol (MCP) servers extend AWS DevOps Agent's investigation capabilities by providing access to data from your external observability tools, custom monitoring systems, and operational data sources.
- [Connecting multiple AWS Accounts](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-multiple-aws-accounts.html): Secondary AWS accounts allow AWS DevOps Agent to investigate resources across multiple AWS accounts in your organization.

### [Connecting telemetry sources](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-telemetry-sources-index.html)

AWS DevOps Agent provides three ways to connect to your telemetry sources.

- [Connecting Dynatrace](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-telemetry-sources-connecting-dynatrace.html)
- [Connecting DataDog](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-telemetry-sources-connecting-datadog.html)
- [Connecting New Relic](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-telemetry-sources-connecting-new-relic.html)
- [Connecting Splunk](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-telemetry-sources-connecting-splunk.html)

### [Connecting to ticketing and chat](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-to-ticketing-and-chat-index.html)

AWS DevOps Agent is designed to act as a member of your team by participating in your teamâs existing communication channels.

- [Connecting ServiceNow](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-to-ticketing-and-chat-connecting-servicenow.html): This tutorial walks you through connecting a ServiceNow instance to AWS DevOps Agent to enable it to automatically initiate incident response investigations when a ticket is created and post its key findings into the originating ticket.
- [Connecting Slack](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-connecting-to-ticketing-and-chat-connecting-slack.html): You can configure AWS DevOps Agent to update a Slack channel you select with incident response investigation key findings, root cause analyses, and generated mitigation plans.
- [Invoking DevOps Agent through Webhook](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-invoking-devops-agent-through-webhook.html): Webhooks allow external systems to automatically trigger AWS DevOps Agent investigations.


## [AWS DevOps Agent Security](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security.html)

- [DevOps Agent IAM permissions](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-devops-agent-iam-permissions.html): AWS DevOps Agent uses service-specific IAM actions to control access to its features and capabilities.
- [Limiting Agent Access in an AWS Account](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-limiting-agent-access-in-an-aws-account.html): AWS DevOps Agent uses IAM roles to discover and describe AWS resources during incident investigations and preventative evaluations.
- [Setting Up IAM Identity Center Authentication](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-setting-up-iam-identity-center-authentication.html): IAM Identity Center authentication provides a centralized way to manage user access to the AWS DevOps Agent Space web application.
