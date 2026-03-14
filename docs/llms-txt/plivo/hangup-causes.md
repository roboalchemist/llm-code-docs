# Source: https://plivo.com/docs/voice/troubleshooting/hangup-causes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hangup Causes

> Voice API hangup codes, causes, and troubleshooting

Plivo identifies why and how calls are disconnected in call detail records (CDR), which you can [retrieve via API](/voice/api/call/retrieve-a-call/) or view on the Plivo console at Voice → Logs → [Calls](https://cx.plivo.com/logs?tab=voice).

Hangup information is also included in callback requests:

* **Outbound API calls**: Sent to `hangup_url` specified in [Make Call API](/voice/api/call/make-a-call/)
* **Incoming calls**: Sent to `hangup_url` in the [Plivo application](/account/api/application/)
* **Dial XML calls**: Sent to `callbackUrl` in DialHangup events

***

## Hangup Sources

| Source             | Description                                             |
| ------------------ | ------------------------------------------------------- |
| **Caller**         | Call hung up by the caller                              |
| **Call recipient** | Call hung up by the dialed party                        |
| **Plivo**          | Plivo initiated hangup (various reasons detailed below) |
| **Carrier**        | Hangup signal from remote carrier                       |
| **API Request**    | Terminated via Hangup or Cancel Call API                |
| **Answer XML**     | Hung up using Hangup XML element                        |
| **Error**          | Error condition terminated the call                     |
| **Unknown**        | Hangup source could not be determined                   |

***

## Hangup Causes

<AccordionGroup>
  <Accordion title="Normal Completions (4000-4030)">
    Normal call terminations - typically no action required.

    | Code | Cause                           | Description                         | Next Steps                                     |
    | ---- | ------------------------------- | ----------------------------------- | ---------------------------------------------- |
    | 4000 | `Normal Hangup`                 | Call terminated normally            | None - call completed successfully             |
    | 4010 | `End Of XML Instructions`       | No more XML instructions to execute | None - normal for XML-controlled calls         |
    | 4020 | `Multiparty Call Ended`         | MPC ended via API or max duration   | None - check if max duration was intentional   |
    | 4030 | `Kicked Out Of Multiparty Call` | Participant removed via API         | None - verify participant removal was expected |
  </Accordion>

  <Accordion title="Canceled Calls (1000-1020)">
    Calls canceled before being answered.

    | Code | Cause                                        | Description                                                           | Next Steps                                             |
    | ---- | -------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------ |
    | 0    | `Unknown`                                    | Hangup reason undetermined. Known bug: Delete All Calls API sets this | Check call logs for context                            |
    | 1000 | `Canceled`                                   | Call canceled via Hangup Call API before answer                       | None - intentional cancellation                        |
    | 1010 | `Canceled (Out Of Credits)`                  | Account ran out of credits                                            | Add credits. Enable auto-recharge in Console → Billing |
    | 1020 | `Canceled (Simultaneous dial limit reached)` | Simultaneous dial limit exceeded                                      | Reduce concurrent dials to same destination            |
  </Accordion>

  <Accordion title="Destination Issues (2000-2070)">
    Issues with the destination number or endpoint.

    | Code | Cause                         | Description                           | Next Steps                                                                                        |
    | ---- | ----------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------- |
    | 2000 | `Invalid Destination Address` | Destination number/endpoint invalid   | Use E.164 format (+12292442099). Verify number is valid                                           |
    | 2010 | `Destination Out Of Service`  | Destination unavailable               | Retry later. Verify destination is active                                                         |
    | 2020 | `Endpoint Not Registered`     | SIP endpoint unregistered/unreachable | Verify endpoint is logged in. Check [SDK troubleshooting](/sdk/client/troubleshooting-guide/)     |
    | 2030 | `Destination Country Barred`  | Country disabled in geo permissions   | Enable country in Console → Voice → [Geo Permissions](https://cx.plivo.com/geo-permissions/voice) |
    | 2040 | `Destination Number Barred`   | Premium rate numbers disabled         | Enable high-risk permissions in Console → Voice → Geo Permissions                                 |
    | 2050 | `Destination Prefix Barred`   | Prefix not permitted                  | Enable prefix in Console → Voice → Geo Permissions                                                |
    | 2060 | `Loop Detected`               | B-leg would redial A leg's number     | Fix routing logic to prevent loops                                                                |
    | 2070 | `Violates Media Anchoring`    | India PSTN regulation violation       | For India calls: server must be in India. Don't mix PSTN and WebRTC in conferences                |
  </Accordion>

  <Accordion title="Call Rejections (3000-3050)">
    Calls rejected by destination or carrier.

    | Code | Cause                | Description                           | Next Steps                                  |
    | ---- | -------------------- | ------------------------------------- | ------------------------------------------- |
    | 3000 | `No Answer`          | Destination unavailable/unreachable   | Retry. Check if destination is online       |
    | 3010 | `Busy Line`          | Destination is busy                   | Retry later or implement voicemail fallback |
    | 3020 | `Rejected`           | Call rejected by called party         | None - recipient declined the call          |
    | 3030 | `Unknown Caller ID`  | Non-Plivo number used as caller ID    | Use a Plivo-rented number as caller ID      |
    | 3040 | `Forbidden`          | Destination rejected/blocked call     | Have recipient check for blocked numbers    |
    | 3050 | `Unallocated number` | Destination invalid or out of service | Verify destination number accuracy          |
  </Accordion>

  <Accordion title="Carrier Errors (3070-3140)">
    Errors from remote carrier or network.

    | Code | Cause                                | Description                          | Next Steps                                                     |
    | ---- | ------------------------------------ | ------------------------------------ | -------------------------------------------------------------- |
    | 3070 | `Request timeout`                    | Carrier didn't respond in time       | Retry. Check carrier availability                              |
    | 3080 | `Internal server error from carrier` | Carrier encountered error            | Retry. If persistent, contact support                          |
    | 3090 | `Network congestion from carrier`    | Carrier network overloaded           | Retry with backoff                                             |
    | 3100 | `Busy everywhere`                    | All destination endpoints busy       | Retry later                                                    |
    | 3110 | `Declined`                           | Destination cannot/won't participate | Verify destination accepts calls                               |
    | 3120 | `User does not exist anywhere`       | End user doesn't exist               | Verify destination number                                      |
    | 3130 | `Spam block`                         | Carrier rejected due to spam flag    | Register number with STIR/SHAKEN. Consider different caller ID |
    | 3140 | `DNO Caller ID`                      | Caller ID on Do Not Originate list   | Use different number - this one is inbound-only                |
  </Accordion>

  <Accordion title="System Errors (5000-5020)">
    Internal system or network errors.

    | Code | Cause            | Description                    | Next Steps                                                        |
    | ---- | ---------------- | ------------------------------ | ----------------------------------------------------------------- |
    | 5000 | `Network Error`  | Fatal network condition        | [Contact Plivo support](https://support.plivo.com) with call UUID |
    | 5010 | `Internal Error` | Plivo system error             | [Contact Plivo support](https://support.plivo.com) with call UUID |
    | 5020 | `Routing Error`  | Could not route to destination | [Contact Plivo support](https://support.plivo.com) with call UUID |
  </Accordion>

  <Accordion title="Timeouts (6000-6020)">
    Calls ended due to timeout conditions.

    | Code | Cause                  | Description                      | Next Steps                                                                           |
    | ---- | ---------------------- | -------------------------------- | ------------------------------------------------------------------------------------ |
    | 6000 | `Scheduled Hangup`     | Max call duration reached        | None - configure `time_limit` (API) or `timeLimit` (Dial XML) if longer calls needed |
    | 6010 | `Ring Timeout Reached` | Not answered within ring timeout | Increase `ring_timeout` (API) or `timeout` (Dial XML). Default is 120 seconds        |
    | 6020 | `Media Timeout`        | No media packets for 60 seconds  | Check network connectivity. May indicate lost connection                             |
  </Accordion>

  <Accordion title="URL Errors (7011-7034)">
    Errors fetching or validating callback URLs.

    | Code | Cause                             | Description                        | Next Steps                                               |
    | ---- | --------------------------------- | ---------------------------------- | -------------------------------------------------------- |
    | 7011 | `Error Reaching Answer URL`       | Non-2xx response from answer URL   | Verify URL is accessible. Check server logs              |
    | 7012 | `Error Reaching Action URL`       | Non-2xx response from action URL   | Verify URL is accessible (only fails if `redirect=true`) |
    | 7013 | `Error Reaching Transfer URL`     | Non-2xx response from transfer URL | Verify URL is accessible                                 |
    | 7014 | `Error Reaching Redirect URL`     | Non-2xx response from redirect URL | Verify URL is accessible                                 |
    | 7022 | `Invalid Action URL`              | Action URL not valid               | Ensure URL starts with `http://` or `https://`           |
    | 7023 | `Invalid Transfer URL`            | Transfer URL not valid             | Ensure URL starts with `http://` or `https://`           |
    | 7024 | `Invalid Redirect URL`            | Redirect URL not valid             | Ensure URL starts with `http://` or `https://`           |
    | 7032 | `Invalid Method For Action URL`   | Unsupported HTTP method            | Use only GET or POST                                     |
    | 7033 | `Invalid Method For Transfer URL` | Unsupported HTTP method            | Use only GET or POST                                     |
    | 7034 | `Invalid Method For Redirect URL` | Unsupported HTTP method            | Use only GET or POST                                     |
  </Accordion>

  <Accordion title="XML Errors (8011-8014)">
    Invalid Plivo XML returned by URLs.

    | Code | Cause                  | Description                       | Next Steps                                       |
    | ---- | ---------------------- | --------------------------------- | ------------------------------------------------ |
    | 8011 | `Invalid Answer XML`   | Answer URL returned invalid XML   | Check debug logs in Console. Validate XML syntax |
    | 8012 | `Invalid Action XML`   | Action URL returned invalid XML   | Check debug logs. Only fails if `redirect=true`  |
    | 8013 | `Invalid Transfer XML` | Transfer URL returned invalid XML | Check debug logs. Validate XML syntax            |
    | 8014 | `Invalid Redirect XML` | Redirect URL returned invalid XML | Check debug logs. Validate XML syntax            |
  </Accordion>

  <Accordion title="Special Cases (9000-9110)">
    Specialized hangup scenarios.

    | Code | Cause                          | Description                             | Next Steps                                    |
    | ---- | ------------------------------ | --------------------------------------- | --------------------------------------------- |
    | 9000 | `Lost Race`                    | Another parallel B-leg answered first   | None - normal for simultaneous dial           |
    | 9100 | `Machine Detected`             | Answered by answering machine           | None - occurs when `machine_detection=hangup` |
    | 9110 | `Confirm Key Challenge Failed` | Participant failed to enter confirm key | Inform participant of required DTMF input     |
  </Accordion>
</AccordionGroup>

***

## Getting Help

If issues persist after troubleshooting:

1. View debug logs in Console → Voice → Logs → Calls
2. Note the Call UUID and hangup code
3. Contact [Plivo Support](https://support.plivo.com) with this information
