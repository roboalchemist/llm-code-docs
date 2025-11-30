# Source: https://dagshub.com/docs/quick_start/version_data/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/quick_start/version_data.md "Edit this page")

# Version Data[¶](#version-data "Permanent link")

After [creating](../create_new_project/) or [connecting](../connect_existing_project/) your project, you\'ll need to add your project\'s data. For most cases, we recommend [uploading your data](../upload_data/) to DagsHub storage, and relying on [Dataset Versioning](../../use_cases/data_engine/version_datasets/) for reproducibility - since this approach is faster and more scalable.

However, if your data files change, for example if you overwrite a file\'s content, you\'ll need to version your data files as well to achieve full reproducibility.

For data file versioning, DagsHub fully supports vanilla DVC, while also providing DagsHub Client, which leverages DVC under the hood but makes using it more convenient.

**DagsHub is the easiest way to work with DVC. If you\'re already familiar with DVC and want to use it, [here is a guide on using DVC directly with DagsHub](../../integration_guide/dvc/).**

The main advantage of using DagsHub Client over vanilla DVC is that it utilizes DagsHub backend capabilities to calculate the DVC hashes without conducting any action locally or requiring having the entire folder content locally.

## Video Tutorial[¶](#video-tutorial "Permanent link")

# An error occurred. 

Unable to execute JavaScript.

## Step-by-Step Guide[¶](#step-by-step-guide "Permanent link")

Let\'s see how to our data directory with the DagsHub Client. With the Client, you can version your data from the CLI or Python scripts to enable integrations into your project pipeline.

**For the purpose of this guide, let\'s assume your data is in a folder called `data/`**

### Installing DagsHub Client[¶](#installing-dagshub-client "Permanent link")

We will start by installing DagsHub Client using pip:

    pip install dagshub

### Version data from CLI[¶](#version-data-from-cli "Permanent link")

In your project\'s folder, put your data files in your `data/` folder, then run the following command:

    dagshub upload --update --versioning dvc --message "<commit_message>" "<repo_owner>/<repo_name>" "<local_path>" "<remote_path>"

Options:

    -m, --message TEXT           Commit message for the upload
    -b, --branch TEXT            Branch to upload the file to
    --update                     Force update existing files/directories
    -v, --verbose                Verbosity level
    -q, --quiet                  Suppress print output
    --host TEXT                  DagsHub instance to which you want to login
    --versioning [git|dvc|auto]  Versioning system to be used to upload the file(s)
    --bucket                     Upload the file(s) to the repo's DagsHub Storage bucket (s3-compatible)
    --help                       Show this message and exit.

The output will look as following:

    dagshub upload --update --versioning dvc --message "Adding raw data" "my_user/my_repo" "data/" "data/"
        â  Uploading files... ââââââââââââââââââââââââââââââââââââââââ   0% -:--:--
        Uploading files (1) to "my_user/my_repo"...
        Upload finished successfully!
        Directory upload complete, uploaded n files

### Version data using Python[¶](#version-data-using-python "Permanent link")

You can also create new versions using the DagsHub Client in Python, below is the same example as before by in Pythonic form.

    dagshub.upload_files("<user_name>/<repo_name>", "<local_path>", remote_path="<remote_path>", versioning="dvc")

By conducting this action, the data directory is uploaded to DagsHub Storage, versioned by DVC, and the new `data.dvc` pointer file is committed to Git.

## Results[¶](#results "Permanent link")

Now, our DagsHub repository will look like this:

[![Project After Data Push](../assets/version_data/project_after_data_push.jpeg)](../assets/version_data/project_after_data_push.jpeg)

And we\'ll be able to see our data file in the `data/` folder:

[![Project Data Preview](../assets/version_data/project_data_preview.jpeg)](../assets/version_data/project_data_preview.jpeg)

DagsHub\'s Data Catalog

As we can see in the image above, DagsHub displays the content of the files (e.g. CSV, YAML, image, etc.), tracked by both Git and DVC. In this case, the CSV file, tracked by DVC, is displayed in a table that you can filter and compare to different commits.

Since DagsHub client does all the hash calculation and DVC file creation on the DagsHub remote, making this process short and simple, we\'d like to pull the latest commit from DagsHub. We will do it with Git by running the following command:

    git pull

## Next Steps[¶](#next-steps "Permanent link")

Now that you\'ve versioned your data files, you have your data alongside your code. That\'s a great first step, but to train a model, you\'ll need to create and curate a dataset. Learn how to actually [turn your data into a dataset](../create_dataset/).

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).