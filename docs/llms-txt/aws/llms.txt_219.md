# Source: https://docs.aws.amazon.com/codecommit/latest/userguide/llms.txt

# AWS CodeCommit User Guide

> Privately store and manage assets (such as documents, source code, and binary files) in the cloud with AWS CodeCommit.

- [What is CodeCommit?](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html)
- [Product and service integrations](https://docs.aws.amazon.com/codecommit/latest/userguide/integrations.html)
- [Working with user preferences](https://docs.aws.amazon.com/codecommit/latest/userguide/user-preferences.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/codecommit/latest/userguide/creating-resources-with-cloudformation.html)
- [Document history](https://docs.aws.amazon.com/codecommit/latest/userguide/history.html)
- [AWS Glossary](https://docs.aws.amazon.com/codecommit/latest/userguide/glossary.html)

## [Setting up](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up.html)

- [For HTTPS users using Git credentials](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html): Provides steps for users to connect to CodeCommit repositories over HTTPS using a user name and password.
- [For HTTPS connections with git-remote-codecommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html): Provides steps for setting up to connect to CodeCommit repositories over HTTPS with git-remote-codecommit, a utility that modifies Git.

### [For connections from development tools](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ide.html)

Provides steps for users to connect to CodeCommit repositories from development tools using a user name and password.

- [Integrate AWS Cloud9 with AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ide-c9.html): Learn how to integrate AWS Cloud9 with AWS CodeCommit.
- [Integrate Visual Studio with AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ide-vs.html): Learn how to use the AWS Toolkit for Visual Studio to integrate Visual Studio with CodeCommit.
- [For SSH users not using the AWS CLI](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-without-cli.html): Provides steps for users familiar with Git, SSH, and private/public key management to connect to CodeCommit repositories.
- [For SSH connections on Linux, macOS, or Unix](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ssh-unixes.html): Provides detailed steps for setting up to connect to CodeCommit repositories over SSH on Linux, macOS, or Unix, including creating and using public/private key pairs.
- [For SSH connections on Windows](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ssh-windows.html): Provides detailed steps for setting up to connect to CodeCommit repositories over SSH on Windows, including creating and using public/private key pairs.
- [For HTTPS connections on Linux, macOS, or Unix with the AWS CLI credential helper](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-unixes.html): Provides detailed steps for setting up to connect to CodeCommit repositories over HTTPS on Linux, macOS, or Unix, including setting up a credential helper.
- [For HTTPS connections on Windows with the AWS CLI credential helper](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-windows.html): Provides detailed steps for setting up to connect to CodeCommit repositories over HTTPS on Windows, including setting up a credential helper.


## [Getting started](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started-topnode.html)

- [Getting started with CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started-cc.html): A tutorial on how to get started with CodeCommit.
- [Getting started with Git and CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started.html): Provides a tutorial on using Git commands when working with a CodeCommit repository.


## [Working with repositories](https://docs.aws.amazon.com/codecommit/latest/userguide/repositories.html)

- [Create a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html): Describes how to use the AWS Management Console or the AWS CLI to create a CodeCommit repository.
- [Connect to a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-connect.html): Describes how to connect to a CodeCommit repository.
- [Share a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-share-repository.html): Provides information about how to share a repository with other users in CodeCommit.

### [Configuring notifications for repository events](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-repository-email.html)

Describes how to set up notifications about repository events for a repository in CodeCommit.

- [Create a notification rule](https://docs.aws.amazon.com/codecommit/latest/userguide/notification-rule-create.html): Learn how to create a notification rule for AWS CodeCommit.
- [Change or disable notifications](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-repository-email-console-edit.html): You can use the AWS CodeCommit console to change how notifications created before November 5, 2019 are configured, including the event types that send emails to users and the Amazon SNS topic used to send emails about the repository.
- [Delete notifications](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-repository-email-delete.html): If you no longer want to use notifications created for a repository before November 5, 2019, you can delete the Amazon CloudWatch Events rule associated with the notification.

### [Tagging a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-tag-repository.html)

Describes how to tag resources in AWS CodeCommit.

- [Add a tag to a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-tag-repository-add.html): Adding tags to a repository can help you identify and organize your AWS resources and manage access to them.
- [View tags for a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-tag-repository-list.html): Tags can help you identify and organize your AWS resources and manage access to them.
- [Edit tags for a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-tag-repository-update.html): You can change the value for a tag associated with a repository.
- [Remove a tag from a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-tag-repository-delete.html): You can remove one or more tags associated with a repository.

### [Manage triggers for a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify.html)

Describes how to create triggers for events in a CodeCommit repository that can be integrated with other AWS services, including AWS Lambda and Amazon Simple Notification Service.

- [Create a trigger for an Amazon SNS topic](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-sns.html): Describes how to create a trigger for events in a CodeCommit repository that can be integrated with Amazon Simple Notification Service.
- [Create a trigger for a Lambda function](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-lambda.html): Describes how to create a trigger for events in a CodeCommit repository that can be integrated with AWS Lambda.
- [Create a trigger for an existing Lambda function](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-lambda-cc.html): Describes how to create a trigger for events in a CodeCommit repository that can be used with an existing AWS Lambda function.
- [Edit triggers for a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-edit.html): Describes how to edit triggers for events in a CodeCommit repository.
- [Test triggers for a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-test.html): Describes how to test triggers for events in a CodeCommit repository.
- [Delete triggers from a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-delete.html): Describes how to delete triggers for events in a CodeCommit repository.
- [Associate or disassociate a repository with Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-amazon-codeguru-reviewer.html): Describes how to associate or disassociate a CodeCommit repository with Amazon CodeGuru Reviewer.
- [View repository details](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-repository-details.html): Describes how to view the details and settings for a CodeCommit repository.
- [Change repository settings](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-change-repository.html): Describes how to change settings for a repository in AWS CodeCommit.
- [Sync changes between repositories](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-sync-changes.html): Describes how to synchronize changes between a local repo and a CodeCommit repository.
- [Push commits to two repositories](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-mirror-repo-pushes.html): Describes how to push changes to two different remote repositories with a single command.

### [Configure cross-account access to a repository using roles](https://docs.aws.amazon.com/codecommit/latest/userguide/cross-account.html)

Describes how to configure access to CodeCommit repositories in one Amazon Web Services account to IAM users and groups in another Amazon Web Services account.

- [Cross-account repository access: Actions for the administrator in AccountA](https://docs.aws.amazon.com/codecommit/latest/userguide/cross-account-administrator-a.html): To allow users or groups in AccountB to access a repository in AccountA, an AccountA administrator must:
- [Cross-account repository access: Actions for the administrator in AccountB](https://docs.aws.amazon.com/codecommit/latest/userguide/cross-account-administrator-b.html): To allow users or groups in AccountB to access a repository in AccountA, the AccountB administrator must create a group in AccountB.
- [Cross-account repository access: Actions for the repository user in AccountB](https://docs.aws.amazon.com/codecommit/latest/userguide/cross-account-user-b.html): To access the repository in AccountA, users in the AccountB group must configure their local computers for repository access.
- [Delete a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-delete-repository.html): Describes how to delete a repository in CodeCommit.


## [Working with files](https://docs.aws.amazon.com/codecommit/latest/userguide/files.html)

- [Browse files in a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-browse.html): Describes how to browse the contents of a CodeCommit repository, including its structure and individual files.
- [Create or add a file](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-file.html): Describes how to add a file to a CodeCommit repository.
- [Edit the contents of a file](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-edit-file.html): Describes how to edit the contents of a file in a CodeCommit repository.


## [Working with pull requests](https://docs.aws.amazon.com/codecommit/latest/userguide/pull-requests.html)

- [Create a pull request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-pull-request.html): Describes how to create a pull request in a CodeCommit repository.
- [Create an approval rule](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-pull-request-approval-rule.html): Describes how to create an approval rule for a pull request in a CodeCommit repository.
- [View pull requests](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-pull-request.html): Describes how to view a list of pull requests in a CodeCommit repository and how to use filters to refine the view.
- [Review a pull request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-review-pull-request.html): Describes how to review a pull request in a CodeCommit repository.
- [Update a pull request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-update-pull-request.html): Describes how to update a pull request in a CodeCommit repository.
- [Edit or delete an approval rule](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-edit-delete-pull-request-approval-rule.html): Describes how to edit or delete an approval rule for a pull request in a CodeCommit repository.
- [Override approval rules on a pull request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-override-approval-rules.html): Describes how to override approval rule requirements for a pull request.
- [Merge a pull request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-merge-pull-request.html): Describes how to merge a pull request in a CodeCommit repository.
- [Resolve conflicts in a pull request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-resolve-conflict-pull-request.html): Describes how to resolve conflicts in a pull request in a CodeCommit repository.
- [Close a pull request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-close-pull-request.html): Describes how to close a pull request in a CodeCommit repository.


## [Working with approval rule templates](https://docs.aws.amazon.com/codecommit/latest/userguide/approval-rule-templates.html)

- [Create an approval rule template](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-template.html): You can create one or more approval rule templates to help you customize your development workflows across repositories.
- [Associate an approval rule template with a repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-associate-template.html): Approval rule templates are created in a specific AWS Region, but they do not affect any repositores in that AWS Region until they are associated.
- [Manage approval rule templates](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-manage-templates.html): You can manage the approval rule templates in an AWS Region to help understand how they are being used and what they are for.
- [Disassociate an approval rule template](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-disassociate-template.html): If the approval rules generated by an approval rule template no longer make sense for your team's workflow in a repository, you can disassociate the template from that repository.
- [Delete an approval rule template](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-delete-template.html): You can delete an approval rule template if you are not using it in any repositories.


## [Working with commits](https://docs.aws.amazon.com/codecommit/latest/userguide/commits.html)

- [Create a commit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-commit.html): Describes how to create and push a commit to a CodeCommit repository.
- [View commit details](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-commit-details.html): Describes how to view the details of a commit, including the history of commits to a CodeCommit repository.
- [Compare commits](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-compare-commits.html): Describes how to compare the differences between two commit specifiers in a CodeCommit repository.
- [Comment on a commit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-commit-comment.html): Describes how to create and view comments on a commit in a CodeCommit repository.
- [Create a Git tag](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-tag.html): Describes how to create a tag in Git.
- [View tag details](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-tag-details.html): Describes how to view the details of a Git tag.
- [Delete a tag](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-delete-tag.html): Describes how to delete a tag.


## [Working with branches](https://docs.aws.amazon.com/codecommit/latest/userguide/branches.html)

- [Create a branch](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-branch.html): Describes how to create a branch for a CodeCommit repository.
- [Limit pushes and merges to branches](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-conditional-branch.html): Describes how to configure a policy in IAM that limits who can push or merge changes to a branch in CodeCommit.
- [View branch details](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-branch-details.html): Describes how to view the details of a branch in CodeCommit.
- [Compare and merge branches](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-compare-branches.html): Describes how to compare and merge two branches in CodeCommit.
- [Change branch settings](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-change-branch.html): Describes how to change the settings for a branch in AWS CodeCommit.
- [Delete a branch](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-delete-branch.html): Describes how to delete a branch from a repository.


## [Migrate to CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-migrate-repository.html)

- [Migrate a Git repository to AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-migrate-repository-existing.html): Describes how to migrate an existing Git repository to a CodeCommit repository.
- [Migrate content to CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-migrate-repository-local.html): Describes how to migrate local or unversioned content to a CodeCommit repository.
- [Migrate a repository in increments](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-push-large-repositories.html): Describes how to migrate or push a repository in increments, to avoid potential problems with network connectivity or other issues.


## [Security](https://docs.aws.amazon.com/codecommit/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/codecommit/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS CodeCommit.

- [AWS KMS and encryption](https://docs.aws.amazon.com/codecommit/latest/userguide/encryption.html): Describes how CodeCommit interacts with AWS KMS to encrypt repositories.
- [Using rotating credentials](https://docs.aws.amazon.com/codecommit/latest/userguide/temporary-access.html): Describes how to use AWS Security Token Service to grant temporary access to CodeCommit repositories.

### [Identity and Access Management](https://docs.aws.amazon.com/codecommit/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your CodeCommit resources.

### [Authentication and access control](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control.html)

Control user access using IAM policies to specify which CodeCommit actions a user in your Amazon Web Services account can perform.

### [Using identity-based policies (IAM policies)](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html)

Provides examples of IAM identity-based policies for controlling access to AWS CodeCommit.

- [AWS managed policies for CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/security-iam-awsmanpol.html): Describes the AWS managed policies for CodeCommit.
- [Customer managed policy examples](https://docs.aws.amazon.com/codecommit/latest/userguide/customer-managed-policies.html): Provides examples of customer managed policies for CodeCommit.
- [CodeCommit permissions reference](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html): Describes the CodeCommit API operations and the corresponding actions that you can grant permissions to perform.
- [How AWS CodeCommit works with IAM](https://docs.aws.amazon.com/codecommit/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to CodeCommit, you should understand what IAM features are available to use with CodeCommit.
- [Resilience](https://docs.aws.amazon.com/codecommit/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn aboutg AWS CodeCommit features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/codecommit/latest/userguide/infrastructure-security.html): Learn how AWS CodeCommit isolates service traffic.


## [Monitoring CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/monitoring-overview.html)

- [Monitoring CodeCommit events](https://docs.aws.amazon.com/codecommit/latest/userguide/monitoring-events.html): You can monitor AWS CodeCommit events in EventBridge, which delivers a stream of real-time data from your own applications, software-as-a-service (SaaS) applications, and AWS services.
- [Logging AWS CodeCommit API calls with AWS CloudTrail](https://docs.aws.amazon.com/codecommit/latest/userguide/integ-cloudtrail.html): Learn how to monitor CodeCommit usage by logging CodeCommit API calls with AWS CloudTrail.


## [Troubleshooting](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting.html)

- [Troubleshooting Git credentials (HTTPS)](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-gc.html): Describes common issues when using Git credentials and HTTPS to connect to CodeCommit and provides guidance for troubleshooting problems.
- [Troubleshooting git-remote-codecommit](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-grc.html): Describes common issues and provides guidance for troubleshooting problems with git-remote-codecommit.
- [Troubleshooting SSH connections](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-ssh.html): Describes common issues when using SSH to connect to CodeCommit and provides guidance for troubleshooting problems.
- [Troubleshooting the credential helper (HTTPS)](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-ch.html): Describes common issues when using Git credentials and HTTPS to connect to CodeCommit.
- [Troubleshooting Git clients](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-git.html): Describes common issues with Git clients and provides guidance for troubleshooting problems.
- [Troubleshooting access errors](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-ae.html): Describes common access errors and provides guidance for troubleshooting problems.
- [Troubleshooting configuration errors](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-cf.html): Describes common configuration errors and provides guidance for troubleshooting problems.
- [Troubleshooting console errors](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-cs.html): Describes console errors in CodeCommit and provides guidance for troubleshooting problems.
- [Troubleshooting triggers](https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-ti.html): Describes common trigger issues and provides guidance for troubleshooting problems.


## [CodeCommit reference](https://docs.aws.amazon.com/codecommit/latest/userguide/references.html)

- [Regions and Git connection endpoints](https://docs.aws.amazon.com/codecommit/latest/userguide/regions.html): Describes the AWS Regions where CodeCommit is available.
- [Using AWS CodeCommit with interface VPC endpoints](https://docs.aws.amazon.com/codecommit/latest/userguide/codecommit-and-interface-VPC.html): Explains how to use CodeCommit with interface VPC endpoints.
- [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html): Describes service quotas in CodeCommit.
- [Command line reference](https://docs.aws.amazon.com/codecommit/latest/userguide/cmd-ref.html): Provides a reference of all the AWS CLI commands for CodeCommit, including links to example usage.
- [Basic Git commands](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-basic-git.html): Provides a reference of basic Git commands you can use with AWS CodeCommit.
