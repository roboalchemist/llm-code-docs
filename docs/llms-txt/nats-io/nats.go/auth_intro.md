# Source: https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro.md

# Authentication

NATS authentication is multi-level. All of the security modes have an [*accounts*](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) level with [*users*](#user-configuration-map) belonging to those accounts. The decentralized JWT Authentication also has an *operator* to which the accounts belong.

Each account has its own independent subject namespace: a message published on subject 'foo' in one account will not be seen by subscribers to 'foo' in other accounts. Accounts can however define exports and imports of subject(s) streams as well as expose request-reply services between accounts. Users within an account will share the same subject namespace but can be restricted to only be able to publish-subscribe to specific subjects.

## Authentication Methods

The NATS server provides various ways of authenticating clients:

* [Token Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens)
* [Plain Text Username/Password credentials](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/username_password#plain-text-passwords)
* [Bcrypted Username/Password credentials](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/username_password#bcrypted-passwords)
* [TLS Certificate](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth)
* [NKEY with Challenge](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth)
* [Decentralized JWT Authentication/Authorization](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt)

Authentication deals with allowing a NATS client to connect to the server. Except for JWT authentication, authentication and authorization are configured in the `authorization` section of the configuration. With JWT authentication the account and user information are stored in the [resolver](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt/resolver) rather than in the server configuration file.

## Authorization Map

The `authorization` block provides *authentication* configuration as well as [*authorization*](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization):

| Property                                                                                                            | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| [`token`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens)                | Specifies a global token that can be used to authenticate to the server (exclusive of user and password)                              |
| [`user`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/username_password#single-user)     | Specifies a single *global* user name for clients to the server (exclusive of token)                                                  |
| [`password`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password)  | Specifies a single *global* password for clients to the server (exclusive of `token`)                                                 |
| [`users`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/username_password#multiple-users) | A list of [user configuration](#user-configuration-map) maps. For multiple username and password credentials, specify a `users` list. |
| [`timeout`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/auth_timeout)        | Maximum number of seconds to wait for client authentication                                                                           |
| [`auth_callout`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_callout)              | Enables the auth callout extension                                                                                                    |

## User Configuration Map

A `user` configuration map specifies credentials and permissions options for a single user:

| Property                                                                                                           | Description                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`user`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password)     | username for client authentication. (Can also be a user for [tls authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls_mutual_auth#mapping-client-certificates-to-a-user)) |
| [`password`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password) | password for the user entry                                                                                                                                                                                      |
| [`nkey`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth)             | public nkey identifying an user                                                                                                                                                                                  |
| [`permissions`](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization)             | permissions map configuring subjects accessible to the user                                                                                                                                                      |
