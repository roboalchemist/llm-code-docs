# Source: https://help.aikido.dev/container-image-scanning/configuration/export-raw-sbom-of-your-containers.md

# Export RAW SBOM of Your Containers

## Introduction <a href="#introduction" id="introduction"></a>

Exporting a RAW SBOM with Aikido enhances software security and transparency. This feature is particularly useful for:

* Identifying the filesystem locations of issue discoveries.
* Tracking the origin of installed components.

## Step-by-Step Guide <a href="#step-by-step-guide" id="step-by-step-guide"></a>

**Step 1:** Navigate to any **container detail** page on Aikido.

**Step 2:** Click **Actions** in the top right.\
​

![Dropdown menu for refreshing data and exporting issues or raw SBOM files.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6a1f30813b800452aa8cec091222a5ab498e6946%2Fexport-raw-sbom-of-your-containers_fc079c8a-dbd1-48b2-a52d-788db57184da.png?alt=media)

​**Step 3:** Choose **Export RAW SBOM** to generate and download the SBOM for your container.

## Limitations <a href="#limitations" id="limitations"></a>

The RAW SBOM Export is available only for images scanned by Aikido, not for those analyzed through AWS Inspector or GCP Vulnerability Scanning.

More information on setting up your container scanning with the Aikido Scanner can be found [here](https://help.aikido.dev/en/articles/8911170-container-scanning-for-aws-ecr-with-the-aikido-scanner).

### Generate and Export via API <a href="#generate-and-export-via-api" id="generate-and-export-via-api"></a>

Aikido also supports generation and download of SBOM via API. More information can be found in our [Apidocs](https://apidocs.aikido.dev/reference/exportcontainerrepolicenses)[.](https://apidocs.aikido.dev/reference/exportcoderepolicenses)

***
