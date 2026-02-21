# Source: https://docs.wiremock.io/response-templating/xml.md

# Source: https://docs.wiremock.io/request-matching/xml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Request Matching - Matching XML bodies

> Matching XML

When stubbing API functions that accept XML request bodies we may want to
return different responses based on the XML sent. WireMock Cloud provides two match types
to supports this case - `equalToXml` and `matchesXPath`, which are described
in detail in this article.

## Matching via XML equality - `equalToXml`

The `equalToXml` match operator performs a semantic comparison of the input XML
against the expected XML. This has a number of advantages over a straight string
comparison:

* Ignores differences in whitespace
* Ignores element and attribute order
* Supports placeholders so that specific elements or attributes can be excluded from the comparison

By default `equalToXml` will match the input to the expected XML if all elements
and attributes are present, have the same value and there are no additional
elements or attributes.

For instance, given the following configuration:

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=174657a8a9a6aeb833c28a263ed6225b" title="Default equal to XML" data-og-width="793" width="793" data-og-height="224" height="224" data-path="images/screenshots/equal-to-xml.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=0da73420b88e215105e71ec1983e441d 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=a80de5695e255776f0ce77993c7673b3 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=69c30373f984e1f63ca29ab6ff4372f3 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=df636bc18d3e6dae2182f5f8b0f73c90 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=09eda2efaddd5b1a20b6403760ce289a 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=20520fba71b64f9a2ca35092aaa29d63 2500w" />

The following XML would match:

```xml  theme={null}
<things>
  <two id="234" val="2"/>
  <one val="1" id="123" />

</things>
```

### Using placeholders to ignore specific elements or attributes

As with JSON equality matching, placeholders can be used with XML to ignore specific
elements or attributes.

Given the following configuration:

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml-with-placeholders.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=9379522e48a2d31bb646a0676d053cf2" title="Equal to XML with placeholders" data-og-width="793" width="793" data-og-height="236" height="236" data-path="images/screenshots/equal-to-xml-with-placeholders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml-with-placeholders.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=ba1b7b4eb3c6f66e7ec5f23d2168f212 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml-with-placeholders.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=ea99a47ef35b3e671cff679fc73a73aa 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml-with-placeholders.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=4daa4d53f7d693d4e07be035f1c038e2 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml-with-placeholders.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=e2977b14565782a9196baabf0b436a41 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml-with-placeholders.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=7718ab5e549e6e7176fd5dd48a406426 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/equal-to-xml-with-placeholders.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=781d548c6f1126fd19f83e7b72ee58cb 2500w" />

The following XML will match:

```xml  theme={null}
<things>
  <one id="123" val="123456789"/>
  <two id="234" val="2"/>
  <three>999999</three>
</things>
```

## Matching via XPath - `matchesXPath`

WireMock Cloud supports matching incoming XML using XPath 1.0 expressions. The most common
use case for this is when accepting XML request bodies, although it can be used
with other request fields such as headers.

The input XML is deemed a match if any elements are returned when the XPath
expression is evaluated against it.

Given a body match on the XPath expression `/things/thing[@name = 'socks']`.

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-body-match.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=42fc2c25521b88938b6157ac96b97037" title="Matching on XPath" data-og-width="795" width="795" data-og-height="159" height="159" data-path="images/screenshots/xpath-body-match.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-body-match.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=5ffaf0d8a73eee7e333ca9ffc7a8f1d5 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-body-match.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a7ec9eea79eb64926a51330fab452879 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-body-match.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=23df8884aa7b9a75cdedb01548a58f6f 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-body-match.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=781c4a8da5c61334bc3c9d1c6a6c2c85 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-body-match.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=52fbeacd1a6b8436b00a853b57144e8d 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/xpath-body-match.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=cd1df0eddfd7f49af9706b1096647bbb 2500w" />

The following XML will match:

```xml  theme={null}
<things>
  <thing name="socks"></thing>
  <thing name="shoes"></thing>
</things>
```
