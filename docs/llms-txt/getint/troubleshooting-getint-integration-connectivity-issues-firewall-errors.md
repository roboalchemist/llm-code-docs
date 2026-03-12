# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users/troubleshooting-getint-integration-connectivity-issues-firewall-errors.md

# Troubleshooting Getint Integration Connectivity Issues

### **Introduction** <a href="#introduction" id="introduction"></a>

Ensuring a stable connection between Getint and various applications like JIRA, ServiceNow, and Freshdesk is crucial for seamless integration. However, intermittent connectivity issues can occur, potentially disrupting workflow. This guide addresses common errors and provides steps to resolve connectivity problems effectively.

### **Common Connectivity Errors** <a href="#common-connectivity-errors" id="common-connectivity-errors"></a>

#### **Error Types and Descriptions**

#### **1. Firewall Configuration Issues**

* **Errors Encountered**:
  * 502 Bad Gateway
  * 503 Service Unavailable
  * 504 Gateway Timeout
  * Connection timed out
  * Temporary failure in name resolution

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPK3CqaCBma29TrgFYMQw%2Fimage-20240417-172637.png?alt=media&#x26;token=49e8a566-a71e-4b4b-bd76-de9cf0a21040" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FfsHo9JBxtvd7baxCEk96%2FScreenshot%202024-04-17%201441061.jpg?alt=media&#x26;token=f49215be-b4dd-4e5d-8c92-f81ce2f1a693" alt=""><figcaption></figcaption></figure>

* **Identifying the Problem:** These errors usually indicate that network requests made by Getint are being blocked by your firewall.
  * **Solution**:
    * **Gather Required URLs and IP Addresses:**
      * Obtain a list of all URLs and IP addresses that Getint needs to access. This information can usually be found with the Getin team l or from the support team.
      * **Engage Your IT Team:**
        * Provide the list to your IT or network team and explain that these are essential for Getint’s operations.
      * **Review Firewall Rules:**
      * Ask your IT team to review the current firewall rules and identify if any of the required URLs or IP addresses are being blocked.
      * **Modify Firewall Settings:**
        * Request that your IT team modify the firewall settings to allow traffic to and from these URLs and IP addresses. They may need to:
        * Add new rules to allow these addresses.
        * Adjust existing rules that may be too restrictive.
      * **Verify Changes:**
        * After the firewall settings have been adjusted, perform a connectivity test to ensure that Getint can now communicate with the external applications without interruption.

#### **2. Intermittent Network Failures**

* **Error Example**:
  * `[ERROR] 2024-01-09T13:47:19.747Z - [main-0-1408647-119] Error occurred when performing flow org.apache.http.conn.HttpHostConnectException: Connect to 1234.service-now.com:443 [ServiceNow] failed: Connection timed out (Connection timed out)`
* **Possible Cause**: This error signifies a network connection failure, potentially due to temporary network issues or configuration errors impacting connectivity.
* **Solution**: Since Getint cannot directly resolve network issues, it is recommended that the customer's network team investigates and resolves the connectivity problems.

#### **3. Steps to Resolve Connectivity Issues**

* **Document Specific Error Details:**
  * Record the error code, the exact URL or IP address involved, and the time when the error occurred.
* **Communicate with Your Network Team:**
  * Provide these details to your network team and ask them to investigate potential causes.
* **Conduct Network Diagnostics:**:
  * For intermittent connectivity errors, perform network diagnostics to check the stability of your connection to the affected applications. Ensure that no disruptions or blockages are affecting the network paths.
* **Check Network Equipment and Configuration:**
  * Have the network team check routers, switches, and other network devices for any misconfigurations or failures that could be causing connectivity issues.
* **Ongoing Monitoring and Adjustment:**
  * Ensure that the network team continues to monitor the network traffic and adjust as necessary to maintain stable connectivity.

### **Conclusion**

Connectivity issues between Getint and integrated applications can vary, but with proper troubleshooting and cooperation from your network team, these issues can be resolved effectively. For further support and guidance, contact our support [here](https://getint.io/help-center)[.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FARqisDpTn5nDx8qz68lf%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=69cbd158-18f3-4597-8ed5-57b9471ba976" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues to build your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
