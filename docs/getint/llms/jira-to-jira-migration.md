# Source: https://docs.getint.io/guides/migration/jira-to-jira-migration.md

# Jira to Jira migration

Migrating Epics, tasks, and issues from Jira to Jira can be a significant move for a team or organization.

Getint specializes in handling complex data migrations, ensuring that all relevant data/fields—including Epics, tasks, and issue item types—are accurately transferred from Jira to Jira. We address the data and the relationships and hierarchies between different elements.

Our emphasis on data accuracy and integrity is often a standout feature, ensuring that no important information is lost or corrupted during the migration process.

Discover our comprehensive guide to mastering Jira migrations with Getint. To learn more about how our tool works and how you can maximize its potential, visit [Mastering Jira Migration: A Comprehensive Guide with Getint.](https://www.getint.io/blog/mastering-jira-migration-a-comprehensive-guide-with-getint)

{% hint style="info" %}
This guide is intended to support users of Jira Software, Jira Service Management, and Jira Data Center.
{% endhint %}

### **Requirements for migrating historical data** <a href="#requirements-for-migrating-historical-data" id="requirements-for-migrating-historical-data"></a>

For migrating historical items, you must have a migration license with us as an integration license won’t suffice in this case.

The migration licenses offer different features depending on the scale of your migration. To learn more about and purchase our migration license, please visit our pricing page <https://www.getint.io/pricing> and select the "Migration" tab for more details.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuZOZBdZuG8mWtxKiqMUT%2FPrices%20for%20data%20migration.png?alt=media&#x26;token=a4cb8326-84aa-4aa0-9b63-0b38e92ae91a" alt=""><figcaption><p>If you have further questions regarding the migration license details, or if you are ready to proceed with your purchase, you can quickly reach out to us via our chat icon, located in the lower right corner of the page.</p></figcaption></figure>

{% hint style="info" %}
Before buying a license, you can use our trial application to preview the migration process. The trial allows up to 20 migration runs, each with a maximum of 5 historical items. After reaching the 20 migration runs threshold, further migrations require a license.

To access our app and install the trial version, please go to
{% endhint %}

### **How to set up your migration** <a href="#how-to-set-up-your-migration" id="how-to-set-up-your-migration"></a>

**1.** For setup integration between Jira and Jira, you can check the steps to build this integration here:[<img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Ficon%2FPRq8D5IBseUvQPEVFVwD%2FGitbook%20getint%20sygnet%20logo.png?alt=media&#x26;token=3353768c-d008-46f7-bc2d-fd71b5d48f14" alt="" data-size="line">Jira Jira integration | Getint: Where every ticket finds it's place.](https://docs.getint.io/guides/integration-synchronization/jira-jira-integration)

{% hint style="warning" %}
When you set up the integration, new items created in either of the Jira instances will sync across both platforms. To avoid issues with live environments, you can disable the integration right after setup, schedule migration with the integration off, or pause work in both systems during the migration.
{% endhint %}

**2.** With your integration set, click on the "Migrate Data" button, located in the left side menu:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAWIsciXqseUz4SgaZzID%2FGo%20to%20Migrate%20data%20in%20the%20integration%20editor.png?alt=media&#x26;token=165d0d23-f3c3-484c-9c9c-205ac0ea2235" alt=""><figcaption></figcaption></figure>

If you are using the app's trial version or have a limited integration license, you'll see a warning indicating that you have a restricted number of Migration Runs available. Each Migration Run is capped at migrating a maximum of 5 items. If you’d like to learn more about the different licensing models and pricing, please visit [<img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Ficon%2FPRq8D5IBseUvQPEVFVwD%2FGitbook%20getint%20sygnet%20logo.png?alt=media&#x26;token=3353768c-d008-46f7-bc2d-fd71b5d48f14" alt="" data-size="line">Licensing and payments | Getint: Where every ticket finds it's place.](https://docs.getint.io/billing-and-services/licensing)

Check the "Enable Migration on Next run" box to continue.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJ9pkwDckr3EpVU66iQRr%2FEnable%20migration%20on%20the%20next%20run.png?alt=media&#x26;token=01cd14ec-71cb-4ee1-8b74-64e089b465c2" alt=""><figcaption></figcaption></figure>

**3**. On this screen, you can customize your migration by choosing the direction (Right to Left or Left to Right), determining the handling of previously migrated items (replace, update, or skip), and specifying any fields you want to resync to capture updated data post-migration.

Configure your migration preferences, then either enter the specific item IDs you wish to migrate or leave the field blank to instead add a date range at the bottom to include items created within that period. The tool will migrate all items that fall within the specified date range, so please make sure that in case you want to migrate specific items by their IDs, to fill a date range that covers the date of creation of these items.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FW0SU7nx22oC2mifIUkcq%2FMigration%20configuration.png?alt=media&#x26;token=e6554eff-2f88-4f26-9959-6187ce82893e" alt=""><figcaption></figcaption></figure>

**4**. With the migration set per your preference, click "Schedule Migration" at the bottom. The tool should migrate the items based on the specifications on the next synchronization run.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6KWTTSBUafSGoNeC1Mbo%2FJira%20Jira%20Scheduling%20migration.png?alt=media&#x26;token=216fc84c-9ded-404d-9759-c5be9d8d0ef2" alt=""><figcaption></figcaption></figure>

**5.** After scheduling a migration, you can observe the results of your migration through the reporting section or the "latest runs" from the left menu.

Your items should have been successfully migrated, you can check the receiving end to verify the integrity of the migrated data (note that migration runs are displayed as "MIGRATION," under the "Mode" column)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMe4NNw7FiRBAGVZG86j8%2FChecking%20migration%20on%20latest%20runs.png?alt=media&#x26;token=20469597-2e83-4ed9-a57d-31b63047e28f" alt=""><figcaption></figcaption></figure>

### **Jira Service Management - Jira Software migration**

When it comes to Jira Jira migrations, the most common scenario is syncing Jira Software with Jira Service Management or vice-versa. With Getint, this is achievable by simply connecting the corresponding projects to both Jira instances. For more information on how to connect Jira instances, please refer to this [guide](https://docs.getint.io/guides/quickstart/connection#jira).

Below you can see an example of how tasks will be migrated from one side to the other.

#### **Project 1 - Jira Software**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRmFNW5ixytLkmNqxy8Zd%2FJira%20Software%20Tasks.png?alt=media&#x26;token=6de72060-9dd2-47c8-b986-7ea3bdef787f" alt=""><figcaption><p>Existing tasks in a Jira Software project</p></figcaption></figure>

#### **Project 2 - Jira Service Management**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZz2wrlsbNCSXjDMFH8Fs%2FMigratin%20tasks%20from%20Jira%20Software%20to%20Jira%20Service%20Management.png?alt=media&#x26;token=3205877a-c5e3-4511-82c5-39b07bb91bf1" alt=""><figcaption><p>Note how tasks were recreated in this Jira Service Management project</p></figcaption></figure>

### **Migrating based on Date Range**

To migrate data based on creation dates, use our calendar to select the relevant dates for your tasks. Getint will then recognize the specified timeframe and fetch only the tasks from that period.

{% embed url="<https://www.loom.com/share/79edd7b69a6b4f5cac5a9ab0a4056cd6?sid=813dcc76-0277-42b0-8175-2c1fc1d97139>" %}

### **Migrating based on item's IDs**

To migrate data based on item IDs, simply copy the relevant IDs to sync only the specified tasks. Getint will then identify these IDs and retrieve the associated tasks.

{% embed url="<https://www.loom.com/share/7c6122a6e5a647f0b0c7528b0b658455?sid=23396daa-f5a6-41e5-ac53-91970830def4>" %}

### **Migrating based on Filters**

To migrate data based on the filters you applied to the integration, use the relevant filters to sync only the specified tasks. Getint will then recognize these filters and retrieve the associated tasks.

{% embed url="<https://www.loom.com/share/448fbda5211844ff8428f232bfe5a897?sid=8fc8d84c-f891-44a3-8b60-932495e47082>" %}

{% hint style="info" %}
If you experience any issues while performing the process above, please raise a ticket through our [support portal.](https://getint.io/help-center)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
