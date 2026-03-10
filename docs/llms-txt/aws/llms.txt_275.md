# Source: https://docs.aws.amazon.com/dcv/latest/adminguide/llms.txt

# Amazon DCV Administrator Guide

- [What Is Amazon DCV?](https://docs.aws.amazon.com/dcv/latest/adminguide/what-is-dcv.html)
- [Understanding Amazon DCV Servers](https://docs.aws.amazon.com/dcv/latest/adminguide/servers.html)
- [Amazon DCV end of support life](https://docs.aws.amazon.com/dcv/latest/adminguide/eosl.html)
- [Release notes and document history](https://docs.aws.amazon.com/dcv/latest/adminguide/doc-history-release-notes.html)

## [Setting up the Amazon DCV server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up.html)

### [Step 1: Install the Amazon DCV Server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing.html)

Steps for installing the Amazon DCV server on a Windows, Linux, and macOS host server.

### [Installing on Windows](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-windows.html)

Steps for installing the Amazon DCV server on a Windows server.

- [Prerequisites](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-winprereq.html): This topic describes how to configure your Windows Amazon EC2 instance before you install the Amazon DCV server.
- [Installing the Server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-wininstall.html): You can use an installation wizard to install the Amazon DCV server on a Windows host server.

### [Installing on Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-linux.html)

Steps for installing the Amazon DCV server on Linux.

- [Prerequisites](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-linux-prereq.html): Amazon DCV enables clients to access a remote graphical X session on a Linux server.
- [Installing the Server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-linux-server.html): The Amazon DCV server is installed using a series of RPM or .deb packages, depending on your host server's operating system.
- [Performing post-installation checks](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-linux-checks.html): This topic provides some post-installation checks that you should perform after installing Amazon DCV to ensure that your Amazon DCV server is properly configured.

### [Installing on macOS](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-macos.html)

Steps for installing the Amazon DCV server on an Amazon EC2 Mac instance.

- [Prerequisites](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-macosprereq.html): This topic describes how to prepare your Amazon EC2 Mac instance before you install the Amazon DCV server.
- [Installing the Server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-macosinstall.html): You can use an installation wizard to install the Amazon DCV server on an Amazon EC2 Mac instance.

### [Step 2: License the Amazon DCV Server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-license.html)

Licensing requirements for the Amazon DCV server.

- [Installing an extended evaluation license](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-evaluation.html): Steps for installing a Amazon DCV extended evaluation license.
- [Installing a production license](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-production.html): Steps for installing a Amazon DCV production license.
- [Updating the production license](https://docs.aws.amazon.com/dcv/latest/adminguide/updating-licenses.html): Steps for updating the DCV license on the RLM server
- [Step 3: Set up Amazon DCV Server imaging (Optional)](https://docs.aws.amazon.com/dcv/latest/adminguide/imaging.html): Steps for imaging the Amazon DCV server on a Windows and Linux host server.


## [Managing the Amazon DCV server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage.html)

- [Starting the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html): Start the Amazon DCV server.
- [Stopping the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html): Stop the Amazon DCV server.
- [Upgrading the server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-upgrading.html): Steps for upgrading the Amazon DCV server on a Windows, Linux, and macOS host server.
- [Uninstalling the server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-uninstalling.html): Steps for uninstalling the Amazon DCV server on a Windows and Linux host server.
- [Disabling QUIC UDP](https://docs.aws.amazon.com/dcv/latest/adminguide/disable-quic.html): By default, since version 2024.0, Amazon DCV supports both the WebSocket protocol, which is based on TCP, and the QUIC protocol, which is based on UDP for data transport.
- [Changing the TCP/UDP ports and address](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-port-addr.html): Change the Amazon DCV server's TCP and UDP ports and address.
- [Managing the TLS certificate](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-cert.html): Change the TLS certificate used to secure traffic between the Amazon DCV client and Amazon DCV server.
- [Disconnecting idle clients](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-disconnect.html): Disconnect idle Amazon DCV clients from the Amazon DCV session.
- [Enabling GPU sharing on Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-gpu.html): Steps for enabling GPU sharing on a Linux Amazon DCV server.
- [Enabling touchscreen and stylus support](https://docs.aws.amazon.com/dcv/latest/adminguide/enable-stylus.html)
- [Enabling gamepad support](https://docs.aws.amazon.com/dcv/latest/adminguide/enable-gamepad.html): Beginning with Amazon DCV Server 2022.0, gamepad devices can be used when connecting to any of the supported Windows or Linux operating systems.
- [Enabling USB remotization](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-usb-remote.html): Enabling specialized USB device remotization.
- [Configuring smart card caching](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-smart-card.html): Configuring smart card caching.

### [Configuring WebAuthn Redirection](https://docs.aws.amazon.com/dcv/latest/adminguide/config-webauthn-redirect.html)

Configuring WebAuthn Redirection

- [Configuring WebAuthn redirection on Windows hosts](https://docs.aws.amazon.com/dcv/latest/adminguide/webauth-windows.html): WebAuthn can be enabled or disabled using the webauthn-redirection permission.
- [Configuring WebAuthn redirection on Linux hosts](https://docs.aws.amazon.com/dcv/latest/adminguide/webauth-linux.html): DCV Linux server currently support Standard WebAuthn.
- [Enabling session storage](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-storage.html): Enabling Amazon DCV session storage.
- [Configuring the printer on Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-printer.html): Amazon DCV allows you to print either to a local redirected printer or to a virtual Amazon DCV printer.
- [Configuring the clipboard on Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-clipboard.html): Linux operating systems feature two buffers that you can use to copy and paste content.
- [Configuring multi-channel audio](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-audio.html): Amazon DCV supports up to 7.1 audio channels when using the Amazon DCV native clients.
- [Configuring the HTTP headers](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-headers.html): You can configure the Amazon DCV server to send additional HTTP response headers to the Amazon DCV client when users connect to a session using the web browser client.

### [Configuring authentication](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authentication.html)

Learn how to configure client authentication requirements.

- [Use External Authentication](https://docs.aws.amazon.com/dcv/latest/adminguide/external-authentication.html): By default, Amazon DCV client authentication is delegated to the underlying operating system.

### [Configuring authorization](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization.html)

Introduction to Amazon DCV authorization.

### [Understanding permissions files](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization-file-create.html)

You can create a custom permissions file or update an existing permissions file using your preferred text editor.

- [Importing a permissions file](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization-file-create-import.html): The imports section is typically the first section of the permissions file.
- [Creating groups](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization-file-create-group.html): You can use [groups] section of the permissions file to define user groups for users that have similar use cases or permissions requirements.
- [Creating aliases](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization-file-create-alias.html): You can use the [aliases] section of the permissions file to create sets of Amazon DCV features.
- [Adding permissions](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization-file-create-permission.html): The [permissions] section of the permissions file lets you control user and group access to specific features or aliases.
- [Enable Remote X connections to the X Server for virtual sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/setup-xforwarding.html): By default, Xdcv prevents the use of X forwarding, because of inherent security risks.
- [Embed the Amazon DCV web browser client inside an iFrame](https://docs.aws.amazon.com/dcv/latest/adminguide/embed-in-iframe.html): By default, to protect against clickjacking attacks, Amazon DCV doesn't allow the web browser client to be embedded inside an iFrame.


## [Managing Amazon DCV sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions.html)

- [Understanding Amazon DCV sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions-intro.html): Introduction to Amazon DCV sessions.
- [Using the Command Line Tool](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions-cli.html): Using the Amazon DCV command line tool.
- [Starting sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions-start.html): How to start a Amazon DCV session.
- [Stopping Sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions-lifecycle-stop.html): How to stop a Amazon DCV session.
- [Viewing sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions-lifecycle-view.html): How to view a Amazon DCV session.

### [Managing active sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-running-session.html)

How to manage running Amazon DCV sessions.

- [Managing session storage](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-session-storage.html): Session storage is a directory on the Amazon DCV server that clients can access when they are connected to a Amazon DCV session.
- [Managing session authorization](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-session-perms.html): Authorization is used to grant or deny Amazon DCV clients permissions to specific Amazon DCV features.
- [Managing the session display layout](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-session-display.html): You can set the display layout for a running Amazon DCV session.
- [Managing the session name](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-session-name.html): You can change the name of a running session at any time.
- [Finding and stopping idle sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/stop-idle-sessions.html): You can identify idle Amazon DCV sessions using the dcv describe-sessions CLI command with the -j command option.
- [Setting session time zone](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-session-time-zone.html): DCV allows session owners and users to set the time zone of their session to reflect either the location of the DCV Server or their current location.
- [Managing screen blanking on Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-screen-blanking.html): For Console sessions on a Linux server, DCV blanks the local screen by default when at least one remote user is connected to the server, and restores the output (also locking the screen) upon disconnection of the last remote user.
- [Taking a screenshot](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions-lifecycle-screenshot.html): How to get screenshots from a running Amazon DCV session.


## [Troubleshooting](https://docs.aws.amazon.com/dcv/latest/adminguide/troubleshooting.html)

- [Using the Log Files](https://docs.aws.amazon.com/dcv/latest/adminguide/troubleshooting-logs.html): Using the log files to diagnose issues.

### [Troubleshooting Virtual Session Creation on Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/troubleshooting-linux-virtual-session-creation.html)

If connecting to a virtual session results in a No session available or The sessionId session is not available error, this is probably due to the fact that the virtual session creation failed and was terminated.

- [Investigating Virtual Session Creation Failure on Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/investigating-linux-virtual-session-creation-failure.html): A virtual session is created on Linux with the command:
- [Creating a Failsafe Virtual Session on Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/creating-linux-failsafe-virtual-session-creation.html): A common strategy to verify if the session creation failure is tied to the startup of the desktop environment consists in creating a minimal session.
- [Linux Sessions fail to start after UID change](https://docs.aws.amazon.com/dcv/latest/adminguide/linux-change-uid.html): On a Linux host, changing the user ID (UID) of an user or using a different Active Directory configuration that modifies the UID of an user, could cause failures in starting Amazon DCV sessions on the host.
- [Fixing cursor issues on Windows](https://docs.aws.amazon.com/dcv/latest/adminguide/fixing-windows-cursor-issues.html): With Amazon DCV servers running on Windows Server 2016 or Windows 10 and later, the mouse cursor always appears as an arrow.
- [Fixing Copy and Paste to IntelliJ IDEA](https://docs.aws.amazon.com/dcv/latest/adminguide/fixing-copy-paste-intellij.html): When trying to copy text from the macOS Amazon DCV Client to IntelliJ IDEA, the text cannot be pasted.
- [Redirection clarifications with self-signed certificates](https://docs.aws.amazon.com/dcv/latest/adminguide/redirection-clarifications-with-self-signed-certs.html): When redirecting to a Amazon DCV session from a web-based portal or application, self-signed certificates can break the browser trust with the session if the certificate has not been previously trusted.
- [Multimonitor/full screen failure with NVIDIA GPUs on Windows](https://docs.aws.amazon.com/dcv/latest/adminguide/multimonitor-failure-nvidia.html): DCV full screen/multimonitor feature may fail in cases where a Windows server host has an NVIDIA GPU.

### [Monitoring Amazon DCV Performance and Statistics](https://docs.aws.amazon.com/dcv/latest/adminguide/monitoring-dcv-performance.html)

Starting with Amazon DCV 2023.1 server, you can use Windows Performance Counters to monitor various aspects of the protocol performance and collect the statistics about the Amazon DCV sessions and connections.

- [Amazon DCV server](https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-server.html): This counter set contains global statistics about the DCV Server service on the host.
- [Amazon DCV server processes](https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-server-processes.html): This counter set contains information about the individual Amazon DCV processes.
- [Amazon DCV server sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-server-sessions.html): Counters in this set provide information about a single session.
- [Amazon DCV server connections](https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-server-connections.html): Counters in this set provide information about a single client connection.
- [Amazon DCV server channels](https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-server-channels.html): Counters in this set provide information about individual channels in a client connection.
- [Amazon DCV server imaging](https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-server-imaging.html): Counters in this set provide information about the subsystems responsible for screen grabbing, encoding and delivery.


## [Server parameter reference](https://docs.aws.amazon.com/dcv/latest/adminguide/config-param-ref.html)

- [Modifying configuration parameters](https://docs.aws.amazon.com/dcv/latest/adminguide/config-param-ref-modify.html): This section describes how to modify the configuration parameters for your Amazon DCV server.


## [Security](https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-security.html)

- [Data protection](https://docs.aws.amazon.com/dcv/latest/adminguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection when using Amazon DCV.
- [Compliance validation](https://docs.aws.amazon.com/dcv/latest/adminguide/security-compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
