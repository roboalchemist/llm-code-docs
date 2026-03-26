# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/hardening.md

# Source: https://docs.api7.ai/cloud/reference/hardening.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/hardening.md

# Source: https://docs.api7.ai/cloud/reference/hardening.md

# Security Hardening Reference

Infrastructure security is an important topic that organizations scrutinize to stay compliant with the latest regulatory and legal requirements. Understanding where and how sensitive information is stored is of paramount importance to implement robust security measures and safeguard against unauthorized access, data breaches, or malicious attacks in your organization.

![cloud-arch-diagram](https://static.api7.ai/uploads/2024/04/17/oVNPFzAV_whiteboard_exported_image%20%281%29.png)

This document provides a reference detailing where sensitive information in API7 Cloud is, how they are stored, and how they are protected.

## Between Data Plane (DP) and Control Plane (CP)[â](#between-data-plane-dp-and-control-plane-cp "Direct link to Between Data Plane (DP) and Control Plane (CP)")

The communication between the data plane and the control plane is secured with mTLS. Certificates used for mTLS are signed by HashiCorp Vault, encrypted with based64, and stored in K8s secrets. Access model to K8s secrets, such as RBAC, should be configured in K8s.

Ingress Controller watches certificates in K8s secrets and creates SSL resources in API7 Cloud.

Certificates are sent from the control plane encrypted. The data plane obtains the decryption key from the control plane to decrypt and use the certificates. The encryption private key is configured in `key_encrypt_salt` of the `config.yaml`.

## Data Plane (DP)[â](#data-plane-dp "Direct link to Data Plane (DP)")

### Configuration File[â](#configuration-file "Direct link to Configuration File")

The configuration file `config.yaml` usually contains a few sensitive information, such as the API key and private key used in encryption. Rotation of private keys is currently not supported.

When working with API7 Cloud, if you do not pass a customized `config.yaml` file to the Cloud CLI, it initializes the instance with the default `config.yaml` file. If you pass a customized `config.yaml` file, the Cloud CLI does not cache the `config.yaml` file.

## Control Plane (CP)[â](#control-plane-cp "Direct link to Control Plane (CP)")

### etcd[â](#etcd "Direct link to etcd")

In the control plane, the etcd proxy (gRPC gateway) distributes traffic to the etcd cluster. A subset of users share the same etcd cluster.

etcd credentials are securely kept in HashiCorp Vault.

### Database Connection Credentials[â](#database-connection-credentials "Direct link to Database Connection Credentials")

RDS connection credentials are configured in the K8s deployment YAML file.

Communicate with RDS uses TLS by default. TLS certificates are stored in the K8s secret.

### HashiCorp Vault[â](#hashicorp-vault "Direct link to HashiCorp Vault")

API7 Cloud hosts HashiCorp Vault on AWS EKS. The connection to Vault is authenticated with tokens configured in the K8s deployment YAML file and protected by mTLS.

### Plugin Resources[â](#plugin-resources "Direct link to Plugin Resources")

Certain sensitive plugin information, such as OIDC client secret and Kafka password, are stored in RDS and etcd in plaintext.

### Internal Components[â](#internal-components "Direct link to Internal Components")

Communications between other API7 internal components are all secured with mTLS, using the certificates issued by cert manager and saved in K8s secrets.
