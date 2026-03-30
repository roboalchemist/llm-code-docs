# Source: https://docs.knock.app/mapi-reference/channel_groups/schemas/channel_group_rule.md

### ChannelGroupRule

A rule that determines if a channel should be executed as part of a channel group.

#### Attributes

- **argument** (string) - For conditional rules, the value to compare against.
- **channel** (object) *required* - A configured channel, which is a way to route messages to a provider.
- **created_at** (string) *required* - The timestamp of when the rule was created.
- **index** (integer) *required* - The order index of this rule within the channel group.
- **operator** (string) - For conditional rules, the operator to apply.
- **rule_type** (string) *required* - The type of rule (if = conditional, unless = negative conditional, always = always apply).
- **updated_at** (string) *required* - The timestamp of when the rule was last updated.
- **variable** (string) - For conditional rules, the variable to evaluate.

#### Example

```json
{
  "channel": {
    "archived_at": null,
    "created_at": "2021-01-01T00:00:00Z",
    "custom_icon_url": null,
    "id": "01234567-89ab-cdef-0123-456789abcdef",
    "key": "my-sendgrid-channel",
    "name": "My Sendgrid Channel",
    "provider": "sendgrid",
    "type": "email",
    "updated_at": "2021-01-01T00:00:00Z"
  },
  "created_at": "2021-01-01T00:00:00Z",
  "index": 0,
  "rule_type": "always",
  "updated_at": "2021-01-01T00:00:00Z"
}
```

