# Source: https://docs.gitguardian.com/self-hosting/security/database-security.md

# Database Security

> Configure database-level security for GitGuardian self-hosted, including encryption at rest and connection security.

Maintaining the security of your database systems is paramount in protecting sensitive information and ensuring the integrity of your data. This guide provides comprehensive steps for updating the security settings of PostgreSQL and Redis databases, including password changes, encryption key rotation, and client certificate updates. Follow these procedures carefully to enhance the security posture of your databases.

## Update PostgreSQL Password

Ensure the security of your PostgreSQL database by setting a new password.

:::caution
Ensure you back up your database before starting this procedure, which will incur minimal application downtimeâfrom scaling down to full redeployment.
:::

1. Scale down the Dashboard, Public API and Webhook receivers.

```bash
kubectl --namespace <namespace> get deploy -o name \
   | grep webapp \
   | xargs kubectl --namespace <namespace> scale deploy/% --replicas 0
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

2. Confirm all asynchronous and scheduled tasks have finished.

```bash
kubectl exec --namespace <namespace> -t deploy/worker-scanners \
    -- celery -A ward_run_app inspect active
```

The output should indicate `- empty -` for each pod, signaling completion.

```bash
app@(...):/app$ celery -A ward_run_app inspect active
(...)
->  workers@worker-worker-(...): OK
    - empty -
->  long_tasks@worker-long-tasks-(...): OK
    - empty -
->  scanner@worker-scanners-(...): OK
    - empty -
->  email@worker-email-(...): OK
    - empty -
->  email@worker-email-(...): OK
    - empty -
->  scanner@worker-scanners-(...): OK
    - empty -
->  long_tasks@worker-long-tasks-(...): OK
    - empty -
->  workers@worker-worker-(...): OK
    - empty -
```

3. Scale down all workers and scheduler pods.

```bash
kubectl --namespace <namespace> get deploy -o name \
   | grep worker \
   | xargs kubectl --namespace <namespace> scale deploy/% --replicas 0
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

4. Configure your environment, update the namespace `gg_namespace` as needed.

```bash
gg_namespace=<namespace>
pg_host=$(kubectl -n $gg_namespace get cm gim-config -o jsonpath="{.data.POSTGRES_HOST}")
pg_port=$(kubectl -n $gg_namespace get cm gim-config -o jsonpath="{.data.POSTGRES_PORT}")
pg_user=$(kubectl -n $gg_namespace get cm gim-config -o jsonpath="{.data.POSTGRES_USER}")
pg_passwd=$(kubectl -n $gg_namespace get secret gim-secrets -o jsonpath="{.data.POSTGRES_PASSWORD}" | base64 -d)
pg_db=$(kubectl -n $gg_namespace get cm gim-config -o jsonpath="{.data.POSTGRES_DB}")
```

5. With your environment set, you're ready to launch a PostgreSQL shell.

```bash
echo "Connection to $pg_user@$pg_host:$pg_port/$pg_db"
kubectl -n $gg_namespace run postgresql-client --rm -it \
  --restart='Never' --image docker.io/bitnamilegacy/postgresql:13 \
  --env="PGPASSWORD=$pg_passwd" --command \
  -- psql --host $pg_host -U $pg_user -d $pg_db -p $pg_port
```

6. Inside the shell, update your password.

```sql
ALTER USER <postgres user> WITH PASSWORD '<new password>';
```

Replace `<postgres user>` with your username and `<new password>` with the desired password.

### KOTS-Based Installation

1. Navigate to the âConfigâ tab in the [KOTS Admin Console](../management/infrastructure-management/admin-console.md) and update the PostgreSQL password.
2. Save the configuration.
3. Deploy the updated configuration.

![Deploying the updated configuration](/img/self-hosting/security/kots-deploy.png)

### Helm-Based Installation

:::caution
Do not directly modify values within the Kubernetes secret `gim-secrets`, as such changes will be overridden by subsequent Helm upgrades.
:::

1. For secrets management, ensure updates are made in the appropriate location based on your setup. Look at your values file under the `postgresql` section to find how the password is stored. For further details, see [Helm sensitive information management](../installation/helm-secrets).

- If you use a secret manager, change the required values in it.
- If you use a secret inside the namespace, patch it:

```bash
kubectl patch secret -n $gg_namespace gim-secrets \
   -p "{\"data\":{\"POSTGRES_PASSWORD\":\"$(echo '<new_password>' | base64)\"}}"
```

2. Once the new password is set you can redeploy the application:

`helm upgrade <release-name> -n <namespace> -f local-values.yaml`

Replace `<release-name>` with the release name you specified during the initial installation (use `helm ls` to find it). If needed, specify the Kubernetes namespace with `-n` (default namespace is used if not specified). Stick to the same version using the `--version` flag.

## Update Redis main Password (external cluster)

The process for updating the Redis main password varies by installation method:

- **Standard Redis Installation**: either create a new instance with identical settings or directly update the password in the existing instance's configuration file.
- **AWS Elasticache**: use the AWS CLI or API to follow the [Rotate AUTH token](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html#auth-modifyng-token) guidelines.
- **GCP Memorystore**: modify the AUTH string by [toggling AUTH from off to on](https://cloud.google.com/memorystore/docs/redis/about-redis-auth).
- **Bitnami Helm chart**: in the Redis Helm Chart value file, change the value `global.redis.password` with the new password. Apply changes with `helm upgrade <redis-release> -f <redis-values.yaml>`.

### KOTS-Based Installation

1. Navigate to the âConfigâ tab in the [KOTS Admin Console](../management/infrastructure-management/admin-console.md) and update the PostgreSQL password.
2. Save the configuration.
3. Deploy the updated configuration.

![Deploying the updated configuration](/img/self-hosting/security/kots-deploy.png)

### Helm-Based Installation

:::caution
Do not directly modify values within the Kubernetes secret `gim-secrets`, as such changes will be overridden by subsequent Helm upgrades.
:::

1. For secrets management, ensure updates are made in the appropriate location based on your setup. Look at your values file under the `redis.main` section to find how the password is stored. For further details, see [Helm sensitive information management](../installation/helm-secrets).

- If you use a secret manager, change the required values in it.
- If you use a secret inside the namespace, patch it:

```bash
kubectl patch secret -n <namespace> <secret_name> \
  -p "{\"data\":{\"REDIS_URL\":\"<redis|rediss>://:$(echo -n '<new_password>' | base64)@<redis_host>:<redis_port>\"}}"
```

2. Once the new password is set you can redeploy the application:

`helm upgrade <release-name> -n <namespace> -f local-values.yaml`

Replace `<release-name>` with the release name you specified during the initial installation (use `helm ls` to find it). If needed, specify the Kubernetes namespace with `-n` (default namespace is used if not specified). Stick to the same version using the `--version` flag.

## Update Redis main Password (embedded cluster)

Replace the value of the key `redis-password` in the secret `redis` by your new password.

```bash
NEWPASSWORD=$(echo -n '<new password>' | base64)
kubectl patch secret --namespace <namespace> redis \
   -p "{\"data\":{\"redis-password\":\"${NEWPASSWORD}\"}}"
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

## Update PostgreSQL client certificate (external cluster)

:::info
This procedure is intended for PostgreSQL configurations using mTLS (Mutual TLS). Please be aware that configuring PostgreSQL to utilize client certificates is not feasible with AWS RDS.
:::

:::caution
Ensure you back up your database before starting this procedure, which will incur minimal application downtimeâfrom scaling down to full redeployment.
:::

1. Scale down the Dashboard, Public API and Webhook receivers.

```bash
kubectl --namespace <namespace> get deploy -o name \
   | grep webapp \
   | xargs kubectl --namespace <namespace> scale deploy/% --replicas 0
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

2. Confirm all asynchronous and scheduled tasks have finished.

```bash
$ kubectl exec --namespace <namespace> -t deploy/worker-scanners \
   -- celery -A ward_run_app inspect active
```

The output should indicate `- empty -` for each pod, signaling completion.

```bash
app@(...):/app$ celery -A ward_run_app inspect active
(...)
->  workers@worker-worker-(...): OK
    - empty -
->  long_tasks@worker-long-tasks-(...): OK
    - empty -
->  scanner@worker-scanners-(...): OK
    - empty -
->  email@worker-email-(...): OK
    - empty -
->  email@worker-email-(...): OK
    - empty -
->  scanner@worker-scanners-(...): OK
    - empty -
->  long_tasks@worker-long-tasks-(...): OK
    - empty -
->  workers@worker-worker-(...): OK
    - empty -
```

3. Scale down all workers and scheduler pods.

```bash
kubectl --namespace <namespace> get deploy -o name \
   | grep worker \
   | xargs kubectl --namespace <namespace> scale deploy/% --replicas 0
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

4. The process for updating the PostgreSQL client certificate varies by installation method:

- **GCP Cloud SQL**: Create a new client certificate following the [procedure](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance#new-client).

### KOTS-Based Installation

1. Navigate to the âConfigâ tab in the [KOTS Admin Console](../management/infrastructure-management/admin-console.md) and update the PostgreSQL password.
2. Save the configuration.
3. Deploy the updated configuration.

![Deploying the updated configuration](/img/self-hosting/security/kots-deploy.png)

### Helm-Based Installation

:::caution
Do not directly modify values within the Kubernetes secret `gim-secrets`, as such changes will be overridden by subsequent Helm upgrades.
:::

1. For secrets management, ensure updates are made in the appropriate location based on your setup. Look at your values file under the `postgresql` section to find how the password is stored. For further details, see [Helm sensitive information management](../installation/helm-secrets).

- If you use a secret manager, change the required values in it.
- If you use a secret inside the namespace, patch it:

```bash
kubectl patch secret --namespace <namespace> <secret-name>\
   -p "{\"data\": { \"pg_client.key\": \"$(base64 -w0 ./tls.key)\", \"pg_client.crt\": \"$(base64 -w0 ./tls.crt)\"}}"
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

2. Once the new certificate & key are set you can redeploy the application:

`helm upgrade <release-name> -n <namespace> -f local-values.yaml`

Replace `<release-name>` with the release name you specified during the initial installation (use `helm ls` to find it). If needed, specify the Kubernetes namespace with `-n` (default namespace is used if not specified). Stick to the same version using the `--version` flag.

## Update PostgreSQL Data Encryption Key

Rotating the encryption key (Django Secret Key) is a critical process that involves several steps.

:::caution
Encryption key rotation is an intensive process that may:

- Take significant time to complete, fully occupying a Celery worker.
- Generate constant read/write load on the database.
- Increase database disk space usage (it's recommended to ensure at least 5GB of free disk space).

:::

### KOTS-Based Installation

The [gitguardian_secret_key.sh](https://raw.githubusercontent.com/GitGuardian/ggtools/refs/heads/main/secret-key-rotation/scripts/gitguardian_secret_key.sh) script enables you to rotate the database encryption key.

**Prerequisites**:

- `kubectl` and `kots` CLI (refer to the [installation documentation](https://docs.replicated.com/reference/kots-cli-getting-started)).
- Access to the Kubernetes namespace where the GitGuardian application is installed.

Ensure these requirements are met before running the script.

Install the script using the following command:

```bash
curl -O https://raw.githubusercontent.com/GitGuardian/ggtools/refs/heads/main/secret-key-rotation/scripts/gitguardian_secret_key.sh
chmod +x gitguardian_secret_key.sh
```

The script has two actions, `status` and `rotate`. `status` will output current key(s) hashes, and `rotate` will update the configuration.

```bash
bash gitguardian_secret_key.sh rotate --namespace <namespace>
```

Specify the Kubernetes namespace with `--namespace`.

![Script to add new data encryption key](/img/self-hosting/security/key-rotation-script.png)

After configuration update, the script will launch the [KOTS Admin Console](../management/infrastructure-management/admin-console.md) where you will need to deploy the updated configuration.

![Deploying the updated configuration](/img/self-hosting/security/kots-deploy.png)

### Helm-Based Installation

:::caution
Do not directly modify values within the Kubernetes secret `gim-secrets`, as such changes will be overridden by subsequent Helm upgrades.
:::

1. Generate a New Key: While any string is technically acceptable, we advise using a long (minimum 50 characters), high-entropy string for enhanced security.

Update the namespace `gg_namespace` as needed.

```bash
gg_namespace=<namespace>
new_django_key=$(LC_ALL=C tr -dc A-Za-z0-9 </dev/urandom | head -c 50 )
current_key=$(kubectl get secret -n $gg_namespace gim-secrets \
                  -o jsonpath='{.data.DJANGO_SECRET_KEY}' | base64 --decode)
current_encryption_keys=$(kubectl get secret -n $gg_namespace gim-secrets \
              -o jsonpath='{.data.ENCRYPTION_KEYS}' | base64 --decode)

# new encryption starts with new key, that will be used for re-encryption, then current key for fallback
if [ -n "$current_encryption_keys" ]; then
  new_encryption_keys=$(echo -n "$new_django_key,$current_encryption_keys,$current_key")
else
  new_encryption_keys=$(echo -n "$new_django_key,$current_key")
fi

echo "Please set djangoSecretKey with ${new_django_key}"
echo "Please set dbEncryptionKeys with ${new_encryption_keys}"
```

2. For secrets management, ensure updates are made in the appropriate location based on your setup. Look at your values file under the `miscEncryption` section to find how the password is stored. For further details, see [Helm sensitive information management](../installation/helm-secrets).

- If you use a secret manager, change the required values in it.
- If you use a secret inside the namespace, patch it:

```bash
kubectl patch secret -n $gg_namespace <secret-name> \
    -p "{\"data\":{\"DJANGO_SECRET_KEY\":\"${new_django_key}\"}}"
kubectl patch secret -n $gg_namespace <secret-name> \
    -p "{\"data\":{\"ENCRYPTION_KEYS\":\"${new_encryption_keys}\"}}"
```

3. Once the new password is set you can redeploy the application:

`helm upgrade <release-name> -n <namespace> -f local-values.yaml`

Replace `<release-name>` with the release name you specified during the initial installation (use `helm ls` to find it). If needed, specify the Kubernetes namespace with `-n` (default namespace is used if not specified). Stick to the same version using the `--version` flag.

### Initiating data encryption key rotation

Once at least two encryption keys are set in your settings:

1. Navigate to the Encryption Key Rotation page in the [Admin area](../management/application-management/admin-area.md):

![Encryption Key Rotation Page](/img/self-hosting/security/key-rotation-admin-area.png)

2. If no rotation has been initiated for the recently added key, start by triggering the creation of rotation jobs. Click the âPrepare Key Rotationâ button.

![Prepare Key Rotation](/img/self-hosting/security/key-rotation-prepare.png)

3. Activate the key rotation jobs

:::caution
Be aware that these jobs may take a long time and will fully occupy one Celery worker.
:::

![Activate Jobs](/img/self-hosting/security/key-rotation-activate-jobs.png)

4. The jobs will run automatically. All that's left is to wait for their completion. You have the option to stop or restart the jobs as needed.

![Jobs Running](/img/self-hosting/security/key-rotation-activate-jobs-running.png)
