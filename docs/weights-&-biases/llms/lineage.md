# Source: https://docs.wandb.ai/models/registry/lineage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Use lineage graphs to visualize a linked artifact's history and audit a collection's history.

# Lineage graphs and audit history

Use a lineage graph to visualize a linked artifact's history. Audit a collection's history to track changes made to artifacts in that collection.

## Lineage graphs

Within a collection in the W\&B Registry, you can view a history of the artifacts that an ML experiment uses. This history is called a *lineage graph*.

A lineage graph shows:

* Artifacts used as [inputs to a run](/models/artifacts/explore-and-traverse-an-artifact-graph#track-the-input-of-a-run).
* Artifacts created as [outputs from a run](/models/artifacts/explore-and-traverse-an-artifact-graph#track-the-output-of-a-run).

In other words, a lineage graph shows the input and output of a run.

For example, the following image shows a typical lineage graph for artifacts created and used throughout an ML experiment:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/uqPGOvf46GQ1vVUB/images/registry/registry_lineage.png?fit=max&auto=format&n=uqPGOvf46GQ1vVUB&q=85&s=6ecdeb4eef6a40e43916110899e47da3" alt="Registry lineage" width="3828" height="1624" data-path="images/registry/registry_lineage.png" />
</Frame>

From left to right, the image shows:

1. Multiple runs log the `split_zoo_dataset:v4` artifact.
2. The "rural-feather-20" run uses the `split_zoo_dataset:v4` artifact for training.
3. The output of the "rural-feather-20" run is a model artifact called `zoo-ylbchv20:v0`.
4. A run called "northern-lake-21" uses the model artifact `zoo-ylbchv20:v0` to evaluate the model.

To view a lineage graph for an artifact in a collection:

1. Navigate to the W\&B Registry.
2. Select the collection that contains the artifact.
3. From the dropdown, select the artifact version you want to view its lineage graph.
4. Select the **Lineage** tab.
5. Select a node to view detailed information about the run or artifact.

<Info>
  See [Enable lineage graph tracking](/models/artifacts/explore-and-traverse-an-artifact-graph#enable-lineage-graph-tracking) to learn how to track the input and output of a run using the W\&B Python SDK.
</Info>

The following image shows the expanded detailed view of a run (`rural-feather-20`) when you select a node in the lineage graph:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mmuC1X8m1VKb0ElQ/images/registry/lineage_expanded_node.png?fit=max&auto=format&n=mmuC1X8m1VKb0ElQ&q=85&s=faf7aafca042ca512b89398b5fc3315a" alt="Expanded lineage node" width="2298" height="1568" data-path="images/registry/lineage_expanded_node.png" />
</Frame>

The following image shows the expanded detailed view of an artifact (`zoo-ylbchv20:v0`) when you select an artifact node in the lineage graph:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/mmuC1X8m1VKb0ElQ/images/registry/lineage_expanded_artifact_node.png?fit=max&auto=format&n=mmuC1X8m1VKb0ElQ&q=85&s=63941a65a3e7b742c135a5177c56ae00" alt="Expanded artifact node details" width="2294" height="1566" data-path="images/registry/lineage_expanded_artifact_node.png" />
</Frame>

<Info>
  You can also view lineage graphs for artifacts you log to W\&B that are not part of a collection. See E[xplore artifact graphs](/models/artifacts/explore-and-traverse-an-artifact-graph) for more information.
</Info>

## Audit a collection's history

View actions that members of your organization take on that collection. You can view:

* If an alias was added or removed from an artifact version.
* If an artifact version was added or removed from a collection.

For both actions, you can view the user that performed the action and the date the action occurred.

To view a collection's action history:

1. Navigate to the W\&B Registry.
2. Select the collection you want to view its action history.
3. Select the dropdown menu next to the collection name.
4. Select the **Action History** option.
