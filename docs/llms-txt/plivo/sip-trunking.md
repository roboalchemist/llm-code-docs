# Source: https://plivo.com/docs/voice-agents/sip-trunking/api/sip-trunking.md

# Source: https://plivo.com/docs/sip-trunking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart Guide

> Set up Plivo Zentrunk SIP trunking for inbound and outbound voice calls.

<Frame>
    <img src="https://mintcdn.com/plivo/V2GGXaNKq8uCbGT3/images/zentrunk-hero.png?fit=max&auto=format&n=V2GGXaNKq8uCbGT3&q=85&s=37f5a9e3d5e4d38704d4f61535725cd8" alt="" width="2880" height="1456" data-path="images/zentrunk-hero.png" />
</Frame>

## Overview

Zentrunk, Plivo’s SIP trunking service, provides global coverage for your outbound and inbound voice calls, working with your current cloud or on-premises communications infrastructure. Whether you’re looking to increase the capacity of your current telecom stack, increase coverage and phone number inventory, or extend your on-premises infrastructure to the cloud, Zentrunk can get you started. No minimum spends, carrier negotiations, or long-term contracts are required, and you can provision SIP trunks instantly using our console.

## Why Zentrunk?

Zentrunk provides benefits such as:

**Scalability**: Zentrunk supports your organization’s growth across multiple geographic locations. By combining voice and data in a single network, SIP trunking lets your organization quickly open new sites or establish full-time remote workers. You can scale as you grow by self-provisioning local, international, mobile, and toll-free numbers in more than 70 countries, configuring them in your trunk, and terminating calls from your IP PBX. You can also make calls to more than 190 countries using Zentrunk to make your business more globally accessible.

**Cost savings**: With traditional phone service, your organization is subject to different, often variable charges for your local, long distance, and international calling. Moving from traditional telecom systems to SIP trunking helps you save on recurring costs, as you can build your entire telecom system in the cloud, and be billed on a simple per-usage basis. You can also save by forgoing the physical infrastructure and hardware investments that typically come with scaling phone lines. With Zentrunk, adding phone lines or services is as simple as purchasing an additional handset and scaling your monthly service agreement.

**Reliability**: Traditional phone systems are prone to interruptions from factors such as weather events and networking issues. SIP trunking is more reliable, since you can add failover routing if a primary IP address is not responsive. With a redundant infrastructure across multiple geographies and at least three local carrier connections across countries, Zentrunk promises 99.99% uptime.

**Easy management for your IT teams:** Your IT team will never have to wait on hold to speak to a customer service representative again. SIP trunking and VoIP phones offer easy-to-use administrative portals for on-site management, including actions like adjusting call routing, changing extensions, and adding phone lines on demand.

Plivo’s 24x7 premium support and consultative customer success team can provide you with technical guidance when you need it.

## Getting started

### Plivo account

You need a Plivo account to start using Zentrunk. You can get a free trial account to experiment with and learn about our services.

1. [Sign up](https://cx.plivo.com/signup) through our console with your work email address
2. Check your inbox for an activation email message from Plivo. Click on the link in the message to activate your account.
3. Enter your mobile number to complete the phone verification step.

If you have any questions about creating a Plivo account, reach out to our [support team](https://support.plivo.com/hc/en-us) for assistance.

### Supported software and hardware

Zentrunk is compatible with a broad range of software and devices. We support:

* [All major IP PBXes](/sip-trunking/interconnection-guides/overview/)
* All SIP-based hardphones and softphones
* Integrations with all WebRTC clients and endpoints

### Supported SIP methods

Zentrunk supports these SIP methods: ACK, BYE, CANCEL, INVITE, OPTIONS, and UPDATE. We don’t support INFO, MESSAGE, NOTIFY, PRACK, PUBLISH, REFER, REGISTER, or SUBSCRIBE.

### Supported codecs

Zentrunk supports G.711 U-law (PCMU) and A-law (PCMA) codecs.

### Signaling / Media IP addresses

You may need to whitelist Plivo IP addresses in your firewall to ensure that calls get routed without interruption. Please whitelist all of these IP addresses, as calls might get routed through a different region in the event of a service disruption in a specific region.

| **Regions**           | **IP Addresses**                                               | **Signaling Ports**            | **Media Ports**         |
| --------------------- | -------------------------------------------------------------- | ------------------------------ | ----------------------- |
| North California, USA | 13.52.9.0/25<br />216.120.187.128/26                           | 5060 (UDP/TCP)<br />5061 (TLS) | 10000 - 30000 (UDP/TCP) |
| Virginia, USA         | 18.214.109.128/25<br />18.215.142.0/26<br />204.89.148.128/26  | 5060 (UDP/TCP)<br />5061 (TLS) | 10000 - 30000 (UDP/TCP) |
| Frankfurt, Germany    | 3.120.121.128/26                                               | 5060 (UDP/TCP)<br />5061 (TLS) | 10000 - 30000 (UDP/TCP) |
| São Paulo, Brazil     | 18.228.70.64/26<br />54.233.191.0/27                           | 5060 (UDP/TCP)<br />5061 (TLS) | 10000 - 30000 (UDP/TCP) |
| Sydney, Australia     | 13.238.202.192/26                                              | 5060 (UDP/TCP)<br />5061 (TLS) | 10000 - 30000 (UDP/TCP) |
| Singapore             | 18.136.1.128/26<br />204.89.149.128/27                         | 5060 (UDP/TCP)<br />5061 (TLS) | 10000 - 30000 (UDP/TCP) |
| India                 | 15.207.90.192/31<br />204.89.151.128/27<br />204.89.151.160/27 | 5060 (UDP/TCP)<br />5061 (TLS) | 10000 - 30000 (UDP/TCP) |

### Internet bandwidth

SIP trunk calls over the internet require sufficient bandwidth to support peak concurrent call traffic. Plivo needs about 100Kbps for every successful call, so your peak bandwidth requirements can be calculated as 100Kbps \* peak concurrent calls.

### Calls-per-second limitations

#### Outbound limitations

The calls-per-second limitation for Zentrunk SIP trunking is based on both account-level CPS and trunk-level CPS. The account-level CPS is the rate at which calls may be made from an account in a second, while the trunk-level CPS applies to each of the trunks individually in the account.

Businesses can choose different ways to allocate their account-level CPS across trunks in their account.

**Scenario 1**: A user has 25 account-level CPS and three trunks

* 2 trunks are set at 10 CPS (high-volume use cases)
* 1 trunk is set at 5 CPS (low-volume use case)

**Scenario 2**: A user has 10 account-level CPS and 10 trunks

* Each trunk has a CPS of 10
* This allows for a “free-for-all” where if one trunk is consistently initiating calls at a rate of 10 CPS, calls from other trunks would fail

<Note>
  **Note:** You cannot exceed the account CPS limit even if you have multiple trunks in your account. If it exceeds, then calls will fail with the error “cps\_limit\_reached” and error code 5180.
</Note>

By default, the calls-per-second rate for Zentrunk is set to 2 CPS per account and 1 CPS per trunk. If you have higher CPS requirements, please contact our [sales team](https://www.plivo.com/contact/sales/). For help with technical issues related to Zentrunk, please submit a ticket with the [Plivo support team](https://support.plivo.com/hc/en-us/requests/new?ticket_form_id=360000156292).

#### Inbound limitations

There are no calls-per-second constraints for inbound trunks in Zentrunk SIP trunking.

## Outbound trunks (termination)

<Frame>
    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-sip-trunking.png?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=0c32acd5ea89ce0fe4bb729181c8cf6f" alt="" width="1255" height="687" data-path="images/outbound-sip-trunking.png" />
</Frame>

Zentrunk’s outbound SIP trunks let you reach fixed and mobile phones in more than 190 countries. There are no restrictions or limitations on channels or ports. Each trunk comes with unlimited concurrent call capability. You get all of the standard features of a telco (such as dynamic CLI, DTMF support, and per-second billing) and more (including secure trunking, fraud detection, and instant provisioning). You pay only for what you use, with no long-term contracts.

### Create an outbound trunk

To use Zentrunk to terminate calls, you need to set up trunk authentication on the Plivo console. Authenticating your trunk ensures that Zentrunk accepts only traffic that your infrastructure sends securely. You can configure your trunk to be authenticated by an IP access control list, a credentials list, or both.

<Frame>
    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-trunk.gif?s=deac527874c38c60a17431c14d787b04" alt="" width="1024" height="562" data-path="images/outbound-trunk.gif" />
</Frame>

#### To create an outbound trunk:

1. In the Plivo console, visit Zentrunk > [Outbound Trunks](https://cx.plivo.com/sip-trunking) and click **Create New Outbound Trunk**.
2. Under Trunk Details, enter a name for your trunk (for example, Plivo Test).

   <Note>
     **Note:** By default, the trunk is enabled.
   </Note>
3. Under Trunk Authentication, select the IP Access Control List, the Credentials List, or both.

   <Note>
     **Note:** Make sure to choose either an IP Access Control List or a Credentials List. The IP Access Control List consists of a list of the IP addresses from which a SIP Invite will be accepted for this trunk. The Credentials List provides a username and password that will be used to authenticate a SIP Invite.
   </Note>

   **To create an IP Access Control List:**

   1. To add a new IP Access Control List, click **+ Add New IP ACL**.
   2. In the Create New IP Access Control List window, enter the name for your IP Access Control List (for example, TestACL) and then enter the IP addresses to be whitelisted in the IP Address List field.

      <Note>
        **Note:** You can add multiple comma-separated IP addresses.
      </Note>
   3. Click **Create ACL** to save and add your IP Access Control List.

   **To create a Credentials List:**

   1. To add a new Credentials List, click **+ Add New Credentials List**.
   2. In the Create Credentials List window, enter a name for your Auth Group (for example, TestCredList), a username, and a password.
   3. Click **Create Credentials List** to save and add your Credentials List.

   Select an IP Group, Auth Group, or both.

   Under Secure Trunking, use the Disabled/Enabled toggle button to enable secure trunking.

   <Note>
     **Note:** By default, secure trunking is disabled, but we strongly recommend you enable it, as we discuss in the next section.
   </Note>
4. Click **Create Trunk** to create your outbound trunk.

## Secure trunking on outbound trunks

To ensure that the information shared between your communication infrastructure and Zentrunk is secure, we recommend using the Secure Trunking feature. You can secure your trunk by encrypting and authenticating the signaling and media data packets involved for a SIP call over the internet.

### Encrypt signaling packets

You can encrypt signaling by using TLS (Transport Layer Security) protocol. Communication over TLS ensures authentication between two transport endpoints over an unsecured path for the SIP messages. We support TLS versions 1.2 and 1.3.

* **If Secure Trunking is enabled**: Zentrunk will communicate with your PBX or SBC over **TLS** for **Signaling**.
* **If Secure Trunking is disabled**: The calls will be over **TCP/UDP** for **Signaling**.

### Encrypt media packets

Zentrunk uses Secure Real-Time Protocol (SRTP) to secure RTP (media) packets.

* **If Secure Trunking is enabled**: Zentrunk will communicate with your PBX or SBC over **SRTP** for **Media**.
* **If Secure Trunking is disabled**: The calls will be over **RTP** for **Media**.

<Note>
  **Note:** You can use SRTP regardless of the SIP signaling messages being on TCP/UDP. However, Plivo strongly recommends you enable a secure mode of communication between your infrastructure and Zentrunk.
</Note>

## Inbound trunks (origination)

<Frame>
    <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/inbound-phone-number.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=e7bd7b93d055b6da5fd634535c383cb0" alt="" width="1255" height="687" data-path="images/inbound-phone-number.png" />
</Frame>

<Warning>
  **Only inbound trunks can be attached to phone numbers.** Outbound trunks are used by your applications to place calls through Plivo but cannot be mapped to phone numbers in the console. If you need both inbound and outbound capabilities, create separate trunks for each direction.
</Warning>

With Zentrunk, you can instantly access the inbound phone number DIDs in Plivo's inventory of more than 5 million phone numbers representing more than 60 countries. Each phone number comes with unlimited concurrent call capacity. Zentrunk customers can also instantly search, filter, and provision fixed, mobile, toll-free, and SMS-enabled phone numbers through the Zentrunk API or user interface. Also, our carrier team can help you to port your phone numbers to Zentrunk from your current provider.

### Create an inbound trunk

<Frame>
    <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/inbound-trunk.gif?s=f77a165552b4e44ec441f53d2856be9a" alt="" width="1024" height="562" data-path="images/inbound-trunk.gif" />
</Frame>

To create an inbound trunk:

1. In the Plivo console, visit Zentrunk > [Inbound Trunks](https://cx.plivo.com/sip-trunking) and click **Create New Inbound Trunk**.
2. Under Trunk Details, enter a name for your trunk (for example, Plivo Inbound).

   <Note>
     **Note:** The Enabled checkbox is selected by default.
   </Note>
3. Under Trunk Authentication, select the Primary URI and Fallback URI of your PBX.

   <Note>
     **Note:** The Primary URI is the FQDN or IP address to which all calls are forwarded first. If the Primary URI is unresponsive, calls will be forwarded to the Fallback URI.
   </Note>

   To add a new Primary or Fallback URI, click **Add New URI**.

   On the Create URI window, enter a name for your URI (for example, inbounduri), and then enter the URI (the FQDN or IP address of your VoIP infrastructure).

   To enable Authentication, click on the **Authentication** option and provide your username and password.

   Click **Create URI** to save and add your URI.
4. Once you’ve created and selected your Primary and Fallback URI, click **Create Trunk**. Your inbound trunk will be created.

### Assigning an inbound trunk to a phone number

The next task is to link your trunk with phone numbers. You can link the trunk with existing phone numbers in your account or buy a new phone number to use.

1. If you wish to use existing numbers, select the phone numbers under the **Current Phone Numbers** section, and click **Link Selected Numbers**.
2. If you wish to use a new number, navigate to the **Buy New Number** section and choose the country, prefix, type, capability, and click on **Search**.
3. Select a phone number and click **Buy Number**. The number will be added to your account and linked with your inbound trunk.

To learn more about buying a Plivo phone number, visit our [Buy a Phone Number Quickstart Guide](/numbers/phone-numbers#buy-a-phone-number).
