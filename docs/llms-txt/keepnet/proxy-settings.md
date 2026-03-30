# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/proxy-settings.md

# Proxy Settings

This section explains the purpose and basic functions of proxy server settings. Go to **Company > Company Settings > Proxy Settings** to access all of the settings options described below.

## **Why Is A Proxy Needed?**

A proxy server is a system or router that provides a gateway between users and the internet. The users or products depending on the organization’s policy must/may use the proxy server settings to access the internet connection or log the traffic.

The steps below explain how to define proxy server settings for the platform to access the internet or other networks.

## Proxy Settings Page

You can view, edit, or delete any proxy configurations at the **Company > Company Settings > Proxy Settings** page.

<table><thead><tr><th width="169"></th><th width="579.1428571428571"></th></tr></thead><tbody><tr><td>Proxy Setting Name</td><td>The proxy settings name.</td></tr><tr><td>Proxy Address or IP</td><td>The proxy server address (hostname or IP address)</td></tr><tr><td>Port</td><td>The port number of the proxy server.</td></tr><tr><td>Authentication Method</td><td>Selected proxy connection method:<br><br><strong>Transparent:</strong> No user authentication is required.<br><br><strong>Basic:</strong> User authentication is required.</td></tr><tr><td>Is Default?</td><td>If it’s selected, the new settings that will be created in the platform will have a default proxy setting automatically.</td></tr><tr><td>Date Created</td><td>The date and time that proxy settings were created.</td></tr><tr><td>Actions</td><td>Proxy settings can be edited or deleted.</td></tr></tbody></table>

## **How to Configure Proxy Settings**

Go to **Company > Company Settings > Proxy Settings** from the main menu. Click on **+ NEW** to create a proxy setting.

The elements of the proxy settings page are defined in the table below.

<table data-header-hidden><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Proxy Setting Name</td><td>Name of the proxy rule</td></tr><tr><td>Proxy Address or IP</td><td>The proxy server address (hostname or IP address)</td></tr><tr><td>Port</td><td>The port number of the proxy server.</td></tr><tr><td>Authentication Method</td><td>Select a proxy connection method:<br><br><strong>Transparent:</strong> No user authentication is required.<br><br><strong>Basic:</strong> User authentication is required.</td></tr><tr><td>Make Default Proxy Setting</td><td>If it’s selected, the new settings that will be created in the platform will have a default proxy setting automatically.</td></tr><tr><td>Test Connection</td><td>Confirm if the proxy settings work correctly.</td></tr></tbody></table>

## **Use Cases of Proxy**

#### **Incident Responder Integration**

The layer of security provided by your defined proxy settings can easily be integrated with the Incident Responder product’s integrations.

* Go to **Incident Responder > Integrations**.
* Edit one of your created integrations that you wish to set the proxy for.
* Find the **Proxy** field and select the **Proxy** **setting** to be applied.
* Click Save to apply the changes.

If you do not want to use a proxy, choose the **No Proxy** option. If you want to use the default system proxy settings, select the **Default Proxy** option.

## **FAQ:**

### **Q: Can I use my own proxy server in a Cloud version of the platform?**

A: Yes. You can configure your own proxy settings to enable access to many of the platform features; however, the internet IP address and Port information of your proxy server must be defined to allow access by the platform.

### **Q: Can I use my own proxy server in an On-Premise version of the platform?**

A: Yes. You can use your own proxy settings to give internet access and record the platform's internet traffic.
