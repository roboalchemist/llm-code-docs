# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_client_certificate.dataset.md

---
title: API Gateway Client Certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Client Certificate
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigateway_client_certificate.dataset/index.html
---

# API Gateway Client Certificate

An API Gateway Client Certificate in AWS is a resource that provides a client-side SSL/TLS certificate for authenticating requests to your API. It is typically used when enabling mutual TLS between clients and API Gateway, ensuring secure communication by verifying both the client and the server.

```
aws.apigateway_client_certificate
```

## Fields

| Title                   | ID   | Type      | Data Type                                                                                                                                     | Description |
| ----------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string    |
| account_id              | core | string    |
| client_certificate_arn  | core | string    |
| client_certificate_id   | core | string    | The identifier of the client certificate.                                                                                                     |
| created_date            | core | timestamp | The timestamp when the client certificate was created.                                                                                        |
| description             | core | string    | The description of the client certificate.                                                                                                    |
| expiration_date         | core | timestamp | The timestamp when the client certificate will expire.                                                                                        |
| pem_encoded_certificate | core | string    | The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint . |
| tags                    | core | hstore    |
