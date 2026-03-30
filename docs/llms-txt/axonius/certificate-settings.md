# Source: https://docs.axonius.com/docs/certificate-settings.md

# Managing Certificate and Encryption Settings

The **Certificate and Encryption** settings enable configuring certificate related settings.

**To open the Certificate and Encryption settings**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Privacy and Security**, and select **Certificate and Encryption**.

<Image align="center" alt="Certificates" width="800px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Certificates.png" />

The **Certificate Settings** consists of the following sections:

* [SSL Certificate](#ssl-certificate)
* [Certificate Signing Request (CSR)](#certificate-signing-request-csr)
* [SSL Trust & CA Settings](certificate-settings#ssl-trust--ca-settings)
* [Mutual TLS Settings](#mutual-tls-settings)
* [Encryption Settings](#encryption-settings)

## SSL Certificate

You need to present an SSL certificate when accessing the Axonius GUI.
Axonius accepts X.509 SSL certificates and requests in most formats, including combined certificate files. It is recommended to use a certificate configured to meet or exceed your organization’s security requirements.
The default certificate is the Axonius self-signed SSL certificate.
This section displays the following details about the SSL certificate:

* Issued to
* Alternative Names (if configured)
* Issued by
* SHA1 fingerprint
* Expires on

  ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1151\).png)

## Certificate Signing Request (CSR)

This section displays the Certificate Signing Request (CSR) details:

* If there is no pending CSR request, "None" is displayed.
* If there is a pending CSR, this section lets you perform the following actions:
  * **Download  CSR** - Download the current CSR, which is pending.
  * **Cancel Pending Request** - Cancel the current CSR request.

In order to create a CSR request, in the [**Certificate Actions**](#certificate-actions) menu, click **Generate CSR**.

<Callout icon="📘" theme="info">
  Note

  Certificate Actions are not applicable for Axonius-hosted (SaaS) customers.
</Callout>

The CSR remains in pending state until you sign it with a Certificate Authority (CA) and then upload the signed CSR from the **Import Signed Certificate (CSR)** option in the [**Certificate Actions**](#certificate-actions) menu. A certificate signing request should have a SAN "Alternative Names" value which matches the CN "Domain Name".

![CSR](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CSR.png)

<Callout icon="📘" theme="info">
  Note

  IP addresses are not supported as a Subject Alternative Name (SAN) when using the "Generate CSR" option within the Axonius UI. Customers must generate their own certificate if an IP address is needed as a SAN.
</Callout>

## SSL Trust & CA Settings

* **Use Custom CA certificate** - When enabled, upload Certificate Authority (CA) certificate files used when **Verify SSL** is enabled for an adapter connection. The CA certificates provided here are used in combination with  the [Mozilla CA Certificate List](https://wiki.mozilla.org/CA/Included_Certificates) to verify that the certificate presented by the host defined in the adapter connection is valid.

![CACertificates](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CACertificates.png)

## Mutual TLS Settings

* **Enable mutual TLS** - Mutual TLS is a common security practice that uses client TLS certificates to provide an additional layer of protection, allowing to cryptographically verify the client information. For more details, see [Mutual TLS](/docs/mutual-tls).

![MutualTLSSettings.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MutualTLSSettings.png)

## Encryption Settings

* **Allow legacy SSL cipher suites for adapters** - When selected, allows adapter connectivity to systems that support only legacy ciphers. This option is only available for customer hosted on-premises instances.

<Image align="center" alt="EncryptionSettings-LegacySSLCipher.png" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EncryptionSettings-LegacySSLCipher.png" />

## Certificate Actions

<Callout icon="📘" theme="info">
  Note

  Certificate Actions are not applicable for Axonius-hosted (SaaS) customers.
</Callout>

The **Certificate Actions** menu is located on the top right of this section. When clicking **Certificate Actions**, the following options are available:

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1152\).png)

* **Generate CSR**
  * This option generates a private key that is stored internally in Axonius and then opens the **Create Certificate Signing Request** dialog where you need to specify Certificate Signing Request (CSR) details in order to create the CSR.
  * Once the CSR is created, it goes into pending state and is shown in the [**Certificate Signing Request (CSR)** section](#certificate-signing-request-csr) where it can be downloaded.
  * You can specify the following CSR details:
    * **Domain name** *(required)* - The domain name must match the domain name of the Axonius instance in order for the certificate to be validated. The domain name can contain wildcards.
    * **Alternative Names** *(optional, default: empty)* - Semicolon or comma-separated values of either alternative IP addresses or alternate DNS names. The Domain name is always included as a subject alternative name.
    * **Organization** *(optional, default: Internet Widgits Pty Ltd)* - The organization or company name
    * **Organization Unit** *(optional, default: empty)* - The department
    * **City/Location** *(optional, default: empty)* - The city
    * **State/Province** *(optional, default: Some-State)* - The state
    * **Country** *(optional, default: AU)* - The country **must be exactly two letters** which represent the country. Refer to the list of [Country Codes](https://www.ssl.com/country-codes/).
    * **Email** *(optional, default: empty)* - The email address
  * **Private key characteristics**
    * Private key is generated using:
      * Key exchange algorithm - RSA
      * Key size - 4096
      * Hashing algorithm - SHA256

<Callout icon="📘" theme="info">
  Notes

  * The generated CSR does not contain the expiration date of the certificate. It is mandatory to provide the expiration date of the certificate while signing the CSR with your CA. Note that since July 2020, Chrome and Firefox browsers do not allow certificates with TLS Certificate Lifespan longer than 398 days.

  * The generated CSR contains constraints. The signing CA should copy these constraints to the signed CSR. Not copying these constraints may result in the browser not validating the certificate.
    The following constraints are used:

    * *keyUsage (Digital Signature, Non Repudiation, Key Encipherment)*

    * *subjectAltName*  - contains the domain name (Chrome must have it in order to validate the certificate)

    * *basicConstraints - CA:FALSE*
</Callout>

![CreateCSR](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateCSR.png)

* **Import Certificate and Private Key**
  * This option enables you to import a certificate public key and private key (with an optional passphrase) in order to replace the existing SSL certificate that is presented when accessing the Axonius GUI.
  * The imported certificate details are displayed in the [**SSL Certificate** section](#ssl-certificate-details).
  * The **Import Certificate and Private Key** dialog requires you to specify the following fields:
    * **Domain name** *(required)* - The hostname of the certificate. This must match the value defined in the certificates ***Common Name*** or ***Subject Alternative Name***.
    * **Certificate file** *(required)* - Upload the public certificate (DER, PFX, or PEM format)
    * **Private key file** *(required)* - Upload the private key certificate (PEM format)
    * **CA Chain file** *(optional)* - Upload the CA chain file in (DER, PFX or PEM format)
      Axonius automatically concatenates them and creates a valid certificate file for the Axonius system to use and serve to clients.
* **Private key passphrase** *(optional, default: empty)* - The password for  the **Private key file**, if it is password-protected.

![ImportCertificateAndPrivateKey](https://raw.githubusercontent.com/Axonius/ax-docs-pub/8aa28cbd032997982d1ddcd4a405f0ba71173a7b/Images/ImportCertificateAndPrivateKey.png)

* **Import Signed Certificate (CSR)**
  * This option is enabled only when you have a pending Certificate Signing Request (CSR).
  * You should only import the Signed CSR after you have signed the CSR with your Certificate Authority(CA).
  * This option opens the **Installed Signed Certificate** dialog which lets you upload the signed CSR.
  * The new certificate details are replaced and displayed in the [**SSL Certificate** section](#ssl-certificate-details).

![InstallSignedCertificate](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/InstallSignedCertificate.png)

* **Restore to System Default**
  * This option restores the Axonius default self-signed SSL certificate, which is presented when accessing the Axonius GUI. The certificate details are displayed in the [**SSL Certificate** section](#ssl-certificate).

Once you click **Restore to Default**, the Certificate settings in the webserver are 'reloaded' without any downtime.