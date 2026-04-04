# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dialogflow_conversation_profile.dataset.md

---
title: Dialogflow Conversation Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dialogflow Conversation Profile
---

# Dialogflow Conversation Profile

A Dialogflow Conversation Profile in Google Cloud defines the configuration for managing conversations between users and virtual agents. It specifies settings such as language, agent behavior, logging, and integration with contact centers or telephony systems. This resource helps customize how Dialogflow handles interactions, ensuring consistent and context-aware responses across different communication channels.

```
gcp.dialogflow_conversation_profile
```

## Fields

| Title                                      | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                        | Description |
| ------------------------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                       | core | string        |
| ancestors                                  | core | array<string> |
| automated_agent_config                     | core | json          | Configuration for an automated agent to use with this profile.                                                                                                                                                                                                                                   |
| create_time                                | core | timestamp     | Output only. Create time of the conversation profile.                                                                                                                                                                                                                                            |
| datadog_display_name                       | core | string        |
| gcp_display_name                           | core | string        | Required. Human readable name for this profile. Max length 1024 bytes.                                                                                                                                                                                                                           |
| human_agent_assistant_config               | core | json          | Configuration for agent assistance to use with this profile.                                                                                                                                                                                                                                     |
| human_agent_handoff_config                 | core | json          | Configuration for connecting to a live agent. Currently, this feature is not general available, please contact Google to get access.                                                                                                                                                             |
| labels                                     | core | array<string> |
| language_code                              | core | string        | Language code for the conversation profile. If not specified, the language is en-US. Language at ConversationProfile should be set for all non en-US languages. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".                          |
| logging_config                             | core | json          | Configuration for logging conversation lifecycle events.                                                                                                                                                                                                                                         |
| name                                       | core | string        | The unique identifier of this conversation profile. Format: `projects//locations//conversationProfiles/`.                                                                                                                                                                                        |
| new_message_event_notification_config      | core | json          | Configuration for publishing new message events. Event will be sent in format of ConversationEvent                                                                                                                                                                                               |
| new_recognition_result_notification_config | core | json          | Optional. Configuration for publishing transcription intermediate results. Event will be sent in format of ConversationEvent. If configured, the following information will be populated as ConversationEvent Pub/Sub message attributes: - "participant_id" - "participant_role" - "message_id" |
| notification_config                        | core | json          | Configuration for publishing conversation lifecycle events.                                                                                                                                                                                                                                      |
| organization_id                            | core | string        |
| parent                                     | core | string        |
| project_id                                 | core | string        |
| project_number                             | core | string        |
| region_id                                  | core | string        |
| resource_name                              | core | string        |
| security_settings                          | core | string        | Name of the CX SecuritySettings reference for the agent. Format: `projects//locations//securitySettings/`.                                                                                                                                                                                       |
| stt_config                                 | core | json          | Settings for speech transcription.                                                                                                                                                                                                                                                               |
| tags                                       | core | hstore_csv    |
| time_zone                                  | core | string        | The time zone of this conversational profile from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. Defaults to America/New_York.                                                                                                                 |
| tts_config                                 | core | json          | Configuration for Text-to-Speech synthesization. Used by Phone Gateway to specify synthesization options. If agent defines synthesization options as well, agent settings overrides the option here.                                                                                             |
| update_time                                | core | timestamp     | Output only. Update time of the conversation profile.                                                                                                                                                                                                                                            |
| zone_id                                    | core | string        |
