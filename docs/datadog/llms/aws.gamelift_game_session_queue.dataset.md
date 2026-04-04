# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.gamelift_game_session_queue.dataset.md

---
title: GameLift Game Session Queue
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GameLift Game Session Queue
---

# GameLift Game Session Queue

An Amazon GameLift Game Session Queue is a resource that manages how new game sessions are placed across fleets or aliases. It allows you to define a set of destinations, placement priorities, and latency policies to ensure players are matched to the best available resources. This helps optimize player experience by reducing wait times and improving game performance.

```
aws.gamelift_game_session_queue
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                 | Description |
| ----------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| custom_event_data       | core | string     | Information that is added to all events that are related to this game session queue.                                                                                                                                                                                                                                                      |
| destinations            | core | json       | A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.                                                                                                  |
| filter_configuration    | core | json       | A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of Amazon Web Services Region codes, such as us-west-2. If this parameter is not set, game sessions can be placed in any queue location.                                                                                     |
| game_session_queue_arn  | core | string     | The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is arn:aws:gamelift:<region>::gamesessionqueue/<queue name>. In a Amazon GameLift Servers game session queue ARN, the resource ID matches the Name value. |
| name                    | core | string     | A descriptive label that is associated with game session queue. Queue names must be unique within each Region.                                                                                                                                                                                                                            |
| notification_target     | core | string     | An SNS topic ARN that is set up to receive game session placement notifications. See Setting up notifications for game session placement.                                                                                                                                                                                                 |
| player_latency_policies | core | json       | A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value.                            |
| priority_configuration  | core | json       | Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.                                             |
| tags                    | core | hstore_csv |
| timeout_in_seconds      | core | int64      | The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.                                                                                                                                                 |
