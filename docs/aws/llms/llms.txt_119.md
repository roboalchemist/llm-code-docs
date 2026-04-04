# Source: https://docs.aws.amazon.com/aurora-dsql/latest/userguide/llms.txt

# Amazon Aurora DSQL User Guide

> Provides concepts, tasks, and reference topics for the Amazon Aurora DSQL service.

- [What is Amazon Aurora DSQL?](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html)
- [Getting started](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html)
- [Backup and restore](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html)
- [Tagging resources](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/CHAP_tagging.html)
- [Considerations](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/considerations.html)
- [Quotas and limits](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/CHAP_quotas.html)
- [API reference](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/CHAP_api_reference.html)
- [Troubleshooting](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/troubleshooting.html)
- [Providing feedback](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/providing-feedback.html)
- [Document history](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/doc-history.html)

## [Authentication and authorization](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/authentication-authorization.html)

- [Generate an authentication token](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_authentication-token.html): To connect to Amazon Aurora DSQL with a SQL client, generate an authentication token to use as the password.
- [Database roles and IAM authentication](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/using-database-and-iam-roles.html): Aurora DSQL supports authentication using both IAM roles and IAM users.


## [Aurora DSQL and PostgreSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with.html)

### [SQL compatibility](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility.html)

In the following sections, learn about Aurora DSQL support for PostgreSQL data types and SQL commands.

- [Supported data types](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility-supported-data-types.html): Aurora DSQL supports a subset of the common PostgreSQL types.
- [Supported SQL features](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility-supported-sql-features.html): Aurora DSQL supports a wide range of core PostgreSQL SQL features.

### [Supported subsets of SQL commands](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility-supported-sql-subsets.html)

This section provides detailed information about supported SQL commands, focusing on commands with extensive parameter sets and subcommands.

- [CREATE TABLE](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/create-table-syntax-support.html): CREATE TABLE defines a new table.
- [ALTER TABLE](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/alter-table-syntax-support.html): ALTER TABLE changes the definition of a table.
- [CREATE SEQUENCE](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/create-sequence-syntax-support.html): CREATE SEQUENCE â define a new sequence generator.
- [ALTER SEQUENCE](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/alter-sequence-syntax-support.html): ALTER SEQUENCE â change the definition of a sequence generator.
- [DROP SEQUENCE](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/drop-sequence-syntax-support.html): DROP SEQUENCE â remove a sequence.
- [CREATE VIEW](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/create-view.html): CREATE VIEW defines a new persistent view.
- [ALTER VIEW](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/alter-view-syntax-support.html): The ALTER VIEW statement allows changing various properties of an existing view, and Aurora DSQL supports all the PostgreSQL syntax for this command.
- [DROP VIEW](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/drop-view-overview.html): The DROP VIEW statement removes an existing view.

### [Migration guide](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility-migration-guide.html)

Aurora DSQL is designed to be PostgreSQL compatible, supporting core relational features such as ACID transactions, secondary indexes, joins, and standard DML operations.

- [Agentic migration](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/dsql-agentic-migration.html): AI coding agents can accelerate your migration to Aurora DSQL by analyzing schemas, transforming code, and executing DDL migrations with built-in safety checks.
- [Concurrency control](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-concurrency-control.html): Concurrency allows multiple sessions to access and modify data simultaneously without compromising data integrity and consistency.
- [DDL and distributed transactions](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-ddl.html): Data definition language (DDL) behaves differently in Aurora DSQL from PostgreSQL.
- [Primary keys](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-primary-keys.html): In Aurora DSQL, a primary key is a feature that physically organizes table data.

### [Sequences and identity columns](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/sequences-identity-columns.html)

Sequences and identity columns generate integer values and are useful when compact or human-readable identifiers are needed.

- [Sequence manipulation functions](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/sequence-functions-syntax-support.html): This section describes functions for operating on sequence objects, also called sequence generators or just sequences.
- [Identity columns](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/sequences-identity-columns-overview.html)
- [Working with sequences and identity columns](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/sequences-identity-columns-working-with.html): This section helps you understand how best to use sequences and identity columns based on workload patterns.
- [Asynchronous indexes](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-create-index-async.html): The CREATE INDEX ASYNC command creates an index on one or more columns of a specified table.
- [System tables and commands](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-systems-tables.html): See the following sections to learn about the supported system tables and catalogs in Aurora DSQL.

### [EXPLAIN plans](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-explain-plans.html)

Understand how your queries are executed and optimized in Aurora DSQL using explain plans.

- [Reading EXPLAIN plans](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/reading-dsql-explain-plans.html): Learn how to interpret Aurora DSQL EXPLAIN plan output and identify optimization opportunities.
- [DPUs in EXPLAIN ANALYZE](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/understanding-dpus-explain-analyze.html): Aurora DSQL provides statement-level Distributed Processing Unit (DPU) information in EXPLAIN ANALYZE VERBOSE plan output, giving you deeper visibility into query cost during development.


## [Managing Aurora DSQL clusters](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/setting-up-dsql.html)

### [Single-Region clusters](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/configuring-single-region-clusters.html)

Learn how to manage your clusters using the AWS SDKs and AWS CLI.

- [Using AWS SDKs](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/single-region-aws-sdks.html): The AWS SDKs provide programmatic access to Aurora DSQL in your preferred programming language.
- [Using AWS CLI](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/single-region-aws-cli.html): The AWS CLI provides a command-line interface for managing your Aurora DSQL clusters.

### [Multi-Region clusters](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/configuring-multi-region-clusters.html)

Learn how to work with clusters that span multiple AWS Regions.

- [Using AWS SDKs](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/multi-region-aws-sdks.html): The AWS SDKs provide programmatic access to Aurora DSQL in your preferred programming language.
- [Using AWS CLI](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/multi-region-aws-cli.html): Learn how to create and manage multi-Region clusters using the AWS CLI.
- [CloudFormation](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/mr-cluster-setup.html): Learn how to set up and configure Aurora DSQL clusters using AWS CloudFormation.
- [Aurora DSQL Cluster lifecycle](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cluster-lifecycle.html): Learn about Amazon Aurora DSQL cluster lifecycle, including cluster status and scale to zero functionality.


## [Programming with Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/programming-with.html)

### [Connectors](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_connectors.html)

Aurora DSQL provides specialized connectors that extend existing database drivers to enable seamless IAM authentication and integration with AWS services.

- [JDBC connector](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_program-with-jdbc-connector.html): The Aurora DSQL Connector for JDBC is designed as an authentication plugin that extends the functionality of the PostgreSQL JDBC driver to enable applications to authenticate with Aurora DSQL using IAM credentials.
- [Python connector](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_program-with-dsql-connector-for-python.html): The Aurora DSQL Connector for Python integrates IAM Authentication for connecting Python applications to Amazon Aurora DSQL clusters.
- [Go connector](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_program-with-go-pgx-connector.html): The Aurora DSQL Connector for Go wraps pgx with automatic IAM authentication.

### [Node.js connectors](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_Node-js-connectors.html)

The Aurora DSQL Connector for node-postgres and the Aurora DSQL Connector for Postgres.js are authentication plugins that extend the functionality of the node-postgres and Postgres.js clients to enable applications to authenticate with Aurora DSQL using IAM credentials.

- [node-postgres connector](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_program-with-dsql-connector-for-node-postgres.html): The Aurora DSQL Connector for node-postgres is a Node.js connector built on node-postgres that integrates IAM Authentication for connecting JavaScript/TypeScript applications to Amazon Aurora DSQL clusters.
- [Postgres.js connector](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_program-with-dsql-connector-for-postgresjs.html): The Aurora DSQL Connector for Postgres.js is a Node.js connector built on Postgres.js that integrates IAM Authentication for connecting JavaScript applications to Amazon Aurora DSQL clusters.

### [Accessing Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/accessing.html)

Connect to Aurora DSQL clusters using PostgreSQL-compatible clients, such as AWS CloudShell, psql, DBeaver, DataGrip, with IAM authentication tokens and SSL encryption.

- [DBeaver](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/accessing-dbeaver.html): DBeaver is a universal SQL client that can be used to manage any database that has a JDBC driver.
- [JetBrains DataGrip](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/accessing-datagrip.html): JetBrains DataGrip is a cross-platform IDE for working with SQL and databases, including PostgreSQL.
- [Psql](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/accessing-psql.html)
- [VSCode](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/accessing-vscode.html): The Aurora DSQL Driver for SQLTools is a Visual Studio Code extension for Amazon Aurora DSQL that integrates with SQLTools.
- [Database Connectivity Tools](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/aws-sdks.html): Aurora DSQL is compatible with many third-party database drivers and ORM libraries.

### [Generative AI](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_generative_ai.html)

This section provides detailed instructions for how to use Generative AI tools with Aurora DSQL

- [AWS Labs Aurora DSQL MCP Server](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_aurora-dsql-mcp-server.html): An AWS Labs Model Context Protocol (MCP) server for Aurora DSQL
- [Aurora DSQL Steering: Skills and Powers](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_aurora-dsql-steering.html): This section describes how to configure AI steering for Aurora DSQL using skills and powers.
- [Query Editor](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started-query-editor.html): Connect to your Aurora DSQL clusters and run SQL queries directly from the AWS Management Console.
- [Query Editors: Using JupyterLab with Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_program-with-jupyter.html): This guide provides step-by-step instructions on how to connect and query Amazon Aurora DSQL using JupyterLab with Python.


## [Monitoring and logging](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cloudwatch-monitoring.html): Monitor Aurora DSQL using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Logging with CloudTrail](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/logging-using-cloudtrail.html): Learn about logging Amazon Aurora DSQL with AWS CloudTrail.


## [Security](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security.html)

- [AWS managed policies](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Aurora DSQL and recent changes to those policies.

### [Data protection](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Aurora DSQL.

- [SSL/TLS certificates](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/configure-root-certificates.html): Learn how to configure and verify SSL/TLS certificates for secure connections to your Aurora DSQL cluster.
- [Data encryption](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/data-encryption.html): Protect sensitive data in Aurora DSQL using AWS KMS encryption keys for data at rest and in transit.

### [Identity and access management](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Aurora DSQL resources.

- [How Aurora DSQL works with IAM](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Aurora DSQL, learn what IAM features are available to use with Aurora DSQL.
- [Identity-based policy examples](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Aurora DSQL resources.
- [Troubleshooting](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Aurora DSQL and IAM.

### [Resource-based policies](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/resource-based-policies.html)

Control access to your Aurora DSQL clusters using resource-based policies that attach directly to cluster resources.

- [Create with policies](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/rbp-create-cluster.html): Attach resource-based policies when creating a new cluster to ensure access controls are in place from the start.
- [Add and edit policies](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/rbp-attach-policy.html): Attach or modify resource-based policies for existing clusters to add or update access controls.
- [View Policy](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/rbp-view-policy.html): View resource-based policies attached to your clusters.
- [Remove Policy](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/rbp-remove-policy.html): Remove resource-based policies from clusters to change access controls.
- [Policy examples](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/rbp-examples.html): Examples of common resource-based policy patterns for controlling access to your Aurora DSQL clusters.
- [Block public access](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/rbp-block-public-access.html): Block Public Access (BPA) prevents resource-based policies from granting public access to Aurora DSQL clusters.
- [API Operations](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/rbp-api-operations.html): Aurora DSQL API operations that support or don't support resource-based policies.
- [Using a service-linked role](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-service-linked-roles.html): Aurora DSQL uses AWS Identity and Access Management (IAM) service-linked roles.
- [Using IAM condition keys](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/using-iam-condition-keys.html): When you grant permissions in Aurora DSQL you can specify conditions that determine how a permissions policy takes effect.
- [Incident response](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/incident-response.html): Security is the highest priority at AWS.
- [Compliance validation](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Aurora DSQL features for data resiliency.

### [Infrastructure Security](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/infrastructure-security.html)

Learn how Amazon Aurora DSQL isolates service traffic.

- [Managing clusters using AWS PrivateLink](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/privatelink-managing-clusters.html): Establish secure, private connections to Amazon Aurora DSQL clusters using AWS PrivateLink within your VPC, eliminating public internet exposure.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/configuration-vulnerability.html): AWS handles basic security tasks like guest operating system (OS) and database patching, firewall configuration, and disaster recovery.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.

### [Security best practices](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/best-practices-security.html)

Aurora DSQL provides a number of security features to consider as you develop and implement your own security policies.

- [Detective security best practices](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/best-practices-security-detective.html): In addition to the following ways to securely use Aurora DSQL, see Security in AWS Well-Architected Tool to learn about how cloud technologies improve your security.
- [Preventative security best practices](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/best-practices-security-preventative.html): In addition to the following ways to securely use Aurora DSQL, see Security in AWS Well-Architected Tool to learn about how cloud technologies improve your security.
