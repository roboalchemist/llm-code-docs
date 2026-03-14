# Source: https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/importing-issues-from-external-files.md

# Importing Issues by File Upload

You can upload files containing security issues discovered outside of OX, so you can manage them together with your other issues.

Typical use cases include:

* You received a pen-test report and want the findings to appear in OX alongside your other issues.
* You use a product that OX does not natively integrate with and want those findings in OX for single-pane tracking.

Currently, the supported file format is JSON.

## Uploading issue files

You upload issue files to OX through the OX platform or using the OX API. You prepare the file according to the required schema, upload it, and OX processes the data and displays the issues in the UI.

**To import the file using OX platform:**

1. [Prepare the file that you want to upload.](https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/importing-issues-from-external-files/preparing-a-file-for-manual-upload)
2. In the **Active Issues** page, select **Import** from the top bar.
3. Drag and drop or search for the file you want to upload.

> **Note:** Make sure the files that you import have meaningful names that identify the origin of the uploaded issues, for example, Pen Test, Black Duck, Snyk, Torque. The name you provide in this field is used later in the Source Tool filter in OX, when you want to view the imported issues in OX.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2534ec358df6ae0ee9f75bceca475ccb6121212a%2FImport_issues1.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select **IMPORT**. When your file is successfully uploaded, you have the option to download or remove it.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-44d683c02979ed05d26c3e66950d42583bb8c77c%2FImport_issues2.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select **CLOSE**. The imported issues appear in the Active Issues page only after you run a new scan.

**To import the file using OX API:**

1. [Prepare the file that you want to upload.](https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/importing-issues-from-external-files/preparing-a-file-for-manual-upload)
2. [Create a new API key.](https://docs.ox.security/api-documentation/api-reference/ox-api-authentication)
3. Upload the file using OX API. OX processes the file and creates or maps Applications and Issues.

An example of an API call to upload a file as curl:

```
curl --location '' \
--header 'content-type: application/json' \
--header 'Authorization: <ox api token>' \
--header 'x-apollo-operation-name: file-upload' \
--data '{"query":"mutation UploadThirdPartyFileBase64($data: String!, $tool: String!, $fileType: ThirdPartyUploadDataType) {\n  uploadThirdPartyFileBase64(data: $data, tool: $tool, fileType: $fileType) {\n    requestId\n    success\n  }\n}","variables":{"data":"<base64 string>","tool":"<tool name>","fileType":"<file type>"}}'
```

Where:

| Placeholder      | Description                                                                                                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<OX API token>` | The API key you have created in OX.                                                                                                                                          |
| `<tool name>`    | The name of the tool that generated the issues. Can be any string.                                                                                                           |
| `<data>`         | The JSON file encoded as a Base64 string.                                                                                                                                    |
| `<file type>`    | <p>Supports the following values:</p><ul><li><strong>JSON:</strong> Used for regular uploads in OX format.</li><li><strong>SARIF:</strong> Used for SARIF uploads.</li></ul> |

1. Perform a scan to ensure the uploaded issues are added to your organization in OX.

   > **Note:** Running a scan after the upload is required for the issues to be registered in your organization.

## Viewing and managing imported files

After you run a scan, you can view the imported issues in the Active Issues page and the Applications page.

OX validates each uploaded file automatically. If any required fields are missing or invalid, the upload fails. A tooltip appears in the UI showing which fields caused the problem.

You can download or drag the file back to your computer, fix the errors, and re-upload it.\
Invalid files cannot be imported until all validation errors are resolved.

In case you don't want to view the imported issues, you can remove the imported files at any time. The issues imported from the removed file will not appear in OX after the next scan.

You can also download the file to your system and view the issues contained in it.

**To view the imported issues in OX Security:**

* Go to **Active Issues** and in the **Filters** pane, select **Source Tool > Manual Upload**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0b75344714cecf9cdc2ed67182a1ffe001548621%2Fissues%20from%20file%20in%20the%20Active%20issues.png?alt=media" alt=""><figcaption></figcaption></figure>

* **Applications** and in the **Filters** pane, select **Category > Manual Upload**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-df9f0f7d7d03b287e4845d148044ef481c36983e%2Fissues%20from%20file%20in%20the%20Applications.png?alt=media" alt=""><figcaption></figcaption></figure>

**To remove/download the imported files:**

1. Go to **Active Issues > Manage Files**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f6e4b3520488ab4bab4f94c028c1f4584f0293c6%2FManage_Uploaded_files%20(2).png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

1. Remove the files that you want, or download the files to view the issues that were imported. After the next scan, the issues that were imported from the file you removed no longer appear in OX.
