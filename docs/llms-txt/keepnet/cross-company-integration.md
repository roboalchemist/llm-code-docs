# Source: https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder/cross-company-integration.md

# Cross Company Integration

This section explains the functions in **Incident Responder > Cross Company Integration**. You will see basic functions such as adding Cross Company Integration, editing, disabling deleting and an existing integration in the Incident Responder.

To access all the sections described in this document, go to **Incident Responder > Cross Company Integration, Incident Responder > Integrations,** and **Company > Company Settings**.

{% hint style="info" %}
The steps detailed below are explained by exemplary companies such as Company A and Company B.
{% endhint %}

### **Steps to Create Rest API Client ID and Client Secret** <a href="#steps-to-create-rest-api-client-id-and-client-secret" id="steps-to-create-rest-api-client-id-and-client-secret"></a>

Please complete the following steps to create the Rest API Client ID and Client Secret.

The platform client (Company A) who will grant permission for the use of their integrations should visit the menu **Company > Company Settings**. On this page, the Rest API tab is clicked. Click on the **New** button on the page, then fill in the following fields:

<table data-header-hidden><thead><tr><th width="163"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Client Name</td><td>Enter the name of the customer for which the API is provided.</td><td></td></tr><tr><td>Client ID</td><td>Client ID information is created automatically. Please save this information.</td><td></td></tr><tr><td>Client Secret</td><td>Client Secret information is created automatically. Please save this information.</td><td></td></tr><tr><td>IP Restriction</td><td>Use this menu to define an IP restriction for access.</td><td></td></tr><tr><td>Client Role</td><td>The created API Key will have the relevant privileges for the user role it was created for. You can only define a Custom Role for Cross Company Integration.</td><td></td></tr></tbody></table>

### **How to Add Cross Company Integration?** <a href="#how-to-add-cross-company-integration" id="how-to-add-cross-company-integration"></a>

By using the **Client** **ID** and **Client** **Secret** information shared by **Company A** of **Company B**, which will receive integration service from **Company** **A**, it can be integrated on the Incident Responder platform by following the steps below, and the capabilities of the analysis products used by **Company A** can be utilized.

In order to receive service from **Company A**, **Company B** must use the **Client** **ID** and **Client** **Secret** information shared by **Company** **A**. For this, by following the steps below on the [Incident Responder](https://keepnetlabs.com/products/incident-responder) platform, the products used by **Company** **A** and the analysis capabilities of these products can be integrated into **Company** **B’s** profile.

Click the **New** button on the relevant page, then fill in the fields:

<table data-header-hidden><thead><tr><th width="148"></th><th></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select Cross Company Integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of Cross Company Integration is defined automatically. Please do not change it except in special circumstances.</td><td></td></tr><tr><td>Client ID</td><td>Define the Client ID information.</td><td></td></tr><tr><td>Client Secret</td><td>Define the Client Secret information.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure that the Client ID and Client Secret information are working correctly with the Test Connection button.</td><td></td></tr><tr><td>Tags</td><td>Tag can be specified optionally for Cross Company Integration.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave <strong>Default</strong>.</td><td></td></tr><tr><td>URLs</td><td>URL analysis capability is enabled by default, you can disable it if needed.</td><td></td></tr><tr><td>Sender IP</td><td>Sender IP analysis capability is active by default, it can be disabled if needed.</td><td></td></tr><tr><td>Attachments</td><td>URL analysis capability is enabled by default, you can disable it if needed.<br>Optionally, you can add to the scanning process by selecting the “Upload PE files” and “Upload other file types” fields.</td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>
