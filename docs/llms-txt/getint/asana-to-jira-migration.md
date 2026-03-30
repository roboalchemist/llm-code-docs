# Source: https://docs.getint.io/guides/migration/asana-to-jira-migration.md

# Jira to Asana Migration

Migrating tasks and projects from Asana to Jira is an important process when transitioning between project management platforms. Whether you're unifying workflows, scaling operations, or consolidating tools across departments, Getint’s Migration Feature ensures a structured and accurate transfer of historical data.

Unlike standard integrations that sync only newly created or updated items, the migration feature enables a one-time, bulk transfer of existing data while preserving essential details such as custom fields, status, relationships, and item types.

This guide walks you through the steps to configure and execute a migration from Asana to Jira using Getint.

### Requirements for Migrating Historical Data <a href="#requirements-for-migrating-historical-data" id="requirements-for-migrating-historical-data"></a>

#### Migration License <a href="#migration-license" id="migration-license"></a>

Migrating historical data requires a migration license, as integration licenses alone do not support this functionality. Migration licenses are billed separately.

To purchase a license, visit our [Pricing Page](https://www.getint.io/pricing) and select the "Migration" tab. You can also contact our team via the [Help Center](https://getint.io/help-center) for assistance.

Before purchasing, we encourage you to test the process using our trial version, which allows:

* Up to 20 migration runs
* A maximum of 5 items per run

To begin your trial, visit: [Getint for Asana and Jira on Atlassian Marketplace](https://marketplace.atlassian.com/apps/1223932/asana-integration-for-jira-2-way-sync-and-data-migration?hosting=cloud\&tab=overview)

For best practices and advanced tips, see: [Master Jira Migration with Getint](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint)

### Preparing Your Environment Before Migration <a href="#preparing-your-environment-before-migration" id="preparing-your-environment-before-migration"></a>

#### Handling Fields That Cannot Be Mapped <a href="#handling-fields-that-cannot-be-mapped" id="handling-fields-that-cannot-be-mapped"></a>

Before starting the migration, ensure that all required custom fields exist on both Asana and Jira. If a field does not exist on one side, you must create it before attempting to map it.

Need help? Refer to: [How to Create Custom Fields](https://docs.getint.io/guides/integration-synchronization/how-to-create-a-custom-field-in-all-supported-software#hardbreak-asana).

#### Migrating Values Without 1:1 Mapping <a href="#migrating-values-without-1-1-mapping" id="migrating-values-without-1-1-mapping"></a>

If a field in Asana doesn’t have a direct counterpart in Jira, you can use the **Use label from the other side** option to inject its value into a custom text field.

**Steps:**

* Create a custom Text field in Asana.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjV3EFDOyvvjTKSlxjRPX%2Fimage-20250512-123626.png?alt=media&#x26;token=c4745cca-0dc8-4b6f-808f-e936df3fc380" alt=""><figcaption></figcaption></figure>

* In the Getint field mapping screen, map the source Asana field to the Jira text field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHyU4ZnAYjT1mzZjWv6zA%2Fimage-20250512-123903.png?alt=media&#x26;token=5ee09a3d-c1cb-4610-bcef-22bbcbdd2d1b" alt=""><figcaption></figcaption></figure>

* Enable **Use label from the other side** to insert the original value.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0MZYv42b7ypYLJmtPjnX%2Fimage-20250512-123959.png?alt=media&#x26;token=b3d1bf63-d2b2-4c9e-aab1-a325ad66d660" alt=""><figcaption></figcaption></figure>

This approach will insert the label/value of the original field into the destination field. Especially helpful for migrating the Assignees. You probably don’t want to recreate the accounts of people no longer in the company in Jira. This way, no mapping is required; we will inject the value into a text field.

You can also migrate values from **multiple source fields into one** text field. You can read more about how to set up this option [here](https://docs.getint.io/guides/integration-synchronization/how-to-map-fields#concatenating-fields).

For more tips, refer to [Master Jira Migration with Getint - Your Ultimate Guide](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### How to Set Up Your Asana to Jira Migration <a href="#how-to-set-up-your-asana-to-jira-migration" id="how-to-set-up-your-asana-to-jira-migration"></a>

#### 1. Set Up an Asana to Jira Integration <a href="#id-1.-set-up-an-asana-to-jira-integration" id="id-1.-set-up-an-asana-to-jira-integration"></a>

Before migrating, you must set up a working integration between Jira and Asana. Follow our full [Jira-Asana Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-asana-integration) to configure your connection properly.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSvy95z9Kvshil5z0p8mM%2Fimage-20250512-124531.png?alt=media&#x26;token=0224910d-eba6-476c-abd8-0668b5da5478" alt=""><figcaption></figcaption></figure>

To avoid live data conflicts, we recommend either disabling the integration after setup or scheduling the migration outside of active working hours.

#### 2. Access the Migration Feature <a href="#id-2.-access-the-migration-feature" id="id-2.-access-the-migration-feature"></a>

Once your integration is set:

* Click **Migrate Data** from the left-side menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdrtpInX8JzdfzQX0V0lm%2Fimage-20250512-125316.png?alt=media&#x26;token=5e2f9ecd-9cf6-439c-b772-91f500e5d21e" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If you're on a trial version, a warning will appear regarding your migration limits (5 items per run, 20 runs).
{% endhint %}

* Check the **Enable Migration on the Next Run** box to proceed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgadajEQ4kTU24NjEcZ9E%2Fimage-20250512-125558.png?alt=media&#x26;token=acb0d343-8551-4d9e-bb79-96a34fd92330" alt=""><figcaption></figcaption></figure>

#### 3. Configure Migration Settings <a href="#id-3.-configure-migration-settings" id="id-3.-configure-migration-settings"></a>

* **Migration Direction:** Choose whether data flows from Asana to Jira or vice versa.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZaqQt83Ese1D2djmuzlQ%2Fimage-20250512-125705.png?alt=media&#x26;token=e6c4edc7-79ef-44c3-8b25-e06474986abf" alt=""><figcaption></figcaption></figure>

* **Handling Previously Migrated Items:** Choose how to handle items that were already migrated:
  * **Replace** (overwrite existing items).
  * **Update** (sync only new changes).
  * **Skip** (ignore already migrated items).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdRNDAuISjwsO7seO1AMz%2Fimage-20250512-125821.png?alt=media&#x26;token=25d81f7b-5429-4c0b-ae7b-87aebdb4c03f" alt=""><figcaption></figcaption></figure>

* **Selective Resync (Optional)**: If a previous migration was incomplete, choose specific fields to **resync**, such as **Assignee, Status, and Description**.
  * To resync **all fields**, enter ***ALL**.*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPPNPalCKtrdlhqNF2EQU%2Fimage-20250512-130254.png?alt=media&#x26;token=20265acc-6a3a-497c-80ef-e04472dd2e5b" alt=""><figcaption></figcaption></figure>

* **Selective Item Migration (Optional)**:
  * Enter specific **item IDs** to migrate **only selected tasks**.
  * Use **JQL filtering** for refined selection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSsDfVm3pzYRUCCRqkbEU%2Fimage-20250512-140152.png?alt=media&#x26;token=cb91ba8a-0acd-4b17-a6b9-b3b580fd3d0c" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Important:** Ensure that your **JQL filter or item IDs align with the creation/updating date range** to avoid missing items during migration.
{% endhint %}

* **Time Range Filtering:**
  * Select a **creation date range** in the **UTC timezone**.
  * Only issues created or updated **within the selected period** will be migrated.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLZfYYu3i2xtfj3AbmeBF%2Fimage-20250512-140320.png?alt=media&#x26;token=3d628d54-3843-46bf-bef1-d7bb9b778e27" alt=""><figcaption></figcaption></figure>

#### 4. Schedule and Run the Migration <a href="#id-4.-schedule-and-run-the-migration" id="id-4.-schedule-and-run-the-migration"></a>

* Click **Schedule Migration** to queue the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fz2H6pQvQ6vEFueqHMnqA%2Fimage-20250512-140451.png?alt=media&#x26;token=935d2c4f-9efe-4510-b684-adbb75dbf51c" alt=""><figcaption></figcaption></figure>

* The system will begin migration during the next synchronization run.
* Monitor progress in the **Reporting section** or the **Latest Runs tab**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9I93s40uthydlKArWKxH%2Fimage-20250512-140605.png?alt=media&#x26;token=5a4f893c-c72d-47c0-9f3b-8732cf08e89f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Migration runs appear under the **Mode** column as **MIGRATION** instead of **SYNC**.
{% endhint %}

#### 5. Enable Continuous Sync After Migration (Optional) <a href="#id-5.-enable-continuous-sync-after-migration-optional" id="id-5.-enable-continuous-sync-after-migration-optional"></a>

If you want to keep the items in sync after migration:

* Open the **Integration Settings**.
* Click **More > Enable Continuous Sync**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Frb861nQrkzpw6C0jtivW%2Fimage-20250512-140811.png?alt=media&#x26;token=7ce59181-861f-4dcf-bba0-a8e8f42f3040" alt=""><figcaption></figcaption></figure>

Alternatively, you can uncheck the disable box when setting up the migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F67jPVRSm3xwinnGkbzyn%2Fimage-20250512-140848.png?alt=media&#x26;token=bd21e263-3330-4c61-b048-a0be5f4a54c4" alt=""><figcaption></figcaption></figure>

This ensures that **newly created** tasks, issues, and updates flow **between Jira and Zendesk** moving forward.

### Why Choose Getint Migration Over CSV Import? <a href="#why-choose-getint-migration-over-csv-import" id="why-choose-getint-migration-over-csv-import"></a>

Traditional CSV methods can result in data loss, manual fixes, and inconsistencies. Getint Migration offers key advantages:

#### 1. Smart Field Mapping <a href="#id-1.-smart-field-mapping" id="id-1.-smart-field-mapping"></a>

* ✔ Allows precise manual field mapping for accuracy
* ❌ CSV imports require manual rework after upload

#### 2. Selective Migration <a href="#id-2.-selective-migration" id="id-2.-selective-migration"></a>

* ✔ JQL filtering, item ID targeting, and date-based migrations
* ❌ CSV imports require entire bulk imports

#### 3. Real-Time Monitoring <a href="#id-3.-real-time-monitoring" id="id-3.-real-time-monitoring"></a>

* ✔ Live sync logs, error reports, and migration tracking
* ❌ CSV imports offer no live visibility

#### 4. Seamless Transition <a href="#id-4.-seamless-transition" id="id-4.-seamless-transition"></a>

* ✔ Integrated post-migration syncing
* ❌ CSV requires additional manual alignment

### Need Help? <a href="#need-help" id="need-help"></a>

If you need further assistance with your Jira to Asana migration, please open a ticket at our [Help Center.](https://getint.io/help-center)

Considering migration? [**Schedule a Demo**](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team) with our **experts** to explore how **Getint** can optimize your **Jira to Asana** migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
