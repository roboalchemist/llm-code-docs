# Source: https://dagshub.com/docs/use_cases/data_engine/connect_datasource/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/use_cases/data_engine/connect_datasource.md "Edit this page")

# Working with Datasources[¶](#working-with-datasources "Permanent link")

To start querying, visualizing, and generating new training-ready datasets, you first need to connect the data you want to work with. Connecting data sources can be done via the DagsHub UI, or the DagsHub Python Client.

Thereâ€™s no limitation on the amount of data sources per repository. Different data sources can point to the same bucket (or different paths within the same bucket) without being related to each other. This allows you to manage different metadata tables and use cases on the same raw data. Once the data source is created, DagsHub will scan it and automatically add metadata, such as file size to each data point as a meta-data field.

## Uploading or connecting data[¶](#uploading-or-connecting-data "Permanent link")

There are 3 ways to connect a data source:

1.  **[Use data you already have](#1-create-a-data-source-with-data-in-your-repository)** in your repository
2.  **[Upload new data](#2-create-a-data-source-by-uploading-new-data-to-your-repository)** to your repository
3.  **[Connect external storage](#3-create-data-source-from-external-storage)**, like AWS S3, GCS, Azure Blob Storage, MinIO, Ceph and any S3-Compatible storage to your repository

Select the approach that\'s relevant to you, then proceed to the next step.

### 1. Create a data source with data in your repository[¶](#1-create-a-data-source-with-data-in-your-repository "Permanent link") 

#### Using the DagsHub UI[¶](#using-the-dagshub-ui "Permanent link")

In your repository, navigate to the Datasets tab and click on the â€˜Add new sourceâ€™ button. [![add_new_source_button](../assets/connect_datasource/add_new_source_button.png)](../assets/connect_datasource/add_new_source_button.png)

Click on the â€˜Choose from existing dataâ€™ option. [![add_source_from_existing_data](../assets/connect_datasource/choose_existing_data_in_repo.png)](../assets/connect_datasource/choose_existing_data_in_repo.png)

Choose the folder that contains the data you want to work with, fill in the name you want to give to your data source, and click on the â€˜choose data as datasourceâ€™ button. [![select_data_folder](../assets/connect_datasource/choose_data_folder.png)](../assets/connect_datasource/choose_data_folder.png)

The new source will be added to the table. [![datasource_list_in_ui](../assets/connect_datasource/datasource_list_in_ui.png)](../assets/connect_datasource/datasource_list_in_ui.png) You can already use your data source while it is being loaded. Keep in mind that using the datasource while metadata is being generated means that some of the rows in the table might not be available.

#### Using the DagsHub Python client[¶](#using-the-dagshub-python-client "Permanent link")

    from dagshub.data_engine import datasources

    ds = datasources.create_from_repo(repo="UserName/RepoName", name="DataSourceName", path="/DataFolderName")

- `repo` - a string with the repo owner and name of the repository you want to work on.
- `name`- the name you want to give to your data source.
- `path` - the path of your data folder inside your repository, relative to the repo root. Data Engine will scan all files in this folder, and create the datasource from them.

case sensitivity

Properties are case-sensitive, make sure you use capitals when needed.

For example, for our [baby Yoda segmentation repo](https://dagshub.com/Simon/baby-yoda-segmentation-dataset), this is how to create a data source named `"default-datasource"`, pointing to the data under the `/images` folder at the root of the repository:

    ds = datasources.create_from_repo(
        repo="Simon/baby-yoda-segmentation-dataset", 
        name="default-datasource",
        path="/images"
    )

### 2. Create a data source by uploading new data to your repository[¶](#2-create-a-data-source-by-uploading-new-data-to-your-repository "Permanent link") 

To create data source with new data, you will first have to add the new data to your repository. There are 3 ways to upload new data to a DagsHub repository:

#### (Recommended) Upload data using [DagsHub client](../../../quick_start/upload_data/):[¶](#recommended-upload-data-using-dagshub-client "Permanent link")

    # Upload data to dagsHub repository
    dagshub upload <repo_owner>/<repo_name> <local_file_path> <path_in_remote>

#### Upload data using DVC[¶](#upload-data-using-dvc "Permanent link")

To learn how to upload your data with DVC, please check out the [tutorial](../../../tutorials/experiment_tutorial/)

#### Use the DagsHub UI[¶](#use-the-dagshub-ui "Permanent link")

Navigate to the â€˜Datasetsâ€™ tab and click on the â€˜Add new sourceâ€™ button. Choose the â€˜Upload new data directlyâ€™ option and follow the instructions: [![upload_new_data_to_repo](../assets/connect_datasource/choose_upload_new_data.png)](../assets/connect_datasource/choose_upload_new_data.png) This will present you with a notebook, that youâ€™ll be able to open in Google Colab, or download to run locally, which includes code snippets you can run to upload your files to DagsHub directly, and create a datasource from it.

### 3. Create data source from external storage[¶](#3-create-data-source-from-external-storage "Permanent link") 

External Storage Credentials

When working with external storage, note that you\'ll need to set up proper permissions for your remote storage. To read more about how this is done, check out the [external storage integration guide](../../../integration_guide/set_up_remote_storage_for_data_and_models/)

#### Using the DagsHub UI[¶](#using-the-dagshub-ui_1 "Permanent link") 

Click on the â€˜Add new sourceâ€™ button. [![add_new_source_button](../assets/connect_datasource/add_new_source_button.png)](../assets/connect_datasource/add_new_source_button.png)

Click on the â€˜Connect new remote storageâ€™ option. [![show_externalstorage_option](../assets/connect_datasource/mark_externalstorage_option.png)](../assets/connect_datasource/mark_externalstorage_option.png)

Choose the relevant provider and follow the integration instructions. [![show_storage_providers](../assets/connect_datasource/external_storage_providers.png)](../assets/connect_datasource/external_storage_providers.png)

You will need to provide DagsHub with the following:

- Bucket URL & Prefix
- Region
- Access Key ID
- Secret Access Key

Once your external storage is successfully connected, choose the folder that contains the data you want to work with, fill in the name you want to give to your data source, and click on the â€˜choose data as datasourceâ€™ button. [![choose_bucket_in_repo](../assets/connect_datasource/external_storage_chosen_datasource.png)](../assets/connect_datasource/external_storage_chosen_datasource.png)

The new source will be added to the table, but you can already use your data source while it is being loaded. [![externalstorage_source_displayed](../assets/connect_datasource/external_storage_datasource_display.png)](../assets/connect_datasource/external_storage_datasource_display.png)

Datasource availability

You can start using your data source while it is being scanned. Keep in mind that using the datasource while metadata is being generated means that some of the rows in the table might not be available.

#### Using the DagsHub Client[¶](#using-the-dagshub-client "Permanent link")

Before creating a data source from external storage, you will have to connect it to your repository using DagsHub UI.\
[![mark_settings_tab](../assets/connect_datasource/mark_settings_tab.png)](../assets/connect_datasource/mark_settings_tab.png)

Navigate to the Integration section. [![integrations_subtab](../assets/connect_datasource/mark_integration_in_settings.png)](../assets/connect_datasource/mark_integration_in_settings.png)

Choose the relevant provider and follow the integration instructions. [![add_new_source_button](../assets/connect_datasource/mark_externalstorage_in_settings.png)](../assets/connect_datasource/mark_externalstorage_in_settings.png) You will need to provide DagsHub with the following:

- Bucket URL & Prefix
- Region
- Access Key ID
- Secret Access Key

Once your external storage was successfully connected, use the following command to create a new data source with it:

    ds = datasources.create_from_bucket(
        repo="UserName/RepoName", 
        name="DataSourceName",
        path="s3://external-bucket-url/dataFolder"
    )

## View your connected datasources[¶](#view-your-connected-datasources "Permanent link")

To list all data sources in the repository, use the `get_datasources` command, which returns a list of datasource objects:

    ds_list = datasources.get_datasources("UserName/RepoName")

    # Get the second datasource in the list
    ds = ds_list[1]

For example, for our [baby Yoda segmentation repo](https://dagshub.com/Simon/baby-yoda-segmentation-dataset):

    ds_list = datasources.get_datasources("simon/baby-yoda-segmentation-dataset")

To get specific data source, use the `get_datasource` command:

    ds = datasources.get_datasource("UserName/RepoName", name="dataSourceName")

For example, for our [baby Yoda segmentation repo](https://dagshub.com/Simon/baby-yoda-segmentation-dataset):

    ds = datasources.get_datasource("simon/baby-yoda-segmentation-dataset", name="bucket-ds")

## Add new data points to a data source:[¶](#add-new-data-points-to-a-data-source "Permanent link")

### For data in your repository:[¶](#for-data-in-your-repository "Permanent link")

In case the data is located in a repository (tracked & versioned by DagsHub), Data Engine will automatically scan the data source for changes after uploading new data points and commiting. To add data points to your data source - simply upload the new data points to your repository. There are 2 ways to add data to your repository:

### **(Recommended)** Upload data using the [DagsHub client](https://dagshub.com/docs/feature_guide/direct_data_access/)[¶](#recommended-upload-data-using-the-dagshub-client "Permanent link")

    pip3 install dagshub

    # Upload data to dagshub repository
    dagshub upload <repo_owner>/<repo_name> <local_file_path> <path_in_remote>

Pro Tip

To upload data to your project\'s DagsHub-hosted S3 bucket, add the `--bucket` flag to the above command.

### Upload data using DVC[¶](#upload-data-using-dvc_1 "Permanent link") 

To learn how to upload your data with DVC, please check out the [tutorial](../../../tutorials/experiment_tutorial/).

### For data located in an external storage:[¶](#for-data-located-in-an-external-storage "Permanent link")

In cases where your data is located in an external bucket, Data Engine will automatically scan the bucket for changes every 24 hours - newly added data points will be available after scanning.

## Manual datasource Updates[¶](#manual-datasource-updates "Permanent link")

To make sure the data source is up to date, Data Engine scans the data source automatically and displays the changes immediately once scanning complete.

However, you can manually scan your data source for updates. To do that, use the following command:

    ds.scan_source()

or, click on the \'refresh\' icon in DagsHub UI: [![datasource_refresh_button](../assets/connect_datasource/refresh_button_ui.png)](../assets/connect_datasource/refresh_button_ui.png)

## Delete datasource[¶](#delete-datasource "Permanent link")

To delete a data source (the required permissions are Repository Admin), use the following function:

    ds.delete_source()

Warning

This is a destructive operation! If you delete the datasource, all the datapoints and metadata will be removed.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).