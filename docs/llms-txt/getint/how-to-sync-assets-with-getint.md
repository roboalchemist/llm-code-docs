# Source: https://docs.getint.io/getintio-platform/workflows/how-to-sync-assets-with-getint.md

# How to Sync Assets with Getint

Jira Assets lets you track configuration items, services, and other resources. With Getint, you can keep those Assets up to date across connected systems. This article shows you how to configure Getint to pull and push Jira Assets, map fields, and schedule regular updates.

### What Are Assets? <a href="#what-are-assets" id="what-are-assets"></a>

In Jira, an Asset is an object composed of fields and values in a key-value format, similar to a JSON structure. If your organization assigns devices to employees (such as phones or laptops), these devices are usually tracked in tickets that include one or more Asset fields.

These objects live inside custom fields created by users, just like other field types. However, querying them requires a different syntax than standard JQL. Instead, you'll use[AQL (Assets Query Language)](https://support.atlassian.com/assets/docs/use-assets-query-language-aql/).

To search for data within an asset object, you'll need two things:

* The name of the custom field that contains the asset.
* The specific field and value within the object you want to locate.

### Mapping Assets in Getint  <a href="#mapping-assets-in-getint" id="mapping-assets-in-getint"></a>

Mapping assets works like any other field in Getint. To locate specific objects, you'll need to include a query written in AQL (Assets Query Language). Here's how to map two related fields:

1. Identify the custom fields that contain the asset data, and map them. In this example, we will use the **Multi Related Asset** field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSttXBWoOGwEnrNg1Diac%2FMapping%20assets%20in%20Getint..png?alt=media&#x26;token=30a58309-8427-40a3-9b58-fdef411b789f" alt=""><figcaption></figcaption></figure>

1. Assets can store multiple objects/values. Therefore, you will need to select the Assets schema and write an AQL query that targets the relevant object type and attributes.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGUJ5EriyfJEDPEN5SJ5r%2FSelect%20the%20assets%20schema.png?alt=media&#x26;token=fe589efb-815a-4010-bf72-7150e1de0f1b" alt=""><figcaption></figcaption></figure>

1. Asset queries should now be visible. You can edit the selected schemas at any time from the same menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtQAxbKJ4P19HgqYCTNOT%2FResults%20after%20accepting%20both%20queries.png?alt=media&#x26;token=d1fc446f-afe7-4c86-9322-dc15b0714827" alt=""><figcaption></figcaption></figure>

1. Test the query to confirm it returns the expected results, and match the options based on shared values or reference.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNthYuFGY0ocZtN9CZfEC%2FMap%20available%20options.png?alt=media&#x26;token=39ea8d5e-829b-46fe-9097-b55fc5e81fad" alt=""><figcaption></figcaption></figure>

### Mapping Assets to Other Fields <a href="#mapping-assets-to-other-fields" id="mapping-assets-to-other-fields"></a>

Assets can be mapped to various fields, including text, picklist, and multi-select fields.

* To map another field to your assets, add a field mapping and select the field to sync. For example, using a custom cascading field requires matching options in the mapping configuration, as shown below.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSL2vxN9DntHtIvss25rx%2FMapping%20Assets%20to%20a%20Cascading%20Field.png?alt=media&#x26;token=8809d3a6-190d-4ef4-a91c-1296fec67d07" alt=""><figcaption></figcaption></figure>

* To map assets to text fields, repeat the process and select the corresponding text field to sync. Unlike the picklist, no dropdown options are needed. Instead, set the text field to **use label from other side**, so it receives values from assets during sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIL46JRjYgokIJkMmhLik%2FMapping%20assets%20to%20custom%20text%20fields.png?alt=media&#x26;token=75950908-ed62-439b-aeaf-e55d5260e813" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Mapping assets to text fields works unidirectionally—from assets to the custom field only. Changes to the custom field will not sync back to assets.
{% endhint %}

### How to Query Assets? <a href="#how-to-query-assets" id="how-to-query-assets"></a>

For example, let’s say we have a project where we only want to sync work items that include a custom field called **Multi Related Asset**. This field contains an Asset object, and we’re looking for items where the **Name** inside that object field is set to *MacBook Pro 15''*.

In the project's JQL selection box, we would enter:

`project = "Jira Jesus" AND "Multi Related Asset" in aqlFunction("Name = \"MacBook Pro 15\\\"\"")`

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzXPwXYsYC7hTIK2NOP6e%2FQuerying%20assets.png?alt=media&#x26;token=c269b746-7a88-45f2-b9e2-9dbae6b4c614" alt=""><figcaption></figcaption></figure>

Once you've confirmed that the JQL returns the correct work items in your project, you can paste the query into the appropriate field in Getint, as shown below.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrPdNDzUkLefVHwmQJLK7%2FEntering%20the%20custom%20JQL%20in%20the%20project%20box.png?alt=media&#x26;token=0ad14452-c1da-49fe-9711-fe16bd80773c" alt=""><figcaption></figcaption></figure>

### Important Notes: <a href="#important-notes" id="important-notes"></a>

* Asset objects often include multiple fields, and each one can be queried on its own. If you need to check more than one field, create separate AQL clauses and combine them using `AND` or `OR`, depending on the logic you want to apply.

`project = "Jira Jesus" AND "Multi Related Asset" in aqlFunction("Name = "MacBook Pro 15\""") OR "Related Asset" in aqlFunction("Name = "Lenovo Thinkpad\"")`

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOgnm3ZwiUdfmzVpufq6r%2FAdding%20more%20clauses%20to%20the%20query.png?alt=media&#x26;token=ad89d451-bf51-42e6-95b4-736f15e69bb0" alt=""><figcaption></figcaption></figure>

* Before syncing or migrating, make sure your JQL query returns only the work items you want to move. Double-check that nothing extra is included and nothing important is left out. Once you're confident the results are accurate, paste the query into the JQL selector in your Getint connector. This ensures that only the intended items are included in the sync or migration.

### Conclusion <a href="#conclusion" id="conclusion"></a>

Syncing Jira Assets with Getint comes down to understanding how Assets are structured, writing precise AQL queries, and mapping fields correctly. Once your queries are tested and your connector is configured, Getint will handle the syncing based on your setup. This gives you a reliable way to keep asset data aligned across systems without surprises or unnecessary transfers.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FU3RRRGTfyYJytqi3bHSj%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=79c09491-90bb-4310-bd4a-ead5bc263af4" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
