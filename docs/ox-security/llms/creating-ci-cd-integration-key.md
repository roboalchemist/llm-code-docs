# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/creating-ci-cd-integration-key.md

# Creating CI/CD Integration Key

To integrate with CI/CD platforms, you need to create integration keys.

**To create a new integration key:**

1. From the left pane of the **OX dashboard**, select **Settings > API Key Settings**.
2. In the **API Key Settings** window, select **CREATE API KEY**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-81d3e33e58918419c8508c194e90479c1b274f70%2FAPI%20key%20for%20pipeline%20(1).png?alt=media" alt="" width="358"><figcaption></figcaption></figure>

1. In the **Create API Key** box set the following and select **CREATE**:

* **API Key Name:** Add a meaningful name that is easy to identify. It is good practice to include the key's intended purpose in the name.
* **API Key Type:** Select **CI/CD Integration**.
* **Expiration Date:** Until when you can use this key.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7ad7fbbb73b081bcac69083afc801e6ebc0569c4%2FAPI%20key%20for%20pipeline%201.png?alt=media" alt="" width="358"><figcaption></figcaption></figure>

1. Copy the **API Key Secret** to be used when connecting to APIs. Save the key in a safe location. This is the only time when you can see and copy the actual key.
2. Select **CLOSE**. The new key appears in the **API Key Settings** page.
