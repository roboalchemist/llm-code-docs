# Source: https://dagshub.com/docs/integration_guide/set_up_remote_storage_for_data_and_models/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/set_up_remote_storage_for_data_and_models.md "Edit this page")

# Setup Remote Storage for Data & Models[¶](#setup-remote-storage-for-data-models "Permanent link")

DagsHub supports connecting external storage from [AWS S3](https://aws.amazon.com/s3/), [Google Cloud Storage](https://cloud.google.com/storage) (GCS), [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/), and S3-compatible storage to DagsHub repositories. It enables to access and interact with your data and large files without leaving the DagsHub platform.

In this section, we\'ll cover all the required steps to set up an external remote storage for your project. We assume that you have already [created a DagsHub project and added a Git remote](../../quick_start/create_new_project/).

## Creating a Storage Bucket[¶](#creating-a-storage-bucket "Permanent link")

If you haven\'t already created a storage bucket, you should set it up now. Follow the instructions in one of these links:

AWS â€" S3GCP â€" Google StorageAzure â€" Blob Storage

## Making Sure You Have Permissions[¶](#making-sure-you-have-permissions "Permanent link")

We need a minimum set of permission in order to use the bucket we created as our remote. If you have admin access to your cloud account, you might be able to skip this step. Here we assume you start without permissions and set up minimum permissions for the remote storage use case.

AWS â€" S3GCP â€" Google StorageAzure â€" Blob Storage

Paste it into your policy editor [found here](https://console.aws.amazon.com/iam/home#/policies). This requires you to log into your aws console. After you have created the policy, make sure it is attached to the relevant IAM user/s (if you\'re not sure how to do this, [follow these steps](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console)).

#### S3 public buckets:[¶](#s3-public-buckets "Permanent link")

Making a bucket public is not enough, Its required to have global ListBucket and GetObject capabilities set on the bucket permissions - Copy the following JSON permission file:

    ,
                "Action": "s3:ListBucket",
                "Resource": "arn:aws:s3:::my-bucket"
            },
            ,
                "Action":  "s3:GetObject",
                "Resource": "arn:aws:s3:::my-bucket/*"
            }
            ]
    }

## Installing the Command Line Tools[¶](#installing-the-command-line-tools "Permanent link")

The easiest way to allow you to push and pull to your remote storage is by installing the appropriate command line tools.

AWS â€" S3GCP â€" Google StorageAzure â€" Blob Storage

## Connect the remote storage to DagsHub[¶](#connect-the-remote-storage-to-dagshub "Permanent link")

Now that we have our bucket configured with the correct permissions, we can go to the guide on how to [connect it to DagsHub](../../feature_guide/connect_external_storage/).

## Manage your data with DVC[¶](#manage-your-data-with-dvc "Permanent link")

DagsHub external storage support also works with DVC. If you use the supported external storage types as a DVC remote. The following section will walk you through how to do this.

### Adding the DVC remote locally[¶](#adding-the-dvc-remote-locally "Permanent link")

This step consists of 2 parts - installing the DVC extension and configuring the remote. If at this point you still don\'t have DVC installed, you should [install it](https://dvc.org/doc/install).

#### Installing the DVC extension[¶](#installing-the-dvc-extension "Permanent link")

Type in the following command (according to the service you are using):

AWS â€" S3GCP â€" Google StorageAzure â€" Blob StorageAll Extensions

After the installation reopen the terminal window to make sure the changes have taken place.

#### Configuring the remote in DVC[¶](#configuring-the-remote-in-dvc "Permanent link")

Define the [dvc remote](https://dvc.org/doc/commands-reference/remote). We do this with one command (don\'t forget to replace the bucket name with your own bucket):

AWS â€" S3GCP â€" Google StorageAzure â€" Blob Storage

Consider using `--local`

It is our opinion that the configuration of the remote may vary between team members (working in various environments) and over time (if you switch between cloud providers), therefore it is prudent not to modify the `.dvc/config` file which is monitored by Git.

Instead, we prefer to use the local configuration instead. You can find it in `.dvc/config.local`, and confirm that it\'s ignored in `.dvc/.gitignore`.

That way you don\'t couple the current environment configuration to the code history. This is the same best practice which naturally occurs when you run `git remote add` - the configuration is only local to your own working repo, and won\'t be pushed to any git remote.

### Pushing files to the DVC remote storage[¶](#pushing-files-to-the-dvc-remote-storage "Permanent link")

Is as simple as one command.

    dvc push -r <remote-name>

This step might take a while, depending on the size of files you are pushing.

### Connect DagsHub to the DVC Remote Storage[¶](#connect-dagshub-to-the-dvc-remote-storage "Permanent link")

We automatically detect your remote location normally. If you used the `--local` option when configuring your DVC remote, follow the instructions here:

Connecting DagsHub to a remote configured with `--local`

To reap the benefits of doing this while using DagsHub to host your repo, go to your repo settings, and add the link to the bucket in the Advanced Settings `Local DVC cache URL`. In our case it looks something like this:\

[![Screenshot](../assets/external_storage/local_dvc_remote_url.png)](../assets/external_storage/local_dvc_remote_url.png) ~Local\ DVC\ cache\ URL\ setting~

\

With DagsHub, when you track files with DVC you\'ll see them both in your file viewer, and in your pipeline view.\

[![File Viewer](../assets/external_storage/file_viewer.png)](../assets/external_storage/file_viewer.png) ~File\ viewer\ with\ blue\ files\ that\ are\ DVC\ tracked~

\
After connecting your remote storage to DagsHub, these files now have functioning links, and are therefore available for viewing or download for anyone who would want to (provided they have authorization to your bucket, of course).

<figure>
<a href="../../tutorials/pipeline_tutorial/assets/cache_node_change.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../../tutorials/pipeline_tutorial/assets/cache_node_change.png" height="200" alt="Cache Node Change" /></a>
<figcaption>Path link change after adding remote</figcaption>
</figure>

We believe this is useful for several reasons:

- If you want to let someone browse your data and trained models, you can just send them a link to your DagsHub repo. They don\'t need to clone or run anything, or sift through undocumented directory structures to find the model they are looking for.
- The files managed by DVC and pushed to the cloud are **immutable** - just like a specific version of a file which is saved in a Git commit, even if you continue working and the branch has moved on, you can always go back to some old branch or commit, and the download links will still point to the files as they were in the past.
- By using DVC and DagsHub, you can preserve your own sanity when running a lot of different experiments in multiple parallel branches. Don\'t remember where you saved that model which you trained a month ago? Just take a look at your repo, it\'s a click away. **Let software do the grunt work of organizing files, just like those wonderfully lazy software developers do**.

Warning

When downloading a link through the graph, it might be saved as a file with the DVC hash as its filename. You can safely change it to the intended filename, including the original extension and it\'ll work just fine.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).