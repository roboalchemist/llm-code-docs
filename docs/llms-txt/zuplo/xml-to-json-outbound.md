# Source: https://www.zuplo.com/docs/policies/xml-to-json-outbound.md

# XML to JSON Outbound Policy

This policy is useful for converting legacy XML or SOAP APIs into modern REST
APIs. It can be useful to add a custom outbound policy that runs after this
policy to further transform the raw converted content into something more user
friendly.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-xml-to-json-outbound-policy",
  "policyType": "xml-to-json-outbound",
  "handler": {
    "export": "XmlToJsonOutboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "attributeNamePrefix": "@_",
      "ignoreAttributes": true,
      "ignoreDeclarations": true,
      "ignoreProcessingInstructions": true,
      "parseOnStatusCodes": "200-299",
      "removeNSPrefix": true,
      "stopNodes": ["root.a", "*.accounts"],
      "textNodeName": "#text",
      "trimValues": true
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `xml-to-json-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `XmlToJsonOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `removeNSPrefix` <code className="text-green-600">&lt;boolean&gt;</code> - Remove namespace string from tag and attribute names. Defaults to `true`.
- `ignoreProcessingInstructions` <code className="text-green-600">&lt;boolean&gt;</code> - Ignore processing instruction tags. i.e. `<?elementnames <fred>, <bert>, <harry> ?>`. Defaults to `true`.
- `ignoreDeclarations` <code className="text-green-600">&lt;boolean&gt;</code> - Ignore declarations. i.e. `<?xml version="1.0"?>`. Defaults to `true`.
- `ignoreAttributes` <code className="text-green-600">&lt;boolean&gt;</code> - Ignore tag attributes. Defaults to `true`.
- `stopNodes` <code className="text-green-600">&lt;string[]&gt;</code> - At particular point, if you don't want to parse a tag and it's nested tags then you can set their path in stopNodes. You can also set tags which should not be processed irrespective of their path using \* as the wildcard.
- `attributeNamePrefix` <code className="text-green-600">&lt;string&gt;</code> - The prefix of attribute names in the resulting JS object. Defaults to `"@_"`.
- `textNodeName` <code className="text-green-600">&lt;string&gt;</code> - Text value of a tag is parsed to \#text property by default. Defaults to `"#text"`.
- `trimValues` <code className="text-green-600">&lt;boolean&gt;</code> - Remove surrounding whitespace from tag or attribute value. Defaults to `true`.
- `parseOnStatusCodes` <code className="text-green-600">&lt;undefined&gt;</code> - A list of status codes and ranges "200-299, 304" that should the XML parser should run on. If not set, the parser will run on all status codes.

## Using the Policy

This policy can help expose legacy XML or SOAP APIs using modern JSON REST APIs.
The policy is configurable in ways that make it easier to strip parts of the XML
document that you are unlikely to use, such as processing instructions,
namespaces, or directives. The default options for this policy will generally
give you a fairly clean output. However, it is likely that the output of the raw
conversion is still not in the best format.

The best way to clean up the output of your XML is first, run this policy, then
add a [custom code outbound policy](/docs/policies/custom-code-outbound) that
further reshapes the JSON data structure. An example policy that cleans up a
SOAP response is shown below.

```xml title="SOAP Response"
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <m:ListOfCurrenciesByNameResponse xmlns:m="http://www.oorsprong.org/websamples.countryinfo">
      <m:ListOfCurrenciesByNameResult>
        <m:tCurrency>
          <m:sISOCode>USD</m:sISOCode>
          <m:sName>Dollar</m:sName>
        </m:tCurrency>
        <m:tCurrency>
          <m:sISOCode>EUR</m:sISOCode>
          <m:sName>Euro</m:sName>
        </m:tCurrency>
      </m:ListOfCurrenciesByNameResult>
    </m:ListOfCurrenciesByNameResponse>
  </soap:Body>
</soap:Envelope>
```

The code in the policy below takes the output (`response.json()`) of the XML to
JSON Outbound policy and reshapes it to a simple JSON structure.

```ts title="modules/clean-soap.ts"
import { ZuploContext, ZuploRequest } from "@zuplo/runtime";

export default async function cleanSoapBody(
  response: Response,
  request: ZuploRequest,
  context: ZuploContext,
) {
  const soap = await response.json();
  const data: { isoCode: string; name: string }[] =
    soap.Envelope.Body.ListOfCurrenciesByNameResponse.ListOfCurrenciesByNameResult.tCurrency.map(
      (c) => ({
        isoCode: c.sISOCode,
        name: c.sName,
      }),
    );

  return new Response(JSON.stringify({ total: data.length, data }), {
    headers: response.headers,
    status: response.status,
    statusText: response.statusText,
  });
}
``;
```

The JSON response of your API would then be a easily consumable JSON object.

```json title="JSON Response"
{
  "total": 2,
  "data": [
    { "isoCode": "USD", "name": "Dollar" },
    { "isoCode": "EUR", "name": "Euro" }
  ]
}
```

Read more about [how policies work](/articles/policies)
