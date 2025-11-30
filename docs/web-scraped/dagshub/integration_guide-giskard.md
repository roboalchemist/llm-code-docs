# Source: https://dagshub.com/docs/integration_guide/giskard/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/giskard.md "Edit this page")

# Giskard

[Giskard](https://www.giskard.ai/) is an open-source AI quality management system dedicated to ML models.

Giskard provides a suite of tools for scanning, testing, debugging, and monitoring all AI models, from tabular to LLMs.

**With DagsHub and Giskard, you can easily debug your models and view Giskard\'s vulnerability and testing reports.** This functionality is based on the [MLflow](../mlflow_tracking/) server that comes with each DagsHub project

Check out [the example repo](https://dagshub.com/Dean/Giskard-Integration-Demo) to see a Tabular and LLM testing example, or open the examples directly in Colab:

Tabular Example: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https%3a%2f%2fdagshub.com%2fDean%2fGiskard-Integration-Demo%2fraw%2fd1961e79a0962fe2c18257bfd829f2eb3fa0dfb5%2fgiskard_dagshub_tabular_demo.ipynb)

LLM Example: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https%3a%2f%2fdagshub.com%2fDean%2fGiskard-Integration-Demo%2fraw%2fd1961e79a0962fe2c18257bfd829f2eb3fa0dfb5%2fgiskard_dagshub_LLM_RAG.ipynb)

## How does Giskard work with DagsHub?[¶](#how-does-giskard-work-with-dagshub "Permanent link")

By setting DagsHub as the logger of the experiment, it authenticates your DagsHub user and uses MLflow and DagsHub Client to log the information of the experiment to your DagsHub repository. We use built-in Giskard callbacks to log the metrics and parameters of every run using MLflow, and the artifacts, as in data and trained model, using either MLflow or DVC. You can find the source code of the logger in the [Giskard repository](https://github.com/Giskard/Giskard/blob/master/Giskard/loggers/dagshub_logger.py).

## How to log Giskard Vulnerability & Testing Reports to DagsHub?[¶](#how-to-log-giskard-vulnerability-testing-reports-to-dagshub "Permanent link")

### Setup[¶](#setup "Permanent link")

We will start by installing Giskard, DagsHub, and MLflow by running the following command from the CLI

    pip install giskard mlflow dagshub

Next, log the Giskard report to your repository\'s MLflow server, simply use `dagshub.init()` as following:

    # Only DagsHub related lines you need:
    import dagshub 

    # This will work if you have write access to the repo below, if you cloned it, please change the repo_owner to your user name
    dagshub.init(repo_name="your_repo_name", repo_owner="your_username")

### Perform the evaluation[¶](#perform-the-evaluation "Permanent link")

To make sure everything is installed correctly, and Giskard is now part of MLflow\'s evaluators, run:

    import mlflow
    mlflow.models.list_evaluators() # ['default', 'giskard']

The configuration of the Giskard evaluator can be done entirely through the evaluator_config argument that can yield 3 keys:

- `model_config`
- `dataset_config`
- `scan_config`

Read Giskard\'s [guides](https://docs.giskard.ai/en/latest/open_source/scan/index.html) for more information on how to set these variables.

Hereâ€™s the integration in a nutshell:

    evaluator_config = ,
                        "dataset_config": ,
                        "scan_config":    }}}

    with mlflow.start_run(run_name="my_run") as run:
      model_uri = mlflow.sklearn.log_model(..., pyfunc_predict_fn="predict_proba").model_uri
      mlflow.evaluate(model=model_uri,
                      model_type="classifier",
                      data=df_sample,
                      evaluators="giskard",
                      evaluator_config=evaluator_config)

### View the report[¶](#view-the-report "Permanent link")

If you\'re working with Python files, you can commit them to your DagsHub repository, or if you\'re in a Colab notebook, simply use:

    dagshub.notebook.save_notebook(repo="repo_owner/repo_name")

To save it to DagsHub.

To view it, click on the \"Go to MLflow UI\" button in the Experiments Tab: [![Go To MLflow UI](../assets/giskard/giskard_report_viewing.png)](../assets/giskard/giskard_report_viewing.png)

Then click on the experiment with the model you want to view the report for, and you\'ll see is at \"giskard-scan-results.html\" In the artifacts view: [![Giskard Report](../assets/giskard/giskard_report.png)](../assets/giskard/giskard_report.png)

**Congratulations, youâ€™re all set to track & view your Giskard reports using DagsHub**!

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).