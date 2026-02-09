# Source: https://docs.datadoghq.com/security/default_rules/yqe-gyj-js8.md

---
title: Impossible travel observed on IAM User access key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Impossible travel observed on IAM User
  access key
---

# Impossible travel observed on IAM User access key
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect an Impossible Travel event when a `@userIdentity.type:` `{{@userIdentity.type}}` uses an AWS IAM access key and filter out VPNs and AWS Internal IPs.

## Strategy{% #strategy %}

The Impossible Travel detection type's algorithm compares the GeoIP data of the last log and the current log to determine if the IAM user with `@userIdentity.session_name:` `{{@userIdentity.session_name}}` traveled more than 500km at over 1,000km/hr and used an AWS IAM access key.

## Triage and response{% #triage-and-response %}

1. Determine if the `@userIdentity.accessKeyId:` `{{@userIdentity.accessKeyId}}` for `@userIdentity.session_name:` `{{@userIdentity.session_name}}` should be used from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`.
1. If the IAM user should not be used from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`, then consider isolating the account and reset credentials.
1. Audit any user actions that may have occurred after the illegitimate login.

## Changelog{% #changelog %}

- 7 April 2022 - Updated signal message.
- 3 August 2022 - Fixed null groupby field in query.
- 11 September 2024 - Tuned rule to remove internal network IPs and the three major cloud provider IPs: Azure, AWS, and GCP.
- 30 September 2024 - Updated query to replace attribute `@threat_intel.results.subcategory:anonymizer`.
- 18 November 2024 - Updated query to remove when accessKeyId is empty.
- 9 May 2025 - Updated title to be clear on impossible travel detection method usage.
