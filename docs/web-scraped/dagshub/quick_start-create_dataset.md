# Source: https://dagshub.com/docs/quick_start/create_dataset/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/quick_start/create_dataset.md "Edit this page")

# Create a Dataset[¶](#create-a-dataset "Permanent link")

After [uploading](../upload_data/), [connecting](../connect_external_storage/), or [versioning](../version_data/), we have our data files as part of our DagsHub repository. That\'s a great first step, but in order to build models with it, we need to turn this heap of files into a proper dataset. The next step in that process is to create a DagsHub Dataset.

For the purpose of this quick start, we assume you\'ve already uploaded, connected or added a data version into your project.

## Video Tutorial[¶](#video-tutorial "Permanent link")

# An error occurred. 

Unable to execute JavaScript.

## Step-by-Step Guide[¶](#step-by-step-guide "Permanent link")

### UI Flow[¶](#ui-flow "Permanent link")

1.  In your project containing the data, click on the \"Datasets tab\".

    <figure data-markdown="span">
    <a href="../assets/create_dataset/datasets_tab.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/create_dataset/datasets_tab.png" alt="Datasets Tab" /></a>
    <figcaption>Datasets Tab</figcaption>
    </figure>

2.  Then click on \"Add New Source\".

    <figure data-markdown="span">
    <a href="../assets/create_dataset/add_source.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/create_dataset/add_source.png" alt="Add Datasource" /></a>
    <figcaption>Add New Datasource</figcaption>
    </figure>

3.  Now, you\'ll need to select the location of your data files. This can be any folder in your project files, DagsHub Storage, or any connected storage. You can also give it a name - the default name is the folder name.

    <figure data-markdown="span">
    <a href="../assets/create_dataset/folder_select.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/create_dataset/folder_select.png" alt="Select Folder &amp; Datasource Name" /></a>
    <figcaption>Select Folder &amp; Datasource Name</figcaption>
    </figure>

4.  You\'re done. You\'ll be redirected to your datasource, and see it scanning (the orange dot next to the name). You\'ll be able to see datapoints that have already been scanned and start working without needing to wait for scanning to finish. Once scanning is done, the dot will turn green.

    <figure data-markdown="span">
    <a href="../assets/create_dataset/success.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/create_dataset/success.png" alt="Datasource Successfully Created" /></a>
    <figcaption>Datasource Successfully Created</figcaption>
    </figure>

5.  **Deleting a Datasource** - To delete a datasource, click back to the datasets tab, then click on the three dots at the side of the datasource row, then click on \"Delete this source\". The system will ask you to make sure this is what you want to do, since deleting a datasource will irreversibly delete all the metadata (it won\'t delete the underlying files, but you will lose all enrichments and metadata).

    <figure data-markdown="span">
    <a href="../assets/create_dataset/delete_datasource.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/create_dataset/delete_datasource.png" alt="Delete a Datasource" /></a>
    <figcaption>Delete a Datasource</figcaption>
    </figure>

### Python Client Flow[¶](#python-client-flow "Permanent link")

1.  Start by installing the DagsHub client. Simply type in the following:

    ::: highlight
        $ pip3 install dagshub
    :::
2.  Run the following code to create the datasource:

    ::: highlight
        from dagshub.data_engine import datasources

        ds = datasources.create_datasource(
          repo="<user_name>/<repo_name>", # User name and repository name separated by a "/"
          name="awesome-datasource", # Name of your datasource
          path="s3://<repo_name>/<path_to_data_folder>" # Path to your data folder in your repo, this example is for a path inside DagsHub Storage, for a different bucket or files in the repo, use the appropriate path.
        ) 
    :::
3.  **Deleting the Datasource** - To delete the datasource, simply run:

    ::: highlight
        ds.delete_source()
    :::

## Next Steps[¶](#next-steps "Permanent link")

Now that you have your datasource ready, you can go ahead and [add enrichments](../add_edit_metadata/), or [query](../query_data/) to curate it and create datasets.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).