# Source: https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration.md

# Jira ServiceNow integration

Easily integrate Jira and Jira Service Management with ServiceNow for enhanced workflow efficiency. You can ensure data consistency by bridging the gap between IT teams (using ServiceNow) and software development teams (relying on Jira). The integration provides a unified workspace where users can manage Jira incidents, problems, changes, and service requests within ServiceNow, and vice versa. Set up the Jira-ServiceNow integration using the application available in the Atlassian Marketplace (for cloud customers), the Data Center apps, or the On-Premise version of Getint. This bi-directional integration allows you to send ServiceNow incident events to Jira Service Management and vice versa. Enjoy cross-functional collaboration, streamlined processes, and a cohesive view of your tickets across platforms.

### Requirements to build your integration: <a href="#requirements-to-build-your-integration" id="requirements-to-build-your-integration"></a>

* A Jira instance with a dedicated user, and an API token for that user.
* A ServiceNow instance with a dedicated user. For testing purposes, you can create a developer instance here:[<img src="https://developer.servicenow.com/favicon.ico" alt="" data-size="line">ServiceNow Developers](https://developer.servicenow.com/dev.do)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxPB2B3r5PhVg3ItlD8qS%2FJira%20Snow%20developer%20instance.png?alt=media&#x26;token=0481d2b1-54b9-4a0f-bc1c-bf00df3bbe64" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
For a detailed guide on how to create a ServiceNow user, please visit the following link: [How to create a ServiceNow user.](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration)
{% endhint %}

* For Jira **Cloud customers,** download the corresponding app from the Atlassian Marketplace, and launch it. Please note that we support both Jira Software and Jira Service Management.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtlJcuf7AEnbuDyYe8lEE%2FJira%20Snow%20developer%20instance.png?alt=media&#x26;token=830c6e40-d4b9-4b90-9fd8-d2dfa80ec403" alt=""><figcaption></figcaption></figure>

* For Jira **Data Center,** please click your profile icon at the top right corner of your Jira instance, click **Atlassian Marketplace,** and use the option **Find new apps** to search for our **Jira ServiceNow integration app by Getint** (similar to the apps found below).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSgpVKMXdpz03ISXtpRVX%2FDownloading%20the%20Snow%20app%20from%20the%20Atlassian%20marketplace.png?alt=media&#x26;token=7d911c5d-052e-4840-a84e-39833d1d2457" alt=""><figcaption></figcaption></figure>

### Setting up your ServiceNow integration <a href="#setting-up-your-servicenow-integration" id="setting-up-your-servicenow-integration"></a>

#### **1. Accessing Getint:**

* Launch the app, and click **Create integration** or **Migration.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F883r3IPFXuCiKBuWdWOG%2FBuilding%20an%20integration.png?alt=media&#x26;token=67ab614f-ef65-4fe7-bd44-d0b474e048ee" alt=""><figcaption></figcaption></figure>

#### **2. Token generation for Jira Cloud:**

* For **Jira Cloud,** generate a Jira token. This token will act as your password.
* Go to **Atlassian Account Settings.**
* Navigate to **Security** and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FP69SIlFBn8plq08HvUIW%2FCreating%20API%20token.png?alt=media&#x26;token=1e792058-668b-420d-aa08-c63d1b730aef" alt=""><figcaption></figcaption></figure>

#### **3. Establishing a Connection with Jira:**

* Ensure you’re logged in as a user with admin rights, click on **Connect App,** and select Jira. Choose **Create New** to set up a fresh connection with your Jira instance and input the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FV9C3x2mgvJYSJiArz0np%2FCreating%20a%20connection.png?alt=media&#x26;token=e4b6d266-b59f-4e97-9c88-1b4049ab0026" alt=""><figcaption></figcaption></figure>

* After establishing the connection, select the **Jira project** you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4moYvRxpyVvijr8xDp3u%2FName%20your%20connection.png?alt=media&#x26;token=9da2f3c5-3ed5-40b6-b050-3fee414dc9af" alt=""><figcaption></figcaption></figure>

#### **4. Establishing a Connection with ServiceNow:**

* Connect to **ServiceNow.** If no connection is established yet, create a new one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzY9rsJh8WpaMBnK6ZOin%2FEstablishing%20connection%20with%20Snow.png?alt=media&#x26;token=6dadcf71-048e-45e0-9ccc-a43320c2287b" alt=""><figcaption><p>You can find your credentials within the settings in your <strong>ServiceNow</strong> instance.</p></figcaption></figure>

{% hint style="info" %}
It is crucial to grant specific access permissions to your ServiceNow user; otherwise, the connection will fail. You can find the full list of required permissions [here.](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration)
{% endhint %}

#### **5. Type mapping:**

* **Quick Build (Beta):** You can use the Quick Build feature to automatically map fields and types between your apps. It’s a convenient way to make the process easier.
* **Manual Mapping:** If you prefer more control, you can manually map the types yourself. This allows you to customize the mapping based on your specific requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FI2NhvHzOZUnXtt1ta4mW%2FUsing%20Quick%20build.png?alt=media&#x26;token=ffb84f96-aca7-4d2d-873a-15edc5a0f610" alt=""><figcaption></figcaption></figure>

* **Mapping ServiceNow Projects:** Projects in ServiceNow are part of the [Strategic Portfolio Management](https://www.servicenow.com/docs/bundle/vancouver-it-business-management/page/product/project-management/concept/c_ProjectApplicationOverview.html) (SPM) module. This module must be installed so that project mappings appear as an option in the dropdown list when pairing your type mappings. You can find more information about this module [here.](https://www.servicenow.com/docs/bundle/vancouver-it-business-management/page/product/project-management/concept/c_ProjectApplicationOverview.html)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FN6By0OLuQUQbNpfvlM4b%2FProject%20type%20mapping%20for%20ServiceNow.png?alt=media&#x26;token=312fc436-e213-4662-9d6c-05911f8322c0" alt=""><figcaption><p>Project mapping in Jira ServiceNow integration</p></figcaption></figure>

* After enabling this module, you can start syncing ServiceNow projects from your **Project workspace.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLsL177WgZnvAm9Y6ocsH%2FServiceNow%20project%20workspace.png?alt=media&#x26;token=24c343f0-1b7f-4e47-b81f-28f4999531e9" alt=""><figcaption></figcaption></figure>

* These will sync just like any other ServiceNow table, such as incidents, change requests, and more. Consequently, any new project from ServiceNow can be seamlessly transferred as a new task in Jira.

#### **6. Field mapping:**

* Review or manually map which fields to integrate and sync within the mapped types, including title, description, assignees, custom fields, and more.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqvGhGmzPWxEE8KCoSWGP%2FField%20mappings.png?alt=media&#x26;token=d0b18993-80cd-491d-98e8-cfd5e4f3206a" alt=""><figcaption><p>Example of automatic field mappings with <strong>Quick Build</strong> where you can also add fields manually while using <strong>Quick Build.</strong></p></figcaption></figure>

#### **7. Assignees:**

* Map **Assignees** according to your user pairing requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F1kJFuLpmBOUoGCNljb4Q%2FAssignees.png?alt=media&#x26;token=e8ba8667-648f-4168-8f0f-457b15cae87b" alt=""><figcaption><p><strong>Assignees</strong> in Jira (left). <strong>Assigned to</strong> in ServiceNow (right)</p></figcaption></figure>

#### **8. How to Manage Comments & Attachments:**

* Check the **Comments & Attachments** tab. These are activated by default, but you’re free to modify them depending on your organization’s needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8BfwAoqxdtjJeCSfkqeI%2FComments%20%26%20attachments%20sync%20(1).png?alt=media&#x26;token=5cb295fc-7433-4d21-be30-ff4d8d478ec0" alt=""><figcaption></figcaption></figure>

* For ServiceNow integrations, there’s an option to further customize how comments are created under **Customize comments creation.** It can be incredibly helpful to make specific comments that either go Public or Private or **be skipped completely.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2GRWwL02S0XDabziBvC8%2FServiceNow%20Comments%20and%20Attachments%20Customization%20(1).png?alt=media&#x26;token=5b333fcf-21ce-4539-85a9-21898e8b16ea" alt=""><figcaption></figcaption></figure>

* You can also choose the sync direction for attachments: **both ways,** **only to App A (left),** or **only to App B (right).** This feature adds an extra layer of customization to meet your organizational needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9oIFLum46yiunQjQBtfV%2FSynchronizing%20attachments.png?alt=media&#x26;token=7bf4d0d7-257f-4aeb-adbd-7b66ae057f51" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You can disable comments and attachments entirely if they are not needed or are restricted in your organization.
{% endhint %}

#### **9. How to Map Statuses:**

* Map **Statuses.** Ensure you’re using the correct fields that represent the statuses for each app.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxqdpiwpJxjUVQ9HEpW6L%2FMapping%20statuses.png?alt=media&#x26;token=d9421809-c87f-4b75-9a6f-06c6d1933da4" alt=""><figcaption></figcaption></figure>

#### **10. Finishing your Integration**

* Name your project and click **Create** at the top right corner to finish the integration setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfHJYlwdle2DMjzmxKedU%2FFinishing%20your%20integration.png?alt=media&#x26;token=e0e87faa-90da-4587-ab46-53067bd170d7" alt=""><figcaption></figcaption></figure>

#### **11. UI Filtering**

* After finalizing your integration, you may also add filters to each app. Select the filter icon adjacent to the app icon within your integration. This action will affect the corresponding side of the integration.
* **Define Filter Rules**:
  * **ALL items filters**: Rules will be verified for every item before synchronization.
  * **NEW items filters**: Rules will be verified only for newly created items that have not yet been synced.
  * **SYNCED items filters**: Rules will be verified for items that were already synced in the past.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9bmB9mrXlZnRbBNIbBcL%2FItems%20filtering.png?alt=media&#x26;token=46a7aab0-09c3-49cc-923e-ee13c93112c1" alt=""><figcaption><p>For more information about this feature, please visit <a href="https://docs.getint.io/getintio-platform/workflows/items-filtering">Items Filtering.</a></p></figcaption></figure>

* You can also use custom queries to synchronize tickets only when the Assignment Group is set to a specific value. For example:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkWUUNXiTeE7CB3GvDi8G%2FCustom%20query%20for%20SNOW%20groups.png?alt=media&#x26;token=b98c3036-6aa9-4d8f-8c58-bfc575359ee6" alt=""><figcaption><p>A custom query to sync ServiceNow tickets by the Assignment Group ID</p></figcaption></figure>

#### **12. Case Scenario for Items Filtering:**

* For example, If you want to integrate **Jira Project A** with ServiceNow Incidents that belong to **Assignment Group A,** use the filter items feature. In Getint, you can configure the connection by mapping the types and fields between ServiceNow and Jira, ensuring that fields like **Assignee** and **Assignment Group** are correctly synchronized.
* On a separate integration, you can set up (or duplicate the existing integration) to integrate **Jira Project B** with ServiceNow Incidents that belong to **Assignment Group B.** Here, different filtering will be needed. You can define filter rules in Getint to control which items are synchronized, specifying criteria such as status or priority to ensure only relevant items are synced. This helps manage data efficiently and avoids unnecessary clutter. Remember to save the integration once the filters are applied to ensure they are active.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjeQHAfpEIT9mwpPlvjn4%2FFiltering%20items%20by%20assignment%20groups.png?alt=media&#x26;token=bc630a57-cec2-41ab-a420-eded3eea8e80" alt=""><figcaption><p>Filtering items by Assignment Group</p></figcaption></figure>

#### **13. Test your integration:**

* Ensure you aren’t experiencing any errors and that your integration is running smoothly. Create test scenarios to validate the functionality of your setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQdZBNclmbe5HGkyHXVFv%2FServiceNow%20incident.png?alt=media&#x26;token=c380cfae-d5d9-4f76-a71f-ed14af519906" alt=""><figcaption><p>ServiceNow ticket created for testing purposes</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ffdcp5Jssc6u3C18YbGpX%2FNew%20Jira%20ticket%20created%20from%20SNOW%20integration.png?alt=media&#x26;token=eb6dd91a-efa8-4ca8-9aba-57b32c6ea6a3" alt=""><figcaption><p>A new Jira ticket was created on the other end as a result of the integration</p></figcaption></figure>

### Conclusion <a href="#conclusion" id="conclusion"></a>

By following these steps, you can easily integrate Jira with ServiceNow, ensuring efficient synchronization of tasks, issues, and workflows across both platforms. This configuration promotes collaboration and streamlines project management processes. Please contact our [Support Team](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team), if you require further assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
