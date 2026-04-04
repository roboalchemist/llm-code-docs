# Source: https://docs.aws.amazon.com/simspaceweaver/latest/userguide/llms.txt

# AWS SimSpace Weaver User Guide for version 1.17.0

> Learn how to use SimSpace Weaver to build and run large-scale spatial simulations in the AWS Cloud.

- [AWS SimSpace Weaver end of support](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/simspaceweaver-end-of-support.html)
- [Best practices](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/best-practices.html)
- [Endpoints and service quotas](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/service-quotas.html)
- [API references](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/api-reference.html)
- [Document history](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/document-history.html)

## [What is SimSpace Weaver?](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is.html)

- [Key concepts](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is_key-concepts.html): Learn key concepts about SimSpace Weaver and how it works.
- [Example use cases](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is_example-use-cases.html): Learn about some example use cases for SimSpace Weaver.


## [Setting up](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/setting-up.html)

- [Set up your account](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/setting-up_account.html): Follow these steps to set up your AWS account to use SimSpace Weaver.

### [Set up your local environment](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/setting-up_local.html)

SimSpace Weaver simulations run in containerized Amazon Linux 2 (AL2) environments.

- [AL2 in Docker](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/setting-up_local_docker.html): This section provides instructions for setting up your local SimSpace Weaver distribution zip with an AL2 environment in Docker.
- [AL2 in WSL](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/setting-up_local_wsl.html): This section provides instructions for setting up your SimSpace Weaver distribution zip with an AL2 environment in Windows Subsystem for Linux (WSL).
- [Use of licensed software](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/setting-up_byol.html): AWS SimSpace Weaver allows you to build simulations with your choice of simulation engine and content.


## [Getting started](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/getting-started.html)

- [Quick start tutorial](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/getting-started_quickstart.html): This tutorial guides you through the process to build and run a simulation in minutes.
- [Detailed tutorial](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/getting-started_detailed.html): This tutorial will guide you through the details of the build and deployment process for the sample application.


## [Working with SimSpace Weaver](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with.html)

### [Configuring your simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation.html)

A simulation schema (or schema) is a YAML-formatted text file that specifies the configuration for a simulation.

- [SDK version](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_sdk-version.html): The sdk_version field specifies the version of SimSpace Weaver that the schema is formatted for.
- [Simulation properties](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_simulation-properties.html): The simulation_properties section of your schema specifies the logging configuration and a data type for the index field (usually the spatial location) of entities.
- [Workers](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_workers.html): The workers section specifies the type and number of workers that you want for your simulation.
- [Clock](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_clock.html): The clock section specifies properties of the simulation clock.
- [Partitioning strategies](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_partitioning-strategies.html): The partitioning_strategies section specifies configuration properties for the partitions of spatial apps.

### [Domains](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_domains.html)

You provide a name for a set of configuration properties for a domain.

- [App configuration](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_domains_app-config.html): You specify the configuration of an app (app_config) as part of the configuration for its domain.
- [Configuring spatial domains](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_domains_spatial.html): For spatial domains, you must specify a partitioning_strategy.
- [Network endpoints](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_domains_endpoints.html): Custom and service apps can have network endpoints that external clients can connect to.
- [Configuring service domains](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation_domains_service-domains.html): The presence of launch_apps_per_worker: in a domain configuration indicates that it is a service domain that has service apps.
- [Maximum duration](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_max-duration.html): Each simulation in AWS SimSpace Weaver has a maximum duration setting that specifies the maximum time that the simulation can run.
- [Developing apps](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_developing-apps.html): SimSpace Weaver development requires an Amazon Linux 2 (AL2) environment to build apps because your simulations run on Amazon Linux in the AWS Cloud.
- [Developing client applications](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_developing-client-applications.html): Some of the reasons you might want to connect a client to a simulation include:
- [Get the IP address and port number](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_get-ip.html): To view your simulation, you create a custom app and connect to it with a client.
- [Launching the Unreal Engine view client](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_unreal-client.html): Navigate to:

### [Local development](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_local-development.html)

You can deploy your SimSpace Weaver applications locally for rapid testing and debugging.

- [Step 1: Launch your local simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_local_launch.html)
- [Step 2: View your local simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_local-development_view.html): To view your local simulation, you can use any of the clients that are included with the SimSpaceWeaverAppSdkDistributable.
- [Step 3: Stop your local simulation (optional on Windows)](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_local-development_stop-sim.html)
- [Troubleshooting local development](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_local-development_troubleshooting.html)

### [SimSpace Weaver app SDK](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk.html)

The SimSpace Weaver app SDK provides APIs that you can use to control the entities in your simulation and respond to SimSpace Weaver events.

- [API methods return a Result](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_return-result.html): The majority of SimSpace Weaver API functions have a return type Aws::WeaverRuntime::Result<T>.
- [Interacting with the app SDK at the top level](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_top-level.html)

### [Simulation management](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_sim.html)

This section describes solutions for common simulation management tasks.

- [Start a simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_sim_start.html): Use CreateApplication() to create an app.
- [Update a simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_sim_update.html): Use the following BeginUpdate functions to update the app:
- [Terminate a simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_sim_terminate.html): Use Result<void> DestroyApplication(Application&& app) to terminate the app and the simulation.
- [Subscriptions](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_sub.html): You create a subscription with a subscription area and a domain ID.

### [Entities](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_ent.html)

You call the Store and Load APIs using the Api:Entity of the Result<Api::Entity> returned from CreateEntity(), or from an ownership change event when an entity enters the app's subscription area (for more information, see ).

- [Create entities](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_ent_create.html): Use CreateEntity() to create an entity.
- [Transfer an entity to a spatial domain](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_ent_transfer.html): After a custom app or service app creates an entity, the app must transfer the entity to a spatial domain in order for the entity to exist spatially in the simulation.

### [Write and read entity field data](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_ent_readwrite.html)

All entity data fields are blob types.

- [Store the field data of an entity](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_ent_readwrite_store.html): The following examples demonstrate how you can store (write to the state fabric) the field data of an entity that the app owns.
- [Load the field data of an entity](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_ent_readwrite_load.html): The following examples demonstrate how you can load (read from the state fabric) the field data of an entity.
- [Loading the field data of removed entities](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_ent_readwrite_load-removed.html): You canât load (read from the state fabric) entity field data for entities that have been removed from the appâs ownership and subscription areas.
- [Store the position of an entity](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_ent_store-position.html): You can store (write to the state fabric) the position of an entity using an integer data structure.
- [Load the position of an entity](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_ent_load-position.html): You can load (read from the state fabric) the position of an entity using an integer data structure.

### [Entity events](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_events.html)

You can use the following functions in the SimSpace Weaver app SDK to get all ownership and subscription events:

- [Iterate through events for owned entities](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_events_own.html): Use OwnershipChanges() to get a list of events for owned entities (entities in the app's ownership area).
- [Iterate through events for subscribed entities](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_events_sub.html): Use AllSubscriptionEvents() to get a list of events for subscribed entities (entities in the app's subscription area).
- [Iterate through ownership change events for entities](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_events_change.html): To get events where an entity moves between an ownership area and subscription area, compare the changes between the current and previous entity ownership and subscription events.
- [Result and error handling](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_result.html): The Aws::WeaverRuntime::Result<T> class uses a third-party Outcome library.
- [Generics and domain types](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_generics.html): The SimSpace Weaver app SDK provides the single-precision data types Api::Vector2F32 and Api::BoundingBox2F32, and the double-precision Api::Vector2F64 and Api::BoundingBox2F64.

### [Miscellaneous app SDK operations](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_misc.html)

- [AllSubscriptionEvents and OwnershipChanges](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_misc_events-from-last-call.html): The return values of calls to Api::AllSubscriptionEvents() and Api::OwnershipChanges() contain events from the last call, not the last tick.
- [Release read locks](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_misc_release-locks.html): When you begin an update, there are shared memory segments for the committed data in other partitions for the previous tick.
- [Create an app for testing](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_app-sdk_misc_testing-app.html): You can use Api::CreateStandaloneApplication() to create a standalone app to test app logic before running the code in an actual simulation.
- [SimSpace Weaver demo framework](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_demo-framework.html): The AWS SimSpace Weaver demo framework (demo framework) is a library of utilities that you can use to develop SimSpace Weaver apps.
- [Working with quotas](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_quotas.html): Learn how to work with service quotas for SimSpace Weaver

### [Debugging simulations](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_debugging.html)

You can use the following methods to get information about your simulations.

- [Debugging local simulations](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_debugging_local.html): Learn how to debug your SimSpace Weaver Local simulations.

### [Custom containers](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_custom-containers.html)

Learn how to use a custom container to run your AWS SimSpace Weaver simulations.

- [Create a custom container](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_custom-containers_create.html): These instructions assume that you know how to use Docker and Amazon Elastic Container Registry (Amazon ECR).
- [Modify a project to use a custom container](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_custom-containers_modify-project.html): These instructions assume that you already know how to use AWS SimSpace Weaver and want to make your app storage and development workflows in the AWS Cloud more efficient.
- [FAQ](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_custom-containers_faq.html)

### [Troubleshooting](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_custom-containers_troubleshooting.html)

- [AccessDeniedException](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_custom-containers_troubleshooting_access-denied.html): If you get an AccessDeniedException error when you try to upload your container image to Amazon ECR, your IAM identity (user or role) might not have the necessary permissions to use Amazon ECR.
- [Failed simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_custom-containers_troubleshooting_no-start.html)

### [Working with Python](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_python.html)

Learn how to start working with Python for your spatial apps in AWS SimSpace Weaver.

- [Creating a Python project](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_python_create-project.html)
- [Starting a Python simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_python_start-sim.html): You can start your Python-based simulation the same way as a regular SimSpace Weaver simulation, both in SimSpace Weaver Local and in SimSpace Weaver in the AWS Cloud.
- [The sample Python client](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_python_client.html): If you use the PythonBubblesSample template to create a project then your project contains a Python sample client.
- [FAQ](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_python_faq.html)

### [Troubleshooting](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_python_troubleshooting.html)

- [Failure during custom container creation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_python_troubleshooting_create-container-failure.html): If you get an error no basic auth credentials after you run quick-start.py then there could be a problem with your temporary credentials for Amazon ECR.
- [Your Python simulation fails to start](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_python_troubleshooting_no-start.html): You might see an Unable to start app error in your simulation's management log.
- [Python ModuleNotFound error](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_python_troubleshooting_module-not-found.html): Python throws a ModuleNotFound error when it can't locate a required Python package.
- [Support for other engines](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_engines.html): You can use your own custom C++ engine with SimSpace Weaver.
- [Use of licensed software](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_byol.html): AWS SimSpace Weaver allows you to build simulations with your choice of simulation engine and content.

### [Managing resources with CloudFormation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_cloudformation.html)

You can use AWS CloudFormation to manage your AWS SimSpace Weaver resources.

- [Snapshots](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_cloudformation_snapshots.html): A snapshot is a backup of a simulation.

### [Snapshots](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots.html)

You can create a snapshot to back up your simulation entity data at any point in time.

- [SimSpace Weaver Console](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots_console.html): You can use the SimSpace Weaver console to create a snapshot of your simulation.
- [AWS CLI](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots_cli.html): You can use the AWS CLI to call the SimSpace Weaver APIs from a command prompt.
- [FAQ](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots_faq.html)

### [Messaging](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_messaging.html)

The messaging API simplifies application to application communication within the simulation.

- [Using the messaging APIs](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_messaging_using.html): The messaging APIs are contained within the SimSpace Weaver app SDK (minimum version 1.16.0).
- [When to use messaging](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_messaging_when-to-use.html): Messaging in SimSpace Weaver offers another pattern for exchanging information between simulation applications.
- [Tips when working with messaging](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_messaging_tips.html)
- [Messaging errors and troubleshooting](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_messaging_troubleshooting.html): You might experience the following errors when you use the messaging APIs.


## [Security](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security_data-protection.html): Learn how the AWS shared responsibility model applies to data protection in SimSpace Weaver.

### [Identity and Access Management](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your SimSpace Weaver resources.

- [How AWS SimSpace Weaver works with IAM](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to SimSpace Weaver, learn what IAM features are available to use with SimSpace Weaver.
- [Identity-based policy examples](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify SimSpace Weaver resources.
- [Permissions that SimSpace Weaver creates for you](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security_iam_service-created-permissions.html): When you create a SimSpace Weaver project, the service will create an AWS Identity and Access Management (IAM) role with the name weaver-project-name-app-role and an IAM trust policy.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can trick a more-privileged entity to perform the action.
- [Troubleshooting](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with SimSpace Weaver and IAM.
- [Security event logging and monitoring](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security_event-logging-and-monitoring.html): Learn how you can enhance your security in SimSpace Weaver using logging and monitoring.
- [Compliance Validation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS SimSpace Weaver features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/infrastructure-security.html): Learn how AWS SimSpace Weaver isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security_vulnerability-analysis.html): Configuration and vulnerability analysis in SimSpace Weaver
- [Security best practices](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security_best-practices.html): Security best practices for SimSpace Weaver


## [Logging and monitoring](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/logging-and-monitoring.html)

- [Logs in CloudWatch](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/cloudwatch-logs.html)
- [Monitoring with CloudWatch](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/monitoring-with-cloudwatch.html): You can monitor SimSpace Weaver using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [CloudTrail logs](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/logging-using-cloudtrail.html): Learn about logging SimSpace Weaver with AWS CloudTrail.


## [Troubleshooting](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/troubleshooting.html)

- [AssumeRoleAccessDenied](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/troubleshooting_assume-role-denied.html): You might receive the following error if your simulation fails to start:
- [InvalidBucketName](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/troubleshooting_bucket-name-too-long.html): You might receive the following error while creating a project:
- [ServiceQuotaExceededException](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/troubleshooting_quota-exceeded.html): You might receive the following error when you start a simulation:
- [TooManyBuckets](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/troubleshooting_too-many-buckets.html): You might receive the following error while creating a project:
- [Permission denied during simulation start](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/troubleshooting_permission-denied-during-sim-launch.html): When you start a simulation, you might get an error message indicating that permission was denied or that there was an error accessing your app artifacts.
- [Problems related to time when using Docker](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/troubleshooting_docker-time-problems.html): If you are using Docker and you receive time-related errors while running scripts from the SimSpace Weaver app SDK, the cause could be that your Docker virtual machine clock is incorrect.
- [Console client fails to connect](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/troubleshooting_console-client-connect-error.html): You might get the following error from the console client when you connect to the PathfindingSample simulation described in the tutorials in .
- [No simspaceweaver in the AWS CLI](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/troubleshooting_old-cli.html): If the AWS CLI gives you errors that suggest that it doesn't know about SimSpace Weaver, run the following command.


## [Schema reference](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference.html)

- [Example of a complete schema](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_example.html): The following example shows the YAML-formatted text file that describes a SimSpace Weaver simulation.

### [Schema format](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format.html)

The following example shows the overall structure of a schema.

- [SDK version](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_sdk-version.html): The sdk_version section (required) identifies the version of the SimSpace Weaver app SDK that supports this schema.
- [Simulation properties](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_simulation-properties.html): The simulation_properties section (required) specifies various properties of your simulation.
- [Workers](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_workers.html): The workers section (required) specifies configurations for worker groups (groups of workers).
- [Clock](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_clock.html): The clock section (required) specifies the properties of the simulation clock.
- [Partitioning strategies](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_partitioning-strategies.html): The partitioning_strategies section (required) specifies the organization of partitions for a spatial domain.

### [Domains](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_domains.html)

The domains section (required) specifies the properties for each of your domains.

- [Spatial](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_domains_spatial.html): To specify the properties for a spatial domain, replace spatial-domain-name with a name of your choice.
- [Custom](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_domains_custom.html): To specify the properties for a custom domain, replace custom-domain-name with a name of your choice.
- [Service](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_domains_service.html): To specify the properties for a service domain, replace service-domain-name with a name of your choice.
- [Placement constraints](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference_format_placement-constraints.html): The placement_constraints section (optional) specifies which spatial domains SimSpace Weaver should place together on the same workers.


## [SimSpace Weaver versions](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/service-versions.html)

- [1.17.0](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/service-versions_1-17-0.html): This release is an overhaul of the SimSpace Weaver app SDK distributable package.
- [1.15.1](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/service-versions_1-15-1.html): This release is a required update for the Python SDK that was originally released in SimSpace Weaver version 1.15.0.
