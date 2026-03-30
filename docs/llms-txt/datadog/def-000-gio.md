# Source: https://docs.datadoghq.com/security/default_rules/def-000-gio.md

---
title: EC2 paravirtual instance types should not be used
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 paravirtual instance types should
  not be used
---

# EC2 paravirtual instance types should not be used

## Description{% #description %}

This control checks the virtualization type of an EC2 instance to determine if it is set to paravirtual. The control fails if the instance is using paravirtualization.

Amazon Machine Images (AMIs) for Linux come in two virtualization types: paravirtual (PV) and hardware virtual machine (HVM). The primary distinctions between PV and HVM AMIs include their boot methods and their ability to leverage hardware extensions (such as CPU, network, and storage) for enhanced performance.

Historically, PV instances often outperformed HVM instances in many scenarios. However, with advancements in HVM technology and the availability of PV drivers for HVM AMIs, this is no longer the case. For further details, refer to the section on [Linux AMI virtualization types in the Amazon EC2 User Guide for Linux Instances](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-tunnel-options.html).

## Remediation{% #remediation %}

For instructions on updating an EC2 instance to a new instance type, refer to the section on [changing the instance type in the Amazon EC2 User Guide for Linux Instances][2].
