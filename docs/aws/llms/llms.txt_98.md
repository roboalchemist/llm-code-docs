# Source: https://docs.aws.amazon.com/application-discovery/latest/userguide/llms.txt

# AWS Application Discovery Service User Guide

> The AWS Application Discovery Service streamlines the process of migrating to Amazon Web Services by helping you identify applications and application dependencies in your data center.

- [What is AWS Application Discovery Service?](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html)
- [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html)
- [Setting up](https://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html)
- [Importing data into Migration Hub](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html)
- [Using the API to query discovered items](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html)
- [AWS PrivateLink](https://docs.aws.amazon.com/application-discovery/latest/userguide/vpc-interface-endpoints.html)
- [ARN formats](https://docs.aws.amazon.com/application-discovery/latest/userguide/arn-formats.html)
- [Quotas](https://docs.aws.amazon.com/application-discovery/latest/userguide/ads_service_limits.html)
- [Troubleshooting](https://docs.aws.amazon.com/application-discovery/latest/userguide/troubleshooting.html)
- [Document History](https://docs.aws.amazon.com/application-discovery/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/application-discovery/latest/userguide/glossary.html)

## [Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html)

- [Prerequisites](https://docs.aws.amazon.com/application-discovery/latest/userguide/gen-prep-agents.html): Review the prerequisites for installing the Discovery Agent.
- [Installing Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/install.html): Learn how to install the Discovery Agent.
- [Managing the Discovery Agent process](https://docs.aws.amazon.com/application-discovery/latest/userguide/managing.html): This page covers how to manage the Discovery Agent on Linux and Microsoft Windows.
- [Uninstalling Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/uninstall.html): This page covers how to uninstall the Discovery Agent on Linux and Microsoft Windows.
- [Starting and stopping data collection](https://docs.aws.amazon.com/application-discovery/latest/userguide/start-agent-data-collection.html): Learn how to start and stop Discovery Agent data collection.
- [Troubleshooting Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/troubleshooting_da.html): This page covers troubleshooting the Discovery Agent on Linux and Microsoft Windows.


## [Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector.html)

- [Prerequisites](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-prerequisites.html): The prerequisites for using Application Discovery Service Agentless Collector.
- [Deploying a collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-deploying.html): How to deploy for Application Discovery Service Agentless Collector.
- [Accessing the collector console](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-access-console.html): How to access the Application Discovery Service Agentless Collector console.
- [Configuring the collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-configure.html): How to configure Agentless Collector.

### [Using the Network Data Collection module](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-network-data-collection.html)

Learn how to set up and use the Agentless Collector network data collection module.

- [Setting up the Network Data Collection module](https://docs.aws.amazon.com/application-discovery/latest/userguide/network-data-module-setup.html): The Network Data Collection module collects network data for the server inventory that comes from the VMware vCenter module.
- [Network data collection attempts](https://docs.aws.amazon.com/application-discovery/latest/userguide/collection-attempts.html): When a new server is discovered, the collector attempts each configured credential for each IP address.
- [Server status in the Network Data Collection module](https://docs.aws.amazon.com/application-discovery/latest/userguide/network-data-collection-status.html): The following table explains the collection status values.

### [Using the VMware data collection module](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-data-collection-vcenter.html)

Contains topics about the VMware vCenter Agentless Collector data collection module.

- [Setting up vCenter data collection](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-vcenter.html): Learn how to set up the data collection module.
- [Viewing VMware data collection details](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-vcenter-details.html): Learn how to view VMware data collection details.
- [Controlling data collection scope](https://docs.aws.amazon.com/application-discovery/latest/userguide/control-data-collection-scope.html): Learn how to control the scope of vCenter data collection.
- [Data collected by the VMware module](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-data-collected-vmware.html): Describes details about the data that's collected by the Application Discovery Service Agentless Collector VMware vCenter data collection module.

### [Using the database and analytics data collection module](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-database-analytics-collection.html)

Describes how to set up, configure, and use the database and analytics data collection module.

- [Creating the AWS DMS data collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-database-analytics-collection-resources.html): Describes how to create the AWS DMS data collector for the database and analytics data collection module.
- [Configuring data forwarding](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-database-analytics-collection-prerequisites.html): Describes how to configure data forwarding from the database and analytics data collection module to your AWS DMS collector.
- [Adding your LDAP and OS servers](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-database-analytics-collection-add-servers.html): Describes how to add your LDAP and OS database servers with the database and analytics data collection module.

### [Discovering your databases](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-database-analytics-collection-discovery.html)

Describes how to discover your database servers with the database and analytics data collection module.

- [Configuring set up](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-database-analytics-collection-discovery-setup.html): To discover the databases running on the previously added OS Servers, the data collection module requires access to the operating system and database servers.
- [Discovering a database server](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-database-analytics-collection-discovery-tutorial.html): Complete the following set of tasks to discover and add database servers on the console.
- [Data collected by the database and analytics module](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-data-collected-database-analytics.html): Describes details about the data that the Application Discovery Service Agentless Collector database and analytics data collection module collects from the data environment.
- [Viewing collected data](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-view-collected-data.html): How to view data that's collected by Application Discovery Service Agentless Collector.

### [Accessing the Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-using.html)

Describes how to use the Application Discovery Service Agentless Collector (Agentless Collector).

- [Collector dashboard](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-dashboard.html): On the Application Discovery Service Agentless Collector (Agentless Collector) dashboard page you can see the status of the collector and choose a method of data collection as described in the following topics.
- [Editing collector settings](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-edit-configure.html): You configured the collector when you first set up Application Discovery Service Agentless Collector (Agentless Collector) as described in .
- [Editing vCenter credentials](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-vcenter-edit.html): To collect server inventory, profile, and utilization data from your VMware VMs, set up connections to your vCenter servers.
- [Updating Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-update.html): How to manually update the Application Discovery Service Agentless Collector.
- [Troubleshooting](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-troubleshooting.html): How to troubleshoot Application Discovery Service Agentless Collector.


## [View and explore data](https://docs.aws.amazon.com/application-discovery/latest/userguide/view-and-explore.html)

- [View collected data](https://docs.aws.amazon.com/application-discovery/latest/userguide/view-data.html): How to view data that's collected by AWS Application Discovery Service using the AWS Migration Hub console.

### [Exploring data in Athena](https://docs.aws.amazon.com/application-discovery/latest/userguide/explore-data.html)

Explore data discovered by AWS Application Discovery Service in Amazon Athena.

- [Turning on data exploration](https://docs.aws.amazon.com/application-discovery/latest/userguide/ce-prep-agents.html): Learn how to turn on data exploration in Amazon Athena.
- [Exploring data](https://docs.aws.amazon.com/application-discovery/latest/userguide/explore-direct-in-ate.html): How to work with discovered data in Amazon Athena.
- [Visualizing data](https://docs.aws.amazon.com/application-discovery/latest/userguide/port-query-to-visualization.html): How to visualize discovered data in Amazon Athena.
- [Using predefined queries](https://docs.aws.amazon.com/application-discovery/latest/userguide/predefined-queries.html): How to use predefined queries in Amazon Athena.


## [Discovering data with the Migration Hub console](https://docs.aws.amazon.com/application-discovery/latest/userguide/console-walkthrough.html)

- [Viewing data in the dashboard](https://docs.aws.amazon.com/application-discovery/latest/userguide/dashboard.html): To view the main dashboard, choose Dashboard from the AWS Migration Hub (Migration Hub) console navigation pane.
- [Starting and stopping data collectors](https://docs.aws.amazon.com/application-discovery/latest/userguide/start-stop-data_collection.html): Learn how to start and stop data collectors.
- [Sorting data collectors](https://docs.aws.amazon.com/application-discovery/latest/userguide/sort-data-collectors.html): Learn how to sort data collectors.
- [Viewing servers](https://docs.aws.amazon.com/application-discovery/latest/userguide/view-servers.html): Learn how to get a general view and a detailed view of servers.
- [Sorting servers](https://docs.aws.amazon.com/application-discovery/latest/userguide/sort-servers.html): Learn how to sort servers with search filters.
- [Tagging servers](https://docs.aws.amazon.com/application-discovery/latest/userguide/tag-servers.html): Learn how to tag servers.
- [Exporting server data](https://docs.aws.amazon.com/application-discovery/latest/userguide/export-server-data.html): Learn how to export server data.
- [Grouping servers](https://docs.aws.amazon.com/application-discovery/latest/userguide/applications.html): Learn how to group servers.


## [Security](https://docs.aws.amazon.com/application-discovery/latest/userguide/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/application-discovery/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your Application Discovery Service resources.

- [How AWS Application Discovery Service works with IAM](https://docs.aws.amazon.com/application-discovery/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Application Discovery Service, you should understand what IAM features are available to use with Application Discovery Service.
- [AWS managed policies](https://docs.aws.amazon.com/application-discovery/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Application Discovery Service and recent changes to those policies.
- [Identity-based policy examples](https://docs.aws.amazon.com/application-discovery/latest/userguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify Application Discovery Service resources.

### [Understanding and using service-linked roles](https://docs.aws.amazon.com/application-discovery/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give Application Discovery Service access to resources in your AWS account.

- [Service-linked role permissions for Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/service-linked-role-permissions.html): Application Discovery Service uses the service-linked role named AWSServiceRoleForApplicationDiscoveryServiceContinuousExport â Enables access to AWS Services and Resources used or managed by AWS Application Discovery Service.
- [Creating a service-linked role for Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/create-service-linked-role.html): You don't need to manually create a service-linked role.
- [Deleting a service-linked role for Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/delete-service-linked-role.html): If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role.
- [Troubleshooting IAM](https://docs.aws.amazon.com/application-discovery/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Application Discovery Service and IAM.
- [Logging API calls with CloudTrail](https://docs.aws.amazon.com/application-discovery/latest/userguide/logging-using-cloudtrail.html): Learn about logging Application Discovery Service with AWS CloudTrail.
