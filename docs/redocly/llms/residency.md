# Source: https://redocly.com/docs/realm/config/access/residency.md

# `residency`


Choose where your application resides when you set it up, then use this configuration setting for local tools to know where to connect to.

This option is needed if your projects have residency outside our main US-based location.
For example, if you choose another geographical location such as Europe or self-host.

Legacy products
Older Redocly products such as Workflows used the setting `region` with the value `eu` or `us`.
For new products, the `residency` configuration setting is used.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| residency | string | URL to the platform where your application resides, e.g. `https://app.cloud.eu.redocly.com` for EU-region deployments.
The default value is the main hosting platform at `https://app.cloud.redocly.com`. |


## Examples

### Use the access object (recommended)

The recommended way to configure `residency` is within the `access` object:


```yaml redocly.yaml
access:
  residency: https://app.cloud.eu.redocly.com
```

### Root-level configuration (deprecated)

**Deprecated:** Root-level `residency` is still supported for backward compatibility but will show deprecation warnings when used alongside the `access` object. Please migrate to the `access` object format.


```yaml redocly.yaml
residency: https://app.cloud.eu.redocly.com
```

## Resources

- **[Access configuration](/docs/realm/config/access)** - Group authentication and access settings together using the `access` object
- **[Remote content](/docs/realm/reunite/project/remote-content)** - Use remote content in your projects for flexible data residency and content management strategies
- **[Develop locally](/docs/realm/get-started/start-local-dev)** - Set up local development environments while maintaining cloud deployment capabilities for data residency compliance