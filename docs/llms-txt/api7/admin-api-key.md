# Source: https://docs.api7.ai/apisix/production/security/admin-api-key.md

# Admin API Key

Admin API keys are used to control access to the APISIX Admin API endpoints, allowing only authorized users to manage and administer APISIX resources via the Admin API.

## Key Requirement and Permissions[â](#key-requirement-and-permissions "Direct link to Key Requirement and Permissions")

It is strongly recommended that you switch on the mandatory requirement of Admin API keys in production and configure a set of complex keys to harden your APISIX instances.

The example [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) documents the following details, where Admin API key is required by default and set to an empty string:

config.yaml.example

```
deployment:
  admin:
    admin_key_required: true
    admin_key:
      -
        name: admin
        key: ''
        role: admin    # read and write access
      -
        name: viewer
        key: 4054f7cf07e344346cd3f287985e76a2
        role: viewer   # read-only access
```

If you do not configure a custom Admin API key, APISIX will automatically generate a key at runtime.

To customize these configurations for your deployment, add the custom configurations to the `config.yaml` [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) and [reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

## Other Admin API Security Options[â](#other-admin-api-security-options "Direct link to Other Admin API Security Options")

In addition to setting the Admin API keys, you can also customize other configurations to further secure the Admin API, such as:

* Admin API CORS
* [Admin API Access IP whitelist](https://docs.api7.ai/apisix/production/security/ip-restriction.md#restrict-admin-api-access-by-ip)
* [Admin API mTLS](https://docs.api7.ai/apisix/production/security/mtls/configure-mtls-between-client-and-admin-api.md)

For a complete list of configuration options, see [`config.yaml.example`](https://github.com/apache/apisix/blob/master/conf/config.yaml.example).
