# Source: https://docs.getint.io/guides/integration-synchronization/jira-gitlab.md

# Jira GitLab integration

### **Introduction**

Integrating Jira with GitLab enables seamless synchronization between project management and version control, enhancing collaboration and workflow efficiency. Follow this comprehensive guide to set up a two-way integration between Jira and GitLab quickly and easily.

### Step-by-Step Setup Guide <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

#### **0. Access the Getint App in Jira**

* Navigate to "Apps" and select “Jira - GitLab Integration”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fk4lt3ZVafvd38ZWsu72X%2Fimage-20240617-154412.png?alt=media&#x26;token=7d1b0094-0a2b-4ee9-aeba-c963ccfa7a16" alt=""><figcaption></figcaption></figure>

#### **1. Create Integration**

* Click "Create integration” or “Migration”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJebLOxMpqGdg4Ml4R4U4%2Fimage-20240619-115231.png?alt=media&#x26;token=040467a0-212f-46a1-84d8-b731d80d3575" alt=""><figcaption></figcaption></figure>

#### **2. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAjTYyEg7wJ0rOH9rn06Y%2FScreenshot%202024-06-19%20085658.png?alt=media&#x26;token=5b480230-999b-489b-94a0-7814884fb944" alt=""><figcaption></figcaption></figure>

#### **3. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click on "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjP3Zl01xPNTvzaasBNCG%2Fimage-20240620-165801.png?alt=media&#x26;token=71153fff-310f-4239-88b1-c2ae62827052" alt=""><figcaption></figcaption></figure>

#### **4. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FloMoKloeDsLHZVf6CKeU%2Fimage-20240620-170315.png?alt=media&#x26;token=78f729d4-4905-4cd4-abec-39335d2b22bf" alt=""><figcaption></figcaption></figure>

#### **5. Generate GitLab Token**

* Go to the GitLab developer console and generate a token. This token will serve as the password for the integration. Follow the steps [here](https://docs.getint.io/guides/quickstart/connection#gitlab) for the token with the correct permissions.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtLKPmpuDjisXuwSTZ4LJ%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=9714219f-de96-40b9-9041-7d7f17cb8e3d" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

#### **6. Connect to GitLab**

* If no connection is established yet, create a new one.
* Use the GitLab token generated as a password.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUY4eFKXWqewsRxwmS58g%2Fimage-20240620-171013.png?alt=media&#x26;token=4f0b1155-a521-4852-84a2-25c8011e33a3" alt=""><figcaption></figcaption></figure>

#### **7. Select the Connection and Project**

* Select the established GitLab connection and choose the project you want to integrate with.

#### **8. Type Mapping**

* Map the Jira issue types you want to sync with GitLab issues, such as mapping a GitLab issue to a Jira task or a Jira bug to a GitLab issue.
* Consider using the "Quick Build" beta feature for automated type and field mapping, which can streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJNK7Uf5to7oNvXBYFqBb%2Fimage-20240621-101521.png?alt=media&#x26;token=61d252c2-1f2b-42a7-b19e-e27544a37614" alt=""><figcaption></figcaption></figure>

#### **9. Field Mapping**

* Review or manually map which fields to integrate and sync within the mapped types, including title, description, assignees, custom fields, and more.

#### **10. Assignee Mapping**

* Map and match assignees according to your desired configuration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlNhgQ78GwibAqwZ1JQJk%2Fimage-20240620-171902.png?alt=media&#x26;token=ff68dd4b-9f8e-44f4-a6b6-131e2a4ce89d" alt=""><figcaption></figcaption></figure>

#### **11. Comments**

* If needed, enable the integration and synchronization of comments.
* Filter the comments with the criteria that suit you. Make them private/public or use the preferred attributes such as created date or author.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYrl9lfjW3wXBIeDU4vt4%2Fimage-20240621-102606.png?alt=media&#x26;token=61aa9388-80c9-4ae4-b060-701494ba92df" alt=""><figcaption></figcaption></figure>

#### **12. Finalize Integration**

* Name your project and click "Create" to finalize the integration setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMbNyYKcJ2eJ6Uy63USCO%2Fimage-20240621-102709.png?alt=media&#x26;token=4870a7ae-2972-49dc-9ea7-7fb48b2b6956" alt=""><figcaption></figcaption></figure>

#### **13. Filtering:**

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3bYZlY7VvCQe8BQB1zkX%2Fimage-20240621-102751.png?alt=media&#x26;token=3dd7f8a0-3175-4f62-ad5a-dd653a4c109f" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option “*New items”* is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option “*Synced items”* is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and Save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjKfXYFdXfIbBThJjorZ4%2Fimage-20240621-102849.png?alt=media&#x26;token=8010f270-b7ab-4938-a6f8-f94011f041d2" alt=""><figcaption></figcaption></figure>

### Conclusion <a href="#conclusion" id="conclusion"></a>

Following these steps, you can effectively integrate Jira with GitLab, ensuring smooth synchronization of tasks, issues, and workflows between the two platforms. This setup enhances collaboration and streamlines project management processes.

For further assistance, please contact us at the [Support Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCQdON7rk1lCKReSQtp9W%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=e240ec28-3056-42c7-968c-c66de763b0d5" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
