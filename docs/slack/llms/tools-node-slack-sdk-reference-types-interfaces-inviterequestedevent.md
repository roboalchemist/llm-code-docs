Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/InviteRequestedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / InviteRequestedEvent

# Interface: InviteRequestedEvent

Defined in: [events/invite.ts:1](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/invite.ts#L1)

## Properties {#properties}

### invite_request {#invite_request}

```
invite_request: object;
```

Defined in: [events/invite.ts:3](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/invite.ts#L3)

#### channel_ids {#channel_ids}

```
channel_ids: string[];
```

#### date_created {#date_created}

```
date_created: number;
```

#### date_expire {#date_expire}

```
date_expire: number;
```

#### email {#email}

```
email: string;
```

#### id {#id}

```
id: string;
```

#### invite_type {#invite_type}

```
invite_type: "restricted" | "ultra_restricted" | "full_member";
```

#### real_name {#real_name}

```
real_name: string;
```

#### request_reason {#request_reason}

```
request_reason: string;
```

#### requester_ids {#requester_ids}

```
requester_ids: string[];
```

#### team {#team}

```
team: object;
```

##### team.domain {#teamdomain}

```
domain: string;
```

##### team.id {#teamid}

```
id: string;
```

##### team.name {#teamname}

```
name: string;
```

* * *

### type {#type}

```
type: "invite_requested";
```

Defined in: [events/invite.ts:2](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/invite.ts#L2)
