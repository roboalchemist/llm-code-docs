# Source: https://docs.api7.ai/enterprise/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-consumption/manage-consumer-credentials.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-consumption/manage-consumer-credentials.md

# Manage Consumer Credentials

A [consumer](https://docs.api7.ai/enterprise/3.3.x/key-concepts/consumers.md) is an application that consumes your API. Enabling authentication on a [service](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md) allows you to control access, requiring consumers to obtain the credentials before accessing the APIs.

Authentication plugins enabled on services act as locks on your APIs, while consumer credentials serve as the keys to unlock them. In API7 Enterprise, you need a unique username and at least one credential to set up a consumer.

Consumers can utilize multiple credentials of different types, all are treated equally for authentication purposes.

note

Consider if the [Developers](https://docs.api7.ai/enterprise/3.3.x/key-concepts/developers.md) is a better solution before implementing consumer-based credential management.

This tutorial guides you in creating a consumer and configuring authentication credentials.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have a running API on the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

## Configure Key Authentication Credentials[â](#configure-key-authentication-credentials "Direct link to Configure Key Authentication Credentials")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Click **+ Add Consumer**.
3. In the dialog box, do the following:

* In the **Name** field, enter `Alice`.
* Click **Add**.

4. Under the **Credentials** tab, click **+ Add Key Authentication Credential**.
5. In the dialog box, do the following:

* In the **Name** field, enter `primary-key`.
* In the **Key** field, choose **Manually Input**, then enter `alice-primary-key`.
  <!-- -->
  * If you want to choose **Reference from Secret Provider**, see [Reference Secrets in HashiCorp Vault](https://docs.api7.ai/enterprise/3.3.x/api-security/hashicorp-vault.md) or [Reference Secrets in AWS Secrets Manager](https://docs.api7.ai/enterprise/3.3.x/api-security/aws-secrets-manager.md).
* Click **Add**.

6. Try again to add another Key Authentication Credential named `backup-key` with key `alice-backup-key`. All credentials are valid and can be used interchangeably for API authentication.

Below is an interactive demo that provides a hands-on introduction to configuring key authentication credential using API7 Enterprise.

adc-consumer.yaml

```
consumers:
  - username: Alice
    credentials:
      - name: primary-key
        type: key-auth
        config:
          key: alice-primary-key
      - name: backup-key
        type: key-auth
        config:
          key: alice-backup-key
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc-consumer.yaml
```

Ingress Controller currently does not support credentials and anonymous consumer.

### Validate[â](#validate "Direct link to Validate")

See [Enable Key Authentication for APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#enable-key-authentication-for-apis) for instructions, and enable the [Key Auth Plugin](https://docs.api7.ai/hub/key-auth.md) on the service level.

Then follow [Validate Key Authentication](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#validate-key-authentication) instructions.

## Configure Basic Authentication Credentials[â](#configure-basic-authentication-credentials "Direct link to Configure Basic Authentication Credentials")

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Click **Add Consumer**.
3. From the dialog box, do the following:

* In the **Name** field, enter `Alice`.
* Click **Add**.

4. Under the **Credentials** tab, click **Basic Authentication** tab, then click **Add Basic Authentication Credential**.
5. From the dialog box, do the following:

* In the **Name** field, enter `primary-basic`.
* In the **Username** field, enter `alice`.
* In the **Password** field, choose **Manually Input**, then enter `alice-password`.
  <!-- -->
  * If you want to choose **Reference from Secret Provider**, see [Reference Secrets in HashiCorp Vault](https://docs.api7.ai/enterprise/3.3.x/api-security/hashicorp-vault.md) or [Reference Secrets in AWS Secrets Manager](https://docs.api7.ai/enterprise/3.3.x/api-security/aws-secrets-manager.md).
* Click **Add**.

6. Try again to add another Basic Authentication Credential named `backup-basic` with username `alice-backup` and password `alice-backup-password`. All credentials are valid and can be used interchangeably for API authentication.

Coming Soon.

Ingress Controller currently does not support credentials and anonymous consumer.

### Validate[â](#validate-1 "Direct link to Validate")

See [Enable Basic Authentication for APIs](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#enable-basic-authentication-for-apis) for instructions, and enable the [Basic Auth Plugin](https://docs.api7.ai/hub/basic-auth.md) on the service level.

Then follow [Validate Basic Authentication](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md#validate-basic-authentication) instructions.

## Configure Varied Authentication Credentials[â](#configure-varied-authentication-credentials "Direct link to Configure Varied Authentication Credentials")

While consumers can have multiple credentials of different types, each route in a published service should be configured with only one authentication plugin. This allows consumers to access multiple routes using their preferred authentication methods.

Below is an interactive demo that provides a hands-on introduction to configuring various authentication credentials using API7 Enterprise.

* Dashboard
* ADC
* Ingress Controller

1. Select **Consumers** of your gateway group from the side navigation bar.
2. Click **+ Add Consumer**.
3. In the dialog box, do the following:

* In the **Name** field, enter `John`.
* Click **Add**.

4. Under the **Credentials** tab, click **Add Key Authentication Credential**.
5. In the dialog box, do the following:

* In the **Name** field, enter `key-auth`.
* In the **Key** field, choose **Manually Input**, then enter `john-key-auth`.
* Click **Add**.

6. Under the **Credentials** tab, select **Basic Authentication** and click **Add Basic Authentication Credential**.
7. In the dialog box, do the following:

* In the **Name** field, enter `basic-auth`.
* In the **Username** field, enter `john`.
* In the **Password** field, choose **Manually Input**, then enter `john-password`.
* Click **Add**.

8. Under the **Credentials** tab, select **JWT** and click **Add JWT Credential**.
9. In the dialog box, do the following:

* In the **Name** field, enter `jwt-auth`.
* In the **Key** field, enter `john-jwt-key`.
* In the **Algorithm** field, select `RS256`.
* In the **Public Key** field, choose **Manually Input**, then enter your public key.
* Click **Add**.

10. Under the **Credentials** tab, select **HMAC Authentication** and click **Add HMAC Authentication Credential**.
11. In the dialog box, do the following:

* In the **Name** field, enter `hmac-auth`.
* In the **Key ID** field, enter `john-key`.
* In the **Secret Key** field, choose **Manually Input**, then enter `john-hmac-key`.
* Click **Add**.

Coming Soon.

Ingress Controller currently does not support credentials and anonymous consumer.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Routes](https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md)
  * [Plugins](https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md)
  * [Consumers](https://docs.api7.ai/enterprise/3.3.x/key-concepts/consumers.md)

* API Security
  <!-- -->
  * [Set up API authentication](https://docs.api7.ai/enterprise/3.3.x/api-security/api-authentication.md)

* API Consumption
  <!-- -->
  * [Apply list-based access control](https://docs.api7.ai/enterprise/3.3.x/api-consumption/consumer-restriction.md)

* Plugin Hub

  <!-- -->

  * [Key Authentication](https://docs.api7.ai/hub/key-auth.md)
  * [Basic Authentication](https://docs.api7.ai/hub/basic-auth.md)
  * [JWT Auth Plugin](https://docs.api7.ai/hub/jwt-auth.md)
  * [HMAC Auth Plugin](https://docs.api7.ai/hub/hmac-auth.md)
