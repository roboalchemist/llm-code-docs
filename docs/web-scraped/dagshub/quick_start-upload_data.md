# Source: https://dagshub.com/docs/quick_start/upload_data/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/quick_start/upload_data.md "Edit this page")

# Upload Data[¶](#upload-data "Permanent link")

Now that you\'ve [created your DagsHub project](../create_new_project/), or [connected an existing project](../connect_existing_project/), the next step is to get your data on DagsHub. The easiest way to do that is to upload your data to [DagsHub Storage](../../feature_guide/dagshub_storage/). DagsHub storage is a hosted S3-Compatible bucket that comes with every DagsHub repository. It\'s easy to use, and highly scalable.

If you already have your data in a storage bucket, check out the guide on [connecting external buckets](../connect_external_storage/). If you\'d like to use DVC to version your data files, check out the guide for [versioning data](../version_data/).

## Video Tutorial[¶](#video-tutorial "Permanent link")

# An error occurred. 

Unable to execute JavaScript.

## Step-by-Step Guide[¶](#step-by-step-guide "Permanent link")

### Installation and Setup[¶](#installation-and-setup "Permanent link")

Start by installing the DagsHub client. Simply type in the following:

    $ pip3 install dagshub

### Uploading the actual data[¶](#uploading-the-actual-data "Permanent link")

The structure of the upload command is very simple:

    $ dagshub upload --bucket <repo_owner>/<repo_name> <local_path> <remote_path>

Using all functionality of DagsHub\'s data access tools requires authentication, which by default will use an interactive OAuth flow. If you want to use persistent tokens, read our short guide about [authentication](https://dagshub.com/docs/client/reference/auth.html#authentication)

Let\'s assume your data is in a folder named `my_data/`, and that we\'d like to upload it to a folder called `dataset/` in our S3-Compatible storage in a repo called `my_project` owned by `DagsHub`. In your terminal, run:

    $ dagshub upload --bucket DagsHub/my_project my_data/ dataset/

If you prefer to upload the data in Python over the terminal, you can do that by running the following:

    dagshub.upload_files("<user_name>/<repo_name>", "<local_path>", remote_path="<remote_path>", bucket=True)

## Next Steps[¶](#next-steps "Permanent link")

Now that you\'ve uploaded your data files, you have your data alongside your code. That\'s a great first step, but to train a model, you\'ll need to create and curate a dataset. Learn how to actually [turn your data into a dataset](../create_dataset/).

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).