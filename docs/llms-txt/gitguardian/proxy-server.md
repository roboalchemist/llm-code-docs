# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/proxy-server.md

# HTTP Proxy

> Configure HTTP/HTTPS proxy settings for GitGuardian self-hosted installations that require outbound internet access through a proxy.

GitGuardian allows you to configure an HTTP proxy for outgoing traffic from the application.

This includes traffic to services like Replicated, Docker, messaging integrations, and other external connections. For more details, refer to our [Network Requirements](../../network-requirements#outbound-rules) page.

:::caution

- You must add `127.0.0.1,10.0.0.0/8` to the list of proxy exceptions `NO_PROXY` to permit
  the local and internal cluster traffic through the proxy (replace `10.0.0.0/8` with your internal subnet).
- Verify the proxy FQDNs are resolvable and reachable within your Kubernetes cluster.
- Specifying password in proxy URLs is supported.
- GitGuardian can be deployed with both HTTP and HTTPS proxies. For the HTTPS
  proxy, it may be necessary to add a Certificate Authority (CA) so that the
  proxy's SSL certificate is trusted. This process ensures secure and reliable
  communication between the application and the proxy. For more information,
  please refer to the **[custom CA section](../../security/custom-ca)**.

:::

## Helm-based installation

To configure a **proxy** for [outgoing](../../network-requirements#outbound-rules) HTTP(s) traffic, update your Helm `values` file accordingly. If you are using a custom Certificate Authority (CA), ensure it is configured both under `replicated.privateCASecret` and within the application configuration under `tls.customCa`. For more details, refer to the [Custom CA](../../security/custom-ca#helm-based-installation) documentation.

:::info
From **2025.5.0** version, proxy urls are always stored as Secret.
:::

### Using an existing secret

:::info
The secret must be present before the installation of GitGuardian.
:::

The following example will set the `http_proxy` and `https_proxy` keys of the `gim-proxy` Kubernetes Secret.

```yaml
proxy:
  noProxyHostNames:
    - 127.0.0.1
    - 10.0.0.0/8
  existingSecret: 'gim-proxy'
  existingSecretKeys:
    httpProxyUrl: 'http_proxy'   # Secret should contain: http://username:password@proxy.company.com:8080
    httpsProxyUrl: 'https_proxy' # Secret should contain: https://username:password@proxy.company.com:8080

replicated:
  privateCASecret: # optional if you are using a custom CA
    name: custom-ca-secret-name
    key: 'custom-ca.pem'
  extraEnv:
    - name: NO_PROXY
      valueFrom:
        configMapKeyRef:
          name: gim-config
          key: 'NO_PROXY'
    - name: HTTP_PROXY
      valueFrom:
        secretKeyRef:
          name: 'gim-proxy'
          key: 'http_proxy'        # Example: http://username:password@proxy.company.com:8080
    - name: HTTPS_PROXY
      valueFrom:
        secretKeyRef:
          name: 'gim-proxy'
          key: 'https_proxy'       # Example: https://username:password@proxy.company.com:8080
```

### Using inline values

:::info
When using this method, GitGuardian chart will handle the Kubernetes Secret containing proxy urls for you.
:::

```yaml
proxy:
  httpProxyUrl: 'http://proxy:8080'
  httpsProxyUrl: 'http://proxy:8080'
  noProxyHostNames:
    - 127.0.0.1
    - 10.0.0.0/8
```

## KOTS-based installation

In the [KOTS Admin Console](./admin-console), you can configure the URL(s) for the [outgoing](../../network-requirements#outbound-rules) HTTP(s)
traffic to your proxy server:

![Services and components](/img/self-hosting/management/infrastructure-management/proxy.png)

## Embedded cluster-specific

For embedded cluster installations, additional proxy configuration may be required at the cluster level to handle container image pulls and system-level communications.

:::info
The embedded cluster-level proxy configuration handles system-level traffic (container image pulls, Kubernetes API communications), while the application-level proxy configuration described above handles GitGuardian application traffic (integrations, notifications, etc.). Both may be needed depending on your environment.
:::

For the embedded cluster installation method, you can configure proxy settings during installation.

To configure an HTTP proxy without authentication during installation:

```bash
LICENSE_ID=your_license
curl -f https://replicated.app/embedded/gitguardian/stable -H "Authorization: $LICENSE_ID" -o gitguardian.tgz
tar -xvzf gitguardian.tgz
sudo ./gitguardian install --license license.yaml \
  --http-proxy http://proxy.example.com:8080 \
  --https-proxy http://proxy.example.com:8080
```

When using a proxy that requires authentication, you can include credentials in the proxy URL:

```bash
sudo ./gitguardian install --license license.yaml \
  --http-proxy http://username:password@proxy.example.com:8080 \
  --https-proxy http://username:password@proxy.example.com:8080
```

However, **some Kubernetes components do not support authenticated proxies**. If you encounter issues with container image pulls (such as `ImagePullBackOff` errors), you may need to apply the workaround described below.

**Workaround for Authenticated Proxy Issues**

The embedded cluster creates proxy configuration in `/etc/systemd/system/k0scontroller.service.d/http-proxy.conf`. To work around authentication issues:

1. **Locate the proxy configuration file**:
   ```bash
   sudo cat /etc/systemd/system/k0scontroller.service.d/http-proxy.conf
   ```

2. **Edit the file to prefix environment variables with `CONTAINERD_`**:
   ```bash
   sudo vi /etc/systemd/system/k0scontroller.service.d/http-proxy.conf
   ```

3. **Modify the file to look like this**:
   ```ini
   [Service]
   Environment="CONTAINERD_HTTP_PROXY=http://username:password@proxy.example.com:8080"
   Environment="CONTAINERD_HTTPS_PROXY=http://username:password@proxy.example.com:8080"
   Environment="CONTAINERD_NO_PROXY=localhost,127.0.0.1,.cluster.local,.svc,10.244.0.0/16"
   ```

4. **Restart the k0s controller service**:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart k0scontroller
   ```

5. **Verify proxy configuration** by checking that pods can pull images and external connectivity works:
   ```bash
   sudo ./gitguardian shell
   kubectl get pods -A
   kubectl run test-pod --image=curlimages/curl --rm -it --restart=Never -- curl -I https://www.gitguardian.com
   ```
