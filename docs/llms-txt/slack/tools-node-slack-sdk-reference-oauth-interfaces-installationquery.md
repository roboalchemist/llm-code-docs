Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/interfaces/InstallationQuery

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / InstallationQuery

# Interface: InstallationQuery<isEnterpriseInstall>

Defined in: [packages/oauth/src/installation-query.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-query.ts#L4)

## Type Parameters {#type-parameters}

### isEnterpriseInstall {#isenterpriseinstall}

`isEnterpriseInstall` _extends_ `boolean`

## Properties {#properties}

### conversationId? {#conversationid}

```text
optional conversationId: string;
```

Defined in: [packages/oauth/src/installation-query.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-query.ts#L8)

* * *

### enterpriseId {#enterpriseid}

```text
enterpriseId: isEnterpriseInstall extends true ? string : string | undefined;
```

Defined in: [packages/oauth/src/installation-query.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-query.ts#L6)

* * *

### isEnterpriseInstall {#isenterpriseinstall-1}

```text
isEnterpriseInstall: isEnterpriseInstall;
```

Defined in: [packages/oauth/src/installation-query.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-query.ts#L4)

* * *

### teamId {#teamid}

```text
teamId: isEnterpriseInstall extends false ? string : undefined;
```

Defined in: [packages/oauth/src/installation-query.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-query.ts#L5)

* * *

### userId? {#userid}

```text
optional userId: string;
```

Defined in: [packages/oauth/src/installation-query.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/installation-query.ts#L7)
