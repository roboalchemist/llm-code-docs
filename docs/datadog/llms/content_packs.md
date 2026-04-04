# Source: https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/content_packs.md

---
title: Content Packs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud SIEM > Ingest and Enrich > Content Packs
---

# Content Packs

## Overview{% #overview %}

[Cloud SIEM Content Packs](https://app.datadoghq.com/security/siem/content-packs) provide out-of-the box content for key security integrations. Depending on the integration, a Content Pack can include the following:

- [Detection Rules](https://docs.datadoghq.com/security/detection_rules/) to provide comprehensive coverage of your environment
- An interactive dashboard with detailed insights into the state of logs and security signals for the Content Pack
- [Investigator](https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigator), an interactive graphical interface for investigating suspicious activity by a user or resource
- [Workflow Automation](https://docs.datadoghq.com/service_management/workflows/), to automate actions and accelerate investigation and remediation of issues
- Configuration guides

Content Packs are grouped into the following categories:

- [Authentication: 1Password, Datadog Audit Trail, Auth0, BeyondTrust Identity Security Insights, BeyondTrust Password Safe, Bitwarden, Cisco DUO, Delinea Privilege Manager, Delinea Secret Server, Have I Been Pwned, Jumpcloud, Keeper Security, Keycloak, LastPass, Okta, Ping Federate, PingOne, Push Security, Symantec VIP, Zscaler](#authentication)
- [Cloud Audit: AWS CloudTrail, Azure Security, GCP Audit Logs, Greenhouse, Kubernetes Audit Logs, Linux Audit Logs, Oracle Cloud Infrastructure](#cloud_audit)
- [Cloud Developer Tools: Atlassian Jira & Confluence Audit Records, Atlassian Organization Event Logs, Confluent Cloud Audit Logs, GitHub, GitLab Audit Events, HCP Terraform, Snowflake, Sonatype Nexus, Twilio](#cloud_developer_tools)
- [Cloud Security: Falco, Google Security Command Center, Microsoft Graph, Orca Security, Wiz, Wiz Vulnerabilities](#cloud_security)
- [Collaboration: Asana, Box, Google Workspace, Microsoft 365, Salesforce, Slack, Zendesk, Zoom Activity Logs](#collaboration)
- [Email Security: Abnormal Security, Check Point Harmony Email & Collaboration, Cisco Secure Email Threat Defense, Mimecast, Trend Micro Email Security](#email_security)
- [Endpoint: Bitdefender, Cisco Secure Endpoint, Crowdstrike, ESET Protect, Jamf Pro, Jamf Protect, Mac Audit Logs, Microsoft Sysmon, OSSEC, SentinelOne, Sophos Central Cloud, Supply-Chain Firewall, Trend Micro Vision One Endpoint Security, Trend Micro Vision One XDR, Windows Event Logs](#endpoint)
- [Network: Bind9, Checkpoint Quantum Firewall, Cisco Secure Firewall, Cisco Umbrella DNS, Cloudflare, DNSFilter, ExtraHop, Fortinet FortiManager, Imperva, Ivanti Connect Secure, Juniper SRX Firewall, Cisco Meraki, Microsoft DNS, OpenVPN, Palo Alto Cortex XDR, Palo Alto Networks Firewall, Palo Alto Panorama, Suricata, WatchGuard Firebox, Zeek](#network)
- [Web Security: Apache, App & API Protection for .NET, App & API Protection for Go, App & API Protection for Java, App & API Protection for Node.js, App & API Protection for PHP, App & API Protection for Python, App & API Protection for Ruby, Cisco Secure Web Appliance, Fastly, Forcepoint Secure Web Gateway, Forcepoint Security Service Edge, iboss, Netskope, NGINX](#web_security)

## Authentication Content Packs{% #authentication %}

### 1Password

Monitor account activity with 1Password Events Reporting.

[1Password](https://app.datadoghq.com/security/content-packs?contentPackId=1password) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#1password)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/1password/)

### Datadog Audit Trail

Gain visibility into user and configuration changes across Datadog to monitor activity, detect unauthorized modifications, and support compliance and governance requirements.

[Datadog Audit Trail](https://app.datadoghq.com/security/content-packs?contentPackId=audit-trail) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/account_management/audit_trail/)

### Auth0

Monitor and generate signals around Auth0 user activity.

[Auth0](https://app.datadoghq.com/security/content-packs?contentPackId=auth0) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#auth0)
- An interactive dashboard
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/auth0/)

### BeyondTrust Identity Security Insights

Monitor identity risks with BeyondTrust Identity Security Insights.

[BeyondTrust Identity Security Insights](https://app.datadoghq.com/security/content-packs?contentPackId=beyondtrust-identity-security-insights) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/beyondtrust-identity-security-insights/)

### BeyondTrust Password Safe

Monitor privileged access activity with BeyondTrust Password Safe.

[BeyondTrust Password Safe](https://app.datadoghq.com/security/content-packs?contentPackId=beyondtrust-password-safe) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/beyondtrust-password-safe/)

### Bitwarden

Ingest and analyze Bitwarden event logs, including item events, user events, group events, and organization activity.

[Bitwarden](https://app.datadoghq.com/security/content-packs?contentPackId=bitwarden) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/bitwarden/)

### Cisco DUO

Monitor and analyze MFA and secure access logs from Cisco DUO.

[Cisco DUO](https://app.datadoghq.com/security/content-packs?contentPackId=cisco-duo) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#cisco-duo)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/cisco_duo/)

### Delinea Privilege Manager

Gain insights into Delinea Privilege Manager events.

[Delinea Privilege Manager](https://app.datadoghq.com/security/content-packs?contentPackId=delinea-privilege-manager) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#delinea-privilege-manager)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/delinea-privilege-manager/)

### Delinea Secret Server

Track privileged credential usage and user activity from Delinea Secret Server to monitor authentication events and secure access to sensitive systems.

[Delinea Secret Server](https://app.datadoghq.com/security/content-packs?contentPackId=delinea-secret-server) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/delinea-secret-server/)

### Have I Been Pwned

Collect breach activity logs from Have I Been Pwned.

[Have I Been Pwned](https://app.datadoghq.com/security/content-packs?contentPackId=have-i-been-pwned) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#have-i-been-pwned)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/have-i-been-pwned/)

### Jumpcloud

Track user activity by monitoring Jumpcloud audit Logs.

[Jumpcloud](https://app.datadoghq.com/security/content-packs?contentPackId=jumpcloud) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#jumpcloud)
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/jumpcloud/)

### Keeper Security

Monitor credential use, privileged access, and security events from Keeper Security.

[Keeper Security](https://app.datadoghq.com/security/content-packs?contentPackId=keeper) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#keeper)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/keeper/)

### Keycloak

Gain insights into user and administrative activity from Keycloak.

[Keycloak](https://app.datadoghq.com/security/content-packs?contentPackId=keycloak) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#keycloak)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/keycloak/)

### LastPass

Monitor LastPass activity and analyze with detection rules

[LastPass](https://app.datadoghq.com/security/content-packs?contentPackId=lastpass) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#lastpass)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/lastpass)

### Okta

Track user activity by monitoring Okta audit logs.

[Okta](https://app.datadoghq.com/security/content-packs?contentPackId=okta) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#okta)
- An interactive dashboard
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/okta/)

### Ping Federate

Collect and analyze Ping Federate admin and audit logs

[Ping Federate](https://app.datadoghq.com/security/content-packs?contentPackId=ping-federate) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#ping-federate)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/ping_federate/)

### PingOne

Analyze PingOne audit events

[PingOne](https://app.datadoghq.com/security/content-packs?contentPackId=pingone) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#ping-one)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/ping_one/)

### Push Security

Gain visibility into user activity with Push Security.

[Push Security](https://app.datadoghq.com/security/content-packs?contentPackId=push-security) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/push-security/)

### Symantec VIP

Ingest Symantec VIP logs to track user creation, password changes, group management events, and more.

[Symantec VIP](https://app.datadoghq.com/security/content-packs?contentPackId=symantec-vip) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#symantec-vip)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/symantec-vip/)

### Zscaler

Gain visibility into internet and security activity with Zscaler Internet Access.

[Zscaler](https://app.datadoghq.com/security/content-packs?contentPackId=z-scaler) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/z-scaler/)

## Cloud Audit Content Packs{% #cloud_audit %}

### AWS CloudTrail

Monitor security and compliance levels of your AWS operations.

[AWS CloudTrail](https://app.datadoghq.com/security/content-packs?contentPackId=aws-cloudtrail) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#cloudtrail)
- An interactive dashboard
- AWS Investigator
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/security/cloud_siem/guide/aws-config-guide-for-cloud-siem/)

### Azure Security

Protect your Azure environment by tracking attacker activity.

[Azure Security](https://app.datadoghq.com/security/content-packs?contentPackId=azure) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#azure)
- An interactive dashboard
- AZURE Investigator
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/security/cloud_siem/guide/azure-config-guide-for-cloud-siem)

### GCP Audit Logs

Protect your GCP environment by monitoring audit logs.

[GCP Audit Logs](https://app.datadoghq.com/security/content-packs?contentPackId=gcp-audit-logs) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#gcp)
- An interactive dashboard
- GCP Investigator
- [Configuration guide](https://docs.datadoghq.com/security/cloud_siem/guide/google-cloud-config-guide-for-cloud-siem/)

### Greenhouse

Gain insights into your organization's hiring activities by monitoring Greenhouse audit logs

[Greenhouse](https://app.datadoghq.com/security/content-packs?contentPackId=greenhouse) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/greenhouse/)

### Kubernetes Audit Logs

Monitor open source Kubernetes and Amazon Elastic Kubernetes Service (EKS) audit logs for threats.

[Kubernetes Audit Logs](https://app.datadoghq.com/security/content-packs?contentPackId=kubernetes-audit-logs) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#kubernetes)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/kubernetes_audit_logs/)

### Linux Audit Logs

Monitor user activity, authentication events, and policy changes with enriched Linux audit logs across Red Hat, Ubuntu, and CentOS.

[Linux Audit Logs](https://app.datadoghq.com/security/content-packs?contentPackId=linux-audit-logs) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/linux-audit-logs/)

### Oracle Cloud Infrastructure

Monitor Oracle Cloud Infrastructure audit logs to detect suspicious activity, failed access, and resource changes.

[Oracle Cloud Infrastructure](https://app.datadoghq.com/security/content-packs?contentPackId=oracle-cloud-infrastructure) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#oracle-cloud-infrastructure)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/oracle-cloud-infrastructure/)

## Cloud Developer Tools Content Packs{% #cloud_developer_tools %}

### Atlassian Jira & Confluence Audit Records

Monitor, secure, and optimize your Atlassian's Jira & Confluence environments.

[Atlassian Jira & Confluence Audit Records](https://app.datadoghq.com/security/content-packs?contentPackId=atlassian-audit) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#jira-audit-records)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/atlassian-audit-records/)

### Atlassian Organization Event Logs

Monitor admin activity from your organization's Atlassian Org including your Atlassian Guard subscription, Jira, and Confluence

[Atlassian Organization Event Logs](https://app.datadoghq.com/security/content-packs?contentPackId=atlassian-event-logs) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#atlassian-event-logs)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/atlassian_event_logs/)

### Confluent Cloud Audit Logs

Monitor Confluent Cloud audit logs

[Confluent Cloud Audit Logs](https://app.datadoghq.com/security/content-packs?contentPackId=confluent-cloud-audit-logs) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/confluent_cloud_audit_logs/)

### GitHub

Track user activity and code change history by monitoring GitHub audit logs.

[GitHub](https://app.datadoghq.com/security/content-packs?contentPackId=github) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#github-telemetry)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/github/)

### GitLab Audit Events

Collect GitLab Audit Events to assess risk, security, and compliance

[GitLab Audit Events](https://app.datadoghq.com/security/content-packs?contentPackId=gitlab-audit-events) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#gitlab)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/gitlab_audit_events/)

### HCP Terraform

Collect activity and audit logs from Terraform

[HCP Terraform](https://app.datadoghq.com/security/content-packs?contentPackId=hcp-terraform) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/hcp_terraform/)

### Snowflake

Collect snowflake logs to monitor for threats, conduct hunts, and perform investigations.

[Snowflake](https://app.datadoghq.com/security/content-packs?contentPackId=snowflake) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#snowflake)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/snowflake_web/)

### Sonatype Nexus

Collect instance health and repository analytics from Sonatype Nexus to monitor software artifact infrastructure.

[Sonatype Nexus](https://app.datadoghq.com/security/content-packs?contentPackId=sonatype-nexus) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/sonatype-nexus/)

### Twilio

Collect and analyze Twilio message, call summary, and event logs

[Twilio](https://app.datadoghq.com/security/content-packs?contentPackId=twilio) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#twilio)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/twilio/)

## Cloud Security Content Packs{% #cloud_security %}

### Falco

Detect runtime threats across containers, Kubernetes, and cloud workloads using enriched alert logs from Falco.

[Falco](https://app.datadoghq.com/security/content-packs?contentPackId=falco) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#falco)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/falco/)

### Google Security Command Center

Track and analyze Google Security Command Center findings.

[Google Security Command Center](https://app.datadoghq.com/security/content-packs?contentPackId=google-security-command-center) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#google.security.command.center)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/google_cloud_security_command_center/)

### Microsoft Graph

Collect security logs and alerts from Defender, Purview, Entra ID, and Sentinel

[Microsoft Graph](https://app.datadoghq.com/security/content-packs?contentPackId=microsoft-graph) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#microsoft-graph)
- An interactive dashboard
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/microsoft_graph/)

### Orca Security

Ingest cloud security alerts from Orca to monitor risk, compliance, and workload protection across your cloud environment.

[Orca Security](https://app.datadoghq.com/security/content-packs?contentPackId=orca-security) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/orca-security/)

### Wiz

View and monitor Wiz audit logs and issues, including toxic combinations.

[Wiz](https://app.datadoghq.com/security/content-packs?contentPackId=wiz) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#wiz)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/wiz/)

### Wiz Vulnerabilities

Enrich signals and detections with vulnerability data from Wiz.

[Wiz Vulnerabilities](https://app.datadoghq.com/security/content-packs?contentPackId=wiz-vulnerabilities) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/wiz/)

## Collaboration Content Packs{% #collaboration %}

### Asana

Explore and analyze Asana audit logs

[Asana](https://app.datadoghq.com/security/content-packs?contentPackId=asana) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#asana)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/asana/)

### Box

Monitor activity across your Box environment with enterprise event logs.

[Box](https://app.datadoghq.com/security/content-packs?contentPackId=box) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/box/)

### Google Workspace

Optimize your security monitoring within Google Workspace.

[Google Workspace](https://app.datadoghq.com/security/content-packs?contentPackId=google-workspace) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#gsuite)
- An interactive dashboard
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/gsuite/)

### Microsoft 365

Monitor key security events from Microsoft 365 logs.

[Microsoft 365](https://app.datadoghq.com/security/content-packs?contentPackId=microsoft-365) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#microsoft-365)
- An interactive dashboard
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/microsoft_365/)

### Salesforce

Collect Salesforce real-time platform events as Datadog logs.

[Salesforce](https://app.datadoghq.com/security/content-packs?contentPackId=salesforce) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#salesforce)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/salesforce/)

### Slack

View, analyze, and monitor Slack audit logs.

[Slack](https://app.datadoghq.com/security/content-packs?contentPackId=slack) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#slack)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/slack/?tab=datadogforslack#enterprise-grid-audit-logs)

### Zendesk

Ingest Zendesk audit and access logs to monitor user and admin activity.

[Zendesk](https://app.datadoghq.com/security/content-packs?contentPackId=zendesk) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#zendesk)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/zendesk/)

### Zoom Activity Logs

Collect and monitor Zoom activity

[Zoom Activity Logs](https://app.datadoghq.com/security/content-packs?contentPackId=zoom-activity-logs) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#zoom)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/zoom_activity_logs/)

## Email Security Content Packs{% #email_security %}

### Abnormal Security

Monitor threat events, cases, and audit logs for Abnormal Security

[Abnormal Security](https://app.datadoghq.com/security/content-packs?contentPackId=abnormal-security) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#abnormal-security)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/abnormal_security/)

### Check Point Harmony Email & Collaboration

Collect security events from Check Point Harmony Email & Collaboration.

[Check Point Harmony Email & Collaboration](https://app.datadoghq.com/security/content-packs?contentPackId=checkpoint-harmony-email-and-collaboration) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#checkpoint-harmony-email-and-collaboration)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/checkpoint-harmony-email-and-collaboration/)

### Cisco Secure Email Threat Defense

Gain insights into Cisco Secure Email Threat Defense message logs.

[Cisco Secure Email Threat Defense](https://app.datadoghq.com/security/content-packs?contentPackId=cisco-secure-email-threat-defense) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#cisco-secure-email-threat-defense)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/cisco-secure-email-threat-defense/)

### Mimecast

Analyze logs and generate signals from Mimecast email security solutions

[Mimecast](https://app.datadoghq.com/security/content-packs?contentPackId=mimecast) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#mimecast)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/mimecast/)

### Trend Micro Email Security

Analyze email policy events and track mail flows for Trend Micro Email Security

[Trend Micro Email Security](https://app.datadoghq.com/security/content-packs?contentPackId=trend-micro-email-security) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#trend-micro-email-security)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/trend_micro_email_security/)

## Endpoint Content Packs{% #endpoint %}

### Bitdefender

Ingest endpoint threat detections and incident activity from Bitdefender EDR, including malware, phishing, exploits, and ransomware events.

[Bitdefender](https://app.datadoghq.com/security/content-packs?contentPackId=bitdefender) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/bitdefender/)

### Cisco Secure Endpoint

Collect Cisco Secure Endpoint alerts and audit logs

[Cisco Secure Endpoint](https://app.datadoghq.com/security/content-packs?contentPackId=cisco-secure-endpoint) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#cisco-secure-endpoint)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/cisco_secure_endpoint/)

### Crowdstrike

Improve the security posture of your endpoints with Crowdstrike.

[Crowdstrike](https://app.datadoghq.com/security/content-packs?contentPackId=crowdstrike) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#crowdstrike)
- An interactive dashboard
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/crowdstrike/)

### ESET Protect

Monitor endpoint threats, firewall activity, and web filtering logs from ESET Protect.

[ESET Protect](https://app.datadoghq.com/security/content-packs?contentPackId=eset-protect) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/eset-protect/)

### Jamf Pro

Monitor Apple device activity and management events using Jamf Pro logs.

[Jamf Pro](https://app.datadoghq.com/security/content-packs?contentPackId=jamf-pro) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/jamf-pro/)

### Jamf Protect

Endpoint security and mobile threat defense (MTD) for Mac and mobile devices.

[Jamf Protect](https://app.datadoghq.com/security/content-packs?contentPackId=jamf-protect) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#jamfprotect)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/jamf_protect)

### Mac Audit Logs

Monitor macOS system events, user actions, and security activity using Mac Audit Logs.

[Mac Audit Logs](https://app.datadoghq.com/security/content-packs?contentPackId=mac-audit-logs) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/mac-audit-logs/)

### Microsoft Sysmon

Gain insights into Windows system activity events.

[Microsoft Sysmon](https://app.datadoghq.com/security/content-packs?contentPackId=microsoft-sysmon) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/microsoft-sysmon/)

### OSSEC

Ingest OSSEC alerts from monitored hosts

[OSSEC](https://app.datadoghq.com/security/content-packs?contentPackId=ossec-security) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#ossec-security)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/ossec-security/)

### SentinelOne

Integrate SentinelOne Singularlity Endpoint alerts and threats into Cloud SIEM.

[SentinelOne](https://app.datadoghq.com/security/content-packs?contentPackId=sentinel-one) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#sentinelone)
- An interactive dashboard
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/sentinelone/)

### Sophos Central Cloud

Monitor and analyze Sophos Central Cloud events and alerts

[Sophos Central Cloud](https://app.datadoghq.com/security/content-packs?contentPackId=sophos-central-cloud) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#sophos-central-cloud)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/sophos_central_cloud/)

### Supply-Chain Firewall

View, analyze, and monitor package manager usage with Supply-Chain Firewall.

[Supply-Chain Firewall](https://app.datadoghq.com/security/content-packs?contentPackId=supply-chain-firewall) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/supply-chain-firewall/)

### Trend Micro Vision One Endpoint Security

Collect and analyze extensive logs from Trend Micro Vision One Endpoint Security

[Trend Micro Vision One Endpoint Security](https://app.datadoghq.com/security/content-packs?contentPackId=trend-micro-vision-one-endpoint-security) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#trend-micro-vision-one-endpoint-security)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/trend-micro-vision-one-endpoint-security/)

### Trend Micro Vision One XDR

Gain insights into Trend Micro Vision One XDR logs.

[Trend Micro Vision One XDR](https://app.datadoghq.com/security/content-packs?contentPackId=trend-micro-vision-one-xdr) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#trend-micro-vision-one-xdr)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/trend-micro-vision-one-xdr/)

### Windows Event Logs

Monitor and analyze your Windows system for potential threats with Windows Event Logs.

[Windows Event Logs](https://app.datadoghq.com/security/content-packs?contentPackId=windows-event-logs) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#windows)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/win32_event_log)

## Network Content Packs{% #network %}

### Bind9

Collect Bind9 DNS server logs

[Bind9](https://app.datadoghq.com/security/content-packs?contentPackId=bind9) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/bind9/)

### Checkpoint Quantum Firewall

Monitor and alert on your network's Check Point Quantum firewalls.

[Checkpoint Quantum Firewall](https://app.datadoghq.com/security/content-packs?contentPackId=checkpoint-quantum-firewall) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#checkpoint-quantum-firewall)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/checkpoint_quantum_firewall/)

### Cisco Secure Firewall

Gain insights into Cisco Secure Firewall logs.

[Cisco Secure Firewall](https://app.datadoghq.com/security/content-packs?contentPackId=cisco-secure-firewall) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/cisco_secure_firewall/)

### Cisco Umbrella DNS

Collect and monitor logs from Cisco Umbrella to gain insights into DNS and Proxy logs.

[Cisco Umbrella DNS](https://app.datadoghq.com/security/content-packs?contentPackId=cisco-umbrella-dns) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#cisco-umbrella-dns)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/cisco_umbrella_dns/)

### Cloudflare

Enhance security for your web applications.

[Cloudflare](https://app.datadoghq.com/security/content-packs?contentPackId=cloudflare) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#cloudflare)
- An interactive dashboard
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/cloudflare/)

### DNSFilter

Monitor and analyze DNSFilter logs to detect blocked threats and DNS activity.

[DNSFilter](https://app.datadoghq.com/security/content-packs?contentPackId=dnsfilter) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/dnsfilter/)

### ExtraHop

Gain insights into ExtraHop detection and investigation logs.

[ExtraHop](https://app.datadoghq.com/security/content-packs?contentPackId=extrahop) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#extrahop)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/extrahop/)

### Fortinet FortiManager

Monitor device health, security telemetry, and more across your networks managed by Fortinet, including FortiGate Next Generation Firewalls (NGFW).

[Fortinet FortiManager](https://app.datadoghq.com/security/content-packs?contentPackId=fortinet-fortimanager) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#fortinet-fortimanager)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/fortinet-fortimanager/)

### Imperva

Collect and analyze Imperva web application firewall logs, audit logs, and attack analytics

[Imperva](https://app.datadoghq.com/security/content-packs?contentPackId=imperva) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/imperva/)

### Ivanti Connect Secure

Monitor Ivanti Connect Secure logs to gain visibility into authentication activity, system changes, and security events.

[Ivanti Connect Secure](https://app.datadoghq.com/security/content-packs?contentPackId=ivanti-connect-secure) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#ivanti-connect-secure)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/ivanti-connect-secure/)

### Juniper SRX Firewall

Monitor session activity, security threats, and authentication events from Juniper SRX Firewall logs.

[Juniper SRX Firewall](https://app.datadoghq.com/security/content-packs?contentPackId=juniper-srx-firewall) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/juniper-srx-firewall/)

### Cisco Meraki

Monitor Cisco Meraki logs and identify attacker activity.

[Cisco Meraki](https://app.datadoghq.com/security/content-packs?contentPackId=meraki) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#meraki)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/meraki/)

### Microsoft DNS

Gain insights into Microsoft DNS Server audit events.

[Microsoft DNS](https://app.datadoghq.com/security/content-packs?contentPackId=microsoft-dns) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/microsoft-dns/)

### OpenVPN

Monitor VPN session activity and authentication events with real-time insights from OpenVPN logs.

[OpenVPN](https://app.datadoghq.com/security/content-packs?contentPackId=openvpn) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/openvpn/)

### Palo Alto Cortex XDR

Collect and analyze Palo Alto Cortex XDR logs

[Palo Alto Cortex XDR](https://app.datadoghq.com/security/content-packs?contentPackId=palo-alto-cortex-xdr) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#palo-alto-cortex-xdr)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/palo-alto-cortex-xdr/)

### Palo Alto Networks Firewall

Analyze traffic and detect threats with Palo Alto Networks Firewall.

[Palo Alto Networks Firewall](https://app.datadoghq.com/security/content-packs?contentPackId=pan-firewall) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#pan.firewall)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/pan_firewall/)

### Palo Alto Panorama

Monitor and detect your Palo Alto Panorama firewalls.

[Palo Alto Panorama](https://app.datadoghq.com/security/content-packs?contentPackId=pan-panorama) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/palo_alto_panorama/)

### Suricata

Gain insights into Suricata logs.

[Suricata](https://app.datadoghq.com/security/content-packs?contentPackId=suricata) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#suricata)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/suricata/)

### WatchGuard Firebox

Analyze firewall, VPN, proxy, and system events from WatchGuard Firebox logs.

[WatchGuard Firebox](https://app.datadoghq.com/security/content-packs?contentPackId=watchguard-firebox) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/watchguard-firebox/)

### Zeek

Analyze and store Corelight / Zeek logs to gain insights into network threats.

[Zeek](https://app.datadoghq.com/security/content-packs?contentPackId=zeek) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#zeek)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/zeek/)

## Web Security Content Packs{% #web_security %}

### Apache

Collect and analyze Apache logs and metrics

[Apache](https://app.datadoghq.com/security/content-packs?contentPackId=apache) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#apache)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/apache/?tab=host)

### App & API Protection for .NET

Monitor and Protect your .NET applications with App & API Protection

[App & API Protection for .NET](https://app.datadoghq.com/security/content-packs?contentPackId=appsec-dotnet) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/security/application_security/setup/dotnet/)

### App & API Protection for Go

Monitor and Protect your Go applications with App & API Protection

[App & API Protection for Go](https://app.datadoghq.com/security/content-packs?contentPackId=appsec-go) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/security/application_security/setup/go/)

### App & API Protection for Java

Monitor and Protect your Java applications with App & API Protection

[App & API Protection for Java](https://app.datadoghq.com/security/content-packs?contentPackId=appsec-java) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/security/application_security/setup/java/)

### App & API Protection for Node.js

Monitor and Protect your Node.js applications with App & API Protection

[App & API Protection for Node.js](https://app.datadoghq.com/security/content-packs?contentPackId=appsec-node) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/security/application_security/setup/nodejs/)

### App & API Protection for PHP

Monitor and Protect your PHP applications with App & API Protection

[App & API Protection for PHP](https://app.datadoghq.com/security/content-packs?contentPackId=appsec-php) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/security/application_security/setup/php/)

### App & API Protection for Python

Monitor and Protect your Python applications with App & API Protection

[App & API Protection for Python](https://app.datadoghq.com/security/content-packs?contentPackId=appsec-python) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/security/application_security/setup/python/)

### App & API Protection for Ruby

Monitor and Protect your Ruby applications with App & API Protection

[App & API Protection for Ruby](https://app.datadoghq.com/security/content-packs?contentPackId=appsec-ruby) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/security/application_security/setup/ruby/)

### Cisco Secure Web Appliance

Gain visibility into access and traffic logs from Cisco Secure Web Appliance to detect web threats and enforce security policies.

[Cisco Secure Web Appliance](https://app.datadoghq.com/security/content-packs?contentPackId=cisco-secure-web-appliance) Content Pack includes:

- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/cisco-secure-web-appliance/)

### Fastly

Monitor HTTP server performance, traffic, and uptime metrics.

[Fastly](https://app.datadoghq.com/security/content-packs?contentPackId=fastly) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#fastly)
- An interactive dashboard
- Workflow Automation
- [Configuration guide](https://docs.datadoghq.com/integrations/fastly/)

### Forcepoint Secure Web Gateway

Monitor user web activity and data loss prevention events with real-time logs from Forcepoint Secure Web Gateway.

[Forcepoint Secure Web Gateway](https://app.datadoghq.com/security/content-packs?contentPackId=forcepoint-secure-web-gateway) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#forcepoint-secure-web-gateway)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/forcepoint-secure-web-gateway/)

### Forcepoint Security Service Edge

Collect and analyze cloud activity, access, admin, and health logs from Forcepoint Security Service Edge

[Forcepoint Security Service Edge](https://app.datadoghq.com/security/content-packs?contentPackId=forcepoint-security-service-edge) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#forcepoint-security-service-edge)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/forcepoint-security-service-edge/)

### iboss

Ingest iboss web, DLP, and audit logs to monitor traffic activity, data loss risks, and user actions.

[iboss](https://app.datadoghq.com/security/content-packs?contentPackId=iboss) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#iboss)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/iboss/)

### Netskope

Gain visibility into user web traffic and security events with Netskope transaction logs.

[Netskope](https://app.datadoghq.com/security/content-packs?contentPackId=netskope) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#netskope)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/netskope/)

### NGINX

Monitor and respond to web-based risks with Nginx.

[NGINX](https://app.datadoghq.com/security/content-packs?contentPackId=nginx) Content Pack includes:

- [Detection Rules](https://docs.datadoghq.com/security/default_rules/#nginx)
- An interactive dashboard
- [Configuration guide](https://docs.datadoghq.com/integrations/nginx/)

## Further reading{% #further-reading %}

- [Datadog Cloud SIEM: Driving innovation in security operations](https://www.datadoghq.com/blog/cloud-siem-enterprise-security)
- [Monitor OCI Audit Logs with Datadog Cloud SIEM](https://www.datadoghq.com/blog/oci-content-pack)
- [Create log detection rules](https://docs.datadoghq.com/security/cloud_siem/detection_rules)
- [Learn more about the Investigator](https://docs.datadoghq.com/security/cloud_siem/investigator)
- [Investigate security signals](https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigate_security_signals)
- [What's new in Cloud SIEM Content Packs: September 2024](https://www.datadoghq.com/blog/cloud-siem-content-packs-whats-new-2024-09/)
- [How attackers take advantage of Microsoft 365 services](https://www.datadoghq.com/blog/microsoft-365-detections/)
- [Detect malicious activity in Google Workspace apps with Datadog Cloud SIEM](https://www.datadoghq.com/blog/google-workspace-detections/)
- [Normalize your data with the OCSF Common Data Model in Datadog Cloud SIEM](https://www.datadoghq.com/blog/ocsf-common-data-model/)
