# Source: https://docs.prefect.io/integrations/prefect-gcp/api-ref/prefect_gcp-experimental-bundles-upload.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# upload

# `prefect_gcp.experimental.bundles.upload`

## Functions

### `upload_bundle_to_gcs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-gcp/prefect_gcp/experimental/bundles/upload.py#L23" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
upload_bundle_to_gcs(local_filepath: Path, bucket: str, key: str, gcp_credentials_block_name: str | None = None) -> UploadBundleToGcsOutput
```

Uploads a bundle file to a GCS bucket.

**Args:**

* `local_filepath`: The path to the bundle file to upload.
* `bucket`: The name of the GCS bucket to upload the bundle to.
* `key`: The key (path) to upload the bundle to in the GCS bucket.
* `gcp_credentials_block_name`: The name of the GCP credentials block to use.

**Returns:**

* A dictionary containing the bucket and key of the uploaded bundle.

## Classes

### `UploadBundleToGcsOutput` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-gcp/prefect_gcp/experimental/bundles/upload.py#L14" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

The output of the `upload_bundle_to_gcs` step.


Built with [Mintlify](https://mintlify.com).