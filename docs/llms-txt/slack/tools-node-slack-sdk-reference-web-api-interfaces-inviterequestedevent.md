Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/InviteRequestedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / InviteRequestedEvent

# Interface: InviteRequestedEvent

Defined in: packages/types/dist/events/invite.d.ts:1

## Properties {#properties}

### invite_request {#invite_request}

```text
invite_request: object;
```text

Defined in: packages/types/dist/events/invite.d.ts:3

#### channel_ids {#channel_ids}

```text
channel_ids: string[];
```text

#### date_created {#date_created}

```text
date_created: number;
```text

#### date_expire {#date_expire}

```text
date_expire: number;
```text

#### email {#email}

```text
email: string;
```text

#### id {#id}

```text
id: string;
```text

#### invite_type {#invite_type}

```text
invite_type: "restricted" | "ultra_restricted" | "full_member";
```text

#### real_name {#real_name}

```text
real_name: string;
```text

#### request_reason {#request_reason}

```text
request_reason: string;
```text

#### requester_ids {#requester_ids}

```text
requester_ids: string[];
```text

#### team {#team}

```text
team: object;
```text

##### team.domain {#teamdomain}

```text
domain: string;
```text

##### team.id {#teamid}

```text
id: string;
```text

##### team.name {#teamname}

```text
name: string;
```text

* * *

### type {#type}

```text
type: "invite_requested";
```text

Defined in: packages/types/dist/events/invite.d.ts:2
