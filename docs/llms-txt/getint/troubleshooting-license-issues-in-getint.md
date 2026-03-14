# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users/troubleshooting-license-issues-in-getint.md

# Troubleshooting License Issues in Getint

If you’re experiencing license-related issues in Getint, follow this guide to diagnose and resolve common problems, such as selecting the correct app, handling license verification errors, and ensuring proper integration setup. This will help you address issues independently and ensure your integrations run smoothly.

***

### Common License Issues <a href="#common-license-issues" id="common-license-issues"></a>

Getint users may encounter the following license issues:

1. **Missing or Expired License**: The license is missing or expired, preventing integration.
2. **Invalid License Key**: An unrecognized or incorrectly entered license key.
3. **Incorrect App Selection**: Attempting to create an integration under an app that does not align with the intended integration type.
4. **Deployment-Specific Issues**: Differences between Jira Cloud, Data Center, and on-premise setups that may impact license.

***

### Key Troubleshooting Steps <a href="#key-troubleshooting-steps" id="key-troubleshooting-steps"></a>

#### 1. Verify App Selection for Integrations <a href="#id-1.-verify-app-selection-for-integrations" id="id-1.-verify-app-selection-for-integrations"></a>

Each Getint app is tailored to specific integrations (e.g., Jira-Asana, Jira-DevOps). It is crucial to select the correct app for your integration to avoid licensing errors.

**How to Select the Correct App:**

* **Jira Cloud:**
  * Confirm the integration type you’re creating (e.g., Jira with Asana).
  * Navigate to **Apps** at the top of your Jira screen.
  * Select the appropriate Getint app matching your integration (e.g., “Jira-Asana” if integrating Jira with Asana).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fg71RxfLlliBWdoQ5WVdM%2FLicense%20issues%20in%20getint.png?alt=media&#x26;token=311bad35-d729-4f5c-9f4d-50fa4c58a11b" alt=""><figcaption></figcaption></figure>

* **Jira Data Center:**
  * Confirm the integration type you’re creating (e.g., Jira with Asana).
  * Go to Manage Apps on the Settings Icon.
  * Select Administration on the appropriate app, like “Jira-Asana” if integrating Jira with Asana.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F24IkwvoWSTWeDAIn7wey%2FFinding%20the%20app.png?alt=media&#x26;token=e2c757fa-4514-476e-9607-ff8ada77de03" alt=""><figcaption></figcaption></figure>

If you see the error message *“Failed to fetch flow triggers: Invalid Jira license,”* this may indicate the incorrect app has been selected for the integration or that you do not have the license for that integration.

{% hint style="info" %}
If you need to expand integrations within your existing app (e.g., add Asana-DevOps integration when you have a Jira-Asana license), contact [Getint Support](https://getint.io/help-center) for guidance on purchasing an additional license.
{% endhint %}

#### 2. Confirm License Status <a href="#id-2.-confirm-license-status" id="id-2.-confirm-license-status"></a>

To check the status of your license, follow these steps based on your environment:

* **For Cloud and Data Center**:
  * Go to **Marketplace** > **Manage Apps** in your Atlassian instance.
  * Locate the Getint app to confirm the license is active.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FwOyhVrzdzGI2OIxxMrkj%2FChecking%20your%20DC%20app%20settings.png?alt=media&#x26;token=eec295fe-7f4d-425f-8f3e-0b676dad1c44" alt=""><figcaption></figcaption></figure>

* **On-Premise**:
  * Access **Settings** > **License** within the Getint app to verify your license status.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqcBKd9lAq7lQgcg8jayc%2FChecking%20your%20license.png?alt=media&#x26;token=e2320210-c6d2-4f77-b58e-30cfbc6acb00" alt=""><figcaption></figcaption></figure>

#### 3. Renewing or Updating a License <a href="#id-3.-renewing-or-updating-a-license" id="id-3.-renewing-or-updating-a-license"></a>

If you find your license has expired or you need a new one:

1. **Jira Cloud / DataCenter - Renew Your License**:
   * Go to the Atlassian Marketplace and search for the relevant Getint app (e.g., Jira-Asana).
   * Renew, purchase a license, or activate a trial if you're starting the trial period.
2. **Getint On-Premise - Updating the License Key**:
   * If you have a new key, navigate to **Settings** > **License** in Getint.
   * Enter the new license key and click **Update**.

***

#### 4. Check for Common Errors in the Logs <a href="#id-4.-check-for-common-errors-in-the-logs" id="id-4.-check-for-common-errors-in-the-logs"></a>

For detailed troubleshooting, review the logs in Getint to identify any license-related errors:

* **Where to Find Logs**:
  * Access logs by checking the latest Runs, then select the 3 dots in the right corner and details. Select **Logs** on the left side
* **Enable Debug and HTTP Logging**:
  * Go to **Settings > Data Storage**. Set logs level to **Debug** level and enable **HTTP logging** for detailed error tracking.
  * Look for keywords like ***License** and* ***Invalid***.

{% hint style="info" %}
**Tip**: Analyze log messages related to license validation to understand the issue.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWshBClQk9llsWQvz49uw%2FChecking%20the%20logs.png?alt=media&#x26;token=d9a216f0-8f7a-41c5-b17a-e6731f7660ff" alt=""><figcaption></figcaption></figure>

***

### Diagnosing Specific License Issues <a href="#diagnosing-specific-license-issues" id="diagnosing-specific-license-issues"></a>

#### Invalid License Key <a href="#invalid-license-key" id="invalid-license-key"></a>

If you encounter an **Invalid License Key** error:

1. Re-Enter the License Key, if you have received a license from us:
   * Go to **Settings > License** and carefully re-enter the license key.
   * Ensure the key matches the one provided by Getint.
2. Check for Key Formatting:
   * Avoid extra spaces or incorrect characters.
   * If errors persist, reach out to [Getint Support](https://getint.io/help-center) for assistance.

#### Missing Permissions on Jira Integration <a href="#missing-permissions-on-jira-integration" id="missing-permissions-on-jira-integration"></a>

If the Jira integration isn’t running as expected:

1. Confirm the Jira user used for integration has the required permissions, as Getint uses the Jira REST API to validate licenses.
2. To validate the connection:
   * Go to **Integrations** > select the **connection** name > click **Update** to refresh the connection and test permissions.

***

### Contacting Getint Support <a href="#contacting-getint-support" id="contacting-getint-support"></a>

If you cannot resolve your issue using this guide, contact [Getint Support](https://getint.io/help-center) with the following details:

* **Instance ID** and **Entitlement number (SEN)**.
* **Screenshots** of the license settings and any error messages.
* **Logs** (ensure Debug and HTTP logging are enabled).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
