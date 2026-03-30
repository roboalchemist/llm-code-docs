# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-use-data-storage-optimizer/pdso-workflows.md

# Workflows

Use the workflow examples in this section as a guide to rules-governed tiering and purging data operations.

Also see [Rehydration](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-rehydration).

## Tiering workflow

Use the workflow example below to perform rules-governed file tiering to move files older than a specified date into long term storage.

{% hint style="info" %}
To manually migrate a file, see **Explore Your Data in Data Catalog**.
{% endhint %}

Before you begin, the data sources and storage destinations should already be present in Data Catalog. Also, your role in Data Catalog and Data Optimizer must have permissions for the operations you want to perform. See [Default user roles and permissions in Data Optimizer](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-rbac).

{% hint style="info" %}
If you are tiering from an HDFS data source, you can only move files to the preconfigured archive destination within the HDFS cluster.
{% endhint %}

1. From Data Storage Optimizer, click **Check Data Temperature** to open the **Glossary** in Data Catalog.
2. Create a domain. For example, `Data Temperature`. See [Assign data temperatures](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-use-data-storage-optimizer/pdso-assign-data-temperatures).
3. Create terms in the domain to apply to your files or folders. For example, `Boiling`, `Hot`, `Warm`, `Cold`, and `Frozen`.
4. Click **Management** to open the Manage Your Environment page. On the **Metadata Rules** card, click **Add New** > **Add Rule Definition** and create a rule definition with the following attributes:
   1. Name the rule definition. For example, `Cold Files`.
   2. In **Criteria** select **Object** equals **File**.
   3. Select **Create a condition** and **Attribute** equals **Last Access Date**.
   4. In **Operator** select **Less Than Date**, and then enter a time and date. For example, `1 October 2022, 00:00:00`.
   5. In **Add Action** select **Apply Business Terms**.
   6. In **Add Term** select `Cold` (for example).
   7. In **Add Action** select **Remove Business Terms**.
   8. In **Add Term** select `Boiling`, `Hot`, `Warm`, and `Frozen` (for example).
   9. Click **Save**.
5. Open the Manage Your Environment page, and on the **Metadata Rules** card, click **Add New** > **Add Rule** then create a metadata rule with these attributes:
   1. Name the metadata rule. For example, `Find Cold Files`
   2. Select the **Source Data Asset** on which to run the metadata rule.
   3. Select the rule definition created earlier. For example, `Cold Files`.
   4. Select the checkbox to run the rule now, enter a time to run it later, or both.
   5. Click **Apply**.
6. Click the **App Switcher** then select Data Optimizer.
7. Click **Management** to open the Manage Your Environment page. On the **Rules** card, click **Add New** > **Add Rule Definition** and create a rule definition to tier files:
   1. Name the rule definition. For example, `Tier Cold Data`.
   2. In **Criteria** select **Object** equals **File**.
   3. Click **Create a condition** and select **Attribute** equals **Business Term**.
   4. In **Operator** select **Equals Ignore Case**.
   5. In **Value** select `Cold` (for example).
   6. Click **Start Process**.
   7. In **Action** select **Move** and then select the file destination.
   8. Click **Save**.
8. On the **Rules** card, click **Add New** > **Add Rule** then create a metadata rule with these attributes:
   1. Name the metadata rule. For example, `Move Cold Files`.
   2. Select the **Source Data Asset** on which you want to run the metadata rule.
   3. Select the rule definition created earlier. For example, `Tier Cold Data`.
   4. Select the checkbox to run the rule now, enter a time to schedule it to run, or both.
   5. Click **Apply**.

**Result**

Files marked Cold are moved to the target destination. 

To view the progress of the tiering operation, go to the Manage Your Environment page and on the **Data Operations** card, click **Submitted**. On the Data Operations page, the status of the operation, file name, path, source, type, and destination are provided. What remains in the folder of the data source is an `.html` stub file, except in HDFS, that can be used for rehydration if needed.

## Purging workflow

Use the workflow example below to perform rules-governed file purging to delete files older than a specified date for the data source.

{% hint style="warning" %}
Purged files are permanently deleted.
{% endhint %}

{% hint style="info" %}
To manually delete a file, see **Explore Your Data** in **Data Catalog**.
{% endhint %}

Before you begin, the data sources and storage destinations should already be present in Data Catalog. Also, your role in Data Catalog and Data Optimizer must have permissions for the operations you want to perform. See [Default user roles and permissions in Data Optimizer](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-rbac).

1. From Data Optimizer, click **Check Data Temperature** to open the **Glossary** in Data Catalog.
2. Create a domain. For example, `Data Temperature`. See [Assign data temperatures](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-use-data-storage-optimizer/pdso-assign-data-temperatures).
3. Create terms for the domain to apply to your files or folders. For example, `Boiling`, `Hot`, `Warm`, `Cold`, and `Frozen`.
4. Click **Management** to open the Manage Your Environment page, and on the **Metadata Rules** card, click **Add New**. Then click **Add Rule Definition** and create a rule definition with the following attributes:
   1. Name the rule definition. For example, `Frozen Files`.
   2. In **Criteria** select **Object** equals **File**
   3. Click **Create a condition** and select **Attribute** equals **Last Access Date**.
   4. In **Operator** select **Less Than Date**, and then enter a time and date. For example, `1 October 2020, 00:00:00`
   5. In **Add Action** select **Apply Business Terms**
   6. In **Add Term** enter `Frozen` (for example)
   7. In **Add Action** select **Remove Business Terms**
   8. In **Add Term** enter `Boiling`, `Hot`, `Warm`, and `Cold` (for example).
   9. Click **Save**.
5. Open the Manage Your Environment page, and on the **Metadata Rules** card, click **Add New** > **Add Rule** then create a metadata rule with these attributes:
   1. Name the metadata rule. For example, `Find Frozen Files`.
   2. Select the **Source Data Asset** on which to run the rule.
   3. Select the rule definition created earlier. For example, `Frozen Files`.
   4. Select the checkbox to run the rule now, enter a time to run it later, or both.
   5. Click **Apply**.
6. Click the **App Switcher** then select Data Optimizer.
7. Click **Management** to open the Manage Your Environment page. On the **Rules** card, click **Add New** > **Add Rule Definition** and create a rule definition to delete files:
   1. Name the rule definition. For example, `Purge Frozen Data`.
   2. In **Criteria** select **Object** equals **File**.
   3. Click **Create a condition** and select **Attribute** equals **Business Term**.
   4. In **Operator** select **Equals Ignore Case**.
   5. In **Value** select `Frozen` (for example).
   6. Click **Start Process**.
   7. In **Action** select **Delete**.
   8. Click **Save**.
8. On the **Rules** card, click **Add New** > **Add Rule** then create a metadata rule with these attributes:
   1. Name the metadata rule. For example, `Delete Frozen Data`.
   2. Select the **Source Data Asset** on which to run the metadata rule.
   3. Select the rule definition created earlier. For example, `Purge Frozen Data`.
   4. Select the checkbox to run the rule now, enter a time to run it later, or both.
   5. Click **Apply**.

**Result**

Files marked Frozen are deleted.

To view the history of the execution, on the **Rules** card, click **Rules**. Locate the name of the metadata rule and select **View**. Click the **History** tab to view the status and click **Statistics** to view detailed results.
