# Source: https://dagshub.com/docs/use_cases/reproduce_experiment_results/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/use_cases/reproduce_experiment_results.md "Edit this page")

# Reproduce experiment results[¶](#reproduce-experiment-results "Permanent link")

DagsHub enables its users to compare and reproduce results of ML experiments with a click of a button. â€œHow?â€?, you ask? Let\'s see how it works.

[![Reproduce an Experiment](../assets/reproduce/reproduce_single_experiment.png)](../assets/reproduce/reproduce_single_experiment.png)

## How DagsHub achieves full reproducibility?[¶](#how-dagshub-achieves-full-reproducibility "Permanent link")

DagsHub achieves full reproducibility of ML experiments by leveraging the capabilities of Git, [DVC](../../integration_guide/dvc/) or [Data Engine](../../feature_guide/data_engine/), and [MLflow](../../integration_guide/mlflow_tracking/). This combination of tools allows for comprehensive tracking and versioning of project components.

With Git and DVC/Data Engine, we can encapsulate the version of all ML project components, including code, data, configurations, annotations, models, etc., as a single \"package\". This \"package\" becomes the single source of truth of our project.

When tracking the experiments with MLflow, it automatically detects if the code is executed within a Git repository, fetches the current Git commit, and logs it to DagsHub. If you use DVC, your data file\'s version will be contained in this commit. When you use Data Engine, calling `ds.all()` or `ds.log_to_mlflow()` logs the dataset including the current query to the experiment.

The commit and dataset is associated under the experiment tab with each run, and traced back with a click of a button, providing the version of all components to unlock full reproducibility.

Additionally, if the model is logged using MLflow, it will be recorded to DagsHub servers and found in the artifacts tab at the bottom of the experiment page.

## Starting point[¶](#starting-point "Permanent link")

To begin, we assume you have [created a project on DagsHub](../../quick_start/create_new_project/). We also assume your code is versioned with Git, [data is versioned using DVC](../../quick_start/version_data/) or your [dataset is versioned](../data_engine/version_datasets/), and model versioned using either DVC or MLflow. Additionally, experiments should be [tracked using MLflow](../../integration_guide/mlflow_tracking/). These components form the foundation for reproducibility.

## How to choose the best ML experiment?[¶](#how-to-choose-the-best-ml-experiment "Permanent link")

Before we reproduce an experiment, we need to first choose the experiment that provides the best results. To do so, weâ€™ll click on the [experiment tab](https://dagshub.com/docs/feature_guide/experiment_tracking/index.html), and [sort the table](https://dagshub.com/docs/feature_guide/experiment_tracking/#sort-experiments) based on our golden metric.

[![Experiments tab](../assets/reproduce/experiments_tab.png)](../assets/reproduce/experiments_tab.png)

But is it enough to simply choose the first experiment in the sorted table? Real-life projects are not a Kaggle competition. We often try to optimize experiments based on multiple metrics and parameters. For that, weâ€™ll choose the first X experiments, and [compare them](https://dagshub.com/docs/feature_guide/experiment_tracking/#how-to-compare-experiments) to make a data-driven dissection.

~Comparing\ experiments\ using\ the\ UI~

## How to reproduce an ML experiment on DagsHub?[¶](#how-to-reproduce-an-ml-experiment-on-dagshub "Permanent link")

To reproduce this experiment, all you need to do is click on the code icon. Thatâ€™s it! DagsHub will lead you to the Git commit of the experimentâ€™s run with the version of all project components that provided the experiment results

[![Reproduce an Experiment](../assets/reproduce/reproduce_single_experiment.png)](../assets/reproduce/reproduce_single_experiment.png)

## How to reproduce an ML experiment locally?[¶](#how-to-reproduce-an-ml-experiment-locally "Permanent link")

To reproduce the above experiment on a local machine, we will use Git and DVC in the following steps:

1.  Copy the Git commit hash from DagsHub
2.  Use Git to retrieve that commit `git checkout <commit-hash>`
3.  For retrieving data:
    1.  If you used DVC: Use DVC to pull the version of the data and model by running `dvc pull -r <remote-name>`
    2.  If you\'re versioning your dataset with data engine, simply click on the dataset button of the experiment, then click on use this dataset button and copy the code.

### How to retrieve MLflow artifacts from DagsHub remote server?[¶](#how-to-retrieve-mlflow-artifacts-from-dagshub-remote-server "Permanent link")

To retrieve a version of artifacts (e.g., model, data) tracked by MLflow, follow these steps:

1.  Go to the [MLflow UI on DagsHub](https://dagshub.com/docs/integration_guide/mlflow_tracking/index.html#how-to-launch-the-dagshub-mlflow-ui)
2.  Copy the URI pointing to the the artifacts
3.  Run the following command:

    import mlflow

    mlflow.artifacts.download_artifacts(artifact_uri="<copied_artifact_uri>")

The `artifact_uri` can point to:

- a run `"runs:/c82f6add249f4b578241932d5b9bff74/finetuned"`, or
- a model `"models:/SquirrelDetector/5"`

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).