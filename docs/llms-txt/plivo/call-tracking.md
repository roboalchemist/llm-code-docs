# Source: https://plivo.com/docs/voice/use-cases/call-tracking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Tracking

> Track and analyze inbound calls to measure marketing campaign performance

Call tracking lets marketers measure the performance of marketing campaigns both online (such as with Google Ads) and offline (using newspaper, billboards, etc.) via analytics of inbound calls. With call tracking, you can see how many times a phone number has been called, the duration of each call, the number and location of the caller, and more. These analytics helps companies track conversion rates across all marketing channels to optimize marketing ROI and identify unique behaviors of highly qualified leads.

## Basic call tracking

Plivo lets you retrieve call analytics on all live and completed calls to and from Plivo phone numbers. We provide examples and [server SDKs](/sdk/server/) so that you can add the functionality in any web standard languages you need.

To get all call details, set your URI to:

```sh  theme={null}
    URI: https://api.plivo.com/v1/Account/{auth_id}/Call/
    Method: GET
```

Plivo will return values for these parameters:

```json  theme={null}
[{
    "call_duration": 3,
    "total_amount": "0.02000",
    "parent_call_uuid": null,
    "call_direction": "outbound",
    "to_number": "<destination_number>",
    "total_rate": "0.02000",
    "from_number": "<caller_id>",
    "end_time": "2022-08-20T10:53:17",
    "call_uuid": "xxx-1111-xxxx-",
    "resource_uri": "/v1/Account/XXXXXXXXXXXXXXXX/Call/XXXX1/"
},
{
    "call_duration": 3,
    "total_amount": "0.02000",
    "parent_call_uuid": null,
    "call_direction": "inbound",
    "to_number": "xxxxxxxxx",
    "total_rate": "0.02000",
    "from_number": "xxxxxxxxx",
    "end_time": "2022-08-20T10:59:16",
    "call_uuid": "xxx-2222-xxxx-",
    "resource_uri": "/v1/Account/XXXXXXXXXXXXXXXX/Call/XXXX2/"
}]
```
