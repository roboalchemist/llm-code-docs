# Source: https://docs.axonius.com/docs/export-assets-to-external-axonius.md

# Axonius - Export Assets to Instance

**Axonius - Export Assets to Instance** exports the assets returned by the selected query or assets selected on the relevant asset page to an additional Axonius node. Data can be exported to an Amazon S3 Bucket, Azure blob Storage, SMB Share, or SSH.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

**Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

<br />

## Export Settings

Fields in this section are required and must be configured in order to run the enforcement set.

* **Storage type** - Select one of the following storage types to which to export the data:
  * **Amazon S3 bucket name** - Refer to [Core Node and Central Core Node Configuration Amazon S3 Settings](/docs/core-node-and-central-core-node-configuration#amazon-s3-settings) for full details about all configuration settings.
  * **Azure Blob Storage Settings**  - Refer to [Core Node and Central Core Node Configuration Azure Blob Storage Settings](/docs/core-node-and-central-core-node-configuration#azure-blob-storage-settings) for full details about all configuration settings.
  * **SMB Share** - Refer to [Core Node and Central Core Node Configuration SMB Share Settings](/docs/core-node-and-central-core-node-configuration#smb-share-settings) for full details about all configuration settings.
  * **SSH** -  Refer to [Core Node and Central Core Node Configuration SSH Settings](/docs/core-node-and-central-core-node-configuration#ssh-settings) for full details about all configuration settings.

## Additional Fields

These fields are optional.

* **Don't send preferred fields** - When selected, preferred fields are not exported to the target Axonius instance.
* **Upload CVEs to Central Core** - When selected, uploads data from the Aggregated Security Findings module to the central core.
* **Upload Software data to Central Core** - When selected, uploads data from the Software Management module to the central core.
* **Export only the queried asset type** - When selected, only assets of the asset type selected when creating the Enforcement Action are exported. When not selected, all asset types are exported.
* **Exclude/Include Adapters** - You can select adapters and adapter connections to include or exclude.
  * **Action Type** - Select whether to include or exclude the selected adapters and connections.
  * **Select adapters or adapter connections to exclude** - Select adapters or adapter connections to exclude. Data fetched from these adapters or adapter connections will not be exported.
  * **Adapter Fields Selection** - Configure fields from specific adapters to be excluded from the export.
    1. Click **+ Add fields selection from a specific adapter**. The field configuration options appear. The asset type is the same as selected for the Enforcement Action query under **Run action on assets matching the following query**. Some default fields are pre-populated.
       ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddAdapterFieldsToExclude.png)

    2. You can select a different adapter and different fields according to your needs.

    3. Click **+ Add fields from a different adapter** again to add more fields to exclude. You can configure as many as you need.
       ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddAdapterFieldsToExclude-2.png)

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).