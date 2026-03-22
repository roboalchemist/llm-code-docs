# Source: https://docs.mage.ai/guides/streaming/destinations/redshift.md

# Source: https://docs.mage.ai/data-integrations/sources/redshift.md

# Source: https://docs.mage.ai/data-integrations/destinations/redshift.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Redshift

> How to configure Amazon Redshift as a destination in Mage to write data into Redshift tables using user credentials or IAM-based authentication.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

![Amazon Redshift Logo](https://user-images.githubusercontent.com/78053898/198753538-2d606c3a-f6b0-472a-b0b3-c16086f256fc.png)

***

## Overview

Use **Amazon Redshift** as a destination in Mage to export pipeline data into a highly scalable, cloud-based data warehouse. Mage supports both **standard username/password authentication** and **IAM database authentication** using AWS access keys.

Mage will automatically create and write to the specified table, with support for optional schema management and merge-based updates.

***

## Configuration Parameters

You must provide the following credentials when configuring Redshift as a destination:

| Key              | Description                                                                                                                                          | Example Value                                  | Required             |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------- |
| `database`       | Name of the Redshift database where data will be written.                                                                                            | `demo`                                         | ✅                    |
| `host`           | Hostname of the Redshift cluster endpoint.                                                                                                           | `mage-prod.3.us-west-2.redshift.amazonaws.com` | ✅                    |
| `port`           | Redshift port (default is `5439`).                                                                                                                   | `5439`                                         | ✅                    |
| `user`           | Redshift username with access to the database and schema.                                                                                            | `awsuser`                                      | ✅ (if not using IAM) |
| `password`       | Password for the Redshift user.                                                                                                                      | `abc123...`                                    | ✅ (if not using IAM) |
| `schema`         | Schema within the database where the table will be created or written to.                                                                            | `public`                                       | ✅                    |
| `table`          | Name of the destination table to store data from your pipeline.                                                                                      | `dim_users_v1`                                 | ✅                    |
| `region`         | AWS region where the Redshift cluster is hosted.                                                                                                     | `us-west-2`                                    | ✅                    |
| `use_merge_load` | If `true`, Mage will attempt to merge incoming data with existing records (UPSERT-like behavior).                                                    | `false` *(default)*                            | ❌                    |
| `use_s3_copy`    | If `true`, Mage will upload data to S3 and load into Redshift using the COPY command (Pro feature).                                                  | `false` *(default)*                            | ❌                    |
| `type_mapping`   | Custom mapping to override default column type conversions. Useful for specifying custom Redshift data types like SUPER for JSON data (Pro feature). | see below                                      | ❌ (Pro)              |

> **Note**: `use_s3_copy` and `type_mapping` are Mage **Pro-only** features. `use_s3_copy` enables faster bulk loads via S3 and supports IAM roles or access key authentication.

***

## IAM-Based Authentication (Alternative to User/Password)

If you prefer to use **IAM credentials** instead of traditional authentication, you can use the following fields:

| Key                  | Description                                                              | Example Value | Required (if using IAM) |
| -------------------- | ------------------------------------------------------------------------ | ------------- | ----------------------- |
| `access_key_id`      | AWS access key ID for an IAM user or role with Redshift database access. | `AKIA...`     | ✅                       |
| `secret_access_key`  | AWS secret access key corresponding to the above access key ID.          | `xyz123...`   | ✅                       |
| `cluster_identifier` | Identifier of the Amazon Redshift cluster.                               | `mage-prod`   | ✅                       |
| `db_user`            | IAM-authenticated Redshift user.                                         | `admin`       | ✅                       |

***

## S3 Configuration (Required if `use_s3_copy` is true)

<ProOnly source="redshift" />

| Key                     | Description                                                         | Required                  | Sample Value                                    |
| ----------------------- | ------------------------------------------------------------------- | ------------------------- | ----------------------------------------------- |
| `aws_access_key_id`     | AWS access key for uploading data to S3. Ignored if using IAM role. | ✅ (unless using IAM role) | `AKIA...`                                       |
| `aws_secret_access_key` | AWS secret key for uploading data to S3. Ignored if using IAM role. | ✅ (unless using IAM role) | `xyz...`                                        |
| `aws_region`            | Region where the S3 bucket is located.                              | ✅                         | `us-west-2`                                     |
| `bucket`                | S3 bucket to temporarily stage Parquet files for Redshift COPY.     | ✅                         | `mage-feature-sets`                             |
| `redshift_iam_role`     | IAM role ARN with S3 read access attached to your Redshift cluster. | Optional                  | `arn:aws:iam::123456789012:role/MyRedshiftRole` |

Configure these inside a nested `s3_creds` config object:

```yaml  theme={"system"}
use_s3_copy: true
s3_creds:
  aws_access_key_id: AKIA...
  aws_secret_access_key: xyz...
  aws_region: us-west-2
  bucket: mage-feature-sets
  redshift_iam_role: arn:aws:iam::123456789012:role/MyRedshiftRole
```

***

## Type Mapping

<ProOnly source="redshift" />

The `type_mapping` configuration allows you to override default column type conversions. This is useful for advanced cases like storing JSON in Redshift’s `SUPER` type or adjusting column widths.

### Example Configuration

**YAML Format:**

```yaml  theme={"system"}
type_mapping:
  object: SUPER
  array: SUPER
  string: VARCHAR(1000)
```

**Complete YAML Example:**

```yaml  theme={"system"}
database: demo
host: mage-prod.3.us-west-2.redshift.amazonaws.com
password: abc123...
port: 5439
region: us-west-2
schema: public
user: awsuser
use_merge_load: false
use_s3_copy: false
lower_case: true
type_mapping:
  object: SUPER
  array: SUPER
  string: VARCHAR(1000)
  datetime: TIMESTAMPTZ
  number: BIGINT
```

### Supported Overrides

* **`object`** → Redshift type for JSON objects (e.g., `SUPER`)
* **`array`** → Redshift type for JSON arrays (e.g., `SUPER`)
* **`string`** → Custom VARCHAR or other string type
* **`datetime`** → Custom timestamp type (e.g., `TIMESTAMPTZ`)
* **`number`** → Custom numeric type (e.g., `BIGINT`)

> When using `SUPER`, Mage automatically applies `JSON_PARSE()` for correct Redshift insertion.

***

## Optional Parameters

| Key                    | Description                                                                                                                                                     | Example Value |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `skip_schema_creation` | If `true`, Mage will skip running the `CREATE SCHEMA` command. Useful if the schema already exists. [See issue](https://github.com/mage-ai/mage-ai/issues/3416) | `true`        |
| `lower_case`           | If `true`, Mage will automatically convert column names to lowercase. Default is `true`.                                                                        | `true`        |

***

## Grant Permissions

To allow Mage to create schemas and insert data, grant the following permissions to your Redshift user or IAM role:

```sql  theme={"system"}
GRANT CREATE ON DATABASE your_database TO your_user;
GRANT CREATE ON ALL TABLES IN SCHEMA your_schema TO your_user;
```

Refer to the [Redshift GRANT command documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT.html) for details.

***

## Related Resources

* [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)
* [Redshift IAM Database Authentication](https://docs.aws.amazon.com/redshift/latest/mgmt/guid-iam-db-authentication.html)
* [Redshift SQL GRANT Syntax](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT.html)
* [Redshift JDBC and ODBC Drivers](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html)


Built with [Mintlify](https://mintlify.com).