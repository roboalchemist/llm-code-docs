# Source: https://docs.ghost.org/migration/medium.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating from Medium

> Migrate from Medium and import your content to Ghost with this guide

You can easily migrate your posts and subscribers from Medium to Ghost in just a few clicks, using the Medium migrator in Ghost Admin.

## **Run the migration**

The Medium migrator allows you to quickly import content and members from your Medium to your Ghost publication. You can access the migrator tool from the **Settings → Advanced →** **Import/Export** area of Ghost Admin.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/migrate-tools-apr-2025.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=ea5e2e43c61b34a3df46aff7e2284e75" alt="migrate-tools-apr-2025.png" width="1000" height="441" data-path="images/migrate-tools-apr-2025.png" />

It's helpful to log in to your Medium account before running the migration in Ghost Admin.

### **1. Enter your Medium URL**

To start the migration process, enter the public URL to your Medium, and click **Continue**.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/url.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=4196f5c27e93dea8bdb6c2bcee4fd9de" alt="url.png" width="1582" height="1154" data-path="images/url.png" />

### **2. Export content**

Next, click **Open Medium Settings**, and click **Download your information**. A link to download the export will be sent to your email.

<img src="https://mintcdn.com/ghost/KePyCzI5-bxtjueF/images/content.png?fit=max&auto=format&n=KePyCzI5-bxtjueF&q=85&s=370afaaa97b89e36db8fd6ef4745913f" alt="content.png" width="1582" height="2408" data-path="images/content.png" />

### **3. Upload content**

Once your export has been downloaded, return to the migrator window in Ghost Admin, and select **Click or drag file here to upload**, and navigate to the zip file you downloaded from Medium, once uploaded click **Continue**.

If you're unsure of where the file was saved, check your Downloads folder.

### **4. Export subscribers**

Next, it's time to import your Medium subscribers. Click **Open Medium Audience stats**, and click **Export this list**.

Once downloaded, select **Click or drag file here to upload** and navigate to the text download, and click **Continue**.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/subscribers.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=4df916dc508445c18a9d7f23e7003762" alt="subscribers.png" width="1582" height="2318" data-path="images/subscribers.png" />

### **5. Review**

Ghost will confirm the number of posts and members that will be imported to your publication. If satisfied, click **Import content and subscribers** to begin the import of your data.

<img src="https://mintcdn.com/ghost/aGR3I5_lq1oxakuc/images/overview.png?fit=max&auto=format&n=aGR3I5_lq1oxakuc&q=85&s=456e95e54c705a7812ef89da292daf50" alt="overview.png" width="1582" height="1364" data-path="images/overview.png" />

After a few moments, you'll see a confirmation message, confirming that your data was successfully migrated to your Ghost site.

### **6. Verification and manual checks**

<Warning>
  ⚠️ The Medium content export includes all of your posts and **all of the comments you've written across Medium**. There is no sure-fire way to differentiate between these content types, so you should check the import to verify your posts are live.
</Warning>

The importer will make a post in Ghost for all posts and comments in your Medium export. The importer will try to sort posts and comments, based on the following rules:

* If a piece has only one paragraph, treat it as a **comment**
* If a piece of any length has an image, treat it as a **post**
* Otherwise, treat the piece as a **post**
* All pieces that are treated as **comments** will be saved as **drafts**
* All **posts** that were **drafts** in Medium, will be **drafts** in Ghost
* All \*\*posts \*\*that were **published** in Medium will be **published** in Ghost

You should check that comments and posts were sorted correctly. Possible comments that have been saved as drafts will be tagged `#Medium Possible Comment`.

### Using custom domains

If you’re using a custom domain on Medium, you’ll need to implement redirects in Ghost to prevent broken links.

Medium appends a small random ID to each post, which is removed in the migration step above. The regular expression below removes that random ID, but does not affect preview links.

```yaml  theme={"dark"}
# redirects.yaml
301:
    ^\/(?!p\/?)(.*)(-[0-9a-f]{10,12}): /$1

302:
```

This means that if a visitor or crawler goes to `https://mysite.com/awesome-post-a1b2c3d4e5f6`, they will automatically be redirected to `https://mysite.com/awesome-post`.

Learn more about Medium redirects [here](https://ghost.org/tutorials/implementing-redirects/#medium).

***

## **Large and Complex migrations**

If your migration needs go beyond what our in-built migration tools can support you can still move to Ghost.

If you're a **Ghost(Pro) customer**, our Migrations team can support you in migrating your content and subscribers. Learn more and get in touch with the team [here](https://ghost.org/concierge/).

Alternatively, if you are a developer, comfortable with using the command line, or running a self-hosted Ghost instance, we have a suite of[ open-source migration tools ](https://github.com/TryGhost/migrate)to help with large, complex and custom migrations.


Built with [Mintlify](https://mintlify.com).