# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/keepnet-tools-allow-listing-guidelines.md

# Keepnet Tools Allow Listing Guidelines

It's important to note that both the Phishing Reporter and Diagnostic Tool are legitimate and secure applications developed by Keepnet Labs. They have been thoroughly tested and should not trigger any issues with Antivirus or Endpoint Detection and Response (EDR) solutions under normal circumstances.

However, specific configurations or strict policies within Antivirus, EDR, or other security tools may sometimes lead to these applications being blocked or their functionality being restricted. This can occur despite the applications being entirely safe and free of malicious code. It is these particular scenarios that the "Keepnet Labs Tools Allow Listing Guidelines" document aims to address.

By following the steps outlined in this guide, including the calculation and allow listing of the unique hash of the downloaded files, customers can ensure the seamless operation of the Phishing Reporter and Diagnostic Tool within their unique security environments.

Indeed, each enterprise has a unique set of security tools and configurations in place to secure its environment. These tools, while effectively preventing threats, can sometimes interfere with legitimate applications and tools such as the Phishing Reporter and Diagnostic Tool from Keepnet Labs. They may hinder these applications' functionality or block their network communications.

To address this issue, Keepnet Labs recommends a Proof of Concept (PoC) test where enterprises can see how their security solutions interact with the Phishing Reporter and Diagnostic Tool. This PoC allows Keepnet Labs and the enterprise to identify potential conflicts, adjust settings, or create necessary exceptions to ensure the tools work smoothly.

However, in cases where enterprises want to ensure the uninterrupted operation of Keepnet Labs' tools, a allow listing document is provided. This document is a comprehensive list of all the potential tools and configurations that may need to be adjusted to allow for full functionality. By following the allow listing document, enterprises can ensure that the Phishing Reporter and Diagnostic Tool will operate as intended within their network environment.

## Understanding the Phishing Reporter and Diagnostic Tool

[**Phishing** **Reporter**](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization) is a tool that allows users to easily report suspicious emails and contribute to the organization's security by reinforcing its human firewall. By installing this tool on their devices, users have a straightforward mechanism to report potentially harmful emails directly from their mailbox interface. Phishing Reporter communicates with the Keepnet Labs platform via the <https://api.keepnetlabs.com/api/\\>\* network route.

[**Diagnostic** **Tool**](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/diagnostic-tool) is an auxiliary service as part of the Phishing Reporter suite. It is designed to help troubleshoot potential issues with the Phishing Reporter. When issues arise, the Diagnostic Tool gathers necessary system information to assist Keepnet Labs' support teams to quickly identify and solve the problem. This tool also uses the same network route as the Phishing Reporter, i.e., <https://api.keepnetlabs.com/api/\\>\*.

## Essential Allow Listing Checklist for Security Software

The below checklist provides a guideline for the allow listing process in different security software categories:

<table><thead><tr><th width="132">Security Tool</th><th width="142">Allow Listing Component</th><th>Description</th></tr></thead><tbody><tr><td>Anti-Virus</td><td>File-based Exception</td><td>The downloaded executable files (Phishing Reporter and Diagnostic Tool) need to be added to the exceptions in your antivirus software.</td></tr><tr><td>EDR</td><td>File-based Exception</td><td>Add the hash of the downloaded files (Phishing Reporter and Diagnostic Tool) to the exceptions in your EDR system.</td></tr><tr><td>Proxy</td><td>URL Exception</td><td>Add https://api.keepnetlabs.com/api/ and https://addin-api.keepnetlabs.com/api/ to your proxy server's exception list to allow network communications.</td></tr><tr><td>DLP</td><td>Data Transfer Exception</td><td>Configure your DLP to allow data transfer to https://api.keepnetlabs.com/api/ and https://addin-api.keepnetlabs.com/api/</td></tr><tr><td>DDoS Prevention</td><td>IP/URL Exception</td><td>DDoS Prevention tools should be configured to allow incoming and outgoing traffic to https://api.keepnetlabs.com/api/ and https://addin-api.keepnetlabs.com/api/. This will ensure uninterrupted communication with the Keepnet Labs server.</td></tr></tbody></table>

It's critical to verify the integrity of the downloaded Phishing Reporter and Diagnostic Tool through their unique hash values. Once you download these applications, you should calculate their hash and allow list this hash value in the respective security solutions. This process ensures that you're using the legitimate version of the tools and it hasn't been tampered with during the download process.

Here's how you can calculate the hash of a file on different platforms:

Replace **'yourfilename.exe'** with the actual filename of the downloaded file.

* **Windows:** You can use the built-in 'CertUtil' tool. Open the Command Prompt, navigate to the directory where your file is located, and then use the following command:
  * **certutil -hashfile yourfilename.exe SHA256**
* **Linux:** The 'sha256sum' tool is usually available by default. Open the terminal, navigate to the directory containing the file, and then use the following command:
  * **sha256sum yourfilename**
* **Mac OS:** You can use the built-in 'shasum' command. Open the Terminal, navigate to the directory where your file is located, and then use the following command:
  * **shasum -a 256 yourfilename**

## Allow Listing Procedures for Various Security Products

### 1. Symantec Antivirus

Symantec Antivirus provides both file and network-based protection. Therefore, you need to allow list the application executables as well as the network communications.

* **File-Based Exceptions:** Open your Symantec Antivirus, go to Settings > Exceptions > Add Exception > Security Risk Exception > File. Then, locate the Phishing Reporter and Diagnostic Tool executables and add them as exceptions. Please ensure to verify the hash of the downloaded files to ensure their integrity.
* **Network-Based Exceptions:** Go to Settings > Exceptions > Add Exception > Security Risk Exception > Known Risk. Add <https://api.keepnetlabs.com/api/\\>\* to the exceptions to ensure that network communications are not blocked.

### 2. Palo Alto Proxy

To allow list network communications in Palo Alto Proxy, you need to create a custom URL category.

* **Custom URL Category:** Go to Objects > Custom Objects > URL Category > Add. Name the new category (e.g., "Keepnet Labs"). In the Sites section, add \*.keepnetlabs.com/\*. Apply the changes.
* **URL Filtering:** Create or modify a URL Filtering profile to allow the new custom URL category. This can be done in Objects > Security Profiles > URL Filtering.

### 3. Forcepoint DLP

For Forcepoint DLP, create a new rule to allow data to be sent to Keepnet Labs' server.

* **New Rule:** Go to DLP Policy Manager > File > New > DLP Policy > Rule > Add. In the new rule, set "Endpoint" as the Data Endpoint. Under "Destinations", add <https://api.keepnetlabs.com/api/\\>\*. Under "Actions", select "Allow". Name and save the new rule.

### 4. CrowdStrike Falcon

CrowdStrike Falcon uses a cloud-based system to handle threats. Allow Listing can be done through the Falcon console.

* **Prevention Policy Allow Listing:** Log into the Falcon console. Navigate to Configuration > Prevention Policies. Select the policy to which you wish to add the exceptions. Under the 'Exclusions' section, click on 'Add New' > 'File'. In the dialog box, enter the SHA-256 hash of the Phishing Reporter and Diagnostic Tool files. Make sure to calculate the hash of the downloaded files to ensure their integrity. Set the 'Type' as 'Whitelist' and the 'Platform' as per your environment (Windows, Linux, or macOS). Add a description for your reference, and save the changes.
* **Network Allow Listing:** In the same policy configuration, navigate to the 'IOCs' section. Click on 'Add New' > 'Indicator'. Add <https://api.keepnetlabs.com/api/\\>\* as an Indicator, select 'Network' as the type, and select 'Whitelist' as the action. Save the changes.

## Need Help? Contact Support Team

For additional assistance or questions regarding the implementation and usage of our products, please contact our support team at <support@keepnetlabs.com>. Keepnet Labs is committed to supporting our customers at every step, providing necessary insights and assistance to ensure the successful implementation and usage of our products.
