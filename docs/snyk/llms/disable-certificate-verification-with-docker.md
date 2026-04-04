# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/advanced-configuration-for-snyk-broker-docker-installation/disable-certificate-verification-with-docker.md

# Disable certificate verification with Docker

To disable certificate verification, for example, in the case of self-signed certificates, add the following to the docker run command:

```
-e NODE_TLS_REJECT_UNAUTHORIZED=0
```
