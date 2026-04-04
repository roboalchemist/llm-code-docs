# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/advanced-configuration-for-helm-chart-installation/parameters-for-troubleshooting-and-providing-your-own-certificate-with-helm.md

# Parameters for troubleshooting and providing your own certificate with Helm

To troubleshoot SSL inspection issues, you can set the `tlsRejectUnauthorized` parameter to `disable`.

```
--set tlsRejectUnauthorized=disable
```

To trust your own Certificate Authority, you can pass a certificate file name to the `caCert` parameter. The file must reside within the Helm chart directory.

```
--set caCert=<CERT_NAME>
```

Alternatively, provide the content of the certificate to the `caCertFile` parameter.

```
--set caCertFile="-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"
```

To troubleshoot CA trust issues, you can set the `disableCaCertTrust` parameter to `true`.

```
--set disableCaCertTrust=true
```

If you want your Broker to run as an HTTPS server, you can pass the files to the `httpsCert` and `httpsKey` parameters. The files must reside within the Helm chart directory.

```
--set httpsCert=<CERT_NAME> --set httpsKey=<CERT_KEY>
```

For more information about using your own certificate, see [Backend requests with an internal certificate for Docker](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/advanced-configuration-for-snyk-broker-docker-installation/backend-requests-with-an-internal-certificate-for-docker) and [HTTPS for Broker Client with Docker](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/https-for-broker-client-with-docker).
