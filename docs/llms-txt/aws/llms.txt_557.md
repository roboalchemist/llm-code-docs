# Source: https://docs.aws.amazon.com/managedservices/latest/appguide/llms.txt

# AMS Advanced Application Developer's Guide AMS Advanced Application Deployment Options

> Describes AMS application deployment considerations and options.

- [Document history](https://docs.aws.amazon.com/managedservices/latest/appguide/doc-history.html)

## [Application onboarding](https://docs.aws.amazon.com/managedservices/latest/appguide/intro-aog.html)

- [What we do, what we do not do](https://docs.aws.amazon.com/managedservices/latest/appguide/ams-do-not-do.html): AMS gives you a standardized approach to deploying AWS infrastructure and provides the necessary ongoing operational management, and there are some things that we do not do.

### [AMS Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/managedservices/latest/appguide/ams-amis.html)

Learn about AMS Amazon machine images or AMIs.

- [Security enhanced AMIs](https://docs.aws.amazon.com/managedservices/latest/appguide/ams-amis-security-enhanced.html): Security enhanced AMIs contain additional security settings that are aligned with the Center for Internet Security (CIS) Operating System Security Configuration Benchmarks - Level-1.
- [Key terms](https://docs.aws.amazon.com/managedservices/latest/appguide/key-terms.html): Describes AMS key terms.
- [What is my operating model?](https://docs.aws.amazon.com/managedservices/latest/appguide/op-model-aog.html): As an AMS customer, your organization has decided to separate application and infrastructure operations and use AMS for infrastructure operations.


## [Service management](https://docs.aws.amazon.com/managedservices/latest/appguide/service-management.html)

- [Account governance](https://docs.aws.amazon.com/managedservices/latest/appguide/apx-gov.html): Describes account governance in AWS Managed Services.
- [Service commencement](https://docs.aws.amazon.com/managedservices/latest/appguide/srv-mgmt-srv-commence.html): Describes service commencement in AWS Managed Services.
- [Customer relationship management (CRM)](https://docs.aws.amazon.com/managedservices/latest/appguide/apx-crm.html): The purpose of AMS's customer relationship management (CRM) process is to ensure that a well-defined relationship is established and maintained with you.
- [Cost optimization](https://docs.aws.amazon.com/managedservices/latest/appguide/cost-optimization.html): Describs cost optimization for your AMS Advanced accounts.
- [Service hours](https://docs.aws.amazon.com/managedservices/latest/appguide/apx-gov-hours.html): Describes AMS contact hours
- [Getting help](https://docs.aws.amazon.com/managedservices/latest/appguide/faq-get-help.html): Describes how to get help in AWS Managed Services.


## [Application development](https://docs.aws.amazon.com/managedservices/latest/appguide/app-dev-deploy-overview.html)

- [Being well-architected](https://docs.aws.amazon.com/managedservices/latest/appguide/well-architected-aog.html): Describes how to get guidance on architecting in the AWS Cloud.
- [Application layer vs infrastructure layer responsibilities](https://docs.aws.amazon.com/managedservices/latest/appguide/app-layer-resp-vs-infra-layer-resp-aog.html): Describes application layer responsibilities vs infrastructure layer responsibilities in AMS.
- [EC2 instance mutability](https://docs.aws.amazon.com/managedservices/latest/appguide/compute-instance-mutability-aog.html): Describes EC2 instance mutability in AMS.
- [Using AWS Secrets Manager with AMS resources](https://docs.aws.amazon.com/managedservices/latest/appguide/secrets-manager.html): Describes using AWS Secrets Manager with AMS resources.


## [Application deployment in AMS](https://docs.aws.amazon.com/managedservices/latest/appguide/app-deployment.html)

- [Planning your application deployment](https://docs.aws.amazon.com/managedservices/latest/appguide/plan-app-deploy-aog.html): Learn about planning your application deployment in AMS.

### [AMS Workload Ingest (WIGS)](https://docs.aws.amazon.com/managedservices/latest/appguide/ams-workload-ingest.html)

Learn about AMS Workload Ingest (WIGS).

### [Migrating Workloads: Prerequisites for Linux and Windows](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-instance-prereqs.html)

Before ingesting a copy of an on-premises instance into AWS Managed Services (AMS), certain prerequisites must be met.

- [LINUX Prerequisites](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-prereqs-linux.html): Observe the requirements listed in and ensure the following before submitting a WIGS RFC:
- [Windows Prerequisites](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-prereqs-win.html): Observe the requirements listed in and ensure the following before submitting a WIGS RFC:
- [How Migration Changes Your Resource](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-changes.html): The ingestion RFC described in this section takes the next step of adding configurations to the instance, once it is migrated to your AMS account, so that AMS can manage it.
- [Migrating Workloads: Standard Process](https://docs.aws.amazon.com/managedservices/latest/appguide/mp-migrate-stack-process.html): Two parties are required for this process: an AMS Cloud Migration Partner (migration partner), and an Application Owner (you).
- [Migrating workloads: CloudEndure landing zone (SALZ)](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-instance-cloud-endure.html): This section provides information on setting up an intermediate migration single-account landing zone (SALZ) for CloudEndure (CE) cutover instances to be available for a WIGS RFC.

### [Tools account (migrating workloads)](https://docs.aws.amazon.com/managedservices/latest/appguide/tools-account.html)

Learn about migrating workloads in AMS with a Tools account.

- [AWS Application Migration Service (AWS MGN)](https://docs.aws.amazon.com/managedservices/latest/appguide/tools-account-mgn.html): Learn about the AWS Application Migration Service and AMS
- [Enable access to the new Tools account](https://docs.aws.amazon.com/managedservices/latest/appguide/tools-account-enable.html): Describes how to enable access to the new AMS Tools account.
- [Example IAM CloudEndure policy](https://docs.aws.amazon.com/managedservices/latest/appguide/tools-account-ex-policy.html): See an AMS pre-approved IAM CloudEndure policy.
- [Testing connectivity and end-to-end setup](https://docs.aws.amazon.com/managedservices/latest/appguide/tools-account-test.html): Describes how to test the AMS Tools account connectivity and end-to-end setup.
- [Tools account hygiene](https://docs.aws.amazon.com/managedservices/latest/appguide/tools-account-hygiene.html): Learn about AMS Tools account hygiene.
- [Migration at scale - Migration Factory](https://docs.aws.amazon.com/managedservices/latest/appguide/migration-factory.html): Learn about AWS Migration at scale - Migration Factory
- [Migrating workloads: Linux pre-ingestion validation](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-instance-linux-validation.html): You can validate that your instance is ready for ingestion into your AMS account.
- [Migrating workloads: Windows pre-ingestion validation](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-migrate-instance-win-validation.html): You can validate that your instance is ready for ingestion into your AMS account.

### [AMS CloudFormation ingest](https://docs.aws.amazon.com/managedservices/latest/appguide/ams-cfn-ingest.html)

Learn about AMS CloudFormation ingest.

### [CloudFormation Ingest Guidelines, Best Practices, and Limitations](https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-author-templates.html)

For AMS to process your CloudFormation template, there are some guidelines and restrictions.

- [Best Practices](https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-ingest-best-practices.html): Following are some best practices you can use to migrate resources using the AMS CloudFormation ingest process:

### [Template validation](https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-ingest-validate.html)

Learn about CloudFormation template validation in AMS.

- [CloudFormation ingest stack: CFN validator examples](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-cfn-ingest-validator.html): These examples can help you prepare your template for a successful ingest.
- [Limitations](https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-limitations.html): The following features and functionality currently aren't supported by the AMS CloudFormation ingest process.
- [Supported Resources](https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-ingest-supp-services.html): The following AWS resources are supported in the AMS CloudFormation ingest process.

### [CloudFormation Ingest: Examples](https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-ingest-examples.html)

Describes AMS CloudFormation Ingest examples.

- [CloudFormation Ingest examples: Defining resources](https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-ingest-ex-define-resource.html): Describes CloudFormation ingest examples for defining resources.
- [CloudFormation Ingest examples: 3-tier Web application](https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-ingest-ex-3-tier.html): Describes how to ingest a CloudFormation template for a standard 3-Tier Web application.
- [Automated IAM deployments using CFN ingest or stack update CTs](https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-ingest-iam-deploy.html): Describes automated IAM deployments using CFN ingest or stack update CTs in AMS.

### [CodeDeploy requests](https://docs.aws.amazon.com/managedservices/latest/appguide/service-create-codedeploy.html)

You use CodeDeploy to create application containers that you can then deploy via a CodeDeploy application group.

- [CodeDeploy application](https://docs.aws.amazon.com/managedservices/latest/appguide/service-create-codedeploy-app.html): You use CodeDeploy to create application containers that you can then deploy via a CodeDeploy application group.
- [CodeDeploy deployment groups](https://docs.aws.amazon.com/managedservices/latest/appguide/service-create-codedeploy-dep-group.html): Create CodeDeploy application groups.

### [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/managedservices/latest/appguide/service-create-dms.html)

AWS Database Migration Service (AWS DMS) helps you migrate databases to AMS easily and securely.

- [Planning for AWS DMS](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-create-dms-plan.html): When planning a database migration using the AMS AWS DMS, consider the following:
- [Required data for AWS DMS setup](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-create-dms-reqs.html): For each of the following AWS DMS walkthroughs, some data in common is needed.

### [Tasks for AWS DMS setup](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-create-dms-all-tasks.html)

Set up AWS DMS with the following walkthroughs.

- [1: AWS DMS replication subnet group: Create](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-dms-rsg-create-1.html): Learn how to create an AMS AWS DMS replication subnet group.
- [2: AWS DMS replication instance: Create](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-dms-ri-create-2.html): Learn how to create an AMS AWS DMS replication instance.
- [3: AWS DMS source endpoint: Create, create for Mongo DB, create for S3](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-dms-se-create.html): You can use the AMS console or API/CLI to create an AMS AWS DMS source endpoint for various databases, we provide three examples.
- [4: AWS DMS target endpoint: Create, create for S3](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-dms-te-create.html): You can use the AMS console or API/CLI to create an AMS AWS DMS target endpoint for various databases, we provide two examples.
- [5: AWS DMS replication task: Create](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-dms-rt-create-5.html): Learn how to create an AMS AWS DMS replication task.
- [Managing your AWS DMS](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-create-dms-manage.html): Managing your AWS DMS.

### [Database (DB) import to AMS RDS for SQL Server](https://docs.aws.amazon.com/managedservices/latest/appguide/db-to-sql-rds.html)

Learn about database (DB) import to AMS RDS for SQL Server.

- [Setting up](https://docs.aws.amazon.com/managedservices/latest/appguide/db-to-sql-rds-setup.html): Describes setting up to begin the RDS for SQL Server import process.
- [Importing the database](https://docs.aws.amazon.com/managedservices/latest/appguide/db-to-sql-rds-import-db.html): Describes how to importing the database to RDS for SQL Server.
- [Cleanup](https://docs.aws.amazon.com/managedservices/latest/appguide/db-to-sql-rds-cleanup.html): Describes system cleanup after you've imported the RDS for SQL Server database.
- [Tier and Tie app deployments](https://docs.aws.amazon.com/managedservices/latest/appguide/tier-and-tie-aog.html): Learn about AMS Tier and Tie deployment.
- [Full stack app deployments](https://docs.aws.amazon.com/managedservices/latest/appguide/full-stack-aog.html): Learn about an AMS full stack app deployments.
- [Working with provisioning change types (CTs)](https://docs.aws.amazon.com/managedservices/latest/appguide/deploy-new-aog.html): Learn about working with AMS provisioning change types (CTs).


## [Quick starts](https://docs.aws.amazon.com/managedservices/latest/appguide/quick-starts.html)

- [AMS Resource Scheduler quick start](https://docs.aws.amazon.com/managedservices/latest/appguide/qs-resource-scheduler.html): AMS Resource Scheduler quick start.
- [Setting up cross account backups (intra-Region)](https://docs.aws.amazon.com/managedservices/latest/appguide/qs-backup-cross-account-snapshot.html): AWS Backup cross account snapshot copy.


## [Tutorials](https://docs.aws.amazon.com/managedservices/latest/appguide/tutorials.html)

### [Console Tutorial: High Availability Two Tier Stack (Linux/RHEL)](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-ha-stack.html)

This section describes how to deploy a high availability (HA) WordPress site into an AMS environment using the AMS console.

- [Before You Begin](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ha-stack-ex-before-begin.html): The Deployment | Advanced Stack Components | High Availability Two Tier Stack | Create CT creates an Auto Scaling group, a load balancer, a database, and a CodeDeploy application name and deployment group (with the same name that you give the application).
- [Create the Infrastructure](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-ha-rfc.html): This procedure utilizes the High availability two-tier stack CT followed by the Create S3 storage CT.
- [Create, Upload, and Deploy the Application](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-app.html): First, create a WordPress application bundle, and then use the CodeDeploy CTs to create and deploy the application.
- [Validate the Application Deployment](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-validate-app-deploy.html): Navigate to the endpoint (LoadBalancerCName) of the previously-created load balancer, with the WordPress deployed path: /WordPress.
- [Tear Down the High Availability Deployment](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-delete-ha-deploy.html): To tear down the deployment, you submit the Delete Stack CT against the HA Two-Tier stack, and the S3 bucket, and you can request that RDS snapshots be deleted.

### [Console Tutorial: Deploying a Tier and Tie WordPress Website](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-wp-stack.html)

This section describes how to deploy a high availability (HA) WordPress site into an AMS environment using the AMS console.

- [Creating an RFC using the Console (Basics)](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-rfc-template-params-create-WP.html): These are some steps that you must follow each time you create an RFC using the Console.

### [Creating the Infrastructure](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-wp-infra-deploy.html)

Log in to the AWS Console for the target AMS account and then the AMS Console for the account.

- [Create an RDS Stack](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-WP-stack-rds-create.html): Create an RDS stack.
- [Create an ELB Stack](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-WP-stack-elb-create.html): Launch a public ELB.
- [Create an Auto Scaling Group Stack](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-WP-stack-asg-create.html): Launch an Auto scaling group.
- [Create an S3 Stack](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-s3.html): Launch an S3 bucket.
- [Create a WordPress CodeDeploy Bundle](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-wp-package.html): The section provides an example of creating an application deployment bundle.

### [Deploy the WordPress Application Bundle with CodeDeploy](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-wp-deploy-app.html)

The CodeDeploy is an AWS deployment service that automates application deployments to Amazon EC2 instances.

- [Create a CodeDeploy Application](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-cd-app.html): The CodeDeploy application is simply a name or container used by AWS CodeDeploy to ensure that the correct revision, deployment configuration, and deployment group are referenced during a deployment.
- [Create a CodeDeploy Deployment Group](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-cd-dep-group.html): Create the CodeDeploy deployment group.
- [Upload the WordPress Application](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-upload-wp-package.html): You automatically have access to any S3 bucket instance that you create.
- [Deploy the WordPress Application with CodeDeploy](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-cd-deploy-wp-package.html): Deploy the CodeDeploy application.
- [Validate the Application Deployment](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-validate-wp-deploy.html): Navigate to the endpoint (ELB CName) of the previously-created load balancer, with the WordPress deployed path: /WordPress.
- [Tear Down the Application Deployment](https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-delete-wp-deploy.html): To tear down the deployment, you submit the Delete Stack CT against the RDS database stack, the application load balancer, the Auto Scaling group, the S3 bucket, and the Code Deploy application and group--six RFCs in all..

### [CLI Tutorial: High Availability Two-Tier Stack (Linux/RHEL)](https://docs.aws.amazon.com/managedservices/latest/appguide/tut-create-ha-stack.html)

This section describes how to deploy a high availability (HA) two-tier stack into an AMS environment using the AMS CLI.

- [Before You Begin](https://docs.aws.amazon.com/managedservices/latest/appguide/ha-stack-ex-before-begin.html): The Deployment | Advanced Stack Components | High Availability Two Tier Stack Advanced | Create CT creates an Auto Scaling group, a load balancer, a database, and a CodeDeploy application name and deployment group (with the same name that you give the application).
- [Create the Infrastructure](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-create-ha-infra-deploy.html): Gathering the following data before you begin will make the deployment go more quickly.
- [Create, Upload, and Deploy the Application](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-create-app.html): First, create a WordPress application bundle, and then use the CodeDeploy CTs to create and deploy the application.
- [Validate the Application Deployment](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-validate-app-deploy.html): Navigate to the endpoint (ELB CName) of the previously-created load balancer, with the WordPress deployed path: /WordPress.
- [Tear Down the Application Deployment](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-tear-down-app-deploy.html): Once you are finished with the tutorial, you will want to tear down the deployment so you are not charged for the resources.

### [CLI Tutorial: Deploying a Tier and Tie WordPress Website](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-create-wp-stack.html)

This section describes how to deploy a high availability (HA) WordPress site into an AMS environment using the AMS CLI.

### [Create the Infrastructure](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-create-wp-infra-deploy.html)

Creating an RDS database, a load balancer, and an Auto Scaling group.

- [Create an RDS Stack (CLI)](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-WP-stack-rds-create.html): Create an RDS Stack.


## [Application maintenance](https://docs.aws.amazon.com/managedservices/latest/appguide/app-deploy-strategy-exs.html)

- [Mutable deployment with a CodeDeploy-enabled AMI](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-mute-codedeploy.html): You can use CodeDeploy with AMS to create and deploy a CodeDeploy application.
- [Mutable deployment, manually configured and updated application instances](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-mute-manual.html): This application deployment strategy is a simple and manual update of application instances.
- [Mutable deployment with a pull-based deployment tool-configured AMI](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-mute-pull-based.html): This strategy relies on the InstanceUserData parameter in the Managed Services Create EC2 CT.
- [Mutable deployment with a push-based deployment tool-configured AMI](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-mute-push-based.html): This strategy relies on the InstanceUserData parameter in the Managed Services Create EC2 CT.
- [Immutable deployment with a golden AMI](https://docs.aws.amazon.com/managedservices/latest/appguide/ex-immute-gold-ami.html): This strategy employs a golden AMI that you have configured to behave as you want all of your application instances to.
- [Update Strategies](https://docs.aws.amazon.com/managedservices/latest/appguide/update-strategies.html): There are a few different strategies you can employ to update your applications or instances in your AMS-managed environment.

### [Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/appguide/ams-resource-scheduler.html)

Describes the AMS Resource Scheduler.

- [Deploying Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/appguide/res-sched-deploying.html): Deploying AMS Resource Scheduler.
- [Customizing Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/appguide/res-sched-customize.html): Customizing AMS Resource Scheduler.
- [Using Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/appguide/res-sched-using.html): Describes using AMS Resource Scheduler.

### [AMS Resource Scheduler cost estimator](https://docs.aws.amazon.com/managedservices/latest/appguide/resource-scheduler-cost-est.html)

AMS Resource Scheduler cost estimator

- [Cost estimator tips](https://docs.aws.amazon.com/managedservices/latest/appguide/resource-scheduler-cost-est-faqs.html): AMS Resource Scheduler tips
- [AMS Resource Scheduler best practices](https://docs.aws.amazon.com/managedservices/latest/appguide/resource-scheduler-bp.html): Scheduling Amazon EC2 Instances


## [Application security considerations](https://docs.aws.amazon.com/managedservices/latest/appguide/app-security.html)

### [Windows Instances](https://docs.aws.amazon.com/managedservices/latest/appguide/fw-app-access-windows.html)

These are the rules to configure for your Windows parent and child domain controllers.

- [Linux Instances](https://docs.aws.amazon.com/managedservices/latest/appguide/fw-app-access-linux.html): These are the rules to configure for your Linux parent and child domain controllers.
- [AMS egress traffic management](https://docs.aws.amazon.com/managedservices/latest/appguide/egress-traffic-mgmt.html): AMS egress traffic management.
- [Security groups](https://docs.aws.amazon.com/managedservices/latest/appguide/about-security-groups.html): In AWS Virtual Private Clouds (VPCs), AWS Security Groups act as virtual firewalls, controlling the traffic for one or more stacks (an instance or a set of instances).


## [Appendix: Application onboarding questionnaire](https://docs.aws.amazon.com/managedservices/latest/appguide/apx-aog-questions.html)

- [Deployment summary](https://docs.aws.amazon.com/managedservices/latest/appguide/deployment-summary.html): A description of the deployment.
- [Infrastructure deployment components](https://docs.aws.amazon.com/managedservices/latest/appguide/apx-aog-infra-components.html): What are all the different components that will need configuring to support your application?
- [Application hosting platform](https://docs.aws.amazon.com/managedservices/latest/appguide/app-host-platform.html): For your application hosting platform, consider the following possible requirements.
- [Application deployment model](https://docs.aws.amazon.com/managedservices/latest/appguide/app-deploy-model.html): Considerations of how you plan your application deployments.
- [Application dependencies](https://docs.aws.amazon.com/managedservices/latest/appguide/app-depends.html): Do you need instances for Line-of-Business (LoB) applications? For product applications?
- [SSL certificates for product applications](https://docs.aws.amazon.com/managedservices/latest/appguide/ssl-certs-for-prod-apps.html): What SSL certificates will your servers need so your applications (LoB and product) can reach everything they need to run and be accessible?
