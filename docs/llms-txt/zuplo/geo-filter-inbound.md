# Source: https://www.zuplo.com/docs/policies/geo-filter-inbound.md

# Geo-location filtering Policy

Block requests based on geo-location parameters: country, region code, and ASN

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-geo-filter-inbound-policy",
  "policyType": "geo-filter-inbound",
  "handler": {
    "export": "GeoFilterInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "allow": {
        "asns": "395747, 28304",
        "countries": "US, CA",
        "regionCodes": "TX, WA"
      },
      "block": {
        "asns": "395747, 28304",
        "countries": "US, CA",
        "regionCodes": "TX, WA"
      },
      "ignoreUnknown": true
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `geo-filter-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `GeoFilterInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `block` <code className="text-green-600">&lt;object&gt;</code> - No description available.
  - `countries` <code className="text-green-600">&lt;string&gt;</code> - comma separated string of country codes to allow (e.g. "US, CA").
  - `regionCodes` <code className="text-green-600">&lt;string&gt;</code> - comma separated string of region codes to allow (e.g. "TX, WA").
  - `asns` <code className="text-green-600">&lt;string&gt;</code> - comma separated string of ASNs to allow (e.g. "395747, 28304").
- `allow` <code className="text-green-600">&lt;object&gt;</code> - No description available.
  - `countries` <code className="text-green-600">&lt;string&gt;</code> - comma separated string of country codes to allow (e.g. "US, CA").
  - `regionCodes` <code className="text-green-600">&lt;string&gt;</code> - comma separated string of region codes to allow (e.g. "TX, WA").
  - `asns` <code className="text-green-600">&lt;string&gt;</code> - comma separated string of ASNs to allow (e.g. "395747, 28304").
- `ignoreUnknown` <code className="text-green-600">&lt;boolean&gt;</code> - Specifies whether unknown geo-location parameters should be ignored (allowed through). Defaults to `true`.

## Using the Policy

## Geo-location Filter Policy

Specify an allow list or block list of:

- **Countries** - Country of the incoming request. The
  [two-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) in
  the request, for example, "US".
- **regionCodes** - If known, the
  [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) code for the
  first-level region associated with the IP address of the incoming request, for
  example, "TX"
- **ASNs** - ASN of the incoming request, for example, 395747.

:::warning

If you specify an allow and block list for the same location type (e.g.
`country`) may have no effect or block all requests.

```
{
  "allow" : {
    "countries" : "US"
  },
  "block" : {
    "countries" : "MC"
  }
}
```

The policy will only allow requests from US, so any request from MC would be
automatically blocked.

:::

Read more about [how policies work](/articles/policies)
