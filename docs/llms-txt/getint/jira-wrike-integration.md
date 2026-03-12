# Source: https://docs.getint.io/guides/integration-synchronization/jira-wrike-integration.md

# Jira Wrike integration

Managing tasks and projects across Jira and Wrike can be challenging without a unified system. Getint simplifies this process by enabling seamless two-way synchronization between the two platforms. This integration ensures that both teams stay aligned, whether you're handling development in Jira or managing tasks in Wrike. With features like field mapping, status synchronization, and customizable workflows, you can streamline collaboration, enhance efficiency, and tailor the integration to meet your unique business needs.

This guide will walk you through the setup process, ensuring a smooth and efficient integration experience.

### **Step-by-Step Setup Guide** <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

#### **1. Access the Getint App in Jira** <a href="#id-1.-access-the-getint-app-in-jira" id="id-1.-access-the-getint-app-in-jira"></a>

Navigate to **Apps** and select **Jira-Wrike Integration.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdSHRWruRuz1G5Pbb1Ydn%2FJira%20Wrike%20Integration%20App.png?alt=media&#x26;token=b7bbeb91-a1e3-4688-866f-d84ef2b1e461" alt=""><figcaption></figcaption></figure>

#### **2. Create Integration** <a href="#id-2.-create-integration" id="id-2.-create-integration"></a>

Click **Create Integration** and choose between **Continuous Sync** or **Migration** based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0LhTTdNgsUH4vh95s8Yy%2FContinuous%20Sync%20or%20Migration.png?alt=media&#x26;token=460f20d9-0c04-4034-ac65-2a4ef0c0623e" alt=""><figcaption></figcaption></figure>

#### **3. Generate a Jira API Token** <a href="#id-3.-generate-a-jira-api-token" id="id-3.-generate-a-jira-api-token"></a>

For Jira Cloud:

* Log in to your Atlassian account and navigate to **Account Settings > Security**.
* Generate an API token, which will act as your password for integration.
* Copy and securely store the token.

For detailed instructions, refer to guide [**Connection**](https://docs.getint.io/guides/quickstart/connection).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhsPN7FHhoLb3eYAOKcuN%2FJira%20API%20Token.png?alt=media&#x26;token=e52d779d-c0ad-4149-8102-0988dfef1d9b" alt=""><figcaption></figcaption></figure>

#### **4. Generate a Wrike Permanent Access Token** <a href="#id-4.-generate-a-wrike-permanent-access-token" id="id-4.-generate-a-wrike-permanent-access-token"></a>

1. Log in to your Wrike account.
2. Verify your Wrike account if the API settings are unavailable.
3. Go to **Account Settings > Apps & Integrations > API Access**.
4. Generate an Access Token and securely store it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXYqCZltZXm0Ek8AKilAQ%2FWrike%20access%20token.png?alt=media&#x26;token=2295fb7d-b7f6-4bad-a74c-a60d01c6bd03" alt=""><figcaption></figcaption></figure>

For detailed instructions, refer to our [Connection](https://docs.getint.io/guides/quickstart/connection) guide.

#### **5. Connect to Jira and Wrike** <a href="#id-5.-connect-to-jira-and-wrike" id="id-5.-connect-to-jira-and-wrike"></a>

**Jira Connection:**

* Enter your Jira instance URL, username, and API token in Getint.
* Select the Jira project you want to synchronize.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsiWQrwcbl76Kt8ctoMEu%2FJira%20Wrike%20Connection.png?alt=media&#x26;token=869e2a9a-629c-4d6f-8b81-9745a31376a2" alt=""><figcaption></figcaption></figure>

**Wrike Connection:**

* Use the Permanent Access Token to connect Wrike to Getint.
* Select the Wrike workspace and Folder you wish to sync with Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F13QTj2iocFtrDk42dlWB%2FWrike%20connection.png?alt=media&#x26;token=6c5877fd-eb64-4dd2-a98d-bd7aa7eb7019" alt=""><figcaption></figcaption></figure>

* Click **Save** to establish the connection.

#### **6. Type Mapping** <a href="#id-6.-type-mapping" id="id-6.-type-mapping"></a>

Map the types of items you want to synchronize between Jira and Wrike.

* **Tasks ↔ Tasks**
* **Subtasks ↔ Subtasks**

Use the **Type Mapping** screen in Getint to configure the mappings according to your workflow needs.

Consider using the **Quick Build** beta feature for automated type and field mapping to streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVmoFoUONXEjvI3g9TrFE%2FJira%20Wrike%20type%20mapping.png?alt=media&#x26;token=149b16fb-8c38-4cce-9826-c8f5a35c17dc" alt=""><figcaption></figcaption></figure>

#### **7. Field Mapping** <a href="#id-7.-field-mapping" id="id-7.-field-mapping"></a>

* Select the fields to synchronize, such as **Title**, **Description**, **Assignees**, and **Custom** fields.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4AUxgFbSRofGluLsCE2Z%2FField%20mapping%20Jira%20Wrike.png?alt=media&#x26;token=1c5642bf-232a-441c-87d7-100413761ae9" alt=""><figcaption></figcaption></figure>

* Use the arrows to define the synchronization direction:
  * **Unidirectional:** Sync changes from one platform to another.
  * **Bidirectional:** Sync updates in both directions.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkwsEYv0GOxsOhOLRQnwH%2FSynchronization%20direction%20in%20a%20Jira%20Wrike%20integration.png?alt=media&#x26;token=3d1bc7cc-1c4d-46e4-9a4a-471c91c957cf" alt=""><figcaption></figcaption></figure>

* Click **Apply** to save your field mappings.

#### **8. Status Mapping** <a href="#id-8.-status-mapping" id="id-8.-status-mapping"></a>

1. Create tasks in Wrike for each status you wish to synchronize.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpwTIhhYxmsVQNyB1fDiB%2FStatus%20mapping%20for%20a%20Jira%20Wrike%20integration.png?alt=media&#x26;token=d3449143-2eb5-4635-a28c-afecbb357b6f" alt=""><figcaption></figcaption></figure>

1. In Getint, go to the **Status Mapping** tab.
2. As Wrike does not provide the API, it is necessary to select **Add Option Manually** for its side.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOD6aK47GE4JV1U8sJrDG%2Fadding%20option%20manually.png?alt=media&#x26;token=04477a34-2b83-4f9e-a70f-b70c1a45173f" alt=""><figcaption></figcaption></figure>

1. Copy the Wrike task status ID and paste it into Getint.
2. Assign a name to the status and map it to its Jira counterpart.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9kKzFb3jGRsJJek9c8jS%2FAssign%20a%20name%20to%20the%20status.png?alt=media&#x26;token=640a611a-d34a-4c21-9cf9-3f1bbdf9d3b5" alt=""><figcaption></figcaption></figure>

1. Repeat for all statuses and then **Apply**.

{% hint style="info" %}
**Tip:** Add and map statuses one at a time to avoid resetting the dropdown menu.
{% endhint %}

#### **9. Filtering Options** <a href="#id-9.-filtering-options" id="id-9.-filtering-options"></a>

Customize synchronization by applying filters:

1. Click the **Filtering** icon near the app icon in your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FseqdR7Akcs0KVEMUNtv0%2FFiltering%20options%20for%20Jira%20Wrike%20integration.png?alt=media&#x26;token=513ab821-5359-4de0-bff5-644b7fddfb64" alt=""><figcaption></figcaption></figure>

1. Choose the filter scope:

* **All**: Apply the filter to all items.
* **New**: Apply the filter to newly created items only.
* **Synced**: Apply the filter to already synchronized items.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjPxOQtpKi4TXS593mSKk%2FChoose%20the%20filter%20scope.png?alt=media&#x26;token=34c705f0-5572-479f-84b6-362a499c9be5" alt=""><figcaption></figcaption></figure>

1. Add values for the filters and click **Apply**.
2. Name and click on **Create** to save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FINkVbHu7QZb1mx2toSYa%2FSaving%20your%20integration.png?alt=media&#x26;token=929240f5-b366-4902-b39c-17fc75960673" alt=""><figcaption></figcaption></figure>

For more details, refer to our [Filtering Guide](https://docs.getint.io/getintio-platform/workflows/items-filtering).

#### **10. Test the Integration** <a href="#id-10.-test-the-integration" id="id-10.-test-the-integration"></a>

1. Create test tasks in both Jira and Wrike.
2. Verify synchronization by adding comments, attachments, or updating task statuses.
3. Check logs in Getint to ensure proper synchronization.

{% embed url="<https://www.loom.com/share/a67d469bd38f40b79092430a53595a60?sid=f435dd99-b3d1-4ab5-b1ac-246aaa5fd709>" %}

### **Conclusion** <a href="#conclusion" id="conclusion"></a>

By following this guide, you can successfully integrate Jira and Wrike using Getint. This setup allows you to synchronize tasks, statuses, and workflows, fostering seamless collaboration between teams.

For further assistance, visit our [Help Center](https://getint.io/help-center) or schedule a demo to explore the full potential of Getint.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmLeA5dSF46PtimhtWwRE%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=4a7609ca-78d2-4f00-acd0-74d4a58bacaf" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
