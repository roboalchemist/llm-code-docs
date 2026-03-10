# Source: https://docs.aws.amazon.com/launchwizard/latest/userguide/llms.txt

# AWS Launch Wizard User Guide

> AWS Launch Wizard reduces the time it takes to deploy application solutions to the cloud by providing easy step-by-step guidance. You input your application requirements, and AWS Launch Wizard identifies the right AWS resources to deploy and run your solution. AWS Launch Wizard provides an estimated cost of deployment, and gives you the ability to modify your resources and instantly view the updated cost assessment. When you approve, AWS Launch Wizard provisions and configures the selected resources in a few hours to create a fully-functioning, production-ready application. It also creates custom AWS CloudFormation templates, which can be reused and customized for subsequent deployments.

- [Workload availability](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-workload-availability.html)
- [CloudTrail logs](https://docs.aws.amazon.com/launchwizard/latest/userguide/logging-using-cloudtrail.html)
- [Document history](https://docs.aws.amazon.com/launchwizard/latest/userguide/doc-history.html)

## [Active Directory](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-active-directory-landing.html)

- [How it works](https://docs.aws.amazon.com/launchwizard/latest/userguide/how-launch-wizard-ad-works.html): This section walks you through how you can set up a new AWS Launch Wizard Active Directory infrastructure.
- [Get started](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-getting-started.html): Get started with AWS Launch Wizard Active Directory by setting up, verifying prerequisites, and deploying domain controllers on Amazon EC2 instances, or with AWS Managed Microsoft AD.

### [Deploy to a new VPC (Console)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-new-vpc.html)

Create an Active Directory deployment in a new VPC using the Launch Wizard console.

- [Deploy self-managed AD](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-new-vpc-self-managed.html): Create a self-managed Active Directory deployment in a new VPC.
- [Extend on-premises AD](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-new-vpc-extend.html): Extend an existing Active Directory deployment to a new VPC.
- [Deploy AWS Managed Microsoft AD](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-new-vpc-managed-ad.html): Create a AWS Directory Service for Microsoft Active Directory deployment in a new VPC.

### [Deploy to an existing VPC (Console)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-existing-vpc.html)

Create an Active Directory deployment in an existing VPC.

- [Deploy self-managed AD](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-existing-vpc-self-managed.html): Create a self-managed Active Directory in an existing VPC.
- [Extend on-premises AD](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-existing-vpc-extend.html): Extend an on-premises Active Directory to an existing VPC.
- [Deploy AWS Managed Microsoft AD](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-existing-vpc-managed-ad.html): Create a AWS Directory Service for Microsoft Active Directory in an existing VPC.
- [Deploy to a new or existing VPC (AWS CLI)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-deploying-cli.html): Create a deployment for Active Directory to a new or existing VPC using the AWS CLI.
- [Manage application resources](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-managing.html): Learn how to manage application resources after deploying with AWS Launch Wizard.
- [Post-deployment steps](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-post-deployment-steps.html): AWS Launch Wizard provides an efficient way to start deploying Active Directory in AWS.
- [Best practices](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-best-practices.html): Learn how AWS Launch Wizard supports AWS best practices for high availability and security.
- [Troubleshoot](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-troubleshooting.html): Troubleshoot common errors in AWS Launch Wizard.


## [Remote Desktop Gateway](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-remote-desktop-gateway.html)

- [Get Started](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-remote-desktop-gateway-getting-started.html): Get started with AWS Launch Wizard by setting up, verifying prerequisites for, and deploying a Remote Desktop Gateway application.
- [Deploy to a new VPC (Console)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-remote-desktop-gateway-deployment-steps-new-vpc.html): The following steps guide you through a Remote Desktop Gateway deployment with AWS Launch Wizard after you have launched it from the console.
- [Deploy to an existing VPC (Console)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-remote-desktop-gateway-deployment-steps-existing-vpc-standalone.html): The following steps guide you through a Remote Desktop Gateway deployment with AWS Launch Wizard after you have launched it from the console.
- [Deploy to a new or existing VPC (AWS CLI)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-rdgw-deploying-cli.html): Create a deployment for Remote Desktop Gateway to a new or existing VPC using the AWS CLI.
- [Post-deployment steps](https://docs.aws.amazon.com/launchwizard/latest/userguide/post-deployment-steps.html): AWS Launch Wizard provides an efficient way to start deploying a Remote Desktop Gateway.
- [Best practices](https://docs.aws.amazon.com/launchwizard/latest/userguide/best-practices.html): AWS Launch Wizard provides an efficient way to start deploying Remote Desktop Gateway.
- [Troubleshoot](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-remote-desktop-gateway-troubleshooting.html): Troubleshoot AWS Launch Wizard for Remote Desktop Gateway common errors.


## [Launch Wizard for SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap.html)

- [Version support for SAP deployments](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-versions.html): Provides a list of all of the operating system and application versions that are supported by Launch Wizard for SAP deployments.
- [How it works](https://docs.aws.amazon.com/launchwizard/latest/userguide/how-launch-wizard-sap-works.html): AWS Launch Wizard provisions and configures the infrastructure required to run SAP HANA database and SAP NetWeaver based SAP applications on SAP HANA or SAP ASE database on AWS.

### [Get started](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-getting-started.html)

Get started with AWS Launch Wizard by setting up, verifying prerequisites for, and deploying an SAP application.

- [Set Up](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-setting-up.html): This section describes the prerequisites that you must verify to deploy an SAP application with AWS Launch Wizard.

### [Deploy an application with Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-deploying.html)

This section contains steps for deploying an SAP application with Launch Wizard.

- [Deploying an SAP application (Console)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-deploying-console.html): You can deploy an SAP application using the AWS Launch Wizard console.
- [Deploying an SAP application (AWS CLI)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-deploying-cli.html): You can deploy, describe, and delete SAP applications you create using Launch Wizard with the AWS CLI.
- [Monitor Launch Wizard for SAP deployments](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-monitoring.html): You can monitor your Launch Wizard for SAP deployments using the AWS Launch Wizard console and AWS CLI.
- [Deploying SAP Web Dispatcher](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-deploy-web-dispatcher.html): AWS Launch Wizard supports the deployment of SAP Web Dispatcher as an optional component for Netweaver stack on HANA deployments.
- [Tutorials](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-tutorials.html): The following tutorials can help you get started with deploying an application with AWS Launch Wizard.

### [Manage application resources](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-managing.html)

Manage your SAP application, check logs, review saved infrastructure configurations, and delete your deployments and infrastructure configurations.

- [Manage deployments](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-managing-manage.html)
- [Delete infrastructure configuration](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-managing-delete-config.html)
- [Make SAP HANA software available to Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-structure.html): How to download the SAP HANA software and set up your destination Amazon S3 bucket.
- [Make SAP application software available to Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-software-install-details.html): Learn how to download the SAP application software and set up your destination S3 bucket.

### [Repeat SAP application deployments](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-deployment-artifacts.html)

This section contains information about how to repeat deployments using deployment artifacts created with Launch Wizard.

### [Launch AWS Service Catalog products](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog.html)

This section contains information to help you set up for and access AWS Service Catalog products created with AWS Launch Wizard to launch those products.

- [Set up](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog-setup.html): This section provides the required steps to grant permissions to the user group.
- [Create launch constraint](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog-constraint.html): A launch constraint specifies the AWS Identity and Access Management role that AWS Service Catalog assumes when a user launches a product.
- [Access AWS Service Catalog products](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog-access.html): Perform the following steps to access AWS Service Catalog products created with AWS Launch Wizard.
- [Deployment errors](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog-errors.html): For AWS Service Catalog deployments completed prior to February 7, 2022, perform the following steps to remove the AmazonLambdaRolePolicyForLaunchWizardSAP policy from the AmazonLambdaRoleForLaunchWizard role, and add a new inline policy.
- [Launch AWS Service Catalog products with ServiceNow](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog-servicenow.html): ServiceNow users can natively browse and provision AWS Service Catalog products created with AWS Launch Wizard by using the AWS Management Connector for ServiceNow.
- [Launch AWS Service Catalog products with Jira](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog-jira.html): AWS Service Catalog products created with AWS Launch Wizard can be integrated with Jira workflows.
- [Launch AWS Service Catalog products with Terraform](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog-terraform.html): The official HashiCorp AWS provider supports AWS Service Catalog resources.
- [Launch CloudFormation templates created in Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-launch-artifacts-cloudformation.html): You can launch CloudFormation stacks from the CloudFormation templates that you saved from your successful Launch Wizard deployments.
- [Deploy SAP applications using proxy server](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-deploy-proxy-server.html): AWS Launch Wizard for SAP launches and configures Amazon EC2 instances to deploy an SAP system on AWS.
- [Security groups](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-security-groups.html): How Launch Wizard creates and configures security groups.
- [Troubleshoot SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-troubleshooting.html): Troubleshooting AWS Launch Wizard for SAP common errors.


## [Launch Wizard for SQL](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sql.html)

- [Get started](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-getting-started.html): Get started with AWS Launch Wizard by setting up, verifying prerequisites, and deploying a SQL Server Always On application.
- [Deploy on Windows (Console)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-deploying.html)
- [Deploy on Ubuntu (Console)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-deploying-linux.html)
- [Deploy to a new or existing VPC (AWS CLI)](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sql-deploying-cli.html): Create a deployment for SQL Server to a new or existing VPC using the AWS CLI.
- [Manage application resources with Launch Wizard for SQL Server](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-managing.html): Manage resources, access SQL Server, manage your SQL Server Always On application on Systems Manager, view the generated SSM deployment template, delete a deployment, or drill down into application resource details after deploying a SQL Server Always On application with AWS Launch Wizard.
- [Manage application resources with SSM Application Manager](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sql-app-manager.html): Use SSM Application Manager to view operations details and perform operations tasks from the SSM Application Manager console.
- [Automation documents](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sql-provided-runbooks.html): Use AWS Launch Wizard-provided Automation documents, or runbooks, to run predefined workflows for common application tasks .
- [Monitoring](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sql-monitoring.html): Learn how AWS Launch Wizard supports monitoring using Amazon CloudWatch Application Insights.
- [Best practices](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-best-practices.html): Learn how AWS Launch Wizard supports AWS best practices for high availability and security.
- [Troubleshoot](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-troubleshooting.html): Troubleshoot AWS Launch Wizard common errors.


## [Security](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-security.html)

- [AWS managed policies](https://docs.aws.amazon.com/launchwizard/latest/userguide/security-iam-awsmanpol.html): Describes AWS managed policies for AWS Launch Wizard and recent changes to those policies.
