# Source: https://www.aptible.com/docs/how-to-guides/app-guides/establish-client-certificiate-auth.md

# How to establish client certificate authentication

> Client certificate authentication, also known as two-way SSL authentication, is a form of mutual Transport Layer Security(TLS) authentication that involves both the server and the client in the authentication process. Users and the third party they are working with need to establish, own, and manage this type of authentication.

## Standard TLS Authentication v. Mutual TLS Authentication

The standard TLS authentication process works as follows:

1. The client sends a request to the server.

2. The server presents its SSL certificate to the client.

3. The client validates the server's SSL certificate with the certificate authority that issued the server's certificate. If the certificate is valid, the client generates a random encryption key, encrypts it with the server's public key, and then sends it to the server.

4. The server decrypts the encryption key using its private key. The server and client now share a secret encryption key and can communicate securely.

Mutual TLS authentication includes additional steps:

1. The server will request the client's certificate.

2. The client sends its certificate to the server.

3. The server validates the client's certificate with the certificate authority that issued it. If the certificate is valid, the server can trust that the client is who it claims to be.

## Generating a Client Certificate

Client certificate authentication is more secure than using an API key or basic authentication because it verifies the identity of both parties involved in the communication and provides a secure method of communication. However, setting up and managing client certificate authentication is also more complex because certificates must be generated, distributed, and validated for each client. A client certificate is typically a digital certificate used to authenticate requests to a remote server.

For example, if you are working with a third-party API, their server can ensure that only trusted clients can access their API by requiring client certificates. The client in this example would be your application sending the API request. We recommend that you verify accepted Certificate Authorities with your third-party API provider and then generate a client certificate using these steps:

1. Generate a private key. This must be securely stored and should never be exposed or transmitted. It's used to generate the Certificate Signing Request (CSR) and to decrypt incoming messages.

2. Use the private key to generate a Certificate Signing Request (CSR). The CSR includes details like your organization's name, domain name, locality, and country.

3. Submit this CSR to a trusted Certificate Authority (CA). The CA verifies the information in the CSR to ensure that it's accurate. After verification, the CA will issue a client certificate, which is then sent back to you.

4. Configure your application or client to use both the private key and the client certificate when making requests to the third-party service.

> 📘 Certificates are only valid for a certain time (like one or two years), after which they need to be renewed. Repeat the process above to get a new certificate when the old one expires.

## Commercial Certificate Authorities (CAs)

Popular CAs that issue client certificates for use in client certificate authentication:

1. DigiCert: one of the most popular providers of SSL/TLS certificates and can also issue client certificates.

2. GlobalSign: offers PersonalSign certificates that can be used for client authentication.

3. Sectigo (formerly Comodo): provides several client certificates, including the Sectigo Personal Authentication Certificate.

4. Entrust Datacard: offers various certificate services, including client certificates.

5. GoDaddy: known primarily for its domain registration services but also offers SSL certificates, including client certificates.
