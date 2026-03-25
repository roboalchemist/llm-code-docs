# Source: https://docs.ox.security/generate-reports/built-in-reports/sbom-reports.md

# SBOM Reports

You can use SBOM reports to review and share your software bill of materials. There are two views:

* [**Detailed SBOM Report – Internal**](#detailed-sbom-report-internal)**:** Intended for AppSec engineers to inspect component health, license status, and vulnerability metrics.
* [**SBOM Report:**](#sbom-report) Intended for managers and customers to verify your security posture using a detailed component list.

You can [filter](#filtering-report-info)and [export](#exporting-info)the report info.

## Detailed SBOM Report - Internal

Detailed SBOM Report – Internal shows the health and risk of every component in your software bill of materials.

It displays hygiene metrics, license approval breakdowns, vulnerability severity summaries, and a detailed list of all components.

You can use filters, export data, or start a scan to focus on the items you need.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d8a41efc8e9eb41070fc0daf5ed1578fd088f586%2FSBOM-Internal.png?alt=media" alt=""><figcaption></figcaption></figure>

You can view the following information:

| Section                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SBOM Issues Hygiene**              | Displays counts of SBOM items by their hygiene status, such as Deprecated, Unapproved license, Has vulnerabilities and so on.                                                                                                                                                                                                                                                                                                               |
| **Unapproved Licenses**              | Shows breakdown of SBOM items according to license type for unapproved licenses.                                                                                                                                                                                                                                                                                                                                                            |
| **Vulnerable Libraries by Severity** | Shows breakdown of vulnerable libraries according to severity.                                                                                                                                                                                                                                                                                                                                                                              |
| **SBOM Items**                       | <p>Lists all SBOM components with details such as license, CVE status, source, application and so on.<br><br>You can click <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dc15af6c699447a10d3deefccdc39302a17f3b31%2Fcustom_columns_icon.png?alt=media" alt=""> above the SBOM Items table and select which columns to present in the table.</p> |

## SBOM Report

SBOM Report provides an inventory of your software components in your software bill of materials, mainly third party and open sources.

You can share this view with managers and customers to demonstrate license compliance by showing whether each component meets its legal obligations..

The SBOM items table lists all SBOM components with details such as library name, license status, source, application, and so on. You can click ![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dc15af6c699447a10d3deefccdc39302a17f3b31%2Fcustom_columns_icon.png?alt=media) above the SBOM Items table and select which columns to present in the table.

To focus on the items you need, you can use [filters](#filtering-report-info).

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5b7327c3c204bece1f6ca781090983272cc615a4%2FSBOM_report.png?alt=media" alt=""><figcaption></figcaption></figure>

## Filtering report info

The following filter options are available in both reports:

| Filter name                | Description                                       |
| -------------------------- | ------------------------------------------------- |
| **Application**            | Filters components by application                 |
| **App Tag**                | Filters components by app tag                     |
| **Library Name**           | Filters components by library name                |
| **Library Version**        | Filters components by library version             |
| **Dependency**             | Filters components by dependency type             |
| **Issues**                 | Filters components by SBOM issue status           |
| **License**                | Filters components by license status              |
| **Source**                 | Filters components by source                      |
| **Code-to-Cloud Exposure** | Filters components by exposure path to cloud code |

## Exporting info

The following export options are available in both reports:

| Option                  | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| **Export as PDF**       | Generate a PDF file of the report, including charts and tables.    |
| **Export as CSV**       | Generate a CSV file containing raw SBOM data for further analysis. |
| **Export as CycloneDX** | Generate a CycloneDX-formatted SBOM for import into other tools.   |

> **Note:** By default, the exported report includes all columns from the SBOM Items table. If you hide any columns in your custom view, the export reflects those changes.
