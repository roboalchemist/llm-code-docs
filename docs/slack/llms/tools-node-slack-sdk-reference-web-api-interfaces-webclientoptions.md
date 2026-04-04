Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WebClientOptions

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WebClientOptions

# Interface: WebClientOptions

Defined in: [packages/web-api/src/WebClient.ts:79](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L79)

## Properties {#properties}

### adapter? {#adapter}

```text
optional adapter: AxiosAdapter;
```text

Defined in: [packages/web-api/src/WebClient.ts:126](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L126)

Custom functions for modifing and handling outgoing requests. Useful if you would like to manage outgoing request with a custom http client. See [Axios adapter documentation](https://github.com/axios/axios/blob/v1.x/README.md?plain=1#L586) for more information.

#### Default {#default}

```text
undefined
```text

* * *

### agent? {#agent}

```text
optional agent: Agent;
```text

Defined in: [packages/web-api/src/WebClient.ts:91](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L91)

* * *

### allowAbsoluteUrls? {#allowabsoluteurls}

```text
optional allowAbsoluteUrls: boolean;
```text

Defined in: [packages/web-api/src/WebClient.ts:105](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L105)

Determines if a dynamic method name being an absolute URL overrides the configured slackApiUrl. When set to false, the URL used in Slack API requests will always begin with the slackApiUrl.

See [https://docs.slack.dev/tools/node-slack-sdk/web-api/#call-a-method](https://docs.slack.dev/tools/node-slack-sdk/web-api/#call-a-method) for more details. See [https://github.com/axios/axios?tab=readme-ov-file#request-config](https://github.com/axios/axios?tab=readme-ov-file#request-config) for more details.

#### Default {#default-1}

```text
true
```text

* * *

### attachOriginalToWebAPIRequestError? {#attachoriginaltowebapirequesterror}

```text
optional attachOriginalToWebAPIRequestError: boolean;
```text

Defined in: [packages/web-api/src/WebClient.ts:112](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L112)

Indicates whether to attach the original error to a Web API request error. When set to true, the original error object will be attached to the Web API request error.

#### Default {#default-2}

```text
true
```text

* * *

### headers? {#headers}

```text
optional headers: Record<string, string>;
```text

Defined in: [packages/web-api/src/WebClient.ts:95](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L95)

* * *

### logger? {#logger}

```text
optional logger: Logger;
```text

Defined in: [packages/web-api/src/WebClient.ts:87](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L87)

* * *

### logLevel? {#loglevel}

```text
optional logLevel: LogLevel;
```text

Defined in: [packages/web-api/src/WebClient.ts:88](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L88)

* * *

### maxRequestConcurrency? {#maxrequestconcurrency}

```text
optional maxRequestConcurrency: number;
```text

Defined in: [packages/web-api/src/WebClient.ts:89](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L89)

* * *

### rejectRateLimitedCalls? {#rejectratelimitedcalls}

```text
optional rejectRateLimitedCalls: boolean;
```text

Defined in: [packages/web-api/src/WebClient.ts:94](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L94)

* * *

### requestInterceptor? {#requestinterceptor}

```text
optional requestInterceptor: RequestInterceptor;
```text

Defined in: [packages/web-api/src/WebClient.ts:118](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L118)

Custom function to modify outgoing requests. See [Axios interceptor documentation](https://axios-http.com/docs/interceptors) for more details.

#### Default {#default-3}

```text
undefined
```text

* * *

### retryConfig? {#retryconfig}

```text
optional retryConfig: RetryOptions;
```text

Defined in: [packages/web-api/src/WebClient.ts:90](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L90)

* * *

### slackApiUrl? {#slackapiurl}

```text
optional slackApiUrl: string;
```text

Defined in: [packages/web-api/src/WebClient.ts:86](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L86)

The base URL requests are sent to. Often unchanged, but might be set for testing techniques.

See [https://docs.slack.dev/tools/node-slack-sdk/web-api/#custom-api-url](https://docs.slack.dev/tools/node-slack-sdk/web-api/#custom-api-url) for more information.

#### Default {#default-4}

```text
https://slack.com/api/
```text

* * *

### teamId? {#teamid}

```text
optional teamId: string;
```text

Defined in: [packages/web-api/src/WebClient.ts:96](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L96)

* * *

### timeout? {#timeout}

```text
optional timeout: number;
```text

Defined in: [packages/web-api/src/WebClient.ts:93](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L93)

* * *

### tls? {#tls}

```text
optional tls: TLSOptions;
```text

Defined in: [packages/web-api/src/WebClient.ts:92](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L92)
