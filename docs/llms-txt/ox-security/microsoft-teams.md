# Source: https://docs.ox.security/ticketing-and-messaging/messaging/microsoft-teams.md

# Microsoft Teams

Microsoft Teams is a powerful collaboration platform that enables seamless communication and coordination across organizations. With its integration capabilities, it can serve as an effective notification and communication system for security platforms such as OX Security.

By leveraging Microsoft Teams, you can receive real-time security alerts, incident updates, and workflow notifications directly within your Teams channels or private chats, ensuring swift response and improved security operations.

This way, you can streamline incident management, reduce response time, and enhance team collaboration.

Integration use-cases:

* [Sending information about an individual issue to Teams.](#sending-a-teams-message-about-an-issue)
* [Adding OX-Teams related tasks as part of OX workflows.](#adding-teams-messages-to-workflows)

## Prerequisites

* Microsoft Teams account
* (Optional) Administrative access to Microsoft Azure Admin Center
* Permissions to manage enterprise applications in Azure

## Connecting to Microsoft Teams

1. In the **OX app**, go to **Connectors** and search for Microsoft Teams.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2be737198576ca1ce5a95ba2f7dc954ce2ed0291%2FTeams%20icon%20in%20Ox.png?alt=media" alt="" width="139"><figcaption></figcaption></figure>

1. Select **Microsoft Teams**. The **Configure your Microsoft Teams credentials** dialog appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7a49a7e92e26d5a70c15d7c946f78244831b9448%2FConfigure%20MS%20teams%20credentials%20in%20OX_identity_provider.png?alt=media" alt="" width="357"><figcaption></figcaption></figure>

1. Select **CONNECT**. The Microsoft Teams connector is configured.
2. In case you do not have the administrative access to Microsoft Azure Admin Center, the permissions request appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-718b7643ace610e2c5ab56d80cfb43d7b691700d%2FPemission%20Request.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

1. Select **Accept**.

## Viewing OX in Microsoft Entra admin center

1. Go to **Microsoft Entra admin center,** login and select **Applications** **>** **Enterprise Applications**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ca2f9fb8cac96c7261e7dd89ad590f830374ab1b%2FEnterprise%20applications%20in%20MS.png?alt=media" alt=""><figcaption></figcaption></figure>

1. From the right pane, select **OXSecurity**. The **OX Security Overview** pane appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a75fd12e647bf904b21ee7e3b754cd28447506f0%2FEnterprise%20applications%20in%20MS_OX.png?alt=media" alt=""><figcaption></figcaption></figure>

1. From the left pane, select **Permissions**. The **Permissions** pane appears, displaying the list of the channels through which you can get messages to Teams.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b64833ced487ab6519a16da950b051920af5c008%2FEnterprise%20applications%20in%20MS_OX_permissions.png?alt=media" alt=""><figcaption></figcaption></figure>

## Sending a Teams message about an issue

1. In the **OX app**, go to **Active Issues,** select the issue about which you want to send a message to Microsoft Teams, and in the issue property section, select the Teams icon. The **Send message to Teams** dialog appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0d138ca3e42280ce357045ae5e553d184161e2a6%2FSend%20message%20to%20teams.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

1. Add recipients and a comment, and select **SEND**.

## Adding Teams messages to workflows

1. In the **OX app**, go to **Workflows** and select the workflow to which you want to add sending Teams messages.
2. In the workflow, find the step to which you want to add the Teams-related action and click **+**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-61a38d478b1a7735acc9a7558cfc0cf33433f3d9%2FWF_teams_message_1%20(1).png?alt=media" alt="" width="130"><figcaption></figcaption></figure>

1. Select **Action > Teams** and set the following:

| **Select recipients:**               | Select message recipients.                                                                                                                                       |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Select recipients fallback:**      | Select fallback recipients.                                                                                                                                      |
| **(Optional) Add your own comment:** | IT's a good practice to add a comment to the message, providing additional info.                                                                                 |
| **Execute on:**                      | <p>Select one of the following conditions:<br>- New Issues<br>- Updated Issues<br>- New or Updated Issues<br>- New, Updated or Existing Issues<br>- Periodic</p> |

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e077bcf2df6bd0a953101a38a76d32934109911a%2FWF_teams_message.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select **ADD**. The new action appears in the workflow.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-73800adc7d0792af6bac89a2922c87e0e467353c%2FWF_teams_message_2.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>
