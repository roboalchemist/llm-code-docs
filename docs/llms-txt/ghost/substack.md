# Source: https://docs.ghost.org/migration/substack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating from Substack

> Migrate from Substack and import your content to Ghost with this guide

<Tip>
  💡 **Migrating paid memberships from Substack?** You will need to set up Stripe first — [**find out more**](https://ghost.org/help/stripe/). Make sure to use the same Stripe account that is connected to your Substack.
</Tip>

## **Run the migration**

The Substack migrator allows you to quickly import content and members from your Substack to your Ghost publication. You can access the migrator tool from the **Settings → Advanced →** **Import/Export** area of Ghost Admin.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/migrate-tools-apr-2025.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=ea5e2e43c61b34a3df46aff7e2284e75" alt="Migrate Tools Apr 2025 Pn" width="1000" height="441" data-path="images/migrate-tools-apr-2025.png" />

It's helpful to log in to your Substack account before running the migration in Ghost Admin.

### **1. Enter your Substack URL**

To start the migration process, enter the public URL to your Substack, and click **Continue**.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/enter-url.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=2a841004278c2585bd25d438605e4bd7" alt="enter-url.png" width="1582" height="1154" data-path="images/enter-url.png" />

### **2. Export content**

Next, click **Open Substack Settings.** If already logged into Substack, this will take you directly to the location of your Substack account where an export can be generated.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/import-content.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=30b256ab7c14801de1fea6ec7e96c4b3" alt="import-content.png" width="1582" height="2296" data-path="images/import-content.png" />

Click **Create new export**, and then download the zip file that's generated after the export is completed in Substack.

### **3. Upload content**

Once your export has been downloaded, return to the migrator window in Ghost Admin, and select **Click or drag file here to upload**, and navigate to the zip file you downloaded from Substack, once uploaded click **Continue**.

If you're unsure of where the file was saved, check your Downloads folder.

### **4. Export free subscribers**

Next, it's time to import your Substack subscribers. Click **Download free subscribers from Substack**, to trigger a CSV file download of your subscriber list.

Once downloaded, select **Click or drag CSV file here to upload** and navigate to the CSV download, and click **Continue**.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/import-free-subscribers.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=9419cf3991836a6fb9f5570c351cc73c" alt="import-free-subscribers.png" width="1582" height="1770" data-path="images/import-free-subscribers.png" />

### **5. Export paid subscribers**

<Tip>
  💡 **Migrating paid memberships from Substack?** You will need to set up Stripe first — [**find out more**](https://ghost.org/help/stripe/). Make sure to use the same Stripe account that is connected to your Substack.
</Tip>

Next, it's time to import your Substack subscribers, if you have them. Click **Download paid subscribers from Substack**, to trigger a CSV file download of your subscriber list.

Once downloaded, select **Click or drag CSV file here to upload** and navigate to the CSV download, and click **Continue**.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/import-paid-subscribers.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=c0601ec4d554da6e91660da58b60129c" alt="import-paid-subscribers.png" width="1582" height="1770" data-path="images/import-paid-subscribers.png" />

### **6. Review**

Ghost will confirm the number of posts and members that will be imported to your publication. If satisfied, click **Import content and subscribers** to begin the import of your data.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/summary.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=f5b5b427309a614760af7075b8965f79" alt="summary.png" width="1582" height="1430" data-path="images/summary.png" />

After a few moments, you'll see a confirmation message, confirming that your data was successfully migrated to your Ghost site.

### **Substack fees**

Ghost does not take a cut of your revenue. Substack will continue to take **10% fees** on your existing paid subscriptions. If you would like help getting payment fees removed, contact [concierge@ghost.org](mailto:concierge@ghost.org).

### **Statement descriptor**

The statement descriptor is what's shown on bank statements, and depending on how the account was set up, might include 'Substack' in the name. We recommend updating this in your [Stripe public details settings](https://dashboard.stripe.com/settings/update/public/support-details).

### **Using custom domains**

If you’re using a custom domain on Substack, you’ll need to implement redirects in Ghost to prevent broken links.

Substack uses `/p/` as part of the public post URL, where as Ghost uses it in the URL for post previews. This means the redirect regular expression is quite complex, but necessary so that post previews in Ghost function correctly.

```yaml  theme={"dark"}
# redirects.yaml
301:
    \/p\/(?![0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})(.*): /$1

302:
```

This means that if a visitor or crawler goes to `https://mysite.com/p/awesome-post`, they will automatically be redirected to `https://mysite.com/awesome-post`.

For more information on Substack redirects, visit our guide [here](https://ghost.org/tutorials/implementing-redirects/#substack).

## Large and Complex migrations

If your migration needs go beyond what our in-built migration tools can support you can still move to Ghost.

If you're a **Ghost(Pro) customer**, our Migrations team can support you in migrating your content and subscribers. Learn more and get in touch with the team [here](https://ghost.org/concierge/).

Alternatively, if you are a developer, comfortable with using the command line, or running a self-hosted Ghost instance, we have a suite of[ open-source migration tools ](https://github.com/TryGhost/migrate)to help with large, complex and custom migrations.


Built with [Mintlify](https://mintlify.com).