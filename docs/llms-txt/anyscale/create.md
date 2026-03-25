# Source: https://docs.anyscale.com/configuration/compute/create.md

# Create or version a compute config

[View Markdown](/configuration/compute/create.md)

# Create or version a compute config

This page provides an overview of creating and versioning reusable compute configs using the Anyscale console. You can use compute configs stored in your Anyscale cloud when deploying Anyscale workspace, jobs, or services. See [Define a Ray cluster](/configuration.md).

To prevent changing behaviors for existing workload definitions, you can't edit or update compute configs registered to Anyscale. The following table provides a high-level overview of options for registering compute configs:

| Process                                                     | Description                                                                                                                                                    |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Create a compute config](#create)                          | Create a new compute config when you have a new workload or use case and want to have a compute config for use across multiple Ray clusters.                   |
| [Create a new version of a compute config](#version)        | Version an existing compute config for small updates or changes, such as during interactive development or troubleshooting production workloads.               |
| [Modify and save a compute config for a workspace](#modify) | Modify the compute settings for a workspace during interactive development, then optionally save this custom configuration to launch other Anyscale workloads. |

If you use the console to create a new Anyscale workspace, you can select an existing compute config or define a custom compute config. See [Manage workspaces](/platform/workspaces/manage.md).

note

Your Anyscale cluster must have a head node. Worker nodes are optional. You configure worker nodes on Anyscale as groups of machines.

For an overview of Ray clusters, see the [Ray docs on key Ray cluster concepts](https://docs.ray.io/en/latest/cluster/key-concepts.html).

You can also create and modify compute configs using the CLI or SDK. See the following pages:

* CLI: [Compute Config CLI](/reference/compute-config-api.md#compute-config-cli)
* SDK: [`anyscale.compute_config.create`](/reference/compute-config-api.md#anyscalecompute_configcreate)
* Compute config model: [`ComputeConfig`](/reference/compute-config-api.md#computeconfig)

## Create a compute config[​](#create "Direct link to Create a compute config")

Complete the following steps to create a new compute config:

note

Anyscale recommends configuring a head node with at least 8 vCPUs and 32 GB of RAM and worker nodes with at least 4 vCPUs and 16 GB of RAM. See [Node sizing guidelines](/configuration/compute.md#sizing-recs).

1. [Log in to the Anyscale console](https://console.anyscale.com/).

2. Click **Advanced > Compute configs**.

3. Click **+ Create**.

4. In the **Name** field, enter a name for your compute config.

5. To configure your head node, click the default entry under **Head node**, for example **8CPU-32GB**.

   <!-- -->

   * Use the **Instance type** field to change the instance type.
   * Click **Advanced config** to set additional JSON-formatted options. See [Node config](/configuration/compute.md#node).

6. Click **+ Add worker nodes** to define a group of worker nodes. A default worker group configuration appears, for example **8CPU-32GB**.

7. To configure your worker group, click the default entry.

   <!-- -->

   * Use the **Instance type** field to specify the instance type for the group.
   * Set the **Autoscaling** field to **Enabled** to configure scaling behaviors. See [Worker nodes scaling config](/configuration/compute.md#scaling).
   * Click **Advanced config** to set additional JSON-formatted options. See [Node config](/configuration/compute.md#node).

8. Add and configure additional worker groups as desired.

9. Click **Advanced settings** to view cluster-wide configuration options. See [Cluster config advanced settings](/configuration/compute.md#cluster).

10. Click **Create**.

## Create a new version of a compute config[​](#version "Direct link to Create a new version of a compute config")

Complete the following steps to create a new version of an existing compute config:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Advanced > Compute configs**.
3. Click the name of the desired compute config.
4. Click **+ Create new version** to start with the most recent version, or click the desired version from the list.
5. Modify the compute config settings as desired.
6. Click **Create**.

The options to create a new version are identical to those for creating a new compute config, but you can't change the name.

## Modify and save a compute config for a workspace[​](#modify "Direct link to Modify and save a compute config for a workspace")

You can use the Anyscale console to modify the compute config for a workspace and optionally save it as a new compute config. Complete the following steps:

note

Modifying an existing compute config always results in a **Custom configuration**, which you can optionally save. You can't create a new version of an existing compute config using this flow.

1. Navigate to the Anyscale console.
2. Click **Workspaces**.
3. Click the name of a workspace.
4. In the top right corner, click **...** and select **Manage cluster**.

The **Compute resources** panel slides open from the right side and displays the current compute config for your workspace. You can modify, add, or delete compute configurations by completing any of the following actions:

* To change the compute config for your workspace, click the edit icon ![Edit icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAUCAYAAACAl21KAAABU2lDQ1BJQ0MgUHJvZmlsZQAAGJVtkD0sQ2EUhp9WpZQIYTR0EH8pkdJgrA4iQZqi/qbb26ombd3cXhGJTSIWIxOLwWyrUcRELAiJ3WCSkHShrnNbtMVJ3pwnb97vy5sDdhRNSzqAVNrQQ6Mj7rn5BbfzCSc2amlmSFEzmj8YHJcI37tycneSlbnpsf46POjYfd4JP17WvFwsnnW7/uYrxhWNZVTZ76J2VdMNsLUJB9cMzWIRLbqUEt62OF7kfYsjRT4uZKZDAeFz4UZ1WYkK3wp7ImV+vIxTyVX1q4PVvj6Wnpmy+ohaCTOJl0GG5S7/5wYKuQAraKyjkyDOMgZu/OJoJIkJj5FGpRePsJc+kc+67++7lbzEFvhE9uuSF72Ckw2pPFHyOjeh6QNOGzRFV36uacs5Mkv93iLXZaF6zzRfZ8HZBfl703zLmmb+CKoe5G3uE9a9YtwqEWfPAAAARGVYSWZNTQAqAAAACAACARIAAwAAAAEAAQAAh2kABAAAAAEAAAAmAAAAAAACoAIABAAAAAEAAAASoAMABAAAAAEAAAAUAAAAAN+Z0lsAAAICaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4xODwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4yMDwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo46BEmAAAAxUlEQVQ4Ea3Uiw2EIAwG4Hq5SWAWZmElmIVZYJU7f5ISwGp9NVFB6icvXX5r0AvxuWKUUnbTT0MpJQohUIxRxE5BQHBYaynnLGIqxIhzjrz3hKuEHUI9AgDB82SMGYa4C0kI5ge9AcowayJ0FQG2ge4gG+guMkBPkAY9RRqEAgIbDnG0OjVBOH37e+gZYm+J+9y5PEAAENI+mR+c68tbv5HaI2x77s38Jq2OecXnUiEgPD/ag1I7oDY0/hilRO3eAGnJWvsfEn+dcYp+Fp8AAAAASUVORK5CYII=) next to the name of your compute config.
* To change the settings for the head node or worker nodes in your cluster, click the edit icon ![Edit icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAUCAYAAACAl21KAAABU2lDQ1BJQ0MgUHJvZmlsZQAAGJVtkD0sQ2EUhp9WpZQIYTR0EH8pkdJgrA4iQZqi/qbb26ombd3cXhGJTSIWIxOLwWyrUcRELAiJ3WCSkHShrnNbtMVJ3pwnb97vy5sDdhRNSzqAVNrQQ6Mj7rn5BbfzCSc2amlmSFEzmj8YHJcI37tycneSlbnpsf46POjYfd4JP17WvFwsnnW7/uYrxhWNZVTZ76J2VdMNsLUJB9cMzWIRLbqUEt62OF7kfYsjRT4uZKZDAeFz4UZ1WYkK3wp7ImV+vIxTyVX1q4PVvj6Wnpmy+ohaCTOJl0GG5S7/5wYKuQAraKyjkyDOMgZu/OJoJIkJj5FGpRePsJc+kc+67++7lbzEFvhE9uuSF72Ckw2pPFHyOjeh6QNOGzRFV36uacs5Mkv93iLXZaF6zzRfZ8HZBfl703zLmmb+CKoe5G3uE9a9YtwqEWfPAAAARGVYSWZNTQAqAAAACAACARIAAwAAAAEAAQAAh2kABAAAAAEAAAAmAAAAAAACoAIABAAAAAEAAAASoAMABAAAAAEAAAAUAAAAAN+Z0lsAAAICaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4xODwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4yMDwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo46BEmAAAAxUlEQVQ4Ea3Uiw2EIAwG4Hq5SWAWZmElmIVZYJU7f5ISwGp9NVFB6icvXX5r0AvxuWKUUnbTT0MpJQohUIxRxE5BQHBYaynnLGIqxIhzjrz3hKuEHUI9AgDB82SMGYa4C0kI5ge9AcowayJ0FQG2ge4gG+guMkBPkAY9RRqEAgIbDnG0OjVBOH37e+gZYm+J+9y5PEAAENI+mR+c68tbv5HaI2x77s38Jq2OecXnUiEgPD/ag1I7oDY0/hilRO3eAGnJWvsfEn+dcYp+Fp8AAAAASUVORK5CYII=) for the desired node. Click **Save** to commit changes to your current workspace cluster.
  <!-- -->
  * You must disable **Auto-select worker nodes** to edit worker group configurations.
* To delete a worker group from your cluster, click the **X** for the desired worker group.
* To add new worker node groups, click the **+ Add worker nodes** button. Click **Save** to commit changes to your current workspace cluster.
* To view and modify cluster-wide settings, click **Advanced settings**. Click **Save** to commit changes to your current workspace cluster.

Click the ![Save icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAATCAYAAAByUDbMAAABU2lDQ1BJQ0MgUHJvZmlsZQAAGJVtkD0sQ2EUhp9WpZQIYTR0EH8pkdJgrA4iQZqi/qbb26ombd3cXhGJTSIWIxOLwWyrUcRELAiJ3WCSkHShrnNbtMVJ3pwnb97vy5sDdhRNSzqAVNrQQ6Mj7rn5BbfzCSc2amlmSFEzmj8YHJcI37tycneSlbnpsf46POjYfd4JP17WvFwsnnW7/uYrxhWNZVTZ76J2VdMNsLUJB9cMzWIRLbqUEt62OF7kfYsjRT4uZKZDAeFz4UZ1WYkK3wp7ImV+vIxTyVX1q4PVvj6Wnpmy+ohaCTOJl0GG5S7/5wYKuQAraKyjkyDOMgZu/OJoJIkJj5FGpRePsJc+kc+67++7lbzEFvhE9uuSF72Ckw2pPFHyOjeh6QNOGzRFV36uacs5Mkv93iLXZaF6zzRfZ8HZBfl703zLmmb+CKoe5G3uE9a9YtwqEWfPAAAARGVYSWZNTQAqAAAACAACARIAAwAAAAEAAQAAh2kABAAAAAEAAAAmAAAAAAACoAIABAAAAAEAAAAToAMABAAAAAEAAAATAAAAAOofxQgAAAICaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4xOTwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4xOTwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgpnTmKRAAABCUlEQVQ4Ec2USw6CMBCGW6NuPQOPnYkrFl4AE0/AFbgAe05BuAIn0NDEtZ4BgWNIdFFnTIYUaMEYF0xCZkr/+TplJjA2V+NUWJ7nkuIp77ruwbZt0de1sCiKvoYhJAiCted5LxW4VBe+7zPHcdRXg7gsSyaEYFmWPeu6PlqWdSZRB4YgKJ/2tB73UZemKUuS5ATAPQBvKF5oMyZeIjAMw4+qKIoryX+CUXLfzxfWaQCVXVUVhVpvatIAhiDs1JjRx+9rBjAS6MYED8I5M5kRhlfBIVYNh3UM9tdudipTT8UrmRqh6tTKW1jTNBv4c1xwk3N+h4QHPFsp5QLWMfiYEuG6O4hXtJ6/fwMTI1toETesEQAAAABJRU5ErkJggg==) to save your current configuration to make it available to all users and workloads in your Anyscale cloud. You must provide a unique name for your compute config.
