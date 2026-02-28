# Harbor docs | Customize the Harbor Token Service

**Source:** https://goharbor.io/docs/2.14.0/install-config/customize-token-service/

Customize the Harbor Token Service

[Harbor version 2.14.0](/docs/2.14.0)

[Harbor Installation and Configuration](/docs/2.14.0/install-config/)

* [Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/)
* [Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/)
* [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/)
* [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
* [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
* [Configure Internal TLS communication between Harbor Component](/docs/2.14.0/install-config/configure-internal-tls/)
* [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
* [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)
* [Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/)
* [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/)
* [Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/)
* [Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/)
* [Harbor Configuration](/docs/2.14.0/install-config/configure-system-settings-cli/)

[Harbor Administration](/docs/2.14.0/administration/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

By default, Harbor uses its own private key and certificate to authenticate with Docker clients. This topic describes how to optionally customize your configuration to use your own key and certificate.

Harbor requires the Docker client to access the Harbor registry with a token. The procedure to generate a token is like
[Distribution Registry v2 authentication](https://github.com/distribution/distribution/blob/main/docs/content/spec/auth/token.md). Firstly, you make a request to the token service for a token. The token is signed by the private key. After that, you make a new request with the token to the Harbor registry, Harbor registry verifies the token with the public key in the root cert bundle. Then Harbor registry authorizes the Docker client to push and pull images.

* If you do not already have a certificate, follow the instructions in
  [Generate a Root Certificate](#gen-cert) to generate a root certificate by using openSSL.
* If you already have a certificate, go to
  [Provide the Certificate to Harbor](#provide-cert).

## Generate a Root Certificate

1. Generate a private key.

   ```
   openssl genrsa -out private_key.pem 4096
   ```
2. Generate a certificate.

   ```
   openssl req -new -x509 -key private_key.pem -out root.crt -days 3650
   ```
3. Enter information to include in your certificate request.

   What you are about to enter is what is called a Distinguished Name or a DN. There are quite a few fields but you can leave some of them blank. For some fields there is a default value. If you enter `.`, the field is left blank.

   * Country Name (2 letter code) [AU]:
   * State or Province Name (full name) [Some-State]:
   * Locality Name (eg, city) []:
   * Organization Name (eg, company) [Internet Widgits Pty Ltd]:
   * Organizational Unit Name (eg, section) []:
   * Common Name (eg, server FQDN or YOUR name) []:
   * Email Address []:

   After you run these commands, the files `private_key.pem` and `root.crt` are created in the current directory.

## Provide the Certificate to Harbor

See
[Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/) or
[Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/) to install or reconfigure Harbor. After you run `./install` or `./prepare`, Harbor generates several configuration files. You need to replace the original private key and certificate with your own key and certificate.

1. Replace the default key and certificate.

   Assuming that the new key and certificate are in `/root/cert`, and `/srv/harbor/data` was specified as `data_volume` run the following commands:

   ```
   cd config/ui
   cp /root/cert/private_key.pem /srv/harbor/data/secret/core/private_key.pem
   cp /root/cert/root.crt /srv/harbor/data/secret/registry/root.crt
   ```
2. Go back to the `make` directory, and start Harbor by using following command:

   ```
   docker compose up -d
   ```
3. Push and pull images to and from Harbor to check that your own certificate works.

On this page

  
  

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/customize-token-service.md)
[Create issue](https://github.com/goharbor/harbor/issues)