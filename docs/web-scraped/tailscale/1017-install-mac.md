# Installation on macOS

**Source:** https://tailscale.com/kb/1017/install-mac

---

Docs›Start›QuickstartTailscale quickstartWelcome! Follow the steps below to create your own private Tailscale network (known as a tailnet), or watch the video to learn how to get started with Tailscale and set up some useful features.
Create a tailnet
Go to tailscale.com and select Get Started. Alternatively, you can download and install the Tailscale client on your device, then sign up.
On the Sign up with your identity provider page, log in using a single sign-on (SSO) identity provider account.
If you sign up using a custom-owned domain, you are automatically enrolled in the Enterprise plan for a 14-day trial. If you sign up using a public domain email account such as @gmail.com, you are automatically enrolled in the Personal plan, which entitles you to three free users and many of the features offered in the Enterprise plan. You can always change your plan. For details, refer to Modify billing.
On the Welcome to Tailscale page, select either Business use or Personal use.
On the Let's add your first device page, select the OS that corresponds to the device you are using to download and install the client. Authenticate the client using the same credentials that you used to create the tailnet in step 2.
Once you are authenticated, the device will appear in the browser window.
On the Next, add a second device page, select the OS for another machine to add to the tailnet. Copy the link and send it to the second device. After the second device is authenticated, both devices will display.
Select Take me home. You will be redirected to the Tailscale admin console. This interface lets you control most aspects of your tailnet including users, devices, DNS, permissions, authentication keys, and more.
Rename devices
Every device added to a tailnet, including servers, nodes, phones, and personal computers is assigned a unique name generated from the device's OS hostname. This name is displayed in the Machines page of the admin console. You can also rename a device to help you locate and organize devices in the Machines page list.
Use MagicDNS
MagicDNS makes communicating with devices across your tailnet easier by allowing you to use the name listed in the Machines page of the admin console instead of an IP address. This works using automatically assigned OS hostnames or renamed device names. MagicDNS is enabled by default, and we recommend you keep it enabled.
Invite users
There are two types of tailnet user invites.
Team member invites are for users who will authenticate using the same identity provider you used when creating the tailnet.
External invites are for users who are not part of your custom domain, such as contractors, friends, and family.
Team members
If your tailnet uses a custom domain (example.com), users with email addresses with the same domain can log in without needing an invite. Alternatively, you can send team member invites to notify them to join.
External users
To invite external users to a tailnet, open the Users page of the admin console, select Invite external users, and choose one of the following options:
Invite via email to send one or more invites.
Copy invite link to share the invite link with others.
When users select the link, they will be directed to the Tailscale login page, where they can authenticate using a supported single sign-on (SSO) identity provider account. Once they are authenticated, users are added on the Users page of the admin console.
For more information, refer to Invite any user to your tailnet.
Add devices
You can add more devices to your tailnet using one of the following methods:
Login to the tailnet from other devices using an existing user account.
Add servers to a tailnet using a tag as the identity of the server, and provision the server using an authentication key. For more information, refer to Setting up a server on your Tailscale network.
Incorporate your existing system policies such as mobile device management (MDM) to control device management. For more information, refer to Integrate with an MDM solution.
Tailscale automatically assigns each device on your network a unique 100.x.y.z IP address, to establish stable connections between machines no matter where they are in the world, even when they switch networks or are behind a firewall.
To learn more about adding devices, refer to Add a device.
Secure traffic using exit nodes
Keep your internet activity private on an untrusted network by designating devices in your tailnet as exit nodes, then configure your tailnet devices to use those exit nodes.
For details on how to quickly configure and use exit nodes, refer to Use exit nodes.
For more in-depth information about exit nodes, refer to the main Exit nodes topic.
Route traffic using subnets
You can provide tailnet access to existing resources in your network using a subnet router. This can be useful if you need to access devices on which the Tailscale client cannot be installed, such as printers.
For details on how to quickly configure and use a subnet router, refer to Configure a subnet router.
For more in-depth information about subnet routers, refer to the main Subnet routers topic.
Manage permissions with access control policies
You can define your own custom permission for the users and devices in your tailnet, using access control policies (such as ACLs or grants). These permissions are configured in the tailnet policy file, which is located on the Access controls page of the admin console.
Monitor and log traffic
You can monitor and log tailnet activity such as network traffic, client activity, tailnet configuration changes, and SSH session recordings.
For more information, refer to Logging, auditing, and streaming.
Use cases
Need some inspiration? Tailscale can be used for a wide variety of users and environments. This section provides guidance for some common scenarios that you may want to use in your tailnet.
Developers
Interact with tailnet resources from Visual Studio Code using our Visual Studio Code extension.
Deploy, scale, and manage containerized applications such as Kubernetes, Docker, and Proxmox.
Connect to serverless apps such as AWS App Runner, AWS Lambda, Google Cloud Run, and Heroku.
Connect to cloud services such as AWS, Azure, Google Compute Engine, Hetzner, and Oracle Cloud.
Share local services on your machine such as web applications, accessible only from your tailnet using Tailscale Serve or share publicly over the internet using Tailscale Funnel.
Share prototype servers with other colleagues without needing to modify firewall settings.
IT admins
Manage the authentication and authorization of SSH connections in your tailnet using Tailscale SSH.
Integrate Tailscale deployments on AWS and Azure.
Control device and user access to your third-party applications without requiring any end-user configuration using app connectors.
Control what users can access in their Tailscale client using system policies.
Use Tailscale SSH session recording to stream recordings of Tailscale SSH sessions from the destination node to a recorder node in your tailnet.
Automate aspects of your Tailscale network using the Tailscale API.
Share an existing service with your peers outside your domain with node sharing.
Administer a computer remotely and lock down your connections to a Microsoft Remote Desktop Protocol (RDP) server.
Personal users
Connect an Apple TV to your tailnet for viewing your media server files, use your Apple TV as an exit node to route traffic through your home internet connection when you're away, or choose an exit node to route your Apple TV's traffic through.
Receive files from a network attached storage (NAS) server using FTP, and access media files from players such as VLC, Plex, and JellyFin.
Implement DNS-based ad blocking for your tailnet using Control D, NextDNS or a Pi-hole server.
Share files between your own devices, even across operating systems, with Taildrop.
Host a private server for you and your peers to play Minecraft or chat on IRC.
Troubleshooting and support
Visit our Support page to read common questions and answers, file bugs, request new features, observe Tailscale's operational status, or engage directly with our Support team.
Here are some links that provide assistance for common inquiries:
Troubleshooting guide
Production best practices
Security best practices
Using Tailscale with your firewall
