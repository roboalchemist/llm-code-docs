# Source: https://docs.wiremock.io/advanced-stubbing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced Stubbing

> Advanced request matching, using query, header and body matching with regexes, JSONPath, XPath and others.

In some cases matching on the URL alone is not specific enough. For instance you may want to simulate creation of a new
to-do item in a RESTful API by stubbing `POST` to `/api/to-do`. In order to test both success and failure cases it will be
necessary to return different responses depending on the post body (since the URL would always be the same).

We can do this by adding a body matching clause in the Advanced portion of the Request section.

Click the button to add the clause, select the match type from the drop-down, then write (or paste) the expected value or expression into the text area.

If your API uses JSON as its serialisation format you might want to match using `equalToJson`:

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/advanced-section-body-match.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=dda22182765824b4638c9d854e29e638" title="Advanced" data-og-width="902" width="902" data-og-height="422" height="422" data-path="images/screenshots/advanced-section-body-match.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/advanced-section-body-match.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=b308b801fab371fd89e34c8de628b2bb 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/advanced-section-body-match.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=303178b13335b146e0eee1c1d81402c5 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/advanced-section-body-match.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=bb8f4bf0bda6c57f2f1681f70bd3994b 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/advanced-section-body-match.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=499451e7d6cc14432844de5197f3a102 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/advanced-section-body-match.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=d30edc3e8241c00c2c8da13b52f3874f 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/advanced-section-body-match.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=d7563bb1d19b7f1624ad1fe8e33bf908 2500w" />

For quick reference, here are the options available to you:

* ***Equals*** - matches if the request body is equal to the expected body
* ***Matches Regex*** - matches if the request body matches the specified regex
* ***Does Not Match Regex*** - matches if the request body does not match the specified regex
* ***Contains*** - matches if the request body contains the expected body
* ***Equals XML*** - matches if the request body is equal to the expected XML
* ***Matches XPath*** - matches if the request body matches the specified XPath
* ***Equals JSON*** - matches if the request body is equal to the expected JSON
* ***Matches JSONPath*** - matches if the request body matches the specified JSONPath
* ***Matches JSON Schema*** - matches if the request body matches the specified JSON schema
* ***Is Absent*** - matches if the request body is absent

**Note** that the `NOT` checkbox can be used to negate the selected matcher.

## Request method matching

The HTTP method that required for this stub to match. This defaults to `ANY`, meaning that a request with any method
will match.

## Request priority matching

Requests of a higher priority (i.e. lower number) will be matched first, in cases where more than one stub mapping in the
list would match a given request.

Normally it's fine to leave the priority at its default. However it can sometimes be useful to so create a low priority,
broadly matching stub defining some default behaviour e.g. a 404 page, and then create a set of higher priority, more specific
stubs for testing individual cases. See [Serving Default Responses](/default-responses/) for more details.

## URL matching

Determines how the URL will be matched. The options are:

* **Path and query** - exactly matches the path and query string parts of the URL
* **Path and query regex** - matches the path and query string parts of the URL against a regular expression
* **Path** - exactly matches the path part of the URL
* **Path regex** - matches the path part of the URL against a regular expression
* **Any URL** - matches any URL

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3f01540a07c388d14f17e376447dcd5e" title="URL match types" height="150px" data-og-width="249" data-og-height="147" data-path="images/screenshots/url-match-type-screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=89e466a60aa80428857768c9827caf63 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=f998d86c8fb156867f0b9a202b03efa8 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=938e157cda59c07b7975f33d62e3b264 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=8057601bde8592a5ba2d4b606df63530 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=658334eec9489ed982fa55f1564efa77 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=72f7cc8747ddd54f96813a5e12b565b3 2500w" />

## Advanced - Query parameters, headers and more

In addition to the URL and body, requests can be matched on:

* Headers
* Query parameters
* Cookies

Parameter match clauses can use the same set of match operations as body clauses:

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/request-parameters-screenshot.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=7df0ca775c5b0fcaf5f38e22499771de" title="Request parameters" data-og-width="670" width="670" data-og-height="208" height="208" data-path="images/screenshots/request-parameters-screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/request-parameters-screenshot.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=8c96a22e075a62ebbddf436d7527402e 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/request-parameters-screenshot.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=9b5bd549da99fbcc1e18ad12ecf2f7a3 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/request-parameters-screenshot.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=ad693e37afedf89cdccf461caa0f4934 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/request-parameters-screenshot.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=a3c382164c18e90338891af66ca30c11 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/request-parameters-screenshot.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=58a2df868d886d67d5bade1c22297d87 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/request-parameters-screenshot.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=b2cc1a9c6645e9e46eec92244cf7f028 2500w" />

It's usually a good idea to use path only URL matching with query parameter matches.

When multiple match clauses are added a request must match all of them for the response to be served (they are combined
with logical AND).

### Logical AND OR matchers

You can build complex logic using AND OR operators for Headers, Query parameters, Cookies, Form parameters and Path parameters.

These operators can be nested to help build realistic matching logic into your stubs.

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/OR-predicate-example.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=fb39fa44135d770293e142e2e0facb4e" title="OR predicate" data-og-width="1000" width="1000" data-og-height="629" height="629" data-path="images/screenshots/OR-predicate-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/OR-predicate-example.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=c586cf46a525abb7707a1f2a93d50b0c 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/OR-predicate-example.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=7c14fa234806ae836d4c384ce3788455 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/OR-predicate-example.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=1d09fa35745af077fd2cfd05b744801f 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/OR-predicate-example.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=dd58640584b1a3d483df9b4fe651953e 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/OR-predicate-example.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=9cf8f0ad10cbe0748061bb1d224975ba 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/OR-predicate-example.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=540c82ce9c3ff41fff50f45a321608ba 2500w" />

## Matching JSON request bodies

Two specific match types exist for JSON formatted request bodies: equality (`equalToJson`) and JSONPath (`matchesJsonPath`).

### Equality

`equalToJson` performs a semantic comparison between the incoming JSON and the expected value, meaning that
it will return a match even when, for instance, the two documents have different amounts of whitespace.

You can also specify that array order an additional elements in the request JSON be ignored.

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/equal-to-json.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=85250ec0c90e7d45371ed17823e03853" title="JSON equality" data-og-width="424" width="424" data-og-height="240" height="240" data-path="images/screenshots/equal-to-json.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/equal-to-json.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=61d3ba2907ecd60cd9cb61b6bab608f5 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/equal-to-json.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=d67204229840465e089ab5190631caa2 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/equal-to-json.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=c49d0de9dc4bb6b174dc0b8b4510883c 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/equal-to-json.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=2fc93526ae421d2b72ccc9e273ae2002 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/equal-to-json.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=302b2a58a7584f81d08a60ed66926346 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/equal-to-json.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=59cdb0535ccf9ca111ff4671affd1873 2500w" />

### JSON Placeholders

JSON equality matching is implemented by [JsonUnit](https://github.com/lukas-krecan/JsonUnit), and
therefore supports placeholder syntax, allowing looser specification of fields within the document.

For instance, consider a request body like this, where `transaction_id` is unique to
each request:

```json  theme={null}
{
  "event": "details-updated",
  "transaction_id": "abc-123-def"
}
```

Requiring an exact match on this document would ensure no match could ever be made, since
the same transaction ID would never be repeated.

This can be solved using a placeholder:

```json  theme={null}
{
  "event": "details-updated",
  "transaction_id": "${json-unit.ignore}"
}
```

If you want to constrain the value to a specific type or pattern the following placeholders are also valid:

* `${json-unit.regex}[A-Z]+` (any Java-style regular expression can be used)
* `${json-unit.any-string}`
* `${json-unit.any-boolean}`
* `${json-unit.any-number}`

### JSONPath

`matchesJsonPath` allows request bodies to be matched according to a [JSONPath](https://github.com/json-path/JsonPath) expression. The
JSONPath expression is used to select one or more values from the request body, then the result is matched against sub-matcher (`equal to`, `contains` etc.).
It is also possible to simply assert that the expression returns something, by selecting `is present` from the list.

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/matches-json-path.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=fe7cc67b259fe8531212957a16b8522e" title="JSONPath matching" data-og-width="2080" width="2080" data-og-height="338" height="338" data-path="images/screenshots/matches-json-path.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/matches-json-path.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=007e05cd7b58d2a670055f0a8e2ea8f6 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/matches-json-path.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=6748b0b052be42f3993f5bb9228cd1d1 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/matches-json-path.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=999f7617491d02bb70101a6105590205 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/matches-json-path.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=70b2bb40f9afe9931e2cb1e0f0e66d79 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/matches-json-path.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=b895fb9f7b23d360b2c8caef7755afa4 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/matches-json-path.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=50574beff17cc500eb7b4971b2ca2c1f 2500w" />

The expression in the above screenshot (`$.event` `equal to` `description-updated`) would match a request body of

```json  theme={null}
{
  "event": "description-updated"
}
```

but not

```json  theme={null}
{
  "event": "document-created"
}
```

## Matching XML request bodies

As with JSON matching, there are two match types available for working with XML: `equalToXml` and `matchesXPath`.

### Equality

`equalToXml` performs a semantic comparison between the incoming and expected XML documents, meaning that it will return a match regardless of whitespace, comments and node order.

### XML placeholders

When using `equalToXml` it is possible to ignore the value of specific elements using [XMLUnit](https://github.com/xmlunit/user-guide/wiki/Placeholders)'s placeholder syntax. For instance if you
expected to receive an XML request body containing a transaction ID that changed on every request you could ignore that value like this:

```xml  theme={null}
<transaction>
  <id>${xmlunit.ignore}</id>
  <value>1234</value>
</transaction>
```

To use XML placeholders you must enable them by ticking the box:

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-xml-placeholders.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=81d334b57e6d806332b2c46b2d662102" title="Enable XML placeholders" width="300px" data-og-width="219" data-og-height="130" data-path="images/screenshots/enable-xml-placeholders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-xml-placeholders.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=2faacfac811ab3071630ba0125858b54 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-xml-placeholders.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=cc8c19fbaad60dd397c6be0c764c3663 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-xml-placeholders.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=be245874cb5501df503a8befb201b00e 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-xml-placeholders.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=fb7b4ec73451a3c147b7cb9524f369a1 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-xml-placeholders.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=69daa19ed840fef9846c24672b3f6cf0 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/enable-xml-placeholders.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=ee739a2a3a24117a0f31a403657f6368 2500w" />

### XPath

`matchesXPath` allows XML request bodies to be matched according to an [XPath](https://www.w3schools.com/xml/xpath_syntax.asp) expression.

For instance, an XML request body like

```xml  theme={null}
<stuff>
  <id>abc123</id>
</stuff>
```

could be matched using the XPath expression

```
//stuff[id='abc123']
```

## Setting the response status

The HTTP status code to be sent with the response.

## Sending response headers

Headers can be set on the response:

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/response-headers-screenshot.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=1f00b4c7d93f720459014e41a8a4c29b" title="Response headers" data-og-width="529" width="529" data-og-height="128" height="128" data-path="images/screenshots/response-headers-screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/response-headers-screenshot.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=71b17dc2fd79f3760a5f6724d9cd7e05 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/response-headers-screenshot.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=3dd17f8dc8b5072380a8d72920fdff11 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/response-headers-screenshot.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=ca852efaedbd7aa3266f13e2074a92be 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/response-headers-screenshot.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=21481b2aba2f91356cd8780270f36b0c 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/response-headers-screenshot.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=5726091d8447fa1bfa993581abde7f35 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/response-headers-screenshot.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=5d537d17d641ae07cc7da09be0a41731 2500w" />

## Response body

A response body can optionally be specified. If [response templating](/response-templating/)
is enabled, certain parts can be dynamically generated using request attributes and random data.
