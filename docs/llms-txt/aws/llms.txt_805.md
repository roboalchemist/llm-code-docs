# Source: https://docs.aws.amazon.com/ssm-sap/latest/userguide/llms.txt

# AWS Systems Manager for SAP User Guide

- [What is AWS Systems Manager for SAP?](https://docs.aws.amazon.com/ssm-sap/latest/userguide/what-is-ssm-for-sap.html)
- [Setting up](https://docs.aws.amazon.com/ssm-sap/latest/userguide/setting-up.html)
- [Get started](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html)
- [Supported versions](https://docs.aws.amazon.com/ssm-sap/latest/userguide/supported-versions.html)
- [Quotas](https://docs.aws.amazon.com/ssm-sap/latest/userguide/load-balancer-limits.html)
- [Troubleshooting](https://docs.aws.amazon.com/ssm-sap/latest/userguide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/ssm-sap/latest/userguide/doc-history.html)

## [Tutorials](https://docs.aws.amazon.com/ssm-sap/latest/userguide/tutorials.html)

### [AWS CLI](https://docs.aws.amazon.com/ssm-sap/latest/userguide/cli.html)

Using AWS CLI, you can register SAP HANA or SAP ABAP applications, start, stop, refresh, and deregister SAP applications with Systems Manager for SAP.

- [Register SAP HANA database](https://docs.aws.amazon.com/ssm-sap/latest/userguide/register-database.html): You can register a single node or a high availability setup with multiple nodes for SAP HANA database with Systems Manager for SAP.
- [Register SAP ABAP application](https://docs.aws.amazon.com/ssm-sap/latest/userguide/register-abap.html): You can register a single node or multi node (distributed or high availability) setup for SAP ABAP application with Systems Manager for SAP.
- [Start SAP application](https://docs.aws.amazon.com/ssm-sap/latest/userguide/start-sap-application.html): You can perform a start operation on a single node or HA (high availability) SAP HANA application or on a single node or distributed setup of an SAP ABAP application which is registered with AWS Systems Manager for SAP.
- [Stop SAP application](https://docs.aws.amazon.com/ssm-sap/latest/userguide/stop-sap-application.html): You can perform a stop operation on a single node or HA (high availability) SAP HANA application or on a single node or distrubuted setup of SAP ABAP application that has been registered with AWS Systems Manager for SAP.
- [Refresh SAP application](https://docs.aws.amazon.com/ssm-sap/latest/userguide/refresh-sap-application.html): The following steps will guide you through a refresh of your SAP HANA application or of your single node setup of SAP ABAP application.
- [Deregister SAP application](https://docs.aws.amazon.com/ssm-sap/latest/userguide/deregister-sap-application.html): The following steps will guide you through deregistration your SAP HANA application or of your single node setup of SAP ABAP application registered with Systems Manager for SAP.
- [Run Configuration Checks](https://docs.aws.amazon.com/ssm-sap/latest/userguide/configuration-checks.html): You can run configuration checks on your registered SAP applications to validate their setup and ensure they follow best practices.

### [AWS Management Console](https://docs.aws.amazon.com/ssm-sap/latest/userguide/console.html)

Using AWS Management Console, you can register SAP HANA and SAP ABAP applications, and start or stop SAP applications with Systems Manager for SAP.

- [Register SAP HANA database](https://docs.aws.amazon.com/ssm-sap/latest/userguide/hana-app-manager.html): Follow along these steps to register SAP HANA database as a Systems Manager for SAP application.
- [Register SAP ABAP application](https://docs.aws.amazon.com/ssm-sap/latest/userguide/abap-app-manager.html)
- [Start SAP application](https://docs.aws.amazon.com/ssm-sap/latest/userguide/start-console.html): Follow along these steps to start Systems Manager for SAP application using AWS Management Console.
- [Stop SAP application](https://docs.aws.amazon.com/ssm-sap/latest/userguide/stop-console.html): Follow along these steps to stop Systems Manager for SAP application using AWS Management Console.
- [Run Configuration Checks](https://docs.aws.amazon.com/ssm-sap/latest/userguide/configuration-checks-console.html): Use the following steps to evaluate the SAP configuration of a Systems Manager for SAP application, which is either of type SAP HANA or SAP ABAP.


## [Security](https://docs.aws.amazon.com/ssm-sap/latest/userguide/security.html)

- [AWS managed policies](https://docs.aws.amazon.com/ssm-sap/latest/userguide/iam-policies.html): Learn about AWS managed policies for Systems Manager for SAP and recent changes to those policies.
- [Using service linked roles](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html): How to use service-linked roles to give Systems Manager for SAP access to resources in your AWS account.
- [Using AWS PrivateLink](https://docs.aws.amazon.com/ssm-sap/latest/userguide/privatelink.html): You can use AWS PrivateLink to establish a private connection between your VPC and AWS Systems Manager for SAP by creating an interface VPC endpoint.


## [Monitoring](https://docs.aws.amazon.com/ssm-sap/latest/userguide/monitoring.html)

- [Monitoring AWS Systems Manager for SAP events using EventBridge](https://docs.aws.amazon.com/ssm-sap/latest/userguide/eventbridge.html)
- [AWS Systems Manager for SAP metrics with Amazon CloudWatch](https://docs.aws.amazon.com/ssm-sap/latest/userguide/cloudwatch.html): You can view CloudTrail metrics for AWS Systems Manager for SAP via AWS Management Console or AWS CLI.
- [Log API calls using CloudTrail](https://docs.aws.amazon.com/ssm-sap/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS Systems Manager for SAP with AWS CloudTrail.
