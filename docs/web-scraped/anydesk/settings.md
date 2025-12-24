# Source: https://support.anydesk.com/docs/settings

You can customize AnyDesk to fit your needs using a variety of available settings.

To open AnyDesk [Client Settings]:

1.  Open the AnyDesk app on your device.

2.  In the upper-right corner, click ![image.png](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/image(102).png) and select **Settings**.

3.  Choose a category from a menu.\
    ![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20all.png)

Settings in the AnyDesk client are grouped into categories for easier navigation:

  -------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [**Category**]                                                                                                                                                                                                                                                                                                                                                                                                                           [**Description**]
  [**Application**](/v1/docs/settings-1#application)   ![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20application(1).png)   Configure general app behavior, connection preferences, [Screen Recording], and Wake-on-LAN settings.
  [**Security**](/v1/docs/settings-1#security)         ![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20security(1).png)      Set up Interactive and [Unattended Access], permission profiles, privacy settings, and [Access Control List] rules.
  [**Session**](/v1/docs/settings-1#session)           ![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20session(1).png)       Manage display, audio, recording, and [Remote Printing] settings used during active remote sessions.
  [**Account**](/v1/docs/settings-1#account)           ![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20account.png)          View or change your license key, [Alias], and desk preview image.
  -------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this article, find detailed information on each setting category.

------------------------------------------------------------------------

## Application 

Learn how to configure general app behavior, connection preferences, screen recording, and Wake-on-LAN settings.

### General 

The **General** section in AnyDesk settings allows you to customize application behavior, session preferences, and data storage.

![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20general%201.png)

Configure the followings settings:

-   **Language** - select the interface language from the dropdown list.

-   **Theme** (Windows) - switch between light, dark, or system theme.

-   **Keyboard** (macOS) - control how keyboard input is handled during remote sessions.

    -   ***Transmit keyboard shortcuts***  - enables the transmission of system-level shortcuts (such as Command or Ctrl+Alt+Del) to the remote device.

    -   ***Use Right Command as a Host Key*** - the right *Command* key acts as a host key to trigger local shortcuts.

    -   ***Accept all remote keyboard shortcuts*** - if enabled, AnyDesk accepts all shortcuts from the remote side, overriding local ones.

-   **Miscellaneous** - additional behavioral settings for [Session Management] and resolution handling.

    -   ***Request a comment on session end*** - prompts the user to leave a comment when a session ends. You can then see the comments after session in [my.anydesk](https://my.anydesk.com/v2).

    -   ***Open [Address Book] on startup*** - automatically opens the address book when AnyDesk launches.

    -   ***Transmit Original Resolution (Retina)***  - sends the full native resolution (e.g., Retina on Mac) to the remote device for optimal clarity.

    -   ***Prevent display sleep in outgoing sessions*** - keeps the display on the local device active during an outgoing session to avoid interruptions.

-   **Screenshot Path** - specify the default save location for screenshots taken during sessions.

    -   ***Default*** - saves screenshots to the predefined system location.

    -   ***Custom*** - specify a custom directory by browsing to a preferred folder.

-   **Chat Log** - manage how chat logs are stored locally.

    -   ***Disabled*** - turns off chat logging.

    -   ***Default*** - saves chat logs in the default AnyDesk directory.

    -   ***Custom*** - lets the user define a specific folder for chat log storage.

-   **Online Status Visibility** - select the *Show remote clients\' online status* checkbox to display the online availability of other clients in your address book or recent connections.

-   **Help Us Improve** - select the *Allow collection of usage data* checkbox to allow AnyDesk to collect client, device, and network usage data to enhance product quality. This data is used only with your consent.

------------------------------------------------------------------------

### Connection 

This section manages how AnyDesk communicates over networks, including direct connections, ports, and proxies. To modify the *Connection* settings, click ![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/unlock%20button.png) at the top of the *Connection* section.

![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20connection.png)

-   **General**

    -   ***Allow direct connections*** - select the checkbox to allow faster, direct connections between clients. If disabled, sessions are routed through AnyDesk servers. All session data is end-to-end encrypted, regardless of connection type.

    -   ***Local port*** - AnyDesk uses TCP port **7070** by default for direct connections. You can specify a custom port here.

-   **HTTP-Proxy** (Windows, macOS, Linux) - configure how the client connects through a proxy:

    -   ***No proxy*** - connects directly without using a proxy.

    -   ***Detect proxy*** - uses Proxy Auto-Config (PAC) to detect proxy settings.

    -   ***Manual proxy setup*** - specify the proxy's IP address, Port, and authentication details.\
        ⚠️ The proxy must support the CONNECT method and must not interfere with SSL/TLS traffic.

-   [**NTLM Authentication**](/v1/docs/what-is-ntlm-authentication) - if you\'re using a proxy, AnyDesk supports **NTLM** authentication on Windows (v6.3 and later). This allows secure proxy login using your existing Windows domain credentials, without needing separate login details.

------------------------------------------------------------------------

### Wake-On-LAN 

Configure remote wake via Wake‑On‑LAN.

![AnyDesk settings showing Wake-on-LAN options and instructions for device wake-up.](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20wakeonlan.png)

> 🦉[ For more details on Wake-on-LAN, see ][[**this article**]](/v1/docs/wake-on-lan)[. ]

------------------------------------------------------------------------

### Screen recording (Windows only) 

Enable and configure screen recording and audio options.

![Settings menu showing screen recording options and audio input selections in AnyDesk application.](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20screen%20recording.png)

> 🦉[ For more details about the Screen Recording feature, see ][[**this article**]](/v1/docs/screen-recording)[. ]

------------------------------------------------------------------------

## Security 

Learn how to set up Interactive and Unattended access, permission profiles, privacy settings, and Access Control List rules.

### Access 

If AnyDesk is installed on your device, administrative privileges are required to modify [Security Settings]. To modify the *Access* settings, click ![](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/unlock%20button.png) at the top of the *Access* section.

![Settings menu for AnyDesk showing access options and security features.](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20access%201.png)

#### **[Interactive Access]** 

Control how incoming [Session Requests] are handled. This setting determines when the **Accept Window** appears:

-   **Always show incoming session requests** - always prompt the user to accept the session.

-   **Only show incoming session requests if AnyDesk window is open** - show the prompt only if AnyDesk is open.

-   **Never show incoming session requests** - do not prompt. Sessions require valid *Unattended Access* credentials to connect.

#### **Unattended Access** 

Configure access credentials that allow connections without manual confirmation. This is required when **Interactive Access** is set to *Never* *show incoming session requests.*

> 🦉[ For more on Unattended Access, see ][[**this article**]](/v1/docs/unattended-access)[. ]

#### **Access Control List** 

Restrict connections to specific AnyDesk IDs or aliases. This whitelist-based feature ensures only defined entries can establish a connection.

-   Use wildcards (`*`, `?`) to define patterns.

    -   `*` matches any number of characters.

    -   `?` matches a single character.

-   Example: `*@company` allows access only from aliases within your custom [Namespace].

> 🦉[ For more on Namespaces, see ][[**this article**]](/v1/docs/anydesk-id-and-alias#namespace)[. ]

#### **Discovery** 

Enable automatic detection of AnyDesk apps on the same local network, and allow your AnyDesk app to be discovered by others. It is enabled by default for the installed AnyDesk app and can be manually enabled in portable mode.

Discovered items include:

-   Operating system

-   Device name

-   Alias/ID

> ::: blockquote-title
> 💡 **NOTE**
> :::
>
> If **Discovery** is enabled, you may need to adjust your [firewall](/v1/docs/firewall) settings to allow traffic.

------------------------------------------------------------------------

### Permissions 

Define default permission profiles for remote users:

![AnyDesk settings showing permissions for remote access and control options.](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20permissions.png)

> 🦉[ For more details about permission profiles, see ][[**this article**]](/v1/docs/permission-profiles)[. ]

### Privacy 

-   **Screen Frame** - enable this option to display an always-on-top border around your screen during a session. This helps you quickly see when someone is connected to your device.

------------------------------------------------------------------------

## Session 

Learn how to manage display, audio, recording, and remote printing settings used during active remote sessions.

### Display 

> 🦉[ For more details about Display settings, see ][[**this article**]](/v1/docs/display)[. ]

### Audio 

Adjust whether to transmit local audio and/or receive remote sound.

> 🦉[ For more details about Audio settings, see ][[**this article**]](/v1/docs/audio)[. ]

### Recording 

You can choose to automatically record incoming or outgoing sessions.

Set [Session Recording] preferences and default or custom save paths. The default path is `%HOME%\Videos\AnyDesk`.

![AnyDesk settings menu showing recording options and path selection for screen recordings.](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20recording(1).png)

> 🦉[ For more details on Session recording, see ][[**this article**]](/v1/docs/session-recording)[. ]

### Printer 

Select how to manage remote print jobs:

-   **Dismiss**

-   **Use default printer**

-   **Use specific printer**

    ![Settings menu showing printer options and installation prompt for AnyDesk Printer.](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20printer.png)

> 🦉[ For more details about Remote Print feature, see ][[**this article**]](/v1/docs/remote-print)[. ]

------------------------------------------------------------------------

## Account 

Learn how to change your license, Alias, user image, and other identity details associated with your AnyDesk account.

### My account 

On this page, you can do the following:

-   **Log in / Register** - sign in to link your AnyDesk client to an existing account or create a new one.

-   **Current License** - displays the license currently assigned to your AnyDesk client.

-   **Change [License Key]** - enter a new license key to switch or upgrade your license.

    ![AnyDesk settings page showing login and account registration options for users.](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20my%20account.png)

> 🦉[ For more information on how to register the license, see ][[**this article**]](/v1/docs/register-your-license)[. ]

------------------------------------------------------------------------

### Identity 

Configure how your AnyDesk client is presented to others in the Address Book, Accept Window, and session list.

![AnyDesk settings page showing identity options and desktop preview settings.](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/no%20user%20image(1).png)

-   **Alias** - your AnyDesk client address used to establish connections. You can learn how to manage AnyDesk Alias [here](/v1/docs/manage-anydesk-alias).

-   **Desk Preview** - control what preview image is shown to others when your AnyDesk client is listed in their Address Book or Recent Sessions:

    -   **Hide** - replace the preview with a generic placeholder image.

    -   **Account's desktop wallpaper** - show your desktop background.

    -   **Screenshot** - show a live image of your desktop.

------------------------------------------------------------------------

## About AnyDesk   

In **About AnyDesk**, you can see the version of your AnyDesk client, as well as what license is currently registered to the AnyDesk client.

![AnyDesk settings page showing version, license information, and copyright details.](https://cdn.document360.io/b94c9ac2-20ec-4c7e-b325-135b0ed113f9/Images/Documentation/settings%20about%20anydesk.png)

-   **Help Center** - opens our Help Center using the default browser.

-   **Send Support Information** - sends our Support team an email with your [[Trace Files]](/v1/docs/what-are-trace-files). Please do not forget to also provide a description of the issue.

-   **Open Connection Trace** - view a list of all clients that have made a connection request to this AnyDesk client.

Configuration options available in AnyDesk that allow users to customize security settings, session preferences, and more.

A feature that allows users to record their screen during an active session or independently, useful for creating tutorials or capturing solutions.

A feature that allows connections to a remote device without requiring manual approval on the other end, enabling access using just a password.

A security feature that lets you define which AnyDesk IDs or Aliases are allowed to connect to a device. All devices outside of your Access Control List are automatically blocked.

A feature that allows users to print documents from a remote device to a local printer during a remote session.

A name-based address used to identify a device in AnyDesk. Unlike the AnyDesk ID, which is a numerical address, the Alias uses a username and a Namespace (e.g. name@namespace) to make devices easier to recognize and manage.

The process of overseeing and controlling remote sessions, including starting, ending, and monitoring connections.

A feature that lets you save and organize your contacts, which you can group using tags, for quick and easy access to remote devices.

Options available in AnyDesk to enhance the security of remote connections, including password protection and access controls.

This gives the remote user control to either approve or deny a connection request, ensuring the session only starts with their permission.

A feature in AnyDesk that allows support agents to connect with users via a session link without needing the user\'s AnyDesk ID, streamlining remote support.

A custom AnyDesk domain used to identify devices and enhance security. It helps control access by allowing only trusted devices within the same domain to connect to you.

A feature that records the remote screen during active sessions, enabling users to capture, document, and review their sessions.

A unique code used to activate your AnyDesk license and give you access to all the features included in it.

Files automatically created during AnyDesk sessions that provide diagnostic information, useful for troubleshooting issues.