# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.gamelift_matchmaking_rule_set.dataset.md

---
title: GameLift Matchmaking Rule Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GameLift Matchmaking Rule Set
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.gamelift_matchmaking_rule_set.dataset/index.html
---

# GameLift Matchmaking Rule Set

An AWS GameLift Matchmaking Rule Set defines the rules and logic used by GameLift FlexMatch to create balanced multiplayer matches. It specifies player attributes, team composition, and match requirements, ensuring fair and competitive gameplay experiences.

```
aws.gamelift_matchmaking_rule_set
```

## Fields

| Title         | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                     | Description |
| ------------- | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string    |
| account_id    | core | string    |
| creation_time | core | timestamp | A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").                                                                                                                                                                          |
| rule_set_arn  | core | string    | The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift Servers matchmaking rule set resource and uniquely identifies it. ARNs are unique across all Regions. Format is arn:aws:gamelift:<region>::matchmakingruleset/<ruleset name>. In a GameLift rule set ARN, the resource ID matches the RuleSetName value. |
| rule_set_body | core | string    | A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.                                                                                                                                                                               |
| rule_set_name | core | string    | A unique identifier for the matchmaking rule set                                                                                                                                                                                                                                                                              |
| tags          | core | hstore    |
