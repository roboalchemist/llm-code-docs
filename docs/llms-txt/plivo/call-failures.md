# Source: https://plivo.com/docs/voice/troubleshooting/call-failures.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Call Failures

> Debug and resolve voice call issues including failed connections, one-way audio, and quality problems

Use this guide to diagnose and fix common voice call issues. Start with the symptom you're experiencing.

***

## Quick Diagnosis

<AccordionGroup>
  <Accordion title="Outbound calls not connecting">
    **Check in order:**

    1. Verify credits balance in Console → Billing
    2. Check geo permissions for destination country
    3. Verify caller ID is a Plivo number or verified
    4. Review [hangup cause](/voice/troubleshooting/hangup-causes) in call logs

    **Common causes:**

    | Hangup Cause                 | Solution                                            |
    | ---------------------------- | --------------------------------------------------- |
    | `destination_country_barred` | Enable country in Console → Voice → Geo Permissions |
    | `unknown_caller_id`          | Use Plivo-rented number as caller ID                |
    | `insufficient_credits`       | Add credits to account                              |
    | `invalid_destination`        | Use E.164 format (+14155551234)                     |
  </Accordion>

  <Accordion title="Inbound calls not reaching my app">
    **Check in order:**

    1. Verify number is assigned to an application (Console → Phone Numbers)
    2. Check application Answer URL is accessible
    3. Verify Answer URL returns valid Plivo XML
    4. Check for firewall blocking Plivo IPs

    **Debug steps:**

    1. Go to Console → Voice → Logs → Calls
    2. Find the failed call
    3. Check the hangup cause and debug logs
    4. Test your Answer URL manually with curl
  </Accordion>

  <Accordion title="Calls connect but no audio (one-way or silent)">
    **Common causes:**

    * Firewall blocking RTP/media ports
    * NAT traversal issues
    * Codec mismatch

    **Solutions:**

    1. Whitelist Plivo IP ranges for UDP ports 10000-60000
    2. Enable STUN/TURN if behind NAT
    3. Use standard codecs (G.711, Opus)

    See [Plivo IP Ranges](https://www.plivo.com/docs/voice/concepts/ip-addresses/) for whitelisting.
  </Accordion>

  <Accordion title="Calls dropping mid-conversation">
    **Check hangup cause in call logs:**

    | Hangup Cause           | Meaning                     | Solution                        |
    | ---------------------- | --------------------------- | ------------------------------- |
    | `scheduled_hangup`     | Max duration reached        | Increase `time_limit` parameter |
    | `media_timeout`        | No audio for 60 seconds     | Check network stability         |
    | `xml_end`              | No more XML instructions    | Add more XML or use `<Wait>`    |
    | `insufficient_credits` | Ran out of credits mid-call | Enable auto-recharge            |
  </Accordion>

  <Accordion title="Poor audio quality (echo, delay, choppy)">
    | Issue         | Likely Cause      | Solution                                          |
    | ------------- | ----------------- | ------------------------------------------------- |
    | Echo          | Acoustic feedback | Use headset, reduce speaker volume                |
    | Delay/latency | Network distance  | Use nearest Plivo region                          |
    | Choppy audio  | Packet loss       | Check internet connection, reduce bandwidth usage |
    | Robotic voice | Codec issues      | Use G.711 codec                                   |

    For persistent issues, capture a PCAP and contact [Plivo Support](https://support.plivo.com).
  </Accordion>
</AccordionGroup>

***

## Step-by-Step Debugging

### 1. Check Call Logs

1. Go to **Console → Voice → Logs → Calls**
2. Find the failed call by time or phone number
3. Note the **Hangup Cause** and **Hangup Source**
4. Click the call to view debug details

### 2. Verify Configuration

**For outbound calls:**

```bash  theme={null}
# Test your setup with curl
curl -i --user AUTH_ID:AUTH_TOKEN \
  -H "Content-Type: application/json" \
  -d '{"from": "+14155551234", "to": "+14155559876", "answer_url": "https://example.com/answer"}' \
  https://api.plivo.com/v1/Account/{auth_id}/Call/
```

**For inbound calls:**

* Verify number → application assignment in Console
* Test Answer URL returns valid XML

### 3. Test Answer URL

Your Answer URL must:

* Return HTTP 200 status
* Return `Content-Type: application/xml` or `text/xml`
* Return valid [Plivo XML](/voice/xml/overview)

**Example valid response:**

```xml  theme={null}
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Speak>Hello, this is a test call.</Speak>
</Response>
```

### 4. Check Firewall Settings

Plivo requires these ports open:

| Traffic         | Protocol | Ports       |
| --------------- | -------- | ----------- |
| SIP signaling   | UDP/TCP  | 5060, 5080  |
| Secure SIP      | TLS      | 5061        |
| RTP (audio)     | UDP      | 10000-60000 |
| HTTPS callbacks | TCP      | 443         |

See [IP Addresses](/voice/concepts/ip-addresses) for ranges to whitelist.

***

## Common Error Scenarios

### "Call immediately goes to voicemail"

**Possible causes:**

1. Carrier is blocking based on caller ID reputation
2. Number flagged as spam
3. Destination has call blocking enabled

**Solutions:**

* Register for STIR/SHAKEN attestation
* Use a different caller ID
* Contact carrier about spam flagging

### "API returns 403 Forbidden"

**Check:**

1. Account is verified and active
2. Geo permissions enabled for destination
3. Caller ID is verified or Plivo-owned
4. No outstanding balance issues

### "Calls work sometimes but not always"

**Debug steps:**

1. Check if failures correlate with specific destinations
2. Review call volume vs CPS limits
3. Check for carrier-specific issues in logs
4. Monitor for pattern (time of day, destination, etc.)

***

## Debug Logs

For detailed debugging, enable debug logs:

1. Go to **Console → Voice → Logs → Calls**
2. Click on the specific call
3. View the **Debug** tab for:
   * XML requests/responses
   * SIP signaling details
   * Timing information

***

## When to Contact Support

Contact [Plivo Support](https://support.plivo.com) if:

* Issue persists after following this guide
* You see `internal_error` or `routing_error` hangup causes
* Calls fail with no clear hangup cause
* You need PCAP analysis for audio issues

**Include in your support request:**

* Call UUID(s)
* Timestamp of failures
* Steps already tried
* Any error messages

***

## Related

* [Hangup Causes Reference](/voice/troubleshooting/hangup-causes)
* [Voice API Overview](/voice/api/overview)
* [IP Addresses](/voice/concepts/ip-addresses)
* [Account Limits](/voice/concepts/account-limits)
