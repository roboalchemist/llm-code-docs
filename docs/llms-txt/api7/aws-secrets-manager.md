# Source: https://docs.api7.ai/enterprise/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-security/aws-secrets-manager.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-security/aws-secrets-manager.md

# Reference Secrets in AWS Secrets Manager

[AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) is a fully managed service that you can integrate with API7 Enterprise to securely store, manage, and retrieve sensitive information such as API keys, passwords, and other types of credentials. It allows automatic rotation of secrets, reducing the risk of credentials being exposed over time.

This tutorial demonstrates how to integrate API7 Enterprise with AWS Secrets Manager, enabling you to securely store and reference consumer credentials and plugin configurations.

Below is an interactive demo providing a hands-on introduction to storing and retrieving key-auth secrets in AWS Secrets Manager with API7 Enterprise.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have at least one gateway instance](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md) in your gateway group.
3. Have an [AWS account](https://aws.amazon.com) to access IAM and Secrets Manager modules.

## Obtain IAM Access Key ID and Secret Access Key[â](#obtain-iam-access-key-id-and-secret-access-key "Direct link to Obtain IAM Access Key ID and Secret Access Key")

Obtain the [IAM user access key and secret access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey), which will be configured in API7 Enterprise in the next step to access AWS Secrets Manager.

note

Please ensure that the appropriate permissions are correctly assigned to users to avoid validation failures due to insufficient permissions.

## Add Secret Provider in Gateway Group[â](#add-secret-provider-in-gateway-group "Direct link to Add Secret Provider in Gateway Group")

* Dashboard
* ADC
* Ingress Controller

1. Select **Secret Providers** of your gateway group from the side navigation bar, then click **Add Secret Provider**.
2. From the dialog box, do the following:

* In the **Secret Provider ID** field, enter `my-secrets-manager`.
* In the **Secret Manager** field, choose `AWS Secrets Manager`.
* In the **Region** field, choose the region of your AWS Secrets Manager service. For example, `us-east-1`.
* Fill in the **Access Key ID** and **Secret Access Key** fields with access key and secret access key obtained in the [last step](#obtain-iam-access-key-id-and-secret-access-key).
* Click **Add**.

Not applicable.

Not applicable.

## Reference Secrets to Create Consumer Credential[â](#reference-secrets-to-create-consumer-credential "Direct link to Reference Secrets to Create Consumer Credential")

The following sensitive field in consumer credentials can be stored in an external secret manager (HashiCorp Vault, AWS Secrets Manager, etc.) and referenced in API7 Enterprise:

* `key` in Key Authentication credential
* `password` in Basic Authentication credential
* `secret`, `public key` in JWT Authentication credential
* `secret_key` in HMAC Authentication credential

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

Not supported yet.

### Create a Secret in AWS Secrets Manager[â](#create-a-secret-in-aws-secrets-manager "Direct link to Create a Secret in AWS Secrets Manager")

In this section, you will be creating a secret to store consumer credentials for user `alice`. You can also refer to [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html).

1. Navigate to AWS Secrets Manager in the console and store a new secret. Choose **Other type of secret** as the secret type and enter the key name `alice-key-auth` and the value `alice-key` in the key-value pairs.
2. In the next step, configure the secret name to be `alice-credentials` and optionally add a description.
3. Click **Next** to review the rest of the information and finish the secret creation. You should see the secret listed in AWS Secrets Manager.
4. Repeat to create more key/value pairs for other consumer credentials:

* For basic authentication credential: `password: alice-password`.
* For JWT authentication credential: `secret: alice-secret`.
* For HMAC authentication credential: `secret-key: alice-secret-key`.

### Add Key Authentication Credential[â](#add-key-authentication-credential "Direct link to Add Key Authentication Credential")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Select your target consumer, for example, `Alice`.
3. Under the **Credentials** tab, click **Add Key Authentication Credential**.
4. From the dialog box, do the following:

* In the **Name** field, enter `primary-key`.
* In the **Key** field, choose **Reference from Secret Provider**, then enter `$secret://aws/my-secrets-manager/alice-credentias/alice-key-auth`.
* Click **Add**.

note

All secret references start with `$secret://`. `aws` is **Secret Manager Name** of the secret provider, `my-secrets-manager` is **Secret Provider ID** on the API7 Enterprise dashboard. `alice-credentials` is **Secret Name** and `alice-key-auth` is **Key Name** you created on AWS Secrets Manager console.

To use ADC to create a consumer with `key-auth`, update your configuration:

consumer.yaml

```
consumers:
  - username: Alice
    credentials:
      - name: primary-key
        type: key-auth
        config:
          key: $secret://aws/my-secrets-manager/alice-credentias/alice-key-auth
```

Not supported yet.

### Add Basic Authentication Credential[â](#add-basic-authentication-credential "Direct link to Add Basic Authentication Credential")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Select your target consumer, for example, `Alice`.
3. Under the **Credentials** tab, click **Basic Authentication** tab, then click **Add Basic Authentication Credential**.
4. From the dialog box, do the following:

* In the **Name** field, enter `primary-basic`.
* In the **Username** field, enter `alice`.
* In the **Password** field, choose **Reference from Secret Provider**, then enter `$secret://aws/my-secrets-manager/alice-credentias/password`.
* Click **Add**.

note

All secret references start with `$secret://`. `aws` is **Secret Manager** and `my-secrets-manager` is the **Secret Provider ID**.

To use ADC to create a consumer with `basic-auth`, update your configuration:

consumer.yaml

```
consumers:
  - username: Alice
    credentials:
      - name: primary-basic
        type: basic-auth
        config:
          password: $secret://aws/my-secrets-manager/alice-credentials/password
          username: Alice
```

Not supported yet.

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
* In the **Secret** field, choose **Reference from Secret Provider**, then enter `$secret://aws/my-secrets-manager/alice-credentias/secret`.
* Click **Add**.

note

All secret references start with `$secret://`. `aws` is **Secret Manager** of the secret provider, `my-secrets-manager` is **Secret Provider ID**.

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
          secret: $secret://aws/my-secrets-manager/alice-credentials/secret
```

Not supported yet.

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
* In the **Secret Key** field, choose **Reference from Secret Provider**, then enter `$secret://aws/my-secrets-manager/alice-credentias/secret-key`.
* Click **Add**.

note

All secret references start with `$secret://`. `aws` is **Secret Manager** of the secret provider, `my-secrets-manager` is **Secret Provider ID**.

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
          secret_key: $secret://aws/my-secrets-manager/alice-credentials/secret-key
```

Not supported yet.

## Validate[â](#validate "Direct link to Validate")

See [Enable Key Authentication for APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#enable-key-authentication-for-apis) for instructions, and enable the [Key Auth Plugin](https://docs.api7.ai/hub/key-auth.md) on the service level.

Send a request to the route with the valid credential:

```
curl -i "http://127.0.0.1:9080/ip" -H 'apikey: alice-key'
```

You should receive an `HTTP/1.1 200 OK` response.

note

`alice-key` is the **value** of your key/value pair created on AWS Secrets Manager rather than the key name.

* For basic authentication credentials, validate with: `password: alice-password`.
* For JWT authentication credentials, validate with: `secret: alice-secret`.
* For HMAC authentication credentials, validate with: `secret-key: alice-secret-key`.

## Reference Secrets to Enable Plugin[â](#reference-secrets-to-enable-plugin "Direct link to Reference Secrets to Enable Plugin")

The following sensitive field in plugin configurations can be stored in an external secret manager (HashiCorp Vault, AWS Secrets Manager, etc.) and referenced in API7 Gateway:

| Plugin                                                                          | Field                              |
| ------------------------------------------------------------------------------- | ---------------------------------- |
| [Limit Count](https://docs.api7.ai/hub/limit-count.md)                          | `redis_username`, `redis_password` |
| [Authz-Casdoor](https://apisix.apache.org/docs/apisix/plugins/authz-casdoor/)   | `client_id`, `client_secret`       |
| [Wolf RBAC](https://apisix.apache.org/docs/apisix/plugins/wolf-rbac/)           | `appid`                            |
| [LDAP Authentication](https://apisix.apache.org/docs/apisix/plugins/ldap-auth/) | `user_dn`                          |

This section demonstrates configuring [limit-count](https://docs.api7.ai/hub/limit-count.md) plugin as an example.

### Create a Secret[â](#create-a-secret "Direct link to Create a Secret")

Create a secret using the key/value pair `username:api7` and `password:redis-api7`, under the secret name `redis` in your AWS Secrets Manager.

### Configure limit-count Plugin[â](#configure-limit-count-plugin "Direct link to Configure limit-count Plugin")

For where and how to enable the [limit-count](https://docs.api7.ai/hub/limit-count.md) plugin, refer to [Apply Rate Limiting to APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/rate-limiting.md).

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
  "redis_username": "$secret://aws/my-secrets-manager/redis/username",
  "redis_password": "$secret://aws/my-secrets-manager/redis/password",
  "redis_database": 1,
  "redis_timeout": 1001,
  "allow_degradation": false,
  "show_limit_quota_header": true
}
```

note

All secret references start with `$secret://`. `aws` is **Secret Manager** of the secret provider, `my-secrets-manager` is **Secret Provider ID**.

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
  redis_username: $secret://aws/my-secrets-manager/redis/username
  redis_password: $secret://aws/my-secrets-manager/redis/password
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
