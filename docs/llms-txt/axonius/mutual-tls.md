# Source: https://docs.axonius.com/docs/mutual-tls.md

# Mutual TLS

Mutual TLS is a common security practice that uses client TLS certificates to provide an additional layer of protection, allowing to cryptographically verify the client information.

In most cases, when you try to access a secured HTTPS/TLS endpoint, you experience only the client-side check of the server certificate. The purpose of this check is to ensure that no fraudulent activity is involved, and the data transfer between the client and server is encrypted. In Mutual TLS, the client certificate is specified as well, so the server can accept connections only for clients with certificates registered with the server certificate authority, or provide additional security checks based on the information stored in the client certificate.

In Axonius, mutual TLS restricts clients' access to the Axonius GUI and Axonius API if they do not have verified client SSL certificates. Once enabled, clients trying to access the Axonius GUI or trying to interact with the Axonius API are blocked.

<Callout icon="📘" theme="info">
  Note

  When you configure LDAP Login Settings as 'Smartcard', Mutual TLS is not available.
</Callout>

**To enable mutual TLS in Axonius:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.

2. In the Categories/Subcategories pane of the System Settings page, expand **Privacy and Security**, and select **Certificate**.

3. Under the **Mutual TLS Settings** section, toggle on **Enable mutual TLS**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MutualTLS.png)

4. From the **CA certificate (PEM format)** field, click **Upload File** and upload a PEM format CA certificate that will be used for the client access verification.

<Callout icon="📘" theme="info">
  Note

  Before uploading the file, it is recommended to import your personal certificate and install it in your web browser.
</Callout>

5. Click **Save**.

   Once successfully saved, when any request is sent to access the Axonius GUI or Axonius API, Axonius requests an optional client certificate during the TLS handshake. However, Axonius does not check the validity of the client certificate, meaning that also clients that do not possess the verified certificate can access the Axonius GUI/API.
6. Close and reopen your web browser, and log into Axonius. Your web browser might ask you to pick a client certificate. Note that at this point Axonius does not check the validity of your client certificate.
7. Reenter the **Certificates** page (steps 1 and 2 above).
8. To complete the process of mandatory mutual TLS, under the **Mutual TLS Settings** section, select the **Enforce client certificate validation** checkbox.
9. Click **Save**.
   Axonius validates your client certificate against the CA you uploaded.
   * If this validation passes, Mutual TLS becomes mandatory and access to Axonius is not possible without a matching client certificate.
   * If this validation fails, Mutual TLS remains optional. The validation might fail due to the following reasons:

| Error Reason        | Error Message                                                                                               |
| ------------------- | ----------------------------------------------------------------------------------------------------------- |
| Missing certificate | Client certificate not found in request. Please make sure your client uses a certificate to access Axonius. |
| Invalid certificate | Current client certificate can not be validated by the uploaded CA.                                         |