# Source: https://docs.aws.amazon.com/codecatalyst/latest/adminguide/llms.txt

# Amazon CodeCatalyst Administrator Guide

- [Who is this guide for?](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/what-is.html)
- [Concepts](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/concepts.html)
- [Inviting users to a Builder ID space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/inviting-users.html)
- [Creating additional Builder ID spaces](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/spaces-create.html)
- [Deleting a Builder ID space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/spaces-delete.html)
- [Viewing and configuring your user profile](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/view-profiles.html)
- [Document history](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/doc-history.html)

## [Setting up a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/setting-up.html)

- [Setting up a Builder ID space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/setting-up-space.html): You can create a space that manages users with AWS Builder ID access to CodeCatalyst.
- [Setting up a federated space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/setting-up-federation.html): Insert chapter abstract text here.


## [Administering federated spaces](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-space.html)

- [Creating a space for identity federation](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/setting-up-federation-space-create.html): You cannot directly add or remove users in your space that supports identity federation.
- [Configure an existing CodeCatalyst space for identity federation](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-space-existing.html): You must have the Space administrator role and access to the billing account for the space in order to view SSO users and groups for your space.
- [Viewing SSO users and groups for a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-space-view-users-groups.html): You must have the Space administrator role and access to the billing account for your space to view SSO users and groups for your space.
- [Adding SSO groups to a space that supports identity federation](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-space-add-users-groups.html): You can use the Amazon CodeCatalyst page in the AWS Management Console to add SSO groups to your space.
- [Adding the Space administrator role to SSO users in a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-space-change-administrator.html): You can use the Amazon CodeCatalyst page in the AWS Management Console to assign the Space administrator role to individual users in your SSO groups.
- [Deleting a space that supports identity federation](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-space-delete.html): You can delete a space that supports identity federation when you no longer need it.

### [Administering Identity Center applications](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-application.html)

Learn about the steps you must perform to manage applications for your CodeCatalyst space that supports identity federation.

- [Viewing Identity Center application details](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-application-view.html): You can view the details for the space associated with your Identity Center application.
- [Editing Identity Center application details](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-application-edit.html): You can edit the details for your Identity Center application, such as choosing SSO users and groups that are available in IAM Identity Center.
- [Associating a space to your Identity Center application](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-application-associate.html): You can associate a space with your CodeCatalyst Identity Center application.
- [Disassociating an Identity Center application from a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-federation-application-disassociate.html): You can disassociate the Identity Center application that is associated with your CodeCatalyst space.


## [Administering connected accounts](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-accounts.html)

- [Removing an account from a space (in AWS)](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-accounts-remove.html): You can use the page for CodeCatalyst in AWS to remove an account that has been added to a space.
- [Tagging account connections](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-accounts-tag.html): Connections are represented by a connection resource Amazon Resource Name (ARN) that is unique to the connection between a specific AWS account and a specific space in CodeCatalyst.
- [Enabling or disabling project-restricted account connections](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-accounts-restriction.html): The default in CodeCatalyst is to add an AWS account connection to your space that is then made immediately available for all projects and resources in the space.


## [Enabling generative AI features](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-generative-ai-features.html)

- [Enabling or disabling generative AI features](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-generative-ai-features-enable-disable.html): Learn how to enable or disable generative AI features for a space.
- [Viewing usage of generative AI features](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-generative-ai-features-view-usage.html): Learn how view your individual usage of generative AI features in a space.


## [Connecting a VPC to a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.html)

- [Setting up a VPC](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.set-up.html): Use the following procedure to create a VPC.
- [Adding VPC connections for a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.add.html): You can add VPC connections in the Amazon CodeCatalyst console.
- [Configuring VPC endpoints for a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.endpoint.html): VPCs allow you to define a virtual network that isolates AWS resources, securely connects to remote networks, and safely accesses service endpoints through AWS PrivateLink.
- [Managing a default VPC connection for a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.default.html): You can set a default VPC connection for a space.
- [Editing VPC connections for a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.edit.html): You can edit the configuration for a VPC connection, such as the associated subnets or security groups.
- [Removing VPC connections for a space](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.remove.html): You can remove a VPC connection that is no longer needed or that no longer has an owner.


## [Administering billing](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing.html)

- [Setting up a billing account](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing-add-account.html): To set up billing, you must add an authorized AWS account to your CodeCatalyst space and configure it for billing.
- [Changing allowed tiers for a billing account](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing-turn-on-tier.html): When you set up a billing account, the allowed CodeCatalyst tiers that you want to allow your space to use defaults to the free and paid tiers.
- [Changing your CodeCatalyst billing tier](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing-change-plan.html): When you set up a billing account, the allowed CodeCatalyst tiers that you want to allow your space to use defaults to the free and paid tiers.
- [Changing a billing account](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing-change-account.html): You can change the AWS account that you want to specify as the billing account for your CodeCatalyst space.
- [Viewing your CodeCatalyst plan and billing](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing-view-plan.html): When you set up a billing account, the allowed CodeCatalyst tiers that you want to allow your space to use defaults to the free and paid tiers.
- [Viewing CodeCatalyst accounts for billing in AWS](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing-view-connections.html): The Amazon CodeCatalyst page in the AWS Management Consoleshows the account name that you have specified for billing.
- [Getting AWS billing information](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-billing-information.html): If you have the necessary permissions, you can get information about your AWS charges from the AWS Management Console.
- [Troubleshooting billing](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/troubleshooting-billing.html): Learn how to troubleshoot problems with billing in Amazon CodeCatalyst.
