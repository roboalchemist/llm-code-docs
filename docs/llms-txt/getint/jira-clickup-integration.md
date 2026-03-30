# Source: https://docs.getint.io/guides/integration-synchronization/jira-clickup-integration.md

# Jira ClickUp integration

Integrating Jira with ClickUp using Getint allows teams to manage projects seamlessly across platforms, combining Jira’s robust issue tracking with ClickUp’s dynamic task management. This powerful integration supports both Jira Cloud and Jira Server, enabling real-time data synchronization between Jira issues and ClickUp tasks. Whether you need a one-way or two-way sync, this step-by-step guide ensures you can set up the integration quickly and effortlessly, improving productivity and collaboration across your teams with **enterprise-grade, no-code solutions**.

### **Why Choose Getint for Atlassian Native Integrations?** <a href="#why-choose-getint-for-atlassian-native-integrations" id="why-choose-getint-for-atlassian-native-integrations"></a>

Getint specializes in **secure, SOC 2 Type 2 certified integrations** for enterprise environments, ensuring that data synchronization across platforms like **Jira, Azure, ClickUp, Confluence, and Trello** remains efficient and secure. With **no-code integrations for Jira**, Getint makes it easy for teams to connect platforms without extensive technical knowledge, offering solutions that integrate natively with Atlassian tools.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDFiMQ5y6jPSGhzwEFQTb%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=f02690b6-d42f-4b2d-ad72-da0b788c6e31" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

### **Step-by-Step Guide to Integrating Jira with ClickUp** <a href="#step-by-step-guide-to-integrating-jira-with-clickup" id="step-by-step-guide-to-integrating-jira-with-clickup"></a>

Here’s how to set up **Jira-ClickUp integration** using **Getint’s real-time sync** solution:

#### **1. Access the Getint App in Jira**

* Navigate to Jira, go to **Apps**, and select **ClickUp Integration for Jira** to start the integration process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIzIKcKYk7d5V3OuBFgN5%2FLaunching%20Getint%20Jira%20Clickup%20app%20integration.png?alt=media&#x26;token=1eb11411-c325-44b7-abe7-fa32d89141e1" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Pro tip**: Ensure you’re logged in as an admin user to avoid permission issues during setup.
{% endhint %}

#### **2. Create a New Integration**

* Click **Create Integration** for ongoing sync or **Migration** to transfer existing data.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBqUsLQI0qqerbaqjn7dy%2FInitiating%20app.png?alt=media&#x26;token=9d227f6a-fab9-4ec1-8e67-179eac97d0da" alt=""><figcaption></figcaption></figure>

#### **3. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbmHNJBVnrEaDJIMNvWbB%2FAPI%20Token.png?alt=media&#x26;token=64428dc4-e407-456e-a625-9d00787b2ae8" alt=""><figcaption></figcaption></figure>

#### **4. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click on "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoVSRYR0eneTbFvJGYViI%2FChose%20the%20app%20and%20established%20connections.png?alt=media&#x26;token=f802e601-2b01-43d0-a39a-04a80ea021ec" alt=""><figcaption></figcaption></figure>

#### **5. Select the Jira Project**

* Once the connection is established, a dropdown menu will appear. Choose the **Jira project** you want to sync with ClickUp.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLPVPuuq5ciJiuplvjd6A%2FSelecting%20Jira%20project.png?alt=media&#x26;token=b1dd1ceb-d928-46ec-b812-fd30e435436c" alt=""><figcaption></figcaption></figure>

#### **6. Generate ClickUp API Token**

* Follow our guide to generate the [**ClickUp API Token**](https://docs.getint.io/guides/quickstart/connection#clickup) and create the connection.
* Then select the connection, and choose the space and folder you wish to sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F1aF5KC8QCUce45bse0Qb%2FChose%20the%20app%20and%20established%20connections.png?alt=media&#x26;token=3a001f7b-2036-4b45-a0e5-c3b67797f9a7" alt=""><figcaption></figcaption></figure>

#### **7. Map Issue Types and fields**

Consider using the **Quick Build beta feature** for automated type and field mapping to simplify the setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9pIK91w86sNcMfSFSkg1%2FUsing%20Quick%20Build.jpg?alt=media&#x26;token=54353b32-c9a5-4e12-9fa1-34d021adc43d" alt=""><figcaption></figcaption></figure>

* Define how Jira issue types will sync with ClickUp task types.
  * Example: map a **Jira Task** to a **ClickUp Task** or a **Jira Bug** to a **ClickUp Task**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4OcEeDGgW6uWXJRpN3rH%2FDefine%20issue%20types.png?alt=media&#x26;token=b9ca50d1-b73d-4073-ba03-d0c78f084864" alt=""><figcaption></figcaption></figure>

* Manually map or modify fields like **Title**, **Description**, **Assignee**, and **Custom Fields** between Jira and ClickUp.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FT859ESZMW8STGdRvH5lm%2FModify%20issues%20manually.png?alt=media&#x26;token=1207dd27-a0a4-4ee0-ba3e-4f495fb4a265" alt=""><figcaption></figcaption></figure>

#### **8. Status Mapping**

* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process
* Enable and configure **Status Mapping** between Jira and ClickUp.
  * Map Jira statuses (e.g., **To Do**, **In Progress**, **Done**) to their corresponding ClickUp statuses for consistency.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxAejkaQLUnyM3N5TyVBJ%2Fimage-20240918-134034.png?alt=media&#x26;token=b9d9a16e-e484-4823-af50-799faa862173" alt=""><figcaption></figcaption></figure>

#### **9. Sync Comments and Attachments**

* If needed, enable the synchronization of comments and attachments. Customize comment syncing, such as making them private or public or providing the parameters that fit your synchronization. Then apply and save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGvGu8JbPsctfiEFypJXm%2FSynchronizating%20too%20many%20songs%2C%20right%2B.jpg?alt=media&#x26;token=f53c0ea3-6ba7-4c9d-8b98-bb9c68b9bebf" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQU8sw7JbkJ5FGvlHrA60%2F%C3%B6ptions%20for%20synchronization.jpg?alt=media&#x26;token=302afa52-2e5b-4dc4-aa5a-17a146fa36d1" alt=""><figcaption></figcaption></figure>

#### **10. UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCpxSpYZoBpLRLimjk1pT%2FGithub%20pendiente.png?alt=media&#x26;token=e89ba532-e405-4e1c-9f32-ff84768d771e" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvpWZgeo8gmaPs844ZZKF%2FClickup%20user.jpg?alt=media&#x26;token=bc977f0c-75a8-4f9c-8ebc-359edfb90159" alt=""><figcaption></figcaption></figure>

Once you create the filters, Name the integration and Save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLEJwpDI8b22K7wczWaq5%2FUntitled%20design%20(4)%20(1).jpg?alt=media&#x26;token=e5bbcb67-9f58-4787-8a5a-4f65181c899d" alt=""><figcaption></figcaption></figure>

#### **11. Test the Integration**

* Create sample tasks in both Jira and ClickUp to ensure the integration works as expected.
* Check the **reporting section** to confirm the sync is successful. If issues arise, visit our [**Help Center**](https://getint.io/help-center) for assistance.

#### **Advanced Settings for Your Atlassian Integration**

For users looking for advanced integration features, Getint allows for custom configurations, such as syncing **comments, attachments**, and **custom fields** between Jira and ClickUp. You can also tailor **workflow automation** to your team’s needs, ensuring that your data flows exactly how you need it to.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdyysprFdJEELfEZqwFPB%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=3b653e81-cace-400d-9405-0bb554b122f0" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues to build your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
