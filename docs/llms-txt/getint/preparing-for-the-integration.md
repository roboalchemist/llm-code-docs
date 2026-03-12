# Source: https://docs.getint.io/getting-started-with-the-platform/preparing-for-the-integration.md

# Preparing for the Integration

### **Setting Up Service Accounts**

Before initiating an integration with Getint, one critical step is to prepare and set up Service Accounts in the systems you plan to integrate. Service Accounts act as the bridge through which Getint accesses and synchronizes data between different platforms. Here’s a guide on how to effectively prepare these accounts:

#### Choose the Right Account Type

* Opt for dedicated Service Accounts rather than personal user accounts. Service Accounts are designed to facilitate automated processes and integrations, ensuring uninterrupted service and more controlled access.
* Comments are added as the user you chose to create the connection. Therefore, we recommend using a dedicated Service Account for this purpose. While there is no technical possibility of adding comments as the original authors, you can still map the assignees. However, issues, incidents, and tasks will be created, and comments will be attributed to the user who established the connection.

{% hint style="info" %}
Example of a comment that was synced with Getint: **`[Author: Radek, Created on: 2024-08-12T12:53:21.711+0000] [Origin: DEMO-346, Comment ID: 26888].`**

Although comments are still attributed to the integration account, the footer includes additional details such as the original author, creation date, the task that triggered the comment, and the comment ID. It’s an industry standard to add comments as one, the default user, but Getint adds the information about the original commenter and the original date of the comment in the footer, which is not an industry standard.
{% endhint %}

### How to Create a Jira Service Account <a href="#how-to-create-a-jira-service-account" id="how-to-create-a-jira-service-account"></a>

Atlassian now provides native Service Accounts that are ideal for integrations like Getint. These accounts do not consume a standard user license and are purpose-built for API interactions.

#### Why use a Service Account? <a href="#why-use-a-service-account" id="why-use-a-service-account"></a>

* **Security**: Avoid sharing personal login credentials.
* **Continuity**: Integrations won't break when individual passwords change or when users are deactivated.
* **Audit Trails**: Easily distinguish between actions performed by company users and those performed by Getint.
* **Permission Control**: Only grant the specific access required for the integration.

#### Creating a Service Account

To begin, you need to define the account within your Atlassian Organization.

1. Log in to **admin.atlassian.com**.
2. Select your **Organization** from the list.
3. Navigate to **Directory** > **Service accounts**.
4. Click **Create service account**.
5. Enter a **Name** (for example, `Getint-Sync-Bot`) and an optional **Description**.
6. Select the **user** role for the service account in Jira.
7. Click **Create**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAmNLl2yF4CsedMe7NFGq%2FUser%20role%20for%20service%20account.png?alt=media&#x26;token=adb708e3-6082-445c-ba91-1da6e7a84ca8" alt=""><figcaption></figcaption></figure>

#### Generate Authentication Credentials

Service accounts cannot log in via a browser UI. You must use an **API Token** with classic or granular scopes.

{% hint style="warning" %}
**OAuth 2.0** isn't supported yet.
{% endhint %}

**Creating an API Token**

1. Go to **Directory** > **Service accounts** and select your account.
2. Click **More actions** (•••) > **Create credentials**.
3. Select **API token** and click **Next**.
4. **Name your token**: Use something descriptive like `Production-Sync-Token`.
5. **Set Scopes**: To know the necessary permissions to connect with Getint, please click [here](https://docs.getint.io/guides/quickstart/connection#forge-apps-onpremise-scoped-tokens).
6. **Set Expiration**: Choose a duration (1–365 days) that aligns with your security policy.
7. **Copy & Save**: Copy the token immediately. You will not be able to see it again.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTt9HVz6RnfoVitvH1F76%2FAPI%20token%20for%20the%20service%20account.png?alt=media&#x26;token=1984213d-9ed2-4d78-8baa-a35f708b323e" alt=""><figcaption></figcaption></figure>

Your service account is now ready for use with Getint.

#### Document and Maintain

* Keep a record of the Service Accounts you've created for integration purposes. Document their purpose, associated systems, and any relevant details.
* Regularly review and maintain these accounts. Update credentials periodically and ensure they’re in line with your organization's security policies.

#### Test the Accounts

* Before finalizing the integration setup, test the Service Accounts to ensure they have the appropriate level of access and can perform all intended functions successfully.

If you're setting up a service account to synchronize Jira with tools like Azure DevOps, ServiceNow, Asana, and so on, check out our [Integration Guides](https://docs.getint.io/guides/integration-synchronization) or reach out to our [Getint support team](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
