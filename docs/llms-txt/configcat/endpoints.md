# Source: https://configcat.com/docs/advanced/proxy/endpoints.md

# Endpoints

Copy page

The Proxy accepts HTTP requests on the following endpoints.

## CDN Proxy[​](#cdn-proxy "Direct link to CDN Proxy")

The CDN proxy endpoint's purpose is to forward the underlying *config JSON* to other ConfigCat SDKs used by your application.

GETOPTIONS/configuration-files/{path}

This endpoint is mainly used by ConfigCat SDKs to retrieve all required data for feature flag evaluation.

**Route parameters**:

* `path`: It's set by the ConfigCat SDK configured to use the ConfigCat Proxy. It contains either an SDK key or an [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that uniquely identifies an SDK within the Proxy.

**Responses**:

* 200: The `config.json` file is downloaded successfully.
* 204: In response to an `OPTIONS` request.
* 304: The `config.json` file isn't modified based on the `Etag` sent in the `If-None-Match` header.
* 400: The `sdkId` is missing.
* 404: The `sdkId` is pointing to a non-existent SDK.

### SDK Usage[​](#sdk-usage "Direct link to SDK Usage")

In order to let a ConfigCat SDK use the Proxy, you have to set the SDK's `baseUrl` parameter to point to the Proxy's host.

example.js

```js
import * as configcat from "@configcat/sdk";

const configCatClient = configcat.getClient(
  "#YOUR-SDK-KEY#", 
  configcat.PollingMode.AutoPoll,
  { baseUrl: "http://localhost:8050" } // Proxy URL
);

```

Additionally, as the Proxy maps [unique identifiers to each configured SDK key](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) it works with, you can use that identifier prefixed with `configcat-proxy/` as the SDK key at the ConfigCat SDK's initialization.

So, let's assume you set up the Proxy with an SDK key mapped to the `my_sdk` SDK identifier:

example.js

```js
import * as configcat from "@configcat/sdk";

const configCatClient = configcat.getClient(
  "configcat-proxy/my_sdk", // SDK identifier prefixed with 'configcat-proxy/'
  configcat.PollingMode.AutoPoll,
  { baseUrl: "http://localhost:8050" } // Proxy URL
);

```

### Supported SDK Versions[​](#supported-sdk-versions "Direct link to Supported SDK Versions")

The following SDK versions are supported by the `>=v0.3.X` Proxy's CDN endpoint:

| SDK                                                                          | Version                                                                     |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| .NET                                                                         | >= [v9.0.0](https://github.com/configcat/.net-sdk/releases/tag/v9.0.0)      |
| Android (Java)                                                               | >= [v10.0.0](https://github.com/configcat/android-sdk/releases/tag/v10.0.0) |
| C++                                                                          | >= [v4.0.0](https://github.com/configcat/cpp-sdk/releases/tag/v4.0.0)       |
| Dart (Flutter)                                                               | >= [v4.0.0](https://github.com/configcat/dart-sdk/releases/tag/4.0.0)       |
| Elixir                                                                       | >= [v4.0.0](https://github.com/configcat/elixir-sdk/releases/tag/v4.0.0)    |
| Go                                                                           | >= [v9.0.0](https://github.com/configcat/go-sdk/releases/tag/v9.0.0)        |
| Java                                                                         | >= [v9.0.0](https://github.com/configcat/java-sdk/releases/tag/v9.0.0)      |
| JavaScript (Browser, Bun, Chromium Extension, Cloudflare Worker, Deno, Node) | >= [v1.0.0](https://github.com/configcat/js-unified-sdk/releases)           |
| JS - Legacy                                                                  | >= [v9.0.0](https://github.com/configcat/js-sdk/releases/tag/v9.0.0)        |
| JS SSR - Legacy                                                              | >= [v8.0.0](https://github.com/configcat/js-ssr-sdk/releases/tag/v8.0.0)    |
| Kotlin                                                                       | >= [v3.0.0](https://github.com/configcat/kotlin-sdk/releases/tag/3.0.0)     |
| Node - Legacy                                                                | >= [v11.0.0](https://github.com/configcat/node-sdk/releases/tag/v11.0.0)    |
| PHP 8.1+                                                                     | >= [v9.0.0](https://github.com/configcat/php-sdk/releases/tag/v9.0.0)       |
| PHP 7.1+                                                                     | >= [v3.0.0](https://github.com/configcat/php7-sdk/releases/tag/v3.0.0)      |
| Python                                                                       | >= [v9.0.3](https://github.com/configcat/python-sdk/releases/tag/v9.0.3)    |
| React                                                                        | >= [v4.0.0](https://github.com/configcat/react-sdk/releases/tag/v4.0.0)     |
| Ruby                                                                         | >= [v8.0.0](https://github.com/configcat/ruby-sdk/releases/tag/v8.0.0)      |
| Rust                                                                         | >= [v0.1.0](https://github.com/configcat/rust-sdk/releases/tag/v0.1.0)      |
| Swift (iOS)                                                                  | >= [v11.0.0](https://github.com/configcat/swift-sdk/releases/tag/11.0.0)    |

### Available Options[​](#available-options "Direct link to Available Options")

The following CDN Proxy related options are available:

| Option                                                                                                                                                                                                                                                                                                                             | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - YAML<br />- Environment variable```yaml
http:
  cdn_proxy:
    enabled: <true|false>

``````shell
CONFIGCAT_HTTP_CDN_PROXY_ENABLED=<true|false>

```                                                                                                                                                                                     | `true`  | Turns the hosting of the CDN proxy endpoint on/off. This endpoint can be used by other ConfigCat SDKs in your applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - YAML<br />- Environment variable```yaml
http:
  cdn_proxy:
    cors:
      enabled: <true|false>

``````shell
CONFIGCAT_HTTP_CDN_PROXY_CORS_ENABLED=<true|false>

```                                                                                                                                                                     | `true`  | Turns the sending of CORS headers on/off. It can be used to restrict access to specific domains. By default, the Proxy allows each origin by setting the `Access-Control-Allow-Origin` response header to the request's origin. You can override this functionality by restricting the allowed origins with the `allowed_origins` or `allowed_origins_regex` options.                                                                                                                                                                                                                                                                                             |
| - YAML<br />- Environment variable```yaml
http:
  cdn_proxy:
    cors:
      allowed_origins: 
        - https://domain1.com
        - https://domain2.com

``````shell
CONFIGCAT_HTTP_CDN_PROXY_CORS_ALLOWED_ORIGINS='["https://domain1.com","https://domain2.com"]'

```                                                                    | -       | List of allowed CORS origins. When it's set, the Proxy will include only that origin in the `Access-Control-Allow-Origin` response header which matches the request's `Origin`.<br />When there's no matching request origin and the `allowed_origins_regex` option is not set, the Proxy will set the `Access-Control-Allow-Origin` response header to the first item in the allowed origins list.                                                                                                                                                                                                                                                               |
| - YAML<br />- Environment variable```yaml
http:
  cdn_proxy:
    cors:
      allowed_origins_regex:
        patterns:
          - https:\/\/.*domain1\.com
          - https:\/\/.*domain2\.com

``````shell
CONFIGCAT_HTTP_CDN_PROXY_CORS_ALLOWED_ORIGINS_REGEX_PATTERNS='["https:\\/\\/.*domain1\\.com","https:\\/\\/.*domain2\\.com"]'

``` | -       | List of regex patterns used to match allowed CORS origins. When it's set, the Proxy will match the request's `Origin` with the given regex patterns. When there's a match, the `Access-Control-Allow-Origin` response header will be set to the matched origin.<br />When there's no matching request origin, the Proxy will set the `Access-Control-Allow-Origin` response header to the `if_no_match` field's value.<br />The `if_no_match` option is mandatory if this option is used.<br />When using the environment variable, the regex escape character must be doubled (`\\`) because it's parsed as a JSON list and `\` is also a JSON escape character. |
| - YAML<br />- Environment variable```yaml
http:
  cdn_proxy:
    cors:
      allowed_origins_regex:
        if_no_match: https://domain1.com

``````shell
CONFIGCAT_HTTP_CDN_PROXY_CORS_ALLOWED_ORIGINS_REGEX_IF_NO_MATCH="https://domain1.com"

```                                                                                         | -       | Required when the previous `patterns` option is set. It's value is used in the `Access-Control-Allow-Origin` header when an incoming request's `Origin` doesn't match with any previously configured regex patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - YAML<br />- Environment variable```yaml
http:
  cdn_proxy:
    headers:
      Custom-Header-Name: "<header-value>"

``````shell
CONFIGCAT_HTTP_CDN_PROXY_HEADERS='{"Custom-Header-Name":"<header-value>"}'

```                                                                                                                           | -       | Additional headers that must be sent back on each CDN proxy endpoint response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## API[​](#api "Direct link to API")

These API endpoints are for server side feature flag evaluation.

### Endpoints using SDK key[​](#endpoints-using-sdk-key "Direct link to Endpoints using SDK key")

The following endpoints are using SDK keys to determine which config / environment is the target of the desired action. The SDK key must be provided in the `X-ConfigCat-SdkKey` HTTP header.

info

These endpoints are only available from Proxy version [`v3.0.0`](https://github.com/configcat/configcat-proxy/releases/tag/v3.0.0).

POSTOPTIONS/api/eval

This endpoint evaluates a single feature flag identified by a `key` with the given [User Object](https://configcat.com/docs/targeting/user-object.md).

**Headers**:

* `X-ConfigCat-SdkKey`: The SDK key that determines the feature flag's config / environment.

**Request body**:

```json
{
  "key": "<feature-flag-key>",
  "user": {
    "Identifier": "<user-id>",
    "Rating": 4.5,
    "Roles": ["Role1","Role2"],
    // any other attribute
  }
}

```

The type of the `user` object's fields can only be `string`, `number`, or `string[]`.

**Responses**:

* 200: The feature flag evaluation finished successfully.
* Response body:
  ```json
  {
    "value": <evaluated-value>,
    "variationId": "<variation-id>"
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `X-ConfigCat-SdkKey` header or the `key` from the request body is missing.
* 404: The `X-ConfigCat-SdkKey` header is pointing to a non-existent SDK.

**Example**:

example.js

```js
const url = "http://localhost:8050/api/eval"; // Proxy API URL

const data = {
  key: "isMyAwesomeFeatureEnabled", // Feature flag key
  user: { // User Object for evaluation
    Identifier: "#UNIQUE-USER-IDENTIFIER#"
  }
};

const requestOptions = {
  method: "POST",
  headers: {
    "X-ConfigCat-SdkKey": "#YOUR-SDK-KEY#",
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
};

try {
  const response = await fetch(url, requestOptions);
  const responseData = await response.json();
  console.log(responseData); // {"value":<evaluated-value>,"variationId":"<variation-id>"}
} catch (error) {
  console.error("Error:", error)
}

```

POSTOPTIONS/api/eval-all

This endpoint evaluates all feature flags with the given [User Object](https://configcat.com/docs/targeting/user-object.md).

**Headers**:

* `X-ConfigCat-SdkKey`: The SDK key that determines which config's feature flags should be evaluated in which environment.

**Request body**:

```json
{
  "user": {
    "Identifier": "<user-id>",
    "Rating": 4.5,
    "Roles": ["Role1","Role2"],
    // any other attribute
  }
}

```

The type of the `user` object's fields can only be `string`, `number`, or `string[]`.

**Responses**:

* 200: The evaluation of all feature flags finished successfully.
* Response body:
  ```json
  {
    "feature-flag-key-1": {
      "value": <evaluated-value>,
      "variationId": "<variation-id>"
    },
    "feature-flag-key-2": {
      "value": <evaluated-value>,
      "variationId": "<variation-id>"
    }
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `X-ConfigCat-SdkKey` header is missing.
* 404: The `X-ConfigCat-SdkKey` header is pointing to a non-existent SDK.

**Example**:

example.js

```js
const url = "http://localhost:8050/api/eval-all"; // Proxy API URL

const data = {
  user: { // User Object for evaluation
    Identifier: "#UNIQUE-USER-IDENTIFIER#"
  }
};

const requestOptions = {
  method: "POST",
  headers: {
    "X-ConfigCat-SdkKey": "#YOUR-SDK-KEY#",
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
};

try {
  const response = await fetch(url, requestOptions);
  const responseData = await response.json();
  console.log(responseData);
} catch (error) {
  console.error("Error:", error)
}

```

POSTOPTIONS/api/refresh

This endpoint commands the underlying SDK to download the latest available *config JSON*.

**Headers**:

* `X-ConfigCat-SdkKey`: The SDK key that identifies an SDK within the Proxy.

**Responses**:

* 200: The refresh was successful.
* 204: In response to an `OPTIONS` request.
* 400: The `X-ConfigCat-SdkKey` header is missing.
* 404: The `X-ConfigCat-SdkKey` header is pointing to a non-existent SDK.

GETOPTIONS/api/keys

This endpoint returns all feature flag keys belonging to the given SDK key.

**Headers**:

* `X-ConfigCat-SdkKey`: The SDK key that identifies an SDK within the Proxy.

**Responses**:

* 200: The keys are returned successfully.
* Response body:
  ```json
  {
    "keys": [
      "feature-flag-key-1",
      "feature-flag-key-2"
    ]
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `X-ConfigCat-SdkKey` header is missing.
* 404: The `X-ConfigCat-SdkKey` header is pointing to a non-existent SDK.

### Endpoints using SDK identifier[​](#endpoints-using-sdk-identifier "Direct link to Endpoints using SDK identifier")

The following endpoints are using an [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) to determine which config / environment is the target of the desired action. The SDK identifier must be provided as a route parameter of the HTTP request.

POSTOPTIONS/api/{sdkId}/eval

This endpoint evaluates a single feature flag identified by a `key` with the given [User Object](https://configcat.com/docs/targeting/user-object.md).

**Route parameters**:

* `sdkId`: The [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that determines the feature flag's config / environment.

**Request body**:

```json
{
  "key": "<feature-flag-key>",
  "user": {
    "Identifier": "<user-id>",
    "Rating": 4.5,
    "Roles": ["Role1","Role2"],
    // any other attribute
  }
}

```

The type of the `user` object's fields can only be `string`, `number`, or `string[]`.

**Responses**:

* 200: The feature flag evaluation finished successfully.
* Response body:
  ```json
  {
    "value": <evaluated-value>,
    "variationId": "<variation-id>"
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `sdkId` or the `key` from the request body is missing.
* 404: The `sdkId` is pointing to a non-existent SDK.

**Example**:

example.js

```js
const url = "http://localhost:8050/api/#SDK-IDENTIFIER#/eval"; // Proxy API URL with SDK identifier

const data = {
  key: "isMyAwesomeFeatureEnabled", // Feature flag key
  user: { // User Object for evaluation
    Identifier: "#UNIQUE-USER-IDENTIFIER#"
  }
};

const requestOptions = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
};

try {
  const response = await fetch(url, requestOptions);
  const responseData = await response.json();
  console.log(responseData); // {"value":<evaluated-value>,"variationId":"<variation-id>"}
} catch (error) {
  console.error("Error:", error)
}

```

POSTOPTIONS/api/{sdkId}/eval-all

This endpoint evaluates all feature flags with the given [User Object](https://configcat.com/docs/targeting/user-object.md).

**Route parameters**:

* `sdkId`: The [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that determines which config's feature flags should be evaluated in which environment.

**Request body**:

```json
{
  "user": {
    "Identifier": "<user-id>",
    "Rating": 4.5,
    "Roles": ["Role1","Role2"],
    // any other attribute
  }
}

```

The type of the `user` object's fields can only be `string`, `number`, or `string[]`.

**Responses**:

* 200: The evaluation of all feature flags finished successfully.
* Response body:
  ```json
  {
    "feature-flag-key-1": {
      "value": <evaluated-value>,
      "variationId": "<variation-id>"
    },
    "feature-flag-key-2": {
      "value": <evaluated-value>,
      "variationId": "<variation-id>"
    }
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `sdkId` is missing.
* 404: The `sdkId` is pointing to a non-existent SDK.

**Example**:

example.js

```js
const url = "http://localhost:8050/api/#SDK-IDENTIFIER#/eval-all"; // Proxy API URL with SDK identifier

const data = {
  user: { // User Object for evaluation
    Identifier: "#UNIQUE-USER-IDENTIFIER#"
  }
};

const requestOptions = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
};

try {
  const response = await fetch(url, requestOptions);
  const responseData = await response.json();
  console.log(responseData);
} catch (error) {
  console.error("Error:", error)
}

```

POSTOPTIONS/api/{sdkId}/refresh

This endpoint commands the underlying SDK to download the latest available *config JSON*.

**Route parameters**:

* `sdkId`: The [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that uniquely identifies an SDK within the Proxy.

**Responses**:

* 200: The refresh was successful.
* 204: In response to an `OPTIONS` request.
* 400: The `sdkId` is missing.
* 404: The `sdkId` is pointing to a non-existent SDK.

GETOPTIONS/api/{sdkId}/keys

This endpoint returns all feature flag keys belonging to the given [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key).

**Route parameters**:

* `sdkId`: The [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that uniquely identifies an SDK within the Proxy.

**Responses**:

* 200: The keys are returned successfully.
* Response body:
  ```json
  {
    "keys": [
      "feature-flag-key-1",
      "feature-flag-key-2"
    ]
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `sdkId` is missing.
* 404: The `sdkId` is pointing to a non-existent SDK.

### Available Options[​](#available-options-1 "Direct link to Available Options")

The following API related options are available:

| Option                                                                                                                                                                                                                                                                                                                 | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - YAML<br />- Environment variable```yaml
http:
  api:
    enabled: <true|false>

``````shell
CONFIGCAT_HTTP_API_ENABLED=<true|false>

```                                                                                                                                                                                     | `true`  | Turns the hosting of the API endpoints on/off. These endpoints can be used for server side feature flag evaluation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - YAML<br />- Environment variable```yaml
http:
  api:
    cors:
      enabled: <true|false>

``````shell
CONFIGCAT_HTTP_API_CORS_ENABLED=<true|false>

```                                                                                                                                                                     | `true`  | Turns the sending of CORS headers on/off. It can be used to restrict access to specific domains. By default, the Proxy allows each origin by setting the `Access-Control-Allow-Origin` response header to the request's origin. You can override this functionality by restricting the allowed origins with the `allowed_origins` or `allowed_origins_regex` options.                                                                                                                                                                                                                                                                                             |
| - YAML<br />- Environment variable```yaml
http:
  api:
    cors:
      allowed_origins: 
        - https://domain1.com
        - https://domain2.com

``````shell
CONFIGCAT_HTTP_API_CORS_ALLOWED_ORIGINS='["https://domain1.com","https://domain2.com"]'

```                                                                    | -       | List of allowed CORS origins. When it's set, the Proxy will include only that origin in the `Access-Control-Allow-Origin` response header which matches the request's `Origin`.<br />When there's no matching request origin and the `allowed_origins_regex` option is not set, the Proxy will set the `Access-Control-Allow-Origin` response header to the first item in the allowed origins list.                                                                                                                                                                                                                                                               |
| - YAML<br />- Environment variable```yaml
http:
  api:
    cors:
      allowed_origins_regex:
        patterns:
          - https:\/\/.*domain1\.com
          - https:\/\/.*domain2\.com

``````shell
CONFIGCAT_HTTP_API_CORS_ALLOWED_ORIGINS_REGEX_PATTERNS='["https:\\/\\/.*domain1\\.com","https:\\/\\/.*domain2\\.com"]'

``` | -       | List of regex patterns used to match allowed CORS origins. When it's set, the Proxy will match the request's `Origin` with the given regex patterns. When there's a match, the `Access-Control-Allow-Origin` response header will be set to the matched origin.<br />When there's no matching request origin, the Proxy will set the `Access-Control-Allow-Origin` response header to the `if_no_match` field's value.<br />The `if_no_match` option is mandatory if this option is used.<br />When using the environment variable, the regex escape character must be doubled (`\\`) because it's parsed as a JSON list and `\` is also a JSON escape character. |
| - YAML<br />- Environment variable```yaml
http:
  api:
    cors:
      allowed_origins_regex:
        if_no_match: https://domain1.com

``````shell
CONFIGCAT_HTTP_API_CORS_ALLOWED_ORIGINS_REGEX_IF_NO_MATCH="https://domain1.com"

```                                                                                         | -       | Required when the previous `patterns` option is set. It's value is used in the `Access-Control-Allow-Origin` header when an incoming request's `Origin` doesn't match with any previously configured regex patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - YAML<br />- Environment variable```yaml
http:
  api:
    headers:
      Custom-Header-Name: "<header-value>"

``````shell
CONFIGCAT_HTTP_API_HEADERS='{"Custom-Header-Name":"<header-value>"}'

```                                                                                                                           | -       | Additional headers that must be sent back on each API endpoint response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - YAML<br />- Environment variable```yaml
http:
  api:
    auth_headers:
      X-API-KEY: "<auth-value>"

``````shell
CONFIGCAT_HTTP_API_AUTH_HEADERS='{"X-API-KEY":"<auth-value>"}'

```                                                                                                                                       | -       | Additional headers that must be on each request sent to the API endpoints. If the request doesn't include the specified header, or the values are not matching, the Proxy will respond with a `401` HTTP status code.                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## OpenFeature Remote Evaluation Protocol (OFREP)[​](#openfeature-remote-evaluation-protocol-ofrep "Direct link to OpenFeature Remote Evaluation Protocol (OFREP)")

info

OFREP compatibility is only available from Proxy version [`v2.0.0`](https://github.com/configcat/configcat-proxy/releases/tag/v2.0.0).

The Proxy conforms to the [OpenFeature Remote Evaluation Protocol](https://github.com/open-feature/protocol), which means it can be used with OFREP compatible OpenFeature providers.

### Endpoints using SDK key[​](#endpoints-using-sdk-key-1 "Direct link to Endpoints using SDK key")

The following endpoints are using SDK keys to determine which config / environment is the target of the desired action. The SDK key must be provided in the `X-ConfigCat-SdkKey` HTTP header.

info

These endpoints are only available from Proxy version [`v3.0.0`](https://github.com/configcat/configcat-proxy/releases/tag/v3.0.0).

POSTOPTIONS/ofrep/v1/evaluate/flags/{key}

This endpoint is used by OFREP compatible OpenFeature providers to evaluate a feature flag.

**Route parameters**:

* `key`: The key of the feature flag to evaluate.

**Headers**:

* `X-ConfigCat-SdkKey`: The SDK key that determines the feature flag's config / environment.

**Request body**:

```json
{
  "context": {
    "targetingKey": "<user-id>",
    "Rating": 4.5,
    "Roles": ["Role1","Role2"],
  }
}

```

**Responses**:

* 200: The feature flag evaluation finished successfully.
* Response body:
  ```json
  {
    "key": "<flag-key>",
    "value": <evaluated-value>,
    "variant": "<variation-id>",
    "reason": "<reason>"
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `X-ConfigCat-SdkKey` header is missing.
* 404: The `X-ConfigCat-SdkKey` header is pointing to a non-existent SDK or the feature flag for `key` is not found.

**Example**:

example.js

```js
import { OpenFeature } from "@openfeature/web-sdk";
import { OFREPWebProvider } from '@openfeature/ofrep-web-provider';

OpenFeature.setProvider(
  new OFREPWebProvider({
    baseUrl: "http://localhost:8050", // Proxy URL
    headers: [
      ["X-ConfigCat-SdkKey", "#YOUR-SDK-KEY#"],
    ],
  }),
);

```

POSTOPTIONS/ofrep/v1/evaluate/flags

This endpoint is used by OFREP compatible OpenFeature providers to evaluate all feature flags.

**Headers**:

* `X-ConfigCat-SdkKey`: The SDK key that determines which config's feature flags should be evaluated in which environment.

**Request body**:

```json
{
  "context": {
    "targetingKey": "<user-id>",
    "Rating": 4.5,
    "Roles": ["Role1","Role2"],
  }
}

```

**Responses**:

* 200: The evaluation of all feature flags finished successfully.
* Response body:
  ```json
  {
    "flags": [
      {
        "key": "<flag1-key>",
        "value": <evaluated-value>,
        "variant": "<variation-id>",
        "reason": "<reason>"
      },
      {
        "key": "<flag2-key>",
        "value": <evaluated-value>,
        "variant": "<variation-id>",
        "reason": "<reason>"
      }
    ]
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `X-ConfigCat-SdkKey` header is missing.
* 404: The `X-ConfigCat-SdkKey` header is pointing to a non-existent SDK.

**Example**:

example.js

```js
import { OpenFeature } from "@openfeature/web-sdk";
import { OFREPWebProvider } from '@openfeature/ofrep-web-provider';

OpenFeature.setProvider(
  new OFREPWebProvider({
    baseUrl: "http://localhost:8050", // Proxy URL
    headers: [
      ["X-ConfigCat-SdkKey", "#YOUR-SDK-KEY#"],
    ],
  }),
);

```

### Endpoints using SDK identifier[​](#endpoints-using-sdk-identifier-1 "Direct link to Endpoints using SDK identifier")

The following endpoints are using an [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) to determine which config / environment is the target of the desired action. The SDK identifier must be provided in the `X-ConfigCat-SdkId` HTTP header.

POSTOPTIONS/ofrep/v1/evaluate/flags/{key}

This endpoint is used by OFREP compatible OpenFeature providers to evaluate a feature flag.

**Route parameters**:

* `key`: The key of the feature flag to evaluate.

**Headers**:

* `X-ConfigCat-SdkId`: The [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that determines the feature flag's config / environment.

**Request body**:

```json
{
  "context": {
    "targetingKey": "<user-id>",
    "Rating": 4.5,
    "Roles": ["Role1","Role2"],
  }
}

```

**Responses**:

* 200: The feature flag evaluation finished successfully.
* Response body:
  ```json
  {
    "key": "<flag-key>",
    "value": <evaluated-value>,
    "variant": "<variation-id>",
    "reason": "<reason>"
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `X-ConfigCat-SdkId` header is missing.
* 404: The `X-ConfigCat-SdkId` header is pointing to a non-existent SDK or the feature flag for `key` is not found.

**Example**:

example.js

```js
import { OpenFeature } from "@openfeature/web-sdk";
import { OFREPWebProvider } from '@openfeature/ofrep-web-provider';

OpenFeature.setProvider(
  new OFREPWebProvider({
    baseUrl: "http://localhost:8050", // Proxy URL
    headers: [
      ["X-ConfigCat-SdkId", "#SDK-IDENTIFIER#"],
    ],
  }),
);

```

POSTOPTIONS/ofrep/v1/evaluate/flags

This endpoint is used by OFREP compatible OpenFeature providers to evaluate all feature flags.

**Headers**:

* `X-ConfigCat-SdkId`: The [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that determines which config's feature flags should be evaluated in which environment.

**Request body**:

```json
{
  "context": {
    "targetingKey": "<user-id>",
    "Rating": 4.5,
    "Roles": ["Role1","Role2"],
  }
}

```

**Responses**:

* 200: The evaluation of all feature flags finished successfully.
* Response body:
  ```json
  {
    "flags": [
      {
        "key": "<flag1-key>",
        "value": <evaluated-value>,
        "variant": "<variation-id>",
        "reason": "<reason>"
      },
      {
        "key": "<flag2-key>",
        "value": <evaluated-value>,
        "variant": "<variation-id>",
        "reason": "<reason>"
      }
    ]
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `X-ConfigCat-SdkId` header is missing.
* 404: The `X-ConfigCat-SdkId` header is pointing to a non-existent SDK.

**Example**:

example.js

```js
import { OpenFeature } from "@openfeature/web-sdk";
import { OFREPWebProvider } from '@openfeature/ofrep-web-provider';

OpenFeature.setProvider(
  new OFREPWebProvider({
    baseUrl: 'http://localhost:8050', // Proxy URL
    headers: [
      ["X-ConfigCat-SdkId", "#SDK-IDENTIFIER#"],
    ],
  }),
);

```

### Available Options[​](#available-options-2 "Direct link to Available Options")

The following OFREP related options are available:

| Option                                                                                                                                                                                                                                                                                                                     | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - YAML<br />- Environment variable```yaml
http:
  ofrep:
    enabled: <true|false>

``````shell
CONFIGCAT_HTTP_OFREP_ENABLED=<true|false>

```                                                                                                                                                                                     | `true`  | Turns the hosting of the OFREP endpoints on/off. These endpoints can be used by OFREP compatible OpenFeature providers for server side feature flag evaluation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - YAML<br />- Environment variable```yaml
http:
  ofrep:
    cors:
      enabled: <true|false>

``````shell
CONFIGCAT_HTTP_OFREP_CORS_ENABLED=<true|false>

```                                                                                                                                                                     | `true`  | Turns the sending of CORS headers on/off. It can be used to restrict access to specific domains. By default, the Proxy allows each origin by setting the `Access-Control-Allow-Origin` response header to the request's origin. You can override this functionality by restricting the allowed origins with the `allowed_origins` or `allowed_origins_regex` options.                                                                                                                                                                                                                                                                                             |
| - YAML<br />- Environment variable```yaml
http:
  ofrep:
    cors:
      allowed_origins: 
        - https://domain1.com
        - https://domain2.com

``````shell
CONFIGCAT_HTTP_OFREP_CORS_ALLOWED_ORIGINS='["https://domain1.com","https://domain2.com"]'

```                                                                    | -       | List of allowed CORS origins. When it's set, the Proxy will include only that origin in the `Access-Control-Allow-Origin` response header which matches the request's `Origin`.<br />When there's no matching request origin and the `allowed_origins_regex` option is not set, the Proxy will set the `Access-Control-Allow-Origin` response header to the first item in the allowed origins list.                                                                                                                                                                                                                                                               |
| - YAML<br />- Environment variable```yaml
http:
  ofrep:
    cors:
      allowed_origins_regex:
        patterns:
          - https:\/\/.*domain1\.com
          - https:\/\/.*domain2\.com

``````shell
CONFIGCAT_HTTP_OFREP_CORS_ALLOWED_ORIGINS_REGEX_PATTERNS='["https:\\/\\/.*domain1\\.com","https:\\/\\/.*domain2\\.com"]'

``` | -       | List of regex patterns used to match allowed CORS origins. When it's set, the Proxy will match the request's `Origin` with the given regex patterns. When there's a match, the `Access-Control-Allow-Origin` response header will be set to the matched origin.<br />When there's no matching request origin, the Proxy will set the `Access-Control-Allow-Origin` response header to the `if_no_match` field's value.<br />The `if_no_match` option is mandatory if this option is used.<br />When using the environment variable, the regex escape character must be doubled (`\\`) because it's parsed as a JSON list and `\` is also a JSON escape character. |
| - YAML<br />- Environment variable```yaml
http:
  ofrep:
    cors:
      allowed_origins_regex:
        if_no_match: https://domain1.com

``````shell
CONFIGCAT_HTTP_OFREP_CORS_ALLOWED_ORIGINS_REGEX_IF_NO_MATCH="https://domain1.com"

```                                                                                         | -       | Required when the previous `patterns` option is set. It's value is used in the `Access-Control-Allow-Origin` header when an incoming request's `Origin` doesn't match with any previously configured regex patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - YAML<br />- Environment variable```yaml
http:
  ofrep:
    headers:
      Custom-Header-Name: "<header-value>"

``````shell
CONFIGCAT_HTTP_OFREP_HEADERS='{"Custom-Header-Name":"<header-value>"}'

```                                                                                                                           | -       | Additional headers that must be sent back on each OFREP endpoint response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - YAML<br />- Environment variable```yaml
http:
  ofrep:
    auth_headers:
      X-API-KEY: "<auth-value>"

``````shell
CONFIGCAT_HTTP_OFREP_AUTH_HEADERS='{"X-API-KEY":"<auth-value>"}'

```                                                                                                                                       | -       | Additional headers that must be on each request sent to the OFREP endpoints. If the request doesn't include the specified header, or the values are not matching, the Proxy will respond with a `401` HTTP status code.                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## SSE[​](#sse "Direct link to SSE")

The SSE endpoint allows you to subscribe for feature flag value changes through [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) connections.

### Endpoints using SDK key[​](#endpoints-using-sdk-key-2 "Direct link to Endpoints using SDK key")

The following endpoints are using SDK keys to determine which config / environment is the target of the desired action. The SDK key must be provided in the `sdkKey` field of the base64 encoded `data` route parameter.

info

These endpoints are only available from Proxy version [`v3.0.0`](https://github.com/configcat/configcat-proxy/releases/tag/v3.0.0).

GETOPTIONS/sse/eval/k/{data}

This endpoint subscribes to a single flag's changes. Whenever the watched flag's value changes, the Proxy sends the new value to each connected client.

**Route parameters**:

* `data`: The `base64` encoded input data for feature flag evaluation that must contain the SDK key, the feature flag's key, and a [User Object](https://configcat.com/docs/targeting/user-object.md).

**Responses**:

* 200: The SSE connection established successfully.
* Response body:
  ```json
  {
    "value": <evaluated-value>,
    "variationId": "<variation-id>"
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `data`, or the `sdkKey` or `key` field of `data` is missing.
* 404: The `sdkKey` is pointing to a non-existent SDK.

**Example**:

example.js

```js
const rawData = {
  sdkKey: "#YOUR-SDK-KEY#",
  key: "isMyAwesomeFeatureEnabled",
  user: { // field types can only be `string`, `number`, or `string[]`.
    Identifier: "#UNIQUE-USER-IDENTIFIER#",
    Rating: 4.5,
    Roles: ["Role1","Role2"],
    // any other attribute
  }
};

const data = btoa(JSON.stringify(rawData));
const evtSource = new EventSource("http://localhost:8050/sse/eval/k/" + data);
evtSource.onmessage = (event) => {
  console.log(event.data); // {"value":<evaluated-value>,"variationId":"<variation-id>"}
};

```

GETOPTIONS/sse/eval-all/k/{data}

This endpoint subscribes to all feature flags' changes behind the given SDK key. When any of the watched flags' value change, the Proxy sends its new value to each connected client.

**Route parameters**:

* `data`: The `base64` encoded input data for feature flag evaluation that contains the SDK key and a [User Object](https://configcat.com/docs/targeting/user-object.md).

**Responses**:

* 200: The SSE connection established successfully.
* Response body:
  ```json
  {
    "feature-flag-key-1": {
      "value": <evaluated-value>,
      "variationId": "<variation-id>"
    },
    "feature-flag-key-2": {
      "value": <evaluated-value>,
      "variationId": "<variation-id>"
    }
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `sdkKey` field of `data` is missing.
* 404: The `sdkKey` is pointing to a non-existent SDK.

**Example**:

example.js

```js
const rawData = {
  sdkKey: "#YOUR-SDK-KEY#",
  user: { // field types can only be `string`, `number`, or `string[]`.
    Identifier: "#UNIQUE-USER-IDENTIFIER#",
    Rating: 4.5,
    Roles: ["Role1","Role2"],
    // any other attribute
  }
};

const data = btoa(JSON.stringify(rawData));
const evtSource = new EventSource("http://localhost:8050/sse/eval-all/k/" + data);
evtSource.onmessage = (event) => {
  console.log(event.data); // {"feature-flag-key":{"value":<evaluated-value>,"variationId":"<variation-id>"}}
};

```

### Endpoints using SDK identifier[​](#endpoints-using-sdk-identifier-2 "Direct link to Endpoints using SDK identifier")

The following endpoints are using an SDK identifier to determine which config / environment is the target of the desired action. The SDK identifier must be provided in the `sdkId` route parameter.

GETOPTIONS/sse/{sdkId}/eval/{data}

This endpoint subscribes to a single flag's changes. Whenever the watched flag's value changes, the Proxy sends the new value to each connected client.

**Route parameters**:

* `sdkId`: The [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that uniquely identifies an SDK within the Proxy.
* `data`: The `base64` encoded input data for feature flag evaluation that must contain the feature flag's key and a [User Object](https://configcat.com/docs/targeting/user-object.md).

**Responses**:

* 200: The SSE connection established successfully.
* Response body:
  ```json
  {
    "value": <evaluated-value>,
    "variationId": "<variation-id>"
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `sdkId`, `data`, or the `key` attribute of `data` is missing.
* 404: The `sdkId` is pointing to a non-existent SDK.

**Example**:

example.js

```js
const rawData = {
  key: "isMyAwesomeFeatureEnabled",
  user: { // field types can only be `string`, `number`, or `string[]`.
    Identifier: "#UNIQUE-USER-IDENTIFIER#",
    Rating: 4.5,
    Roles: ["Role1","Role2"],
    // any other attribute
  }
};

const data = btoa(JSON.stringify(rawData));
const evtSource = new EventSource("http://localhost:8050/sse/#SDK-IDENTIFIER#/eval/" + data);
evtSource.onmessage = (event) => {
  console.log(event.data); // {"value":<evaluated-value>,"variationId":"<variation-id>"}
};

```

GETOPTIONS/sse/{sdkId}/eval-all/{data}

This endpoint subscribes to all feature flags' changes behind the given [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key). When any of the watched flags' value change, the Proxy sends its new value to each connected client.

**Route parameters**:

* `sdkId`: The [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that uniquely identifies an SDK within the Proxy.
* `data`: **Optional**. The `base64` encoded input data for feature flag evaluation that contains a [User Object](https://configcat.com/docs/targeting/user-object.md).

**Responses**:

* 200: The SSE connection established successfully.
* Response body:
  ```json
  {
    "feature-flag-key-1": {
      "value": <evaluated-value>,
      "variationId": "<variation-id>"
    },
    "feature-flag-key-2": {
      "value": <evaluated-value>,
      "variationId": "<variation-id>"
    }
  }

  ```
  204: In response to an `OPTIONS` request.
* 400: The `sdkId` is missing.
* 404: The `sdkId` is pointing to a non-existent SDK.

**Example**:

example.js

```js
const rawData = {
  user: { // field types can only be `string`, `number`, or `string[]`.
    Identifier: "#UNIQUE-USER-IDENTIFIER#",
    Rating: 4.5,
    Roles: ["Role1","Role2"],
    // any other attribute
  }
};

const data = btoa(JSON.stringify(rawData));
const evtSource = new EventSource("http://localhost:8050/sse/#SDK-IDENTIFIER#/eval-all/" + data);
evtSource.onmessage = (event) => {
  console.log(event.data); // {"feature-flag-key":{"value":<evaluated-value>,"variationId":"<variation-id>"}}
};

```

### Available Options[​](#available-options-3 "Direct link to Available Options")

The following SSE related options are available:

| Option                                                                                                                                                                                                                                                                                                                 | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - YAML<br />- Environment variable```yaml
http:
  sse:
    enabled: <true|false>

``````shell
CONFIGCAT_HTTP_SSE_ENABLED=<true|false>

```                                                                                                                                                                                     | `true`  | Turns the hosting of the SSE endpoint on/off, This endpoint can be used to stream feature flag value changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - YAML<br />- Environment variable```yaml
http:
  sse:
    cors:
      enabled: <true|false>

``````shell
CONFIGCAT_HTTP_SSE_CORS_ENABLED=<true|false>

```                                                                                                                                                                     | `true`  | Turns the sending of CORS headers on/off. It can be used to restrict access to specific domains. By default, the Proxy allows each origin by setting the `Access-Control-Allow-Origin` response header to the request's origin. You can override this functionality by restricting the allowed origins with the `allowed_origins` or `allowed_origins_regex` options.                                                                                                                                                                                                                                                                                             |
| - YAML<br />- Environment variable```yaml
http:
  sse:
    cors:
      allowed_origins: 
        - https://domain1.com
        - https://domain2.com

``````shell
CONFIGCAT_HTTP_SSE_CORS_ALLOWED_ORIGINS='["https://domain1.com","https://domain2.com"]'

```                                                                    | -       | List of allowed CORS origins. When it's set, the Proxy will include only that origin in the `Access-Control-Allow-Origin` response header which matches the request's `Origin`.<br />When there's no matching request origin and the `allowed_origins_regex` option is not set, the Proxy will set the `Access-Control-Allow-Origin` response header to the first item in the allowed origins list.                                                                                                                                                                                                                                                               |
| - YAML<br />- Environment variable```yaml
http:
  sse:
    cors:
      allowed_origins_regex:
        patterns:
          - https:\/\/.*domain1\.com
          - https:\/\/.*domain2\.com

``````shell
CONFIGCAT_HTTP_SSE_CORS_ALLOWED_ORIGINS_REGEX_PATTERNS='["https:\\/\\/.*domain1\\.com","https:\\/\\/.*domain2\\.com"]'

``` | -       | List of regex patterns used to match allowed CORS origins. When it's set, the Proxy will match the request's `Origin` with the given regex patterns. When there's a match, the `Access-Control-Allow-Origin` response header will be set to the matched origin.<br />When there's no matching request origin, the Proxy will set the `Access-Control-Allow-Origin` response header to the `if_no_match` field's value.<br />The `if_no_match` option is mandatory if this option is used.<br />When using the environment variable, the regex escape character must be doubled (`\\`) because it's parsed as a JSON list and `\` is also a JSON escape character. |
| - YAML<br />- Environment variable```yaml
http:
  sse:
    cors:
      allowed_origins_regex:
        if_no_match: https://domain1.com

``````shell
CONFIGCAT_HTTP_SSE_CORS_ALLOWED_ORIGINS_REGEX_IF_NO_MATCH="https://domain1.com"

```                                                                                         | -       | Required when the previous `patterns` option is set. It's value is used in the `Access-Control-Allow-Origin` header when an incoming request's `Origin` doesn't match with any previously configured regex patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - YAML<br />- Environment variable```yaml
http:
  sse:
    headers:
      Custom-Header-Name: "<header-value>"

``````shell
CONFIGCAT_HTTP_SSE_HEADERS='{"Custom-Header-Name":"<header-value>"}'

```                                                                                                                           | -       | Additional headers that must be sent back on each [SSE endpoint](#sse) response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - YAML<br />- Environment variable```yaml
http:
  sse:
    log:
      level: "<error|warn|info|debug>"

``````shell
CONFIGCAT_HTTP_SSE_LOG_LEVEL="<error|warn|info|debug>"

```                                                                                                                                                 | `warn`  | The verbosity of the SSE related logs.<br />Possible values: `error`, `warn`, `info` or `debug`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Webhook[​](#webhook "Direct link to Webhook")

Through the webhook endpoint, you can notify the Proxy about the availability of new feature flag evaluation data. Also, with the appropriate [SDK options](https://configcat.com/docs/advanced/proxy/proxy-overview.md#additional-options-for-underlying-sdks), the Proxy can [validate the signature](https://configcat.com/docs/advanced/notifications-webhooks.md#verifying-webhook-requests) of each incoming webhook request.

info

If you use the [automatic configuration with Proxy profiles](https://configcat.com/docs/advanced/proxy/proxy-overview.md#1-automatic-configuration-with-proxy-profiles), you don't have to set up individual webhooks manually. You can follow the documentation of webhook notifications for Proxy profiles [here](https://configcat.com/docs/advanced/proxy/proxy-overview.md#webhook-notification).

GETPOST/hook/{sdkId}

Notifies the Proxy that the SDK with the given [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) must refresh its *config JSON* to the latest version.

**Route parameters**:

* `sdkId`: The [SDK identifier](https://configcat.com/docs/advanced/proxy/proxy-overview.md#sdk-identifier--sdk-key) that uniquely identifies an SDK within the Proxy.

**Responses**:

* 200: The Proxy accepted the notification.
* 400: The `sdkId` is missing or the [webhook signature validation](https://configcat.com/docs/advanced/notifications-webhooks.md#verifying-webhook-requests) failed.
* 404: The `sdkId` is pointing to a non-existent SDK.

### ConfigCat Dashboard[​](#configcat-dashboard "Direct link to ConfigCat Dashboard")

You can set up webhooks to invoke the Proxy on the [Webhooks page](https://app.configcat.com/product/webhooks) of the ConfigCat Dashboard.

![Webhook](/docs/assets/proxy/webhook.png)

### Available Options[​](#available-options-4 "Direct link to Available Options")

The following webhook related options are available:

| Option                                                                                                                                                                                   | Default | Description                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - YAML<br />- Environment variable```yaml
http:
  webhook:
    enabled: <true|false>

``````shell
CONFIGCAT_HTTP_WEBHOOK_ENABLED=<true|false>

```                                               | `true`  | Turns the hosting of the Webhook endpoint on/off. This endpoint can be used to notify the Proxy about the availability of new feature flag evaluation data.                                                      |
| - YAML<br />- Environment variable```yaml
http:
  webhook:
    auth:
      user: "<auth-user>"

``````shell
CONFIGCAT_HTTP_WEBHOOK_AUTH_USER="<auth-user>"

```                                   | -       | Basic authentication user. The basic authentication webhook header can be set on the [Webhooks page](https://app.configcat.com/product/webhooks) of the ConfigCat Dashboard.                                     |
| - YAML<br />- Environment variable```yaml
http:
  webhook:
    auth:
      password: "<auth-pass>"

``````shell
CONFIGCAT_HTTP_WEBHOOK_AUTH_PASSWORD="<auth-pass>"

```                           | -       | Basic authentication password. The basic authentication webhook header can be set on the [Webhooks page](https://app.configcat.com/product/webhooks) of the ConfigCat Dashboard.                                 |
| - YAML<br />- Environment variable```yaml
http:
  webhook:
    auth_headers:
      X-API-KEY: "<auth-value>"

``````shell
CONFIGCAT_HTTP_WEBHOOK_AUTH_HEADERS='{"X-API-KEY":"<auth-value>"}'

``` | -       | Additional headers that ConfigCat must send with each request to the Webhook endpoint. Webhook headers can be set on the [Webhooks page](https://app.configcat.com/product/webhooks) of the ConfigCat Dashboard. |
