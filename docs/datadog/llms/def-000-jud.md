# Source: https://docs.datadoghq.com/security/default_rules/def-000-jud.md

---
title: >-
  Cloud DNS DNSSEC should use a zone-signing key with a secure algorithm other
  than RSASHA1
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cloud DNS DNSSEC should use a
  zone-signing key with a secure algorithm other than RSASHA1
---

# Cloud DNS DNSSEC should use a zone-signing key with a secure algorithm other than RSASHA1

## Description{% #description %}

Certificate resource records may use the domain name system security extensions (DNSSEC) algorithm numbers in this registry. DNSSEC zone signing and transaction security mechanisms (SIG(0) and TSIG) make use of subsets of these algorithms. Use the Google recommended algorithms for key signing.

**Note**: The SHA1 algorithm has been removed from general use by Google, and if being used, needs to be safe listed on a project basis by Google, which require a Google Cloud support contract.

## Rationale{% #rationale %}

Use DNSSEC algorithm numbers from this registry in certificate resource records. When enabling DNSSEC for a managed zone or creating a managed zone with DNSSEC, select the DNSSEC signing algorithms and the denial-of-existence type. Changing the DNSSEC settings is only effective for a managed zone if DNSSEC is not already enabled. If you need to change the settings for a managed zone where it has been enabled, turn DNSSEC off and then re-enable it with different settings.

**note**: RSASHA1 zone-signing support may be required for compatibility reasons. **note**: The remediation CLI works well with gcloud-cli version 221.0.0 and later.

## Remediation{% #remediation %}

1. If you need to change the settings for a managed zone where it has been enabled, DNSSEC must be turned off and then re-enabled with different settings. To turn off DNSSEC, run this command:

   ```
   gcloud dns managed-zones update ZONE_NAME --dnssec-state off
   ```

1. To update zone-signing for a reported managed DNS Zone, run the following command:

   ```
   gcloud dns managed-zones update ZONE_NAME --dnssec-state on --ksk-algorithm KSK_ALGORITHM --ksk-key-length KSK_KEY_LENGTH --zsk-algorithm ZSK_ALGORITHM --zsk-key-length ZSK_KEY_LENGTH --denial-of-existence DENIAL_OF_EXISTENCE
   ```

## References{% #references %}

1. [https://cloud.google.com/dns/dnssec-advanced#advanced_signing_options](https://cloud.google.com/dns/dnssec-advanced#advanced_signing_options)
