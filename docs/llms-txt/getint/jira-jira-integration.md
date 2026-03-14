# Source: https://docs.getint.io/guides/integration-synchronization/jira-jira-integration.md

# Jira Jira integration

Integrating Jira with Jira through Getint provides users with a robust solution to streamline project management and collaboration workflows. This powerful integration enables seamless data synchronization across different projects within the same platform, allowing users to efficiently track and manage Jira tickets, tasks, bugs, and epics in diverse Jira environments. For example, a company developing various products such as mobile phones, computers, and smartwatches can benefit from this integration. While each development team operates within its designated Jira environment, Getint facilitates collaboration across projects by enabling integration and filtering of relevant projects, ensuring teams can work together effectively while maintaining appropriate access restrictions.

{% hint style="info" %}
While some steps may vary depending on your current deployment, we support syncing items from Jira Software (Cloud and Service Management), and Jira Data Center.
{% endhint %}

### Jira Jira Licensing Model: <a href="#jira-jira-licensing-model" id="jira-jira-licensing-model"></a>

The Jira Jira licensing model with Getint is designed to accommodate various integration scenarios. Here's a breakdown:

* **Standard Dual Licensing:** This model requires the Getint license to be installed on both Jira instances involved in the integration. This ensures that each instance is properly licensed and can communicate seamlessly.
* **Remote License:** For situations where installing the Getint app on both Jira instances is not feasible (e.g., when integrating with a partner company that doesn't want to install any additional apps), Getint offers a **Remote License** for a fixed fee. This provides a flexible solution for such cases.
* **Flexible License:** For managed services companies or organizations looking to integrate four or more instances (regardless of whether they are the same or different tools), Getint offers a **Flexible License.** This custom license covers a specific number of connections (i.e., up to 10 instances) without restrictions on the tools involved. You can also swap the integrated tools while the license remains active, offering unparalleled flexibility.

For more information about our licensing options, please read [more.](https://docs.getint.io/billing-and-services/licensing)

### Requirements to Build Your Integration: <a href="#requirements-to-build-your-integration" id="requirements-to-build-your-integration"></a>

* The Jira Jira Getint app must be installed on both instances unless you’re opting for a **Remote License** (app installed on a single instance only)**.**
* Both Jira instances should include a dedicated user and an associated API token. These users must have permission to read, write, view, and modify the project.
* Comments are added as the user you chose to create the connection. Therefore, we recommend using dedicated Service Accounts for both instances as comments will be attributed to the user who established the connection.
* Personal Access Tokens to establish the connections. More information about creating API tokens here: [<img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Ficon%2FPRq8D5IBseUvQPEVFVwD%2FGitbook%20getint%20sygnet%20logo.png?alt=media&#x26;token=3353768c-d008-46f7-bc2d-fd71b5d48f14" alt="" data-size="line">Connection](https://docs.getint.io/guides/quickstart/connection#jira).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJlxO4cRlrnMNKihzj5J7%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=39917e2c-268a-456e-ac81-bc1e9c44b149" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

### Setting up your Jira integration <a href="#setting-up-your-jira-integration" id="setting-up-your-jira-integration"></a>

#### **1. Access the** [**Getint**](https://marketplace.atlassian.com/apps/1223930/issue-sync-integration-for-jira-getint-issue-sync?hosting=cloud\&tab=overview) **App in Jira:**

* Navigate to Jira, go to **Apps**, and select the Getint app (Jira - Jira integration in this case).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUN0eSqTxVkL47IMsdIeo%2FJira%20jira%20integration%20app.png?alt=media&#x26;token=19eca1f6-9386-4125-b63e-789adba8a461" alt=""><figcaption></figcaption></figure>

* Select **Create Integration** then **Continuous Sync** or **Migration** based on your requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVNDkkoLk6Xu14yj5iCl7%2FContinuous%20Sync%20or%20Migration.png?alt=media&#x26;token=003d7bef-af3e-4c65-8b63-4938a1485211" alt=""><figcaption></figcaption></figure>

#### **2. Token Generation for Jira:**

#### **Jira Cloud**

* Sign in to your Atlassian account and navigate to the Account Settings.
* Head to the Security section and select **Personal API Token**.
* Click on **Create API token** and provide a label to identify your token easily.
* Hit **Create** to generate the token.
* Copy the token and store it securely in a safe location.

{% embed url="<https://youtu.be/K5jRfZVKLOo>" %}

#### **Jira Data Center**

Unlike Jira Cloud, the Data Center does not require a token and can be accessed using an email and password. If you choose to use a token, leave the **email** option blank on the Getint platform:

1. Log in to your Jira Data Center instance.
2. Click on the Avatar at the top right of the screen.
3. Select **Profile** and then **Personal Access Tokens**.
4. Click on **Create Token**, provide a name for your token, and specify whether the token will expire and when.
5. Copy the token and store it in a safe location.

{% embed url="<https://youtu.be/5bpdLeFn-Qo>" %}

#### **3. Establish a Connection with Jira:**

* Ensure you're logged in as a user with the correct permissions.
* Click **Select App** and choose Jira.
* Select **Create New** to connect with your Jira instance.
* Name your connection, and add the URL of your Jira instance.
* Provide the login credentials.

{% embed url="<https://www.loom.com/share/50ef974c586a49d7b5537bba8106e341?sid=14829839-3999-4a47-921f-b845ea84eac3>" %}

#### **4. Choose and Connect the Second Jira Project:**

* Repeat the process on the other side. Since you are connecting Jira with Jira, repeat the steps.

{% embed url="<https://www.loom.com/share/56ae6bc216d84dccb7a4537f5b2e3cfe?sid=2b0e23d8-ecfb-4c57-a83f-e2b814f900be>" %}

#### **5. Type Mapping:**

* **Quick Build (Beta):** Utilize the Quick Build feature to automatically map fields and types between your applications. This feature simplifies the process.
* **Manual Mapping:** For greater control, manually map the types yourself. This approach lets you tailor the mapping to meet your specific needs. Click **+ Add type mapping** to add Jira types (Task, Bug, Epic, Story) by yourself.
* After configuring your type and field mappings, name and save your integration settings.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fvgv4Ed3JBr6oB9BfWv62%2FQuick%20build%20type%20mapping%20for%20jira%20jira%20integration.png?alt=media&#x26;token=9fc73fd2-4982-4c71-9024-47c9d6d429af" alt=""><figcaption></figcaption></figure>

#### **6. Field Mapping:**

* Review or manually assign the fields to integrate and synchronize within the mapped types, such as title, description, assignees, custom fields, and more.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFKyYI8y877XWNlRJcVZz%2FJira%20Jira%20field%20mapping.png?alt=media&#x26;token=76754361-8922-4f71-bae0-a8d1f30ca9ca" alt=""><figcaption><p>Example of automatic field mappings with <strong>Quick Build</strong> where you can also add fields manually while using this feature.</p></figcaption></figure>

#### **7. Assignees Mapping:**

* Map assignees according to your organization’s requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvtpH9DI5um49ZRhuF1rJ%2FAssignees%20in%20Jira%20Jira.png?alt=media&#x26;token=6f9446d9-8b5f-4b97-85bf-c560a4c9e470" alt=""><figcaption></figcaption></figure>

#### **8. How to Manage Comments & Attachments:**

* Review the **Comments & Attachments** tab. These features are enabled by default, but you can adjust them as needed to suit your organization's requirements.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDnRnJDn3JNloxrt4sR49%2FComments%20%26%20attachment%20sync%20in%20Jira%20Jira%20integration.png?alt=media&#x26;token=084ea820-d684-484a-a7dc-466bde27caf6" alt=""><figcaption></figcaption></figure>

* For Jira Jira integrations, you have the option to further customize comment creation under **Customize comments creation**. This allows you to specify whether comments should be Public, Private, or omitted entirely, providing flexibility to meet your needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCdRqKu8I1O6nirMLgsc1%2FComments%20configuration%20for%20Jira%20Jira%20integrations.png?alt=media&#x26;token=201777d7-fe32-46c8-b041-1e5d06c08e3e" alt=""><figcaption></figcaption></figure>

* You can also modify the sync direction for comments and attachments: **Both ways,** **only to Jira A (left),** or **only to Jira B (right).**

{% hint style="info" %}
You can disable comments and attachments entirely if they are not needed or are restricted in your organization.
{% endhint %}

#### **9. Mapping Statuses**

* Make sure you’re using the correct fields that represent the statuses for each Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmrLnMOwMmMMik0nvWHmz%2FStatus%20for%20Jira%20Jira.png?alt=media&#x26;token=538474c2-8a7d-460b-915d-83a6efb03092" alt=""><figcaption></figcaption></figure>

#### **10. How to Enable Filters:**

It is possible to filter the synchronization to have them customized for your needs and requirements.

#### **UI Filtering**

* After finalizing your integration, you may also add filters to each Jira instance. Select the filter icon adjacent to the app icon within your integration. This action will affect the corresponding side of the integration.
* **Define Filter Rules:**
  * **ALL items filters:** Rules will be verified for every item before synchronization.
  * **NEW items filters:** Rules will be verified only for newly created items that have not yet been synced.
  * **SYNCED items filters:** Rules will be verified for items that were already synced in the past.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fjd5tQYSLDYOmJh7ymHb0%2FJira%20items%20filtering.png?alt=media&#x26;token=98c88e10-4434-4210-a574-a80f911b96dc" alt=""><figcaption><p>For more information about this feature, please visit <a href="https://docs.getint.io/getintio-platform/workflows/items-filtering">Items Filtering.</a></p></figcaption></figure>

#### **JQL Filtering:**&#x20;

* Select the side that will receive the filter.
* Under the field Custom JQL, it is possible to provide a JQL, which will be the filter for your sync and appended to the one generated when searching for issues in Jira (i.e., status in ("In Progress")).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTuiyjbQeBvITKrW1WXft%2FJira%20JQL.png?alt=media&#x26;token=75b8d907-c0cb-49d6-bfe7-5c6b3c21a39d" alt=""><figcaption></figcaption></figure>

#### **11. Duplicating Your Setup and Selecting Different Projects:**

* Go to Workflows.
* Click the 3 dots on the right side and select **Duplicate**.
* A side panel will appear. Select a new name for the integration (by default, the integration will be called **copy of** if the same projects are established).
* On the dropdown menu, select the projects that you would like to integrate.
* For each side, select **Connect**. Then **Duplicate**.
* Save the new integration.

{% embed url="<https://www.loom.com/share/8e0f7b01d465470498af29b0d3224f23?sid=0746ccf2-4f87-4fcc-90fd-facba4f2befe>" %}

{% hint style="warning" %}
This setup applies to both Jira Software and Jira Service Management, enabling integration of tasks, bugs, and epics, as well as incidents, service requests, and IT help types specific to Jira Service Management.
{% endhint %}

#### **12. Final Steps:**

* Complete the integration setup by naming your project and clicking **SAVE** in the top right corner.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4DKF862kjSI2O3yK3tsu%2FJira%20Jira%20main%20screen.png?alt=media&#x26;token=0fc09650-7cf6-4813-bcaf-1e7f6180aec6" alt=""><figcaption></figcaption></figure>

At Getint, we're dedicated to providing exceptional support throughout your integration journey. Our team is committed to delivering the best customer experience. For any questions about this integration or assistance with the setup process, don't hesitate to open a ticket at our [Help Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team). We're here to help!

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
