# Source: https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder/integrations.md

# Integrations

This section explains the functions of **Incident Responder > Integrations**. The Incident Responder product can be used to perform simple tasks like adding a new integration, modifying, deactivating, and deleting the existing integration.

To access every section of this document, go to the **Incident Responder > Integrations** menu.

## **Integrations**

The components of the Integrations page are:

<table data-header-hidden><thead><tr><th width="150"></th><th width="582.2051282051282"></th><th data-hidden></th></tr></thead><tbody><tr><td>Integration Name</td><td>Name of the Integration.</td><td></td></tr><tr><td>Integration Type</td><td>Type of the Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Status</td><td>The status information of the integration. (Active, Inactive)</td><td></td></tr><tr><td>Date Created</td><td>The date of the integration creation.</td><td></td></tr><tr><td>Actions</td><td>You can edit the selected integration. You can change the status or delete the integration by clicking the "︙" button.</td><td></td></tr></tbody></table>

## **Creating New Integration**

If you want to add an integration for the first time, click the **New** button (on the middle of the page), if there is an integration that has been added before, click the **New** button (in the upper right corner of the page).

You can create a new integration by following the steps in the table below.

<table data-header-hidden><thead><tr><th width="150"></th><th width="582.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Integration Name</td><td>Name of the Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select an integration type.</td><td></td></tr><tr><td>API URL</td><td>The API URL address of the integration type. The VirusTotal, Google Safe Browsing, Zen Spamhaus, IBM X-Force, Opswat, Google Web Risk, VMRay, AnyRun, and Cyber X-Ray analysis engines have API URLs by default on the platform and changing the domain may cause disfunction.</td><td></td></tr><tr><td>Tags</td><td>Labeling function. Integrations defined in the system can be filtered more easily by labeling them.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave <strong>Default</strong>.</td><td></td></tr><tr><td>URLs</td><td>URL analysis capability is enabled by default, you can disable it if needed.</td><td></td></tr><tr><td>Sender IP</td><td>Sender IP analysis capability is active by default, you can disable it if needed.</td><td></td></tr><tr><td>Attachments</td><td>File analysis capability is active by default, you can disable it if needed.</td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

## **Advanced Settings**

If there are emails that you do not want to be analyzed in the [Incident Responder](https://keepnetlabs.com/products/incident-responder), you can exclude them from analysis by adding their IP addresses, URL addresses, and File Extensions to this menu. Using this feature, you can ensure that secure IP addresses, domains, and file extensions are not analyzed. Thus, API limits used in integrations are utilized more efficiently.

You can access this feature from the **Advanced Settings** page on the **Incident Responder > Integration** menu.

<table data-header-hidden><thead><tr><th width="150"></th><th width="585.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>URLs</td><td>Exclude URL addresses in a reported email from the analysis.</td><td></td></tr><tr><td>IP Addresses</td><td>Exclude the IP address of a reported email server and the IP addresses included as URLs in the email from the analysis.</td><td></td></tr><tr><td>Attachments</td><td>Exclude file extensions in a reported email from the analysis.</td><td></td></tr></tbody></table>

## **How to Add Integration**

### **IBM X-Force**

IBM X-Force is a commercial threat analysis engine from IBM. It is available in a premium version. The IBM X-Force doesn't provide a free API key subscription. The IBM X-Force threat analysis engine analyzes whether a reported email is malicious or not using the following capabilities.

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Sender IP</td><td>The sender email server IP address of a reported email is analyzed.</td><td></td></tr><tr><td>URLs</td><td>URL addresses in a reported email are analyzed.</td><td></td></tr><tr><td>Attachments</td><td><p>The hash information of the file in a reported email is analyzed.</p><p>NOTE: The file itself is not analyzed, its hash data is analyzed.</p></td><td></td></tr></tbody></table>

#### **IBM X-Force API Key and Password Generating Steps**

1. First, go to the [IBM X-Force API Key generation process](https://www.ibm.com/account/reg/us-en/signup?formid=urx-30292). Sign up on the appropriate page, then confirm your account by clicking the verification link in the email that was delivered to your inbox.
2. To view the **Profile Summary**, click the user icon at the top right corner of the X-Force Exchange page.
3. To visit the **Settings** page, click the **Settings** link in the lower left corner. From there, click the **API Access** link to view the API information page.
4. To generate a brand-new API key and password, click the **Generate** button.
5. Before refreshing the page after creating an API key and password, save your API key and password information.

#### How to Integrate IBM X-Force into the Platform?

You can integrate the API key and password (which you obtained by following the steps in the '**IBM X-Force API Key and Password Creation** Steps' section) to the Incident Responder by the following steps below and benefit from its capabilities.

Click the **New** button on the relevant page, then fill in the fields:

<table data-header-hidden><thead><tr><th width="150"></th><th width="583.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select IBM X-force integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of the IBM X-force integration is defined automatically. Please do not change.</td><td></td></tr><tr><td>API Key</td><td>Define the API key.</td><td></td></tr><tr><td>API Password</td><td>Define the password for the API key.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure the API key and password are working correctly with the <strong>Test Connection</strong> button.</td><td></td></tr><tr><td>Tags</td><td>Tags are used to filter the integrations defined in the system.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave <strong>Default.</strong></td><td></td></tr><tr><td>URLs</td><td><p>URL analysis capability is enabled by default, you can disable it if needed.</p><p>Optionally, you can add it to the scanning process by selecting the "<strong>Hide URL Parameters</strong>" field.</p><p><strong>NOTE</strong>: With the Hide URL Parameters feature, instead of analyzing the entire URL address, only the relevant domain is analyzed.</p></td><td></td></tr><tr><td>Sender IP</td><td>Sender IP analysis capability is enabled by default, you can disable it if needed.</td><td></td></tr><tr><td>Attachments</td><td>File Hash analysis capability is enabled by default, you can disable it if needed.</td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

### **VirusTotal**

VirusTotal is a commercial threat analysis engine, also available in a free version. The VirusTotal analysis engine analyzes whether a reported email is malicious or not.

<table data-header-hidden><thead><tr><th width="150"></th><th width="583.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>URLs</td><td>URL addresses in a reported email are analyzed.</td><td></td></tr><tr><td>Attachments</td><td><p>Only the hash data of the file in a reported email is analyzed.</p><p><br>NOTE: The file itself is not analyzed, the Hash of the file is analyzed.</p></td><td></td></tr><tr><td>Sender IP</td><td>The sender email server IP address of a reported email is analyzed.</td><td></td></tr></tbody></table>

#### **VirusTotal API Key Creation Steps**

You must have a VirusTotal ID to use the VirusTotal API. After registering via the link [here](https://www.virustotal.com/gui/join-us), you must verify your account via the verification link you received.

Once verified, log into your VirusTotal account and view the API key from the API menu on your profile.

#### **How to Integrate VirusTotal?**

The API key obtained by applying the '**VirusTotal API Key Creation Steps**' can be integrated into the Incident Responder platform by following the steps below and its capabilities can be utilized.

Click the **New** button on the relevant page, then fill in the fields:

<table data-header-hidden><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select the Virustotal integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of the Virustotal integration is defined automatically. Please do not change.</td><td></td></tr><tr><td>API Key</td><td>Define the API key.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure the API key is working correctly with the <strong>Test Connection</strong> button<strong>.</strong></td><td></td></tr><tr><td>Detection Threshold</td><td>How many analyzing tools in Virustotal need to flag it as malicious for you to consider a link, attachment, or sender IP to be harmful in your analysis results?</td><td></td></tr><tr><td>Tags</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave Default.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave <strong>Default.</strong></td><td></td></tr><tr><td>URLs</td><td>URL analysis capability is enabled by default, you can disable it if needed.<br><br>Optionally, you can add it to the scanning process by selecting the "<strong>Hide URL Parameters</strong>" field.<br><br><strong>NOTE:</strong> With the Hide URL Parameters feature, instead of analyzing the entire URL address, only the relevant domain is analyzed.</td><td></td></tr><tr><td>Sender IP</td><td>Sender IP analysis capability is enabled by default, you can disable it if needed.</td><td></td></tr><tr><td>Cache</td><td>It recommends enabling to use of API key limits more effectively. If this option is enabled, the reported domain such as "test.com" results (undetected or phishing) will be saved, and when the same domain is requested to be analyzed again, the previous results (undetected or phishing) will be referenced until the X hours and Y times.<br><br>After exceeding the X hours or Y times query for the related domain, the domain will be analyzed via Virustotal and the same process will be working again.</td><td></td></tr><tr><td>Attachments</td><td>File Hash analysis capability is enabled by default, you can disable it if needed.</td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

### **Google Safe Browsing**

Google Safe Browsing is an analytics engine offered by Google for free. The Google Safe Browsing analysis engine analyzes whether a reported email is malicious.

<table data-header-hidden><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>URLs</td><td>URL addresses in a reported email are analyzed.</td><td></td></tr></tbody></table>

#### Google Safe Browsing API Key Creation Steps

1. **Sign in to the** [**Google Developers Console.**](https://console.cloud.google.com/apis/dashboard)
2. After opening the Dashboard from the left menu, click the Select a **Project button** above.
3. Click on the **New Project** button in the upper right corner of the new window, give the project a name and create the project with the **Create** button.
4. Open the left menu and click on the **Library** module.
5. Type **Safe Browsing** in the Search field. Then click on **Safe Browsing API**.
6. Click the **Enable** button in the new window.
7. Click **APIs & Services > Credentials** in the left menu.
8. Click the **Create Credentials** button at the top. Then click on **API Key.**
9. You can save your API key created here and use it in the necessary field on our platform.

Please note that you must enable billing for the project which you created in step 3.

#### How to Integrate Google Safe Browsing?

The API key obtained by applying the '**Google Safe Browsing API Key Creation Steps**' can be integrated on the Incident Responder platform by following the steps below and its capabilities can be utilized.

Click the **New** button on the relevant page, then fill in the fields:

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select the Google Safe Browsing integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of Google Safe Browsing integration is defined automatically. Please do not change.</td><td></td></tr><tr><td>API Key</td><td>Define the API key.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure the <strong>API key</strong> is working correctly with the <strong>Test Connection</strong> button.</td><td></td></tr><tr><td>Tags</td><td>You can filter the integrations defined in the system more easily by labeling them.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave <strong>Default</strong>.</td><td></td></tr><tr><td>URLs</td><td>URL analysis capability is enabled by default, you can disable it if needed.<br><br>Optionally, you can add it to the scanning process by selecting the "<strong>Hide URL Parameters</strong>" field.<br><br><strong>NOTE:</strong> With the Hide URL Parameters feature, instead of analyzing the entire URL address, only the relevant domain is analyzed.</td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

### Google Web Risk

Google Web Risk is an analytics engine offered by Google for free for up to 100.000 requests per month. The Google Web Risk analysis engine analyzes whether a reported email is malicious.

<table data-header-hidden><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>URLs</td><td>URL addresses in a reported email are analyzed.</td><td></td></tr></tbody></table>

#### **Google Web Risk API Key Creation Steps**

1. **Sign in to the** [**Google Developers Console.**](https://console.cloud.google.com/apis/dashboard)
2. After opening the Dashboard from the left menu, click the **Select a Project** button above.
3. Click on the **New Project** button in the upper right corner of the new window, give the project a name and create the project with the **Create** button.
4. Open the left menu and click on the **Library** module.
5. Type **Web Risk API** in the Search field. Then click on **Web Risk API.**
6. Click the **Enable** button in the new window.
7. Click **APIs & Services > Credentials** in the left menu.
8. Click the **Create Credentials** button at the top. Then click on **API Key**.
9. As the last step, you can save your API key created here and use it in the necessary field on our platform.

#### How to Integrate Google Web Risk?

The API key obtained by applying the '**Google Web Risk API Key Creation Steps**' can be integrated on the Incident Responder platform by following the steps below and its capabilities can be utilized.

Click the **New** button on the relevant page, then fill in the fields:

<table data-header-hidden><thead><tr><th width="150"></th><th width="585.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select the Google Web Risk integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of Google Web Risk integration is defined automatically. Please do not change.</td><td></td></tr><tr><td>API Key</td><td>Define the API key.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure the API key is working correctly with the Test Connection button.</td><td></td></tr><tr><td>Tags</td><td>You can filter the integrations defined in the system more easily by labeling them.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave Default.</td><td></td></tr><tr><td>URLs</td><td><p>URL analysis capability is enabled by default, you can disable it if needed.<br></p><p>Optionally, you can add it to the scanning process by selecting the "<strong>Hide URL Parameters</strong>" field.<br></p><p><strong>NOTE</strong>: With the Hide URL Parameters feature, instead of analyzing the entire URL address, only the relevant domain is analyzed.</p></td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

### Zen SpamHaus

Zen Spamhaus is a spam analysis engine made available for free by Spamhaus. SpamHaus spam analysis engine has the following capabilities and features to analyze whether a reported email is malicious or not.

SpamHaus integration does not use API keys, analysis is done over DNS.

<table data-header-hidden><thead><tr><th width="150"></th><th width="585.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Sender IP</td><td>The sender's email server IP address of a reported email is analyzed. If the sender's IP address has previously performed malicious or suspicious activity (e.g. Phishing or Blacklisted), you can see it on this interface.</td><td></td></tr></tbody></table>

#### **How to Integrate Zen SpamHaus?**

By following the steps below on the Incident Responder module, it can be integrated into the system and its capabilities can be utilized.

Click the **New** button on the relevant page, then fill in the fields below:

<table data-header-hidden><thead><tr><th width="150"></th><th width="583.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Choose Zen SpamHaus integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of the Zen SpamHaus integration is defined automatically.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure that the integration works correctly with the <strong>Test Connection</strong> button.</td><td></td></tr><tr><td>Tags</td><td>You can filter the integrations defined in the system more easily by labeling them.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave Default<strong>.</strong></td><td></td></tr><tr><td>Sender IP</td><td>Sender IP analysis capability is enabled by default, you can disable it if needed.</td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

### **FortiSandbox**

The FortiSandbox is a paid analysis engine offered by Fortinet has the following capabilities, and it automatically scans whether a reported email is malicious or not.

<table data-header-hidden><thead><tr><th width="150"></th><th width="585.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>URLs</td><td>URL addresses in a reported email are analyzed.</td><td></td></tr><tr><td>Attachments</td><td>The files in a reported email are analyzed.</td><td></td></tr></tbody></table>

#### **FortiSandbox API Key Creation Steps**

1. Use the FortiSandbox administration page to log in.
2. Go to the **Administrators** page in the left menu under the **System.**
3. By selecting the **Create** option from the menu, you can create a user.
4. For the relevant person, you can provide either a **Super Admin** or **Custom Role.**
5. Please go to the **Admin Profiles** under the **System** heading if you wish to define a **Custom** Role.
6. Save the relevant user's username and password.

#### **How to Integrate FortiSandbox?**

By following the steps below on the Incident Responder module, you can integrate it to our platform and utilize its capabilities.

Click the **New** button on the relevant page, then fill in the fields below on the new page.

<table data-header-hidden><thead><tr><th width="150"></th><th width="585.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select FortiSandbox integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of FortiSandbox integration is defined automatically. Please do not change.</td><td></td></tr><tr><td>API Key</td><td>Define the API key.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure the API key is working correctly with the Test button.</td><td></td></tr><tr><td>Tags</td><td>You can filter the integrations defined in the system more easily by labeling them.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave <strong>Default.</strong></td><td></td></tr><tr><td>URLs</td><td><p>URL analysis capability is enabled by default, you can disable it if needed.<br></p><p>Optionally, you can add it to the scanning process by selecting the"<strong>Hide URL Parameters</strong>" field.<br></p><p><strong>NOTE:</strong> With the Hide URL Parameters feature, instead of analyzing the entire URL address, only the relevant domain is analyzed.</p></td><td></td></tr><tr><td>Attachments</td><td><p>File Hash analysis capability is enabled by default, you can disable it if needed.<br></p><p>Optionally, you can add to the scanning process by selecting the “Upload PE files” and “Upload other file types” fields.</p></td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

### **Cyber X-Ray**

Cyber X-Ray is a commercial AI-powered threat analysis engine, also available in a free version created by Roksit. Cyber X-Ray artificial intelligence threat analysis engine has the following capabilities and it automatically scans whether a reported email is malicious or not thanks to the following features.

<table data-header-hidden><thead><tr><th width="150"></th><th width="586.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>URLs</td><td>URL addresses in a reported email are analyzed.</td><td></td></tr></tbody></table>

#### **Cyber X-Ray API Key Creation Steps**

1. Complete the registration process through the Roksit platform [here](https://portal.roksit.com/#/register).
2. Verify your account with the activation email sent to your email and log in to your account.
3. Click on **Settings > API Key** on the left menu.
4. Click the **Create New API Key** button in the upper right corner of the page that opens. Fill in the relevant fields in the API Key Information in the new window.
5. Click the **Save** button. Thus, a new API Key will be created, and save the new API key before closing this page.

#### **How to Integrate Cyber X-Ray?**

By following the steps below on the Incident Responder platform, it can be integrated and its capabilities can be used.

Click the New button on the relevant page, then fill in the following fields on the page that opens.

<table data-header-hidden><thead><tr><th width="150"></th><th width="583.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Choose Cyber X-Ray integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of Cyber X-Ray integration is defined automatically. Please do not change.</td><td></td></tr><tr><td>API Key</td><td>Define the API key.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure the API key is working correctly with the <strong>Test Connection</strong> button.</td><td></td></tr><tr><td>Tags</td><td>You can filter the integrations defined in the system more easily by labeling them.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave <strong>Default.</strong></td><td></td></tr><tr><td>URLs</td><td><p>URL analysis capability is active by default, you can disable it if needed.<br></p><p>You can optionally add it to the scanning process by selecting the "<strong>Hide URL Parameters</strong>" field.<br></p><p><strong>NOTE:</strong> With the Hide URL Parameters feature, only the domain name is analyzed instead of analyzing the entire URL address.</p></td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

### OPSWAT

OPSWAT is an analysis engine available to companies for a fee. OPSWAT analysis engine has the following capabilities and automatically scans to identify whether a reported email is malicious or not. If you have the OPSWAT product, you can integrate the Incident Responder platform.

<table data-header-hidden><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>URLs</td><td>URL addresses in a reported email are analyzed.</td><td></td></tr><tr><td>Sender IP</td><td>The sender email server IP address of a reported email is analyzed.</td><td></td></tr><tr><td>Attachments</td><td>Analysis of the files in a reported email is performed.</td><td></td></tr></tbody></table>

#### **How to create OPSWAT API?**

Please follow the steps below to create an API to use OPSWAT integration on the platform.

* Create an account on <https://my.opswat.com/register> and then log in.
* Go to the **Home > Licensed Products > Cloud-based Products** tab, and you can find the **API** **Key** on the same page.

#### **How to Integrate** OPSWAT\*\*?\*\*

By following the steps below on the Incident Responder platform, you can integrate OPSWAT and its capabilities.

Click the **New** button on the relevant page, then fill in the fields below:

<table data-header-hidden><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select OPSWAT integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of OPSWAT integration is defined automatically. If you are not using a cloud-based solution, you can enter the URL information of the product.</td><td></td></tr><tr><td>API Key</td><td>Enter the API key.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure the API key is working correctly with the <strong>Test Connection</strong> button.</td><td></td></tr><tr><td>Tags</td><td>You can filter the integrations defined in the system more easily by labeling them.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave Default.</td><td></td></tr><tr><td>URLs</td><td>URL analysis capability is enabled by default, you can disable it if needed.<br><br>Optionally, you can add it to the scanning process by selecting the "<strong>Hide URL Parameters</strong>" field.<br><br><strong>NOTE:</strong> With the Hide URL Parameters feature, only the domain name is analyzed instead of analyzing the entire URL address.</td><td></td></tr><tr><td>Sender IP</td><td>Sender IP analysis capability is active by default, you can disable it if needed.</td><td></td></tr><tr><td>Attachments</td><td>URL analysis capability is not enabled by default, you can enable it if needed. You can add to the scanning process by selecting the “Upload PE files” and “Upload other file types” fields.</td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

### **VMRay**

VMRay is an analysis engine available to companies for a fee. VMRay analysis engine has the following capabilities and automatically scans to identify whether a reported email is malicious or not. If you have the VMRay product, you can integrate the Incident Responder platform.

<table data-header-hidden><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>URLs</td><td>URL addresses in a reported email are analyzed.</td><td></td></tr><tr><td>Attachments</td><td>Dynamic and static analysis of the files in a reported email is performed.</td><td></td></tr></tbody></table>

#### **How to Integrate VMRay?**

By following the steps below on the Incident Responder platform, you can integrate VMRay and its capabilities to utilize.

Click the **New** button on the relevant page, then fill in the fields below:

<table data-header-hidden><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select VMRay integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of VMRay integration is defined automatically. If you are not using a cloud-based solution, you can enter the URL information of the product.</td><td></td></tr><tr><td>API Key</td><td>Define the API key.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure the API key is working correctly with the <strong>Test Connection</strong> button.</td><td></td></tr><tr><td>Tags</td><td>You can filter the integrations defined in the system more easily by labeling them.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave <strong>Default</strong>.</td><td></td></tr><tr><td>URLs</td><td>URL analysis capability is enabled by default, you can disable it if needed.<br><br>Optionally, you can add it to the scanning process by selecting the "<strong>Hide URL Parameters</strong>" field.<br><br><strong>NOTE:</strong> With the Hide URL Parameters feature, only the domain name is analyzed instead of analyzing the entire URL address.</td><td></td></tr><tr><td>Cache</td><td>It recommends enabling to use of API key limits more effectively. If this option is enabled, the reported domain such as "test.com" results (undetected or phishing) will be saved, and when the same domain is requested to be analyzed again, the previous results (undetected or phishing) will be referenced until the X hours and Y times.<br><br>After exceeding the X hours or Y times query for the related domain, the domain will be analyzed via Vmray and the same process will be working again.</td><td></td></tr><tr><td>Attachments</td><td><p>URL analysis capability is enabled by default, you can disable it if needed.<br></p><p>Optionally, you can add to the scanning process by selecting the “Upload PE files” and “Upload other file types” fields.</p></td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>

### AnyRun

AnyRun is a tool for the detection, monitoring, and research of cyber threats in real-time. The service is available in free demo trial and licensed versions. The AnyRun threat analysis engine analyzes whether a reported email is malicious or not using the following capabilities.

<table><thead><tr><th width="150"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>URLs</td><td>URL addresses in a reported email are analyzed.</td><td></td></tr><tr><td>Attachments</td><td>The original file itself in a reported email is analyzed. <strong>Please note</strong> if you enable the Attachment scan option, the original file in the reported email will be uploaded and analyzed in AnyRun cloud services.</td><td></td></tr></tbody></table>

#### **AnyRun API Key Generating Steps**

1. Go to the [AnyRun website](https://any.run/) and sign up for a free trial or purchase a license.
2. Go to your profile.
3. Click on the API and Limits menu.
4. Copy your API key.

#### How to Integrate AnyRun into the Platform?

After you copy your API key, go to the Incident Responder by the following steps below and benefit from AnyRun capabilities.

Click the **New** button on the relevant page, then fill in the fields:

<table data-header-hidden><thead><tr><th width="150"></th><th width="583.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Name</td><td>Name of the Integration.</td><td></td></tr><tr><td>Description</td><td>Description of the integration.</td><td></td></tr><tr><td>Integration Type</td><td>Select AnyRun integration.</td><td></td></tr><tr><td>API URL</td><td>The URL address of the AnyRun integration is defined automatically. Please do not change.</td><td></td></tr><tr><td>API Key</td><td>Define the API key.</td><td></td></tr><tr><td>Test Connection</td><td>Make sure the API key is working correctly with the <strong>Test Connection</strong> button.</td><td></td></tr><tr><td>Tags</td><td>Tags are used to filter the integrations defined in the system.</td><td></td></tr><tr><td>Proxy</td><td>You can choose the proxy server that the platform will use for the connections to the integration. If not, leave <strong>Default.</strong></td><td></td></tr><tr><td>URLs</td><td><p>URL analysis capability is enabled by default; you can disable it if needed.</p><p>Optionally, you can add it to the scanning process by selecting the "<strong>Hide</strong></p><p><strong>URL Parameters</strong>" field.</p><p><strong>NOTE</strong>: With the Hide URL Parameters feature, instead of analyzing the entire URL address, only the relevant domain is analyzed.</p></td><td></td></tr><tr><td>Attachments</td><td>The attachment analysis capability is disabled by default, you can enable it if needed.</td><td></td></tr><tr><td>Status</td><td>Integration is active by default, you can disable the integration if needed.</td><td></td></tr></tbody></table>
