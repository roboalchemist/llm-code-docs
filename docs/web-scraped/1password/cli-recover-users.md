# Source: https://developer.1password.com/docs/cli/recover-users

On this page

# Recover accounts using 1Password CLI

You can use 1Password CLI to begin the account recovery process for a family or team member if they can\'t sign in to or unlock 1Password. When you recover an account for someone:

- They\'ll receive a new Secret Key and create a new 1Password account password.\
  [If your team uses Unlock with SSO, they\'ll be able to [link a new app or browser to their account](https://support.1password.com/sso-linked-apps-browsers/) again.]
- They\'ll be able to access all the data they had before.
- They\'ll need to sign in again on all their devices once recovery is complete.
- Their two-factor authentication will be reset.

## Requirements[â€‹](#requirements "Direct link to Requirements") 

- [Sign up for 1Password](https://1password.com/pricing/password-manager).
- [Install 1Password CLI](/docs/cli/get-started#step-1-install-1password-cli) version `2.32.0` or later.

You can recover accounts for other people if:

- You\'re a team [administrator](https://support.1password.com/groups#administrators) or [owner](https://support.1password.com/groups#owners).
- You belong to a [custom group](https://support.1password.com/custom-groups/) that has the \"Recover Accounts\" permission.
- You\'re a [family organizer](https://support.1password.com/family-organizer/).

## Begin recovery[â€‹](#begin-recovery "Direct link to Begin recovery") 

Use the command `op user recovery begin` with a person\'s name, email address, or [unique identifier (ID)](/docs/cli/reference#unique-identifiers-ids) to begin the account recovery process. You can recover up to ten accounts with each command.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

For example, to begin recovery for multiple accounts using each person\'s ID:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

The person whose account you\'re recovering will get an email from 1Password. When they select **Recover my account** in the email, a page will open in their browser and they\'ll be asked to confirm their email address. Then they\'ll get a new Secret Key and create a new account password.

## Complete recovery[â€‹](#complete-recovery "Direct link to Complete recovery") 

After the person whose account you recovered creates a new account password, you\'ll need to complete the recovery process before they can access their account.

Learn how to [complete account recovery for one or more people](https://support.1password.com/recovery#complete-recovery).

## Learn more[â€‹](#learn-more "Direct link to Learn more") 

- [Add and remove team members](/docs/cli/provision-users)
- [Grant and revoke vault permissions](/docs/cli/grant-revoke-vault-permissions)
- [Sign back in to 1Password after your account has been recovered](https://support.1password.com/after-recovery/)