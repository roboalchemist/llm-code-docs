# Source: https://docs.envzero.com/changelogs/2022/07/cloudformation-support.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ⛅ CloudFormation Support

> We're happy to announce that from today, CloudFormation joins Terraform, Terragrunt, Pulumi, and Kubernetes as a core IaC tool supported in env0! Manage your CloudFormation stack within env0, to enjoy features, such as Continuous Deployment, Policies and RBAC. You can also use Custom Flows to alter the deployment by running commands, or Workflows to orchestrate multiple IaC stacks and dependencies between them.

We're happy to announce that from today, CloudFormation joins Terraform, Terragrunt, Pulumi, and Kubernetes as a core IaC tool supported in env zero! [AWS CloudFormation](https://aws.amazon.com/cloudformation/) lets you model, provision, and manage AWS and third-party resources by treating infrastructure as code. With CloudFormation, you declare all your resources and dependencies in a template file. The template defines a collection of resources as a single unit called a stack. CloudFormation creates and deletes all member resources of the stack together and manages all dependencies between the resources for you.

Manage your CloudFormation stack within env zero, to enjoy [features](/guides/overview/about-env0), such as [Continuous Deployment](/guides/admin-guide/environments/continuous-deployment), [Policies](/guides/policies-governance/policies) and [RBAC](/guides/admin-guide/user-role-and-team-management/rbac). You can also use [Custom Flows](/guides/admin-guide/custom-flows) to alter the deployment by running commands, or [Workflows](/guides/admin-guide/workflows) to orchestrate multiple IaC stacks and dependencies between them.

### ✨ Get Started ✨

CloudFormation uses either YAML or JSON template file to describe the resources that are managed by it.

To manage your CloudFormation stack using env zero, you will need to create a new CloudFormation template, or run an [environment without template](/guides/admin-guide/environments/setting-up-a-new-environment#based-on-a-direct-vcs-integration) and choose type CloudFormation

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/07/cc8099b-cf-type.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=2ceaa1d5afd0339f627b27d4f75e0c83" alt="Feature demonstration screenshot showing new functionality" width="961" height="556" style={{ backgroundColor: '#f7fbfb' }} data-path="images/changelogs/2022/07/cc8099b-cf-type.png" />
</Frame>

Learn more about [CloudFormation support](/guides/admin-guide/templates) in env0.

Built with [Mintlify](https://mintlify.com).
