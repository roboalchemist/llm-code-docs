# Source: https://docs.datadoghq.com/database_monitoring/guide/managed_authentication.md

---
title: Connecting with Managed Authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Database Monitoring > Database Monitoring Guides > Connecting with
  Managed Authentication
---

# Connecting with Managed Authentication

This guide assumes that you have configured [Database Monitoring](https://docs.datadoghq.com/database_monitoring/#getting-started).

[Datadog Database Monitoring (DBM)](https://docs.datadoghq.com/database_monitoring) allows you to view explain plans and query samples running on your database hosts. This guide shows you how to use cloud managed authentication features, such as IAM, to connect the Agent to your database. This provides a more secure way to authenticate and saves you from having to manage database credentials across your agent hosts.

## Before you begin{% #before-you-begin %}

{% dl %}

{% dt %}
Supported databases
{% /dt %}

{% dd %}
Postgres, MySQL, SQL Server
{% /dd %}

{% /dl %}

Supported authentication types and Agent versions :

| Authentication Type                                                                                                                   | Agent Version | Postgres | MySQL | SQL Server |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------- | ----- | ---------- |
| [IAM](https://repost.aws/knowledge-center/rds-postgresql-connect-using-iam)                                                           |
| 7.46                                                                                                                                  | yes           |
| 7.67                                                                                                                                  | yes           |
| [Microsoft Entra ID Managed Identity](https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview) |
| 7.48                                                                                                                                  | yes           | yes      |

## Configure IAM authentication{% #configure-iam-authentication %}

AWS supports IAM authentication to RDS and Aurora databases. Starting with Datadog Agent version 7.57, cross-account IAM authentication is supported for RDS and Aurora databases. In order to configure the Agent to connect using IAM, follow the steps to complete the setup for the database and the Datadog Agent.

### Enable IAM authentication for your database{% #enable-iam-authentication-for-your-database %}

1. Turn on IAM authentication on your [RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Enabling.html) or [Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Enabling.html) instance.
1. Create an IAM policy for DB authentication. Replace `<YOUR_IAM_AUTH_DB_USER>` with the local database user in the IAM policy document:
   {% tab title="RDS" %}
   
   ```json
   {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "rds-db:connect"
              ],
              "Resource": [
                  "arn:aws:rds-db:REGION:ACCOUNT:dbuser:db-<RESOURCE_ID>/<YOUR_IAM_AUTH_DB_USER>"
              ]
          }
      ]
   }
   ```

For example, if you want to use the `datadog` user, use the following resource ARN:

   ```json
   {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "rds-db:connect"
              ],
              "Resource": [
                  "arn:aws:rds-db:REGION:ACCOUNT:dbuser:db-<RESOURCE_ID>/datadog"
              ]
          }
      ]
   }
   ```

      {% /tab %}

   {% tab title="Aurora" %}
   
   ```json
   {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "rds-db:connect"
              ],
              "Resource": [
                  "arn:aws:rds-db:REGION:ACCOUNT:dbuser:cluster-<RESOURCE_ID>/<YOUR_IAM_AUTH_DB_USER>"
              ]
          }
      ]
   }
   ```

For example, if you wanted to use the `datadog` user, you would use the following resource ARN:

   ```json
   {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "rds-db:connect"
              ],
              "Resource": [
                  "arn:aws:rds-db:REGION:ACCOUNT:dbuser:cluster-<RESOURCE_ID>/datadog"
              ]
          }
      ]
   }
   ```

      {% /tab %}

AWS also supports wildcards for specifying the resource, for example if you wanted to allow the `datadog` user to authenticate across all instances for an account add the following:

```json
  "Resource": [
    "arn:aws:rds-db:*:ACCOUNT:dbuser:cluster-*/datadog",
    "arn:aws:rds-db:*:ACCOUNT:dbuser:db-*/datadog"
  ],
```
Log in to your database instance as the root user, and create an IAM authenticated [role](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.html#UsingWithRDS.IAMDBAuth.DBAccounts.PostgreSQL):
{% tab title="Postgres" %}

```tsql
CREATE USER <YOUR_IAM_ROLE> WITH LOGIN;
GRANT rds_iam TO <YOUR_IAM_ROLE>;
```

For example, for the `datadog` user you would run:

```tsql
CREATE USER datadog WITH LOGIN;
GRANT rds_iam TO datadog;
```

{% /tab %}

{% tab title="MySQL" %}

```tsql
CREATE USER <YOUR_IAM_ROLE> IDENTIFIED WITH AWSAuthenticationPlugin AS 'RDS';
ALTER USER <YOUR_IAM_ROLE>@'%' REQUIRE SSL;
```

For example, for the `datadog` user you would run:

```tsql
CREATE USER 'datadog' IDENTIFIED WITH AWSAuthenticationPlugin AS 'RDS';
ALTER USER 'datadog'@'%' REQUIRE SSL;
```

{% /tab %}

**Note:** this has to be a new user created without a password, or IAM authentication will fail.
Complete the Agent setup steps for your RDS ([Postgres](https://docs.datadoghq.com/database_monitoring/setup_postgres/rds/#grant-the-agent-access), [MySQL](https://docs.datadoghq.com/database_monitoring/setup_mysql/rds/#grant-the-agent-access)) or Aurora ([Postgres](https://docs.datadoghq.com/database_monitoring/setup_postgres/aurora/#grant-the-agent-access), [MySQL](https://docs.datadoghq.com/database_monitoring/setup_mysql/aurora/#grant-the-agent-access)) instance.
### Enable IAM authentication for the Agent host in the same AWS account as the RDS instance{% #enable-iam-authentication-for-the-agent-host-in-the-same-aws-account-as-the-rds-instance %}

{% tab title="EC2" %}

1. Create an IAM role and attach the IAM policy created for DB authentication to the role.

```bash
# Create an IAM role for EC2 instance
# Replace `<YOUR_IAM_AUTH_DB_ROLE>` with the name of the IAM role
aws iam create-role --role-name <YOUR_IAM_AUTH_DB_ROLE> --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'

# Attach the IAM policy to the IAM role
# Replace `<YOUR_IAM_AUTH_DB_POLICY_ARN>` with the ARN of the IAM policy from step 2
aws iam attach-role-policy --role-name <YOUR_IAM_AUTH_DB_ROLE> --policy-arn <YOUR_IAM_AUTH_DB_POLICY_ARN>
```

Attach the IAM role to the EC2 instance where the Agent is running. For more information, see [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html).
{% /tab %}

{% tab title="ECS Fargate" %}

1. Create an IAM role and attach the IAM policy created for DB authentication to the role.

```bash
# Create an IAM role for ECS task
# Replace `<YOUR_IAM_AUTH_DB_ROLE>` with the name of the IAM role
aws iam create-role --role-name <YOUR_IAM_AUTH_DB_ROLE> --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'

# Attach the IAM policy to the IAM role
# Replace `<YOUR_IAM_AUTH_DB_POLICY_ARN>` with the ARN of the IAM policy from step 2
aws iam attach-role-policy --role-name <YOUR_IAM_AUTH_DB_ROLE> --policy-arn <YOUR_IAM_AUTH_DB_POLICY_ARN>
```

In the ECS task definition, attach the IAM role to the task role where the Agent container is defined. For more information, see [IAM roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).
{% /tab %}

{% tab title="EKS" %}

1. Create an IAM role and attach the IAM policy created for DB authentication to the role.

```bash
# Create an IAM OIDC provider for your cluster
# Replace `<YOUR_ESK_REGION>` and `<YOUR_ESK_CLUSTER>` with the region and name of your ESK cluster
$ eksctl utils associate-iam-oidc-provider \
  --region=<YOUR_ESK_REGION> \
  --cluster=<YOUR_ESK_CLUSTER> \
  --approve

# Create a service account
# Replace `<YOUR_IAM_AUTH_DB_POLICY_ARN>` with the ARN of the IAM policy from step 2
# Replace `<YOUR_IAM_AUTH_SERVICE_ACCOUNT>` and `<YOUR_IAM_AUTH_SERVICE_ACCOUNT_NAMESPACE>` with the name and namespace of the service account
$ eksctl create iamserviceaccount \
  --cluster <YOUR_ESK_CLUSTER> \
  --name <YOUR_IAM_AUTH_SERVICE_ACCOUNT> \
  --namespace <YOUR_IAM_AUTH_SERVICE_ACCOUNT_NAMESPACE> \
  --attach-policy-arn <YOUR_IAM_AUTH_DB_POLICY_ARN> \
  --override-existing-serviceaccounts \
  --approve
```

Map the IAM role to the Kubernetes service account where the Agent is running. For more information, see [IAM roles for Amazon EKS service account](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).
{% /tab %}
Update your Postgres or MySQL instance config with an `aws` block specifying the `region` of the RDS instance, and set `managed_authentication.enabled` to `true`:
```yaml
instances:
  - host: example-endpoint.us-east-2.rds.amazonaws.com
    port: 5432
    username: datadog
    dbm: true
    aws:
      instance_endpoint: example-endpoint.us-east-2.rds.amazonaws.com
      region: us-east-2
      managed_authentication:
        enabled: true
```

### Enable IAM authentication for the Agent host in a different AWS account than the RDS instance{% #enable-iam-authentication-for-the-agent-host-in-a-different-aws-account-than-the-rds-instance %}

**NOTE: Cross-account IAM authentication is supported starting from Agent version 7.57.**

{% tab title="EC2" %}

1. Create an IAM role in the account where the RDS instance is located, and attach the IAM policy created for DB authentication to the role using the example below.
   - Replace `<YOUR_IAM_AUTH_DB_ROLE>` with the name of the IAM role
   - Replace `<YOUR_AWS_ACCOUNT_FOR_AGENT>` with the AWS account ID where the Agent is running
   - Replace `<YOUR_AGENT_EC2_ROLE>` with the IAM role of the EC2 instance where the Agent is running
   - Replace `<YOUR_IAM_AUTH_DB_POLICY_ARN>` with the ARN of the IAM policy created for DB authentication

```bash
aws iam create-role --role-name <YOUR_IAM_AUTH_DB_ROLE> --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<YOUR_AWS_ACCOUNT_FOR_AGENT>:role/<YOUR_AGENT_EC2_ROLE>"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'

aws iam attach-role-policy --role-name <YOUR_IAM_AUTH_DB_ROLE> --policy-arn <YOUR_IAM_AUTH_DB_POLICY_ARN>
```
Modify the IAM role permission policies of the EC2 instance where the Agent is running, to allow assuming the IAM role created in the previous step.
- Replace `<YOUR_AGENT_EC2_ROLE>` with the IAM role of the EC2 instance where the Agent is running
- Replace `<YOUR_IAM_AUTH_DB_ROLE>` with the name of the IAM role created for DB authentication
- Replace `<YOUR_AWS_ACCOUNT_FOR_DB>` with the AWS account ID where the RDS instance is located

```bash
aws iam update-assume-role-policy --role-name <YOUR_AGENT_EC2_ROLE> --policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<YOUR_AWS_ACCOUNT_FOR_DB>:role/<YOUR_IAM_AUTH_DB_ROLE>"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'
```

{% /tab %}

{% tab title="ECS Fargate" %}

1. Create an IAM role in the account where the RDS instance is located, and attach the IAM policy created for DB authentication to the role using the example below.
   - Replace `<YOUR_IAM_AUTH_DB_ROLE>` with the name of the IAM role created for DB authentication
   - Replace `<YOUR_AWS_ACCOUNT_FOR_AGENT>` with the AWS account ID where the Agent is running
   - Replace `<YOUR_AGENT_ECS_ROLE>` with the IAM role of the ECS task where the Agent is running
   - Replace `<YOUR_IAM_AUTH_DB_POLICY_ARN>` with the ARN of the IAM policy created for DB authentication

```bash
aws iam create-role --role-name <YOUR_IAM_AUTH_DB_ROLE> --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<YOUR_AWS_ACCOUNT_FOR_AGENT>:role/<YOUR_AGENT_ECS_ROLE>"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'

aws iam attach-role-policy --role-name <YOUR_IAM_AUTH_DB_ROLE> --policy-arn <YOUR_IAM_AUTH_DB_POLICY_ARN>
```
Modify the IAM role permission policies of the ECS task where the Agent is running to allow the agent to assume the IAM role created in the previous step.
- Replace `<YOUR_AGENT_ECS_ROLE>` with the IAM role of the ECS task where the Agent is running
- Replace `<YOUR_IAM_AUTH_DB_ROLE>` with the name of the IAM role
- Replace `<YOUR_AWS_ACCOUNT_FOR_DB>` with the AWS account ID where the RDS instance is located

```bash
aws iam update-assume-role-policy --role-name <YOUR_AGENT_ECS_ROLE> --policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<YOUR_AWS_ACCOUNT_FOR_DB>:role/<YOUR_IAM_AUTH_DB_ROLE>"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'
```

{% /tab %}

{% tab title="EKS" %}

1. Create an IAM role in the account where the RDS instance is located, and attach the IAM policy created for DB authentication to the role using the example below.
   - Replace `<YOUR_IAM_AUTH_DB_ROLE>` with the name of the IAM role
   - Replace `<YOUR_AWS_ACCOUNT_FOR_AGENT>` with the AWS account ID where the Agent is running
   - Replace `<YOUR_AGENT_EKS_ROLE>` with the IAM role to be used by the EKS pods where the Agent is running
   - Replace `<YOUR_IAM_AUTH_DB_POLICY_ARN>` with the ARN of the IAM policy created for DB authentication

```bash
aws iam create-role --role-name <YOUR_IAM_AUTH_DB_ROLE> --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<YOUR_AWS_ACCOUNT_FOR_AGENT>:role/<YOUR_AGENT_EKS_ROLE>"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'

aws iam attach-role-policy --role-name <YOUR_IAM_AUTH_DB_ROLE> --policy-arn <YOUR_IAM_AUTH_DB_POLICY_ARN>
```
Modify the IAM role for the EKS Service Account where the Agent is running to allow assuming the IAM role created in the previous step.
- Replace `<YOUR_AGENT_EKS_ROLE>` with the EKS Service Account IAM role the Agent is using
- Replace `<YOUR_IAM_AUTH_DB_ROLE>` with the name of the IAM role
- Replace `<YOUR_AWS_ACCOUNT_FOR_DB>` with the AWS account ID where the RDS instance is located

```bash
aws iam update-assume-role-policy --role-name <YOUR_AGENT_EKS_ROLE> --policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<YOUR_AWS_ACCOUNT_FOR_DB>:role/<YOUR_IAM_AUTH_DB_ROLE>"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'
```
Create an IAM OIDC provider for your cluster and a service account for the Agent using the example below.
- Replace `<YOUR_EKS_REGION>` and `<YOUR_EKS_CLUSTER>` with the region and name of your EKS cluster
- Replace `<YOUR_IAM_AUTH_DB_POLICY_ARN>` with the ARN of the IAM policy created for DB authentication
- Replace `<YOUR_IAM_AUTH_SERVICE_ACCOUNT>` and `<YOUR_IAM_AUTH_SERVICE_ACCOUNT_NAMESPACE>` with the name and namespace of the service account
- Replace `<YOUR_AGENT_EKS_ROLE>` with the IAM role to be used by the EKS pods where the Agent is running

```bash
$ eksctl utils associate-iam-oidc-provider \
  --region <YOUR_EKS_REGION> \
  --cluster <YOUR_EKS_CLUSTER> \
  --approve

$ eksctl create iamserviceaccount \
  --cluster <YOUR_EKS_CLUSTER> \
  --name <YOUR_IAM_AUTH_SERVICE_ACCOUNT> \
  --namespace <YOUR_IAM_AUTH_SERVICE_ACCOUNT_NAMESPACE> \
  --role-name arn:aws:iam::<YOUR_AWS_ACCOUNT_FOR_AGENT>:role/<YOUR_AGENT_EKS_ROLE> \
  --override-existing-serviceaccounts \
  --approve
```

{% /tab %}

Update your Postgres or MySQL instance config with an `aws` block as shown below:

- Specify the `region` of the RDS instance
- Set `managed_authentication.enabled` to `true`
- Specify the role ARN, replacing `<YOUR_AWS_ACCOUNT_FOR_DB>` with the AWS account ID where the RDS instance is located, and `<YOUR_IAM_AUTH_DB_ROLE>` with the name of the IAM role created in step 1

```yaml
instances:
  - host: example-endpoint.us-east-2.rds.amazonaws.com
    port: 5432
    username: datadog
    dbm: true
    aws:
      instance_endpoint: example-endpoint.us-east-2.rds.amazonaws.com
      region: us-east-2
      managed_authentication:
        enabled: true
        role_arn: arn:aws:iam::<YOUR_AWS_ACCOUNT_FOR_DB>:role/<YOUR_IAM_AUTH_DB_ROLE>
```

## Configure Microsoft Entra ID managed identity authentication{% #configure-microsoft-entra-id-managed-identity-authentication %}

Azure allows users to configure managed identity authentication for any resource that can access [Microsoft Entra ID](https://learn.microsoft.com/azure/active-directory/fundamentals/whatis), formerly Azure Active Directory. The Datadog Agent supports [user-assigned](https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview#managed-identity-types) managed identity authentication to your cloud databases.

### Connect to PostgreSQL{% #connect-to-postgresql %}

In order to configure authentication to your PostgreSQL Flexible or Single Server instance, do the following:

1. Create your [managed identity](https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities?pivots=identity-mi-methods-azp#create-a-user-assigned-managed-identity) in the Azure portal, and assign it to your Azure Virtual Machine where the agent is deployed.
1. Configure a [Microsoft Entra ID admin user](https://learn.microsoft.com/azure/postgresql/single-server/how-to-configure-sign-in-azure-ad-authentication) on your PostgreSQL instance.
1. Connect to your PostgreSQL instance as the [Microsoft Entra ID admin user](https://learn.microsoft.com/azure/postgresql/flexible-server/how-to-configure-sign-in-azure-ad-authentication#authenticate-with-azure-ad), and run the following command:

```tsql
select * from pgaadauth_create_principal('<IDENTITY_NAME>', false, false);
```
Proceed with the normal [Agent setup steps](https://docs.datadoghq.com/database_monitoring/setup_postgres/azure/#grant-the-agent-access) for Azure. For example:
Create the following schema **in every database**:

```tsql
CREATE SCHEMA datadog;
GRANT USAGE ON SCHEMA datadog TO "<IDENTITY_NAME>";
GRANT USAGE ON SCHEMA public TO "<IDENTITY_NAME>";
GRANT pg_monitor TO datadog;
```

Create the function **in every database** to enable the Agent to collect explain plans.

```tsql
CREATE OR REPLACE FUNCTION datadog.explain_statement(
   l_query TEXT,
   OUT explain JSON
)
RETURNS SETOF JSON AS
$$
DECLARE
curs REFCURSOR;
plan JSON;

BEGIN
   SET TRANSACTION READ ONLY;

   OPEN curs FOR EXECUTE pg_catalog.concat('EXPLAIN (FORMAT JSON) ', l_query);
   FETCH curs INTO plan;
   CLOSE curs;
   RETURN QUERY SELECT plan;
END;
$$
LANGUAGE 'plpgsql'
RETURNS NULL ON NULL INPUT
SECURITY DEFINER;
```
Configure your instance config with the `azure.managed_authentication` YAML block, where the `CLIENT_ID` is the Client ID of the Managed Identity:
```yaml
instances:
  - host: example-flex-server.postgres.database.azure.com
    dbm: true
    username: "<IDENTITY_NAME>"
    ssl: "require"
    azure:
      deployment_type: flexible_server
      fully_qualified_domain_name: example-flex-server.postgres.database.azure.com
      managed_authentication:
        enabled: true
        client_id: "<CLIENT_ID>"
        # Optionally set the scope from where to request the identity token
        identity_scope: "https://ossrdbms-aad.database.windows.net/.default"
```

### Connect to SQL Server{% #connect-to-sql-server %}

In order to configure authentication to your Azure SQL DB or Azure Managed Instance, do the following:

1. Create your [managed identity](https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities?pivots=identity-mi-methods-azp#create-a-user-assigned-managed-identity) in the Azure portal, and assign it to your Azure Virtual Machine where the agent is deployed.
1. Configure a [Microsoft Entra ID admin user](https://learn.microsoft.com/azure/azure-sql/database/authentication-aad-configure?view=azuresql&tabs=azure-powershell#provision-azure-ad-admin-sql-managed-instance) on your SQL Server instance.
1. Connect to your SQL Server instance as the Microsoft Entra ID admin user, and run the following command in the `master` database:

```tsql
CREATE LOGIN <MANAGED_IDENTITY_NAME> FROM EXTERNAL PROVIDER;
```
Proceed with the normal Agent setup steps, for Azure. For example, for [Azure Managed Instance](https://docs.datadoghq.com/database_monitoring/setup_sql_server/azure/?tab=azuresqlmanagedinstance):
```tsql
CREATE USER <MANAGED_IDENTITY_NAME> FOR LOGIN <MANAGED_IDENTITY_NAME>;
GRANT CONNECT ANY DATABASE to <MANAGED_IDENTITY_NAME>;
GRANT VIEW SERVER STATE to <MANAGED_IDENTITY_NAME>;
GRANT VIEW ANY DEFINITION to <MANAGED_IDENTITY_NAME>;
GO
```

If you are using [Azure SQL DB](https://docs.datadoghq.com/database_monitoring/setup_sql_server/azure/?tab=azuresqldatabase), run the following from the `master` database:

```tsql
CREATE LOGIN <MANAGED_IDENTITY_NAME> FROM EXTERNAL PROVIDER;
CREATE USER datadog FOR LOGIN <MANAGED_IDENTITY_NAME>;
ALTER SERVER ROLE ##MS_ServerStateReader## ADD MEMBER <MANAGED_IDENTITY_NAME>;
ALTER SERVER ROLE ##MS_DefinitionReader## ADD MEMBER <MANAGED_IDENTITY_NAME>;
```

And then create the user **in every database**:

```tsql
CREATE USER <DBM_DATADOG_TEST_IDENTITY> FOR LOGIN <DBM_DATADOG_TEST_IDENTITY>;
```
Update your instance config with the `managed_identity` config block:
**Note**: [ODBC Driver 17 for SQL Server](https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16) or greater is required to use this feature.

```yaml
instances:
 - host: "example.cfcc2366ab90.database.windows.net,1433"
   connector: "odbc"
   driver: "{ODBC Driver 18 for SQL Server}"
   dbm: true
   connection_string: "TrustServerCertificate=no;Encrypt=yes;"
   managed_identity:
     client_id: "<CLIENT_ID>"
   azure:
     deployment_type: managed_instance
     fully_qualified_domain_name: example.cfcc2366ab90.database.windows.net
```
