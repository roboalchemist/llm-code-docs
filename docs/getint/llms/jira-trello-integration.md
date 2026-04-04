# Source: https://docs.getint.io/guides/integration-synchronization/jira-trello-integration.md

# Jira Trello integration

Integrating Jira with Trello via Getint revolutionizes project management by combining detailed tracking with visual task management. This seamless integration works for Jira Cloud, Jira Data Center, Jira Software, and Jira Service Management. Our step-by-step guide will help you quickly set up the Jira-Trello connection, enhancing productivity and collaboration for your team. Transform your project management experience today.

### Step-by-Step Setup Guide <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

#### **0. Access the Getint App in Jira**

* Navigate to "Apps" and select "Integration for Jira - Trello."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fb8HeKpXorqEcVSc5s7LV%2Fimage-20240628-150153.png?alt=media&#x26;token=e638f224-2746-4069-80d7-eac35a62d415" alt=""><figcaption></figcaption></figure>

#### **1. Create Integration**

* Click "Create integration" for ongoing sync or "Migration" to transfer existing data: [Migration Guide.](https://docs.getint.io/guides/migration)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtBYpcOXKgHt6d5b558wJ%2Fimage-20240619-115231%20(2).png?alt=media&#x26;token=84eb0cf9-9909-455b-9e16-4bc331c0ea05" alt=""><figcaption></figcaption></figure>

#### **2. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtsxTENzoWRPEVY3WDjbt%2Fimage-20240628-150712.png?alt=media&#x26;token=41cdecd5-ac26-4971-abec-85a486f3ab51" alt=""><figcaption></figcaption></figure>

#### **3. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoB22bIX8YzzkEwTDtur7%2Fimage-20240620-165801%20(2).png?alt=media&#x26;token=fc8461e7-3b8c-4ed9-9ccb-7f87d4c73e8d" alt=""><figcaption></figcaption></figure>

#### **4. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FQIUXlyHnEeL0LZuxnIFo%2Fimage-20240620-170315%20(3).png?alt=media&#x26;token=8db3c53d-de39-4687-b6fa-0dbcfef92612" alt=""><figcaption></figcaption></figure>

#### **5. Connect to Trello**

* Select the Trello app authorize the app and allow Getint to connect with your Trello board on the popup screen that will appear.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FZ8tsKzdLtb9box44SYto%2Fimage-20240628-151651.png?alt=media&#x26;token=f086d1ce-dd9d-41a3-978d-9ad10e2ae91f" alt=""><figcaption></figcaption></figure>

* Select "Add" to start the integration.
* Choose the board that you want to integrate.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdGuzIupcLB7iiBiMhgpv%2Fimage-20240628-152006.png?alt=media&#x26;token=b0e24687-5b77-4ec7-a3aa-116d2b994972" alt=""><figcaption></figcaption></figure>

#### **6. Type Mapping**

* Map the Jira issue types you want to sync with Trello Cards, such as mapping a Trello card to a Jira task or a Jira bug.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaKFs3HHIn2naqAPODVC0%2Fimage-20240628-200542.png?alt=media&#x26;token=a7e47a61-6d7c-4588-9104-8967af4c5bf2" alt=""><figcaption></figcaption></figure>

* Consider using the "Quick Build" beta feature for automated type and field mapping, which can facilitate the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRrUFpyclvfntt3kAm1Oj%2FUntitled%20design%20(12)%20(2).jpg?alt=media&#x26;token=70f3f1ba-52e3-4570-a879-3edc1e42e6f6" alt=""><figcaption></figcaption></figure>

#### **7. Field Mapping**

* Review or manually map which fields to integrate and sync within supported mapped types.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2EDKhoqr6HXJmwQtE27D%2Fimage-20240628-201703.png?alt=media&#x26;token=b70c7ed4-dfea-4923-8e19-80503a0ac9db" alt=""><figcaption></figcaption></figure>

#### **8. Comments**

* If needed, enable the integration and synchronization of comments.
* Filter the comments with the criteria that suit you. Make them private/public or use the preferred attributes such as created date or author.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F1iIB9YbnTX2bs8jS6czM%2Fimage-20240628-201754.png?alt=media&#x26;token=e77e4c77-0d9c-4417-b803-bf3db4ee85e5" alt=""><figcaption></figcaption></figure>

#### **9. Finalize Integration**

* Name your project and click "Create" to finalize the integration setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F56Y8FFSMAjHWydrHFPaH%2FUntitled%20design%20(13).jpg?alt=media&#x26;token=5b1b8ce1-4062-40f4-b9eb-780e00584e92" alt=""><figcaption></figcaption></figure>

#### **10. Filtering:**

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FwtcY0sfIs69CBal8dKQZ%2FScreenshot%20from%20June%2028%2C%202024%2C%205_21%20PM.png?alt=media&#x26;token=0e244782-f898-45d8-b22c-c6d287b0ea9d" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and “Save” the integration.

#### **11. Test the integration**

To ensure everything is working correctly, create tasks and go to the reporting section to verify that all syncs are functioning as expected. If you encounter any issues, don't hesitate to contact our support team for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzsaMrqpYC0H8d39VdpaG%2Fimage-20240710-094940%20(1).png?alt=media&#x26;token=72049f3a-18a5-4c64-89f2-ac3c7603cae8" alt=""><figcaption></figcaption></figure>

### Conclusion

Following these steps, you can effectively integrate Jira with Trello, ensuring smooth synchronization of tasks, issues, and workflows between the two platforms. This setup enhances collaboration and project management processes.

For further assistance contact our support at <https://getint.io/help-center>.
