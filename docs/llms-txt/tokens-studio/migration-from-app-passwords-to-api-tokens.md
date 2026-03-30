# Source: https://docs.tokens.studio/token-storage/remote/sync-git-bitbucket/migration-from-app-passwords-to-api-tokens.md

# Migration from App Passwords to API Tokens

This change is part of Atlassian’s ongoing effort to strengthen account security by phasing out weaker authentication methods and moving to **API tokens**, which offer finer-grained access controls and better security practices.\
\
**Important:** No changes are taking effect immediately, and existing integrations using app passwords will continue to function without interruption. However, this change is time-sensitive, with a 12-month transition period. Integrations with app passwords will stop working entirely on June 9, 2026.

## **Impact on Existing sync Providers**

If you already have a Bitbucket sync provider connected with an app password, it will continue to work after September 9th.\
However, users will be unable to add new Bitbucket sync providers using App passwords. We highly recommend migrating from app passwords to API tokens.\
Read more [here](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) for scopes on API tokens.

## Migration steps

* Open the sync provider settings, go to your list of configured sync providers
* Find the bitbucket sync provider using App passwords(we will highlight that in red for your view, along with the warning, *'App Password migration required'*)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F4J8TsgLzXvEWRXAmRyYG%2FScreenshot%202025-09-04%20at%202.06.21%E2%80%AFPM.png?alt=media&#x26;token=cfb81d24-4402-4eed-b77c-5fc6bbf36430" alt="" width="375"><figcaption></figcaption></figure>

* Click on Migrate to API Tokens
* Your form will open with all existing details, except app passwords

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FstNi1Bloy1N4uizp4CHp%2FScreenshot%202025-09-04%20at%202.07.02%E2%80%AFPM.png?alt=media&#x26;token=33c16409-fd31-4177-b1c7-d4fb838d1f95" alt="" width="375"><figcaption></figcaption></figure>

* Add an API Token generated from Atlassian
* Replace user name with user email
* Click on save to complete the migration of your existing sync from App passwords to API tokens
* Repeat the above steps for any other existing Bitbucket syncs with App passwords\ <br>
