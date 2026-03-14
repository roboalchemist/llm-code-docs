# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/siem-integrations/splunk-integration.md

# Splunk Integration

The Splunk HTTP Event Collector (HEC) allows you to send data and application events to a Splunk distribution over HTTP and HTTPS protocols. The HEC uses a token-based authentication model.

The steps and guidance provided below will ensure a successful integration.

## Integration Steps

From the left menu go to **Company Settings > SIEM Integrations** and click the **+ NEW** button and provide the information requested.

<table data-header-hidden><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Integration Name</td><td>SIEM configuration name.</td></tr><tr><td>History Logs</td><td><p>Select this option to ensure that all data in the audit log will be transferred to your SIEM solution.<br></p><p>If this feature is inactive, only the audit log data recorded after defining the SIEM integration will be transferred to your SIEM solution.</p></td></tr><tr><td>Integration Type</td><td>Select Splunk integration type.</td></tr><tr><td>URL</td><td>The URL address of your Splunk solution.</td></tr><tr><td>Secret Token</td><td>Define Secret Token.</td></tr><tr><td>Test Connection</td><td>Test the connection to be sure it works correctly.</td></tr></tbody></table>

### **How to Get the Splunk URL Address**

To learn the URL address of the Splunk product, log in to the Splunk management console, then click **Data Inputs** in the **Data** field from the **Settings** section at the top. In the **Data Inputs** window that opens, click on **HTTP Event Collector (HEC).**

* Click the **Global Settings** button in the upper right of the HTTP Event Collector page.
* Retrieve the Splunk URL and the HTTP port number to be entered in the URL field of the platform.

### **How to Get Secret Token**

Log in to the Splunk management console, then click **Data Inputs** in the **Data** field from the **Settings** section at the top. Next, click on **HTTP Event Collector (HEC)** in the **Data Inputs** window.

* Click the **New Token** button on the upper right of the HTTP Event Collector (HEC) page.
* Complete the **Name** field and click the **Next** button.
* Click the **Select** button to apply the resource type specified in the **Input Settings** page to the data.
* Choose **select\_json (JavaScript Object Notation format)** from the **Structured** field of the window that opens.
* Click the **Review** button. After verifying the selections in the **Review** field, click the **Submit** button.
* After receiving a message indicating that the token has been created successfully, you can copy the **Token Value** created here and use it in the relevant field of the platform.

## **Control Phase**

In order to make sure that the integration works and logs are being transferred from the platform to the Splunk product properly, a test is advise&#x64;**.**

* After performing the integration, click the **Start Searching** button on the Splunk administration panel.
* When you click the **Test Connection** button on the platform, you can see this request or other platform logs in the **Search** field on the Splunk administration panel.
