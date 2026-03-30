# Source: https://docs.getint.io/guides/migration/azure-devops-to-jira-migration.md

# Jira to Azure DevOps Migration

Migrating Epics, tasks, and work items from Jira to Azure DevOps is a critical step for organizations consolidating platforms or transitioning development and support workflows. With Getint, this migration process becomes straightforward, accurate, and reliable.

Getint ensures that all essential data, including issue types, custom fields, and relationships, are transferred while preserving the integrity and hierarchy of your records. Whether you're moving an entire backlog or selectively migrating specific items, this guide walks you through the process step-by-step.

### Requirements for Migrating Historical Data <a href="#requirements-for-migrating-historical-data" id="requirements-for-migrating-historical-data"></a>

#### Migration License <a href="#migration-license" id="migration-license"></a>

Migrating historical data requires a migration license, as integration licenses alone do not support this functionality. Migration licenses are billed separately.

To purchase a license, visit our [Pricing Page](https://www.getint.io/pricing) and select the "Migration" tab. You can also contact our team via the [Help Center](https://getint.io/help-center) for assistance.

Before purchasing, we encourage you to test the process using our trial version, which allows:

* Up to 20 migration runs
* A maximum of 5 items per run

To begin your trial, visit: [Azure DevOps Integration for Jira (Azure DevOps Connector)](https://marketplace.atlassian.com/apps/1223931/azure-devops-integration-for-jira-azure-devops-connector?hosting=cloud\&tab=overview)

For best practices and advanced tips, see: [Master Jira Migration with Getint](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### Preparing Your Environment Before Migration <a href="#preparing-your-environment-before-migration" id="preparing-your-environment-before-migration"></a>

#### Handling Fields That Cannot Be Mapped <a href="#handling-fields-that-cannot-be-mapped" id="handling-fields-that-cannot-be-mapped"></a>

Before starting your migration, ensure that custom fields used in Azure DevOps also exist in Jira. If the destination field is missing, it must be created manually to enable proper mapping.

For steps to create fields in both tools, refer to: [How to Create Custom Fields](https://docs.getint.io/guides/integration-synchronization/how-to-create-a-custom-field-in-all-supported-software#hardbreak-azure-devops).

#### Migrating Values Without 1:1 Mapping <a href="#migrating-values-without-1-1-mapping" id="migrating-values-without-1-1-mapping"></a>

If a field in Azure DevOps doesn’t have a direct counterpart in Jira or you want to avoid the 1:1 mapping, you can use the **Use label from the other side** option to inject its value into a custom text field.

**Steps:**

* Create a text custom field in Azure DevOps.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpzDvf5Rf2blw7Hj9MVOU%2FCreate%20a%20custom%20field%20in%20Azure%20DevOps.png?alt=media&#x26;token=62d2bbf7-82d9-4e62-bb59-bcda4f56bc09" alt=""><figcaption></figcaption></figure>

* In the Getint field mapping screen, map the source Azure DevOps field to the Jira text field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4Tp7DUr0rnDfwNQyvX9a%2Fmapping%20the%20custom%20field%20in%20Azure.png?alt=media&#x26;token=ff76e065-671a-4881-ac76-d689367ae95d" alt=""><figcaption></figcaption></figure>

* Enable **Use label from the other side** to insert the original value.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIuUUNbxAP8Jpm7QCUMsC%2Fuse%20label%20from%20other%20side%20Jira%20Azure.png?alt=media&#x26;token=28b12597-6f67-42ae-9143-e8cf40ec985e" alt=""><figcaption></figcaption></figure>

This approach will insert the label/value of the original field into the destination field. Especially helpful for migrating the Assignees. You probably don’t want to recreate the accounts of people no longer in the company in Jira. This way, no mapping is required; we will inject the value into a text field.

You can also migrate values from **multiple source fields into one** text field. You can read more about how to set up this option [here](https://docs.getint.io/guides/integration-synchronization/how-to-map-fields#concatenating-fields).

For more tips, refer to: [Master Jira Migration with Getint - Your Ultimate Guide](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### Setting Up Your Azure DevOps to Jira Migration <a href="#setting-up-your-azure-devops-to-jira-migration" id="setting-up-your-azure-devops-to-jira-migration"></a>

#### 1. Set Up the Integration <a href="#id-1.-set-up-the-integration" id="id-1.-set-up-the-integration"></a>

Before migrating, you must set up a working integration between Jira and Azure DevOps. Follow our full integration guide, [Jira Azure DevOps Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration), to configure your connection properly.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmHL3ePjZNb7xfL7lpFsv%2FJira%20Azure%20Migration.png?alt=media&#x26;token=d9d95ed8-63c5-4b33-96bd-679f72d77640" alt=""><figcaption></figcaption></figure>

After setup, we recommend disabling the integration or pausing activity in both tools during migration to avoid sync conflicts.

#### 2. Access the Migration Feature <a href="#id-2.-access-the-migration-feature" id="id-2.-access-the-migration-feature"></a>

Once your integration is set:

* Click **Migrate Data** from the left-side menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FN4qV2A2sfVgfJKoNFgs6%2FJira%20Azure%20Migration%20Setup.png?alt=media&#x26;token=08a22f37-e623-4520-b13d-7e8aa4210ddb" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If you're on a trial version, a warning will appear regarding your migration limits (5 items per run, 20 runs).
{% endhint %}

* Enable **Migration on Next Run** to proceed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtnIaYWS8PNOX2dxaXQIL%2FEnable%20migration%20in%20the%20next%20run%20Azure.png?alt=media&#x26;token=ce7c8159-b43a-4df4-9db6-fdac9857fb0b" alt=""><figcaption></figcaption></figure>

#### 3. Configure Migration Settings <a href="#id-3.-configure-migration-settings" id="id-3.-configure-migration-settings"></a>

* **Migration Direction:** Choose whether data flows from Azure DevOps to Jira or vice versa.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2T5dRDuJdOHvJ8AvUfAY%2Fconfigure%20migration%20settings.png?alt=media&#x26;token=7593f941-076f-4bf5-9292-3376715c0563" alt=""><figcaption></figcaption></figure>

* **Handling Previously Migrated Items:** Choose how to handle items that were already migrated:
  * **Replace** (overwrite existing items).
  * **Update** (sync only new changes).
  * **Skip** (ignore already migrated items).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxR15fCl6XSwuhZFtnj1U%2Fhandling%20previously%20migrated%20items.png?alt=media&#x26;token=9fd1d89f-c909-4f70-9c35-febfbdd42795" alt=""><figcaption></figcaption></figure>

* **Selective Resync (Optional)**: If a previous migration was incomplete, choose specific fields to **resync**, such as **Assignee, Status, and Description**.
  * To resync **all fields**, enter ***ALL**.*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYNcO6muware6HZM7JZza%2Fimage-20250523-130947.png?alt=media&#x26;token=82f08bf0-0f24-4987-8766-9bc13846b73a" alt=""><figcaption></figcaption></figure>

* **Selective Item Migration (Optional)**:
  * Enter specific **item IDs** to migrate **only selected tasks**.
  * Use **JQL filtering** for refined selection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoLrap4iw5XORIS36RJyH%2Fimage-20250523-131103.png?alt=media&#x26;token=33ceb6e0-b674-4318-9c3b-447ab412c357" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Important:** Ensure that your **JQL filter or item IDs align with the creation/updating date range** to avoid missing items during migration. Learn more: [Filtering Items for Integration](https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint).
{% endhint %}

* **Time Range Filtering:**
  * Select a **creation date range** in the **UTC timezone**.
  * Only issues created or updated **within the selected period** will be migrated.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMGZrMQO1xaLGJhgQwB8i%2Fimage-20250523-131322.png?alt=media&#x26;token=e5a678b6-5cff-4015-8f57-0606e01125b5" alt=""><figcaption></figcaption></figure>

#### 4. Schedule and Run the Migration <a href="#id-4.-schedule-and-run-the-migration" id="id-4.-schedule-and-run-the-migration"></a>

When your settings are complete, click **Schedule Migration** at the bottom of the screen.

* Click **Schedule Migration** to queue the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDbwJaUrzp1IceajTLkvN%2Fimage-20250523-131558.png?alt=media&#x26;token=e101f590-8137-475a-925b-8e02872b8f98" alt=""><figcaption></figcaption></figure>

* The system will begin migration during the next synchronization run.
* Monitor progress in the **Reporting section** or the **Latest Runs tab**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLMTmoSTXztlRkJrQHFM4%2Fimage-20250523-131516.png?alt=media&#x26;token=b78ef2c3-c451-4f2f-a31a-14f23488fa73" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Migration runs appear under the **Mode** column as **MIGRATION** instead of **SYNC**.
{% endhint %}

#### **5. Enable Continuous Sync After Migration (Optional)** <a href="#id-5.-enable-continuous-sync-after-migration-optional" id="id-5.-enable-continuous-sync-after-migration-optional"></a>

If you want to keep the items in sync after migration:

* Open the **Integration Settings**.
* Click **More > Enable Continuous Sync**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVAtUH8FJ12qL34ca3sOk%2Fimage-20250523-131839.png?alt=media&#x26;token=bf53a187-b090-42f1-8ece-a18c952ae3ed" alt=""><figcaption></figcaption></figure>

You can also uncheck the box below when you are setting up the migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGSvfgOEKyKwlYxDPNg1t%2Fimage-20250523-131757.png?alt=media&#x26;token=7cea7425-52d7-4ef5-8cda-14206b62f7e0" alt=""><figcaption></figcaption></figure>

This ensures that **newly created** tasks, issues, and updates flow **between Jira and Azure DevOps** moving forward.

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

Considering migration? [**Schedule a Demo**](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team) with our **experts** to explore how **Getint** can optimize your **Jira to Azure DevOps** migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
