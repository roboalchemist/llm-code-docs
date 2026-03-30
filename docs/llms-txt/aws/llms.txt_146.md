# Source: https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/llms.txt

# AWS Supply Chain Administrator Guide

> AWS Supply Chain is a cloud-based supply chain management application that works with your existing solutions such as enterprise resource planning (ERP) and supply chain management systems. Using AWS Supply Chain, you can connect and extract your inventory, supply, and demand related data from existing ERP or supply chain systems into one unified AWS Supply Chain data model.

- [What is AWS Supply Chain?](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/what-is-service.html)
- [Setting up an AWS account](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/setting-up.html)
- [Prerequisites to use AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/prerequisites.html)
- [Quotas](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/quotas.html)
- [Frequently asked questions (FAQs)](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/faq.html)
- [Administrative support](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/admin-support.html)
- [Document history](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/doc-history.html)

## [Getting started with AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/getting-started.html)

- [Step 1: Assign an IAM Identity Center User profile](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/create-cid.html): To create an instance and use the AWS Supply Chain service, you need to either connect an existing IAM Identity Center user profile or create a new one.

### [Step 2: Create an instance](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/creating-instance.html)

Creating an instance in AWS Supply Chain establishes a dedicated environment for supply chain management and analytics.

- [Use standard configuration](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/create-instance-standard.html): Standard configuration creates your AWS Supply Chain instance using default security and encryption settings.
- [Use advanced configuration](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/create-instance-advanced.html): Advanced configuration allows you to customize your instance by setting your own parameters.
- [Step 3: Choose an AWS Supply Chain application owner](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/choosing-admin.html): As an AWS console administrator, you choose an AWS Supply Chain application owner to manage the AWS Supply Chain web application access.
- [Log on to AWS Supply Chain web application](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/viewing-homepage.html): As an AWS Supply Chain administrator, you should have received an email invite to the AWS Supply Chain web application.


## [Using the AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/using-supply-chain.html)

- [Using AWS Supply Chain console](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/using-console.html): Using the console is the easiest way to manage your service resources and configurations.
- [Updating your profile](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/updating-profile.html): You can update your account and organization profile anytime on the AWS Supply Chain web application.

### [Managing user permission roles](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/adding-users-groups.html)

As an AWS Supply Chain administrator, you can either use the default user permission roles or create custom permission roles.

- [Adding users](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/adding-new-users.html): As an AWS Supply Chain administrator, you can add users to access the AWS Supply Chain web application.
- [Updating user permissions](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/permission-roles.html): To update the user permission role for the current AWS Supply Chain users, follow these steps.
- [Deleting users](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/deleting-users.html): As an AWS Supply Chain administrator, you can delete users from the AWS Supply Chain web application.
- [Creating custom user permission roles](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/create-new-permission-roles.html): In addition to default user permission roles, you can create custom user permission roles to include multiple permission roles and add specific locations and products.
- [Deleting an instance](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/deleting-instance.html): To delete an instance, follow these steps.


## [Security](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/security.html)

- [Data protection](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Supply Chain.
- [AWS PrivateLink](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/vpc-interface-endpoints.html): You can use AWS PrivateLink to create a private connection between your VPC and AWS Supply Chain.

### [IAM](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/security-iam.html)

How to authenticate requests and manage access for your AWS Supply Chain resources.

- [How AWS Supply Chain works with IAM](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Supply Chain, learn what IAM features are available to use with AWS Supply Chain.
- [Identity-based policy examples](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Supply Chain resources.
- [Troubleshooting](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Supply Chain and IAM.
- [AWS managed policies](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Supply Chain .
- [Compliance validation](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/compliance-validation.html): Learn what AWS AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Supply Chain features for data resiliency.

### [Logging and Monitoring AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/monitoring-overview.html)

Monitor AWS Supply Chain to maintain reliability, availability, and performance.

### [Web application APIs](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/webappi.html)

Supported web application APIs

- [User roles](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/userpermissions.html): The following APIs are used for managing users, user roles, user notifications, and chat messages in AWS Supply Chain.
- [Data lake](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/datalake.html): The following APIs are used for creating and managing data flows and connections in data lake.
- [Insights](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/Insights.html): The following APIs are used by the Insights application to manage filters, watchlists, and view inventory changes.
- [Demand Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/adp.html): The following APIs are used in AWS Supply Chain to create and manage forecasts, demand plans, or workbooks.
- [Supply Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/sp.html): The following APIs are used in AWS Supply Chain to create and manage supply plans.
- [Amazon Q in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/ASCQ.html): The following APIs are used in Amazon Q in AWS Supply Chain.

### [Managing events using EventBridge](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/eventbridge-integration.html)

Receive notifications when specific AWS Supply Chain events such as object creation or deletion occur in an AWS Supply Chain with EventBridge.

- [Events detail reference](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/events-detail-reference.html): All events from AWS services have a common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others.
