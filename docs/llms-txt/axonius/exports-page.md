# Source: https://docs.axonius.com/docs/exports-page.md

# Exports Page

The **Exports** page lists all the exported CSV files. Use this page to view a historical record of your initiated exports, or download them to your machine.

<Image alt="ExportsPageOverview" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/Exports%20Page.png" />

To access Exports page, from the platform's left navigation menu, select **Exports** (under **Adapters**).

<Image alt="ExportsNavigationMenu" border={false} src="https://files.readme.io/a87f8037c329273ab968be399deff478b11669bb92ad880b2a11e31d62d9dcd1-image.png" />

For each export, the following information is provided:

* File name, type and size
* The duration of the export process, and its generation time and date
* **Export Status** - Completed, Failed, In Progress, or Cancelled
* **Related Query** - The name of the query as it was **at the time of the export**. If the query's name was changed since then, it is not reflected in the table.
* **Source** - The Assets page from which the file was generated.
* **File Status** - Exports are available for downloads for a limited period of time. If the export is available for downloads, the time and date until it is available is displayed. Other options are Deleted (export was deleted from the table) or Expired (export is no longer available for download).

The **Export Status**, **Source**, **File Status**, and **Generated On** can also be used to filter the table results.

## Actions

### Canceling an Export

To cancel an export or multiple exports, select them and click the **Cancel** button, located above the table on the right.

You can only cancel exports that are pending or in progress.

### Deleting an Export

To delete an export or multiple exports, select them and click the **Delete** button, located above the table on the right.

You can only delete exports that are completed and available for download.

### Downloading an Export

To download an export, hover over its row and click the download icon on the right. The deletion and cancelation icons are also available there. If the **File Status** of the export is Expired, it is no longer available for download.

<Callout icon="📘" theme="info">
  **Note**

  The file is only downloaded if the session remains open until export is complete. If the session was closed mid-export - due to a lack of internet connection or any other reason - the file is not automatically downloaded.
</Callout>

<br />