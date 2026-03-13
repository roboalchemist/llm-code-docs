# Source: https://docs.gitguardian.com/self-hosting/installation/helm-secrets.md

# Helm Sensitive Information Management

> Manage sensitive configuration values for GitGuardian self-hosted Helm installations using Kubernetes secrets.

## Introduction

GitGuardian Helm installations are configured through a values file (see [GitGuardian Helm Installation](./installation-existing-cluster-helm) for more information). It requires configuring sensitive information.

GitGuardian supports three ways to set this information:

- Sensitive parameters in Kubernetes secrets
- Parameters inherited from external secrets (deprecated)
- All parameters inline

Passing sensitive information through secrets should be favored over the inline
option.

## Kubernetes secrets

In the namespace prepared for the GitGuardian installation, you can set up
secrets to safely store the sensitive information needed for the deployment and the configuration.

If you choose this method for the deployment, you can optionally specify Docker secrets
used to pull images from a private container registry.

For the configuration, two secrets are needed for PostgreSQL and Redis
information, and another one can optionally be added for encryption parameters.

### Docker secret (optional)

You can create a [Docker secret](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry) to pull images from a private registry.
Once created, you can specify the secret name in your `local-values.yaml` file:

```yaml
global:
  imageRegistry: docker.internal # The host of the private registry
  imagePullSecrets:
    - name: pull-secret # The name of the secret previously created
```

With this configuration, pods will use `pull-secret` docker secret to pull images from the `docker.internal` private registry.

> Note: Replicated SDK is not impacted by the `global.imageRegistry` attribute and is pulled directly from `docker.io` at the moment. You may pull this image from another registry using `replicated.images.replicated-sdk` and `replicated.imagePullSecrets`.

### Database parameters

Check the relevant pages to see how to implement this option for :

- [PostgreSQL password](./databases/database-config#postgresql)
- [PostgreSQL TLS parameters](./databases/tls#postgresql)
- [Redis password](./databases/database-config#redis)
- [Redis TLS parameters](./databases/tls#redis)

### Existing secret

You may choose to set parameters relevant to the application using an [existing secret](https://kubernetes.io/docs/concepts/configuration/secret/).

The secret described there must contain the following keys :

- `ADMIN_PASSWORD`: admin password (only used during the first install)
- `DJANGO_SECRET_KEY`
- `REDIS_URL`: redis://username:password@host:port
- `POSTGRES_PASSWORD`
- `SP_X509_CERT`: a valid X509 certificate for SAML SP
- `SP_PRIVATE_KEY`: a valid X509 private key for SAML SP

```bash
kubectl create secret generic gitguardian-secret \
  --from-literal=ADMIN_PASSWORD=my_admin_password \
  --from-literal=DJANGO_SECRET_KEY=my_django_secret_key \
  --from-literal=REDIS_URL=my_redis_url \
  --from-literal=POSTGRES_PASSWORD=my_postgres_password \
  --from-file=SP_PRIVATE_KEY=/path/to/x509-key \
  --from-file=SP_X509_CERT=/path/to/x509-cert \
  --namespace <namespace>
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

To reference this secret for installation, include this
extract in your `local-values.yaml` file:

```yaml
onPrem:
  adminUser:
    email: your.email@example.com
    firstname: user_name
    existingSecret: gitguardian-secret
    existingSecretKeys:
      password: ADMIN_PASSWORD

postgresql:
  existingSecret: gitguardian-secret
  existingSecretKeys:
    password: POSTGRES_PASSWORD

redis:
  main:
    existingSecret: gitguardian-secret
    existingSecretKeys:
      url: REDIS_URL

miscEncryption:
  existingSecret: gitguardian-secret # The name of the secret previously created
  existingSecretKeys:
    djangoSecretKey: DJANGO_SECRET_KEY
    x509Cert: SP_X509_CERT
    x509PrivateKey: SP_PRIVATE_KEY
```

In this case, as some pieces of configuration are managed outside of the Helm chart, you should consider using [Reloader](https://github.com/stakater/Reloader/blob/master/README.md) to automatically perform a rolling upgrade on relevant Kubernetes workloads like `Deployments`.

For example, if you annotate the `gitguardian-secret` secret with `reloader.stakater.com/match: 'true'`, you can configure the following annotations in `local-values.yaml` to perform a rollout on secret changes:

```yaml
front:
  nginx:
    annotations:
      reloader.stakater.com/search: 'true'

webapps:
  hook:
    annotations:
      reloader.stakater.com/search: 'true'
  internal_api:
    annotations:
      reloader.stakater.com/search: 'true'
  internal_api_long:
    annotations:
      reloader.stakater.com/search: 'true'
  public_api:
    annotations:
      reloader.stakater.com/search: 'true'

celeryWorkers:
  email:
    annotations:
      reloader.stakater.com/search: 'true'
  long:
    annotations:
      reloader.stakater.com/search: 'true'
  realtime-ods:
    annotations:
      reloader.stakater.com/search: 'true'
  scanners:
    annotations:
      reloader.stakater.com/search: 'true'
  worker:
    annotations:
      reloader.stakater.com/search: 'true'
```

After installation, if you didn't set these values yourself, you should retrieve
the ones generated automatically and **store them in a secure location**.

```shell
kubectl get secrets gim-secrets --namespace <namespace> -o jsonpath='{.data.DJANGO_SECRET_KEY}' | base64 -d
kubectl get secrets gim-secrets --namespace <namespace> -o jsonpath='{.data.SP_X509_CERT}' | base64 -d
kubectl get secrets gim-secrets --namespace <namespace> -o jsonpath='{.data.SP_PRIVATE_KEY}' | base64 -d
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

## Inline parameters

You may store all information required for the configuration directly in your
`local-values.yaml` file. If you choose to do so, the below example file shows
the minimal elements that are required for a successful installation.

```yaml
hostname: gitguardian.internal.yourcompany.com

postgresql:
  host: 'postgresql'
  username: postgres
  database: postgres
  password: postgres-password

redis:
  main:
    url: redis-url

onPrem:
  adminUser:
    email: your.email@example.com
    firstname: user_name
```

For optional fields that may be needed for your specific installations,
such as TLS parameters, see the
[values reference documentation](/self-hosting/management/infrastructure-management/helm-values).

:::caution

If you don't specify the
`miscEncryption.djangoSecretKey` (which is the preferred method), it will be
generated during the first installation, and you should then retrieve it and
**store it in a secure location**.

:::

```shell
kubectl get secrets gim-secrets --namespace <namespace> -o jsonpath='{.data.DJANGO_SECRET_KEY}' | base64 -d
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

## External Secret

:::caution

External secrets handling is deprecated and will be removed in a near future.
It is recommended that you handle the management of `externalSecret` resources on your own and use `existingSecrets` parameters instead. This will help you to better organize and secure your secrets.

:::

You may want to store the sensitive information in your secret management system.
If that is the case, you should reference it in the `local-values.yaml` file in
this way :

```yaml
externalSecrets:
  enabled: true
  path: 'path/to/file'
  secretStoreRef:
    name: vault # The secretStoreRef name
    kind: SecretStore
```

The secret described there must contain the following keys :

- `DJANGO_SECRET_KEY`
- `REDIS_URL`: redis://username:password@host:port
- `POSTGRES_PASSWORD`
- `SP_X509_CERT`: a valid X509 certificate for SAML SP
- `SP_PRIVATE_KEY`: a valid X509 private key for SAML SP

## Expected result

After the installation, no matter the method you chose, there should be a secret
called `gim-secrets` in your namespace.
It is expected to contain 6 parameters :

- `ADMIN_PASSWORD`
- `DJANGO_SECRET_KEY`
- `POSTGRES_PASSWORD`
- `REDIS_URL`
- `SP_PRIVATE_KEY`
- `SP_X509_CERT`

You can check this secret has been correctly created with:

```shell
kubectl get secrets gim-secrets --namespace <namespace> -o jsonpath='{.data}' | python -m json.tool
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).
