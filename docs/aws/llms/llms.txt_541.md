# Source: https://docs.aws.amazon.com/m2/latest/userguide/llms.txt

# AWS Mainframe Modernization User Guide

> Describes all AWS Mainframe Modernization concepts and provides instructions on using the various features with both the console and the command line interface.

- [What is AWS Mainframe Modernization](https://docs.aws.amazon.com/m2/latest/userguide/what-is-m2.html)
- [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html)
- [Set up for AWS Mainframe Modernization](https://docs.aws.amazon.com/m2/latest/userguide/setting-up.html)
- [Concepts](https://docs.aws.amazon.com/m2/latest/userguide/concept-m2.html)
- [Modernization approach](https://docs.aws.amazon.com/m2/latest/userguide/modernization-m2.html)
- [Components lifecycle](https://docs.aws.amazon.com/m2/latest/userguide/lifecycle-m2.html)
- [AWS Transform for mainframe](https://docs.aws.amazon.com/m2/latest/userguide/qt-webapp-mainframe.html)
- [Data replication with Precisely](https://docs.aws.amazon.com/m2/latest/userguide/precisely.html)
- [Charon integration](https://docs.aws.amazon.com/m2/latest/userguide/stromasys.html)
- [Document history](https://docs.aws.amazon.com/m2/latest/userguide/doc-history.html)

## [Get started](https://docs.aws.amazon.com/m2/latest/userguide/getting-started.html)

- [Tutorial: Set up managed runtime for AWS Blu Age](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-runtime-ba.html): Learn how to create a runtime environment and an AWS Mainframe Modernization application for the AWS Blu Age engine.
- [Tutorial: Set up managed runtime for Rocket Software](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-runtime-mf.html): Learn how to create a runtime environment and an AWS Mainframe Modernization application for the Rocket Software (formerly Micro Focus) engine.


## [Managed applications](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2.html)

- [Create AWS resources for a migrated application](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-other-resources.html): Learn how to create AWS resources such as required permissions, Amazon S3 buckets, databases, and secret keys for a migrated application.
- [Create an application](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-create.html): Learn how to create AWS Mainframe Modernization applications.
- [Deploy an application](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-deploy.html): Learn how to deploy AWS Mainframe Modernization applications in the console.
- [Update an application](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-update.html): Learn how to update an application in the AWS Mainframe Modernization console.
- [Delete an application](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-delete.html): Learn how to delete an AWS Mainframe Modernization application from an environment.
- [Submit batch jobs for applications](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-batch-job.html): Learn how to submit batch jobs for AWS Mainframe Modernization applications in the console.
- [Cancel batch jobs for applications](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-cancel-batch-job.html): Learn how to cancel batch jobs for AWS Mainframe Modernization applications in the console.
- [Import data sets for applications](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-dataset.html): Learn how to import data sets for AWS Mainframe Modernization applications.
- [Export data sets for applications](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-dataset.export.html): Learn how to export data sets for AWS Mainframe Modernization applications.
- [Manage transactions for applications](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-transactions.console.html): Learn how to manage transactions for AWS Mainframe Modernization applications in the console.
- [Configure the Rocket Software managed application](https://docs.aws.amazon.com/m2/latest/userguide/mf-app-config.html): Learn how to configure your application and understand the overall structure of the Rocket Software modernized application.

### [Configure the AWS Blu Age managed application](https://docs.aws.amazon.com/m2/latest/userguide/ba-app-config.html)

Learn how to configure your application and understand the overall structure of the AWS Blu Age modernized application.

- [Structure of AWS Blu Age managed applications](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-other-resources-structure.html): Discover how the applications are structured in your Amazon S3 buckets for the AWS Blu Age runtime engine.
- [Configure access to utilities for managed applications](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-ba-utilities.html): Discover the various utility programs and learn how to manage configuration access for your AWS Blu Age runtime engine.
- [Configure additional properties for managed application](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-ba-config-props.html): Learn how to add different configurations for your refactored applications and manage access for new features to your AWS Blu Age runtime engine.
- [Application definition reference](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-definition.html): Learn more about the AWS Blu Age and Rocket Software application definitions that contain both general information and engine-specific information.
- [Data set definition reference](https://docs.aws.amazon.com/m2/latest/userguide/datasets-m2-definition.html): Learn the details for specifying supported data sets in AWS Mainframe Modernization service.


## [Managed runtime environments](https://docs.aws.amazon.com/m2/latest/userguide/environments-m2.html)

- [Create a runtime environment](https://docs.aws.amazon.com/m2/latest/userguide/create-environments-m2.html): Learn how to create an AWS Mainframe Modernization runtime environment.
- [Update a runtime environment](https://docs.aws.amazon.com/m2/latest/userguide/update-environments-m2.html): Learn how to update an AWS Mainframe Modernization runtime environment and how maintenance window works.
- [Stop a runtime environment](https://docs.aws.amazon.com/m2/latest/userguide/stop-environments-m2.html): Learn how to stop an AWS Mainframe Modernization runtime environment.
- [Restart a runtime environment](https://docs.aws.amazon.com/m2/latest/userguide/restart-environments-m2.html): Learn how to restart an AWS Mainframe Modernization runtime environment.
- [Delete a runtime environment](https://docs.aws.amazon.com/m2/latest/userguide/delete-environments-m2.html): Learn how to delete an AWS Mainframe Modernization runtime environment.


## [AWS Blu Age Refactoring](https://docs.aws.amazon.com/m2/latest/userguide/refactoring-m2.html)

### [AWS Blu Age releases](https://docs.aws.amazon.com/m2/latest/userguide/ba-releases.html)

Learn about the AWS Blu Age versioning, updates, and security handling.

- [AWS Blu Age versioning](https://docs.aws.amazon.com/m2/latest/userguide/ba-versioning.html): Learn about how the AWS Blu Age Transformation and Runtime products are versioned using a semantic versioning compliant scheme.
- [AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-options.html): Learn about the AWS Blu Age Runtime options to cater to different stages of your modernization journey and operational needs.
- [AWS Blu Age release notes](https://docs.aws.amazon.com/m2/latest/userguide/ba-release-notes.html): Learn about the different releases of AWS Blu Age Runtime and modernization tools.
- [AWS Blu Age security vulnerabilities](https://docs.aws.amazon.com/m2/latest/userguide/ba-security-cve.html): Learn about the common vulnerabilities and exposures for the AWS Blu Age engine.
- [Upgrading AWS Blu Age](https://docs.aws.amazon.com/m2/latest/userguide/ba-migration-notes.html): Learn how to upgrade the AWS Blu Age version.
- [AWS Blu Age lifecycle](https://docs.aws.amazon.com/m2/latest/userguide/ba-lifecycle.html): Learn about the AWS Blu Age engine lifecycle and end of life (EOL) dates for the engine's major versions.

### [AWS Blu Age Runtime concepts](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-concept.html)

Learn about the AWS Blu Age runtime architecture and basic concepts to understand how your applications are modernized with automated refactoring.

- [High level architecture](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-architecture.html): Learn about the AWS Blu Age Runtime engine's high level architecture, including the runtime components, execution environments, and session handling.
- [Modernized application structure](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-structure.html): Learn about the structure of modernized applications to perform various tasks with AWS Mainframe Modernization refactoring tools.
- [Understand data simplifiers](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-data.html): Learn more about what data simplifiers are and different types of constructs to modernize Java programs on the mainframe.
- [AWS Blu Age Blusam](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-blusam.html): Learn about AWS Blu Age Blusam engine's high level architecture, including Blusam intrinsics and data migration from legacy, Blusam configuration, and the Blusam Administration Console.

### [Blusam Administration Console](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-bac-userguide.html)

Learn about the AWS Blu Age Blusam Administration Console (BAC) with different endpoints and its data set handling

- [Deploying the BAC](https://docs.aws.amazon.com/m2/latest/userguide/bac-deployment.html): Learn about how the Blusam Administration Console (BAC) deploys applications.
- [Using the BAC](https://docs.aws.amazon.com/m2/latest/userguide/bac-usage.html): Learn about BAC security and permissions to use features based on the role and required authentications.
- [LISTCAT JSON format](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-bac-listcat-json-format.html): Learn about the different attributes of the LISTCAT JSON format.

### [AWS Blu Age Runtime configuration](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-config.html)

Learn to configure various YAML files in AWS Blu Age runtime engine.

- [AWS Blu Age Runtime secrets](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-config-app-secrets.html): Learn about the AWS Blu Age Runtime secrets and their configurations.
- [Enable properties](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-key-value.html): Learn different properties of the YAML files and how to configure them with AWS Blu Age Runtime.
- [Available Redis cache properties](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-redis-configuration.html): Learn about the Redis cache properties in AWS Blu Age.

### [Configure security for Gapwalk applications](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-security.html)

Configure security for Gapwalk applications.

- [Configure URI accessibility for Gapwalk applications](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-filteringURIs.html): Learn how to configure URI accessibility for Gapwalk applications.

### [Configure authentication for Gapwalk applications](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-auth.html)

Learn how configure OAuth2 authentication for Gapwalk applications for AWS Blu Age.

- [Configure Gapwalk OAuth2 authentication with Amazon Cognito](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-auth-cognito.html): Learn how to setup Gapwalk OAuth2 authentication with Amazon Cognito as the identity provider (IdP).
- [Configure Gapwalk OAuth2 authentication with Keycloak](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-auth-keycloak.html): Learn how to configure the OAuth2 authentication for Gapwalk applications using Keycloak as an identity provider (IdP).
- [Configure rate limiting for AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-rate-limiting.html): AWS Blu Age Runtime includes built-in rate limiting functionality to protect gapwalk application from excessive requests and potential abuse.

### [AWS Blu Age Runtime Error Codes](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes.html)

Learn about the AWS Blu Age versioning, updates, and security handling.

- [Generic Error Codes (BA-A)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-a.html): Generic error codes, prefixed with BA-A.
- [Error codes related to Blusam (BA-B)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-b.html): Blusam error codes, prefixed with BA-B.
- [Error codes related to Batches (BA-C)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-c.html): Batches error codes, prefixed with BA-C.
- [Error codes related to Datasimplifier (BA-D)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-d.html): Datasimplifier error codes, prefixed with BA-D.
- [Error codes related to Files (BA-F)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-f.html): Files error codes, prefixed with BA-F.
- [Error codes related to CL Command Programs (BA-H)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-h.html): CL Command pgm error codes, prefixed with BA-H.
- [Error codes related to JICS (BA-J)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-j.html): JICS error codes, prefixed with BA-J.
- [Error codes related to ADABAS (BA-N)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-n.html): ADABAS error codes, prefixed with BA-N.
- [Error codes related to Queue (BA-Q)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-q.html): Queue error codes, prefixed with BA-Q.
- [Error codes related to Redis (BA-R)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-r.html): Redis error codes, prefixed with BA-R.
- [Error codes related to Utility programs (BA-U)](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-u.html): Utility pgm error codes, prefixed with BA-U.

### [AWS Blu Age Runtime APIs](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-endpoints.html)

Discover the AWS Blu Age Runtime REST endpoints and learn how to use them.

- [Endpoints for building URLs](https://docs.aws.amazon.com/m2/latest/userguide/ba-endpoints-build-urls.html): Discover the root paths shared by all endpoints for AWS Blu Age runtime engine.
- [Endpoints for Gapwalk application](https://docs.aws.amazon.com/m2/latest/userguide/ba-endpoints-gapwalk.html): Discover different endpoints for the Gapwalk web application and learn how to configure them.
- [Blusam application console REST endpoints](https://docs.aws.amazon.com/m2/latest/userguide/ba-endpoints-bac.html): Learn about the Blusam application console API and different endpoints for the Blusam web applications.
- [Manage JICS application console](https://docs.aws.amazon.com/m2/latest/userguide/ba-endpoints-jac.html): Learn about different endpoints you may need to perform the administration tasks with the JICS application console web application.
- [Data structures](https://docs.aws.amazon.com/m2/latest/userguide/ba-endpoints-apx.html): Discover various data structures and fields in AWS Blu Age that is available for user.

### [AWS Blu Age Runtime Utilities](https://docs.aws.amazon.com/m2/latest/userguide/system-utilities.html)

Learn about system utilities supported by AWS Blu Age Runtime for JCL modernization.

- [Datasets Utilities](https://docs.aws.amazon.com/m2/latest/userguide/system-datasets-utilities.html): Utilities for managing and manipulating datasets in Blu Age applications.
- [Database Utilities](https://docs.aws.amazon.com/m2/latest/userguide/system-database-utilities.html): Database related utilities for data operations.
- [Commands Utilities](https://docs.aws.amazon.com/m2/latest/userguide/system-commands-utilities.html): Utility programs for handling user commands provided using control cards.
- [Sort Utilities](https://docs.aws.amazon.com/m2/latest/userguide/system-sort-utilities.html): Utilities for sorting, merging, and copying data from datasets based on provided criteria.
- [Other / Miscellaneous Utilities](https://docs.aws.amazon.com/m2/latest/userguide/system-misc-utilities.html): Various utilities programs with miscellaneous purposes that could not be attached to existing categories.

### [Set up AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-setup.html)

Learn how to set up AWS Blu Age Runtime on your AWS infrastructure.

- [AWS Blu Age Runtime prerequisites](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-setup-prereq.html): Learn what prerequisites to meet before testing features of AWS Blu Age Runtime for your application.
- [Onboarding AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-setup-onboard.html): Discover the access points for the different AWS Blu Age Runtime versions.
- [Infrastructure setup requirements](https://docs.aws.amazon.com/m2/latest/userguide/ba-infrastructure-setup.html): Learn about the minimum infrastructure configuration required to run AWS Blu Age Runtime.
- [AWS Blu Age Runtime artifacts](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-artifacts.html): Learn about various artifacts for AWS Blu Age Runtime.

### [Deploy AWS Blu Age Runtime on Amazon EC2](https://docs.aws.amazon.com/m2/latest/userguide/ba-deploy-ec2.html)

Learn how to deploy AWS Blu Age Runtime on Amazon EC2, and perform various other tasks.

- [Set up AWS Blu Age Runtime on Amazon EC2](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-deploy-ec2.html): Set up and deploy sample application using AWS Blu Age Runtime on Amazon EC2.
- [Upgrade the AWS Blu Age Runtime on Amazon EC2](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-maint-ec2.html): Learn how to upgrade the AWS Blu Age Runtime version on Amazon EC2.
- [Set up AWS Blu Age CloudWatch alarms on Amazon EC2](https://docs.aws.amazon.com/m2/latest/userguide/ba-cw-alarms-ec2.html): Discover how to set up CloudWatch and alarms to get notified about errors for your deployed applications.
- [Set up licensed dependencies on Amazon EC2](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-dependencies-ec2.html): Learn how to set up licensed dependencies for AWS Blu Age runtime engine on Amazon EC2.

### [Deploy AWS Blu Age Runtime on Amazon ECS and Amazon EKS](https://docs.aws.amazon.com/m2/latest/userguide/ba-deploy-container.html)

Learn how to set up AWS Blu Age Runtime on Amazon ECS and Amazon EKS to perform various tasks.

- [Set up AWS Blu Age Runtime on container](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-deploy-container.html): Set up and deploy sample application using AWS Blu Age Runtime on container.
- [Upgrade the AWS Blu Age Runtime on container](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-maint-container.html): Learn how to upgrade the AWS Blu Age Runtime on container.
- [Set up CloudWatch alarms for AWS Blu Age Runtime on container](https://docs.aws.amazon.com/m2/latest/userguide/ba-cw-alarms-container.html): Learn how to set up CloudWatch alarms for AWS Blu Age Runtime on Amazon ECS managed by AWS Fargate.
- [Set up licensed dependencies on container](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-dependencies-container.html): Learn how to set up licensed dependencies for AWS Blu Age Runtime on container.
- [Test the PlanetsDemo application](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-test-planetsdemo.html): Learn about running the test application in AWS Blu Age Runtime engine.

### [Modify the source code with Blu Age Developer IDE](https://docs.aws.amazon.com/m2/latest/userguide/ba-modify-source.html)

Learn how to use Blu Age Developer to modify the generated source code in the AWS Blu Age engine.

- [Tutorial: Set up WorkSpaces Applications for AWS Blu Age Developer IDE](https://docs.aws.amazon.com/m2/latest/userguide/set-up-appstream-ba.html): Learn how to set up AWS Blu Age Developer IDE on an WorkSpaces Applications fleet so that you can update code for modernized mainframe applications.
- [Tutorial: Use AWS Blu Age Developer on WorkSpaces Applications](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-ba-developer.html): Learn how to access AWS Blu Age Developer on WorkSpaces Applications.
- [AWS Blu Age FAQ](https://docs.aws.amazon.com/m2/latest/userguide/ba-faq.html): Find answers to frequently asked questions for AWS Blu Age.


## [Rocket Software Replatforming](https://docs.aws.amazon.com/m2/latest/userguide/replatforming-m2.html)

### [Set up Rocket Software (on Amazon EC2)](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup.html)

Learn about the various Amazon Machine Images (AMIs) that include Rocket Software (formerly Micro Focus) licensed products for AWS Mainframe Modernization.

- [Rocket Software (on Amazon EC2) prerequisites](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup-prereq.html): Learn what prerequisites to meet when setting up Rocket Software runtime engine on Amazon EC2.
- [Create the Amazon VPC endpoint for Amazon S3](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup-vpc.html): Learn how to create the Amazon VPC Endpoint for Amazon S3.
- [Request the allowlist update for the account](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup-allowlist.html): Learn how to request allowlist update for your AWS account for setting up Rocket Software runtime (on Amazon EC2).
- [Create the AWS Identity and Access Management role](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup-iam-role.html): Learn how to create the AWS Identity and Access Management role.
- [Grant License Manager the required permissions](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup-lic.html): Learn how to grant License Manager required permissions when setting up Rocket Software runtime engine (on Amazon EC2).
- [Subscribe to the Amazon Machine Images](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup-ami.html): Learn how to subscribe to the Amazon Machine Images.
- [Launch a Rocket Software instance](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup-mf-instance.html): Learn how to launch the AWS Mainframe Modernization Rocket Software instance.
- [Subnet or VPC with no internet access](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup-no-access.html): Learn what to do if your Subnet or VPC has no internet access.
- [Set up WorkSpaces Applications Automation](https://docs.aws.amazon.com/m2/latest/userguide/set-up-automation-m2.html): Learn how to set up custom automation for WorkSpaces Applications session start and end if needed for your situation.
- [View data sets as tables in Enterprise Developer](https://docs.aws.amazon.com/m2/latest/userguide/view-datasets-tables-m2.html): Learn how to view mainframe data sets as tables and columns in Rocket Enterprise Developer running under WorkSpaces Applications.
- [Edit data sets using Data File Tools in Enterprise Developer](https://docs.aws.amazon.com/m2/latest/userguide/edit-datasets-m2.html): Learn how to edit mainframe data sets using the Rocket Enterprise Developer Data File Tools.

### [Tutorials for Rocket Software](https://docs.aws.amazon.com/m2/latest/userguide/tutorials-mf.html)

Discover various tutorials that walk you through performing tasks in the Rocket Software runtime environment for AWS Mainframe Modernization.

- [Tutorial: Set up the build for the BankDemo sample application](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-build-mf.html): Learn how to set up a build for the AWS Mainframe Modernization BankDemo sample application using CodeBuild.
- [Tutorial: Set up WorkSpaces Applications for Enterprise Analyzer and Enterprise Developer](https://docs.aws.amazon.com/m2/latest/userguide/set-up-appstream-mf.html): Learn how to set up WorkSpaces Applications so you can use it to complete modernization tasks with Rocket Enterprise Analyzer (formerly Micro Focus Enterprise Analyzer) or Rocket Enterprise Developer formerly Micro Focus Enterprise Developer).
- [Tutorial: Use templates with Rocket Enterprise Developer](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-templates-ed.html): Learn how to use templates and predefined projects with Rocket Enterprise Developer.
- [Tutorial: Set up Enterprise Analyzer](https://docs.aws.amazon.com/m2/latest/userguide/set-up-ea.html): Learn how to set up Enterprise Analyzer so that you can complete modernization tasks.
- [Tutorial: Set up Enterprise Developer](https://docs.aws.amazon.com/m2/latest/userguide/set-up-ed.html): Learn how to set up Rocket Enterprise Developer (formerly Micro Focus Enterprise Developer) on WorkSpaces Applications so you can maintain, compile, and test migrated mainframe applications.

### [Batch utilities](https://docs.aws.amazon.com/m2/latest/userguide/utilities-m2.html)

Learn about different batch utility programs in mainframe applications for performing functions such as sorting, transferring, loading, and unloading data.

- [M2SFTP batch utility](https://docs.aws.amazon.com/m2/latest/userguide/m2sftp.html): Learn about M2SFTP, a JCL utility program designed to perform secure file transfers between systems using the Secure File Transfer Protocol (SFTP).
- [M2WAIT batch utility](https://docs.aws.amazon.com/m2/latest/userguide/m2wait.html): Learn about the M2WAIT a mainframe utility program that enables you to introduce a wait period in your JCL scripts.
- [TXT2PDF batch utility](https://docs.aws.amazon.com/m2/latest/userguide/txt2pdf.html): Learn about the TXT2PDF, a mainframe utility program commonly used to convert text files to PDF files.
- [M2DFUTIL batch utility](https://docs.aws.amazon.com/m2/latest/userguide/m2dfutil.html): Learn about the M2DFUTIL batch utility, a JCL utility program that provides backup, restore, delete, and copy functions on datasets.
- [M2RUNCMD batch utility](https://docs.aws.amazon.com/m2/latest/userguide/m2runcmd.html): Learn about the M2RUNCMD, a batch utility program to run Rocket Software (formerly Micro Focus) commands, scripts, and system calls directly from JCL.


## [File Transfer](https://docs.aws.amazon.com/m2/latest/userguide/filetransfer.html)

- [What is File Transfer](https://docs.aws.amazon.com/m2/latest/userguide/what-is-filetransfer.html): Learn about AWS Mainframe Modernization File Transfer, a feature of AWS Mainframe Modernization that helps you transfer files from mainframe to AWS.
- [Install a File Transfer agent](https://docs.aws.amazon.com/m2/latest/userguide/m2-agent-installation.html): Learn how to install a file transfer agent on the source mainframe.
- [Configure a File Transfer agent](https://docs.aws.amazon.com/m2/latest/userguide/m2-agent-configuration.html): Learn how to configure a file transfer agent.
- [Create data transfer endpoints](https://docs.aws.amazon.com/m2/latest/userguide/filetransfer-data-transfer-endpoints.html): Learn how to create data transfer endpoints in AWS Mainframe Modernization File Transfer.
- [Create transfer tasks](https://docs.aws.amazon.com/m2/latest/userguide/filetransfer-transfer-tasks.html): Learn how to create transfer tasks in AWS Mainframe Modernization File Transfer that allow data sets to be transferred from mainframe to Amazon S3 with code page conversion options.
- [Tutorial: Getting started with File Transfer](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-filetransfer-getting-started.html): Learn how to transfer and convert mainframe data sets for AWS Mainframe Modernization with AWS Mainframe Modernization File Transfer.
- [Supported source and target code pages](https://docs.aws.amazon.com/m2/latest/userguide/filetransfer-encodings.html): Learn what source and target code pages for conversion between mainframe and AWS cloud encodings are supported by AWS Mainframe Modernization File Transfer.


## [Assembler Conversion with mLogica](https://docs.aws.amazon.com/m2/latest/userguide/assembler-conversion.html)

- [What is Assembler Conversion with mLogica](https://docs.aws.amazon.com/m2/latest/userguide/assembler-conversion-what-is.html): Learn what is the assembler conversion that converts code from z/OS Mainframe Assembler to COBOL.
- [Understand Code conversion billing](https://docs.aws.amazon.com/m2/latest/userguide/assembler-conversion-billing.html): Learn how the Code conversion billing works in the AWS Mainframe Modernization service.
- [Code conversion concepts](https://docs.aws.amazon.com/m2/latest/userguide/assembler-conversion-concepts.html): Learn about various conversion concepts when converting code from Assembler to COBOL.
- [Understand components and process](https://docs.aws.amazon.com/m2/latest/userguide/assembler-conversion-components-process.html): Learn about the different components in the Code conversion process.
- [Tutorial: Convert code from Assembler to COBOL](https://docs.aws.amazon.com/m2/latest/userguide/assembler-conversion-steps.html): Learn about the steps required to convert code from Assembler to COBOL.


## [Replatforming with NTT DATA](https://docs.aws.amazon.com/m2/latest/userguide/unikix.html)

- [Tutorial: Deploy CardDemo application on NTT DATA](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-unikix-runtime.html): Learn about how to deploy the CardDemo sample application on NTT DATA using the UniKix runtime.


## [Security](https://docs.aws.amazon.com/m2/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/m2/latest/userguide/data-protection.html): Learn about the types of data that AWS Mainframe Modernization collects and how it encrypts the data both at rest and in transit.

### [Identity and Access Management](https://docs.aws.amazon.com/m2/latest/userguide/security-iam.html)

Learn how to authenticate requests and manage access for your AWS Mainframe Modernization resources.

### [How AWS Mainframe Modernization works with IAM](https://docs.aws.amazon.com/m2/latest/userguide/security_iam_service-with-iam.html)

Learn how the AWS Mainframe Modernization works with IAM to manage access.

- [AWS Mainframe Modernization API permissions reference](https://docs.aws.amazon.com/m2/latest/userguide/UsingWithM2_IAM_ResourcePermissions.html): Learn about permissions for
- [Identity-based policy examples](https://docs.aws.amazon.com/m2/latest/userguide/security_iam_id-based-policy-examples.html): Discover various examples of identity-based policy for AWS Mainframe Modernization.
- [Troubleshooting](https://docs.aws.amazon.com/m2/latest/userguide/security_iam_troubleshoot.html): Learn how to troubleshoot AWS Mainframe Modernization identity and access.
- [Using service-linked roles](https://docs.aws.amazon.com/m2/latest/userguide/using-service-linked-roles.html): Learn how to use service-linked roles to give AWS Mainframe Modernization access to resources in your AWS account.
- [Compliance validation](https://docs.aws.amazon.com/m2/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/m2/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Mainframe Modernization features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/m2/latest/userguide/infrastructure-security.html): Learn how AWS Mainframe Modernization isolates service traffic.
- [AWS PrivateLink](https://docs.aws.amazon.com/m2/latest/userguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Mainframe Modernization.


## [Monitoring](https://docs.aws.amazon.com/m2/latest/userguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/m2/latest/userguide/monitoring-cloudwatch.html): Learn how to set up monitoring in AWS Mainframe Modernization with Amazon CloudWatch.
- [Logging API calls with CloudTrail](https://docs.aws.amazon.com/m2/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS Mainframe Modernization with AWS CloudTrail.


## [Troubleshooting in M2](https://docs.aws.amazon.com/m2/latest/userguide/troubleshooting-m2.html)

- [Troubleshooting error: Time out while waiting for data set name to be unlocked](https://docs.aws.amazon.com/m2/latest/userguide/ba-blusam-timeout.html): Learn how to fix the time out error when an application in environment is holding a lock or shared data set.
- [Troubleshooting error: Cannot access an application URL](https://docs.aws.amazon.com/m2/latest/userguide/both-application-connectivity.html): Learn how to troubleshoot when you can't access an applications' URL.
- [Troubleshooting: AWS AWS Transform for mainframe refactor does not open from the console](https://docs.aws.amazon.com/m2/latest/userguide/ba-bi-tabclose.html): Learn how to fix when AWS AWS Transform for mainframe refactor doesn't open from the console.
- [Troubleshooting error: Environment unhealthy](https://docs.aws.amazon.com/m2/latest/userguide/env-unhealthy.html): Learn how to fix the environment unhealthy error.
- [Troubleshooting license issues for Rocket Software](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup-troubleshoot.html): Learn how to troubleshoot license issues when accessing or using Amazon Machine Images (AMIs) for Rocket Software.
