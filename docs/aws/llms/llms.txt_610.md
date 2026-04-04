# Source: https://docs.aws.amazon.com/neptune/latest/userguide/llms.txt

# Amazon Neptune User Guide

> Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets.

- [What is Neptune?](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)
- [Latest Updates](https://docs.aws.amazon.com/neptune/latest/userguide/doc-history.html)
- [Neptune Limits](https://docs.aws.amazon.com/neptune/latest/userguide/limits.html)
- [Neptune integrations](https://docs.aws.amazon.com/neptune/latest/userguide/integrations.html)
- [Using Neptune APIs](https://docs.aws.amazon.com/neptune/latest/userguide/using-neptune-apis.html)

## [Getting started with Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/graph-get-started.html)

- [Using Neptune with graph notebooks](https://docs.aws.amazon.com/neptune/latest/userguide/graph-notebooks.html): This section of the Amazon Neptune User Guide shows you how to use graph notebooks, such as Jupyter Notebooks, to interact with your Amazon Neptune graph database and visualize your data.
- [Neptune graph notebooks magics](https://docs.aws.amazon.com/neptune/latest/userguide/notebooks-magics.html): This section of the Amazon Neptune user guide explains how to use "magics" in your Amazon Neptune graph notebooks to simplify the process of querying your Neptune database using SPARQL or Gremlin.
- [Graph data visualization](https://docs.aws.amazon.com/neptune/latest/userguide/notebooks-visualization.html): This section of the Amazon Neptune user guide explores how to leverage data visualization capabilities within your Neptune graph notebooks.


## [Neptune setup](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-setup.html)

- [DB instance types](https://docs.aws.amazon.com/neptune/latest/userguide/instance-types.html): This section of the Amazon Neptune user guide shows you how to choose the right instance types for your Neptune workloads.
- [Storage types](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html): This section of the Amazon Neptune user guide shows you how to choose the appropriate storage types for your Neptune cluster.

### [Create Neptune cluster](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-create-cluster.html)

This section of the Amazon Neptune user guide shows you how to create a new Neptune cluster, including configuring the required VPC settings and specifying the cluster parameters.

- [Prerequisites](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-prereqs.html): This section of the Amazon Neptune user guide covers the prerequisites for getting started with the service using AWS CloudFormation.
- [Create a cluster](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-cfn-create.html): This section of the Amazon Neptune user guide shows you how to use AWS CloudFormation to create a new Neptune cluster.
- [Configure the VPC](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-vpc.html): An Amazon Neptune DB cluster can only be created in an Amazon Virtual Private Cloud (Amazon VPC).

### [Connect to a cluster](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-connecting.html)

This section of the Amazon Neptune user guide provides guidance on connecting to your Neptune cluster.

- [In the VPC](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-connect-ec2-same-vpc.html): This section of the Amazon Neptune user guide shows you how to connect an Amazon EC2 instance to a Neptune cluster when both are located within the same Virtual Private Cloud (VPC).
- [From a different VPC](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-connect-ec2-other-vpc.html): This section of the Amazon Neptune user guide shows you how to connect an Amazon EC2 instance to a Neptune cluster when they are located in different Virtual Private Clouds (VPCs).
- [Over a private network](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-connect-private-net.html): This section of the Amazon Neptune user guide provides guidance on connecting to your Neptune cluster over a private network, such as an AWS Direct Connect or VPN connection.
- [Public Endpoints](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-public-endpoints.html): Connect to your Neptune database from outside your Amazon VPC using public endpoints.
- [Securing access to Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-security.html): This section of the Amazon Neptune user guide covers the security measures you can implement to protect your Neptune cluster.

### [Accessing graph data](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-access-graph.html)

This section of the Amazon Neptune user guide shows you how to access and query the graph data stored in your Neptune cluster.

- [Using Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-graph-gremlin.html): This section of the Amazon Neptune user guide shows you how to use the Gremlin query language to access and traverse the graph data stored in your Neptune cluster.
- [Using openCypher](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-graph-opencypher.html): This section of the Amazon Neptune user guide demonstrates how to use the OpenCypher query language to access and interact with the graph data stored in your Neptune cluster.
- [Using SPARQL](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-graph-sparql.html): This section of the Amazon Neptune user guide shows you how to use the SPARQL query language to access and interact with the graph data stored in your Neptune cluster.
- [Loading data](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-loading.html): This section of the Amazon Neptune user guide covers the process of loading data into your Neptune cluster.
- [Monitoring Neptune cluster](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-monitoring.html): This section of the Amazon Neptune user guide shows you how to monitor your Neptune cluster.
- [Troubleshooting Neptune cluster](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-troubleshooting.html): This section of the Amazon Neptune user guide provides guidance on troubleshooting issues that may arise with your Neptune cluster.


## [Neptune Serverless](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless.html)

- [Capacity scaling](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-capacity-scaling.html): Setting up a Neptune Serverless DB cluster is similar to setting up a normal provisioned cluster, with additional configuration for minimum and maximum units for scaling, and with the instance type set to db.serverless.
- [Additional configuration](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-configuration.html): In addition to setting minimum and maximum capacity for your Neptune Serverless DB cluster, there are a few other configuration choices to consider.
- [Using Serverless](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html): You can create a new Neptune DB cluster as a serverless one, or in some cases you can convert an existing DB cluster to use serverless.


## [Neptune global databases](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-global-database.html)

- [Setting up a global database](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-setup.html): This section of the Amazon Neptune user guide provides detailed guidance on setting up a global database for your Neptune cluster.

### [Managing a global database](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-managing.html)

This section of the Amazon Neptune user guide covers the management of a Neptune global database.

- [Removing a cluster](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-detaching.html): There are several reasons you might want to remove a DB cluster from a global database.
- [Deleting a global database](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-deleting.html): You can't delete a global database and its associated clusters in a single step.
- [Modifying a global database](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-modifying.html): The DB cluster parameter groups can be configured independently for each Neptune DB cluster in a global database, but it's best to keep settings consistent across the clusters to avoid unexpected behavior changes if a secondary cluster has to be promoted to primary.
- [Disaster recovery in Neptune database](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-disaster-recovery.html): This section of the Amazon Neptune user guide shows you how to perform disaster recovery, including how to back up and restore your data, set up replication, and recover your database in the event of a disaster.
- [Monitoring Neptune deployments](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-monitoring.html): This section of the Amazon Neptune user guide shows you how to monitor your Neptune deployment, including how to use Amazon CloudWatch to view metrics, set alarms, and analyze logs.


## [Neptune overview](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview.html)

### [Standards Compliance](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-standards-compliance.html)

Amazon Neptune complies with applicable standards in implementing the Gremlin and SPARQL graph query languages in most cases.

- [Gremlin standards compliance](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-differences.html): Overview of differences between the Neptune and TinkerPop implementations of Gremlin.
- [SPARQL standards compliance](https://docs.aws.amazon.com/neptune/latest/userguide/feature-sparql-compliance.html): Overview of Neptune compliance with SPARQL graph query language standards.
- [openCypher specification compliance](https://docs.aws.amazon.com/neptune/latest/userguide/feature-opencypher-compliance.html): Overview of Neptune compliance with openCypher graph query language specification.

### [Graph Data Model](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-data-model.html)

Learn about the four positions of a Neptune quad element.

- [The dictionary](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-storage-dictionary.html): Neptune does not store most user-facing values directly in the various indexes it maintains.
- [Indexing Strategy](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-storage-indexing.html): How Neptune uses indexing.

### [Lookup cache](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-lookup-cache.html)

Amazon Neptune implements a lookup cache that uses the R5d instance's NVMe-based SSD to improve read performance for queries with frequent, repetitive lookups of property values or RDF literals.

- [Use cases for the lookup cache](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-lookup-cache-when-to-use.html): The lookup cache only helps when your read queries are returning the properties of a very large number of vertices and edges, or of RDF triples.
- [Using the cache](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-lookup-cache-using.html): The lookup cache is only available on an R5d instance type, where it is automatically enabled by default.

### [Transaction Semantics](https://docs.aws.amazon.com/neptune/latest/userguide/transactions.html)

How Neptune handles transactions and isolation levels.

- [Isolation Levels](https://docs.aws.amazon.com/neptune/latest/userguide/transactions-isolation-levels.html): Describes isolation levels as defined in the SQL:92 standard.
- [Neptune Isolation Levels](https://docs.aws.amazon.com/neptune/latest/userguide/transactions-neptune.html): Neptune implements different transaction isolation levels for read-only and mutation queries.
- [Transaction examples](https://docs.aws.amazon.com/neptune/latest/userguide/transactions-examples.html): Examples of transaction isolation levels in Neptune.
- [Clusters and Instances](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-db-clusters.html): Learn about DB clusters and Instances on Neptune.
- [Storage, reliability and availability](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-storage.html): Amazon Neptune uses a distributed and shared storage architecture that scales automatically as your database storage needs grow.

### [Endpoint Connections](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-endpoints.html)

Amazon Neptune uses a cluster of DB instances rather than a single instance.

- [Working with custom endpoints](https://docs.aws.amazon.com/neptune/latest/userguide/feature-custom-endpoint-membership.html): When you add a DB instance to a custom endpoint or remove it from a custom endpoint, any existing connections to that DB instance remain active.
- [Lab Mode](https://docs.aws.amazon.com/neptune/latest/userguide/features-lab-mode.html): Use Neptune lab mode to enable new features that are present in the current release.

### [Neptune DFE engine](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-engine.html)

Amazon Neptune has a fast and efficient new engine.

- [Controlling DFE use](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-enabling-disabling.html): By default, the instance parameter of an instance is set to viaQueryHint, which causes the DFE engine to be used only for openCypher queries and for Gremlin and SPARQL queries that explicitly include the useDFE query hint set to true.
- [Queries executed by the DFE](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-suppoorts-subset.html): Currently, the Neptune DFE supports a subset of SPARQL and Gremlin query constructs.
- [DFE statistics](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-statistics.html)
- [Graph summary API](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-graph-summary.html): The Neptune graph summary API retrieves the following information about your graph:

### [JDBC connectivity](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-jdbc.html)

Amazon Neptune has released an open-source JDBC driver that supports openCypher, Gremlin, SQL-Gremlin, and SPARQL queries.

- [Getting started](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-jdbc-getting-started.html): To use the Neptune JDBC driver to connect to a Neptune instance, either the JDBC driver must be deployed on an Amazon EC2 instance in the same VPC as your Neptune DB cluster, or the instance must be available through an SSH tunnel or load balancer.
- [Using Tableau](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-jdbc-tableau.html): To use Tableau with the Neptune JDBC driver, start by downloading and installing the most recent version of Tableau Desktop.
- [Troubleshooting](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-jdbc-troubleshooting.html): If the driver fails to connect to the server, use the isValid function of the JDBC Connection object to check whether the connection is valid.
- [Neptune engine updates](https://docs.aws.amazon.com/neptune/latest/userguide/features-engine-updates.html): Updating the Neptune engine.
- [Exceptions and Retries](https://docs.aws.amazon.com/neptune/latest/userguide/transactions-exceptions.html): Learn how to implement effective retry strategies for Neptune applications to handle transient errors and improve reliability.


## [Security](https://docs.aws.amazon.com/neptune/latest/userguide/security.html)

- [Amazon Neptune operating system upgrades](https://docs.aws.amazon.com/neptune/latest/userguide/security-os-upgrades.html): Amazon Neptune ensures continuous improvements in database performance, security, and stability through regular OS upgrades.

### [Protecting data in Neptune databases](https://docs.aws.amazon.com/neptune/latest/userguide/data-protection.html)

This section of the Amazon Neptune user guide describes the data protection features available for your Neptune database, including backup, restore, and encryption options to help safeguard your data.

- [Securing Neptune databases with Amazon VPC](https://docs.aws.amazon.com/neptune/latest/userguide/security-vpc.html): This section of the Amazon Neptune user guide explains how to use Amazon Virtual Private Cloud (Amazon VPC) to secure your Neptune database, including how to control network access and isolate your database within a private network.
- [Encrypting connects to Neptune databases](https://docs.aws.amazon.com/neptune/latest/userguide/security-ssl.html): This section of the Amazon Neptune user guide describes how to encrypt connections to your Neptune database using Secure Sockets Layer (SSL) or Transport Layer Security (TLS) protocols, providing secure data transmission between your application and the database.
- [Encrypting data at Rest](https://docs.aws.amazon.com/neptune/latest/userguide/encrypt.html): This section of the Amazon Neptune user guide explains how to encrypt data at rest in your Neptune database using AWS Key Management Service (AWS KMS) to protect sensitive information stored in your database.
- [Authenticating with IAM](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html): This section of the Amazon Neptune user guide describes how to use AWS Identity and Access Management (IAM) to authenticate users and applications that connect to your Neptune database, providing a secure way to control access to your data.
- [Enabling IAM](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-enable.html): This section of the Amazon Neptune user guide explains how to enable IAM database authentication for your Neptune database, allowing you to use IAM credentials to authenticate and manage access to your database resources.

### [Connecting with IAM authentication](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connecting.html)

This section of the Amazon Neptune user guide provides guidance on how to connect to your Neptune database using IAM authentication, including the necessary steps and sample code for various programming languages and tools.

- [Prerequisites](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connect-prerq.html): This section of the Amazon Neptune user guide outlines the prerequisites for connecting to your Neptune database using IAM authentication, including setting up the necessary AWS resources and configuring your application to support IAM-based authentication.
- [Connecting from the command line](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connect-command-line.html): This section of the Amazon Neptune user guide provides instructions on how to connect to your Neptune database using IAM authentication from the command line, including examples for various tools and programming languages.
- [Connecting from Gremlin Console](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connecting-gremlin-console.html): This section of the Amazon Neptune user guide explains how to connect to your Neptune database using IAM authentication with the Gremlin Console with Signature Version 4 Signing.
- [Connecting using Gremlin Java](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connecting-gremlin-java.html): This section of the Amazon Neptune user guide provides instructions on how to connect to your Neptune database using IAM authentication with the Gremlin Java API with Signature Version 4 authentication.
- [Connecting with SPARQL Java](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connecting-sparql-java.html): This section of the Amazon Neptune user guide explains how to connect to your Neptune database using IAM authentication with the SPARQL Java API (RDF4J or Apache Jena) with Signature Version 4 authentication.
- [Conncting with SPARQL and Node.js](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connecting-sparql-node.html): This section of the Amazon Neptune user guide provides instructions on how to connect to your Neptune database using IAM authentication with the SPARQL Node.js API with Signature Version 4 authentication.
- [Connecting with Python](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connecting-python.html): This section of the Amazon Neptune user guide explains how to connect to your Neptune database using IAM authentication with Python using Python Signature Version 4 authentication.
- [Gremlin Python](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-python-iam-auth.html)
- [Gremlin Javascript](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-javascript-iam-auth.html)
- [Gremlin Go](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-go-iam-auth.html)
- [Gremlin .NET](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-dotnet-iam-auth.html)

### [Using IAM policies](https://docs.aws.amazon.com/neptune/latest/userguide/security-iam-access-manage.html)

This section of the Amazon Neptune user guide describes how to use AWS Identity and Access Management policies to manage and control access to your Neptune database, ensuring only authorized users and applications can interact with your graph data.

### [Using managed policies](https://docs.aws.amazon.com/neptune/latest/userguide/security-iam-access-managed-policies.html)

This section of the Amazon Neptune user guide explains how to use AWS-managed IAM policies to grant access to your Neptune database, providing a convenient way to set up permissions without having to create custom policies.

- [Granting read-only access](https://docs.aws.amazon.com/neptune/latest/userguide/read-only-access-iam-managed-policy.html): This section of the Amazon Neptune user guide describes how to grant read-only access to your Neptune graph using an AWS-managed IAM policy, allowing users to view but not modify your graph data.
- [Granting Full Access](https://docs.aws.amazon.com/neptune/latest/userguide/full-access-iam-managed-policy.html): This section of the Amazon Neptune user guide explains how to grant full access to your Neptune database using an AWS-managed IAM policy, allowing users to perform all operations on your graph data.
- [Granting full access to Neptune console](https://docs.aws.amazon.com/neptune/latest/userguide/console-full-access-iam-managed-policy.html): This section of the Amazon Neptune user guide describes how to grant full access to the Neptune console using an AWS-managed IAM policy, allowing users to perform all administrative tasks and access all features of the Neptune management console.
- [Granting read-only access to Neptune graph](https://docs.aws.amazon.com/neptune/latest/userguide/graph-read-only-access-iam-managed-policy.html): This section of the Amazon Neptune user guide explains how to grant read-only access to your Neptune graph database using an AWS-managed IAM policy, allowing users to view and query your graph data without the ability to modify it.
- [Using AWSServiceRoleForNeptuneGraphPolicy](https://docs.aws.amazon.com/neptune/latest/userguide/aws-service-role-for-neptune-graph-policy.html): This section of the Amazon Neptune user guide describes how to use the AWS Service Role for Neptune to grant access to your graph, allowing other AWS services to interact with your Neptune graph on your behalf.
- [Using condition Keys](https://docs.aws.amazon.com/neptune/latest/userguide/iam-condition-keys.html): This section of the Amazon Neptune user guide explains how to use IAM condition keys to customize and fine-tune access to your Neptune database, allowing you to create more granular and specific IAM policies.

### [IAM administrative policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-admin-policies.html)

This section of the Amazon Neptune user guide provides guidance on how to create custom IAM policies to manage and administer your Neptune graph, including examples of policies for common administrative tasks.

- [Administrative actions](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-iam-admin-actions.html): This section of the Amazon Neptune user guide provides a reference of the IAM actions that can be used to grant permissions for administering your Neptune database, including actions for managing instances, clusters, and other resources.
- [Resources types](https://docs.aws.amazon.com/neptune/latest/userguide/iam-admin-resources.html): This section of the Amazon Neptune user guide lists the IAM resource types that can be used to grant permissions for administering your Neptune database, including Neptune-specific resources and general AWS resources.
- [Condition Keys](https://docs.aws.amazon.com/neptune/latest/userguide/iam-admin-condition-keys.html): This section of the Amazon Neptune user guide describes the IAM condition keys that can be used to create more granular and specific policies for administering your Neptune database, allowing you to control access based on various conditions and context.
- [Administrative policy examples](https://docs.aws.amazon.com/neptune/latest/userguide/iam-admin-policy-examples.html): This section of the Amazon Neptune user guide provides example IAM adminstrative policies that you can use as a starting point for administering your Neptune database, including policies for common administrative tasks such as managing instances, clusters, and backups.

### [Custom data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-access-policies.html)

This section of the Amazon Neptune user guide explains how to create custom IAM policies to control access to the data stored in your Neptune database, allowing you to grant fine-grained permissions for different users and applications.

- [Data access actions](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html): This section of the Amazon Neptune user guide provides a reference of the IAM actions that can be used to grant permissions for data in your Neptune database, including actions for managing backups, restores, and other data protection features.
- [Data acccess resources](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-resources.html): This section of the Amazon Neptune user guide lists the IAM resource types that can be used to grant permissions for accessing the data stored in your Neptune database, including Neptune-specific resources and general AWS resources.
- [Condition Keys](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html): This section of the Amazon Neptune user guide describes the IAM condition keys that can be used to create more granular and specific policies for controlling access to the data in your Neptune database, allowing you to enforce additional constraints and conditions.
- [Data-access policy examples](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-access-examples.html): This section of the Amazon Amazon Neptune user guide provides example IAM data-access policies that you can use as a starting point for controlling access to the data stored in your Neptune database, including policies for common data access scenarios.
- [Service-Linked Roles](https://docs.aws.amazon.com/neptune/latest/userguide/security-iam-service-linked-roles.html): This section of the Amazon Neptune user guide explains how to use service-linked roles for Neptune to manage permissions and access to your database, allowing other AWS services to interact with Neptune resources.
- [Temporary credentials](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-temporary-credentials.html): This section of the Amazon Neptune user guide explains how to use temporary credentials, such as those provided by AWS Security Token Service, to connect to your Neptune database, allowing you to grant limited-time access to users or applications.
- [Logging and Monitoring](https://docs.aws.amazon.com/neptune/latest/userguide/security-monitoring.html): This section of the Amazon Amazon Neptune user provides resources that monitor the usage and performance of Neptune clusters and log the data.
- [Compliance considerations](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-compliance.html): This section of the Amazon Neptune user guide discusses compliance considerations for your Neptune database, including information about security and compliance regulations, auditing, and other factors to keep in mind when using Neptune in regulated environments.
- [Building resilient deployments](https://docs.aws.amazon.com/neptune/latest/userguide/disaster-recovery-resiliency.html): This section of the Amazon Neptune user guide provides guidance on how to build resilient and disaster-tolerant Neptune deployments, including strategies for ensuring high availability, data durability, and business continuity in the face of failures or disruptions.


## [Migrating to Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/migrating.html)

### [Migrating from Neo4j](https://docs.aws.amazon.com/neptune/latest/userguide/migrating-from-neo4j.html)

Overview of how to migrate an existing graph from Neo4j into Neptune.

- [General information](https://docs.aws.amazon.com/neptune/latest/userguide/migrating-from-neo4j-general.html): With Neptune support for the openCypher query language, you can move most Neo4j workloads that use the Bolt protocol or HTTPS to Neptune.

### [Preparing for migration](https://docs.aws.amazon.com/neptune/latest/userguide/preparing-to-migrate-from-neo4j.html)

Migrating from the Neo4j graph database to the Neptune graph database service can be approached in one of two main ways: re-platforming or refactoring/re-architecting.

- [Architectural differences](https://docs.aws.amazon.com/neptune/latest/userguide/migration-architectural-differences.html): When customers first consider migrating an application from Neo4j to Neptune, it is often tempting to perform a like-to-like comparison based on instance size.
- [Data storage differences](https://docs.aws.amazon.com/neptune/latest/userguide/migration-storage-differences.html): Neptune uses a graph data model based on a native quad model.
- [Operational differences](https://docs.aws.amazon.com/neptune/latest/userguide/migration-operational-differences.html): Neptune is a fully managed service that automates many of the normal operational tasks you would have to do when using on-premise or self-managed databases such as Neo4j Enterprise or Community Edition:
- [Provisioning infrastructure](https://docs.aws.amazon.com/neptune/latest/userguide/migration-provisioning-infrastructure.html): Amazon Neptune clusters are built to scale in three dimensions: storage, write capacity, and read capacity.
- [Data migration](https://docs.aws.amazon.com/neptune/latest/userguide/migration-data-migration.html): When performing a migration from Neo4j to Amazon Neptune, migrating the data is a major step in the process.
- [Application migration](https://docs.aws.amazon.com/neptune/latest/userguide/migration-app-migration.html): After you have migrated your data from Neo4j to Neptune, the next step is to migrate the application itself.
- [Neptune compatibility](https://docs.aws.amazon.com/neptune/latest/userguide/migration-compatibility.html): Neo4j's has an all-in-one architectural approach, where data loading, data ETL, application queries, data storage, and management operations all occur in the same set of compute resources, such as EC2 instances.
- [Cypher rewrites](https://docs.aws.amazon.com/neptune/latest/userguide/migration-opencypher-rewrites.html): The openCypher language is a declarative query language for property graphs that was originally developed by Neo4j, then open-sourced in 2015, and contributed to the openCypher project under an Apache 2 open-source license.
- [Migration resources](https://docs.aws.amazon.com/neptune/latest/userguide/migration-resources.html): Neptune provides several tools and resources that can assist in the migration process.
- [Migrating from TinkerPop](https://docs.aws.amazon.com/neptune/latest/userguide/migrating-from-tinkerpop.html): Overview of how to migrate from an Apache TinkerPop Gremlin server to Neptune.
- [Migrating from RDF](https://docs.aws.amazon.com/neptune/latest/userguide/migrating-from-rdf.html): Overview of how to migrate from an RDF triple store to Neptune.
- [Using AWS DMS to migrate](https://docs.aws.amazon.com/neptune/latest/userguide/migrating-using-dms.html): Overview of using AWS DMS to migrate existing graph data into Neptune.
- [Migrating from Blazegraph](https://docs.aws.amazon.com/neptune/latest/userguide/migrating-from-blazegraph.html): Overview of how to migrate from Blazegraph to Neptune.


## [Loading data](https://docs.aws.amazon.com/neptune/latest/userguide/load-data.html)

### [Neptune Bulk Loader](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html)

Overview of how to load data from external files into a Neptune DB instance using the Neptune bulk loader.

### [IAM Role and Amazon S3 Access](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM.html)

Prerequisites for loading data from an S3 bucket into Neptune.

- [Creating an IAM role to access Amazon S3](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM-CreateRole.html): Use the AmazonS3ReadOnlyAccess managed IAM policy to create a new IAM role that will allow Amazon Neptune access to Amazon S3 resources.
- [Adding the IAM Role to a Cluster](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM-add-role-cluster.html): Use the console to add the IAM role to an Amazon Neptune cluster.
- [Creating the VPC Endpoint](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-vpc.html): The Neptune loader requires a VPC endpoint of type Gateway for Amazon S3.
- [Chaining IAM roles](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-chain-roles.html)

### [Data Formats](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format.html)

List of data formats that are available for the Neptune Load API.

- [Gremlin data format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html): Requirements for loading Gremlin data into Neptune.
- [openCypher data format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html): Requirements for loading RDF data into Neptune.
- [RDF data formats](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-rdf.html): Requirements for loading RDF data into Neptune.
- [Loading Example](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-data.html): Example of loading data into Amazon Neptune.
- [Optimizing a bulk load](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-optimize.html): Use the following strategies to keep the load time to a minimum for a Neptune bulk load:

### [Loader Reference](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference.html)

Loader APIs for Amazon Neptune that are available from the HTTP endpoint of a Neptune DB instance.

### [Loader Command](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-load.html)

Loads data from an Amazon S3 bucket into a Neptune DB instance.

- [Errors](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-load-errors.html): When an error occurs, a JSON object is returned in the BODY of the response.
- [Examples](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-load-examples.html): This example demonstrates how to use the Neptune loader to load data into a Neptune graph database using the Gremlin CSV format.

### [Get-Status API](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-status.html)

Gets the status of a loader job.

- [Requests](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-status-requests.html)
- [Responses](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-status-response.html): The following example response from the Neptune Get-Status API describes the overall structure of the response, explains the various fields and their data types, as well as the error handling and error log details.
- [Examples](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-status-examples.html): The following examples showcase the usage of the Neptune loader's GET-Status API, which allows you to retrieve information about the status of your data loads into the Amazon Neptune graph database.
- [errorLogs examples](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-error-logs-examples.html): The following examples showcase the detailed status response from the Neptune loader when errors have occurred during the data loading process.
- [Cancel Job](https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-cancel.html): Cancels a load job.

### [Load data using DMS](https://docs.aws.amazon.com/neptune/latest/userguide/dms-neptune.html)

Overview of how to use AWS Database Migration Service (AWS DMS) to load data into Neptune.

- [GraphMappingConfig](https://docs.aws.amazon.com/neptune/latest/userguide/dms-neptune-graph-mapping.html): The GraphMappingConfig that you create specifies how data extracted from a source data store should be loaded into a Neptune DB cluster.
- [Replicating to Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/dms-neptune-replication.html): Once you have created your table mapping and graph mapping configurations, use the following process to load data from the source store into Neptune.
- [Load data using queries](https://docs.aws.amazon.com/neptune/latest/userguide/load-data-via-query.html): Overview of how to load data from external files into a Neptune DB instance using Neptune's supported query languages.


## [Storage](https://docs.aws.amazon.com/neptune/latest/userguide/storage.html)

- [Dictionary garbage collection](https://docs.aws.amazon.com/neptune/latest/userguide/storage-gc.html): Neptune supports dictionary garbage collection (GC) which can be enabled via the neptune_lab_mode parameter for property graph data.
- [Inlined server-generated edge ID](https://docs.aws.amazon.com/neptune/latest/userguide/storage-edge-id.html): Neptune supports inline Server-Generated Edge IDs.


## [Querying](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-queries.html)

- [Query queuing](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-queuing.html): How queries are queued in Neptune and how queuing can affect performance.
- [Query plan cache](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-qpc.html): How Amazon Neptune utilizes the query plan cache to reduce the overall latency and avoid parsing and optimization for repeated patterns.
- [Custom queryId](https://docs.aws.amazon.com/neptune/latest/userguide/features-query-id.html): You can inject your own custom queryId into a Gremlin or SPARQL query.

### [Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin.html)

Set up your environment to use Gremlin to access a Neptune graph.

### [Installing the Gremlin console](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-console.html)

Steps for connecting to Neptune using the Gremlin Console.

- [Another way to connect](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-console-connect.html): Drawbacks of the normal connection approach

### [HTTPS REST](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-rest.html)

Steps for connecting to Neptune using the HTTPS REST Endpoint.

- [Enable multi-part responses](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-rest-trailing-headers.html): By default, the HTTP response to Gremlin queries is returned in a single JSON result set.

### [Java](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-client.html)

You can use either of two open-source Java-based Gremlin clients with Amazon Neptune: the Apache TinkerPop Java Gremlin client, or the Gremlin client for Amazon Neptune.

- [Using a Java client](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-java.html): Steps for connecting to Neptune using Java
- [Java reconnect sample](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-java-reconnect-example.html): Steps for connecting to Neptune using Java with reconnect logic
- [Python](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-python.html): Steps for connecting to Neptune using Python.
- [.NET](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-dotnet.html): Steps for connecting to Neptune using .NET.
- [Node.js](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-node-js.html): Steps for connecting to Neptune using Node.js.
- [Go](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-go.html): Steps for connecting to Neptune using the Go language.

### [Query hints](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-query-hints.html)

You can use query hints to specify optimization and evaluation strategies for a particular Gremlin query in Amazon Neptune.

- [repeatMode](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-query-hints-repeatMode.html): The Neptune repeatMode query hint specifies how the Neptune engine evaluates the repeat() step in a Gremlin traversal: breadth first, depth first, or chunked depth first.
- [noReordering](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-query-hints-noReordering.html): When you submit a Gremlin traversal, the Neptune query engine investigates the structure of the traversal and reorders parts of the query, trying to minimize the amount of work required for evaluation and query response time.
- [typePromotion](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-query-hints-typePromotion.html): When you submit a Gremlin traversal that filters on a numerical value or range, the Neptune query engine must normally use type promotion when it executes the query.
- [useDFE](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-query-hints-useDFE.html): Use this query hint to enable use of the DFE for executing the query.
- [Results cache query hints](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-query-hints-results-cache.html): The following query hints can be used when the query results cache is enabled.
- [Query status](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status.html): Information about using the Gremlin query status HTTP API in Neptune.
- [Query cancellation](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status-cancel.html): Information about using the Gremlin query cancellation HTTP API in Neptune.
- [Gremlin script-based sessions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-sessions.html): How to use Gremlin script-based sessions with implicit transactions in Neptune.
- [Gremlin transactions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-transactions.html): How to use Gremlin transactions in Neptune.
- [Using the Gremlin API](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-reference.html): Overview of using Gremlin HTTP(S) API with Neptune.
- [Caching query results](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-results-cache.html): Overview of using the query results cache with Gremlin.
- [Efficient upserts from 3.6.x forward](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-efficient-upserts.html): How to optimize upserts in Gremlin using mergeV() and mergeE().
- [Efficient upserts before 3.6.x](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-efficient-upserts-pre-3.6.html): How to optimize upserts in Gremlin.

### [Gremlin explain](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-explain.html)

Use the Gremlin explain feature in Neptune to understand and improve your query execution.

### [Background information](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-explain-background.html)

Understand how to use the Neptune Gremlin explain/profile feature.

- [Statements](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-explain-background-statements.html): Gremlin uses statements to represent data in Neptune.
- [Statement Indexes](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-explain-background-indexing-examples.html): Gremlin uses statement indexes to process queries in Neptune.
- [Query processing](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-explain-background-querying.html): How Gremlin processes queries in Neptune.
- [Gremlin explain API](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-explain-api.html): How to use the Gremlin explain API in Neptune.
- [Gremlin profile API](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html): The Gremlin profile feature in Neptune runs a specified traversal, collects metrics about the run, and produces a profile report.
- [Tuning Gremlin queries](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-traversal-tuning.html): Learn how to tune Gremlin queries in Neptune.
- [Gremlin step support](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-step-support.html): The Amazon Neptune engine does not currently have full native support for all Gremlin steps, as explained in .

### [Gremlin and DFE](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-with-dfe.html)

If you enable Neptunes alternative query engine known as the DFE in lab mode (by setting the neptune_lab_mode DB cluster parameter to DFEQueryEngine=enabled), then Neptune translates read-only Gremlin queries/traversals into an intermediate logical representation and runs them on the DFE engine whenever possible.

- [Gremlin step coverage in DFE](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-step-coverage-in-DFE.html): Gremlin DFE is a labmode feature and can be used by either enabling the cluster parameter or using the Neptune#useDFE query hint.

### [openCypher](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html)

Set up your environment to use the openCypher query language to access a Neptune graph.

- [Using openCypher](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-overview-getting-started.html): You can query property-graph data in Neptune using openCypher regardless of how it was loaded, but you can't use openCypher to query data loaded as RDF.
- [Status endpoint](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-status.html): The openCypher status endpoint provides access to information about queries that are currently running on the server or waiting to run.
- [HTTPS endpoint](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-queries.html)
- [Using the Bolt protocol](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-bolt.html): Bolt is a statement-oriented client/server protocol initially developed by Neo4j and licensed under the Creative Commons 3.0 Attribution-ShareAlike license.
- [Parameterized examples](https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-parameterized-queries.html): Neptune supports parameterized openCypher queries.
- [Data model](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-data-model.html): The Neptune openCypher engine builds on the same property-graph model as Gremlin.

### [openCypher explain](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain.html)

The openCypher explain feature is a self-service tool in Amazon Neptune that helps you understand the execution approach taken by the Neptune engine.

- [Example: relationship lookup](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain-example-2.html): This query looks for relationships between two anonymous nodes with type route, and returns at most 10.
- [Example: value function](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain-example-3.html): The function is:
- [Example: mathematical expression](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain-example-4.html): In this example, RETURN abs(-10) performs a simple evaluation, taking the absolute value of a constant, -10.
- [Example: variable-length path](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain-example-5.html): This is an example of a more complex query plan for handling a variable-length path query.
- [Transactions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-transactions.html): The openCypher implementation in Amazon Neptune uses the transaction semantics defined by Neptune However, isolation levels provided by the Bolt driver have some specific implications for Bolt transaction semantics, as described in the sections below.

### [Query hints](https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-query-hints.html)

- [Query plan cache](https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-query-hints-qpc-hint.html): Query plan cache behavior can be overridden on a per-query (parameterized or not) basis by query-level query hint QUERY:PLANCACHE.
- [AssumeConsistentDataTypes hint](https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-query-hints-AssumeConsistentDataTypes.html): openCypher follows a paradigm where matches of numerical datatypes (e.g., int, byte, short, long, etc.) are carried out under type promotion semantics.
- [Query timeout](https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-query-hints-timeout-hint.html): Query timeout behavior can be configured on a per-query basis by query-level query hint QUERY:TIMEOUTMILLISECONDS.
- [Restrictions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-limitations.html): The Amazon Neptune release of openCypher still does not support everything that is specified in the Cypher Query Language Reference, Version 9, as is detailed in .
- [Exceptions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-exceptions.html): When working with openCypher on Amazon Neptune, a variety of exceptions may occur.

### [Extensions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-extensions.html)

Amazon Neptune supports the openCypher specification reference version 9.

### [neptune.read()](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-21-extensions-s3-read.html)

Neptune supports a CALL procedure neptune.read to read data from Amazon S3 and then run an openCypher query (read, insert, update) using the data.

- [Query examples using parquet](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-21-extensions-s3-read-parquet.html): The following example query returns the number of rows in a given Parquet file:
- [Query examples using CSV](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-21-extensions-s3-read-csv.html): In this example, the query returns the number of rows in a given CSV file:
- [neptune.read() permissions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-21-extensions-s3-read-permissions.html): Required IAM policies and permissions for using neptune.read() with openCypher queries.

### [Spatial Data](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-data.html)

Learn how to query spatial data in Neptune using spatial types and functions.

### [Spatial Functions](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions.html)

Reference for spatial functions available in Neptune openCypher.

- [ST_Point](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-point.html): ST_Point returns a point from the input coordinate values.
- [ST_GeomFromText](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-geomfromtext.html): ST_GeomFromText constructs a geometry object from a well-known text (WKT) representation of an input geometry.
- [ST_AsText](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-astext.html): ST_AsText returns the well-known text (WKT) representation of an input geometry.
- [ST_GeometryType](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-geometrytype.html): ST_GeometryType returns the type of the geometry as a string.
- [ST_Equals](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-equals.html): ST_Equals returns true if the 2D projections of the input geometries are topologically equal.
- [ST_Contains](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-contains.html): ST_Contains returns true if the 2D projection of the first input geometry contains the 2D projection of the second input geometry.
- [ST_Intersects](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-intersect.html): ST_Intersects returns true if the 2D projections of the two input geometries have at least one point in common.
- [ST_Distance](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-distance.html): For input geometries, ST_Distance returns the minimum Euclidean distance between the 2D projections of the two input geometry values.
- [ST_DistanceSpheroid](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-distancespheroid.html): Returns the minimum distance in meters between two lon/lat geometries.
- [ST_Envelope](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-envelope.html): ST_Envelope returns the minimum bounding box of the input geometry, as follows:
- [ST_Buffer](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-buffer.html): ST_Buffer returns 2D geometry that represents all points whose distance from the input geometry projected on the xy-Cartesian plane is less than or equal to the input distance.

### [SPARQL](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html)

Set up your environment to use SPARQL to access Neptune.

- [RDF4J Console](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql-rdf4j-console.html): Steps for connecting to Neptune using the RDF4J console.
- [RDF4J Workbench](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql-rdf4j-workbench.html): Steps for connecting to Neptune using RDF4J Workbench.
- [Java](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql-java.html): Steps for connecting to Neptune using Java and performing a SPARQL query.

### [HTTP API](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-api-reference.html)

Information about using the SPARQL HTTP API in Neptune.

- [HTTP REST](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql-http-rest.html): Steps for connecting to Neptune using the HTTP REST endpoint and performing a SPARQL query.
- [Optional HTTP trailing headers](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql-http-trailing-headers.html)
- [RDF media-type support](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-media-type-support.html): Resource Description Framework (RDF) data can be serialized in many different ways, most of which SPARQL can consume or output:
- [SPARQL UPDATE LOAD](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-api-reference-update-load.html): The syntax of the SPARQL UPDATE LOAD command is specified in the SPARQL 1.1 Update recommendation:
- [SPARQL UPDATE UNLOAD](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-api-reference-unload.html): Neptune also provides a custom SPARQL operation, UNLOAD, for removing data that is specified in a remote source.

### [Query hints](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-query-hints.html)

Use query hints to specify optimization and evaluation strategies for a particular SPARQL query in Neptune.

- [joinOrder](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-query-hints-joinOrder.html): Use the Neptune joinOrder query hint to specify that the query should be evaluated in a given order.
- [evaluationStrategy](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-query-hints-evaluationStrategy.html): Use the evaluationStrategy query hint to tell Amazon Neptune that a query fragment should be evaluated from the bottom up as an independent unit.
- [queryTimeout](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-query-hints-queryTimeout.html): Use the queryTimeout query hint to reduce the time it takes for a query to time out.
- [rangeSafe](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-query-hints-rangeSafe.html): Use the rangeSafe query hint to turn off type promotion.
- [queryId](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-query-hints-queryId.html): Use the queryId query hint to assign your own ID value to a SPARQL query.
- [useDFE](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-query-hints-useDFE.html): Use the useDFE query hint to turn use of the DFE alternative query engine on or off.
- [DESCRIBE query hints](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-query-hints-for-describe.html): A SPARQL DESCRIBE query provides a flexible mechanism for requesting resource descriptions.
- [DESCRIBE and the default graph](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-default-describe.html): Neptune implements SPARQL DESCRIBE using the default graph.
- [Query status](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-api-status.html): Information about using the SPARQL query status HTTP API in Neptune.
- [Query cancellation](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-api-status-cancel.html): Information about using the SPARQL query cancellation HTTP API in Neptune.
- [Graph store protocol](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-graph-store-protocol.html): Information about using the SPARQL graph-store HTTP API in Neptune.

### [SPARQL explain](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain.html)

Use the SPARQL explain feature in Neptune to understand and improve your query execution.

- [SPARQL query engine](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain-engine.html): Understand how the Neptune SPARQL query engine works.
- [Using SPARQL explain](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain-using.html): Use SPARQL explain to analyze and improve query execution in Neptune.
- [explain Examples](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain-examples.html): Understand the various kinds of output that you can produce by invoking the SPARQL explain feature in Neptune.
- [explain operators](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain-operators.html): Description of operators and parameters for the Amazon Neptune SPARQL explain feature.
- [explain Limitations](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain-limitations.html): Limitations of the release of the SPARQL explain feature in Neptune.
- [SPARQL SERVICE Extension](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-service.html): Use the SPARQL SERVICE keyword in Neptune to federate queries.


## [Visualization tools](https://docs.aws.amazon.com/neptune/latest/userguide/visualization-tools.html)

- [Graph-explorer](https://docs.aws.amazon.com/neptune/latest/userguide/visualization-graph-explorer.html): Graph-explorer is an open-source low-code visual exploration tool for graph data, available under the Apache-2.0 license.
- [Tom Sawyer Software](https://docs.aws.amazon.com/neptune/latest/userguide/visualization-tom-sawyer.html): Tom Sawyer Perspectives is a low-code graph and data visualization and analysis development platform for data stored in Amazon Neptune.
- [Cambridge Intelligence](https://docs.aws.amazon.com/neptune/latest/userguide/visualization-cambridge-intelligence.html): Cambridge Intelligence provides data visualization technologies for exploring and understanding Amazon Neptune data.
- [Graphistry](https://docs.aws.amazon.com/neptune/latest/userguide/visualization-graphistry.html): Graphistry is a visual graph intelligence platform that leverages GPU acceleration for rich visual experiences.
- [metaphacts](https://docs.aws.amazon.com/neptune/latest/userguide/visualization-metaphacts.html): metaphacts offers a flexible, open platform for describing and querying graph data and for visualizing and interacting with knowledge graphs.
- [G.V() graph database client](https://docs.aws.amazon.com/neptune/latest/userguide/gv-tool.html): G.V() is a comprehensive graph database client for Amazon Neptune that helps you explore, visualize, and interact with your graph data.
- [Linkurious](https://docs.aws.amazon.com/neptune/latest/userguide/visualization-Linkurious.html): Linkurious provides different graph intelligence solutions for both technical and non-technical users and a variety of use cases.
- [Graph.Build](https://docs.aws.amazon.com/neptune/latest/userguide/visualization-graph.build.html): In any domain, collaboration with subject matter experts is key to designing graph models that effectively address specific use cases.


## [Exporting data](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-data-export.html)

- [neptune-export](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-export.html): You can use the open-source neptune-export tool in two different ways:

### [Neptune-Export service](https://docs.aws.amazon.com/neptune/latest/userguide/export-service.html)

You can use the following steps to export data from your Neptune DB cluster to Amazon S3 using the Neptune-Export service:

- [Run an export job](https://docs.aws.amazon.com/neptune/latest/userguide/export-service-run-export.html): The Outputs tab of the CloudFormation stack also includes the NeptuneExportApiUri.
- [neptune-export utility](https://docs.aws.amazon.com/neptune/latest/userguide/export-utility.html): You can use the following steps to export data from your Neptune DB cluster to Amazon S3 using the neptune-export command-line utility:
- [Exported files](https://docs.aws.amazon.com/neptune/latest/userguide/exported-files.html): When an export is complete, the export files are published to the Amazon S3 location you have specified.

### [Export parameters](https://docs.aws.amazon.com/neptune/latest/userguide/export-parameters.html)

Whether you are using the Neptune-Export service or the neptune-export command line utility, the parameters you use to control the export are mostly the same.

- [params](https://docs.aws.amazon.com/neptune/latest/userguide/export-params-fields.html): The Neptune export params JSON object allows you to control the export, including the type and format of the exported data.
- [Filtering examples](https://docs.aws.amazon.com/neptune/latest/userguide/export-filtering-examples.html): Here are examples that illustrate ways to filter the data that is exported.
- [Troubleshooting](https://docs.aws.amazon.com/neptune/latest/userguide/export-troubleshooting.html): The Amazon Neptune export process uses AWS Batch to provision the compute and storage resources necessary to export your Neptune data.

### [Exporting Gremlin query results to Amazon S3](https://docs.aws.amazon.com/neptune/latest/userguide/exporting-gremlin.html)

Starting in engine release 1.4.3.0, Amazon Neptune supports exporting Gremlin query results directly to Amazon S3.

- [Granting access for Gremlin Amazon S3 export feature](https://docs.aws.amazon.com/neptune/latest/userguide/granting-access-gremlin.html): Required IAM policies


## [Managing Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console.html)

### [Neptune Blue/Green solution](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-deployments.html)

Amazon Neptune engine upgrades can require application downtime because the database is unavailable while the updates are being installed and verified.

- [Use CloudFormation to run the solution](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-console-cfn.html): You can use AWS CloudFormation to deploy the Neptune Blue/Green solution.
- [Monitoring progress](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-monitoring.html): You can monitor the progress of the Neptune Blue/Green solution by going to the CloudWatch console and looking at logs in the /aws/neptune/(Neptune Blue/Green deployment ID) CloudWatch log group.
- [Cutting over to the updated cluster](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-cutover.html): Before promoting the green cluster to production, ensure that the commit difference between the blue and green clusters is zero and then disable all write traffic to the blue cluster.
- [Cleanup](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-cleanup.html): After you have promoted the staging (green) cluster to production, clean up the resources created by the Neptune Blue/Green solution:
- [Best practices](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-best-practices.html)
- [Troubleshooting](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-troubleshooting.html): The following information highlights issues that can arise during the Blue/Green solution deployment process, such as conflicts with existing clusters, the need to enable Neptune streams, ongoing bulk load operations, and version compatibility requirements.
- [IAM user permissions](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-iam-user.html): To access the Neptune console to create and manage a Neptune DB cluster, you need to create an IAM user with all the necessary permissions.
- [Parameter groups](https://docs.aws.amazon.com/neptune/latest/userguide/parameter-groups.html): Overview of parameter groups and how to create and edit them in Neptune.
- [Parameters](https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html): Parameters that you can use to configure Neptune.
- [Launch using the console](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-launch-console.html): The easiest way to launch a new Neptune DB cluster is to use an CloudFormation template that creates all the required resources for you, as explained in .
- [Stopping and starting a cluster](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-stop-start.html): Stop and start all DB instances in an Amazon Neptune cluster at once.
- [Fast reset API](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-fast-reset.html): How to reset a Neptune DB cluster quickly and easily.
- [Adding reader instances](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-add-replicas.html): Add Neptune read-replicas to a DB cluster to offload read workloads from the primary DB instance.
- [Creating a reader instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-create-replica.html): After creating the primary instance for your Neptune DB cluster, you can add additional Neptune reader instances using the Neptune console.
- [Modifying a DB Cluster](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-modify.html): When you modify a DB instance using the AWS Management Console, you can choose to apply the changes right away by selecting Apply Immediately.
- [Performance and Scaling](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-performance-scaling.html): Neptune DB clusters and instances scale at three different levels:
- [Auto-scaling](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-autoscaling.html): How to auto-scale the number of Neptune replicas.

### [Cluster maintenance](https://docs.aws.amazon.com/neptune/latest/userguide/cluster-maintenance.html)

Neptune periodically performs maintenance on Neptune resources.

- [Release types](https://docs.aws.amazon.com/neptune/latest/userguide/release-types.html): The four types of engine release that correspond to the four parts of an engine version number are as follows:
- [Engine version life-spans](https://docs.aws.amazon.com/neptune/latest/userguide/engine-updates-eol-planning.html): Neptune engine versions almost always reach their end of life at the end of a calendar quarter.
- [Managing engine updates](https://docs.aws.amazon.com/neptune/latest/userguide/engine-maintenance-management.html)
- [Upgrade process](https://docs.aws.amazon.com/neptune/latest/userguide/engine-updates-manually.html)
- [Upgrading to 1.2.0.0 or above](https://docs.aws.amazon.com/neptune/latest/userguide/engine-updates-1200-changes.html): Engine release 1.2.0.0 introduced several significant changes that can make upgrading from an earlier version more complicated than usual:

### [Update via CloudFormation](https://docs.aws.amazon.com/neptune/latest/userguide/cfn-engine-update.html)

You can re-use the Neptune CloudFormation template that you used to create your Neptune DB Cluster to update its engine version.

- [1.2.0.1 to 1.2.0.2](https://docs.aws.amazon.com/neptune/latest/userguide/cfn-engine-update-1201-1202.html): Find the DB cluster that you want to upgrade, and the template you used to create it.
- [1.1.1.0 to 1.2.0.2, default](https://docs.aws.amazon.com/neptune/latest/userguide/cfn-engine-update-1110-1202-default.html): Find the DBCluster that you want to upgrade, and the template you used to create it.
- [1.1.1.0 to 1.2.0.2, custom](https://docs.aws.amazon.com/neptune/latest/userguide/cfn-engine-update-1110-1202-custom.html): Find the DBCluster that you want to upgrade, and the template you used to create it.
- [1.1.1.0 to 1.2.0.2, mixed](https://docs.aws.amazon.com/neptune/latest/userguide/cfn-engine-update-1110-1202-mixed.html): Find the DBCluster that you want to upgrade, and the template you used to create it.
- [Cloning a DB Cluster](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-cloning.html): Using DB cloning, you can quickly and cost-effectively create clones of all your databases in Amazon Neptune.

### [Managing Instances](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances.html)

The following sections have information on instance-level operations.

- [T3 Burstable Instances](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-t3.html): A T3 burstable DB instance is the most cost-effective for development.
- [Modifying an Instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-modify.html): Modify a Neptune DB instance and choose when to apply the changes.
- [Renaming a Neptune DB Instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-rename.html): Rename a DB instance by using the Neptune console.
- [Rebooting a DB instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-reboot.html): Reboot the DB instance for the changes to take effect by using the Neptune console.
- [Deleting a DB Instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html): Delete a Neptune DB instance by specifying the name of the instance with or without a final DB snapshot.


## [Neptune streams](https://docs.aws.amazon.com/neptune/latest/userguide/streams.html)

### [Using Streams](https://docs.aws.amazon.com/neptune/latest/userguide/streams-using.html)

Enable change logging and get access to the change-log stream in Neptune.

- [Enabling Streams](https://docs.aws.amazon.com/neptune/latest/userguide/streams-using-enabling.html): You can enable or disable Neptune Streams at any time by setting the neptune_streams DB cluster parameter.
- [Disabling Streams](https://docs.aws.amazon.com/neptune/latest/userguide/streams-using-disabling.html): You can turn Neptune Streams off any time that it is running.
- [Calling the Streams API](https://docs.aws.amazon.com/neptune/latest/userguide/streams-using-api-call.html): You access Neptune Streams using a REST API that sends an HTTP GET request to one of the following local endpoints:
- [Streams Response](https://docs.aws.amazon.com/neptune/latest/userguide/streams-using-api-reponse.html): A response to a Neptune Streams REST API request has the following fields:
- [Streams Exceptions](https://docs.aws.amazon.com/neptune/latest/userguide/streams-using-api-exceptions.html): The following table describes Neptune Streams exceptions.
- [Streams Record Formats](https://docs.aws.amazon.com/neptune/latest/userguide/streams-change-formats.html): The serialization formats for changes to Gremlin and SPARQL graph data in Neptune.
- [Streams Examples](https://docs.aws.amazon.com/neptune/latest/userguide/streams-examples.html): Examples of accessing change-log stream data in Neptune.
- [Neptune-to-Neptune Replication Setup](https://docs.aws.amazon.com/neptune/latest/userguide/streams-consumer-setup.html): You can use an CloudFormation template to set up the Neptune streams consumer application to support Neptune-to-Neptune replication.

### [Streams for disaster recovery](https://docs.aws.amazon.com/neptune/latest/userguide/streams-disaster-recovery.html)

Using Neptune streams cross-region replication for disaster recovery.

- [Replication setup](https://docs.aws.amazon.com/neptune/latest/userguide/streams-disaster-recovery-setup.html): Your primary production DB cluster resides in a VPC in a given source region.
- [Other considerations](https://docs.aws.amazon.com/neptune/latest/userguide/streams-disaster-recovery-setup-other.html)


## [Neptune full text search](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search.html)

### [Full-text search setup](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-cfn-setup.html)

Amazon Neptune supports full-text search in Gremlin and SPARQL queries using Amazon OpenSearch Service (OpenSearch Service).

- [CloudFormation template](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-cfn-create.html)
- [Existing databases](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-cfn-enabling.html): These are the established approaches to enabling full text search on existing Amazon Neptune databases.
- [Updating the poller](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-cfn-update-poller.html): The following information outlines the steps needed to update the stream poller with the latest Lambda artifacts using the AWS management console.

### [Stopping and starting the poller](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-using-pausing-poller.html)

- [Pause the poller](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-pause-poller.html)
- [Re-enable the poller](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-re-enable-poller.html)
- [OpenSearch Serverless](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-serverless.html): Starting with engine release 1.3.0.0, Amazon Neptune supports using Amazon OpenSearch Service Serverless for full-text search in Gremlin and SPARQL queries.
- [Querying with fine-grained access control](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-fgac.html): If you have enabled fine-grained access control on your OpenSearch cluster, you need to enable IAM authentication in your Neptune database as well.
- [Use of Lucene syntax](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-lucene.html): OpenSearch supports using Apache Lucene syntax for query_string queries.
- [Neptune Full-text search data model](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-model.html): Overview of unified JSON document structure used by Neptune for storing SPARQL and Gremlin data in OpenSearch Service.
- [Full-text search parameters](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-parameters.html): Amazon Neptune uses the following parameters for specifying full-text OpenSearch queries in both Gremlin and SPARQL:

### [Non-string indexing](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-non-string-indexing.html)

How Neptune lets you index non-string values in OpenSearch.

- [Updating an existing stack](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-non-string-indexing-update.html): If you are already using Neptune full-text search, here are the steps you need to take to support non-string indexing:
- [Excluding fields](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-non-string-indexing-filters.html): There are two fields in the CloudFormation template details that let you specify property or predicate keys or datatypes to exclude from OpenSearch indexing:
- [Datatype mappings](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-non-string-indexing-mapping.html): New datatype mappings in OpenSearch are created based on the datatype being used in the property or object.
- [Datatype validation](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-data-validation.html)
- [Sample queries](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-non-string-examples.html): Neptune does not currently support OpenSearch range queries directly.
- [Full-text-search query execution](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-query-execution.html): How Neptune plans and executes full-text search queries.
- [Sample SPARQL full-text search queries](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-sparql-examples.html): The following are some sample SPARQL queries that use full-text search in Amazon Neptune.
- [Sample Gremlin full-text search queries](https://docs.aws.amazon.com/neptune/latest/userguide/full-text-search-gremlin.html): NeptuneSearchStep enables full-text search queries for the part of a Gremlin traversal that is not converted into Neptune steps.
- [Troubleshooting and metrics](https://docs.aws.amazon.com/neptune/latest/userguide/streams-consumer-troubleshooting.html)


## [AWS Lambda functions](https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions.html)

- [Gremlin WebSocket connections](https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions-websocket-connections.html): If you use a Gremlin language variant to query Neptune, the driver connects to the database using a WebSocket connection.

### [Gremlin Lambda recommendations](https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions-gremlin-recommendations.html)

We now recommend using a single connection and graph traversal source for the entire lifetime of a Lambda execution context, rather than one for each function invocation (every function invocation handles only one client request).

- [Write-request recommendations](https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions-gremlin-write-recommendations.html): If your Lambda function modifies graph data, consider adopting a back-off-and-retry strategy to handle the following exceptions:
- [Read-request recommendations](https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions-gremlin-read-recommendations.html): If you have one or more read replicas in your cluster, it's a good idea to balance read requests across these replicas.
- [Cold-start latency](https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions-gremlin-cold-start-recommendations.html): The first time an AWS Lambda function is invoked is referred to as a cold start.
- [Creating a Lambda Function](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-cfn-lambda.html): You can use an CloudFormation template to create an AWS Lambda function that can access Neptune.
- [Lambda function examples](https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions-examples.html): The following example AWS Lambda functions, written in Java, JavaScript and Python, illustrate upserting a single vertex with a randomly generated ID using the fold().coalesce().unfold() idiom.


## [Neptune machine learning](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning.html)

### [Neptune ML setup](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-setup.html)

The easiest way to get started with Neptune ML is to use the CloudFormation quick-start template.

- [Setup using CloudFormation](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-quick-start.html): The easiest way to get started with Neptune ML is to use the CloudFormation quick-start template.

### [Manual setup](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-manual-setup.html)

What you need to do to set up Neptune ML without using the quick-start CloudFormation template.

- [Manual ML notebook setup](https://docs.aws.amazon.com/neptune/latest/userguide/ml-manual-setup-notebooks.html): Neptune SageMaker AI notebooks come pre-loaded with a variety of sample notebooks for Neptune ML.
- [Using the AWS CLI](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-cluster-setup.html): In addition to the CloudFormation quick-start template and the AWS Management Console, you can also set up Neptune ML using the AWS CLI.

### [Using Neptune ML](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-overview.html)

The Neptune ML feature in Amazon Neptune provides a streamlined workflow for leveraging machine learning models within a graph database.

- [Handling evolving data](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-overview-evolving-data.html): With a continuously changing graph, you may want to create new batch predictions periodically using fresh data.
- [Updating the model artifacts](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-overview-evolving-data-incremental.html): While you update model artifacts simply by re-running the steps one through three (from Data export and configuration to Model transform), Neptune ML supports simpler ways to update your batch ML predictions using new data.
- [Custom model workflow](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-overview-custom-model-workflow.html): Neptune ML lets you implement, train and deploy custom models of your own for any of the tasks that Neptune ML supports.
- [Instance selection](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-on-graphs-instance-selection.html): The different stages of Neptune ML processing use different SageMaker AI instances.

### [Data export](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-data-export.html)

Neptune ML requires that you provide training data for the Deep Graph Library (DGL) to create and evaluate models.

- [Neptune-Export examples](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-export-examples.html): This request exports property-graph training data for a node classification task:
- [Params settings](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-params.html): The params object in an export request can contain various fields, as described in the params documentation.

### [AdditionalParams](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-additionalParams.html)

The additionalParams object contains fields that you can use to specify machine-learning class labels and features for training purposes and guide the creation of a training data configuration file.

- [Top-level neptune_ml fields](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-neptune_ml-top-level.html)
- [targets](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-neptune_ml-targets.html): The targets field in a JSON training data export configuration contains an array of target objects that specify a training task and and the machine-learning class labels for training this task.
- [features](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-neptune_ml-features.html): Property values and RDF literals come in different formats and data types.
- [Examples](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-data-export-additionalParams-examples.html): The following examples demonstrate how to utilize the "additionalParams" feature in property-graph and RDF data models to configure various aspects of the model training process for a Neptune ML application.

### [Data processing](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-on-graphs-processing.html)

The data-processing step takes the Neptune graph data created by the export process and creates the information that is used by the Deep Graph Library (DGL) during training.

- [Feature encoding](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-feature-encoding.html): Property values come in different formats and data types.

### [Editing a training data file](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-processing-training-config-file.html)

The Neptune export process exports Neptune ML data from a Neptune DB cluster into an S3 bucket.

- [Sample file](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-processing-training-config-file-example.html): Here is a sample training data configuration file that describes a graph for a node-classification task:
- [File structure](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-processing-training-config-file-structure.html): The training configuration file refers to CSV files saved by the export process in the nodes/ and edges/ folders.

### [Model training](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-on-graphs-model-training.html)

After you have processed the data that you exported from Neptune for model training, you can start a model-training job using a curl (or awscurl) command like the following:

- [Models and training](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-models-and-training.html): Neptune ML uses Graph Neural Networks (GNN) to create models for the various machine-learning tasks.
- [Customizing hyperparameters](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-customizing-hyperparams.html): When you start a Neptune ML model-training job, Neptune ML automatically uses the information inferred from the preceding data-processing job.
- [Training best practices](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-improve-model-performance.html): There are things you can do to improve the performance of Neptune ML models.
- [Model transform](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-model-transform.html): Using the Neptune ML model transform command, you can compute model artifacts like node embeddings on processed graph data using pre-trained model parameters.
- [Model artifacts](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-model-artifacts.html): After model training, Neptune ML uses the best trained model parameters to generate model artifacts that are necessary for launching the inference endpoint and providing model predictions.

### [Custom models](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-custom-models.html)

- [Custom model overview](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-custom-model-overview.html)
- [Custom model development](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-custom-model-development.html): A good way to start custom model development is by following Neptune ML toolkit examples to structure and write your training module.
- [Inference endpoint](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-on-graphs-inference-endpoint.html): An inference endpoint lets you query one specific model that the model-training process constructed.

### [Inference queries](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-inference-queries.html)

Query the Neptune ML inference endpoint using Gremlin or SPARQL.

### [Gremlin inference queries](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-gremlin-inference-queries.html)

Query the Neptune ML inference endpoint using the Gremlin query language.

- [Inference query predicates](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-gremlin-inference-query-predicates.html)
- [Node classification](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-gremlin-vertex-classification-queries.html): For Gremlin node classification in Neptune ML:
- [Node regression](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-gremlin-vertex-regression-queries.html): Node regression is similar to node classification, except that the value inferred from the regression model for each node is numeric.
- [Edge classification](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-gremlin-edge-classification-queries.html): For Gremlin edge classification in Neptune ML:
- [Edge regression](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-gremlin-edge-regression.html): Edge regression is similar to edge classification, except that the value inferred from the ML model is numeric.
- [Link prediction](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-gremlin-link-prediction-queries.html): Link-prediction models can solve problems such as the following:
- [Exceptions list](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-gremlin-exceptions.html): This is a comprehensive list of exceptions that can occur when executing Neptune ML Gremlin inference queries.

### [SPARQL inference queries](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-sparql-inference-queries.html)

Query the Neptune ML inference endpoint using the SPARQL query language.

- [SPARQL inference query predicates](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-sparql-inference-query-predicates.html): The following predicates are used with SPARQL inference:
- [Object classification](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-sparql-inference-object-classification.html): For SPARQL object classification in Neptune ML, the model is trained on one of the predicate values.
- [Object regression](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-sparql-inference-object-regression.html): Object regression is similar to object classification, except that a numerical predicate value inferred from the regression model for each node.
- [Object prediction](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-sparql-inference-object-prediction.html): Object prediction predicts the object value for a given subject and predicate.
- [Subject prediction](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-sparql-inference-subject-prediction.html): Subject prediction predicts the subject given a predicate and an object.
- [Exceptions list](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-sparql-exceptions.html)

### [Neptune ML API](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-reference.html)

- [The dataprocessing command](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-dataprocessing.html): You use the Neptune ML dataprocessing command to create a data processing job, check its status, stop it, or list all active data-processing jobs.
- [The modeltraining command](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-modeltraining.html): You use the Neptune ML modeltraining command to create a model training job, check its status, stop it, or list all active model-training jobs.
- [The modeltransform command](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-modeltransform.html): You use the Neptune ML modeltransform command to create a model transform job, check its status, stop it, or list all active model-transform jobs.
- [The endpoints command](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-endpoints.html): You use the Neptune ML endpoints command to create an inference endpoint, check its status, delete it, or list existing inference endpoints.
- [Exceptions](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-exceptions.html): All Neptune ML management API exceptions return a 400 HTTP code.
- [Limits](https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-limits.html)


## [Monitoring Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/monitoring.html)

- [Instance Status](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-status.html): How to check the status of a DB instance in Neptune.

### [Using CloudWatch](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch.html)

View and monitor metrics for your Neptune DB instances using the CloudWatch console, CloudWatch CLI, or programmatically with the CloudWatch API.

- [Monitor instance performance](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-monitoring-instances.html): You can use CloudWatch metrics in Neptune to monitor what is happening on your DB instances and keep track of the query queue length as observed by the database.
- [Neptune Metrics](https://docs.aws.amazon.com/neptune/latest/userguide/cw-metrics.html)
- [Neptune Dimensions](https://docs.aws.amazon.com/neptune/latest/userguide/cw-dimensions.html): The metrics for Amazon Neptune are qualified by the values for the account, graph name, or operation.
- [Audit Logs with Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/auditing.html): Audit the activity in your Neptune DB cluster.
- [Neptune CloudWatch Logs](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html): Publish audit and error logs from Neptune to CloudWatch Logs.
- [Notebook CloudWatch Logs](https://docs.aws.amazon.com/neptune/latest/userguide/notebook-logs.html): How to enable CloudWatch Logs for a Neptune notebook.
- [Slow-query logs](https://docs.aws.amazon.com/neptune/latest/userguide/slow-query-logs.html): How to use slow-query logging in Neptune.

### [Logging Neptune API Calls with AWS CloudTrail](https://docs.aws.amazon.com/neptune/latest/userguide/cloudtrail.html)

Learn about logging Amazon Neptune with AWS CloudTrail.

- [Neptune Information in CloudTrail](https://docs.aws.amazon.com/neptune/latest/userguide/cloudtrail.CloudTrail.html): CloudTrail is enabled on your AWS account when you create the account.
- [Understanding log file entries](https://docs.aws.amazon.com/neptune/latest/userguide/cloudtrail.CloudTrail_Events.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.

### [Event Notifications](https://docs.aws.amazon.com/neptune/latest/userguide/events.html)

Get a notification using Amazon SNS by email, text message, or a call to an HTTP endpoint when a Neptune event occurs.

- [Categories and messages](https://docs.aws.amazon.com/neptune/latest/userguide/event-lists.html): Neptune generates a significant number of events in categories that you can subscribe to using the Neptune console.
- [Subscribing to events](https://docs.aws.amazon.com/neptune/latest/userguide/events-subscribing.html): You can use the Neptune console to subscribe to event notifications, as follows:
- [Manage subscriptions](https://docs.aws.amazon.com/neptune/latest/userguide/events-manage.html): If you choose Event subscriptions in the navigation pane of the Neptune console, you can view subscription categories and a list of your current subscriptions.

### [Tagging Neptune resources](https://docs.aws.amazon.com/neptune/latest/userguide/tagging.html)

Use tags to manage access, control what actions can be applied to resources, and track costs by adding metadata to your Amazon Neptune resources.

- [Tagging in the console](https://docs.aws.amazon.com/neptune/latest/userguide/tagging-console.html): The process to tag an Amazon Neptune resource is similar for all resources.
- [Tagging with the CLI](https://docs.aws.amazon.com/neptune/latest/userguide/tagging-cli.html): You can add, list, or remove tags for a DB instance in Neptune using the AWS CLI.
- [Tagging with the API](https://docs.aws.amazon.com/neptune/latest/userguide/tagging-api.html): You can add, list, or remove tags for a DB instance using the Neptune API.

### [Working with ARNs](https://docs.aws.amazon.com/neptune/latest/userguide/tagging-arns.html)

Get the format for the Amazon Resource Name (ARN) for Neptune resources.

- [Constructing an ARN](https://docs.aws.amazon.com/neptune/latest/userguide/tagging-arns-constructing.html): You can construct an ARN for an Amazon Neptune resource using the following syntax.


## [Backing up and restoring](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore.html)

- [Fault Tolerance](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-overview-fault-tolerance.html): A Neptune DB cluster is fault tolerant by design.
- [Backup metrics](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-overview-metrics.html): You can use the Amazon CloudWatch metrics TotalBackupStorageBilled, SnapshotStorageUsed, and BackupRetentionPeriodStorageUsed to review and monitor the amount of storage used by your Neptune backups, as follows:
- [Restoring Data](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-overview-restore.html): You can recover your data by creating a new Neptune DB cluster from the backup data that Neptune retains, or from a DB cluster snapshot that you have saved.
- [Backup window](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-overview-backup-window.html): Automated backups occur daily during the preferred backup window.
- [Creating a Snapshot](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-create-snapshot.html): Create a DB cluster snapshot by identifying which DB cluster you are going to back up and give that DB cluster snapshot a name.
- [Restoring from a Snapshot](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-restore-snapshot.html): Restore a Neptune DB cluster from a DB cluster snapshot.
- [Copying a Snapshot](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-copy-snapshot.html): Copy a Neptune snapshot.
- [Sharing a Snapshot](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-share-snapshot.html): Share a manual DB cluster snapshot so that other AWS accounts can copy or restore a DB instance from it.
- [Deleting a Snapshot](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-delete-snapshot.html): Delete a Neptune snapshot.


## [Best practices](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices.html)

### [Basic operational guidelines](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-general-basic.html)

The following are basic operational guidelines that you should follow when working with Neptune.

- [Security](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-general-security.html): Use AWS Identity and Access Management (IAM) accounts to control access to Neptune API actions.
- [Using Metrics](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-general-metrics.html): To identify performance issues caused by insufficient resources and other common bottlenecks, you can monitor the metrics available for your Neptune DB cluster.

### [Gremlin (General)](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin.html)

Follow these recommendations when using the Gremlin graph traversal language with Neptune.

- [Heartbeat Configuration](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-heartbeat-serverless.html): When using Gremlin WebSocket clients with Neptune Serverless, you need to configure the client's ping interval appropriately to maintain stable connections during scaling events.
- [GLV execution differences](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-console-glv-differences.html): In Gremlin, there are multiple ways for clients to submit queries to the server: using WebSocket, or Bytecode GLV, or through the Gremlin console using string-based scripts.
- [Multithreaded Writes](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-multithreaded-writes.html): There are a few guidelines for multithreaded loading of data into Neptune using Gremlin.
- [Pruning Records](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-prune.html): You can prune stale records by storing the creation time as a property on vertices and dropping them periodically.
- [datetime( )](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-datetime.html): Neptune provides the datetime method for specifying dates and times for queries sent in the Gremlin Groovy variant.
- [Native Date and Time](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-datetime-glv.html): If you are using a Gremlin Language Variant (GLV), you must use the native date and time classes and functions provided by the programming language for Gremlin time data.

### [Gremlin (Java client)](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-client.html)

Follow these recommendations when using the Gremlin Java client with Neptune.

- [Re-use the client object](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-reuse.html): Re-use the same client (or GraphTraversalSource) object across multiple threads.
- [Separate Clients for Reading and Writing](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-separate.html): You can increase performance by only performing writes on the writer endpoint and reading from one or more read-only endpoints.
- [Multiple replica endpoints](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-multiple.html): When creating a Gremlin Java Cluster object, you can use the .addContactPoint() method to add multiple read replica instances to the connection pool's contact points.
- [Close the client when finished](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-close-connections.html): It is important to close the client when you are finished with it to ensure that the WebSocket connections are closed by the server and all resources associated with the connections are released.
- [New connection after failover](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-new-connection.html): In case of failover, the Gremlin Driver might continue connecting to the old writer because the cluster DNS name is resolved to an IP address.
- [Set maxInProcessPerConnection = maxSimultaneousUsagePerConnection](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-maxes.html): Both the maxInProcessPerConnection and the maxSimultaneousUsagePerConnection parameters are related to the maximum number of simultaneous queries you can submit on a single WebSocket connection.
- [Send queries as bytecode](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-bytecode.html): There are advantages to using bytecode rather than a string when submitting queries:
- [Completely consume query results](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-resultset.html): The client object should always completely consume the ResultSet (in the case of string-based submission), or the iterator returned by GraphTraversal.
- [Bulk add vertices and edges](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-batch-add.html): Every query to the Neptune DB runs in the scope of a single transaction, unless you use a session.
- [Disable JVM DNS caching](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-disable-dns-caching.html): In an environment where you want to load-balance requests across multiple read replicas, you need to disable DNS caching in the Java Virtual Machine (JVM) and provide Neptune's reader endpoint while creating the Cluster object.
- [Per-query timeouts](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-per-query-timeout.html): Neptune provides you with the ability to set a timeout for your queries using the parameter group option neptune_query_timeout (see ).
- [Handling a TimeoutException](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-exceptions-TimeoutException.html): The Gremlin Java client throws a java.util.concurrent.TimeoutException when a Gremlin request times out at the client itself while waiting for a slot in one of the WebSocket connections to become available.

### [openCypher and Bolt](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-opencypher.html)

Follow these best practices when using the openCypher query language and Bolt protocol with Neptune.

- [Prefer directed edges](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-opencypher-directed-edges.html): When Neptune performs query optimizations, bi-directional edges make it difficult to create optimal query plans.
- [No concurrent transaction queries](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-opencypher-multiple-queries.html): Although the Bolt driver itself allows concurrent queries in a transaction, Neptune does not support multiple queries in a transaction running concurrently.
- [Close driver objects](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-opencypher-close-driver.html): Be sure to close the client when you are finished with it, so that the Bolt connections are closed by the server and all resources associated with the connections are released.
- [Use explicit transaction modes](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-opencypher-use-explicit-txs.html): When using transactions with Neptune and the Bolt driver, it is best to explicitly set the access mode for both read and write transactions to the right settings.
- [Retry logic](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-opencypher-retry-logic.html): For all exceptions that allow a retry, it is generally best to use an exponential backoff and retry strategy that provides progressively longer wait times between retries so as to better handle transient issues such as ConcurrentModificationException errors.
- [Using the SET clause](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-0.html): Instead of using multiple SET clauses to set individual properties, use a map to set multiple properties for an entity at once.
- [Use parameterized queries](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-2.html): It is recommended to always use parameterized queries when querying using openCypher.
- [UNWIND clase](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-3.html): Deep nested structure can restrict the ability of the query engine to generate an optimal query plan.
- [Variable-Length Path (VLP) expressions](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-4.html): In Variable-Length Path (VLP) queries, the query engine optimizes the evaluation by choosing to start the traversal on the left or right side of the expression.
- [Use granular relationship names](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-5.html): When optimizing for performance, using relationship labels that are exclusive to node patterns allows the removal of label filtering on nodes.
- [Specify edge labels](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-6.html): It is recommended to provide an edge label where possible when specifying an edge in a pattern.
- [Avoid the WITH clause](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-7.html): The WITH clause in openCypher acts as a boundary where everything before it executes, and then the resulting values are passed to the remaining portions of the query.
- [Restrictive filters](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-8.html): In all scenarios, early placement of filters in the query helps in reducing the intermediate solutions a query plan must consider.
- [Explicitly check properties](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-9.html): Based on openCypher semantics, when a property is accessed it is equivalent to an optional join and must retain all rows even if the property does not exist.
- [Avoid named path](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-10.html): Named path in a query always comes at an additional cost, which can add penalties in terms of higher latency and memory usage.
- [Avoid COLLECT(DISTINCT())](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-11.html)
- [Prefer the properties function](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-12.html): The properties() function is used to return a map containing all properties for an entity, and is much more efficient than returning properties individually.
- [Static computations](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-13.html): It is recommended to resolve static computations (simple mathematical/string operations) on the client-side.
- [Batching inputs](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-14.html): Whenever the same query needs to be executed for different inputs, instead of executing one query per input, it would be much more performant to run a query for a batch of inputs.
- [Prefer custom IDs](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-15.html): Neptune allows users to explicitly assign IDs on nodes and relationships.
- [Avoid ~id computations](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-content-16.html): When using custom IDs in the queries, always perform static computations outside the queries and provide these values in the parameters.
- [Updating/Merging multiple nodes](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-merge-multiple-nodes.html): When running MERGE or CREATE queries on multiple nodes it is recommended to use an UNWIND in combination with a single MERGE/CREATE clause versus using a MERGE/CREATE clause for each node.

### [SPARQL](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-sparql.html)

Follow these best practices when using the SPARQL query language with Neptune.

- [Query All Named Graphs](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-sparql-query.html): Amazon Neptune associates every triple with a named graph.
- [Specify a Named Graph to Load](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-sparql-graph.html): Amazon Neptune associates every triple with a named graph.
- [FILTER vs. VALUES](https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-sparql-batch.html): There are three basic ways to inject values in SPARQL queries: Â  FILTER, Â  FILTER...IN, Â  and Â  VALUES.


## [Tools and utilities](https://docs.aws.amazon.com/neptune/latest/userguide/tools.html)

### [GraphQL utility](https://docs.aws.amazon.com/neptune/latest/userguide/tools-graphql.html)

Learn about using the GraphQL utility when working with Amazon Neptune.

- [Installation and setup](https://docs.aws.amazon.com/neptune/latest/userguide/tools-graphql-setup.html): If you're going to use the utility with an existing Neptune database, you need it to be able to connect to the database endpoint.
- [Using existing data](https://docs.aws.amazon.com/neptune/latest/userguide/tools-graphql-scan-existing.html): Whether you are familiar with GraphQL or not, the command below is the fastest way to create a GraphQL API.
- [Using a schema with no directives](https://docs.aws.amazon.com/neptune/latest/userguide/tools-graphql-start-from-schema.html): You can start from an empty Neptune database and use a GraphQL schema with no directives to create the data and query it.
- [Working with directives](https://docs.aws.amazon.com/neptune/latest/userguide/tools-graphql-schema-with-directives.html): You can start from a GraphQL schema that already has directives, using a command like the following:
- [Command-line arguments](https://docs.aws.amazon.com/neptune/latest/userguide/tools-graphql-cmd-line-args.html)
- [Nodestream](https://docs.aws.amazon.com/neptune/latest/userguide/tools-Nodestream.html): Nodestream is a framework for dealing with semantically modeling data as a graph.


## [Neptune Errors](https://docs.aws.amazon.com/neptune/latest/userguide/errors.html)

- [Insufficient DB instances available](https://docs.aws.amazon.com/neptune/latest/userguide/insufficientDBInstancesAvailable.html): The InsufficientDBInstanceCapacity error can be returned when you try to create, start, or modify a DB instance.
- [Engine Error Codes](https://docs.aws.amazon.com/neptune/latest/userguide/errors-engine-codes.html): Amazon Neptune endpoints return the standard errors for Gremlin and SPARQL when encountered.
- [API Errors](https://docs.aws.amazon.com/neptune/latest/userguide/CommonErrors.html): These Amazon Neptune errors are associated with the APIs for creating and modifying Neptune resources with the AWS SDK and AWS CLI.
- [Loader Errors](https://docs.aws.amazon.com/neptune/latest/userguide/loader-message.html): The following messages are returned by the status endpoint of the Neptune Loader.


## [Engine releases](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html)

- [Release: 1.4.7.0 (2026-03-03)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.7.0.html): Amazon Neptune engine update, version 1.4.7.0 on 2026-03-03.
- [Release: 1.4.6.3 (2025-12-18)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.6.3.html): Amazon Neptune engine update, version 1.4.6.3 on 2025-12-18.
- [Release: 1.4.6.2 (2025-11-18)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.6.2.html): Amazon Neptune engine update, version 1.4.6.2 on 2025-11-18.
- [Release: 1.4.6.1 (2025-09-18)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.6.1.html): Amazon Neptune engine update, version 1.4.6.1 on 2025-09-18.
- [Release: 1.4.6.0 (2025-09-02)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.6.0.html): Amazon Neptune engine update, version 1.4.6.0 on 2025-09-02.
- [Release: 1.4.5.1 (2025-06-30)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.5.1.html): Amazon Neptune engine update, version 1.4.5.1 on 2025-06-30.
- [Release: 1.4.5.0 (2025-04-09)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.5.0.html): Amazon Neptune engine update, version 1.4.5.0 on 2025-04-09.
- [Release: 1.4.4.0 (2025-02-24)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.4.0.html): Amazon Neptune engine update, version 1.4.4.0 on 2025-02-24.
- [Release: 1.4.3.0 (2025-01-21)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.3.0.html): Amazon Neptune engine update, version 1.4.3.0 on 2025-01-21.
- [Release: 1.4.2.0 (2024-12-19)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.2.0.html): Amazon Neptune engine update, version 1.4.2.0 on 2024-12-19.
- [Release: 1.4.1.0 (2024-11-21)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.1.0.html): Amazon Neptune engine update, version 1.4.1.0 on 2024-11-21.
- [Release: 1.4.0.0 (2024-11-06)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.4.0.0.html): Amazon Neptune engine update, version 1.4.0.0 on 2024-11-06.
- [Release: 1.3.4.0 (2024-10-01)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.3.4.0.html): Amazon Neptune engine update, version 1.3.4.0 on 2024-10-01.
- [Release: 1.3.3.0 (2024-08-05)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.3.3.0.html): Amazon Neptune engine update, version 1.3.3.0 on 2024-08-05.
- [Release: 1.3.2.1 (2024-06-20)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.3.2.1.html): Amazon Neptune engine update, version 1.3.2.1 on 2024-06-20.
- [Release: 1.3.2.0 (2024-06-10)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.3.2.0.html): Amazon Neptune engine update, version 1.3.2.0 on 2024-06-10.
- [Release: 1.3.1.0 (2024-03-06)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.3.1.0.html): Amazon Neptune engine update, version 1.3.1.0 on 2024-03-06.
- [Release: 1.3.0.0 (2023-11-15)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.3.0.0.html): Amazon Neptune engine update, version 1.3.0.0 on 2023-11-15.
- [Release: 1.2.1.2 (2024-08-05)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.1.2.html): Amazon Neptune engine update, version 1.2.1.2 on 2024-08-05.
- [Release: 1.2.1.1 (2024-03-11)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.1.1.html): Amazon Neptune engine update, version 1.2.1.1 on 2024-03-11.

### [Release: 1.2.1.0 (2023-03-08)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.1.0.html)

Amazon Neptune engine update, version 1.2.1.0 on 2023-03-08.

- [Release: 1.2.1.0.R7 (2023-10-06)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.1.0.R7.html): Amazon Neptune engine update, version 1.2.1.0.R7 on 2023-10-06.
- [Release: 1.2.1.0.R6 (2023-09-12)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.1.0.R6.html): Amazon Neptune engine update, version 1.2.1.0.R6 on 2023-09-12.
- [Release: 1.2.1.0.R5 (2023-09-02)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.1.0.R5.html): Amazon Neptune engine update, version 1.2.1.0.R5 on 2023-09-02.
- [Release: 1.2.1.0.R4 (2023-08-10)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.1.0.R4.html): Amazon Neptune engine update, version 1.2.1.0.R4 on 2023-08-10.
- [Release: 1.2.1.0.R3 (2023-06-13)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.1.0.R3.html): Amazon Neptune engine update, version 1.2.1.0.R3 on 2023-06-13.
- [Release: 1.2.1.0.R2 (2023-05-02)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.1.0.R2.html): Amazon Neptune engine update, version 1.2.1.0.R2 on 2023-05-02.

### [Release: 1.2.0.2 (2022-11-20)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.2.html)

Amazon Neptune engine update, version 1.2.0.2 on 2022-11-20.

- [Release: 1.2.0.2.R6 (2023-09-12)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.2.R6.html): Amazon Neptune engine update, version 1.2.0.2.R6 on 2023-09-12.
- [Release: 1.2.0.2.R5 (2023-08-16)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.2.R5.html): Amazon Neptune engine update, version 1.2.0.2.R5 on 2023-08-16.
- [Release: 1.2.0.2.R4 (2023-05-08)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.2.R4.html): Amazon Neptune engine update, version 1.2.0.2.R4 on 2023-05-08.
- [Release: 1.2.0.2.R3 (2023-03-27)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.2.R3.html): Amazon Neptune engine update, version 1.2.0.2.R3 on 2023-03-27.
- [Release: 1.2.0.2.R2 (2022-12-15)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.2.R2.html): Amazon Neptune engine update, version 1.2.0.2.R2 on 2022-12-15.

### [Release: 1.2.0.1 (2022-10-26)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.1.html)

Amazon Neptune engine update, version 1.2.0.1 on 2022-10-26.

- [Maintenance Release: 1.2.0.1.R3 (2023-09-27)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.1.R3.html): Amazon Neptune engine update, version 1.2.0.1.R3 on 2023-09-27.
- [Maintenance Release: 1.2.0.1.R2 (2022-12-13)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.1.R2.html): Amazon Neptune engine update, version 1.2.0.1.R2 on 2022-12-13.

### [Release: 1.2.0.0 (2022-07-21)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html)

Amazon Neptune engine update, version 1.2.0.0 on 2022-07-21.

- [Release: 1.2.0.0.R4 (2023-09-29)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.R4.html): Amazon Neptune engine update, version 1.2.0.0.R4 on 2023-09-29.
- [Release: 1.2.0.0.R3 (2022-12-15)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.R3.html): Amazon Neptune engine update, version 1.2.0.0.R3 on 2022-12-15.
- [Release: 1.2.0.0.R2 (2022-10-14)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.R2.html): Amazon Neptune engine update, version 1.2.0.0.R2 on 2022-10-14.

### [Release: 1.1.1.0 (2022-04-19)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.1.0.html)

Amazon Neptune engine update, version 1.1.1.0 on 2022-04-19.

- [Release: 1.1.1.0.R7 (2023-01-23)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.1.0.R7.html): Amazon Neptune engine update, version 1.1.1.0.R7 on 2023-01-23.
- [Release: 1.1.1.0.R6 (2022-09-23)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.1.0.R6.html): Amazon Neptune engine update, version 1.1.1.0.R6 on 2022-09-23.
- [Release: 1.1.1.0.R5 (2022-07-21)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.1.0.R5.html): Amazon Neptune engine update, version 1.1.1.0.R5 on 2022-07-21.
- [Release: 1.1.1.0.R4 (2022-06-23)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.1.0.R4.html): Amazon Neptune engine update, version 1.1.1.0.R4 on 2022-06-23.
- [Release: 1.1.1.0.R3 (2022-06-07)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.1.0.R3.html): Amazon Neptune engine update, version 1.1.1.0.R3 on 2022-06-07.
- [Maintenance release: 1.1.1.0.R2 (2022-05-16)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.1.0.R2.html): Amazon Neptune maintenance release engine update, version 1.1.1.0.R2 on 2022-05-16.

### [Release: 1.1.0.0 (2021-11-19)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.0.0.html)

Amazon Neptune engine update, version 1.1.0.0 on 2021-11-19.

- [Maintenance release: 1.1.0.0.R3 (2022-12-23)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.0.0.R3.html): Amazon Neptune maintenance release engine update, version 1.1.0.0.R3 on 2022-12-23.
- [Maintenance release: 1.1.0.0.R2 (2022-05-16)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.1.0.0.R2.html): Amazon Neptune maintenance release engine update, version 1.1.0.0.R2 on 2022-05-16.

### [Release: 1.0.5.1 (2021-10-01)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.5.1.html)

Amazon Neptune engine update, version 1.0.5.1 on 2021-10-01.

- [Maintenance release: 1.0.5.1.R4 (2022-05-16)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.5.1.R4.html): Amazon Neptune maintenance release engine update, version 1.0.5.1.R4 on 2022-05-16.
- [Release: 1.0.5.1.R3 (2022-01-13)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.5.1.R3.html): Amazon Neptune engine update, version 1.0.5.1.R3 on 2022-01-13.
- [Release: 1.0.5.1.R2 (2021-10-26)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.5.1.R2.html): Amazon Neptune engine update, version 1.0.5.1.R2 on 2021-10-26.

### [Release: 1.0.5.0 (2021-07-27)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.5.0.html)

Amazon Neptune engine update, version 1.0.5.0 on 2021-07-27.

- [Maintenance release: 1.0.5.0.R5 (2022-05-16)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.5.0.R5.html): Amazon Neptune maintenance release engine update, version 1.0.5.0.R5 on 2022-05-16.
- [Release: 1.0.5.0.R3 (2021-09-15)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.5.0.R3.html): Amazon Neptune engine update, version 1.0.5.0.R3 on 2021-09-15.
- [Release: 1.0.5.0.R2 (2021-08-16)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.5.0.R2.html): Amazon Neptune engine update, version 1.0.5.0.R2 on 2021-08-16.

### [Release: 1.0.4.2 (2021-06-01)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.2.html)

- [Release: 1.0.4.2.R5 (2021-08-16)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.2.R5.html): Amazon Neptune engine update, version 1.0.4.2.R5 on 2021-08-16.
- [Release: 1.0.4.2.R4 (2021-07-23)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.2.R4.html): Amazon Neptune engine update, version 1.0.4.2.R4 on 2021-07-23.
- [Release: 1.0.4.2.R3 (2021-06-28)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.2.R3.html): Amazon Neptune engine update, version 1.0.4.2.R3 on 2021-06-28.
- [Release: 1.0.4.2.R2 (2021-06-01)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.2.R2.html): Amazon Neptune engine update, version 1.0.4.2.R2 on 2021-06-01.
- [Release: 1.0.4.2.R1 (2021-05-27)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.2.R1.html): Amazon Neptune engine update, version 1.0.4.2.R1 on 2021-05-27.

### [Release: 1.0.4.1 (2020-12-08)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.1.html)

Amazon Neptune engine update, version 1.0.4.1 on 2020-12-08.

- [Release: 1.0.4.1.R1.1 (2021-03-22)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.1.R1.1.html): Amazon Neptune engine update, version 1.0.4.1.R1.1 on 2021-03-22.

### [Release: 1.0.4.1.R2 (2021-02-24)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.1.R2.html)

Amazon Neptune engine update, version 1.0.4.1.R2 on 2021-02-24.

- [Release: 1.0.4.1.R2.1 (2021-03-11)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.1.R2.1.html): Amazon Neptune engine update, version 1.0.4.1.R2.1 on 2021-03-11.

### [Release: 1.0.4.0 (2020-10-12)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.0.html)

Amazon Neptune engine update, version 1.0.4.0 on 2020-10-12.

- [Release: 1.0.4.0.R2 (2021-02-24)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.4.0.R2.html): Amazon Neptune engine update, version 1.0.4.0.R2 on 2021-02-24.

### [Release: 1.0.3.0 (2020-08-03)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.3.0.html)

Amazon Neptune engine update, version 1.0.3.0 on 2020-08-03.

- [Release: 1.0.3.0.R3 (2021-02-19)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.3.0.R3.html): Amazon Neptune engine update, version 1.0.3.0.R3 on 2021-02-19.
- [Release: 1.0.3.0.R2 (2020-10-12)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.3.0.R2.html): Amazon Neptune engine update, version 1.0.3.0.R2 on 2020-10-12.

### [Release: 1.0.2.2 (2020-03-09)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.2.html)

Amazon Neptune engine update, version 1.0.2.2 on 2020-03-09.

- [Release: 1.0.2.2.R6 (2021-02-19)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.2.R6.html): Amazon Neptune engine update, version 1.0.2.2.R6 on 2021-02-19.
- [Release: 1.0.2.2.R5 (2020-10-12)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.2.R5.html): Amazon Neptune engine update, version 1.0.2.2.R5 on 2020-10-12.
- [Release: 1.0.2.2.R4 (2020-07-23)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.2.R4.html): Amazon Neptune engine update, version 1.0.2.2.R4 on 2020-07-23.
- [Release: 1.0.2.2.R3 (2020-07-22)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.2.R3.html): Amazon Neptune engine update, version 1.0.2.2.R3 on 2020-07-22.
- [Release: 1.0.2.2.R2 (2020-04-02)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.2.R2.html): Amazon Neptune engine update, version 1.0.2.2.R2 on 2020-04-02.

### [Release: 1.0.2.1 (2019-11-22)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.1.html)

Amazon Neptune engine update, version 1.0.2.1 on 2019-11-22.

- [Release: 1.0.2.1.R6 (2020-04-22)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.1.R6.html): Amazon Neptune engine update, version 1.0.2.1.R6 on 2020-04-22.
- [Release: 1.0.2.1.R5 (2020-04-22)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.1.R5.html): Amazon Neptune engine update, version 1.0.2.1.R5 on 2020-04-22.
- [Release: 1.0.2.1.R4 (2019-12-20)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.1.R4.html): Amazon Neptune engine update, version 1.0.2.1.R4 on 2019-12-20.
- [Release: 1.0.2.1.R3 (2019-12-12)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.1.R3.html): Amazon Neptune engine update, version 1.0.2.1.R3 on 2019-12-12.
- [Release: 1.0.2.1.R2 (2019-11-25)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.1.R2.html): Amazon Neptune engine update, version 1.0.2.1.R2 on 2019-11-25.

### [Release: 1.0.2.0 (2019-11-08)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.0.html)

Amazon Neptune engine update, version 1.0.2.0 on 2019-11-08.

- [Release: 1.0.2.0.R3 (2020-05-05)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.0.R3.html): Amazon Neptune engine update, version 1.0.2.0.R3 on 2020-05-05.
- [Release: 1.0.2.0.R2 (2019-11-21)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.2.0.R2.html): Amazon Neptune engine update, version 1.0.2.0.R2 on 2019-11-21.
- [Release: 1.0.1.2 (2020-06-10)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.2.html): Amazon Neptune engine update, version 1.0.1.2 on 2020-06-10.
- [Release: 1.0.1.1 (2020-06-26)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.1.html): Amazon Neptune engine update, version 1.0.1.1 on 2020-06-26.

### [Release: 1.0.1.0 (2019-07-02)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.html)

Amazon Neptune engine update, version 1.0.1.0 on 2019-07-02.

- [Release 1.0.1.0.200502.0 (2019-10-31)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200502.0.html): Amazon Neptune engine updates for 2019-10-31.
- [Release 1.0.1.0.200463.0 (2019-10-15)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200463.0.html): Amazon Neptune engine updates for 2019-10-15.
- [Release 1.0.1.0.200457.0 (2019-09-19)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200457.0.html): Amazon Neptune engine updates for 2019-09-19.
- [Release 1.0.1.0.200369.0 (2019-08-13)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200369.0.html): Amazon Neptune engine updates for 2019-08-13.
- [Release 1.0.1.0.200366.0 (2019-07-26)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200366.0.html): Amazon Neptune engine updates for 2019-07-26.
- [Release 1.0.1.0.200348.0 (2019-07-02)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200348.0.html): Amazon Neptune engine updates for 2019-07-02.

### [Earlier Releases](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-earlier.html)

- [Release 1.0.1.0.200310.0 (2019-06-12)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200310.0.html): Amazon Neptune engine updates for 2019-06-12.
- [Release 1.0.1.0.200296.0 (2019-05-01)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200296.0.html): Amazon Neptune engine updates for 2019-05-01.
- [Release 1.0.1.0.200267.0 (2019-01-21)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200267.0.html): Amazon Neptune engine updates for 2019-01-21.
- [Release 1.0.1.0.200264.0 (2018-11-19)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200264.0.html): Amazon Neptune engine updates for 2018-11-19.
- [Release 1.0.1.0.200258.0 (2018-11-08)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200258.0.html): Amazon Neptune engine updates for 2018-11-08.
- [Release 1.0.1.0.200255.0 (2018-10-29)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200255.0.html): Amazon Neptune engine updates for 2018-10-29.
- [Release 1.0.1.0.200237.0 (2018-09-06)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200237.0.html): Amazon Neptune engine updates for 2018-09-06.
- [Release 1.0.1.0.200236.0 (2018-07-24)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200236.0.html): Amazon Neptune engine updates for 2018-07-24.
- [Release 1.0.1.0.200233.0 (2018-06-22)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.0.1.0.200233.0.html): Amazon Neptune engine updates for 2018-06-22.


## [Management API reference](https://docs.aws.amazon.com/neptune/latest/userguide/api.html)

- [Clusters](https://docs.aws.amazon.com/neptune/latest/userguide/api-clusters.html): This section describes Neptune DB cluster data types, along with the API for managing them.
- [Global databases](https://docs.aws.amazon.com/neptune/latest/userguide/api-global-dbs.html): This section describes Neptune global database data types, along with the API for managing them.
- [Instances](https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html): This section describes Neptune instance data types, along with the API for managing them.
- [Parameters](https://docs.aws.amazon.com/neptune/latest/userguide/api-parameters.html): This section describes Neptune parameters and parameter group data types, along with the API for creating, deleting, updating, resetting, copying, and listing them.
- [Subnets](https://docs.aws.amazon.com/neptune/latest/userguide/api-subnets.html): This section describes Neptune subnets and subnet group data types, along with the API for creating, deleting, updating, resetting, copying, and listing them.
- [Snapshots](https://docs.aws.amazon.com/neptune/latest/userguide/api-snapshots.html): This section describes Neptune sanpshot data types, along with the API for managing them.
- [Events](https://docs.aws.amazon.com/neptune/latest/userguide/api-events.html): This section describes Neptune event data types, along with the API for managing them.
- [Other](https://docs.aws.amazon.com/neptune/latest/userguide/api-other-apis.html): This section describes various other Neptune data types, along with the API for managing them.
- [Datatypes](https://docs.aws.amazon.com/neptune/latest/userguide/api-datatypes.html): This section describes various common Neptune data types.
- [API Faults](https://docs.aws.amazon.com/neptune/latest/userguide/api-faults.html): This section describes Neptune exceptions raised by individual APIs.


## [Data API reference](https://docs.aws.amazon.com/neptune/latest/userguide/data-api.html)

- [General](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-environment-APIs.html): Engine operations:
- [Querying](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-queries.html): Gremlin query actions:
- [Bulk loader](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-loader.html): Bulk-load actions:
- [Streams](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-streams.html): Stream access actions:
- [Statistics](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-statistics.html): This section describes.
- [ML data processing](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-ml-data-processing.html): Data-processing actions:
- [ML model training](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-ml-training.html): Model training actions:
- [ML model transform](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-ml-transform.html): Model transform actions:
- [ML Inference endpoint](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-inference.html): Inference endpoint actions:
- [Exceptions](https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-errors.html): Exceptions:
