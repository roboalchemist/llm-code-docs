# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/rds_instance_events_not_logged.md

---
title: RDS instance events not logged
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RDS instance events not logged
---

# RDS instance events not logged

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b9c524a4-fe76-4021-a6a2-cb978fb4fde1`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/log_audit)

### Description{% #description %}

All RDS instance event trackers should be set to `true`. The rule verifies the `alicloud_log_audit` resource `variable_map` contains the parameters `rds_enabled`, `rds_ti_enabled`, `rds_slow_enabled`, and `rds_perf_enabled`. It reports a `MissingAttribute` when a parameter is not defined and an `IncorrectValue` when a parameter is set to `false`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_log_audit" "example" {
  display_name = "tf-audit-test"
  aliuid       = "12345678"
  variable_map = {
    "actiontrail_enabled" = "true",
    "actiontrail_ttl" = "180",
    "actiontrail_ti_enabled" = "true",
    "oss_access_enabled" = "true",
    "oss_access_ttl" = "7",
    "oss_sync_enabled" = "true",
    "oss_sync_ttl" = "180",
    "oss_access_ti_enabled" = "true",
    "oss_metering_enabled" = "true",
    "oss_metering_ttl" = "180",
    "rds_enabled" = "true",
    "rds_audit_collection_policy" = "",
    "rds_ttl" = "180",
    "rds_ti_enabled" = "true",
    "rds_slow_enabled" = "true",
    "rds_slow_collection_policy" = "",
    "rds_slow_ttl" = "180",
    "rds_perf_enabled" = "true",
    "rds_perf_collection_policy" = "",
    "rds_perf_ttl" = "180",
    "vpc_flow_enabled" = "true",
    "vpc_flow_ttl" = "7",
    "vpc_flow_collection_policy" = "",
    "vpc_sync_enabled" = "true",
    "vpc_sync_ttl" = "180",
    "polardb_enabled" = "true",
    "polardb_audit_collection_policy" = "",
    "polardb_ttl" = "180",
    "polardb_ti_enabled" = "true",
    "polardb_slow_enabled" = "true",
    "polardb_slow_collection_policy" = "",
    "polardb_slow_ttl" = "180",
    "polardb_perf_enabled" = "true",
    "polardb_perf_collection_policy" = "",
    "polardb_perf_ttl" = "180",
    "drds_audit_enabled" = "true",
    "drds_audit_collection_policy" = "",
    "drds_audit_ttl" = "7",
    "drds_sync_enabled" = "true",
    "drds_sync_ttl" = "180",
    "drds_audit_ti_enabled" = "true",
    "slb_access_enabled" = "true",
    "slb_access_collection_policy" = "",
    "slb_access_ttl" = "7",
    "slb_sync_enabled" = "true",
    "slb_sync_ttl" = "180",
    "slb_access_ti_enabled" = "true",
    "bastion_enabled" = "true",
    "bastion_ttl" = "180",
    "bastion_ti_enabled" = "true",
    "waf_enabled" = "true",
    "waf_ttl" = "180",
    "waf_ti_enabled" = "true",
    "cloudfirewall_enabled" = "true",
    "cloudfirewall_ttl" = "180",
    "cloudfirewall_ti_enabled" = "true",
    "ddos_coo_access_enabled" = "true",
    "ddos_coo_access_ttl" = "180",
    "ddos_coo_access_ti_enabled" = "true",
    "ddos_bgp_access_enabled" = "true",
    "ddos_bgp_access_ttl" = "180",
    "ddos_dip_access_enabled" = "true",
    "ddos_dip_access_ttl" = "180",
    "ddos_dip_access_ti_enabled" = "true",
    "sas_crack_enabled" = "true",
    "sas_dns_enabled" = "true",
    "sas_http_enabled" = "true",
    "sas_local_dns_enabled" = "true",
    "sas_login_enabled" = "true",
    "sas_network_enabled" = "true",
    "sas_process_enabled" = "true",
    "sas_security_alert_enabled" = "true",
    "sas_security_hc_enabled" = "true",
    "sas_security_vul_enabled" = "true",
    "sas_session_enabled" = "true",
    "sas_snapshot_account_enabled" = "true",
    "sas_snapshot_port_enabled" = "true",
    "sas_snapshot_process_enabled" = "true",
    "sas_ttl" = "180",
    "sas_ti_enabled" = "true",
    "apigateway_enabled" = "true",
    "apigateway_ttl" = "180",
    "apigateway_ti_enabled" = "true",
    "nas_enabled" = "true",
    "nas_ttl" = "180",
    "nas_ti_enabled" = "true",
    "appconnect_enabled" = "true",
    "appconnect_ttl" = "180",
    "cps_enabled" = "true",
    "cps_ttl" = "180",
    "cps_ti_enabled" = "true",
    "k8s_audit_enabled" = "true",
    "k8s_audit_collection_policy" = "",
    "k8s_audit_ttl" = "180",
    "k8s_event_enabled" = "true",
    "k8s_event_collection_policy" = "",
    "k8s_event_ttl" = "180",
    "k8s_ingress_enabled" = "true",
    "k8s_ingress_collection_policy" = "",
    "k8s_ingress_ttl" = "180",
    "appconnect_ti_enabled":"true"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_log_audit" "example" {
  display_name = "tf-audit-test"
  aliuid       = "12345678"
  variable_map = {
    "actiontrail_enabled" = "true",
    "actiontrail_ttl" = "180",
    "actiontrail_ti_enabled" = "true",
    "oss_access_enabled" = "true",
    "oss_access_ttl" = "7",
    "oss_sync_enabled" = "true",
    "oss_sync_ttl" = "180",
    "oss_access_ti_enabled" = "true",
    "oss_metering_enabled" = "true",
    "oss_metering_ttl" = "180",
    "rds_audit_collection_policy" = "",
    "rds_ttl" = "180",
    "rds_ti_enabled" = "true",
    "rds_slow_enabled" = "true",
    "rds_slow_collection_policy" = "",
    "rds_slow_ttl" = "180",
    "rds_perf_enabled" = "true",
    "rds_perf_collection_policy" = "",
    "rds_perf_ttl" = "180",
    "vpc_flow_enabled" = "true",
    "vpc_flow_ttl" = "7",
    "vpc_flow_collection_policy" = "",
    "vpc_sync_enabled" = "true",
    "vpc_sync_ttl" = "180",
    "polardb_enabled" = "true",
    "polardb_audit_collection_policy" = "",
    "polardb_ttl" = "180",
    "polardb_ti_enabled" = "true",
    "polardb_slow_enabled" = "true",
    "polardb_slow_collection_policy" = "",
    "polardb_slow_ttl" = "180",
    "polardb_perf_enabled" = "true",
    "polardb_perf_collection_policy" = "",
    "polardb_perf_ttl" = "180",
    "drds_audit_enabled" = "true",
    "drds_audit_collection_policy" = "",
    "drds_audit_ttl" = "7",
    "drds_sync_enabled" = "true",
    "drds_sync_ttl" = "180",
    "drds_audit_ti_enabled" = "true",
    "slb_access_enabled" = "true",
    "slb_access_collection_policy" = "",
    "slb_access_ttl" = "7",
    "slb_sync_enabled" = "true",
    "slb_sync_ttl" = "180",
    "slb_access_ti_enabled" = "true",
    "bastion_enabled" = "true",
    "bastion_ttl" = "180",
    "bastion_ti_enabled" = "true",
    "waf_enabled" = "true",
    "waf_ttl" = "180",
    "waf_ti_enabled" = "true",
    "cloudfirewall_enabled" = "true",
    "cloudfirewall_ttl" = "180",
    "cloudfirewall_ti_enabled" = "true",
    "ddos_coo_access_enabled" = "true",
    "ddos_coo_access_ttl" = "180",
    "ddos_coo_access_ti_enabled" = "true",
    "ddos_bgp_access_enabled" = "true",
    "ddos_bgp_access_ttl" = "180",
    "ddos_dip_access_enabled" = "true",
    "ddos_dip_access_ttl" = "180",
    "ddos_dip_access_ti_enabled" = "true",
    "sas_crack_enabled" = "true",
    "sas_dns_enabled" = "true",
    "sas_http_enabled" = "true",
    "sas_local_dns_enabled" = "true",
    "sas_login_enabled" = "true",
    "sas_network_enabled" = "true",
    "sas_process_enabled" = "true",
    "sas_security_alert_enabled" = "true",
    "sas_security_hc_enabled" = "true",
    "sas_security_vul_enabled" = "true",
    "sas_session_enabled" = "true",
    "sas_snapshot_account_enabled" = "true",
    "sas_snapshot_port_enabled" = "true",
    "sas_snapshot_process_enabled" = "true",
    "sas_ttl" = "180",
    "sas_ti_enabled" = "true",
    "apigateway_enabled" = "true",
    "apigateway_ttl" = "180",
    "apigateway_ti_enabled" = "true",
    "nas_enabled" = "true",
    "nas_ttl" = "180",
    "nas_ti_enabled" = "true",
    "appconnect_enabled" = "true",
    "appconnect_ttl" = "180",
    "cps_enabled" = "true",
    "cps_ttl" = "180",
    "cps_ti_enabled" = "true",
    "k8s_audit_enabled" = "true",
    "k8s_audit_collection_policy" = "",
    "k8s_audit_ttl" = "180",
    "k8s_event_enabled" = "true",
    "k8s_event_collection_policy" = "",
    "k8s_event_ttl" = "180",
    "k8s_ingress_enabled" = "true",
    "k8s_ingress_collection_policy" = "",
    "k8s_ingress_ttl" = "180"
  }
}
```

```terraform
resource "alicloud_log_audit" "example" {
  display_name = "tf-audit-test"
  aliuid       = "12345678"
  variable_map = {
    "actiontrail_enabled" = "true",
    "actiontrail_ttl" = "180",
    "actiontrail_ti_enabled" = "true",
    "oss_access_enabled" = "true",
    "oss_access_ttl" = "7",
    "oss_sync_enabled" = "true",
    "oss_sync_ttl" = "180",
    "oss_access_ti_enabled" = "true",
    "oss_metering_enabled" = "true",
    "oss_metering_ttl" = "180",
    "rds_enabled" = "false",
    "rds_audit_collection_policy" = "",
    "rds_ttl" = "180",
    "rds_ti_enabled" = "true",
    "rds_slow_enabled" = "true",
    "rds_slow_collection_policy" = "",
    "rds_slow_ttl" = "180",
    "rds_perf_enabled" = "true",
    "rds_perf_collection_policy" = "",
    "rds_perf_ttl" = "180",
    "vpc_flow_enabled" = "true",
    "vpc_flow_ttl" = "7",
    "vpc_flow_collection_policy" = "",
    "vpc_sync_enabled" = "true",
    "vpc_sync_ttl" = "180",
    "polardb_enabled" = "true",
    "polardb_audit_collection_policy" = "",
    "polardb_ttl" = "180",
    "polardb_ti_enabled" = "true",
    "polardb_slow_enabled" = "true",
    "polardb_slow_collection_policy" = "",
    "polardb_slow_ttl" = "180",
    "polardb_perf_enabled" = "true",
    "polardb_perf_collection_policy" = "",
    "polardb_perf_ttl" = "180",
    "drds_audit_enabled" = "true",
    "drds_audit_collection_policy" = "",
    "drds_audit_ttl" = "7",
    "drds_sync_enabled" = "true",
    "drds_sync_ttl" = "180",
    "drds_audit_ti_enabled" = "true",
    "slb_access_enabled" = "true",
    "slb_access_collection_policy" = "",
    "slb_access_ttl" = "7",
    "slb_sync_enabled" = "true",
    "slb_sync_ttl" = "180",
    "slb_access_ti_enabled" = "true",
    "bastion_enabled" = "true",
    "bastion_ttl" = "180",
    "bastion_ti_enabled" = "true",
    "waf_enabled" = "true",
    "waf_ttl" = "180",
    "waf_ti_enabled" = "true",
    "cloudfirewall_enabled" = "true",
    "cloudfirewall_ttl" = "180",
    "cloudfirewall_ti_enabled" = "true",
    "ddos_coo_access_enabled" = "true",
    "ddos_coo_access_ttl" = "180",
    "ddos_coo_access_ti_enabled" = "true",
    "ddos_bgp_access_enabled" = "true",
    "ddos_bgp_access_ttl" = "180",
    "ddos_dip_access_enabled" = "true",
    "ddos_dip_access_ttl" = "180",
    "ddos_dip_access_ti_enabled" = "true",
    "sas_crack_enabled" = "true",
    "sas_dns_enabled" = "true",
    "sas_http_enabled" = "true",
    "sas_local_dns_enabled" = "true",
    "sas_login_enabled" = "true",
    "sas_network_enabled" = "true",
    "sas_process_enabled" = "true",
    "sas_security_alert_enabled" = "true",
    "sas_security_hc_enabled" = "true",
    "sas_security_vul_enabled" = "true",
    "sas_session_enabled" = "true",
    "sas_snapshot_account_enabled" = "true",
    "sas_snapshot_port_enabled" = "true",
    "sas_snapshot_process_enabled" = "true",
    "sas_ttl" = "180",
    "sas_ti_enabled" = "true",
    "apigateway_enabled" = "true",
    "apigateway_ttl" = "180",
    "apigateway_ti_enabled" = "true",
    "nas_enabled" = "true",
    "nas_ttl" = "180",
    "nas_ti_enabled" = "true",
    "appconnect_enabled" = "true",
    "appconnect_ttl" = "180",
    "cps_enabled" = "true",
    "cps_ttl" = "180",
    "cps_ti_enabled" = "true",
    "k8s_audit_enabled" = "true",
    "k8s_audit_collection_policy" = "",
    "k8s_audit_ttl" = "180",
    "k8s_event_enabled" = "true",
    "k8s_event_collection_policy" = "",
    "k8s_event_ttl" = "180",
    "k8s_ingress_enabled" = "true",
    "k8s_ingress_collection_policy" = "",
    "k8s_ingress_ttl" = "180"
    "appconnect_ti_enabled":"false"
  }
}
```
