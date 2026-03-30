# Source: https://docs.api7.ai/apisix/production/security/data-encryption-with-keyring.md

# Data Encryption with Keyring

Data encryption is a key consideration of APISIX. Sensitive information, such as user passwords and private keys, is often present in gateway configurations when implementing authentication or integrating with another system. To prevent this information from being intercepted and exploited by malicious actors, APISIX encrypts this information and transforms it into unintelligible ciphertext for storage. The ciphertexts are then transformed back to plaintexts with the correct keys, whenever needed.

In APISIX, when the data encryption is enabled, the following data will be encrypted before being saved to etcd:

* [Sensitive plugin fields](#understand-plugin-encrypt-fields)
* TLS certificate private key

This guide will help you understand why you should enable data encryption for sensitive data and how you can enable data encryption to harden security.

## Enable Data Encryption[â](#enable-data-encryption "Direct link to Enable Data Encryption")

By default, APISIX has data encryption enabled with two default keys:

apisix/cli/config.lua

```
apisix ={
  ...,
  data_encryption = {
    enable_encrypt_fields = true,
    keyring = { "qeddd145sfvddff3", "edd1c9f0985e76a2" }
  },
  ...
}
```

To see data encryption in effect, create a consumer `JohnDoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "JohnDoe"
  }'
```

Configure the `key-auth` credential for `JohnDoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/JohnDoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-key-auth",
    "plugins": {
      "key-auth": {
        "key": "john-key"
      }
    }
  }'
```

In this configuration, the user key is sensitive information that should not be stored in plaintext.

You should see a response when the consumer is created, showing an encrypted key:

```
{
  "key": "/apisix/consumers/JohnDoe/credentials",
  "value": {
    "create_time": 1726300662,
    "update_time": 1726300662,
    "plugins": {
      "key-auth": {
        "key": "a/TGSySA4i1LGn4ZXlYuew=="
      }
    },
    "id": "cred-john-key-auth"
  }
}
```

To further verify that the key is encrypted, you can also examine the item saved to etcd:

```
etcdctl get /apisix/consumers/JohnDoe/credentials
```

You should see the key has been encrypted:

```
{
  "update_time":1726300662,
  "create_time":1726300662,
  "plugins":{
    "key-auth":{
      "key":"a/TGSySA4i1LGn4ZXlYuew=="
      }
    },
  "id": "cred-john-key-auth"
}
```

Similarly, APISIX will also encrypt the TLS certificate private key before saving it to etcd. To verify, you can follow steps in [Configure HTTPS Between Client and APISIX](https://docs.api7.ai/apisix/how-to-guide/traffic-management/tls-and-mtls/configure-https-between-client-and-apisix.md#configure-https-for-apisix) and observe that `server_key` is encrypted.

## Verify Decryption[â](#verify-decryption "Direct link to Verify Decryption")

To verify the consumer `key-auth` key will be decrypted and used as intended in authentication, create a route with [`key-auth`](https://docs.api7.ai/hub/key-auth.md) enabled:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "auth-route",
    "uri": "/get",
    "plugins": {
      "key-auth": {},
    },
    "upstream" : {
      "nodes": {
        "httpbin.org":1
      }
    }
  }'
```

Send a request to the route with the consumer credential:

```
curl -i "http://127.0.0.1:9080/get" -H 'apikey: john-key'
```

You should receive an `HTTP/1.1 200 OK` response, verifying the key has been successfully decrypted and used in authentication.

## Update Keyring[â](#update-keyring "Direct link to Update Keyring")

The encrypted data can be reversed to plaintext with the correct keyring. Therefore, it is strongly recommended that you use a customized keyring in production.

The keys should be hexadecimal strings of length 16 to accompany the underlying cipher `AES-128-CBC`. To update the keyring, you can add the new keys as such:

config.yaml

```
apisix:
  data_encryption:
    enable_encrypt_fields: true
    keyring:
      - aa2b3c4d1e6f7g9h
      - xiy8z7a2b522dke
      - qeddd145sfvddff3
      - edd1c9f0985e76a2
```

â¶ Enable the encryption for [sensitive plugin fields](#understand-plugin-encrypt-fields).

â· Add the first and second new keys.

â¸ Add the first and second old keys.

caution

If your APISIX is already running and has data encrypted, do not remove the old keys. Add the new keys at the top of the array, as shown above, so that the encrypted data can be correctly decrypted. Removing the old keys directly can render the encrypted data irreversible.

If no data has been encrypted, you may directly configure the section with your custom keys.

If your APISIX is already running, [reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect.

## Disable Data Encryption[â](#disable-data-encryption "Direct link to Disable Data Encryption")

To disable data encryption, simply update the `enable_encrypt_fields` to `false`:

config.yaml

```
apisix:
  data_encryption:
    enable_encrypt_fields: false
```

If your APISIX is already running, [reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect.

Now if you configure the consumer credential with [`key-auth`](https://docs.api7.ai/hub/key-auth.md) again:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/JohnDoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-key-auth",
    "plugins": {
      "key-auth": {
        "key": "john-key"
      }
    }
  }'
```

You should see a response where the key is saved in plaintext:

```
{
  "key": "/apisix/consumers/JohnDoe/credentials",
  "value": {
    "create_time": 1726300662,
    "update_time": 1726300668,
    "plugins": {
      "key-auth": {
        "key": "john-key"
      }
    },
    "id": "cred-john-key-auth"
  }
}
```

## Understand Plugin Encrypt Fields[â](#understand-plugin-encrypt-fields "Direct link to Understand Plugin Encrypt Fields")

Encrypt plugin fields are defined in the `encrypt_fields` attribute of each plugin schema. For example:

apisix/plugins/basic-auth.lua

```
local consumer_schema = {
  type = "object",
  title = "work with consumer object",
  properties = {
      username = { type = "string" },
      password = { type = "string" },
  },
  # highlight-next-line
  encrypt_fields = {"password"},
  required = {"username", "password"},
}
```

Once defined, these fields will be encrypted when data encryption is enabled.

The table below summarizes encrypt plugin fields of all plugins:

| **Plugin**             | **Field(s)**                              |
| ---------------------- | ----------------------------------------- |
| `authz-casdoor`        | `client_secret`                           |
| `authz-keycloak`       | `client_secret`                           |
| `basic-auth`           | `password`                                |
| `clickhouse-logger`    | `password`                                |
| `elasticsearch-logger` | `auth.password`                           |
| `rocketmq-logger`      | `secret_key`                              |
| `sls-logger`           | `access_key_secret`                       |
| `error-log-logger`     | `clickhouse.password`                     |
| `google-cloud-logging` | `auth_config.private_key`                 |
| `csrf`                 | `key`                                     |
| `hmac-auth`            | `secret_key`                              |
| `jwt-auth`             | `secret`, `private_key`                   |
| `key-auth`             | `key`                                     |
| `openwhisk`            | `service_token`                           |
| `tencent-cloud-cls`    | `secret_key`                              |
| `openid-connect`       | `client_secret`, `client_rsa_private_key` |
| `kafka-proxy`          | `sasl.password`                           |
| `jwt-decrypt`          | `key`, `secret`                           |
