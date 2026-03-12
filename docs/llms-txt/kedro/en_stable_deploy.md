# Source: https://docs.kedro.org/en/stable/deploy/index.md

# Deployment

## Overview

In this section we provide guides for different deployment methods; your choice will depend on a range of factors.

If you decide to deploy your Kedro project onto a single machine, you should consult our [guide to single-machine deployment](https://docs.kedro.org/en/stable/deploy/single_machine/index.md), and decide whether to:

- [use Docker for container-based deployment](https://docs.kedro.org/en/stable/deploy/single_machine/#container-based)
- [use package-based deployment](https://docs.kedro.org/en/stable/deploy/single_machine/#package-based)
- [use the CLI to clone and deploy your codebase to a server](https://docs.kedro.org/en/stable/deploy/single_machine/#cli-based)

If your pipeline is sizeable, you may want to run it across separate machines, so will need to consult our [guide to distributed deployment](https://docs.kedro.org/en/stable/deploy/distributed/index.md).

```
flowchart TD
    A{Can your Kedro pipeline run on a single machine?} -- YES --> B[Consult the single-machine deployment guide]
    B --> C{Do you have Docker on your machine?}
    C -- YES --> D[Use a container-based approach]
    C -- NO --> E[Use the CLI or package mode]
    A -- NO --> F[Consult the distributed deployment guide]
    F --> G["What distributed platform are you using?<br/><br/>Check out the guides for:<br/><br/><li>Airflow</li><li>Amazon SageMaker</li><li>AWS Step functions</li><li>Azure</li><li>Dask</li><li>Databricks</li><li>Kubeflow Pipelines</li><li>Prefect</li><li>Vertex AI</li>"]
```

## Deployment methods

The following pages provide information for deployment to, or integration with, the following:

- [Airflow](https://docs.kedro.org/en/stable/deploy/supported-platforms/airflow/index.md)
- [Amazon SageMaker](https://docs.kedro.org/en/stable/deploy/supported-platforms/amazon_sagemaker/index.md)
- [Amazon EMR Serverless](https://docs.kedro.org/en/stable/deploy/supported-platforms/amazon_emr_serverless/index.md)
- [AWS Step functions](https://docs.kedro.org/en/stable/deploy/supported-platforms/aws_step_functions/index.md)
- [Azure](https://docs.kedro.org/en/stable/deploy/supported-platforms/azure/index.md)
- [Dagster](https://docs.kedro.org/en/stable/deploy/supported-platforms/dagster/index.md)
- [Dask](https://docs.kedro.org/en/stable/deploy/supported-platforms/dask/index.md)
- [Databricks](https://docs.kedro.org/en/stable/deploy/supported-platforms/databricks/index.md)
- [Kubeflow Pipelines](https://docs.kedro.org/en/stable/deploy/supported-platforms/kubeflow/index.md)
- [Prefect](https://docs.kedro.org/en/stable/deploy/supported-platforms/prefect/index.md)
- [Vertex AI](https://docs.kedro.org/en/stable/deploy/supported-platforms/vertexai/index.md)

Warning

We also have legacy documentation pages for the following deployment targets, but these have not been tested against recent Kedro releases and we cannot guarantee them:

- for [Argo Workflows](https://docs.kedro.org/en/stable/deploy/supported-platforms/argo/index.md)
- for [AWS Batch](https://docs.kedro.org/en/stable/deploy/supported-platforms/aws_batch/index.md)

## Effective node grouping for deployment

Effective node grouping makes deployments easier to manage and update. It also improves performance by using resources more efficiently and enables pipelines to handle larger datasets as they scale across different environments. To learn more about grouping nodes using pipelines, tags, and namespaces, follow our detailed guide:

- [Node Grouping in Kedro](https://docs.kedro.org/en/stable/deploy/nodes_grouping/index.md)
