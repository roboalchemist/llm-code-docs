# Source: https://plivo.com/docs/voice/api/calls.md

# Source: https://plivo.com/docs/sip-trunking/api/calls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Calls

> Retrieve call detail records (CDRs) and call insights for SIP trunk calls

The Calls API lets you retrieve call detail records (CDRs) and quality insights for calls made through your SIP trunks.

## API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Call/
```

***

## The Call Object

### Attributes

<ParamField body="call_uuid" type="string">
  Unique call identifier.
</ParamField>

<ParamField body="from_number" type="string">
  Caller ID.
</ParamField>

<ParamField body="to_number" type="string">
  Destination number.
</ParamField>

<ParamField body="call_direction" type="string">
  Direction. Values: `inbound`, `outbound`.
</ParamField>

<ParamField body="call_duration" type="integer">
  Actual call duration in seconds.
</ParamField>

<ParamField body="bill_duration" type="integer">
  Billed duration in seconds.
</ParamField>

<ParamField body="billed_duration" type="integer">
  Billed duration (may differ based on billing interval).
</ParamField>

<ParamField body="initiation_time" type="string">
  When call was initiated (UTC).
</ParamField>

<ParamField body="answer_time" type="string">
  When call was answered (UTC).
</ParamField>

<ParamField body="end_time" type="string">
  When call ended (UTC).
</ParamField>

<ParamField body="hangup_cause_name" type="string">
  Reason for hangup.
</ParamField>

<ParamField body="hangup_cause_code" type="integer">
  Numeric hangup cause code.
</ParamField>

<ParamField body="hangup_source" type="string">
  Who ended the call. Values: `customer`, `carrier`, `zentrunk`.
</ParamField>

<ParamField body="total_rate" type="string">
  Per-minute rate (USD).
</ParamField>

<ParamField body="total_amount" type="string">
  Total cost (USD).
</ParamField>

<ParamField body="trunk_domain" type="string">
  Trunk domain used.
</ParamField>

<ParamField body="from_country" type="string">
  Caller's country (ISO2).
</ParamField>

<ParamField body="to_country" type="string">
  Destination country (ISO2).
</ParamField>

<ParamField body="transport_protocol" type="string">
  Protocol used (e.g., `udp`, `tcp`).
</ParamField>

<ParamField body="srtp" type="boolean">
  Whether SRTP encryption was used.
</ParamField>

<ParamField body="secure_trunking" type="boolean">
  Whether secure trunking was enabled.
</ParamField>

<ParamField body="secure_trunking_rate" type="string">
  Secure trunking per-minute rate.
</ParamField>

<ParamField body="stir_verification" type="string">
  STIR/SHAKEN status.
</ParamField>

<ParamField body="attestation_indicator" type="string">
  Attestation level. Values: `A`, `B`, `C`.
</ParamField>

### Example Response

```json  theme={null}
{
  "call_uuid": "90b6eb07-796c-4d86-a4fd-44ed11667ddb",
  "from_number": "+12025551234",
  "to_number": "+13128574907",
  "call_direction": "outbound",
  "call_duration": 180,
  "bill_duration": 180,
  "billed_duration": 180,
  "end_time": "2024-01-15 14:32:00",
  "hangup_cause_name": "normal_hangup",
  "hangup_source": "carrier",
  "total_rate": "0.00500",
  "total_amount": "0.01500",
  "initiation_time": "2024-01-15 14:28:48",
  "answer_time": "2024-01-15 14:29:00",
  "trunk_domain": "93667062664669661.zt.plivo.com",
  "from_country": "US",
  "to_country": "US",
  "transport_protocol": "udp",
  "srtp": false,
  "hangup_cause_code": 3000,
  "secure_trunking": false,
  "secure_trunking_rate": "0.00000",
  "stir_verification": "Verified",
  "attestation_indicator": "A"
}
```

***

## Retrieve a Call

Get the call detail record (CDR) for a specific call.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Call/{call_uuid}/
```

```bash cURL theme={null}
curl -i --user AUTH_ID:AUTH_TOKEN \
    https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Call/90b6eb07-796c-4d86-a4fd-44ed11667ddb/
```

### Response

Returns the Call object for the specified call UUID.

***

## List All Calls

Retrieve CDRs for all calls with optional filtering.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Call/
```

### Query Parameters

<ParamField query="from_number" type="string">
  Filter by caller ID (exact or prefix).
</ParamField>

<ParamField query="to_number" type="string">
  Filter by destination (exact or prefix).
</ParamField>

<ParamField query="call_direction" type="string">
  Filter by direction. Values: `inbound`, `outbound`.
</ParamField>

<ParamField query="hangup_cause_code" type="integer">
  Filter by hangup cause code.
</ParamField>

<ParamField query="hangup_source" type="string">
  Filter by hangup source. Values: `customer`, `carrier`, `zentrunk`.
</ParamField>

<ParamField query="stir_verification" type="string">
  Filter by STIR status. Values: `Verified`, `Not Verified`, `Not Applicable`.
</ParamField>

<ParamField query="bill_duration" type="integer">
  Filter by duration in seconds. Supports variants: `bill_duration__gt`, `bill_duration__gte`, `bill_duration__lt`, `bill_duration__lte`.
</ParamField>

<ParamField query="end_time" type="string">
  Filter by call end time. Format: `YYYY-MM-DD HH:MM[:ss]` (UTC). Supports variants: `end_time__gt`, `end_time__gte`, `end_time__lt`, `end_time__lte`.
</ParamField>

<ParamField query="limit" type="integer">
  Results per page. Max: 20. Default: 20.
</ParamField>

<ParamField query="offset" type="integer">
  Pagination offset. Default: 0.
</ParamField>

<Note>
  You can retrieve only calls from the last 90 days. Without an `end_time` filter, the API searches the last 30 days.
</Note>

### Example Request

```bash cURL theme={null}
curl -i --user AUTH_ID:AUTH_TOKEN \
    "https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Call/?call_direction=outbound&end_time__gte=2024-01-01%2000:00&limit=20"
```

### Response

```json  theme={null}
{
  "api_id": "a04ad809-3b78-4bbe-9baf-acfc7800b10f",
  "meta": {
    "limit": 20,
    "offset": 0,
    "total_count": 2,
    "previous": null,
    "next": null
  },
  "objects": [
    {
      "call_uuid": "90b6eb07-796c-4d86-a4fd-44ed11667ddb",
      "from_number": "+12025551111",
      "to_number": "+13128574907",
      "call_direction": "outbound",
      "call_duration": 180,
      "bill_duration": 180,
      "stir_verification": "Verified",
      "attestation_indicator": "A"
    }
  ]
}
```

***

## Retrieve Call Insights

Get quality metrics for a specific call.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Call/{call_uuid}/Insights/
```

```bash cURL theme={null}
curl -i --user AUTH_ID:AUTH_TOKEN \
    https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Call/c9d6be3d-94c3-4b38-a2eb-8063ca404d77/Insights/
```

### Response

```json  theme={null}
{
  "api_id": "a63df7e3-9f24-4aae-2152-dc8f92548290",
  "call_uuid": "c9d6be3d-94c3-4b38-a2eb-8063ca404d77",
  "from": {
    "carrier": "Verizon Wireless",
    "number": "+12025551234",
    "region": "US"
  },
  "to": {
    "carrier": "AT&T",
    "number": "+13128574907",
    "region": "US"
  },
  "hangup_cause": "normal_hangup",
  "hangup_source": "customer",
  "rtt": "24",
  "jitter": "3",
  "packet_loss": "0",
  "post_dial_delay": 1000.0,
  "plivo_quality_score": "4.2"
}
```

### Insights Metrics

<ParamField body="rtt" type="string">
  Round-trip time in milliseconds. High values indicate network latency.
</ParamField>

<ParamField body="jitter" type="string">
  Variance in packet delay (ms). Causes robotic-sounding audio.
</ParamField>

<ParamField body="packet_loss" type="string">
  Percentage of lost packets. Causes broken audio.
</ParamField>

<ParamField body="post_dial_delay" type="float">
  Time from call initiation to ringing (ms).
</ParamField>

<ParamField body="plivo_quality_score" type="string">
  Quality rating from 1-5. Higher is better.
</ParamField>

### Quality Score Guidelines

| Score       | Quality   |
| ----------- | --------- |
| `4.0 - 5.0` | Excellent |
| `3.0 - 4.0` | Good      |
| `2.0 - 3.0` | Fair      |
| `1.0 - 2.0` | Poor      |

***

## STIR/SHAKEN Verification

The `stir_verification` field indicates call authenticity:

| Value            | Description                              |
| ---------------- | ---------------------------------------- |
| `Verified`       | Caller verified with attestation level A |
| `Not Verified`   | Attestation level B or C                 |
| `Not Applicable` | Non-US calls or cloud calls (WebRTC/SIP) |

***

## Hangup Sources

| Source     | Description                                  |
| ---------- | -------------------------------------------- |
| `customer` | Your infrastructure ended the call           |
| `carrier`  | The terminating carrier ended the call       |
| `zentrunk` | Plivo's SIP trunking platform ended the call |

***

## Related

* [Trunks](/sip-trunking/api/trunks/) - Manage SIP trunks
* [Hangup Codes](/sip-trunking/troubleshooting/zentrunk-hangup-codes) - Complete hangup cause reference
