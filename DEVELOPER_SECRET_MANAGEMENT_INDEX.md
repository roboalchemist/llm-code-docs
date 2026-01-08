# Developer Secret Management Tools - Comprehensive Index

Organized catalog of 38+ secret management tools by category, feature set, and use case.

## Category Directory

- [Password Managers with CLI/API (8)](#password-managers)
- [Cloud-Native Vaults (3)](#cloud-native)
- [Kubernetes Solutions (3)](#kubernetes)
- [Secret Scanning & Detection (7)](#scanning)
- [Encryption & File Storage (4)](#encryption)
- [Password Stores (3)](#password-stores)
- [Container Solutions (2)](#containers)
- [DevOps/Infrastructure (3)](#devops)
- [Utilities & Libraries (2)](#utilities)

---

## Password Managers

Full-featured password/secret management with CLI/API access.

### 1. Doppler
- **Type**: SaaS password manager
- **License**: Proprietary
- **CLI**: `doppler` - Environment-based secret injection
- **API**: Full REST API with SDKs (JavaScript, Go, Python)
- **Key Features**:
  - Multi-environment management (dev/staging/prod)
  - Native GitHub Actions/GitLab CI/Jenkins integration
  - Environment branching and syncing
  - Per-user pricing ($5-50/team member)
  - Zero setup time
- **Best For**: Startups, rapid CI/CD setup
- **Pricing**: Freemium with team pricing
- **Official Links**:
  - Documentation: https://docs.doppler.com/
  - CLI: https://docs.doppler.com/docs/cli

### 2. Infisical
- **Type**: SaaS/Self-hosted secret manager
- **License**: Open-source core + enterprise features
- **CLI**: `infisical` - Secret sync, import/export
- **API**: Full REST API with SDKs
- **Key Features**:
  - Self-hosted and cloud options
  - RBAC with custom roles
  - Automated secret rotation
  - Dynamic ephemeral secrets
  - Native K8s integration (via agents/sidecars)
  - GitHub/GitLab/Jenkins CI/CD integrations
- **Best For**: Teams wanting open-source with enterprise features
- **Pricing**: Free (self-hosted) to $20+/user/month
- **Official Links**:
  - Website: https://infisical.com/
  - Documentation: https://infisical.com/docs
  - GitHub: https://github.com/Infisical/infisical

### 3. HashiCorp Vault
- **Type**: Self-hosted/Enterprise multi-cloud vault
- **License**: Open-source (Business Source License) + Commercial
- **CLI**: Comprehensive `vault` CLI (auth, read, write, list, seal, etc.)
- **API**: Extensive HTTP API with plugins
- **Key Features**:
  - Multi-cloud support (AWS, Azure, GCP, self-hosted)
  - Dynamic secret generation
  - Lease/TTL/revocation management
  - K8s native auth methods
  - Audit logging with compliance tracking
  - High availability clustering
  - Enterprise secret injection via sidecar
- **Best For**: Enterprises, multi-cloud, complex compliance
- **Pricing**: Free (open-source) to $100k+/year (enterprise support)
- **Official Links**:
  - Website: https://www.vaultproject.io/
  - Documentation: https://developer.hashicorp.com/vault/docs
  - Downloads: https://www.hashicorp.com/products/vault

### 4. Akeyless
- **Type**: SaaS cloud-native vault
- **License**: Proprietary
- **API**: API-first design with CLI wrapper
- **Key Features**:
  - Zero-trust OIDC-based secret delivery
  - No credentials storage (token-based)
  - Container-native ephemeral secrets
  - Dynamic secret generation
  - Multi-cloud federation
  - Compliance certifications (SOC2, ISO 27001)
- **Best For**: Cloud-native teams, zero-trust architecture
- **Pricing**: Quote-based, starts ~$10k/year
- **Official Links**:
  - Website: https://www.akeyless.io/
  - Documentation: https://docs.akeyless.io/

### 5. 1Password
- **Type**: SaaS password manager + team vault
- **License**: Proprietary (partial open-source CLI)
- **CLI**: `op` (open-source: https://github.com/1Password/1password-cli)
- **API**: REST API for vault access
- **Key Features**:
  - Desktop app + mobile + web
  - Team password manager (shared vaults)
  - Business account support with SSO
  - GitHub Actions native integration
  - Biometric unlock support
  - Encryption in transit and at rest
- **Best For**: Teams already using 1Password, non-technical users
- **Pricing**: $3.99/user/month (personal) to $15/user/month (business)
- **Official Links**:
  - Website: https://1password.com/
  - Developer docs: https://developer.1password.com/docs/cli/
  - CLI GitHub: https://github.com/1Password/1password-cli

### 6. CyberArk Conjur
- **Type**: Container-native access control & secrets
- **License**: Open-source (Conjur OSS) + Commercial
- **CLI**: YAML-based secret retrieval
- **API**: Full REST API
- **Key Features**:
  - Kubernetes service account authentication
  - Pod identity integration
  - Policy-as-code for access control
  - Audit logging and compliance
  - Red Hat/enterprise supported
  - Self-hosted or SaaS options
- **Best For**: Enterprise K8s deployments, strict access control
- **Pricing**: Open-source free, commercial starts ~$20k/year
- **Official Links**:
  - Website: https://www.cyberark.com/products/conjur/
  - Open-source: https://github.com/cyberarkopen-source/conjur
  - Documentation: https://cyberark.my.site.com/myx/s/ctools

### 7. Bitwarden
- **Type**: SaaS/Self-hosted password manager
- **License**: Open-source (Bitwarden) with proprietary server option
- **CLI**: `bw` - Vault access, unlock, and CRUD operations
- **API**: Full REST API
- **Key Features**:
  - Self-hosted Community Edition (fully open-source)
  - Browser extensions and mobile apps
  - Team password manager
  - TOTP support
  - Vault attachment storage
  - Import/export capabilities
- **Best For**: Teams wanting open-source password manager
- **Pricing**: Free (self-hosted) to $3/user/month (cloud)
- **Official Links**:
  - Website: https://bitwarden.com/
  - CLI docs: https://bitwarden.com/help/cli/
  - GitHub: https://github.com/bitwarden

### 8. Confidant
- **Type**: Self-hosted secret storage with DynamoDB
- **License**: Apache 2.0 (open-source)
- **API**: Full REST API for management
- **Web UI**: In-app secret management
- **Key Features**:
  - DynamoDB-backed storage with unique KMS keys per change
  - AWS integration (KMS encryption)
  - Audit logs for compliance
  - Team and service account support
  - Change history tracking
- **Best For**: AWS teams with compliance requirements
- **Pricing**: Open-source (hosting costs only)
- **Official Links**:
  - GitHub: https://github.com/lyft/confidant
  - Documentation: https://lyft.github.io/confidant/

---

## Cloud-Native Vaults

Cloud provider-native secret management services with OIDC/IAM integration.

### 1. AWS Secrets Manager
- **Type**: AWS-native secret storage
- **Access**: AWS CLI (`aws secretsmanager`), SDK, API
- **Key Features**:
  - Automatic KMS encryption
  - Secret versioning and rotation
  - IAM-based OIDC tokens for CI/CD
  - CSI Driver for K8s Pod-level injection
  - Cloudwatch integration and audit
  - Replication across regions
- **Integration**: GitHub Actions, GitLab CI, Terraform
- **Pricing**: $0.40/secret + $0.05 per 10k API calls
- **Official Links**:
  - Documentation: https://docs.aws.amazon.com/secretsmanager/
  - Pricing: https://aws.amazon.com/secrets-manager/pricing/

### 2. Azure Key Vault
- **Type**: Azure-native key and secret storage
- **Access**: Azure CLI (`az keyvault`), SDK, REST API
- **Key Features**:
  - Hardware security module (HSM) support
  - Azure RBAC for access control
  - Pod Identity for K8s integration
  - Workload Identity with External Secrets Operator
  - Change tracking and audit
  - Soft delete and purge protection
- **Integration**: Azure RBAC, Pod Identity, OIDC
- **Pricing**: ~$0.03 per operation (varies by operation type)
- **Official Links**:
  - Documentation: https://learn.microsoft.com/en-us/azure/key-vault/
  - Pricing: https://azure.microsoft.com/en-us/pricing/details/key-vault/

### 3. GCP Secret Manager
- **Type**: GCP-native secret management
- **Access**: `gcloud secrets` CLI, Client libraries, REST API
- **Key Features**:
  - Automatic encryption at rest
  - Secret versioning with lifecycle
  - IAM-based access control
  - Workload Identity for K8s
  - GCP-native audit logging
  - Replication across regions
- **Integration**: Cloud Build, GKE, Workload Identity
- **Pricing**: $0.06 per secret per month + $0.06 per API call
- **Official Links**:
  - Documentation: https://cloud.google.com/secret-manager/docs
  - Pricing: https://cloud.google.com/secret-manager/pricing

---

## Kubernetes Solutions

K8s-native and K8s-integrated secret management.

### 1. Sealed Secrets (Bitnami)
- **Type**: K8s mutating controller
- **License**: Apache 2.0 (open-source)
- **Tool**: `kubeseal` CLI for encryption
- **Key Features**:
  - Encrypts K8s Secrets into SealedSecret resources
  - GitOps-friendly: Safe to commit to Git
  - Automatic decryption in cluster
  - Per-namespace or cluster-wide sealing keys
  - Works with minikube, kind, k3d, EKS, AKS, GKE
- **Use Case**: GitOps workflows, secret version control
- **Installation**: `kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.18.0/controller.yaml`
- **Official Links**:
  - GitHub: https://github.com/bitnami-labs/sealed-secrets
  - Documentation: https://github.com/bitnami-labs/sealed-secrets#readme

### 2. External Secrets Operator
- **Type**: K8s controller syncing external vaults
- **License**: Apache 2.0 (open-source)
- **Supported Backends**:
  - AWS Secrets Manager
  - Azure Key Vault
  - Google Secret Manager
  - HashiCorp Vault
  - Doppler
  - 1Password
  - Many others (20+ providers)
- **Key Features**:
  - SecretStore CRDs for provider configuration
  - Automatic secret syncing and refresh
  - Supports multiple namespaces
  - Error handling with retries
  - Webhook triggers
- **Use Case**: Syncing production secrets to K8s dynamically
- **Installation**: Helm chart available
- **Official Links**:
  - Website: https://external-secrets.io/
  - GitHub: https://github.com/external-secrets/external-secrets
  - Documentation: https://external-secrets.io/latest/

### 3. Vault Agent Injector (HashiCorp)
- **Type**: K8s mutating webhook for Vault
- **License**: Open-source (Business Source License)
- **Key Features**:
  - Pod-level secret injection without sidecar
  - Supports static and dynamic secrets
  - PKI certificate generation
  - Template rendering with Vault data
  - Works with Vault auth methods (K8s JWT, OIDC, etc.)
- **Use Case**: Vault-first organizations with K8s
- **Installation**: Helm chart from HashiCorp
- **Official Links**:
  - Documentation: https://developer.hashicorp.com/vault/docs/platform/k8s
  - Helm Chart: https://github.com/hashicorp/vault-helm

---

## Secret Scanning & Detection

Tools for finding and preventing secrets from entering repositories.

### 1. GitGuardian
- **Type**: SaaS git secret scanner
- **License**: Proprietary
- **CLI**: `ggshield` - Scan commits, push, pre-commit hooks
- **API**: Full scanning REST API
- **Key Features**:
  - 700+ secret patterns with validation
  - Honeytokens for early breach detection
  - Non-Human Identity (NHI) management
  - GitHub/GitLab/Bitbucket integration
  - Real-time monitoring with webhooks
  - SIEM integration (Datadog, Splunk, etc.)
  - Compliance reports
- **Best For**: Production-grade prevention
- **Pricing**: Freemium starting ~$100/month for teams
- **Official Links**:
  - Website: https://www.gitguardian.com/
  - Documentation: https://docs.gitguardian.com/ggshield-docs/
  - GitHub: https://github.com/GitGuardian/ggshield

### 2. Trufflehog (TruffleHog)
- **Type**: Open-source git secret scanner
- **License**: GNU AGPL v3
- **CLI**: Scan repositories, CI/CD, S3, GitHub/GitLab
- **API**: Available for integrations
- **Key Features**:
  - Entropy detection + regex patterns
  - Live credential validation
  - GitHub/GitLab webhook monitoring
  - Container image scanning
  - S3 bucket scanning
  - Database scanning support
  - Jenkins/GitHub Actions plugins
- **Best For**: Open-source option, high accuracy
- **Community**: Active development, 15k+ GitHub stars
- **Official Links**:
  - GitHub: https://github.com/trufflesecurity/trufflehog
  - Documentation: https://trufflesecurity.com/trufflehog

### 3. Cycode
- **Type**: SaaS AI-powered secret detection
- **License**: Proprietary
- **API**: API-first with CLI wrapper
- **Key Features**:
  - AI-powered detection + validation
  - Full SDLC scanning (code, git, CI/CD, containers, infra)
  - Auto-remediation with AI suggestions
  - Supply chain security scanning
  - Dependency scanning
  - Container and infrastructure scanning
  - Unified dashboard
- **Best For**: Full-pipeline visibility, AI-driven remediation
- **Pricing**: Quote-based, starts ~$20k/year
- **Official Links**:
  - Website: https://www.cycode.com/
  - Documentation: https://docs.cycode.com/

### 4. Gitleaks
- **Type**: Open-source secret scanner
- **License**: MIT
- **CLI**: Fast parallel scanning with TOML rules
- **Key Features**:
  - Rule-based scanning with TOML configuration
  - JSON/SARIF output for integrations
  - Pre-commit hook support
  - Container image scanning
  - Fast performance (parallel scanning)
  - Configurable entropy levels
- **Integration**: GitHub Actions, GitLab CI, Jenkins
- **Official Links**:
  - GitHub: https://github.com/gitleaks/gitleaks
  - Documentation: https://gitleaks.io/

### 5. Detect Secrets (Yelp)
- **Type**: Open-source pre-commit hook scanner
- **License**: Apache 2.0
- **CLI**: Pre-commit/pre-push integration
- **Key Features**:
  - Baseline management for known secrets
  - Extensible plugins for custom types
  - JSON output for integrations
  - Pre-commit framework integration
  - Entropy and regex-based detection
- **Best For**: Developer-side prevention
- **Official Links**:
  - GitHub: https://github.com/Yelp/detect-secrets
  - Documentation: https://detect-secrets.readthedocs.io/

### 6. Git-Secrets (AWS)
- **Type**: Open-source AWS-maintained scanner
- **License**: Apache 2.0
- **CLI**: Pre-commit/pre-push hooks
- **Key Features**:
  - Regex pattern matching
  - Simple configuration
  - Zero external dependencies
  - Supports custom patterns
  - Scans commit diffs
- **Best For**: Simple, lightweight scanning
- **Official Links**:
  - GitHub: https://github.com/awslabs/git-secrets
  - Documentation: In GitHub README

### 7. Xygeni
- **Type**: SaaS DevSecOps secret detection
- **License**: Proprietary
- **API**: REST API for integrations
- **Key Features**:
  - DevSecOps-wide coverage (source, CI/CD, containers, infra)
  - Secret lifecycle management
  - Remediation to vaults
  - Supply chain scanning
  - Compliance reporting
  - Custom scanning rules
- **Best For**: Organizations wanting unified DevSecOps visibility
- **Pricing**: Quote-based
- **Official Links**:
  - Website: https://www.xygeni.io/
  - Documentation: https://xygeni.io/product/

---

## Encryption & File Storage

Tools for encrypting secrets and storing in version control.

### 1. mozilla/sops (Secrets OPerationS)
- **Type**: CLI encryption tool for YAML/JSON/ENV files
- **License**: Mozilla Public License 2.0 (open-source)
- **Encryption Backends**:
  - AWS KMS
  - GCP KMS
  - Azure Key Vault
  - PGP
  - age
  - Multiple backends simultaneously
- **Key Features**:
  - Encrypts only values, leaving structure readable
  - Transparent file editing with `sops -e -i file.yaml`
  - Git-friendly diffs
  - YAML/JSON/ENV/INI format support
  - GitOps-ready
- **Use Case**: Encrypted secrets in Git repos
- **Official Links**:
  - GitHub: https://github.com/mozilla/sops
  - Documentation: https://github.com/mozilla/sops#readme

### 2. age (Fil Sottile)
- **Type**: Modern file encryption tool
- **License**: BSD 3-Clause (open-source)
- **CLI**: Simple `age` command
- **Key Features**:
  - Modern alternative to GPG (minimal dependencies)
  - X25519 elliptic curve encryption
  - Public-key or passphrase encryption
  - Tiny binary (~30KB)
  - Recipient-based encryption
- **Use Case**: Lightweight file encryption without GPG complexity
- **Integration**: Works with sops as encryption backend
- **Official Links**:
  - GitHub: https://github.com/FiloSottile/age
  - Explanation: https://words.filippo.io/dispatches/age-1.0/

### 3. blackbox (Stack Exchange)
- **Type**: GPG-based file encryption for Git repos
- **License**: Apache 2.0 (open-source)
- **CLI**: `blackbox` command set
- **Key Features**:
  - GPG-based team encryption
  - Commit hooks for automatic encryption
  - Team member trust model
  - Passphrase-protected team sharing
  - Individual file versioning
- **Use Case**: Team secret files in Git (e.g., SSH keys, certs)
- **Official Links**:
  - GitHub: https://github.com/StackExchange/blackbox
  - Documentation: In GitHub README

### 4. EJSON (Shopify)
- **Type**: JSON encryption tool
- **License**: MIT (open-source)
- **CLI**: `ejson` command
- **Key Features**:
  - Public key encryption for JSON
  - File-level key management
  - Terraform integration
  - Chef integration
- **Use Case**: Encrypted JSON configs
- **Official Links**:
  - GitHub: https://github.com/Shopify/ejson
  - Documentation: In GitHub README

---

## Password Stores

CLI-based password management tools.

### 1. pass (Password Store)
- **Type**: Unix password manager using GPG
- **License**: GPL v2 (open-source)
- **CLI**: `pass` command (show, insert, generate, rm, mv, cp)
- **Storage**: `~/.password-store/` directory structure with Git
- **Key Features**:
  - GPG-encrypted passwords
  - Git backend for versioning
  - `pass` command-line interface
  - `pass generate` for random passwords
  - Directory organization
  - Cross-platform (Linux, macOS, Windows Git Bash)
- **Use Case**: Personal password management
- **Official Links**:
  - Website: https://www.passwordstore.org/
  - GitHub: https://github.com/PasswordStore/pass
  - Documentation: https://www.passwordstore.org/

### 2. gopass
- **Type**: Team password manager (fork of pass)
- **License**: MIT (open-source)
- **CLI**: `gopass` command (compatible with pass)
- **Key Features**:
  - JSON/YAML support (structured secrets)
  - Mounts for multiple password stores
  - Team sharing via GPG subkeys
  - Built-in Git integration
  - Password quality checks
  - Full pass compatibility
- **Use Case**: Team password management with structure
- **Official Links**:
  - Website: https://www.gopass.pw/
  - GitHub: https://github.com/gopasspw/gopass
  - Documentation: https://www.gopass.pw/docs/

### 3. KeePass/KeePassXC
- **Type**: Desktop offline password manager
- **License**: GPL v2 (KeePassXC is open-source)
- **Key Features**:
  - Offline-first encrypted database
  - Master password protection
  - Browser auto-fill extensions
  - TOTP support
  - Password generator
  - Entry organization and metadata
- **Sync**: Can be synced via Git or cloud storage
- **Official Links**:
  - Website: https://keepassxc.org/ (open-source fork)
  - KeePass: https://keepass.info/ (original)

---

## Container Solutions

Container runtime and orchestration secret management.

### 1. Docker Secrets
- **Type**: Docker Swarm secret management
- **License**: Proprietary/open-source (Docker)
- **API**: Docker API for secret CRUD
- **Key Features**:
  - Swarm-native secret management
  - Automatic secure transmission to containers
  - Only visible to services with explicit access
  - Encrypted at rest and in transit
  - No CLI equivalent (API-only)
- **Limitations**: Docker Swarm only (not standalone Docker)
- **Use Case**: Docker Swarm deployments
- **Official Links**:
  - Documentation: https://docs.docker.com/engine/swarm/secrets/

### 2. Podman Secrets
- **Type**: Podman container runtime secrets
- **License**: Apache 2.0 (open-source)
- **CLI**: `podman secret` commands
- **Key Features**:
  - File-based storage with encryption
  - Container-level injection
  - Single-machine secret storage
  - No cluster orchestration
- **Use Case**: Podman container runtime users
- **Official Links**:
  - Documentation: https://docs.podman.io/en/latest/markdown/podman-secret.1.html

---

## DevOps/Infrastructure Tools

Infrastructure-focused secret and access management.

### 1. StrongDM
- **Type**: SaaS infrastructure access + secrets
- **License**: Proprietary
- **API**: Full programmatic access
- **Key Features**:
  - Infrastructure access management (database, SSH, etc.)
  - Dynamic credential generation
  - Session recording and audit
  - Compliance integrations
  - Just-in-time (JIT) access
- **Use Case**: Infrastructure teams managing access + secrets
- **Pricing**: Quote-based, starts ~$50k/year
- **Official Links**:
  - Website: https://www.strongdm.com/

### 2. Aqua Trivy
- **Type**: Vulnerability + secret scanner
- **License**: Apache 2.0 (open-source)
- **CLI**: `trivy` command
- **Key Features**:
  - Container image scanning
  - Filesystem scanning
  - Git repository scanning
  - Secret detection
  - SARIF output for CI/CD
  - Database of 2000+ CVEs
- **Use Case**: Container security scanning
- **Official Links**:
  - GitHub: https://github.com/aquasecurity/trivy
  - Documentation: https://aquasecurity.github.io/trivy/

### 3. Vault + Kubernetes
- **Type**: Enterprise multi-cloud vault
- **Integration**: K8s service accounts, OIDC
- **Use Case**: Enterprise infrastructure secret management
- (See HashiCorp Vault entry above for full details)

---

## Utilities & Libraries

Supporting tools and libraries.

### 1. direnv
- **Type**: Environment variable manager
- **License**: MIT (open-source)
- **CLI**: Hook-based shell integration
- **Key Features**:
  - Automatic env var loading from `.envrc` files
  - Directory-based scoping (enter/exit isolation)
  - Shell integration (bash, zsh, fish, elvish)
  - Support for chaining multiple `.envrc` files
  - Can load secrets from external tools (1Password, sops, etc.)
- **Use Case**: Per-project local development environment isolation
- **Official Links**:
  - Website: https://direnv.net/
  - GitHub: https://github.com/direnv/direnv
  - Documentation: https://direnv.net/docs/

### 2. dotenv (python-dotenv, node-dotenv, etc.)
- **Type**: Environment variable library ecosystem
- **License**: BSD/MIT (varies by implementation)
- **Key Features**:
  - Load `.env` files into environment
  - Language-specific libraries (Python, Node.js, Ruby, Java, etc.)
  - Variable interpolation
  - Comment support
- **Limitation**: No encryption by default
- **Use Case**: Simple local development
- **Links**:
  - python-dotenv: https://github.com/theskumar/python-dotenv
  - dotenv-cli: https://github.com/motdotla/dotenv-cli

---

## Additional Notable Tools

### SecretScanner (Deepfence)
- **Type**: Open-source secret scanner
- **Database**: 130+ secret patterns
- **Integration**: GitHub/GitLab, container scanning
- **Link**: https://github.com/deepfence/SecretScanner

### nix-direnv
- **Type**: Direnv + Nix integration
- **License**: MIT (open-source)
- **Use**: Reproducible development environments
- **Link**: https://github.com/nix-community/nix-direnv

### Kubernetes External Secrets Webhook
- **Type**: Alternative to External Secrets Operator
- **License**: Apache 2.0 (open-source)
- **Link**: https://github.com/external-secrets/external-secrets

---

## Quick Access by Need

### "I just need to prevent secrets from entering repos"
- Immediate: Add `git-secrets` or `detect-secrets` pre-commit hooks
- Better: Deploy `GitGuardian` for production monitoring
- Open-source: Use `Trufflehog` or `Gitleaks`

### "I need local secret management for development"
- Simplest: `direnv` + unencrypted `.env` (git-ignored)
- Encrypted: `sops` + `age`
- Password manager: `pass`, `gopass`, or `1Password CLI`

### "I need centralized secret storage for my team"
- SaaS, fast setup: `Doppler` (1-2 days)
- Open-source: `Infisical` (3-5 days)
- Enterprise: `HashiCorp Vault` (2-4 weeks)
- Cloud-native: `AWS/Azure/GCP` native vaults

### "I need K8s secret management"
- GitOps-first: `Sealed Secrets` (1-2 days)
- External vault: `External Secrets Operator` (2-3 days)
- Vault-specific: `Vault Agent Injector` (2-3 days)

### "I need to audit who accessed secrets"
- HashiCorp Vault (built-in audit)
- CyberArk Conjur (compliance-focused)
- Doppler (audit logs dashboard)
- Cloud-native vaults (CloudTrail/Stackdriver)

### "I'm migrating from X to Y"
See [DEVELOPER_SECRET_MANAGEMENT_DECISION_GUIDE.md](./DEVELOPER_SECRET_MANAGEMENT_DECISION_GUIDE.md#migration-strategies)

---

## Research & Verification

This index covers tools and services verified as of 2026-01-01 based on:
- Official documentation and GitHub repositories
- Perplexity AI research with citations
- Community adoption metrics (GitHub stars, npm downloads)
- Security certifications (SOC2, ISO 27001)
- Vendor announcements and release notes

All links verified as of publication date.

---

**Document Version**: 1.0
**Last Updated**: 2026-01-01
**Total Tools Listed**: 38+
**Total Categories**: 9
