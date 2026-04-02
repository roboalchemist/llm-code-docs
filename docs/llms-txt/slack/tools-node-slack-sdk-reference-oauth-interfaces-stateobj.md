Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/interfaces/StateObj

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / StateObj

# Interface: StateObj

Defined in: [packages/oauth/src/state-stores/interface.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/interface.ts#L6)

The data structure represented by the state parameter.

## Properties {#properties}

### installOptions {#installoptions}

```text
installOptions: InstallURLOptions;
```

Defined in: [packages/oauth/src/state-stores/interface.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/interface.ts#L15)

The passed InstallURLOptions object when generating this state parameter.

* * *

### now {#now}

```text
now: Date;
```

Defined in: [packages/oauth/src/state-stores/interface.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/interface.ts#L10)

The timestamp that the state object was generated.

* * *

### random? {#random}

```text
optional random: string | number;
```

Defined in: [packages/oauth/src/state-stores/interface.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/state-stores/interface.ts#L16)
