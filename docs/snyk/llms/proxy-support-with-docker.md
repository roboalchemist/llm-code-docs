# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/advanced-configuration-for-snyk-broker-docker-installation/proxy-support-with-docker.md

# Proxy support with Docker

For proxy configuration, see [Configure Docker to use a proxy server](https://docs.docker.com/network/proxy/).

```
 -e HTTP_PROXY=http://my.proxy.address:8080
 -e HTTPS_PROXY=http://my.proxy.address:8080
 -e NO_PROXY=*.test.example.com,.example2.com,127.0.0.0/8
```

If your proxy requires username and password authentication, provide the following additional environment variable:

```
-e PROXY_AUTH=userID:userPass
```
