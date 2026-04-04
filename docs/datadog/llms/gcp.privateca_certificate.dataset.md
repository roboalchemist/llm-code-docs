# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.privateca_certificate.dataset.md

---
title: Certificate Authority Service Certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Certificate Authority Service
  Certificate
---

# Certificate Authority Service Certificate

Certificate Authority Service Certificate in Google Cloud is a managed resource used to create, manage, and deploy X.509 certificates issued by a private or public certificate authority. It enables secure communication between services and users by providing identity verification and encryption. This resource integrates with Google Cloud's Certificate Authority Service to automate certificate lifecycle management, including issuance, renewal, and revocation.

```
gcp.privateca_certificate
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                    | Description |
| ---------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                         | core | string        |
| ancestors                    | core | array<string> |
| certificate_description      | core | json          | Output only. A structured description of the issued X.509 certificate.                                                                                                                                                                                                                                                                                       |
| certificate_template         | core | string        | Immutable. The resource name for a CertificateTemplate used to issue this certificate, in the format `projects/*/locations/*/certificateTemplates/*`. If this is specified, the caller must have the necessary permission to use this template. If this is omitted, no template will be used. This template must be in the same location as the Certificate. |
| config                       | core | json          | Immutable. A description of the certificate and key that does not require X.509 or ASN.1.                                                                                                                                                                                                                                                                    |
| create_time                  | core | timestamp     | Output only. The time at which this Certificate was created.                                                                                                                                                                                                                                                                                                 |
| datadog_display_name         | core | string        |
| issuer_certificate_authority | core | string        | Output only. The resource name of the issuing CertificateAuthority in the format `projects/*/locations/*/caPools/*/certificateAuthorities/*`.                                                                                                                                                                                                                |
| labels                       | core | array<string> | Optional. Labels with user-defined metadata.                                                                                                                                                                                                                                                                                                                 |
| lifetime                     | core | string        | Required. Immutable. The desired lifetime of a certificate. Used to create the "not_before_time" and "not_after_time" fields inside an X.509 certificate. Note that the lifetime may be truncated if it would extend past the life of any certificate authority in the issuing chain.                                                                        |
| name                         | core | string        | Identifier. The resource name for this Certificate in the format `projects/*/locations/*/caPools/*/certificates/*`.                                                                                                                                                                                                                                          |
| organization_id              | core | string        |
| parent                       | core | string        |
| pem_certificate              | core | string        | Output only. The pem-encoded, signed X.509 certificate.                                                                                                                                                                                                                                                                                                      |
| pem_certificate_chain        | core | array<string> | Output only. The chain that may be used to verify the X.509 certificate. Expected to be in issuer-to-root order according to RFC 5246.                                                                                                                                                                                                                       |
| pem_csr                      | core | string        | Immutable. A pem-encoded X.509 certificate signing request (CSR).                                                                                                                                                                                                                                                                                            |
| project_id                   | core | string        |
| project_number               | core | string        |
| region_id                    | core | string        |
| resource_name                | core | string        |
| revocation_details           | core | json          | Output only. Details regarding the revocation of this Certificate. This Certificate is considered revoked if and only if this field is present.                                                                                                                                                                                                              |
| subject_mode                 | core | string        | Immutable. Specifies how the Certificate's identity fields are to be decided. If this is omitted, the `DEFAULT` subject mode will be used.                                                                                                                                                                                                                   |
| tags                         | core | hstore_csv    |
| update_time                  | core | timestamp     | Output only. The time at which this Certificate was updated.                                                                                                                                                                                                                                                                                                 |
| zone_id                      | core | string        |
