# Source: https://docs.asapp.com/ai-productivity/ai-compose/deploying-ai-compose-for-liveperson.md

# Deploying AI Compose for LivePerson

> Use AI Compose on your LivePerson application.

## Overview

This page describes how to Integrate AI Compose in your LivePerson application.

### Integration Steps

There are four parts to the AI Compose setup process. Use the links below to skip to information about a specific part of the process:

1. [Install the ASAPP browser extension](#1-install-the-asapp-browser-extension) on all agents' desktop (via a system policy or using your company's existing deployment processes)
2. [Configure the LivePerson organization](#2-configure-liveperson) centrally using an administrator account
3. [Setup agent/user authentication](#3-set-up-single-sign-on) through the existing single sign-on (SSO) service
4. [Work with your ASAPP contact to configure Auto-Pilot Greetings](#4-configure-auto-pilot-greetings), if desired

## Requirements

**Browser Support**

ASAPP AI Compose is supported in Google Chrome and Microsoft Edge

* NOTE: This support covers the latest version of each browser and extends to the previous two versions

Please consult your ASAPP account contact if your installation requires support for other browsers

**LivePerson**

ASAPP supports LivePerson's Messaging conversation type

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25692af3-f40a-506d-128f-9b57931ae9b1.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=02b81669d00a7709f69a50fb818ab925" data-og-width="560" width="560" data-og-height="253" height="253" data-path="image/uuid-25692af3-f40a-506d-128f-9b57931ae9b1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25692af3-f40a-506d-128f-9b57931ae9b1.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=bc6c61ee2e9df9941fa3bc5752df0c4d 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25692af3-f40a-506d-128f-9b57931ae9b1.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=9f11caca8deb598a5e55232aaf5b3557 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25692af3-f40a-506d-128f-9b57931ae9b1.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=b92e559254a0ac1f32c1192eeadf4c43 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25692af3-f40a-506d-128f-9b57931ae9b1.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=777316bc295c4e388af562dea49982b7 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25692af3-f40a-506d-128f-9b57931ae9b1.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=6982e50522819d74b20f5c3d9aeace8f 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25692af3-f40a-506d-128f-9b57931ae9b1.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d734c76de25e95c374e2d5ba72b9b760 2500w" />
</Frame>

**SSO Support**

The AI Compose widget supports SP-initiated SSO with either OIDC (preferred method) or SAML.

**Domain Whitelisting**

In order for AI Compose to interact with ASAPP's backend and third-party support services, the following domains need to be accessible from end-user environments:

| Domain                                     | Description                                                        |
| :----------------------------------------- | :----------------------------------------------------------------- |
| \*.asapp.com                               | ASAPP service URLs                                                 |
| \*.ingest.sentry.io                        | Application performance monitoring tool                            |
| fonts.googleapis.com                       | Fonts                                                              |
| google-analytics.com                       | Page analytics                                                     |
| asapp-chat-sdk-production.s3.amazonaws.com | Static ASAPP AWS URL for desktop network connectivity health check |

**Policy Check**

Before proceeding, check the current order of precedence of policies deployed in your organization. Platform-deployed policies (like Group Policy Objects) and cloud-deployed policies (like Google Admin Console) are enforced in a priority order that can lead to lower-priority policies not being enforced.

* If installing the ASAPP browser extension via Group Policy Objects, set platform policies to have precedence over cloud policies.
* If installing the ASAPP browser extension via Google Admin Console, set cloud policies to have precedence over platform policies.
  For more on how to check and modify order of precedence, see [policy management guides from Google Enterprise](https://support.google.com/chrome/a/answer/9037717).

## Integrate with LivePerson

### 1. Install the ASAPP Browser Extension

Customers have two options for installing the AI Compose browser extension:

A.  Group Policy Objects (GPO)

B.  Google Admin Console

#### A. Install Group Policy Objects (GPO)

Customers can automatically install and manage the ASAPP AI Compose browser extension via Group Policy Objects (GPO). ASAPP provides an installation server from which the extension can be downloaded and automatically updated.

The Customer's system administrator must configure GPO rules to allow the installation server URL and the software component ID. Through GPO, the administrator can choose to force the installation (i.e., install without requiring human intervention).

The following policies will configure Chrome and Edge to download the AI Compose browser extension in all on-premise managed devices via GPO:

| **Policy Name**                                                                                                         | **Value to Set**                                                                                                                                                                |
| :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [ExtensionInstallSources](https://cloud.google.com/docs/chrome-enterprise/policies/?policy=ExtensionInstallSources)     | https\://\*.asapp.com/\*                                                                                                                                                        |
| [ExtensionInstallAllowlist](https://cloud.google.com/docs/chrome-enterprise/policies/?policy=ExtensionInstallAllowlist) | bfcmlmledhddbnialbbdopfefoelbbei                                                                                                                                                |
| [ExtensionInstallForcelist](https://cloud.google.com/docs/chrome-enterprise/policies/?policy=ExtensionInstallForcelist) | bfcmlmledhddbnialbbdopfefoelbbei;[https://app.asapp.com/autocompose-liveperson-chrome-extension/updates](https://app.asapp.com/autocompose-liveperson-chrome-extension/updates) |

Each Policy Name above links to documentation that describes how to set the values with the proper format depending on the platform.

<Note>
  When policy changes occur, you may need to reload policies manually or force restart the browser to ensure newly deployed policies are applied.
</Note>

Figure 2 shows example policy files for the Windows platform. The policy adds the URL 'https\://\*.asapp.com/\*' as a valid extension install source, allows the extension ID 'bfcmlmledhddbnialbbdopfefoelbbei', and forces the extension installation.

Google Chrome:

```registry  theme={null}
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome]
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\ExtensionInstallAllowlist]
"1"="bfcmlmledhddbnialbbdopfefoelbbei"
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\ExtensionInstallSources]
"1"="https://*.asapp.com/*"
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\ExtensionInstallForcelist]
"1"="bfcmlmledhddbnialbbdopfefoelbbei;https://app.asapp.com/autocompose-liveperson-chrome-extension/updates”
```

Microsoft Edge:

```registry  theme={null}
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge]
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\ExtensionInstallAllowlist]
"1"="bfcmlmledhddbnialbbdopfefoelbbei"
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\ExtensionInstallSources]
"1"="https://*.asapp.com/*"
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\ExtensionInstallForcelist]
"1"="bfcmlmledhddbnialbbdopfefoelbbei;https://app.asapp.com/autocompose-liveperson-chrome-extension/updates”
```

Figure 2: Example policy files to install the AI Compose browser extension in Google Chrome and Microsoft Edge browsers respectively (*Windows Registry*)

#### B. Install via Google Admin Console

For Google Chrome deployments, customers can install and manage the ASAPP AI Compose browser extension using Managed Chrome Device policies in the Google Admin console. The Customer's system administrator must set up the AI Compose browser extension through the Google Admin console by creating a custom app and configuring the extension ID and XML manifest URL. Through managed Chrome policies the administrator can choose to force the installation (i.e. install without requiring human intervention).

In order to have Chrome download the ASAPP hosted extension in all managed devices through the Google Admin console:

1. Navigate to **Device management > Chrome**.
2. Click **Apps & Extensions**.
3. Click on **Add (+)** and look for **Add Chrome app or extension by ID** option.
4. Complete the fields using the values provided below. Be sure to select the **From a custom URL** option.

| **Field** | **Value**                                                                                                                                      |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| ID        | bfcmlmledhddbnialbbdopfefoelbbei                                                                                                               |
| URL       | [https://app.asapp.com/autocompose-liveperson-chrome-extension/updates](https://app.asapp.com/autocompose-liveperson-chrome-extension/updates) |

Please check Google's [Managing Extensions in Your Enterprise](https://docs.google.com/document/d/1pT0ZSbGdrbGvuCsVD2jjxrw-GVz-80rMS2dgkkquhTY/edit#heading=h.ojow7ntunwpx) for more information.

<Note>
  To ensure that cloud policies are enabled for production environment users in a given organizational unit, locate that group of users by navigating to **Devices** > **Chrome** > **Settings** menu in Google Suite.

  Ensure the setting **[Chrome management for signed-in users](https://support.google.com/chrome/a/answer/2657289?hl=en#zippy=%2Cchrome-management-for-signed-in-users)** is set to **Apply all user policies when users sign into Chrome, and provide a managed Chrome experience.**
</Note>

**Testing**

The following two checks on a target machine will verify the extension is installed correctly:

1. **The extension is force-installed in the browser**
   a.  Expand the extension icon in the browser toolbar.
   b.  Alternatively, navigate to chrome://extensions/ or edge://extensions/ and look for 'ASAPP Extension'
   c.  Alternatively, navigate to edge://extensions/ and look for 'ASAPP Extension'
2. **The extension is properly configured**
   a.  Click the extension icon and validate that the allowlist and denylist values in the extension's options are as they were set.
   b.  Alternatively, navigate to chrome://policy and search for the extension policies.
   c.  Alternatively, navigate to edge://policy and search for the extension policies.

### 2. Configure LivePerson

**Before You Begin**

You will need the following information to configure ASAPP for LivePerson:

* The URL for your custom widget, which will be provided to you by ASAPP

* Credentials to login to your LivePerson organization as an administrator

**Configuration Steps**

1. **Add New Widget**
   * Open the LivePerson website and login as an administrator.
   * Go to 'agent workspace' and click **Night Vision**, in the top right:
     <Frame>
       <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0fc19664-1fdd-cae9-f0e1-deb3a73b1c54.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b4a2b77224e00250ae6f35b342c5f5e1" data-og-width="248" width="248" data-og-height="154" height="154" data-path="image/uuid-0fc19664-1fdd-cae9-f0e1-deb3a73b1c54.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0fc19664-1fdd-cae9-f0e1-deb3a73b1c54.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=590729aec62bce996c83542d1a1837d4 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0fc19664-1fdd-cae9-f0e1-deb3a73b1c54.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=99e9f513add25df3c379e1c5a116caa7 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0fc19664-1fdd-cae9-f0e1-deb3a73b1c54.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=24cf9a1077c79466e536cd7f318c7f99 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0fc19664-1fdd-cae9-f0e1-deb3a73b1c54.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=76e204314d111eb7989421fd2772ef36 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0fc19664-1fdd-cae9-f0e1-deb3a73b1c54.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=2794fd1c6c124ea055fb44cb12f71ae8 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0fc19664-1fdd-cae9-f0e1-deb3a73b1c54.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=3632fe52cb6533cd2a21d6c8c3c66b4f 2500w" />
     </Frame>
   * Click +, then **Add new widget**.
     <Frame>
       <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d4ab75f3-3c1a-7d12-e5e7-77d35f5dcebf.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=0c1f4474c53ce745c307a70ec48e27b4" data-og-width="376" width="376" data-og-height="163" height="163" data-path="image/uuid-d4ab75f3-3c1a-7d12-e5e7-77d35f5dcebf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d4ab75f3-3c1a-7d12-e5e7-77d35f5dcebf.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=47b2d3a445c2a05ebecd2ff391e98a30 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d4ab75f3-3c1a-7d12-e5e7-77d35f5dcebf.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=2de121427b46a1f89d84160527a0c9e4 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d4ab75f3-3c1a-7d12-e5e7-77d35f5dcebf.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=98b44f5699a2ebb22d409125a59a1529 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d4ab75f3-3c1a-7d12-e5e7-77d35f5dcebf.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=5fdb8228166648472c7940ee9c73d270 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d4ab75f3-3c1a-7d12-e5e7-77d35f5dcebf.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=31d3034ece31ba273d45e12cc2bc4363 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d4ab75f3-3c1a-7d12-e5e7-77d35f5dcebf.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=36194d604b277f2a0fd1f3adcce19f69 2500w" />
     </Frame>
2. **Enter Widget Attributes**
   * Fill in the **Widget name** as 'ASAPP'
   * Assign the conversation skill(s) to which ASAPP is being deployed in the **Assigned skills** dropdown menu.
     <Caution>
       Leaving **Assigned skills** blank will show the ASAPP widget for all conversation regardless of skill.
     </Caution>
   * Enter the URL that contains the API key you were provided by your ASAPP account contact for your custom widget in the **URL** field.

     <Note>
       When configuring for a sandbox environment, use this URL format: `https://app.asapp.com/autocompose-liveperson/autocompose.html?apikey=\{your_sandbox_api_key\}&asapp_api_domain=api.sandbox.asapp.com`

       When configuring for a production environment, use this URL format: `https://app.asapp.com/autocompose-liveperson/autocompose.html?apikey=\{your_prod_api_key\}`
     </Note>

     <Frame>
       <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-763a008b-cd5b-688f-8cc6-0bd15ad1db91.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1baab0c12f5bde83ce00d3885fce0926" data-og-width="770" width="770" data-og-height="956" height="956" data-path="image/uuid-763a008b-cd5b-688f-8cc6-0bd15ad1db91.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-763a008b-cd5b-688f-8cc6-0bd15ad1db91.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=636bf1936d2fe7784655fb24af6d9c65 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-763a008b-cd5b-688f-8cc6-0bd15ad1db91.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1fa299f2293f38811c7de0b3e559232f 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-763a008b-cd5b-688f-8cc6-0bd15ad1db91.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=940b7ae46f0264a254631a09d95ce1be 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-763a008b-cd5b-688f-8cc6-0bd15ad1db91.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=a0a285491ba513910fe30961ed2ab9e0 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-763a008b-cd5b-688f-8cc6-0bd15ad1db91.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=890358336711c5bf2426f1304fa1cf83 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-763a008b-cd5b-688f-8cc6-0bd15ad1db91.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=dc4b0aa72a8e8ffc141cd76707900da3 2500w" />
     </Frame>
   * Click the **Save** button.
     <Note>
       Ensure **Hide** and **Manager View** are unselected once you are ready for agents to see the widget for conversations with the assigned skill(s).

       <Frame>
         <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4d3271ac-3a6a-9deb-af4a-fdd5061ea20d.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=bc490193e78bf93e23825c33db2b440a" data-og-width="322" width="322" data-og-height="322" height="322" data-path="image/uuid-4d3271ac-3a6a-9deb-af4a-fdd5061ea20d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4d3271ac-3a6a-9deb-af4a-fdd5061ea20d.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=595ec8799464e2e70713d879cd683eed 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4d3271ac-3a6a-9deb-af4a-fdd5061ea20d.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=33cb50776da70d4bb0f309bd601405e1 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4d3271ac-3a6a-9deb-af4a-fdd5061ea20d.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a3ca56c43d21a368fd3747f8566f5596 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4d3271ac-3a6a-9deb-af4a-fdd5061ea20d.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=55e6c99d7a6c26fa68d04bb1cfa4c922 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4d3271ac-3a6a-9deb-af4a-fdd5061ea20d.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=b7ebd6bc694e90825d6cca9059244c01 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4d3271ac-3a6a-9deb-af4a-fdd5061ea20d.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=0e45c8e0c0c66e42d6e511c052b54281 2500w" />
       </Frame>
     </Note>
3. **Move Widget to Top**
   * Click the **Organize** button
   * Scroll down to the ASAPP widget, and click the **Move top** button:
     <Frame>
       <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13d78edd-6c73-7c9d-65a9-edfe08088a33.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b7ed923f3c046293a1628fcb4bc358f2" data-og-width="483" width="483" data-og-height="115" height="115" data-path="image/uuid-13d78edd-6c73-7c9d-65a9-edfe08088a33.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13d78edd-6c73-7c9d-65a9-edfe08088a33.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=ef5f4bd2fa6b444fba39ad88119f60e2 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13d78edd-6c73-7c9d-65a9-edfe08088a33.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=cc56695b3f271a48ba467e2413ff7669 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13d78edd-6c73-7c9d-65a9-edfe08088a33.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b3091441f5e6763d0dc33f0120c79364 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13d78edd-6c73-7c9d-65a9-edfe08088a33.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=75248d1f978ae60610c8df6c0c6d4b05 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13d78edd-6c73-7c9d-65a9-edfe08088a33.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=46494b490c5b3f4e14824c36c234c2cd 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-13d78edd-6c73-7c9d-65a9-edfe08088a33.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=d6842701f2b3cd92e17ecb7a7b37851d 2500w" />
     </Frame>
   * Click the **Done** button
4. **Enable Pop-in Composer**
   * In the Agent Workspace, click the nut icon (similar to a gear shape) next to the **+** icon at the bottom of the AI Compose panel widget.
   * Enable the **Pop-in Composer** option.
     <Frame>
       <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3001d768-5dfb-e02e-24fa-6adcb8e513b4.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=b6206ae82c25ed75482a670facaf4352" data-og-width="1230" width="1230" data-og-height="404" height="404" data-path="image/uuid-3001d768-5dfb-e02e-24fa-6adcb8e513b4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3001d768-5dfb-e02e-24fa-6adcb8e513b4.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a77db78a0898256118cb380b2ace0b9f 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3001d768-5dfb-e02e-24fa-6adcb8e513b4.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0496387f7f6334e8f2f8b0bb3efd67fb 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3001d768-5dfb-e02e-24fa-6adcb8e513b4.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=184631cdb58199cb8dae8100e8fec9ca 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3001d768-5dfb-e02e-24fa-6adcb8e513b4.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=7fe89888ec8eebd61aa12c816cf3fee6 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3001d768-5dfb-e02e-24fa-6adcb8e513b4.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e237807c21ac7871abd03b005d055397 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3001d768-5dfb-e02e-24fa-6adcb8e513b4.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=ea58132e2ff7b6ebd83a5856a1acb893 2500w" />
     </Frame>

Press the escape key and reload the page to see the changes; the ASAPP widget should now be available across your LivePerson organization

Upon login to the Agent Workspace, the ASAPP widget for AI Compose will appear in place of the standard LivePerson composer, underneath the conversation transcript. By default, the response panel for AI Compose will appear to the right of the conversational panel.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4b2626ec-266c-fbcf-f28f-0c10080ea306.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6b598672fe1d2420fe97c77a0dd0388a" data-og-width="1820" width="1820" data-og-height="1138" height="1138" data-path="image/uuid-4b2626ec-266c-fbcf-f28f-0c10080ea306.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4b2626ec-266c-fbcf-f28f-0c10080ea306.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=96278b047df461cda31397e859a2dbf1 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4b2626ec-266c-fbcf-f28f-0c10080ea306.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=4f2d6da4ae211afd5eaa0eb2df0572dc 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4b2626ec-266c-fbcf-f28f-0c10080ea306.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a063e13414e360163dbcaa40a7009bb8 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4b2626ec-266c-fbcf-f28f-0c10080ea306.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=427ae3a7bba3d847478f924a4a1eaa32 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4b2626ec-266c-fbcf-f28f-0c10080ea306.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=c15cab3f32adb1b597117da2c3953b65 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4b2626ec-266c-fbcf-f28f-0c10080ea306.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=25381363f4db315f69f834da3c8700df 2500w" />
</Frame>

### 3. Set Up Single Sign-On

ASAPP handles authentication through the customer's SSO service to confirm the identity of the agent.

ASAPP acts as the Service Provider (SP) with the customer acting as the Identity Provider (IDP). The customer's authentication system performs user authentication using their existing user credentials.

ASAPP supports SP-initiated SSO with either OIDC (preferred method) and SAML. Once the user initiates sign-in, ASAPP detects that the user is authenticated and requests an assertion from the customer's SSO service.

**Configuration Steps for OIDC (preferred method)**

1. Create a new IDP OIDC application with type `Web`
2. Set the following attributes for the app:
   <table class="informaltable frame-void rules-rows">
     <thead>
       <tr>
         <th class="th"><p>Attribute</p></th>
         <th class="th"><p>Value\*</p></th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td class="td"><p>Grant Type</p></td>
         <td class="td"><p>authorization code</p></td>
       </tr>

       <tr>
         <td class="td"><p>Sign-in Redirect URIs</p></td>

         <td class="td">
           <p>Production: [https://api.asapp.com/auth/v1/callback/\\\{company\_marker\\}](https://api.asapp.com/auth/v1/callback/\\\{company_marker\\})</p>
           <p>Sandbox: [https://api.sandbox.asapp.com/auth/v1/callback/\\\{company\_marker\\}-sandbox](https://api.sandbox.asapp.com/auth/v1/callback/\\\{company_marker\\}-sandbox)</p>
         </td>
       </tr>
     </tbody>
   </table>
   **\*NOTE:** ASAPP to provide `company_marker` value
3. Save the application and send ASAPP the `Client ID` and `Client Secret` from the app through a secure communication channel
4. Set scopes for the OIDC application:
   * Required: `openid`
   * Preferred: `email`, `profile`
5. Tell ASAPP which end-user attribute should be used a unique identifier
6. Tell ASAPP your IDP domain name

**Configuration Steps for SAML**

1. Create a new IDP SAML application.
2. Set the following attributes for the app:

   | Attribute            | Value\*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Single Sign On URL   | Production: [https://sso.asapp.com/auth/realms/standalone-\{company\_marker}-auth/broker/saml/endpoint/clients/asapp-saml](https://sso.asapp.com/auth/realms/standalone-\{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml)<br /><br />Sandbox: [https://sso.asapp.com/auth/realms/standalone-\{company\_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox](https://sso.asapp.com/auth/realms/standalone-\{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox) |
   | Recipient URL        | Production: [https://sso.asapp.com/auth/realms/standalone-\{company\_marker}-auth/broker/saml/endpoint/clients/asapp-saml](https://sso.asapp.com/auth/realms/standalone-\{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml)<br /><br />Sandbox: [https://sso.asapp.com/auth/realms/standalone-\{company\_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox](https://sso.asapp.com/auth/realms/standalone-\{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox) |
   | Destination URL      | Production: [https://sso.asapp.com/auth/realms/standalone-\{company\_marker}-auth/broker/saml/endpoint/clients/asapp-saml](https://sso.asapp.com/auth/realms/standalone-\{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml)<br /><br />Sandbox: [https://sso.asapp.com/auth/realms/standalone-\{company\_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox](https://sso.asapp.com/auth/realms/standalone-\{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox) |
   | Audience Restriction | Production: [https://sso.asapp.com/auth/realms/standalone-\{company\_marker}-auth/broker/saml/endpoint/clients/asapp-saml](https://sso.asapp.com/auth/realms/standalone-\{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml)<br /><br />Sandbox: [https://sso.asapp.com/auth/realms/standalone-\{company\_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox](https://sso.asapp.com/auth/realms/standalone-\{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox) |
   | Response             | Signed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | Assertion            | Signed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | Signature Algorithm  | RSA\_SHA256                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | Digest Algorithm     | SHA256                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | Attribute Statements | externalUserId: {unique_id_to_identify_the_user}                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

   **\*NOTE:** ASAPP to provide `company_marker` value
3. Save the application and send the Public Certificate to validate Signature for this app SAML payload to ASAPP team
4. Send ASAPP team the URL of the SAML application

### 4. Configure Auto-Pilot Greetings

If you so choose, you can work with your ASAPP contact to enable Auto-Pilot Greetings in your AI Compose installation.

Auto-Pilot Greetings automatically generates a greeting at the beginning of a conversation, and that greeting can be automatically sent to a customer on your agent's behalf after a configurable timer elapses.

Your ASAPP contact can:

* Turn Auto-Pilot Greetings on or off for your organization
* Set a countdown timer value after which the Auto-Pilot Greeting is sent if an agent does not cancel Auto-Pilot by typing or clicking a "cancel" button
* Set the global default messages that will be provided for Auto-Pilot Greetings across your organization (note that agents can optionally customize their Auto-Pilot Greetings messages within the Auto-Pilot tab of the AI Compose panel)

## Usage

### Customization

#### LivePerson

For LivePerson, the standard process is to download ASAPP AI Compose as a standalone widget. In the case that you already have your own LivePerson custom widget, ASAPP also provides the option for you to embed our custom widget inside your own custom widget, thus economizing on-screen real estate.

**Conversation Attributes**

Once the ASAPP AI Compose widget is embedded, LivePerson shares the following conversation attributes with ASAPP: customer name, agent name and skill.

ASAPP can use name attributes to populate values into templated responses (e.g. "Hi \[customer name], how can I help you today?") and to selectively filter response lists based on the skill of the conversation.

**Conversation Redaction**

When message text in the conversation transcript is sent to ASAPP, ASAPP applies redaction to the message text to prevent transmission of sensitive information. Reach out to your ASAPP account contact for information on available redaction capabilities to configure for your implementation.

### Data Security

ASAPP's security protocols protect data at each point of transmission from first user authentication, to secure communications, to our auditing and logging system, all the way to securing the environment when data is at rest in the data logging system. Access to data by ASAPP teams is tightly constrained and monitored. Strict security protocols protect both ASAPP and our customers.

The following security controls are particularly relevant to AI Compose:

1. Client sessions are controlled using a time-limited authorization token. Privileges for each active session are controlled server-side to mitigate potential elevation-of-privilege and information disclosure risks.
2. To avoid unauthorized disclosure of information, unique, non-guessable IDs are used to identify conversations. These conversations can only be accessed using a valid client session.
3. Requests to API endpoints that can potentially receive sensitive data are put through a round of redaction to strip the request of sensitive data (like SSNs and phone numbers).

### Additional Considerations

#### Historical Conversation Data for Generating a Response List

ASAPP uses past agent conversations to generate a customized response list tailored to a given use case. In order to create an accurate and relevant list, ASAPP requires a minimum of 200,000 historical transcripts to be supplied ahead of implementing AI Compose.

For more information on how to transmit the conversation data, reach out to your ASAPP account contact.

#### LivePerson

ASAPP uses a browser extension to replace the LivePerson composer with the ASAPP composer. In the unlikely event that the DOM of the LivePerson composer or its surrounding area changes, the LivePerson composer may no longer be replaced by the ASAPP composer.

In this case, the CSR has the option to toggle the ASAPP composer so that it 'retreats' into the ASAPP Custom Widget. In such a case, the ASAPP composer will continue to be fully functional, even if it is no longer ideally placed just below the LivePerson chat history.

In order to quickly restore the placement of the ASAPP composer directly beneath the LivePerson chat log, ASAPP deploys its extension so that the extension's configuration is pulled down from our servers in real-time. If the LivePerson DOM does change, we can deploy a fix rapidly.
