# Source: https://docs.datadoghq.com/security/default_rules/def-000-t9l.md

---
title: GitHub personal access token used to add collaborator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub personal access token used to
  add collaborator
---

# GitHub personal access token used to add collaborator
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detects when GitHub personal access tokens are used to add collaborators to repositories or organizations.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for adding collaborators executed through personal access tokens. It tracks two distinct scenarios:

- Repository collaborator additions via API calls to `/repositories/:repository_id/collaborators/:username` with PUT method.
- External collaborator additions to organizations through `org.add_outside_collaborator` actions.

## Triage & Response{% #triage--response %}

- Examine the `{{@hashed_token}}` to identify the personal access token responsible for the collaborator addition and trace its usage patterns.
- Verify if the token owner has legitimate authorization to add collaborators to the affected repository or organization.
- Review the added collaborator's identity and determine if they are an expected team member or external party with business justification.
- Check the repository or organization's access policies to confirm the collaborator addition aligns with established security controls.
- Analyze the timing and frequency of collaborator additions to identify potential bulk operations or suspicious automation patterns.
