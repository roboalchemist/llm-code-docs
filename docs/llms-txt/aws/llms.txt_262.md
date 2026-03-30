# Source: https://docs.aws.amazon.com/cur/latest/userguide/llms.txt

# AWS Data Exports User Guide

> Describes how to use the AWS Data Exports feature, integrated with the AWS Billing and Cost Management console.

- [What is AWS Data Exports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html)
- [Processing data exports](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-processing.html)
- [Understanding the Cost and Usage Dashboard](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-dashboard-info.html)
- [Understanding the Cost and Usage Report (CUR)](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-cur-info.html)
- [Understanding the carbon emissions data export](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-carbon-emissions-info.html)
- [Quotas and restrictions](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-quotas.html)
- [Getting help](https://docs.aws.amazon.com/cur/latest/userguide/billing-get-answers.html)
- [Document history](https://docs.aws.amazon.com/cur/latest/userguide/doc-history.html)

## [Migrating from CUR to Data Exports CUR 2.0](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-migrate.html)

- [Creating an export using the CUR schema](https://docs.aws.amazon.com/cur/latest/userguide/data-exports-migrate-one.html): This shows you how to create an export with an SQL query with the export schema matching what you receive today in CUR.
- [Creating an export of CUR 2.0 with its new schema](https://docs.aws.amazon.com/cur/latest/userguide/data-exports-migrate-two.html): This shows you how to create an export of CUR 2.0 with its new schema of nested columns and additional columns.


## [Creating data exports](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create.html)

- [Setting up an Amazon S3 bucket for data exports](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-s3-bucket.html): This is an overview of how to set up an Amazon S3 bucket to receive and store your data exports.
- [Creating a standard export](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-standard.html): Learn about creating a standard data export.
- [Creating a cost and usage dashboard](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-dashboard.html): Learn about creating a cost and usage dashboard.
- [Creating a Legacy CUR export](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-legacy.html): Learn about creating a data export of your legacy Cost and Usage Report (CUR).
- [Creating exports with billing views](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-billing-view.html): Learn about creating a data export of your legacy Cost and Usage Report (CUR).
- [Data queryâSQL query and table configurations](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-data-query.html): Learn about the workflow that builds the SQL statement and table configurations based on your selections.
- [Configuring AWS CUR 2.0 using Billing Conductor](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-abc.html): With AWS Billing Conductor, you can create pro forma AWS Cost and Usage Report (AWS CUR) 2.0 for each billing group.


## [Viewing and managing data exports](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-manage.html)

- [Understanding export delivery](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-export-delivery.html): An overview of how export data is structured, delivered, and overwritten.
- [Editing export details](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-edit-export-details.html): Learn about editing your export details.
- [Editing export tags](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-edit-export-tags.html): Learn about editing your export tags.
- [Deleting exports](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-delete.html): Learn about deleting your exports.
- [Using Data Exports with AWS Organizations](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-organizations.html): Learn about using Data Exports with AWS Organizations as a management account and as a member account.


## [Data Exports table dictionary](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-table-dictionary.html)

### [Cost and Usage Report (CUR) 2.0](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2.html)

Details for Cost and Usage Report (CUR) 2.0 table dictionary.

- [Bill columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-bill.html): Bill columns contain data about your bill for the billing period.
- [Cost category columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-cost-category.html): Cost category columns contain data about cost categories that apply to the line item.
- [Discount columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-discount.html): Discount columns contain data about any discounts you are receiving.
- [Identity columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-identity.html): Identity columns contain data to identify a line item.
- [Line item columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-line-item.html): Line item columns contain data about cost, usage, type of usage, pricing rates, product name, and more.
- [Pricing columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-pricing.html): Pricing columns contain data about the pricing for a line item.
- [Product columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-product.html): Product columns contain data about the product that is being charged in the line item.
- [Reservation columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-reservation.html): Reservation columns contain data about a reservation that applies to the line item.
- [Resource tags columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-resource-tags.html): Resource tags columns contain data about resource tags that apply to the line item.
- [Savings plan columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-savings-plan.html): Saving Plan columns contain data about savings plans that apply to the line item.
- [Split line item columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-split-line-item.html): Columns under the split_line_item header are fields that appear in Data Exports if you've opted in to the split cost allocation data feature.
- [Tags Column](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-tag-columns.html): Tags column contains data about user, account, cost category and resource tags that apply to the line item.
- [Capacity reservation columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-capacity-reservation.html): Capacity reservation columns contain data about capacity reservations that apply to the line item.

### [Cost optimization recommendations](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cor.html)

Details for cost optimization recommendations table dictionary.

- [Cost optimization recommendations columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cor-columns.html)

### [FOCUS 1.2 with AWS columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-focus-1-2-aws.html)

Details for FOCUS 1.0 with AWS columns table dictionary.

- [FOCUS 1.2 with AWS columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-focus-1-2-aws-columns.html)
- [FOCUS 1.2 with AWS columns conformance gaps](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-focus-1-2-aws-conformance.html): The following table provides all of the conformance gaps that might exist in an export of the FOCUS 1.2 with AWS columns table.
- [Migrating from FOCUS 1.0 to FOCUS 1.2](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-focus-1-2-migrating.html): AWS Data Exports allows you to create exports of FOCUS 1.2 with AWS columns, which provides the same standardized cost and usage information as FOCUS 1.0 along with several enhancements for invoice reconciliation, capacity reservation tracking, and SaaS integration.

### [FOCUS 1.0 with AWS columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-focus-1-0-aws.html)

Details for FOCUS 1.0 with AWS columns table dictionary.

- [FOCUS 1.0 with AWS columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-focus-1-0-aws-columns.html)
- [FOCUS 1.0 with AWS columns conformance gaps](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-focus-1-0-aws-conformance.html): The following table provides all of the conformance gaps that might exist in an export of the FOCUS 1.0 with AWS columns table.
- [Cost and usage dashboard](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur-dashboard.html): Details for cost and usage dashboard table dictionary.

### [Carbon emissions](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-carbon-emissions.html)

Details for carbon emissions table dictionary.

- [Carbon emissions columns](https://docs.aws.amazon.com/cur/latest/userguide/carbon-emissions-columns.html)


## [Security and permissions](https://docs.aws.amazon.com/cur/latest/userguide/security.html)

- [Identity and access management for Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/bcm-data-exports-access.html): AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources.
- [Data protection in Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Data Exports.


## [Troubleshooting](https://docs.aws.amazon.com/cur/latest/userguide/datatexports-troubleshoot.html)

- [General troubleshooting](https://docs.aws.amazon.com/cur/latest/userguide/troubleshooting-data-exports.html): Use the following topics to help you troubleshoot common issues with Data Exports and Cost and Usage Reports.
- [Troubleshooting CUR 2.0](https://docs.aws.amazon.com/cur/latest/userguide/troubleshooting-cur-2-0.html): Use the following topics to help you troubleshoot common issues with Data Exports and Cost and Usage Reports.
- [Troubleshooting the cost and usage dashboard](https://docs.aws.amazon.com/cur/latest/userguide/troubleshooting-dashboard.html): Use the following topics to help you troubleshoot common issues with Data Exports and Cost and Usage Reports.
- [Troubleshooting Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/troubleshooting-cur.html): Use the following topics to help you troubleshoot common issues with Data Exports and Cost and Usage Reports.
- [Troubleshooting carbon emissions data exports](https://docs.aws.amazon.com/cur/latest/userguide/troubleshooting-carbon-emissions.html): Use the following topics to help you troubleshoot common issues with Data Exports and Cost and Usage Reports.


## [Legacy Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-overview.html)

- [What are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html): How to use AWS Cost and Usage Reports.

### [Creating Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/creating-cur.html)

Learn how to create a new AWS Cost and Usage Reports.

- [Setting up an Amazon S3 bucket for Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-s3.html): To receive billing reports, you must have an Amazon S3 bucket in your AWS account to receive and store your reports.
- [Creating reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-create.html)

### [Viewing and managing reports](https://docs.aws.amazon.com/cur/latest/userguide/managing-cur.html)

Learn how to view and manage your Cost and Usage Reports.

- [Viewing the latest report version](https://docs.aws.amazon.com/cur/latest/userguide/view-latest-cur.html): Learn how to view your latest report version.
- [Viewing your finalized report](https://docs.aws.amazon.com/cur/latest/userguide/view-finalized-cur.html): Learn how to view your finalized report.
- [Understanding your report versions](https://docs.aws.amazon.com/cur/latest/userguide/understanding-report-versions.html): Learn to understand your report versions.
- [Editing reports](https://docs.aws.amazon.com/cur/latest/userguide/edit-cur.html): Learn how to edit Cost and Usage Reports.
- [Using Cost and Usage Reports for AWS Organizations](https://docs.aws.amazon.com/cur/latest/userguide/cur-consolidated-billing.html): Learn about managing Cost and Usage Reports as a management account and as a member account.

### [Querying reports using Athena](https://docs.aws.amazon.com/cur/latest/userguide/cur-query-athena.html)

Use Amazon Athena to analyze the data from your AWS Cost and Usage Reports in Amazon S3 using standard SQL.

- [Setting up Athena with CloudFormation](https://docs.aws.amazon.com/cur/latest/userguide/use-athena-cf.html): Use Athena CloudFormation templates to streamline and automate integration of your Cost and Usage Reports with Athena.

### [Setting up Athena manually](https://docs.aws.amazon.com/cur/latest/userguide/cur-ate-manual.html)

We strongly recommend that you use the AWS CloudFormation template to create your table instead of creating it yourself.

- [Creating an Athena table](https://docs.aws.amazon.com/cur/latest/userguide/create-manual-table.html): AWS includes the SQL that you need to run to create this table in your AWS CUR bucket.
- [Creating a report status table](https://docs.aws.amazon.com/cur/latest/userguide/create-manual-cur-table.html): AWS refreshes your AWS CUR multiple times a day.
- [Uploading your report partitions](https://docs.aws.amazon.com/cur/latest/userguide/upload-report-partitions.html): To query your Cost and Usage Reports data, you need to upload the data into your Athena table.
- [Running Athena queries](https://docs.aws.amazon.com/cur/latest/userguide/cur-ate-run.html): To run Athena queries on your data, first use the Athena console to check whether AWS is refreshing your data and then run your query on the Athena console.
- [Other resources](https://docs.aws.amazon.com/cur/latest/userguide/cur-query-other.html): You can upload Cost and Usage Reports to Amazon Redshift and Amazon Quick to analyze your AWS cost and usage.
- [Configuring AWS CUR using Billing Conductor](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-view.html): Create pro forma AWS CUR for each billing group you create for Billing Conductor

### [Data dictionary](https://docs.aws.amazon.com/cur/latest/userguide/data-dictionary.html)

Details for line items in your Cost and Usage Reports.

- [Identity details](https://docs.aws.amazon.com/cur/latest/userguide/identity-columns.html): Details for identity line items in your Cost and Usage Reports.
- [Billing details](https://docs.aws.amazon.com/cur/latest/userguide/billing-columns.html): Details for billing line items in your Cost and Usage Reports.
- [Line item details](https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html): Details for lineItem in your Cost and Usage Reports.
- [Reservation details](https://docs.aws.amazon.com/cur/latest/userguide/reservation-columns.html): Details for reservation line items in your Cost and Usage Reports.
- [Pricing details](https://docs.aws.amazon.com/cur/latest/userguide/pricing-columns.html): Details for pricing line items in your Cost and Usage Reports.
- [Product details](https://docs.aws.amazon.com/cur/latest/userguide/product-columns.html): Details for product line items in your Cost and Usage Reports.
- [Resource tags details](https://docs.aws.amazon.com/cur/latest/userguide/resource-tags-columns.html): Details for resource tags line items in your Cost and Usage Reports.
- [Savings Plans details](https://docs.aws.amazon.com/cur/latest/userguide/savingsplans-columns.html): Details for Savings Plans line items in your Cost and Usage Reports.
- [Cost Categories details](https://docs.aws.amazon.com/cur/latest/userguide/cost-categories-columns.html): Details for categories line items in your Cost and Usage Reports.
- [Discount details](https://docs.aws.amazon.com/cur/latest/userguide/discount-details.html): Details for discount line items in your Cost and Usage Reports.
- [Split line item details](https://docs.aws.amazon.com/cur/latest/userguide/split-line-item-columns.html): Details for splitLineItem in your Cost and Usage Reports.

### [Use cases](https://docs.aws.amazon.com/cur/latest/userguide/use-cases.html)

Outlines the use cases for Cost and Usage Reports, specifically for Savings Plans and Reservations

- [Understanding Savings Plans](https://docs.aws.amazon.com/cur/latest/userguide/cur-sp.html): Use Cost and Usage Reports to track your Savings Plans utilization, charges, and allocations.

### [Understanding reservations](https://docs.aws.amazon.com/cur/latest/userguide/understanding-ri.html)

Use Cost and Usage Reports to track your Reserved Instance (RI) utilization, charges, and allocations.

- [Understanding your reservation line items](https://docs.aws.amazon.com/cur/latest/userguide/regular-reserved-instances.html): RIs provide you a significant discount compared to On-Demand Instance pricing.
- [Understanding your amortized reservation data](https://docs.aws.amazon.com/cur/latest/userguide/amortized-reservation.html): Amortizing is when you distribute one-time reservation costs across the billing period that is affected by that cost.
- [Monitoring your size flexible reservations for Amazon EC2](https://docs.aws.amazon.com/cur/latest/userguide/monitor-flexible-reservation.html): Amazon EC2 Reserved Instances that apply to a Region provide Availability Zone flexibility and instance size flexibility.
- [Monitoring your On-Demand capacity reservations](https://docs.aws.amazon.com/cur/latest/userguide/monitor-ondemand-reservations.html): Capacity reservations enable you to reserve capacity for your Amazon EC2 instances for any duration in a specific Availability Zone.
- [Understanding data transfer charges](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html): You can identify your AWS data transfer charges using the column of your AWS CUR.

### [Understanding split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html)

You can use Cost and Usage Reports (AWS CUR) to track your Amazon ECS and Amazon EKS container costs.

- [Enabling split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html)
- [Example of split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/example-split-cost-allocation-data.html): The purpose of the following example is to show you how split cost allocation data is calculated by computing the cost of individual Amazon ECS services, tasks in Amazon ECS clusters, and Kubernetes namespace and pods in Amazon EKS clusters.
- [Example of split cost allocation data for accelerated instances](https://docs.aws.amazon.com/cur/latest/userguide/example-accelerated-instances.html): The purpose of the following example is to show you how split cost allocation data is calculated by computing the cost of Kubernetes namespace and pods in Amazon EKS clusters.
- [Using Kubernetes labels for cost allocation in EKS](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data-kubernetes-labels.html): Split cost allocation data supports Kubernetes labels as cost allocation tags for Amazon EKS clusters.
- [Using split cost allocation data with Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data-resource-amp.html): Splitting the cost data for Amazon EKS requires that you collect and store metrics from your clusters, including memory and CPU usage.
- [Using split cost allocation data with Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data-cloudwatch.html): Splitting the cost data for Amazon EKS requires that you collect and store metrics from your clusters, including memory and CPU usage.

### [Understanding legacy billing reports](https://docs.aws.amazon.com/cur/latest/userguide/legacy-reports.html)

Resources for report alternatives to AWS Data Exports and AWS Cost and Usage Reports.

- [Detailed Billing Reports](https://docs.aws.amazon.com/cur/latest/userguide/detailed-billing.html)
- [Migrating From DBR to AWS CUR](https://docs.aws.amazon.com/cur/latest/userguide/detailed-billing-migrate.html): Detailed Billing Reports (DBR) and AWS Cost and Usage Reports (AWS CUR) both provide information about your charges.
- [Understanding unused reservation costs](https://docs.aws.amazon.com/cur/latest/userguide/unused-reservation-costs.html): You can use AWS Cost and Usage Reports (AWS CUR) to understand unused RI costs.
- [Monthly report](https://docs.aws.amazon.com/cur/latest/userguide/monthly-report.html): You can download a monthly report of your estimated AWS charges from the Bills page of the Billing and Cost Management console.
- [Monthly cost allocation report](https://docs.aws.amazon.com/cur/latest/userguide/monthly-cost-allocation.html)
- [AWS Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/usage-report.html)
- [Troubleshooting](https://docs.aws.amazon.com/cur/latest/userguide/troubleshooting.html): Use the following topics to help you troubleshoot common issues with Cost and Usage Reports.
- [Security and permissions](https://docs.aws.amazon.com/cur/latest/userguide/security-cur.html): Configure AWS Cost and Usage Reports to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your AWS CUR resources.
- [Quotas and restrictions](https://docs.aws.amazon.com/cur/latest/userguide/billing-cur-limits.html): Lists the quotas and restrictions for AWS Cost and Usage Reports.
