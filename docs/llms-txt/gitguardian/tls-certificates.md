# Source: https://docs.gitguardian.com/self-hosting/security/tls-certificates.md

# TLS certificates

> Configure TLS certificates for securing external access to your GitGuardian self-hosted instance.

TLS certificates need to be defined so that the domain on referring to your GitGuardian instance is correctly authenticated and secured. The TLS certificate's Common Name must match the domain set for your GitGuardian instance hostname.

You can use self-signed certificates to test the deployment of the application, be aware that this may lead to integration issues with VCS and is not recommended beyond initial testing.

You need to configure TLS certificates for:

1. **KOTS Admin Console**: used for the KOTS Admin Console user access.
2. **GitGuardian Application**: used for the GitGuardian application user access (sometimes also referred to as _NGINX_).
3. **SAML SSO**: used for Single Sign-On (or SSO) to manage your organizationâs entire membership via a third-party provider.

:::caution
We strongly recommend revoking any certificate being replaced, regardless of its expiration status, to maintain system security.
:::

## KOTS Admin Console

To update the TLS certificate for the KOTS Admin Console, follow these
[instructions](https://docs.replicated.com/enterprise/updating-tls-cert#update-custom-tls-certificates).

:::caution
Adding the `acceptAnonymousUploads` annotation temporarily creates a vulnerability for an attacker to maliciously upload TLS certificates. After TLS certificates have been uploaded, the vulnerability is closed again.
:::

Short version:

```bash
NAMESPACE=default
kubectl --namespace "${NAMESPACE}" annotate secret kotsadm-tls acceptAnonymousUploads=1
kubectl --namespace "${NAMESPACE}" delete pod -l app=kurl-proxy-kotsadm
```

If needed, specify another Kubernetes namespace (default namespace is used if not specified).

After the pod has restarted, direct your browser to `http://<ip>:8800/tls` and go through the upload process in the user interface.

## GitGuardian Application

:::caution
When using self-signed or **[custom CA](./custom-ca)** certificates, ensure to disable SSL verification for the GitHub webhook.
:::

### KOTS-based installation

TLS Certificates are configured in the **TLS certificates** section.

You have the option to use the self signed TLS certificates, or you can provide your own certificates as shown below.
The recommended method is to use an [existing secret](../installation/helm-secrets#existing-secret).

![generic-tls.png](/img/self-hosting/security/generic-tls.png)

For existing clusters, in scenarios where the TLS certificate is managed by your cloud provider's infrastructure, you may reference it directly in your Ingress or Service annotations, depending on your specific cloud provider's requirements.

To upload new certificates, replace the previously uploaded files in the KOTS Admin Console.

After updating the configuration, deploy the new version which includes only the configuration changes:

![Deploying the updated configuration](/img/self-hosting/security/kots-deploy.png)

### Helm-based installation

In Helm installation, the certificate can be set in the `front.ingress.tls` section.

You may provide TLS certificates as existing secret (recommended) or raw certificate.

```yaml
ingress:
  enabled: true
  ingressClassName: 'nginx'
  tls:
    enabled: true
    existingSecret: my-gitguardian-certificate
```

:::caution
When using **[certificate-based authentication](../management/infrastructure-management/cert-based-auth.md)**, the TLS configuration is located in `tls.clientAuth`.
:::

#### Using cert-manager

In Helm installation, you can use [cert-manager](https://cert-manager.io/) to issue the TLS certificates automatically. Cert-manager [must be correctly installed](https://cert-manager.io/docs/installation/) and configured in your cluster, with [an Issuer or a ClusterIssuer resource](https://cert-manager.io/docs/concepts/issuer/).

The certificates are created in a Kubernetes secret, and can be used by either Istio Ingress or a classic Ingress.

The private key is PKCS#1 with 2048 length.

The configuration is done in the local values file with the `tls` section:

```yaml
tls:
  certManager:
    enabled: true
    issuer:
      kind: ClusterIssuer
      name: my-cluster-issuer
    certificatesSecret: my-gitguardian-certificate
```

If using a [classic ingress](../management/infrastructure-management/ingress) with `front.ingress` values, the secret name of the certificate must be specified in `front.ingress.tls.secretName`.

## SAML SSO

This guide outlines the steps to update the SSO X509 certificate used by GitGuardian for authentication with a third-party SSO provider. For more detailed information on configuring SAML SSO, refer to the [Configure SAML SSO](../../platform/enterprise-administration/saml-sso-configuration) page.

If you install GitGuardian using Helm, generate a new SSO certificate, and then edit your Helm values file. For more details, refer to the [Helm Sensitive Information Management](../installation/helm-secrets#existing-secret) page.

### Generate a Self-Signed Certificate

To rotate the SSO certificate, start by generating a new self-signed certificate:

1. Generate a new RSA private key:

Generate a new 2048-bit RSA private key using OpenSSL with the following command:

```bash
openssl genrsa -out gitguardian.key 2048
```

2. Create a Certificate Signing Request (CSR):

Use the generated private key to create a CSR. Replace `<hostname>` with the Fully Qualified Domain Name of your self-hosted instance.

```bash
openssl req -new -subj '/CN=<hostname>' \
  -key gitguardian.key \
  -out gitguardian.csr
```

3. Create a self-signed certificate:

Use the CSR to create a self-signed certificate valid for 365 days (or as required):

```bash
openssl x509 -req -days 365 -in gitguardian.csr \
  -signkey gitguardian.key -out gitguardian.crt
```

### Preparing the KOTS Configuration File

Create or update your `config.yaml` to include the new certificate and key:

```yaml
apiVersion: kots.io/v1beta1
kind: ConfigValues
spec:
  values:
    embedded_certificate:
      values: |
        <content_of_gitguardian.crt>

    embedded_key:
      values: |
        <content_of_gitguardian.key>
```

### Update KOTS Configuration Values

Update the KOTS configuration with the new certificate and private key:

```bash
kubectl kots set config gitguardian --namespace <namespace> \
  --config-file config.yaml \
  --merge
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

### Connect to the KOTS Admin Console

To apply the changes, connect to the KOTS admin console:

```bash
kubectl kots --namespace <namespace> admin-console
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

### Deploy the New Version

After updating the configuration, deploy the new version which includes only the configuration changes:

![Deploying the updated configuration](/img/self-hosting/security/kots-deploy.png)

:::info
If you encounter 403 errors after attempting to "Login with Okta," clearing your web browser's cache may resolve the issue.
:::
