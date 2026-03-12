# Source: https://neo4j.com/docs/aura/managing-instances/instance-actions/

Title: Instance actions - Neo4j Aura

URL Source: https://neo4j.com/docs/aura/managing-instances/instance-actions/

Markdown Content:
Perform multiple instance actions directly from an instance card: connect to tools, pause/resume, inspect the instance’s details, take a snapshot, restore a backup, clone to new instance/clone to existing instance, edit secondaries, delete, resize, view resources/view all metrics.

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_connect_to_tools)Connect to tools
------------------------------------------------------------------------------------------------------

The **Connect** button allows you to connect your instance to one of the tools; Query, Explore, or Dashboards, or to the Developer hub. This is possible from both Aura instances as well as self-managed deployments (see [Self-managed instances](https://neo4j.com/docs/aura/managing-instances/self-managed/)), as long as the instance/deployment is running.

![Image 1: connect to tools](https://neo4j.com/docs/aura/_images/connect-to-tools.png)

Figure 1. Connect to tools

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_pause_an_instance)Pause an instance
--------------------------------------------------------------------------------------------------------

Pausing a Neo4j instance temporarily stops the database, which means:

*   No Access to Data: The data stored in the database becomes inaccessible. Any applications or users trying to connect to the instance won’t be able to run queries or retrieve data until the instance is resumed.

*   No Processing: The database won’t process any operations or transactions while it is paused. Any ongoing operations are halted.

*   Data is Preserved: Your data remains safe and unchanged while the instance is paused. When you resume the instance, you can pick up right where you left off.

Pausing is putting the database on hold without shutting it down completely, so you can restart it quickly when needed.

You cannot manually pause an AuraDB Free instance; they are paused automatically after 72 hours of inactivity.

You can pause an instance when not needed and resume it at any time. Do so by using the **Pause** button on the instance card. After confirming, the instance begins pausing, and a play button replaces the pause button.

When you pause an instance, Aura performs a backup operation behind the scenes. It can take a while to pause, depending on your instance size, because Aura is creating the backup.

Paused instances run at a discounted rate compared to standard consumption, as outlined in the confirmation window. You can pause an instance for up to 30 days, after which point Aura automatically resumes the instance.

### [](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_resume_a_paused_instance)Resume a paused instance

Resume a paused instance with the **Play** button on the instance card.

After confirming, the instance begins resuming, which may take a few minutes. Resuming an instance restores the database from the backup.

Aura Free instances do not automatically resume after 30 days. If an Aura Free instance remains paused for more than 30 days, Aura deletes the instance, and all information is lost.

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_inspect_an_instances_details)Inspect an instance’s details
-------------------------------------------------------------------------------------------------------------------------------

From the instance card, select the more menu (**…​**) then select **instance details**. From the instance details you can rename an instance and view instance details. See [Instance details](https://neo4j.com/docs/aura/managing-instances/instance-details/) for more information.

![Image 2: instance actions](https://neo4j.com/docs/aura/_images/instance-actions.png)

Figure 2. The more (…​) menu on an AuraDB Free instance

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_snapshots_and_backups)Snapshots and backups
----------------------------------------------------------------------------------------------------------------

Snapshots are taken at regular intervals and can be used to download or dump your data to a new instance. You can also restore backups of 4GB or less. See [Backup, export, restore, and upload](https://neo4j.com/docs/aura/managing-instances/backup-restore-export/) for more information

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_clone_an_instance)Clone an instance
--------------------------------------------------------------------------------------------------------

You can clone an existing instance to create a new instance with the same data. You can clone across regions, and from Neo4j version 4 to Neo4j latest version.

There are two options to clone an instance:

*   Clone to a new instance

*   Clone to an existing instance

You can access all the cloning options from the more menu (**…​**) on the instance.

You cannot clone from a Neo4j latest version instance to a Neo4j version 4 instance.

### [](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_clone_to_a_new_instance)Clone to a new instance

1.   From the more menu (**…​**) on the instance you want to clone, select **Clone to** and then **New instance** from the contextual menu.

2.   Set your desired settings for the new database. For more information on AuraDB database creation, see [Create an instance](https://neo4j.com/docs/aura/getting-started/create-instance/).

3.   Check the **I accept** box and select **Create**.

Make sure that the username and password are stored safely before continuing. Credentials cannot be recovered afterwards. 

### [](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_clone_to_an_existing_instance)Clone to an existing instance

When you clone an instance to an existing instance, the database connection URI stays the same, but the data is replaced with the data from the cloned instance.

Cloning into an existing instance will replace all existing data. If you want to keep the current data, take a snapshot and export it.

1.   From the more menu (**…​**) on the instance you want to clone, select **Clone to** and then **Existing instance** from the contextual menu.

2.   Select the existing AuraDB database to clone to from the dropdown menu.

Existing instances that are not large enough to clone into will not be available for selection. 
3.   Check the **I understand the target instance will be overwritten** box and select **Clone**.

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_upgrade_an_instance)Upgrade an instance
------------------------------------------------------------------------------------------------------------

AuraDB Free instances have an **Upgrade** button that you can use to upgrade to either Professional or Business Critical. You can upgrade an AuraDB Professional instance to an Business Critical instance using the **Upgrade** action from the **(…​)** menu.

![Image 3: upgradeprotobc](https://neo4j.com/docs/aura/_images/upgradeprotobc.png)

Figure 3. Upgrade your AuraDB Professional instance to AuraDB Business Critical

This upgrade does not change the original DBID, so your application strings remain valid.

**GDS plugin removal:** If your AuraDB Professional instance uses the GDS plugin, it is removed during the upgrade. The GDS plugin is not supported in AuraDB Business Critical.

**Minimum instance size:** If you try to upgrade a 1GB Professional instance, you need to resize it to at least 2GB of storage, because this is the minimum supported size in AuraDB Business Critical.

Secondaries are read-only copies of your database used for scaling. You can edit the number of secondary copies on applicable instances. See [Secondaries](https://neo4j.com/docs/aura/managing-instances/secondaries/) for more information.

You can clear all data in an instance using the **Reset to blank** action.

Select **Reset to blank** from the **(…​)** more menu on the instance card. You need to confirm your intention since this action cannot be undone.

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_resize_an_instance)Resize an instance
----------------------------------------------------------------------------------------------------------

Resizing an instance means adjusting memory, CPU, and storage size. **Memory and CPU** are configured together, since each instance size pairs a specific amount of memory with a corresponding number of CPUs. A base allocation of storage is also included with each configuration. If you change the memory and CPU, the storage allowance also changes. However, you can also change the storage size independently.

An instance remains available during the resize operation.

Note that this option is **not available** for **Free instances**.

You can change the size of an existing instance using the **Configure** button on the instance you want to resize. From the **Configure Instance** settings, go to **Sizing** and then select the preferred sizes from the dropdown.

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_adjust_memory_and_cpu)Adjust memory and CPU
----------------------------------------------------------------------------------------------------------------

You select the amount of resources you need when you create your AuraDB instance, but this can be adjusted at any time if your needs change.

To adjust memory and CPU, use the **Configure** button on the instance card and select a new value. Note that the included storage value changes automatically when you change the memory and CPU value, but this can be adjusted (see below).

You may **reduce** your memory and CPU, provided that the new value is **equal to or greater** than your current usage.

![Image 4: adjust memory cpu](https://neo4j.com/docs/aura/_images/adjust-memory-cpu.jpg)

Figure 4. Adjust memeory and CPU

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_adjust_storage)Adjust storage
--------------------------------------------------------------------------------------------------

Adjustable storage is available for all AuraDB tiers on the latest Neo4j version — with PAYG (direct) or Prepaid on AWS, Azure and GCP. Available as PAYG on GCP Marketplace for new subscriptions after September 19, 2025, and on AWS Marketplace for new subscriptions after November 19, 2025, and on Azure Marketplace for new subscriptions after January 13, 2026.

Adjust the storage size of your instance at any time. Each AuraDB instance includes a standard storage allocation and configuration; additional storage is chargeable.

To select the storage size during instance creation, select the desired value in the **Storage (Adjustable)** column.

To adjust an existing instance’s storage, use the **Configure** button on the instance card and select a new value for the storage size.

You may reduce your storage allocation, provided the new size is equal to or greater than your current usage. For example, if you are using 8GB of data, the minimum selectable option will be 8GB. Selecting a size smaller than your current usage is not permitted. This store size policy also applies to general instance downsizing.

![Image 5: adjust storage1](https://neo4j.com/docs/aura/_images/adjust-storage1.jpg)

Figure 5. Adjust storage size

Custom endpoints are used for database management and migration. You set up endpoints in the **Project settings**. See [Custom endpoints](https://neo4j.com/docs/aura/managing-instances/custom-endpoints/) for more information.

Admins can mark a database instance as `production` in AuraDB Virtual Dedicated Cloud and AuraDB Business Critical.

When Neo4j updates Aura Database versions, instances marked as `production` are last to have the Aura Database version updated. Because updates are applied to these database instances after other database instances receive updates, you can monitor any potential impact on less critical instances first.

After marking the instance as `production` the label is applied immediately, and all instance actions (such as pause or clone) are temporarily unavailable while the instance is set to `production` in the Neo4j backend.

Use the more menu (**…​**) on the instance card to mark it as `production`.

![Image 6: mark as production](https://neo4j.com/docs/aura/_images/mark-as-production.png)

Figure 6. Mark an instance as production

![Image 7: marked as production](https://neo4j.com/docs/aura/_images/marked-as-production.png)

Figure 7. Instance marked as production

[](https://neo4j.com/docs/aura/managing-instances/instance-actions/#_delete_an_instance)Delete an instance
----------------------------------------------------------------------------------------------------------

Delete an instance using the trashcan icon on the instance card.

Type the exact name of the instance (as instructed) to confirm your decision, and select **Destroy**.

There is no way to recover data from a deleted Aura instance.

On the bottom of the instance card you can find a selection of collapsible metrics. Use the **View all metrics** button to see more. See [View metrics](https://neo4j.com/docs/aura/metrics/view-metrics/) for more information.
