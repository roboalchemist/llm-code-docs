# Source: https://docs.aws.amazon.com/billingconductor/latest/userguide/llms.txt

# AWS Billing Conductor User Guide

> Describes how to use the AWS Billing Conductor, integrated with the AWS Management Console.

- [What is AWS Billing Conductor?](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html)
- [What is pro forma data?](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-proforma.html)
- [Understanding your dashboard](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html)
- [Concepts and best practices](https://docs.aws.amazon.com/billingconductor/latest/userguide/best-practices.html)
- [Quotas and restrictions](https://docs.aws.amazon.com/billingconductor/latest/userguide/limits.html)
- [Document history](https://docs.aws.amazon.com/billingconductor/latest/userguide/doc-history.html)

## [Billing groups](https://docs.aws.amazon.com/billingconductor/latest/userguide/creating-abc.html)

- [Creating billing groups](https://docs.aws.amazon.com/billingconductor/latest/userguide/create-billing-group.html): Create billing groups in AWS Billing Conductor.
- [Viewing your billing group details](https://docs.aws.amazon.com/billingconductor/latest/userguide/viewing-abc.html): Use your billing group details to monitor, analyze, and edit your billing group in AWS Billing Conductor.
- [Configuring AWS CUR by billing group](https://docs.aws.amazon.com/billingconductor/latest/userguide/configuring-abc.html): Create pro forma Cost and Usage Reports (AWS CUR) for each billing group using AWS Billing Conductor.


## [Pricing rules](https://docs.aws.amazon.com/billingconductor/latest/userguide/create-pricingrule.html)

- [Creating pricing rules](https://docs.aws.amazon.com/billingconductor/latest/userguide/create-pricingrule-abc.html): Use the following steps to create a pricing rule.
- [Viewing the pricing rule table](https://docs.aws.amazon.com/billingconductor/latest/userguide/table-pricingrule.html): After you create a pricing rule, you can view the details of the pricing rule in a filterable table.


## [Pricing plans](https://docs.aws.amazon.com/billingconductor/latest/userguide/abc-pricingplan.html)

- [Select an AWS managed pricing plan](https://docs.aws.amazon.com/billingconductor/latest/userguide/select-pricingplan.html): Use the following steps to select an AWS managed pricing plan.
- [Creating pricing plans](https://docs.aws.amazon.com/billingconductor/latest/userguide/create-pricingplan.html): Use the following steps to create a pricing plan (customer managed).
- [Viewing the pricing plan table](https://docs.aws.amazon.com/billingconductor/latest/userguide/table-pricingplan.html): After you create a pricing plan, you can view the details of the pricing plan in a filterable table.


## [Custom line items](https://docs.aws.amazon.com/billingconductor/latest/userguide/create-cli.html)

- [Creating a flat charge custom line item](https://docs.aws.amazon.com/billingconductor/latest/userguide/create-cli-flat.html): Use the following steps to create a custom line item that applies either a credit or fee line item to an individual billing group.
- [Creating a percentage charge custom line item](https://docs.aws.amazon.com/billingconductor/latest/userguide/create-cli-percentage.html): Use the following steps to create a custom line item that applies either a credit or fee line item to an individual billing group.
- [Viewing the custom line items table](https://docs.aws.amazon.com/billingconductor/latest/userguide/table-cli.html): After you create a custom line item, you can view the details of the line item in a filterable table.
- [Editing custom line items](https://docs.aws.amazon.com/billingconductor/latest/userguide/edit-cli.html): Edit custom line items in AWS Billing Conductor.
- [Deleting custom line items](https://docs.aws.amazon.com/billingconductor/latest/userguide/delete-cli.html): Delete your custom line items in AWS Billing Conductor.


## [Analyzing your margins](https://docs.aws.amazon.com/billingconductor/latest/userguide/analyzing-abc.html)

- [View your aggregate margins with margin summary](https://docs.aws.amazon.com/billingconductor/latest/userguide/view-margin-summary.html)
- [View your margins by AWS service using margin details](https://docs.aws.amazon.com/billingconductor/latest/userguide/view-margins-by-service-margin-details.html)


## [Viewing pro forma data in Billing and Cost Management](https://docs.aws.amazon.com/billingconductor/latest/userguide/viewing-in-billing.html)

- [Viewing your pro forma costs on the Bills page](https://docs.aws.amazon.com/billingconductor/latest/userguide/custom-pricing-view.html): After you create and assign your billing groups and pricing plans, you can view your custom billing dimensions with usage type granularity for each billing group under management.
- [Performing analysis on pro forma costs in Cost Explorer](https://docs.aws.amazon.com/billingconductor/latest/userguide/ad-hoc-cost-explorer-analysis.html): You can use Cost Explorer to perform analysis on your pro forma costs.

### [Analyzing Savings Plans, reservation coverage, and utilization reports](https://docs.aws.amazon.com/billingconductor/latest/userguide/analyzing-abc-sp.html)

Billing Conductor billing groups can analyze Savings Plans, reservation coverage, and utilization reports.

- [View your reservation and Savings Plans inventory](https://docs.aws.amazon.com/billingconductor/latest/userguide/view-ri-sp.html): You can view Savings Plans and reservation inventory for AWS accounts in Billing Conductor billing groups.
- [Viewing your pro forma data in AWS Budgets](https://docs.aws.amazon.com/billingconductor/latest/userguide/abc-budgets.html): Billing Conductor billing groups can monitor pro forma spendings with AWS Budgets.
- [AWS services that support pro forma-based billing view costs](https://docs.aws.amazon.com/billingconductor/latest/userguide/service-integrations-support-proforma.html): See the following AWS services that support pro forma costs.


## [Security](https://docs.aws.amazon.com/billingconductor/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/billingconductor/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Billing Conductor.

### [Identity and access management](https://docs.aws.amazon.com/billingconductor/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Billing Conductor resources.

- [How AWS Billing Conductor works with IAM](https://docs.aws.amazon.com/billingconductor/latest/userguide/security_iam_service-with-iam.html): Use IAM to manage access to Billing Conductor.

### [Identity-based policy examples](https://docs.aws.amazon.com/billingconductor/latest/userguide/security_iam_id-based-policy-examples.html)

Use example IAM policies to grant access to Billing Conductor.

- [AWS managed policies for Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Billing Conductor and recent changes to those policies.
- [Resource-based policy examples](https://docs.aws.amazon.com/billingconductor/latest/userguide/security_iam_resource-based-policy-examples.html)
- [Troubleshooting](https://docs.aws.amazon.com/billingconductor/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Billing Conductor and IAM.

### [Logging and monitoring](https://docs.aws.amazon.com/billingconductor/latest/userguide/billing-security-logging.html)

Learn the best practices for AWS Billing Conductor.

- [CloudTrail logs](https://docs.aws.amazon.com/billingconductor/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS Billing Conductor with AWS CloudTrail.
- [Compliance validation](https://docs.aws.amazon.com/billingconductor/latest/userguide/Billing-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/billingconductor/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Billing Conductor features for data resiliency.

### [Infrastructure security](https://docs.aws.amazon.com/billingconductor/latest/userguide/infrastructure-security.html)

Learn how AWS Billing Conductor isolates service traffic.

- [AWS PrivateLink](https://docs.aws.amazon.com/billingconductor/latest/userguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Billing Conductor.
