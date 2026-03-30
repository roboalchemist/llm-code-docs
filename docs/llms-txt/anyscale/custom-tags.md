# Source: https://docs.anyscale.com/resources/custom-tags.md

# Add custom tags to workloads and cloud resources

[View Markdown](/resources/custom-tags.md)

# Add custom tags to workloads and cloud resources

This page provides an overview of configuring and using custom resource tags in Anyscale.

note

You can use custom tags to set scheduling priorities for workloads managed by the global resource scheduler. See [Example: Use custom resource tags for scheduling rules](/machine-pools/global-resource-scheduler.md#custom-tags).

## What are custom resource tags?[​](#what-are-custom-resource-tags "Direct link to What are custom resource tags?")

Custom resource tags are key-value pairs that you configure as metadata for Anyscale workspaces, services, jobs, or job queues.

You use tags in the Anyscale console or CLI to filter results and organize dashboards.

Anyscale passes all custom resource tags through to underlying infrastructure in your cloud provider account. For workloads running on virtual machines (VMs), these values appear on underlying AWS resources as tags or Google Cloud resources as labels. Anyscale workloads running on Kubernetes pass tags through to your Kubernetes infrastructure using labels.

important

Anyscale assigns default resource tags to underlying cloud infrastructure. These tags start with `anyscale-`.

You can't use these tags to filter results in the Anyscale console or CLI, but they can be useful for monitoring, observability, and cost attribution in your cloud provider account.

## Use for monitoring, observability, and permissions[​](#use-for-monitoring-observability-and-permissions "Direct link to Use for monitoring, observability, and permissions")

You can use either system tags or custom tags for monitoring and observability for use cases such as the following:

* Cost management and attribution.
* Filtering and finding virtual machines.
* Identifying cloud infrastructure associated with a specific workload.
* Cleanup queries or cronjobs.

## Tag propagation semantics[​](#propagation "Direct link to Tag propagation semantics")

Resources in your cloud provider initialize with tags you include in the deploy command or configuration for your workload.

When you add tags using the Anyscale console or CLI, Anyscale propagates these changes to underlying cloud resources for running workloads in an eventually-consistent manner.

For tags on running workloads, Anyscale sends commands to add tags for cloud resources after you apply changes in the console or CLI. Resources and logs in your cloud provider reflect these tags after a short delay.

Anyscale doesn't attempt to delete tags from cloud resources associated with running workloads. When you restart a cluster, Anyscale doesn't include deleted tags.

Anyscale uses ephemeral resources for launching clusters, so when you update tags on terminated workloads, these tag updates can't propagate to underlying cloud resources. If you restart a terminated workload after changing tags, the updated tags apply to the new resources provisioned in your cloud provider.

### Tags and machine pools[​](#machine-pools "Direct link to Tags and machine pools")

You can configure the global resource scheduler to reuse VMs and Kubernetes pods registered as machine pools to queue, preempt, and run multiple workloads. When you run workloads with tags on machine pools, the following behavior applies:

* When the workload begins, Anyscale adds tags for the workload to the underlying resources in your cloud provider or Kubernetes cluster.
* When the workload completes or when preemption occurs, Anyscale removes all tags for the workload from the underlying resources.
* When you delete or update tags for a running workload, Anyscale propagates these changes in an eventually-consistent manner.

This means that the tags or labels assigned to the resources running your workloads always reflect the running workloads, and that tags update dynamically with workload scheduling and preemption.

note

You can use tags to set priority for workloads. See [Example: Use custom resource tags for scheduling rules](/machine-pools/global-resource-scheduler.md#custom-tags).

## Custom tag requirements and limitations[​](#custom-tag-requirements-and-limitations "Direct link to Custom tag requirements and limitations")

Anyscale always displays custom resource tags as key-value pairs using the standard `key:value` format.

The following requirements and limitations apply:

* The maximum length for a tag is 63 characters. This limit includes the length of both the key and the value.
* Keys and values can include lowercase letters, numbers, and the characters `_.-`.
* Each workload can only have a single tag for each unique key. Setting a tag with the same key and a different value overwrites the previous tag.
* Each workload can have a maximum of 20 tags.
* Anyscale disallows custom keys with some prefixes and reserved keywords to avoid conflict with system tags. An error message appears when you attempt to set a tag with a disallowed key.

important

AWS, Google Cloud, Azure, and other cloud providers enforce their own limits for resource tags and labels. If you have additional custom tagging implemented in your cloud provider account, adjust your tagging strategy to respect these limits. For Anyscale clouds using Kubernetes resources, consult documentation for your managed Kubernetes service to learn how tags pass through to your cloud provider resources. In addition to custom tags, Anyscale sets systems tags on resources deployed in your cloud provider account. The total number of tags set by Anyscale shouldn't exceed the limits enforced by your cloud provider. Contact [Anyscale Support](mailto:support@anyscale.com) to troubleshoot errors related to tags.

## Add a custom tag during workspace creation[​](#add-a-custom-tag-during-workspace-creation "Direct link to Add a custom tag during workspace creation")

You can use the Anyscale console to add tags while creating a workspace.

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Workspaces**.
3. Click **Create**.
4. Click **Custom blank workspace**.
5. Click **Tags**.
6. Click **Add a tag**.
7. Use the field to add a new tag using `key:value` syntax, or search for an existing tag and click to select.
   <!-- -->
   * Anyscale greys out tags with keys already set for your workload.
8. Add multiple tags by clicking **Add a tag** and repeating.

## Add custom tags for new workloads with the Anyscale CLI[​](#add-custom-tags-for-new-workloads-with-the-anyscale-cli "Direct link to Add custom tags for new workloads with the Anyscale CLI")

Anyscale jobs, service, and workspaces support adding tags during workload creation.

You can pass multiple tags using the `--tag` parameter as `key:value` pairs, as in the following example:

* Job
* Service
* Workspace

```
anyscale job submit --config-file /path/to/config.yaml --tag <key1:value> --tag <key2:value>
```

```
anyscale service deploy --config-file /path/to/config.yaml --tag <key1:value> --tag <key2:value>
```

```
anyscale workspace_v2 create --config-file /path/to/config.yaml --tag <key1:value> --tag <key2:value>
```

You can also define tags as a top-level field in a YAML config for each workload, as in the following example:

```
tags:
  key1: value
  key2: value
```

## Add, update, or remove a custom tag for an existing workload[​](#add-update-or-remove-a-custom-tag-for-an-existing-workload "Direct link to Add, update, or remove a custom tag for an existing workload")

Anyscale workspace, services, jobs, and job queues using similar flows for managing tags for existing workloads in either the Anyscale console or through the CLI.

note

You can update tags for workloads regardless of their state in Anyscale, but tags can only propagate to underlying resources in your cloud provider for running workloads. See [Tag propagation semantics](#propagation).

Anyscale treats each job run as a separate job. While workspaces, services, and job queues apply tags when you restart them from a terminated state, you must update job tags in the config file or in your `job submit` command to reflect the change in subsequent runs.

### Manage tags in the Anyscale console[​](#manage-tags-in-the-anyscale-console "Direct link to Manage tags in the Anyscale console")

To manage custom tags for an existing workload in the Anyscale console, complete the following steps:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Workspaces**, **Jobs**, or **Services**.
   <!-- -->
   * For a job queue, click **Jobs** then **Job queues**.
3. Click the name of the workload.
4. Click the edit icon ![Edit icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAUCAYAAACAl21KAAABU2lDQ1BJQ0MgUHJvZmlsZQAAGJVtkD0sQ2EUhp9WpZQIYTR0EH8pkdJgrA4iQZqi/qbb26ombd3cXhGJTSIWIxOLwWyrUcRELAiJ3WCSkHShrnNbtMVJ3pwnb97vy5sDdhRNSzqAVNrQQ6Mj7rn5BbfzCSc2amlmSFEzmj8YHJcI37tycneSlbnpsf46POjYfd4JP17WvFwsnnW7/uYrxhWNZVTZ76J2VdMNsLUJB9cMzWIRLbqUEt62OF7kfYsjRT4uZKZDAeFz4UZ1WYkK3wp7ImV+vIxTyVX1q4PVvj6Wnpmy+ohaCTOJl0GG5S7/5wYKuQAraKyjkyDOMgZu/OJoJIkJj5FGpRePsJc+kc+67++7lbzEFvhE9uuSF72Ckw2pPFHyOjeh6QNOGzRFV36uacs5Mkv93iLXZaF6zzRfZ8HZBfl703zLmmb+CKoe5G3uE9a9YtwqEWfPAAAARGVYSWZNTQAqAAAACAACARIAAwAAAAEAAQAAh2kABAAAAAEAAAAmAAAAAAACoAIABAAAAAEAAAASoAMABAAAAAEAAAAUAAAAAN+Z0lsAAAICaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4xODwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4yMDwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo46BEmAAAAxUlEQVQ4Ea3Uiw2EIAwG4Hq5SWAWZmElmIVZYJU7f5ISwGp9NVFB6icvXX5r0AvxuWKUUnbTT0MpJQohUIxRxE5BQHBYaynnLGIqxIhzjrz3hKuEHUI9AgDB82SMGYa4C0kI5ge9AcowayJ0FQG2ge4gG+guMkBPkAY9RRqEAgIbDnG0OjVBOH37e+gZYm+J+9y5PEAAENI+mR+c68tbv5HaI2x77s38Jq2OecXnUiEgPD/ag1I7oDY0/hilRO3eAGnJWvsfEn+dcYp+Fp8AAAAASUVORK5CYII=) under **Tags**. The **Tags** flyout appears.

You can now add, update, or remove tags.

important

To update the value of a key, you must first remove the tag then add a new tag.

Tags appear in the console if they exist in any workload in your cloud. You must remove a tag from all workloads in the cloud to remove it from the list.

To add a tag, do the following:

1. Click **Add more tags**.
2. Click **Add a tag**.
3. Use the field to add a new tag using `key:value` syntax, or search for an existing tag and click to select.
   <!-- -->
   * Anyscale greys out tags with keys already set for your workload.
4. Add multiple tags by clicking **Add a tag** and repeating.
5. Click **Update**.

To remove a tag, click the trash can icon next to the tag name.

### Manage tags in the Anyscale CLI[​](#manage-tags-in-the-anyscale-cli "Direct link to Manage tags in the Anyscale CLI")

To manage custom tags for an existing workload using the Anyscale CLI, use the following syntax pattern for the appropriate workload type.

#### Add or update tags with the Anyscale CLI[​](#add-or-update-tags-with-the-anyscale-cli "Direct link to Add or update tags with the Anyscale CLI")

* Job
* Service
* Workspace

Use the following example syntax to add or update tags for a job with the CLI:

```
anyscale job tags add --id <workload-id> --tag <key1:value> --tag <key2:value>
```

Use the following example syntax to add or update tags for a service with the CLI:

```
anyscale service tags add --id <workload-id> --tag <key1:value> --tag <key2:value>
```

Use the following example syntax to add or update tags for a workspace with the CLI:

```
anyscale workspace_v2 tags add --id <workload-id> --tag <key1:value> --tag <key2:value>
```

Substitute the following values:

* `workload_id`: The ID for your workspace, job, or service.
* `key:value`: The key-value pair to define the tag. If a tag with the key already exists, the value updates.

#### Remove tags with the Anyscale CLI[​](#remove-tags-with-the-anyscale-cli "Direct link to Remove tags with the Anyscale CLI")

* Job
* Service
* Workspace

Use the following example syntax to remove tags from a job with the CLI:

```
anyscale job tags remove --id <workload-id> --key <key1> --key <key2>
```

Use the following example syntax to remove tags from a service with the CLI:

```
anyscale service tags remove --id <workload-id> --key <key1> --key <key2>
```

Use the following example syntax to remove tags from a workspace with the CLI:

```
anyscale workspace_v2 tags remove --id <workload-id> --key <key1> --key <key2>
```

Substitute the following values:

* `workload_id`: The ID for your workspace, job, or service.
* `key`: The key of the tag you want to remove. You can remove multiple keys by passing the `--key` parameter multiple times.

#### List tags with the Anyscale CLI[​](#list-tags-with-the-anyscale-cli "Direct link to List tags with the Anyscale CLI")

* Job
* Service
* Workspace

Use the following example syntax to list all tags attached to a job with the CLI:

```
anyscale job tags list --id <workload-id>
```

Use the following example syntax to list all tags attached to a service with the CLI:

```
anyscale service tags list --id <workload-id>
```

Use the following example syntax to list all tags attached to a workspace with the CLI:

```
anyscale workspace_v2 tags list --id <workload-id>
```

Substitute the ID for your workspace, job, or service for `workload_id`.

## Filter results with custom tags[​](#filter-results-with-custom-tags "Direct link to Filter results with custom tags")

You can use custom tags to filter workspaces, services, jobs, and job queues.

Tag filtering only supports exact matching semantics for keys and values.

note

When you're using the Anyscale console to search for tags, Anyscale searches for substring matches across keys and values.

Anyscale console queries that filter using many tags might experience a slight query overhead.

When using either the console or CLI to filter using tags, Anyscale applies the following logic:

* If you specify multiple tags with the same key, Anyscale uses **OR** logic to match any of the values specified.
* If you specify multiple tags with different keys, Anyscale uses **AND** logic to match all values specified.

- Anyscale console
- CLI

In the console, you select each tag individually from the list view for the workload type using the following steps:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Workspaces**, **Jobs**, or **Services**.
   <!-- -->
   * For a job queue, click **Jobs** then **Job queues**.
3. Click **Tags**.
4. Use the field search for an existing tag and click to select.
5. Click **Tags**, search, and click to add additional tags.

In the CLI, you pass each tag using a separate `--tag` parameter, as in the following example:

```
anyscale <workload-type> list --tag <key1:value1> --tag <key1:value2> --tag <key2:value> 
```

Substitute the following values:

* `workload-type`: The type of workload. One of `workspace`, `job`, or `service`.
* `key:value`: The key-value pair for the tag.

## Best practices[​](#best-practices "Direct link to Best practices")

Anyscale recommends the following best practices for custom tags:

* Standardize a taxonomy of tags that you can apply to all workloads, for example `team`, `env`, `project`, and `cost-center`.
* Use controlled vocabularies where possible to ensure consistency.
* Use short, meaningful keys in `kebab-case` or `snake_case` format.

## Common tag examples[​](#common-tag-examples "Direct link to Common tag examples")

The follow table shows examples for how you might implement a custom tagging strategy:

| Category         | Examples                                                                 |
| ---------------- | ------------------------------------------------------------------------ |
| Ownership        | `team:mlops`, `owner:jane.doe`                                           |
| Environment      | `env:dev`, `env:staging`, `env:prod`                                     |
| Cost and project | `cost-center:cc-123`, `project:alpha`                                    |
| Lifecycle        | `purpose:batch`, `purpose:realtime`, `retention:short`, `retention:long` |
