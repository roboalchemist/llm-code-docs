# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lexv2_bot.dataset.md

---
title: Lex V2 Bot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lex V2 Bot
---

# Lex V2 Bot

This table represents the Lex V2 Bot resource from Amazon Web Services.

```
aws.lexv2_bot
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                         | Description |
| --------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| bot_id                      | core | string        | The unique identifier of the bot.                                                                                                 |
| bot_members                 | core | json          | The list of bots in the network that was described.                                                                               |
| bot_name                    | core | string        | The name of the bot.                                                                                                              |
| bot_status                  | core | string        | The current status of the bot. When the status is <code>Available</code> the bot is ready to be used in conversations with users. |
| bot_type                    | core | string        | The type of the bot that was described.                                                                                           |
| creation_date_time          | core | timestamp     | A timestamp of the date and time that the bot was created.                                                                        |
| data_privacy                | core | json          | Settings for managing data privacy of the bot and its conversations with users.                                                   |
| description                 | core | string        | The description of the bot.                                                                                                       |
| failure_reasons             | core | array<string> | If the <code>botStatus</code> is <code>Failed</code>, this contains a list of reasons that the bot couldn't be built.             |
| idle_session_ttl_in_seconds | core | int64         | The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.                                          |
| last_updated_date_time      | core | timestamp     | A timestamp of the date and time that the bot was last updated.                                                                   |
| role_arn                    | core | string        | The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot.                                              |
| tags                        | core | hstore_csv    |
