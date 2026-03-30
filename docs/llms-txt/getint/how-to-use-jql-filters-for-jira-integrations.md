# Source: https://docs.getint.io/getintio-platform/workflows/how-to-use-jql-filters-for-jira-integrations.md

# How to Use JQL Filters for Jira Integrations

In this guide, we will explore how to use Jira Query Language (JQL) filters to enhance and customize integrations with Jira. JQL is a powerful tool that helps build structured queries for better data management and synchronization between tools. By leveraging JQL, you can create highly specific queries that help streamline the flow of information between integrated systems, ensuring that only the most relevant issues are synchronized according to your workflow needs.

However, JQL is just one of the filtering options available. We encourage users to also explore the filtering capabilities provided through the Getint user interface (UI). In this guide, we'll explain how to use JQL for filtering, compare it to UI-based filtering, and discuss how Getint approaches these filtering methods.

### **What is JQL?**

Jira Query Language (JQL) is a flexible query language used to search for issues in Jira. It allows you to build custom queries using fields, operators, keywords, and functions, which helps filter the right data to be synced during integrations. This advanced search capability is handy for large projects or teams with complex workflows.

#### **Why Use JQL for Integrations?**

* **Enhanced control:** By applying JQL filters, you can sync only the relevant issues between Jira and other platforms.
* **Custom synchronization:** JQL filters allow you to create conditions such as syncing by assignee, status, due date, priority, or any custom fields.
* **Improved efficiency:** Filtering reduces data fetching and decreases processing time by applying conditions, such as JQL filters, on the Jira REST API side, instead of fetching a broader range of results and filtering them with UI filters (link here) by Getint., speeds up syncs, and minimizes potential errors.

#### **Setting Up JQL Filters for Integration**

Here’s how you can set up a JQL filter for your Jira integration:

1. **Navigate to the Integration Setup:**
   * Open the Getint app.
   * Go to the **Workflows** section, and locate the integration you want to configure.
2. **Access JQL Filters:**
   * Once you’ve selected your integration, select the **Jira** app.
   * Look for the **Custom JQL Filter** field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRYWCaggfF0ZjM1uEGb3z%2FCustom%20JQL%20filter.png?alt=media&#x26;token=f028ce8d-f889-409e-b445-a229c6db831d" alt=""><figcaption></figcaption></figure>

1. **Writing Your JQL Query:**

* In the JQL filter field, you can define specific criteria for your integration. Here are some common JQL queries you might use:
* **Filter by Status:**

  `status = "In Progress"`

  This query will sync only the issues that are currently marked as “In Progress”.
* **Filter by Assignee:**

  `assignee = "jsmith"`

  This query will sync issues assigned to the user `jsmith`.
* **Filter by Priority:**

  `priority = "High"`

  This query will sync only the issues with high priority.
* **Combine Multiple Conditions:** You can combine conditions using operators like `AND`, `OR`, and parentheses:

  `project = "PROJ" AND status = "In Progress" AND assignee = currentUser()`

  This query will sync only the issues from the project "PROJ", which are in progress and assigned to the currently logged-in user.

1. **Apply the Filter:**

* Once you have written the JQL query, click **Close** and Save the integration to activate the filter.
* The integration will now sync only the issues that match your JQL query.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FE0XIe7q05VC5KGv1SB5X%2FAplying%20JQL%20filters.png?alt=media&#x26;token=51028fe9-ccd7-471d-94fc-f3eb39d7b172" alt=""><figcaption></figcaption></figure>

#### **Examples of Advanced JQL Queries for Integrations**

* **Sync by Custom Field:**

  `customField_12345 = "Critical"`

  Sync issues where the custom field with ID `12345` has a value of "Critical".
* **Filter by Date Range:**

  `created >= "2024/01/01" AND created <= "2024/12/31"`

  Sync only issues created within the year 2023.
* **Issues with Open Pull Requests:**

  `development[pullrequests].open > 0`

  Sync only issues that have open pull requests linked to them.

#### **Best Practices for JQL Filtering**

* **Keep queries simple** to avoid performance bottlenecks.
* **Test your JQL query** in Jira’s advanced search feature before applying it to an integration.
* **Use specific criteria** to narrow down the number of issues synced. This reduces load and speeds up synchronization.
* **Avoid unnecessary complexity** by using common fields like status, assignee, and priority for the most relevant filtering.

#### **Limitations**

* **Text fields** like Summary or Description may require special operators like `~` for partial matches (e.g., `summary ~ "error"`).
* **Reserved words** and special characters may require additional syntax such as quotation marks.

#### **Verifying Your JQL**

To ensure your JQL query is correctly scoping to the tickets you want, you can take the JQL and test it directly in Jira. This allows you to see the exact issues that match your query before applying it to your Getint integration. By doing this, you can be confident that your query will return the desired results when used to filter issues during synchronization.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtiOgzxXthQuQNSUB7VRY%2FVerifying%20your%20JQL.png?alt=media&#x26;token=38cc0b02-a630-4e83-a619-18ef94adb364" alt=""><figcaption></figcaption></figure>

#### **Automatic Addition of Project and Issue Types**

One of the conveniences provided by Getint is that project and issue types are automatically added to your query. This means that when you create a JQL filter within Getint, you don't need to manually include these elements in your query—they are automatically appended, ensuring that your filters are scoped correctly to the relevant projects and issue types.

#### **UI-Based Filtering**

While JQL offers a high degree of customization, Getint also provides a user-friendly interface for filtering issues. The UI-based filtering option allows you to select filters through dropdown menus and checkboxes, making it accessible for users who may not be familiar with JQL syntax. This method is ideal for quick setups and less complex filtering needs.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsUk5ZcB3Ajqj3jNzYkSq%2FUI%20Filters.png?alt=media&#x26;token=83515231-4c35-4255-b7f4-c9e2c03ced55" alt=""><figcaption><p>UI filter</p></figcaption></figure>

#### **Comparing JQL vs. UI-Based Filtering**

* **Flexibility**: JQL is more flexible and allows for more complex queries, making it ideal for advanced users who need precise control over their data synchronization.
* **Ease of Use**: UI-based filtering is easier to set up and doesn't require knowledge of JQL syntax, making it more accessible to a broader range of users.
* **Performance**: Depending on the complexity of the JQL query, filtering via the UI might offer quicker setup and execution times, especially for basic filtering needs.

#### **Getint's Approach to Filtering**

At Getint, we understand that different users have different needs. That's why we offer both JQL and UI-based filtering options. For users who require advanced, granular control over their integration rules, JQL is the recommended approach. For those who prefer a simpler, more intuitive setup, our UI-based filtering provides a quick and efficient way to manage data synchronization.

We encourage customers to experiment with both methods to find the best fit for their specific use case. Testing filters via the UI can provide immediate feedback and is a great way to refine your filtering criteria before applying more complex JQL queries.

#### **Conclusion**

Both JQL and UI-based filtering offer valuable tools for managing your Jira integrations. By understanding the strengths and differences of each method, you can choose the one that best aligns with your workflow and integration needs. Whether you're syncing issues between Jira and ServiceNow, Azure DevOps, or any other platform, Getint provides the flexibility and power to ensure your integrations work seamlessly.

Before finalizing your JQL query within Getint, we recommend testing it in Jira to verify that it scopes to the exact tickets you need. For additional support, visit our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
