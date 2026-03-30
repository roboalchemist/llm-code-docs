# Source: https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint/filtering-by-assignment-group-and-status.md

# Filtering by Assignment Group and Status

When integrating different platforms with Jira, Azure DevOps, ServiceNow, or other tools, it's often necessary to filter issues based on specific criteria such as assignment groups and statuses. This guide will walk you through the steps to set up filtering by assignment group and status within your Getint integration, ensuring that only the relevant issues are synchronized between systems.

### Introduction <a href="#introduction" id="introduction"></a>

Efficient issue management requires precise control over the flow of information between integrated systems. Filtering by assignment group and status allows you to streamline this process, ensuring that only the necessary issues are synchronized according to your workflow needs. In this guide, we will focus on configuring these filters within your Getint integration, using a common use case: filtering by assignment group and status for ServiceNow, particularly in the context of a Jira-ServiceNow integration.

By filtering issues based on assignment group and status, you can ensure that only relevant tickets are synced between Jira and ServiceNow, reducing noise and improving the efficiency of your teams. Whether you're managing IT service requests or software development tasks, these filters will help tailor the integration to suit your specific workflow requirements.

### Step-by-Step Guide to Filtering by Assignment Group and Status <a href="#step-by-step-guide-to-filtering-by-assignment-group-and-status" id="step-by-step-guide-to-filtering-by-assignment-group-and-status"></a>

#### **1. Navigate to Filtering Options**

* Within the integration setup, locate the filtering options by clicking on the filtering icon near the app icon.
* This will allow you to apply specific filters to the issues being synchronized.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkmLing68AUN85RqjJDUJ%2FServiceNow%20assignment%20group.jpg?alt=media&#x26;token=0861b8db-3c22-4f6e-8d7f-ca72c5aeedb2" alt=""><figcaption></figcaption></figure>

#### **2. Set Up Filtering by Assignment Group**

**Field Selection:**

In the filtering options, select the "Field" dropdown and choose "Assignment Group" (or the equivalent field in your integrated tool) from the list.

* Choose the appropriate operator, such as "Contains," depending on your needs.
  * Enter the name of the assignment group(s) by which you want to filter. You can filter by multiple groups by adding additional values.
  * Click "Apply" to implement the assignment group filter in your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVfZGEcmC7xJVCGU1ksgA%2FSelecting%20the%20filtering%20options.png?alt=media&#x26;token=88629da6-4ea0-431c-a159-7837f7c05401" alt=""><figcaption></figcaption></figure>

#### **3. Set Up Filtering by Status**

**Field Selection:**

In the filtering options, select the "Field" dropdown and choose "Status" from the list.

* Choose the appropriate operator, such as "Contains" depending on the statuses you wish to filter by.
  * Enter the specific status or statuses by which you want to filter. Multiple statuses can be added by entering them in separate value fields.
  * Click "Apply" to implement the status filter in your integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FYj1cORfTjodrpU6xtSQX%2FOther%20filtering%20options.jpg?alt=media&#x26;token=6bbb15eb-8886-4f00-8d6a-7cab2426fe21" alt=""><figcaption></figcaption></figure>

#### **4. Combine Filters for Precise Control**

* **Multiple Filters:**
  * You can combine filters by adding assignment groups and status filters within the same integration. This ensures that only issues assigned to specific groups and in specific statuses are synchronized. For example, you can filter issues that belong to a particular assignment group AND are in a specific status.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIK2GAvmLFWnl4RnixsQv%2FCombine%20filters.png?alt=media&#x26;token=c90cb724-95c3-448e-846f-b2106d20165e" alt=""><figcaption></figcaption></figure>

#### **5. Save and Test Your Filters**

* **Save Integration:**
  * Once you have configured your filters, click "Save" to apply them to your integration.
* **Test the Setup:**
  * Create test issues or use existing ones to verify that the filtering works as expected. Only issues that match your filter criteria should be synchronized between systems.

### Conclusion <a href="#conclusion" id="conclusion"></a>

Filtering by assignment group and status within your integration allows you to control precisely which issues are synchronized across platforms. This functionality is essential for ensuring that your teams only receive relevant information, thus optimizing workflow efficiency and reducing clutter. Following this guide, you can easily configure these filters to match your business needs across all integrated tools.

For further assistance or feedback, visit our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
