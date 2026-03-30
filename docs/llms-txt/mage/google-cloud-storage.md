# Source: https://docs.mage.ai/guides/streaming/destinations/google-cloud-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Cloud Storage

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
connector_type: google_cloud_storage
bucket: bucket
prefix: prefix
file_type: parquet
buffer_size_mb: 5
buffer_timeout_seconds: 300
path_to_credentials_json_file: /path/to/your/service/account/key.json
```

* `bucket`: The Google Cloud Storage bucket you want to use to store the data.
* `prefix`: The Google Cloud Storage path prefix. The whole GCS path will be `gs://{bucket}/{prefix}`.
* `file_type`: `parquet`, `csv`, or `delta` (for Delta Lake tables)
* `buffer_size_mb` and `buffer_timeout_seconds`: Mage puts messages in a buffer before uploading to Google Cloud Storage.
  You can configure the size and timeout of the buffer to control the file size and the delay.
* `path_to_credentials_json_file`: Google service account credential json file. If Mage is running on GCP, you can leave this value null and then Mage will use the instance service account to authenticate. See [Referencing Variables](/development/variables/referencing-variables) for configuring credentials via environment variables or secret variables.

## Configure time-based partition

```yaml  theme={"system"}
date_partition_format: "%Y%m%dT%H"
```

If you want to store the Google Cloud Storage data in time-based partition folders. You can add `date_partition_format`
to the config. Example values: `%Y%m%d`, `%Y%m%dT%H`.

## Delta Lake configuration

**Note:** Delta Lake format (`file_type: delta`) is a Mage Pro only feature.

<ProOnly source="gcs-deltalake" />

When using `file_type: delta`, you can write data to Delta Lake tables in Google Cloud Storage.

```yaml  theme={"system"}
connector_type: google_cloud_storage
bucket: my-bucket
prefix: my-prefix
file_type: delta
table_uri: gs://my-bucket/path/to/delta-table  # Optional: if not provided, constructed from bucket/prefix
mode: append  # 'append' or 'overwrite'
buffer_size_mb: 5
buffer_timeout_seconds: 300
path_to_credentials_json_file: /path/to/your/service/account/key.json
```

* `table_uri`: (Optional) Full URI for the Delta Lake table (e.g., `gs://bucket/path/to/table`). If not provided, the URI will be automatically constructed from `bucket` and `prefix`.
* `mode`: Write mode for Delta Lake tables. Valid values:
  * `append`: Adds new rows to the existing table (default)
  * `overwrite`: Replaces all existing rows in the table

**Note:** When using Delta Lake format, time-based partitioning (`date_partition_format`) is not applied as Delta Lake manages its own internal file structure.

**Security Note:** Storing credentials in configuration files can be insecure. Prefer using environment variables (e.g., `GOOGLE_APPLICATION_CREDENTIALS`) or secret variables when possible, especially for production deployments. See [Referencing Variables](/development/variables/referencing-variables) for configuring credentials via environment variables or secret variables.


Built with [Mintlify](https://mintlify.com).