Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationsAcceptSharedInviteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsAcceptSharedInviteArguments

# Type Alias: ConversationsAcceptSharedInviteArguments

```typescript
type ConversationsAcceptSharedInviteArguments = TokenOverridable & OptionalTeamAssignable & ChannelID | InviteID & IsPrivate & object;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:52](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L52)

## Type Declaration {#type-declaration}

### channel_name {#channel_name}

```typescript
channel_name: string;
```

#### Description {#description}

Name of the channel. If the channel does not exist already in your workspace, this name is the one that the channel will take.

### free_trial_accepted? {#free_trial_accepted}

```typescript
optional free_trial_accepted: boolean;
```

#### Description {#description-1}

Whether you'd like to use your workspace's free trial to begin using Slack Connect.
