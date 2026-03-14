# Source: https://docs.getint.io/support-legal-and-others/faq/technical-faq.md

# Technical FAQ

### **Can I sync projects within one Jira instance?**&#x20;

Yes, Getint supports internal synchronization within a single Jira instance, allowing project-to-project syncs just as seamlessly as synchronizing between different instances.

### **Can I integrate Jira Cloud with Jira Server?**&#x20;

Absolutely. Getint facilitates integration across all versions of Jira, enabling combinations like Jira Cloud to Jira Cloud, Jira Cloud to Jira Server, and Jira Server to Jira Data Center, among others.

### **What versions of Jira are supported by Getint?**&#x20;

Getint is compatible with Jira Cloud and Jira Server / Data Center versions 7.0 and above.

### **Does Getint operate by polling or pushing changes for synchronization?**&#x20;

Getint operates on a polling model, where it periodically fetches changes from the connected applications to synchronize data. Further details are available in our synchronization section.

### **What additional support does Getint offer?**&#x20;

Our standard Service Level Agreement (SLA) promises a 24-hour response time. Premium support customers enjoy not only faster responses but also direct access to our tech team via Slack, ensuring immediate assistance with any issues.

### **Does Getint offer built-in Self-Monitoring and High-Availability features for On-Premise deployment?**&#x20;

Currently, these features are not available for On-Premise deployments. Customers can utilize external tools to monitor server performance and alert for any errors. A list of recommended tools is available upon request.

### **Is Getint a standalone platform?**&#x20;

Yes, Getint functions as a standalone platform, independent of the applications it integrates with, such as Jira. While Getint Jira apps are primarily for licensing, all configuration and synchronization logic is executed externally, making the On-Premise version essential for server/DC behind firewalls.

### **Is the On-Premise version of Getint Dockerized?**&#x20;

Indeed, the On-Premise version utilizes Docker for various services like PostgreSQL and NGINX, streamlining installation and trial processes with docker-compose.

### **If unable to open a firewall port, is hosting Getint On-Premise necessary?**&#x20;

Yes, opening a port in the firewall is required. Alternatively, hosting Getint On-Premise on your servers is necessary.

### **How can I quickly sync a large volume of data?**&#x20;

Setting up multiple integration threads allows for parallel processing, enabling simultaneous synchronization without waiting for other integrations to complete.

### **Can Getint handle custom scripting for data transmission/reception like Exalate?**&#x20;

While Getint doesn't offer scripting to the extent of Exalate, it supports variables and logical conditions for dynamic value construction in fields, covering most use cases through its UI. For additional needs, contacting our support is recommended.

### **Can Getint synchronize project settings?**&#x20;

Currently, Getint focuses on data synchronization. Interest in syncing project settings is noted, and updates will be shared in our roadmap.

### **Can Getint synchronize Jira apps from one instance to another?**&#x20;

This feature is not in our plans, as Getint's focus remains on issues and data synchronization.

### **What about custom fields of apps installed in my Jira?**&#x20;

Custom fields are treated the same as standard Jira fields in Getint and can be synchronized. If a custom field is not listed, please contact our support.

### **What if custom development is needed for extra features?**&#x20;

If you require custom features, reach out with your use case. If deemed beneficial for the product, it may be added to our roadmap.

### **How does Getint approach the need to migrate only specific tickets?**&#x20;

Integration setup allows for custom queries to filter items for synchronization, ensuring only relevant items are selected for migration.

### **What setup is needed in tools for using Getint?**&#x20;

For Jira Cloud, installing a Getint app from the Atlassian Marketplace is necessary. Credentials for app users are needed for integration setup across all platforms. For Jira Server, install Getint on a Linux machine if behind a firewall, or create an account on our SaaS instance for external Jira Servers.

### **What kind of user is needed for setting up the connection?**&#x20;

A user with permission to access the projects and items you wish to synchronize. Administrator permissions are not required.

### **What if another connection method besides Basic Auth/OAuth is used?**&#x20;

Getint supports various authentication methods. If using SSO or other methods, contact our support to explore options.

### **Is installation required in the apps themselves (e.g., Jira, ServiceNow)?**&#x20;

For Jira Cloud, installing a Getint app is mandatory. For other apps and Jira Server/DC, no additional installations are necessary.

### **What are the main differences between SaaS and On-Premise deployments?**&#x20;

Differences mainly lie in data hosting and security policy compliance. On-Premise is recommended for Jira instances behind firewalls or when large-scale data synchronization is needed.
