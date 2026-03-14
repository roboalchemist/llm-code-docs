# Source: https://docs.getint.io/guides/migration/jira-to-zendesk-migration-guide.md

# Jira to Zendesk Migration Guide

Migrating data from Jira to Zendesk is more than a technical transition — it’s a strategic move to unify engineering workflows with customer support operations. Whether you’re shifting responsibilities across teams, retiring legacy tools, or preparing for a broader digital transformation, Getint provides a structured, reliable solution to bring your Jira issues into Zendesk with clarity and control.

This migration is not just about transferring tasks or tickets. It’s about preserving the integrity of your historical data, aligning workflows across departments, and ensuring that no context is lost when engineering hands off to support. With Getint’s Migration Feature, you can move key issue types, comments, attachments, and custom fields into Zendesk in a single, organized process, tailored to fit the nuances of both platforms.

In this guide, we’ll show you how to configure and execute a successful Jira to Zendesk migration using Getint.

### Requirements for Migrating Historical Data

#### 1. Migration License

Migrating historical data requires a **migration license**, as a standard integration license will not suffice. Migration licenses are billed separately from integration licenses.

To acquire a **migration license**, please visit our [**Pricing Page**](https://www.getint.io/pricing) and click on the **Migration** tab for more details. Contact our team through our [**help page**](https://getint.io/help-center) to proceed with your purchase.

Before purchasing a license, you can test the migration with a **trial version**, which allows:

* **Up to 20 migration runs**
* **A maximum of 5 items per run**

To access the trial version, follow the steps here: [Starting the Free Trial and Access the Getint App](https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app).

Also, see our full migration guide: [Master Jira Migration with Getint - Your Ultimate Guide](https://docs.getint.io/guides/migration).

### Preparing Your Environment Before Migration

#### Handling Fields That Cannot Be Mapped

Before starting the migration, ensure that all required custom fields are created and available on both Jira and Zendesk. If a corresponding field is missing, it must be created in advance to allow proper field mapping.

For help creating custom fields, refer to our guide: [How to Create Custom Fields](https://docs.getint.io/guides/integration-synchronization/how-to-create-a-custom-field-in-all-supported-software#hardbreak-zendesk).

#### Migrating Values from Fields Without 1:1 Mapping

If a Jira field does not have a direct counterpart in Zendesk (e.g., priority, component, or assignees), you can still migrate the information using the **Use label from the other side** setting.

Steps:

1. Create a custom Text field in Zendesk.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fp0zIVxc9MdIdefBrt00u%2Fimage-20250502-133923.png?alt=media&#x26;token=eb1d2330-b7c5-4106-a256-df161a0b2f17" alt=""><figcaption></figcaption></figure>

1. In the field mapping screen, select the Jira field to be migrated and map it to the new custom field in Zendesk.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQ9Avit0bV25puW176trZ%2Fimage-20250502-134036%20(1).png?alt=media&#x26;token=a944f550-53f4-4b8e-8be9-bf7915af9016" alt=""><figcaption></figcaption></figure>

1. Enable **Use label from the other side**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLDcE9woRidZcTiyZb5F4%2Fimage-20250502-134132.png?alt=media&#x26;token=f62cb592-a3d3-4c24-bb44-0128f56b4370" alt=""><figcaption></figcaption></figure>

This approach will insert the label/value of the original field into the destination field. Especially helpful for migrating the Assignees. You probably don’t want to recreate the accounts of people no longer in the company in Jira. This way, no mapping is required; we will inject the value into a text field

You can also migrate values from **multiple source fields into one** text field. You can read more about how to set up this option [here](https://docs.getint.io/guides/integration-synchronization/how-to-map-fields#concatenating-fields).

For more tips, refer to [Master Jira Migration with Getint - Your Ultimate Guide](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint).

### How to Set Up Your Jira to Zendesk Migration <a href="#how-to-set-up-your-jira-to-zendesk-migration" id="how-to-set-up-your-jira-to-zendesk-migration"></a>

#### 1. Set Up a Jira to Zendesk Integration <a href="#id-1.-set-up-a-jira-to-zendesk-integration" id="id-1.-set-up-a-jira-to-zendesk-integration"></a>

Before migrating, you must set up a working integration between Jira and Zendesk. Follow our full [Jira-Zendesk Integration Guide](https://docs.getint.io/guides/integration-synchronization/jira-zendesk-integration) to configure your connection properly.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ftgv6fsfiO8NQ9kvDiykI%2Fimage-20250502-134232.png?alt=media&#x26;token=2e16a9f9-f1f4-4ab0-9a51-6bd2e3e16b2b" alt=""><figcaption></figcaption></figure>

#### 2. Access the Migration Feature <a href="#id-2.-access-the-migration-feature" id="id-2.-access-the-migration-feature"></a>

Once your integration is set:

* Click **Migrate Data** from the left-side menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWhoBdmIoHdmE4PKuOBlA%2Fimage-20250502-135120.png?alt=media&#x26;token=c05d4a13-cda5-4224-b6ff-a8c6b580b28b" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you're on a trial version, a warning will appear regarding your migration limits (5 items per run, 20 runs).
{% endhint %}

* Check the **Enable Migration on the Next Run** box to proceed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqlTetkuCHEQLsKGv61uw%2Fimage-20250318-181244.png?alt=media&#x26;token=10f987a0-f1bd-459c-90fe-ac718c90d0cb" alt=""><figcaption></figcaption></figure>

#### 3. Configure Migration Settings <a href="#id-3.-configure-migration-settings" id="id-3.-configure-migration-settings"></a>

* **Migration Direction:** Define whether data flows from Jira to Zendesk.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FamscsZjDmIhgSQaZFWjZ%2Fimage-20250505-111349.png?alt=media&#x26;token=016509b7-afd2-46f5-b6ad-a1450dc2037c" alt=""><figcaption></figcaption></figure>

* **Handling Previously Migrated Items:** Choose how to handle items that were already migrated:
  * **Replace** (overwrite existing items).
  * **Update** (sync only new changes).
  * **Skip** (ignore already migrated items).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F02p49woQeiMBvJLwpNuc%2Fimage-20250505-113550.png?alt=media&#x26;token=95cce8ee-7cb2-4b87-bab6-dd7bdd79a8ff" alt=""><figcaption></figcaption></figure>

* **Selective Resync (Optional)**: If a previous migration was incomplete, choose specific fields to **resync**, such as **Assignee, Status, and Description**.
  * To resync **all fields**, enter ***ALL**.*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7nqOoxdlzYXtUCHQXjv1%2Fimage-20250505-113648.png?alt=media&#x26;token=27aa3dc2-7092-4fbb-b6d5-e8f9d31d732f" alt=""><figcaption></figcaption></figure>

* **Selective Item Migration (Optional)**:
  * Enter specific **item IDs** to migrate **only selected tasks**.
  * Use **JQL filtering** for refined selection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2zd2rzFu7HnMqkk2ByxL%2Fimage-20250505-113827.png?alt=media&#x26;token=a37604c8-9fe6-44e0-8173-2a45cd0ce921" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Important:** Ensure that your **JQL filter or item IDs align with the creation/updating date range** to avoid missing items during migration.
{% endhint %}

* **Time Range Filtering:**
  * Select a **creation date range** in the **UTC timezone**.
  * Only issues created or updated **within the selected period** will be migrated.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnEWAuRWwNsTk49dEFugx%2Fimage-20250505-114120.png?alt=media&#x26;token=4acd84a4-cfb2-40a4-b4b4-76a9f2ad3281" alt=""><figcaption></figcaption></figure>

#### 4. Schedule and Execute Migration <a href="#id-4.-schedule-and-execute-migration" id="id-4.-schedule-and-execute-migration"></a>

* Click **Schedule Migration** to queue the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FE7hqT2fr3z8YP7Yn5Gns%2Fimage-20250505-114258.png?alt=media&#x26;token=ad057450-2047-4233-87e0-160a0f24411c" alt=""><figcaption></figcaption></figure>

* The system will begin migration during the next synchronization run.
* Monitor progress in the **Reporting section** or the **Latest Runs tab**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCmvnOe3EYut2LXNcPI5M%2Fimage-20250505-114340.png?alt=media&#x26;token=2eac317f-61ad-432e-83ca-44a7052f67e3" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Migration runs appear under the **Mode** column as **MIGRATION** instead of **SYNC**.
{% endhint %}

#### 5. Enable Continuous Sync After Migration (Optional) <a href="#id-5.-enable-continuous-sync-after-migration-optional" id="id-5.-enable-continuous-sync-after-migration-optional"></a>

If you want to keep the items in sync after migration:

* Open the **Integration Settings**.
* Click **More > Enable Continuous Sync**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrwyEktuGzVbdch4sLGdw%2Fimage-20250505-114506.png?alt=media&#x26;token=62548ead-d241-4574-b38d-200a79481368" alt=""><figcaption></figcaption></figure>

Alternatively, you can uncheck the disable box when setting up the migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fe3umtZcZy0u2k7GJ35Se%2Fimage-20250505-114537.png?alt=media&#x26;token=abc83bdf-600b-427f-acd3-30f34bb594a9" alt=""><figcaption></figcaption></figure>

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

If you need further assistance with your Jira to Zendesk migration, please open a ticket at our [Help Center.](https://getint.io/help-center)

Considering migration? [**Schedule a Demo**](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team) with our **experts** to explore how **Getint** can optimize your **Jira to Zendesk** migration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
