# Source: https://docs.getint.io/guides/integration-synchronization/jira-salesforce-integration.md

# Jira Salesforce integration

Integrating Salesforce with Jira using Getint improves team collaboration. Real-time data sync allows the management of customer requests, tasks, bugs, and projects without manual input. This integration supports Salesforce Lightning, Classic, and various Jira deployments, including Cloud, Data Center, and Service Management.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2qEXNxGFHbXeqES3p4dE%2FSalesforce%20Integration%20for%20Jira.png?alt=media&#x26;token=794f5956-471a-46f2-9fba-aa37fd7ea671" alt=""><figcaption><p>Check out our Salesforce integration app on the Atlassian Marketplace</p></figcaption></figure>

### **Salesforce-Jira Licensing Model** <a href="#salesforce-jira-licensing-model" id="salesforce-jira-licensing-model"></a>

The **Salesforce-Jira licensing model** with Getint is designed to accommodate different integration needs. Here’s an overview:

#### **Standard Licensing** <a href="#standard-licensing" id="standard-licensing"></a>

* A Getint license is only required on Jira, allowing seamless data synchronization between Salesforce and Jira.
* This makes setup simpler and faster, without the need for additional configurations in Salesforce.

#### **Flexible License** <a href="#flexible-license" id="flexible-license"></a>

* For managed services companies or organizations looking to integrate four or more instances (regardless of whether they are the same or different tools), Getint offers a **Flexible License.** This custom license covers a specific number of connections (i.e., up to 10 instances) without restrictions on the tools involved. You can also swap the integrated tools while the license remains active, offering unparalleled flexibility.

For more details on licensing, visit our [**Pricing Page**](https://docs.getint.io/billing-and-services/licensing)**.**

### **Requirements to Build Your Integration** <a href="#requirements-to-build-your-integration" id="requirements-to-build-your-integration"></a>

* The **Getint app** must be installed in Jira.

#### **Salesforce API Requirements** <a href="#salesforce-api-requirements" id="salesforce-api-requirements"></a>

Salesforce requires API access for integration. API access is enabled by default in the following editions:

* Enterprise Edition
* Unlimited Edition
* Performance Edition
* Developer Edition

API access is **NOT enabled** by default in:

* Group Edition
* Essentials Edition
* Professional Edition

{% hint style="info" %}
If using a Salesforce edition without API access enabled, please contact Salesforce support or refer to the Salesforce Help & Training Community.
{% endhint %}

#### **Authentication and Access Requirements** <a href="#authentication-and-access-requirements" id="authentication-and-access-requirements"></a>

* OAuth authentication is required to establish a secure connection between Salesforce and Jira.
* Comments are attributed to the user who created the connection. Therefore, we recommend using dedicated Service Accounts for both instances.
* Jira instances must have a dedicated user and an associated API token with permissions to read, write, view, and modify the project.
* **Personal Access Tokens** are required for Jira authentication. Learn more here: [Connection Guide](https://docs.getint.io/guides/quickstart/connection#salesforce).

### **Setting Up Your Salesforce-Jira Integration** <a href="#setting-up-your-salesforce-jira-integration" id="setting-up-your-salesforce-jira-integration"></a>

#### **1. Access the** [**Getint**](https://marketplace.atlassian.com/apps/1223930/issue-sync-integration-for-jira-getint-issue-sync?hosting=cloud\&tab=overview) **App in Jira:**

* Navigate to Jira, go to Apps, and select the Getint app (Salesforce integration for Jira in this case).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FyK2OhTeupywShD8810yD%2FSelecting%20the%20Jira%20Salesforce%20app.png?alt=media&#x26;token=73aefd46-0f0e-486e-b9f0-21d2b92a37bb" alt=""><figcaption></figcaption></figure>

#### **2. Create Integration**

Click **Create Integration** and select either:

* **Continuous Sync** for ongoing synchronization.
* **Migration** for a one-time data transfer.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEFVi5oJIlDxyWWYIprla%2FSelecting%20Continuos%20Sync%20or%20Migration.png?alt=media&#x26;token=45b25f45-0a77-40f7-aa82-dba35b27ca82" alt=""><figcaption></figcaption></figure>

#### **3. Generate a Jira API Token**

* Log in to your Atlassian account and navigate to **Account Settings > Security**.
* Generate an API token.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhfzIIgY8fiL0vtQiPEZ1%2FCreating%20an%20API%20token%20for%20Jira%20Salesforce.png?alt=media&#x26;token=c2960bad-ec80-4ab7-b768-f8af8abb58e9" alt=""><figcaption></figcaption></figure>

* Copy and securely store the token, as it will be used as the password for Jira Cloud.

For detailed steps, refer to our guide [Connection](https://docs.getint.io/guides/quickstart/connection#jira).

#### **4. Create a connection to Jira and Salesforce and authorize Getint**

**Jira Connection:**

* Select the **Jira** app. Then enter your Jira instance **URL**, username, and Access token generated.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F49m2fgJzZ7xSnTXFZAPW%2FConnection%20with%20Jira.png?alt=media&#x26;token=cc87470e-980a-4eeb-813e-b9404ed82f92" alt=""><figcaption></figcaption></figure>

* Select the Jira project you want to synchronize and select **Connect**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfyI3T747GlRa9j6riDDo%2Festablishing%20a%20connection%20with%20Jira.png?alt=media&#x26;token=cdd19a39-3c27-435e-b3a5-0223cb84a0fe" alt=""><figcaption></figcaption></figure>

#### **Salesforce Connection:**

* Select **Salesforce** and click **Create a Connection**.
* Enter your Salesforce instance URL in the **URL** field and click **Next**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFZ4r8qYmAVmFyfXWdi4C%2FEstablishing%20a%20connection%20with%20Salesforce.png?alt=media&#x26;token=830a89fa-6026-4060-8c47-855e85e73159" alt=""><figcaption></figcaption></figure>

* Assign a name to the connection and enter the **client\_id** and **client\_secret** credentials.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0yfhjmL41mlSI3JDlqEJ%2FCreating%20a%20connection%20with%20Salesforce.png?alt=media&#x26;token=952855e4-2592-4892-819b-0fe85e914619" alt=""><figcaption></figcaption></figure>

* **Add** the connection and select it.

{% hint style="info" %}
For detailed steps on how to configure your **Salesforce credentials**, please refer to our guide [Connection](https://docs.getint.io/guides/integration-synchronization/jira-salesforce-integration/salesforce-oauth-authentication).
{% endhint %}

#### **6. Configure Type Mapping**

* **Quick Build (Beta):** Use the Quick Build feature to automatically map fields and types between applications, simplifying the process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVu1lj4Q4F4kapIbW3ni6%2FUsing%20quickbuild%20for%20a%20Jira%20Salesforce%20integration.png?alt=media&#x26;token=17c3e67b-cc1a-4b0b-b0fa-0b528dfe0405" alt=""><figcaption></figcaption></figure>

* **Manual Mapping:** For greater control, manually map the types yourself. This approach lets you tailor the mapping to meet your specific needs. Click **+ Add type mapping** to add the types (Case, Task, Bug, Epic, Story) by yourself.
  * **Story ↔ Case**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fq0FgOjEMiUyPYimZE0oY%2FAdding%20a%20manual%20mapping%20Jira%20Salesforce.png?alt=media&#x26;token=94ca3ce7-981b-4f0e-972d-b024413e44d0" alt=""><figcaption></figcaption></figure>

#### **7. Configure Field Mapping**

* Select the fields to synchronize, such as **Title**, **Description**, **Assignees**, and **Custom** fields.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FX0ANoBXjkRTzv4sK5fQR%2Ffield%20mappings%20in%20Salesforce%20integration.png?alt=media&#x26;token=d44a911b-ee24-4fa4-8662-7f522f9af176" alt=""><figcaption></figcaption></figure>

* Ensure synchronization flow is defined for each field, using the arrows and selecting **Apply**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FV5XTfLWJqWB0Pict3skP%2FChoosing%20the%20sync%20direction.png?alt=media&#x26;token=8e30bcdf-fd73-46df-acb6-4ef193245b37" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Some custom field types may not be supported. Please check our [Connectors Salesforce page](https://docs.getint.io/getting-started-with-the-platform/apps-connectors/salesforce) for a list of supported fields. If a field is missing or you need custom development, visit our [Help Center](https://getint.io/help-center).
{% endhint %}

#### **8. Configure Status Mapping**

Ensure you are using the correct fields for each instance's status.

* Navigate to the **Status Mapping** tab.
* Use the dropdown menu to map Salesforce statuses to their Jira equivalents (e.g., **Open ↔ To Do**).
* **Apply** the status mappings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxXZX352z8tmmZtuajaxc%2Ftype%20mapping%20configuration.png?alt=media&#x26;token=9a1e34ee-8ddd-4a29-bb0f-d3889dfb1504" alt=""><figcaption></figcaption></figure>

#### **9. How to Manage Comments & Attachments:**

* Review the **Comments & Attachments** tab. These features are enabled by default but can be adjusted to meet your organization's needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWfddpamcXLWps9wrnxQT%2Fcomments%20%26%20attachments%20jira%20salesforce.png?alt=media&#x26;token=121d799f-8630-4693-93f2-7cde99dcd8ad" alt=""><figcaption></figcaption></figure>

* You can adjust the sync direction for comments and attachments to be bidirectional, **unidirectional to Jira**, or **unidirectional to Salesforce**. Also, you can completely disable comments and attachments if they are unnecessary or restricted in your organization.

{% hint style="warning" %}
Comments and attachments do not automatically sync from Salesforce to Jira. To ensure they appear in Jira, update either the Salesforce ticket or the Jira ticket, depending on whether bidirectional sync is enabled.
{% endhint %}

#### **10. Filtering Option**

Customize synchronization by applying filters:

* After completing your integration, add filters to each app by clicking the filter icon next to its app icon. This will affect the corresponding side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FM5N89dkWN1egx0Ct3OnT%2FUI%20filters%20Jira%20Salesforce.png?alt=media&#x26;token=32d48849-6a50-44d3-8802-03928fed52f3" alt=""><figcaption></figcaption></figure>

* Choose the filter scope:
  * **ALL items filter:** Rules will be verified for every item before synchronization.
  * **NEW items filter:** Rules will be verified only for newly created items that have not yet been synced.
  * **SYNCED items filter:** Rules will be verified for items that were already synced in the past.

Add values for the filters and click **Apply**. For more details on how to use the filter, refer to our [Filtering Guide](https://docs.getint.io/getintio-platform/workflows/items-filtering).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7tJBiZKGYu4x6lEAPlQz%2FFiltering%20options%20Jira%20Salesforce.png?alt=media&#x26;token=2d9bf42a-e42a-4060-b716-ff83b77a411b" alt=""><figcaption></figcaption></figure>

#### **JQL Filtering (For Jira Side Only)**

* In addition to the Item Filtering options mentioned above, Jira apps also support JQL (Jira Query Language) Filtering, allowing you to refine and customize which items are included in the sync.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (i.e., status in (“In Progress”)).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkG3TMZ2rZuszUvtrtdpp%2FJQL%20filtering%20options.png?alt=media&#x26;token=22c7eff4-d46d-4021-88d4-a846acbb32bd" alt=""><figcaption></figcaption></figure>

* Name your integration and click on **Create** to save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMBxugNOPFUg5jQXtOTT7%2FSaving%20the%20integration.png?alt=media&#x26;token=76d19028-f188-43ba-a707-5394cb4d72ec" alt=""><figcaption></figcaption></figure>

#### **11. Test the Integration**

* Create a test case in Salesforce and a test task in Jira.
* Verify synchronization by performing actions like adding comments, attachments, or changing statuses.
* Check logs in Getint to ensure the integration is working as expected.

{% embed url="<https://www.loom.com/share/31c28c0ceade49319dfd3868c628188b?sid=12551b4c-3a64-4957-94fd-5f8b39c8f5f7>" %}

#### **12. Duplicating Your Setup and Selecting Different Projects:**

* Navigate to Workflows.
* Click the three dots on the right and choose Duplicate.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7foFv7QPO0Zgc0AKm4vz%2FDuplicating%20your%20integration.png?alt=media&#x26;token=4973c435-dc92-4d94-b256-9b4837f7f4be" alt=""><figcaption></figcaption></figure>

* A side panel will appear. Enter a new name for the integration, which defaults to "copy" if the same projects are used.
* In the dropdown menu, choose the projects to integrate.
* For each side, click Connect, then Duplicate.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWM4ZCQ02wrIB7yvaGWRW%2FCopying%20the%20Jira%20Salesforce%20integration.png?alt=media&#x26;token=ab554067-a169-4502-9350-90bff27ae515" alt=""><figcaption></figcaption></figure>

* Save the new integration.

### **Conclusion** <a href="#conclusion" id="conclusion"></a>

At Getint, we're dedicated to providing exceptional support throughout your integration journey. Our team is committed to delivering the best customer experience. For any questions about this integration or assistance with the setup process, don't hesitate to open a ticket at our [Help Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team). We're here to help!

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
