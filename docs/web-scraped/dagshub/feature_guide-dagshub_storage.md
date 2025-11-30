# Source: https://dagshub.com/docs/feature_guide/dagshub_storage/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/feature_guide/dagshub_storage.md "Edit this page")

# DagsHub Storage[¶](#dagshub-storage "Permanent link")

DagsHub automatically configures an S3-Compatible storage bucket with every repository. The storage can be used as a general purpose storage bucket, or you can utilize [DVC](../../integration_guide/dvc/) to get more advanced versioning capabilities.

<figure>
<a href="../assets/dagshub_storage/storage_home.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/dagshub_storage/storage_home.png" alt="DagsHub Storage" /></a>
<figcaption>DagsHub Storage</figcaption>
</figure>

Connect External Storage Buckets

If you already have a storage bucket set up somewhere, you can get all the benefits of DagsHub Storage with your own storage bucket. To learn how to do that, go to the guide for [connecting external storage](../../quick_start/connect_external_storage/).

## What you get with DagsHub Storage[¶](#what-you-get-with-dagshub-storage "Permanent link")

Every repository is provided with two places you can store the data your project needs:

- An S3-Compatible storage bucket
- A DVC remote

You can use [your access token](https://dagshub.com/user/settings/tokens) to interact with either of them, and access control is based on the access control of your repository. Meaning that only repository writers can change the data, and if your repository is private, then you\'re in control of who can look at and read the files.

Both of the storages are explorable through the web interface of the repository and through the [Content API](../../api/). DVC data will be shown along with git repository files, whenever we find any dvc pointer files (`.dvc`) that were pushed to git, and the bucket is explorable through \"DagsHub Storage\" entry in the \"Storage Buckets\" section at the homepage of your repository.

The DVC remote and the bucket are separate from each other

That means that the files you pushed to the DVC remote won\'t show up in the storage bucket, and same for the opposite.

## Working with the S3 compatible storage bucket[¶](#working-with-the-s3-compatible-storage-bucket "Permanent link")

### DagsHub Client[¶](#dagshub-client "Permanent link")

The easiest way to upload files to your DagsHub storage bucket is by using the DagsHub Client.

Simply run:

    $ dagshub upload --bucket <repo_owner>/<repo_name> <local_file_path> <path_in_remote>

To download, simply run:

    $ dagshub download --bucket <repo_owner>/<repo_name> <path_in_remote> <local_file_path>

#### Mounting the bucket as a filesystem \[Linux only\][¶](#mounting-the-bucket-as-a-filesystem-linux-only "Permanent link")

If your operating system supports FUSE, you can use the DagsHub client mount command to work with your DagsHub storage bucket as a local filesystem. After you mount a bucket you can interact with it in your file explorer.

Here\'s how you can mount the dagshub bucket at in python:

    dagshub.storage.mount("<repo_owner>/<repo_name>")

This will mount your repository\'s DagsHub storage bucket to the following folder in your current working directory `<repo_name>/dagshub_storage/...` folder with the repo name in your current directory.

You can also interact with the bucket in a few additional ways:

### Boto/S3FS[¶](#botos3fs "Permanent link")

The DagsHub Python client has a function that can generate clients for the following S3 libraries:

- [Boto3](https://github.com/boto/boto3) (returns a boto3.client object) â€" Read the [Boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html)
- [S3Fs](https://github.com/fsspec/s3fs) â€" Read the [S3Fs docs](https://s3fs.readthedocs.io/en/latest/)

To get a client add the following code, then use the client according to the documentation of the library:

Note

Most functions in the libraries ask for the name of the bucket as an argument. In those cases, use the name of the repository as the bucket name.

boto3s3fs

### RClone[¶](#rclone "Permanent link")

[RClone](https://rclone.org/) is a very convenient CLI tool that allows you to synchronize data between different storages, be they local, FTP or object storages.

To add the DagsHub storage bucket to RClone as a remote:

1.  Run `rclone config` in your terminal
2.  Type `n` to add a new remote
3.  Choose `s3` as the storage type
4.  Choose `Other` (last) as the provider
5.  Choose `Enter AWS credentials in the next step.` to enter the credentials manually
6.  Input your [DagsHub token](https://dagshub.com/user/settings/tokens) as both the Access Key ID and Secret Access Key
7.  Leave the region empty
8.  Set the `endpoint` to `https://dagshub.com/api/v1/repo-buckets/s3/<user>` (where user is the owner of the repository)
9.  Leave all the other steps empty, until you complete the setup.

The resulting config from RClone should look like this:

    Configuration complete.
    Options:
    - type: s3
    - provider: Other
    - access_key_id: <token>
    - secret_access_key: <token>
    - endpoint: https://dagshub.com/api/v1/repo-buckets/s3/<user>

After the setup is done you can start using RClone with the bucket!

Here\'s an example of how you can copy a local folder to the bucket (assuming the name of the remote in RClone is `dagshub`):

    rclone sync <local_path_to_folder> dagshub:<repo_name>/<remote_path_to_folder>

## Working with the DVC remote[¶](#working-with-the-dvc-remote "Permanent link")

### Configuring DVC[¶](#configuring-dvc "Permanent link")

1.  Go to your repository homepage, click on the green \"Remote\" button in the top right, go to the Data section and choose DVC there.
2.  Copy the commands to set up your local machine with DagsHub Storage

[![DVC remote](../../integration_guide/assets/dvc/dvc_remote.jpeg)](../../integration_guide/assets/dvc/dvc_remote.jpeg)

1.  Enter a terminal in your project, paste the commands and run them (the following commands are an example, and the actual commands are the ones you should copy from the Remote dropdown):

    ::: highlight
        dvc remote add origin s3://dvc
        dvc remote modify origin  endpointurl https://dagshub.com/<DagsHub-user-name>/hello-world.s3
        dvc remote modify origin --local access_key_id <Token>
        dvc remote modify origin --local secret_access_key <Token>
    :::

    Why \--local?

    Everything you configure without `--local` will end up in the `.dvc/config` file, which is tracked by git, and appear in your repository. Personal info like authentication details should always be kept local.

**That\'s it! You can now pull data from your remote cache**

**Note:** *You need to be inside a Git and DVC directory for this process to succeed. To learn how to do that, please follow the [first part](../../quick_start/create_new_project/) of the Get Started section.*

### Pull data[¶](#pull-data "Permanent link")

    dvc pull -r origin

### Push data[¶](#push-data "Permanent link")

    dvc push -r origin

## Miscellaneous[¶](#miscellaneous "Permanent link")

### S3 Compatible Bucket credentials[¶](#s3-compatible-bucket-credentials "Permanent link")

In case you have a usecase not covered in the \"Working with the S3 compatible storage bucket\" section, here are the credentials you need to connect to the bucket:

- Bucket name: `<name of the repo>`
- Endpoint URL: `https://dagshub.com/api/v1/repo-buckets/s3/<username>`
- Access Key ID: `<Token>`
- Secret Access Key: `<Token>`

The region is irrelevant. If your library/program requires a region, put in the AWS default `us-east-1`

### Endpoints supported by the S3 Compatible Bucket[¶](#endpoints-supported-by-the-s3-compatible-bucket "Permanent link")

**Objects:**

- [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)
- [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
- [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)

**Multipart uploads:**

- [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)
- [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
- [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
- [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)
- [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
- [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).