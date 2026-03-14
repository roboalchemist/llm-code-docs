# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users.md

# Troubleshooting Guide for Getint Users

### **How to Provide a Support Package for Problematic Sync Items** <a href="#how-to-provide-a-support-package-for-problematic-sync-items" id="how-to-provide-a-support-package-for-problematic-sync-items"></a>

1. Navigate to the **Reporting** page.
2. Select the **Synced Items** tab.
3. Click **EXPORT SUPPORT PACKAGE**.
4. Provide the item IDs that have synchronization issues.
5. Click **GENERATE**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FA58rhzz2f4Fxc84Cy75F%2FGenerate%20Support%20Package.png?alt=media&#x26;token=b026539b-48a6-4b6a-9501-745e13396c5b" alt=""><figcaption></figcaption></figure>

This will create a `.zip` file containing all the logs and data related to the problematic items. Send this file to our support team for further analysis.

### **How to Check Your Instance ID** <a href="#how-to-check-your-instance-id" id="how-to-check-your-instance-id"></a>

1. Click the **Help** button on the left bottom corner of the menu.
2. Your instance name will be displayed in the popup window.

   For example, in the image below, the instance ID is `a3f4e86e2`.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FoWYVuYerZVKbqwZlPPiI%2FChecking%20Instance%20ID.png?alt=media&#x26;token=8bb43ca4-565e-4f31-bc62-38a52a00dcd1" alt=""><figcaption></figcaption></figure>

### **How to Specify Issues for Synchronization** <a href="#how-to-specify-issues-for-synchronization" id="how-to-specify-issues-for-synchronization"></a>

Use the Custom Query feature to limit the scope of issues for synchronization. For each app in the integration, you can provide a query aligned with the app's REST API specification.

#### **Example for Jira:**

1. Provide a custom JQL query, such as `labels = sync`. Ensure the query adheres to JQL syntax. [Learn more about JQL here](https://www.atlassian.com/blog/jira-software/jql-the-most-flexible-way-to-search-jira-14) and in our article [How to Use JQL Filters for Jira Integrations](https://docs.getint.io/getintio-platform/workflows/how-to-use-jql-filters-for-jira-integrations).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkWTqN5dBrZqdBJlAaftO%2FEntering%20a%20Custom%20JQL.png?alt=media&#x26;token=03e3807b-8a97-4832-833d-8a268f9ff91c" alt=""><figcaption></figcaption></figure>

1. Save the integration.
2. Confirm your custom JQL query is appended to the auto-generated query by reviewing logs, such as:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAAbP8sP93NipvER8tclO%2FLogs%20preview.png?alt=media&#x26;token=7f4f0041-8dd6-429e-9212-c04ade4e72ea" alt=""><figcaption></figcaption></figure>

`[INFO ] 2024-11-25T16:46:05.945Z - [main-0-2790043-208] Prepared Jira jql: project = "JIRA" AND issuetype IN (10022,10023) AND labels = sync AND updated >= '2024/11/25 17:44'`

{% hint style="warning" %}
**Important:** Ensure the custom JQL includes criteria to match newly created items resulting from syncs. Otherwise, updates may not be picked up for re-synchronization.
{% endhint %}

### **Why Can't I See My Custom Field in the Fields List?** <a href="#why-cant-i-see-my-custom-field-in-the-fields-list" id="why-cant-i-see-my-custom-field-in-the-fields-list"></a>

If using Jira Cloud:

1. Go to **Settings** and select **Issues** to configure the issue types.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F06QJ0pKL4kJdy6frAFbC%2FJira%20settings.png?alt=media&#x26;token=17c23884-0305-4f37-ace1-1a90e4bc95d6" alt=""><figcaption></figcaption></figure>

1. Select the **Custom Fields** on the left side menu
2. Locate your custom field and click **Associate to Screens**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsmQhu4hqsaAmg18Xz57A%2FCustom%20fields%20page.png?alt=media&#x26;token=6332b47e-3459-43b8-803d-6f7447c86a89" alt=""><figcaption></figcaption></figure>

1. On the **Screens** page, ensure the checkbox is selected for the project you are integrating.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXvTS0wtaqkhJPHmxxI1c%2FAssociated%20issues%20in%20Jira.png?alt=media&#x26;token=e1b1943a-9f89-4de8-aaed-8c49a04ed58d" alt=""><figcaption></figcaption></figure>

1. Click **Update**.
2. Refresh the **Getint** app and check again.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FP3stMvKiL8lxLNVwWTi8%2FCustom%20fields%20in%20Getint.png?alt=media&#x26;token=5ff49e55-a045-47e7-b53c-f8569d78a12f" alt=""><figcaption></figcaption></figure>

If the issue persists, or you are using another app, submit a [support ticket](https://getintio.atlassian.net/servicedesk/customer/portals) for assistance.

### **How to Stop a Migration Run** <a href="#how-to-stop-a-migration-run" id="how-to-stop-a-migration-run"></a>

1. Go to **Analysis > Integration Threads**.
2. When an integration is running, a **STOP RUN** button will appear.
3. Click the button to stop the run.

   The run will stop after the synchronization of the current item is complete.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fp76nhYIPPgEOXj2QJJXK%2FStop%20a%20migration%20run.png?alt=media&#x26;token=fd9d2c3a-8feb-4362-b141-f433f239d95f" alt=""><figcaption></figcaption></figure>

### **How to Provide a Fixed Value for a Field** <a href="#how-to-provide-a-fixed-value-for-a-field" id="how-to-provide-a-fixed-value-for-a-field"></a>

To set a fixed value for a field:

1. Add a field mapping.
2. Enter the fixed value into the **Predefined Value** field.
3. Click **Add** to create the mapping.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FAnTobszE2PqD1WAmyp2X%2FProviding%20a%20fixed%20value%20for%20a%20field.png?alt=media&#x26;token=61a01fcb-680e-4cba-8184-514964982bd7" alt=""><figcaption></figcaption></figure>

### **How to Exclude Private Comments from Sync** <a href="#how-to-exclude-private-comments-from-sync" id="how-to-exclude-private-comments-from-sync"></a>

Filtering private comments can be done at the **Comments and Attachments** tab:

1. Open the relevant **Type Mapping**.
2. Go to the **Comments & Attachments** tab.
3. Select the criteria below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxGfuyyxCGPf0WJ3bPamF%2FExcluding%20private%20comments%20from%20sync.png?alt=media&#x26;token=bf697206-e4b5-422b-aaa6-fefc640d3e4c" alt=""><figcaption></figcaption></figure>

1. Save the integration.

Only public comments will sync, while private comments will be excluded. Please review our doc [How to filter comments](https://docs.getint.io/getintio-platform/workflows/items-filtering/how-to-filter-comments) for more details.

### **Troubleshooting Connections to the Jira Server/Data Center** <a href="#troubleshooting-connections-to-the-jira-server-data-center" id="troubleshooting-connections-to-the-jira-server-data-center"></a>

Errors during connection setup may occur due to firewalls blocking access. Examples include:

* `ERR_CONNECTION_RESET`
* `Unknown hostname`
* `Socket timeout`

#### **Solution Options**

1. **Whitelist Getint’s SaaS Infrastructure**:
   * Open your firewall to allow incoming requests from Getint ’s IP address on ports 443 (HTTPS) or 80 (HTTP).
   * Contact our support team for the specific IP addresses.
2. **Use Getint’s On-Premise Platform**:
   * Host the app on a Linux machine within your network, bypassing firewall restrictions.
   * Learn more about [On-Premise Deployment](https://docs.getint.io/getting-started-with-the-platform/deployment-options/on-premise-deployment).
3. **Test with a Cloud Instance**:
   * Create a temporary Jira Cloud account and test the integration with your destination app. If satisfied, purchase the On-Premise version for your production environment.
4. **Request Assistance**:
   * Share the apps and versions you want to integrate, and we can create a test environment for you.
   * Our team can assist with installation via remote access or guided Zoom sessions.

We recommend reviewing our guide [Troubleshooting Getint Integration Connectivity Issues](https://docs.getint.io/getintio-platform/connections/troubleshooting-getint-integration-connectivity-issues-firewall-errors) for more details.

***

By following these instructions and leveraging Getint’s support resources, you can effectively address integration challenges and optimize your workflows. For more help, visit our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgCfQJX8Bur2XgVPQN8ya%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=542ea79a-7c00-43db-9cb2-e95b5f8c8e46" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues to build your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
