# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-physical-assets.md

# Manage physical assets

In Pentaho Data Catalog, you can manage physical assets through Pentaho Edge application and locally from both the Physical Assets view and table view, including import and export of physical assets. To configure physical assets data in Pentaho Edge, you should contact [Pentaho Support](https://support.pentaho.com/hc/en-us). Then, the Pentaho Support team, in collaboration with the Pentaho Edge team, will assist in configuring the data in Pentaho Edge. When configured, the data will automatically sync with Data Catalog. In addition, you can also add physical assets locally to Data Catalog, but the assets will only exist in Data Catalog and are not synchronized with Pentaho Edge.

**Note:** To add and delete physical assets, you need the Data Steward or Admin role. Based on the other roles assigned to you, you can associate data elements or applications to a standard, or manage those associations. For more information, see the **Default user roles and permissions** section in the **Administer Pentaho Data Catalog** document.

## Add a new device or value through Pentaho Edge

In Data Catalog, you can add new devices and values through Pentaho Edge, to enable ingesting, cleansing, blending, and loading of data from diverse sources, including OT systems. After you add physical assets data in Pentaho Edge, the Physical Assets section in Data Catalog will be updated automatically.

Perform the following steps to create physical assets through Pentaho Edge:

Ensure you have access to Pentaho Edge and the respective roles in both Pentaho Edge and Data Catalog.

1. On the left navigation menu, click **Physical Assets**.

   The Physical Assets page opens.
2. Click **Actions** and then select **Add New Device** or **Add New Value**.

   The Add New Device or Add New Value dialog box appears with two options, **Create in Pentaho Data Catalog** and **Create in Pentaho Edge**.

   **Note:** You can also use the **Add New Device** and **Add New Value** options under **Actions** in the Physical Assets table view.
3. Select **Create in Pentaho Edge** and click **Confirm**.

   It redirects you to Pentaho Edge, where you can create physical asset components. For assistance with configuring physical asset data, contact [Pentaho Support](https://support.pentaho.com/hc/en-us). After completing the configuration. Physical asset data will automatically sync with the Data Catalog Physical Assets section.

## Add a new device locally to Data Catalog

In Data Catalog, you can add physical asset devices locally and link to the respective device services (protocols), which helps you to experiment with data organization, simulate asset hierarchies or test scenarios, define relationships, add metadata, and customize properties without affecting live data or external systems.

Perform the following steps to add a new device locally in Data Catalog:

1. On the left navigation menu, click **Physical Assets**.

   The Physical Assets page opens.
2. Click **Actions** and then select **Add New Device**.

   The Add New Device dialog box appears with two options, **Create in Pentaho Data Catalog** and **Create in Pentaho Edge**.

   **Note:** You can also use the **Add New Device** option under **Actions** in the Asset Hierarchy table view.
3. Select **Create in Pentaho Data Catalog** and click **Confirm**.

   The **Create Device** dialog box appears.
4. In the **Device Name** box, enter a name for the asset, select an appropriate device profile (protocol) in the **Parent** box, and then click **Create**.

   The newly added device appears on the list but does not sync with Pentaho Edge.

You have successfully added a new device in Data Catalog locally.

You can add a new value to the added device. For more information, see [Add a new device or value through Pentaho Edge](#add-a-new-device-or-value-through-pentaho-edge).

## Add a new value locally to Data Catalog

Similar to [adding new devices locally](#add-a-new-device-locally-to-data-catalog), in Data Catalog, you can add new values to the devices. Perform the following steps to add a new value locally in Data Catalog:

1. On the left navigation menu, click **Physical Assets**.

   The Physical Assets page opens.
2. Click **Actions** and then select **Add New Value**.

   The Add New Value dialog box appears with two options, **Create in Pentaho Data Catalog** and **Create in Pentaho Edge**.

   **Note:** You can also use the **Add New Device** option under **Actions** in the Asset Hierarchy table view.
3. Select **Create in Pentaho Data Catalog** and click **Confirm**.

   The **Create Value** dialog box appears.
4. In the **Value Name** box, enter a name for the value, select an appropriate device in the **Parent** box, and then click **Create**.

   The newly added value appears on the list but does not sync with Pentaho Edge.

You have successfully added a new value in Data Catalog locally.

## Delete physical assets

In the Physical Assets table view, you can remove the physical asset from Data Catalog without affecting the underlying data in Pentaho Edge. This feature helps you to maintain an organized and focused Data Catalog by decluttering irrelevant or outdated physical assets while preserving the integrity of operational data in Data Catalog Edge.

Perform the following steps to delete an physical asset from Data Catalog:

1. On the left navigation menu, click **Physical Assets**.

   The Physical Assets page opens.
2. Click **Actions** and select **Table View**.

   The **Physical Assets** Table View page with a list of physical assets appears.
3. Click the **Delete** icon of the respective physical asset you want to remove from Data Catalog. The Confirm Deletion dialog box opens.
4. Click **Confirm** to confirm the deletion.

You have successfully removed the physical asset from Data Catalog. However, it doesn’t remove the physical asset in Pentaho Edge.

## Import physical assets

In Data Catalog, you can quickly import and add large volumes of physical assets data into the Physical Assets section from a file in one of the following file types while reducing the risk of manual errors:

* JSON Lines (Not JSON. See more here [https://jsonlines.org/](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fjsonlines.org%2F\&data=05%7C02%7Cemily.reidenbach%40hitachivantara.com%7C06c222e611c84b0aef2208dd394286c7%7C18791e1761594f52a8d4de814ca8284a%7C0%7C0%7C638729680092734770%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C\&sdata=HiGtTRKXD79qgYPX2Ra0bPhsbZrqAku6Mvco%2FKIgaPE%3D\&reserved=0))
* Comma Separated Values (text/csv)

Perform the following steps to export physical assets into Data Catalog:

1. On the left navigation menu, click **Physical Assets**.

   The Physical Assets page opens.
2. Click **Actions** and select **Import**.

   The Import Assets dialog box appears.

   **Note:** You can also use the **Import** option available under **Actions** in the Physical Assets table view.
3. You can drag and drop the file or browse and select the file you want to import and click **Submit**.

   Ensure the file format and structure align with the requirements of the physical assets feature.

You have successfully imported the physical assets in Data Catalog Physical Assets section.

You can also export physical assets for Data Catalog. For more information, see [Export physical assets](#export-physical-assets).

## Export physical assets

In Data Catalog, you can export existing physical assets data in CSV or JSON format for backup purposes to save and restore them if necessary. Additionally, you can share physical assets across teams or other Data Catalog instances.

Perform the following steps to export physical assets in Data Catalog:

1. On the left navigation menu, click **Physical Assets**.

   The Physical Assets page opens.
2. Click **Actions** and select **Export**.

   The **Export Assets** dialog box appears.

   **Note:** You can also use the **Export** option available under **Actions** in the Physical Assets table view.
3. Select what to export. Select individual physical assets, or choose **Select all** to export every physical assets in the list.\
   You can also use **Search** to find items. The counter (for example, **0/11**) shows how many are selected.
4. Select the file type, **CSV** or **JSON**, to which you want to export the physical asset hierarchy and then click **Submit**.

   The file containing the physical assets in the selected format will be downloaded into the local folder.

You have successfully exported the physical assets from Data Catalog.

You can also import physical assets into Data Catalog. For more information, see [Import physical assets](#import-physical-assets).
