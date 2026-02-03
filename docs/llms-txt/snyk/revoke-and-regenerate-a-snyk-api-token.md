# Source: https://docs.snyk.io/snyk-api/authentication-for-api/revoke-and-regenerate-a-snyk-api-token.md

# Revoke and regenerate a Snyk API token

{% hint style="warning" %}
When an API token is revoked, all integrations using that key immediately stop working. Proceed with caution!
{% endhint %}

If you suspect an API token has been leaked, it is good practice to revoke that token and generate a new one to use in its place.

To revoke your Snyk user API token, navigate to your personal General Account Settings in the Snyk Web UI at [app.snyk.io/account](https://app.snyk.io/account).

![API token screen, Revoke & Regenerate button](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e99a1d116aa121b1c43c60dfc20e6e585ce5e069%2Faccount-settings-general-auth-token.png?alt=media)

Click the **Revoke & Regenerate** button to revoke your API token. A new one will be generated in its place. You can now copy the newly generated API token and update integrations that used the old token.
