# Source: https://redocly.com/learn/openapi/openapi-visual-reference/responses.md

# Responses Map

The Responses Map describes the possible responses to an HTTP request.
It is declared in the Operation Object.
The documentation is expected to cover at least one successful case.


```yaml
responses:
  '200':
    # Response Object | Reference Object
```

details
summary

Excerpt from the OpenAPI 3.1 specification about responses

> A container for the expected responses of an operation. The container maps a HTTP response code to the expected response.
The documentation is not necessarily expected to cover all possible HTTP response codes because they may not be known in advance. However, documentation is expected to cover a successful operation response and any known errors.
The `default` MAY be used as a default response object for all HTTP codes that are not covered individually by the `Responses Object`.
The `Responses Object` MUST contain at least one response code, and if only one response code is provided it SHOULD be the response for a successful operation call.
This object MAY be extended with Specification Extensions.
## Fixed Fields
| Field Name | Type | Description |
|  --- | --- | --- |
| default | [Response Object](/learn/openapi/openapi-visual-reference/response) | [Reference Object](/learn/openapi/openapi-visual-reference/reference) | The documentation of responses other than the ones declared for specific HTTP response codes. Use this field to cover undeclared responses. |

## Patterned Fields
| Field Pattern | Type | Description |
|  --- | --- | --- |
| HTTP Status Code | [Response Object](/learn/openapi/openapi-visual-reference/response) | [Reference Object](/learn/openapi/openapi-visual-reference/reference) | Any HTTP status code can be used as the property name, but only one property per code, to describe the expected response for that HTTP status code. This field MUST be enclosed in quotation marks (for example, "200") for compatibility between JSON and YAML. To define a range of response codes, this field MAY contain the uppercase wildcard character `X`. For example, `2XX` represents all response codes between `[200-299]`. Only the following range definitions are allowed: `1XX`, `2XX`, `3XX`, `4XX`, and `5XX`. If a response is defined using an explicit code, the explicit code definition takes precedence over the range definition for that code. |



## Visuals

The following examples use a minimal [Response Object](/learn/openapi/openapi-visual-reference/response) with a `description`.
The [Response Object](/learn/openapi/openapi-visual-reference/response) topic covers the response object in depth.

### default

The `default` can be used to cover undeclared responses.
The `default` response is not required and used less frequently.

If there are no successful responses declared in the responses map, then the `default` is highlighted as successful in green.


```yaml
responses:
  default:
    description: Default response
  '400':
    description: Bad Request
  '409':
    description: Conflict
  '503':
    description: Service unavailable
```

![default is green](/assets/responses-default-success.0380bf483f1e6923deeeea79d880b0775c54e1515ae90add3ef9b90675e2cd58.6f948c6e.png)

If there is at least one successful response declared, then the `default` is highlighted similarly to an error in red.


```yaml
responses:
  '200':
    description: OK
  default:
    description: Default response
```

![default is red](/assets/responses-default-error.3e557e6918e1a061ae798ad91ad2e59fa556dfea3126946b03445215ee288ad5.6f948c6e.png)

### Successful response

The responses MUST contain one successful response.
As mentioned above, if there is a `default` and no other successful responses, then it is assumed to be the successful response.

Otherwise, the successful responses are in the 200-series from 200 to 299.
The common responses are:

| Successful code | Description |
|  --- | --- |
| 200 | OK |
| 201 | Created |
| 202 | Accepted |
| 204 | No Content |


It is also possible to use `2XX` to indicate any successful response.


```yaml
responses:
  '200':
    description: OK
  '201':
    description: Created
  '202':
    description: Accepted
```

![200, 201, 202 green](/assets/responses-success.223c0682ae7ad82bcefe01172268bdc96e318556f179527765c9daca85810eb2.6f948c6e.png)


```yaml
responses:
  2XX:
    description: Success
```

![200, 201, 202 green](/assets/responses-success-range.49d9e15a1e0a6212bdca04eac58ffc6cab5dbd7efac1c0b24837df60fee560da.6f948c6e.png)

### Redirects

Redirects are in the 300-series (300-399).
`3XX` is used to indicate any redirect response.

The common responses are:

| Redirect code | Description |
|  --- | --- |
| 301 | Moved Permanently |
| 302 | Found |
| 303 | See Other |



```yaml
responses:
  '200':
    description: OK
  '303':
    description: See Other
```

![redirect](/assets/responses-redirect.c398e50067f448e2f956ec8e09a52d20e8b2e174facdbcad53202cbc437050bf.6f948c6e.png)

### Client errors

Client errors are in the 400-series (400-499).
It is possible to use `4XX` to indicate any client error.

The common client errors are:

| Error code | Description |
|  --- | --- |
| 400 | Moved Permanently |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Unprocessable Content |
| 429 | Too Many Requests |



```yaml
responses:
  '200':
    description: OK
  '400':
    description: Bad Request
  '409':
    description: Conflict
```

![client errors](/assets/responses-client-errors.fc1004e9abea1a6833aa5b36ea7a9496b208e22f29a4663fcbce1c2ef213c5ab.6f948c6e.png)

### Server errors

Server errors are in the 500-series (500-599).
They can be represented with `5XX` to indicate any server error.

Server errors are usually not described in API definitions.

The common server errors are:

| Error code | Description |
|  --- | --- |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |



```yaml
responses:
  '200':
    description: OK
  '503':
    description: Service Unavailable
```

![server errors](/assets/responses-server-errors.95d9368316dd895d4936481bb5b2f07857192afa4933b92b7139f32540747f11.6f948c6e.png)

### Informational response

While rarely defined in APIs, it is possible to describe informational responses which are in the 100-series (100-199).
Use `1XX` to describe the entire range of informational responses.

The common informational responses are:

| Informational code | Description |
|  --- | --- |
| 100 | Continue |
| 101 | Switching Protocols |



```yaml
responses:
  '100':
    description: Continue
  '200':
    description: OK
```

![informational continue](/assets/responses-informational.4b1ff8d034e7ac2697a8c02b5de6c1706dc077d071c6207a5d5392e4b74689a3.6f948c6e.png)

## Types

- NamedResponses
- Responses
- Response



```ts
const Responses: NodeType = {
  properties: { default: 'Response' },
  additionalProperties: (_v: any, key: string) =>
    responseCodeRegexp.test(key) ? 'Response' : undefined,
};

const Response: NodeType = {
  properties: {
    description: { type: 'string' },
    headers: mapOf('Header'),
    content: 'MediaTypesMap',
    links: mapOf('Link'),
  },
  required: ['description'],
};
```