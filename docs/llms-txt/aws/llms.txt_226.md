# Source: https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/llms.txt

# Amazon CodeGuru Reviewer User Guide

> Provides a conceptual overview of Amazon CodeGuru Reviewer, instructions for getting started, product and service integrations, and review recommendations.

- [What is CodeGuru Reviewer?](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html)
- [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html)
- [How CodeGuru Reviewer works](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-codeguru-reviewer-works.html)
- [Tutorial: monitor source code in GitHub](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/tutorial-github-reviewer.html)
- [Create code reviews with GitHub Actions](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-cicd.html)
- [Product and service integrations](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/integrations.html)
- [Recommendation types](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/recommendations.html)
- [Quotas](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/quotas.html)
- [Troubleshooting](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/glossary.html)

## [Setting up](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/setting-up-codeguru-reviewer.html)

- [Sign up for AWS](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/get-set-up-sign-up-for-aws.html): Steps to sign up for an AWS account.
- [Configure IAM permissions](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/get-set-up-configure-iam-permissions.html): Information about the prerequisite to configure IAM permissions to us Amazon CodeGuru Reviewer.
- [Install or upgrade and then configure the AWS CLI](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/get-set-up-install-cli.html): Install, upgrade, and configure the AWS CLI for use with Amazon CodeGuru Reviewer.
- [Create a repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/get-set-up-setup-repository.html): Information about provisioning the required repository for Amazon CodeGuru Reviewer code reviews.


## [Getting started](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-with-guru.html)

- [Step 1: Get set up](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-prequisites.html): Indicates what steps to take before associating a repository in Amazon CodeGuru Reviewer.
- [Step 2: Associate a repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-associate-repository.html): Explains what a repository association does and how to create an association for different repository types in Amazon CodeGuru Reviewer.
- [Step 3: Get recommendations](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/get-results.html): Describes the recommendations to improve your code that Amazon CodeGuru Reviewer provides in code reviews.
- [Step 4: Provide feedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/provide-feedback.html): Explains how you can give feedback about Amazon CodeGuru Reviewer recommendations.


## [Working with repository associations](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-repositories.html)

- [Create a CodeCommit repository association](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-codecommit-association.html): How to create an AWS CodeCommit repository association.
- [Create a Bitbucket repository association](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-bitbucket-association.html): How to create a Bitbucket repository association in Amazon CodeGuru Reviewer.
- [Create a GitHub or GitHub Enterprise Cloud repository association](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-association.html): How to create a GitHub repository association in Amazon CodeGuru Reviewer.
- [Create a GitHub Enterprise Server repository association](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-enterprise-association.html): How to create a GitHub Enterprise Server repository association in Amazon CodeGuru Reviewer.
- [View all repository associations](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/repository-association-view-all.html): How to disassociate a repository association in Amazon CodeGuru Reviewer.
- [Disassociate a repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/disassociate-repository-association.html): How to disassociate a repository association in Amazon CodeGuru Reviewer.
- [Encrypting a repository association](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/encrypt-repository-association.html): Describes how to encrypt an associated repository in Amazon CodeGuru Reviewer.

### [Tagging a repository association](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/tag-repository-association.html)

Describes how to tag an associated repository in Amazon CodeGuru Reviewer.

### [Add a tag to an associated repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repositories-add.html)

Describes how to add a tag to an associated repository in Amazon CodeGuru Reviewer.

### [Add a tag to an associated repository (console)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-add-console.html)

Describes how to add a tag to an associated repository in Amazon CodeGuru Reviewer through the console.

- [Add a tag when you create an associated repository (console)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-add-on-create-console.html): Lists the steps to add tags to new repository associations in Amazon CodeGuru Reviewer through the console.
- [Add a tag to an existing associated repository (console)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-add-on-existing-console.html): Lists the steps to add tags to existing repository associations in Amazon CodeGuru Reviewer through the console.

### [Add a tag to an associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-add-cli.html)

Describes how to add a tag to an associated repository in Amazon CodeGuru Reviewer using the AWS AWS CLI.

- [Add a tag when you create an associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-add-on-create-cli.html): Lists the steps to add tags to new repository associations in Amazon CodeGuru Reviewer using the AWS AWS CLI.
- [Add a tag to an existing associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-add-on-existing-cli.html): Lists the steps to add tags to existing repository associations in Amazon CodeGuru Reviewer using the AWS AWS CLI.

### [View tags for an associated repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-view.html)

Describes how to view tags for an associated repository in Amazon CodeGuru Reviewer.

- [View tags for an associated repository (console)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-view-console.html): Describes how to view tags for an associated repository in Amazon CodeGuru Reviewer through the console.
- [View tags for an associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-view-cli.html): Describes how to view tags for an associated repository in Amazon CodeGuru Reviewer using the AWS AWS CLI.

### [Add or update tags for an associated repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-update.html)

Describes how to add or update tags in an associated repository in Amazon CodeGuru Reviewer.

- [Add or update tags for an associated repository (console)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-update-console.html): Describes how to add or update tags in an associated repository in Amazon CodeGuru Reviewer through the console.
- [Add or update tags for an associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-update-cli.html): Describes how to add or update tags in an associated repository in Amazon CodeGuru Reviewer using the AWS AWS CLI.

### [Remove tags from an associated repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-remove.html)

Describes how to remove tags from an associated repository in Amazon CodeGuru Reviewer.

- [Remove tags from an associated repository (console)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-rmeove-console.html): Describes how to remove tags from an associated repository in Amazon CodeGuru Reviewer through the console.
- [Remove tags from an associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-remove-cli.html): Describes how to remove tags from an associated repository using the AWS AWS CLI.


## [Working with code reviews](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/code-reviews.html)

- [About full repository analysis and incremental code reviews](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/repository-analysis-vs-pull-request.html): Learn about the difference between full repository analysis and incremental codes in Amazon CodeGuru Reviewer.
- [Suppress recommendations](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/recommendation-suppression.html): Explains how to suppress recommendations from CodeGuru Reviewer with an aws-codeguru-reviewer.yml file.
- [Create code reviews](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-code-reviews.html): Explains the types of code reviews that Amazon CodeGuru Reviewer creates and how to receive recommendations.
- [View all code reviews](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/view-all-code-reviews.html): Explains how to view previous CodeGuru Reviewer code reviews.
- [View code review details](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/view-code-review-details.html): Describes the information in code review details and why you might want to view this information in Amazon CodeGuru Reviewer.
- [View recommendations and provide feedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/give-feedback-from-code-review-details.html): Lists the steps to provide feedback on Amazon CodeGuru Reviewer recommendations.


## [Security](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/security.html)

- [Data protection](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/data-protection.html): Discusses data protection in Amazon CodeGuru Reviewer.

### [Identity and access management](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control.html)

How to authenticate requests and manage access your CodeGuru Reviewer resources.

- [Overview of managing access](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/security_iam_service-with-iam.html): Describes how account administrators can manage access to resources by attaching permissions policies to IAM identities.
- [Using identity-based policies](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-iam-identity-based-access-control.html): Provides examples of IAM identity-based policies for controlling access to Amazon CodeGuru Reviewer.
- [Using tags to control access to associated repositories](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html): Describes the use of tags to allow or deny actions on associated repositories in Amazon CodeGuru Reviewer and shows examples of their use in API operations.
- [CodeGuru Reviewer permissions reference](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-permissions-reference.html): Describes the Amazon CodeGuru Reviewer API operations and the corresponding actions that you grant permissions to perform.
- [Troubleshooting](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/security_iam_troubleshoot.html): Diagnose and fix common problems with identity and access management in Amazon CodeGuru Reviewer.
- [Compliance validation](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon CodeGuru Reviewer without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Infrastructure security](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/infrastructure-security.html): Learn how Amazon CodeGuru Reviewer isolates service traffic.


## [Logging and monitoring](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/monitoring-overview.html)

- [Logging CodeGuru Reviewer API calls with AWS CloudTrail](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/logging-using-cloudtrail.html): Explains the use of CloudTrail to log any actions that a user, a role, or an AWS service takes in Amazon CodeGuru Reviewer.

### [Monitoring CodeGuru Reviewer with CloudWatch](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/monitoring.html)

Learn about monitoring CodeGuru Reviewer using CloudWatch metrics and alarms.

- [Monitoring recommendations with CloudWatch metrics](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/cloudwatch-metric.html): Learn how to view CodeGuru Reviewer recommendation metrics in the CloudWatch console.
- [Monitoring CodeGuru Reviewer recommendations with CloudWatch alarms](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/cloudwatch-alarm.html): Learn how to create CloudWatch alarms for CodeGuru Reviewer recommendations metrics.
