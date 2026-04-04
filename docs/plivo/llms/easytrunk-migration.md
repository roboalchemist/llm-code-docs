# Source: https://plivo.com/docs/sip-trunking/interconnection-guides/easytrunk-migration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migration Guide: Easytrunk to Zentrunk Inbound Trunk

> Migrate from Easytrunk to Zentrunk — move trunks and phone numbers

## Overview

[Easytrunk](https://github.com/plivo/easytrunk) is a hosted voice application that forwards your Plivo number’s incoming calls to an IP PBX. Similar functionality is now available on Zentrunk, with added feature controls, and as a result, Plivo is decommissioning Easytrunk.

This document explains how to use Zentrunk, and migrate your trunks and phone numbers from Easytrunk, to help you migrate from Easytrunk to Zentrunk.

## Authenticate Plivo IPs

First, whitelist all [Zentrunk IP addresses](/sip-trunking/#signaling-ip-addresses) on your PBX.

## Create an inbound trunk

You can create an inbound trunk as per the [Configuration Guide](/sip-trunking/#inbound-trunks-origination). Follow all the steps except for  assigning an inbound trunk to a phone number. We’ll get to that below.

## Translations of Answer\_URL, Primary URI, and Fallback URLs

Below are the translations from answer\_url to Primary URI. The fallback\_url is the same as the Fallback URI.

| **answer\_url/fallback\_url (Voice XML Application)**                                                                                                                                                                                                                                                                                        | **Primary/Fallback URI (Zentrunk Inbound Trunk)**         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| [https://easytrunk.herokuapp.com/response/sip/inbound\_trunk/?DESTINATION=x.x.x.x](https://easytrunk.herokuapp.com/response/sip/inbound_trunk/?DESTINATION=x.x.x.x)<br />or<br />[https://easytrunk.plivo.com/response/sip/inbound\_trunk/?DESTINATION=x.x.x.x](https://easytrunk.plivo.com/response/sip/inbound_trunk/?DESTINATION=x.x.x.x) | x.x.x.x                                                   |
| [https://easytrunk.plivo.com/response/sip/inbound\_trunk/?DESTINATION=16182324812@173.208.200.98:4560----](https://easytrunk.plivo.com/response/sip/inbound_trunk/?DESTINATION=16182324812@173.208.200.98:4560----)                                                                                                                          | IP:PORT                                                   |
| [https://easytrunk.plivo.com/response/sip/inbound\_trunk/?DESTINATION=sip:number@sipgw.example.com](https://easytrunk.plivo.com/response/sip/inbound_trunk/?DESTINATION=sip:number@sipgw.example.com)                                                                                                                                        | [sipgw.example.com](https://sipgw.example.com/)           |
| [https://easytrunk.plivo.com/response/sip/inbound\_trunk/?DESTINATION=sip:number@sipgw.example.com:5160](https://easytrunk.plivo.com/response/sip/inbound_trunk/?DESTINATION=sip:number@sipgw.example.com:5160)                                                                                                                              | [sipgw.example.com:5160](https://sipgw.example.com:5160/) |
| [https://easytrunk.herokuapp.com/response/sip/inbound\_trunk/?DESTINATION=dial.example.com\&DialMusic=real&](https://easytrunk.herokuapp.com/response/sip/inbound_trunk/?DESTINATION=dial.example.com\&DialMusic=real&)                                                                                                                      | [dial.example.com](https://dial.example.com/)             |

1. If your Easytrunk application contains phone.plivo.com then you can use PHLO. For example, if your app contains something like [https://easytrunk.plivo.com/response/sip/inbound/?DESTINATION=sip:demo123012937129312312@phone.plivo.com](https://easytrunk.plivo.com/response/sip/inbound/?DESTINATION=sip:demo123012937129312312@phone.plivo.com), see [this guide](/voice/use-cases/call-forwarding/#creating-the-use-case-using-phlo) to create a PHLO to forward calls.
2. Alternatively, you can use Zentrunk by creating a user at your PBX. Refer to the [Freeswitch interconnection guide](/sip-trunking/interconnection-guides/freeswitch/#step-3-create-a-user).
3. There are some behavior changes with Zentrunk compared to Easytrunk:
   * Telephone number will be in E.164 format, including the plus sign (+).

   * Caller ID is always provided from the SIP header.

   * Make the necessary changes on your PBX to handle it. You can also look at the [Zentrunk interconnection guide](/sip-trunking/interconnection-guides/overview/) for inbound configuration.

## Assign the inbound trunk to a Plivo number

Assign the phone number to inbound Trunk

1. Go to the [Phone Numbers](https://cx.plivo.com/phone-numbers) page on the Plivo console.
2. Click on the phone number assigned to the application that contains an Easytrunk URL.
3. Note the application’s name.
4. Change the **Application Type** from XML Application to **Zentrunk.**
5. Select the created/appropriate trunk for the selected phone number.
6. Click on **Update Number** to save the changes

## Test

1. Make a test call to the phone number. You should see the calls forwarded to your IP PBX.
2. If it doesn’t work, switch to your original Easytrunk XML Application with the same application name and reach out to us for help with the migration.

[Contact us](https://support.plivo.com/hc/en-us) if you face any issues migrating to Zentrunk.
