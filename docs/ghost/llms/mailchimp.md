# Source: https://docs.ghost.org/migration/mailchimp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating from Mailchimp

> Migrate from Mailchimp and import your content to Ghost with this guide

You can easily migrate your subscribers from Mailchimp to Ghost in just a few clicks, using the Mailchimp migrator in Ghost Admin.

<Warning>
  ✏️ It's not currently possible to migrate your Mailchimp content.
</Warning>

## **Run the migration**

The Mailchimp migrator allows you to quickly import members from your Mailchimp to your Ghost publication. You can access the migrator tool from the **Settings → Advanced →** **Import/Export** area of Ghost Admin.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/migrate-tools-apr-2025.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=ea5e2e43c61b34a3df46aff7e2284e75" alt="migrate-tools-apr-2025.png" width="1000" height="441" data-path="images/migrate-tools-apr-2025.png" />

It's helpful to log in to your Mailchimp account before running the migration in Ghost Admin.

### **1. Export subscribers**

Next, it's time to import your Mailchimp subscribers. Click **Open Mailchimp Audience**, and click **Export Audience**.

Once downloaded, select **Click or drag file here to upload** and navigate to the text download, and click **Continue**.

<img src="https://mintcdn.com/ghost/KePyCzI5-bxtjueF/images/audience-1.png?fit=max&auto=format&n=KePyCzI5-bxtjueF&q=85&s=68a11dc353cbf32c14e2b929314be256" alt="audience-1.png" width="1582" height="2092" data-path="images/audience-1.png" />

### **2. Review**

Ghost will confirm the number of subscribers that will be imported to your publication. If satisfied, click **Import subscribers** to begin the import of your data.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/overview-2.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=016fdc8eb63e21031a09bc080c82fe7a" alt="overview-2.png" width="1582" height="1134" data-path="images/overview-2.png" />

After a few moments, you'll see a confirmation message, confirming that your data was successfully migrated to your Ghost site.

## **Large and Complex migrations**

If your migration needs go beyond what our in-built migration tools can support you can still move to Ghost.

If you're a **Ghost(Pro) customer**, our Migrations team can support you in migrating your content and subscribers. Learn more and get in touch with the team [here](https://ghost.org/concierge/).

Alternatively, if you are a developer, comfortable with using the command line, or running a self-hosted Ghost instance, we have a suite of[ open-source migration tools ](https://github.com/TryGhost/migrate)to help with large, complex and custom migrations.


Built with [Mintlify](https://mintlify.com).