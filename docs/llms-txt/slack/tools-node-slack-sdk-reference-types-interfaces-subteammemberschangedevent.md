Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/SubteamMembersChangedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / SubteamMembersChangedEvent

# Interface: SubteamMembersChangedEvent

Defined in: [events/subteam.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L37)

## Properties {#properties}

### added_users? {#added_users}

```
optional added_users: string[];
```

Defined in: [events/subteam.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L43)

* * *

### added_users_count? {#added_users_count}

```
optional added_users_count: number;
```

Defined in: [events/subteam.ts:44](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L44)

* * *

### date_previous_update {#date_previous_update}

```
date_previous_update: number;
```

Defined in: [events/subteam.ts:41](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L41)

* * *

### date_update {#date_update}

```
date_update: number;
```

Defined in: [events/subteam.ts:42](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L42)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/subteam.ts:47](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L47)

* * *

### removed_users? {#removed_users}

```
optional removed_users: string[];
```

Defined in: [events/subteam.ts:45](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L45)

* * *

### removed_users_count? {#removed_users_count}

```
optional removed_users_count: number;
```

Defined in: [events/subteam.ts:46](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L46)

* * *

### subteam_id {#subteam_id}

```
subteam_id: string;
```

Defined in: [events/subteam.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L39)

* * *

### team_id {#team_id}

```
team_id: string;
```

Defined in: [events/subteam.ts:40](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L40)

* * *

### type {#type}

```
type: "subteam_members_changed";
```

Defined in: [events/subteam.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/subteam.ts#L38)
