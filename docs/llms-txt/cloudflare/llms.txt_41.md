# Source: https://developers.cloudflare.com/logs/llms.txt

# Logs

Access detailed logs with metadata from Cloudflare products

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/logs/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Logs llms-full.txt](https://developers.cloudflare.com/logs/llms-full.txt) for the complete Logs documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Logs](https://developers.cloudflare.com/logs/index.md)

## Logpush

- [Logpush](https://developers.cloudflare.com/logs/logpush/index.md)
- [Logpush alerts and analytics](https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/index.md)
- [Manage Logpush with cURL](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-curl/index.md)
- [Manage Logpush with Python](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-python/index.md)
- [Logpush Health Dashboards](https://developers.cloudflare.com/logs/logpush/logpush-health/index.md)
- [Logpush job setup](https://developers.cloudflare.com/logs/logpush/logpush-job/index.md)
- [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/index.md)
- [Custom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/index.md)
- [Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/index.md)
- [Access requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/access_requests/index.md)
- [Audit Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/index.md)
- [Audit Logs V2](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/index.md)
- [Browser Isolation User Actions](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/index.md)
- [CASB Findings](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/casb_findings/index.md)
- [Device posture results](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/device_posture_results/index.md)
- [DEX Application Tests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_application_tests/index.md)
- [DEX Device State Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_device_state_events/index.md)
- [DLP Forensic Copies](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dlp_forensic_copies/index.md)
- [DNS Firewall Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dns_firewall_logs/index.md)
- [Email Security Alerts](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/email_security_alerts/index.md)
- [Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/index.md)
- [Gateway HTTP](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_http/index.md)
- [Gateway Network](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/index.md)
- [IPSec Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/index.md)
- [Magic IDS Detections](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/index.md)
- [MCP Portal Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/index.md)
- [Network Analytics Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/network_analytics_logs/index.md)
- [Sinkhole HTTP Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/sinkhole_http_logs/index.md)
- [SSH Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/index.md)
- [WARP Config Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_config_changes/index.md)
- [WARP Toggle Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_toggle_changes/index.md)
- [Workers Trace Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events/index.md)
- [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/index.md)
- [CMB support by dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/cmb/index.md)
- [DNS logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/dns_logs/index.md)
- [Firewall events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/index.md)
- [HTTP requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/index.md)
- [NEL reports](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/nel_reports/index.md)
- [Page Shield events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/index.md)
- [Spectrum events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/spectrum_events/index.md)
- [Zaraz Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/zaraz_events/index.md)
- [Edge Log Delivery](https://developers.cloudflare.com/logs/logpush/logpush-job/edge-log-delivery/index.md)
- [Enable destinations](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/index.md)
- [Enable Amazon S3](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/aws-s3/index.md)
- [Enable Microsoft Azure](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/azure/index.md)
- [Enable BigQuery](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/index.md)
- [Enable Datadog](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/datadog/index.md)
- [Dedicated Egress IP for Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/index.md)
- [Enable Elastic](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/elastic/index.md)
- [Enable Google Cloud Storage](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/google-cloud-storage/index.md)
- [Enable HTTP destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/http/index.md)
- [Enable IBM Cloud Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/index.md)
- [Enable IBM QRadar](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-qradar/index.md)
- [Enable Amazon Kinesis](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/kinesis/index.md)
- [Enable New Relic](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/new-relic/index.md)
- [Enable other providers](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/index.md)
- [Enable Cloudflare R2](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/index.md)
- [Enable S3-compatible endpoints](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/s3-compatible-endpoints/index.md)
- [Enable SentinelOne](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sentinelone/index.md)
- [Enable Splunk](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/splunk/index.md)
- [Enable Sumo Logic](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sumo-logic/index.md)
- [Axiom](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/third-party/axiom/index.md)
- [Exabeam](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/third-party/exabeam/index.md)
- [Sekoia](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/third-party/sekoia/index.md)
- [Taegis](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/third-party/taegis/index.md)
- [Filters](https://developers.cloudflare.com/logs/logpush/logpush-job/filters/index.md)
- [Log Output Options](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/index.md)
- [Ownership challenge FAQ](https://developers.cloudflare.com/logs/logpush/logpush-job/logpush-ownership-challenge/index.md)
- [Parse Cloudflare Logs JSON data](https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/index.md)
- [Permissions](https://developers.cloudflare.com/logs/logpush/permissions/index.md)

## Instant Logs

- [Instant Logs](https://developers.cloudflare.com/logs/instant-logs/index.md)

## Logs Engine

- [Logs Engine](https://developers.cloudflare.com/logs/r2-log-retrieval/index.md)

## Logpull

- [Logpull](https://developers.cloudflare.com/logs/logpull/index.md)
- [Additional details](https://developers.cloudflare.com/logs/logpull/additional-details/index.md)
- [Enabling log retention](https://developers.cloudflare.com/logs/logpull/enabling-log-retention/index.md)
- [Requesting logs](https://developers.cloudflare.com/logs/logpull/requesting-logs/index.md)
- [Understanding the basics](https://developers.cloudflare.com/logs/logpull/understanding-the-basics/index.md)

## Changelog

- [Changelog](https://developers.cloudflare.com/logs/changelog/index.md)
- [Audit Logs](https://developers.cloudflare.com/logs/changelog/audit-logs/index.md)
- [Logs](https://developers.cloudflare.com/logs/changelog/logs/index.md)

## Glossary

- [Glossary](https://developers.cloudflare.com/logs/glossary/index.md)

## Logpush MCP server

- [Logpush MCP server](https://developers.cloudflare.com/logs/logpush-mcp-server/index.md)

## Audit Logs MCP server

- [Audit Logs MCP server](https://developers.cloudflare.com/logs/auditlogs-mcp-server/index.md)

## FAQ

- [FAQ](https://developers.cloudflare.com/logs/faq/index.md)
- [Common calculations FAQ](https://developers.cloudflare.com/logs/faq/common-calculations/index.md): Learn more about calculating bytes served by the origin and bandwidth usage.
- [General FAQ](https://developers.cloudflare.com/logs/faq/general-faq/index.md): Review frequently asked questions about Cloudflare Logs.
- [Instant Logs FAQ](https://developers.cloudflare.com/logs/faq/instant-logs/index.md): Review frequently asked questions about Instant Logs.
- [Logpull API FAQ](https://developers.cloudflare.com/logs/faq/logpull-api/index.md): Review frequently asked questions about the Logpull API.
- [Logpush FAQ](https://developers.cloudflare.com/logs/faq/logpush/index.md): Review frequently asked questions about Logpush.
- [Random hostnames](https://developers.cloudflare.com/logs/faq/random-hostnames-partial-zones/index.md): Why unexpected hostnames appear in HTTP logs for partial zones.

## reference

- [2023-02-01 - Updates to security fields](https://developers.cloudflare.com/logs/reference/change-notices/2023-02-01-security-fields-updates/index.md)
- [ClientRequestSource field](https://developers.cloudflare.com/logs/reference/clientrequestsource/index.md)
- [Pathing status](https://developers.cloudflare.com/logs/reference/pathing-status/index.md)
- [Security fields](https://developers.cloudflare.com/logs/reference/security-fields/index.md)
- [WAF fields](https://developers.cloudflare.com/logs/reference/waf-fields/index.md)