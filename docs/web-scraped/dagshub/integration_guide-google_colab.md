# Source: https://dagshub.com/docs/integration_guide/google_colab/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/google_colab.md "Edit this page")

# Google Colab[¶](#google-colab "Permanent link")

[Google Colaboratory](https://colab.research.google.com/) , or \"Colab\" for short, is a free Jupyter notebook environment that runs entirely in the cloud. It does not require any setup, can be shared easily with team members, and provides free access to GPUs. DagsHub provides its users with Colab Notebook templates for various tasks, such as fully configuring DagsHub with Colab runtime, transferring data from Google Drive to DagsHub Storage, tutorials, and more.

## How does DagsHub work with Google Colab?[¶](#how-does-dagshub-work-with-google-colab "Permanent link")

DagsHub is officially integrated with Google Colab, enabling users to:

- [Open notebooks in a Colab environment directly](#open-a-notebook-from-your-dagshub-repo-in-colab) from DagsHub projects (free GPU included)
- [Version and commit Colab notebooks](#versioning-your-colab-notebook-using-git-or-dvc-on-dagshub) back using Git or DVC.
- [Use DagsHub Storage Buckets](#dagshub-storage-buckets-integration-with-google-colab) as a scalable, ML-first alternative to Google Drive, inside Colab notebooks

Seamlessly build, train, and collaborate on ML models with ZERO MLOps friction.

To see an example notebook:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https%3a%2f%2fdagshub.com%2fDagsHub%2fDagsHubxColab%2fraw%2fmain%2fDagsHub_x_Colab-DagsHub_Storage.ipynb)

You can easily access your DagsHub projects code, data and experiments from any Colab environment. By setting your DagsHub credentials, you\'ll be able to clone your code, and pull your data hosted on DagsHub Storage, and then log experiments to the project\'s experiment tracking server.

## How to use DagsHub with Google Colab?[¶](#how-to-use-dagshub-with-google-colab "Permanent link")

### Open a notebook from your DagsHub repo in Colab[¶](#open-a-notebook-from-your-dagshub-repo-in-colab "Permanent link")

To open a notebook from DagsHub in Colab, just navigate to your notebook file preview on DagsHub â€" there you will see the \"Open in Colab\" button which will open the notebook in Colab.

~Adding\ topics\ with\ the\ UI~

Info

\"Open in Colab\" button only works in public projects currently. To open in Colab in a private repo, simply download the file, and upload it to Colab.

### DagsHub Storage Buckets Integration with Google Colab[¶](#dagshub-storage-buckets-integration-with-google-colab "Permanent link")

DagsHub Storage Buckets offer an S3-Compatible, ML-focused storage solution, now seamlessly integrated with Google Colab. This integration enables easy and scalable access to projects working with large-scale datasets, overcoming the limitations of Google Drive and traditional cloud storage solutions for ML workflows.

#### Uploading Data to Your DagsHub Storage Bucket[¶](#uploading-data-to-your-dagshub-storage-bucket "Permanent link")

Use the DagsHub client for an easy data upload process. The client supports both command line and Python API methods for uploading your datasets directly into the DagsHub Storage Bucket.

PythonCommand Line

#### Mounting & Syncing with DagsHub Storage Buckets[¶](#mounting-syncing-with-dagshub-storage-buckets "Permanent link")

Unlike Google Drive, DagsHub Storage Buckets are designed with ML use cases in mind, offering a more scalable and robust backend. You can easily mount your DagsHub Storage Bucket to your Colab instance, facilitating direct access to your data for model training and inference.

##### Sync a Local Folder to DagsHub Storage[¶](#sync-a-local-folder-to-dagshub-storage "Permanent link")

To sync a local folder to DagsHub Storage, simply run:

    dagshub.storage.sync("<user_name>/<repo_name>", "<local_path>", "<remote_path>")

Sync a local folder with your DagsHub storage remote by specifying the paths. This command ensures your local dataset is mirrored in the DagsHub Storage Bucket.

##### Mounting DagsHub Storage to Colab[¶](#mounting-dagshub-storage-to-colab "Permanent link")

Mount your DagsHub Storage Bucket to a Colab notebook for direct file access. If needed, you can specify a custom mount path, by providing a `path=` argument. You can also provide `cache=True` to do smart caching that will accelerate training (at the cost of taking up more disk space).

    mount_path = dagshub.storage.mount("<user_name>/<repo_name>")

To unmount the bucket, simply run:

    dagshub.storage.unmount("<user_name>/<repo_name>", mount_path)

Remounting Buckets

In case of errors or if the Colab cell execution breaks, you can easily remount your DagsHub Storage Bucket using the dagshub.storage.mount() function. This ensures continuous access to your data without disruption.

### Versioning your Colab notebook using Git or DVC on DagsHub[¶](#versioning-your-colab-notebook-using-git-or-dvc-on-dagshub "Permanent link")

Integrating DagsHub and Colab introduces a significant improvement in notebook version control, as users can use DVC to version large notebooks that Git has trouble facilitating. DagsHub lets you diff notebooks and comment on notebook cells which unlocks collaboration for ML teams, without needing third-party platforms or sharing screenshots across Slack

To version your notebook with the DagsHub Client (run `pip install dagshub` to install), use the `save_notebook` function as follows:

    from dagshub.notebook import save_notebook

    save_notebook(repo="<repo_owner>/<repo_name>")

With the following argument:

- `repo` (str): your DagsHub repository in the format of `<repo_owner>/<repo_name>`

You can also use the following optional arguments:

- `path` (str): Where to save the notebook within the repository (including the filename). If the filename is not specified, we\'ll save it as \"notebook-.ipynb\" under the specified folder
- `branch` (str): The branch under which the notebook should be saved. Will commit to the default repo branch if not specified
- `commit_message` (str): The commit message for the update
- `versioning` (str): `['git'|'dvc']` The VCS used to version the notebook

Alternative way to version your Colab notebook

In some cases the above function might fail due to Colab related issues. An alternative way to version your notebook is to download it locally, then in an environment with `pip install dagshub` run the following snippet:

    import dagshub
    dagshub.upload_files(repo="<repo_owner>/<repo_name>", local_path="<path/to/notebook.ipynb>", remote_path="<path/in/remote/notebook.ipynb>", commit_message="<commit_message>")

## Copy your data from GDrive to DagsHub[¶](#copy-your-data-from-gdrive-to-dagshub "Permanent link")

Follow this notebook to move your data from Google Drive to DagsHub Storage Buckets easily:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https%3a%2f%2fdagshub.com%2fDagsHub%2fDagsHubxColab%2fraw%2fmain%2fCopy_Data_From_GDrive_To_DagsHub_Storage.ipynb)

## Other Resources[¶](#other-resources "Permanent link")

- [Hello World Vision](https://colab.research.google.com/#fileId=https%3a%2f%2fdagshub.com%2fDagsHub%2fhello-world-vision%2fraw%2fmain%2fhello-world-vision.ipynb) - Try DagsHub without installing anything locally. The primary goal of this notebook is to help you learn the basic features and usage of DagsHub while maintaining a relatively clean environment. By following this notebook, you will create your first hello-world project on DagsHub.
- [Tensorflow](https://colab.research.google.com/drive/1TrN7YEgiIzt7EelvshJPx2n4j-Qa6LBf?usp=sharing) , [fast.ai](https://colab.research.google.com/drive/1DhHzI5blVbniFwx98EKXYSi0z_Icm07t?usp=sharing) - Learn how to log MLflow Experiments to your DagsHub\'s MLflow Tracking server by following a few steps.
- [DagsHub x GitHub](https://colab.research.google.com/drive/18k1aiqjUoWp04sCUlYBItW3l8cU6KPNV?usp=sharing) - Learn how to use all the benefits DagsHub has to offer in your GitHub project by following this notebook.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).