Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/TokensRevokedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / TokensRevokedEvent

# Interface: TokensRevokedEvent

Defined in: [events/token.ts:1](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/token.ts#L1)

## Properties {#properties}

### tokens {#tokens}

```
tokens: object;
```

Defined in: [events/token.ts:3](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/token.ts#L3)

#### bot? {#bot}

```
optional bot: string[];
```

#### oauth? {#oauth}

```
optional oauth: string[];
```

* * *

### type {#type}

```
type: "tokens_revoked";
```

Defined in: [events/token.ts:2](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/token.ts#L2)
