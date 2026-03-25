# Source: https://docs.axonius.com/docs/central-core-architecture.md

# Central Core Architecture

The Axonius central core system is a completely independent Axonius system that operates in a different mode. The central core has no adapter connections at all. Instead, it is configured to pull and download asset data that other Axonius instances (core nodes) have generated and uploaded into a storage location. The asset data contains assets from the recent discovery cycle on that core node.

The central core loads the downloaded asset data into a central core node, allowing you to manage the consolidated asset inventory of all the different core nodes from a single Axonius instance.

Using the central core functionality does not require any connection from/to the other Axonius instance(s). It only requires an intermediate storage location that is accessible to both systems, where the asset data resides.

Axonius supports three options for the storage of the asset data from each Axonius core node:

* AWS S3 bucket
* Azure Storage
* SMB
* SSH

The common use case for using the central core functionality is to deploy an Axonius core node for each business unit in the organization and to deploy an Axonius central core node. The Axonius central core node will manage the consolidated asset inventory of all the different business units of the organization from a single Axonius instance.

<Image alt="Axonius Central Core (4).png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Axonius%20Central%20Core%20(4).png" />

## Data Synchronization Flow

<Callout icon="📘" theme="info">
  Note

  The following flow uses Amazon S3 bucket as an example, but the same flow applies if you are using Azure Storage or SMB as the storage location.
</Callout>

1. **Upload process (on each core node)**
   1. At the end of every discovery cycle, the core node creates an encrypted zipped assets file that contains all assets managed by that node.
   2. The assets file is uploaded to the specified Amazon S3 bucket.
   3. The created zip assets file is deleted from the core node.

<Callout icon="📘" theme="info">
  Note

  * The assets file is created only if there are at least 15 GB available in the core node disk space.

  * The assets file contains only information about the assets. It does not contain: adapters, dashboards, enforcements, reports, or settings.
</Callout>

2. **Download process (on the central core node)** - The discovery cycle on the central core node includes the following phases:
   1. **Save history** - A snapshot of the current inventory is saved to the database, based on the **[Historical Snapshot Scheduling Settings](/docs/configuring-retention-settings#setting-historical-snapshot-scheduling)**.
   2. **Download** - The central core node downloads all the assets files that have not been restored in the past from the Amazon S3 bucket. The assets on the central core node are replaced with the restored information.
   3. **Correlation** - Asset information from the adapters is correlated to determine the actual asset inventory.
   4. **Trigger enforcements** - All enforcement sets that should run at the end of a discovery cycle are triggered.

<Callout icon="📘" theme="info">
  Notes

  * If no asset  files are found on the Amazon S3 bucket, the data on the central core node will remain as is.

  * If the central core does not have sufficient disk space to download the files, the restore process will be stopped, and the discovery cycle will be completed without restoring all the files.

  * If one of the core nodes  failed to upload the asset file or the central core node  failed to restore it, data may be inaccurate.
</Callout>

## Core Node and Central Core Node Configuration

For details, see [Core Node and Central Core Node Configuration](/docs/core-node-and-central-core-node-configuration).

1. **Download process (on the central core node)** - The discovery cycle on the central core node includes the following phases:
   1. **Save history** - A snapshot of the current inventory is saved to the database, based on the **[Historical Snapshot Scheduling Settings](/docs/configuring-retention-settings#setting-historical-snapshot-scheduling)**.
   2. **Download** - The central core node downloads all the assets files that have not been restored in the past from the Amazon S3 bucket. The assets on the central core node are replaced with the restored information.
   3. **Correlation** - Asset information from the adapters is correlated to determine the actual asset inventory.
   4. **Trigger enforcements** - All enforcement sets that should run at the end of a discovery cycle are triggered.