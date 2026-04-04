Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SubteamMembersChangedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SubteamMembersChangedEvent

# Interface: SubteamMembersChangedEvent

Defined in: packages/types/dist/events/subteam.d.ts:34

## Properties {#properties}

### added_users? {#added_users}

```text
optional added_users: string[];
```text

Defined in: packages/types/dist/events/subteam.d.ts:40

* * *

### added_users_count? {#added_users_count}

```text
optional added_users_count: number;
```text

Defined in: packages/types/dist/events/subteam.d.ts:41

* * *

### date_previous_update {#date_previous_update}

```text
date_previous_update: number;
```text

Defined in: packages/types/dist/events/subteam.d.ts:38

* * *

### date_update {#date_update}

```text
date_update: number;
```text

Defined in: packages/types/dist/events/subteam.d.ts:39

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/subteam.d.ts:44

* * *

### removed_users? {#removed_users}

```text
optional removed_users: string[];
```text

Defined in: packages/types/dist/events/subteam.d.ts:42

* * *

### removed_users_count? {#removed_users_count}

```text
optional removed_users_count: number;
```text

Defined in: packages/types/dist/events/subteam.d.ts:43

* * *

### subteam_id {#subteam_id}

```text
subteam_id: string;
```text

Defined in: packages/types/dist/events/subteam.d.ts:36

* * *

### team_id {#team_id}

```text
team_id: string;
```text

Defined in: packages/types/dist/events/subteam.d.ts:37

* * *

### type {#type}

```text
type: "subteam_members_changed";
```text

Defined in: packages/types/dist/events/subteam.d.ts:35
