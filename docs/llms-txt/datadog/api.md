# Source: https://docs.datadoghq.com/cloudcraft/api.md

---
title: Cloudcraft API Reference
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Cloudcraft API Reference
source_url: https://docs.datadoghq.com/api/index.html
---

# Cloudcraft API Reference
.openapi-spec-content img{max-width:100%}.openapi-spec-content h1 a:hover,.openapi-spec-content h2 a:hover{color:#000;border-bottom:1px solid #000}


The Cloudcraft API provides programmatic access and remote rendering of your architecture diagrams. The API also provides fully automated visualization of AWS and Azure accounts that are linked to your Cloudcraft account, either as ready to use images or as JSON data.

Use case examples:

- Snapshot and visually compare your live AWS environment state before and after a deployment from the command line or as part of your automated CI pipeline.
- Download an inventory of all your AWS resources from a linked account as JSON.
- Write a converter from a third-party data format to Cloudcraft diagrams.
- Backup, export, and import your Cloudcraft data.

Access to the Cloudcraft API requires a [Cloudcraft](https://www.cloudcraft.co/) user account.

## Authentication{% #authentication %}

To authenticate your Cloudcraft account for the API, you must include your secret key in the requests. You can create API keys in the **Manage API keys** > **Create API Key** section of the [Cloudcraft application](https://app.cloudcraft.co/).

The API key provides access to your diagrams and linked AWS accounts in either read or read-write mode. Do not share your secret API keys in publicly accessible areas such as GitHub or client-side code.

Authentication to the API is performed via the *Bearer Authorization* header over HTTPS. For example, using cURL an authorized request looks like this:

```shell
curl -X GET \
  -H 'Authorization: Bearer bear3vFUUkgfzoBK+UKyPmZw1NsdfrFzdvZoyFJwe8=' \
  https://api.cloudcraft.co/user/me
```

## Endpoints{% #endpoints %}

The Cloudcraft API endpoint is [https://api.cloudcraft.co](https://api.cloudcraft.co). For access to the Cloudcraft US GovCloud API, contact [Cloudcraft Support](https://app.cloudcraft.co/support).

All API requests must be made over HTTPS. Calls made over plain HTTP will fail.

## Request rate limiting{% #request-rate-limiting %}

Cloudcraft throttles the number of API request that can be made per API key. This is to help the performance of the service, and to ensure fair usage for all Cloudcraft customers. The current API limits are 20 requests / 10 seconds (120 req / minute).

When the request submissions exceeds the rate limit, clients receive a `429 Too Many Requests` error response with a `Retry-After` header that indicates how long (in seconds) the user agent should wait before making a follow-up request. Clients should catch this exception, and retry based on the hint from `Retry-After` header until successful.

## Access control lists{% #access-control-lists %}

Blueprints and AWS Accounts support the following access control properties:

```json
{
 ...
 readAccess: [],
 writeAccess: []
}
```

Where an ACL is a string of the form:

- `team/TEAM_ID`
- `customer/CUSTOMER_ID`

For example, to share a blueprint with two teams:

```json
 "readAccess": ["team/512184ee-e683-45c1-948a-f588b8c833ca", "team/aab74437-ff4c-4a6d-b366-1311821905b1"]
```

To unshare a blueprint, set the list to `[]`;

**Note**: The APIs validate both read and write access separately. In the UI, only the `readAccess` is reflected.



## SDKs{% #sdks %}

By default, the Cloudcraft API docs show examples in cURL. Each endpoint also includes code examples from one of the official SDKs. To install each SDK:

{% tab title="Go" %}
#### Installation{% #installation %}

```sh
go mod init main && go get github.com/DataDog/cloudcraft-go
```

#### Usage{% #usage %}

```go
import (
        "github.com/DataDog/cloudcraft-go"
)
```

{% /tab %}

{% tab title="Python" %}
#### Installation{% #installation %}

```console
pip3 install cloudcraftco
```

#### Usage{% #usage %}

```python
from cloudcraftco import Cloudcraft
```

{% /tab %}

{% tab title="Node.js" %}
#### Installation{% #installation %}

```sh
npm install cloudcraft
```

#### Usage{% #usage %}

```javascript
import { Cloudcraft } from 'cloudcraft';
```

{% /tab %}

Or check out the SDKs directly:

- [go](https://github.com/DataDog/cloudcraft-go)
- [Python](https://github.com/DataDog/cloudcraft-python)
- [go](https://github.com/DataDog/cloudcraft-node)
