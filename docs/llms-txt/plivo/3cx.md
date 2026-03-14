# Source: https://plivo.com/docs/sip-trunking/interconnection-guides/3cx.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring 3CX to Connect With Zentrunk

> Connect 3CX PBX with Zentrunk — inbound and outbound trunk setup

## Overview

Zentrunk, Plivo’s SIP trunking service, lets you connect with fixed and mobile phones in more than 200 countries. This page provides basic configuration information to get 3CX up and running with Plivo as the external SIP gateway.

To get started with Zentrunk using 3CX:

1. [Install 3CX](https://www.3cx.com/3cxacademy/videos/basic/installing/).
2. [Create a trunk using the Plivo console](/sip-trunking/).
3. [Configure an outbound trunk](/sip-trunking/interconnection-guides/3cx/#configuring-an-outbound-trunk).
4. [Configure an inbound trunk](/sip-trunking/interconnection-guides/3cx/#configuring-an-inbound-trunk).

## Configuring an outbound trunk

Configuring your outbound trunk involves these steps:

1. Adding an extension.
2. Adding a trunk.
3. Adding outbound rules.
4. Configuring your softphone.

**Note:** You can use any softphone; in this tutorial, we use Bria Solo (formerly X-Lite).

### To add an extension

1. From the Extension, click Add.
2. On the Extensions page, in the General tab, enter these details:
   * Extension — name of the extension
   * First Name and Last Name are optional
   * Outbound Caller ID — Caller ID for calls placed out on this trunk
     <Frame>
         <img src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/image_1_3cx.png?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=bbbbb025dad388c387533e2508d20418" alt="" width="940" height="657" data-path="images/image_1_3cx.png" />
     </Frame>
3. On the Extensions page, in the Options tab, uncheck the option **Disallow use of extension outside the LAN (Remote extensions using Direct SIP or STUN will be blocked)**, then click **OK**.
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_2_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=9af0828f321ea8993b7d9b887fa52e49" alt="" width="1203" height="504" data-path="images/image_2_3cx.png" />
   </Frame>

### To add a trunk

1. From your 3CX dashboard, click on **SIP Trunks**.
2. On the SIP Trunks page, click **Add SIP Trunk**.
3. On the Add SIP Trunk/VoIP Provider page:
   * Set **Select Country** to Generic
   * Set **Select Provider in your Country** to Generic SIP Trunk
   * Enter a trunk number in the **Main Trunk No** field.
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_3_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=60d11a794a8a9d164596cd1815025984" alt="" width="592" height="360" data-path="images/image_3_3cx.png" />
     </Frame>
4. Click **OK**.
5. Next, enter the **Trunk Details** fields.
   * **Name of Trunk**: A friendly name for the trunk
   * **Registrar/Server/Gateway Hostname or IP**: Trunk domain from the Plivo console
   * **Outbound Proxy**: The same trunk domain as Registrar/Server/Gateway Hostname or IP field
   * **Authentication ID (aka SIP User ID)**: User name associated with the trunk (if the trunk is auth based)
   * **Authentication Password**: Password associated with the trunk (if the trunk is auth based)
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_4_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=130dfa8a7710f4dcd46888442d2ed937" alt="" width="1189" height="797" data-path="images/image_4_3cx.png" />
     </Frame>
6. In the Route calls to section, under Destination for calls outside office hours, select the extension you created in the previous step for Destination for calls during office hours and Destination for calls outside office hours
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_5_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=59a4b91a0984c77fd755849aec1de36c" alt="" width="1191" height="710" data-path="images/image_5_3cx.png" />
   </Frame>
7. Next, on the Caller ID tab, enter the Configure Outbound Caller ID, and then click **OK**.
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_6_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=5b6cd6fbdb4ca433c4beab4fe8d98220" alt="" width="780" height="340" data-path="images/image_6_3cx.png" />
   </Frame>

### To add an outbound rule

1. From your 3CX dashboard, click on **Outbound Rules**.
2. On the outbound rules page, click on **Add** to add the outbound rules.
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_7_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=f37de8984dc442b9dfc35e45584dbd66" alt="" width="1209" height="822" data-path="images/image_7_3cx.png" />
   </Frame>
3. On the Add Outbound Rule page, fill these details:
   * **Rule name**: a name for the outbound rule
   * **Calls to numbers starting with the prefix**: Specify the prefix to which outbound calls are allowed (optional — leave blank if calls to all numbers need to be allowed)
   * **Calls from extension(s)**: Mention the extension(s) from which calls needs to be allowed
   * **Calls to Numbers with a length of**: Length of the number to which calls needs to be allowed (for example, 12)
4. Select the trunk for the routes in the **Make outbound calls** on section.

## Configuring an inbound trunk

Configuring your inbound Trunk involves:

1. Adding an extension
2. Adding a trunk
3. Configuring your softphone

**Note:** You can use any softphone; in this tutorial, we use Bria Solo (formerly X-Lite).

### To add an extension

1. From your 3CX dashboard, choose Extensions and click **Add**.
2. On the Extensions page, in the General tab, enter:
   * Extension — name of the extension
   * First Name and Last Name are optional
   * Outbound Caller ID — caller ID for calls placed out on this trunk.  **Note:** Note the authentication details, as they will be useful when you configure your softphone.
     <Frame>
         <img src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/image_1_3cx.png?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=bbbbb025dad388c387533e2508d20418" alt="" width="940" height="657" data-path="images/image_1_3cx.png" />
     </Frame>
3. On the Extensions page, in the Options tab, uncheck the **Disallow use of extension outside the LAN (Remote extensions using Direct SIP or STUN will be blocked)** option, and then click **OK**.
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_2_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=9af0828f321ea8993b7d9b887fa52e49" alt="" width="1203" height="504" data-path="images/image_2_3cx.png" />
   </Frame>

### To add a trunk

1. From your 3CX dashboard, click on **SIP Trunks**.

2. On the SIP Trunks page, click **Add SIP Trunk**.

3. On the Add SIP Trunk/VoIP Provider page:
   * Set **Select Country** to Generic.
   * Set **Select Provider in your Country** to Generic SIP Trunk.
   * Enter the **inbound number** on which you wish to receive calls in the **Main Trunk No** field.
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_3_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=60d11a794a8a9d164596cd1815025984" alt="" width="592" height="360" data-path="images/image_3_3cx.png" />
     </Frame>

4. Click **OK**.

5. On the General page, enter the Trunk Details:
   * Name of Trunk: a friendly name for the trunk
   * Registrar/Server/Gateway Hostname or IP: (0.0.0.0 to receive calls from all IP addresses)
   * Outbound Proxy: Trunk domain same as Registrar/Server/Gateway Hostname or IP Authentication.
   * Authentication ID (aka SIP User ID): User name associated with the trunk if the trunk is auth based.
   * Authentication Password: Password associated with the trunk if the trunk is auth based.
     <Frame>
         <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_4_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=130dfa8a7710f4dcd46888442d2ed937" alt="" width="1189" height="797" data-path="images/image_4_3cx.png" />
     </Frame>

6. In the **Route calls to** section, under Destination for calls outside office hours, select the extension you created in the previous step for Destination for calls during office hours and Destination for calls outside office hours.
   <Frame>
       <img src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/image_5_3cx.png?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=59a4b91a0984c77fd755849aec1de36c" alt="" width="1191" height="710" data-path="images/image_5_3cx.png" />
   </Frame>

### Configuring your softphone

You can receive calls when the account is successfully enabled on your softphone. Dial the number attached to your inbound trunk. The calls will first hit the Plivo inbound trunk, then go through your 3CX PBX to reach your endpoint.

To learn more about configuring Bria Solo for inbound calls, see our [X-lite configuration guide](/sip-trunking/interconnection-guides/configuring-x-lite/).
