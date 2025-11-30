# Source: https://developer.1password.com/docs/service-accounts/security

On this page

# 1Password Service Account security

You can automate managing secrets in your apps and systems with [1Password Service Accounts](/docs/service-accounts/). No need for extra services. Explore the sections on this page to learn more about service account security. For information about 1Password security practices, visit the [1Password Security homepage](https://1password.com/security).

## Access control[â€‹](#access-control "Direct link to Access control") 

When creating a service account, you choose the vaults it can access and its level of access. The service account only returns information from vaults it can access. You can also give service accounts permission to create and manage vaults.

## Service accounts and token generation[â€‹](#service-accounts-and-token-generation "Direct link to Service accounts and token generation") 

A service account is a type of user account that\'s meant for programmatic access. Service accounts differ from regular 1Password accounts in that you don\'t need to provide an email or an [account password](https://support.1password.com/1password-glossary#1password-account-password).

When a regular user account creates a master key, the user must provide an email, a [Secret Key](https://support.1password.com/1password-glossary#secret-key), and an account password. When a service account user creates a master key, 1Password generates all the input.

  Element      Regular user    Service account
  ------------ --------------- -----------------
  Secret Key   Generated       Generated
  Password     User provided   Generated

1Password uses the Secret Key and the password as part of the [two-secret key derivation (2SKD)](#2skd) process to create the following:

- [Account Unlock Key (AUK)](#auk)
- [Secure Remote Password (SRP)](#srp)

After deriving these two items, 1Password discards the password used to create them.

Each user, whether a regular user or a service account user, has a [personal keyset](#personal-keyset) that 1Password generates when you create the user account. The AUK encrypts the personal keyset, and 1Password uses the personal keyset to encrypt and decrypt vaults.

A service account token is an authentication string that represents an SRPx object that\'s serialized and Base64 URL encoded. The service account token allows a service account to authenticate with 1Password CLI.

1Password creates the service account token by serializing the Account Unlock Key (AUK), Secure Remote Password (SRP), and the personal keyset into a [JSON Web Token (JWT) ](https://jwt.io/), then Base64 encoding it.

See the following examples of a service account token encoded and decoded.

- Encoded
- Decoded

Encoded service account token:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Decoded service account token:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

1Password uses a unique string format to help code analyzers find accidental credential exposure. The format uses \"`ops_`\" as the token prefix.

The steps to create the token happen on your device (client-side); nothing sensitive goes to 1Password\'s servers. It\'s up to you to save and protect the service account token.

### Token rotation and revocation[â€‹](#token-rotation "Direct link to Token rotation and revocation") 

You can rotate or revoke service account tokens. You might want to revoke or rotate a service account token if a service account token became compromised or you need to comply with a security policy that requires regular token rotation.

- [Learn how to revoke a service account token.](/docs/service-accounts/manage-service-accounts#revoke-token)
- [Learn how to rotate a service account token.](/docs/service-accounts/manage-service-accounts#rotate-token)

## Security model[â€‹](#security-model "Direct link to Security model") 

The 1Password Service Account security model has the following guarantees:

- A service account can only read items from vaults it has READ access to.
- A service account can only update, delete, and create items for vaults it has WRITE access to.
- The creator of a service account can only grant the service account access to vaults that the creator has access to.
- You can\'t grant a service account access to vaults that have service accounts turned off, even if the creator of the service account has permissions to manage the vault.
- Disabling service accounts for a vault removes access to that vault from all pre-existing service accounts.
- By default, account [owners](https://support.1password.com/1password-glossary#owner) and [administrators](https://support.1password.com/1password-glossary#administrator) can create service accounts.
  - All owners and administrators can view service account details and delete service accounts, but they can\'t view the generated service account token.
  - Owners and administrators can [give other team members access](/docs/service-accounts/manage-service-accounts#manage-who-can-create-service-accounts) to create and manage their own service accounts.
  - Team members can only grant service accounts access to a vault if they have the `Manage Vault` permission for that vault.
- A service account token associated with a deleted service account can\'t authenticate.
- You can\'t add vault access to a generated service account after creation.
- A service account can\'t create another service account.
- A service account can\'t manage users.

## Terminology[â€‹](#terminology "Direct link to Terminology") 

##### Account Unlock Key[â€‹](#auk "Direct link to Account Unlock Key") 

The Account Unlock Key (AUK) is a key derived from the [2SKD process](#2skd). It\'s used to decrypt a user\'s [personal keyset](#personal-keyset). It\'s derived from the user\'s account password and Secret Key. Previously known as the â€œMaster Unlock Keyâ€?.

##### Personal keyset[â€‹](#personal-keyset "Direct link to Personal keyset") 

Each user account (whether a regular user or a service account) has a personal keyset that consists of a public and private key pair that\'s used to encrypt and decrypt vaults.

##### Secure Remote Password[â€‹](#srp "Direct link to Secure Remote Password") 

The Secure Remote Password (SRP) is a key derived from the [2SKD process](#2skd). It\'s used for the Secure Remote Password protocol, which is a method for both a client and a server to authenticate each other without either revealing any secrets.

##### Service account token[â€‹](#service-account-token "Direct link to Service account token") 

A service account token is an authentication string that grants a service account access to one or more 1Password vaults. You can use service account tokens to authenticate services and tools, such as the 1Password CLI.

##### Two-secret key derivation[â€‹](#2skd "Direct link to Two-secret key derivation") 

Two-secret key derivation (2SKD) is a type of key derivation function that uses two user secrets (the Account password and Secret Key) to derive two independent keys (the [Account Unlock Key](#auk) and the [Secure Remote Password](#srp)).

## Responsible disclosure[â€‹](#responsible-disclosure "Direct link to Responsible disclosure") 

1Password requests you practice responsible disclosure if you discover a vulnerability. If you find a vulnerability in 1Password, [submit a report on HackerOne. ](https://hackerone.com/1password)