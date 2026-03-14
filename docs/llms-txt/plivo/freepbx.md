# Source: https://plivo.com/docs/sip-trunking/interconnection-guides/freepbx.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring FreePBX to connect with Zentrunk

> Connect FreePBX with Zentrunk — inbound and outbound trunk setup

## Overview

Zentrunk is a SIP Trunking service from Plivo that allows you to connect with fixed and mobile phones in over 200 countries. Connect your cloud or on-premise communication infrastructure to Plivo’s Zentrunk SIP Trunking service to connect to your customers easily.

This documentation provides a basic configuration to get FreePBX up and running with Plivo as the external SIP gateway.

To get started with Zentrunk using FreePBX you would need to do the following:

1. [Install FreePBX on your environment](/sip-trunking/interconnection-guides/freepbx/#installation-of-freepbx).
2. [Create a Trunk on Zentrunk using Plivo Console](/sip-trunking/#create-an-outbound-trunk).
3. [Configure an Outbound Trunk](/sip-trunking/interconnection-guides/freepbx/#configuring-an-outbound-trunk).
4. [Configure the Inbound Trunk](/sip-trunking/interconnection-guides/freepbx/#configuring-an-inbound-trunk).

## Installation of FreePBX

To start using Zentrunk, you would need to install FreePBX on your environment. If you already have a FreePBX instance running, you may ignore this step.

For more information on installing FreePBX, check the following official installation guides:

* Follow the instructions [here](https://wiki.freepbx.org/display/FOP/Installing+FreePBX+13+on+Debian+8.1) to install FreePBX on Debian.
* Follow the instructions [here](https://wiki.freepbx.org/display/FOP/Installing+FreePBX+13+on+CentOS+7) to install FreePBX on CentOS.
* Follow the instructions [here](https://wiki.freepbx.org/display/FOP/Installing+FreePBX+13+on+Ubuntu+Server+14.04.2+LTS) to install FreePBX on Ubuntu.

## Create a Trunk on Zentrunk

You can create a trunk using Plivo Console. For more information on creating a Trunk on Plivo Console, see [Getting Started with Zentrunk](/sip-trunking/).

## Configuring an Outbound Trunk

Configuring your Outbound Trunk involves the following steps:

1. Adding a Trunk
2. Adding Outbound Routes
3. Configuring an Extension
4. Configuring X-Lite
   **Note:** There are many softphones that you can use (for example, X-Lite, Blink for Linux, etc). In this tutorial, we will be using the X-Lite Softphone.

### To add a trunk

1. From your FreePBX dashboard, hover over the **Connectivity** menu, and then click on **Trunks**.
2. On the Trunks page, click **Add Trunk**, and then click **Add SIP (chan\_sip) Trunk**.
3. On the Add Trunk page, enter the following details in the General tab:
   * **Trunk Name**: A friendly name for the trunk (for example, demo-trunk)
   * **Outbound Caller ID**: Caller ID for the calls placed using this trunk. This has to be in the following SIP format:
     ```sip  theme={null}
     "demo" <phone-number>
     ```
     <Frame>
         <img src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/image_0_freePBX.png?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=3315102a7bf7325c11a4ff82c960d0d2" alt="" width="1343" height="439" data-path="images/image_0_freePBX.png" />
     </Frame>
4. Next, enter the following details in the **sip Settings** tab:
   * **Host -** Termination SIP Domain of your Plivo Trunk
   * **Username -** Username for TestAuthGroup
   * **Password -** Password for TestAuthGroup
   * **Peer -** Creates a peer connection
     <Frame>
         <img src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/image_1_freepbx.png?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=0221ea8bfe4a44028f1c7bec851694ce" alt="" width="1350" height="402" data-path="images/image_1_freepbx.png" />
     </Frame>
5. Add dial pattern, you can choose to match any specific digits or use "." as a wildcard to match one or more characters.
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_2_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=0df9814eede7558138104b86c79aca37" alt="" width="1373" height="174" data-path="images/image_2_freepbx.png" />
   </Frame>
6. Enter a friendly name for the Trunk in the Trunk Name field, and then click **Submit**.
   A trunk will be created. You must now configure an outbound route to this trunk.

### To add an outbound route

1. From the **Connectivity** menu, click **Outbound Routes**.
2. On the Outbound Routes page, click **Add Outbound Route**.
3. In the Outbound Route - Add Route page, enter a friendly name for the route in the **Route Name** field.
4. From the list of **Trunk Sequence for Matched Routes**, select the trunk you created in the previous section (demo-outbound).
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_3_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=7fc18677742bacdc44ff8213c7532a98" alt="" width="1341" height="540" data-path="images/image_3_freepbx.png" />
   </Frame>
5. Next, on the Dial Patterns tab, enter the dial pattern that matches your system.
   **Note:** You can choose to match any specific digits or use "." as a wildcard to match one or more characters.
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_4_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=f637789de42f4f91837a210ccfe57aea" alt="" width="1330" height="318" data-path="images/image_4_freepbx.png" />
   </Frame>
6. Once you have entered your dial pattern, click **Submit**.
   The outbound route will be configured to your trunk. You must now configure an extension.

### To add an extension

1. From the **Applications** menu, click **Extensions**.
2. On the Extensions page, click **Add New Chan\_SIP Extension** from the **Add Extension** list.
   The Add SIP Extension page appears.
3. In the General tab, enter the following details:
   * User Extension - The extension number to dial to reach the user
   * Display name - The callerID name for calls from this user will be set to this name
   * Secret - Password configured for the device
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_5_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=a1b2a251e8e42ade265f76497eb59830" alt="" width="1354" height="425" data-path="images/image_5_freepbx.png" />
     </Frame>
4. Once done, click **Submit**.
   Your extension is created.
5. On the All Extensions tab, in the Actions column, click edit for your extension.
6. In the **Advanced** tab, under the **Edit Extension** section, change the configuration for **NAT Mode** to **Yes - (force\_rport,comedia)**.
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_6_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=932f0f637f19b8fc2927aa48a761f63c" alt="" width="1333" height="748" data-path="images/image_6_freepbx.png" />
   </Frame>
7. Click **Submit**.
   Your extension will be created.

**Asterisk SIP Settings**

1. From **Setting** menu, click **Asterisk SIP Settings**.
2. Next, enter the following details in the **General** **SIP Settings** tab:
   * **External Address** - Click on ‘**Detect Network Settings**’ and copy the value for future reference
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_7_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=bae213c89e81e816851eedf65516f201" alt="" width="1335" height="536" data-path="images/image_7_freepbx.png" />
     </Frame>
3. Next, enter the following details in the **Chan** **SIP Settings** tab in **Advance General Settings**  section :
   * **Bind port** - 5060
   * **TLS Bind Port** - 5061
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_8_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=56901baf99336477cc697c48ef81fe23" alt="" width="1328" height="461" data-path="images/image_8_freepbx.png" />
     </Frame>
4. Click **Apply Config** on the top navigation bar.
   All your configurations are complete. You can now configure X-Lite to use your Trunk.
   **Note:** In case you get an error while configuring your softphone, make sure you have clicked **Apply Config** on FreePBX.

## Configuring an Inbound Trunk

Configuring your Inbound Trunk involves the following steps:

1. Configuring an Extension
2. Adding Inbound Routes
3. Configuring X-Lite
   **Note:** There are many softphones that you can use (for example, X-Lite, Blink for Linux, etc). In this tutorial, we will be using the X-Lite Softphone.

### To add an extension

1. From the **Applications** menu, click **Extensions**.
2. On the Extensions page, click **Add New Chan\_SIP Extension** from the **Add Extension** list.
   The Add SIP Extension page appears.
3. In the General tab, enter the following details:
   * User Extension - The extension number to dial to reach the user
   * Display name - The callerID name for calls from this user will be set to this name
   * Secret - Password configured for the device
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_5_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=a1b2a251e8e42ade265f76497eb59830" alt="" width="1354" height="425" data-path="images/image_5_freepbx.png" />
     </Frame>
4. Once done, click **Submit**.
   Your extension is created.
5. On the All Extensions tab, in the Actions column, click edit for your extension.
6. In the **Advanced** tab, under the **Edit Extension** section, change the configuration for **NAT Mode** to **Yes - (force\_rport,comedia)**.
7. Addionally,check if rest of the values are configured in the below format:
   * DTMF Signaling  - RFC 2833
   * Connection Type - friend
   * Port - 5060
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_6_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=932f0f637f19b8fc2927aa48a761f63c" alt="" width="1333" height="748" data-path="images/image_6_freepbx.png" />
     </Frame>
8. Click **Submit**. Your extension will be created.

### To add an inbound route

1. From the **Connectivity** menu, click **Inbound Routes**.
2. On the Inbound Routes page, click **Add Inbound Route**.
3. In the General tab, enter the following details:
   * Description - Provide a meaningful description of what this incoming route is
   * DID Number - Define the expected DID Number if your trunk passes DID on incoming calls or leave it blank to match calls with any or no DID info.
   * Set Destination - Select **Extentions** from the options. Later select the extention which was created earlier.
     <Frame>
         <img src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/image_10_freepbx.png?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=192218de5a0dd07ff5cc4025814f37f5" alt="" width="1343" height="481" data-path="images/image_10_freepbx.png" />
     </Frame>
4. Click **Submit**. Your Inbound route will be created.

**Asterisk SIP Settings**

1. From **Setting** menu, click **Asterisk SIP Settings**.
2. Next, enter the following details in the **General** **SIP Settings** tab:
   * **External Address** - Click on ‘**Detect Network Settings**’ and copy the value for future reference
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_7_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=bae213c89e81e816851eedf65516f201" alt="" width="1335" height="536" data-path="images/image_7_freepbx.png" />
     </Frame>
3. Next, enter the following details in the **Chan** **SIP Settings** tab in **Advance General Settings**  section :
   * **Bind port** - 5060
   * **TLS Bind Port** - 5061
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_8_freepbx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=56901baf99336477cc697c48ef81fe23" alt="" width="1328" height="461" data-path="images/image_8_freepbx.png" />
     </Frame>
4. Click **Apply Config** on the top navigation bar.
   All your configurations are complete. You can now configure X-Lite to use your Trunk.
   **Note:** In case you get an error while configuring your softphone, make sure you have clicked **Apply Config** on FreePBX.
