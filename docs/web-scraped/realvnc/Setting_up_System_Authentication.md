# Source: https://help.realvnc.com/hc/en-us/articles/360002250097-Setting-up-System-Authentication

# Setting up System Authentication 

[Follow](/hc/en-us/articles/360002250097-Setting-up-System-Authentication/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360022267298/MicrosoftTeams-image__3_.png)

**[Tegan](/hc/en-us/profiles/366602748777-Tegan)**

Updated July 17, 2025 12:35

# What is System Authentication? 

System Authentication means that RealVNC Viewer users can authenticate to RealVNC Server using the same credentials they normally use to *log on* to their user account on the RealVNC Server computer.

![VNC_Server_Options_Dialog_System_Authentication.png](/hc/article_attachments/4414019166353)

The system authentication scheme (labelled **Windows password**, **Mac password** or **UNIX password**) is both secure and convenient:

1.  System administrators often implement rules such as password complexity and ageing in enterprise environments to meet organisational security policies
2.  Users can authenticate using already-familiar credentials, and don't have to remember yet another password.

**\*You can combine this authentication scheme with others in order to specify [multi-factor authentication](https://help.realvnc.com/hc/en-us/articles/360002250077) for RealVNC Server.**

# Setting up System Authentication 

The user account of each prospective RealVNC Viewer user must be registered with RealVNC Server. Certain admin groups are [pre-registered](https://help.realvnc.com/hc/en-us/articles/360002253618), to enable connectivity out-of-the-box. This may mean no set up is required, especially under Windows and macOS.

**\*Set up *is* required to register [non-admin users and groups](https://help.realvnc.com/hc/en-us/articles/360002253618) with VNC Server, and prior configuration is required to register [domain accounts under Linux](https://help.realvnc.com/hc/en-us/articles/360002250097).**

To authenticate to RealVNC Server, a RealVNC Viewer user can supply the credentials:

-   Under any platform, of a local user account (that is, one set up directly on the computer).
-   Under Windows and macOS, providing the computer is joined to a domain, of a domain user account (one that is managed by a network service such as Active Directory). Note that prior configuration is required under Linux; see below.
-   Under Windows 8 or later, if the local user account is linked to a Microsoft account, the email address and password of the linked Microsoft account.

If you are unsure of the username to use, please see [this article](https://help.realvnc.com/hc/en-us/articles/360004013351).

[]

## Setting up domain accounts under Linux 

When RealVNC Server is installed on Linux platforms, a suitable PAM library checking credentials against the *local* database store only is automatically referenced. 

To configure RealVNC Server to allow authentication with domain accounts, the below steps will enable a basic configuration to achieve this:

1.  Create [`/etc/pam.d/vncserver.custom`] with the below contents, depending on your operating system:\
    **Ubuntu**\

        @include common-auth
        @include common-account
        @include common-session

    **RHEL / CentOS**

        auth include password-auth
        account include password-auth
        session include password-auth

2.  Create/edit [`/etc/vnc/config.d/common.custom`] and add the line:

        PamApplicationName=vncserver.custom

3.  Restart RealVNC Server.\
    For Service Mode, run the command: [`sudo systemctl restart vncserver-x11-serviced`]

4.  Connect with RealVNC Viewer and try authenticating with domain credentials. Note: you may need to qualify usernames with the domain name, for example [`DEV.ACMECORP.COM\johndoe`]

If you are unable to authenticate with domain credentials after following these steps, please [contact Support](https://help.realvnc.com/hc/en-us/requests/new).

# Registering domain accounts with RealVNC Server 

If the domain accounts you are using are not part of any built-in or local groups on the computer running RealVNC Server, domain accounts must be [registered](https://help.realvnc.com/hc/en-us/articles/360002253618) with RealVNC Server in the standard way, either by:

-   Setting the RealVNC Server [Permissions](https://help.realvnc.com/hc/en-us/articles/360002251297#server-permissions) parameter.
-   Opening RealVNC Server's **Options \> Users & Permissions** page and following [these instructions](https://help.realvnc.com/hc/en-us/articles/360002253618).

You may need to qualify usernames with the domain name, for example [`DEV.ACMECORP.COM\johndoe`]. Note that connecting users may also need to supply the user name qualified in this way too.