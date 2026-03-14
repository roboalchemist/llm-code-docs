# Source: https://docs.gitguardian.com/self-hosting/security/recommendations.md

# Security recommendations and information

> Security best practices and hardening recommendations for GitGuardian self-hosted deployments.

## Common Vulnerabilities and Exposures

Chainguard stands as a leader in security technology, providing robust defenses against Common Vulnerabilities and Exposures (CVEs). In our commitment to heightened security, we utilize Chainguard-approved Base-OS images, which are specifically hardened, for constructing our GitGuardian self-hosted images. This strategic choice markedly diminishes the likelihood of security vulnerabilities that could affect our users.

At GitGuardian, we recognize the critical importance of robust security measures in protecting against Common Vulnerabilities and Exposures (CVEs). Our partnership with Chainguard, a leader in security technology, plays a pivotal role in this endeavor. By using Chainguard-approved, hardened Base-OS images for the construction of our GitGuardian self-hosted images, we significantly enhance our defense mechanisms against potential vulnerabilities.

**Key Benefits:**

- **Zero CVE Goal in Container Images:** Our adoption of Chainguard-approved, hardened Base-OS images is a strategic effort towards achieving zero CVEs in our frontend and backend container images, thereby greatly strengthening their security against various vulnerabilities.
- **FIPS 140-3 Approved Cryptographic Modules (Helm installations only):** The integration with Chainguard can incorporate Federal Information Processing Standards (FIPS 140-3) approved cryptographic modules into GitGuardian, ensuring top-tier encryption of sensitive data, both at rest and in transit. **FIPS 140-3 modules are optional and available only for Helm-based installations.** Learn more about [Chainguard's FIPS validation process](https://www.chainguard.dev/unchained/forging-ahead-in-federal-compliance-chainguards-fips-140-3-and-186-5-milestones).
- **Adherence to Compliance and Security Benchmarks:** With this integration, GitGuardian aligns with the highest standards in compliance and security benchmarks, setting a new standard in the industry.

For detailed information about Chainguard's FIPS warranties and certified cryptographic modules, see [Chainguard's FIPS Commitment](https://www.chainguard.dev/legal/fips-commitment).

**Runtime Image Configuration:**

Our runtime image utilizes the Python image, with the option to use a FIPS-enabled variant for Helm installations. The following additional packages are included: `src-fingerprint`, `libxml2`, `libxslt`, `xmlsec`, `xmlsec-openssl`, and `git`.

**Enabling FIPS on Helm Installations:**

To activate FIPS-compliant cryptographic modules in your Helm installation, set the following in your `values.yaml` file:

```yaml
global:
  fips:
    enabled: true
```

**For Airgap Installations:**

For airgap environments, see the [Airgap Installation Guide](../installation/airgap-installation-existing-cluster-helm#fips-compliance-for-airgap-installations) for FIPS-specific instructions.

When FIPS 140-3 is enabled, the installation will use FIPS compliant versions of the application images with specialized cryptographic modules that meet Federal Information Processing Standards, ensuring top-tier encryption of sensitive data, both at rest and in transit.

[KOTS admin and](https://docs.replicated.com/release-notes/rn-app-manager#improvements-1-104-3) [Replicated SDK](https://docs.replicated.com/release-notes/rn-replicated-sdk#improvements-0-0-1-beta-2) utilize a distroless base image from Chainguard.

## Cosign for image signing

GitGuardian has enhanced the security of our images through the implementation of Cosign for image signing, aligning with [SLSA 2](https://slsa.dev/get-started#slsa-2) standards. This ensures all images are secure from their creation to deployment. All GitGuardian images can be verified following the method described below, except for the Replicated SDK which uses a different verification process (see [Verify SDK Image Integrity](https://docs.replicated.com/vendor/replicated-sdk-slsa-validating#verify-sdk-image-integrity)).

:::info
You can enhance your Kubernetes security by using the Sigstore Policy Controller. For more details, please visit the [Sigstore Policy Controller documentation](https://docs.sigstore.dev/policy-controller/overview/).
:::

**Before You Start**: Download Cosign for image verification: [Download Cosign](https://docs.sigstore.dev/system_config/installation/)

**Verification Steps:**

1. Save the provided public key into a file named `gg_cosign.pub`.

```sh
echo "-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEnVzZQr8D9OgkgZcf9z0v67yrd2pg
+yQtJur1OgetAwij8T8g8VH+IegI6Y+1E3ZEqMast934R35UCzOiiyIadQ==
-----END PUBLIC KEY-----" > gg_cosign.pub
```

2. Retrieve your License ID from your license file, where it's labeled as `licenseID`. Use this ID to authenticate with the GitGuardian image repository by executing the command below. Replace `<your_licenseID>` with your actual License ID.

```sh
LICENSE_ID="<your_licenseID>";
echo "{\"auths\": {\"proxy.replicated.com\": {\"auth\": \"$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64)\"}, \"registry.replicated.com\": {\"auth\": \"$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64)\"}}}" > ~/.docker/config.json
```

3. Execute the following command, replacing `<IMAGE>:<TAG>` with the image's name and tag.

```sh
cosign verify --key gg_cosign.pub <IMAGE>:<TAG>
```

This command verifies the image against the signatures stored with it, using the provided public key.

For the complete list of images you can verify, see the [Upload GitGuardian Images](../installation/airgap-installation-existing-cluster-helm#upload-gitguardian-images) section in the airgap installation guide.

Example:

```sh
cosign verify --key gg_cosign.pub proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-app-chainguard:2025.6.0 | jq .

Verification for proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-app-chainguard:2025.6.0 --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - Existence of the claims in the transparency log was verified offline
  - The signatures were verified against the specified public key
```

Expected output:

```yaml
[
  {
    'critical':
      {
        'identity':
          {
            'docker-reference': 'docker.io/gitguardian/prm-app-chainguard',
          },
        'image': { 'docker-manifest-digest': 'sha256:b842813ffb597a67c...' },
        'type': 'cosign container image signature',
      },
    'optional':
      {
        'Bundle':
          {
            'SignedEntryTimestamp': '',
            'Payload':
              {
                'body': '',
                'integratedTime': 1709632488,
                'logIndex': 75773529,
                'logID': 'c0d23d6ad406...',
              },
          },
      },
  },
]
```

## TLS certificate

To safeguard sensitive information, such as secrets and source code, the application mandates HTTPS access.

We advise using a valid certificate that corresponds with your chosen Fully Qualified Domain Name (FQDN), like `dashboard.gitguardian.mycorp.local`.

**A TLS certificate is required to start the installation.**

For configuring the TLS certificate, see the [following section](./tls-certificates).

By default, we employ a robust cipher suite supporting only TLS 1.2 and TLS 1.3, ensuring compatibility with modern browsers. For any issues, please contact support@gitguardian.com.

The default protocols and ciphers are compliant with modern browsers. **If you enable the FIPS 140-3 option, the following protocols and ciphers are FIPS 140-3 compliant:**

- **Protocols:** `TLS 1.2` / `TLS 1.3`
- **Ciphers:**
  - **TLS 1.3:**
    - `TLS_AES_256_GCM_SHA384`
  - **TLS 1.2:**
    - `ECDHE-ECDSA-AES256-GCM-SHA384`
    - `ECDHE-RSA-AES256-GCM-SHA384`

## Considerations for Self-Signed Certificates

Using a self-signed certificate requires additional SSL validation handling for GitLab or GitHub web hooks. SSL verification is enabled by default, and disabling it is necessary for integrating with GitLab or GitHub.

## Encryption and Access Control

Considering the database will hold sensitive data (like source code and leaks), we strongly recommend encrypting the file system. Additionally, access to the host running the application should be limited to essential personnel (e.g., host and application deployment managers).

## Signup restrictions

By default, joining the GitGuardian workspace requires a sign-up via SSO or an invitation link.

Disabling signup restrictions means **anyone** within the instance network can join your workspace and potentially access secrets. Should you opt to disable these restrictions, ensure your GitGuardian instance is only accessible within a restricted network, not from the Internet.
