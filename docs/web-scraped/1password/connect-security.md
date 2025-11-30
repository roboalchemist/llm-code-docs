# Source: https://developer.1password.com/docs/connect/security

On this page

# About 1Password Connect Server security

You can deploy one or more 1Password Connect servers in your infrastructure to act as a bridge between your applications and the 1Password service. Connect servers allow you to securely share information from 1Password with your applications, tools, and pipelines through the [Connect REST API](/docs/connect/api-reference/). Review the sections on the page to learn more about Connect server security. For information about 1Password security practices, visit the [1Password Security homepage](https://1password.com/security).

## Access control[â€‹](#access-control "Direct link to Access control") 

When you [create a Connect server](/docs/connect/get-started/), you select the vaults it can access. Connect servers can only access the vaults you explicitly allow them to access through a [Connect server access token](#connect-server-access-tokens).

### Authorization[â€‹](#authorization "Direct link to Authorization") 

Only authorized clients can get information from a Connect server.

When a client application, service, or API requests information from a Connect server, the HTTP request must have an `Authorization` header containing an authorization token. Otherwise, the Connect server rejects the request.

Authorization tokens are only valid for the Connect server they\'re created for. They\'re signed by the key for the 1Password account the Connect server uses, using the [ES256 signing algorithm ](https://datatracker.ietf.org/doc/html/rfc7518).

### Usage reports[â€‹](#usage-reports "Direct link to Usage reports") 

[Usage reports](https://support.1password.com/reports#create-a-usage-report-for-a-team-member-service-account-or-vault) can be created for users or vaults.

Usage reports for team members include information on the number of vaults, groups, and items a team member can access, an overview of vaults where a team member has accessed items, when those items were last accessed, and the action performed. Usage reports for vaults include a list of items showing when they were last accessed, the action performed, and the team member who performed the action. These reports can be helpful when offboarding team members.

## Connect server access tokens[â€‹](#connect-server-access-tokens "Direct link to Connect server access tokens") 

A Connect server access token is an authentication string that allows the Connect server to authenticate with 1Password.

Each Connect server can have one or more Connect server access tokens, which allows for more fine tuned [access control](#access-control). Connect server tokens can only access information in the vaults you granted them access to. This allows you more granular control over the vaults a Connect server deployment can access. For example, you can grant a Connect server token access to a specific subset of the vaults the Connect server has access to.

### Token rotation[â€‹](#token-rotation "Direct link to Token rotation") 

You can\'t change or update Connect server access tokens. If a Connect server token becomes compromised, you must create a new token.

To rotate a Connect server access token:

1.  [Create a new Connect server access token.](/docs/connect/manage-connect#create-a-token)
2.  Update all references to the old Connect token.
3.  [Revoke access to the old Connect token.](/docs/connect/manage-connect#revoke-a-token)

## Security model[â€‹](#security-model "Direct link to Security model") 

The Connect server security model has the following guarantees:

- A Connect server access token can only read items from vaults you\'ve explicitly given it `READ` access to.
- A Connect server access token can only update, delete, and create items for vaults it has you\'ve given it `WRITE` access to.
- You can only give a Connect token access to vaults that you have access to.
- A Connect server access token associated with a deleted account can\'t authenticate.
- You can\'t use a Connect server access token to create another Connect server access token.

## Credentials file[â€‹](#credentials-file "Direct link to Credentials file") 

Creating a Connect server generates a credentials file named `1password-credentials.json`. This file has the following components:

  Component          Description
  ------------------ ---------------------------------------------------------------------------------------------------------------------------------------------
  `verifier`         Connect servers use the `verifier` as part of an additional authentication of the bearer token.
  `encCredentials`   The `encCredentials` contains the encrypted credentials necessary for the associated service account.
  `uniqueKey`        The `uniqueKey` identifies the Connect server between its two running processes: the client-facing service and the synchronization service.
  `version`          The `version` indicates the Connect server version number.
  `deviceUuid`       The `deviceUuid` contains the UUID of the device.

## Responsible disclosure[â€‹](#responsible-disclosure "Direct link to Responsible disclosure") 

1Password requests you practice responsible disclosure if you discover a vulnerability. If you find a vulnerability in 1Password, [submit a report on HackerOne. ](https://hackerone.com/1password)