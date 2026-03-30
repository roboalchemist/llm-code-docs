# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/backup.md

# Backup & Restore

> Back up and restore your GitGuardian self-hosted instance, including database and encryption key management.

:::caution
GitGuardian encrypts all sensitive information in the database using a data encryption key (also known as the Django Secret Key). In the event of a disaster, this key will be essential to restore your data.

Regardless of the installation method (KOTS or Helm), **ensure the encryption key is securely stored** and accessible.

Use the following command to display the key:

```shell
kubectl get secrets gim-secrets --namespace=<namespace> -o jsonpath='{.data.DJANGO_SECRET_KEY}' | base64 -d
```
:::

## Backup

To fully back up the GitGuardian application, you need to:

- Back up the PostgreSQL database (â ï¸ and the **data encryption key**).
- Back up the KOTS config (for KOTS-based installations existing cluster).
- Back up the Helm values file (for Helm-based installations existing cluster).

We strongly recommend using externally managed databases and data stores, along with a robust strategy for snapshots and backups. An embedded cluster installation with an embedded PostgreSQL database is not recommended for production deployments and is intended for PoC/testing purposes only. For more information, see the [Choose your installation method](../../installation/choose-embedded-existing) page.

### Helm-based Installation

Ensure you back up the values file you created during the [installation](../../installation/installation-existing-cluster-helm#customize-the-local-values-file).

### KOTS-based Installation

To backup the KOTS config files, use:

```bash
kubectl kots get config \
    --namespace gitguardian \
    --decrypt \
    --appslug gitguardian > config.yaml
```

:::caution
The backup configuration contains secrets. Ensure it is stored securely and access is strictly controlled.
:::

If needed, specify the Kubernetes namespace with `--namespace` (the default namespace is used if not specified).

KOTS offers a mechanism to simplify backups of your GitGuardian application. For detailed information on backup and restore, including Velero Version Compatibility, please refer to the [Replicated website](https://docs.replicated.com/enterprise/snapshots-understanding#velero-version-compatibility).

## Restore

Restoring the GitGuardian instance depends on the situation. Do you just want to go back in time to a previous database backup? Are you looking to roll back to a previous version of the application? Did you lose your database and/or Kubernetes cluster and need to restore the application and database from scratch?

### Database restore only

To restore the PostgreSQL database, follow these steps:

1. Stop the application.
2. Flush the Redis cache.
3. Restore the PostgreSQL database.
4. Restart the application.

### Application version rollback

:::danger
Do not roll back or downgrade without consulting our **[support team](mailto:support@gitguardian.com)** first. Certain scenarios may require restoring the database from a pre-upgrade backup due to the complexity of reversing some database migrations.
:::

### Disaster Recovery

In the event that you need to reinstall the application from scratch for disaster recovery, follow the appropriate installation procedure based on your setup:

- [KOTS existing cluster](../../installation/installation-existing-cluster-kots)
- [KOTS embedded cluster](../../installation/installation-embedded-cluster)
- [Helm](../../installation/installation-existing-cluster-helm)

#### Helm-Based Installation

1. Use your previously backed-up values file.
2. Ensure you specify the encryption key by either:
   - Using the inline parameter `miscEncryption.djangoSecretKey`, or
   - Referencing an existing secret with `miscEncryption.existingSecret`.

#### KOTS-Based Installation

1. Follow the installation procedure for your KOTS setup.
2. Configure the installation with the essential settings.
3. Once the installation is complete, restore the KOTS configuration files using the following command:
   ```bash
   kubectl kots install gitguardian \
       --namespace gitguardian \
       --use-minimal-rbac \
       --shared-password <set_new_password> \
       --license-file license.yaml \
       --config-values config.yaml
   ```
   - Replace `<set_new_password>` with your desired password (used to access [KOTS Admin Console](./admin-console)).
   - Adjust the `namespace` if necessary.
   - Ensure you use the `config.yaml` file from your backup.
   - This command must be executed on a non-existent or empty namespace (i.e., no prior KOTS installation).
4. In the [KOTS Admin Console](./admin-console), verify that the configuration is correct and deploy the application.
   ![KOTS Admin Config](/img/self-hosting/management/infrastructure-management/replicated_kots_admin_config.png)
