# Source: https://docs.getint.io/getintio-platform/request-type-issue-on-jira-service-management-how-to-select-and-work-with-it.md

# Request Type Issue on Jira Service Management - How to Select and Work with It

### Introduction <a href="#introduction" id="introduction"></a>

When integrating with Jira Service Management (JSM) through Getint, users often encounter the additional complexity of request types, which differ from standard issue types in Jira Software. This guide will walk you through the process of mapping request types in JSM to ensure smooth integration and synchronization with other tools like Freshdesk.

### Understanding Request Types <a href="#understanding-request-types" id="understanding-request-types"></a>

In Jira Service Management, request types are specific categories of issues that users can raise, such as "IT Help," "Service Request," or "Incident." These request types are very often mistaken with issue types and are not directly available for mapping in the type mapping section of Getint, which can lead to confusion.

### Step-by-Step Guide to Mapping Request Types <a href="#step-by-step-guide-to-mapping-request-types" id="step-by-step-guide-to-mapping-request-types"></a>

#### **Example Scenario: Mapping "Service Request" to "Incident" and Filtering "Emailed Request"**

#### **1. Map the Issue Types:**

* Map "Service Request" in Jira to "Incident" in Freshdesk.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4UJpj3eQo4Ww8d24b5Ya%2Fimage-20240801-164813%20(1).png?alt=media&#x26;token=3ce2ac8a-5ea8-43da-bf8c-22f3866b5ab6" alt=""><figcaption></figcaption></figure>

#### **2. Type Mapping:**

* Map the issue types as usual. For example, map "Service Request" in JSM to "Incidents" in Freshdesk.
* Ensure all fields are correctly mapped between the two platforms.

#### **3. Set Up Filters:**

* In the filter settings, set the request type field to "contains" and the value to "Emailed Request."
* Set up the filter:
  * Field: Request type
  * Operator: Contains
  * Value: "Emailed Request"

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fox93Ps3Lksbs6Gce1M3I%2FUntitled%20design%20(22).jpg?alt=media&#x26;token=43080e8f-a263-4312-8748-3e63d234621c" alt=""><figcaption></figcaption></figure>

#### **4. Map Request Type Field:**

Once you have set up the filter, you can define how this request type will be handled by the integration. For instance, if you are integrating with Freshdesk and want incidents in Freshdesk to create "Emailed Requests" in Jira Service Management:

* Add field mappings for the request type.
* Select the app, then Jira, then request type, and map it to a fixed value, such as "Emailed Request."

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjECU9OuPIn4T04NdeQ5g%2FUntitled%20design%20(23).jpg?alt=media&#x26;token=29c5efd9-02db-4dfa-895a-f50f9894c210" alt=""><figcaption></figcaption></figure>

### What Happens After Mapping Request Types? <a href="#what-happens-after-mapping-request-types" id="what-happens-after-mapping-request-types"></a>

After completing the request type mapping, the integration will handle data as follows:

* **Issue Creation:** When a new issue is created in the integrated tool (e.g., Freshdesk), the integration will recognize the mapped issue type and request type. It will then create the corresponding issue in Jira Service Management, ensuring that the correct request type (e.g., "Emailed Request") is applied.
* **Field Synchronization:** All mapped fields, including the request type, will be synchronized according to the integration settings. This ensures that any updates to the issue in one platform are reflected in the other, maintaining consistency.
* **Filtering and Customization:** By setting up filters, such as the "Request Type" filter, you can customize which specific types of requests are synchronized. This allows for a more tailored integration that meets the unique needs of your workflow.

### Advanced Configuration <a href="#advanced-configuration" id="advanced-configuration"></a>

For more complex scenarios, such as controlling the request type from other integrated tools, you can use dropdown fields to map request types dynamically.

1. **Create a Dropdown Field:**
   * In the external tool (e.g., Freshdesk), create a dropdown field with options that correspond to Jira request types.
2. **Map Dropdown to Request Type:**
   * In Getint, map the dropdown field to the request type field in Jira. This allows the integration to dynamically set the correct request type based on the dropdown selection.

### Best Practices <a href="#best-practices" id="best-practices"></a>

* **Consistent Naming:** Ensure request types and their corresponding fields have consistent names across platforms.
* **Test Configurations:** Test the mappings and filters in a sandbox environment before deploying them in a live setting.
* **Documentation:** Document the mappings and configurations to ensure all team members understand how request types are managed.

### Conclusion <a href="#conclusion" id="conclusion"></a>

Integrating request types in Jira Service Management with other tools can be complex, but by following this guide, you can ensure accurate and efficient synchronization. For additional support or to provide feedback, don't hesitate to get in touch with our [support team](https://getint.io/help-center).

#### Related Resources <a href="#related-resources" id="related-resources"></a>

* [How to Access the App](https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app)
* [How to Build the Integration](https://docs.getint.io/guides/integration-synchronization)
* [How to Connect the Apps](https://docs.getint.io/guides/quickstart/connection)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
