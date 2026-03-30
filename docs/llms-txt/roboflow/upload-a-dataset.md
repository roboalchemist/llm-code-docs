# Source: https://docs.roboflow.com/developer/python-sdk/upload-a-dataset.md

# Source: https://docs.roboflow.com/developer/command-line-interface/upload-a-dataset.md

# Upload a Dataset

You can upload datasets with images and/or annotations using the Roboflow CLI.

We have prepared a video that walks through how to upload a dataset:

{% embed url="<https://www.loom.com/share/19637984033a466b831af56f9404fa89>" %}

### Upload a Dataset with the CLI

You can use the following command to upload a dataset with the CLI:

```bash
roboflow import -w WORKSPACE_ID -p PROJECT_ID /path/to/dataset/folder
```

Above, set:

* `WORKSPACE_ID` to your Roboflow Workspace ID. [Learn how to find your Workspace ID.](https://docs.roboflow.com/developer/authentication/workspace-and-project-ids)
* `PROJECT_ID` to the ID of the Project within your Workspace to which you want to upload your data. [Learn how to find your Project ID.](https://docs.roboflow.com/developer/authentication/workspace-and-project-ids)
* `/path/to/dataset/folder` to the location of the dataset you want to upload.

You can upload data with the CLI for the following Project types:

* Object Detection
* Single-Label Classification

### Supported data.yaml formats

As of Roboflow CLI **v1.2.1**, the CLI now supports both list-style and key–value pair formatted class name mappings in `data.yaml` files during dataset uploads. This means you can use either of the following formatting styles within your `data.yaml` file:

```bash
nc: 3
names: ['Paper', 'Rock', 'Scissors']
...
```

OR

```yaml
...
nc: 3
names:
  0: Paper
  1: Rock
  2: Scissors
...
```
