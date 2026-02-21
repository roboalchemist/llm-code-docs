# Source: https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3

Title: Upgrading from v0.2 to v0.3

URL Source: https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3

Markdown Content:
Upgrading from v0.2 to v0.3 - cert-manager Documentation
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

Upgrading from v0.2 to v0.3
===========================

During the `v0.3` release, a number of breaking changes were made that require you to update either deployment configuration and runtime configuration (e.g. `Certificate`, `Issuer` and `ClusterIssuer` resources).

After reading these instructions, you should then proceed to upgrade cert-manager according to your deployment configuration (e.g. using `helm upgrade` if installing via Helm chart, or `kubectl apply` if installing with raw manifests).

A brief summary:

*   Supporting resources for `ClusterIssuers` (e.g. signing CA certificates, or ACME account private keys) will now be stored in the same namespace as cert-manager, instead of `kube-system` in previous versions (#329, `@munnerz`)

*   Switch to `ConfigMaps` instead of Endpoints for leader election (#327, `@mikebryant`)

*   Removing support for ACMEv1 in favor of ACMEv2 (#309, `@munnerz`)

*   Removing ingress-shim and compiling it into cert-manager itself (#502, `@munnerz`)

*   Change to the default behavior of ingress-shim. It now generates Certificates with the `ingressClass` field set instead of the `ingress` field. This will mean users of ingress controllers that assign a single IP to a single Ingress (e.g. the GCE ingress controller) will no longer work without adding a new annotation to your ingress resource.

Supporting resources for `ClusterIssuers` moving into the cert-manager namespace[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#supporting-resources-for-clusterissuers-moving-into-the-cert-manager-namespace)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the past, the cert-manager controller was hard coded to look for supplemental resources, such as Secrets containing DNS provider credentials, in the `kube-system` namespace.

We now store these resources in the same namespace as the cert-manager pod itself runs within.

When upgrading, you should make sure to move any of these supplemental resources into the cert-manager deployment namespace, or otherwise deploy cert-manager into `kube-system` itself.

You can also change the 'cluster resource namespace' when deploying cert-manager:

With the helm chart: `--set clusterResourceNamespace=kube-system`.

Or if using the static deployment manifests, by adding the `--cluster-resource-namespace` flag to the `args` field of the cert-manager container.

Switch to `ConfigMaps` instead of Endpoints for leader election[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#switch-to-configmaps-instead-of-endpoints-for-leader-election)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

cert-manager-controller performs leader election to allow you to run 'hot standby' replicas of cert-manager.

In the past, we used Endpoint resources to perform this election. The new best practice is to use `ConfigMap` resources in order to reduce API overhead in large clusters.

As such, `v0.3` switches us to use `ConfigMap` resources for leader election.

During the upgrade, you should first scale your cert-manager-controller deployment to 0 to ensure no other replicas of cert-manager are running when the new `v0.3` deployment starts:

$ kubectl scale --namespace <deployment-namespace> --replicas=0 deployment <cert-manager-deployment-name>

Removing support for ACMEv1 in favor of ACMEv2[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#removing-support-for-acmev1-in-favor-of-acmev2)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

The ACME `v2` specification is now in production with Let's Encrypt. In order to support this new spec, which includes support for wildcard certificates, we have removed support for the `v1` protocol altogether.

If you have any ACME Issuer or `ClusterIssuer` resources, you should update the server fields of these to the new ACMEv2 endpoints.

For example, if you have a Let's Encrypt production issuer, you should update the server URL:

apiVersion: certmanager.k8s.io/v1alpha2

kind: Issuer

...

spec:

 acme:

 # server: https://acme-v01.api.letsencrypt.org/directory

 server: https://acme-v02.api.letsencrypt.org/directory # we switch 'v01' to 'v02'

Removing ingress-shim and compiling it into cert-manager itself[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#removing-ingress-shim-and-compiling-it-into-cert-manager-itself)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In `v0.3` we removed the ingress-shim component and instead now compile in its functionality into the main cert-manager binary.

This change also introduces a change to the way you configure default Issuers and `ClusterIssuers` at deployment time.

The deployment documentation has been updated accordingly, but instead of setting `ingressShim.extraArgs={--default-issuer-name=letsencrypt-pod}` there are now dedicated Helm chart fields:

--set ingressShim.defaultIssuerName=letsencrypt-prod \

 --set ingressShim.defaultIssuerKind=ClusterIssuer

Change to the default behavior of ingress-shim[](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#change-to-the-default-behavior-of-ingress-shim)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the past, when using ingress-shim, we set the `ingress` field on the Certificate resource to trigger cert-manager to edit the specified Ingress resource to solve the challenge.

The alternate option is to set the `ingressClass` field, which causes cert-manager to create temporary Ingress resources to solve the challenge. This behavior provides better compatibility with ingress controllers like [`nginx-ingress`](https://github.com/kubernetes/ingress-nginx).

In `v0.3` we have changed the default behavior of ingress-shim to set the `ingressClass` field instead of `ingress`.

This will cause validations for ingress controllers like [`ingress-gce`](https://github.com/kubernetes/ingress-gce) to fail without additional configuration in your Ingress resources annotations.

Add the follow annotation to your Ingress resources if you are using the GCE ingress controller, in addition to the usual ingress-shim annotation(s):

#### On this page

*   [Supporting resources for `ClusterIssuers` moving into the cert-manager namespace](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#supporting-resources-for-clusterissuers-moving-into-the-cert-manager-namespace "Supporting resources for `ClusterIssuers` moving into the cert-manager namespace")
*   [Switch to `ConfigMaps` instead of Endpoints for leader election](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#switch-to-configmaps-instead-of-endpoints-for-leader-election "Switch to `ConfigMaps` instead of Endpoints for leader election")
*   [Removing support for ACMEv1 in favor of ACMEv2](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#removing-support-for-acmev1-in-favor-of-acmev2 "Removing support for ACMEv1 in favor of ACMEv2")
*   [Removing ingress-shim and compiling it into cert-manager itself](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#removing-ingress-shim-and-compiling-it-into-cert-manager-itself "Removing ingress-shim and compiling it into cert-manager itself")
*   [Change to the default behavior of ingress-shim](https://cert-manager.io/docs/releases/upgrading/upgrading-0.2-0.3#change-to-the-default-behavior-of-ingress-shim "Change to the default behavior of ingress-shim")

© 2026 The cert-manager Authors.

© 2026 The Linux Foundation. All rights reserved.

The Linux Foundation has registered trademarks and uses trademarks.

For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page.](https://www.linuxfoundation.org/trademark-usage/)
