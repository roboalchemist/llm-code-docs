# Source: https://docs.api7.ai/enterprise/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/secrets.md

# Source: https://docs.api7.ai/apisix/key-concepts/secrets.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/secrets.md

# Source: https://docs.api7.ai/apisix/key-concepts/secrets.md

# Secrets

In this document, you will learn the basic concept of secrets in APISIX and why you may need them.

Explore additional resources at the end of the document for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

In APISIX, a *secret* object is used to set up integration with an external secret manager, so that APISIX can establish connections and fetch secrets from the secret manager dynamically at runtime.

The following diagram illustrates the concept of a secret object using an example, where [`key-auth`](https://docs.api7.ai/hub/key-auth.md) is enabled for a user, John, and user credentials are stored in a [HashiCorp Vault](https://www.vaultproject.io) server:

![secrets diagram example when using Vault as the external secret manager to store key for key authentication](https://static.api7.ai/uploads/2024/09/12/8XIiyG1q_secrets_cred_updated.svg)

As demonstrated, when APISIX is used in conjunction with an external secret manager, the field for secret is defined as a variable starting with a fixed prefix `$secret://`, appended with the name of the secret manager, APISIX secret object ID, username, and other details.

Specifically, if Vault is used as the secret manager, the APISIX secret object should specify:

* `uri`: location where Vault server is hosted
* `prefix`: path prefix corresponding to a secret engine that Vault should route traffic to
* `token`: token for APISIX to authenticate to Vault and establish connection

These configurations ensure that John can send requests to APISIX and access the back-end service with the correct key. Requests from unauthenticated users are rejected by APISIX.

In addition to Vault, APISIX also supports the integration with AWS and GCP secret managers. For more details on the secret configurations, please refer to the [Admin API](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Secret).

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Getting Started - [Key Authentication](https://docs.api7.ai/apisix/getting-started/key-authentication.md)

* Key Concepts

  <!-- -->

  * [Plugins](https://docs.api7.ai/apisix/key-concepts/plugins.md)
  * [Consumers](https://docs.api7.ai/apisix/key-concepts/consumers.md)
  * [Credentials](https://docs.api7.ai/apisix/key-concepts/credentials.md)
