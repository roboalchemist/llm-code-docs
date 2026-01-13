# Secret Management Tools - Quick Reference Guide

Fast lookup guide for secret management solutions. For detailed information, see `SECRET_MANAGEMENT_TOOLS_COMPREHENSIVE.md`.

---

## Quick Selection by Use Case

### I'm using AWS
```
Primary: AWS Secrets Manager
Alternatives: HashiCorp Vault, CredStash, AWS Systems Manager Parameter Store
```

### I'm using Azure
```
Primary: Azure Key Vault
Alternatives: HashiCorp Vault, Akeyless
```

### I'm using Google Cloud
```
Primary: GCP Secret Manager
Alternatives: HashiCorp Vault, Akeyless
```

### I want multi-cloud flexibility
```
Primary: HashiCorp Vault
Alternatives: Akeyless, Infisical
```

### I'm running Kubernetes
```
In-cluster: Sealed Secrets + SOPS
External: HashiCorp Vault with K8s auth
GitOps: Flux CD + Sealed Secrets or ArgoCD + SOPS
```

### I'm a developer (startup/small team)
```
Primary: Doppler or Infisical
Backup: dotenv or direnv for local development
```

### I need to detect secrets in code
```
Commercial (full coverage): GitGuardian
Open-source (free): TruffleHog or GitLeaks
GitHub-only (built-in): GitHub Advanced Security
```

### I need compliance/audit trails
```
Enterprise: CyberArk Conjur, Keeper, Akeyless
Self-hosted: HashiCorp Vault Enterprise
```

### I need privileged access management (PAM)
```
Enterprise: CyberArk Conjur, Thycotic, BeyondTrust
```

### I want open-source only
```
Self-hosted: HashiCorp Vault, Infisical, SOPS, Sealed Secrets
Password manager: Vaultwarden (Bitwarden)
Scanning: TruffleHog, GitLeaks
```

---

## Tool Categories at a Glance

### Cloud Native (SaaS) - No Infrastructure
- AWS Secrets Manager
- Azure Key Vault
- GCP Secret Manager
- Doppler
- Akeyless
- Keeper Secrets Manager
- 1Password Business

### Self-Managed Platforms (DIY)
- HashiCorp Vault
- CyberArk Conjur
- Infisical (self-hosted option)
- Vaultwarden
- Keywhiz

### Secret Scanning/Detection (Find Secrets in Code)
- GitGuardian (Commercial)
- TruffleHog (Open-source)
- GitLeaks (Open-source)
- GitHub Advanced Security (Platform-native)
- Snyk (Multi-tool)

### Kubernetes Specific
- Sealed Secrets
- SOPS
- Vault (K8s auth)
- Kubernetes native Secrets (basic)

### Environment Variables
- dotenv / python-dotenv
- direnv
- EnvKey
- Cloud provider parameter stores

### Git-Encrypted (Version Control Friendly)
- Mozilla SOPS
- Sealed Secrets
- Infisical (with Git backend)

---

## Cost Comparison Matrix

### Free/Low Cost
| Tool | Cost | Notes |
|------|------|-------|
| TruffleHog | Free | Open-source, fully featured |
| GitLeaks | Free | Open-source, easy integration |
| Sealed Secrets | Free | Open-source, K8s only |
| SOPS | Free | Open-source, CLI tool |
| HashiCorp Vault (OSS) | Free | Open-source but requires ops |
| Infisical (OSS) | Free | Open-source, can self-host |
| Vaultwarden | Free | Open-source, lightweight |
| dotenv | Free | Open-source, simple |
| direnv | Free | Open-source, shell extension |

### Under $100/month (small team)
| Tool | Cost | Notes |
|------|------|-------|
| Doppler | Free-$99/mo | Excellent UX, generous free tier |
| Infisical | $99+/mo | Cloud tier, self-host free |
| GitGuardian | Custom | Has startup tier |
| Akeyless | Free-Enterprise | Free tier available |

### Enterprise Pricing (custom quote)
| Tool | Cost | Notes |
|------|------|-------|
| HashiCorp Vault Enterprise | Custom | Per-node or per-secret |
| CyberArk Conjur | Custom | Enterprise compliance |
| Keeper | Custom | Custom per-org |
| Thycotic Secret Server | Custom | Per-user or per-secret |
| AWS Secrets Manager | Per secret + API | Can be very cost-effective at scale |
| Azure Key Vault | Per API call | ~$0.03/call, very cheap |
| GCP Secret Manager | Per secret/month | ~$0.06/secret |

---

## Deployment Models

### Cloud SaaS (Easiest)
- Doppler, Infisical Cloud, Keeper, Akeyless, 1Password Business
- **Pros**: No infrastructure, automatic updates
- **Cons**: Vendor lock-in, cost scales with usage

### Self-Hosted (Most Control)
- HashiCorp Vault, Vaultwarden, SOPS, Sealed Secrets
- **Pros**: Full control, no vendor lock-in, meets compliance
- **Cons**: Operational overhead, security responsibility

### Cloud Provider Native (AWS/Azure/GCP)
- AWS Secrets Manager, Azure Key Vault, GCP Secret Manager
- **Pros**: Native integration, pay-as-you-go
- **Cons**: Vendor lock-in, multi-cloud is harder

### Hybrid (Best of Both)
- Infisical (cloud + self-hosted), HashiCorp Vault (self-hosted with cloud features)
- **Pros**: Flexibility, can migrate
- **Cons**: Complex setup

---

## Feature Checklist

### Must-Have Features
- [ ] Encryption at rest
- [ ] Encryption in transit (TLS/HTTPS)
- [ ] Access control (who can see what)
- [ ] Audit logging (what was accessed when)
- [ ] Secret rotation capability

### Important Features
- [ ] Multiple authentication methods
- [ ] API/CLI access
- [ ] Version control of secrets
- [ ] High availability
- [ ] Disaster recovery

### Nice-to-Have Features
- [ ] Web UI
- [ ] Dynamic secret generation
- [ ] Automated compliance reporting
- [ ] Machine learning for threat detection
- [ ] Multi-cloud support
- [ ] GitOps integration

---

## Integration Priority List

### Must Support
1. Your primary cloud provider (AWS/Azure/GCP) or Kubernetes
2. Your VCS (GitHub, GitLab, Bitbucket)
3. Your CI/CD pipeline (Jenkins, GitHub Actions, GitLab CI)
4. Your application runtime (Docker, Kubernetes, Lambda, etc.)

### Should Support
5. Infrastructure-as-Code tools (Terraform, Ansible)
6. Your programming language SDKs
7. Your monitoring/logging platform
8. Your compliance/audit tools

### Nice-to-Have
9. IDE integrations (VS Code, JetBrains)
10. Slack/Teams notifications
11. Specific application frameworks

---

## Comparison: Popular Tools Head-to-Head

| Feature | HashiCorp Vault | Doppler | Infisical | AWS Secrets Mgr | Sealed Secrets |
|---------|-----------------|---------|-----------|-----------------|----------------|
| **Ease of Setup** | Hard | Very Easy | Easy | Medium | Medium |
| **Price** | Free/Enterprise | Free-$99+ | Free/OSS | Pay-per-use | Free |
| **Multi-cloud** | Yes | No | Yes | AWS only | N/A (K8s) |
| **Git-friendly** | No | No | Yes | No | Yes |
| **Secret Rotation** | Yes | Yes | Yes | Yes | No |
| **Kubernetes** | Yes | Limited | Yes | Limited | Yes |
| **Audit Logging** | Excellent | Good | Good | Good | Limited |
| **Open-source** | Yes (BSL) | No | Yes (MIT) | No | Yes |
| **Learning curve** | Steep | Flat | Gentle | Medium | Medium |
| **Community size** | Large | Medium | Growing | Very Large | Large |
| **Enterprise features** | Excellent | Good | Good | Good | Limited |

---

## Red Flags (What to Avoid)

- Storing secrets in plain text in version control
- Storing secrets in environment variables without encryption
- Hardcoding secrets in application code
- Using base64 encoding as encryption (it's not)
- No audit trails or access logs
- No access control (everyone can see everything)
- No secret rotation mechanism
- No TLS/HTTPS for data in transit
- Sharing secrets via email, Slack, or unencrypted channels
- Using expired or weak encryption algorithms
- No disaster recovery plan
- Lack of multi-factor authentication for access

---

## Getting Started Checklist

### Phase 1: Immediate (This Week)
- [ ] Stop committing secrets to Git
- [ ] Remove existing secrets from Git history
- [ ] Add pre-commit hooks to prevent future commits

### Phase 2: Short-term (This Month)
- [ ] Choose a secrets management tool based on your stack
- [ ] Set up basic secret storage
- [ ] Migrate high-risk secrets (API keys, DB passwords)
- [ ] Enable audit logging

### Phase 3: Medium-term (This Quarter)
- [ ] Migrate all secrets to the new system
- [ ] Implement secret rotation
- [ ] Set up secret scanning in CI/CD
- [ ] Train team on new workflows

### Phase 4: Long-term (This Year)
- [ ] Implement advanced features (dynamic secrets, compliance)
- [ ] Regular security audits
- [ ] Disaster recovery testing
- [ ] Performance optimization

---

## Tools by Language/Framework

### Python
- `python-dotenv` for development
- Infisical (multi-language SDK)
- HashiCorp Vault (multiple backends)

### Node.js / JavaScript
- Doppler (JavaScript SDK)
- Infisical (Node.js SDK)
- dotenv packages (npm)

### Java
- HashiCorp Vault
- Keywhiz (Square's solution)
- AWS Secrets Manager SDK

### Go
- HashiCorp Vault (native)
- AWS Secrets Manager SDK
- SOPS (written in Go)

### Kubernetes/DevOps
- Sealed Secrets
- SOPS
- HashiCorp Vault with Kubernetes auth
- External Secrets Operator (works with many backends)

### Containerized Applications
- HashiCorp Vault (Docker-native)
- Infisical (Docker integration)
- AWS Secrets Manager + IAM roles

---

## Key Terms Glossary

| Term | Definition |
|------|-----------|
| **Secret** | Sensitive data like API keys, passwords, certificates |
| **Rotation** | Regularly changing secrets to reduce compromise impact |
| **Audit log** | Record of who accessed what secret and when |
| **ACL** | Access Control List - defines who can access what |
| **Encryption at rest** | Data encrypted when stored |
| **Encryption in transit** | Data encrypted when moving over network |
| **KMS** | Key Management Service (AWS, GCP, Azure) |
| **HSM** | Hardware Security Module - physical encryption device |
| **PAM** | Privileged Access Management - managing admin accounts |
| **Compliance** | Meeting regulatory requirements (HIPAA, SOC 2, etc.) |
| **Dynamic secrets** | Automatically generated temporary credentials |
| **Sealed secrets** | Encrypted secrets stored in version control |
| **GitOps** | Git as source of truth for infrastructure |
| **Zero-trust** | Trust nothing by default, verify everything |

---

## Recommended Reading

1. **OWASP Secrets Management Cheat Sheet** - Industry best practices
2. **CWE-798**: Use of Hard-Coded Credentials - What NOT to do
3. **Cloud Provider Security Best Practices** - For cloud-native setups
4. **HashiCorp Vault Documentation** - Deep dive on enterprise secrets
5. **Kubernetes Secrets Management** - For container orchestration

---

## Quick Links to Tools

### Cloud Providers
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [Azure Key Vault](https://azure.microsoft.com/services/key-vault/)
- [GCP Secret Manager](https://cloud.google.com/secret-manager)

### Commercial Platforms
- [Doppler](https://www.doppler.com)
- [Infisical](https://infisical.com)
- [Akeyless](https://www.akeyless.io)
- [GitGuardian](https://www.gitguardian.com)

### Open-Source
- [HashiCorp Vault](https://www.vaultproject.io)
- [SOPS](https://github.com/mozilla/sops)
- [Sealed Secrets](https://sealed-secrets.dev)
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- [GitLeaks](https://github.com/gitleaks/gitleaks)

---

**Last Updated**: 2026-01-01
**Document Type**: Quick Reference
**For Details**: See `SECRET_MANAGEMENT_TOOLS_COMPREHENSIVE.md`
