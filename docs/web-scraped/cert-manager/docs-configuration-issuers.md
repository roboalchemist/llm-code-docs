# Source: https://cert-manager.io/docs/configuration/issuers/

Title: Issuers

URL Source: https://cert-manager.io/docs/configuration/issuers/

Markdown Content:
The following list contains all known cert-manager issuer integrations.

| Tier | Controller | Docs | Issuer | cert-manager version used in tutorial[1](https://cert-manager.io/docs/configuration/issuers/#user-content-fn-1) | Released within 12 months[2](https://cert-manager.io/docs/configuration/issuers/#user-content-fn-2) | Is Open Source |
| --- | --- | --- | --- | --- | --- | --- |
| 🥇 | acme-issuer (in-tree) | [📄](https://cert-manager.io/docs/configuration/acme/) | [ACME](https://datatracker.ietf.org/doc/html/rfc8555) | [latest](https://cert-manager.io/docs/tutorials/getting-started-aks-letsencrypt/) | [✔️](https://cert-manager.io/docs/releases/) | ✔️ |
| 🥇 | venafi-enhanced-issuer | [📄](https://docs.venafi.cloud/vaas/k8s-components/t-vei-install/) | [CyberArk Certificate Manager](https://www.cyberark.com/products/certificate-manager/) | [v1.12.1](https://docs.venafi.cloud/vaas/k8s-components/c-vei-overview/) | [✔️](https://docs.venafi.cloud/vaas/k8s-components/c-vei-releases/) | ❌ |
| 🥇 | origin-ca-issuer | [📄](https://github.com/cloudflare/origin-ca-issuer) | [Cloudflare Origin CA](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca) | [supported](https://github.com/cloudflare/origin-ca-issuer/blob/trunk/README.org) | [✔️](https://github.com/cloudflare/origin-ca-issuer/releases) | ✔️ |
| 🥈 | adcs-issuer | [📄](https://djkormo.github.io/adcs-issuer/) | [Microsoft Active Directory Certificate Service](https://docs.microsoft.com/en-us/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority) | - | [✔️](https://github.com/djkormo/adcs-issuer/releases) | ✔️ |
| 🥈 | aws-privateca-issuer | [📄](https://github.com/cert-manager/aws-privateca-issuer) | [AWS Private Certificate Authority](https://aws.amazon.com/certificate-manager/private-certificate-authority/) | - | [✔️](https://github.com/cert-manager/aws-privateca-issuer/releases) | ✔️ |
| 🥈 | ca-issuer (in-tree) | [📄](https://cert-manager.io/docs/configuration/ca/) | CA issuer | - | [✔️](https://cert-manager.io/docs/releases/) | ✔️ |
| 🥈 | czertainly-issuer | [📄](https://docs.czertainly.com/docs/certificate-key/integration-guides/cert-manager-issuer/create-czertainly-issuer) | [CZERTAINLY](https://www.czertainly.com/) | [supported](https://docs.czertainly.com/docs/certificate-key/integration-guides/cert-manager-issuer/overview) | [✔️](https://github.com/CZERTAINLY/CZERTAINLY-Cert-Manager-Issuer/releases) | ✔️ |
| 🥈 | command-issuer | [📄](https://github.com/Keyfactor/command-cert-manager-issuer) | [Keyfactor Command](https://www.keyfactor.com/products/command/) | - | [✔️](https://github.com/Keyfactor/command-cert-manager-issuer/releases) | ✔️ |
| 🥈 | cview-issuer | [📄](https://secure-ly.github.io/cview-issuer-chart) | [CView-issuer](https://secure-ly.github.io/cview-issuer-chart) | - | [✔️](https://github.com/secure-ly/cview-issuer-chart/releases) | ❌ |
| 🥈 | ejbca-issuer | [📄](https://github.com/Keyfactor/ejbca-cert-manager-issuer) | [EJBCA](https://www.ejbca.org/) | - | [✔️](https://github.com/Keyfactor/ejbca-cert-manager-issuer/tags) | ✔️ |
| 🥈 | google-cas-issuer | [📄](https://github.com/cert-manager/google-cas-issuer) | [Google Cloud Certificate Authority Service](https://cloud.google.com/certificate-authority-service/) | - | [✔️](https://github.com/cert-manager/google-cas-issuer) | ✔️ |
| 🥈 | gs-atlas-issuer | [📄](https://github.com/globalsign/atlas-cert-manager) | [GlobalSign CA](https://www.globalsign.com/en/atlas) | - | [✔️](https://github.com/globalsign/atlas-cert-manager/releases) | ✔️ |
| 🥈 | horizon-issuer | [📄](https://github.com/evertrust/horizon-issuer) | [EVERTRUST Horizon](https://evertrust.fr/horizon) | - | [✔️](https://github.com/evertrust/horizon-issuer/releases) | ✔️ |
| 🥈 | ncm-issuer | [📄](https://github.com/nokia/ncm-issuer) | [Nokia Netguard Certificate Manager](https://www.nokia.com/networks/security-portfolio/netguard/certificate-manager) | - | [✔️](https://github.com/nokia/ncm-issuer/releases) | ✔️ |
| 🥈 | selfsigned-issuer (in-tree) | [📄](https://cert-manager.io/docs/configuration/selfsigned/) | Self-Signed issuer | - | [✔️](https://cert-manager.io/docs/releases/) | ✔️ |
| 🥈 | step-issuer | [📄](https://github.com/smallstep/step-issuer) | [Certificate Authority server](https://github.com/smallstep/certificates) | - | [✔️](https://github.com/smallstep/step-issuer/releases) | ✔️ |
| 🥈 | vault-issuer (in-tree) | [📄](https://cert-manager.io/docs/configuration/vault/) | [HashiCorp Vault](https://www.vaultproject.io/) | - | [✔️](https://cert-manager.io/docs/releases/) | ✔️ |
| 🥈 | venafi-issuer (in-tree) | [📄](https://cert-manager.io/docs/configuration/venafi/) | [Venafi TLS Protect](https://www.cyberark.com/products/certificate-manager/) | - | [✔️](https://cert-manager.io/docs/releases/) | ✔️ |
| 🥈 | cfssl-issuer | [📄](https://gerrit.wikimedia.org/r/plugins/gitiles/operations/software/cfssl-issuer) | [CFSSL](https://github.com/cloudflare/cfssl) | - | [✔️](https://gerrit.wikimedia.org/r/plugins/gitiles/operations/software/cfssl-issuer/+refs) | ✔️ |
| 🥈 | cfmtls-issuer | [📄](https://github.com/k8stooling/cfmtls-issuer) | [CFMTLS](https://developers.cloudflare.com/ssl/client-certificates/create-a-client-certificate/) | - | [✔️](https://github.com/k8stooling/cfmtls-issuer/releases/) | ✔️ |
| 🥈 | zerossl-issuer | [📄](https://github.com/topfreegames/zerossl-issuer) | [ZeroSSL](https://zerossl.com/) | - | [✔️](https://github.com/topfreegames/zerossl-issuer/releases) | ✔️ |
| 🥉 | tcs-issuer | [📄](https://github.com/intel/trusted-certificate-issuer) | [Intel's SGX technology](https://www.intel.com/content/www/us/en/developer/tools/software-guard-extensions/overview.html) | - | [❌](https://github.com/intel/trusted-certificate-issuer/releases) | ✔️ |
| 🥉 | freeipa-issuer | [📄](https://github.com/guilhem/freeipa-issuer) | [FreeIPA](https://www.freeipa.org/) | - | [❌](https://github.com/guilhem/freeipa-issuer/releases) | ✔️ |
| 🥉 | kms-issuer | [📄](https://github.com/Skyscanner/kms-issuer) | [AWS KMS](https://aws.amazon.com/kms/) | - | [❌](https://github.com/Skyscanner/kms-issuer/releases) | ✔️ |
| 🥉 | keyvault-issuer | [📄](https://github.com/gonicus/azure-keyvault-issuer) | [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/keys/about-keys) | - | [❌](https://github.com/gonicus/azure-keyvault-issuer/releases) | ✔️ |

*   The issuers are sorted by their tier and then alphabetically.
*   "in-tree" issuers are issuers that are shipped with cert-manager itself.
*   These issuers are known to support and honor [approval](https://cert-manager.io/docs/concepts/certificaterequest/#approval).

If you've created an issuer which you'd like to share, [raise a Pull Request](https://github.com/cert-manager/website/pulls) to have it added here!

Issuer Tier system[](https://cert-manager.io/docs/configuration/issuers/#issuer-tier-system)
--------------------------------------------------------------------------------------------

The cert-manager project has a tier system for issuers. This is to help users understand the maturity of the issuer. The tiers are 🥇, 🥈 and 🥉.

NOTE: The cert-manager maintainers can decide to change the criteria and number of tiers at any time.

### 🥇 Tier (Production-ready)[](https://cert-manager.io/docs/configuration/issuers/#-tier-production-ready)

*   The issuer has an end-to-end tutorial on how to set it up with cert-manager for use in production. At the time of checking[1](https://cert-manager.io/docs/configuration/issuers/#user-content-fn-1), the used cert-manager version has to be still supported (see [Supported Releases](https://cert-manager.io/docs/releases/)). An end-to-end tutorial must include:
    1.   a short explanation on how to install cert-manager (including the used version and a link to [https://cert-manager.io/docs/installation/](https://cert-manager.io/docs/installation/))
    2.   all required steps to install the issuer
    3.   an explanation on how to configure the issuer's Custom Resources
    4.   an explanation on how to issue a certificate using the issuer (using a Certificate resource)

### 🥈 Tier (Maintained)[](https://cert-manager.io/docs/configuration/issuers/#-tier-maintained)

*   The issuer has had a release in the last 12 months (at the time of checking all issuers[2](https://cert-manager.io/docs/configuration/issuers/#user-content-fn-2)).

### 🥉 Tier (Unmaintained)[](https://cert-manager.io/docs/configuration/issuers/#-tier-unmaintained)

Other

Building New External Issuers[](https://cert-manager.io/docs/configuration/issuers/#building-new-external-issuers)
------------------------------------------------------------------------------------------------------------------

If you're interested in building a new external issuer, check the [development documentation](https://cert-manager.io/docs/contributing/external-issuers/).

Footnotes[](https://cert-manager.io/docs/configuration/issuers/#footnote-label)
-------------------------------------------------------------------------------

1.   checked on 3rd of October 2024 [↩](https://cert-manager.io/docs/configuration/issuers/#user-content-fnref-1)[↩2](https://cert-manager.io/docs/configuration/issuers/#user-content-fnref-1-2)

2.   checked on 3rd of October 2024 [↩](https://cert-manager.io/docs/configuration/issuers/#user-content-fnref-2)[↩2](https://cert-manager.io/docs/configuration/issuers/#user-content-fnref-2-2)
