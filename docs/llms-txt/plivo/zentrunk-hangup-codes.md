# Source: https://plivo.com/docs/sip-trunking/troubleshooting/zentrunk-hangup-codes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Zentrunk Hangup Codes

> SIP hangup codes, causes, and troubleshooting for Plivo SIP Trunking

Zentrunk uses four-digit hangup codes to identify call issues. Find these codes in the CDR under Zentrunk → [Logs](https://cx.plivo.com/sip-trunking) in the Plivo console.

***

## Hangup Sources

| Source       | Description                             |
| ------------ | --------------------------------------- |
| **Customer** | Hangup initiated by your infrastructure |
| **Carrier**  | Hangup initiated by the remote carrier  |
| **Zentrunk** | Hangup initiated by Plivo               |

***

## Hangup Codes

<AccordionGroup>
  <Accordion title="Normal Hangups (3000-3040)">
    Normal call terminations - typically no action required.

    | Code | Cause                             | Description                   | Next Steps                                                                  |
    | ---- | --------------------------------- | ----------------------------- | --------------------------------------------------------------------------- |
    | 3000 | `normal_hangup`                   | Normal hangup from carrier    | None - call completed normally                                              |
    | 3010 | `normal_hangup`                   | Normal hangup from user       | None - call completed normally                                              |
    | 3020 | `rtp_timeout`                     | Mid-call media timeout        | Check network stability. Verify firewall allows RTP ports (10000-20000 UDP) |
    | 3030 | `insufficient_plivo_credits`      | Call ended due to low credits | Add credits. Enable auto-recharge in Console → Billing                      |
    | 3040 | `abnormal_hangup_due_to_reinvite` | Re-invite rejected            | Check for changes in session parameters during call                         |
  </Accordion>

  <Accordion title="Authentication Errors (4000-4060)">
    Issues with credentials or authorization.

    | Code | Cause                          | Description                     | Next Steps                                          |
    | ---- | ------------------------------ | ------------------------------- | --------------------------------------------------- |
    | 4000 | `bad_request`                  | Malformed SIP request           | Check SIP packet format. Don't retry without fixing |
    | 4010 | `unauthorized_by_carrier`      | Carrier rejected authentication | Verify carrier credentials are not blacklisted      |
    | 4020 | `unauthorized`                 | Authentication required         | Add correct credentials to trunk configuration      |
    | 4030 | `insufficient_plivo_credits`   | No credits to start call        | Add credits to your account                         |
    | 4040 | `forbidden`                    | Carrier refused the request     | Authorization won't help - check with carrier       |
    | 4050 | `blacklisted_for_verification` | Number blacklisted by Zentrunk  | Contact Plivo support                               |
    | 4060 | `forbidden`                    | PBX authentication failed       | Verify credentials on your PBX                      |
  </Accordion>

  <Accordion title="Routing Errors (4070-4120)">
    Issues finding the destination or route.

    | Code | Cause                      | Description                   | Next Steps                                            |
    | ---- | -------------------------- | ----------------------------- | ----------------------------------------------------- |
    | 4070 | `trunk_not_found`          | Trunk lookup failed           | Verify trunk URI is correct in Console                |
    | 4080 | `route_not_found`          | No matching trunk URI         | Check incoming call route settings                    |
    | 4090 | `destination_not_found`    | No route to destination       | Verify destination number. Check carrier availability |
    | 4100 | `prefix_not_supported`     | Invalid number prefix         | Use correct country prefix for destination            |
    | 4110 | `secure_trunking_disabled` | TLS/SRTP used but not enabled | Enable Secure Trunking or use non-secure transport    |
    | 4120 | `destination_invalid`      | Invalid "To" number format    | Use E.164 format: +14155551234                        |
  </Accordion>

  <Accordion title="Caller ID Errors (4130-4200)">
    Issues with the caller ID used for the call.

    | Code | Cause                            | Description                           | Next Steps                                       |
    | ---- | -------------------------------- | ------------------------------------- | ------------------------------------------------ |
    | 4130 | `incorrect_callerid_non_numeric` | Caller ID is not numeric              | Use numeric caller ID only                       |
    | 4140 | `incorrect_callerid_too_short`   | Caller ID less than 6 digits          | Use full phone number as caller ID               |
    | 4190 | `unknown_caller_id`              | Non-Plivo number used as caller ID    | Use a Plivo-rented number as caller ID           |
    | 4200 | `dno_caller_id`                  | Caller ID is on Do Not Originate list | Use a different number. This one is inbound-only |
  </Accordion>

  <Accordion title="Format & Media Errors (4150-4270)">
    Issues with SIP message format or media negotiation.

    | Code | Cause                           | Description                 | Next Steps                                |
    | ---- | ------------------------------- | --------------------------- | ----------------------------------------- |
    | 4150 | `proxy_authentication_required` | Carrier requires proxy auth | Contact carrier for proxy credentials     |
    | 4160 | `request_timeout_carrier`       | No response from carrier    | Retry. Check carrier availability         |
    | 4170 | `request_timeout_customer`      | No response from your PBX   | Check PBX is online and reachable         |
    | 4220 | `unsupported_media_type`        | Unsupported codec           | Use PCMU, PCMA, or telephone-event codecs |
    | 4230 | `unsupported_uri_scheme`        | Unknown request URI         | Check SIP URI format                      |
    | 4270 | `session_interval_too_small`    | Session-expires too short   | Increase session timer interval           |
  </Accordion>

  <Accordion title="URI & Availability Errors (4310-4380)">
    Issues with origination URIs and temporary unavailability.

    | Code | Cause                   | Description                               | Next Steps                                  |
    | ---- | ----------------------- | ----------------------------------------- | ------------------------------------------- |
    | 4310 | `uri_not_found`         | Origination URI not found                 | Create origination URI and attach to trunk  |
    | 4320 | `uri_invalid`           | URI cannot be resolved                    | Verify domain resolves to valid IP address  |
    | 4330 | `temporary_unavailable` | Zentrunk temporarily unavailable          | Retry. May indicate CPS limit reached       |
    | 4340 | `temporary_unavailable` | Callee temporarily unavailable (carrier)  | Retry later. Destination may be offline     |
    | 4350 | `temporary_unavailable` | Callee temporarily unavailable (customer) | Check your PBX is online                    |
    | 4360 | `call_does_not_exist`   | Call ID mismatch                          | Check for duplicate Call-IDs in your system |
    | 4370 | `loop_detected`         | Call loop detected                        | Fix routing to prevent loops                |
    | 4380 | `too_many_hops`         | Hop limit exceeded                        | Reduce SIP proxy hops                       |
  </Accordion>

  <Accordion title="Call State Errors (4410-4550)">
    Issues with call state, busy, or cancellation.

    | Code | Cause                         | Description                 | Next Steps                            |
    | ---- | ----------------------------- | --------------------------- | ------------------------------------- |
    | 4410 | `user_busy`                   | Destination is busy         | Retry later or use voicemail fallback |
    | 4420 | `carrier_cancelled`           | Carrier cancelled the call  | Check carrier logs for reason         |
    | 4430 | `sdp_not_acceptable_here`     | SDP not supported           | Check SDP format compatibility        |
    | 4440 | `request_terminated`          | Zentrunk terminated request | Check logs for specific reason        |
    | 4500 | `request_pending`             | Another request in progress | Wait for current request to complete  |
    | 4520 | `security_agreement_required` | Security negotiation needed | Implement required security mechanism |
    | 4540 | `forbidden`                   | Zentrunk auth failure       | Contact Plivo support                 |
    | 4550 | `user_cancelled`              | User cancelled the call     | None - caller hung up before answer   |
  </Accordion>

  <Accordion title="Geo & Number Restrictions (4560-4590)">
    Calls blocked due to permissions or regulations.

    | Code | Cause                             | Description                        | Next Steps                                                                         |
    | ---- | --------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------- |
    | 4560 | `barred_country`                  | Country blocked in geo permissions | Enable country in Console → Geo Permissions                                        |
    | 4570 | `barred_number`                   | Number is barred                   | Contact support if this is unexpected                                              |
    | 4580 | `invalid_sip_packet`              | Malformed SIP packet               | Check SIP headers and request format                                               |
    | 4590 | `domestic_anchored_terms_not_met` | India media anchoring violation    | For India calls: server must be in India. Don't mix PSTN and WebRTC in conferences |
  </Accordion>

  <Accordion title="SDP & Codec Errors (4610-4640)">
    Issues with session description protocol or codecs.

    | Code | Cause                                | Description             | Next Steps                           |
    | ---- | ------------------------------------ | ----------------------- | ------------------------------------ |
    | 4610 | `ruri_not_acceptable_here`           | Unsupported Request-URI | Check URI format                     |
    | 4620 | `codec_not_acceptable_here`          | Unsupported codec       | Use PCMU, PCMA, or telephone-event   |
    | 4630 | `sdp_not_acceptable_here_by_carrier` | Carrier rejected SDP    | Check SDP compatibility with carrier |
    | 4640 | `sdp_not_acceptable_here_by_user`    | Your PBX rejected SDP   | Check SDP settings on your PBX       |
  </Accordion>

  <Accordion title="Server & Capacity Errors (5000-5200)">
    Server-side issues and capacity limits.

    | Code | Cause                                      | Description                      | Next Steps                                          |
    | ---- | ------------------------------------------ | -------------------------------- | --------------------------------------------------- |
    | 5000 | `service_unavailable_no_more_destinations` | No available routes              | Retry. Check carrier status                         |
    | 5010 | `port_limit_reached`                       | Maximum port capacity reached    | Contact support to increase capacity                |
    | 5020 | `not_implemented`                          | Unsupported functionality        | Check Zentrunk supported features                   |
    | 5030 | `not_implemented_at_carrier`               | Carrier doesn't support request  | Use different request method                        |
    | 5040 | `not_implemented_at_user`                  | Your PBX doesn't support request | Update PBX configuration                            |
    | 5180 | `cps_limit_reached`                        | Calls per second limit exceeded  | Reduce call rate or contact support to increase CPS |
    | 5190 | `concurrent_call_limit_exceeded`           | Too many simultaneous calls      | Wait or contact support to increase limit           |
    | 5200 | `server_timeout`                           | Timer expired                    | Retry the request                                   |
  </Accordion>

  <Accordion title="Mid-Call & Service Errors (5220-5360)">
    Errors occurring during active calls.

    | Code | Cause                                    | Description                          | Next Steps                               |
    | ---- | ---------------------------------------- | ------------------------------------ | ---------------------------------------- |
    | 5220 | `service_interrupted_by_customer`        | 4xx error during call (customer)     | Check your PBX logs                      |
    | 5230 | `service_interrupted_by_customer`        | 5xx/6xx error during call (customer) | Check your PBX logs                      |
    | 5240 | `service_interrupted_by_nomedia`         | Media error during call              | Check network connectivity, NAT settings |
    | 5250 | `internal_error`                         | Backend service issue                | Retry. Contact support if persistent     |
    | 5260 | `internal_error_routing`                 | Internal routing issue               | Retry. Contact support if persistent     |
    | 5270 | `internal_error_media_service`           | Media server issue                   | Retry. Contact support if persistent     |
    | 5290 | `internal_error_trunk`                   | Trunk URI fetch error                | Retry. Verify trunk configuration        |
    | 5300 | `bad_gateway`                            | Carrier returned 502                 | Check carrier status                     |
    | 5310 | `service_interrupted_by_carrier_4xx`     | 4xx error during call (carrier)      | Check carrier logs                       |
    | 5320 | `service_interrupted_by_carrier_5xx_6xx` | 5xx/6xx error during call (carrier)  | Check carrier status                     |
    | 5330 | `server_timeout`                         | Carrier timeout                      | Retry. Check carrier availability        |
    | 5340 | `server_timeout`                         | Your PBX timeout                     | Check PBX is responsive                  |
    | 5350 | `service_unavailable_by_carrier`         | Carrier temporarily unavailable      | Retry later                              |
    | 5360 | `service_unavailable_by_user`            | Your PBX temporarily unavailable     | Check PBX status                         |
  </Accordion>

  <Accordion title="Global Failures (6000-6070)">
    Final failures with no alternatives.

    | Code | Cause                     | Description                        | Next Steps                          |
    | ---- | ------------------------- | ---------------------------------- | ----------------------------------- |
    | 6000 | `busy_everywhere`         | All destinations busy              | Retry later. No voicemail available |
    | 6020 | `does_not_exist_anywhere` | User doesn't exist                 | Verify the destination number       |
    | 6030 | `alloted_timeout`         | Answer timeout exceeded            | Destination took too long to answer |
    | 6040 | `declined_from_carrier`   | Carrier declined the call          | Contact carrier for reason          |
    | 6070 | `not_acceptable`          | Session description not acceptable | Check SDP compatibility             |
  </Accordion>
</AccordionGroup>

***

## Getting Help

If issues persist after troubleshooting:

1. Check [Debug Logs](/sip-trunking/troubleshooting/zentrunk-debug-logs) for detailed call information
2. Download SIP PCAP from debug logs for analysis
3. Contact [Plivo Support](https://support.plivo.com) with the Call UUID and hangup code
