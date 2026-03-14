# Source: https://docs.getint.io/getintio-platform/workflows/storing-reference-ids-urls-across-integrations.md

# Storing Reference IDs/URLs Across Integrations

When integrating tools with Getint, users can capture counterpart IDs/URLs in source and destination tasks. This is particularly valuable when tasks synchronized between platforms have different identifiers. Storing these references improves cross-platform collaboration, allowing teams to communicate effectively and manage tasks more efficiently.

This method can be applied across **any supported integration**. If you encounter difficulties mapping custom fields in your preferred software, don't hesitate to contact us at our [Support Portal](https://getint.io/help-center).

### **Creating Custom Fields** <a href="#creating-custom-fields" id="creating-custom-fields"></a>

#### **Step 1: Create Custom Fields**

Ensure you create the required custom fields in both workspaces:

1. Open a task and scroll down the right-hand panel.
2. Click **Configure** to create a new custom field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeFYdR6CDg77orhsoiUMi%2FCreating%20a%20custom%20field%20from%20the%20Configure%20button.png?alt=media&#x26;token=6deaa6b4-318c-4aea-86b3-a00cda7e27e2" alt=""><figcaption></figcaption></figure>

1. Add:

* **Text Field** for IDs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLFJj6nohftg9d4gvMnxr%2FText%20field%20for%20IDs.png?alt=media&#x26;token=b005eb4a-fcc8-4d4f-ae65-ba62e016101d" alt=""><figcaption></figcaption></figure>

* **URL Field** for links (or use a Text Field if URL fields aren’t supported).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fzn2jHn0e3ivvesi4pCRI%2FUse%20URL%20field%20for%20links.png?alt=media&#x26;token=5053b14b-20af-4074-aac1-12301392dfb5" alt=""><figcaption></figcaption></figure>

1. Add the fields to your layout, name them appropriately, and save the changes.

{% hint style="warning" %}
The process for creating custom fields varies between software platforms. Check our [documentation](https://docs.getint.io/guides/integration-synchronization/how-to-create-a-custom-field-in-all-supported-software) for guidance
{% endhint %}

#### **Step 2: Map Custom Fields**

In Getint, map the custom fields between the two platforms. Here’s an example for Jira (left) and Jira (right):

1. Use the drop-down menus to map the following fields:
   * **ID (On Jira Left) ↔︎ Jira Reference ID**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgRQMEWmhSydCCiI5cOhT%2FMapping%20custom%20fields%20from%20Jira%20to%20Reference%20ID.png?alt=media&#x26;token=78e73047-471a-4cde-9946-f8a67404d18e" alt=""><figcaption></figcaption></figure>

* **URL (On Jira Left) ↔︎ Jira Reference URL**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FwvOfb5v0nr6VHGntXPaV%2FJira%20Reference%20URL.png?alt=media&#x26;token=7be43129-54a1-40b2-b5ab-195970c33f76" alt=""><figcaption></figcaption></figure>

* **Reference ID (custom field) ↔︎ ID (On Jira Right)**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTIEnbXLIUaYAceRrc5pC%2FID%20field%20mapping.png?alt=media&#x26;token=cee0b7ea-938e-4e12-aab6-34dce083dcce" alt=""><figcaption></figcaption></figure>

* **Reference URL (custom field) ↔︎ URL (On Jira Right)**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAztejVPlnObJlKJMrrmg%2FReference%20URL%20right%20side.png?alt=media&#x26;token=8176a176-bd0e-414e-8716-386bc0bc19a8" alt=""><figcaption></figcaption></figure>

1. The fields are one-directional as the data from fields like ID and URL are read-only and cannot be modified:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvmBQGytKfbyhThUP0hzb%2FSync%20direction%20for%20storing%20URL%20and%20ID.png?alt=media&#x26;token=a0890a04-4a27-4133-a9d4-f07f710934a3" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Ensure the fields are mapped correctly to avoid errors or missing data.
{% endhint %}

{% hint style="warning" %}
**Important Warning for ServiceNow Users**\
When integrating **ServiceNow (SNOW)**, if you want the **Ticket Number** to be referenced, you should use **Number** instead of **ID.**

* **Number** → Brings the actual ticket reference (e.g., **INC0001234**).
* **ID** → Brings the system-generated unique identifier (a much larger numeric value).\
  Selecting the wrong field may result in incorrect references being stored.
  {% endhint %}

#### **Step 3: Test the Integration**

After setting up the integration:

1. Run a migration or sync to transfer data between platforms.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvARA4sUAoEl0MND8ol9A%2FRun%20a%20migration%20to%20test%20the%20integration.png?alt=media&#x26;token=6d3b1cf7-1d06-4d49-b481-4694fff380cf" alt=""><figcaption></figcaption></figure>

1. Verify that mapped fields are populated with the correct data:
   * Jira Right fields should contain the IDs and URLs of the corresponding Jira Left tasks.
   * Jira Left fields should contain the IDs and URLs of the corresponding Jira Right tasks.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fra4haLZkDoq0Db1YGUGX%2FChecking%20reference%20ID%20and%20URL.png?alt=media&#x26;token=57368871-53c4-4e08-bf06-cd263ca22ff6" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note that already synchronized issues will not be updated with URLs and Reference IDs unless migration is performed.
{% endhint %}

### **Why Use Reference IDs/URLs?** <a href="#why-use-reference-ids-urls" id="why-use-reference-ids-urls"></a>

Storing reference IDs/URLs is especially helpful for:

* **Filtering and Database Management**: Simplifies handling large volumes of tasks/issues/tickets.
* **Effective Collaboration**: Teams across platforms can reference tasks accurately and resolve issues efficiently.

### **Important!** <a href="#important" id="important"></a>

This setup applies to most integrations supported by Getint. For tools needing custom field mapping that require further development, please reach out through the [Support Portal](https://getint.io/help-center). Our team is here to assist with your integration needs.

Let us know if further adjustments are needed!

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
