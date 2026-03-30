# Source: https://plivo.com/docs/sip-trunking/interconnection-guides/easytrunk-migration-phlo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migration Guide: Easytrunk to PHLO

> Migrate from Easytrunk to PHLO — forward inbound calls using PHLO

## Overview

Plivo’s PHLO allows you to quickly create and configure a similar Easy Trunk call Forwarding system for your business. This guide explains how you can migrate your existing [Easytrunk](https://github.com/plivo/easytrunk) hosted voice application to PHLO, which then forwards  your Plivo number’s incoming calls to an IP PBX and SIP endpoint.

## Prerequisites

1. **Create a Plivo account** *(if you don’t have one already)*: [Sign up](https://cx.plivo.com/signup) with your work email address and complete the phone verification step using your mobile number.
2. **Buy a Plivo number**: You must have a voice-enabled Plivo phone number to receive incoming calls. Purchase numbers from the Numbers section of your [Plivo console](https://cx.plivo.com/home) or using the [Numbers API](/numbers/).
3. **PHLO application**: When you receive a call on a Plivo voice-enabled number, you can control the call flow by associating a PHLO application to that Plivo phone number. Plivo will fetch the PHLO associated with the number and expect valid instructions via PHLO to handle the call. The following steps instruct you how to create a PHLO.

## Create a PHLO to forward inbound calls

To forward an incoming call, you can create and deploy a PHLO with a few clicks on the PHLO canvas. Refer to the instructions below  to create a PHLO that forwards an incoming call:

<Frame>
    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/easytrunk2phlo.gif?s=1edf469471119be460dec03feb7755e2" alt="" width="1024" height="545" data-path="images/easytrunk2phlo.gif" />
</Frame>

* On the side navigation bar, click **PHLO**. The PHLO page will appear and display your existing PHLOs, if any exist. If this is your first PHLO, then the PHLO page will be empty.
* Click **Create New PHLO** to build a new PHLO.
* In the **Choose your use-case** window, choose **Call Forwarding** use-case. The PHLO canvas will appear with a pre-built template for the **Call Forwarding** use-case.
* Configure the **Call Forward** node.
  * **From** field: This will be already configured with \{\{Start.call.from}}. Caller Id to display to the recipient of the forwarded call.
  * **To** field: List of recipients to forward the incoming call and to bridge into the active call. The list can contain IP PBXes, and SIP endpoints separated by a comma. Refer to the below example:
    * sip:[1NPANXXYYYY@sip.example.com](mailto:1NPANXXYYYY@sip.example.com)
    * sip:phonenumber\@192.0.0.1
    * sip:[sipendpoint@phone.plivo.com](mailto:sipendpoint@phone.plivo.com)
    <Note>
      **Note:** You must choose sequential for call forwarding configuration setting so that it will be dialed sequentially on failover.
    </Note>
* Once you have configured the node, click **Validate** to save the configurations.
* After you complete the configurations, provide a recognizable name for your PHLO and click **Save**. Your PHLO is now ready.

## Assign the PHLO to a Plivo number to forward incoming calls

Once you have created and configured your PHLO, assign your PHLO to a Plivo number.

#### To assign a PHLO to a number:

1. Log in to the [Plivo console](https://cx.plivo.com/home).
2. On the Product Navigation bar, click **Phone Numbers**.
3. On the Numbers page, under **Your Numbers**, click the phone number you want to use for the PHLO.
4. In the **Number Configuration** window, select **PHLO** from the **Application Type** list.
5. From the **PHLO Name** list, select the PHLO you wish to use with the phone number, then click **Update Number**.

<Frame>
    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/assign-phlo-forward.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=0dd6efea9b4a1d69e8dda54e7cf001e4" alt="" width="1440" height="785" data-path="images/assign-phlo-forward.png" />
</Frame>

## Test

Make a call to your Plivo phone number and see how the inbound call is forwarded to the list of IP PBXes and endpoint specified in the PHLO.

For more information about creating a PHLO app, see the [PHLO User Guide](/phlo/getting-started/getting-started).<br />
For information on components and their variables, see the [PHLO Components Library](/phlo/#components-library).
