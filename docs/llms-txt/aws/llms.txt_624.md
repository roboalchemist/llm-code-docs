# Source: https://docs.aws.amazon.com/nova-act/latest/userguide/llms.txt

# Amazon Nova Act User Guide

- [Human-in-the-loop (HITL)](https://docs.aws.amazon.com/nova-act/latest/userguide/hitl.html)
- [Tool use beyond the browser (Preview)](https://docs.aws.amazon.com/nova-act/latest/userguide/tool-use.html)
- [Responsible use](https://docs.aws.amazon.com/nova-act/latest/userguide/responsible-use.html)
- [Code examples](https://docs.aws.amazon.com/nova-act/latest/userguide/code-examples.html)
- [Monitoring](https://docs.aws.amazon.com/nova-act/latest/userguide/monitoring-overview.html)
- [Quotas](https://docs.aws.amazon.com/nova-act/latest/userguide/load-balancer-limits.html)
- [Document history](https://docs.aws.amazon.com/nova-act/latest/userguide/doc-history.html)

## [What is Amazon Nova Act?](https://docs.aws.amazon.com/nova-act/latest/userguide/what-is-nova-act.html)

- [Model version selection](https://docs.aws.amazon.com/nova-act/latest/userguide/model-version-selection.html): The Nova Act service relies on a custom foundation model, specially trained for UI-forward applications such as browser automation, tool use, and Human-in-the-Loop.
- [Available interfaces](https://docs.aws.amazon.com/nova-act/latest/userguide/interfaces.html): Nova Act consists of the Nova Act AWS service for production deployment and monitoring, plus Nova Act developer tools (SDK, CLI, and IDE extension) that support your development journey from exploration to production.


## [Getting started](https://docs.aws.amazon.com/nova-act/latest/userguide/getting-started.html)

- [Step 1: Explore the playground](https://docs.aws.amazon.com/nova-act/latest/userguide/step-1-playground.html): The Nova Act playground allows you to explore the capabilities of Nova Act in a hosted web environment, no setup and no AWS account required.
- [Step 2: Develop locally](https://docs.aws.amazon.com/nova-act/latest/userguide/step-2-develop-locally.html): Prerequisites: Python development environment (Python 3.10 or later)
- [Step 3: Deploy to AWS](https://docs.aws.amazon.com/nova-act/latest/userguide/step-3-deploy.html): Nova Act provides two deployment approaches depending on your needs.
- [Step 4: Review workflow runs](https://docs.aws.amazon.com/nova-act/latest/userguide/step-4-review-workflow-runs.html): The Nova Act AWS console provides visibility into your workflow execution with detailed traces and artifacts.


## [Integrate other services and frameworks with Nova Act](https://docs.aws.amazon.com/nova-act/latest/userguide/integrations.html)

- [Bedrock AgentCore](https://docs.aws.amazon.com/nova-act/latest/userguide/bedrock-agentcore.html): Amazon Bedrock AgentCore offers purpose-built infrastructure to deploy and operate production AI agents at scale.
- [Strands](https://docs.aws.amazon.com/nova-act/latest/userguide/strands.html): Strands Agents is an open source framework for building AI agents with a broad set of tool support.


## [Security](https://docs.aws.amazon.com/nova-act/latest/userguide/security.html)

- [SDK security](https://docs.aws.amazon.com/nova-act/latest/userguide/sdk-security.html): Be aware that Nova Act may encounter commands in the content it observes on third party websites, including user-generated content on trusted websites such as social media posts, search results, forum comments, news articles, and document attachments.
- [Data protection](https://docs.aws.amazon.com/nova-act/latest/userguide/data-protection.html)
- [Data encryption](https://docs.aws.amazon.com/nova-act/latest/userguide/data-encryption.html)

### [Identity and access management](https://docs.aws.amazon.com/nova-act/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Amazon Nova Act resources.

- [How Nova Act works with IAM](https://docs.aws.amazon.com/nova-act/latest/userguide/security-iam-service-with-iam.html)
- [Identity-based policy examples](https://docs.aws.amazon.com/nova-act/latest/userguide/security-iam-id-based-policy-examples.html): By default, IAM users and roles donât have permission to create or modify Amazon Nova Act resources.
- [AWS managed policies](https://docs.aws.amazon.com/nova-act/latest/userguide/security-iam-awsmanpol.html): An AWS managed policy is a standalone policy that is created and administered by AWS.
- [Troubleshooting](https://docs.aws.amazon.com/nova-act/latest/userguide/security-iam-troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Nova Act and IAM.
- [Incident response](https://docs.aws.amazon.com/nova-act/latest/userguide/incident-response.html): Security is the highest priority at AWS.
- [Compliance validation](https://docs.aws.amazon.com/nova-act/latest/userguide/compliance-validation.html): To learn whether an AWS service is within the scope of specific compliance programs, see AWS services in Scope by Compliance Program and choose the compliance program that you are interested in.
- [Resilience](https://docs.aws.amazon.com/nova-act/latest/userguide/disaster-recovery-resiliency.html): The AWS global infrastructure is built around AWS Regions and Availability Zones.
- [Infrastructure security](https://docs.aws.amazon.com/nova-act/latest/userguide/infrastructure-security.html): As a managed service, Amazon Nova Act is protected by the AWS global network security.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/nova-act/latest/userguide/configuration-vulnerability.html): Configuration and IT controls are a shared responsibility between AWS and you, our customer.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/nova-act/latest/userguide/cross-service.html): The confused deputy problem is a security issue where an entity that doesnât have permission to perform an action can coerce a more-privileged entity to perform the action.
