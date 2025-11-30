# Source: https://dagshub.com/docs/integration_guide/dvc/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/dvc.md "Edit this page")

# DVC[¶](#dvc "Permanent link")

[DVC](https://dvc.org) is an open-source version control tool for machine learning projects designed to handle large files, data sets, machine learning models, and metrics. It works on top of Git to easily integrate with your existing Git code repositories. DagsHub integration with DVC includes a fully configured [remote object storage](../../feature_guide/dagshub_storage/) managed by DVC, showing and diffing DVC tracked files hosted on DagsHub Storage or S3 compatible, and Data Pipeline visualization.

The easiest way to start using DVC with DagsHub is to [version your data with the DagsHub client](../../quick_start/version_data/).

## How does the integration of DagsHub with DVC work?[¶](#how-does-the-integration-of-dagshub-with-dvc-work "Permanent link")

### DagsHub Storage[¶](#dagshub-storage "Permanent link")

DagsHub automatically configures a remote object storage for every repository with 100 GBs of free space. The storage can be managed by DVC and easily configured with any machine. Using the DVC pointer files (`.dvc`) and the `dvc.lock` file, host on the Git commit, DagsHub parsed the storage and displays the DVC tracked files under the Files tab.

Learn how to use [DagsHub Storage](../../feature_guide/dagshub_storage/)

### External Storage Buckets[¶](#external-storage-buckets "Permanent link")

DagsHub supports visualizing and managing DVC data stored on any AWS S3, Google Cloud Storage, Azure Blob Storage, or any S3 Compatible storage including MinIO.

Learn how to [configure your external bucket](../set_up_remote_storage_for_data_and_models/).

### Visualize DVC pipelines[¶](#visualize-dvc-pipelines "Permanent link")

DagsHub parses the dvc.lock and dvc.yaml file to create the interactive data pipeline. The pipeline is versioned and holds valuable information about the different files, metrics, and data steps.

## How to use DVC with DagsHub?[¶](#how-to-use-dvc-with-dagshub "Permanent link")

### DagsHub Storage[¶](#dagshub-storage_1 "Permanent link") 

#### Configure DagsHub Storage with your machine[¶](#configure-dagshub-storage-with-your-machine "Permanent link")

1.  Go to your repository homepage
2.  Click on the remote button, and select the Data tab.
3.  Select DVC
4.  Copy the commands to set your local machine with DagsHub Storage

~DVC\ remote~

1.  Enter a terminal in your project, paste the commands and run them

    ::: highlight
        dvc remote add origin s3://dvc
        dvc remote modify origin endpointurl https://dagshub.com/<DagsHub-user-name>/<repo_name>.s3
        dvc remote modify origin --local access_key_id <Token>
        dvc remote modify origin --local secret_access_key <Token>
    :::

    Why \--local?

    Everything you configure without `--local` will end up in the `.dvc/config` file, which is tracked by git, and appear in you repository. Personal info like authentication details should always be kept local.

**That\'s it! You can now pull data from your remote cache**

**Note:** *You need to be inside a Git and DVC directory for this process to succeed. To learn how to do that, please follow the [first part](../../quick_start/create_new_project/) of the Get Started section.*

#### Pulling data[¶](#pulling-data "Permanent link")

    dvc pull -r origin

#### Pushing data[¶](#pushing-data "Permanent link")

    dvc push -r origin

### Visualize DVC pipelines:[¶](#visualize-dvc-pipelines_1 "Permanent link") 

1.  Run a DVC pipeline
2.  Version the dvc.lock and dvc.yaml files using Git.
3.  Version with Git the files not tracked by DVC.
4.  Push the Git and DVC tracked files to DagsHub. **Note:** *You can follow the [Pipeline tutorial](../../tutorials/pipeline_tutorial/) to learn how to build a DVC pipeline*

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).