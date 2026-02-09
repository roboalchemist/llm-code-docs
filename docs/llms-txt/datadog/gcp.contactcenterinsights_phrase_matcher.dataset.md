# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.contactcenterinsights_phrase_matcher.dataset.md

---
title: Phrase Matcher
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Phrase Matcher
---

# Phrase Matcher

Phrase Matcher is a Google Cloud resource used to identify and analyze specific phrases within text or audio data. It is commonly used in Contact Center AI and speech analytics to detect predefined terms or expressions in conversations. This helps automate quality monitoring, compliance checks, and customer sentiment analysis by matching phrases against transcripts or real-time speech streams.

```
gcp.contactcenterinsights_phrase_matcher
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                                                                                                                                            | Description |
| ------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                     | core | string        |
| activation_update_time   | core | timestamp     | Output only. The most recent time at which the activation status was updated.                                                                                                                                                                                                        |
| active                   | core | bool          | Applies the phrase matcher only when it is active.                                                                                                                                                                                                                                   |
| ancestors                | core | array<string> |
| datadog_display_name     | core | string        |
| gcp_display_name         | core | string        | The human-readable name of the phrase matcher.                                                                                                                                                                                                                                       |
| labels                   | core | array<string> |
| name                     | core | string        | The resource name of the phrase matcher. Format: projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher}                                                                                                                                                             |
| organization_id          | core | string        |
| parent                   | core | string        |
| phrase_match_rule_groups | core | json          | A list of phase match rule groups that are included in this matcher.                                                                                                                                                                                                                 |
| project_id               | core | string        |
| project_number           | core | string        |
| region_id                | core | string        |
| resource_name            | core | string        |
| revision_create_time     | core | timestamp     | Output only. The timestamp of when the revision was created. It is also the create time when a new matcher is added.                                                                                                                                                                 |
| revision_id              | core | string        | Output only. Immutable. The revision ID of the phrase matcher. A new revision is committed whenever the matcher is changed, except when it is activated or deactivated. A server generated random ID will be used. Example: locations/global/phraseMatchers/my-first-matcher@1234567 |
| role_match               | core | string        | The role whose utterances the phrase matcher should be matched against. If the role is ROLE_UNSPECIFIED it will be matched against any utterances in the transcript.                                                                                                                 |
| tags                     | core | hstore_csv    |
| type                     | core | string        | Required. The type of this phrase matcher.                                                                                                                                                                                                                                           |
| update_time              | core | timestamp     | Output only. The most recent time at which the phrase matcher was updated.                                                                                                                                                                                                           |
| version_tag              | core | string        | The customized version tag to use for the phrase matcher. If not specified, it will default to `revision_id`.                                                                                                                                                                        |
| zone_id                  | core | string        |
