# Source: https://docs.sandboxes.cloud/docs/security.md

## Security

### Data Encryption

All communication between the Crafting Sandbox System and the Internet is encrypted via HTTPS and TLS 1.2. The internal communication between the user's workloads and the system is encrypted via mTLS (with certificate verified mutually by both parties). The HTTP services exposed to the Internet from the user's workload is always using HTTPS and TLS 1.2 and by default protected by a Single-Sign-On system.\
All user data is encrypted at rest (via the mechanism provided by the cloud providers - Google Cloud). Highly sensitive information including user-provided secrets, keypairs are encrypted and secured in Vault ([https://vaultproject.io](https://vaultproject.io)) which is sealed using the Key Management System from the cloud provider.

### Vulnerability Scanning

Continuous vulnerability scanning is adopted on all the components used internally by the system and followed up by our internal remediation process.

### Availability

User information is continuously backed up and can be restored point-in-time. The data generated in user's workloads is backed up using the cloud provider's default configuration, and this doesn't cover the case that users explicitly delete the data.

### Thirdparty Auditing

We employ third-party experts to perform penetration tests annually.

### Internal Control

All full-time employees are required to complete security training. All people who have access to production system undergo background checks.
