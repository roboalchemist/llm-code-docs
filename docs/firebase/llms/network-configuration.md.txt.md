# Source: https://firebase.google.com/docs/cloud-messaging/network-configuration.md.txt

This document outlines the network configurations required for FCM to
function correctly within your network environment.

## Configure your Network for sending messages to FCM

Before you begin, you need to make sure your system is communicating with
FCM servers for sending messages and managing subscriptions.

To send FCM messages or manage subscriptions, your network will need
to communicate with the following servers over https:

- fcm.googleapis.com (message sending)
- accounts.google.com (authentication for message sending)
- iid.googleapis.com (topic subscription \& device group management)

This list is subject to change over time. We are unable to provide an ip based
allowlist for these end points.

## Configure your Network for Android devices using FCM

This section details how to configure your network to support FCM
traffic for Android devices.

### FCM ports and your firewall

The vast majority of networks don't limit devices from connecting to the rest of
the internet. In general, this is our recommendation. However, some
organizations require firewalls as part of their perimeter security plan.

### Firewall options

| Option | What we do | Specific rules | Notes |
|---|---|---|---|
| None (**preferred**) | - | - | - |
| Port based filtering (second choice) | Limit traffic to specific ports | TCP ports to open: - 5228 - 5229 - 5230 - 443 | This is the simplest rule and prevents dependence on things that are more likely to change over time. |
| Hostname based filtering | Using a special firewall configuration to allowlist certain TLS SNI entries to pass through the firewall. This may be combined with port based filtering. | Hostnames to open: - mtalk.google.com - mtalk4.google.com - mtalk-staging.google.com - mtalk-dev.google.com - alt1-mtalk.google.com - alt2-mtalk.google.com - alt3-mtalk.google.com - alt4-mtalk.google.com - alt5-mtalk.google.com - alt6-mtalk.google.com - alt7-mtalk.google.com - alt8-mtalk.google.com - android.apis.google.com - device-provisioning.googleapis.com - firebaseinstallations.googleapis.com | Not all firewall software supports this but many do. This list is pretty stable but we won't proactively notify you if it changes. |
| IP based filtering (strongly **not** recommended) | Use a very large static list of ip addresses. | Allowlist all of the IP addresses listed in [goog.json](https://cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults). This list is updated regularly and you are recommended to **update your rules on a monthly basis**. Problems caused by firewall IP restrictions are often intermittent and difficult to diagnose. | We change our IP address list very frequently and without warning so you will need to enter this big list and to update it frequently. Additionally, we see frequent typos when people try to enter ip allowlists in their firewall rules. We don't recommend this because invariably the information gets out of date and is not maintained. Additionally the size of the list can be unwieldy for some routers. |

> [!NOTE]
> **Note:** If you are receiving notifications over APNs, make sure you have also opened the [ports specified by Apple](https://support.apple.com/en-ph/HT203609).

### Network Address Translation or Stateful Packet Inspection firewalls

If your network implements Network Address Translation (NAT) or Stateful Packet
Inspection (SPI), implement a 30 minute or longer timeout for our connections
over ports 5228-5230. This enables us to provide reliable connectivity while
reducing the battery consumption of your users' mobile devices.

### FCM and Proxies

FCM's protocol for delivering push messages to devices is not able to
be proxied through network proxies. As such you will need to ensure that the
FCM connection from devices on your network can connect directly with
our servers.

## VPN interactions and bypassability

Firebase Cloud Messaging takes various steps to ensure that the push messaging
connection from the phone to the server is reliable and available as often as
possible. The use of a VPN complicates this effort.

VPNs mask the underlying information that FCM needs to tune its
connection to maximize reliability \& battery life. In some cases VPNs actively
break long lived connections resulting in a bad user experience due to missed or
delayed messages or a high battery cost. When the VPN is configured to allow us
to do so, we bypass the VPN using an encrypted connection (over the base network
Wi-Fi or LTE) so as to ensure a reliable, battery friendly
experience. FCM's usage of bypassable VPNs is specific to the
FCM Push Notification channel. Other FCM traffic, such as
registration traffic, uses the VPN if it is active. When the FCM
connection bypasses the VPN it loses additional benefits the VPN may provide,
such as IP masking.

Different VPNs will have different methods for controlling whether or not it can
be bypassed. Consult the documentation for your specific VPN for instructions.

If the VPN is not configured to be bypassable then Firebase Cloud Messaging will
use the VPN network in order to connect to the server. This may result in
periods of time where messages are delayed and may result in more battery
usage as Cloud Messaging works to maintain the connection over the VPN
connection.