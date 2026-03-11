# Source: https://docs.mystic.ai/docs/deploying-pipelines.md

# Deploying Pipelines

Deploy pipelines to a cluster running on your own cloud through Mystic BYOC

There are two methods for deploying a pipeline on your BYOC cluster:

1. One click deploy (migration/clone)
2. Uploading a new pipeline

# One click deploy

When viewing a pipeline on the dashboard there is a `Deploy pipeline` button that allows you to clone an existing pipeline to another cluster.

You can do this for any public pipeline, or private pipeline that you own. When it is deployed the following happens:

* If you owned the pipeline (even if it's public) a new version of the model is created which is identical to the existing one, but with an incremented pipeline pointer version and a new `pipeline_id`. Read mode about pointers and versioning here: [Pointers](https://docs.mystic.ai/docs/pointers-1).
* If you did not own the pipeline, a new version is created and then owned by you. For example say I deploy `mistral/mistral-7b:v5` and my username is `paulh` my newly deployed pipeline would have a pointer of `paulh/mistral-7b:v1` assuming it's the first time I've done this.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e5c14bc-Screenshot_2024-04-08_at_12.42.39.png",
        "",
        "The deploy pipeline field is shown on the bottom right."
      ],
      "align": "center",
      "caption": "The deploy pipeline field is shown on the bottom right."
    }
  ]
}
[/block]

# Uploading a new pipeline

When uploading from your local system you can target a BYOC cluster by using the `pipeline.yaml` configuration file. There is an additional cluster field that takes in 2 arguments:

```yaml
...
pipeline_name: mistral-7b
cluster:
  id: cluster_12345
  node_pool: node_pool_name
```

The cluster field takes in two arguments:

* `id` - The ID of the cluster which you can get on the cluster view page
* `node_pool` - The name of the node pool to deploy the pipeline on

Alternatively, it is also possible to define a target cluster and node-pool for your pipeline, directly in the `pipeline container push` command, as follows:

```shell
pipeline container push --cluster CLUSTER_ID --node-pool NODE_POOL_NAME
```

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3f05bd8-Screenshot_2024-04-08_at_12.52.23.png",
        "",
        "This is a BYOC cluster deployed on Azure in UK South. The Cluster ID is shown at the top begining `cluster_3cd3d01...` and the only present node pool name is `x1a1008020d`."
      ],
      "align": "center",
      "caption": "This is a BYOC cluster deployed on Azure in UK South. The Cluster ID is shown at the top begining `cluster_3cd3d01...` and the only present node pool name is `x1a1008020d`."
    }
  ]
}
[/block]

For the above cluster the `pipeline.yaml` should be:

```yaml
...
pipeline_name: mistral-7b
accelerators:
  - nvidia_a100_80gb_20gb
cluster:
  id: cluster_3cd3d01... # Put the full cluster ID in
  node_pool: x1a1008020d
```

Read more about accelerators here: [GPUs and accelerators](https://docs.mystic.ai/docs/gpus-and-accelerators).