# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment.md

# Phishing Reporter Deployment

This section describes in detail how to deploy the Phishing Reporter add-in to users in Microsoft 365, Exchange, or Google Workspace platforms.

For instructions on the required initial installation of the add-in, please refer to the explanation provided here: [Phishing Reporter Customization](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-customization).

## Shortcuts

* [How to Deploy Microsoft Ribbon Phishing Reporter](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/microsoft-ribbon-phishing-reporter)
* [How to Deploy Microsoft Page View Phishing Reporter](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/microsoft-page-view-phishing-reporter)
* [How to Deploy the Add-in in Exchange Admin Center](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/how-to-deploy-the-add-in-in-exchange-admin-center)
* [How to Deploy the Add-in in Google Workspace](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/how-to-deploy-the-add-in-in-google-workspace)
* [Phishing Reporter Announcement Email Template](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/phishing-reporter-announcement-email-template)

## Comparison: Ribbon vs Page View vs MSI Outlook Phishing Reporter (Microsoft 365)

Use this chart to determine which **Phishing** **Reporter** add-in is best suited for your **Microsoft 365 environment.** The right choice depends on how your employees access Outlook—whether through desktop apps, web browsers, or mobile devices.

| Feature / Platform                              | Ribbon Phishing Reporter                             | Page View Phishing Reporter                          | MSI Outlook Add-in                             |
| ----------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------- |
| **Outlook on Windows (Classic)**                | ✅ Supported (only version 2404 build 17530.15000)    | ✅ Supported                                          | ✅ Supported                                    |
| **Outlook on Windows (New)**                    | ✅ Supported                                          | ✅ Supported                                          | ❌ Not Supported                                |
| **Outlook Classic 2016+ on Windows (Exchange**) | ❌ Not Supported                                      | ✅ Supported                                          | ✅ Supported                                    |
| **Outlook on MacOS (Microsoft 365)**            | ✅ Supported (Version 16.81 (23121700) or later)      | ✅ Supported                                          | ❌ Not Supported                                |
| **Outlook on MacOS (Exchange)**                 | ❌ Not Supported                                      | ❌ Not Supported                                      | ❌ Not Supported                                |
| **Outlook on Web MacOS (Exchange)**             | ❌ Not Supported                                      | ✅ Supported                                          | ❌ Not Supported                                |
| **Outlook on the Web (Microsoft 365)**          | ✅ Supported                                          | ✅ Supported                                          | ❌ Not Supported                                |
| **Outlook on the Web (Exchange)**               | ❌ Not Supported                                      | ✅ Supported                                          | ❌ Not Supported                                |
| **Outlook on iOS (Microsoft 365)**              | ❌ Not Supported                                      | ✅ Supported                                          | ❌ Not Supported                                |
| **Outlook on Android (Microsoft 365)**          | ❌ Not Supported                                      | ✅ Supported                                          | ❌ Not Supported                                |
| **Outlook on iOS (Exchange)**                   | ❌ Not Supported                                      | ❌ Not Supported                                      | ❌ Not Supported                                |
| **Outlook on Android (Exchange)**               | ❌ Not Supported                                      | ❌ Not Supported                                      | ❌ Not Supported                                |
| **Shared Mailboxes (Outlook Desktop)**          | ❌ Not Supported                                      | ❌ Not Supported                                      | ✅ Supported (only within Classic Outlook)      |
| **Shared Mailboxes (Microsoft 365)**            | ❌ Not Supported                                      | ❌ Not Supported                                      | ❌ Not Supported                                |
| **Mobile Browser (OWA)**                        | ❌ Not Supported                                      | ❌ Not Supported                                      | ❌ Not Supported                                |
| **Installation Method**                         | Deploy via Microsoft 365 Admin Center (Manifest XML) | Deploy via Microsoft 365 Admin Center (Manifest XML) | Manual deployment via GPO or SCCM Tools        |
| **User Experience**                             | Ribbon button                                        | Side panel in reading view                           | Ribbon button (Classic Outlook interface only) |

## FAQ

### Q: The add-in was deployed to one of the listed email servers more than 12 hours ago but is still not visible on users' email applications. What can I do?

A: You can try to re-deploy the add-in. If it still does not appear, you should contact the support team of the email service provider.

### **Q: Can an Attacker hijack Outlook Add-in?**

A: The platform uses “Code Signing with Microsoft Authenticode” to protect tools against hacking attempt. For more information, please [click here](https://www.digicert.com/dc/code-signing/microsoft-authenticode.htm)​.

### **Q: Is it possible to centralise the distribution of add-in?**

A: Yes, it is. Many institutions manage the add-in (install, uninstall, enable, disable) with central administration tools, such as Microsoft SCCM, IBM Bigfix.

### Q: Does the Phishing Reporter Add-In work with the Outlook application on iOS?

A: Yes, if you distribute the Phishing Reporter Add-In as an XML package (Microsoft 365), it will be available in both OWA/Outlook applications and will also function within the Outlook application on iOS.

### **Q: Does the Phishing Reporter Add-In work in shared mailboxes in O365?**

**A:** The add-in works in shared mailboxes in the Outlook Desktop Application. However, it is not supported in shared mailboxes in OWA (Outlook Web Access).

### **Q: Does the new Outlook application on Windows 11 support MSI-based add-ins?**

**A:** No, the new Outlook application on Windows 11 does not support MSI-based add-ins. It is designed to work primarily with web-based add-ins such as [XML add-in of Keepnet Phishing Reporter](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/how-to-deploy-the-add-in-in-microsoft-365). If you need MSI-based add-ins, we recommend using the classic Outlook for Windows desktop application. For more information, please find information under the "Extensibility" section in this [document](https://support.microsoft.com/en-us/office/feature-comparison-between-new-outlook-and-classic-outlook-de453583-1e76-48bf-975a-2e9cd2ee16dd).

### Q: Can I use the O365 XML Add-In on OWA in a mobile browser?

A: No, you can't use the add-in if you open OWA in a mobile browser. Microsoft 365 does not support third-party add-ins in mobile browsers for OWA. Please use the Outlook app instead.
