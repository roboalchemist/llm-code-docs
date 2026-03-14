# Source: https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/mapping-repositories-to-third-party-projects.md

# Matching 3rd-Party Projects to OX Apps

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

OX automatically maps repositories to corresponding third-party projects, helping you unify visibility across third party tools, such as Snyk.

This capability allows you the following:

* Display application data and security issues from third-party tools in the correct project context.
* Gain a unified view of your projects across tools.
* Ensure accurate reporting by aligning repository and project data.
* Maintain control over mappings through manual settings or matching files.

Manual matching methods:

* [Manual Matching](#manual-matching)
* [File-Based Matching](#file-based-matching)

Automatic matching that OX Security performs during scan in the following order:

1. [Name-Based Matching](#name-based-matching)
2. [AI-Based Matching](#ai-based-matching)

## Manual matching

When matching OX repository to an external project, you can manually replace an existing match if the automatic match is incorrect.

When matching an external project to a repository, you can create a match manually, if none exists.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e219889b3b4a1ece9ba5a3d0037f563150a32674%2Fmatching%20in%20Applications%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

**To edit an application-to-project match:**

1. In the **Applications** page, select the application for which you want to do the match.
2. In the application details panel, go to the **Matched Projects** tab and select the edit icon in the relevant line.
3. In the **Match Application to Project** dialog, select the app name that you want to assign to this project.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-730d84c6afdb449fe62089111b6c5696cf85421e%2Fmatch%20app%20to%20project.png?alt=media" alt="" width="366"><figcaption></figcaption></figure>

1. Select **SAVE**.

**To match a project to a repository:**

1. In the **Applications** page, select the application for which you want to do the match.
2. In the application details panel, go to the **Matched Projects** tab and click **Match Projects to App**.
3. In the **Match Projects to App** dialog, select the project name that you want to assign to this repo under the relevant connected security tool.
4. Select **SAVE**.

## File-based matching

You can provide a mapping file that defines the relationships between repositories and security projects. This file is uploaded using a specific API endpoint.

If a matching file is provided through the API, OX uses the mappings defined in the file, as follows:

```
// [
    {
      "externalToolProject": "ThirdPartyProjectName",
      "oxRepo": "ServiceChannel/ServiceClick/CustomerRepoName"
    },
    {
      "externalToolProject": "ThirdPartyProjectName",
      "oxRepo": "ServiceChannel/ServiceClick/CustomerRepoName"
    },
    {
      "externalToolProject": "ThirdPartyProjectName",
      "oxRepo": "ServiceChannel/ServiceClick/CustomerRepoName"
    }
  ]
```

Where:

| `externalToolProject` | The name of the project in the third party tool, for example, "Analytics\_Genie-genieApp". |
| --------------------- | ------------------------------------------------------------------------------------------ |
| `oxRepo`              | The name of the application in the OX Security platform, for example, "genie-app".         |

The fileUpload query:

```
// query UploadFile($data: String!, $dataType: UploadDataType!, $connectorName: PolicyFileConnectorName!, $fileType: FileType) {
  uploadFile(data: $data, dataType: $dataType, connectorName: $connectorName, fileType: $fileType) {
    requestId
    success
  }
}
```

The input that you add for file Upload:

```
// {
  "data": "",
  "dataType": "",
  "connectorName": "",
  "fileType": ""
}
```

Where `dataType` must be either `Base64` or `JSON`

For further explanations about connecting to OX API, read [API Documentation](https://docs.ox.security/api-documentation/api-reference).

## Name-based Matching

During scan, OX Security matches repositories and projects based on name similarity, where project name ≈ repository name.

It requires no manual input or configuration, it is performed automatically and is always enabled.

## AI-based matching

> **Notes:** The only customer data that OX Security sends to the AI service is the project name.

If other matching methods are not available, OX applies AI-based logic to match repositories with third-party projects. This method helps reduce manual effort, especially when working with large volumes of data or unclear naming conventions.

The process is done automatically during the scan.

AI algorithms analyze the names of repositories and projects and automatically create matches based on advanced similarity patterns.

This capability is enabled by default, and you can disable it at any moment (Settings > AI > AI Matching Between OX Applications and Third-Party Projects).

When the AI-based matching is used, an indicator appears in the Applications page.
