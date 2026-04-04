# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.privateca_certificate_revocation_list.dataset.md

---
title: Certificate Revocation List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Certificate Revocation List
---

# Certificate Revocation List

A Certificate Revocation List (CRL) in Google Cloud is a list of digital certificates that have been revoked before their scheduled expiration. It is used by Certificate Authorities to inform clients that certain certificates should no longer be trusted. CRLs help maintain the security and integrity of encrypted communications by preventing the use of compromised or invalid certificates.

```
gcp.privateca_certificate_revocation_list
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| access_url           | core | string        | Output only. The location where 'pem_crl' can be accessed.                                                                                                                    |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time at which this CertificateRevocationList was created.                                                                                                    |
| datadog_display_name | core | string        |
| labels               | core | array<string> | Optional. Labels with user-defined metadata.                                                                                                                                  |
| name                 | core | string        | Identifier. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`.      |
| organization_id      | core | string        |
| parent               | core | string        |
| pem_crl              | core | string        | Output only. The PEM-encoded X.509 CRL.                                                                                                                                       |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| revision_id          | core | string        | Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string. |
| revoked_certificates | core | json          | Output only. The revoked serial numbers that appear in pem_crl.                                                                                                               |
| sequence_number      | core | int64         | Output only. The CRL sequence number that appears in pem_crl.                                                                                                                 |
| state                | core | string        | Output only. The State for this CertificateRevocationList.                                                                                                                    |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The time at which this CertificateRevocationList was updated.                                                                                                    |
| zone_id              | core | string        |
