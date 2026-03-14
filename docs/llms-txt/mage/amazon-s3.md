# Source: https://docs.mage.ai/guides/streaming/destinations/amazon-s3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon S3

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

## Basic config

```yaml  theme={"system"}
connector_type: amazon_s3
bucket: bucket
prefix: prefix
file_type: parquet
buffer_size_mb: 5
buffer_timeout_seconds: 300
```

* `bucket`: The S3 bucket you want to use to store the data.
* `prefix`: The S3 path prefix. The whole S3 path will be `s3://{bucket}/{prefix}`.
* `file_type`: `parquet`, `csv`, or `delta` (for Delta Lake tables)
* `buffer_size_mb` and `buffer_timeout_seconds`: Mage puts messages in a buffer before uploading to S3.
  You can configure the size and timeout of the buffer to control the file size and the delay.

You may see a `region` parameter in the default config template, it can be ignored. If you specify any valid AWS region names or null, you can still access to S3 buckets in other regions. However, if you do include the parameter value for `region`, it must be a valid region name for AWS or null so it won't error out.

## Configure time-based partition

```yaml  theme={"system"}
date_partition_format: "%Y%m%dT%H"

```

If you want to store the S3 data in time-based partition folders. You can add `date_partition_format`
to the config. Example values: `%Y%m%d`, `%Y%m%dT%H`.

## Delta Lake configuration

**Note:** Delta Lake format (`file_type: delta`) is a Mage Pro only feature.

<ProOnly source="s3-deltalake" />

When using `file_type: delta`, you can write data to Delta Lake tables in Amazon S3.

```yaml  theme={"system"}
connector_type: amazon_s3
bucket: my-bucket
prefix: my-prefix
file_type: delta
table_uri: s3://my-bucket/path/to/delta-table  # Optional: if not provided, constructed from bucket/prefix
mode: append  # 'append' or 'overwrite'
buffer_size_mb: 5
buffer_timeout_seconds: 300
aws_access_key_id: YOUR_ACCESS_KEY  # Optional: falls back to environment variables or IAM roles
aws_secret_access_key: YOUR_SECRET_KEY  # Optional: falls back to environment variables or IAM roles
aws_region: us-west-2  # Optional: defaults to us-west-2
```

* `table_uri`: (Optional) Full URI for the Delta Lake table (e.g., `s3://bucket/path/to/table`). If not provided, the URI will be automatically constructed from `bucket` and `prefix`.
* `mode`: Write mode for Delta Lake tables. Valid values:
  * `append`: Adds new rows to the existing table (default)
  * `overwrite`: Replaces all existing rows in the table
* `aws_access_key_id`: (Optional) AWS access key ID. If not provided, will fall back to the `AWS_ACCESS_KEY_ID` environment variable or the IAM role attached to the instance. See [Referencing Variables](/development/variables/referencing-variables) for configuring credentials via environment variables or secret variables.
* `aws_secret_access_key`: (Optional) AWS secret access key. If not provided, will fall back to the `AWS_SECRET_ACCESS_KEY` environment variable or the IAM role attached to the instance. See [Referencing Variables](/development/variables/referencing-variables) for configuring credentials via environment variables or secret variables.
* `aws_region`: (Optional) AWS region. If not provided, will fall back to the `AWS_REGION` environment variable or default to `us-west-2`.

**Note:** When using Delta Lake format, time-based partitioning (`date_partition_format`) is not applied as Delta Lake manages its own internal file structure.

## Authentication

Here are the options to authenticate with the AWS S3 bucket.

1. Add the following keys and values to your environment variables

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_REGION`

2. If you deploy Mage on AWS ECS cluster, you can use ECS execution task role to authenticate.
   You can grant the ECS task permissions to access other AWS services by attaching IAM policies
   to this ECS task execution role.

**Security Note:** Storing credentials in configuration files can be insecure. Prefer using environment variables or IAM roles when possible, especially for production deployments. See [Referencing Variables](/development/variables/referencing-variables) for configuring credentials via environment variables or secret variables.


Built with [Mintlify](https://mintlify.com).