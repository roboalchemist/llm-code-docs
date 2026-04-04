# Source: https://docs.anyscale.com/release-notes/cli-sdk.md

# Anyscale CLI and SDK release notes

[View Markdown](/release-notes/cli-sdk.md)

# Anyscale CLI and SDK release notes

This page documents changes to the Anyscale CLI and SDK, including new features, behavior changes, and bug fixes.

For installation and configuration, see [CLI configuration](/reference/quickstart-cli.md) and [Get started with the Anyscale SDK](/reference/quickstart-sdk.md).

## Version 0.26.90 release notes[​](#0-26-90 "Direct link to Version 0.26.90 release notes")

Version 0.26.90 is available as of March 9, 2026.

### New features[​](#0-26-90-features "Direct link to New features")

#### CLI[​](#cli "Direct link to CLI")

* Added `--migrate-dm-to-im` to `anyscale cloud update` to migrate eligible cloud resources deployed on Google Cloud from Deployment Manager to Infrastructure Manager.

### Bug fixes[​](#0-26-90-fixes "Direct link to Bug fixes")

* Fixes custom container image resolution for jobs, services, and workspaces for the Anyscale on Azure Private Preview. The CLI now correctly associates image records with the target cloud, resolving failures when launching workloads with external image URIs on Azure.

## Version 0.26.89 release notes[​](#0-26-89 "Direct link to Version 0.26.89 release notes")

Version 0.26.89 is available as of March 4, 2026.

### Bug fixes[​](#0-26-89-fixes "Direct link to Bug fixes")

* When the image builder is hibernated, the CLI now surfaces a clear user-facing error message.

## Version 0.26.88 release notes[​](#0-26-88 "Direct link to Version 0.26.88 release notes")

Version 0.26.88 is available as of March 2, 2026.

### Behavior changes[​](#0-26-88-changes "Direct link to Behavior changes")

#### CLI[​](#cli-1 "Direct link to CLI")

* Workspace `create`, `start`, and `update` now surface a single clear error message for compute config validation failures instead of a stack trace.
* EFS mount target verification now shows a clearer warning when a mount target exists in the expected subnet but uses a different security group, with guidance to allow inbound NFS (port 2049) from worker nodes.
* Performance improvements for `anyscale schedule list` and `anyscale schedule status`.
* Compute config validation is stricter: memory must include a unit suffix (for example, `8Gi`), empty `required_resources: {}` is rejected, and you can't combine `instance_type` with `required_resources`. Logical resources cannot exceed physical `required_resources`. Out-of-range values (for example, CPU > 512, memory > 24 TiB) are rejected with explicit errors.
* When you add labels in `required_labels` that don't affect VM instance selection, the CLI emits a warning.

#### SDK[​](#sdk "Direct link to SDK")

* Deprecated `AnyscaleSDK.get_default_cluster_environment_build()`. It now raises `AnyscaleSDKDeprecationError`. Use the image and compute config APIs instead. See [Methods removed in version 0.26.88](/archive/ref.md#02688) for migration guidance.
* Removed legacy SDK methods for jobs, schedules, and clusters. See [Methods removed in version 0.26.88](/archive/ref.md#02688).

## Version 0.26.87 release notes[​](#0-26-87 "Direct link to Version 0.26.87 release notes")

Version 0.26.87 is available as of February 19, 2026.

### Behavior changes[​](#0-26-87-changes "Direct link to Behavior changes")

#### CLI[​](#cli-2 "Direct link to CLI")

* You can now delete clouds backed by Google Cloud VMs provisioned with Infrastructure Manager as well as Deployment Manager. `anyscale cloud delete` tears down resources correctly for both provisioning paths.
* `anyscale cloud update` no longer updates the IAM external ID policy when the resulting policy matches the existing one. This avoids failures when you don't have permission to modify IAM policies.

### Bug fixes[​](#0-26-87-fixes "Direct link to Bug fixes")

* Fixed cloud deletion for AWS and Google Cloud VM stacks so that the CLI now cleans up all managed cloud resources attached to a cloud when you run `anyscale cloud delete`. Previously, some managed resources in multi-resource or multi-region setups sometimes remained.

## Version 0.26.86 release notes[​](#0-26-86 "Direct link to Version 0.26.86 release notes")

Version 0.26.86 is available as of February 17, 2026.

### Behavior changes[​](#0-26-86-changes "Direct link to Behavior changes")

#### CLI[​](#cli-3 "Direct link to CLI")

* `anyscale cloud register --skip-verifications` now works without local cloud provider credentials for VM clouds (AWS and Google Cloud). The backend looks up derived values (for example, availability zones and EFS mount targets) instead of requiring local creds.
* Google Cloud VM cloud setup and cloud resource setup now provision resources through Google Cloud Infrastructure Manager instead of Deployment Manager. You can track progress in the Google Cloud console.
* When adding VM resources to a cloud in the same region on Google Cloud, firewall policy names now use a unique deployment name to avoid conflicts. Workload Identity Federation setup no longer creates duplicate pools and returns the correct pool path.

### Bug fixes[​](#0-26-86-fixes "Direct link to Bug fixes")

* Fixed `anyscale cloud setup` for Azure after breaking changes in the Azure management package. Install the CLI with the Azure extra (`pip install anyscale[azure]`) for Azure cloud setup. Azure cloud setup no longer incorrectly requires availability zones.
* Fixed cloud resource setup bugs that could cause 409 conflicts and incorrect IAM bindings when creating multiple Google Cloud resources in the same region.

## Version 0.26.85 release notes[​](#0-26-85 "Direct link to Version 0.26.85 release notes")

Version 0.26.85 is available as of February 11, 2026.

### New features[​](#0-26-85-features "Direct link to New features")

#### SDK[​](#sdk-1 "Direct link to SDK")

* Added job connection support for third-party integrations (for example, Databricks). Use the `connections` field on `JobConfig` with `ConnectionConfig` and `IntegrationType` to associate connections with jobs for credential injection at runtime. See [Job API Reference](/reference/job-api.md).
* Schedules (cron jobs) support `connection_ids` for third-party integrations. The CLI validates connections at create time and associates them with the job when the schedule triggers.

#### CLI[​](#cli-4 "Direct link to CLI")

* Added `--connection` flag to `anyscale job submit` to associate one or more third-party connections with a job. Use `integration_type=DATABRICKS,connection_name=<name>` per connection. Supports multiple `--connection` flags.
* Added `connections` field to job submit YAML config for the same integration.
* Added `--sort` to `anyscale schedule list` for v2 schedules. Supported fields: `id`, `name`, `created_at`, `next_trigger_time`.

### Behavior changes[​](#0-26-85-changes "Direct link to Behavior changes")

#### CLI[​](#cli-5 "Direct link to CLI")

* Removed legacy `anyscale machine list` and `anyscale machine delete` commands. Customer-managed machine pools have been deprecated. See [Customer-managed on-prem machine pools (legacy)](/archive/customer-managed-machine-pools.md).

#### SDK[​](#sdk-2 "Direct link to SDK")

* Removed legacy Service SDK methods: `get_service`, `list_services`, `rollback_service`, `rollout_service`, and `terminate_service`. Use `anyscale.service.status()`, `anyscale.service.list()`, `anyscale.service.rollback()`, `anyscale.service.deploy()`, and `anyscale.service.terminate()` instead. See [Methods removed in version 0.26.85](/archive/ref.md#02685) for migration guidance.
* Removed legacy cloud SDK methods: `get_cloud`, `get_default_cloud`, and `search_clouds`. Use `anyscale.cloud.get`, `anyscale.cloud.get_default`, and `anyscale.cloud.list` instead. See [Methods removed in version 0.26.85](/archive/ref.md#02685) for migration guidance.
* Removed legacy SSO SDK methods: `partial_update_organization`, `upsert_sso_config`, and `upsert_test_sso_config`. There is no replacement in the modern SDK.
* When you submit a job without setting `max_retries`, the CLI and SDK emit a warning. The default is `1` in this release, but Anyscale plans to change the default to `0` in a later release. Set `max_retries` explicitly for consistent behavior.

#### Compute[​](#compute "Direct link to Compute")

* VM-backed clouds now reject TPU shapes with a clear error. Use a Kubernetes (GKE) cloud for TPU workloads, or use GPU resources instead.

### Bug fixes[​](#0-26-85-fixes "Direct link to Bug fixes")

* Fixed resource fetch when uploading files on Anyscale-hosted clouds where the CLI can't resolve resource ID from name; the upload flow now proceeds without requiring the resource name.

## Version 0.26.84 release notes[​](#0-26-84 "Direct link to Version 0.26.84 release notes")

Version 0.26.84 is available as of February 6, 2026.

### Bug fixes[​](#0-26-84-fixes "Direct link to Bug fixes")

* Fixes an error for cloud-isolated projects in legacy Anyscale Connect.

## Version 0.26.83 release notes[​](#0-26-83 "Direct link to Version 0.26.83 release notes")

Version 0.26.83 is available as of February 4, 2026.

### New features[​](#0-26-83-features "Direct link to New features")

#### SDK[​](#sdk-3 "Direct link to SDK")

* Added `anyscale.job.delete()` to permanently delete a job and all associated job runs. The job must be in a terminal state (`SUCCEEDED` or `FAILED`). Supports `name`, `id`, `cloud`, `project`, and `include_archived` parameters.
* Added `anyscale.job_queue.delete()` to delete a job queue. All jobs must be in terminal state with no running clusters. Supports `job_queue_id`, `name`, `project`, `cloud`, and `include_archived` parameters.
* Added `anyscale.schedule.delete()` to delete a schedule. Active schedules are automatically paused before deletion. Supports `id`, `name`, `cloud`, and `project` parameters.

#### CLI[​](#cli-6 "Direct link to CLI")

* Added `anyscale job delete` command to permanently delete a job. Supports `--name`, `--id`, `--cloud`, `--project`, and `--include-archived` options.
* Added `anyscale job-queue delete` command to delete a job queue. Supports `--name` or `--id` options.
* Added `anyscale schedule delete` command to delete a schedule. Supports `--name` or `--id` options.
* Added `--include-archived` flag to `anyscale job` commands (`status`, `terminate`, `archive`, `delete`, `wait`, `logs`, `tags add`, `tags remove`, `tags list`) to support finding archived jobs.
* Added `--include-archived` flag to `anyscale job-queue list` and `anyscale job-queue status`.
* Added `anyscale cloud update-storage-cors` command to update CORS configuration on cloud storage buckets for Anyscale UI features. Works with AWS, GCP, and Azure clouds.

### Behavior changes[​](#0-26-83-changes "Direct link to Behavior changes")

#### CLI[​](#cli-7 "Direct link to CLI")

* Removed legacy `anyscale cluster-env` commands. Use `anyscale image` commands instead.
* Removed legacy `anyscale cluster start` and `anyscale cluster terminate` commands. Use `anyscale workspace_v2` commands instead.

#### SDK[​](#sdk-4 "Direct link to SDK")

* Removed legacy SDK methods for compute config and image modules. See [Methods removed in version 0.26.83](/archive/ref.md#02683) for migration guidance.

## Version 0.26.82 release notes[​](#0-26-82 "Direct link to Version 0.26.82 release notes")

Version 0.26.82 is available as of January 27, 2026.

### New features[​](#0-26-82-features "Direct link to New features")

#### SDK[​](#sdk-5 "Direct link to SDK")

* Added `anyscale.job_queue.archive()` to archive a job queue and prevent new job submissions. Existing pending and running jobs continue to completion. Supports `job_queue_id` or `name` parameters.
* Added `anyscale.job_queue.terminate()` to terminate a job queue and all its pending and running jobs. Supports `job_queue_id` or `name` parameters.
* Added `anyscale.schedule.url()` to get the web UI URL for a schedule. Supports `id` or `name` with optional `cloud` and `project` parameters.

#### CLI[​](#cli-8 "Direct link to CLI")

* Added `anyscale job-queue archive` command to archive a job queue. Supports `--id` or `--name` options.
* Added `anyscale job-queue terminate` command to terminate a job queue. Supports `--id` or `--name` options.
* Enhanced `anyscale job list --v2` with pagination (`--page-size`, `--interactive`/`--no-interactive`), sorting (`--sort`), JSON output (`--json`), and `--max-items` limit.
* Enhanced `anyscale schedule list --v2` with pagination (`--page-size`, `--interactive`/`--no-interactive`), JSON output (`--json`), and user filtering (`--include-all-users`/`--only-mine`).
* Added `--name` option to `anyscale job-queue status` and `anyscale job-queue update` as an alternative to `--id`.
* Added `--v2` flag to `anyscale schedule url` with support for name resolution using `--name`, `--cloud`, and `--project`.

#### Compute config[​](#compute-config "Direct link to Compute config")

* Added validation for accelerator type consistency between `ray.io/accelerator-type` in `required_labels` and `cloud.google.com/gke-accelerator` in `nodeSelector`. Mismatched GPU types now produce a helpful error message.
* Added validation requiring `GPU` count in `required_resources` when specifying a non-TPU accelerator type in `required_labels`.
* Added validation requiring `tpu_hosts` in `required_resources` and `ray.io/tpu-topology` in `required_labels` when specifying a TPU accelerator type.
* CLI output for compute configs now includes `required_resources` and `required_labels` fields.

### Behavior changes[​](#0-26-82-changes "Direct link to Behavior changes")

#### SDK[​](#sdk-6 "Direct link to SDK")

* Deprecated the `AnyscaleSDK` class with a warning. Migrate to `import anyscale` and use `anyscale.<module>.<function>()`. Anyscale will remove the legacy class on February 28, 2026. See [Get started with the Anyscale SDK](/reference/quickstart-sdk.md).

#### CLI[​](#cli-9 "Direct link to CLI")

* `anyscale workspace_v2 push` and `anyscale workspace_v2 pull` now use HTTPS WebSocket tunnel by default for file transfers. Use `--direct-ssh` to force legacy SSH (port 22) connection.
* CLI upgrade warnings now only appear when your version is significantly outdated: major or minor version behind, or more than 5 patch versions behind.
* `anyscale compute-config list` command description improved and no longer marked as limited support.

#### Cloud setup[​](#cloud-setup "Direct link to Cloud setup")

* `anyscale cloud setup` for AWS (VM and Kubernetes) now configures additional CORS headers (`Accept-Ranges`, `Content-Range`, `Content-Length`) on storage buckets to support the optimized File Viewer feature.

## Version 0.26.81 release notes[​](#0-26-81 "Direct link to Version 0.26.81 release notes")

Version 0.26.81 is available as of January 14, 2026.

### New features[​](#0-26-81-features "Direct link to New features")

#### SDK[​](#sdk-7 "Direct link to SDK")

* Added `anyscale.compute_config.get_default()` to retrieve the default compute config. Supports optional `cloud` and `cloud_resource` parameters for filtering. See [Compute Config API Reference](/reference/compute-config-api.md).
* Added `anyscale.compute_config.list()` with filtering, sorting, and pagination. Supports `cloud_id`, `cloud_name`, `sort_by`, `sort_order`, `max_items`, and `next_token` parameters. Returns a `ComputeConfigListResult` object. See [Compute Config API Reference](/reference/compute-config-api.md).
* Added `anyscale.job.list()` with filtering and pagination. Supports filtering by `name`, `project`, `cloud`, `state_filter`, `tags_filter`, and more. See [Job API Reference](/reference/job-api.md).
* Added `anyscale.schedule.list()` with filtering and pagination. Supports filtering by `name`, `project`, `cloud`, and `creator_id`. See [Schedule API Reference](/reference/schedule-api.md).
* Added `anyscale.image.archive()` to archive container images and all versions. See [Image API Reference](/reference/image.md).
* Added `cloud` parameter to `anyscale.compute_config.get()` to filter by cloud name when resolving compute configs.

#### CLI[​](#cli-10 "Direct link to CLI")

* Added `anyscale image archive --name <image>` command to archive container images. See [Image API Reference](/reference/image.md).
* Enhanced `anyscale compute-config list` with pagination (`--next-token`), filtering (`--cloud-id`, `--cloud-name`), sorting (`--sort-by`, `--sort-order`), and JSON output (`--json`).
* Enhanced `anyscale compute-config get` with `--cloud-id` and `--cloud-name` options for filtering.

#### Compute config[​](#compute-config-1 "Direct link to Compute config")

* Added `cpu_architecture` field to `PhysicalResources`. Valid values: `x86_64` (default) and `arm64`. See [Compute Config API Reference](/reference/compute-config-api.md).

* GKE now automatically derives node selectors from Ray labels for TPU workloads. Specify `ray.io/accelerator-type` and `ray.io/tpu-topology` in labels instead of explicit node selectors:

  ```
  labels:
    ray.io/accelerator-type: TPU-V6E
    ray.io/tpu-topology: 2x2
  ```

### Behavior changes[​](#0-26-81-changes "Direct link to Behavior changes")

#### CLI[​](#cli-11 "Direct link to CLI")

* Deprecated `anyscale cloud edit`. Use `anyscale cloud update` instead.
* Refactored `cloud setup`, `cloud update`, and `cloud delete` to use new cloud resource APIs.
* Log downloads now create the temp directory inside the target directory to avoid cross-partition issues. Error messages for disk space limits now include the target directory, available space, and required space.

### Bug fixes[​](#0-26-81-fixes "Direct link to Bug fixes")

* Fixed bug where `JobStatus` returned by `anyscale.job.list()` had `created_at=None` despite the API returning the correct timestamp.
* Fixed `anyscale user list-permissions` command.
