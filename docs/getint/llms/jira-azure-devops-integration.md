# Source: https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration.md

# Jira Azure DevOps integration

Integrating Jira (Software/Service Management) and Azure DevOps (Cloud/OnPremise) is essential for optimizing workflows. Getint's integration bridges the gap between tracking project milestones in Jira and managing development tasks in Azure DevOps. Whether you're using Jira Cloud, Data Center/Server, or On-Premise, this guide will help you set up an efficient information flow between these platforms. Enhance your productivity and collaboration across teams of all sizes by following this guide.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FASVDQPea4wMrFSisW9nM%2FAzure%20DevOps%20Jira%20Integration%20App.png?alt=media&#x26;token=448b36f1-9fc0-4f40-ac5d-c0e831c7bcfc" alt=""><figcaption><p><a href="https://marketplace.atlassian.com/apps/1223931/azure-devops-integration-for-jira-azure-devops-connector?hosting=cloud&#x26;tab=overview">Check out our Azure DevOps integration app on the Atlassian Marketplace</a></p></figcaption></figure>

#### Step-by-Step Setup Guide

**1. Access the Getint App in Jira**

Navigate to Jira, go to "Apps," and select "Jira - Azure DevOps Integration."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUb7y0bNix6nUKR2PPVx4%2Finstalling%20jira%20azure%20app.png?alt=media&#x26;token=6aa644a9-703e-4972-9d3b-e0d743e11a64" alt=""><figcaption></figcaption></figure>

**2. Create Integration**

* Choose "Continuous Sync" for ongoing data synchronization or "Migration" if you need to transfer existing data.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FauPLTmwoTx7ZzZdV3qG6%2FSelecting%20Continuos%20Sync%20or%20Migration.png?alt=media&#x26;token=cfb3998d-5690-48a5-9d70-6e2f4c361e74" alt=""><figcaption></figcaption></figure>

**3. Token Generation (Password for Jira Cloud)**

For Jira Cloud, generate a Jira token. This token will act as your password:

* Go to Atlassian Account Settings.
* Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkN1AECBGj6ezWCzEeJgt%2Fimage-20240812-171049.png?alt=media&#x26;token=d5eb3df0-41a2-4ba6-932a-365dfb742763" alt=""><figcaption></figcaption></figure>

**4. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance.
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fck3TsUWGgXbjMlm3Rq1R%2Fimage-20240715-151822%20(1).png?alt=media&#x26;token=4199e5bf-966e-401f-99ca-12c089753b75" alt=""><figcaption></figcaption></figure>

**5. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaLzTCzZZK2bSl5F1Zn17%2Fimage-20240620-170315%20(2)%20(1).png?alt=media&#x26;token=4628072c-0fa4-4410-9feb-b5a5fefa2855" alt=""><figcaption></figcaption></figure>

**6. Connect to Azure DevOps**

* Select the Azure DevOps app and tap on "Create a new connection." Use the Personal token created following the instructions in the guide: [Connections](https://docs.getint.io/guides/quickstart/connection#azure-devops).
* Tap on "Connect."
* Name the connection, input your email, and paste the token generated. Then click "Add."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRZktv7TnQ801tyYaJH2X%2Fimage-20240812-171756.png?alt=media&#x26;token=a4e80115-8f3e-4900-af99-4bfde8dff19f" alt=""><figcaption></figcaption></figure>

* Select the Azure DevOps connection and choose the database you want to synchronize.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXLeRynMnAO0OIaj3oO7A%2Fimage-20240812-171610.png?alt=media&#x26;token=7d851352-ce4a-40fc-9feb-43e3680f7e51" alt=""><figcaption></figcaption></figure>

**7. Map Types**

* Map the Jira issue types you want to sync with Azure DevOps tasks, such as mapping an Azure DevOps task to a Jira issue or a Jira bug.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBqjeeVDE6niPRQu1a1y4%2Fimage-20240812-172213.png?alt=media&#x26;token=02c3fa3e-3900-4f48-bc0a-12e4417ea69c" alt=""><figcaption></figcaption></figure>

* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process. Quick Build is currently in the beta stage; if you have feedback or questions about it, please contact our [support.](https://getintio.atlassian.net/servicedesk/customer/portals)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0wB95VbhZiq6LTFyyByM%2FUntitled%20design%20(25).jpg?alt=media&#x26;token=1808f599-ff84-4c6c-a720-b7a1966aea6e" alt=""><figcaption></figcaption></figure>

**8. Field Mapping**

Review or manually map which fields to integrate and sync within supported mapped types, make any necessary modifications, and hit apply.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlNNfeI3P5IWZ7ucyPi2i%2FUntitled%20design%20(24).jpg?alt=media&#x26;token=fb626577-0347-4a8c-8377-24ad17f7e785" alt=""><figcaption></figcaption></figure>

#### Advanced Settings <a href="#advanced-settings" id="advanced-settings"></a>

**9. Comments**

If needed, enable the integration and synchronization of comments.

* Filter the comments with the criteria that suit you. Make them private/public or use the preferred attributes, such as created date or author.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEm9fPbbacf4s4DTVK7rQ%2FCaptura%20de%20tela%202024-08-12%20143828.png?alt=media&#x26;token=7ba85ffc-4580-42cb-8a00-e80ccd2ce155" alt=""><figcaption></figcaption></figure>

**10. Statuses Mapping**

Enable status mapping, then map the statuses as desired.

* Specify the Azure DevOps field that will keep the status data from Jira, ensuring fields in Azure DevOps mirror your Jira setup (e.g., Done - Closed, Open - Active).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAsN0MViXkpbc9UTvk1mA%2Fimage-20240812-174143.png?alt=media&#x26;token=176df56f-eba5-4642-b227-c0ba1b930441" alt=""><figcaption></figcaption></figure>

#### **Finalize Integration**

**11. Name the Integration and Click "Create"**

* Name your integration and click "Create" to finalize the setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkREPm5UYV7kAcY78UPmj%2FUntitled%20design%20(26).jpg?alt=media&#x26;token=05ebe7e1-a328-40c8-8622-62779b9f489a" alt=""><figcaption></figcaption></figure>

**12. Filtering**

It is possible to filter the synchronization to have it customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0QFYm1XlWIqLz6XWo3Oj%2FUntitled%20design%20(27).jpg?alt=media&#x26;token=da0c4f07-cbd0-485b-a063-e8c464f09cc1" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option "New items" is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option "Synced items" is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you have created the filters and "Save" the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7o3MGnkJ4plqvEbR36Xi%2FUntitled%20design%20(28).jpg?alt=media&#x26;token=a62bf43b-3860-4058-95fc-af881818be4f" alt=""><figcaption></figcaption></figure>

**13. Test the Integration**

To ensure everything is working correctly, create tasks and go to the reporting section to verify that all syncs are functioning as expected. If you encounter any issues, please contact our [support team](https://getintio.atlassian.net/servicedesk/customer/portals) for assistance.

#### Conclusion <a href="#conclusion" id="conclusion"></a>

Leverage the Jira-Azure DevOps integration by Getint to optimize your project management and development processes. This seamless integration enhances collaboration and productivity, ensuring that all tasks and milestones are accurately tracked and managed across platforms. Please contact our [Support Team](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team), if you require further assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
