# Source: https://plivo.com/docs/sip-trunking/interconnection-guides/configuring-x-lite.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring X-lite (Now Bria Solo)

> Set up Bria Solo softphone with Zentrunk — test inbound and outbound calls

## Overview

This guide will help you test out your origination and termination setup by configuring a VoIP soft client. You can follow the step-by-step instructions available in this guide to configure X-lite (now Bria Solo). Testing your origination and termination setup using a VoIP client should help you to understand the use of Zentrunk. You can test the setup for outbound and inbound calls even before implementing Zentrunk.

## Prerequisites

To get started, you need:

* **Plivo account**: [Sign up](https://cx.plivo.com/signup) to get a free trial account.

* **Bria account and application:** You can use your email address to sign up for [Bria Solo](https://solo.softphone.com/login) and use the free trial plan for termination and origination setup. Once you’ve logged in, download the app from the [Bria Solo dashboard](https://solo.softphone.com/dashboard/) for your preferred platform.

* **Plivo Number** (*for inbound calls*): You need to buy a Plivo number to receive incoming calls and to forward them to your trunk.

## Outbound — Configure ZT for termination

Follow these steps to create an outbound trunk using Zentrunk and configure it on the Bria Solo application to make outbound calls.

### Create an outbound trunk

<Frame>
    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/create-ob-trunk.gif?s=5185eee54d8375c4b4b5964770fd73ca" alt="" width="1024" height="545" data-path="images/create-ob-trunk.gif" />
</Frame>

1. On the [Outbound Trunks](https://cx.plivo.com/sip-trunking) page of the console, click **Create New Outbound Trunk**.
2. In the New Trunk window, enter a name for your trunk (for example, Bria\_termination).
   <Note>
     **Note:** By default, the trunk is enabled.
   </Note>
3. Under Trunk Authentication, select the IP Access Control List, the Credentials List, or both.
   <Note>
     **Note:** Make sure you choose either an IP Access Control List or a Credentials List. The IP Access Control List is a list of the IP addresses from which a SIP invite may be accepted for this trunk. The Credentials List provides a username and password used to authenticate the SIP invite.
   </Note>
4. To create a Credentials List:
   1. Click **+ Add New Credentials List**.
   2. In the Create Credentials List window, enter the name for your auth group (for example, Bria\_termination), username, and password.
   3. Click **Create Credentials List** to save and add your Credentials List.
5. Select the Credentials List, then click **Create Trunk** to create your outbound trunk.
6. Copy and store the **Termination SIP Domain**; you’ll need it when you configure Bria Solo for termination.

### Configure the trunk on Bria

<Frame>
    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/configure-ob-trunk.gif?s=e86c30a7044762850ccdaee755b3f78d" alt="" width="1024" height="545" data-path="images/configure-ob-trunk.gif" />
</Frame>

1. [Sign up](https://solo.softphone.com/signup) for a Bria Solo free-trial account and [log in](https://solo.softphone.com/login).
2. Under the Voice and Video section, click on \*\*Configure Voice and Video. You will be redirected to the Voice Servers and Services page.
3. Click on **Add Voice Configuration** and select the Configure SIP Settings option.
4. Fill the details in the New Voice Configuration window with the details of the outbound trunk created on the Plivo console:
   1. Provide a Service Label — for example, “Plivo Termination.”
   2. Copy and paste the Termination SIP Domain in the Domain field. This is the information that you stored when you created an outbound trunk.
   3. Provide a caller ID for your outbound calls in the SIP Username/Call Extension field.
   4. Configure the Authorization Username and SIP/Voice Password fields with the username and password of the Credentials List you created on the console for the outbound trunk.
5. Go to the sService Settings tab in the New Voice Configuration window and uncheck the “Register with domain and receive calls” option.
6. Click on **Save and Close** to save the configuration.

### Terminate calls from Bria

<Frame>
    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/terminate-calls.gif?s=c473a350ab6bfd7cf71db8a39e50235f" alt="" width="1024" height="545" data-path="images/terminate-calls.gif" />
</Frame>

Download the Bria Solo app from the Downloads section on your [Bria Dashboard](https://solo.softphone.com/dashboard/), open it, and log in to the Bria account. You can then dial out using the outbound trunk created on your Plivo account.

## Inbound — Configure ZT for origination

### Inbound configuration on PBX

Once you’re done with the inbound configuration of any [supported PBXes](/sip-trunking/interconnection-guides/overview/), take note of these details to create an inbound trunk using Zentrunk on the [Plivo console](https://cx.plivo.com/sip-trunking).

1. IP address or FQDN to which an inbound call is to be routed.
2. Credentials related to the ACL with which the inbound trunk is configured on your PBX.

#### Sample details

Use these sample values from the [Freeswitch configuration](/sip-trunking/interconnection-guides/freeswitch/#configuring-an-inbound-trunk) for the test setup:

* IP address: 13.212.193.240
* Username: 1000
* Password: 1234

### Create an inbound trunk

<Frame>
    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/part1.gif?s=11e111647376da612e64cefe875bd016" alt="" width="1920" height="1156" data-path="images/part1.gif" />
</Frame>

1. On the [Inbound Trunks](https://cx.plivo.com/sip-trunking) page of the Plivo console, click **Create New Inbound Trunk**.
2. In the New Trunk window, enter a name for your trunk (for example, Plivo Inbound).
   <Note>
     **Note:** The Enabled checkbox is selected by default.
   </Note>
3. Select the Primary URI and Fallback URI of your PBX.
   <Note>
     **Note:** The Primary URI is the FQDN or IP address to which all calls are forwarded first. If the Primary URI is unresponsive, the calls will be forwarded to the Fallback URI.
   </Note>
4. To add a new Primary or Fallback URI, click **Add New URI**.
5. On the Create URI window, enter a name for your URI (for example, inbounduri), and then enter the URI (the FQDN or IP Address of your VoIP infrastructure).
6. Click **Create URI** to save and add your URI.
7. Once you have created and selected your Primary and Fallback URI, click **Create Trunk**. Your inbound trunk will be created.

### Configure the trunk with a Plivo number

<Frame>
    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/part2.gif?s=853bac58def3316468bc198cafbb7189" alt="" width="1920" height="1156" data-path="images/part2.gif" />
</Frame>

1. Once you click on **Create Trunk** in the next window, you can link your trunk with phone numbers.
2. You can either link the trunk with your existing phone numbers in your account or buy a new phone number and link the trunk.
3. If you want to use your existing numbers, select the phone numbers under the **Current Phone Numbers** section, and click **Link Selected Numbers**.
4. If you want to use a new number, navigate to the **Buy New Number** section and choose the country, prefix, type, capability, and click on Search.
5. Select a phone number and click **Buy Number**. The number will be added to your account and linked with your inbound trunk.

To learn more about renting a Plivo phone number, see our guide to [renting a number](/numbers/phone-numbers#buy-a-phone-number).

### Configure the user with Bria

<Frame>
    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/part3.gif?s=118b57ede71597f658e5730ae85afb7a" alt="" width="1200" height="723" data-path="images/part3.gif" />
</Frame>

1. [Sign up](https://solo.softphone.com/signup) for a Bria Solo free trial account and [log in](https://solo.softphone.com/login).
2. Under the Voice and Video section, click on **Configure Voice and Video**. You will be redirected to the Voice Servers and Services page.
3. Click on **Add Voice Configuration** and select **Configure SIP Settings**.
4. Fill the details on the New Voice Configuration window with the details of the inbound trunk configured on your PBX:
   1. Provide a Service Label — for example, “Plivo Origination.“
   2. Copy and paste the Origination SIP URI in the Domain field. This is the information that you stored when you create the inbound trunk.
   3. Configure the Authorization Username and SIP/Voice Password fields with the username and password of the ACL you updated while configuring the trunk on your PBX. In this guide, we’ll use "1000" as the username and "1234" as the password.
5. Go to the Service Settings tab in the New Voice Configuration window and provide the IP address of the PBX in the SIP Proxy field. Check the “Register with domain and receive calls” option if it’s unchecked.
6. Click **Save and Close**.

### Receive incoming calls on Bria

<Frame>
    <img src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/part4.gif?s=524febd2f55c4cee081cb6484d313fb6" alt="" width="1920" height="1156" data-path="images/part4.gif" />
</Frame>

Download the Bria Solo application from the Downloads section on the [Bria dashboard](https://solo.softphone.com/dashboard/) and start receiving inbound calls.

1. Open the Bria Solo application.
2. Log in to the Bria account using the same email address and password you used to create the Bria Solo account.
3. Once the login is successful, you can receive calls on the Plivo phone number to which the inbound trunk is assigned. The calls will be routed to the user configured on the Bria Solo application using the inbound trunk created on your Plivo account.
