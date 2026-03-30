# Source: https://cert-manager.io/docs/releases/upgrading/upgrading-0.10-0.11

Title: Upgrading from v0.10 to v0.11

URL Source: https://cert-manager.io/docs/releases/upgrading/upgrading-0.10-0.11

Markdown Content:
Upgrading from v0.10 to v0.11 - cert-manager Documentation
===============

[](https://cert-manager.io/)

*   [Project](https://cert-manager.io/)
*   [Documentation](https://cert-manager.io/docs/)
*   [Announcements](https://cert-manager.io/announcements/)
*   [Support](https://cert-manager.io/support/)
*   Search Ctrl K
*   [Get started](https://cert-manager.io/docs/getting-started/)

*   [Project](https://cert-manager.io/)
*   [Documentation](https://cert-manager.io/docs/)
*   [Announcements](https://cert-manager.io/announcements/)
*   [Support](https://cert-manager.io/support/)

*   Search Ctrl K
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

Upgrading from v0.10 to v0.11
=============================

The `v0.11` release marks the removal of the `v1alpha1` API that was used in previous versions of cert-manager, as well as our API group changing to be `cert-manager.io` instead of `certmanager.k8s.io`.

We have also removed support for the **old configuration format** that was deprecated in the `v0.8` release. This means you **must** transition to using the new `solvers` style configuration format for your ACME issuers **before** upgrading to `v0.11`. For more information, see the [upgrading to `v0.8`](https://cert-manager.io/docs/releases/upgrading/upgrading-0.7-0.8/) guide.

This makes for a fairly significant breaking change for users, as **all** cert-manager resources, or even Ingresses that reference cert-manager resources, will need to be updated to reflect these changes.

This upgrade should be performed in a few steps:

1.   Back up existing cert-manager resources, as per the [backup and restore guide](https://cert-manager.io/docs/devops-tips/backup/).

2.   [Uninstall cert-manager](https://cert-manager.io/docs/installation/uninstall/).

3.   Ensure the old cert-manager CRD resources have also been deleted: `kubectl get crd | grep certmanager.k8s.io`

4.   Update the `apiVersion` on all your backed up resources from `certmanager.k8s.io/v1alpha1` to `cert-manager.io/v1alpha2`.

5.   Re-install cert-manager from scratch according to the [installation guide](https://cert-manager.io/docs/installation/upgrade/).

You must be sure to properly **backup**, **uninstall**, **re-install** and **restore** your installation in order to ensure the upgrade is successful.

Additional annotation changes[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.10-0.11#additional-annotation-changes)
----------------------------------------------------------------------------------------------------------------------------------

As well as changing the API group used by our CRDs, we have also changed the annotation-based configuration key to **also** reflect the new API group.

This means that if you use any cert-manager annotations on any of your other resources (such as Ingresses, `{Validating,Mutating}WebhookConfiguration`, etc) you will need to update them to reflect the new API group.

A full table of annotations, including the old and new equivalents:

| Old Annotation | New Annotation |
| --- | --- |
| `certmanager.k8s.io/acme-http01-edit-in-place` | `acme.cert-manager.io/http01-edit-in-place` |
| `certmanager.k8s.io/acme-http01-ingress-class` | `acme.cert-manager.io/http01-ingress-class` |
| `certmanager.k8s.io/issuer` | `cert-manager.io/issuer` |
| `certmanager.k8s.io/cluster-issuer` | `cert-manager.io/cluster-issuer` |
| `certmanager.k8s.io/acme-challenge-type` | `DEPRECATED` |
| `certmanager.k8s.io/acme-dns01-provider` | `DEPRECATED` |
| `certmanager.k8s.io/alt-names` | `cert-manager.io/alt-names` |
| `certmanager.k8s.io/ip-sans` | `cert-manager.io/ip-sans` |
| `certmanager.k8s.io/common-name` | `cert-manager.io/common-name` |
| `certmanager.k8s.io/issuer-name` | `cert-manager.io/issuer-name` |
| `certmanager.k8s.io/issuer-kind` | `cert-manager.io/issuer-kind` |

You can use the following bash magic to print a list of Ingress resources that still contain an old annotation:

$ kubectl get ingress \

 --all-namespaces \

 -o json | \

 jq '.items[] | select(.metadata.annotations| to_entries | map(.key)[] | test("certmanager")) | "Ingress resource \(.metadata.namespace)/\(.metadata.name) contains old annotations: (\( .metadata.annotations | to_entries | map(.key)[] | select( . | test("certmanager") ) ))"'

Ingress resource "demo/testcrt contains old annotations: (certmanager.k8s.io/cluster-issuer)"

Ingress resource "example/ingress-resource contains old annotations: (certmanager.k8s.io/cluster-issuer)"

In order to help with this migration, the following CLI tool will automatically migrate these annotations for you. Note that it _will not_ make any changes to your cluster for you.

Firstly, download the binary for your given platform

$ wget -O api-migration https://github.com/cert-manager/cert-manager/releases/download/v0.11.0/api-migration-linux

Or for Darwin

$ wget -O api-migration https://github.com/cert-manager/cert-manager/releases/download/v0.11.0/api-migration-darwin

Mark the binary as executable and run the binary against your cluster

$ chmod +x api-migration && ./api-migration --kubeconfig /path/to/my/kubeconfig.yaml

Follow the CLI output and check for the difference that has been made in files

$ diff ingress.yaml ingress-migrated.yaml

Finally, once the new ingress resources have been reviewed, apply the manifests

$ kubectl apply -f ingress-migrated.yaml --kubeconfig /path/to/my/kubeconfig.yaml

You should make sure to update _all_ Ingress resources to ensure that your certificates continue to be kept up to date.

`Issuer/ClusterIssuer` solvers[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.10-0.11#issuerclusterissuer-solvers)
---------------------------------------------------------------------------------------------------------------------------------

Support for the deprecated `spec.http01` or `spec.dns01` fields in `Issuer` and `ClusterIssuer` have been removed. Any `Issuer` or `ClusterIssuer` objects must be converted to use the equivalent `spec.solvers[].http01` or `spec.solvers[].dns01` syntax. You can read more about the Issuer resource in the [configuration documentation](https://cert-manager.io/docs/configuration/).

Any issuers that haven't been converted will result the `cert-manager` pod being unable to find any solvers at the expected location. This will result in errors like the following: `no configured challenge solvers can be used for this challenge`

#### On this page

*   [Additional annotation changes](https://cert-manager.io/docs/releases/upgrading/upgrading-0.10-0.11#additional-annotation-changes "Additional annotation changes")
*   [`Issuer/ClusterIssuer` solvers](https://cert-manager.io/docs/releases/upgrading/upgrading-0.10-0.11#issuerclusterissuer-solvers "`Issuer/ClusterIssuer` solvers")

© 2026 The cert-manager Authors.

© 2026 The Linux Foundation. All rights reserved.

The Linux Foundation has registered trademarks and uses trademarks.

For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page.](https://www.linuxfoundation.org/trademark-usage/)
