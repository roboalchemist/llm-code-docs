# Source: https://docs.knock.app/api-reference/recipients/channel_data/schemas/ms_teams_channel_data.md

### MsTeamsChannelData

Microsoft Teams channel data.

#### Attributes

- **connections** (array) *required* - List of Microsoft Teams connections.
- **ms_teams_tenant_id** (string) - Microsoft Teams tenant ID.

#### Example

```json
{
  "connections": [
    {
      "ms_teams_channel_id": "123e4567-e89b-12d3-a456-426614174000",
      "ms_teams_team_id": "123e4567-e89b-12d3-a456-426614174000",
      "ms_teams_tenant_id": null,
      "ms_teams_user_id": null
    }
  ],
  "ms_teams_tenant_id": null
}
```

