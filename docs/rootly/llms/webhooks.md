# Source: https://docs.rootly.com/configuration/webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Configure webhooks to receive real-time event notifications from Rootly for incidents, alerts, and other system events in external applications.

## Payload[](#ZdBIW)

Each event payload is a JSON object with properties event and data objects. The event object holds the event, and the data property holds a representation of the resource at the time the event was issued.

## Supported Events[](#Kdzlw)

[Event Payloads](/configuration/event-payloads)

```
incident.created
incident.updated
incident.mitigated
incident.resolved
incident.cancelled
incident.deleted

incident.scheduled.created
incident.scheduled.updated
incident.scheduled.in_progress
incident.scheduled.completed
incident.scheduled.deleted

incident_post_mortem.created
incident_post_mortem.updated
incident_post_mortem.published
incident_post_mortem.deleted

alert.created
pulse.created
```

## Verifying Webhooks[](#QlKAI)

Each webhook HTTP request includes a `X-Rootly-Signature` header, used to verify the request came from Rootly. The signature header contains a timestamp prefixed with t= and a signature prefixed with v= .

```txt Text theme={null}
X-Rootly-Signature:
t=1492774588,
v1=6657a869e8ecebeda32affa62cdca3fa51cad7e77a0e56ff536d0ce8e108d8bd
```

To verify the request, concatenate the timestamp with the request body and generate a SHA256 HMAC digest using the webhook secret available in the webhook configuration. The HMAC digest should match the provided signature.

```ruby Ruby theme={null}
require 'openssl'

# Assuming 'request' is an object representing the incoming HTTP request
header = request.headers['X-Rootly-Signature']
parts = header.split(',')
timestamp = parts[0].split('t=').last
signature = parts[1].split('v1=').last
secret = 'webhook secret'

# Reading the request body
request_body = request.body

# Create a signature using HMAC SHA256
expected_signature = OpenSSL::HMAC.hexdigest('SHA256', secret, timestamp + request_body)

# Compare the computed signature with the received signature
is_valid = expected_signature == signature
```

```py Python theme={null}
import hmac
import hashlib

header = request.headers['X-Rootly-Signature']
parts = header.split(',')
timestamp = parts[0].split('t=')[1]
signature = parts[1].split('v1=')[1]
secret = "webhook secret"

# Reading the request body
request_body = request.data  # or request.body depending on the framework

# Create a signature using HMAC SHA256
expected_signature = hmac.new(
    key=secret.encode(), 
    msg=(timestamp + request_body).encode(), 
    digestmod=hashlib.sha256
).hexdigest()

# Compare the computed signature with the received signature
is_valid = expected_signature == signature
```

```js JS theme={null}
const crypto = require('crypto');

// Assuming 'request' is an object representing the incoming request
const header = request.headers['x-rootly-signature'];
const parts = header.split(',');
const timestamp = parts[0].split('t=')[1];
const signature = parts[1].split('v1=')[1];
const secret = "webhook secret";

// Reading the request body
// Ensure that the request body is raw or a string
const request_body = request.body; 

// Create a HMAC SHA256 signature
const expectedSignature = crypto.createHmac('sha256', secret)
                                 .update(timestamp + request_body)
                                 .digest('hex');

// Compare the computed signature with the received signature
const isValid = expectedSignature === signature;
```


Built with [Mintlify](https://mintlify.com).