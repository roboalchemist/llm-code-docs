# Source: https://docs.getint.io/guides/migration/migrating-data-with-getint.md

# Migrating Data with Getint

Migrating data between project management tools is a critical step in ensuring seamless transitions during tool changes, company mergers, or acquisitions. Whether you are moving from Azure DevOps, ServiceNow, Asana, or Monday to Jira, or the other way around, consolidating multiple Jira instances, or onboarding Company B’s project data into Company A’s system, Getint’s Migration Feature ensures a smooth and structured transfer of historical issues, tasks, bugs, and more.

Unlike traditional CSV export/import, Getint’s migration offers granular control, automation, and real-time monitoring, eliminating manual errors and data inconsistencies.

### Migration Licensing <a href="#migration-licensing" id="migration-licensing"></a>

Migration is a **premium feature** and is **billed separately** from continuous integration. This ensures an advanced migration experience with **enhanced customization, support, and additional features**.

Before starting your migration, review our [**Migration Pricing Guide**](https://www.getint.io/pricing) for detailed licensing options. If you have any questions, reach out to our [Support.](https://getint.io/help-center)

### **Preparing Your Environment Before Migration** <a href="#preparing-your-environment-before-migration" id="preparing-your-environment-before-migration"></a>

To ensure a smooth migration, consider the following:

* Ensure Matching Fields Exist: If your source system includes fields that do not exist in the destination system, you must create them beforehand. This ensures that 1:1 field mapping can be applied where necessary.
* Handling Fields That Cannot Be Mapped: If some fields cannot be mapped directly, you can still migrate their values. Create a custom text field on the destination tool and map the original field to it, enabling the **Use label from the other side** option. This will transfer the field's value as plain text without requiring a matching field type.
* For advanced use cases, it is also possible to migrate values from multiple source fields into a single text field using a merging option or, if necessary, a custom script. This can be useful when a 1:1 mapping is not required or feasible. For more information on how to merge fields, follow our guide [here](https://docs.getint.io/guides/integration-synchronization/how-to-map-fields#concatenating-fields).

For more tips, refer to [Master Jira Migration with Getint - Your Ultimate Guide](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### Setting Up Your Migration <a href="#setting-up-your-migration" id="setting-up-your-migration"></a>

#### A. Connecting for the First Time and Migrating <a href="#id-1.-connecting-for-the-first-time-and-migrating" id="id-1.-connecting-for-the-first-time-and-migrating"></a>

#### **Create a Connection to Migrate**

1. Open the **Getint App** and select **Create an Integration**.
2. In the pop-up window, choose **Migration** as the integration type.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FL7X0l57FnovAV0TtdUs9%2FData%20migration%20with%20Getint.png?alt=media&#x26;token=29922ab6-dc33-4a67-b5ef-b5b43313c01d" alt=""><figcaption></figcaption></figure>

#### **Set Up the Integration**

1. Select the apps involved in the migration. We recommend checking our documentation to review how to create the integrations: [Integration Guides](https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app/jira-access-and-user-management#jira-server-data-center-dc).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNT9CJ09UqvoKRoYDWfbx%2FSelect%20the%20app%20for%20migration.png?alt=media&#x26;token=cd517892-6586-42e6-82b1-374668cdcce7" alt=""><figcaption></figcaption></figure>

1. Map issue types, according to your needs, between the two systems.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F98B5n6cAsIk7U80dGIgS%2FMap%20issues%20accordingly.png?alt=media&#x26;token=b22def04-3ec3-41b9-83f0-d651dcabb519" alt=""><figcaption></figcaption></figure>

1. Ensure that the fields are mapped correctly. Follow our guides for each app integration to ensure proper mapping.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLiAZLweJSh1PgFFjBK4k%2FEnsure%20all%20fields%20are%20mapped%20properly.png?alt=media&#x26;token=892e2d4a-3427-4ccc-a5bc-76509462a29e" alt=""><figcaption></figcaption></figure>

1. Name the integration and save the configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsaHUsbCehafDs7fFNVvp%2FName%20and%20save%20your%20integration.png?alt=media&#x26;token=f9cff86c-cc35-4e1f-a338-6659faff8b99" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The migration will be created but disabled by default; its status will change once the settings are properly configured.
{% endhint %}

#### **Configure Migration Settings**

With the integration properly configured, it is now time to set up the migration. Go to the **Migrate Data tab** and click **Enable the Migration on the next run.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fauud2ke31GjiS3xup9Ht%2FMigration%20configuration%20with%20Getint.png?alt=media&#x26;token=86d7c983-a6d2-4338-9dd5-ebbfb0a78cd2" alt=""><figcaption></figcaption></figure>

1. **Select Migration Direction**: Define if the items from the app on the left will be migrated to the right or from the app on the right to the left.ft

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FcyK4Plcy5aNvcudQ6BiJ%2FSelect%20a%20side%20to%20move%20the%20items.png?alt=media&#x26;token=6327ce4c-742a-41eb-a759-73321a6c36a6" alt=""><figcaption></figcaption></figure>

1. **Decide on what to do with the items already migrated**: Define whether items will be **recreated, updated, or skipped** if they already exist in the target system.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fv8h5pe5ccXPVy3DOqSyg%2FDecide%20on%20what%20to%20do%20with%20items%20that%20were%20already%20migrated.png?alt=media&#x26;token=2d251855-ab68-4747-b7e5-1430f73b5423" alt=""><figcaption></figcaption></figure>

1. **Field Resynchronization (Optional)**: If you’ve **previously migrated data** and want to update specific fields (e.g., **Assignee, Status, Description**), specify them here. To resync all fields, enter **\_*****ALL*****\_** or leave the field blank.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAQrUqiFslCRyFKzZs6ph%2Ffields%20that%20should%20be%20resynced.png?alt=media&#x26;token=7aa0f48b-d0c6-4b42-aece-780fe67f680f" alt=""><figcaption><p>To ensure the integration continues after migration, disable the option to interrupt it.</p></figcaption></figure>

1. **Selective Migration (Optional)**:

* Provide specific **item IDs** for migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMdKdbBp8tIUG4OEfQaJi%2Fitems%20that%20should%20be%20migrated%20Asana.png?alt=media&#x26;token=b96755b0-b214-4c23-9065-1f3d73d4127d" alt=""><figcaption></figcaption></figure>

* Use **JQL filtering** for more refined data selection. JQL filters can be accessed by clicking the app logo in the integration. You can find more details on filtering in our guide: [Filtering Items for Integration in Getint](https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fh48S5GVEUEaYcrMvDYUC%2FJQL%20filtering.png?alt=media&#x26;token=4691ca4d-9c75-43c1-ad3e-53aa8384a8a3" alt=""><figcaption></figcaption></figure>

1. **Set a Time Range:** To filter which items should be migrated, select the creation date or the last updated date in UTC.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbncxRpypbPb6LV2tbVWR%2FSet%20a%20time%20range.png?alt=media&#x26;token=63b95222-4746-4c37-bfa6-7aa6235b11e5" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note that if the items were not updated or created within the selected time range, Getint will not migrate them.
{% endhint %}

1. **Start the Migration**: Click **Schedule Migration** to begin the process. Migration time depends on the volume of data.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqAymezpjyYU0UPQby4jh%2FSchedule%20the%20migration.png?alt=media&#x26;token=15169e0a-a9dd-40bd-9144-a534b7e32636" alt=""><figcaption></figcaption></figure>

1. Getint will be in migration mode. Monitor progress in **sync logs** to ensure a smooth transfer.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMj8uTwaQ9vDeo8BcISgS%2Fmigration%20mode.png?alt=media&#x26;token=59519a8b-2fcc-4519-9118-2208a543edb4" alt=""><figcaption></figcaption></figure>

1. **Enable Continuous Sync (Optional)**

If you want **newly created issues** to continue syncing after migration:

Disable the option to stop the sync after the migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYIxPnwxCEd1mwPGWqmgF%2FDisable%20the%20option%20to%20stop%20the%20sync%20after%20the%20migration.png?alt=media&#x26;token=c757b393-be0b-4c49-860d-bcc27d64aa36" alt=""><figcaption></figcaption></figure>

Or change the settings after the Migration:

* Go to your integration, click **More >Settings> Enable**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIFWdzHryiznGdMevQEe6%2FEnable%20the%20integration%20after%20the%20migration%20run.png?alt=media&#x26;token=1a351c8c-6900-41ef-8b5c-a578391a8e31" alt=""><figcaption></figcaption></figure>

By default, the integration is disabled after migration to **prevent unintended updates**.

#### B. Migrating on an Existing Integration <a href="#id-2.-migrating-on-an-existing-integration" id="id-2.-migrating-on-an-existing-integration"></a>

If you already have a **continuous sync in place** but need to **migrate older items**, follow these steps:

1. Open the **Getint App** and navigate to your **existing integration**.
2. Select **Migrate Data** from the left-hand menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRAwxPkpql31LIXlUIdF2%2Fmigrate%20data%20on%20an%20existing%20integration.png?alt=media&#x26;token=bde7f12e-d881-4505-af03-119f6a5ba63e" alt=""><figcaption></figcaption></figure>

1. Configure the migration settings as described in the previous section.
2. **Enable migration** for the next sync run.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGdarvEUk36LRBVgdPiel%2Fenable%20migration%20on%20the%20next%20sync%20run.png?alt=media&#x26;token=deb1af3c-b5fb-4346-a64d-7301a04dd1a6" alt=""><figcaption></figcaption></figure>

1. **Monitor progress** on the latest runs and logs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMFVM2b9jUyyFtrNHlMYA%2Fmonitor%20progress.png?alt=media&#x26;token=b4e367c4-d2c5-4bce-9ec6-665c53b1a26f" alt=""><figcaption></figcaption></figure>

### Getint Migration vs. Traditional CSV Import <a href="#getint-migration-vs.-traditional-csv-import" id="getint-migration-vs.-traditional-csv-import"></a>

Many companies use CSV exports/imports for migration, but Getint’s Migration Feature provides several advantages:

#### **1. Advanced Field Mapping** <a href="#id-1.-advanced-field-mapping" id="id-1.-advanced-field-mapping"></a>

* Getint allows users to manually map issue types and fields, ensuring precise data transfer.
* Traditional CSV imports require rigid predefined templates, making data structuring complex.

#### **2. Granular Field Resynchronization** <a href="#id-2.-granular-field-resynchronization" id="id-2.-granular-field-resynchronization"></a>

* With Getint, specific fields can be resynced on demand, preventing unnecessary updates.
* CSV imports lack flexibility—you must re-import everything or risk data loss.

#### **3. Selective Data Migration** <a href="#id-3.-selective-data-migration" id="id-3.-selective-data-migration"></a>

* Getint lets you filter specific items by ID or JQL queries to migrate only what’s necessary.
* CSV methods require manual filtering and do not offer dynamic selection.

#### **4. Real-Time Monitoring & Automation** <a href="#id-4.-real-time-monitoring-and-automation" id="id-4.-real-time-monitoring-and-automation"></a>

* Getint provides live tracking of migration progress with sync logs.
* Traditional CSV methods lack real-time updates—errors may go unnoticed until post-import verification.

#### **5. Seamless Integration with Existing Workflows** <a href="#id-5.-seamless-integration-with-existing-workflows" id="id-5.-seamless-integration-with-existing-workflows"></a>

* Getint migration works alongside existing integrations, allowing continuous sync post-migration.
* CSV imports often overwrite or duplicate data, requiring additional cleanup.

By choosing Getint’s Migration Feature, your organization benefits from precision, automation, and full control over the migration process.

### Need Assistance? <a href="#need-assistance" id="need-assistance"></a>

For **additional support**, visit our [**Help Center**](https://getint.io/help-center).

**Considering migration?** [**Schedule a Demo**](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team) with our team to explore how Getint can support your transition.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
