# Source: https://docs.airbyte.com/platform/deploying-airbyte/integrations/database.md

# Source: https://docs.airbyte.com/platform/2.0/deploying-airbyte/integrations/database.md

# Source: https://docs.airbyte.com/platform/1.8/deploying-airbyte/integrations/database.md

# Source: https://docs.airbyte.com/platform/1.7/deploying-airbyte/integrations/database.md

# Source: https://docs.airbyte.com/platform/1.6/deploying-airbyte/integrations/database.md

# External Database

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

For production deployments, we recommend using a dedicated database instance for better reliability, and backups (such as AWS RDS or GCP Cloud SQL) instead of the default internal Postgres database (`airbyte/db`) that Airbyte spins up within the Kubernetes cluster.

The following instructions assume that you've already configured a Postgres instance:

## Secrets[​](#secrets "Direct link to Secrets")

```
apiVersion: v1
kind: Secret
metadata:
  name: airbyte-config-secrets
type: Opaque
stringData:
  # Database Secrets
  database-user: ## e.g. airbyte
  database-password: ## e.g. password
```

## Values[​](#values "Direct link to Values")

Add external database details to your `values.yaml` file. This disables the default internal Postgres database (`airbyte/db`), and configures your external Postgres database. You can override all of the values below by setting them in the airbyte-config-secrets or set them directly in the `values.yaml` file. **The database password is a special case in that it must be set in the [airbyte-config-secrets](#secrets).**

```
postgresql:
  enabled: false

global:
  database:
    type: external

    # -- Secret name where database credentials are stored
    secretName: "" # e.g. "airbyte-config-secrets"

    # -- The database host
    host: ""

    # -- The database port
    port: ""

    # -- The database name
    database: ""

    # -- The key within `secretName` where database user is stored
    userSecretKey: "" # e.g. "database-user"

    # -- The key within `secretName` where password is stored
    passwordSecretKey: "" # e.g."database-password"
```
