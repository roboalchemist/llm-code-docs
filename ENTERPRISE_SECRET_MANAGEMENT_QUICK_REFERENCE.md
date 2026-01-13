# Enterprise Secret Management Quick Reference Guide

**Purpose**: Rapid decision-making guide for selecting secret management solutions.

---

## Quick Start Decision Tree

### Are you using Kubernetes?
- **YES** → Start with [Kubernetes-First Solutions](#kubernetes-first-solutions)
- **NO** → Skip to [Problem-Based Selection](#problem-based-selection)

### Single Cloud or Multi-Cloud?
- **Single Cloud** → Use cloud-native (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager)
- **Multi-Cloud** → Use HashiCorp Vault, Akeyless, Keeper, or Doppler
- **On-Prem + Cloud** → Use Vault Enterprise or commercial alternatives

### What's Your Primary Challenge?

## Problem-Based Selection

### Problem: Managing Privileged Access for Humans & Services
**Top 3 Solutions**:
1. **CyberArk** - Best-in-class, market leader
2. **BeyondTrust** - Strong alternative, VPN-less remote access
3. **Teleport** - Open-source zero-trust alternative

**Try First**: CyberArk (enterprise) or Teleport (open-source)

---

### Problem: Rotating API Keys & Database Credentials Automatically
**Top 3 Solutions**:
1. **AWS Secrets Manager** (AWS-only) or **HashiCorp Vault** (multi-cloud)
2. **Akeyless** - AI-driven rotation scheduling
3. **Keeper Secrets Manager** - Enterprise automation

**Try First**: AWS Secrets Manager (if AWS) or Vault (if multi-cloud)

---

### Problem: Managing Secrets in Kubernetes
**Top 3 Solutions**:
1. **External Secrets Operator** (ESO) - Multi-backend, industry standard
2. **Sealed Secrets** - Git-friendly, GitOps-native
3. **Vault Secrets Operator** - Vault-specific

**Try First**: ESO (most flexible) or Sealed Secrets (GitOps teams)

---

### Problem: Unified API Key Management Across Multiple Gateways
**Top 3 Solutions**:
1. **DigitalAPI.ai** - Multi-gateway specialist
2. **Kong Konnect** (Kong users) or **Apigee** (Google Cloud)
3. **Tyk** - Open-source alternative

**Try First**: DigitalAPI.ai (multi-gateway) or Kong/Apigee (ecosystem lock-in acceptable)

---

### Problem: Preventing Secrets from Being Committed to Git
**Top 3 Solutions**:
1. **Gitguardian** - Real-time scanning, compliance
2. **TruffleHog** - Open-source, Git history scanning
3. **Snyk** - Comprehensive DevSecOps platform

**Try First**: Gitguardian (enterprise) or TruffleHog (open-source)

---

### Problem: Implementing Zero-Trust Infrastructure
**Top 3 Solutions**:
1. **Teleport** - Complete infrastructure identity platform
2. **Boundary** (Vault integration) - Secure access without VPN
3. **Istio/Linkerd** - Service mesh mutual TLS

**Try First**: Teleport (complete solution) or Boundary (simpler)

---

### Problem: Eliminating Long-Lived Secrets in CI/CD
**Top 3 Solutions**:
1. **OIDC Workload Identity** - GitHub Actions, GitLab CI, CircleCI
2. **Aembit** - Commercial secretless CI/CD
3. **HashiCorp Vault** - Dynamic CI credentials

**Try First**: Native OIDC support (GitHub/GitLab/CircleCI) - it's free

---

### Problem: Compliance Requirements (HIPAA/FIPS/SOC 2/PCI-DSS)
**Top 3 Solutions**:
1. **CyberArk** - All major compliance certifications
2. **Teleport** - HIPAA, FIPS 140-2, SOC 2 built-in
3. **ManageEngine PAM360** - Affordable compliance automation

**Try First**: CyberArk (enterprise) or Teleport (open-source + compliance)

---

## Kubernetes-First Solutions

### For Small Teams (10-50 developers)
1. **Sealed Secrets** - Simplest, Git-native
2. **Doppler** - Cloud-hosted, easy UI
3. **HashiCorp Vault + Injector** - More complex but powerful

**Recommended**: Sealed Secrets + External Secrets Operator

---

### For Growing Teams (50-500 developers)
1. **External Secrets Operator** + **HashiCorp Vault**
2. **External Secrets Operator** + **AWS Secrets Manager**
3. **Akeyless**

**Recommended**: ESO + Vault (most flexible)

---

### For Large Enterprises (500+ developers)
1. **HashiCorp Vault Enterprise** + **ESO**
2. **CyberArk** + **Kubernetes Integration**
3. **Teleport** + **Vault**

**Recommended**: Vault Enterprise + ESO + strong RBAC

---

## Budget-Based Selection

### Free/Open-Source
- **Vault** - Most flexible
- **Teleport** - Complete infrastructure identity
- **Boundary** - Secure access
- **Sealed Secrets** - Kubernetes GitOps
- **ESO** - Kubernetes multi-backend
- **SPIFFE/SPIRE** - Workload identity

---

### Startup Budget ($100-500/month)
- **Doppler** - Generous free tier, pay as you grow
- **Tyk** - Open-source or low-cost SaaS
- **Infisical** - Cloud or self-hosted
- **1Password Teams** - $20-50/month with secret sharing

---

### Growth Budget ($500-5,000/month)
- **Akeyless** - ML-driven rotation
- **Keeper Secrets Manager** - Enterprise automation
- **Kong Konnect** - API gateway + keys
- **AWS/Azure/GCP** native managers - Pay-per-use

---

### Enterprise Budget (5,000+/month)
- **CyberArk** - Full PAM suite
- **BeyondTrust** - Complete PASM
- **Teleport Enterprise** - Full platform
- **HashiCorp Vault Enterprise** - Full platform
- **ManageEngine PAM360** - Mid-market alternative

---

## Technology Stack Matching

### AWS-Centric
1. **Primary**: AWS Secrets Manager (native)
2. **Alternative**: HashiCorp Vault (multi-cloud option)
3. **Advanced**: Akeyless (zero-knowledge)

---

### Azure-Centric
1. **Primary**: Azure Key Vault (native)
2. **Alternative**: HashiCorp Vault
3. **Advanced**: Keeper Secrets Manager

---

### GCP-Centric
1. **Primary**: Google Cloud Secret Manager (native)
2. **Alternative**: HashiCorp Vault
3. **Advanced**: Akeyless

---

### Multi-Cloud
1. **Primary**: HashiCorp Vault
2. **Alternative**: Akeyless
3. **For K8s**: External Secrets Operator

---

### On-Premises / Hybrid
1. **Primary**: HashiCorp Vault (self-hosted)
2. **Alternative**: Boundary + Vault
3. **Legacy PAM**: One Identity Safeguard

---

### Kubernetes-Only
1. **Primary**: External Secrets Operator
2. **Alternative**: Sealed Secrets (GitOps)
3. **Advanced**: Vault Secrets Operator (Vault users)

---

## Top 10 Tools by Category (Ranked)

### Privileged Access Management
1. CyberArk
2. BeyondTrust
3. Teleport
4. ManageEngine PAM360
5. Boundary
6. JumpCloud
7. StrongDM
8. Delinea
9. Heimdal
10. miniOrange

### Secret Rotation & Lifecycle
1. HashiCorp Vault
2. AWS Secrets Manager (AWS)
3. Akeyless
4. Keeper Secrets Manager
5. Azure Key Vault (Azure)
6. Doppler
7. Google Cloud Secret Manager (GCP)
8. 1Password ESC
9. Delinea Secret Server
10. Knox

### API Key Management
1. DigitalAPI.ai
2. Apigee
3. Kong Konnect
4. MuleSoft Anypoint
5. Tyk
6. AWS API Gateway
7. Okta
8. Azure API Management
9. 3scale
10. SwaggerHub

### Kubernetes Secrets
1. External Secrets Operator
2. Sealed Secrets
3. Vault Secrets Operator
4. Secret Store CSI Driver
5. Vault Agent Injector
6. cert-manager
7. KEDA
8. Sealed Secrets + ESO combo
9. Infisical
10. Akeyless K8s Integration

### Open-Source Tools
1. HashiCorp Vault
2. Teleport
3. Boundary
4. Infisical
5. SPIFFE/SPIRE
6. Sealed Secrets
7. External Secrets Operator
8. Cilium
9. Open Policy Agent
10. TruffleHog

### Secrets Scanning/Detection
1. Gitguardian
2. TruffleHog
3. Snyk
4. Aqua Trivy
5. HashiCorp Vault Radar
6. GitHub Advanced Security
7. GitLab Secret Detection
8. Sentry (log detection)
9. Semgrep
10. OWASP ZAP

---

## Key Features Comparison Matrix

### Rotation & Automation
| Tool | Scheduled Rotation | Event-Driven | Dynamic Generation | ML-Optimized |
|------|:---------:|:---------:|:---------:|:---------:|
| Vault | ✓ | ✓ | ✓ | - |
| Akeyless | ✓ | ✓ | ✓ | ✓ |
| AWS Secrets Manager | ✓ (RDS only) | - | Limited | - |
| Keeper | ✓ | ✓ | ✓ | - |
| Doppler | ✓ | ✓ | - | - |

### Multi-Cloud Support
| Tool | AWS | Azure | GCP | On-Prem |
|------|:---------:|:---------:|:---------:|:---------:|
| Vault | ✓ | ✓ | ✓ | ✓ |
| Akeyless | ✓ | ✓ | ✓ | ✓ |
| Teleport | ✓ | ✓ | ✓ | ✓ |
| Doppler | ✓ | ✓ | ✓ | - |
| CyberArk | ✓ | ✓ | ✓ | ✓ |

### Kubernetes Integration
| Tool | Native | ESO Support | Operator | RBAC |
|------|:---------:|:---------:|:---------:|:---------:|
| Vault | - | ✓ | ✓ | ✓ |
| Sealed Secrets | ✓ | ✓ | ✓ | ✓ |
| ESO | ✓ | N/A | ✓ | ✓ |
| CyberArk | ✓ | ✓ | - | ✓ |
| Teleport | ✓ | ✓ | - | ✓ |

### Compliance & Audit
| Tool | HIPAA | FIPS | SOC 2 | PCI-DSS | Audit Logs |
|------|:---------:|:---------:|:---------:|:---------:|:---------:|
| Teleport | ✓ | ✓ | ✓ | ✓ | ✓ |
| CyberArk | ✓ | ✓ | ✓ | ✓ | ✓ |
| Vault Enterprise | ✓ | ✓ | ✓ | ✓ | ✓ |
| Keeper | ✓ | ✓ | ✓ | ✓ | ✓ |
| ManageEngine | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## Migration Paths

### From Static Secrets to Dynamic Secrets
1. **Phase 1**: Inventory all static secrets (API keys, passwords, certs)
2. **Phase 2**: Deploy secrets manager (Vault or cloud-native)
3. **Phase 3**: Migrate high-risk secrets first (database creds, API keys)
4. **Phase 4**: Rotate remaining secrets on schedule
5. **Phase 5**: Enable dynamic secret generation for new resources

**Tools**: HashiCorp Vault, Akeyless, Keeper

---

### From Long-Lived to Short-Lived Credentials
1. **Phase 1**: Implement workload identity (OIDC, SPIFFE)
2. **Phase 2**: Configure cloud providers to accept OIDC tokens
3. **Phase 3**: Update CI/CD to use OIDC (GitHub Actions, GitLab CI)
4. **Phase 4**: Migrate service-to-service auth to mTLS (Istio/Linkerd)
5. **Phase 5**: Eliminate long-lived PATs and static credentials

**Tools**: OIDC/SPIFFE, GitHub Actions, Istio, Linkerd

---

### From Bastion Hosts to Zero-Trust Access
1. **Phase 1**: Deploy Boundary or Teleport
2. **Phase 2**: Migrate SSH access through new platform
3. **Phase 3**: Migrate database access
4. **Phase 4**: Migrate web app access
5. **Phase 5**: Decommission bastion hosts

**Tools**: Boundary, Teleport, StrongDM

---

## Implementation Timeline

### Quick Start (1-2 weeks)
- Cloud-native secrets manager (AWS/Azure/GCP)
- GitHub Actions Secrets for CI/CD
- Sealed Secrets for Kubernetes

---

### Standard Rollout (1-3 months)
- HashiCorp Vault deployment
- External Secrets Operator for K8s
- OIDC integration for CI/CD
- Basic secret scanning (TruffleHog)

---

### Enterprise Transformation (3-12 months)
- Full PAM platform (CyberArk or Teleport)
- Multi-cloud secret sync (Vault, ESO)
- Service mesh mTLS (Istio/Linkerd)
- Compliance automation
- Advanced secret detection (Gitguardian)

---

## Cost Estimation

| Solution | Small Team | Growth Stage | Enterprise |
|----------|-----------|-------------|-----------|
| **Cloud-Native** | ~$50-200/mo | ~$500-2K/mo | $2K-10K/mo |
| **HashiCorp Vault** | $0 (OSS) | ~$200-500/mo | $1K-5K/mo |
| **Akeyless** | $100-300/mo | $500-2K/mo | $3K-10K/mo |
| **CyberArk** | N/A (min ~$10K) | $15K-30K/year | $50K-200K+/year |
| **BeyondTrust** | N/A (min ~$15K) | $20K-50K/year | $75K-300K+/year |
| **Teleport** | $0 (OSS) | ~$500-2K/mo | $5K-15K/mo |

---

## Common Pitfalls to Avoid

### 1. Storing secrets in source code
- Use: CI/CD secrets manager + OIDC
- Scan: TruffleHog, Gitguardian, Snyk

### 2. Never rotating secrets
- Implement: Automated rotation (weekly for API keys, monthly for passwords)
- Use: Vault, Akeyless, Keeper

### 3. Overly complex RBAC
- Use: Principle of Least Privilege (PoLP) templates
- Audit: Regular access reviews

### 4. Single secret manager as SPOF
- Use: High-availability deployment (Vault HA, cloud-managed)
- Backup: Regular secret backups + disaster recovery

### 5. Manual credential provisioning
- Use: Dynamic secrets + automation
- Implement: Just-in-time (JIT) access, ephemeral credentials

### 6. Ignoring non-human identities
- Use: Workload identity (SPIFFE, OIDC)
- Manage: Service accounts, container identity, function identity

---

## Reference Implementation Examples

### AWS-Only Startup
- **Secrets**: AWS Secrets Manager
- **K8s**: External Secrets Operator
- **Scanning**: GitHub Advanced Security
- **Cost**: ~$100-500/month

### Multi-Cloud Growth Stage
- **Secrets**: HashiCorp Vault
- **K8s**: ESO + Vault Secrets Operator
- **Scanning**: Gitguardian + TruffleHog
- **Access**: Teleport for infrastructure
- **Cost**: ~$1K-3K/month

### Regulated Enterprise
- **Secrets**: CyberArk + Vault Enterprise
- **K8s**: ESO + CyberArk integration
- **Scanning**: Gitguardian + Snyk
- **Access**: Teleport Enterprise + Boundary
- **Certificates**: Venafi
- **Cost**: $100K+/year

---

## Resources & Learning

- [OWASP: Secrets Management](https://owasp.org)
- [HashiCorp Learn: Vault](https://learn.hashicorp.com/vault)
- [Kubernetes: Secrets Best Practices](https://kubernetes.io/docs/concepts/configuration/secret/)
- [CNCF: Teleport Documentation](https://goteleport.com/docs/)
- [Aqua: Secrets Management Guide](https://www.aquasec.com)

---

**Document Version**: 1.0
**Last Updated**: 2026-01-01
