# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/siem-integrations.md

# SIEM Integrations

This section explains how to integrate the data in the audit log, a record of all system activity, with your security information and event management (SIEM) products.

## **SIEM Integration Structure**

The characteristics and functionality of an integration can be adjusted as needed using the following path: **Company > Company Settings > SIEM Integrations.**

<table data-header-hidden><thead><tr><th width="150"></th><th width="580.2292817679559"></th></tr></thead><tbody><tr><td>Integration Name</td><td>The name of the integration.</td></tr><tr><td>Integration Type</td><td>The type of the integration.</td></tr><tr><td>Status</td><td>Active or Inactive status of the integration.</td></tr><tr><td>Date Created</td><td>The creation date of the integration.</td></tr><tr><td>Action</td><td>Edit or delete an integration</td></tr></tbody></table>

## **Creating New Integration**

From the main menu, go to **Company > Company Settings > SIEM Integrations.** Then click on the **+ NEW** button to create a new SIEM configuration.

The information on the SIEM configuration edit page is detailed in the table below.

### **Configuration Details**

<table data-header-hidden><thead><tr><th width="150"></th><th width="584.1428571428571"></th></tr></thead><tbody><tr><td>Integration Name</td><td>SIEM configuration name</td></tr><tr><td>History Logs</td><td>Select this option to ensure that all data in the audit log will be transferred to your SIEM solution.<br><br>TIP: If this feature is inactive, only the audit log data recorded after defining the SIEM integration will be transferred to your SIEM solution.</td></tr><tr><td>Integration Type</td><td>SIEM integration type.</td></tr></tbody></table>

The next section describes how to initiate an integration.

## **Integrations**

The platform supports the following SIEM products, please click on it to view the related documentation.

* [How to integrate Splunk](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/siem-integrations/splunk-integration)
* [How to integrate Syslog](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/siem-integrations/syslog-integration)

## FAQ

### Q: What are the kinds of information/logs which can be sent to a SIEM like Sentinel from Keepnet?

A: All audit information/logs under **Company > Audit Log** is sent to the SIEM server.
