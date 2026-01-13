# Configuration Systems Quick Selection Matrix

Fast reference guide to select the right configuration tool in under 60 seconds.

## One-Minute Selector

### Question 1: What's your primary use case?

**A) Application Configuration in Microservices**
→ Go to Section A

**B) Secrets Management**
→ Go to Section B

**C) Infrastructure & Cloud Resources**
→ Go to Section C

**D) Feature Flags & Dynamic Features**
→ Go to Section D

**E) Kubernetes Configuration**
→ Go to Section E

---

## Section A: Application Configuration in Microservices

### Choose Your Deployment Model

**Self-Hosted Only**
- **For Java/Spring apps**: Spring Cloud Config
- **For multi-language**: Consul or etcd
- **For real-time updates**: Apollo or Nacos

**Managed SaaS**
- **AWS-centric**: AWS AppConfig
- **Azure-centric**: Azure App Configuration
- **Cloud-agnostic**: Doppler

**Hybrid Available**
- **Most flexible**: Consul (self-hosted) + optional extensions
- **Enterprise option**: HashiCorp Consul

---

## Section B: Secrets Management

### Budget & Scale

**Startup/Small Team ($0-500/month)**
- Doppler (free tier: $0, paid: $15/month)
- Infisical (self-hosted: $0)
- 1Password Business ($45/user/month)

**Growing Company ($500-2000/month)**
- HashiCorp Vault (self-hosted or $150+/month cloud)
- AWS Secrets Manager (pay-per-secret)
- Azure Key Vault (pay-per-transaction)

**Enterprise ($2000+/month)**
- Vault Enterprise (self-hosted + support)
- CyberArk (PAM comprehensive)
- Delinea (enterprise secrets)

### Cloud Affinity

**AWS-only**: AWS Secrets Manager
**Azure-only**: Azure Key Vault
**GCP-only**: Google Secret Manager
**Multi-cloud**: HashiCorp Vault or Doppler
**Self-hosted**: HashiCorp Vault or Infisical

---

## Section C: Infrastructure & Cloud Resources

### Your Situation

**Need multi-cloud IaC?**
- **Primary**: Terraform
- **Alternative**: Pulumi

**AWS-only**
- **Simple**: CloudFormation
- **Flexible**: Terraform
- **Code-based**: AWS CDK

**Azure-only**
- **Simple**: Azure Resource Manager (ARM)
- **Simplified**: Bicep
- **Flexible**: Terraform

**Want to use code you know?**
- **Python/JavaScript/Go**: Pulumi

**Complex deployment logic?**
- **Primary**: Terraform with modules
- **Alternative**: Ansible + Terraform

**Running existing Ansible playbooks?**
- Stick with Ansible (or add Terraform alongside)

---

## Section D: Feature Flags & Dynamic Features

### Your Budget & Team Size

**Under $100/month**
- ConfigCat (most budget-friendly)
- Unleash (open-source, free to host)
- FeatBit (open-source, free to host)

**$100-1000/month**
- Flagsmith (cloud: ~$250/month)
- Statsig (with analytics)
- PostHog (if you need analytics too)

**$1000+/month**
- LaunchDarkly (premium tier)
- Statsig (enterprise plan)
- Optimizely (full suite)

### Your Primary Need

**Just feature flags?**
- ConfigCat or Unleash

**Flags + A/B Testing?**
- LaunchDarkly or Statsig

**Flags + Full Product Analytics?**
- PostHog

**Flags + Experimentation?**
- Optimizely

**Self-hosted required?**
- Unleash or FeatBit (open-source)
- PostHog (self-hosted plan available)

---

## Section E: Kubernetes Configuration

### What's Your Challenge?

**Managing YAML files in Git?**
- **Simple case**: Kustomize
- **Complex case**: Helm
- **GitOps**: ArgoCD + Helm/Kustomize

**Encrypting secrets in Git?**
- **Easiest**: Sealed Secrets
- **More flexible**: External Secrets Operator + Vault
- **Self-service**: SOPS + helm-secrets plugin

**Managing multi-cluster configs?**
- **Primary**: Helm + Helm Secrets
- **Alternative**: Kustomize + ArgoCD (multi-cluster)
- **Enterprise**: Rancher

**Need service mesh config?**
- **Simple/lightweight**: Linkerd
- **Feature-rich**: Istio
- **Integrated with Consul**: Consul Service Mesh

**Deploying apps to Kubernetes?**
- **Simple**: kubectl + Helm
- **GitOps**: ArgoCD or Flux CD
- **Both**: Helm + ArgoCD

---

## Tool Comparison Cards (One-Liners)

### Centralized Configuration
- **Spring Cloud Config**: Git-backed Spring Boot configuration
- **Consul**: Multi-purpose service discovery + KV store
- **etcd**: Distributed KV store for coordination and config
- **Nacos**: Dynamic config + service discovery (Alibaba)
- **Apollo**: Dynamic config with real-time push (Ctrip)

### Cloud Native Secrets
- **Vault**: Enterprise secrets platform with dynamic credentials
- **AWS Secrets Manager**: AWS native secrets with auto-rotation
- **Azure Key Vault**: Azure native key/secret/certificate store
- **Doppler**: Universal secrets platform across clouds

### Infrastructure as Code
- **Terraform**: Multi-cloud infrastructure provisioning (HCL)
- **Pulumi**: Infrastructure as Code using Python/TypeScript/Go
- **CloudFormation**: AWS native IaC (JSON/YAML)
- **Ansible**: Agentless configuration and orchestration (YAML)

### Kubernetes
- **Helm**: Kubernetes package manager and templating
- **Kustomize**: Kubernetes configuration customization (no templating)
- **ArgoCD**: GitOps continuous deployment controller
- **Sealed Secrets**: Kubernetes secret encryption for Git

### Feature Flags
- **ConfigCat**: Affordable cloud-hosted feature flags
- **Unleash**: Open-source feature flag platform
- **LaunchDarkly**: Enterprise feature flag platform
- **PostHog**: Analytics + feature flags + session recording

### API Gateway
- **Kong**: Open-source API gateway with plugins
- **AWS API Gateway**: AWS managed API service
- **Traefik**: Cloud-native reverse proxy (Kubernetes-friendly)

---

## Decision Tree (Text Version)

```
START: Select Configuration Tool
│
├─→ Is it for APPLICATION CONFIG?
│   ├─→ Microservices? → Nacos / Apollo / Consul / etcd
│   └─→ Spring apps only? → Spring Cloud Config
│
├─→ Is it for SECRETS?
│   ├─→ AWS only? → Secrets Manager
│   ├─→ Self-hosted? → Vault or Infisical
│   └─→ Multi-cloud? → Doppler or Vault
│
├─→ Is it for INFRASTRUCTURE?
│   ├─→ Multi-cloud? → Terraform or Pulumi
│   ├─→ AWS only? → CloudFormation or Terraform
│   └─→ Need code? → Pulumi
│
├─→ Is it for KUBERNETES?
│   ├─→ Package mgmt? → Helm
│   ├─→ YAML customization? → Kustomize
│   ├─→ GitOps? → ArgoCD or Flux
│   └─→ Encrypt secrets in Git? → Sealed Secrets
│
└─→ Is it for FEATURE FLAGS?
    ├─→ Budget conscious? → ConfigCat or Unleash
    ├─→ Need analytics? → PostHog or Statsig
    └─→ Enterprise? → LaunchDarkly
```

---

## Common Combinations (Recommended Stacks)

### Startup Stack
- **Config**: Environment variables + optional Doppler
- **Secrets**: 1Password or Doppler
- **Infrastructure**: CloudFormation (AWS) or Terraform
- **Feature Flags**: ConfigCat
- **Kubernetes**: None needed yet

### Growth Stage Stack
- **Config**: Consul or Helm ConfigMaps
- **Secrets**: Vault or AWS Secrets Manager
- **Infrastructure**: Terraform + Ansible
- **Feature Flags**: Flagsmith or Statsig
- **Kubernetes**: Kubernetes + Helm + Sealed Secrets

### Enterprise Stack
- **Config**: Consul + custom service layer
- **Secrets**: Vault Enterprise + CyberArk
- **Infrastructure**: Terraform + Crossplane + custom tools
- **Feature Flags**: LaunchDarkly
- **Kubernetes**: Rancher + Helm + External Secrets Operator + Istio

### Serverless Stack
- **Config**: AWS AppConfig
- **Secrets**: AWS Secrets Manager
- **Infrastructure**: AWS SAM or Serverless Framework
- **Feature Flags**: PostHog or Statsig
- **Kubernetes**: Not applicable

### Kubernetes-First Stack
- **Config**: ConfigMaps + optional Consul
- **Secrets**: Sealed Secrets or External Secrets Operator
- **Infrastructure**: Terraform (provision cluster) + Helm (manage apps)
- **Feature Flags**: Unleash (self-hosted) or PostHog
- **Kubernetes**: K3s/EKS + Helm + ArgoCD

---

## Red Flags - Avoid These Patterns

❌ Storing secrets in Git (even encrypted without strong secrets system)
❌ Hardcoding API keys in code
❌ Manual configuration changes without version control
❌ No audit trail for configuration changes
❌ Single point of failure for configuration service
❌ Mixing infrastructure code with application code in same repo
❌ No disaster recovery plan for configuration systems
❌ Configuration that can't be reproduced in dev/staging/prod

---

## Green Lights - Good Patterns

✅ All secrets in dedicated secret store with rotation
✅ Infrastructure as Code in Git with review process
✅ Configuration changes tracked with audit logs
✅ Secrets encrypted at rest and in transit
✅ Disaster recovery tested and documented
✅ Dev/staging/prod configs identical (except secrets)
✅ Automated drift detection for infrastructure
✅ Gradual rollout of configuration changes

---

**Research Date**: January 2026
**Total Tools Covered**: 150+
**Categories**: 13 major categories
**Use Cases**: 8 primary scenarios
