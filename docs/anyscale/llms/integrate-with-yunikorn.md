# Source: https://docs.anyscale.com/administration/cloud-deployment/integrate-with-yunikorn.md

# Integrate the Anyscale operator with YuniKorn scheduler

[View Markdown](/administration/cloud-deployment/integrate-with-yunikorn.md)

# Integrate the Anyscale operator with YuniKorn scheduler

info

YuniKorn integration for Anyscale on Kubernetes is in beta release.

This guide explains how to integrate your Anyscale Kubernetes deployments with the YuniKorn scheduler to manage instance upscaling and resource scheduling.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before beginning, ensure that:

* You already configured the Kubernetes cluster with **YuniKorn**.
* You've created a **YuniKorn queue**, for example, `root.sandbox`.

## Configure Anyscale to use YuniKorn[​](#configure-anyscale-to-use-yunikorn "Direct link to Configure Anyscale to use YuniKorn")

In the compute config, configure the cluster advanced configuration to instruct Anyscale to integrate with your YuniKorn queue.

While it's possible to set YuniKorn configurations at the worker group level, you will run into issues with gang scheduling guarantees if worker groups with minimum pods belong to different queues. All worker groups with a minimum pod count must belong to the same YuniKorn queue to ensure the cluster becomes healthy with the minimum expected resources. Groups can belong to other YuniKorn queues if they have a minimum of 0 pods or if the worker groups are intended for autoscaling.

1. **Set the queue label** in your Anyscale cluster advanced configuration:

```
{
  "metadata": {
    "labels": {
      "queue": "root.sandbox"
    }
  }
}
```

**Optional:** To customize scheduling policy behavior, add an arbitrary key-value pair under the `annotations` section as follows:

```
{
  "metadata": {
    "annotations": {
      "yunikorn.apache.org/schedulingPolicyParameters": "YOUR_CUSTOM_PARAMETERS"
    }
  }
}
```

For details on valid policy parameters, see the [Scheduling Policy Parameters documentation](https://yunikorn.apache.org/docs/user_guide/gang_scheduling/#scheduling-policy-parameters).

info

Anyscale highly recommends setting the following annotation.

```
{
  "metadata": {
    "annotations": {
      "yunikorn.apache.org/schedulingPolicyParameters": "gangSchedulingStyle=Hard"
    }
  }
}
```

tip

You can pass [user authentication](http://yunikorn.apache.org/user.info) information to YuniKorn as well using the following annotation:

```
{
  "metadata": {
    "annotations": {
      "yunikorn.apache.org/user.info": "XXXX"
    }
  }
}
```

## How Anyscale works with YuniKorn[​](#how-anyscale-works-with-yunikorn "Direct link to How Anyscale works with YuniKorn")

When you configure the `metadata.labels.queue` label, Anyscale automatically integrates resource scheduling requests with YuniKorn as follows:

* **Batching requests:** Anyscale groups all minimum-resource-based scaling requests,`min_count`, into a single batch request.

* **Task groups:** This batch request includes the annotation `yunikorn.apache.org/task-groups`, required by YuniKorn. Each scaling sub-request maps to a unique `yunikorn.apache.org/task-group-name`.

* **Automatic Pod specifications:** Anyscale automatically sets necessary labels and annotations on the pods it generates:

  * `yunikorn.apache.org/app-id` - Set to `{cluster-id}-min` for minimum-resource requests.
  * `yunikorn.apache.org/task-group-name`
  * `yunikorn.apache.org/task-groups`

* **Autoscaling behavior:**<br /><!-- -->Autoscaling, or non-minimum, requests generate pods without explicit task-group labels or annotations, meaning each autoscaled pod becomes its own separate task group within YuniKorn.

## Managed labels and annotations[​](#managed-labels-and-annotations "Direct link to Managed labels and annotations")

Anyscale explicitly manages the following labels and annotations:

| Type       | Key                                   | Description                                        |
| ---------- | ------------------------------------- | -------------------------------------------------- |
| Label      | `yunikorn.apache.org/app-id`          | YuniKorn application identifier, set by Anyscale.  |
| Annotation | `yunikorn.apache.org/task-group-name` | Specifies the task-group name per sub-request.     |
| Annotation | `yunikorn.apache.org/task-groups`     | Defines the batch of task groups sent to YuniKorn. |

You can freely configure additional labels and annotations from the [YuniKorn documentation](https://yunikorn.apache.org/) as needed.

## Limitations and notes[​](#limitations-and-notes "Direct link to Limitations and notes")

* **Minimum-resource constraints:**
  <br />
  <!-- -->
  When using YuniKorn with Anyscale, the Ray cluster's compute configuration can't include resource-based minimum flags, like `min_cpu`, `min_memory`, etc. Anyscale only supports `min_count`. Any update to `min_count` requires you to relaunch the cluster.
