# Source: https://docs.api7.ai/enterprise/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-security/hashicorp-vault.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-security/hashicorp-vault.md

# Reference Secrets in HashiCorp Vault

[HashiCorp Vault](https://www.vaultproject.io/) is a centralized platform for managing secrets and encryption across different environments and applications. It provides a unified secrets management for storing and accessing, such as API keys, passwords, certificates, and more.

This tutorial demonstrates how to integrate API7 Enterprise with HashiCorp Vault, enabling you to securely store and reference consumer credentials and plugin configurations from Vault.

Below is an interactive demo providing a hands-on introduction to storing and retrieving key-auth secrets in HashiCorp Vault with API7 Enterprise.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have at least one gateway instance](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md) in your gateway group.
3. Install [Docker](https://docs.docker.com/get-docker/).
4. Install [cURL](https://curl.se/) to send requests to the services for validation.
5. Install [ZIP](https://infozip.sourceforge.net/Zip.html) to unzip the Vault binary from the [official distributed zipped file](https://developer.hashicorp.com/vault/downloads).

## Configure Vault Server[â](#configure-vault-server "Direct link to Configure Vault Server")

Start a Vault instance in dev mode in Docker named `api7-quickstart-vault` with the token `api7-quickstart-vault-token`. The exposed port is mapped to `8200` on the host machine:

```
docker run -d --cap-add=IPC_LOCK \
    -e 'VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:8200' \
    -e 'VAULT_ADDR=http://127.0.0.1:8200' \
    -e 'VAULT_DEV_ROOT_TOKEN_ID=api7-quickstart-vault-token' \
    -e 'VAULT_TOKEN=api7-quickstart-vault-token' \
    --name api7-quickstart-vault \
    -p 8200:8200 vault:1.13.0
```

Select `kv` as the API7 SSL certificate storage path.

```
docker exec api7-quickstart-vault vault secrets enable -path=kv -version=1 kv
```

API7 Gateway needs permission to access Vault and retrieve secrets. You should create a policy file in [HashiCorp Configuration Language (HCL)](https://github.com/hashicorp/hcl) to generate a Vault access token for API7 Gateway.

Create a Vault policy file named `api7-policy.hcl` in the Vault instance to grant read permission of the path `secret/` to API7 Gateway. You can put secrets under the path `secret/` to allow API7 Gateway to read them:

```
docker exec api7-quickstart-vault /bin/sh -c "echo '
path \"secret/data/*\" {
    capabilities = [\"read\"]
}
' > /etc/api7-policy.hcl"
```

Apply the policy file to the Vault instance:

```
docker exec api7-quickstart-vault vault policy write api7-policy /etc/api7-policy.hcl
```

Next, generate the access token attached to the newly defined policy for API7 Gateway to access Vault:

```
docker exec api7-quickstart-vault vault token create -policy="api7-policy"
```

Every execution of the above command will generate a different token. If successful, the output should be similar to the following:

```
Key                  Value
---                  -----
token                hvs.CAESIHUznrV4wgcifUia0FROd6iprK7NjipAiHBYwiZDQP9TGh4KHGh2cy5ndHc5dzBPbXd5Y1pzblZXd2ZuQXA3ZHI
token_accessor       YY4iCj2lICDNd50ZJDsBjvZK
token_duration       768h
token_renewable      true
token_policies       ["api7-policy" "default"]
identity_policies    []
policies             ["api7-policy" "default"]
```

## Add Secret Provider in Gateway Group[â](#add-secret-provider-in-gateway-group "Direct link to Add Secret Provider in Gateway Group")

* Dashboard
* ADC
* Ingress Controller

1. Select **Secret Providers** of your gateway group from the side navigation bar, then click **Add Secret Provider**.
2. From the dialog box, do the following:

* In the **Secret Provider ID** field, enter `my-vault`.
* In the **Secret Manager** field, choose `HashiCorp Vault`.
* In the **KV Version** field, choose `KV version 1`.
* Fill in the **Vault Server URL** field. For example, `127.0.0.1:8200`.
* Fill in the **Secret Prefix** field. For example, `kv/api7`.
* In the **Authentication Method** field, choose `Token`.
* Fill in the **Token** field.
* Click **Add**.

Not applicable.

Not applicable.

## Reference Secrets to Create Consumer Credential[â](#reference-secrets-to-create-consumer-credential "Direct link to Reference Secrets to Create Consumer Credential")

The following sensitive field in consumer credentials can be stored in an external secret manager(HashiCorp Vault, AWS Secret Manager, etc.) and referenced in API7 Gateway:

* `key` in Key Authentication credential
* `password` in Basic Authentication credential
* `secret` , `public key` in JWT Authentication credential
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

To use ADC to create a consumer, create the following configuration:

consumer.yaml

```
consumers:
  - username: Alice
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f consumer.yaml
```

Coming Soon.

### Store Secrets[â](#store-secrets "Direct link to Store Secrets")

Create a secret `key=alice-primary-key` for key authentication credential and store it in the path `secret/api7/consumer/alice` of Vault. **Ensure the path aligns with your configured secret prefix**:

```
docker exec api7-quickstart-vault vault kv put kv/api7/consumer/alice key=alice-primary-key
```

The expected response is similar to the following:

```
=== Secret Path ===
secret/data/api7

======= Metadata =======
Key                Value
---                -----
created_time       2023-03-15T11:42:17.123175125Z
custom_metadata    <nil>
deletion_time      n/a
destroyed          false
version            1
```

Repeat to create more secrets for other consumer credentials, all under the same path:

* For basic authentication credential:

```
docker exec api7-quickstart-vault vault kv put kv/api7/consumer/alice password=alice-password
```

* For JWT authentication credential:

```
docker exec api7-quickstart-vault vault kv put kv/api7/consumer/alice secret=alice-secret
```

* For HMAC authentication credential:

```
docker exec api7-quickstart-vault vault kv put kv/api7/consumer/alice secret-key=alice-secret-key
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
* In the **Key** field, choose **Reference from Secret Provider**, then enter `$secret://vault/my-vault/consumer/alice/key`.
* Click **Add**.

note

All secret references start with `$secret://`. `vault` is **Secret Manager** of the secret provider, `my-vault` is **Secret Provider ID**. When connecting to HashiCorp Vault, `$secret://vault/my-vault` will be replaced with the actual **Secret Prefix** of the secret provider. Finally, the path sent to HashiCorp Vault will be `secret/api7/consumer/alice/key`.

To use ADC to create a consumer with `key-auth`, update your configuration:

consumer.yaml

```
consumers:
  - username: Alice
    credentials:
      - name: primary-key
        type: key-auth
        config:
          key: $secret://vault/my-vault/consumer/alice/key
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f consumer.yaml
```

Coming Soon.

### Add Basic Authentication Credential[â](#add-basic-authentication-credential "Direct link to Add Basic Authentication Credential")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Select your target consumer, for example, `Alice`.
3. Under the **Credentials** tab, click **Basic Authentication**tab, then click **Add Basic Authentication Credential**.
4. From the dialog box, do the following:

* In the **Name** field, enter `primary-basic`.
* In the **Username** field, enter `Alice`.
* In the **Password** field, choose **Reference from Secret Provider**, then enter `$secret://vault/my-vault/consumer/alice/password`.
* Click **Add**.

note

All secret references start with `$secret://`. `vault` is **Secret Manager** of the secret provider, `my-vault` is **Secret Provider ID**. When connecting to HashiCorp Vault, `$secret://vault/my-vault` will be replaced with the actual **Secret Prefix** of the secret provider. Finally, the path sent to HashiCorp Vault will be `secret/api7/consumer/alice/password`.

To use ADC to create a consumer with `basic-auth`, update your configuration:

consumer.yaml

```
consumers:
  - username: Alice
    credentials:
      - name: primary-key
        type: basic-auth
        config:
          password: $secret://vault/my-vault/consumer/alice/password
          username: Alice
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f consumer.yaml
```

Coming Soon.

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
* In the **Secret** field, choose **Reference from Secret Provider**, then enter `$secret://vault/my-vault/consumer/alice/secret`.
* Click **Add**.

note

All secret references start with `$secret://`. `vault` is **Secret Manager** of the secret provider, `my-vault` is **Secret Provider ID**. When connecting to HashiCorp Vault, `$secret://vault/my-vault` will be replaced with the actual **Secret Prefix** of the secret provider. Finally, the path sent to HashiCorp Vault will be `secret/api7/consumer/alice/secret`.

To use ADC to create a consumer with `jwt-auth`, update your configuration:

consumer.yaml

```
consumers:
  - username: Alice
    credentials:
      - name: primary-jwt
        type: jwt-auth
        config:
          algorithm: HS256
          key: alice-key
          secret: $secret://vault/my-vault/consumer/alice/secret
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f consumer.yaml
```

Coming Soon.

### Add HMAC Authentication Credential[â](#add-hmac-authentication-credential "Direct link to Add HMAC Authentication Credential")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Select your target consumer, for example, `Alice`.
3. Under the **Credentials** tab, click **HMAC Authentication**tab, then click **Add HMAC Authentication Credential**.
4. From the dialog box, do the following:

* In the **Name** field, enter `primary-hmac`.
* In the **Key ID** field, enter `alice-keyid`.
* In the **Secret Key** field, choose **Reference from Secret Provider**, then enter `$secret://vault/my-vault/consumer/alice/secret-key`.
* Click **Add**.

note

All secret references start with `$secret://`. `vault` is **Secret Manager** of the secret provider, `my-vault` is **Secret Provider ID**. When connecting to HashiCorp Vault, `$secret://vault/my-vault` will be replaced with the actual **Secret Prefix** of the secret provider. Finally, the path sent to HashiCorp Vault will be `secret/api7/consumer/alice/secret-key`.

To use ADC to create a consumer with `hmac-auth`, update your configuration:

consumer.yaml

```
consumers:
  - username: Alice
    credentials:
      - name: primary-hmac
        type: hmac-auth
        config:
          key_id: alice-keyid
          secret_key: $secret://vault/my-vault/consumer/alice/secret-key
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f consumer.yaml
```

Coming Soon.

## Validate[â](#validate "Direct link to Validate")

### Validate Key Authentication[â](#validate-key-authentication "Direct link to Validate Key Authentication")

See [Enable Key Authentication for APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#enable-key-authentication-for-apis) for instruction, and enable the [Key Auth Plugin](https://docs.api7.ai/hub/key-auth.md) on the service level.

Then follow [Validate Key Authentication](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#validate-key-authentication) instruction.

### Validate Basic Authentication[â](#validate-basic-authentication "Direct link to Validate Basic Authentication")

See [Enable Basic Authentication for APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#enable-basic-authentication-for-apis) for instruction, and enable the [Basic Auth Plugin](https://docs.api7.ai/hub/basic-auth.md) on the service level.

Then follow [Validate Basic Authentication](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#validate-basic-authentication) instruction.

### Validate JWT Authentication[â](#validate-jwt-authentication "Direct link to Validate JWT Authentication")

See [Enable JWT Authentication for APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#enable-jwt-authentication-for-apis) for instruction, and enable the [JWT Auth Plugin](https://docs.api7.ai/hub/jwt-auth.md) on the service level.

Then follow [Validate JWT Authentication](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#validate-jwt-authentication) instruction.

### Validate HMAC Authentication[â](#validate-hmac-authentication "Direct link to Validate HMAC Authentication")

See [Enable HMAC Authentication for APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#enable-hmac-authentication-for-apis) for instruction, and enable the [HMAC Auth Plugin](https://docs.api7.ai/hub/hmac-auth.md) on the service level.

Then follow [Validate HMAC Authentication](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#validate-hmac-authentication) instruction.

## Reference Secrets to Enable Plugin[â](#reference-secrets-to-enable-plugin "Direct link to Reference Secrets to Enable Plugin")

The following sensitive field in plugin configurations can be stored in an external secret manager(HashiCorp Vault, AWS Secret Manager, etc.) and referenced in API7 Gateway:

| Plugin                                                                          | Field                              |
| ------------------------------------------------------------------------------- | ---------------------------------- |
| [Limit Count](https://docs.api7.ai/hub/limit-count.md)                          | `redis_username`, `redis_password` |
| [Authz-Casdoor](https://apisix.apache.org/docs/apisix/plugins/authz-casdoor/)   | `client_id`, `client_secret`       |
| [Wolf RBAC](https://apisix.apache.org/docs/apisix/plugins/wolf-rbac/)           | `appid`                            |
| [LDAP Authentication](https://apisix.apache.org/docs/apisix/plugins/ldap-auth/) | `user_dn`                          |

This section demonstrates configuring [Limit Count Plugin](https://docs.api7.ai/hub/limit-count.md) as an example.

### Create a Secret[â](#create-a-secret "Direct link to Create a Secret")

Create a secret `username=api7` and store it in the path `secret/api7/redis` of Vault. **Ensure the path aligns with your configured secret prefix**:

```
docker exec api7-quickstart-vault vault kv put secret/api7/redis username=api7
```

The expected response is similar to the following:

```
=== Secret Path ===
secret/data/api7

======= Metadata =======
Key                Value
---                -----
created_time       2023-03-15T11:42:17.123175125Z
custom_metadata    <nil>
deletion_time      n/a
destroyed          false
version            1
```

Try again to store a secret for Redis password:

```
docker exec api7-quickstart-vault vault kv put secret/api7/redis password=redis-api7
```

### Configure Limit Count Plugin[â](#configure-limit-count-plugin "Direct link to Configure Limit Count Plugin")

For where and how to enable the [Limit Count plugin](https://docs.api7.ai/hub/limit-count.md), refer to [Apply Rate Limiting to APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/rate-limiting.md).

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
  "redis_username": "$secret://vault/my-vault/redis/username",
  "redis_password": "$secret://vault/my-vault/redis/password",
  "redis_database": 1,
  "redis_timeout": 1001,
  "allow_degradation": false,
  "show_limit_quota_header": true
}
```

note

All secret references start with `$secret://`. `vault` is **Secret Manager** of the secret provider, `my-vault` is **Secret Provider ID**. When connecting to HashiCorp Vault, `$secret://vault/my-vault` will be replaced with the actual **Secret Prefix** of the secret provider. Finally, the path sent to HashiCorp Vault will be `secret/api7/redis/username` and `secret/api7/redis/password` .

The following is only the plugin configuration and not a complete configuration file to synchronize. Refer to [Apply Rate Limiting to APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/rate-limiting.md) for where and how to enable the Limit Count plugin using ADC.

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
  redis_username: $secret://vault/my-vault/redis/username
  redis_password: $secret://vault/my-vault/redis/password
  redis_database: 1
  redis_timeout: 1001
  allow_degradation: false
  show_limit_quota_header: true
```

Coming Soon.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Secrets](https://docs.api7.ai/enterprise/3.3.x/key-concepts/secrets.md)
  * [Plugins](https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md)
  * [Consumers](https://docs.api7.ai/enterprise/3.3.x/key-concepts/consumers.md)

* API Consumption
  <!-- -->
  * [Manage Consumer Credentials](https://docs.api7.ai/enterprise/3.3.x/api-consumption/manage-consumer-credentials.md)
