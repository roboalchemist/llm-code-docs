# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users/debugging-connections-in-getint-how-to-troubleshoot-and-resolve-issues.md

# Debugging Connections in Getint: How to Troubleshoot and Resolve Issues

Effective connection management is crucial for seamless integration processes. However, when issues arise, it’s important to understand how to debug these connections to identify and resolve problems efficiently. This KB will guide you through the process of debugging connections in Getint, offering insights into how this feature works and when to use it.

***

### Understanding Debugging Connections <a href="#understanding-debugging-connections" id="understanding-debugging-connections"></a>

The Debug Connections feature in Getint is a powerful tool designed for troubleshooting and verifying the connections between integrated platforms. Whether you're dealing with issues where data isn’t syncing properly or you simply need to confirm that a connection is working as expected, this feature provides a direct method to diagnose and resolve potential problems.

### **Why Debug Connections?**

Debugging connections allows you to:

* Verify that your connection to the API endpoint is correctly established.
* Test API requests directly to ensure that the connection is returning the expected data.
* Identify and troubleshoot specific issues, such as missing projects or data discrepancies between platforms.

### How to Debug Connections <a href="#how-to-debug-connections" id="how-to-debug-connections"></a>

1. **Accessing the Debug Feature**

* Navigate to the **Workflows** section in the Getint app.
* Select **Connections** to view the list of available connections.
* Identify the connection you want to debug.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6vCrzdW1AHVicjqP2BMW%2FUntitled%20design%20(30).jpg?alt=media&#x26;token=bff3eb53-2668-46a2-b987-cbc96bb32f55" alt=""><figcaption></figcaption></figure>

1. **Initiating a Debug Request**

* Click on the connection you wish to debug.
* Use the **Debug Request** feature to call specific API endpoints. This feature supports only GET requests.
* Input the endpoint URL you want to test and send the request. For example, you might use the API endpoint for retrieving projects from Jira to verify that the connection is correctly fetching the data.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBgn7B1JSyZJuH16eP54b%2FUntitled%20design%20(32).jpg?alt=media&#x26;token=709cc84f-296d-423c-942d-10cadefbb802" alt=""><figcaption></figcaption></figure>

1. **Analyzing the Response**

* Review the response returned by the API. This will include data such as project names, user details, or other relevant information that the connection is supposed to access.
* Compare this response with what is displayed in the Getint interface. If discrepancies are found, this could indicate a problem with how the data is being processed or displayed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGDQd4EDDOdXoyXZ9l171%2FUntitled%20design%20(33).jpg?alt=media&#x26;token=c9391297-2f6f-4784-9bad-093eb7546eca" alt=""><figcaption></figcaption></figure>

### Example Scenario: Missing Project Data <a href="#example-scenario-missing-project-data" id="example-scenario-missing-project-data"></a>

Suppose that you cannot see certain projects in Getint that exist in Jira. Here’s how you can use the Debug feature:

* **Step 1:** Access the connection linked to Jira.
* **Step 2:** Use the Debug Request feature to call the Jira API endpoint that retrieves project data.
* **Step 3:** Check the API response to see if the missing project appears. If the project is present in the API response but not in Getint, the issue may lie in how Getint processes or displays the data. In this case, [contact our support](https://getint.io/help-center) for help.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FN5cMt87miCDD7hJaLzSt%2FUntitled%20design%20(34).jpg?alt=media&#x26;token=a7d89aa4-0131-46b6-9400-2a86be13883e" alt=""><figcaption></figcaption></figure>

### Debugging Connections: Tips and Best Practices <a href="#debugging-connections-tips-and-best-practices" id="debugging-connections-tips-and-best-practices"></a>

* **Permission Settings:** Ensure that the connection permissions are correctly set to allow debugging. If you don’t have the necessary permissions, ask the owner to share the connection with you by enabling the "Anyone in workspace can edit" option.
* **Connection Sharing:** If more in-depth analysis is required, customers can share their connections with support for direct debugging. The guide [here](https://docs.getint.io/getintio-platform/settings/sharing-access-permission) will help with how to share with support.

***

### Conclusion <a href="#conclusion" id="conclusion"></a>

The Debug Connections feature in Getint is an invaluable tool for troubleshooting integration issues and ensuring that connections between platforms are functioning correctly. By following the steps outlined in this guide, you can efficiently diagnose and resolve connection problems, helping to maintain smooth and reliable integrations.

For further assistance, please reach out to our [support team](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
