# Source: https://docs.api7.ai/enterprise/api-security/kubernetes-secret.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-security/kubernetes-secret.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-security/kubernetes-secret.md

# Reference Secrets in Kubernetes Secret

Kubernetes Secrets are objects that store sensitive data like passwords, API keys, and tokens. They can be exposed as environment variables within Pods or integrated as a secret provider to enhance API security.

This tutorial demonstrates how to integrate API7 Enterprise with Kubernetes as a secret provider, enabling you to securely store and reference consumer credentials and plugin configurations from Kubernetes secrets.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.7.x/getting-started/install-api7-ee.md).
2. [Have at least one gateway instance](https://docs.api7.ai/enterprise/3.7.x/getting-started/add-gateway-instance.md) in your gateway group.
3. Prepare your Kubernetes cluster to store secrets.
4. Install [cURL](https://curl.se/) to send requests to the services for validation.

## Add Secret Provider in Gateway Group[â](#add-secret-provider-in-gateway-group "Direct link to Add Secret Provider in Gateway Group")

* Dashboard
* ADC
* Ingress Controller

1. Select **Secret Providers** of your gateway group from the side navigation bar, then click **Add Secret Provider**.
2. From the dialog box, do the following:

* In the **Secret Provider ID** field, enter `my-kubernetes-secret`.
* In the **Secret Manager** field, choose `Kubernetes`.
* Fill in the **API Server Address** field. For example, `http://127.0.0.1`.
* Fill in the **Token** field.
* Click **Add**.

3. Copy the **Secret Variable** for future reference. All secret references are generated from it, for example, `$secret://kubernetes/my-kubernetes-secret/$namespace/$secret_name/$key`.

Coming soon.

Coming soon.

## Reference Secrets for SSL Certificate[â](#reference-secrets-for-ssl-certificate "Direct link to Reference Secrets for SSL Certificate")

The sensitive fields `certificate` and `private key` within an SSL certificate object can be securely stored in an external secret manager (such as HashiCorp Vault, AWS Secret Manager or Kubernetes Secret) and referenced within API7 Gateway.

### Store Secrets[â](#store-secrets "Direct link to Store Secrets")

Create a `ssl-secret` YAML file:

```
apiVersion: v1
kind: Secret
metadata:
  namespace: default
  name: ssl
type: kubernetes.io/tls
data: # Must use base64 value
  tls.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUNVakNDQWJzQ0FnMytNQTBHQ1NxR1NJYjNE
    UUVCQlFVQU1JR2JNUXN3Q1FZRFZRUUdFd0pLVURFT01Bd0cKQTFVRUNCTUZWRzlyZVc4eEVEQU9C
    Z05WQkFjVEIwTm9kVzh0YTNVeEVUQVBCZ05WQkFvVENFWnlZVzVyTkVSRQpNUmd3RmdZRFZRUUxF
    dzlYWldKRFpYSjBJRk4xY0hCdmNuUXhHREFXQmdOVkJBTVREMFp5WVc1ck5FUkVJRmRsCllpQkRR
    VEVqTUNFR0NTcUdTSWIzRFFFSkFSWVVjM1Z3Y0c5eWRFQm1jbUZ1YXpSa1pDNWpiMjB3SGhjTk1U
    TXcKTVRFeE1EUTFNVE01V2hjTk1UZ3dNVEV3TURRMU1UTTVXakJMTVFzd0NRWURWUVFHREFKS1VE
    RVBNQTBHQTFVRQpDQXdHWEZSdmEzbHZNUkV3RHdZRFZRUUtEQWhHY21GdWF6UkVSREVZTUJZR0Ex
    VUVBd3dQZDNkM0xtVjRZVzF3CmJHVXVZMjl0TUlHYU1BMEdDU3FHU0liM0RRRUJBUVVBQTRHSUFE
    Q0JoQUo5WThFaUhmeHhNL25PbjJTbkkxWHgKRHdPdEJEVDFKRjBReTliMVlKanV2YjdjaTEwZjVN
    Vm1UQllqMUZTVWZNOU1vejJDVVFZdW4yRFljV29IcFA4ZQpqSG1BUFVrNVd5cDJRN1ArMjh1bklI
    QkphVGZlQ09PekZSUFY2MEdTWWUzNmFScG04L3dVVm16eGFLOGtCOWVaCmhPN3F1TjdtSWQxL2pW
    cTNKODhDQXdFQUFUQU5CZ2txaGtpRzl3MEJBUVVGQUFPQmdRQU1meTQzeE15OHh3QTUKVjF2T2NS
    OEtyNWNaSXdtbFhCUU8xeFEzazlxSGtyNFlUY1JxTVQ5WjVKTm1rWHYxK2VSaGcwTi9WMW5NUTRZ
    RgpnWXcxbnlESnBnOTduZUV4VzQyeXVlMFlHSDYyV1hYUUhyOVNVREgrRlowVnQvRGZsdklVTWRj
    UUFEZjM4aU9zCjlQbG1kb3YrcE0vNCs5a1h5aDhSUEkzZXZ6OS9NQT09Ci0tLS0tRU5EIENFUlRJ
    RklDQVRFLS0tLS0K    
  tls.key: RXhhbXBsZSBkYXRhIGZvciB0aGUgVExTIGNydCBmaWVsZA==
```

Then apply to your Kubernetes cluster:

```
kubectl apply -f ssl-secret.yaml
```

### Add SSL Certificate[â](#add-ssl-certificate "Direct link to Add SSL Certificate")

1. Select **Certificates** of your gateway group from the side navigation bar, enter the **SSL Certificates** tab.
2. Click **Add SSL Certificate**.
3. From the dialog box, do the following:

* In the **Name** field, enter `Test SSL Certificate`.
* In the **Certificate** field, enter `$secret://kubernetes/my-kubernetes-secret/default/ssl/tls.crt`.
* In the **Private Key** field, enter `$secret://kubernetes/my-kubernetes-secret/default/ssl/tls.key`.
* Click **Add**.

4. For full use and validation of SSL certificate, see [Configure mTLS between Client and API7 Gateway](https://docs.api7.ai/enterprise/3.7.x/api-security/client-mtls.md).

## Reference Secrets to Create Consumer Credential[â](#reference-secrets-to-create-consumer-credential "Direct link to Reference Secrets to Create Consumer Credential")

The following sensitive field in consumer credentials can be stored in an external secret manager (HashiCorp Vault, AWS Secret Manager or Kubernetes Secret) and referenced within API7 Gateway:

* `key` in Key Authentication credential
* `password` in Basic Authentication credential
* `secret`, `public key` in JWT Authentication credential
* `secret key` in HMAC Authentication credential

### Add a Consumer[â](#add-a-consumer "Direct link to Add a Consumer")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Click **Add Consumer**.
3. From the dialog box, do the following:

* In the **Name** field, enter `Alice`.
* Click **Add**.

Coming soon.

Coming soon.

### Store Secrets[â](#store-secrets-1 "Direct link to Store Secrets")

Create a `alice-secret` YAML file:

```
apiVersion: v1
kind: Secret
metadata:
  namespace: default
  name: alice
type: Opaque
stringData:
  key: alice-key # for key authentication credential
  password: alice-password # for basic authentication credential
  secret: alice-secret # for JWT credential
  secret-key: alice-secret-key # for HMAC authentication credential
```

Then apply to your Kubernetes cluster:

```
kubectl apply -f alice-secret.yaml
```

### Add Key Authentication Credential[â](#add-key-authentication-credential "Direct link to Add Key Authentication Credential")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Select your target consumer, for example, `Alice`.
3. Under the **Credentials** tab, click **Add Key Authentication Credential**.
4. From the dialog box, do the following:

* In the **Name** field, enter `primary-key`.
* In the **Key** field, enter `$secret://kubernetes/my-kubernetes-secret/default/alice/key`.
* Click **Add**.

Coming soon.

Coming soon.

### Add Basic Authentication Credential[â](#add-basic-authentication-credential "Direct link to Add Basic Authentication Credential")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Select your target consumer, for example, `Alice`.
3. Under the **Credentials** tab, click **Basic Authentication** tab, then click **Add Basic Authentication Credential**.
4. From the dialog box, do the following:

* In the **Name** field, enter `primary-basic`.
* In the **Username** field, enter `Alice`.
* In the **Password** field, enter `$secret://kubernetes/my-kubernetes-secret/default/alice/password`.
* Click **Add**.

Coming soon.

Coming soon.

### Add JWT Authentication Credential[â](#add-jwt-authentication-credential "Direct link to Add JWT Authentication Credential")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Select your target consumer, for example, `Alice`.
3. Under the **Credentials** tab, click **JWT** tab, then click **Add JWT Credential**.
4. From the dialog box, do the following:

* In the **Name** field, enter `primary-jwt`.
* In the **Key** field, enter `alice-key`.
* In the **Algorithm** field, choose `HS256`.
* In the **Secret** field, enter `$secret://kubernetes/my-kubernetes-secret/default/alice/secret`.
* Click **Add**.

Coming soon.

Coming soon.

### Add HMAC Authentication Credential[â](#add-hmac-authentication-credential "Direct link to Add HMAC Authentication Credential")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Select your target consumer, for example, `Alice`.
3. Under the **Credentials** tab, click **HMAC Authentication** tab, then click **Add HMAC Authentication Credential**.
4. From the dialog box, do the following:

* In the **Name** field, enter `primary-hmac`.
* In the **Key ID** field, enter `alice-keyid`.
* In the **Secret Key** field, enter `$secret://kubernetes/my-kubernetes-secret/default/alice/secret-key`.
* Click **Add**.

Coming soon.

Coming soon.

### Validate Consumer Credentials[â](#validate-consumer-credentials "Direct link to Validate Consumer Credentials")

#### Validate Key Authentication[â](#validate-key-authentication "Direct link to Validate Key Authentication")

See [Enable Key Authentication for APIs](https://docs.api7.ai/enterprise/3.7.x/api-security/api-authentication.md#enable-key-authentication-for-apis) for instruction, and enable the [Key Auth Plugin](https://docs.api7.ai/hub/key-auth.md) on the service level.

Then follow [Validate Key Authentication](https://docs.api7.ai/enterprise/3.7.x/api-security/api-authentication.md#validate-key-authentication) instructions.

#### Validate Basic Authentication[â](#validate-basic-authentication "Direct link to Validate Basic Authentication")

See [Enable Basic Authentication for APIs](https://docs.api7.ai/enterprise/3.7.x/api-security/api-authentication.md#enable-basic-authentication-for-apis) for instruction, and enable the [Basic Auth Plugin](https://docs.api7.ai/hub/basic-auth.md) on the service level.

Then follow [Validate Basic Authentication](https://docs.api7.ai/enterprise/3.7.x/api-security/api-authentication.md#validate-basic-authentication) instructions.

#### Validate JWT Authentication[â](#validate-jwt-authentication "Direct link to Validate JWT Authentication")

See [Enable JWT Authentication for APIs](https://docs.api7.ai/enterprise/3.7.x/api-security/api-authentication.md#enable-jwt-authentication-for-apis) for instruction, and enable the [JWT Auth Plugin](https://docs.api7.ai/hub/jwt-auth.md) on the service level.

Then follow [Validate JWT Authentication](https://docs.api7.ai/enterprise/3.7.x/api-security/api-authentication.md#validate-jwt-authentication) instructions.

#### Validate HMAC Authentication[â](#validate-hmac-authentication "Direct link to Validate HMAC Authentication")

See [Enable HMAC Authentication for APIs](https://docs.api7.ai/enterprise/3.7.x/api-security/api-authentication.md#enable-hmac-authentication-for-apis) for instruction, and enable the [HMAC Auth Plugin](https://docs.api7.ai/hub/hmac-auth.md) on the service level.

Then follow [Validate HMAC Authentication](https://docs.api7.ai/enterprise/3.7.x/api-security/api-authentication.md#validate-hmac-authentication) instructions.

## Reference Secrets to Enable Plugin[â](#reference-secrets-to-enable-plugin "Direct link to Reference Secrets to Enable Plugin")

The following sensitive field in plugin configurations can be stored in an external secret manager (HashiCorp Vault, AWS Secret Manager, Kubernetes Secret) and referenced in API7 Gateway:

| Plugin                                                                          | Field                              |
| ------------------------------------------------------------------------------- | ---------------------------------- |
| [Limit Count](https://docs.api7.ai/hub/limit-count.md)                          | `redis_username`, `redis_password` |
| [Authz-Casdoor](https://apisix.apache.org/docs/apisix/plugins/authz-casdoor/)   | `client_id`, `client_secret`       |
| [Wolf RBAC](https://apisix.apache.org/docs/apisix/plugins/wolf-rbac/)           | `appid`                            |
| [LDAP Authentication](https://apisix.apache.org/docs/apisix/plugins/ldap-auth/) | `user_dn`                          |

This section demonstrates configuring [Limit Count Plugin](https://docs.api7.ai/hub/limit-count.md) as an example.

### Store Secret[â](#store-secret "Direct link to Store Secret")

Create a `redis-secret` YAML file:

```
apiVersion: v1
kind: Secret
metadata:
  namespace: default
  name: redis
type: Opaque
stringData:
  username: YXBpNw== 
  password: cmVkaXMtYXBpNw==
```

Then apply to your Kubernetes cluster:

```
kubectl apply -f redis-secret.yaml
```

### Configure Limit Count Plugin[â](#configure-limit-count-plugin "Direct link to Configure Limit Count Plugin")

For where and how to enable the [Limit Count plugin](https://docs.api7.ai/hub/limit-count.md), refer to [Apply Rate Limiting to APIs](https://docs.api7.ai/enterprise/3.7.x/api-security/rate-limiting.md).

* Dashboard
* ADC
* Ingress Controller

Add the following configuration to the **JSON Editor**:

```
{
  "count": 3,
  "time_window": 60,
  "key_type": "var",
  "rejected_code": 429,
  "rejected_msg": "Too many requests",
  "key": "remote_addr",
  "policy": "redis",
  "redis_host": "127.0.0.1",
  "redis_port": 6379,
  "redis_username": "$secret://kubernetes/my-kubernetes-secret/default/redis/username"
  "redis_password": "$secret://kubernetes/my-kubernetes-secret/default/redis/password",
  "redis_database": 1,
  "redis_timeout": 1001,
  "allow_degradation": false,
  "show_limit_quota_header": true
}
```

The following is only the plugin configuration and not a complete configuration file to synchronize. Refer to [Apply Rate Limiting to APIs](https://docs.api7.ai/enterprise/3.7.x/api-security/rate-limiting.md) for where and how to enable the Limit Count plugin using ADC.

```
limit-count:
  count: 3
  time_window: 60
  key_type: var
  rejected_code: 429
  rejected_msg: Too many requests
  key: remote_addr
  policy: redis
  redis_host: 127.0.0.1
  redis_port: 6379
  redis_username: $secret://kubernetes/my-kubernetes-secret/default/redis/username
  redis_password: $secret://kubernetes/my-kubernetes-secret/default/redis/password
  redis_database: 1
  redis_timeout: 1001
  allow_degradation: false
  show_limit_quota_header: true
```

Coming soon.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Secrets](https://docs.api7.ai/enterprise/3.7.x/key-concepts/secrets.md)
  * [Plugins](https://docs.api7.ai/enterprise/3.7.x/key-concepts/plugins.md)
  * [Consumers](https://docs.api7.ai/enterprise/3.7.x/key-concepts/consumers.md)
  * [Certificates](https://docs.api7.ai/enterprise/3.7.x/key-concepts/certificates.md)

* API Consumption
  <!-- -->
  * [Manage Consumer Credentials](https://docs.api7.ai/enterprise/3.7.x/api-consumption/manage-consumer-credentials.md)
