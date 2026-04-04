# Source: https://docs.wiremock.io/openAPI/openapi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAPI Mocking and Prototyping

> Overview of the OpenAPI mock API type and two-way mock generation

WireMock Cloud supports an OpenAPI mock API type that provides both incremental generation of stubs from OpenAPI and OpenAPI generation from stubs. Mock APIs of this type also have an associated auto-generated set of public documentation pages.

This supports two types of workflow:

1. Automatic generation/amendment of a mock API from an existing OpenAPI doc as it evolves,
2. API prototyping - defining API behaviour via stubs and auto-generating OpenAPI + documentation.

These workflows can be combined i.e. when prototyping new behaviour for an existing API.

## Getting started

From the app's home screen, create a new mock API and choose the OpenAPI type:

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-mock-api.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=fcfe74fc94e8e1f66b1daf1d6811dada" alt="New mock API type picker" width="50%" data-og-width="1676" data-og-height="1034" data-path="images/openapi/new-mock-api.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-mock-api.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=88ad3c4277debf924170226ae6ee0901 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-mock-api.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=9d69e3464c0b232974f2481737d334d8 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-mock-api.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=3cf3011b81f8f62beefdae8d761cadf7 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-mock-api.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=e6f5b7abbe9df438bb928107209e1580 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-mock-api.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=1fec6fd3908f8ce5e22d7fe2017e6054 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-mock-api.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=f647ca99d1761b0b1e1b68781d308ec0 2500w" />

When the new mock API is created an extra item will be present on the left-hand nav bar, taking you to the OpenAPI editor page:

<img src="https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/openapi-editor-nav.png?fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=8130098dd6fdf1a9d972af775c915652" alt="OpenAPI editor navigation item" width="50%" data-og-width="968" data-og-height="873" data-path="images/openapi/openapi-editor-nav.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/openapi-editor-nav.png?w=280&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=d7494979a309c380e936d8afa2ecafe2 280w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/openapi-editor-nav.png?w=560&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=28ded1e07877b854646b5c46f5e743cf 560w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/openapi-editor-nav.png?w=840&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=bc3bdb38c9b4e89bdb113eb187fabae8 840w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/openapi-editor-nav.png?w=1100&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=f40c808a64b6bdb2fcd0d339c3dec961 1100w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/openapi-editor-nav.png?w=1650&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=fa255f7de3182c135dcd232a272a7100 1650w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/openapi-editor-nav.png?w=2500&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=f3f41a58968367a67527cd989f071c89 2500w" />

Navigating to the Settings tab on the same page, toggling on "Enable public API documentation" and clicking the link underneath will show the public API documentation (which will be initially empty apart from header information since there are no paths defined in the OpenAPI doc).

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/enabled-portal.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=6d83987dfc04cdb9c59ba3113a6271aa" alt="Public API documentation settings" width="50%" data-og-width="592" data-og-height="318" data-path="images/openapi/enabled-portal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/enabled-portal.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=6d3a74744814e85ff4f4537caf96a307 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/enabled-portal.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=582b651a9792f286fb740bda7d3c58b7 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/enabled-portal.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=e1281f1a9ccba63c661ae1108d064210 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/enabled-portal.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=29521ed3b4c134414a83aa309efdba2f 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/enabled-portal.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=883741ffa7e6124df9601a8cf2a79d90 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/enabled-portal.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=92dfa5f00a23d37d898556ea61c6245a 2500w" />

## Generating stubs from OpenAPI

Stubs will be created or updated whenever changes are saved to the OpenAPI doc.

Add a new path entry and click Save:

<img src="https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/added-customer-openapi-path.png?fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=a2220aed054abec2592b412e1c76008f" alt="Add customer path to OpenAPI" width="50%" data-og-width="687" data-og-height="840" data-path="images/openapi/added-customer-openapi-path.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/added-customer-openapi-path.png?w=280&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=11ac3d50720acac5e77d0c471c9776a5 280w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/added-customer-openapi-path.png?w=560&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=2baaf17464aa480f92637effacdf4c3a 560w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/added-customer-openapi-path.png?w=840&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=eb264dac66a7a326d4f67ecc32d8b5da 840w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/added-customer-openapi-path.png?w=1100&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=0ea72309aee605ed18673311a24b9e2b 1100w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/added-customer-openapi-path.png?w=1650&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=faa35a81238452cf4acd9a65d5e37c58 1650w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/added-customer-openapi-path.png?w=2500&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=a158f9d9aeb61f25818b82f5d83ac2bd 2500w" />

Then navigate to the Stubs page and see that two new stubs have been created - one with specific request parameters required and one "default" i.e. will match regardless of specific parameter values provided the method and URL path are correct.

<img src="https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/generated-customer-stubs.png?fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=ac89ee3a04bfde5b36dfe0094e94c785" alt="Generated customer stubs" width="50%" data-og-width="485" data-og-height="623" data-path="images/openapi/generated-customer-stubs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/generated-customer-stubs.png?w=280&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=8b8ab29cefd9a79cf22a1c5c68f248c9 280w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/generated-customer-stubs.png?w=560&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=9c0be14fb6f5bcc0bbe7e9d956e08f0e 560w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/generated-customer-stubs.png?w=840&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=8a81ebf902dd14b6de14895e159b264a 840w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/generated-customer-stubs.png?w=1100&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=9bc8f74e7fe885474759cc2d1179710c 1100w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/generated-customer-stubs.png?w=1650&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=c96253b472ac8540b8d191c3f2026008 1650w, https://mintcdn.com/wiremockinc/piH_NqX1m4W7gcPW/images/openapi/generated-customer-stubs.png?w=2500&fit=max&auto=format&n=piH_NqX1m4W7gcPW&q=85&s=ad65e263cc167bcc3cad44c693af48d9 2500w" />

Stubs will be generated following the [stub generation rules](#stub-generation-rules).

### Updating an OpenAPI doc

When an OpenAPI doc is updated, for every `path-method-status-contentType`, existing stubs will be updated if any of the following apply:

* The existing stub was generated from an example and the example hasn't changed its name.
* If there is one example within the given `path-method-status-contentType` which shares the response body with the existing stub.
* If the `path-method-status-contentType` only provides a single example.
* If the `path-method-status-contentType` doesn't provide examples at all.

If none of the conditions above are satisfied, one or more stubs will be generated following the [stub generation rules](#stub-generation-rules).

WireMock Cloud takes a non-destructive approach to your stubs.  This means that if you delete a path, method, status
or contentType, the stub that represents that OpenAPI element will remain in your Mock API. This also applies to updating
elements in your OpenAPI.  For example, if you update a path in your OpenAPI from `/orders` to `/v1/orders` the path
will be classed as a new path and a new stub will be created.  The old stub will not be deleted.

If you are modeling new data scenarios and you add new stubs to your Mock API after generating stubs from an OpenAPI
specification, these stubs will not always be updated when you update your OpenAPI specification.  If those new stubs
do not match an example in your OpenAPI specification, they will not be updated when you update your OpenAPI specification
(adding a new parameter for example) and you will need to update those manually.

### Stub generation rules

When updating an OpenAPI doc, the resulting stubs from new OpenAPI elements will be added.
Stub generation will be based on the following rules:

* `304` response:
  * Request header matcher `If-None-Match` with specific value `12345`.
* `422` response:
  * Only one stub will be generated, with a request body matcher not matching the schema or missing.
  * If more than one response example provided, it will pick one randomly as the response body.
  * If no response example provided, the response body will be autogenerated based on the schema.
* `400` response:
  * Only one stub will be generated, with neither request parameters nor body present or matching the schema.
  * If more than one response example provided, it will pick one randomly as the response body.
  * If no response example provided, the response body will be autogenerated based on the schema.
* Any other response status:
  * If no example is provided, it will generate a stub with autogenerated request parameters and response, based on schema.
  * If at least one example is provided:
    * It will generate one stub per example, using specific request parameter matchers and taking the example as the response body.
    * The request parameter matchers will be autogenerated based on the schema, unless the extension `x-parameter-values` is provided (as explained [here](./swagger)), in which case it will be used to generate the expected values of the parameter matchers.

### Controlling generated parameter values in your stubs

If an OpenAPI element has a parameter (header for example) that is set to `required: true` then the stub will be generated
or updated with that parameter. WireMock Cloud adds a value for that parameter to match on.  You can control the value
generated in your stubs using various OpenAPI elements:

If no min or max length are provided in the schema, defaults of a minimum of 3 and a maximum of
200 is used. Therefore, an OpenAPI specification snippet like the following:

```yaml  theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
```

Could generate a `tripId` equalsTo matcher with the following value - `gtpq1fggnuolb31tya6rrc1tye1am5bkzw5kjxxeyscx9lb3zhla`

Adding a `minLength` and a `maxLength` to the schema will control the size of the random string. The snippet below:

```yaml  theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
      schema:
        type: string
      maxLength: 5
      minLength: 2
```

Could generate a `tripId` equalsTo matcher with the following value - `aspp`

You can force a value to be used in the matcher by creating an enum with only one value. This is effectively the same as
generating a constant:

```yaml  theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
      schema:
        type: string
      enum:
        - "1"
```

If an enum is used with multiple values, then a random item from the enum is used in the matcher.

Alternatively, a regex pattern can be used in the schema to further control the value used in the matcher:

```yaml  theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
      schema:
        type: string
      pattern: "^trip-id-\\d{8}$"
```

Could generate a `tripId` equalsTo matcher with the following value - `trip-id-68975013`.

Optional `minLength` and `maxLength` elements can be used to further control the generated value:

```yaml  theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
      schema:
        type: string
      pattern: "^trip-id-\\d{8}$"
      maxLength: 9
      minLength: 2
```

Could generate a `tripId` equalsTo matcher with the following value - `trip-id-6`.

#### Default stubs

[//]: # "WARNING: This heading is referenced by the UI. Do not change it without changing the link in the UI."

Optionally, for each path and method in the OpenAPI specification with a response status of 2xx, a "default" stub can also be generated.
This default stub will not contain any specific request parameter matchers, only a request body matcher that matches the request body schema in the OpenAPI specification, if a schema is provided.
To turn on/off the generation of default stubs, go to the Settings tab of the OpenAPI page, where the toggle is located.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generate-default-stubs-toggle.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=8b07e4d260a84a8266ca293716b767b1" alt="Generate default stubs toggle" data-og-width="370" width="370" data-og-height="277" height="277" data-path="images/openapi/generate-default-stubs-toggle.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generate-default-stubs-toggle.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=00cba21c68961dc94a757bbcb36eea98 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generate-default-stubs-toggle.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=53df3669f2873eb9f556d98507f3a552 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generate-default-stubs-toggle.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=f7533a451c31dd398a3260af016349ff 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generate-default-stubs-toggle.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=77afcac1e7ccd6f0c3eb64c28648cb0a 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generate-default-stubs-toggle.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=823d12906a31cde227fb47b6e418465e 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generate-default-stubs-toggle.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=34c63ddf02fb905a30e79cbb22190226 2500w" />

## Prototyping - generating OpenAPI from stubs

OpenAPI elements will be generated or updated when stubs are created or changed.

Try creating a stub with a new path template that doesn't yet exist in the OpenAPI document:

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-request.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=30900daba8acbe1d124518c1626ba5fa" alt="Stub request with new path template" data-og-width="1608" width="1608" data-og-height="892" height="892" data-path="images/openapi/new-charge-stub-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-request.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=6b0a6cd883a720f97efce267c838e436 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-request.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=6df4d61682db525bea34dda0f1644668 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-request.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=94aada15f9cfbcc2c7a78daf62c59831 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-request.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=4085d3c2ab9a90928c5bb5c282fc7308 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-request.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=bb0e355bd2feb1fbeb22f9b908068fae 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-request.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=8d8651bed6d576fbab985fc2f5b8d6d2 2500w" />

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-response.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=eb2d1ebd50b2e1187e756aa11ac85c21" alt="Stub response with new path template" data-og-width="1618" width="1618" data-og-height="1086" height="1086" data-path="images/openapi/new-charge-stub-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-response.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=879053bfb96a85aa6728152dc96a2713 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-response.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=d57cf39f3a867f3d36988572265a443c 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-response.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=9e7631e6d262591ea80f8c40f8d438b0 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-response.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=1d8ef66bd6b54339d826e6ef6a92348c 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-response.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=e74e24855d1bc38ca259a864c8d87b96 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/new-charge-stub-response.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=8e05de141a0c248ac8b54de73da0d12e 2500w" />

On save, the path plus operation, responses, schemas and examples will be added to the OpenAPI spec and also to the public documentation.

Automatic generation of OpenAPI to stubs and vice versa can be turned off in the Settings tab of the OpenAPI page.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generation-settings.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=a3485801ea60d4ce56ae57d62071c7db" alt="Stub and OpenAPI generation settings" width="50%" data-og-width="845" data-og-height="747" data-path="images/openapi/generation-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generation-settings.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=40b142dde3fad91d6280824c3818674b 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generation-settings.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=f488b4fbe2807513f262e7dba1a35d65 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generation-settings.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=3b40e2afceb1cd1638ba22b9b1ff6d6f 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generation-settings.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=f19d713f4a9ff98c1d880a5b91b8596c 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generation-settings.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=8d11d8cd2e3295e282a8441d662e2f7d 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/generation-settings.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=a3b161ad06bb94ad236630eedd7a43fc 2500w" />
