# Source: https://docs.mage.ai/data-integrations/destinations/iceberg_s3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Iceberg S3

> How to configure Apache Iceberg on S3 as a destination in Mage to write data to ACID-compliant Iceberg tables stored in AWS S3.

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

<ProOnly source="data-integration" />

Use **Apache Iceberg on S3** as a destination in Mage to write data to ACID-compliant Iceberg tables stored in AWS S3.

***

## Overview

This destination writes data to Apache Iceberg tables stored in AWS S3. Iceberg provides:

* **ACID Properties**: Full ACID compliance for data consistency
* **Schema Evolution**: Add, remove, or modify columns without breaking existing queries
* **Time Travel**: Query data as it was at any point in time
* **Partitioning**: Automatic partitioning for better query performance
* **Compaction**: Automatic file compaction to optimize storage

***

## Required Configuration

| Parameter               | Description          | Required | Default |
| ----------------------- | -------------------- | -------- | ------- |
| `aws_access_key_id`     | S3 access key ID     | ✅        | -       |
| `aws_secret_access_key` | S3 secret access key | ✅        | -       |
| `bucket`                | S3 bucket name       | ✅        | -       |
| `namespace`             | Iceberg namespace    | ✅        | -       |
| `table_name`            | Iceberg table name   | ✅        | -       |

***

## Optional Configuration

| Parameter    | Description | Required | Default     |
| ------------ | ----------- | -------- | ----------- |
| `aws_region` | AWS region  | ❌        | `us-west-2` |

***

## Configuration Example

```yaml  theme={"system"}
aws_access_key_id: your_access_key
aws_region: us-west-2
aws_secret_access_key: your_secret_key
bucket: your-bucket-name
namespace: your_namespace
table_name: your_table_name
```

***

## Table Structure

Iceberg tables are created with the following structure:

```
s3://bucket/namespace.db/table_name/
├── metadata/
│   ├── v1.metadata.json
│   ├── v2.metadata.json
│   └── ...
├── data/
│   ├── 00000-0-abc123.parquet
│   ├── 00001-0-def456.parquet
│   └── ...
└── snapshots/
    ├── 1234567890.avro
    └── ...
```

***

## Usage Examples

### Creating a New Table

The destination automatically creates the table if it doesn't exist, using the schema from the incoming data.

### Appending Data

New data is automatically appended to the existing Iceberg table.

### Schema Evolution

If the incoming data has new columns, the table schema is automatically updated.

***

## Troubleshooting

### Common Issues

1. **Access Denied**: Check your S3 credentials and bucket permissions
2. **Region Mismatch**: Ensure the region matches your S3 bucket configuration

### Debugging

Enable debug logging to see detailed information about table creation and data writing operations.

***

## Related Resources

* [Apache Iceberg Documentation](https://iceberg.apache.org/docs/)
* [Iceberg S3 Configuration](https://iceberg.apache.org/docs/latest/aws/)
* [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)


Built with [Mintlify](https://mintlify.com).