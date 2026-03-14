# Source: https://docs.envzero.com/guides/admin-guide/migration-strategy-guide.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Migration Strategy Guide

> Comprehensive strategy for migrating from Terraform Cloud or Jenkins to env zero with minimal disruption

## Introduction

As organizations continuously evolve their infrastructure and adopt new tools, the need for efficient and streamlined processes becomes paramount. If you're a HashiCorp Terraform Cloud user looking to migrate to a competitive tool like env zero, or if you were just using Jenkins, this guide will provide you with a comprehensive strategy to ensure a smooth transition. By following the steps outlined below, you can successfully migrate your workspaces while minimizing disruption to your DevOps process.

<Info>
  📘 This will be a multi-part guide, each section will contain a link to learn more.
</Info>

## Review your Setup

Before initiating the migration, it's crucial to assess your existing setup. Take stock of your current Terraform Cloud environment, including the number and complexity of your workspaces, variables, state files, and associated resources. Understanding your current configuration will help you plan and execute the migration more effectively.  Read more: [Review your setup.](/guides/admin-guide/migration-strategy-guide/review-your-setup)

## Review your DevOps Process

Evaluate your existing DevOps process to identify any pain points or areas for improvement. Consider factors such as collaboration, version control, infrastructure provisioning, and deployment. This analysis will help you identify key requirements for your new tool, ensuring a better fit for your team's workflows and objectives. Read more: [Review your DevOps Process](/guides/admin-guide/migration-strategy-guide/review-your-devops-process)

## Prepare the Migration

A successful migration requires careful planning and preparation. Start by creating a detailed migration plan that outlines the tasks, timelines, and responsibilities involved. Identify potential risks and mitigation strategies, ensuring you have a fallback plan in case of any unforeseen issues. Communicate the migration plan with all relevant stakeholders to manage expectations and gain their support. Read more: \[*Coming soon*]

## Set up env zero

With your migration plan in place, it's time to set up env zero as your new infrastructure-as-code (IaC) tool. Begin by signing up for an env zero account and familiarizing yourself with its features and capabilities. Configure necessary integrations with your version control system (e.g., GitHub) and any other tools that your team relies on for automation, testing, or deployment.

env zero offers an intuitive user interface, fine-grained access controls, and collaborative features to simplify infrastructure management. Spend time understanding and customizing these settings to align with your organization's requirements. Read more: \[*Coming soon*]

## Migrate the Workspaces

The most critical aspect of the migration is moving your existing Terraform workspaces to env zero. Follow these steps to ensure a smooth transition:

a. Export Terraform Configurations: Extract the Terraform configurations from your Terraform Cloud workspaces such as git repo, branch, and variables. This can typically be done by using TFC’s api.

b. Set up Workspaces in env zero: Create equivalent workspaces in env zero, ensuring that the necessary environment variables, input variables, and backend configurations are replicated accurately.

c. Version Control Integration: Connect your env zero workspaces with your preferred version control system. This allows seamless synchronization between your codebase and env zero, ensuring consistency and easy collaboration.

d. Migrate State Files: Depending on the location of your current state, and the env zero features you want to take advantage of (like Remote Plan), you may need to migrate the Terraform state files to env zero. This ensures that env zero has the latest information about your infrastructure resources.

e. Testing and Validation: Before executing any deployments, thoroughly test and validate your migrated workspaces in env zero. Run plan operations to detect any potential issues or conflicts and resolve them accordingly.

f. Go Live: Once you are confident in the accuracy and functionality of your migrated workspaces, it's time to switch over to env zero for your infrastructure provisioning and deployment. Communicate the transition to your team members and stakeholders, ensuring they are aware of the changes and have access to the new tool.

Read more: \[*Coming soon*]

## Conclusion

Migrating from HashiCorp Terraform Cloud to env zero can be a smooth and efficient process by following a well-structured strategy. By reviewing your setup, understanding your DevOps process, preparing for the migration, setting up env zero, and migrating your workspaces, you can successfully transition while minimizing disruptions and maximizing the benefits of your new IaC tool. With env zero's user-friendly interface and powerful features, you'll be well-equipped to manage your infrastructure seamlessly and efficiently.

Built with [Mintlify](https://mintlify.com).
