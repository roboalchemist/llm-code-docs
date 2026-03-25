# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/custom-ca-certificates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Custom CA Certificates

> Add custom or self-signed CA certificates to your env zero self-hosted Kubernetes agent

If you use custom CA certificates in your deployment process, such as self-signed certificates, you can easily add them to env zero's [Self-Hosted Agent](/guides/admin-guide/self-hosted-kubernetes-agent).

To do so, you can attach certificates using the `customCertificates` helm value that can be to the [configuration](/guides/admin-guide/self-hosted-kubernetes-agent/#customoptional-configuration). Its value should be a list of Kubernetes Secret names. Each secret may contain one or more custom certificate files.

For instance, you can add your CA file using the following command in your cluster:

```shell  theme={null}
kubectl create secret generic my-self-signed-cert --from-file=my-self-signed-cert.cer --namespace=env0-agent
```

Then, in your Helm values file, add the related config:

```yaml yaml theme={null}
"customCertificates":
  - "my-self-signed-cert"
```

Now you can proceed with the agent [upgrade](/guides/admin-guide/self-hosted-kubernetes-agent/#upgrade)/[installation](/guides/admin-guide/self-hosted-kubernetes-agent/#installation).

<Info>
  **Node.js scripts**

  During env zero deployment some customers may want to use Node.js scripts.

  <Info>
    To make sure your script using the custom certificates, please add the `NODE_EXTRA_CA_CERTS` environment variable with the value of `/etc/ssl/certs/ca-certificates.crt`. That file contains all the certificates in our agent's pod.
  </Info>
</Info>

<Warning>
  Ignore CA Certs

  Set `gitSslNoVerify` to `true` in your helm values to ignore CA certs.
</Warning>

Built with [Mintlify](https://mintlify.com).
