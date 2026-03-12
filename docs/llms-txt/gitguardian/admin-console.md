# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/admin-console.md

# KOTS Admin Console

> Access and use the KOTS Admin Console for managing your GitGuardian self-hosted installation.

The KOTS Admin Console is your central hub for managing your GitGuardian instance. Here, you can:

- [Upgrade](./upgrade-kots) your GitGuardian platform to access the latest features and improvements.
- [Back up](./backup) your GitGuardian data for safekeeping.
- Re-sync your [license](../../license-management) to stay compliant and up-to-date.
- Configure cluster-side settings, including:
  - [Scaling](./scaling) your instance to meet demand.
  - Configure [TLS certificates](../../security/tls-certificates).
  - Setting up [Ingress](./ingress.md) for external access.
  - Adjusting [Load Balancer](./load-balancer) settings for optimal distribution.
  - Configuring a [Proxy Server](./proxy-server) for network routing and security.
  - Change the periodicity of the [health checks](../../troubleshoot/health-check#integration-connectivity).

:::info
The KOTS Admin Console is not available with **[Helm Installation](../../installation/installation-existing-cluster-helm)**.
For each management action, an alternative method will be described for Helm's environment.
:::

![KOTS admin](/img/self-hosting/management/infrastructure-management/replicated_kots_admin.png)

## Access

The KOTS Admin Console is available on `http://${your-server-address}:8800`. If needed you can set up an SSH tunnel to access it locally on `http://localhost:8800`:

```
ssh -N -L 8800:localhost:8800 ${your-server-ip}
```

You can access it with the password given during the installation:

- [for embedded cluster](../../installation/installation-embedded-cluster#embedded-cluster)
- [for existing cluster](../../installation/installation-existing-cluster-kots#kots-admin-console)

To reset the KOTS Admin Console password, execute the following command:

```bash
kubectl kots reset-password
```

## TLS Certificates

To update the Certificate for the Console, please refer to
[the TLS documentation](../../security/tls-certificates#kots-admin-console).

## Audit Logs

To retrieve the audit logs for the Console, execute the following command:

```bash
kubectl kots get versions gitguardian --namespace <namespace> -o json
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).
