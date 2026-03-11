# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/uipath/setting-up-enate-and-uipath-integration.md

# Setting Up Enate & UiPath Integration

To set up Enate and UiPath, you'll need to go through the following steps in order:

1. [Set up UiPath Studio](#1.-setting-up-uipath-studio)
2. [Set up the Enate Activity Library in UiPath Studio](#2.-setting-up-the-enate-activity-library-in-uipath-studio)
3. [Add a UiPath connection in Enate](#support-for-multiple-orchestration-connections)

## 1. Setting up UiPath Studio

You'll first need to set up UiPath studio. The following video will take you through how to do this.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM5MDU0Mg==>" %}

You can follow this link to create a UiPath Automation Cloud account: <https://cloud.uipath.com/portal_/register>

## 2. Setting up the Enate Activity Library in UiPath Studio

Now you need to set up the Enate Activity Library in your installation of UiPath Studio. Watch the following video to find out how to do this:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM5MDUwMQ==>" %}

## 3. Adding a UiPath Connection in Enate <a href="#support-for-multiple-orchestration-connections" id="support-for-multiple-orchestration-connections"></a>

Once you have set up UiPath Studio and then set up the Enate Activity Library in your installation of UiPath Studio, you can now add a UiPath connection in Enate's [Builder](https://docs.enate.net/enate-help/builder/builder-2021.1).

To do this, go to the [Marketplace ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)section in Builder and click to 'Activate' UiPath Orchestrator.

In the following page click on the '+' to add a new connection.

In the following pop-up, fill in the following fields:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F2dIoCW1VXDb0gsLaQYE2%2Fimage.png?alt=media&#x26;token=d112da38-a9d5-4c6f-9d71-f796e50a709e" alt=""><figcaption></figcaption></figure>

| Name        | This is your Enate-friendly name – you can enter anything you like here as a name. Mandatory.                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Technology  | Select the UiPath technology you want to use. Selecting a technology will bring up other relevant fields to fill in. Mandatory. |
| Description | You can enter a general description for this UiPath connector. Optional.                                                        |

Depending upon which technology you choose, the following fields may also need to be filled in.

| URL                   | The URL of UiPath Orchestrator e.g. <https://platform.uipath.com/>                                                         |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Tenant Name           | Your individual UiPath Tenant Name (also known as Service). Take this from your ‘Services’ section in UiPath Orchestrator. |
| Username              | The username for this Service in UiPath.                                                                                   |
| Password              | The password used to access UiPath orchestrator.                                                                           |
| Tenant Logical Name   | Your individual UiPath Tenant Name (also known as Service). Take this from your ‘Services’ section in UiPath Orchestrator. |
| Account Logical Name  | Account Logical Name for UiPath Orchestrator                                                                               |
| User Key              | User Key for UiPath Orchestrator                                                                                           |
| Client ID             | Client ID for UiPath Orchestrator                                                                                          |
| Credential Store Name | The name of the credential store, used to store robot credentials                                                          |
| Folder Name           | The name of the folder                                                                                                     |

To enable a connection, the connection has been tested successfully first. Click to 'Test Connection' which will run a live connection test and when a successful response has been detected, the connection will be enabled.

You can see details about the connection test in the Connection Logs tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpyAfR-r4E6TotgbJ4%2Fimage.png?alt=media\&token=7362635e-cc46-4c20-9fba-11fbf235c7a5)

### Editing a UiPath Connection

You can edit an existing UiPath connection by going to the Marketplace section in Builder and clicking to 'Update' UiPath Orchestrator.

When editing a connection, you are also able to see the activity history of the connection by clicking on the Show Activity button. You can see when the connection was created and by who and you can see if any subsequent edits have been made, when they were made and by who.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpyEpW_YHAHftn3vm2%2Fimage.png?alt=media\&token=422337dd-ec19-4234-b73d-7c01345e56f9)
