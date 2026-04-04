# Source: https://docs.aws.amazon.com/workspaces-core/latest/pg/llms.txt

# Amazon WorkSpaces Core Technology Partner Integration Guide

> This guide is for third-party VDI solution providers who want to build a solution using Amazon WorkSpaces Core.

- [Introduction](https://docs.aws.amazon.com/workspaces-core/latest/pg/intro.html)
- [Shared responsibility model](https://docs.aws.amazon.com/workspaces-core/latest/pg/shared-model.html)
- [Prerequisites](https://docs.aws.amazon.com/workspaces-core/latest/pg/prerequisites.html)
- [Solution deployment guide example](https://docs.aws.amazon.com/workspaces-core/latest/pg/deployment-guide-example.html)
- [Document history](https://docs.aws.amazon.com/workspaces-core/latest/pg/doc-history.html)

## [Deployment with WorkSpaces Core bundles](https://docs.aws.amazon.com/workspaces-core/latest/pg/deploy-bundles.html)

- [Infrastructure setup](https://docs.aws.amazon.com/workspaces-core/latest/pg/infrastucture-setup.html): Learn more about the infrastructure setup for Amazon WorkSpaces Core.
- [Tag-based authorization guidelines](https://docs.aws.amazon.com/workspaces-core/latest/pg/tag-based-auth-guidelines.html): Learn more about tag-based authorization guidelines and Amazon WorkSpaces Core.
- [WorkSpaces Core bundles management](https://docs.aws.amazon.com/workspaces-core/latest/pg/lifecyle-management-of-instances.html): Learn more about lifecycle management of Amazon WorkSpaces Core bundles.


## [Deployment with WorkSpaces Core Managed Instances](https://docs.aws.amazon.com/workspaces-core/latest/pg/deploy-instances.html)

- [Architecture](https://docs.aws.amazon.com/workspaces-core/latest/pg/instance-architecture.html): Amazon WorkSpaces Core Managed Instances introduce an updated architecture that allows EC2 instances to be launched directly into the customerâs AWS account, rather than into an account owned by Amazon WorkSpaces Core.

### [Setting up partner access to AWS accounts](https://docs.aws.amazon.com/workspaces-core/latest/pg/setting-up-account.html)

This section explains how to deploy WorkSpaces Core Managed Instances in your AWS environment.

- [Grant authorization and permissions](https://docs.aws.amazon.com/workspaces-core/latest/pg/auth-permissions.html): Authorization and permissions in WorkSpaces Core Managed Instances determine who deploys your WorkSpaces resources.
- [Create a Service-Linked Role](https://docs.aws.amazon.com/workspaces-core/latest/pg/create-service-linked-role.html): WorkSpaces Core Managed Instances require an IAM service-linked role.
