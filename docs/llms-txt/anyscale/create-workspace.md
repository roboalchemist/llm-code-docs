# Source: https://docs.anyscale.com/get-started/create-workspace.md

# Tutorial: Create a workspace

[View Markdown](/get-started/create-workspace.md)

# Tutorial: Create a workspace

In this tutorial, you'll learn how to launch an Anyscale Workspace to support interactive development with Ray using Jupyter notebooks or VS Code.

## What is an Anyscale workspace?[​](#what-is "Direct link to What is an Anyscale workspace?")

Anyscale workspaces provide interactive compute resources, dependency management, and other infrastructure for developing and running Ray code and other arbitrary commands. When you launch a workspace, Anyscale deploys a scalable Ray cluster based on two configurations: a container image and a compute config.

The container image defines the software that runs on the cluster, including the Ray and Python versions. This tutorial uses an Anyscale base image, but you can also launch clusters with customized images.

The compute config defines the resources and behaviors for the cluster. The following are examples of parameters you can control:

* Cloud preferences.
* Instance types.
* Scaling options.

If you're familiar with Ray, you can think of the compute config as the replacement for Ray's `cluster.yaml` file.

Anyscale provides default values for these configurations, but most workloads require some customization of compute configurations before being deployed as production jobs.

## Create a workspace[​](#create "Direct link to Create a workspace")

Complete the following steps to create and launch an Anyscale Workspace:

1. Log in to the [Anyscale console](https://console.anyscale.com).

2. In the left navigation bar, select **Workspaces**.

3. Click **+ Create** and select **Custom blank workspace**.

4. Enter a workspace name, such as `my-first-workspace`

5. Select a container image from the dropdown, for example `anyscale/ray:2.45.0-slim-py312`

6. Under **Compute configuration**, select **Use my own configuration**

7. For the **Head node**, stick with the default selection.

8. Under **Worker nodes**, select **+ Add Worker Nodes** to add a new group. A new worker node config appears in the UI.

9. Select the worker node config to customize the workers with the following settings:

   <!-- -->

   * Set **Autoscaling** to **Enabled**.
   * Set **Min nodes** to `0`.
   * Set **Max nodes** to `3`.

10. Optionally, tweak the **Auto termination** settings. Ignore the other settings for now.

11. Click **Create**.

The workspace takes a few moments to launch.

Because the configuration specifies autoscaling with a 0 node minimum, the cluster launches with as a head node with no workers. Running commands on the workspace spawns worker nodes as needed.
