# Source: https://docs.datadoghq.com/security/default_rules/def-000-pyk.md

---
title: Ensure Only One Firewall Service is Active
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure Only One Firewall Service is
  Active
---

# Ensure Only One Firewall Service is Active

## Description{% #description %}

The system must have exactly one active firewall service running to avoid conflicts and ensure consistent packet filtering. Only one of the following services should be enabled and active at any time:

- ufw - Uncomplicated Firewall (Ubuntu/Debian default)
- iptables - Classic Linux firewall
- nftables - Next Generation Firewall replacement for iptables

Having zero active firewalls leaves the system vulnerable, while having multiple active firewalls can lead to rule conflicts and security gaps.

## Rationale{% #rationale %}

Running multiple firewall services simultaneously can lead to conflicts in rule processing, unpredictable behavior, and potential security gaps. A single firewall service ensures consistent and predictable packet filtering. Having no active firewall service leaves the system exposed to network-based attacks and unauthorized access.

## Warning{% #warning %}

This rule does not come with a remediation. There are specific rules for enabling each firewall which should be enabled instead.
