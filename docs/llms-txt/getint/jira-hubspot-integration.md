# Source: https://docs.getint.io/guides/integration-synchronization/jira-hubspot-integration.md

# Jira HubSpot integration

In today's fast-paced business environment, integrating your project management tools with customer relationship management platforms is essential for maintaining seamless operations and maximizing efficiency. Getint's Jira-Hubspot integration brings together the robust issue-tracking capabilities of Jira with the dynamic CRM functionalities of Hubspot, ensuring a continuous flow of information and enhanced collaboration across your teams. Whether you're looking to set up a two-way or a one-way integration, this comprehensive guide will help you establish a streamlined connection, boosting productivity and facilitating superior project management.

### Step-by-Step Setup Guide <a href="#step-by-step-setup-guide" id="step-by-step-setup-guide"></a>

#### **1. Access the Getint App in Jira**

Navigate to "Apps" and select "Hubspot Integration for Jira"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fcp5p3qIfViyQ9m4A0TOD%2Fimage-20240715-150006.png?alt=media&#x26;token=3fa786ac-d84d-4c9b-8a23-f32ed079e9cc" alt=""><figcaption></figcaption></figure>

#### **2. Create Integration**

Click "Create integration" for ongoing sync or "Migration" to transfer existing data: [Migration Guide](https://docs.getint.io/guides/migration).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0RATyPkExYUKG6XXqR5h%2Fimage-20240715-150119.png?alt=media&#x26;token=ef99b370-2b18-48b7-b2e2-97ae28ff1aa4" alt=""><figcaption></figcaption></figure>

#### **3. Token Generation (Password for Jira Cloud)**

For Jira Cloud, generate a Jira token. This token will act as your password:

* Go to Atlassian Account Settings.
* Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fdey3IkQg3fWUG0rcMdpI%2Ff8193fbb-47b9-4cde-951d-924dc076abf4.png?alt=media&#x26;token=f7aab8d5-8244-4a7d-a763-722f50af3882" alt=""><figcaption></figcaption></figure>

#### **4. Choose the Apps and Establish Connections**

* Ensure you are logged in as a user with admin rights, click "Select App" and choose Jira.
* Select "Create New" to establish a new connection with your Jira instance and add the URL of your Jira instance (omit the trailing "/").
* Enter the login credentials of the admin user.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvsH3IQXotbjlDAVnPzBD%2Fimage-20240715-151822.png?alt=media&#x26;token=eb22713c-f3b3-46b3-b541-6b62a273955d" alt=""><figcaption></figcaption></figure>

#### **5. Select the Jira Project**

* Once the connection is established, choose the Jira project you want to connect to from the dropdown menu.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FR4qXw1mhnjBlraSm7nzS%2Fimage-20240620-170315%20(2).png?alt=media&#x26;token=9643bad6-2677-4687-9773-dbcdd9971ebc" alt=""><figcaption></figcaption></figure>

#### **6. Connect to Hubspot**

* Select the Hubspot app and tap on "Create a new connection" Use the Personal token created following the instructions in the guide: [Connections](https://docs.getint.io/guides/quickstart/connection#hubspot)
* Tap on "Connect"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhxVhwLkrkxmxLGGIsGbW%2Fimage-20240715-170006.png?alt=media&#x26;token=3d9d65ac-32eb-4854-9df0-0a9c3bc10629" alt=""><figcaption></figcaption></figure>

#### **7. Type Mapping**

Map the Jira issue types you want to sync with Hubspot tasks, such as mapping a Hubspot task to a Jira issue or a Jira bug.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FaBmgEircnMjbgKxPCvZA%2FScreenshot%20from%20July%2015%2C%202024%2C%202_02%20PM3.png?alt=media&#x26;token=6a07cc71-971b-465a-bdd8-2702e2a7c608" alt=""><figcaption></figcaption></figure>

Consider using the "Quick Build" beta feature for automated type and field mapping, which can facilitate the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FR1p8EfdfeV8OgJ8jFQk2%2FUntitled%20design%20(15).jpg?alt=media&#x26;token=dbb86e56-2c19-4ca1-a328-ffe250554479" alt=""><figcaption></figcaption></figure>

#### **8. Field Mapping**

Review or manually map which fields to integrate and sync within supported mapped types, make any necessary modifications, and hit apply

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7tBSpT20NC8HeqRQ9IoQ%2FScreenshot%20from%20July%2015%2C%202024%2C%202_01%20PM2.png?alt=media&#x26;token=9920d8fe-8b2a-438c-8a40-2729d0859daf" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
To keep your tickets syncing correctly, you MUST map the "Ticket Status" field to a fixed value called "New," just like in the picture above. This lets Jira send new and updated tickets over to HubSpot without any issues. If you don’t do this, you’ll run into a sync error when Jira tries to share data with HubSpot.

The Quick Build feature will add this field mapping by default, but you can also add it manually by selecting Add Field Mapping > HubSpot > Ticket Status > Fixed Value and entering the status for newly created tickets. For most customers, this value is "New," but you can use your status, such as "Open" or "To Do." In these cases, simply enter the corresponding value. For example, map the "Ticket Status" field to the fixed value "To Do."
{% endhint %}

Getint now supports the Satisfaction field in Jira, enabling seamless synchronization and integration of satisfaction ratings across platforms. This new feature ensures that customer feedback and satisfaction metrics are consistently tracked and managed within your Jira projects. This enhancement reflects Getint’s dedication to offering comprehensive and adaptable integration solutions that cater to evolving user needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEzSd5P5UixJjgDNLj8xR%2FAdded%20support%20for%20the%20Satisfaction%20field%20in%20JSM.png?alt=media&#x26;token=93d9af51-52d1-4b74-b3e2-0ff689dd851b" alt=""><figcaption><p>An example of how the Satisfaction field is located in Jira Service Management</p></figcaption></figure>

The Satisfaction field, located in Jira Service Management, can be utilized to track customer feedback in your Jira-HubSpot integration, enhancing your ability to monitor and improve customer satisfaction.

{% hint style="info" %}
If you need custom development or are trying to sync a field that isn't supported, please reach out to our [Service Center](https://getint.io/help-center) or [Schedule a Demo Call](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).
{% endhint %}

### Advanced Settings

#### **9. Comments**

If needed, enable the integration and synchronization of comments.

* Filter the comments with criteria that suit you. Make them private/public or use the preferred attributes such as created date or author.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMT0Oc5nlORciom2L5Xrv%2Fimage-20240715-171122.png?alt=media&#x26;token=15216bda-14b6-448f-aa58-dc6dd2bd38d1" alt=""><figcaption></figcaption></figure>

#### **10. Statuses Mapping**

Enable status mapping, then map the statuses as desired.

* Specify the Hubspot field that will keep the status data from Jira, ensuring fields in Hubspot mirror your Jira setup (e.g., To do - To do, Done - Done).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsZHxtIF6OPs5T94pkO8J%2Fimage-20240715-171606.png?alt=media&#x26;token=b754240c-40b9-4ea6-a576-c476e36da756" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**Note:** In HubSpot, each mapped type has a different status field. For example, a Deal maps to Stage, while a Ticket maps to Ticket Status. Identify the correct field for the mapped type to ensure the status transition syncs properly.
{% endhint %}

### Finalize Integration

#### **11. Name the Integration and Click "Create"**

Name your integration and click "Create" to finalize the setup.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUtlQZJyUPDsnALAFvQvB%2FUntitled%20design%20(16).jpg?alt=media&#x26;token=0fbbeb60-3810-4f33-b3fe-d7bd53fa460a" alt=""><figcaption></figcaption></figure>

#### **12. Filtering**

It is possible to filter the synchronization to have them customized for your needs and requirements.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.
* Select if the filtering applies to All, New, and Synced items.
* Note that if the option "New items" is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option "Synced items" is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select Apply once you created the filters and "Save" the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fj33hBBJYnNxJdE34Qsu4%2Fimage-20240715-172050.png?alt=media&#x26;token=b0bc8f18-c5e1-4d1d-8517-3b883073ce80" alt=""><figcaption></figcaption></figure>

#### **13. Test the Integration**

To ensure everything is working correctly, create tasks and go to the reporting section to verify that all syncs are functioning as expected. If you encounter any issues, please contact our support team for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVUbYKO22D4G6Io0Bt5XF%2Fimage-20240710-094940.png?alt=media&#x26;token=4e9bb60e-eae8-4159-a740-9884295928cf" alt=""><figcaption></figcaption></figure>

### Conclusion

Following these steps, you can effectively integrate Jira with Hubspot, ensuring smooth synchronization of tasks, issues, and workflows between the two platforms. This setup enhances collaboration and project management processes.

For further assistance contact our support at our [Support Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxYEVeDT7MBYDFKg2E56t%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=8db51c7a-b35c-415a-a93c-e2bfb73fb16b" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
