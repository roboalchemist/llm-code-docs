# Source: https://dagshub.com/docs/integration_guide/hugging_face/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/hugging_face.md "Edit this page")

# Hugging Face Transformers[¶](#hugging-face-transformers "Permanent link")

The Hugging Face Transformers library is an open-source machine-learning library. It is built on top of PyTorch and TensorFlow and provides a set of pre-trained models for natural language processing tasks. With Hugging Face Transformers, developers and researchers can easily fine-tune the pre-trained models on their own datasets, or even train their own models from scratch with ease.

**With DagsHub, you can easily log the experiments you run with Hugging Face Transformers to a remote server with minimal changes to your code.**

This includes versioning raw and processed data with DVC, as well as logging experiment metrics, parameters, and trained models with MLflow. This integration enables you to continue using the familiar MLflow interface, while also facilitating collaboration with others, comparing results from different runs, and making data-driven decisions with ease.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https%3A//dagshub.com/Nikitha-Narendra/Sentiment-Analysis-Hugging-Face/raw/main/Sentiment-Analysis.ipynb)

## How do Hugging Face Transformers work with DagsHub?[¶](#how-do-hugging-face-transformers-work-with-dagshub "Permanent link")

DagsHub leverages the hooks developed by Hugging Faceâ€™s Transformers library to inject code at specific points during the training run. These code snippets log information regarding the training run, like metrics and artifacts, to the DagsHub remote using information provided using environment variables set before the trainer is run.

## How to log experiments with Transformers and DagsHub?[¶](#how-to-log-experiments-with-transformers-and-dagshub "Permanent link")

Log your transformer experiments in 3 simple steps:

### Install DagsHub[¶](#install-dagshub "Permanent link")

Mac-os, Linux, Windows

### Configure DagsHub[¶](#configure-dagshub "Permanent link")

    import dagshub 
    import os

    dagshub.init(repo_name='Repository-Name', repo_owner='Username')
    os.environ["HF_DAGSHUB_LOG_ARTIFACTS"]= "True" # optional; if disabled, only logs metrics!

- `dagshub.init` configures your DagsHub account and repository, including the remote Mlflow tracking server and DagsHub Storage, with your local machine. If the repository you provide as input doesnâ€™t exist, it will automatically create it for you.

- Running this command requires authenticating your DagsHub user. If you want to automate this process, you need to set your [DagsHub Token](https://dagshub.com/user/settings/tokens) under `DAGSHUB_USER_TOKEN` environment variable.

You need to set the environment variable before you initialize the `Trainer`

Optional Environment Variables

The following are optional environmental variables that can be configured.

    os.environ["HF_DAGSHUB_MODEL_NAME"] = "model name" # defaults to 'main'
    os.environ["BRANCH"] = "branch" # defaults to 'main'

### Configure Hugging Face Transformers[¶](#configure-hugging-face-transformers "Permanent link")

Mac-os, Linux, Windows

------------------------------------------------------------------------

**Great job!** The integration has been successfully finished. Transformers will automatically recognize the activation of DagsHub integration and include our hook in your pipeline. Consequently, every run will be logged to your DagsHub repository.

### Additional Resources[¶](#additional-resources "Permanent link")

- [DagsHub x Hugging Face](https://dagshub.com/blog/dagshubs-integration-with-huggingface/) - learn more about DagsHub x Hugging Face Transformers integration.
- [Example notebook](https://colab.research.google.com/#scrollTo=tf0hipfTowl_&fileId=https%3A//dagshub.com/Nikitha-Narendra/Sentiment-Analysis/raw/main/Sentiment-Analysis.ipynb) - create your own transformer model and track your experiments.

### Known Issues, Limitations & Restrictions[¶](#known-issues-limitations-restrictions "Permanent link")

The artifacts created during training fail to get overridden if the same experiment is run multiple times. However, the experiments are still logged and can be tracked.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).