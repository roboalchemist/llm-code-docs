# Source: https://docs.wiremock.io/response-templating/json.md

# Source: https://docs.wiremock.io/request-matching/json.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Request Matching - Matching JSON requests

> Matching JSON

When stubbing API functions that accept JSON request bodies we may want to
return different responses based on the JSON sent. WireMock Cloud provides two match types
to supports this case - `equalToJson` and `matchesJsonPath`, which are described
in detail in this article.

## Matching via JSON equality

The `equalToJson` match operator performs a semantic comparison of the input JSON
against the expected JSON. This has a number of advantages over a straight string
comparison:

* Ignores differences in whitespace
* Can be configured to ignore differences in array order
* Can be configured to ignore extra object attributes
* Supports placeholders so that specific attributes can be excluded from the comparison

By default `equalToJson` will match only if all of the elements in the input JSON
are the same as the expected JSON, arrays are in the same order and no additional
attributes are present.

For instance, given an expected JSON document like

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-equal-to-json.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=3a0c7b2f4df3c1bfd863cd6f6a717684" title="Default equal to JSON" data-og-width="799" width="799" data-og-height="365" height="365" data-path="images/screenshots/default-equal-to-json.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-equal-to-json.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=24a37811165fab88c5fd32ddb039cd7f 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-equal-to-json.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=d58469554b96bc5a017d463e34e198e7 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-equal-to-json.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=df9c99739b856766f7f1b2cc61a106db 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-equal-to-json.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=19d9dc77f9752b7987fd795e6a2dd0b0 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-equal-to-json.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=96ac4c0d7bd9bb99060401e83fbf2004 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/default-equal-to-json.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=301080bc0b2a00879775ec4551b998c3 2500w" />

You would need to send in the request body for the stub to match exactly that JSON
in order for the stub to be matched:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["S", "M", "L"]
}'

{ "result": "OK" }
```

Changing the `sizes` order would cause a non-match:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["L", "M", "S"]
}'

                                               Request was not matched
                                               =======================

-----------------------------------------------------------------------------------------------------------------------
| Closest stub                                             | Request                                                  |
-----------------------------------------------------------------------------------------------------------------------
                                                           |
JSON body matching                                         |
                                                           |
POST                                                       | POST
/json                                                      | /json
                                                           |
{                                                          | {                                                   <<<<< Body does not match
  "itemId" : 102938,                                       |   "itemId" : 102938,
  "sizes" : [ "S", "M", "L" ]                              |   "sizes" : [ "L", "M", "S" ]
}                                                          | }
                                                           |
-----------------------------------------------------------------------------------------------------------------------
```

Adding an extra attribute would also cause a non-match:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["S", "M", "L"],
  "tag": "essentials"
}'

                                               Request was not matched
                                               =======================

-----------------------------------------------------------------------------------------------------------------------
| Closest stub                                             | Request                                                  |
-----------------------------------------------------------------------------------------------------------------------
                                                           |
JSON body matching                                         |
                                                           |
POST                                                       | POST
/json                                                      | /json
                                                           |
{                                                          | {                                                   <<<<< Body does not match
  "itemId" : 102938,                                       |   "itemId" : 102938,
  "sizes" : [ "S", "M", "L" ]                              |   "sizes" : [ "S", "M", "L" ],
}                                                          |   "tag" : "essentials"
                                                           | }
                                                           |
-----------------------------------------------------------------------------------------------------------------------
```

### Ignoring array order

Sometimes the order of elements in an array is unimportant and can change arbitrarily
between multiple requests. In this case it's undesirable for your stub match to fail
due to array order, so to remedy this you can simply tick "Ignore array order".

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-array-order.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=d5c1e165bfd27813f84545dc25c7822a" title="Equal to JSON ignoring array order" data-og-width="812" width="812" data-og-height="183" height="183" data-path="images/screenshots/ignore-array-order.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-array-order.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=8e537345221f9f43388a71844c61b7a7 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-array-order.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=db1a347a729a54e0e25306b8a1e1f838 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-array-order.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=5db8f24a9cc6123bcaa40897e1264a2d 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-array-order.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=eec55e77f199c2f29e21cef2bd0c82ee 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-array-order.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=cacd495d5dcadc52acf5729067938434 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-array-order.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=178b4d1f0f0fad21c2cdb0f39f5c12ad 2500w" />

This will allow requests like the following to succeed:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["S", "L", "M"]
}'                   

{ "result": "OK" }
```

### Ignoring extra elements

If you're only interested in matching a specific set of JSON elements and don't mind
if additional elements are present you can tick "Ignore extra elements".

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-extra-elements.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=a0a8f2bffc3bd9ca0d7a4d7fa172fc37" title="Equal to JSON ignoring extra elements" data-og-width="806" width="806" data-og-height="184" height="184" data-path="images/screenshots/ignore-extra-elements.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-extra-elements.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=61fd1ddeb84cf8a977b278b6b2afe197 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-extra-elements.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=ec345c1f9318484c6f3e010680f5ad6e 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-extra-elements.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=51a3b0eb36f4a71fe398c493dfeeb5df 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-extra-elements.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=1c135cebbd653955b698ed8f4d73af16 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-extra-elements.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=4759f10c79e99aafd7ee2c5156c4ed19 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/ignore-extra-elements.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=c0c28c4550c1d781c5978c535c381c7a 2500w" />

This would permit the following to match:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["S", "M", "L"],
  "tag": "essentials"
}'
```

### Using placeholders to ignore specific JSON attributes

If you want to check that an element is present, but don't care what the value is
then you can use JSONUnit placeholder syntax to achieve this.

Note: unlike with XML placeholders this is enabled by default.

For instance, given the following configuration:

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/json-placeholders.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=fed4c3a1385939935e36dc6534b7aee1" title="Equal to JSON with placeholder" data-og-width="803" width="803" data-og-height="183" height="183" data-path="images/screenshots/json-placeholders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/json-placeholders.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=075fd7476460944f81250d318e442ab6 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/json-placeholders.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=0bf299ba7bd4d0a5987d9ff3a1e3aee5 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/json-placeholders.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=1ecc6ad5d1f20d3bc25c8170e3b11088 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/json-placeholders.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=cde1dd0bade5a436fa5072cd5bbe9282 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/json-placeholders.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=1f540c1184cd4d9550f16be5d99a9543 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/json-placeholders.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=9f77ef9e0fccc6d039130045793148da 2500w" />

This would permit the the following to match:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 8888888888,
  "sizes": ["S", "M", "L"],
  "tag": "essentials"
}'
```

When using `${json-unit.ignore}`, the element's type is also ignored (in addition to its value),
so in the above case a string, boolean etc. could have been used in place of the numeric ID.

If you want to constrain an element to a specific type but still ignore the value
you can use one of the following placeholders:

* `${json-unit.regex}[A-Z]+` (any Java-style regular expression can be used)
* `${json-unit.any-string}`
* `${json-unit.any-boolean}`
* `${json-unit.any-number}`

## Matching via JSONPath - `matchesJsonPath`

[JSONPath](https://github.com/json-path/JsonPath) is an expression language,
similar in concept to XPath that permits elements or collections of elements
to be queried from a JSON document.

WireMock Cloud supports stub matching using JSONPath expressions, optionally sub-matching
the result using WireMock Cloud's own operators (`equalTo`, `matches` etc.).

Given the following configration:

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-with-submatch.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=b038c116f52301ef8f4f9fed8f6905b5" title="JSONPath with equal to" data-og-width="795" width="795" data-og-height="150" height="150" data-path="images/screenshots/jsonpath-with-submatch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-with-submatch.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=3ec07fd0ed2107bd80311674e17cb567 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-with-submatch.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=4389d284e62e1af706f55de7e7ba79d0 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-with-submatch.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=fd31fa3572e5fd97533991704dac17f4 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-with-submatch.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=b6f1450934adca457281b530f3d0e2ad 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-with-submatch.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=2a6aff299223d9562630e02f0654d78d 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-with-submatch.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=c67aa861d96ca2034c7f8ea84e5f7784 2500w" />

The following JSON will be matched:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "itemName": "Socks"
}'
```

### Expression only vs. expression + sub-match

It is possible to match a JSON document without a sub-match by selecting "is present"
from the drop-down:

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-no-submatch.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=762027b220471f579dde96666cfee3de" title="JSONPath with equal to" data-og-width="791" width="791" data-og-height="149" height="149" data-path="images/screenshots/jsonpath-no-submatch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-no-submatch.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=19088c5bf8e7bd7740cd0848e3ff98d5 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-no-submatch.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=333766376ec2a97cbb1a5ae94bd213de 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-no-submatch.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=4e4bd2ea085e94c4fbdc5c9e42d7ae6d 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-no-submatch.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=322c9c36f8f9f90e6ba9437325e297d0 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-no-submatch.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=a420440a9b867f07152a932436330343 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/jsonpath-no-submatch.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=4a9beeb981b9c385d91147be4122cbfe 2500w" />

If you do this, the JSON input will be considered a match if the expression returns
1 or more elements.

This feature is primarily present for compatibility with WireMock projects, and
generally it is better to use sub-matches as this results in simpler JSONPath
expressions and more useful debug output when there is a non-match.

### Common JSONPath examples

Matching on a specific array element by position.

`$.sizes[1]` `equal to` `M`

would match:

```json  theme={null}
{
  "sizes": ["S", "M", "L"]
}
```

Matching on an element of an object found via another element.

`$.addresses[?(@.type == 'business')].postcode` `contains` `N11NN`

would match:

```json  theme={null}
{
  "addresses": [
    {
      "type": "home",
      "postcode": "Z55ZZ"
    },
    {
      "type": "business",
      "postcode": "N11NN"
    }
  ]
}
```

It is necessary to use `contains` in this instance as a JSONPath expression containing
a query part (between the `[?` and `]`) will always return a collection
of results.

Matching an element found recursively.

`$..postcode` `contains` `N11NN`

would match:

```json  theme={null}
{
  "addresses": [
    {
      "type": "home",
      "postcode": "Z55ZZ"
    },
    {
      "type": "business",
      "postcode": "N11NN"
    }
  ]
}
```

and would also match:

```json  theme={null}
{
  "address": {
    "type": "business",
    "postcode": "N11NN"
  }
}
```
