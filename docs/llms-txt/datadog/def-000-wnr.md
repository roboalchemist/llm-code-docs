# Source: https://docs.datadoghq.com/security/default_rules/def-000-wnr.md

---
title: Ensure Mail Transfer Agent is not Listening on any non-loopback Address
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure Mail Transfer Agent is not
  Listening on any non-loopback Address
---

# Ensure Mail Transfer Agent is not Listening on any non-loopback Address

## Description{% #description %}

Mail Transfer Agents (MTA), such as sendmail and Postfix, are used to listen for incoming mail and transfer the messages to the appropriate user or mail server. If the system is not intended to be a mail server, it is recommended that the MTA be configured to only process local mail.

## Rationale{% #rationale %}

The software for all Mail Transfer Agents is complex and most have a long history of security issues. While it is important to ensure that the system can process local mail messages, it is not necessary to have the MTA's daemon listening on a port unless the server is intended to be a mail server that receives and processes mail from other systems.
