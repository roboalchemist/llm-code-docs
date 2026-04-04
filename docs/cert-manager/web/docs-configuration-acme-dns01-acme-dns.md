# Source: https://cert-manager.io/docs/configuration/acme/dns01/acme-dns/

Title: ACMEDNS

URL Source: https://cert-manager.io/docs/configuration/acme/dns01/acme-dns/

Markdown Content:
ACMEDNS - cert-manager Documentation
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

ACMEDNS
=======

apiVersion: cert-manager.io/v1

kind: Issuer

metadata:

 name: example-issuer

spec:

 acme:

 solvers:

 - dns01:

 acmeDNS:

 host: https://acme.example.com

 accountSecretRef:

 name: acme-dns

 key: acmedns.json

In general, clients to ACMEDNS perform registration on the users behalf and inform them of the CNAME entries they must create. This is not possible in cert-manager, it is a non-interactive system. Registration must be carried out beforehand and the resulting credentials JSON uploaded to the cluster as a `Secret`. In this example, we use `curl` and the API endpoints directly. Information about setting up and configuring ACMEDNS is available on the [ACMEDNS project page](https://github.com/joohoi/acme-dns).

1.   First, register with the ACMEDNS server, in this example, there is one running at `auth.example.com`. The command:

curl -X POST http://auth.example.com/register  
will return a JSON with credentials for your registration:

{  "username": "eabcdb41-d89f-4580-826f-3e62e9755ef2",  "password": "pbAXVjlIOE01xbut7YnAbkhMQIkcwoHO0ek2j4Q0",  "fulldomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com",  "subdomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf",  "allowfrom": [] }  
It is strongly recommended to restrict the update endpoint to the IP range of your pods. This is done at registration time as follows:

curl -X POST http://auth.example.com/register \  -H "Content-Type: application/json" \  --data '{"allowfrom": ["10.244.0.0/16"]}'  
Make sure to update the `allowfrom` field to match your cluster configuration. The JSON will now look like:

{  "username": "eabcdb41-d89f-4580-826f-3e62e9755ef2",  "password": "pbAXVjlIOE01xbut7YnAbkhMQIkcwoHO0ek2j4Q0",  "fulldomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com",  "subdomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf",  "allowfrom": ["10.244.0.0/16"] }  
2.   Save this JSON to a file with the key as your domain. You can specify multiple domains with the same credentials if you like. In our example, the returned credentials can be used to verify ownership of `example.com` and and `example.org`.

{  "example.com": {  "username": "eabcdb41-d89f-4580-826f-3e62e9755ef2",  "password": "pbAXVjlIOE01xbut7YnAbkhMQIkcwoHO0ek2j4Q0",  "fulldomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com",  "subdomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf",  "allowfrom": ["10.244.0.0/16"]  },  "example.org": {  "username": "eabcdb41-d89f-4580-826f-3e62e9755ef2",  "password": "pbAXVjlIOE01xbut7YnAbkhMQIkcwoHO0ek2j4Q0",  "fulldomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com",  "subdomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf",  "allowfrom": ["10.244.0.0/16"]  } }  
3.   Next, update your primary DNS server with the CNAME record that will tell the verifier how to locate the challenge TXT record. This is obtained from the `fulldomain` field in the registration:

_acme-challenge.example.com CNAME d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com _acme-challenge.example.org CNAME d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com  
The "name" of the record always has the _acme-challenge subdomain, and the "value" of the record matches exactly the fulldomain field from registration.

At verification time, the domain name `d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com` will be a TXT record that is set to your validation token. When the verifier queries `_acme-challenge.example.com`, it will be directed to the correct location by this CNAME record. This proves that you control `example.com`

4.   Create a secret from the credentials JSON that was saved in step 2, this secret is referenced in the `accountSecretRef` field of your DNS01 issuer settings. When creating an `Issuer` both this `Issuer` and `Secret` must be in the same namespace. However for a `ClusterIssuer` (which does not have a namespace) the `Secret` must be placed in the same namespace as where the cert-manager pod is running in (in the default setup `cert-manager`).

kubectl create secret generic acme-dns --from-file acmedns.json  

Limitation of the `acme-dns` server[](https://cert-manager.io/docs/configuration/acme/dns01/acme-dns/#limitation-of-the-acme-dns-server)
----------------------------------------------------------------------------------------------------------------------------------------

The [`acme-dns`](https://github.com/joohoi/acme-dns) server has a [known limitation](https://github.com/cert-manager/cert-manager/issues/3610#issuecomment-849792721): when a set of credentials is used with more than 2 domains, cert-manager will fail solving the DNS01 challenges.

Imagining that you have configured the ACMEDNS issuer with a single set of credentials, and that the "subdomain" of this set of credentials is `d420c923-bbd7-4056-ab64-c3ca54c9b3cf`:

kind: Secret

metadata:

 name: auth-example-com

stringData:

 acmedns.json: |

 {

 "example.com": {

 "username": "eabcdb41-d89f-4580-826f-3e62e9755ef2",

 "password": "pbAXVjlIOE01xbut7YnAbkhMQIkcwoHO0ek2j4Q0",

 "fulldomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com",

 "subdomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf",

 "allowfrom": ["10.244.0.0/16"]

 },

 }

---

apiVersion: cert-manager.io/v1

kind: Issuer

metadata:

 name: my-acme-dns

spec:

 acme:

 solvers:

 - dns01:

 acmeDNS:

 accountSecretRef:

 name: auth-example-com

 key: acmedns.json

 host: auth.example.com

and imagine that you want to create a Certificate with three subdomains:

kind: Certificate

spec:

 issuerRef:

 name: issuer-1

 dnsNames:

 - "example.com"

 - "*.example.com"

 - "foo.example.com"

cert-manager will only be able to solve 2 challenges out of 3 in a non deterministic way. This limitation comes from a "feature" mentioned [this acme-dns issue](https://github.com/joohoi/acme-dns/issues/76).

One workaround is to issue one set of acme-dns credentials for each domain that we want to be challenged, keeping in mind that each acme-dns "subdomain" can only accept at most 2 challenged domains. For example, the above secret would become:

kind: Secret

metadata:

 name: auth-example-com

stringData:

 acmedns.json: |

 {

 "example.com": {

 "username": "eabcdb41-d89f-4580-826f-3e62e9755ef2",

 "password": "pbAXVjlIOE01xbut7YnAbkhMQIkcwoHO0ek2j4Q0",

 "fulldomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com",

 "subdomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf",

 "allowfrom": ["10.244.0.0/16"]

 },

 "foo.example.com": {

 "username": "eabcdb41-d89f-4580-826f-3e62e9755ef2",

 "password": "pbAXVjlIOE01xbut7YnAbkhMQIkcwoHO0ek2j4Q0",

 "fulldomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf.auth.example.com",

 "subdomain": "d420c923-bbd7-4056-ab64-c3ca54c9b3cf",

 "allowfrom": ["10.244.0.0/16"]

 }

With this setup, we have:

*   `example.com` and `*.example.com` are registered in the acme-dns "subdomain" `d420c923-bbd7-4056-ab64-c3ca54c9b3cf`.
*   `foo.example.com` is registered in the acme-dns "subdomain" `d420c923-bbd7-4056-ab64-c3ca54c9b3cf`.

Another workaround is to use `--max-concurrent-challenges 2` when running the `cert-manager-controller`. With this setting, acme-dns will only have 2 TXT records in its database at any time, which mitigates the issue.

#### On this page

*   [Limitation of the `acme-dns` server](https://cert-manager.io/docs/configuration/acme/dns01/acme-dns/#limitation-of-the-acme-dns-server "Limitation of the `acme-dns` server")

© 2026 The cert-manager Authors.

© 2026 The Linux Foundation. All rights reserved.

The Linux Foundation has registered trademarks and uses trademarks.

For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page.](https://www.linuxfoundation.org/trademark-usage/)
