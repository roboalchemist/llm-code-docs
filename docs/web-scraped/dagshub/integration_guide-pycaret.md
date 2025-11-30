# Source: https://dagshub.com/docs/integration_guide/pycaret/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/pycaret.md "Edit this page")

# PyCaret

PyCaret is an open-source, low-code machine learning library in Python that simplifies the process of training and deploying machine learning models. It offers a wide range of functions and features that make it easy to go from preparing your data to deploying your model within seconds.

**With DagsHub, you can log the experiments you run with PyCaret to a remote server with minimal changes to your code.**

This includes versioning raw and processed data with [DVC](../dvc/), as well as logging experiment metrics, parameters, and trained models with [MLflow](../mlflow_tracking/). This integration enables you to continue using the familiar MLflow interface, while also facilitating collaboration with others, comparing results from different runs, and making data-driven decisions with ease.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https%3A//dagshub.com/DagsHub/Stock_Forecasting-PyCaret/raw/main/DagsHubxPyCaret-Stock_Forecasting.ipynb)

## How does PyCaret work with DagsHub?[¶](#how-does-pycaret-work-with-dagshub "Permanent link")

By setting DagsHub as the logger of the experiment, it authenticates your DagsHub user and uses MLflow and DagsHub Client to log the information of the experiment to your DagsHub repository. We use built-in PyCaret callbacks to log the metrics and parameters of every run using MLflow, and the artifacts, as in data and trained model, using either MLflow or DVC. You can find the source code of the logger in the [PyCaret repository](https://github.com/pycaret/pycaret/blob/master/pycaret/loggers/dagshub_logger.py).

## How to log PyCaret Experiments on DagsHub?[¶](#how-to-log-pycaret-experiments-on-dagshub "Permanent link")

### Configurations[¶](#configurations "Permanent link")

- We will start by installing PyCaret, DagsHub, and MLflow by running the following command from the CLI

  ::::: 
  ::: tabbed-labels
  Mac, Linux, Windows
  :::

  ::: tabbed-content
  :::
  :::::

- Configure DagsHub \[optional\] - To avoid the authentication process with DagsHub\'s servers, we can conduct one of the following options:

  1.  Log in using the dagshub client.

  ::::: 
  ::: tabbed-labels
  Mac, Linux, Windows
  :::

  ::: tabbed-content
  :::
  :::::

  ::: highlight
      dagshub login
      export MLFLOW_TRACKING_URI="<enter-your-MLflow-remote-DagsHub>"
  :::

  ### Run an Experiment[¶](#run-an-experiment "Permanent link")

- Choose any one of PyCaret\'s many Machine Learning models and set DagsHub as the logger during initialization. === \"Mac-os, Linux, Windows\"

  ::: highlight
      from pycaret.classification import * 
      s = setup(..... , log_experiment="dagshub" , ....)
  :::

Authentication

If the DagsHub Logger is not already authenticated on your local machine, the terminal will prompt you to enter theÂ `repo_owner/repo_name`Â and provide an authentication link. The repository and remote MLflow server will then be automatically initialized in the background.

**Congratulations, youâ€™re all set to track your PyCaret experiments using DagsHub**!

PyCaret will automatically detect that the integration is triggered and available and will ensure that it adds our hook to your pipeline. Now, when you run your code, you will see new runs appear in the experiment tables, with their status and origin

### Additional Resources[¶](#additional-resources "Permanent link")

- [DagsHub x PyCaret](https://dagshub.com/blog/how-to-use-pycaret-with-dagshub/) - a full tutorial that showcases how to use DagsHub with PyCaret.
- [Example notebook](https://colab.research.google.com/drive/1KblrpUywJ_iaiDOPmdXDIAIgfRYfeI1p?usp=sharing#scrollTo=to-GGu6cBVDY) - create your own transformer model and track your experiments.

### Known Issues, Limitations & Restrictions[¶](#known-issues-limitations-restrictions "Permanent link")

If you do not set the `ML_TRACKING_URI` environment variable, you will be prompted to enter the repo_owner/repo_name every time you run your experiment.

The latest feature of dagshub `dagshub.init` which configures your repository with MLflow configuration does not set this variable, hence this method will still trigger the prompt.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).