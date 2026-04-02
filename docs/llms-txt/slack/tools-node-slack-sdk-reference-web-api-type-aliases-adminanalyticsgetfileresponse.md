Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminAnalyticsGetFileResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminAnalyticsGetFileResponse

# Type Alias: AdminAnalyticsGetFileResponse

```text
type AdminAnalyticsGetFileResponse = WebAPICallResult & object;
```text

Defined in: [packages/web-api/src/types/response/AdminAnalyticsGetFileResponse.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminAnalyticsGetFileResponse.ts#L4)

## Type Declaration {#type-declaration}

### error? {#error}

```text
optional error: string;
```text

### file_data? {#file_data}

```text
optional file_data: (  | AdminAnalyticsMemberDetails  | AdminAnalyticsPublicChannelDetails  | AdminAnalyticsPublicChannelMetadataDetails)[];
```text

### needed? {#needed}

```text
optional needed: string;
```text

### ok? {#ok}

```text
optional ok: boolean;
```text

### provided? {#provided}

```text
optional provided: string;
```text

### response_metadata? {#response_metadata}

```text
optional response_metadata: ResponseMetadata;
```text
