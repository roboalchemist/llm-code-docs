# Source: https://docs.datafold.com/integrations/databases/athena.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Athena

**Steps to complete:**

1. [Create an S3 bucket](/integrations/databases/athena#create-s3-bucket)
2. [Run SQL Script for permissions](/integrations/databases/athena#run-sql-script)
3. [Configure your data connection in Datafold](/integrations/databases/athena#configure-in-datafold)

### Create an S3 bucket

If you don't already have an S3 bucket for your cluster, you'll need to create one. Datafold uses this bucket to create temporary tables and store data in it. You can learn how to create an S3 bucket in AWS by referring to the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).

### Run SQL Script and Create Schema for Datafold

To connect to AWS Athena, you must generate an `AWS Access Key ID` and an `AWS Secret Access Key`. These keys provide read-only access to all tables in all schemas and write access to the Datafold-specific schema for temporary tables. If you don't have these keys yet, follow the steps outlined in the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Faccess-keys.html).

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

```
/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing witin your data warehouse. */

CREATE SCHEMA IF NOT EXISTS awsdatacatlog.datafold_tmp;
```

### Configure in Datafold

| Field Name                  | Description                                                                    |
| --------------------------- | ------------------------------------------------------------------------------ |
| AWS Access Key ID           | Your AWS Access Key, which can be found in your AWS Account.                   |
| AWS Secret Access Key       | The AWS Secret Key (generate it in your AWS account if you don't have it yet). |
| S3 Staging Directory        | The S3 bucket where table data is stored.                                      |
| AWS Region                  | The region of your Athena cluster.                                             |
| Catalog                     | The catalog, which is typically awsdatacatalog by default.                     |
| Database                    | The database or schema with tables, typically default by default.              |
| Schema for Temporary Tables | The schema (datafold\_tmp) created in our SQL script.                          |

Click **Create** to complete the setup of your data connection in Datafold.
