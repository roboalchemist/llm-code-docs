# Source: https://docs.aws.amazon.com/tag-editor/latest/userguide/llms.txt

# Tagging AWS Resources and Tag Editor User Guide

> Describes tagging your AWS resources, using the Tag Editor console, the AWS Resource Groups Tagging API, or the tagging API operations provided by each AWS service. Tagging is a way to apply metadata in the form of tag key and value pairs to categorize your AWS resources .

- [Using tags in IAM policies](https://docs.aws.amazon.com/tag-editor/latest/userguide/tags-in-iam-policies.html)
- [Troubleshooting tag changes](https://docs.aws.amazon.com/tag-editor/latest/userguide/troubleshooting-tags.html)
- [Tag Editor service quotas](https://docs.aws.amazon.com/tag-editor/latest/userguide/reference.html)
- [Document history](https://docs.aws.amazon.com/tag-editor/latest/userguide/doc-history.html)

## [What is Tag Editor?](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)

- [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html): These sections provide information about best practices and strategies when tagging your AWS resources and using Tag Editor.
- [Tagging categories](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-categories.html): Companies that are most effective in their use of tags typically create business-relevant tag groupings to organize their resources along technical, business, and security dimensions.


## [Getting started](https://docs.aws.amazon.com/tag-editor/latest/userguide/gettingstarted.html)

- [Prerequisites](https://docs.aws.amazon.com/tag-editor/latest/userguide/gettingstarted-prereqs.html): Prepare your account to tag your resources.
- [Set up permissions](https://docs.aws.amazon.com/tag-editor/latest/userguide/gettingstarted-prereqs-permissions.html): Set up permissions and review authorization and access control that you'll need to tag resources.


## [Finding resources to tag](https://docs.aws.amazon.com/tag-editor/latest/userguide/find-resources-to-tag.html)

- [View and edit existing tags for a selected resource](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging-resources-view.html): Tag Editor shows you the existing tags on selected resources that are in the results of your Find resources to tag query.


## [Managing tags](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging-resources.html)

- [Add tags to selected resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging-resources-add.html): You can use Tag Editor to add tags to selected resources that are in the results of your Find resources to tag query.
- [Edit tags of selected resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging-resources-edit.html): You can use Tag Editor to change existing tag values on selected resources that are in the results of your Find resources to tag query.
- [Remove tags from selected resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging-resources-delete.html): You can use Tag Editor to remove tags from selected resources that are in the results of your Find resources to tag query.


## [AWS Organizations tag policies](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html)

- [Evaluating compliance for an account](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs-finding-noncompliant-tags.html): Learn how to find and correct noncompliant tags on an account's resources.
- [Evaluating organization-wide compliance](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs-evaluating-org-wide-compliance.html): Generate a report that lists all tagged resources in accounts across your organization and whether each resource is compliant with the effective tag policy.


## [Monitoring tag changes](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-monitor.html)

- [Monitoring tutorial](https://docs.aws.amazon.com/tag-editor/latest/userguide/monitor-example.html): As your pool of AWS resources and AWS accounts that you manage grows, you can use tags to make it easier to categorize your resources.


## [Security](https://docs.aws.amazon.com/tag-editor/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/tag-editor/latest/userguide/security_data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Tag Editor.

### [Identity and access management](https://docs.aws.amazon.com/tag-editor/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Tag Editor resources.

- [How Tag Editor works with IAM](https://docs.aws.amazon.com/tag-editor/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Tag Editor, you should understand what IAM features are available to use with Tag Editor.
- [Identity-based policy examples](https://docs.aws.amazon.com/tag-editor/latest/userguide/security_iam_id-based-policy-examples.html): By default, IAM principals, such as roles and users, don't have permission to create or modify tags.
- [Troubleshooting](https://docs.aws.amazon.com/tag-editor/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Tag Editor and IAM.
- [Logging and monitoring](https://docs.aws.amazon.com/tag-editor/latest/userguide/security_logging-monitoring.html): Learn about logging Tag Editor with AWS CloudTrail.
- [Compliance validation](https://docs.aws.amazon.com/tag-editor/latest/userguide/security_compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/tag-editor/latest/userguide/security_resilience.html): Learn how AWS architecture supports data redundancy, and learn about specific Tag Editor features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/tag-editor/latest/userguide/security_infrastructure.html): Learn how Tag Editor isolates service traffic.
