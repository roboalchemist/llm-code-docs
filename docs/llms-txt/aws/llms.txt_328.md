# Source: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/llms.txt

# AWS Elastic Beanstalk Developer Guide

> Read conceptual and detailed instructions for using AWS Elastic Beanstalk to quickly deploy and manage applications in the AWS cloud without worrying about the infrastructure that runs those applications.

- [What is AWS Elastic Beanstalk?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [Getting started tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)
- [Tutorials and samples](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/tutorials.html)
- [Troubleshooting](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/troubleshooting.html)
- [Resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/RelatedResources.html)
- [Document history](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/document_history.html)

## [Setting up the EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)

- [Configure the EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html): Customize your EB CLI installation with .ebignore and multiple credential storage options.
- [Using the EB CLI with Git](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cli-git.html): Configure the EB CLI for use with your local Git repository.


## [EB CLI commands](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cmd-commands.html)

- [Common options](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cmd-options.html): You can use the following options with all EB CLI commands.
- [eb abort](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-abort.html): Use the EB CLI abort command to cancel an in-progress update to an environment for configuration changes that require Amazon EC2 instance replacement.
- [eb appversion](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-appversion.html): Use the EB CLI appversion command to list and manage the versions of your Elastic Beanstalk application or update the version policy for your Elastic Beanstalk application.
- [eb clone](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-clone.html): Use the EB CLI clone command to create a duplicate environment with identical settings.
- [eb codesource](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-codesource.html): Use the EB CLI codesource command to configure CodeCommit integration.
- [eb config](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-config.html): Use the EB CLI config command to change environment configuration settings.
- [eb console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-console.html): Use the EB CLI console command to display the environment configuration dashboard.
- [eb create](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-create.html): Use the EB CLI create command to create Elastic Beanstalk environments.
- [eb deploy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-deploy.html): Use the EB CLI deploy command to deploy code changes to the instances in your Elastic Beanstalk environment.
- [eb events](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-events.html): Use the EB CLI events command to view your environment's events.
- [eb health](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-health.html): Use the EB CLI health command to view health information about your environment.
- [eb init](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-init.html): Use the EB CLI init command to configure a local repository for your Elastic Beanstalk environment and source code.
- [eb labs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-labs.html): Use the EB CLI labs commands to access experimental functionality.
- [eb list](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-list.html): Use the EB CLI list command to list application environments.
- [eb local](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-local.html): Use the EB CLI local commands to run and manage a Docker application locally.
- [eb logs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-logs.html): Use the EB CLI logs command to view logs from your environment's Amazon EC2 instances.
- [eb migrate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-migrate.html): Use the EB CLI migrate command to migrate IIS applications from Windows servers to Elastic Beanstalk environments.
- [eb open](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-open.html): Use the EB CLI open command to open application in the default browser at the environment CNAME.
- [eb platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-platform.html): Use the EB CLI platform command to view information about supported platforms and change your default platform.
- [eb printenv](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-printenv.html): Use the EB CLI printenv command to view environment properties.
- [eb restore](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-restore.html): Use the EB CLI restore command to rebuild a terminated environment.
- [eb scale](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-scale.html): Use the EB CLI scale command to change the number of EC2 instances in your environment.
- [eb setenv](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-setenv.html): Use the EB CLI setenv command to set environment properties on your Elastic Beanstalk environment.
- [eb ssh](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-ssh.html): Use the EB CLI ssh command to connect to a Linux Amazon EC2 instance in your environment using Secure Shell (SSH).
- [eb status](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-status.html): Use the EB CLI command line tool status command to view information about the environment.
- [eb swap](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-swap.html): Use the EB CLI swap command to swap CNAMEs between two Elastic Beanstalk environments.
- [eb tags](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-tags.html): Use the EB CLI tags command to add, delete, update, and list tags of AWS Elastic Beanstalk resources.
- [eb terminate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-terminate.html): Use the EB CLI terminate command to terminate your Elastic Beanstalk environment.
- [eb upgrade](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-upgrade.html): Use the EB CLI upgrade command to update your environment to use the newest available platform version.
- [eb use](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-use.html): Use the EB CLI use command to change the default environment.


## [Concepts](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.html)

- [Web server environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-webserver.html): The following diagram shows an example Elastic Beanstalk architecture for a web server environment tier, and shows how the components in that type of environment tier work together.
- [Worker environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-worker.html): AWS resources created for a worker environment tier include an Auto Scaling group, one or more Amazon EC2 instances, and an IAM role.
- [Design considerations](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.concepts.design.html): Design your Elastic Beanstalk applications to suit the widest range of use cases.


## [Managing applications](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications.html)

- [Application management console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-console.html): Introduction to the Elastic Beanstalk console for managing applications.

### [Managing application versions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-versions.html)

Create and manage versions of your Elastic Beanstalk application.

- [Version lifecycle](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-lifecycle.html): About application version lifecycle settings
- [Tagging application versions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-versions-tagging.html): Categorize your Elastic Beanstalk application versions by using tags.
- [Create a source bundle](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-sourcebundle.html): Create a compressed source bundle that meets Elastic Beanstalk requirements.
- [Building with CodeBuild](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli-codebuild.html): Use the EB CLI to build your code using AWS CodeBuild.
- [Tagging applications](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging.html): Categorize your Elastic Beanstalk applications by using tags.

### [Tagging resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html)

Categorize your AWS Elastic Beanstalk application resources by using tags.

- [Tag propagation to launch templates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.launch-templates.html): Enable AWS Elastic Beanstalk to propagate resource tags with launch templates.


## [Managing environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.html)

### [Environment management console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-console.html)

Manage your environment from the AWS Elastic Beanstalk environment page in the Elastic Beanstalk console.

- [Accessing the console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-dashboard.html): The following procedure provides steps to launch the environment management console.
- [Environment overview pane](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-dashboard-envoverview.html): This topic describes the information that the Environment overview pane provides.
- [Environment detail](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-dashboard-tabs.html): This topic describes the additional information that the environment management console provides from the left navigation pane and the tabbed pages.
- [Environment actions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-dashboard-actions.html): This topic describes the common operations that you can select to perform on your environment from the Actions drop-down menu on the environment management console.

### [Creating environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.environments.html)

Deploy multiple environments when you need to run multiple versions of your AWS Elastic Beanstalk application if, for example, you have development, integration, and production environments.

- [The create new environment wizard](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-create-wizard.html): Create an environment with the Elastic Beanstalk Management Console
- [Clone an environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.clone.html): Clone an Elastic Beanstalk environment to use the environment and its configuration settings as the foundation for a new environment.
- [Terminate an environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.terminating.html): Terminate a running AWS Elastic Beanstalk environment using the Elastic Beanstalk console to avoid incurring charges for unused AWS resources.
- [With the AWS CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-create-awscli.html): Create an Elastic Beanstalk environment with the AWS CLI
- [With the API](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-create-api.html): Create an Elastic Beanstalk environment with the Elastic Beanstalk API
- [Launch Now URL](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/launch-now-url.html): Build a custom URL that you can distribute to users who want to deploy their own application.
- [Compose environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-mgmt-compose.html): Create and update environments in groups with the AWS Elastic Beanstalk Compose Environments API.
- [Composing environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebcli-compose.html): Use the EB CLI to manage multiple AWS Elastic Beanstalk environments that are each a separate component of an SOA application.

### [Deployments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.deploy-existing-version.html)

Deploy a new or existing version of your application to your AWS Elastic Beanstalk environment.

- [Deployment options](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html): Use rolling application deployments to deploy new application versions to Amazon EC2 instances in your AWS Elastic Beanstalk environment in batches of instances.
- [Blue/Green deployments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.CNAMESwap.html): Deploy updated versions of your AWS Elastic Beanstalk application with zero downtime by swapping the CNAMEs for your environments.

### [CI/CD integration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/deployments.cicd.html)

Elastic Beanstalk integrates with many CI/CD tools to automate your application development workflow.

- [GitHub Actions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/deploying-github-actions.html): Use the Elastic Beanstalk Deploy GitHub Action to automatically deploy your application when you push code changes to your repository.

### [Configuration changes](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-updating.html)

Configure settings on your AWS Elastic Beanstalk environment and the resources that it contains.

- [Rolling updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rollingupdates.html): Use AWS Elastic Beanstalk to apply configuration changes that require instances to be redeployed in batches to avoid downtime.
- [Immutable updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environmentmgmt-updates-immutable.html): Apply AWS Elastic Beanstalk configuration changes by launching a new group of instances in an immutable environment update.

### [Platform updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.platform.upgrade.html)

Update the version of the platform that your environment is running using the Elastic Beanstalk management console.

- [Managed updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html): Schedule automatic platform updates for your AWS Elastic Beanstalk environments.
- [Upgrade a legacy environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.migration.html): Migrate your deployed Elastic Beanstalk application that uses a legacy platform version to a new environment using a non-legacy platform version so that you can get access to new features.

### [Migrate to AL2023/AL2](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.migration-al.html)

Migrate your deployed Elastic Beanstalk Linux application that uses a previous Amazon Linux AMI platform version to a new environment using an Amazon Linux 2 or Amazon Linux 2023 platform version so that you can get access to new features.

- [From AL2 to AL2023](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.migration-al.generic.from-al2.html): This topic provides guidance to migrate your application from an Amazon Linux 2 platform branch to an Amazon Linux 2023 platform branch.
- [From AL1 to AL2023/AL2](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.migration-al.generic.from-al1.html): If your Elastic Beanstalk application is based on an Amazon Linux AMI platform branch, use this section to learn how to migrate your application's environments to Amazon Linux 2 or Amazon Linux 2023.
- [Platform retirement FAQ](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.migration-al.FAQ.html): Frequently Asked Questions (FAQ) about the retirement of Amazon Linux AMI (AL1) platform versions
- [Cancel an update](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rollingupdates.cancel.html): Abort an in-progress rolling update for environment configuration changes that require Amazon EC2 instance replacement and batched application version updates.
- [Rebuild an environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-management-rebuild.html): Info on how to rebuild an AWS Elastic Beanstalk environment.
- [Environment types](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-types.html): Create a load-balanced, scalable environment or a single-instance environment for your AWS Elastic Beanstalk application.
- [Worker environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-tiers.html): Create an AWS Elastic Beanstalk worker environment to run an application that handles background-processing tasks.
- [Environment links](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-links.html): Create links to other AWS Elastic Beanstalk environments to retrieve endpoints and create a connection.
- [Recovering from invalid stack state](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-management-invalid-stack.html): Troubleshooting your AWS Elastic Beanstalk environment when it enters an invalid state due to CloudFormation resource drift


## [Configuring environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers.html)

- [Configuration using the console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-console.html): Customize and configure your AWS Elastic Beanstalk environment using the Elastic Beanstalk console.

### [Amazon EC2 instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.html)

Configure the Amazon EC2 instances in your environment.

- [Amazon EC2 instance types](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.instance-types.html): This topic explains the term instance type.
- [Configuring with the console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.console.html): Configure the Amazon EC2 instances in your environment using the Elastic Beanstalk console.
- [Managing EC2 security groups](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.instances.sg.html): When Elastic Beanstalk creates an environment, it assigns a default security group to the EC2 instances that are launched with it.
- [Configuring with the AWS CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.aws-cli.html): Configure the security groups and instance types for your Amazon EC2 instances in your environment using the AWS CLI.
- [Configuring with namespace](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.namespace.html): Configure the Amazon EC2 instances in your Elastic Beanstalk environment using the aws:autoscaling:launchconfiguration namespace.
- [IMDS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-ec2-imds.html): Configure the instance metadata service (IMDS) on the Amazon EC2 instances in your Elastic Beanstalk environment.

### [Auto Scaling group](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.as.html)

Automatically launch or terminate Amazon EC2 instances based on user-defined triggers, including specific dates and times, by using Amazon EC2 Auto Scaling with your Elastic Beanstalk application.

- [Launch templates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-launch-templates.html): Migrate your Elastic Beanstalk environment from launch configurations to launch templates for improved availability of your applications and access to the latest EC2 and Auto Scaling features.

### [Spot Instance support](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-spot.html)

This topic describes the configuration options that are available for you to manage the capacity and load balancing of Spot Instances in your Elastic Beanstalk environment.

- [Enabling Spot Instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-enable-spot.html): To take advantage of Amazon EC2 Spot Instances, set the EnableSpot option for your environment.
- [Spot allocation strategy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-spot-allocation-strategy.html): You can select any one of the allocation strategies listed in this topic for your Elastic Beanstalk environment.
- [On-Demand and Spot instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-spot-and-demand.html): You can launch and automatically scale a fleet of On-Demand Instances and Spot Instances within a single Auto Scaling group.
- [Configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-configuration-approaches.html): This topic describes the different approaches to configure Auto Scaling capacity for your Elastic Beanstalk environment.
- [Triggers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-triggers.html): The Auto Scaling group in your Elastic Beanstalk environment uses two Amazon CloudWatch alarms to trigger scaling operations.
- [Scheduled actions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-scheduledactions.html): To optimize your environment's use of Amazon EC2 instances through predictable periods of peak traffic, configure your Amazon EC2 Auto Scaling group to change its instance count on a schedule.
- [Health check setting](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environmentconfig-autoscaling-healthchecktype.html): Configure your environment's Amazon EC2 Auto Scaling group to use Elastic Load Balancing Health Checks.

### [Load balancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.elb.html)

Improve the availability and scalability of your AWS Elastic Beanstalk application by using an Elastic Load Balancing load balancer to increase availability and support the application's traffic growth.

- [Classic Load Balancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-clb.html): Use a Classic Load Balancer to route HTTP, HTTPS, or TCP request traffic to different ports on environment instances.
- [Application Load Balancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-alb.html): Use an Application Load Balancer to route application layer request traffic to different ports on environment instances based on the HTTP path.
- [Shared Application Load Balancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-alb-shared.html): Share an Application Load Balancer among multiple environments to route traffic based on the HTTP path while saving on load balancer service costs.
- [Network Load Balancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-nlb.html): Use a Network Load Balancer when you need a high-performance transport layer (layer 4; TCP/UDP) load balancer, which integrates with many AWS services.
- [Configuring dual-stack](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-elbv2-ipv6-dualstack.html): Configure your Elastic Beanstalk environments to serve both IPv4 and IPv6 protocols with dual-stack enabled load balancers.
- [Configuring access logs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-loadbalancer-accesslogs.html): You can use configuration files to configure your environment's load balancer to upload access logs to an Amazon S3 bucket.
- [Database](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.db.html): Set up, operate, and scale a relational database in the cloud for your Elastic Beanstalk application with Amazon Relational Database Service (Amazon RDS).
- [Security](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.security.html): Configure service role and virtual machine permissions for your environment.
- [Tagging environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.tagging.html): Categorize your Elastic Beanstalk environments by using tags.

### [Environment variables and software settings](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-softwaresettings.html)

Configure environment variables and other software settings for the instances in your environment.

- [Debugging](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-debugging.html): Run the AWS X-Ray daemon on the instances in your environment.
- [Log viewing](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-logging.html): Configure your environment to upload rotated logs to Amazon S3, or to stream instance or health logs to Amazon CloudWatch Logs.
- [Notifications](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.sns.html): Configure your Elastic Beanstalk environment to use Amazon Simple Notification Service to notify you of important events.

### [Amazon VPC](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.vpc.html)

Define a virtual network in your own isolated section within the AWS Cloud using Amazon Virtual Private Cloud (Amazon VPC) to deploy your Elastic Beanstalk application.

- [Migrating from EC2-Classic to a VPC](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc-ec2migration.html): This topic describes options for migrating your Elastic Beanstalk environments from an EC2-Classic platform to an Amazon Virtual Private Cloud (Amazon VPC) network.
- [Domain name](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html): Use custom domains for your Elastic Beanstalk application.


## [Configuring environments (advanced)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/beanstalk-environment-configuration-advanced.html)

### [Configuration options](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html)

You can specify the possible option values in the options file with specific API command line operations.

- [Before environment creation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-methods-before.html): Set options prior to environment creation with saved configurations and .ebextensions configuration files in your AWS Elastic Beanstalk source bundle.
- [During creation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-methods-during.html): Set options during AWS Elastic Beanstalk environment creation with options files, the Elastic Beanstalk console, or command line options.
- [After creation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-methods-after.html): Set options during environment creation by using options files, the Elastic Beanstalk console, or command line options.
- [General options](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html): Configure globally available options for your Elastic Beanstalk environment.
- [Platform specific options](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-specific.html): Configure platform-specific options for your Elastic Beanstalk environment.
- [Custom options](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuration-options-custom.html): Use the aws:elasticbeanstalk:customoption namespace to define additional configuration option settings that can be read in configuration files.

### [.Ebextensions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html)

Use configuration files (.ebextensions) to set configuration options, customize the EC2 instances in your environment, and create additional resources.

- [Option settings](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions-optionsettings.html): Define settings for configuration options in configuration files that you can include in your application source code.

### [Linux server](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers-ec2.html)

Include a configuration file to customize the software that your Elastic Beanstalk application depends on in your EC2 instances running Linux.

- [Example: Using custom Amazon CloudWatch metrics](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers-cw.html): Use Amazon CloudWatch web service to manage, monitor, and create custom metrics for your Elastic Beanstalk application running on Linux.
- [Windows server](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers-windows-ec2.html): Include a configuration file to customize the software that your Elastic Beanstalk application depends on in your EC2 instances running Windows.

### [Custom resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-resources.html)

Customize your environment resources at the same time that you deploy your Elastic Beanstalk application by including a configuration file with your source bundle.

- [Elastic Beanstalk resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers-format-resources-eb.html): The resources that Elastic Beanstalk creates for your environment have names.
- [Parameters and other keys](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions-otherkeys.html): Use parameters, outputs, and other CloudFormation keys to customize your environment.
- [Functions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions-functions.html): Use intrinsic functions to populate values in your configuration files.

### [Custom resource examples](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-environment-resources-examples.html)

Examples of configuration files that you can use to customize your Elastic Beanstalk environment.

- [Example: ElastiCache](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-environment-resources-elasticache.html): Example of how to customize your environment resources of your Elastic Beanstalk application by including an Amazon ElastiCache cluster to the environment.
- [Example: SQS, CloudWatch, and SNS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-environment-resources-sqs.html): Example of how to customize your environment resources of your Elastic Beanstalk application by adding an Amazon SQS queue, CloudWatch, and SNS to the environment.
- [Example: DynamoDB, CloudWatch, and SNS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-environment-resources-dynamodb.html): Example of how to customize your environment resources of your Elastic Beanstalk application using eb and Git, and then updating to add an DynamoDB table to the Elastic Beanstalk environment.

### [Saved configurations](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-savedconfig.html)

Save your environment's configuration settings in a configuration file that you can apply to another environment.

- [Tagging saved configurations](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-savedconfig-tagging.html): Categorize your Elastic Beanstalk saved configurations by using tags.
- [env.yaml](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html): Use an environment manifest to store environment creation parameters in your source bundle.

### [Custom image](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.customenv.html)

Create a custom AMI and use it to launch Elastic Beanstalk environments to increase provisioning speed and customize low-level components.

- [AMI based on retired platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.customenv-env-copy.html): Use the AWS CLI to create a custom AMI and create an Elastic Beanstalk environment based on it.
- [Static files](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-staticfiles.html): Use AWS Elastic Beanstalk configuration options to configure your environment's proxy server to serve static content from a folder in your source code.

### [HTTPS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.html)

Configure your Elastic Beanstalk environment to use HTTPS for your application to ensure traffic encryption for client connections to the load balancer.

### [Server certificates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.certificate.html)

Use AWS Certificate Manager to create a trusted certificate for free.

- [Create a certificate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html): Create a self signed certificate for testing or backend authentication on Elastic Beanstalk.
- [Upload a certificate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl-upload.html): Upload an HTTPS certificate to IAM for use with Elastic Beanstalk.
- [Store keys securely](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-storingprivatekeys.html): Store private keys securely in Amazon S3 and download them to your Elastic Beanstalk environment's EC2 instances during deployment.
- [Terminate HTTPS at the load balancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-elb.html): Configure your AWS Elastic Beanstalk environment's load balancer to terminate HTTPS.

### [Terminate HTTPS at the instance](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance.html)

AWS Elastic Beanstalk allows you to configure HTTPS for single-instance environments that have applications running on Docker, Tomcat, Python, Node.js, PHP, or Ruby platforms.

- [HTTPS on Docker](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance-docker.html): Configure the instances in your Docker environment to terminate HTTPS connections
- [HTTPS on Go](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance-go.html): Configure the instances in your Go environment to terminate HTTPS connections
- [HTTPS on Java](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance-java.html): Configure the instances in your Java SE environment to terminate HTTPS connections
- [HTTPS on Node.js](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance-nodejs.html): Configure the instances in your Node.js environment to terminate HTTPS connections
- [HTTPS on PHP](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance-php.html): Configure the instances in your PHP environment to terminate HTTPS connections
- [HTTPS on Python](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance-python.html): Configure the instances in your Python environment to terminate HTTPS connections
- [HTTPS on Ruby](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance-ruby.html): Configure the instances in your Ruby environment to terminate HTTPS connections
- [HTTPS on Tomcat](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance-tomcat.html): Configure the instances in your Tomcat environment to terminate HTTPS connections
- [HTTPS on .NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-singleinstance-dotnet-linux.html): Configure the instances in your .NET environment to terminate HTTPS connections.
- [HTTPS on .NET](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/SSLNET.SingleInstance.html): Configure the instances in your .NET environment to terminate HTTPS connections.
- [End-to-end encryption](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-endtoend.html): Configure your Elastic Beanstalk environment's load balancer to trust the public certificate used by your backend Amazon EC2 instances.
- [TCP Passthrough](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/https-tcp-passthrough.html): You can configure your Elastic Beanstalk environment's load balancer to relay HTTPS requests to backend instances without decrypting.
- [HTTP to HTTPS redirection](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-httpredirect.html): Configure your Elastic Beanstalk environment to redirect HTTP traffic to HTTPS, also known as forcing HTTPS.


## [Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-all-platforms.html)

- [Platforms glossary](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html): Following are key terms related to AWS Elastic Beanstalk platforms and their lifecycle.
- [Shared responsibility model](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-shared-responsibility.html): AWS Elastic Beanstalk and our customers share responsibility for platform management and updates to maintain secure and compliant environments for customer applications.
- [Platform support policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html): Elastic Beanstalk provides support for platform versions that still receive ongoing minor and patch updates.
- [Platform schedule](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-schedule.html): AWS Elastic Beanstalk provides a variety of platforms on which you can build your applications.
- [Supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html): AWS Elastic Beanstalk provides a variety of platforms on which you can build your applications.

### [Linux platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux.html)

Most of the platforms that AWS Elastic Beanstalk supports are based on Amazon Linux, a Linux server operating system from Amazon Web Services (AWS).

- [Instance deployment workflow](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.workflow.html)
- [Instance deployment workflow for ECS on AL2 and later](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.workflow.ecs-al2.html): The previous section describes the supported extensibility features throughout the phases of the application deployment workflow.
- [Platform script tools](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms-scripts.html): Use tools that AWS Elastic Beanstalk provides on platforms based on Amazon Linux in your custom scripts.

### [Extending Linux platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.html)

Extend your AWS Elastic Beanstalk environments based on Amazon Linux with your own commands, scripts, and software, to support the needs of your web application.

- [Buildfile and Procfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.build-proc.html): Some platforms allow you to customize how you build or prepare your application, and to specify the processes that run your application.
- [Platform hooks](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.hooks.html): Platform hooks are specifically designed to extend your environment's platform.
- [Configuration files](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.config-files.html): You can add configuration files to the .ebextensions directory of your application's source code to configure various aspects of your Elastic Beanstalk environment.
- [Reverse proxy configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.proxy.html): All Amazon Linux 2 and Amazon Linux 2023 platform versions use nginx as their default reverse proxy server.
- [Application example with extensions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.example.html): The following example demonstrates an application source bundle with several extensibility features that Elastic Beanstalk Amazon Linux 2 and Amazon Linux 2023 platforms support: a Procfile, .ebextensions configuration files, custom hooks, and proxy configuration files.


## [Deploying .NET (Windows)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.html)

- [QuickStart for .NET Core on Windows](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-quickstart.html): QuickStart to create and deploy a .NET Core on Windows "Hello World" application to AWS Elastic Beanstalk.
- [QuickStart for ASP.NET](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/aspnet-quickstart.html): QuickStart to create and deplay a "Hellow World" ASP.NET Windows server application to AWS Elastic Beanstalk.
- [Development environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-devenv.html): Use the AWS SDK for .NET to build .NET applications that tap into the cost-effective, scalable, and reliable AWS cloud.

### [The .NET platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.container.console.html)

Configure .NET environments for your AWS Elastic Beanstalk application.

- [Major version migration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html): Migrate from pre-v1 or from v1 to v2 of the Elastic Beanstalk Windows Server platform.

### [Deployment manifest](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-manifest.html)

Use a deployment manifest to build ASP.NET Core applications or build multiple applications that run at different paths on your website.

- [Schema reference](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-manifest-schema.html): Detailed reference for the aws-windows-deployment-manifest.json schema, including all supported properties and configuration options.
- [EC2 Fast Launch](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-ec2fastlaunch.html): Configure and use EC2 Fast Launch with Windows platform branches in AWS Elastic Beanstalk.
- [Adding a database](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.rds.html): Add a relational database to your .NET platform Elastic Beanstalk environment with an Amazon Relational Database Service DB instance running MySQL, PostgreSQL, or SQL Server.

### [The AWS Toolkit for Visual Studio](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-toolkit.html)

Develop, test, and deploy your Elastic Beanstalk .NET application with the AWS Toolkit for Visual Studio.

- [Deploy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.sdlc.create.edit.html): Info on deploying to your environment.

### [Managing environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.managing.html)

Change the provisioning and configuration of the AWS resources that are used by your Elastic Beanstalk .NET application environments with the AWS Toolkit for Visual Studio.

- [EC2 server instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.managing.ec2.html): Change your Elastic Beanstalk environment configuration to optimize for your .NET application's scalability with the AWS Toolkit for Visual Studio.
- [Elastic Load Balancing](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.managing.elb.html): Configure your Elastic Beanstalk environment's load balancing configuration to distribute application loads to improve availability for your .NET application with the AWS Toolkit for Visual Studio.
- [Auto Scaling](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.managing.as.html): Configure your Elastic Beanstalk environment's Auto Scaling configuration to automatically launch or terminate Amazon EC2 instances based on user-defined triggers to deal with traffic changes to your .NET application with the AWS Toolkit for Visual Studio.
- [Notifications](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.container.sns.html): Configure your Elastic Beanstalk environment to use the Amazon Simple Notification Service (Amazon SNS) to notify you of important events affecting your .NET application.
- [Containers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.container.html): Configure your Elastic Beanstalk environment to fine-tune the behavior of your Amazon EC2 instances and enable or disable Amazon S3 log rotation of your .NET application with the AWS Toolkit for Visual Studio.
- [Managing accounts](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.accounts.html): Manage accounts with the AWS Toolkit for Visual Studio
- [Debug](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.ec2connect.html): View a list of Amazon EC2 instances running your Elastic Beanstalk application environment through the AWS Toolkit for Visual Studio or from the AWS Management Console.
- [Monitor](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.healthstatus.html): Monitor your .NET applicationâs responsiveness and health with Elastic Beanstalk features to know that your application is available and responding to requests.
- [Deployment tools](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/deploy_NET_standalone_tool.html): Deploy your Elastic Beanstalk applications in .NET using using AWS deployment tools.
- [Migrating on-premises application](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-onpremmigration.html): Use the Elastic Beanstalk Command Line Interface (EB CLI) to migrate your .NET application from on-premises Windows Servers running IIS to an AWS Elastic Beanstalk environment.
- [Retired component recommendations](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-deprecation-recommendations.html): Information about Windows Server 2012 R2 platform branch retirements and TLS 1.2 compatibility.


## [Deploying .NET core (Linux)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-dotnet-core-linux.html)

- [QuickStart for .NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-linux-quickstart.html): Create, configure, and deploy a .NET Core on Linux application to AWS Elastic Beanstalk by using the EB CLI.
- [Development environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-linux-devenv.html): Install tools and configure your computer for .NET core on Linux application development.

### [The .NET core on Linux platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-linux-platform.html)

Configure your environment to use the features of the AWS Elastic Beanstalk .NET core on Linux platform.

- [Bundling applications](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-linux-platform-bundle-app.html): Publish self-contained or runtime-dependent .NET Core applications to AWS Elastic Beanstalk using .NET Core running on a Linux environment.
- [Procfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-linux-procfile.html): Use a Procfile to specify the .NET Core applications to run on AWS Elastic Beanstalk using the .NET Core on Linux platform.
- [Proxy server](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-linux-platform-nginx.html): Configure the NGINX proxy server for your AWS Elastic Beanstalk environment that uses the .NET Core on Linux platform.

### [The AWS Toolkit for Visual Studio](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-toolkit-linux.html)

Develop, test, and deploy your Elastic Beanstalk .NET Core application with the AWS Toolkit for Visual Studio.

### [Managing environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.managing.html)

Use the AWS Toolkit for Visual Studio to change the AWS resource provisioning and configurations used by your Elastic Beanstalk .NET application environments.

- [AWS X-Ray](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.managing.x-ray.html): Change your Elastic Beanstalk environment configuration to enable or disable AWS X-Ray with the AWS Toolkit for Visual Studio.
- [EC2 server instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.managing.ec2.html): Change your Elastic Beanstalk environment configuration to optimize for your .NET application's scalability with the AWS Toolkit for Visual Studio.
- [Elastic Load Balancing](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.managing.elb.html): Set up and edit your Elastic Beanstalk environment's load balancing configuration to distribute application loads to improve availability for your .NET application with the AWS Toolkit for Visual Studio.
- [Auto Scaling](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.managing.as.html): Configure your Elastic Beanstalk environment's Auto Scaling configuration to automatically launch or terminate Amazon EC2 instances based on user-defined triggers to deal with traffic changes to your .NET application with the AWS Toolkit for Visual Studio.
- [Notifications](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.container.sns.html): Configure your Elastic Beanstalk environment to use the Amazon Simple Notification Service (Amazon SNS) to notify you of important events affecting your .NET Core application.
- [Advanced Configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.advanced-otions.html): Configure your Elastic Beanstalk environment with AWS Toolkit for Visual Studio
- [Containers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.container.html): Configure your Elastic Beanstalk environment variables as properties for your .NET Core on Linux application with the AWS Toolkit for Visual Studio.
- [Monitor](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.healthstatus.html): Monitor your .NET applicationâs responsiveness and health with Elastic Beanstalk features to know that your application is available and responding to requests.
- [Migration from Windows to Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-linux-migration.html): Migrate your AWS Elastic Beanstalk applications from Windows to the .NET Core on Linux platform.


## [Deploying Go](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_go.html)

- [QuickStart for Go](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/go-quickstart.html): Create, configure, and deploy a Go application to AWS Elastic Beanstalk by using the EB CLI.
- [Development environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/go-devenv.html): Install tools and configure your computer for Go application development.

### [The Go platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/go-environment.html)

Configure your environment to use the features of the AWS Elastic Beanstalk Go platform.

- [Procfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/go-procfile.html): To specify custom commands to start a Go application on Elastic Beanstalk, include a file called Procfile.
- [Buildfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/go-buildfile.html): To specify a custom build and configuration command in Elastic Beanstalk for your Go application, include a file called Buildfile.
- [Proxy configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/go-nginx.html): Read about the default reverse proxy configuration for Go in Elastic Beanstalk and how to configure it.


## [Deploying Java](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Java.html)

- [QuickStart for Java](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-quickstart.html): Create, configure, and deploy a Java application to AWS Elastic Beanstalk by using the EB CLI.
- [QuickStart for Java on Tomcat](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/tomcat-quickstart.html): Create, configure, and deploy a Java JSP application for running on Apache Tomcat to AWS Elastic Beanstalk by using the EB CLI.
- [Development environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-development-environment.html): Install tools and configure your computer for Java application development.
- [Sample applications and tutorials](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-getstarted.html): Sample applications and tutorials for Java Amazon Corretto on AWS Elastic Beanstalk.

### [The Tomcat platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-tomcat-platform.html)

Learn about the AWS Elastic Beanstalk Tomcat platform â a set of environment configurations for Java web applications that can run in a Tomcat web container.

- [Bundling WAR files](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-tomcat-multiple-war-files.html): Create a compressed source bundle that contains multiple WAR files.
- [Structuring your project folder](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-tomcat-platform-directorystructure.html): Organize your Tomcat source code for use with Elastic Beanstalk.
- [Proxy configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-tomcat-proxy.html): The Tomcat platform uses nginx (the default) or Apache HTTP Server as the reverse proxy to relay requests from port 80 on the instance to your Tomcat web container listening on port 8080.

### [The Java SE platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-se-platform.html)

Learn about AWS Elastic Beanstalk's Java SE platform.

- [Buildfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-se-buildfile.html): You can build your application's class files and JAR(s) on the EC2 instances in your environment by invoking a build command from a Buildfile file in your source bundle.
- [Procfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-se-procfile.html): If you have more than one JAR file in the root of your application source bundle, you must include a Procfile file that tells Elastic Beanstalk which JAR(s) to run.
- [Proxy configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-se-nginx.html): Elastic Beanstalk uses nginx as the reverse proxy to map your application to your Elastic Load Balancing load balancer on port 80.
- [Adding a database](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-rds.html): Add a relational database to your Java SE or Java with Tomcat platform Elastic Beanstalk environment with an Amazon Relational Database Service (Amazon RDS) DB instance running MySQL, PostgreSQL, Oracle, or SQL Server.
- [Resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Java.resources.html): Use these related resources for additional help in developing your Java applications.


## [Deploying Node.js](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs.html)

- [QuickStart for Node.js](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-quickstart.html): Create, configure, and deploy a Node.js application to AWS Elastic Beanstalk by using the EB CLI.
- [Development environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-devenv.html): Install tools and configure your computer for Node.js application development.

### [The Node.js platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs.container.html)

Configure your environment to use the features of the AWS Elastic Beanstalk Node.js platform.

- [Procfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-configuration-procfile.html): To specify custom commands to start a Node.js application on Elastic Beanstalk, include a file called Procfile.
- [Configuring dependencies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-platform-dependencies.html): Configuring the Node.js modules dependencies for your application.
- [npm shrinkwrap file](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-platform-shrinkwrap.html): Lock down your Node.js application dependencies on Elastic Beanstalk with an npm-shrinkwrap.json file.
- [Proxy configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-platform-proxy.html): Configure the proxy server for your Node.js application for either NGINX or Apache on Elastic Beanstalk
- [Sample applications and tutorials](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-getstarted.html): Sample applications and tutorials for Node.js on AWS Elastic Beanstalk.
- [Tutorial - Express](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs_express.html): Deploy a sample Node.js application to Elastic Beanstalk using the EB CLI and then update the application to use the Express framework.
- [Tutorial - Express with clustering](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-express-clustering.html): Example of deploying a sample Express Node.js application with clustering to Elastic Beanstalk.
- [Tutorial - Node.js w/ DynamoDB](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-dynamodb-tutorial.html): Deploy a sample Node.js application that uses DynamoDB and Amazon SNS with the AWS SDK for JavaScript in Node.js and Elastic Beanstalk configuration files.
- [Adding a database](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-nodejs.rds.html): Add an Amazon Relational Database Service to your Node.js Elastic Beanstalk environment running MySQL, PostgreSQL, Oracle, or SQL Server.
- [Resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs.resources.html): Additional resources for developing your Node.js applications.


## [Deploying PHP](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_PHP_eb.html)

- [QuickStart for PHP](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-quickstart.html): Create, configure, and deploy a PHP application to AWS Elastic Beanstalk by using the EB CLI.
- [PHP platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_PHP.container.html): Configure your environment to use the features of the AWS Elastic Beanstalk PHP platform.

### [Advanced examples](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-samples.html)

Example applications for PHP on AWS Elastic Beanstalk

- [Adding a database](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_PHP.rds.html): Add a relational database to your PHP platform Elastic Beanstalk environment with an Amazon Relational Database Service DB instance running MySQL, PostgreSQL, Oracle, or SQL Server.
- [Tutorial - Laravel](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-laravel-tutorial.html): Example of how to deploy your sample PHP application to Elastic Beanstalk and use the Laravel framework.
- [Tutorial - CakePHP](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-cakephp-tutorial.html): Example of how to deploy your sample PHP application to Elastic Beanstalk and use the CakePHP framework.
- [Tutorial - Symfony](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-symfony-tutorial.html): Generate and deploy a basic Symfony application on Elastic Beanstalk.
- [Tutorial - HA production](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-ha-tutorial.html): Example of how to deploy your sample PHP application to Elastic Beanstalk and manage an RDS database instance.
- [Tutorial - HA WordPress](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-hawordpress-tutorial.html): Use this example to learn how to deploy your sample WordPress website to Elastic Beanstalk and manage an Amazon RDS database instance.
- [Tutorial - HA Drupal](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-hadrupal-tutorial.html): Example of how to deploy your sample Drupal website to Elastic Beanstalk and manage an RDS database instance.


## [Deploying Python](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-apps.html)

- [QuickStart for Python](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-quickstart.html): Create, configure, and deploy a Python application to AWS Elastic Beanstalk by using the EB CLI.
- [Development environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-development-environment.html): Install tools and configure your computer for Python application development.

### [The Python platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-container.html)

Configure your environment to use the features of the AWS Elastic Beanstalk Python platform.

- [Procfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-configuration-procfile.html): Configuring the WSGI server for your Elastic Beanstalk Python application with a Procfile.
- [Specifying dependencies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-configuration-requirements.html): Configure you Elastic Beanstalk Python application to install other Python packages that it requires.
- [Tutorial - flask](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html): Create, configure and deploy a Flask application to AWS Elastic Beanstalk with the EB CLI.
- [Tutorial - Django](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html): Create, configure and deploy a Django application to AWS Elastic Beanstalk with the EB CLI.
- [Adding a database](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html): Add a relational database to your Python platform Elastic Beanstalk environment with an Amazon Relational Database Service DB instance running MySQL, PostgreSQL, Oracle, or SQL Server.
- [Resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-tools-resources.html): Additional resources for developing your Python applications on Elastic Beanstalk.


## [Deploying Ruby](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Ruby.html)

- [Development environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ruby-development-environment.html): Install tools and configure your computer for Ruby application development.

### [The Ruby platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Ruby.container.html)

Configure your environment to use the features of the AWS Elastic Beanstalk Ruby platform.

- [Gemfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ruby-platform-gemfile.html): Include a Gemfile in your Elastic Beanstalk environment to use RubyGems to install packages that your application requires.
- [Procfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ruby-platform-procfile.html): Use a Procfile to specify the command that starts your Ruby application on Elastic Beanstalk
- [Tutorial - rails](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ruby-rails-tutorial.html): Deploy a Rails application to an AWS Elastic Beanstalk environment using the EB CLI and Git.
- [Tutorial - sinatra](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ruby-sinatra-tutorial.html): Deploy a Sinatra application to AWS Elastic Beanstalk.
- [Adding a database](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Ruby.rds.html): Add a relational database to your Ruby platform Elastic Beanstalk environment with an Amazon Relational Database Service DB instance running MySQL, PostgreSQL, Oracle, or SQL Server.


## [Deploying with Docker](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.html)

- [Docker platform branches](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker-platform.html): The Elastic Beanstalk Docker platform supports the following platform branches: Docker running on Amazon Linux and ECS-based Docker running on Amazon Linux.

### [Docker platform branch](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker.html)

Deploy a sample Docker application and configure your deployment and environment for an application running on the platforms Docker running Amazon Linux 2 and Docker running AL2023.

- [QuickStart for Docker](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker-quickstart.html): Create, configure, and deploy a Docker application to AWS Elastic Beanstalk by using the EB CLI.
- [QuickStart for Docker Compose](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker-compose-quickstart.html): Create, configure, and deploy a multi-container Docker Compose application to AWS Elastic Beanstalk by using the EB CLI.
- [Docker image configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/single-container-docker-configuration.html): Prepare your Docker image for deployment to Elastic Beanstalk.

### [ECS managed platform branch](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecs.html)

Elastic Beanstalk supports the Amazon ECS-managed Docker platform branch.

### [ECS managed Docker configuration for Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecs_config.html)

Configure your ECS managed Docker environment.

- [Dockerrun.aws.json v2 file](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_v2config.html): Use a Dockerrun.aws.json v2 file to configure applications in an Elastic Beanstalk ECS managed Docker environment.
- [Container managed policy and EC2 instance role](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecs_role.html): If your environment uses a custom EC2 instance profile, to retain the required permissions attach the AWSElasticBeanstalkMulticontainerDocker managed policy to it.
- [Multiple Elastic Load Balancing listeners](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecs_listeners.html): Configure multiple Elastic Load Balancing listeners on a ECS managed Docker environment in order to support inbound traffic for proxies or other services that don't run on the default HTTP port.
- [Tutorial - ECS managed Docker](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecstutorial.html): Follow the steps in this tutorial to configure an ECS managed Docker environment that uses two containers.
- [Migration to ECS running on AL2023](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/migrate-to-ec2-AL2-platform.html): Migrate your application from platform branch Multi-container Docker running on 64bit Amazon Linux to ECS Running on AL2023.
- [Authenticating with image repositories](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker-configuration.remote-repo.html): There are multiple options for authenticating to private repositories and Amazon ECR Public with Elastic Beanstalk.
- [Environment configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.container.console.html): Configure software settings for your Docker application.

### [Legacy platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_dockerpreconfig-legacy.html)

Reference to migrate your applications from the retired Elastic Beanstalk Docker platforms

- [(Legacy) Migrating to Docker running on Amazon Linux 2](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker-multicontainer-migration.html): Migrate your docker application to Docker Compose, by translating the Dockerrun.aws.json file.
- [(Legacy) Docker GlassFish containers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_dockerpreconfig.html): Migrate your applications from the retired preconfigured Docker Glassfish platform.


## [Monitoring environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-health.html)

- [Monitoring console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-health-console.html): Use the Elastic Beanstalk Management Console to monitor environment and instance health.
- [Monitoring health with CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-ebcli.html): Use the Elastic Beanstalk Command Line Interface (EB CLI) to get health information about your environment and the AWS resources that comprise it.
- [Basic health reporting](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.healthstatus.html): Track your applicationâs responsiveness and health with AWS Elastic Beanstalk features that allow you to monitor statistics about your application and create alerts that trigger when thresholds are exceeded.

### [Enhanced health reporting and monitoring](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html)

Monitor application and operating system metrics with AWS Elastic Beanstalk enhanced health reporting.

- [Enable enhanced health](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-enable.html): Enable enhanced health reporting to get a more accurate picture of your AWS Elastic Beanstalk environment's health.
- [Health console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-console.html): Use the AWS Elastic Beanstalk console to get health information about your environment and the AWS resources that comprise it.
- [Health colors and statuses](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html): Learn about the colors and statuses used by AWS Elastic Beanstalk enhanced health reporting.

### [Instance metrics](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-metrics.html)

Learn about the metrics output by the instances in your AWS Elastic Beanstalk environment.

- [IIS metrics capture](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-metrics-server-iis.html): Learn about implementation details of capturing web server metrics from IIS on Windows Server platforms in your AWS Elastic Beanstalk environment.
- [Enhanced health rules](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-rules.html): Configure the health check rules for AWS Elastic Beanstalk environments with enhanced health to adapt to nonstandard application behavior.
- [CloudWatch](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-cloudwatch.html): Publish additional metrics to Amazon CloudWatch to track changes in the health of your AWS Elastic Beanstalk environment.
- [API users](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-api.html): Use the AWS Elastic Beanstalk API to get health information about your environment and the AWS resources that comprise it.
- [Enhanced health log format](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-serverlogs.html): Customize your application's logging to integrate with Elastic Beanstalk enhanced health monitoring.
- [Notifications and troubleshooting](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-health-enhanced-notifications.html): Troubleshoot issues reported by AWS Elastic Beanstalk enhanced health reporting.
- [AI-Powered Environment Analysis](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-ai-analysis.html): Use AI-powered analysis to identify root causes and get solutions for environment health issues in AWS Elastic Beanstalk.
- [Manage alarms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.alarms.html): Create alarms for metrics of your AWS Elastic Beanstalk application that you are monitoring by using the Elastic Beanstalk console.
- [View change history](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.changehistory.html): Use the AWS Management Console to access configuration changes in your Elastic Beanstalk environments.
- [View events](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.events.html): Use the AWS Management Console to access events and notifications associated with your Elastic Beanstalk application.
- [Monitor instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.ec2connect.html): View a list of Amazon EC2 instances running your Elastic Beanstalk application environment through the AWS Management Console.
- [View instance logs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.logging.html): Access logs from the Amazon EC2 instances in your environment by viewing a snapshot of the logs in or downloading all logs from the Elastic Beanstalk console, or by configuring your environment to publish logs to an Amazon S3 bucket.


## [Integrating AWS services](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.html)

- [CloudFront](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudfront.html): After you create and deploy your Elastic Beanstalk, you can use Amazon CloudFront to distribute your web content through a network of edge locations around the world.
- [CloudTrail](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudtrail.html): After you create and deploy your Elastic Beanstalk application, you can use AWS CloudTrail to capture AWS API calls for your account and view the history in log files.
- [CloudWatch](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudwatch.html): After you create and deploy your Elastic Beanstalk, you can use Amazon CloudWatch to monitor, manage, and publish various metrics, as well as configure alarm actions based on data from metrics.

### [CloudWatch Logs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.html)

Elastic Beanstalk integrates with Amazon CloudWatch Logs to monitor log files for your Elastic Beanstalk application and system, and to monitor custom log files.

- [Streaming environment health](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.envhealth.html): Elastic Beanstalk integrates with Amazon CloudWatch Logs to monitor environment health information about environments configured to use enhanced health reporting.
- [EventBridge](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.eventbridge.html): Learn about monitoring Elastic Beanstalk with Amazon EventBridge
- [AWS Config](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.config.html): Use AWS Config to discover your Elastic Beanstalk resources, learn about resource relationships, track resource configuration changes, see the effects of these changes, and create rules to alert you when a resource is noncompliant.
- [DynamoDB](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.dynamoDB.html): You can use Elastic Beanstalk with Amazon DynamoDB, a fully managed NoSQL database service, to provide fast and predictable performance with seamless scalability.
- [ElastiCache](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.ElastiCache.html): You can use Elastic Beanstalk with Amazon ElastiCache web service to set up, manage, and scale distributed in-memory cache environments in the cloud.
- [Amazon EFS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/services-efs.html): You can use Amazon Elastic File System to create a file system that's shared by all of the instances in your AWS Elastic Beanstalk environment.

### [IAM](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.html)

You can use AWS Elastic Beanstalk with AWS Identity and Access Management (IAM) to securely control access to your AWS resources and keep your account credentials private.

- [Instance profiles](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-instanceprofile.html): Use IAM to modify the default Elastic Beanstalk instance profile or create your own.
- [Service roles](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-servicerole.html): Use IAM to modify the default Elastic Beanstalk service role or create your own.

### [Using service-linked roles](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-service-linked-roles.html)

How to use service-linked roles to give Elastic Beanstalk access to resources in your AWS account.

- [Monitoring role](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-service-linked-roles-monitoring.html): How to use service-linked roles to give Elastic Beanstalk access to resources in your AWS account.
- [Maintenance role](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-service-linked-roles-maintenance.html): How to use service-linked roles to give Elastic Beanstalk access to resources in your AWS account.
- [Managed-updates role](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-service-linked-roles-managedupdates.html): How to use service-linked roles to give Elastic Beanstalk access to resources in your AWS account.
- [User policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html): Use AWS Elastic Beanstalk managed user policies to assign full access or read-only access to all Elastic Beanstalk resources.
- [ARN format](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html): You specify a resource for an IAM policy using that resource's Amazon Resource Name (ARN).
- [Resources and conditions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html): You can use resources and conditions in policy statements to grant permissions that allow specific Elastic Beanstalk actions to be performed on specific Elastic Beanstalk resources.
- [Tag-based access control](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.access-tags.html): You can use tags in IAM policy statement conditions to control permissions to Elastic Beanstalk resources and requests.
- [Example managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ExamplePolicies_AEB.html): Example of a use case that demonstrates controlling user access to AWS Elastic Beanstalk.
- [Example resource-specific policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.example.resource.html): Example of a use case for controlling user permissions for Elastic Beanstalk actions that access specific Elastic Beanstalk resources and the sample policies that support the use case.
- [Cross-environment S3 bucket access](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.cross-env-s3-access.html): Elastic Beanstalk managed policies may allow cross-environment S3 bucket access.

### [Amazon RDS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html)

You can use AWS Elastic Beanstalk with Amazon Relational Database Service (Amazon RDS) web service to set up, operate, and scale a relational database in the cloud.

- [Amazon RDS in default VPC](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/rds-external-defaultvpc.html): Launch an Amazon Relational Database Service (Amazon RDS) instance in a default VPC and use it with AWS Elastic Beanstalk.
- [Amazon RDS credentials and Secrets Manager](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/rds-external-credentials.html): Enhance the security of the Amazon Relational Database Service (Amazon RDS) instance you use with AWS Elastic Beanstalk by storing connection information in AWS Secrets Manager.
- [Amazon S3](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.S3.html): You can use Elastic Beanstalk with Amazon S3 simple web service to provide highly durable, fault-tolerant data storage.

### [Secrets Manager & Systems Manager Parameter Store](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.secrets.html)

You can use Elastic Beanstalk environment variables using Amazon Resource Names (ARNs) to securely access sensitive information, such as credentials and API keys, and other configuration values in AWS Secrets Manager and AWS Systems Manager Parameter Store.

- [Fetch secrets to environment variables](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.secrets.env-vars.html): Elastic Beanstalk can fetch values from AWS Secrets Manager and AWS Systems Manager Parameter Store during instance bootstrapping and assign them to environment variables for your application to use.
- [Required IAM permissions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.secrets.IAM-permissions.html): You must grant the necessary permissions to your environmentâs EC2 instances to fetch the secrets and parameters for AWS Secrets Manager and AWS Systems Manager Parameter Store.
- [Using Secrets Manager and Systems Manager Parameter Store](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.secrets.Secrets-Manager-and-Parameter-Store.html): This topic provides a brief introduction of AWS Secrets Manager and AWS Systems Manager Parameter Store, pricing information, and references to learn more about creating and retrieving secrets, using both the console and programmatic options.
- [Troubleshooting secrets and environment variables](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.secrets.troubleshoot.html)

### [Amazon VPC](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc.html)

Amazon Virtual Private Cloud (Amazon VPC) enables you to define a virtual network in your own isolated section within the AWS Cloud, known as a virtual private cloud (VPC).

- [Bastion hosts](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc-bastion-host.html): To connect to your instances, you need to create and connect to a bastion host in your public subnet.
- [Amazon RDS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc-rds.html): This example shows you how to deploy an Elastic Beanstalk application with Amazon RDS in an Amazon Virtual Private Cloud (Amazon VPC) using a NAT instance.
- [VPC endpoints](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc-vpce.html): Configure interface VPC endpoints, which support IPv4, IPv6, and dual-stack traffic, to privately connect your Amazon Virtual Private Cloud (Amazon VPC) to AWS Elastic Beanstalk, other supported AWS services, and VPC endpoint services powered by AWS PrivateLink.
- [VPC endpoint policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc-vpce.policy.html): Attach a policy to a VPC endpoint to control access to your Elastic Beanstalk environment.


## [Security](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Elastic Beanstalk.

- [Data encryption](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-data-protection-encryption.html): Learn about data encryption in AWS Elastic Beanstalk.
- [Internetwork privacy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-data-protection-internetwork.html): Learn about internetwork traffic privacy in AWS Elastic Beanstalk.

### [Identity and access management](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-iam.html)

Learn how to authenticate requests and manage access to your AWS Elastic Beanstalk resources.

- [AWS managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Elastic Beanstalk that you can use to grant permissions.
- [Logging and monitoring](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/incident-response.html): Learn about logging and monitoring in AWS Elastic Beanstalk.
- [Compliance validation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as specific AWS Elastic Beanstalk features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/infrastructure-security.html): Learn how AWS Elastic Beanstalk isolates service traffic.
- [Shared responsibility model](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vulnerability-analysis-and-management.html): AWS Elastic Beanstalk and our customers share responsibility for platform management and updates to maintain secure and compliant environments for customer applications.
- [Security best practices](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-best-practices.html): Follow these security best practices to improve reliability, security, availability, and performance of your AWS Elastic Beanstalk solutions.


## [Permissions](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-roles.html)

- [Service role](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-roles-service.html): A service role is the IAM role that Elastic Beanstalk assumes when calling other services on your behalf.
- [Instance profile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-roles-instance.html): An instance profile is an IAM role that's applied to Amazon EC2 instances that are launched in your Elastic Beanstalk environment.
- [User policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-roles-user.html): Create IAM users for each user who uses Elastic Beanstalk to avoid using your root account or sharing credentials.


## [Migrating IIS applications](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications.html)

- [Prerequisites](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications-prerequisites.html): Before using the eb migrate command, ensure your environment meets these requirements:
- [Migration glossary](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications-glossary.html): Key terms and concepts for IIS to Elastic Beanstalk migration.
- [Basic IIS migrations](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications-basic-migration.html): Learn how to perform basic migrations of IIS applications to Elastic Beanstalk.
- [Network configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications-network.html): Configure network settings, VPC options, and port configurations during IIS migration.
- [Security configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications-security.html): Configure security settings, IAM roles, and SSL certificates during IIS migration to AWS Elastic Beanstalk.
- [IIS to Elastic Beanstalk migration mapping](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications-mapping.html): Learn how IIS components are mapped to Elastic Beanstalk resources during migration.
- [Advanced migration scenarios](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications-advanced-scenarios.html): Handle complex IIS migration scenarios to Elastic Beanstalk, including multi-site deployments, ARR configurations, and virtual directory management.
- [Troubleshooting and diagnostics](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications-troubleshooting.html): Diagnose and resolve common issues during IIS migration to Elastic Beanstalk.
- [Migration options: EB CLI vs. MGN](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-migrating-applications-comparison.html): Compare Elastic Beanstalk migration using the EB CLI with AWS Application Migration Service (MGN) to choose the right approach for your Windows applications.


## [Archived content](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebdg.archived-content.html)

- [Custom platforms (retired)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html): Retired / Archived - Elastic Beanstalk custom platforms
