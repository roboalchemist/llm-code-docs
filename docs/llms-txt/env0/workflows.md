# Source: https://docs.envzero.com/guides/admin-guide/workflows.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflow Overview

> Orchestrate multi-environment deployments with dependency management using env zero workflows

## What is a Workflow?

env zero Workflows provide a structured approach to managing groups of related environments by defining their dependencies and orchestrating the entire process. env zero ensures that all dependencies are satisfied and the Workflow runs smoothly from start to finish.

This is especially useful for managing systems divided into multiple subsystems – allowing you to oversee the entire system as a cohesive unit while retaining control over individual stacks. It also simplifies the process of breaking down IaC stacks into smaller, more manageable parts.

Workflows are defined declaratively through a Workflow configuration YAML file (`env0.workflow.yaml` or `.yml`) and are designed to be reused as templates. The environments within a Workflow are also based on these reusable templates, promoting consistency and efficiency.

Learn more: [Workflow File Reference](/guides/admin-guide/workflows/workflow-file-reference)

## When Should You Use Workflows?

The infrastructure of a production app consists of many different resources. The more resources there are, the more thought and effort is required to manage and deploy them.

We tend to view managing resources as we do code - split them into smaller manageable pieces ([Environments](/guides/admin-guide/environments)) where each piece is cohesive and loosely coupled.

In theory, this textbook solution sounds great because each Environment is independent and can be deployed at any time. The thing is, in the real world we have dependencies, and deploying all these Environments simultaneously is impractical.

## Basic Dependency Example

<Frame caption="A Workflow example">
  <img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/a_workflow_example.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=a22f0937caca6b00efe7dda3d26f63bf" alt="Workflow example diagram showing environment dependencies and execution flow" width="1332" height="442" data-path="images/guides/admin-guide/a_workflow_example.png" />
</Frame>

Environment Network and VPC manages all necessary network configurations.

Environment DB manages a database that multiple services use.

Environment EKS manages the Elastic Kubernetes Service onto which pods of services will be deployed.

Environments Billing Service, Configuration Service, and Notification Service all manage the deployments of services on EKS. These services need access to the database.

For this use case:

* Environment DB depends on the VPC from the Network and VPC IaC stack
* Environment EKS also depends on the VPC from the Network and VPC IaC stack
* All service environments depend on DB and EKS

As you can see, these dependencies make it impossible for all the Environments to be deployed simultaneously. As the resources and Environments grow, the complexity of the dependencies will increase.

Workflows will help you manage and deploy your environments with their dependencies.

## Workflow Environment Status

A Workflow Environment can be in one of the following states:

*Active* - All sub-environments have been successfully deployed and are up and running.\
*Inactive* - All sub-environments have been successfully destroyed, manually or automatically.\
*Deploy in progress* - Currently being deployed.\
*Destroy in progress*- Currently being destroyed.\
*Failed* - Errors were encountered during deployment in at least 1 sub-environment

<Tip>
  **Workflow Benefits**

  1. Manage your entire infrastructure with complex dependencies between Environments
  2. Visual presentation of the complex deployment
  3. Each Environment can use a different IaC tool – one Environment can be managed by Terraform while another is managed by K8S
  4. Enhanced experience from all surrounding env zero features such as [Policies](/guides/policies-governance/policies), [Custom flows](/guides/admin-guide/custom-flows), [Drift Detection](/guides/admin-guide/environments/drift-detection) and [Continuous Deployment](/guides/admin-guide/environments/continuous-deployment)
</Tip>

## Environment Variables

If you'd like to pass [Environment Variables](/guides/admin-guide/variables) to all IaC stacks in the workflow.

To do that, simply add/edit Environment variables when deploying the workflow.

If you'd like to set some specific Environment variable for a specific Environment in the workflow, you'd have to redeploy that specific Environment and add/edit that Environment variable

## Passing Outputs Between Sub-Environments

Workflows often require data from one sub-environment to be used as input in another. For example, a networking stack might output a VPC ID that a compute stack needs as an input variable.

env zero supports this through [Environment Outputs](/guides/admin-guide/variables/environment-outputs). You can configure output-to-variable mappings at the workflow template level so they are automatically applied on every deployment.

Learn more: [Managing Workflow Variables](/guides/admin-guide/variables/workflow-variables#passing-outputs-between-sub-environments)

Built with [Mintlify](https://mintlify.com).
