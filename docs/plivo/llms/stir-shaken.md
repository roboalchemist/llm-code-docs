# Source: https://plivo.com/docs/voice/concepts/stir-shaken.md

# Source: https://plivo.com/docs/sip-trunking/concepts/stir-shaken.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Zentrunk STIR/SHAKEN (US/CA)

> STIR/SHAKEN caller ID authentication for US and Canadian SIP trunking calls

STIR/SHAKEN is basically used in the US and Canada only. It is a framework or a set of protocols that’s designed to prevent caller ID spoofing, which is often used in robocalling. With it, carriers can validate that your calls originate from a trusted source.

To implement STIR/SHAKEN, Plivo sends a custom SIP header, **X-Plivo-Stir-Verification**, as part of the SIP response. Plivo users will also see a parameter called **STIR verification** on the console under Zentrunk > [Logs](https://cx.plivo.com/sip-trunking) and on the call detail record (CDR) for each call.

Attestation is the stamp of the legitimacy of a call provided by the originating service provider, authenticating that the call originated from its network and is then passed to the terminating service provider for verification.

Three levels of call attestations are provided for calls originating from the Plivo network.

* Full attestation (A) — the service provider has authenticated its relationship with the customer making the call and the customer is authorized to use the calling number.
* Partial attestation (B) — the service provider has authenticated its relationship with the customer making the call, but cannot verify that the customer is authorized to use the calling number.
* Gateway attestation (C) — the service provider has authenticated that it has placed the call on its network, but has no relationship with the originator of the call (for example, a call received from an international gateway).

## Outbound calling from Plivo’s network

For outbound calls, STIR verification may have three possible statuses:

* **Verified** status applies to calls that obtain **Full \*\*attestation (A\*\***). This means Plivo is able to validate the calling line identification (CLI) or the call originated from a rented DID on the Plivo platform. This DID should belong to the same Plivo account that originates outbound calls.
* **Not Verified** status applies to calls that have either Partial or Gateway (**B or C**) attestation or that are **unsigned**. This status indicates that Plivo lacks sufficient information for A-level attestation and the calling number is not a Plivo rented DID.
* **Not Applicable** indicates that STIR/SHAKEN doesn’t apply to this call, as is the case if a call is not addressed to a US number.

Plivo will sign outbound calls as Verified (attestation A) for calls that use a Plivo DID as caller ID. The DID used should be rented by the same Plivo account that originates the outbound calls. All other outbound calls, assuming they’re signed at all, are signed as Not Verified (attestation B or C).

Plivo strongly recommends that users place calls using Plivo-procured DIDs to ensure that calls going out of Plivo’s network receive A-level attestation.

### Plivo console logs

In the SIP response, Plivo sends a header called **X-Plivo-Stir-Verification** whose value is one of the aforementioned three states.

<Frame>
  <video autoPlay className="w-full aspect-video" src="https://mintcdn.com/plivo/GjxgkWYDEc2_LVPj/images/outbound-stir-zt.mp4?fit=max&auto=format&n=GjxgkWYDEc2_LVPj&q=85&s=ec1d657da1cb10cbd156d9c6ed4f1b16" data-path="images/outbound-stir-zt.mp4" />
</Frame>

<Note>
  **Notes:**

  1. Call signing logic is subjected to evolve as the STIR/SHAKEN ecosystem evolves.

  2. Since toll-free prefixes are the same across North America, some calls to non-US toll-free numbers may have the status “Verified” or “Not Verified,” but since STIR verification is applicable only to US calls, the actual status should be read as “Not Applicable.”
</Note>

### Example SIP traces

```
SIP/2.0 200 OK
From: <sip:+1NPANXXYYYY@xx.xx.xx.xx;transport=UDP>;tag=62d3ba76
To: <sip:+1NPANXXYYYY@yy.yy.yy.yy>;tag=N3ZgBy4N16DHD
Call-ID: yMFRondjahf1S3RsuMbRkQ..
CSeq: 2 INVITE
Supported: timer, path, replaces
Allow-Events: talk, hold, conference, presence, as-feature-event, dialog, line-seize, call-info, sla, include-session-description, presence.winfo, message-summary, refer
Content-Type: application/sdp
Content-Disposition: session
Content-Length: 275
Remote-Party-ID: "+1NPANXXYYYY" <sip:+1NPANXXYYYY@xx.xx.xx.xx>;party=calling;privacy=off;screen=no
User-Agent: Zentrunk
Accept: application/sdp
Allow: INVITE,ACK,CANCEL,BYE,UPDATE
Via: SIP/2.0/UDP 192.168.1.37:39948;received=192.168.1.37;branch=z9hG4bK-524287-1---e94ad5197a8a6fa9;rport=39948
X-Plivo-Stir-Verification: Verified
```

## Inbound calling to Plivo’s network

Any inbound call that has an identity header as part of the SIP INVITE will be verified using a verification service, and a corresponding verification status will be presented in the custom SIP header **X-Plivo-Stir-Verification**.

For inbound calls, STIR verification may have three possible statuses:

* **Verified**, when the verstat received as part of the PAID header is TN-Validation-Passed
* **Not Verified**, when the verstat received as part of the PAID header is either No-TN-Validation or TN-Validation-Failed
* **Not Applicable**, when an identity header is not received as part of the SIP INVITE and thus the incoming call source couldn’t be verified

Zentrunk will also pass through an identity header along with the PAID header if it received one from the originating service provider following verification. If Plivo receives the origID and the attestation indicator as part of enhanced verification status, it will pass this through along with the PAID header.

Example:

```
P-Asserted-Identity:<sip:+13339990000;verstat=TN-Validation-Passed@67.xxx.x.xx:5060>
```

### Plivo console logs

You can also see STIR verification values on the Zentrunk > [Logs](https://cx.plivo.com/sip-trunking) page of the console as part of CDR.

<Frame>
  <video autoPlay className="w-full aspect-video" src="https://mintcdn.com/plivo/_fSpYHZS4fGpqS0Z/images/inbound-stir-zt.mp4?fit=max&auto=format&n=_fSpYHZS4fGpqS0Z&q=85&s=a902c642832fe13c51ccff4b91b4c995" data-path="images/inbound-stir-zt.mp4" />
</Frame>

### Example SIP traces

```
INVITE sip:+1NPANXXYYYY@customer_URI:5060;transport=udp;timeout=60;carrierid=trunk_id SIP/2.0
Via: SIP/2.0/UDP xx.xx.xx.xx:5060;branch=z9hG4bKa6b8.0edbd44d535baed2b0be4db0758cda90.0
Max-Forwards: 66
From: <sip:1NPANXXYYYY@zt.plivo.com>;tag=jaXtc270DSg6B
To: <sip:+1NPANXXYYYY@customer_URI:5060;transport=udp;timeout=60;carrierid=trunk_id>
Call-ID: 2daa2eef-cfe9-4dfb-a4b0-5bdb79dcfecf
CSeq: 37104264 INVITE
Supported: timer, path, replaces
Allow-Events: talk, hold, conference, refer
Content-Type: application/sdp
Content-Disposition: session
Content-Length: 230
User-Agent: Zentrunk
Accept: application/sdp
Allow: INVITE,ACK,CANCEL,BYE,UPDATE
X-Plivo-Stir-Verification: Verified
X-Plivo-Region: us-east-1
Contact: <sip:btpsh-60c1899e-7f-1@xx.xx.xx.xx>
v=0
o=FreeSWITCH 1623296409 1623296410 IN IP4 xx.xx.xx.xx
s=FreeSWITCH
c=IN IP4 xx.xx.xx.xx
t=0 0
m=audio 10886 RTP/AVP 0 101
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=sendrecv
a=ptime:20
```

<Note>
  **Note:**
  Plivo is also working on sending in the P-Attestation-Indicator, to highlight the exact attestation level, and P-Origination-ID, for a traceback for robocalling.
</Note>
