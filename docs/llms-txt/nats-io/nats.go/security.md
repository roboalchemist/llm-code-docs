# Source: https://docs.nats.io/running-a-nats-service/nats_admin/security.md

# Source: https://docs.nats.io/nats-concepts/security.md

# Security

NATS has a lot of security features:

* Connections can be [*encrypted* with TLS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls)
* Client connections can be [*authenticated*](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) in many ways:
  * [Token Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens)
  * [Username/Password credentials](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password)
  * [TLS Certificate](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth)
  * [NKEY with Challenge](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth)
  * [Decentralized JWT Authentication/Authorization](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt)
  * You can also integrate NATS with your existing authentication/authorization system or create your own custom authentication using the [Auth callout](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_callout)
* Authenticated clients are identified as users and have a set of [*authorizations*](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization)

You can use [accounts](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/accounts) for multi-tenancy: each account has its own independent 'subject namespace' and you control the import/export of both streams of messages and services between accounts, and any number of users that client applications can be authenticated as. The subjects or subject wildcards that a user is allowed to publish and/or subscribe to can be controlled either through server configuration or as part of signed JWTs.

JWT authentication/authorization administration is decentralized because each account private key holder can manage their users and their authorizations on their own, without the need for any configuration change on the NATS servers by minting their own JWTs and distributing them to the users. There is no need for the NATS server to ever store any user private keys as they only need to validate the signature chain of trust contained in the user JWT presented by the client application to validate that they have the proper public key for that user.

The JetStream persistence layer of NATS also provides [encryption at rest](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/encryption_at_rest).
