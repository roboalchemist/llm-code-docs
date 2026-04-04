# Source: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/llms.txt

# Deadline Cloud Developer Guide

> Provides a conceptual overview of AWS Deadline Cloud for developers and provides tutorials for using the various features for the console.

- [Architecture Guidance](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/architecture-guidance.html)
- [What is a Deadline Cloud workload](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/what-is-a-deadline-cloud-workload.html)
- [Using AI agents](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/ai-agents.html)
- [Document history](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/doc-history.html)

## [What is Deadline Cloud?](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/what-is-deadline-cloud.html)

- [Concepts and terminology](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/concepts-terminology.html): Learn about key concepts and terminology to help you understand how AWS Deadline Cloud works.


## [Getting started](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/getting-started.html)

- [Create a farm](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-a-farm.html): Use this tutorial to learn how to create a farm that you can use as a developer to explore the features of Deadline Cloud.
- [Run the worker agent](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/run-worker.html): Learn how to run the Deadline Cloud worker agent on your worker hosts so hat they can process Deadline Cloud jobs.
- [Submit jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/submit-a-job.html): Learn how to submit and run a sample OpenJD job using the Deadline Cloud CLI.
- [Submit jobs with attachments](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/run-jobs-job-attachments.html): Learn how to share your job's files between workstations that use different operating system.
- [Add a service-managed fleet](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/service-managed-fleet.html): Learn how developers can create an auto scaling service-managed fleet (SMF) in Deadline Cloud to provide compute capacity for large test workloads.
- [Clean up farm resources](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/cleaning-up.html): Clean up Deadline Cloud developer farm resources that you used for the getting started tutorial.


## [Build a job](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/building-jobs.html)

### [Job bundles](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle.html)

Learn how to use job bundles in AWS Deadline Cloud to define and submit rendering jobs.

- [Job template elements](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle-template.html): See the elements that you can use in Deadline Cloud job templates.
- [Task chunking](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle-chunking.html): Learn how to use task chunking to group multiple tasks together in Deadline Cloud job templates.
- [Parameter values elements](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle-parameters.html): Learn how to use the OpenJD parameter file to set Deadline Cloud job parameters.
- [Asset references elements](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle-assets.html): Learn how to use the asset reference file to list files and directories for your Deadline Cloud jobs.

### [Using files in your jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/using-files-in-your-jobs.html)

Learn how to use AWS Deadline Cloud job attachments and storage profiles to manage input and output files for your rendering jobs across different filesystems and platforms.

- [Sample project infrastructure](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/sample-project-infrastructure.html): To demonstrate using job attachments and storage profiles, set up a test environment with two separate projects.

### [Storage profiles and path mapping](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/storage-profiles-and-path-mapping.html)

Learn how to use storage profiles in AWS Deadline Cloud to model file systems on workstations and worker hosts, and generate path mapping rules for your jobs.

- [Model shared file system locations with storage profiles](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/modeling-your-shared-filesystem-locations-with-storage-profiles.html): Create storage profiles to model file system configurations for different host configurations in AWS Deadline Cloud.
- [Configure storage profiles for fleets](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configuring-storage-profiles-for-fleets.html): You can configure a fleet to include a storage profile that models the file system locations on all workers in the fleet.
- [Configure storage profiles for queues](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/storage-profiles-for-queues.html): A queue's configuration includes a list of case-sensitive names of the shared file system locations that jobs submitted to the queue require access to. for example, jobs submitted to queue Q1 require file system locations FSCommon and FS1.
- [Derive path mapping rules from storage profiles](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/deriving-path-mapping-rules-from-storage-profiles.html): Path mapping rules describe how paths should be remapped from the job to the path's actual location on a worker host.

### [Job attachments](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-attachments.html)

Use job attachments to make files not in shared directories available for your jobs, and to capture the output files if they are not written to shared directories.

### [Submitting files with a job](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/submitting-files-with-a-job.html)

Share input files that aren't on a worker host with a job.

- [How Deadline Cloud uploads files to Amazon S3](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/what-job-attachments-uploads-to-amazon-s3.html): Use a sample from GitHub and the Deadline Cloud CLI to learn how Deadline Cloud shares files from your workstation using Amazon S3.
- [How Deadline Cloud chooses the files to upload](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/how-job-attachments-decides-what-to-upload-to-amazon-s3.html): See the files and directories that Deadline Cloud uses as inputs to a job.
- [How jobs find input files](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/how-jobs-find-job-attachments-input-files.html): Learn how your Deadline Cloud jobs identify input files from job attachments.
- [Getting output files from a job](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/getting-output-files-from-a-job.html): Learn where Deadline Cloud identifies and stores the output from your jobs.
- [Using files in a dependent step](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/using-files-output-from-a-step-in-a-dependent-step.html): Learn how one step in an Deadline Cloud job can use the output from another step in the same job.

### [Create resource limits for jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-limits.html)

Limit resource usage for tasks in your job's steps.

- [Create a limit](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/job-limit-create.html): Learn how to create a limit for constrained resources in your farm.
- [Associate a limit and a queue](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/job-limit-associate.html): Learn how to associate a limit for constrained resources to a queue so jobs in the queue respect the limit.
- [Submit a job requiring limits](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/job-limit-job.html): Learn how to set a limit for a constrained resource in the job template for a Deadline Cloud processing job.

### [Submit a job](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/submit-jobs-how.html)

Learn how to submit a job to Deadline Cloud using a terminal, a script, or from inside a digital content creation application.

- [From a terminal](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/from-a-terminal.html): Using only a job bundle and the Deadline Cloud CLI, you or your more technical users can rapidly iterate on writing job bundles to test submitting a job.
- [From a script](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/from-a-script.html): To automate submitting jobs to Deadline Cloud, you can script them using tools such as bash, Powershell, and batch files.
- [From within applications](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/from-within-applications.html): To make it easy for users to submit jobs, you can use the scripting runtimes or plugin systems provided by an application.
- [Schedule jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-jobs-scheduling.html): Learn how Deadline Cloud schedules jobs on the workers in your fleets.
- [Modify jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-jobs-modifying.html): Learn how to use the AWS CLI to modify a job in Deadline Cloud.


## [Customer-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/manage-cmf.html)

- [Create a CMF](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-a-cmf.html): Learn how to create a customer-managed fleet (CMF) in AWS Deadline Cloud.
- [Worker host setup](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/worker-host.html): Learn how to set up a worker host and configure it to your specific needs.
- [Manage access](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/manage-access-windows-secrets.html): Learn how to manage access to Windows job user secrets in Deadline Cloud.
- [Install software for jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/install-software.html): This section explains how to install and configure software required for Deadline Cloud jobs.
- [Configure credentials](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/aws-credentials.html): Learn how to configure AWS credentials for Amazon EC2 instances and on-premise environments when setting up Deadline Cloud.
- [Configure network](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/cmf-network.html): Configure network endpoints for Deadline Cloud to enable outbound connections through your firewall for worker hosts.
- [Test your worker host](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/test-software.html): Learn how to test the worker agent and software installed on your Deadline Cloud worker host.
- [Create an AMI](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-ami.html): This section explains how to create an Amazon Machine Image (AMI).
- [Create fleet infrastructure](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-auto-scaling.html): This section explains how to create an Amazon EC2 Auto Scaling fleet.


## [Service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf.html)

- [Connect VPC resources to your SMF](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-vpc.html): Learn how to connect your VPC resource endpoints with your Deadline Cloud service-managed fleets.
- [Job attachments](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-job-attachments.html): Learn how to optimize job attachments performance for AWS Deadline Cloud (Deadline Cloud) service-managed fleet workers.


## [Deploy and configure custom software on workers](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/deploy-custom-software.html)

### [Configure jobs using queue environments](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configure-jobs.html)

Learn how to use queue environments to configure jobs that run on Deadline Cloud workers.

### [Control the job environment](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/control-the-job-environment.html)

You can define customized environments for your rendering jobs using queue environments.

- [Set environment variables](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/set-environment-variables.html): Open Job Description (OpenJD) environments can set environment variables that every task command within their scope uses.
- [Set the path](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/set-the-path.html): Use OpenJD environments to provide new commands in an environment.
- [Run a background daemon process](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/run-a-background-daemon-process.html): In many rendering use cases, loading the application and scene data can take a significant amount of time.
- [Provide applications for your jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/provide-applications.html): Learn how to use queue environments to load applications to process your jobs.

### [Create a conda channel using S3](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configure-jobs-s3-channel.html)

If you have custom packages for applications that are not available on the deadline-cloud or conda-forge channels you can create a conda channel that contains the packages that your environments use.

- [Create a conda package for an application or plugin](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/conda-package.html): You can combine an entire application, including dependencies, into a conda package.

### [Create a conda build recipe for Blender](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-conda-recipe-blender.html)

You can use different applications to create a conda build recipe.

- [Test your package with a Blender 4.2 render job](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/s3-channel-submit-job.html): After you have the Blender 4.2 package built and your production queue configured to use the S3 conda channel, you can submit jobs to render with the package.
- [Create a conda recipe for Maya](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-conda-recipe-maya.html): You can package commercial applications as conda packages.

### [Create a conda recipe for MtoA plugin](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-conda-recipe-mtoa-plugin.html)

You can package plugins for commercial applications as conda packages.

- [Test your package with a Maya render job](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/submit-render-maya-mtoa.html): After you have the Maya 2025 and MtoA packages built, you can submit jobs to render with the package.
- [Host configuration scripts](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-admin.html): Learn how to run administrative scripts with elevated privileges to configure workers in your Deadline Cloud service-managed fleet.


## [Using software licenses](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/license.html)

- [Connect SMF fleets to a license server](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-byol.html): Create a license server using Amazon Virtual Private Cloud and Amazon Elastic Compute Cloud for service-managed fleets in your AWS Deadline Cloud farms.
- [Connect CMF fleets to a license endpoint](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/cmf-ubl.html): Create a usage-based license endpoint using Amazon Virtual Private Cloud and Amazon Elastic Compute Cloud for your AWS Deadline Cloud farms.


## [Monitoring](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/monitoring-overview.html)

- [CloudTrail logs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/logging-using-cloudtrail.html): Learn about logging AWS Deadline Cloud with AWS CloudTrail.

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/monitoring-cloudwatch.html)

Amazon CloudWatch (CloudWatch) collects raw data and processes it into readable, near real-time metrics.

- [CloudWatch metrics](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/cloudwatch-metrics.html): Deadline Cloud sends metrics to Amazon CloudWatch.
- [Recommended alarms](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/recommended-alarms.html): Learn about the key AWS Deadline Cloud (Deadline Cloud) metrics that we recommend you monitor with Amazon CloudWatch (CloudWatch) alarms to maintain the reliability, availability, and performance of your render farm.

### [Managing events using EventBridge](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/eventbridge-integration.html)

Receive notifications when specific Deadline Cloud events such as object creation or deletion occur in an Deadline Cloud with EventBridge.

- [Events detail reference](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/events-detail-reference.html): All events from AWS services have a common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others.


## [Querying session statistics aggregated data](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/query-session-data.html)

- [Retrieving user metadata using userID](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/query-session-data-map-userid.html): Learn how to map user IDs from session statistics to usernames in AWS IAM Identity Center (IAM Identity Center).


## [Security](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security.html)

### [Data protection](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Deadline Cloud.

- [Encryption at rest](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/encryption-rest.html): AWS Deadline Cloud uses encryption keys stored in AWS Key Management Service to encrypt your data.
- [Encryption in transit](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/encryption-transit.html): AWS Deadline Cloud uses TLS 1.2 to encrypt data sent between the service and workers.
- [Key management](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/key-management.html): Learn about using AWS Key Management Service keys to encrypt your AWS Deadline Cloud data.
- [Inter-network traffic privacy](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/inter-network-traffic-privacy.html): Learn how AWS Deadline Cloud works with Amazon Virtual Private Cloud.
- [Opt out](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/opt-out.html): AWS Deadline Cloud collects certain operational information to help us develop and improve Deadline Cloud.

### [Identity and Access Management](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security-iam.html)

How to authenticate requests and manage access to your Deadline Cloud resources.

- [How Deadline Cloud works with IAM](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Deadline Cloud, learn what IAM features are available to use with Deadline Cloud.
- [Identity-based policy examples](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Deadline Cloud resources.
- [AWS managed policies](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Deadline Cloud and recent changes to those policies.
- [Service roles](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security-iam-service-roles.html): Learn how to configure and troubleshoot the IAM roles that AWS Deadline Cloud uses to manage credentials automatically.
- [Troubleshooting](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Deadline Cloud and IAM.
- [Compliance validation](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/SERVICE-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Deadline Cloud features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/infrastructure-security.html): Learn how infrastructure security works in AWS Deadline Cloud.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/vulnerability-analysis-and-management.html): Learn Configuration and vulnerability analysis for AWS Deadline Cloud.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [AWS PrivateLink](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Deadline Cloud.
- [Restricted network environments](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/network-connectivity.html): Learn about the network endpoints and domains that need to be allowlisted for Deadline Cloud client tools and applications.
- [Security best practices](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/security-best-practices.html): Learn about some of the security best practices that you can use with AWS Deadline Cloud to help secure your data.
