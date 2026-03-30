# Source: https://docs.getint.io/guides/migration/jira-to-monday.com-migration.md

# Jira to Monday.com Migration

Migrating issues, tasks, and projects from Jira to Monday.com is a crucial step when transitioning project management platforms. Whether your team is shifting tools, consolidating data, or merging teams, Getint’s Migration Feature ensures an accurate and structured transfer of historical data.

Unlike standard integrations, which sync new and updated items, the migration feature allows for bulk transfer of existing items while maintaining their associated data, including custom fields, relationships, and hierarchies.

This guide walks you through the step-by-step process of setting up and executing a Jira to Monday migration using Getint.

### **Requirements for Migrating Historical Data** <a href="#requirements-for-migrating-historical-data" id="requirements-for-migrating-historical-data"></a>

#### **Migration License** <a href="#id-1.-migration-license" id="id-1.-migration-license"></a>

Migrating historical data requires a **migration license**, as a standard integration license will not suffice. Migration licenses are billed separately from integration licenses.

To acquire a **migration license**, please visit our [**Pricing Page**](https://www.getint.io/pricing) and click on the **Migration** tab for more details. Contact our team through our [**help page**](https://getint.io/help-center) to proceed with your purchase.

Before purchasing a license, you can test the migration with a **trial version**, which allows:

* **Up to 20 migration runs**
* **A maximum of 5 items per run**

To access the trial version, follow the steps here: [Starting the Free Trial and Access the Getint App](https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app).

Also, see our full migration guide: [Master Jira Migration with Getint - Your Ultimate Guide](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### **Preparing Your Environment Before Migration** <a href="#preparing-your-environment-before-migration" id="preparing-your-environment-before-migration"></a>

#### **Handling Fields That Cannot Be Mapped** <a href="#handling-fields-that-cannot-be-mapped" id="handling-fields-that-cannot-be-mapped"></a>

Before you begin, ensure that all custom fields required on both Jira and Monday.com are created and available. If a counterpart field is missing on either side, it must be created first to allow mapping.

For any custom field creation steps, refer to our guide: [How to Create Custom Fields](https://docs.getint.io/guides/integration-synchronization/how-to-create-a-custom-field-in-all-supported-software).

#### **Migrating Values from Fields Without 1:1 Mapping** <a href="#migrating-values-from-fields-without-1-1-mapping" id="migrating-values-from-fields-without-1-1-mapping"></a>

If a field in Jira doesn’t have a direct counterpart in Monday.com (e.g., assignees, priority), you can still capture its value by using a custom text field and the **Use label from the other side** option.

Steps:

1. Create a custom **Text** field in Monday.com.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3GdZ4aAutNPKzGp2iDmb%2FAdding%20a%20custom%20text%20field%20in%20Monday.png?alt=media&#x26;token=fcdc20b2-4ea5-4106-bfd9-e6db6d9c752f" alt=""><figcaption></figcaption></figure>

1. In the field mapping screen, select the Jira field to be migrated and map it to the new custom field in Monday.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ff0cHNuL8qMsQ2Oy9RFwn%2FUsing%20the%20field%20mapping%20screen.png?alt=media&#x26;token=ed850e09-2a7a-46ce-9a97-cc678cfea69d" alt=""><figcaption></figcaption></figure>

1. Enable **Use label from the other side**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjECCcbAAg5YJXlEboh7o%2FEnable%20Use%20label%20from%20the%20other%20side.png?alt=media&#x26;token=82bfaff2-df8c-41eb-b193-27585615613f" alt=""><figcaption></figcaption></figure>

This approach will insert the label/value of the original field into the destination field. Especially helpful for migrating the Assignees. You probably don’t want to recreate the accounts of people no longer in the company in Jira. This way, no mapping is required; we will inject the value to a text field.

You can also migrate values from **multiple source fields into one** text field. You can read more about how to set up this option [here](https://docs.getint.io/guides/integration-synchronization/how-to-map-fields#concatenating-fields).

For more tips, refer to [Master Jira Migration with Getint - Your Ultimate Guide](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### **How to Set Up Your Jira to Monday.com** **Migration** <a href="#how-to-set-up-your-jira-to-monday.com-migration" id="how-to-set-up-your-jira-to-monday.com-migration"></a>

#### **1. Set Up a Jira to Monday.com** **Integration** <a href="#id-1.-set-up-a-jira-to-monday.com-integration" id="id-1.-set-up-a-jira-to-monday.com-integration"></a>

Before migration, you must set up an integration between Jira and Monday.com. Follow our [Jira-Monday Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-monday.com-integration) to configure the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F95EEUS4f58GTV74T5m0q%2FJira%20Monday%20integrations.png?alt=media&#x26;token=f3856ae8-acfc-4da9-adba-c1bc911f6cf9" alt=""><figcaption></figcaption></figure>

#### **2. Access the Migration Feature** <a href="#id-2.-access-the-migration-feature" id="id-2.-access-the-migration-feature"></a>

Once your integration is set, open the **Getint App** and:

* Click **Migrate Data** from the left-side menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQbQsRRN631OyaCUbNgRc%2FClick%20the%20migrate%20data%20button.png?alt=media&#x26;token=42cc64a4-9c43-4471-a0f4-f6e2528fc0f7" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you're using a **trial version**, a warning will appear indicating your **migration run limitations**. Each trial migration run allows **only 5 items** to be transferred, and **20 runs.**
{% endhint %}

* Check the **Enable Migration on the Next Run** box to proceed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNAnR84uL4PvL0jFwrj2S%2Fenable%20migration%20on%20the%20next%20run%20Jira%20Monday.png?alt=media&#x26;token=45656f80-b99c-481e-8961-0aaceecc785e" alt=""><figcaption></figcaption></figure>

#### **3. Configure Migration Settings** <a href="#id-3.-configure-migration-settings" id="id-3.-configure-migration-settings"></a>

* **Migration Direction**: Define whether data flows from **Jira to Monday** or **vice versa**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fl92sjc5X6jN6ACAaqNfF%2FMigration%20direction.png?alt=media&#x26;token=803ba6fd-f379-4cd6-8058-a73959130407" alt=""><figcaption></figcaption></figure>

* **Handling of Previously Migrated Items**: Choose how to handle items that were already migrated:
  * **Replace** (overwrite existing items).
  * **Update** (sync only new changes).
  * **Skip** (ignore already migrated items).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fn79H6E22pwjxvsoYiEeT%2Fmigration%20configuration%20Jira%20Monday.png?alt=media&#x26;token=7246fdf2-4927-4535-9583-109573503f96" alt=""><figcaption></figcaption></figure>

* **Selective Resync (Optional)**: If a previous migration was incomplete, choose specific fields to **resync**, such as **Assignee, Status, and Description**.
  * To resync **all fields**, enter **ALL**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FanXzqq3fcg0EmJI4TJUj%2FEnter%20fields%20that%20should%20be%20resynced.png?alt=media&#x26;token=efdcb66f-2ac5-45a1-bdc3-bb2e4407d9cd" alt=""><figcaption></figcaption></figure>

* **Selective Item Migration (Optional)**:
  * Enter specific **item IDs** to migrate **only selected tasks**.
  * Use **JQL filtering** for refined selection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhnyxrHaV06tSVMkuS6hG%2Fitems%20that%20should%20be%20migrated%20Monday.com%20migration.png?alt=media&#x26;token=c1200565-6c31-48f6-8385-ddee10c08c20" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Important:** Ensure that your **JQL filter or item IDs align with the creation/updating date range** to avoid missing items during migration.
{% endhint %}

* **Time Range Filtering**:
  * Select a **creation date range** in the **UTC timezone**.
  * Only issues created or updated **within the selected period** will be migrated.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKhNF9TNhbwhTRtCU4F9V%2FTime%20range%20filtering.png?alt=media&#x26;token=8a59f93a-3ab3-43e7-95da-4e20ca589562" alt=""><figcaption></figcaption></figure>

#### **4. Schedule and Execute Migration** <a href="#id-4.-schedule-and-execute-migration" id="id-4.-schedule-and-execute-migration"></a>

* Click **Schedule Migration** to queue the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FU0pLzb94JkKgRSIk57ST%2Fschedule%20and%20execute%20migration.png?alt=media&#x26;token=20a7d886-31ff-46f4-9952-14954cc12d19" alt=""><figcaption></figcaption></figure>

* The system will begin migration during the next synchronization run.
* Monitor progress in the **Reporting section** or the **Latest Runs tab**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDy4G9FprUGIFovixVrRl%2FChecking%20latest%20runs.png?alt=media&#x26;token=fb996386-8004-476a-b94e-4eac51d6b357" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Migration runs appear under the **Mode** column as **MIGRATION** instead of **SYNC**.
{% endhint %}

#### **5. Enable Continuous Sync After Migration (Optional)** <a href="#id-5.-enable-continuous-sync-after-migration-optional" id="id-5.-enable-continuous-sync-after-migration-optional"></a>

If you want to keep the items in sync after migration:

* Open the **Integration Settings**.
* Click **More > Enable Continuous Sync**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvV9LDwGoUkP183Tb1YMR%2Fimage-20250318-184154.png?alt=media&#x26;token=5730d799-9be4-4305-ac5b-31599173e48e" alt=""><figcaption></figcaption></figure>

You can also uncheck the box below when you are setting up the migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMjXamgy24VKWpQRCysrb%2Fimage-20250318-184532.png?alt=media&#x26;token=115bd64a-bc59-44c0-98dd-ac8c633d9a2c" alt=""><figcaption></figcaption></figure>

This ensures that **newly created** tasks, issues, and updates flow **between Jira and Monday.com** moving forward.

### **Why Choose Getint Migration Over CSV Import?** <a href="#why-choose-getint-migration-over-csv-import" id="why-choose-getint-migration-over-csv-import"></a>

Traditional CSV imports require manual data manipulation and lack automation, often leading to data loss and inconsistency. Getint eliminates these issues by providing:

#### **1. Smart Field Mapping** <a href="#id-1.-smart-field-mapping" id="id-1.-smart-field-mapping"></a>

✔ Getint enables precise **manual field mapping**, ensuring correct **data alignment**\
❌ CSV imports require **manual restructuring** after import

#### **2. Selective Migration** <a href="#id-2.-selective-migration" id="id-2.-selective-migration"></a>

✔ Getint supports **JQL filtering, item ID selection, and date-based migration**\
❌ CSV imports transfer **all data**, requiring **manual clean-up**

#### **3. Real-Time Monitoring** <a href="#id-3.-real-time-monitoring" id="id-3.-real-time-monitoring"></a>

✔ Getint provides **sync logs, error tracking, and live migration updates**\
❌ CSV imports offer **no real-time feedback**

#### **4. Seamless Integration** <a href="#id-4.-seamless-integration" id="id-4.-seamless-integration"></a>

✔ Getint **automatically syncs** data post-migration\
❌ CSV imports require **additional steps** to align projects and workflows

### **Need Help?** <a href="#need-help" id="need-help"></a>

For additional **assistance or troubleshooting**, visit our [**Help Center**](https://getint.io/help-center).

Considering migration? [**Schedule a Demo**](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team) with our **experts** to explore how **Getint** can optimize your **Jira to Monday.com** migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
