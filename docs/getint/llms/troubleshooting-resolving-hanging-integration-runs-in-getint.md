# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users/troubleshooting-resolving-hanging-integration-runs-in-getint.md

# Troubleshooting: Resolving Hanging Integration Runs in Getint

In the complex world of system integrations, ensuring seamless data synchronization is crucial for maintaining workflow efficiency. However, integration runs can sometimes hang or fail when dealing with large-scale data transfers, disrupting the process. This guide provides a clear solution to tackle such issues in Getint, helping you restore smooth operations quickly and effectively.

#### Understanding the Issue <a href="#understanding-the-issue" id="understanding-the-issue"></a>

When an integration run encounters a significant issue—such as an attempt to sync a large volume of items at once (e.g., 10.000 or more)—the process may hang or fail to complete. In these scenarios, Getint will continuously attempt to sync from where it last stopped, potentially leading to delays or persistent failures.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FzzcdgwLxKpBDmvgkDksF%2FScreenshot%20from%20August%2015%2C%202024%2C%205_40%20PM.png?alt=media&#x26;token=3a14d4af-dcf6-4af1-b793-dcfa1cd3c75f" alt=""><figcaption></figcaption></figure>

### How to Resolve Hanging Integration Runs <a href="#how-to-resolve-hanging-integration-runs" id="how-to-resolve-hanging-integration-runs"></a>

To address this issue and restore normal operation, follow these steps:

#### **1. Disable the Affected Integration**

First, temporarily disable the integration that is encountering the issue.

* Navigate to the specific integration within the Getint app.
* Select the integration and choose the option to disable it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoYxHiv0z3CsDUavGNzhZ%2FUntitled%20design%20(29).jpg?alt=media&#x26;token=6d7e1649-d78e-4be6-9b51-52a7e98b226c" alt=""><figcaption></figcaption></figure>

#### **2. Correct the Underlying Issue**

Identify and resolve the root cause of the problem if possible:

* Review the logs or error messages to determine what caused the integration to hang.
* Address any data inconsistencies, connection issues, or other errors that may have triggered the failure.

#### **3. Duplicate the Integration**

Once the issue is corrected, duplicate the integration to reset its process.

* Go to the integration settings, click on the three dots on the right, and choose the option to duplicate the integration.
* Name the duplicated integration and select “create.”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAAPSPXy0cHHWJkYyD7aP%2FUntitled%20design%20(2).png?alt=media&#x26;token=5319fea0-b473-4664-8ea9-0cff613125fb" alt=""><figcaption></figcaption></figure>

#### **4. Enable the New Integration**

Activate the duplicated integration to start a fresh sync process.

* Once enabled, Getint will begin syncing from the start, effectively bypassing the previous hang-up.
* The system will look for new issues to sync, ensuring a clean and uninterrupted process.

### Conclusion <a href="#conclusion" id="conclusion"></a>

By following these steps, you can effectively resolve hanging integration runs in Getint, ensuring that your sync processes are back on track. If you encounter any further issues or require additional assistance, please don't hesitate to contact our [support team](https://getint.io/help-center).

Keep your integrations running smoothly and maintain the seamless flow of data across your platforms with Getint.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
