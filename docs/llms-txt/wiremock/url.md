# Source: https://docs.wiremock.io/request-matching/url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Request Matching - Matching URLs

> Matching the request's URL

For most HTTP APIs the URL is the primary means by which the appropriate action
is selected. WireMock Cloud provides a number of different options for matching the
URL of an incoming request to a stub.

## Path vs path + query

It's important to be clear exactly which part(s) of the URL you wish to match.

The default strategy WireMock Cloud uses is to match both the path and query parts of the
URL. For instance, if you were you to enter the following in a stub's URL field:

```
/my/path?q=abc&limit=10
```

then the stub would only be matched if that exact path and query were present e.g.
for the URL:

```
https://my-api.wiremockapi.cloud/my/path?q=abc&limit=10
```

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-and-query.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0f3a5703209be5c39efaee35469ca8d4" title="Path and query matching" data-og-width="752" width="752" data-og-height="210" height="210" data-path="images/screenshots/url-path-and-query.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-and-query.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=1c842e7c448d067b5e8edfcf3ada0053 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-and-query.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=e19fcacab9fd46b050e75f7be05e2dbe 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-and-query.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=74aa90f67d043eab000b70bb2dc5f28c 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-and-query.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3968f945b0735be23fd8f72095ddb5e7 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-and-query.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=1a9eae453974b4894c1d5aa2f11708cf 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-and-query.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=27fd9236eda11851c8a7145d664d47d9 2500w" />

However, it's often desirable just to look at the path part of the URL, and either
ignore the query completely or specify it more flexibly using dedicated query parameter
matchers (see [Query Parameters](/advanced-stubbing/#advanced-request-parameter-matching)).
Dedicated query matchers can be useful if the parameter order in the URL can change,
or if you need to match more loosely on the value e.g. using `contains` rater than
exact equality.

To do this, you need to change the URL match type in the Advanced section to `Path`
and ensure you only specify a path in the URL field e.g.

```
/my/path
```

This would now match any of the following URLs:

```
https://my-api.wiremockapi.cloud/my/path?q=abc
https://my-api.wiremockapi.cloud/my/path?q=abc&limit=10
https://my-api.wiremockapi.cloud/my/path
https://my-api.wiremockapi.cloud/my/path?randomqueryparam=123
```

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-matching.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0c9ec0c8799b4ae4da76d2defe0c2b09" title="Path and query matching" data-og-width="803" width="803" data-og-height="374" height="374" data-path="images/screenshots/url-path-matching.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-matching.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=1634a4271a05ea6851ef40c577abb85a 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-matching.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0432dc30352a5f7d289baa575c34accc 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-matching.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0004d3595cf1fc6b8030c6682649da9f 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-matching.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=639f106a52e8c157d1d36eff571d6cc7 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-matching.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a2861dd6c1a12a9f3a35ccd380a637ad 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-matching.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=25745f9bbc9cc80e618ede549e5af844 2500w" />

## Match type - exact vs. regular expression

In addition to choosing the URL part(s) you wish to match, you can also choose whether
to check for exact equality or a regular expression match. By default WireMock Cloud uses
an equality check, but this can be changed in the Advanced section.

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3f01540a07c388d14f17e376447dcd5e" title="URL match types" data-og-width="249" width="249" data-og-height="147" height="147" data-path="images/screenshots/url-match-type-screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=89e466a60aa80428857768c9827caf63 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=f998d86c8fb156867f0b9a202b03efa8 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=938e157cda59c07b7975f33d62e3b264 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=8057601bde8592a5ba2d4b606df63530 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=658334eec9489ed982fa55f1564efa77 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-match-type-screenshot.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=72f7cc8747ddd54f96813a5e12b565b3 2500w" />

Choosing the `Path regex` match type can be particularly useful in cases where
the API you're mocking uses path parameters and you wish to provide a meaningful response
to a specific URL pattern regardless of the specific parameter values.

For instance, choosing `Path regex` as the match type with the following URL

```
/users/[0-9]+
```

would match any of the following request URLs:

```
/users/1
/users/9832749823
/users/321
```

A powerful approach is to combine this with [Response Templating](/response-templating/basics/)
so that the ID used in the URL can be inserted into the response body.

<Note>Using the Path and query regex is generally not advised. This exists primarily for compatibility with projects exported to/from WireMock.</Note>

## Path template (path parameters)

If you require a stub's URL to allow dynamic path variables, you can use the path template URL match type.
This URL match type provides a convenient way to match URLs whose path segments match certain values and/or a way to
reference a request's dynamic path segments by name in a response template, rather than the usual indexed method
(e.g. `request.path.thingId` rather than `request.path.1`).

To configure a stub to use the path template URL match type, enter a path value that declares one or more path variables
using square bracket syntax (e.g. `/things/{thingId}`) and select the "Path template" URL match type.
Now you can add path parameters that match against the value of a request's path variables.

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-template.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=02616cb9e1c5967a7536ed75cba1c365" title="URL path template and parameter" data-og-width="1007" width="1007" data-og-height="361" height="361" data-path="images/screenshots/url-path-template.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-template.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=9014d16fc80ba602b3217cc47052f401 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-template.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=36053178a1d818dd1e6f852e1e963688 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-template.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=d6a9cb730bd8f9cc416b3c61a02b7df4 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-template.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=f3df6174aeba65d0c9ee33ffd2f0bfd9 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-template.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=774ffce37667d694fc3b01923b4f37a2 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-template.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=36fdf576b65a283631df072f08a75779 2500w" />

You can also now reference the value of a request's path variables by name in the response template.

<img src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-parameter-in-template.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=6f8a31f0444763447d86bc3cc905e13a" title="Referencing a URL path parameter in a template" data-og-width="455" width="455" data-og-height="203" height="203" data-path="images/screenshots/url-path-parameter-in-template.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-parameter-in-template.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=c1416d18f90cf9dc1d1a1a9a240c2161 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-parameter-in-template.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=2d1a9d62ee9d5cbc48fd43a0f80efa53 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-parameter-in-template.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=ed129a14920f789e2f456ffdfc963760 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-parameter-in-template.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=213da429bb4e8b2e9dbaff3b9a3fbd92 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-parameter-in-template.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=b7f6f6a1a084cdb7ff652eff0d0b2edb 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/url-path-parameter-in-template.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=6446b8599b890f95831e5311b8d94a8a 2500w" />

## Matching any URL

In some cases you need a stub to match any request URL. A common use case for this
is providing a low priority default response which is matched only if nothing else does.
You might also choose to proxy the request to another endpoint in this case.

For this purpose use the `Any URL` option from the URL match type list under Advanced.
