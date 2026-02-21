# Source: https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0

Title: Upgrading from v0.16 to v1.0

URL Source: https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0

Markdown Content:
Upgrading from v0.16 to v1.0 - cert-manager Documentation
===============

[](https://cert-manager.io/)

*   [Project](https://cert-manager.io/)
*   [Documentation](https://cert-manager.io/docs/)
*   [Announcements](https://cert-manager.io/announcements/)
*   [Support](https://cert-manager.io/support/)
*   Search
*   [Get started](https://cert-manager.io/docs/getting-started/)

*   [Project](https://cert-manager.io/)
*   [Documentation](https://cert-manager.io/docs/)
*   [Announcements](https://cert-manager.io/announcements/)
*   [Support](https://cert-manager.io/support/)

*   Search
*   [Get started](https://cert-manager.io/docs/getting-started/)

NEW: Get project updates on[Twitter](https://twitter.com/CertManager/)and[Mastodon](https://infosec.exchange/@CertManager)

Docs Menu

*   [Introduction](https://cert-manager.io/docs/)
*   [Getting Started](https://cert-manager.io/docs/getting-started/)
*   
Releases
    *   [Supported Releases](https://cert-manager.io/docs/releases/)
    *   [1.19](https://cert-manager.io/docs/releases/release-notes/release-notes-1.19)
    *   [Upgrade 1.18 to 1.19](https://cert-manager.io/docs/releases/upgrading/upgrading-1.18-1.19)
    *   [1.18](https://cert-manager.io/docs/releases/release-notes/release-notes-1.18)
    *   [Upgrade 1.17 to 1.18](https://cert-manager.io/docs/releases/upgrading/upgrading-1.17-1.18)
    *   
Older releases
        *   [Notes on Ingress Class Compatibility](https://cert-manager.io/docs/releases/upgrading/ingress-class-compatibility/)
        *   [Migrating Deprecated API Resources](https://cert-manager.io/docs/releases/upgrading/remove-deprecated-apis/)
        *   [1.17](https://cert-manager.io/docs/releases/release-notes/release-notes-1.17)
        *   [Upgrade 1.16 to 1.17](https://cert-manager.io/docs/releases/upgrading/upgrading-1.16-1.17)
        *   [1.16](https://cert-manager.io/docs/releases/release-notes/release-notes-1.16)
        *   [Upgrade 1.15 to 1.16](https://cert-manager.io/docs/releases/upgrading/upgrading-1.15-1.16)
        *   [1.15](https://cert-manager.io/docs/releases/release-notes/release-notes-1.15)
        *   [Upgrade 1.14 to 1.15](https://cert-manager.io/docs/releases/upgrading/upgrading-1.14-1.15)
        *   [1.14](https://cert-manager.io/docs/releases/release-notes/release-notes-1.14)
        *   [Upgrade 1.13 to 1.14](https://cert-manager.io/docs/releases/upgrading/upgrading-1.13-1.14)
        *   [1.13](https://cert-manager.io/docs/releases/release-notes/release-notes-1.13)
        *   [Upgrading from 1.12](https://cert-manager.io/docs/releases/upgrading/upgrading-1.12)
        *   [1.12](https://cert-manager.io/docs/releases/release-notes/release-notes-1.12)
        *   [Upgrade 1.11 to 1.12](https://cert-manager.io/docs/releases/upgrading/upgrading-1.11-1.12)
        *   [1.11](https://cert-manager.io/docs/releases/release-notes/release-notes-1.11)
        *   [Upgrade 1.10 to 1.11](https://cert-manager.io/docs/releases/upgrading/upgrading-1.10-1.11)
        *   [1.10](https://cert-manager.io/docs/releases/release-notes/release-notes-1.10)
        *   [Upgrade 1.9 to 1.10](https://cert-manager.io/docs/releases/upgrading/upgrading-1.9-1.10)
        *   [1.9](https://cert-manager.io/docs/releases/release-notes/release-notes-1.9)
        *   [Upgrade 1.8 to 1.9](https://cert-manager.io/docs/releases/upgrading/upgrading-1.8-1.9)
        *   [1.8](https://cert-manager.io/docs/releases/release-notes/release-notes-1.8)
        *   [Upgrade 1.7 to 1.8](https://cert-manager.io/docs/releases/upgrading/upgrading-1.7-1.8)
        *   [1.7](https://cert-manager.io/docs/releases/release-notes/release-notes-1.7)
        *   [Upgrade 1.6 to 1.7](https://cert-manager.io/docs/releases/upgrading/upgrading-1.6-1.7)
        *   [1.6](https://cert-manager.io/docs/releases/release-notes/release-notes-1.6)
        *   [Upgrade 1.5 to 1.6](https://cert-manager.io/docs/releases/upgrading/upgrading-1.5-1.6)
        *   [1.5](https://cert-manager.io/docs/releases/release-notes/release-notes-1.5)
        *   [Upgrade 1.4 to 1.5](https://cert-manager.io/docs/releases/upgrading/upgrading-1.4-1.5)
        *   [1.4](https://cert-manager.io/docs/releases/release-notes/release-notes-1.4)
        *   [Upgrade 1.3 to 1.4](https://cert-manager.io/docs/releases/upgrading/upgrading-1.3-1.4)
        *   [1.3](https://cert-manager.io/docs/releases/release-notes/release-notes-1.3)
        *   [Upgrade 1.2 to 1.3](https://cert-manager.io/docs/releases/upgrading/upgrading-1.2-1.3)
        *   [1.2](https://cert-manager.io/docs/releases/release-notes/release-notes-1.2)
        *   [Upgrade 1.1 to 1.2](https://cert-manager.io/docs/releases/upgrading/upgrading-1.1-1.2)
        *   [1.1](https://cert-manager.io/docs/releases/release-notes/release-notes-1.1)
        *   [Upgrade 1.0 to 1.1](https://cert-manager.io/docs/releases/upgrading/upgrading-1.0-1.1)
        *   [1.0](https://cert-manager.io/docs/releases/release-notes/release-notes-1.0)
        *   [Upgrade 0.16 to 1.0](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0)
        *   [0.16](https://cert-manager.io/docs/releases/release-notes/release-notes-0.16)
        *   [Upgrade 0.15 to 0.16](https://cert-manager.io/docs/releases/upgrading/upgrading-0.15-0.16)
        *   [0.15](https://cert-manager.io/docs/releases/release-notes/release-notes-0.15)
        *   [Upgrade 0.14 to 0.15](https://cert-manager.io/docs/releases/upgrading/upgrading-0.14-0.15)
        *   [0.14](https://cert-manager.io/docs/releases/release-notes/release-notes-0.14)
        *   [Upgrade 0.13 to 0.14](https://cert-manager.io/docs/releases/upgrading/upgrading-0.13-0.14)
        *   [0.13](https://cert-manager.io/docs/releases/release-notes/release-notes-0.13)
        *   [Upgrade 0.12 to 0.13](https://cert-manager.io/docs/releases/upgrading/upgrading-0.12-0.13)
        *   [0.12](https://cert-manager.io/docs/releases/release-notes/release-notes-0.12)
        *   [Upgrade 0.11 to 0.12](https://cert-manager.io/docs/releases/upgrading/upgrading-0.11-0.12)
        *   [0.11](https://cert-manager.io/docs/releases/release-notes/release-notes-0.11)
        *   [Upgrade 0.10 to 0.11](https://cert-manager.io/docs/releases/upgrading/upgrading-0.10-0.11)
        *   [0.10](https://cert-manager.io/docs/releases/release-notes/release-notes-0.10)
        *   [Upgrade 0.9 to 0.10](https://cert-manager.io/docs/releases/upgrading/upgrading-0.9-0.10)
        *   [0.9](https://cert-manager.io/docs/releases/release-notes/release-notes-0.9)
        *   [Upgrade 0.8 to 0.9](https://cert-manager.io/docs/releases/upgrading/upgrading-0.8-0.9)
        *   [0.8](https://cert-manager.io/docs/releases/release-notes/release-notes-0.8)
        *   [Upgrade 0.7 to 0.8](https://cert-manager.io/docs/releases/upgrading/upgrading-0.7-0.8)
        *   [0.7](https://cert-manager.io/docs/releases/release-notes/release-notes-0.7)
        *   [Upgrade 0.6 to 0.7](https://cert-manager.io/docs/releases/upgrading/upgrading-0.6-0.7)
        *   [0.6](https://cert-manager.io/docs/releases/release-notes/release-notes-0.6)
        *   [Upgrade 0.5 to 0.6](https://cert-manager.io/docs/releases/upgrading/upgrading-0.5-0.6)
        *   [0.5](https://cert-manager.io/docs/releases/release-notes/release-notes-0.5)
        *   [Upgrade 0.4 to 0.5](https://cert-manager.io/docs/releases/upgrading/upgrading-0.4-0.5)
        *   [0.4](https://cert-manager.io/docs/releases/release-notes/release-notes-0.4)
        *   [Upgrade 0.3 to 0.4](https://cert-manager.io/docs/releases/upgrading/upgrading-0.3-0.4)
        *   [0.3](https://cert-manager.io/docs/releases/release-notes/release-notes-0.3)
        *   [Upgrade 0.2 to 0.3](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3)
        *   [0.2](https://cert-manager.io/docs/releases/release-notes/release-notes-0.2)
        *   [0.1](https://cert-manager.io/docs/releases/release-notes/release-notes-0.1)

*   
0. Installation
    *   [Introduction](https://cert-manager.io/docs/installation/)
    *   [a. kubectl apply](https://cert-manager.io/docs/installation/kubectl/)
    *   [b. Helm](https://cert-manager.io/docs/installation/helm/)
    *   [d. Continuous Deployment](https://cert-manager.io/docs/installation/continuous-deployment-and-gitops/)
    *   [Configuring Components](https://cert-manager.io/docs/installation/configuring-components/)
    *   [Upgrade](https://cert-manager.io/docs/installation/upgrade/)
    *   [Reinstall](https://cert-manager.io/docs/installation/reinstall/)
    *   [Uninstall](https://cert-manager.io/docs/installation/uninstall/)
    *   [Signature Verification](https://cert-manager.io/docs/installation/code-signing/)

*   
1. Configuring Issuers
    *   [Introduction](https://cert-manager.io/docs/configuration/)
    *   [Issuers](https://cert-manager.io/docs/configuration/issuers/)
    *   
In-tree Issuer Config
        *   [SelfSigned](https://cert-manager.io/docs/configuration/selfsigned/)
        *   [CA](https://cert-manager.io/docs/configuration/ca/)
        *   [Vault](https://cert-manager.io/docs/configuration/vault/)
        *   [CyberArk](https://cert-manager.io/docs/configuration/venafi/)
        *   
ACME
            *   [Introduction](https://cert-manager.io/docs/configuration/acme/)
            *   
HTTP01
                *   [Introduction](https://cert-manager.io/docs/configuration/acme/http01/)
                *   [External Load Balancer](https://cert-manager.io/docs/configuration/acme/http01/externalloadbalancer/)

            *   
DNS01
                *   [Introduction](https://cert-manager.io/docs/configuration/acme/dns01/)
                *   [ACMEDNS](https://cert-manager.io/docs/configuration/acme/dns01/acme-dns/)
                *   [Akamai](https://cert-manager.io/docs/configuration/acme/dns01/akamai/)
                *   [AzureDNS](https://cert-manager.io/docs/configuration/acme/dns01/azuredns/)
                *   [Cloudflare](https://cert-manager.io/docs/configuration/acme/dns01/cloudflare/)
                *   [DigitalOcean](https://cert-manager.io/docs/configuration/acme/dns01/digitalocean/)
                *   [Google CloudDNS](https://cert-manager.io/docs/configuration/acme/dns01/google/)
                *   [RFC-2136](https://cert-manager.io/docs/configuration/acme/dns01/rfc2136/)
                *   [Route53](https://cert-manager.io/docs/configuration/acme/dns01/route53/)
                *   [Webhook](https://cert-manager.io/docs/configuration/acme/dns01/webhook/)

*   
2. Requesting Certificates
    *   [Introduction](https://cert-manager.io/docs/usage/)
    *   [Certificate](https://cert-manager.io/docs/usage/certificate/)
    *   [CertificateRequest](https://cert-manager.io/docs/usage/certificaterequest/)
    *   [Ingress](https://cert-manager.io/docs/usage/ingress/)
    *   [Gateway](https://cert-manager.io/docs/usage/gateway/)
    *   [CertificateSigningRequests](https://cert-manager.io/docs/usage/kube-csr/)
    *   
Service Mesh
        *   
istio-csr
            *   [Installation](https://cert-manager.io/docs/usage/istio-csr/installation/)
            *   [Usage](https://cert-manager.io/docs/usage/istio-csr/)

    *   
CSI Driver
        *   [Introduction](https://cert-manager.io/docs/usage/csi/)
        *   
csi-driver
            *   [Installation](https://cert-manager.io/docs/usage/csi-driver/installation/)
            *   [Usage](https://cert-manager.io/docs/usage/csi-driver/)

        *   
csi-driver-spiffe
            *   [Installation](https://cert-manager.io/docs/usage/csi-driver-spiffe/installation/)
            *   [Usage](https://cert-manager.io/docs/usage/csi-driver-spiffe/)

*   
3. Distributing Trust
    *   [Introduction](https://cert-manager.io/docs/trust/)
    *   
trust-manager
        *   [Installation](https://cert-manager.io/docs/trust/trust-manager/installation/)
        *   [Usage](https://cert-manager.io/docs/trust/trust-manager/)
        *   [API Reference](https://cert-manager.io/docs/trust/trust-manager/api-reference/)

*   
4. Defining Policy
    *   [Introduction](https://cert-manager.io/docs/policy/)
    *   [Defaulting](https://cert-manager.io/docs/policy/defaulting/)
    *   
Approval
        *   [Introduction](https://cert-manager.io/docs/policy/approval/)
        *   
approver-policy
            *   [Installation](https://cert-manager.io/docs/policy/approval/approver-policy/installation/)
            *   [Usage](https://cert-manager.io/docs/policy/approval/approver-policy/)
            *   [API Reference](https://cert-manager.io/docs/policy/approval/approver-policy/api-reference/)

    *   [Issuing](https://cert-manager.io/docs/policy/issuing/)

*   
Tutorials
    *   [Introduction](https://cert-manager.io/docs/tutorials/)
    *   [Securing NGINX-ingress](https://cert-manager.io/docs/tutorials/acme/nginx-ingress/)
    *   [GKE + Ingress + Let's Encrypt](https://cert-manager.io/docs/tutorials/getting-started-with-cert-manager-on-google-kubernetes-engine-using-lets-encrypt-for-ingress-ssl/)
    *   [AKS + LoadBalancer + Let's Encrypt](https://cert-manager.io/docs/tutorials/getting-started-aks-letsencrypt/)
    *   [AWS + LoadBalancer + Let's Encrypt](https://cert-manager.io/docs/tutorials/getting-started-aws-letsencrypt/)
    *   [Migrating from Kube-LEGO](https://cert-manager.io/docs/tutorials/acme/migrating-from-kube-lego/)
    *   [DNS Validation](https://cert-manager.io/docs/tutorials/acme/dns-validation/)
    *   [HTTP Validation](https://cert-manager.io/docs/tutorials/acme/http-validation/)
    *   [Pomerium Ingress](https://cert-manager.io/docs/tutorials/acme/pomerium-ingress/)
    *   [EKS + Ingress + CyberArk](https://cert-manager.io/docs/tutorials/venafi/venafi/)
    *   [Securing Ingresses with ZeroSSL](https://cert-manager.io/docs/tutorials/zerossl/zerossl/)
    *   [Managing public trust in kubernetes with trust-manager](https://cert-manager.io/docs/tutorials/getting-started-with-trust-manager/)
    *   [Setting default certificate values](https://cert-manager.io/docs/tutorials/certificate-defaults/)

*   
DevOps Tips
    *   [Installing on a Cloud Provider](https://cert-manager.io/docs/installation/compatibility/)
    *   [Prometheus Metrics](https://cert-manager.io/docs/devops-tips/prometheus-metrics/)
    *   [Backup and Restore Resources](https://cert-manager.io/docs/devops-tips/backup/)
    *   [Syncing Secrets Across Namespaces](https://cert-manager.io/docs/devops-tips/syncing-secrets-across-namespaces/)
    *   [Best Practice Installation Options](https://cert-manager.io/docs/installation/best-practice/)
    *   [Scaling cert-manager](https://cert-manager.io/docs/devops-tips/scaling-cert-manager/)

*   
Troubleshooting & FAQ
    *   [Introduction](https://cert-manager.io/docs/troubleshooting/)
    *   [Frequently Asked Questions](https://cert-manager.io/docs/faq/)
    *   [Troubleshooting ACME / Let's Encrypt Certificates](https://cert-manager.io/docs/troubleshooting/acme/)
    *   [Troubleshooting webhook](https://cert-manager.io/docs/troubleshooting/webhook/)

*   
Contributing
    *   [Introduction](https://cert-manager.io/docs/contributing/)
    *   [Projects](https://cert-manager.io/docs/contributing/projects/)
    *   [Feature Policy](https://cert-manager.io/docs/contributing/policy/)
    *   [Building cert-manager](https://cert-manager.io/docs/contributing/building/)
    *   [Contributing Flow](https://cert-manager.io/docs/contributing/contributing-flow/)
    *   [CRDs](https://cert-manager.io/docs/contributing/crds/)
    *   [DNS Providers](https://cert-manager.io/docs/contributing/dns-providers/)
    *   [Running End-to-End Tests](https://cert-manager.io/docs/contributing/e2e/)
    *   [OSS-Fuzz Tests](https://cert-manager.io/docs/contributing/oss-fuzz/)
    *   [Implementing External Issuers](https://cert-manager.io/docs/contributing/external-issuers/)
    *   [DCO Sign Off](https://cert-manager.io/docs/contributing/sign-off/)
    *   [Release Process](https://cert-manager.io/docs/contributing/release-process/)
    *   [Developing with Kind](https://cert-manager.io/docs/contributing/kind/)
    *   [Feature gates](https://cert-manager.io/docs/contributing/featuregates/)
    *   
Google Season of Docs
        *   [Introduction](https://cert-manager.io/docs/contributing/google-season-of-docs/)
        *   
2022
            *   [Introduction](https://cert-manager.io/docs/contributing/google-season-of-docs/2022/)
            *   [Improve the Navigation and Structure of the cert-manager Website](https://cert-manager.io/docs/contributing/google-season-of-docs/2022/improve-navigation-and-structure/)

    *   [Reporting Security Issues](https://cert-manager.io/docs/contributing/security/)
    *   [Coding Conventions](https://cert-manager.io/docs/contributing/coding-conventions/)
    *   [Third Party Code Donations](https://cert-manager.io/docs/contributing/third-party-code-donation/)
    *   [Signing Keys](https://cert-manager.io/docs/contributing/signing-keys/)
    *   [API compatibility](https://cert-manager.io/docs/contributing/api-compatibility/)
    *   [Importing cert-manager in Go](https://cert-manager.io/docs/contributing/importing/)

*   
Reference
    *   [Introduction](https://cert-manager.io/docs/reference/)
    *   [Command Line Tool (cmctl)](https://cert-manager.io/docs/reference/cmctl/)
    *   [TLS Terminology](https://cert-manager.io/docs/reference/tls-terminology/)
    *   
Components / Docker Images
        *   [Introduction](https://cert-manager.io/docs/cli/)
        *   [acmesolver](https://cert-manager.io/docs/cli/acmesolver/)
        *   [cainjector](https://cert-manager.io/docs/cli/cainjector/)
        *   [cmctl](https://cert-manager.io/docs/cli/cmctl/)
        *   [controller](https://cert-manager.io/docs/cli/controller/)
        *   [webhook](https://cert-manager.io/docs/cli/webhook/)
        *   [startupapicheck](https://cert-manager.io/docs/cli/startupapicheck/)

    *   [API Reference](https://cert-manager.io/docs/reference/api-docs/)
    *   [Annotations](https://cert-manager.io/docs/reference/annotations/)
    *   
Concepts
        *   [Introduction](https://cert-manager.io/docs/concepts/)
        *   [Issuer](https://cert-manager.io/docs/concepts/issuer/)
        *   [ACME Orders and Challenges](https://cert-manager.io/docs/concepts/acme-orders-challenges/)
        *   [Webhook](https://cert-manager.io/docs/concepts/webhook/)
        *   [CA Injector](https://cert-manager.io/docs/concepts/ca-injector/)

version: latest

Upgrading from v0.16 to v1.0
============================

> The upgrade process for upgrading to `v1.0` is very Kubernetes version specific. Please check the version of your cluster using `kubectl version` and follow the steps required for your version of Kubernetes.

Issue with older versions of `kubectl`[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#issue-with-older-versions-of-kubectl)
-------------------------------------------------------------------------------------------------------------------------------------------------

`kubectl` versions with patch versions lower than `v1.18.8``v1.17.11` or `v1.16.14` have issues updating from the `v0.16` CRD files, due to [a bug when handling deeply nested CRDs](https://github.com/kubernetes/kubernetes/issues/91615). This bug will make `kubectl apply -f [...]` hang.

This bug only happens during a re-apply of the v0.16 CRDs or upgrading from it. Upgrades from lower versions do not cause issues. If you have this issue please upgrade your `kubectl` to the latest patch release. Versions of `kubectl` of `v1.15.x` or below are not being supported anymore as these are unsupported by the Kubernetes community.

### Helm[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#helm)

Helm users who use `installCRDs=true` MUST upgrade to Helm `v3.3.1` or later before upgrading.

Upgrade instructions per Kubernetes version[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#upgrade-instructions-per-kubernetes-version)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

### Kubernetes `1.16` and above[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#kubernetes-116-and-above)

These are the upgrade instructions to upgrade from cert-manager `v0.14.0` or higher, please consult other upgrade guides first before upgrading to `v1.0` if you run an older version of cert-manager.

No special requirements, you can follow the [regular upgrade process](https://cert-manager.io/docs/installation/upgrade/).

### Kubernetes `1.15.x`[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#kubernetes-115x)

cert-manager now uses `apiextensions.k8s.io/v1` to install CRDs inside Kubernetes. This got added in Kubernetes `1.16`. Our legacy installation will still be using `apiextensions.k8s.io/v1beta1`. For this reason Kubernetes 1.15 users now need to install the legacy version of the cert-manager manifests. You can follow the instructions of "Kubernetes 1.14" below on how to upgrade to the legacy version of `v1.0`.

> **Note**: The legacy version only supports a single CRD version. We advise you to consider upgrading to Kubernetes 1.16 or above for an easier migration.

### Kubernetes `1.14` and below[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#kubernetes-114-and-below)

These are the upgrade instructions to upgrade from cert-manager `v0.11.0` or higher, please consult other upgrade guides first before upgrading to `v1.0` if you run an older version of cert-manager.

> **Note**: Due to the lack of support for conversion webhooks in your Kubernetes version this will not be an easy migration. We advise you to consider upgrading to Kubernetes 1.16 or higher before upgrading. Upgrading your Kubernetes cluster might be easier than upgrading cert-manager.

We have released our `cert-manager.io/v1` API that replaces `cert-manager.io/v1alpha2`. Since the legacy version for Kubernetes 1.15 and below only supports one CRD version you have to transition all resources to `cert-manager.io/v1`.

This makes for a fairly significant breaking change for users, as **all** cert-manager resources will need to be updated to reflect these changes. Ingress annotations will stay the same, this means if you only use ingress-shim you do not have to convert these resources over but it is recommended. However you should convert the (Cluster)Issuers and delete the old CRD versions.

This upgrade MUST be performed in the following sequence of steps:

1.   [Back up](https://cert-manager.io/docs/devops-tips/backup/) existing cert-manager resources. See the backup section.

2.   [Uninstall cert-manager](https://cert-manager.io/docs/installation/uninstall/).

3.   Update the `apiVersion` on all your backed up resources from `cert-manager.io/v1alpha2` to `cert-manager.io/v1`. See the converting section for that.

4.   Ensure the old cert-manager CRD resources have also been deleted: `kubectl get crd | grep cert-manager.io`

5.   Re-install cert-manager `v1.0` from scratch according to the [installation guide](https://cert-manager.io/docs/installation/upgrade/).

6.   Apply the backed up resources again.

You must be sure to properly **backup**, **uninstall**, **re-install** and **restore** your installation in order to ensure the upgrade is successful.

#### Backing up resources[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#backing-up-resources)

You can backup the custom resources you or cert-manager created using the following `kubectl` command:

kubectl get -o yaml \

 --all-namespaces \

 issuer,clusterissuer,certificates,certificaterequests > cert-manager-backup.yaml

_Note that this will not export private keys or secrets._

#### Converting resources[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#converting-resources)

You can use [cmctl convert](https://cert-manager.io/docs/reference/cmctl/#convert) to automatically convert your backup from `v1alpha2` to `v1` using the following command:

cmctl convert --output-version cert-manager.io/v1 -f cert-manager-backup.yaml > cert-manager-v1.yaml

_Tip:_ you can use `kubectl apply --dry-run` on a local/test cluster with cert-manager `v1.0` installed to validate your conversion

#### Uninstall cert-manager[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#uninstall-cert-manager)

Next step is to uninstall cert-manager. This will cause a temporary halt to renewal of certificates but will not affect any TLS traffic.

How you do this depends on how you installed cert-manager.

Using Helm:

$ helm --namespace cert-manager delete cert-manager

Using `kubectl`:

kubectl delete -f https://github.com/cert-manager/cert-manager/releases/download/vX.Y.Z/cert-manager.yaml

Make sure you also delete the CRDs. This will delete all cert-manager resources, so make sure your backup is complete. You can do this manually by executing the following commands:

kubectl delete crd certificaterequests.cert-manager.io

kubectl delete crd certificates.cert-manager.io

kubectl delete crd challenges.acme.cert-manager.io

kubectl delete crd clusterissuers.cert-manager.io

kubectl delete crd issuers.cert-manager.io

kubectl delete crd orders.acme.cert-manager.io

For more info see the [uninstall cert-manager guide](https://cert-manager.io/docs/installation/uninstall/).

#### Reinstall and restore[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#reinstall-and-restore)

To install cert-manager again you can follow the normal [installation guide](https://cert-manager.io/docs/installation/upgrade/).

Once it has been fully installed you can re-apply the converted resources:

kubectl apply -f cert-manager-v1.yaml

Congratulations you're now fully upgraded to cert-manager `v1.0`

#### On this page

*   [Issue with older versions of `kubectl`](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#issue-with-older-versions-of-kubectl "Issue with older versions of `kubectl`")
*   [Upgrade instructions per Kubernetes version](https://cert-manager.io/docs/releases/upgrading/upgrading-0.16-1.0#upgrade-instructions-per-kubernetes-version "Upgrade instructions per Kubernetes version")

© 2026 The cert-manager Authors.

© 2026 The Linux Foundation. All rights reserved.

The Linux Foundation has registered trademarks and uses trademarks.

For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page.](https://www.linuxfoundation.org/trademark-usage/)
